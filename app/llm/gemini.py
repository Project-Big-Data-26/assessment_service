"""Gemini provider adapter with schema validation and bounded usage."""

from __future__ import annotations

import hashlib
import json
import time
from copy import deepcopy
from typing import Any

from google import genai
from google.genai import types
from pydantic import ValidationError

from app.classification.v2.contracts import V2ClassificationRequest, V2ClassificationResponse
from app.classification.v2.serializer import serialize_question

from .config import GeminiSettings
from .contracts import GeminiReviewOutput, GeminiRunResult, TokenUsage

PROMPT_VERSION = "gemini-indobert-review-v1"


class GeminiProviderError(RuntimeError):
    """Sanitized provider failure that never includes credentials or prompts."""

    def __init__(self, code: str):
        super().__init__(code)
        self.code = code


def _prediction_summary(prediction: V2ClassificationResponse) -> dict[str, Any]:
    def head(value: Any) -> dict[str, Any]:
        return {
            "label": value.label,
            "probabilities": value.probabilities,
            "confidence": value.calibratedConfidence,
            "entropy": value.normalizedEntropy,
            "action": value.action,
            "reasons": value.reasons,
        }

    return {
        "mathCognitiveDomain": head(prediction.mathCognitiveDomain),
        "knowledgeDimension": head(prediction.knowledgeDimension),
        "intendedDifficulty": head(prediction.intendedDifficulty),
    }


def build_review_prompt(
    question: V2ClassificationRequest,
    prediction: V2ClassificationResponse,
    *,
    rubric_version: str,
) -> str:
    """Build a concise prompt; the JSON schema is supplied separately."""
    if (
        question.questionId != prediction.questionId
        or question.contentVersion != prediction.contentVersion
        or question.contentHash != prediction.contentHash
    ):
        raise ValueError("question and prediction identity do not match")
    prediction_json = json.dumps(
        _prediction_summary(prediction), ensure_ascii=False, sort_keys=True, separators=(",", ":")
    )
    return (
        "Tinjau prediksi IndoBERT untuk soal matematika SD menggunakan rubrik "
        f"{rubric_version}. Nilai tuntutan proses matematis sebenarnya, bukan KKO saja. "
        "Untuk setiap head: confirm jika label IndoBERT didukung bukti soal; revise jika "
        "label lain lebih tepat; abstain jika bukti tidak cukup. Kutip maksimal empat "
        "potongan bukti singkat dari soal. Berikan alasan ringkas, bukan chain-of-thought. "
        "Aturan schema wajib: proposedLabel harus null untuk confirm/abstain dan wajib "
        "berisi label yang BERBEDA dari prediksi untuk revise; evidenceSpans berisi 1-4 "
        "kutipan pendek untuk confirm/revise; rationale maksimal 600 karakter. "
        "Berikan keputusan advisory AI dan jangan mengarang informasi yang tidak tersedia.\n\n"
        f"ITEM KANONIS:\n{serialize_question(question)}\n\n"
        f"PREDIKSI INDOBERT:\n{prediction_json}"
    )


def _normalize_provider_payload(value: Any) -> Any:
    """Normalize harmless provider deviations before strict validation.

    Gemini's JSON schema mode can still return an irrelevant proposedLabel for
    confirm/abstain or text just over our storage limits. Removing that ignored
    label and truncating bounded audit text does not alter the decision.
    Missing evidence or a missing revise label remains invalid.
    """
    if not isinstance(value, dict):
        return value
    payload = deepcopy(value)
    concerns = payload.get("contentConcerns")
    if isinstance(concerns, list):
        payload["contentConcerns"] = [str(item)[:600] for item in concerns[:6]]
    for head in (
        "mathCognitiveDomain",
        "knowledgeDimension",
        "intendedDifficulty",
    ):
        decision = payload.get(head)
        if not isinstance(decision, dict):
            continue
        if decision.get("action") != "revise":
            decision["proposedLabel"] = None
        evidence = decision.get("evidenceSpans")
        if isinstance(evidence, list):
            decision["evidenceSpans"] = [str(item)[:240] for item in evidence[:4]]
        rationale = decision.get("rationale")
        if isinstance(rationale, str):
            decision["rationale"] = rationale[:600]
    return payload


