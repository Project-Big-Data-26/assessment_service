"""Canonical serializer shared by dataset building and online inference."""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from collections.abc import Mapping, Sequence
from typing import Any

from .contracts import V2ClassificationRequest

INPUT_SCHEMA_VERSION = "math-question-text-v1"


def normalize_text(value: str | None) -> str:
    """Normalize representation without changing mathematical notation."""
    if not value:
        return "-"
    value = unicodedata.normalize("NFC", value)
    value = value.replace("\r\n", "\n").replace("\r", "\n")
    return re.sub(r"[ \t]+", " ", value).strip() or "-"


def serialize_question(
    question: V2ClassificationRequest | Mapping[str, Any], *, representation: str = "kko"
) -> str:
    """Serialize one question using one preregistered ablation representation."""
    if not isinstance(question, V2ClassificationRequest):
        question = V2ClassificationRequest.model_validate(question)
    options = "\n".join(
        f"{normalize_text(option.label)}. {normalize_text(option.text)}"
        for option in question.options
    ) or "-"
    kko = ", ".join(normalize_text(item) for item in question.detectedKko) or "-"
    all_fields = (
        ("Kelas", str(question.grade)),
        ("Topik", normalize_text(question.topic)),
        ("Subtopik", normalize_text(question.subtopic)),
        ("Tipe soal", normalize_text(question.questionType)),
        ("Stimulus", normalize_text(question.stimulus)),
        ("Soal", normalize_text(question.stem)),
        ("Pilihan", options),
        ("Solusi minimum terverifikasi", normalize_text(question.verifiedMinimalSolution)),
        ("KKO terdeteksi", kko),
        ("Transkripsi visual", normalize_text(question.visualTranscript)),
    )
    included = {
        "stem_options": {"Soal", "Pilihan"},
        "metadata": {"Kelas", "Topik", "Subtopik", "Tipe soal", "Stimulus", "Soal", "Pilihan", "Transkripsi visual"},
        "solution": {"Kelas", "Topik", "Subtopik", "Tipe soal", "Stimulus", "Soal", "Pilihan", "Solusi minimum terverifikasi", "Transkripsi visual"},
        "kko": {key for key, _ in all_fields},
    }
    if representation not in included:
        raise ValueError(f"unknown input representation: {representation}")
    fields = tuple((key, value) for key, value in all_fields if key in included[representation])
    return "\n".join(f"{key}: {value}" for key, value in fields)


def canonical_json_hash(value: Mapping[str, Any] | Sequence[Any]) -> str:
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def classification_input_hash(question: V2ClassificationRequest, *, representation: str = "kko") -> str:
    return hashlib.sha256(serialize_question(question, representation=representation).encode("utf-8")).hexdigest()
