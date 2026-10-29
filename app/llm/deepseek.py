"""Direct DeepSeek silver validation using the shared rubric and strict local schema."""
from __future__ import annotations

from dataclasses import dataclass, field
import hashlib
import json
import os
from pathlib import Path
import time
from urllib.parse import urlparse

from dotenv import dotenv_values
import httpx
from pydantic import ValidationError

from .config import PROJECT_ROOT, _as_bool
from .contracts import TokenUsage
from .silver import (SilverAdjudicationResult, SilverLabelOutput, SilverRunResult,
                     build_silver_prompt, silver_provider_schema)


@dataclass(frozen=True)
class DeepSeekSettings:
    api_key: str = field(default="", repr=False)
    model: str = "deepseek-flash"
    provider: str = "deepseek"
    api_base_url: str = "https://api.deepseek.com"
    live_enabled: bool = False
    timeout_seconds: int = 120
    max_output_tokens: int = 4096
    reasoning_effort: str = "low"

    def __post_init__(self):
        address = urlparse(self.api_base_url)
        if (address.scheme != "https" or address.hostname != "api.deepseek.com"
                or address.username or address.password or address.query or address.fragment
                or address.port not in (None, 443) or address.path not in ("", "/", "/v1", "/v1/")):
            raise ValueError("DEEPSEEK_API_BASE_URL must use the official DeepSeek HTTPS endpoint")
        if self.provider != "deepseek" or not self.model.strip():
            raise ValueError("invalid DeepSeek provider/model")
        if not 5 <= self.timeout_seconds <= 600 or not 128 <= self.max_output_tokens <= 32768:
            raise ValueError("DeepSeek timeout must be 5..600 seconds and output tokens 128..32768")
        if self.reasoning_effort not in ("low", "high", "max"):
            raise ValueError("DEEPSEEK_REASONING_EFFORT must be low, high or max")

    @classmethod
    def from_environment(cls):
        values = dotenv_values(PROJECT_ROOT / ".env")
        def value(name, default):
            return str(os.environ.get(name, values.get(name) or default))
        return cls(api_key=value("DEEPSEEK_API_KEY", ""), model=value("DEEPSEEK_MODEL", "deepseek-flash"),
                   api_base_url=value("DEEPSEEK_API_BASE_URL", "https://api.deepseek.com").rstrip("/"),
                   live_enabled=_as_bool(value("DEEPSEEK_LIVE_ENABLED", "false"), default=False),
                   timeout_seconds=int(value("DEEPSEEK_TIMEOUT_SECONDS", "120")),
                   max_output_tokens=int(value("DEEPSEEK_MAX_OUTPUT_TOKENS", "4096")),
                   reasoning_effort=value("DEEPSEEK_REASONING_EFFORT", "low"))