class GeminiReviewAdapter:
    def __init__(self, settings: GeminiSettings, *, client: Any | None = None):
        self.settings = settings
        self._client = client or genai.Client(
            api_key=settings.api_key,
            http_options=types.HttpOptions(
                api_version="v1beta",
                timeout=settings.timeout_seconds * 1000,
                retry_options=types.HttpRetryOptions(
                    attempts=2,
                    initial_delay=0.5,
                    max_delay=2.0,
                    http_status_codes=[408, 429, 500, 502, 503, 504],
                ),
            ),
        )

    def review_once(
        self,
        question: V2ClassificationRequest,
        prediction: V2ClassificationResponse,
        *,
        rubric_version: str,
        run_index: int,
    ) -> GeminiRunResult:
        prompt = build_review_prompt(question, prediction, rubric_version=rubric_version)
        started = time.perf_counter()
        try:
            response = self._client.models.generate_content(
                model=self.settings.model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=(
                        "Kamu adalah reviewer asesmen matematika berbahasa Indonesia. "
                        "Keluaran harus mematuhi schema dan berisi alasan singkat yang dapat diaudit."
                    ),
                    temperature=self.settings.temperature,
                    max_output_tokens=self.settings.max_output_tokens,
                    response_mime_type="application/json",
                    response_json_schema=GeminiReviewOutput.model_json_schema(),
                    thinking_config=types.ThinkingConfig(
                        include_thoughts=False,
                        thinking_level=types.ThinkingLevel.LOW,
                    ),
                ),
            )
            parsed = response.parsed
            if isinstance(parsed, GeminiReviewOutput):
                review = parsed
            elif parsed is not None:
                review = GeminiReviewOutput.model_validate(
                    _normalize_provider_payload(parsed)
                )
            elif getattr(response, "text", None):
                raw = json.loads(response.text)
                review = GeminiReviewOutput.model_validate(
                    _normalize_provider_payload(raw)
                )
            else:
                raise GeminiProviderError("empty_response")
            self._validate_against_prediction(review, prediction)
        except GeminiProviderError:
            raise
        except ValidationError as exc:
            raise GeminiProviderError("invalid_structured_output") from exc
        except Exception as exc:
            raise GeminiProviderError("provider_request_failed") from exc

        elapsed_ms = int((time.perf_counter() - started) * 1000)
        usage = getattr(response, "usage_metadata", None)
        token_usage = TokenUsage(
            promptTokens=int(getattr(usage, "prompt_token_count", 0) or 0),
            outputTokens=int(getattr(usage, "candidates_token_count", 0) or 0),
            thinkingTokens=int(getattr(usage, "thoughts_token_count", 0) or 0),
            totalTokens=int(getattr(usage, "total_token_count", 0) or 0),
        )
        canonical = review.model_dump_json(by_alias=True)
        return GeminiRunResult(
            runIndex=run_index,
            status="success",
            review=review,
            responseId=getattr(response, "response_id", None),
            responseHash=hashlib.sha256(canonical.encode("utf-8")).hexdigest(),
            latencyMs=elapsed_ms,
            usage=token_usage,
        )

    @staticmethod
    def _validate_against_prediction(
        review: GeminiReviewOutput, prediction: V2ClassificationResponse
    ) -> None:
        pairs = (
            (review.mathCognitiveDomain, prediction.mathCognitiveDomain),
            (review.knowledgeDimension, prediction.knowledgeDimension),
            (review.intendedDifficulty, prediction.intendedDifficulty),
        )
        for reviewed, predicted in pairs:
            if reviewed.action == "confirm" and predicted.label is None:
                raise GeminiProviderError("cannot_confirm_abstained_prediction")
            if reviewed.action == "revise" and reviewed.proposedLabel == predicted.label:
                raise GeminiProviderError("revision_must_change_label")
