"""Gemini silver-label generation for the 3x4x3 bootstrap dataset."""

from __future__ import annotations

import hashlib
import json
import time
from collections import Counter
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Annotated, Any, Literal

from google import genai
from google.genai import types
from pydantic import BaseModel, ConfigDict, Field, StringConstraints, model_validator
import yaml

from app.classification.v2.contracts import (
    CognitiveDomain,
    IntendedDifficulty,
    KnowledgeDimension,
)

from .config import GeminiSettings
from .contracts import TokenUsage

SILVER_PROMPT_VERSION = "gemini-silver-math-3x4x3-v10-blind-key-verified"
SILVER_ADJUDICATION_PROMPT_VERSION = "gemini-silver-math-3x4x3-v10-adjudication"
RUBRIC_VERSION = "math-rubric-3x4x3-v8-sd-grade-aware"
RUBRIC_PATH = Path(__file__).resolve().parents[2] / "configs/rubric_math_3x4x3_v8_sd.yaml"
SUPPORTED_SILVER_GRADES = tuple(range(1, 13))


@dataclass(frozen=True)
class SilverRubric:
    prompt_version: str
    adjudication_version: str
    version: str
    path: Path
    education_level: str


def silver_rubric(grade: int = 1, *, track: str = "regular") -> SilverRubric:
    if track not in ("regular", "tl"):
        raise ValueError("silver track must be regular or tl")
    if track == "tl":
        if grade not in (11, 12):
            raise ValueError("Matematika Tingkat Lanjut supports grade 11 or 12")
        return SilverRubric(
            f"gemini-silver-math-3x4x3-v10-blind-sma{grade}-tl-key-verified",
            f"gemini-silver-math-3x4x3-v10-adjudication-sma{grade}-tl",
            f"math-rubric-3x4x3-v8-sma{grade}-tl-grade-aware",
            RUBRIC_PATH.with_name(f"rubric_math_3x4x3_v8_sma{grade}_tl.yaml"), "SMA",
        )
    if grade in range(1, 7):
        return SilverRubric(
            SILVER_PROMPT_VERSION, SILVER_ADJUDICATION_PROMPT_VERSION,
            RUBRIC_VERSION, RUBRIC_PATH, "SD",
        )
    if grade in (7, 8, 9):
        return SilverRubric(
            f"gemini-silver-math-3x4x3-v10-blind-smp{grade}-key-verified",
            f"gemini-silver-math-3x4x3-v10-adjudication-smp{grade}",
            f"math-rubric-3x4x3-v8-smp{grade}-grade-aware",
            RUBRIC_PATH.with_name(f"rubric_math_3x4x3_v8_smp{grade}.yaml"), "SMP",
        )
    if grade in (10, 11, 12):
        return SilverRubric(
            f"gemini-silver-math-3x4x3-v10-blind-sma{grade}-key-verified",
            f"gemini-silver-math-3x4x3-v10-adjudication-sma{grade}",
            f"math-rubric-3x4x3-v8-sma{grade}-grade-aware",
            RUBRIC_PATH.with_name(f"rubric_math_3x4x3_v8_sma{grade}.yaml"), "SMA",
        )
    raise ValueError("silver review supports grade 1-6 (SD), grade 7-9 (SMP), and grade 10-12 (SMA)")

ShortText = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=700)]
EvidenceText = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=260)]
ContentConcernText = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=1800)]


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
    profile: "DifficultyEvidenceProfile | None" = None

    @model_validator(mode="after")
    def validate_action(self) -> "SilverDifficultyHead":
        self.validate_common(self.label)
        if self.action == "classify" and self.profile is None:
            raise ValueError("difficulty classification requires an evidence profile")
        if self.action == "abstain" and self.profile is not None:
            raise ValueError("difficulty abstention must not invent an evidence profile")
        return self


