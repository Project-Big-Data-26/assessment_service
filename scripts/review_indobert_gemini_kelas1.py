"""Legacy anchored review retained only for historical reproduction.

New experiments must lock blind silver labels first and then use
``compare_blind_labels_to_predictions.py``. This script exposes model output to
the reviewer and is therefore intentionally disabled unless explicitly opted in.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import replace
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.classification.v2.contracts import V2ClassificationResponse  # noqa: E402
from app.llm.config import GeminiSettings  # noqa: E402
from app.llm.contracts import GeminiAdvisoryResult, GeminiRunResult  # noqa: E402
from app.llm.gemini import PROMPT_VERSION, GeminiProviderError, GeminiReviewAdapter  # noqa: E402
from app.llm.runtime import _aggregate  # noqa: E402
from app.training.v2.dataset import DatasetSnapshot  # noqa: E402

SNAPSHOT = ROOT / "output/pretest/kelas1/dataset_snapshot_silver.json"
PREDICTIONS = ROOT / "output/pretest/kelas1/indobert_predictions_silver.json"
OUTPUT = ROOT / "output/pretest/kelas1/gemini_review_indobert_3_5_flash_lite.json"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic_write(payload: dict, path: Path) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(temporary, path)


def summarize(checkpoint: dict) -> dict:
    records = list(checkpoint["items"].values())
    usages = [
        run.get("usage", {})
        for record in records
        for run in record.get("runs", [])
        if run.get("status") == "success"
    ]
    return {
        "itemsProcessed": len(records),
        "successfulRuns": sum(
            run.get("status") == "success"
            for record in records
            for run in record.get("runs", [])
        ),
        "failedRuns": sum(
            run.get("status") == "failed"
            for record in records
            for run in record.get("runs", [])
        ),
        "promptTokens": sum(int(value.get("promptTokens", 0)) for value in usages),
        "outputTokens": sum(int(value.get("outputTokens", 0)) for value in usages),
        "thinkingTokens": sum(int(value.get("thinkingTokens", 0)) for value in usages),
        "totalTokens": sum(int(value.get("totalTokens", 0)) for value in usages),
    }


def aggregate_record(runs: list[GeminiRunResult], prediction: V2ClassificationResponse, settings: GeminiSettings, rubric: str) -> dict:
    advisory = GeminiAdvisoryResult(
        model=settings.model,
        promptVersion=PROMPT_VERSION,
        rubricVersion=rubric,
        runs=runs,
        mathCognitiveDomain=_aggregate(
            runs,
            head_name="mathCognitiveDomain",
            original_label=prediction.mathCognitiveDomain.label,
        ),
        knowledgeDimension=_aggregate(
            runs,
            head_name="knowledgeDimension",
            original_label=prediction.knowledgeDimension.label,
        ),
        intendedDifficulty=_aggregate(
            runs,
            head_name="intendedDifficulty",
            original_label=prediction.intendedDifficulty.label,
        ),
    )
    return advisory.model_dump(mode="json", exclude={"runs"})


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot", type=Path, default=SNAPSHOT)
    parser.add_argument("--predictions", type=Path, default=PREDICTIONS)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--runs", type=int, choices=(1, 3), default=3)
    parser.add_argument("--attempts", type=int, default=4)
    parser.add_argument("--workers", type=int, choices=(1, 2, 3), default=3)
    parser.add_argument("--pause", type=float, default=0.0)
    parser.add_argument("--allow-legacy-anchored-review", action="store_true")
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()
    if not args.allow_legacy_anchored_review:
        raise SystemExit(
            "anchored post-prediction review is disabled; use blind silver labeling, "
            "lock it with audit_grade_aware_pilot.py, then compare with "
            "compare_blind_labels_to_predictions.py"
        )
    if not args.execute:
        raise SystemExit("live generation requires --execute")

    snapshot = DatasetSnapshot.model_validate_json(args.snapshot.read_text(encoding="utf-8"))
    predictions_payload = json.loads(args.predictions.read_text(encoding="utf-8"))
    predictions = {item["questionId"]: item for item in predictions_payload["items"]}
    settings = replace(GeminiSettings.from_environment(), live_enabled=True)
    adapter = GeminiReviewAdapter(settings)
    checkpoint = {
        "schemaVersion": "gemini-indobert-review-checkpoint-v1",
        "provider": "gemini",
        "model": settings.model,
        "promptVersion": PROMPT_VERSION,
        "rubricVersion": snapshot.rows[0].rubricVersion,
        "requestedRuns": args.runs,
        "snapshotHash": sha256_file(args.snapshot),
        "predictionsHash": sha256_file(args.predictions),
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "updatedAt": None,
        "items": {},
        "summary": {},
    }
    if args.output.is_file():
        existing = json.loads(args.output.read_text(encoding="utf-8"))
        expected = (
            existing.get("model") == settings.model
            and existing.get("requestedRuns") == args.runs
            and existing.get("snapshotHash") == checkpoint["snapshotHash"]
            and existing.get("predictionsHash") == checkpoint["predictionsHash"]
        )
        if not expected:
            raise ValueError("existing review checkpoint uses different inputs/configuration")
        checkpoint = existing

    for index, row in enumerate(snapshot.rows, start=1):
        question = row.inference_request()
        prediction = V2ClassificationResponse.model_validate(
            predictions[row.questionId]["prediction"]
        )
        record = checkpoint["items"].setdefault(
            row.questionId,
            {"index": index, "questionId": row.questionId, "runs": [], "aggregate": {}},
        )
        completed = {
            run["runIndex"] for run in record["runs"] if run.get("status") == "success"
        }
        pending = [value for value in range(1, args.runs + 1) if value not in completed]

        def execute(run_index: int) -> GeminiRunResult:
            last: GeminiRunResult | None = None
            for attempt in range(1, args.attempts + 1):
                started = time.perf_counter()
                try:
                    return adapter.review_once(
                        question,
                        prediction,
                        rubric_version=row.rubricVersion,
                        run_index=run_index,
                    )
                except GeminiProviderError as exc:
                    last = GeminiRunResult(
                        runIndex=run_index,
                        status="failed",
                        errorCode=exc.code,
                        latencyMs=int((time.perf_counter() - started) * 1000),
                    )
                    if attempt < args.attempts:
                        time.sleep(min(2 ** attempt, 8))
            assert last is not None
            return last

        if args.workers == 1 or len(pending) <= 1:
            completed_results = (execute(value) for value in pending)
        else:
            with ThreadPoolExecutor(max_workers=min(args.workers, len(pending))) as executor:
                futures = [executor.submit(execute, value) for value in pending]
                completed_results = [future.result() for future in as_completed(futures)]
        for result in completed_results:
            record["runs"] = [
                value for value in record["runs"] if value["runIndex"] != result.runIndex
            ]
            record["runs"].append(result.model_dump(mode="json"))
            record["runs"].sort(key=lambda value: value["runIndex"])
            typed = [GeminiRunResult.model_validate(value) for value in record["runs"]]
            record["aggregate"] = aggregate_record(
                typed, prediction, settings, row.rubricVersion
            )
            checkpoint["updatedAt"] = datetime.now(timezone.utc).isoformat()
            checkpoint["summary"] = summarize(checkpoint)
            atomic_write(checkpoint, args.output)
            print(
                f"item={index}/{len(snapshot.rows)} run={result.runIndex}/{args.runs} "
                f"status={result.status} total_tokens={result.usage.totalTokens}",
                flush=True,
            )
            if args.pause > 0:
                time.sleep(args.pause)
        typed = [GeminiRunResult.model_validate(value) for value in record["runs"]]
        record["aggregate"] = aggregate_record(typed, prediction, settings, row.rubricVersion)
        checkpoint["summary"] = summarize(checkpoint)
        atomic_write(checkpoint, args.output)
    print(json.dumps(checkpoint["summary"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
