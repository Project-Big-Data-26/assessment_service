"""Gemini silver-label generation for the 3x4x3 bootstrap dataset."""

from __future__ import annotations

import hashlib
import json
import time
from collections import Counter
from pathlib import Path
from typing import Annotated, Any, Literal

from google import genai
from google.genai import types
from pydantic import BaseModel, ConfigDict, Field, StringConstraints, model_validator

from app.classification.v2.contracts import (
    CognitiveDomain,
    IntendedDifficulty,
    KnowledgeDimension,
)

from .config import GeminiSettings
from .contracts import TokenUsage

SILVER_PROMPT_VERSION = "gemini-silver-math-3x4x3-v1"
RUBRIC_VERSION = "math-rubric-3x4x3-v1"

ShortText = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=700)]
EvidenceText = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=260)]


class _SilverHead(BaseModel):
    model_config = ConfigDict(extra="forbid")

    action: Literal["classify", "abstain"]
    evidenceSpans: list[EvidenceText] = Field(default_factory=list, max_length=4)
    rationale: ShortText

    def validate_common(self, label: object | None) -> None:
        if self.action == "classify" and label is None:
            raise ValueError("classify requires label")
        if self.action == "abstain" and label is not None:
            raise ValueError("abstain requires a null label")
        if self.action == "classify" and not self.evidenceSpans:
            raise ValueError("classification requires evidence")


class SilverCognitiveHead(_SilverHead):
    label: CognitiveDomain | None = None

    @model_validator(mode="after")
    def validate_action(self) -> "SilverCognitiveHead":
        self.validate_common(self.label)
        return self


class SilverKnowledgeHead(_SilverHead):
    label: KnowledgeDimension | None = None

    @model_validator(mode="after")
    def validate_action(self) -> "SilverKnowledgeHead":
        self.validate_common(self.label)
        return self


class SilverDifficultyHead(_SilverHead):
    label: IntendedDifficulty | None = None

    @model_validator(mode="after")
    def validate_action(self) -> "SilverDifficultyHead":
        self.validate_common(self.label)
        return self


class SilverLabelOutput(BaseModel):
    model_config = ConfigDict(extra="forbid")

    contentStatus: Literal["valid", "concern", "insufficient_evidence"]
    contentConcerns: list[ShortText] = Field(default_factory=list, max_length=6)
    visualTranscript: str | None = Field(default=None, max_length=1800)
    mathCognitiveDomain: SilverCognitiveHead
    knowledgeDimension: SilverKnowledgeHead
    intendedDifficulty: SilverDifficultyHead


class SilverRunResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    runIndex: int = Field(ge=1)
    status: Literal["success", "failed"]
    output: SilverLabelOutput | None = None
    errorCode: str | None = None
    responseId: str | None = None
    responseHash: str | None = None
    latencyMs: int = Field(ge=0)
    usage: TokenUsage = Field(default_factory=TokenUsage)


def build_silver_prompt(item: dict[str, Any]) -> str:
    options = "\n".join(
        f"{option['option_id']}. {option['text']} | catatan sumber: {option.get('alasan') or '-'}"
        for option in item["options"]
    )
    image_note = (
        f"Ada {len(item.get('image_url') or [])} gambar terlampir. Tulis visualTranscript yang "
        "hanya memuat fakta visual relevan untuk menjawab dan mengklasifikasikan soal."
        if item.get("image_url") else
        "Tidak ada gambar terlampir; visualTranscript harus null."
    )
    return f"""Klasifikasikan satu soal matematika kelas 1 sebagai SILVER LABEL penelitian awal.

Gunakan rubrik berikut.
- Domain kognitif matematika:
  knowing = mengingat/mengenali/membaca fakta atau melakukan proses sangat langsung;
  applying = memilih dan memakai konsep/prosedur pada situasi rutin;
  reasoning = menyusun strategi nonrutin, mengintegrasikan informasi, menyimpulkan,
  menggeneralisasi, atau memberi pembenaran.
- Dimensi pengetahuan:
  factual = istilah, simbol, fakta dasar;
  conceptual = hubungan, kategori, prinsip, atau struktur konsep;
  procedural = algoritma, teknik, atau urutan langkah;
  metacognitive = memilih/memantau strategi berpikir secara eksplisit.
- Intended difficulty adalah tuntutan isi bagi siswa kelas 1 sebelum data respons:
  Easy = langsung/satu keputusan; Medium = beberapa langkah/representasi rutin;
  Hard = strategi nonrutin, banyak constraint, atau justifikasi kompleks.

Nilai tuntutan penyelesaian yang benar-benar diperlukan. KKO hanyalah petunjuk lemah.
Audit kunci dan catatan opsi, tetapi jangan menganggapnya gold manusia. Jika bukti tidak cukup,
gunakan abstain. Beri evidence span dan alasan singkat yang dapat diaudit; jangan berikan
chain-of-thought. {image_note}

ID: {item['_id']}
Subtopik: {item.get('subbab_id') or '-'}
Tipe: {item.get('soal_type') or '-'}
Soal:
{item['soal_text']}

Pilihan dan catatan ekstraksi:
{options}

Kunci pada sumber: {item.get('jawaban') or '-'}
"""


