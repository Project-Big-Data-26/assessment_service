"""Build a reproducible class-1 training snapshot from Gemini N=3 silver labels.

This is deliberately separate from ``freeze_dataset_v2.py``: it never claims
that machine-produced labels are expert gold labels.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.classification.v2.contracts import QuestionOption  # noqa: E402
from app.classification.v2.kko import detect_kko  # noqa: E402
from app.classification.v2.serializer import canonical_json_hash  # noqa: E402
from app.llm.silver import SILVER_PROMPT_VERSION  # noqa: E402
from app.training.v2.dataset import GoldTrainingRow, build_snapshot, save_snapshot  # noqa: E402

SOURCE = ROOT / "output/pretest/kelas1/soal_pretest_db.json"
SILVER = ROOT / "output/pretest/kelas1/silver_labels_gemini_3_5_flash_lite.json"
OUTPUT = ROOT / "output/pretest/kelas1/dataset_snapshot_silver.json"


def source_family_from_id(item_id: str, *, grade: int, ordinal: int) -> str:
    base = re.sub(r"(?<=\d)[a-z]$", "", item_id.casefold())
    if base:
        return f"pretest-kelas{grade}-{base}"
    return f"pretest-kelas{grade}-item-{ordinal:03d}"


def minimal_solution(item: dict) -> str:
    key = str(item.get("jawaban") or "").strip().casefold()
    for option in item.get("options") or []:
        if str(option.get("option_id") or "").strip().casefold() == key:
            reason = str(option.get("alasan") or "").strip()
            if reason.casefold().startswith("benar:"):
                reason = reason.split(":", 1)[1].strip()
            return reason or f"Jawaban sumber menunjuk pilihan {item.get('jawaban')}."
    return f"Jawaban sumber menunjuk pilihan {item.get('jawaban') or '-'}; alasan belum tersedia."


def content_hash(item: dict, visual_transcript: str | None, *, grade: int) -> str:
    content = {
        "grade": grade,
        "stem": item["soal_text"],
        "options": [
            {"label": option["option_id"], "text": option["text"]}
            for option in item["options"]
        ],
        "answerKey": item.get("jawaban"),
        "imageRefs": item.get("image_url") or [],
        "visualTranscript": visual_transcript,
    }
    return canonical_json_hash(content)


def build_rows(
    source: list[dict],
    silver: dict,
    *,
    grade: int,
    topic: str,
    id_namespace: str | None = None,
) -> tuple[list[GoldTrainingRow], Counter[str]]:
    rows: list[GoldTrainingRow] = []
    excluded: Counter[str] = Counter()
    for ordinal, item in enumerate(source, start=1):
        item_id = str(item["_id"])
        question_id = f"{id_namespace}:{item_id}" if id_namespace else item_id
        record = silver.get("items", {}).get(item_id)
        if not record:
            excluded["silver_result_missing"] += 1
            continue
        aggregate = record.get("aggregate") or {}
        if not aggregate.get("eligibleForTraining"):
            excluded["silver_no_consensus_or_insufficient"] += 1
            continue
        if (
            aggregate.get("answerKeyStatus") != "verified"
            or not aggregate.get("verifiedAnswerKey")
            or not aggregate.get("verifiedMinimalSolution")
        ):
            excluded["answer_key_or_solution_not_verified"] += 1
            continue
        heads = aggregate.get("heads") or {}
        labels = {
            head: (heads.get(head) or {}).get("label")
            for head in ("mathCognitiveDomain", "knowledgeDimension", "intendedDifficulty")
        }
        if not all(labels.values()):
            excluded["silver_label_missing"] += 1
            continue
        transcript = aggregate.get("visualTranscript")
        if item.get("image_url") and not transcript:
            excluded["visual_transcript_missing"] += 1
            continue
        digest = content_hash(item, transcript, grade=grade)
        adjudicated_profile = (
            (record.get("adjudication") or {})
            .get("output", {})
            .get("intendedDifficulty", {})
            .get("profile")
        )
        run_profile = next(
            (
                run.get("output", {}).get("intendedDifficulty", {}).get("profile")
                for run in record.get("runs", [])
                if run.get("status") == "success"
            ),
            None,
        )
        rows.append(
            GoldTrainingRow(
                questionId=question_id,
                questionVersionId=f"{question_id}:silver-v2",
                contentVersion=1,
                contentHash=digest,
                sourceGroup=(
                    str(item.get("source_family"))
                    if item.get("source_family")
                    else source_family_from_id(item_id, grade=grade, ordinal=ordinal)
                ),
                grade=grade,
                topic=topic,
                subtopic=item.get("subbab_id"),
                questionType="multiple_choice",
                stimulus=item.get("stimulus"),
                stem=item.get("stem") or item["soal_text"],
                options=[
                    QuestionOption(label=option["option_id"], text=option["text"])
                    for option in item["options"]
                ],
                # This source-derived explanation satisfies the technical field,
                # but its provenance below explicitly says it is not expert gold.
                verifiedMinimalSolution=(
                    aggregate.get("verifiedMinimalSolution") or minimal_solution(item)
                ),
                detectedKko=detect_kko(item.get("soal_text")),
                visualTranscript=transcript,
                rubricVersion=silver["rubricVersion"],
                decisionProvenance={
                    "kind": "gemini_n3_blind_adjudicated_silver",
                    "notGold": True,
                    "provider": silver["provider"],
                    "model": silver["model"],
                    "promptVersion": silver["promptVersion"],
                    "requestedRuns": silver["requestedRuns"],
                    "adjudicationPromptVersion": silver.get("adjudicationPromptVersion"),
                    "adjudicated": aggregate.get("adjudicated", False),
                    "difficultyEvidenceProfile": adjudicated_profile or run_profile,
                    "successfulRuns": aggregate.get("successfulRuns"),
                    "contentStatus": aggregate.get("contentStatus"),
                    "sourceAnswerKey": item.get("jawaban"),
                    "verifiedAnswerKey": aggregate.get("verifiedAnswerKey"),
                    "answerKeyStatus": aggregate.get("answerKeyStatus"),
                    "sourceInputHash": record.get("inputHash"),
                    "sourceExternalId": item_id,
                    "sourceResponseHashes": [
                        run.get("responseHash")
                        for run in record.get("runs", [])
                        if run.get("status") == "success"
                    ],
                },
                **labels,
            )
        )
    return rows, excluded


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=SOURCE)
    parser.add_argument("--silver", type=Path, default=SILVER)
    parser.add_argument(
        "--audit",
        type=Path,
        required=True,
        help="A passing immutable pilot/corpus audit that locks this silver checkpoint.",
    )
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--snapshot-id", default="kelas1-grade-aware-silver-v2")
    parser.add_argument("--grade", type=int, default=1, choices=range(1, 13))
    parser.add_argument("--topic")
    parser.add_argument(
        "--id-namespace",
        help="Prefix canonical question IDs, for example kelas2, to avoid cross-source collisions.",
    )
    args = parser.parse_args()

    if args.output.exists():
        raise FileExistsError(f"refusing to overwrite immutable snapshot: {args.output}")

    source = json.loads(args.source.read_text(encoding="utf-8"))
    silver = json.loads(args.silver.read_text(encoding="utf-8"))
    audit = json.loads(args.audit.read_text(encoding="utf-8"))
    silver_hash = hashlib.sha256(args.silver.read_bytes()).hexdigest()
    if silver.get("promptVersion") != SILVER_PROMPT_VERSION:
        raise ValueError(
            "silver checkpoint does not use the current blind key-verified prompt; "
            "preserve it for historical analysis and use a new output version"
        )
    expected_hash = hashlib.sha256(args.source.read_bytes()).hexdigest()
    if silver.get("sourceHash") != expected_hash:
        raise ValueError("silver labels were generated from a different source file")
    if (
        audit.get("readyForExpansion") is not True
        or audit.get("checkpointLockedByAudit") is not True
        or audit.get("checkpointSha256") != silver_hash
        or audit.get("sourceSha256") != expected_hash
    ):
        raise ValueError(
            "passing audit does not lock the supplied source/checkpoint; expansion is blocked"
        )
    topic = args.topic or f"Matematika SD Kelas {args.grade}"
    rows, excluded = build_rows(
        source,
        silver,
        grade=args.grade,
        topic=topic,
        id_namespace=args.id_namespace,
    )
    if not rows:
        raise ValueError("no eligible silver rows were available")
    snapshot = build_snapshot(
        rows,
        snapshot_id=args.snapshot_id,
        seed=42,
        minimum_per_class=15,
        research_only=True,
        label_provenance="llm_silver_blind_v4",
        exclusion_summary=dict(excluded),
    )
    save_snapshot(snapshot, args.output)
    summary = {
        "rows": len(snapshot.rows),
        "excluded": dict(excluded),
        "splitCounts": dict(Counter(entry.split for entry in snapshot.splitManifest)),
        "testUnlockStatus": snapshot.testUnlockStatus,
        "gateFailureCount": len(snapshot.gateFailures),
        "snapshotHash": snapshot.snapshotHash,
        "output": str(args.output),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if not snapshot.gateFailures else 2


if __name__ == "__main__":
    raise SystemExit(main())
