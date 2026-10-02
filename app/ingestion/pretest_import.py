"""Import babNN.json records without treating agent judgments as gold labels."""

from __future__ import annotations

import hashlib
import random
import re
from fractions import Fraction
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field

from app.classification.v2.serializer import canonical_json_hash, normalize_text
from app.services.pretest.agentic.schema import BabFile, derive_status


class ImportedOption(BaseModel):
    model_config = ConfigDict(extra="forbid")
    label: str
    text: str


class QuestionVersionDocument(BaseModel):
    model_config = ConfigDict(extra="forbid")

    questionVersionId: str
    questionId: str
    contentVersion: int = 1
    contentHash: str
    grade: int
    book: str
    chapter: str
    chapterNumber: int
    subchapter: str | None
    sourcePage: int
    sourceSection: str
    sourceItemNumber: str
    sourceKind: str
    stimulus: str | None
    stem: str
    options: list[ImportedOption]
    answerKey: str
    imageRefs: list[str]
    extractionStatus: str
    extractionFlags: list[str]
    extractionEvidence: dict[str, Any]
    sourceRecordChecksum: str
    sourceAssetChecksum: str | None = None
    pipelineVersion: str
    qualificationStatus: Literal[
        "pending_qualification", "eligible", "revision_required", "excluded", "out_of_scope"
    ]
    qualificationReasons: list[str] = Field(default_factory=list)


def grade_from_book(book: str) -> int:
    match = re.search(r"kelas\s*([0-9]+)", book, flags=re.IGNORECASE)
    if not match:
        raise ValueError(f"cannot derive grade from book={book!r}")
    return int(match.group(1))


def _stable_options(source_id: str, answer: str, distractors: list[str]) -> tuple[list[ImportedOption], str]:
    texts = [answer, *distractors]
    seed = int(hashlib.sha256(source_id.encode("utf-8")).hexdigest()[:16], 16)
    random.Random(seed).shuffle(texts)
    labels = "ABCDEFGH"
    options = [ImportedOption(label=labels[index], text=text) for index, text in enumerate(texts)]
    answer_key = next(option.label for option in options if option.text == answer)
    return options, answer_key


def _numeric_value(value: str) -> Fraction | None:
    compact = normalize_text(value).replace(" ", "").replace(",", ".")
    try:
        if re.fullmatch(r"[-+]?\d+(?:\.\d+)?%", compact):
            return Fraction(compact[:-1]) / 100
        if re.fullmatch(r"[-+]?\d+/\d+", compact):
            return Fraction(compact)
        if re.fullmatch(r"[-+]?\d+(?:\.\d+)?", compact):
            return Fraction(compact)
    except (ValueError, ZeroDivisionError):
        return None
    return None


def equivalent_option_flags(options: list[ImportedOption]) -> list[str]:
    reasons: list[str] = []
    text_values = [normalize_text(option.text).casefold() for option in options]
    if len(set(text_values)) != len(text_values):
        reasons.append("duplicate_option_text")
    numeric = [_numeric_value(option.text) for option in options]
    comparable = [value for value in numeric if value is not None]
    if len(set(comparable)) != len(comparable):
        reasons.append("numerically_equivalent_options")
    return reasons


def import_bab_file(
    path: str | Path,
    *,
    pipeline_version: str = "pretest-agentic-v1",
    source_asset_checksum: str | None = None,
) -> list[QuestionVersionDocument]:
    source_path = Path(path)
    source_bytes = source_path.read_bytes()
    bab = BabFile.model_validate_json(source_bytes)
    source_record_checksum = hashlib.sha256(source_bytes).hexdigest()
    grade = grade_from_book(bab.book)
    imported: list[QuestionVersionDocument] = []
    for item in bab.soal:
        status, flags = derive_status(item)
        options, answer_key = _stable_options(item.id, item.jawaban_benar, [entry.teks for entry in item.distraktor])
        qualification: str = "pending_qualification"
        reasons: list[str] = []
        if grade > 6:
            qualification = "out_of_scope"
            reasons.append("grade_outside_sd_v1")
        if status != "draft":
            if qualification != "out_of_scope":
                qualification = "revision_required"
            reasons.append(status)
        option_reasons = equivalent_option_flags(options)
        if option_reasons:
            qualification = "revision_required"
            reasons.extend(option_reasons)
        content = {
            "grade": grade,
            "stimulus": item.stimulus,
            "stem": item.pertanyaan,
            "options": [option.model_dump() for option in options],
            "answerKey": answer_key,
            "imageRefs": item.image_refs,
        }
        content_hash = canonical_json_hash(content)
        imported.append(
            QuestionVersionDocument(
                questionVersionId=f"{item.id}:v1",
                questionId=item.id,
                contentHash=content_hash,
                grade=grade,
                book=bab.book,
                chapter=bab.bab,
                chapterNumber=bab.bab_no,
                subchapter=item.subbab,
                sourcePage=item.source_page,
                sourceSection=item.source_section,
                sourceItemNumber=item.source_item_no,
                sourceKind=item.sumber_soal,
                stimulus=item.stimulus,
                stem=item.pertanyaan,
                options=options,
                answerKey=answer_key,
                imageRefs=item.image_refs,
                extractionStatus=status,
                extractionFlags=flags,
                extractionEvidence={
                    "agentAnswer": item.jawaban_agen,
                    "teacherKey": item.kunci_guru.model_dump() if item.kunci_guru else None,
                    "sourceKeyStatus": item.status_kunci,
                    "agentDifficulty": item.tingkat_kesulitan,
                    "agentDifficultyReason": item.alasan_kesulitan,
                },
                sourceRecordChecksum=source_record_checksum,
                sourceAssetChecksum=source_asset_checksum,
                pipelineVersion=pipeline_version,
                qualificationStatus=qualification,
                qualificationReasons=reasons,
            )
        )
    return imported


def import_directory(directory: str | Path) -> list[QuestionVersionDocument]:
    paths = sorted(Path(directory).glob("kelas*/bab[0-9][0-9].json"))
    return [record for path in paths for record in import_bab_file(path)]


def next_content_version(previous: QuestionVersionDocument, changed_content: dict[str, Any]) -> tuple[int, str]:
    digest = canonical_json_hash(changed_content)
    return (previous.contentVersion if digest == previous.contentHash else previous.contentVersion + 1, digest)
