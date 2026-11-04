"""Resume only the approved reference-replenishment IDs, preserving paid evidence."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time
from collections import Counter
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from dotenv import dotenv_values
from app.llm.credentials import credential_slots, use_credential_slot
from app.services.exercise.workflow import approve_validation, batch_lock, atomic_json
from scripts import validate_exercise_batch as exercise
from scripts.provider_failover import activate_checkpoint
from app.llm.providers import settings_for

RUN = ROOT / "runs/exercise_replenishment/codex_batch01"


def pending_by_shortfall(name, ids, checkpoint):
    """Prioritize deficient target slots using published active labels only."""
    p = exercise.paths(name, "batch01")
    meta = load(p["exercise"] / "soal_exercise_meta.json")
    final = p["final"] / "validation_results.json"
    stock = Counter((meta[str(q["_id"])]["bab_id"], meta[str(q["_id"])]["subbab_kode"], q.get("cognitive_level"))
                    for q in (load(final) if final.exists() else []) if q.get("status") == "active")
    minimum = 10 if exercise.CLASSES[name][0] <= 6 else 15 if exercise.CLASSES[name][0] <= 9 else 20
    def missing(qid):
        row = meta[qid]
        return max(0, minimum - stock[row["bab_id"], row["subbab_kode"], row["level_target"]])
    # Surplus candidates stay after deficient targets, preserving the original
    # authorized validation scope without relabeling results to force quotas.
    return sorted((qid for qid in ids if not exercise.complete(checkpoint, [qid])), key=lambda qid: -missing(qid))


def retry_delay(checkpoint, attempt):
    """Respect brief rate limits; stop a slot on daily quota or repeated errors."""
    status = checkpoint.get("executionStatus", "")
    if "daily_quota" in status or attempt >= 2:
        return None
    limits = (checkpoint.get("stopReason") or {}).get("quotaLimits") or []
    delays = []
    for limit in limits:
        metric = str(limit.get("quotaMetric", "")).lower()
        if "per_day" in metric or "daily" in metric:
            return None
        try:
            delays.append(float(limit.get("retryAfterSeconds", 0)))
        except (ValueError, TypeError):
            pass
    if status == "blocked_provider_quota_or_rate_limit" and any(delays):
        delay = max(delays) + 1
        return delay if delay <= 300 else None
    if status in ("blocked_provider_http_503", "blocked_provider_temporarily_unavailable"):
        return (15, 30)[attempt]
    return None


def wait_seconds(delay):
    # Keep long provider cooldowns interruptible in short increments.
    while delay > 0:
        step = min(delay, 30)
        time.sleep(step)
        delay -= step


def selected_ids(name, progress):
    return [hashlib.md5(qid.encode()).hexdigest()[:24]
            for key, job in progress["jobs"].items() if key.startswith(name + "-")
            for qid in job["ids"]]


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def report(name, ids, status, calls, code=None):
    p = exercise.paths(name, "batch01")
    cp = load(p["checkpoint"])
    done = sum(exercise.complete(cp, [qid]) for qid in ids)
    result = {"class": name, "updatedAt": datetime.now(timezone.utc).isoformat(),
              "status": status, "target": len(ids), "completed": done,
              "pending": len(ids) - done, "newApiCallsThisInvocation": calls,
              "provider": cp.get("provider"), "executionStatus": cp.get("executionStatus"),
              "exitCode": code, "checkpoint": str(p["checkpoint"].relative_to(ROOT))}
    atomic_json(RUN / "validation" / (name + ".json"), result)
    print(json.dumps(result), flush=True)
    return done


def prepare(name):
    exercise.set_provider("gemini")
    candidates = []
    for namespace in (None, "failover"):
        exercise.set_namespace(namespace)
        p = exercise.paths(name, "batch01")
        if p["checkpoint"].exists():
            cp = load(p["checkpoint"])
            candidates.append((sum(exercise.complete(cp, [i]) for i in cp["items"]),
                               namespace == "failover", namespace))
    exercise.set_namespace(max(candidates)[2])
    p = exercise.paths(name, "batch01")
    state_path = p["exercise"] / "reference_replenishment_state.json"
    state = load(state_path)
    state["validationOwner"] = "replenishment_runner"
    atomic_json(state_path, state)
    if state["phase"] == "generation_complete":
        manifest = p["exercise"] / "reference_replenishment_manifest.json"
        approve_validation(p["exercise"], hashlib.sha256(manifest.read_bytes()).hexdigest())
    with batch_lock(p["exercise"]):
        exercise.extend_class(name, "batch01")
        exercise.package(name, "batch01", allow_partial=True)
    exercise.set_namespace("failover")
    activate_checkpoint(name, "batch01", "gemini")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--classes", nargs="+", required=True, choices=list(exercise.CLASSES))
    parser.add_argument("--slot", type=int, default=1)
    parser.add_argument("--max-api-calls", type=int, help="Optional explicit limit; default continues until providers stop or scope completes")
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()
    progress = load(RUN / "progress.json")
    if not args.execute:
        print(json.dumps({n: len(selected_ids(n, progress)) for n in args.classes}))
        return
    (RUN / "validation").mkdir(exist_ok=True)
    values = dotenv_values(ROOT / ".env")
    calls = 0
    budget = args.max_api_calls if args.max_api_calls is not None else sys.maxsize
    if budget <= 0:
        parser.error("--max-api-calls must be positive")
    unavailable = set()
    attempts = []
    run_state = RUN / "validation" / "current_run.json"
    def save_run(status):
        atomic_json(run_state, {"status": status, "updatedAt": datetime.now(timezone.utc).isoformat(),
            "requestedRuns": 1, "classes": args.classes, "newApiCalls": calls,
            "unavailableSlots": [{"provider": p, "slot": s} for p, s in sorted(unavailable)], "attempts": attempts})
    save_run("running")
    for name in args.classes:
        ids = selected_ids(name, progress)
        prepare(name)
        providers = [(provider, slot) for provider in ("gemini", "groq")
                     for slot in sorted(credential_slots(provider, values),
                                        key=lambda s: (s != args.slot, s))]
        finished = False
        for provider, slot in providers:
            if (provider, slot) in unavailable or calls >= budget:
                continue
            with use_credential_slot(provider, slot):
                settings = settings_for(provider)
                if not settings.live_enabled:
                    unavailable.add((provider, slot))
                    attempts.append({"provider": provider, "slot": slot, "status": "disabled"})
                    save_run("running")
                    continue
                activate_checkpoint(name, "batch01", provider)
                if load(exercise.paths(name, "batch01")["checkpoint"]).get("requestedRuns") != 1:
                    raise ValueError("Replenishment validation requires N=1")
                retries = 0
                while calls < budget:
                    p = exercise.paths(name, "batch01")
                    cp = load(p["checkpoint"])
                    pending = pending_by_shortfall(name, ids, cp)
                    if not pending:
                        finished = True
                        break
                    selected = pending[:10]
                    extra = [arg for qid in selected for arg in ("--question-id", qid)]
                    before = cp.get("apiAttempts", 0)
                    with batch_lock(p["exercise"]):
                        code = exercise.run_labeler(name, "batch01", extra,
                            min(len(selected) * 3, budget - calls),
                            4096, stop_on_503=True)
                        after = load(p["checkpoint"])
                        spent = max(0, after.get("apiAttempts", 0) - before)
                        calls += spent
                        exercise.package(name, "batch01", allow_partial=True)
                    done = report(name, ids, "running", calls, code)
                    attempts.append({"class": name, "provider": provider, "slot": slot,
                                     "apiCalls": spent, "status": after.get("executionStatus"),
                                     "errorCode": (after.get("stopReason") or {}).get("errorCode")})
                    save_run("running")
                    if done == len(ids):
                        finished = True
                        break
                    if str(after.get("executionStatus", "")).startswith("blocked_provider"):
                        delay = retry_delay(after, retries)
                        if delay is not None:
                            print(json.dumps({"provider": provider, "slot": slot, "retryInSeconds": delay}), flush=True)
                            retries += 1
                            wait_seconds(delay)
                            continue
                        unavailable.add((provider, slot))
                        break
                    retries = 0
                    if spent == 0 or not any(exercise.complete(after, [qid]) for qid in selected):
                        unavailable.add((provider, slot))
                        break
            if finished:
                break
        report(name, ids, "complete" if finished else "blocked_or_budget_exhausted", calls)
        if not finished:
            save_run("api_call_budget_reached" if calls >= budget else "all_configured_provider_slots_unavailable")
            return 3
    save_run("validation_scope_complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
