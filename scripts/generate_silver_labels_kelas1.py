"""Generate resumable N-run Gemini silver labels for all class-1 pretest items."""

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

from app.llm.config import GeminiSettings  # noqa: E402
from app.llm.silver import (  # noqa: E402
    RUBRIC_VERSION,
    SILVER_PROMPT_VERSION,
    GeminiSilverAdapter,
    SilverRunResult,
    aggregate_silver_runs,
)

SOURCE = ROOT / "output/pretest/kelas1/soal_pretest_db.json"
DEFAULT_OUTPUT = ROOT / "output/pretest/kelas1/silver_labels_gemini.json"


def atomic_write(payload: dict, path: Path) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(temporary, path)


def input_hash(item: dict) -> str:
    encoded = json.dumps(item, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def load_checkpoint(path: Path, source_hash: str, model: str, runs: int) -> dict:
    if path.is_file():
        checkpoint = json.loads(path.read_text(encoding="utf-8"))
        if checkpoint.get("sourceHash") != source_hash:
            raise ValueError("checkpoint sourceHash does not match current question file")
        if checkpoint.get("model") != model or checkpoint.get("requestedRuns") != runs:
            raise ValueError("checkpoint model/run configuration differs; use another output path")
        return checkpoint
    return {
        "schemaVersion": "gemini-silver-labels-v1",
        "source": SOURCE.relative_to(ROOT).as_posix(),
        "sourceHash": source_hash,
        "provider": "gemini",
        "model": model,
        "promptVersion": SILVER_PROMPT_VERSION,
        "rubricVersion": RUBRIC_VERSION,
        "requestedRuns": runs,
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "updatedAt": None,
        "items": {},
        "summary": {},
    }


def summarize(checkpoint: dict) -> dict:
    items = list(checkpoint["items"].values())
    usages = [
        run.get("usage", {})
        for item in items
        for run in item.get("runs", [])
        if run.get("status") == "success"
    ]
    return {
        "itemsProcessed": len(items),
        "itemsEligibleForTraining": sum(
            bool(item.get("aggregate", {}).get("eligibleForTraining")) for item in items
        ),
        "successfulRuns": sum(
            run.get("status") == "success" for item in items for run in item.get("runs", [])
        ),
        "failedRuns": sum(
            run.get("status") == "failed" for item in items for run in item.get("runs", [])
        ),
        "promptTokens": sum(int(usage.get("promptTokens", 0)) for usage in usages),
        "outputTokens": sum(int(usage.get("outputTokens", 0)) for usage in usages),
        "thinkingTokens": sum(int(usage.get("thinkingTokens", 0)) for usage in usages),
        "totalTokens": sum(int(usage.get("totalTokens", 0)) for usage in usages),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--runs", type=int, default=3, choices=(1, 3))
    parser.add_argument("--limit", type=int)
    parser.add_argument("--attempts", type=int, default=3)
    parser.add_argument("--pause", type=float, default=0.5)
    parser.add_argument("--workers", type=int, default=1, choices=(1, 2, 3))
    parser.add_argument("--execute", action="store_true", help="Required confirmation for live API calls")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.execute:
        raise SystemExit("live generation requires --execute")
    items = json.loads(SOURCE.read_text(encoding="utf-8"))
    if args.limit is not None:
        items = items[: args.limit]
    source_hash = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    settings = replace(GeminiSettings.from_environment(), live_enabled=True)
    adapter = GeminiSilverAdapter(settings)
    checkpoint = load_checkpoint(args.output, source_hash, settings.model, args.runs)

    for ordinal, item in enumerate(items, start=1):
        item_id = str(item["_id"])
        digest = input_hash(item)
        record = checkpoint["items"].get(item_id)
        if record and record.get("inputHash") != digest:
            raise ValueError(f"input changed for {item_id}")
        if record is None:
            record = {
                "index": ordinal,
                "questionId": item_id,
                "inputHash": digest,
                "runs": [],
                "aggregate": {},
            }
            checkpoint["items"][item_id] = record
        completed = {run["runIndex"] for run in record["runs"] if run["status"] == "success"}
        image_paths = [SOURCE.parent / ref for ref in (item.get("image_url") or [])]
        missing = [path for path in image_paths if not path.is_file()]
        if missing:
            raise FileNotFoundError(f"missing image assets for {item_id}: {len(missing)}")
        pending = [run_index for run_index in range(1, args.runs + 1) if run_index not in completed]

        def execute_run(run_index: int) -> SilverRunResult:
            result: SilverRunResult | None = None
            for attempt in range(1, args.attempts + 1):
                result = adapter.label_once(item, image_paths, run_index=run_index)
                if result.status == "success":
                    break
                if attempt < args.attempts:
                    time.sleep(min(2 ** attempt, 8))
            assert result is not None
            return result

        if args.workers == 1 or len(pending) <= 1:
            completed_results = [execute_run(run_index) for run_index in pending]
        else:
            with ThreadPoolExecutor(max_workers=min(args.workers, len(pending))) as executor:
                futures = {executor.submit(execute_run, run_index): run_index for run_index in pending}
                completed_results = [future.result() for future in as_completed(futures)]

        for result in completed_results:
            run_index = result.runIndex
            record["runs"] = [run for run in record["runs"] if run["runIndex"] != run_index]
            record["runs"].append(result.model_dump(mode="json"))
            record["runs"].sort(key=lambda value: value["runIndex"])
            typed_runs = [SilverRunResult.model_validate(run) for run in record["runs"]]
            record["aggregate"] = aggregate_silver_runs(typed_runs)
            checkpoint["updatedAt"] = datetime.now(timezone.utc).isoformat()
            checkpoint["summary"] = summarize(checkpoint)
            atomic_write(checkpoint, args.output)
            print(
                f"item={ordinal}/{len(items)} run={run_index}/{args.runs} "
                f"status={result.status} total_tokens={result.usage.totalTokens}",
                flush=True,
            )
            time.sleep(args.pause)
        typed_runs = [SilverRunResult.model_validate(run) for run in record["runs"]]
        record["aggregate"] = aggregate_silver_runs(typed_runs)
        checkpoint["summary"] = summarize(checkpoint)
        atomic_write(checkpoint, args.output)
    print(json.dumps(checkpoint["summary"], ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
