"""Verify a completed decision reused from an immutable provider checkpoint."""
import hashlib
import json
from pathlib import Path

from .silver import requested_runs_for, requested_run_indices


def verify_retained_record(source, question_id, record, cache=None):
    reference = record.get("retainedProviderEvidence")
    if not reference:
        raise ValueError("foreign provider evidence must have an immutable checkpoint reference")
    path = Path(reference["path"]).resolve()
    if not path.is_relative_to(Path(source).resolve().parent):
        raise ValueError("retained provider checkpoint must stay inside the staging directory")
    cache = {} if cache is None else cache
    identity = (str(path), reference["sha256"])
    if identity not in cache:
        data = path.read_bytes()
        if hashlib.sha256(data).hexdigest() != reference["sha256"]:
            raise ValueError("retained provider checkpoint checksum differs")
        cache[identity] = json.loads(data)
    original = cache[identity]
    if (original["sourceHash"] != hashlib.sha256(Path(source).read_bytes()).hexdigest()
            or original["provider"] != record["provider"] or original["model"] != record["model"]):
        raise ValueError("retained provider/source identity differs")
    before = original["items"][question_id]
    actual = {key: value for key, value in record.items() if key != "retainedProviderEvidence"}
    for key in ("provider", "model"):
        if key not in before:
            actual.pop(key, None)
    if actual != before:
        raise ValueError("a retained paid decision was changed")
    requested = requested_runs_for(original, before)
    successes = [run for run in before.get("runs", []) if run["status"] == "success"]
    if (len(successes) != requested or {run["runIndex"] for run in successes}
            != set(requested_run_indices(before, requested)) or before.get("aggregate", {}).get("needsAdjudication") is not False):
        raise ValueError("only completed foreign-provider decisions may be retained")
