"""Immutable evidence migration for sequential Gemini/Groq quota failover."""
from collections import Counter
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path

from app.llm.providers import settings_for
from scripts import validate_exercise_batch as exercise
from scripts.generate_silver_labels_kelas1 import atomic_write, load_checkpoint, summarize
from scripts.refresh_ai_validation_reports import digest, load, verify_evidence, verify_bundle
from scripts.revalidate_all_grades import complete


class ProviderFailoverError(RuntimeError):
    def __init__(self, remaining_budget):
        super().__init__("provider failover stopped; technical details are in the local traceback")
        self.remaining_budget = remaining_budget


def select_provider(provider):
    exercise.set_provider(provider)
    os.environ["LLM_PROVIDER"] = provider


def archive_bytes(stage, raw):
    destination = stage / "history" / ("provider_" + hashlib.sha256(raw).hexdigest()[:20]) / "silver_labels.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists() and destination.read_bytes() != raw:
        raise ValueError("provider archive differs from immutable evidence")
    if not destination.exists():
        destination.write_bytes(raw)
    return destination


def activate_checkpoint(name, batch, provider):
    from app.services.exercise.workflow import batch_lock
    with batch_lock(exercise.paths(name, batch)["exercise"]):
        return _activate_checkpoint(name, batch, provider)


def _activate_checkpoint(name, batch, provider):
    """Keep completed decisions and their actual provider/model, including older models."""
    if exercise.VALIDATION_NAMESPACE != "failover":
        raise ValueError("provider failover requires its separate checkpoint namespace")
    select_provider(provider)
    settings = settings_for(provider)
    target = exercise.paths(name, batch)
    from app.services.exercise.workflow import require_validation
    require_validation(target["exercise"])
    grade, track = exercise.CLASSES[name]
    previous_path = target["checkpoint"] if target["checkpoint"].exists() else None
    if previous_path is None:
        candidates = []
        for legacy_provider in ("groq", "gemini"):
            legacy = exercise.paths(name, batch, provider=legacy_provider)
            if legacy["checkpoint"].exists():
                cp = load(legacy["checkpoint"])
                verify_evidence(legacy["source"], legacy["checkpoint"], grade)
                candidates.append((sum(complete(cp, [qid]) for qid in cp["items"]), legacy["checkpoint"]))
        if candidates:
            previous_path = max(candidates, key=lambda pair: pair[0])[1]
    exercise.stage_class(name, batch)
    if previous_path is None:
        cp = exercise.init_checkpoint(name, batch, 1)
        cp["providerFailover"] = {"enabled": True, "transitions": []}
        atomic_write(cp, target["checkpoint"])
        return cp
    source = previous_path.parent / "soal_exercise_db.json"
    verify_evidence(source, previous_path, grade)
    old_bytes, original = previous_path.read_bytes(), load(previous_path)
    if (previous_path == target["checkpoint"] and original["provider"] == provider
            and original["model"] == settings.model):
        return original
    if load(source) != load(target["source"]):
        raise ValueError("provider switching requires unchanged questions and order")
    if target["source"].read_bytes() != source.read_bytes():
        if target["checkpoint"].exists():
            raise ValueError("existing failover source checksum differs")
        target["source"].write_bytes(source.read_bytes())
    if (target["final"] / "manifest.json").exists():
        verify_bundle(source, target["final"])
    archived = archive_bytes(target["stage"], old_bytes)
    # A legacy checkpoint may already include an append-only source extension.
    # Carry its immutable old-source proofs into the failover staging directory.
    if source.parent.resolve() != target["stage"].resolve():
        for proof_source in source.parent.glob("history/source_extension_*/soal_exercise_db.json"):
            destination = target["stage"] / proof_source.relative_to(source.parent)
            destination.parent.mkdir(parents=True, exist_ok=True)
            if destination.exists() and destination.read_bytes() != proof_source.read_bytes():
                raise ValueError("source-extension proof differs during provider migration")
            if not destination.exists():
                destination.write_bytes(proof_source.read_bytes())
    # Construct a fresh active-provider header without reading/overwriting the old checkpoint.
    cp = load_checkpoint(target["stage"] / "unused_header.json", target["source"], digest(target["source"]),
                         settings.model, 1, grade, track=track, provider=provider)
    counts = Counter()
    for qid, record in original["items"].items():
        if not complete(original, [qid]):
            continue
        retained = deepcopy(record)
        if record.get("retainedProviderEvidence"):
            root = Path(record["retainedProviderEvidence"]["path"])
            if digest(root) != record["retainedProviderEvidence"]["sha256"]:
                raise ValueError("retained provider archive checksum differs")
            proof = archive_bytes(target["stage"], root.read_bytes())
        else:
            proof = archived
        actual_provider = record.get("provider", original["provider"])
        actual_model = record.get("model", original["model"])
        retained.update(provider=actual_provider, model=actual_model,
                        retainedProviderEvidence={"path": str(proof), "sha256": digest(proof)})
        cp["items"][qid] = retained
        counts[actual_provider] += 1
    event = {"at": datetime.now(timezone.utc).isoformat(), "fromProvider": original["provider"],
             "fromModel": original["model"], "toProvider": provider, "toModel": settings.model,
             "retainedItems": len(cp["items"]), "previousApiAttempts": original.get("apiAttempts", 0),
             "previousStopReason": original.get("stopReason"), "previousCheckpoint": str(archived),
             "previousCheckpointSha256": digest(archived)}
    events = list(original.get("providerFailover", {}).get("transitions", [])) + [event]
    cp["providerFailover"] = {"enabled": True, "transitions": events}
    cp["providerMigration"] = {**event, "retainedCompletedItems": len(cp["items"]),
                               "retainedProviderCounts": dict(counts), "newApiCalls": 0}
    cp.update(executionStatus="queued_provider_resume", apiAttempts=0, summary=summarize(cp))
    # Verify before committing, so a failed migration leaves the active checkpoint intact.
    candidate = target["stage"] / "candidate_silver_labels.json"
    atomic_write(cp, candidate)
    verify_evidence(target["source"], candidate, grade)
    atomic_write(cp, target["checkpoint"])
    return cp
