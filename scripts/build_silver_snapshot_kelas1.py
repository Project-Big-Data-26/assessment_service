"""Build a reproducible class-1 training snapshot from Gemini N=3 silver labels.

This is deliberately separate from ``freeze_dataset_v2.py``: it never claims
that machine-produced labels are expert gold labels.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.classification.v2.contracts import QuestionOption  # noqa: E402
from app.classification.v2.kko import detect_kko  # noqa: E402
from app.classification.v2.serializer import canonical_json_hash  # noqa: E402
from app.training.v2.dataset import GoldTrainingRow, build_snapshot, save_snapshot  # noqa: E402

SOURCE = ROOT / "output/pretest/kelas1/soal_pretest_db.json"
SILVER = ROOT / "output/pretest/kelas1/silver_labels_gemini_3_5_flash_lite.json"
OUTPUT = ROOT / "output/pretest/kelas1/dataset_snapshot_silver.json"


def minimal_solution(item: dict) -> str:
    key = str(item.get("jawaban") or "").strip().casefold()
    for option in item.get("options") or []:
        if str(option.get("option_id") or "").strip().casefold() == key:
            reason = str(option.get("alasan") or "").strip()
            if reason.casefold().startswith("benar:"):
                reason = reason.split(":", 1)[1].strip()
            return reason or f"Jawaban sumber menunjuk pilihan {item.get('jawaban')}."
    return f"Jawaban sumber menunjuk pilihan {item.get('jawaban') or '-'}; alasan belum tersedia."


def content_hash(item: dict, visual_transcript: str | None) -> str:
    content = {
        "grade": 1,
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


def build_rows(source: list[dict], silver: dict) -> tuple[list[GoldTrainingRow], Counter[str]]:
    rows: list[GoldTrainingRow] = []
    excluded: Counter[str] = Counter()
    for ordinal, item in enumerate(source, start=1):
        item_id = str(item["_id"])
        record = silver.get("items", {}).get(item_id)
        if not record:
            excluded["silver_result_missing"] += 1
            continue
        aggregate = record.get("aggregate") or {}
        if not aggregate.get("eligibleForTraining"):
            excluded["silver_no_consensus_or_insufficient"] += 1
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
        digest = content_hash(item, transcript)
        rows.append(
            GoldTrainingRow(
                questionId=item_id,
                questionVersionId=f"{item_id}:silver-v1",
                contentVersion=1,
                contentHash=digest,
                # Each extracted question is an independent exercise here;
                # exact/near duplicates are still joined by dataset.py.
                sourceGroup=f"pretest-kelas1-item-{ordinal:03d}",
                grade=1,
                topic="Matematika SD Kelas 1",
                subtopic=item.get("subbab_id"),
                questionType="multiple_choice",
                stem=item["soal_text"],
                options=[
                    QuestionOption(label=option["option_id"], text=option["text"])
                    for option in item["options"]
                ],
                # This source-derived explanation satisfies the technical field,
                # but its provenance below explicitly says it is not expert gold.
                verifiedMinimalSolution=minimal_solution(item),
                detectedKko=detect_kko(item.get("soal_text")),
                visualTranscript=transcript,
                rubricVersion=silver["rubricVersion"],
                decisionProvenance={
                    "kind": "gemini_n3_silver_bootstrap",
                    "notGold": True,
                    "provider": silver["provider"],
                    "model": silver["model"],
                    "promptVersion": silver["promptVersion"],
                    "requestedRuns": silver["requestedRuns"],
                    "successfulRuns": aggregate.get("successfulRuns"),
                    "contentStatus": aggregate.get("contentStatus"),
                    "verifiedAnswerKey": item.get("jawaban"),
                    "sourceInputHash": record.get("inputHash"),
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
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--snapshot-id", default="kelas1-gemini-silver-n3-v1")
    args = parser.parse_args()

    source = json.loads(args.source.read_text(encoding="utf-8"))
    silver = json.loads(args.silver.read_text(encoding="utf-8"))
    expected_hash = hashlib.sha256(args.source.read_bytes()).hexdigest()
    if silver.get("sourceHash") != expected_hash:
        raise ValueError("silver labels were generated from a different source file")
    rows, excluded = build_rows(source, silver)
    if not rows:
        raise ValueError("no eligible silver rows were available")
    snapshot = build_snapshot(
        rows,
        snapshot_id=args.snapshot_id,
        seed=42,
        minimum_per_class=15,
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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