class DifficultyEvidenceProfile(BaseModel):
    model_config = ConfigDict(extra="forbid")

    expectedPrerequisite: ShortText
    dependentSteps: int = Field(ge=1, le=12)
    routineStatus: Literal["familiar_routine", "routine_selection", "nonroutine_strategy"]
    strategySelection: bool
    representationTransfer: bool
    relevantInformationUnits: int = Field(ge=1, le=24)
    interactingConstraints: int = Field(ge=0, le=12)
    calculationLoad: Literal["low", "moderate", "high"]
    scaffoldLevel: Literal["none", "partial", "strong"]
    distractorQuality: Literal["weak", "plausible", "strong", "not_applicable"]
    gradeRelativeRationale: ShortText


class SilverLabelOutput(BaseModel):
    model_config = ConfigDict(extra="forbid")

    contentStatus: Literal["valid", "concern", "insufficient_evidence"]
    # Preserve a detailed content/key concern instead of rejecting the paid
    # assessment solely because its explanation exceeds a short rationale.
    contentConcerns: list[ContentConcernText] = Field(default_factory=list, max_length=6)
    answerKeyStatus: Literal["verified", "conflict", "unverifiable"]
    verifiedAnswerKey: ShortText | None = None
    visualTranscript: str | None = Field(default=None, max_length=1800)
    verifiedMinimalSolution: ShortText
    mathCognitiveDomain: SilverCognitiveHead
    knowledgeDimension: SilverKnowledgeHead
    intendedDifficulty: SilverDifficultyHead

    @model_validator(mode="after")
    def validate_answer_key(self) -> "SilverLabelOutput":
        if self.answerKeyStatus == "verified" and not self.verifiedAnswerKey:
            raise ValueError("verified answer key status requires verifiedAnswerKey")
        if self.answerKeyStatus == "unverifiable" and self.verifiedAnswerKey is not None:
            raise ValueError("unverifiable answer key must not invent verifiedAnswerKey")
        return self


def silver_provider_schema() -> dict[str, Any]:
    """Encode head validators in the provider schema, preserving abstention.

    Pydantic after validators are absent from model_json_schema. Without the
    conditional branches, the provider can repeatedly classify with no evidence.
    Local validation still checks the unmodified SilverLabelOutput contract.
    """
    schema = SilverLabelOutput.model_json_schema()
    for name in ("SilverCognitiveHead", "SilverKnowledgeHead", "SilverDifficultyHead"):
        original = schema["$defs"][name]
        classify, abstain = deepcopy(original), deepcopy(original)
        classify["properties"]["action"] = {"type": "string", "enum": ["classify"]}
        classify["properties"]["evidenceSpans"]["minItems"] = 1
        classify["required"] = list(dict.fromkeys([*classify["required"], "label", "evidenceSpans"]))
        classify["properties"]["label"] = next(
            branch for branch in original["properties"]["label"]["anyOf"] if branch.get("type") != "null"
        )
        abstain["properties"]["action"] = {"type": "string", "enum": ["abstain"]}
        abstain["properties"]["label"] = {"type": "null"}
        if name == "SilverDifficultyHead":
            classify["properties"]["profile"] = {"$ref": "#/$defs/DifficultyEvidenceProfile"}
            classify["required"].append("profile")
            abstain["properties"]["profile"] = {"type": "null"}
        schema["$defs"][name] = {"anyOf": [classify, abstain]}
    return schema


class SilverRunResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    runIndex: int = Field(ge=1)
    status: Literal["success", "failed"]
    output: SilverLabelOutput | None = None
    errorCode: str | None = None
    errorDetails: list[dict[str, str]] = Field(default_factory=list)
    quotaDailyExhausted: bool = False
    quotaLimits: list[dict[str, str]] = Field(default_factory=list)
    providerFailureReason: str | None = None
    responseId: str | None = None
    promptHash: str | None = None
    responseHash: str | None = None
    latencyMs: int = Field(ge=0)
    usage: TokenUsage = Field(default_factory=TokenUsage)


class SilverAdjudicationResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: Literal["success", "failed"]
    output: SilverLabelOutput | None = None
    errorCode: str | None = None
    errorDetails: list[dict[str, str]] = Field(default_factory=list)
    quotaDailyExhausted: bool = False
    quotaLimits: list[dict[str, str]] = Field(default_factory=list)
    providerFailureReason: str | None = None
    responseId: str | None = None
    promptHash: str | None = None
    responseHash: str | None = None
    latencyMs: int = Field(ge=0)
    usage: TokenUsage = Field(default_factory=TokenUsage)


def build_silver_prompt(item: dict[str, Any], *, grade: int = 1, track: str = "regular") -> str:
    rubric = silver_rubric(grade, track=track)
    configuration = yaml.safe_load(rubric.path.read_text(encoding="utf-8"))
    if configuration["rubric_version"] != rubric.version:
        raise ValueError("silver rubric file version does not match its configured identity")
    domain_definitions = "\n".join(
        f"  {label} = {configuration['mathCognitiveDomain'][label]}"
        for label in ("knowing", "applying", "reasoning")
    )
    knowledge_definitions = "\n".join(
        f"  {label} = {configuration['knowledgeDimension'][label]}"
        for label in ("factual", "conceptual", "procedural", "metacognitive")
    )
    difficulty_definitions = "\n".join(
        f"  {label} = {configuration['intendedDifficulty'][label]}"
        for label in ("Easy", "Medium", "Hard")
    )
    boundary_rules = "\n".join(
        f"- {rule}" for rule in configuration["difficulty_boundary_rules"]
    )
    examples = configuration.get("difficulty_examples_by_grade", {}).get(grade)
    if examples is None:
        examples = configuration["difficulty_examples"]
    examples_text = "\n".join(f"- {label}: {examples[label]}" for label in ("Easy", "Medium", "Hard"))
    context = configuration["grade_context"].strip()
    if rubric.education_level in ("SMP", "SMA"):
        context = f"Jenjang sasaran: {rubric.education_level} kelas {grade}.\n{context}"
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
    prompt = f"""Klasifikasikan satu soal matematika kelas {grade} sebagai SILVER LABEL penelitian awal.

PENILAIAN INI BLIND. Jangan menebak atau meminta prediksi model, vote reviewer lain,
konsensus, distribusi label, atau estimasi kesulitan agen. Informasi tersebut sengaja tidak diberikan.

{context}

Gunakan rubrik berikut.
- Domain kognitif matematika:
{domain_definitions}
- Dimensi pengetahuan:
{knowledge_definitions}
- Intended difficulty adalah tuntutan isi bagi siswa kelas {grade} sebelum data respons:
{difficulty_definitions}

Aturan batas kesulitan:
{boundary_rules}

Contoh pembanding bagi kelas sasaran, bukan soal sumber atau label otomatis:
{examples_text}
Gunakan tuntutan solusi minimum soal yang sedang dinilai; contoh tidak menetapkan
kuota kategori dan tidak menggantikan bukti soal.

Verifikasi kunci sumber terhadap soal. Isi answerKeyStatus=verified hanya jika solusi
minimum membuktikannya, conflict bila kunci sumber salah/ambigu, dan unverifiable bila
bukti soal tidak cukup. Isi verifiedAnswerKey hanya jika jawabannya dapat diverifikasi.
Tulis verifiedMinimalSolution yang paling singkat tetapi cukup untuk membuktikan jawaban.
Untuk difficulty isi seluruh evidence profile. Profil adalah bukti audit, bukan skor yang
dijumlahkan otomatis. Hard tidak berarti sekadar angka besar atau stem panjang; Easy juga
tidak berarti semua operasi dasar. Nilai familiaritas dan tuntutan terhadap kelas {grade}.
Rationale difficulty harus menjelaskan ketergantungan langkah, keputusan strategi,
kendala yang berinteraksi, bantuan soal, dan tuntutan relatif kelas sesuai profil.

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
    return prompt


def rubric_file_hash(grade: int = 1, *, track: str = "regular") -> str:
    return hashlib.sha256(silver_rubric(grade, track=track).path.read_bytes()).hexdigest()


def provider_quota_details(exc: Exception) -> dict[str, Any]:
    """Keep only quota identifiers/limits, never raw provider messages or credentials."""
    message = str(getattr(exc, "message", "")).casefold()
    code = getattr(exc, "code", None) or getattr(exc, "status_code", None)
    reason = (
        "api_key_invalid" if "api key not valid" in message
        else "provider_configuration_error" if code in (400, 401, 403, 404)
        else None
    )
    data = getattr(exc, "details", {})
    if not isinstance(data, dict):
        return {"providerFailureReason": reason}
    error = data.get("error", data)
    if not isinstance(error, dict):
        return {"providerFailureReason": reason}
    limits = []
    for detail in error.get("details", []) or []:
        if not isinstance(detail, dict):
            continue
        for violation in detail.get("violations", []) or []:
            if not isinstance(violation, dict):
                continue
            limits.append({
                field: str(violation[field])[:240]
                for field in ("quotaMetric", "quotaId", "quotaValue")
                if field in violation
            })
    return {
        "quotaDailyExhausted": any(
            "perday" in limit.get("quotaId", "").casefold() for limit in limits
        ),
        "quotaLimits": limits,
        "providerFailureReason": reason,
    }


def failed_response_evidence(exc: Exception, response: Any | None) -> dict[str, Any]:
    """Retain paid usage and error locations without response text or credentials."""
    errors = []
    if callable(getattr(exc, "errors", None)):
        for error in exc.errors(include_input=False, include_url=False)[:12]:
            errors.append({"location": ".".join(map(str, error.get("loc", []))),
                           "type": str(error.get("type", "unknown"))})
    candidates = getattr(response, "candidates", None) or []
    if candidates:
        finish = getattr(candidates[0], "finish_reason", None)
        if finish is not None:
            errors.append({"location": "provider.finishReason", "type": str(finish)})
    usage = getattr(response, "usage_metadata", None)
    raw = getattr(response, "text", None)
    return {"errorDetails": errors, "responseId": getattr(response, "response_id", None),
            "responseHash": hashlib.sha256(raw.encode("utf-8")).hexdigest() if raw else None,
            "usage": TokenUsage(
                promptTokens=int(getattr(usage, "prompt_token_count", 0) or 0),
                outputTokens=int(getattr(usage, "candidates_token_count", 0) or 0),
                thinkingTokens=int(getattr(usage, "thoughts_token_count", 0) or 0),
                totalTokens=int(getattr(usage, "total_token_count", 0) or 0))}


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
                    http_status_codes=[408, 500, 502, 503, 504],
                ),
            ),
        )

    def label_once(
        self, item: dict[str, Any], image_paths: list[Path], *, run_index: int, grade: int = 1,
        track: str = "regular",
    ) -> SilverRunResult:
        prompt = build_silver_prompt(item, grade=grade, track=track)
        prompt_hash = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
        contents: list[Any] = [prompt]
        for image_path in image_paths:
            contents.append(types.Part.from_bytes(data=image_path.read_bytes(), mime_type="image/png"))
        started = time.perf_counter()
        response = None
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
                    response_json_schema=silver_provider_schema(),
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
                promptHash=prompt_hash,
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
                promptHash=prompt_hash,
                latencyMs=int((time.perf_counter() - started) * 1000),
                **provider_quota_details(exc),
                **failed_response_evidence(exc, response),
            )

    def adjudicate_once(
        self,
        item: dict[str, Any],
        image_paths: list[Path],
        runs: list[SilverRunResult],
        *,
        grade: int,
        track: str = "regular",
    ) -> SilverAdjudicationResult:
        successful = [run for run in runs if run.status == "success" and run.output]
        evidence = [
            {
                "runIndex": run.runIndex,
                "contentStatus": run.output.contentStatus,
                "answerKeyStatus": run.output.answerKeyStatus,
                "verifiedAnswerKey": run.output.verifiedAnswerKey,
                "verifiedMinimalSolution": run.output.verifiedMinimalSolution,
                "mathCognitiveDomain": run.output.mathCognitiveDomain.model_dump(mode="json"),
                "knowledgeDimension": run.output.knowledgeDimension.model_dump(mode="json"),
                "intendedDifficulty": run.output.intendedDifficulty.model_dump(mode="json"),
            }
            for run in successful
        ]
        prompt = (
            build_silver_prompt(item, grade=grade, track=track)
            + "\n\nADJUDIKASI SILVER: nilai ulang soal secara independen, lalu gunakan bukti run blind "
            "berikut hanya untuk menemukan sumber perbedaan. Jangan melakukan voting mekanis. "
            "Tidak ada prediksi IndoBERT atau estimasi kesulitan agen di dalam data ini.\n"
            + json.dumps(evidence, ensure_ascii=False, sort_keys=True)
        )
        prompt_hash = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
        contents: list[Any] = [prompt]
        for image_path in image_paths:
            contents.append(types.Part.from_bytes(data=image_path.read_bytes(), mime_type="image/png"))
        started = time.perf_counter()
        response = None
        try:
            response = self.client.models.generate_content(
                model=self.settings.model,
                contents=contents,
                config=types.GenerateContentConfig(
                    system_instruction=(
                        "Kamu adalah adjudikator asesmen matematika Indonesia. Putuskan dari "
                        "rubrik dan bukti soal; jangan mengikuti suara mayoritas secara otomatis."
                    ),
                    temperature=0.0,
                    max_output_tokens=self.settings.max_output_tokens,
                    response_mime_type="application/json",
                    response_json_schema=silver_provider_schema(),
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
            return SilverAdjudicationResult(
                status="success",
                output=output,
                responseId=getattr(response, "response_id", None),
                promptHash=prompt_hash,
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
            return SilverAdjudicationResult(
                status="failed",
                errorCode=f"{type(exc).__name__}:{code or 'unknown'}",
                promptHash=prompt_hash,
                latencyMs=int((time.perf_counter() - started) * 1000),
                **provider_quota_details(exc),
                **failed_response_evidence(exc, response),
            )


def requested_runs_for(checkpoint: dict, record: dict | None = None) -> int:
    """A resumed batch may retain completed N=3 items beside new N=1 items."""
    requested = (record or {}).get("requestedRuns", checkpoint.get("requestedRuns", 3))
    if not isinstance(requested, int) or isinstance(requested, bool) or requested not in (1, 3):
        raise ValueError("requestedRuns must be 1 or 3")
    return requested


def requested_run_indices(record: dict, requested: int) -> list[int]:
    """Preserve the original index when reusing a paid run in single-run mode."""
    indices = record.get("requestedRunIndices", list(range(1, requested + 1)))
    if (len(indices) != requested or len(set(indices)) != requested
            or any(not isinstance(index, int) or isinstance(index, bool) or index not in (1, 2, 3) for index in indices)
            or (requested == 3 and set(indices) != {1, 2, 3})):
        raise ValueError("requested run indices must match the evaluation mode")
    return sorted(indices)


def aggregate_silver_runs(
    runs: list[SilverRunResult],
    adjudication: SilverAdjudicationResult | None = None,
    *, requested_runs: int = 3,
) -> dict[str, Any]:
    if not isinstance(requested_runs, int) or isinstance(requested_runs, bool) or requested_runs not in (1, 3):
        raise ValueError("requested_runs must be 1 or 3")
    successful = [run for run in runs if run.status == "success" and run.output is not None]
    result: dict[str, Any] = {
        "successfulRuns": len(successful),
        "requiredMajority": len(runs) // 2 + 1,
        "contentStatus": None,
        "contentConcerns": [],
        "answerKeyStatus": None,
        "verifiedAnswerKey": None,
        "visualTranscript": None,
        "verifiedMinimalSolution": None,
        "heads": {},
        "needsAdjudication": False,
        "adjudicated": False,
        "eligibleForTraining": False,
    }
    if not successful:
        return result
    statuses = Counter(run.output.contentStatus for run in successful)
    result["contentStatus"] = statuses.most_common(1)[0][0]
    answer_statuses = Counter(run.output.answerKeyStatus for run in successful)
    result["answerKeyStatus"] = answer_statuses.most_common(1)[0][0]
    result["verifiedAnswerKey"] = next(
        (run.output.verifiedAnswerKey for run in successful if run.output.verifiedAnswerKey),
        None,
    )
    result["contentConcerns"] = list(dict.fromkeys(
        concern for run in successful for concern in run.output.contentConcerns
    ))
    result["visualTranscript"] = next(
        (run.output.visualTranscript for run in successful if run.output.visualTranscript), None
    )
    result["verifiedMinimalSolution"] = next(
        (run.output.verifiedMinimalSolution for run in successful), None
    )
    if requested_runs == 1:
        if len(runs) != 1 or len(successful) != 1 or adjudication is not None:
            raise ValueError("single-run evaluation requires one response and no adjudication")
        output = successful[0].output
        for head in ("mathCognitiveDomain", "knowledgeDimension", "intendedDifficulty"):
            decision = getattr(output, head)
            label = decision.label.value if decision.action == "classify" and decision.label else None
            result["heads"][head] = {
                "label": label, "voteCounts": {label: 1} if label else {},
                "supportingRuns": 1 if label else 0,
                "status": "single_run" if label else "abstained",
            }
        # One valid provider response completes N=1. Content/key problems and
        # abstentions are held by qualification, without another paid judgment.
        result["contentQualified"] = bool(
            output.contentStatus == "valid" and output.answerKeyStatus == "verified"
            and output.verifiedAnswerKey and output.verifiedMinimalSolution
            and all(value["label"] is not None for value in result["heads"].values())
        )
        result["singleRunEvaluated"] = True
        result["eligibleForTraining"] = False
        return result
    all_unanimous = len(successful) == len(runs) == 3
    if not (all_unanimous and len(statuses) == 1 and len(answer_statuses) == 1):
        result["needsAdjudication"] = True
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
            "label": label if all_unanimous and count == 3 else None,
            "voteCounts": dict(counts),
            "supportingRuns": count,
            "status": "unanimous" if all_unanimous and count == 3 else "needs_adjudication",
        }
        if not (all_unanimous and count == 3):
            result["needsAdjudication"] = True
    if result["contentStatus"] != "valid" or result["answerKeyStatus"] != "verified":
        result["needsAdjudication"] = True
    if result["needsAdjudication"] and adjudication and adjudication.status == "success":
        assert adjudication.output is not None
        result["contentStatus"] = adjudication.output.contentStatus
        result["contentConcerns"] = adjudication.output.contentConcerns
        result["answerKeyStatus"] = adjudication.output.answerKeyStatus
        result["verifiedAnswerKey"] = adjudication.output.verifiedAnswerKey
        result["visualTranscript"] = adjudication.output.visualTranscript
        result["verifiedMinimalSolution"] = adjudication.output.verifiedMinimalSolution
        for head in ("mathCognitiveDomain", "knowledgeDimension", "intendedDifficulty"):
            decision = getattr(adjudication.output, head)
            result["heads"][head].update(
                {
                    "label": decision.label.value if decision.label else None,
                    "status": "adjudicated" if decision.action == "classify" else "abstained",
                    "adjudicationRationale": decision.rationale,
                }
            )
        result["adjudicated"] = True
        result["needsAdjudication"] = False
    result["eligibleForTraining"] = bool(
        result["contentStatus"] == "valid"
        and result["answerKeyStatus"] == "verified"
        and bool(result["verifiedAnswerKey"])
        and bool(result["verifiedMinimalSolution"])
        and not result["needsAdjudication"]
        and all(value["label"] is not None for value in result["heads"].values())
    )
    return result


SilverDifficultyHead.model_rebuild()
