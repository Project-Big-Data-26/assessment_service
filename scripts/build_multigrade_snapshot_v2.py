"""Combine versioned per-grade silver snapshots and rebuild one leakage-safe split."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.training.v2.dataset import DatasetSnapshot, build_snapshot, save_snapshot  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot", type=Path, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--snapshot-id", required=True)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--all-grades", action="store_true")
    parser.add_argument("--rubric-version")
    args = parser.parse_args()
    destination = args.output.resolve()
    if destination.exists():
        raise FileExistsError(f"refusing to overwrite immutable snapshot: {destination}")
    inputs = [
        DatasetSnapshot.model_validate_json(path.read_text(encoding="utf-8"))
        for path in args.snapshot
    ]
    rows = [row for snapshot in inputs for row in [*snapshot.rows, *snapshot.expansionRows]]
    duplicate_ids = [item for item, count in Counter(row.questionVersionId for row in rows).items() if count > 1]
    if duplicate_ids:
        raise ValueError(f"duplicate questionVersionId across snapshots: {duplicate_ids[:5]}")
    if args.rubric_version and {row.rubricVersion for row in rows} != {args.rubric_version}:
        raise ValueError("combined rows must all use the requested rubric version")
    training_grades = tuple(range(1, 13)) if args.all_grades else tuple(range(1, 7))
    snapshot = build_snapshot(
        rows,
        snapshot_id=args.snapshot_id,
        seed=args.seed,
        minimum_train_per_class=30,
        minimum_per_class=15,
        required_grades=training_grades,
        training_grades=training_grades,
        required_grade_tracks=(
            tuple(f"{grade}:regular" for grade in range(1, 13)) + ("11:tl", "12:tl")
            if args.all_grades else ()
        ),
        research_only=any(item.researchOnly for item in inputs),
        label_provenance="ai_silver",
        exclusion_summary=dict(
            sum((Counter(item.exclusionSummary) for item in inputs), Counter())
        ),
    )
    save_snapshot(snapshot, destination)
    print(
        json.dumps(
            {
                "snapshotId": snapshot.snapshotId,
                "rows": len(snapshot.rows),
                "grades": dict(Counter(str(row.grade) for row in snapshot.rows)),
                "difficulty": dict(
                    Counter(row.intendedDifficulty.value for row in snapshot.rows)
                ),
                "testUnlockStatus": snapshot.testUnlockStatus,
                "researchOnly": snapshot.researchOnly,
                "labelProvenance": snapshot.labelProvenance,
                "gateFailures": snapshot.gateFailures,
                "output": destination.as_posix(),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if not snapshot.gateFailures else 2


if __name__ == "__main__":
    raise SystemExit(main())
