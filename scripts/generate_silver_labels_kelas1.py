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
from threading import RLock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.llm.config import GeminiSettings  # noqa: E402
from app.llm.silver import (  # noqa: E402
    SUPPORTED_SILVER_GRADES,
    GeminiSilverAdapter,
    SilverAdjudicationResult,
    SilverRunResult,
    aggregate_silver_runs,
    rubric_file_hash,
    requested_runs_for,
    requested_run_indices,
    silver_rubric,
)

SOURCE = ROOT / "output/pretest/kelas1/soal_pretest_db.json"
DEFAULT_OUTPUT = ROOT / "output/pretest/kelas1/silver_labels_gemini.json"


def atomic_write(payload: dict, path: Path) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    # Windows readers (including editors and antivirus) can briefly block a
    # replace. Retry the completed file, preserving both files if it stays locked.
    for attempt in range(6):
        try:
            os.replace(temporary, path)
            return
        except PermissionError as exc:
            if getattr(exc, "winerror", None) not in (5, 32, 33) or attempt == 5:
                raise
            time.sleep(0.1 * 2 ** attempt)


def input_hash(item: dict) -> str:
    encoded = json.dumps(item, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def store_run_result(record: dict, result: dict) -> None:
    """Keep failed attempts as evidence when a resumed run replaces them."""
    run_index = result["runIndex"]
    previous = [run for run in record["runs"] if run["runIndex"] == run_index]
    if any(run["status"] == "success" for run in previous):
        raise ValueError("successful paid runs must not be overwritten")
    if previous:
        record.setdefault("retryHistory", []).extend(previous)
    record["runs"] = [run for run in record["runs"] if run["runIndex"] != run_index]
    record["runs"].append(result)
    record["runs"].sort(key=lambda value: value["runIndex"])


def load_checkpoint(
    path: Path, source: Path, source_hash: str, model: str, runs: int, grade: int,
    *, track: str = "regular",
) -> dict:
    rubric = silver_rubric(grade, track=track)
    if path.is_file():
        checkpoint = json.loads(path.read_text(encoding="utf-8"))
        if checkpoint.get("subjectTrack", "regular") != track:
            raise ValueError("checkpoint subject track differs; use another output path")
        if checkpoint.get("sourceHash") != source_hash:
            raise ValueError("checkpoint sourceHash does not match current question file")
        if checkpoint.get("model") != model or checkpoint.get("requestedRuns") != runs:
            raise ValueError("checkpoint model/run configuration differs; use another output path")
        if checkpoint.get("sourceGrade", 1) != grade or checkpoint.get("promptVersion") != rubric.prompt_version:
            raise ValueError("checkpoint grade/prompt version differs; preserve history and use another output path")
        if checkpoint.get("rubricVersion") != rubric.version or checkpoint.get("rubricHash") != rubric_file_hash(grade, track=track):
            raise ValueError("checkpoint rubric hash differs; preserve history and use another output path")
        return checkpoint
    return {
        "schemaVersion": "gemini-silver-labels-v3-blind-key-verified",
        "source": source.relative_to(ROOT).as_posix(),
        "sourceHash": source_hash,
        "sourceGrade": grade,
        "subjectTrack": track,
        "provider": "gemini",
        "model": model,
        "promptVersion": rubric.prompt_version,
        "adjudicationPromptVersion": rubric.adjudication_version,
        "rubricVersion": rubric.version,
        "rubricHash": rubric_file_hash(grade, track=track),
        "educationLevel": rubric.education_level,
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
    adjudication_usages = [
        (item.get("adjudication") or {}).get("usage", {})
        for item in items
        if (item.get("adjudication") or {}).get("status") == "success"
    ]
    usages.extend(adjudication_usages)
    archived_runs = [run for item in items for run in item.get("previousN3Evidence", {}).get("runs", [])]
    usages.extend(run.get("usage", {}) for run in archived_runs if run.get("status") == "success")
    usages.extend((item.get("previousN3Evidence", {}).get("adjudication") or {}).get("usage", {})
                  for item in items
                  if (item.get("previousN3Evidence", {}).get("adjudication") or {}).get("status") == "success")
    labels = [
        item.get("aggregate", {}).get("heads", {}).get("intendedDifficulty", {}).get("label")
        for item in items
        if (item.get("aggregate", {}).get("eligibleForTraining")
            or item.get("aggregate", {}).get("contentQualified"))
    ]
    label_counts = {label: labels.count(label) for label in ("Easy", "Medium", "Hard")}
    dominant = max(label_counts.values(), default=0)
    eligible = max(sum(label_counts.values()), 1)
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
        "adjudicatedItems": sum(
            item.get("aggregate", {}).get("adjudicated") is True for item in items
        ),
        "pendingAdjudication": sum(
            item.get("aggregate", {}).get("needsAdjudication") is True for item in items
        ),
        "difficultyDistribution": label_counts,
        "dominantDifficultyShare": dominant / eligible,
        "boundaryAnalysisRequired": bool(
            dominant / eligible > 0.90
            or label_counts["Medium"] == 0
            or label_counts["Hard"] == 0
        ),
        "promptTokens": sum(int(usage.get("promptTokens", 0)) for usage in usages),
        "outputTokens": sum(int(usage.get("outputTokens", 0)) for usage in usages),
        "thinkingTokens": sum(int(usage.get("thinkingTokens", 0)) for usage in usages),
        "totalTokens": sum(int(usage.get("totalTokens", 0)) for usage in usages),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=SOURCE)
    parser.add_argument("--grade", type=int, choices=SUPPORTED_SILVER_GRADES, default=1)
    parser.add_argument("--track", choices=("regular", "tl"), default="regular")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--runs", type=int, default=3, choices=(1, 3))
    parser.add_argument("--limit", type=int)
    parser.add_argument("--question-id", action="append", help="Pilot IDs from the unchanged source; reuse its checkpoint for the full batch.")
    parser.add_argument("--stop-on-quota", action="store_true", help="Stop immediately on any 429, including short-term limits.")
    parser.add_argument("--max-consecutive-provider-failures", type=int, default=0,
                        help="Stop on repeated transport/5xx failures; 0 keeps the legacy retry behavior.")
    parser.add_argument("--max-api-calls", type=int, help="Maximum new application requests in this invocation, including adjudication and retries.")
    parser.add_argument("--attempts", type=int, default=3)
    parser.add_argument("--pause", type=float, default=0.5)
    parser.add_argument("--workers", type=int, default=1, choices=(1, 2, 3))
    parser.add_argument(
        "--adjudicate",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Adjudicate non-unanimous or abstained blind runs after all runs are locked.",
    )
    parser.add_argument("--execute", action="store_true", help="Required confirmation for live API calls")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    track = getattr(args, "track", "regular")
    silver_rubric(args.grade, track=track)
    if not args.execute:
        raise SystemExit("live generation requires --execute")
    args.source = args.source.resolve()
    args.output = args.output.resolve()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    items = json.loads(args.source.read_text(encoding="utf-8"))
    selected_ids = getattr(args, "question_id", None)
    if selected_ids:
        if args.limit is not None:
            raise ValueError("select pilot IDs or a limit, not both")
        wanted = set(selected_ids)
        if not wanted <= {str(item["_id"]) for item in items}:
            raise ValueError("pilot contains unknown question IDs")
        items = [item for item in items if str(item["_id"]) in wanted]
    if args.limit is not None:
        items = items[: args.limit]
    max_calls = getattr(args, "max_api_calls", None)
    stop_on_quota = getattr(args, "stop_on_quota", False)
    max_provider_failures = getattr(args, "max_consecutive_provider_failures", 0)
    if max_provider_failures < 0:
        raise ValueError("max-consecutive-provider-failures must be nonnegative")
    if max_calls is not None and max_calls < 1:
        raise ValueError("max-api-calls must be positive")
    if (max_calls is not None or stop_on_quota or max_provider_failures) and args.workers != 1:
        raise ValueError("bounded quota-safe execution requires one worker")
    source_hash = hashlib.sha256(args.source.read_bytes()).hexdigest()
    settings = replace(GeminiSettings.from_environment(), live_enabled=True)
    adapter = GeminiSilverAdapter(settings)
    checkpoint = load_checkpoint(
        args.output, args.source, source_hash, settings.model, args.runs, args.grade,
        track=track,
    )
    checkpoint["executionStatus"] = "running"
    checkpoint.pop("stopReason", None)
    checkpoint.pop("blockedByGrade", None)
    initial_calls = int(checkpoint.get("apiAttempts", 0))
    progress_lock = RLock()
    consecutive_provider_failures = 0
    provider_unavailable = False

    def budget_available() -> bool:
        return max_calls is None or checkpoint.get("apiAttempts", 0) - initial_calls < max_calls

    def provider_block(result) -> bool:
        return bool(provider_unavailable or result.quotaDailyExhausted or result.providerFailureReason
                    or (stop_on_quota and (result.errorCode or "").endswith(":429")))

    def observe_provider_result(result) -> None:
        nonlocal consecutive_provider_failures, provider_unavailable
        code = result.errorCode or ""
        temporary = code.startswith(("ConnectError:", "ConnectTimeout:", "ReadTimeout:",
                                     "RemoteProtocolError:", "ServerError:"))
        consecutive_provider_failures = consecutive_provider_failures + 1 if temporary else 0
        provider_unavailable = bool(max_provider_failures and consecutive_provider_failures >= max_provider_failures)

    def block_status(result) -> str:
        if result.quotaDailyExhausted:
            return "blocked_provider_daily_quota"
        if (result.errorCode or "").endswith(":429"):
            return "blocked_provider_quota_or_rate_limit"
        if provider_unavailable:
            return "blocked_provider_temporarily_unavailable"
        return "blocked_provider_configuration"

    def stop_details(result) -> dict:
        details = {"errorCode": result.errorCode, "quotaLimits": result.quotaLimits,
                   "providerFailureReason": result.providerFailureReason}
        if provider_unavailable:
            details.update(stopCategory="network_or_service", consecutiveProviderFailures=consecutive_provider_failures)
        return details

    def save_progress() -> None:
        with progress_lock:
            checkpoint["updatedAt"] = datetime.now(timezone.utc).isoformat()
            checkpoint["summary"] = summarize(checkpoint)
            atomic_write(checkpoint, args.output)

    def begin_request() -> bool:
        with progress_lock:
            if not budget_available():
                return False
            checkpoint["apiAttempts"] = checkpoint.get("apiAttempts", 0) + 1
            save_progress()
            return True

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
                "adjudication": None,
            }
            checkpoint["items"][item_id] = record
        required_runs = requested_runs_for(checkpoint, record)
        required_indices = requested_run_indices(record, required_runs)
        completed = {run["runIndex"] for run in record["runs"] if run["status"] == "success"}
        image_paths = [args.source.parent / ref for ref in (item.get("image_url") or [])]
        missing = [path for path in image_paths if not path.is_file()]
        if missing:
            raise FileNotFoundError(f"missing image assets for {item_id}: {len(missing)}")
        pending = [run_index for run_index in required_indices if run_index not in completed]

        def execute_run(run_index: int) -> SilverRunResult | None:
            result: SilverRunResult | None = None
            for attempt in range(1, args.attempts + 1):
                if not begin_request():
                    return None
                result = adapter.label_once(
                    item, image_paths, run_index=run_index, grade=args.grade,
                    **({"track": track} if track != "regular" else {}),
                )
                observe_provider_result(result)
                if result.status == "success" or provider_block(result):
                    break
                record.setdefault("attemptHistory", []).append(result.model_dump(mode="json"))
                save_progress()
                if attempt < args.attempts:
                    time.sleep(min(2 ** attempt, 8))
            assert result is not None
            return result

        if args.workers == 1 or len(pending) <= 1:
            # A generator lets the checkpoint commit each serial run before
            # the next request, preserving paid results across interruptions.
            completed_results = (execute_run(run_index) for run_index in pending)
        else:
            with ThreadPoolExecutor(max_workers=min(args.workers, len(pending))) as executor:
                futures = {executor.submit(execute_run, run_index): run_index for run_index in pending}
                completed_results = [future.result() for future in as_completed(futures)]

        for result in completed_results:
            if result is None:
                checkpoint["executionStatus"] = "stopped_api_call_budget"
                checkpoint["stopReason"] = {"maxNewApiCalls": max_calls}
                save_progress()
                return 4
            run_index = result.runIndex
            store_run_result(record, result.model_dump(mode="json"))
            typed_runs = [SilverRunResult.model_validate(run) for run in record["runs"]]
            typed_adjudication = (
                SilverAdjudicationResult.model_validate(record["adjudication"])
                if record.get("adjudication")
                else None
            )
            record["aggregate"] = aggregate_silver_runs(typed_runs, typed_adjudication, requested_runs=required_runs)
            save_progress()
            print(
                f"item={ordinal}/{len(items)} runIndex={run_index} requestedRuns={required_runs} "
                f"status={result.status} total_tokens={result.usage.totalTokens}",
                flush=True,
            )
            if provider_block(result):
                checkpoint["executionStatus"] = block_status(result)
                checkpoint["stopReason"] = stop_details(result)
                save_progress()
                print(json.dumps(checkpoint["stopReason"]), flush=True)
                return 3
            time.sleep(args.pause)
        typed_runs = [SilverRunResult.model_validate(run) for run in record["runs"]]
        # Reuse a previously successful adjudication without losing its labels.
        existing = record.get("adjudication") or {}
        typed_existing = SilverAdjudicationResult.model_validate(existing) if existing.get("status") == "success" else None
        record["aggregate"] = aggregate_silver_runs(typed_runs, typed_existing, requested_runs=required_runs)
        if (
            required_runs == 3
            and args.adjudicate
            and record["aggregate"].get("needsAdjudication")
            and sum(run.status == "success" for run in typed_runs) == required_runs
        ):
            existing = record.get("adjudication") or {}
            if existing.get("status") != "success":
                adjudication: SilverAdjudicationResult | None = None
                for attempt in range(1, args.attempts + 1):
                    if not begin_request():
                        checkpoint["executionStatus"] = "stopped_api_call_budget"
                        checkpoint["stopReason"] = {"maxNewApiCalls": max_calls}
                        save_progress()
                        return 4
                    adjudication = adapter.adjudicate_once(
                        item, image_paths, typed_runs, grade=args.grade,
                        **({"track": track} if track != "regular" else {}),
                    )
                    observe_provider_result(adjudication)
                    if adjudication.status == "success" or provider_block(adjudication):
                        break
                    record.setdefault("adjudicationAttemptHistory", []).append(adjudication.model_dump(mode="json"))
                    save_progress()
                    if attempt < args.attempts:
                        time.sleep(min(2 ** attempt, 8))
                assert adjudication is not None
                record["adjudication"] = adjudication.model_dump(mode="json")
            typed_adjudication = SilverAdjudicationResult.model_validate(
                record["adjudication"]
            )
            record["aggregate"] = aggregate_silver_runs(
                typed_runs, typed_adjudication, requested_runs=required_runs
            )
            if provider_block(typed_adjudication):
                checkpoint["executionStatus"] = block_status(typed_adjudication)
                checkpoint["stopReason"] = stop_details(typed_adjudication)
                save_progress()
                print(json.dumps(checkpoint["stopReason"]), flush=True)
                return 3
        save_progress()
    checkpoint["executionStatus"] = "completed_batch"
    save_progress()
    print(json.dumps(checkpoint["summary"], ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
