"""Resume only the approved reference-replenishment IDs, preserving paid evidence."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from dotenv import dotenv_values
from app.llm.credentials import credential_slots, use_credential_slot
from app.services.exercise.workflow import approve_validation, batch_lock, atomic_json
from scripts import validate_exercise_batch as exercise
from scripts.provider_failover import activate_checkpoint

RUN = ROOT / "runs/exercise_replenishment/codex_batch01"


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
        if not p["final"].exists():
            exercise.package(name, "batch01", allow_partial=True)
    exercise.set_namespace("failover")
    activate_checkpoint(name, "batch01", "gemini")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--classes", nargs="+", required=True, choices=list(exercise.CLASSES))
    parser.add_argument("--slot", type=int, default=1)
    parser.add_argument("--max-api-calls", type=int, required=True)
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()
    progress = load(RUN / "progress.json")
    if not args.execute:
        print(json.dumps({n: len(selected_ids(n, progress)) for n in args.classes}))
        return
    (RUN / "validation").mkdir(exist_ok=True)
    values = dotenv_values(ROOT / ".env")
    calls = 0
    unavailable = set()
    for name in args.classes:
        ids = selected_ids(name, progress)
        prepare(name)
        providers = [(provider, slot) for provider in ("gemini", "groq")
                     for slot in sorted(credential_slots(provider, values),
                                        key=lambda s: (s != args.slot, s))]
        finished = False
        for provider, slot in providers:
            if (provider, slot) in unavailable or calls >= args.max_api_calls:
                continue
            activate_checkpoint(name, "batch01", provider)
            with use_credential_slot(provider, slot):
                while calls < args.max_api_calls:
                    p = exercise.paths(name, "batch01")
                    cp = load(p["checkpoint"])
                    pending = [qid for qid in ids if not exercise.complete(cp, [qid])]
                    if not pending:
                        finished = True
                        break
                    selected = pending[:10]
                    extra = [arg for qid in selected for arg in ("--question-id", qid)]
                    before = cp.get("apiAttempts", 0)
                    with batch_lock(p["exercise"]):
                        code = exercise.run_labeler(name, "batch01", extra,
                            min(len(selected) * 3, args.max_api_calls - calls),
                            4096, stop_on_503=True)
                        after = load(p["checkpoint"])
                        spent = max(0, after.get("apiAttempts", 0) - before)
                        calls += spent
                        exercise.package(name, "batch01", allow_partial=True)
                    done = report(name, ids, "running", calls, code)
                    if done == len(ids):
                        finished = True
                        break
                    if str(after.get("executionStatus", "")).startswith("blocked_provider"):
                        unavailable.add((provider, slot))
                        break
                    if spent == 0 or not any(exercise.complete(after, [qid]) for qid in selected):
                        unavailable.add((provider, slot))
                        break
            if finished:
                break
        report(name, ids, "complete" if finished else "blocked_or_budget_exhausted", calls)
        if not finished:
            return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