class DeepSeekSilverAdapter:
    def __init__(self, settings: DeepSeekSettings, *, client=None, stop_on_503=False):
        label = settings.provider.capitalize() if settings.provider != "groq" else "Groq"
        prefix = settings.provider.upper()
        if not settings.api_key.strip():
            raise ValueError(f"{prefix}_API_KEY is required; use the provider's own API key")
        if not settings.live_enabled:
            raise ValueError(f"{prefix}_LIVE_ENABLED must be true for live {label} requests")
        self.settings = settings
        self.client = client or httpx.Client(timeout=settings.timeout_seconds, follow_redirects=False)

    def _request_payload(self, prompt):
        return {"model": self.settings.model, "stream": False,
                "messages": [{"role": "system", "content":
                    "Kamu reviewer asesmen matematika Indonesia. Keluarkan hanya JSON, tanpa markdown, "
                    "sesuai schema berikut. Gunakan bukti singkat; jangan keluarkan penalaran internal.\n"
                    + json.dumps(silver_provider_schema(), ensure_ascii=False)},
                    {"role": "user", "content": prompt}],
                "response_format": {"type": "json_object"},
                "thinking": {"type": "enabled"}, "reasoning_effort": self.settings.reasoning_effort,
                "max_tokens": self.settings.max_output_tokens}

    def _error_metadata(self, error, status):
        return {"providerFailureReason": {
            400: "provider_configuration_error", 401: "api_key_invalid", 402: "insufficient_balance",
            403: "permission_denied", 404: "model_not_found"}.get(status)}

    def _generate(self, prompt, *, result_type, run_index=None):
        started, data, content = time.perf_counter(), {}, ""
        common = {"promptHash": hashlib.sha256(prompt.encode("utf-8")).hexdigest()}
        if run_index is not None:
            common["runIndex"] = run_index
        usage = TokenUsage()
        try:
            response = self.client.post(self.settings.api_base_url.rstrip("/") + "/chat/completions",
                headers={"Authorization": "Bearer " + self.settings.api_key},
                json=self._request_payload(prompt))
            response.raise_for_status()
            data = response.json()
            raw_usage = data.get("usage") or {}
            completion = int(raw_usage.get("completion_tokens") or 0)
            thinking = int((raw_usage.get("completion_tokens_details") or {}).get("reasoning_tokens") or 0)
            usage = TokenUsage(promptTokens=int(raw_usage.get("prompt_tokens") or 0),
                               outputTokens=max(0, completion - thinking), thinkingTokens=thinking,
                               totalTokens=int(raw_usage.get("total_tokens") or 0))
            choice = data["choices"][0]
            content = choice["message"].get("content") or ""
            # reasoning_content is deliberately never persisted or passed to the rubric.
            if choice.get("finish_reason") != "stop":
                raise ValueError("incomplete provider response")
            output = SilverLabelOutput.model_validate_json(content)
            return result_type(status="success", output=output, usage=usage,
                               responseId=data.get("id"), responseHash=hashlib.sha256(
                                   output.model_dump_json().encode("utf-8")).hexdigest(),
                               latencyMs=int((time.perf_counter() - started) * 1000), **common)
        except Exception as error:
            status = error.response.status_code if isinstance(error, httpx.HTTPStatusError) else None
            code = ("ServerError" if status and status >= 500 else "ClientError") + ":" + str(status) if status else type(error).__name__ + ":unknown"
            metadata = self._error_metadata(error, status)
            details = ([{"location": ".".join(str(part) for part in entry["loc"]), "type": entry["type"]}
                        for entry in error.errors(include_input=False, include_url=False)]
                       if isinstance(error, ValidationError) else [])
            return result_type(status="failed", errorCode=code, errorDetails=details,
                               **metadata, usage=usage, responseId=data.get("id"),
                               responseHash=hashlib.sha256(content.encode("utf-8")).hexdigest() if content else None,
                               latencyMs=int((time.perf_counter() - started) * 1000), **common)

    def label_once(self, item, image_paths, *, run_index, grade=1, track="regular"):
        if image_paths:
            raise ValueError("this exercise adapter accepts text-only items")
        return self._generate(build_silver_prompt(item, grade=grade, track=track),
                              result_type=SilverRunResult, run_index=run_index)

    def adjudicate_once(self, item, image_paths, runs, *, grade, track="regular"):
        if image_paths:
            raise ValueError("this exercise adapter accepts text-only items")
        evidence = [{"runIndex": run.runIndex, "contentStatus": run.output.contentStatus,
                     "answerKeyStatus": run.output.answerKeyStatus, "verifiedAnswerKey": run.output.verifiedAnswerKey,
                     "verifiedMinimalSolution": run.output.verifiedMinimalSolution,
                     **{head: getattr(run.output, head).model_dump(mode="json") for head in
                        ("mathCognitiveDomain", "knowledgeDimension", "intendedDifficulty")}}
                    for run in runs if run.status == "success" and run.output]
        prompt = (build_silver_prompt(item, grade=grade, track=track)
                  + "\n\nADJUDIKASI SILVER: nilai ulang soal secara independen, lalu gunakan bukti run blind "
                  "berikut hanya untuk menemukan sumber perbedaan. Jangan melakukan voting mekanis. "
                  "Tidak ada prediksi IndoBERT atau estimasi kesulitan agen di dalam data ini.\n"
                  + json.dumps(evidence, ensure_ascii=False, sort_keys=True))
        return self._generate(prompt, result_type=SilverAdjudicationResult)
