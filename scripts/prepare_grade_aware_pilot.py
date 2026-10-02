"""Create a deterministic, blind 60-item pilot without leaking agent judgments."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.ingestion.pretest_import import QuestionVersionDocument, import_directory  # noqa: E402


def difficulty_band(value: object) -> str:
    numeric = int(value or 0)
    return "low" if numeric <= 2 else "middle" if numeric == 3 else "high"


def image_source(record: QuestionVersionDocument, ref: str) -> Path:
    return ROOT / f"output/pretest/kelas{record.grade}/images" / (
        f"kelas{record.grade}_{Path(ref).name}"
    )


def qualified_candidates(grade: int) -> list[QuestionVersionDocument]:
    candidates = [
        record
        for record in import_directory(ROOT / "output/pretest")
        if record.grade == grade and record.extractionStatus == "draft"
    ]
    return [
        record
        for record in candidates
        if not record.imageRefs
        or all(image_source(record, ref).is_file() for ref in record.imageRefs)
    ]


def qualification_summary(grade: int) -> dict:
    records = [
        record
        for record in import_directory(ROOT / "output/pretest")
        if record.grade == grade
    ]
    draft_missing_assets = sum(
        record.extractionStatus == "draft"
        and bool(record.imageRefs)
        and not all(image_source(record, ref).is_file() for ref in record.imageRefs)
        for record in records
    )
    return {
        "totalGradeCorpus": len(records),
        "extractionStatus": dict(Counter(record.extractionStatus for record in records)),
        "excludedStatusNotDraft": sum(
            record.extractionStatus != "draft" for record in records
        ),
        "excludedDraftMissingAssets": draft_missing_assets,
    }
def select_stratified(
    candidates: list[QuestionVersionDocument], *, limit: int, seed: int
) -> list[QuestionVersionDocument]:
    strata: dict[tuple[object, ...], deque[QuestionVersionDocument]] = defaultdict(deque)
    for record in candidates:
        key = (
            record.chapterNumber,
            bool(record.imageRefs),
            difficulty_band(record.extractionEvidence.get("agentDifficulty")),
            record.sourceKind,
        )
        strata[key].append(record)
    for key, values in strata.items():
        ordered = sorted(
            values,
            key=lambda item: hashlib.sha256(
                f"{seed}:{item.questionVersionId}".encode("utf-8")
            ).hexdigest(),
        )
        strata[key] = deque(ordered)
    selected: list[QuestionVersionDocument] = []
    keys = sorted(strata, key=lambda value: repr(value))
    while len(selected) < limit and any(strata.values()):
        for key in keys:
            if strata[key] and len(selected) < limit:
                selected.append(strata[key].popleft())
    return selected


def export_record(record: QuestionVersionDocument, destination: Path) -> dict:
    image_urls: list[str] = []
    for ref in record.imageRefs:
        source = image_source(record, ref)
        target = destination / "images" / source.name
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.is_file():
            shutil.copyfile(source, target)
        image_urls.append(f"images/{target.name}")
    stem = (
        f"{record.stimulus.strip()}\n\n{record.stem.strip()}"
        if record.stimulus
        else record.stem.strip()
    )
    source_item_family = re.sub(
        r"(?<=\d)[a-z]$", "", record.sourceItemNumber.strip().casefold()
    )
    return {
        "_id": record.questionId,
        "berkas_id": None,
        "subbab_id": record.subchapter,
        "kelas_id": record.grade,
        "soal_text": stem,
        "stimulus": record.stimulus,
        "stem": record.stem,
        "source_family": (
            f"{record.book}|bab={record.chapterNumber}|page={record.sourcePage}|"
            f"section={record.sourceSection}|item={source_item_family}"
        ),
        "image_url": image_urls,
        "soal_type": "Pilihan Ganda",
        "options": [
            {"option_id": option.label, "text": option.text, "alasan": None}
            for option in record.options
        ],
        "matching_pairs": None,
        "jawaban": record.answerKey,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--grade", type=int, choices=range(1, 7), default=1)
    parser.add_argument("--limit", type=int, default=60)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "output/pilots/kelas1-grade-aware-v2",
    )
    args = parser.parse_args()
    candidates = qualified_candidates(args.grade)
    if len(candidates) < args.limit:
        raise ValueError(
            f"only {len(candidates)} qualified questions with available assets; need {args.limit}"
        )
    selected = select_stratified(candidates, limit=args.limit, seed=args.seed)
    destination = args.output_dir.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    question_path = destination / "questions.json"
    sampling_path = destination / "sampling_manifest.json"
    if question_path.exists() or sampling_path.exists():
        raise FileExistsError(f"refusing to overwrite immutable pilot: {destination}")
    questions = [export_record(record, destination) for record in selected]
    question_path.write_text(
        json.dumps(questions, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    sampling = {
        "schemaVersion": "grade-aware-pilot-sampling-v1",
        "grade": args.grade,
        "seed": args.seed,
        "candidateCount": len(candidates),
        "selectedCount": len(selected),
        "qualification": qualification_summary(args.grade),
        "samplingOnlyNotLabels": True,
        "strata": {
            "chapter": dict(Counter(str(item.chapterNumber) for item in selected)),
            "visual": dict(Counter(str(bool(item.imageRefs)).lower() for item in selected)),
            "agentDifficultyBand": dict(
                Counter(
                    difficulty_band(item.extractionEvidence.get("agentDifficulty"))
                    for item in selected
                )
            ),
            "sourceKind": dict(Counter(item.sourceKind for item in selected)),
        },
        "questionIds": [item.questionId for item in selected],
    }
    sampling_path.write_text(
        json.dumps(sampling, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(sampling, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