class GeminiSilverAdapter:
    def __init__(self, settings: GeminiSettings, *, client: Any | None = None) -> None:
        self.settings = settings
        self.client = client or genai.Client(
            api_key=settings.api_key,
            http_options=types.HttpOptions(
                api_version="v1beta",
                timeout=settings.timeout_seconds * 1000,
                retry_options=types.HttpRetryOptions(
                    attempts=2,
                    initial_delay=1.0,
                    max_delay=4.0,
                    http_status_codes=[408, 429, 500, 502, 503, 504],
                ),
            ),
        )

    def label_once(
        self, item: dict[str, Any], image_paths: list[Path], *, run_index: int
    ) -> SilverRunResult:
        contents: list[Any] = [build_silver_prompt(item)]
        for image_path in image_paths:
            contents.append(types.Part.from_bytes(data=image_path.read_bytes(), mime_type="image/png"))
        started = time.perf_counter()
        try:
            response = self.client.models.generate_content(
                model=self.settings.model,
                contents=contents,
                config=types.GenerateContentConfig(
                    system_instruction=(
                        "Kamu adalah reviewer asesmen matematika Indonesia. Ikuti schema, "
                        "gunakan bukti singkat, dan nyatakan abstain bila bukti tidak cukup."
                    ),
                    temperature=self.settings.temperature,
                    max_output_tokens=self.settings.max_output_tokens,
                    response_mime_type="application/json",
                    # response_schema currently serializes Pydantic's
                    # additionalProperties as an unsupported snake_case field
                    # for the Gemini API. response_json_schema preserves the
                    # accepted JSON Schema spelling and is validated again below.
                    response_json_schema=SilverLabelOutput.model_json_schema(),
                    thinking_config=types.ThinkingConfig(
                        include_thoughts=False,
                        thinking_level=types.ThinkingLevel.LOW,
                    ),
                ),
            )
            if isinstance(response.parsed, SilverLabelOutput):
                output = response.parsed
            elif response.parsed is not None:
                output = SilverLabelOutput.model_validate(response.parsed)
            else:
                output = SilverLabelOutput.model_validate_json(response.text)
            canonical = output.model_dump_json()
            usage = getattr(response, "usage_metadata", None)
            return SilverRunResult(
                runIndex=run_index,
                status="success",
                output=output,
                responseId=getattr(response, "response_id", None),
                responseHash=hashlib.sha256(canonical.encode("utf-8")).hexdigest(),
                latencyMs=int((time.perf_counter() - started) * 1000),
                usage=TokenUsage(
                    promptTokens=int(getattr(usage, "prompt_token_count", 0) or 0),
                    outputTokens=int(getattr(usage, "candidates_token_count", 0) or 0),
                    thinkingTokens=int(getattr(usage, "thoughts_token_count", 0) or 0),
                    totalTokens=int(getattr(usage, "total_token_count", 0) or 0),
                ),
            )
        except Exception as exc:
            code = getattr(exc, "code", None) or getattr(exc, "status_code", None)
            return SilverRunResult(
                runIndex=run_index,
                status="failed",
                errorCode=f"{type(exc).__name__}:{code or 'unknown'}",
                latencyMs=int((time.perf_counter() - started) * 1000),
            )


def aggregate_silver_runs(runs: list[SilverRunResult]) -> dict[str, Any]:
    successful = [run for run in runs if run.status == "success" and run.output is not None]
    result: dict[str, Any] = {
        "successfulRuns": len(successful),
        "requiredMajority": len(runs) // 2 + 1,
        "contentStatus": None,
        "contentConcerns": [],
        "visualTranscript": None,
        "heads": {},
        "eligibleForTraining": False,
    }
    if not successful:
        return result
    statuses = Counter(run.output.contentStatus for run in successful)
    result["contentStatus"] = statuses.most_common(1)[0][0]
    result["contentConcerns"] = list(dict.fromkeys(
        concern for run in successful for concern in run.output.contentConcerns
    ))
    result["visualTranscript"] = next(
        (run.output.visualTranscript for run in successful if run.output.visualTranscript), None
    )
    for head in ("mathCognitiveDomain", "knowledgeDimension", "intendedDifficulty"):
        labels = []
        for run in successful:
            decision = getattr(run.output, head)
            if decision.action == "classify" and decision.label is not None:
                labels.append(decision.label.value)
        counts = Counter(labels)
        label, count = counts.most_common(1)[0] if counts else (None, 0)
        majority = len(runs) // 2 + 1
        result["heads"][head] = {
            "label": label if count >= majority else None,
            "voteCounts": dict(counts),
            "supportingRuns": count,
            "status": "consistent" if count >= majority else "no_consensus",
        }
    result["eligibleForTraining"] = (
        result["contentStatus"] != "insufficient_evidence"
        and all(value["label"] is not None for value in result["heads"].values())
    )
    return result
