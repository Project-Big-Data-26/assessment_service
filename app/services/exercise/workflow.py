"""Durable, hash-bound generation/validation phases for new exercise batches.

Legacy batches without generation_state.json keep their existing resume contract.
Managed batches fail closed, including when a stale extraction marker exists.
"""
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import tempfile
import time


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def atomic_json(path, payload):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(payload, ensure_ascii=False, indent=2)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                     prefix=".write-", suffix=".tmp", delete=False) as stream:
        temporary = Path(stream.name)
        stream.write(encoded)
    for attempt in range(6):
        try:
            os.replace(temporary, path)
            return
        except PermissionError as exc:
            if getattr(exc, "winerror", None) not in (5, 32, 33) or attempt == 5:
                # Keep the complete uniquely named file for recovery. Never
                # overwrite another writer's temporary checkpoint.
                raise
            time.sleep(0.1 * 2 ** attempt)


@contextmanager
def batch_lock(base):
    """Cross-process lock shared by generation, approval, export and validation."""
    base = Path(base)
    base.mkdir(parents=True, exist_ok=True)
    with (base / ".workflow.lock").open("a+b") as stream:
        if not stream.tell():
            stream.write(b"0")
            stream.flush()
        stream.seek(0)
        try:
            if os.name == "nt":
                import msvcrt
                msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            raise RuntimeError("another generation/export/validation owns this exercise batch") from None
        try:
            yield
        finally:
            stream.seek(0)
            if os.name == "nt":
                msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(stream, fcntl.LOCK_UN)


def managed(base):
    base = Path(base)
    return any((base / name).exists() for name in
               ("generation_state.json", "generation_manifest.json", "generation_plan.json"))


def begin_generation(base, book, batch):
    base = Path(base)
    if not managed(base) and any((base / name).exists() for name in
                                ("soal_exercise_db.json", "hasil_validasi", "extraction_ready.json")):
        raise ValueError("generation-only requires a new batch; existing exports/evidence are preserved")
    state_path = base / "generation_state.json"
    if state_path.exists():
        state = load(state_path)
        if state.get("class") != book or state.get("batch") != f"batch{batch:02d}":
            raise ValueError("generation batch identity mismatch")
        if state.get("phase") == "validation_authorized":
            raise ValueError("generation is frozen after validation approval; use a new batch")
    # This guard is committed BEFORE any candidate or asset is written.
    atomic_json(state_path, {"schemaVersion": "exercise-generation-state-v1", "class": book,
        "batch": f"batch{batch:02d}", "phase": "generating", "validationStatus": "validation_pending",
        "updatedAt": datetime.now(timezone.utc).isoformat()})
    (base / "extraction_ready.json").unlink(missing_ok=True)
    (base / "validation_authorization.json").unlink(missing_ok=True)


def safe_asset(base, reference):
    base = Path(base).resolve()
    if not isinstance(reference, str) or Path(reference).is_absolute() or ":" in reference or "\\" in reference:
        raise ValueError("asset reference must be relative to the exercise batch")
    path = (base / reference).resolve()
    if not path.is_relative_to(base) or not path.is_file():
        raise ValueError("asset is missing or outside the exercise batch")
    if path.suffix.lower() not in (".png", ".jpg", ".jpeg", ".webp"):
        raise ValueError("validation assets must be PNG/JPEG/WebP")
    return path


def current_files(base):
    base = Path(base)
    envelope = load(base / "soal_exercise_db.json")
    metadata = load(base / "soal_exercise_meta.json")
    items = envelope["items"]
    ids = [str(row["_id"]) for row in items]
    if not items or len(ids) != len(set(ids)) or set(ids) != set(metadata):
        raise ValueError("generation master and metadata must contain the same unique nonempty IDs")
    files = {name: digest(base / name) for name in ("soal_exercise_db.json", "soal_exercise_meta.json")}
    for row in items:
        for reference in row.get("image_url") or []:
            files[reference] = digest(safe_asset(base, reference))
    # Also bind raw candidates, semantic specs, renderer source and allocation.
    for pattern in ("bab*/*.json", "assets/*", "generation_plan.json"):
        for path in sorted(base.glob(pattern)):
            if path.name.endswith((".blind.json", ".solver.json", ".verifikasi.json", ".tanpagambar.json")):
                continue
            files[path.relative_to(base).as_posix()] = digest(path)
    return files, envelope, metadata


def finish_generation(base, *, complete, problems=None):
    base = Path(base)
    state = load(base / "generation_state.json")
    if state.get("phase") == "validation_authorized":
        raise ValueError("approved generation cannot be rewritten")
    files, envelope, meta = current_files(base)
    if envelope.get("book") != state["class"] or envelope.get("batch") != int(state["batch"][5:]):
        raise ValueError("master generation identity mismatch")
    counts = {level: sum(m.get("level_target") == level for m in meta.values())
              for level in ("easy", "medium", "hard")}
    manifest = {"schemaVersion": "exercise-generation-manifest-v1", "class": state["class"],
        "batch": state["batch"], "complete": bool(complete and not problems),
        "questionCount": len(envelope["items"]), "visualQuestions": sum(bool(r.get("image_url")) for r in envelope["items"]),
        "targetDifficultyDistribution": counts, "files": files, "problems": problems or []}
    atomic_json(base / "generation_manifest.json", manifest)
    state.update(phase="generation_complete" if manifest["complete"] else "generation_incomplete",
                 validationStatus="validation_pending", manifestSha256=digest(base / "generation_manifest.json"))
    atomic_json(base / "generation_state.json", state)
    (base / "extraction_ready.json").unlink(missing_ok=True)
    (base / "validation_authorization.json").unlink(missing_ok=True)
    return {**manifest, "manifestSha256": state["manifestSha256"], "validationStatus": "validation_pending"}


def verify_generation(base):
    base = Path(base)
    state = load(base / "generation_state.json")
    manifest = load(base / "generation_manifest.json")
    checksum = digest(base / "generation_manifest.json")
    if (state.get("phase") not in ("generation_complete", "validation_authorized")
            or state.get("manifestSha256") != checksum or manifest.get("complete") is not True
            or any(manifest.get(k) != state.get(k) for k in ("class", "batch"))):
        raise ValueError("generation is incomplete or its manifest differs")
    files, _, _ = current_files(base)
    if files != manifest.get("files"):
        raise ValueError("generation text/assets changed; use a new batch and new approval")
    return checksum


def reference_manifest_paths(base, manifest):
    """Resolve question files in the batch and audit files within the project."""
    base = Path(base).resolve()
    paths = {}
    for name in manifest.get("files", {}):
        path = (base / name).resolve()
        if Path(name).is_absolute() or not path.is_relative_to(base):
            raise ValueError("reference question file is outside its batch")
        paths[name] = path
    if manifest.get("auditFiles"):
        project = base.parents[3]
        for name in manifest["auditFiles"]:
            path = (project / name).resolve()
            if Path(name).is_absolute() or ".." in Path(name).parts or not path.is_relative_to(project):
                raise ValueError("reference audit file is outside the project")
            paths["audit:" + name] = path
    return paths


def reference_manifest_intact(base, manifest):
    checksums = {**manifest.get("files", {}),
                 **{"audit:" + key: value for key, value in manifest.get("auditFiles", {}).items()}}
    return all(digest(path) == checksums[key] for key, path in reference_manifest_paths(base, manifest).items())


def require_validation(base):
    base = Path(base)
    hold = base / "reference_replenishment_state.json"
    if hold.exists():
        state = load(hold)
        manifest = base / "reference_replenishment_manifest.json"
        if state.get("phase") != "validation_authorized" or not manifest.exists():
            raise ValueError("validation_pending: batch01 reference additions are generation-only")
        if state.get("manifestSha256") != digest(manifest):
            raise ValueError("reference addition manifest changed")
        if not reference_manifest_intact(base, load(manifest)):
            raise ValueError("reference addition files changed after approval")
    if not managed(base):
        return  # Existing paid legacy batches are unaffected.
    checksum = verify_generation(base)
    approval = load(base / "validation_authorization.json") if (base / "validation_authorization.json").exists() else {}
    state = load(base / "generation_state.json")
    if (state.get("phase") != "validation_authorized" or approval.get("manifestSha256") != checksum
            or any(approval.get(k) != state.get(k) for k in ("class", "batch"))):
        raise ValueError("validation_pending: explicit hash-bound validation approval is required")


def validation_allowed(base):
    try:
        require_validation(base)
        return True
    except (ValueError, OSError, KeyError, TypeError):
        return False


def approve_validation(base, expected_hash):
    base = Path(base)
    with batch_lock(base):
        hold = base / "reference_replenishment_state.json"
        if hold.exists():
            manifest = base / "reference_replenishment_manifest.json"
            state = load(hold)
            if (state.get("phase") != "generation_complete" or not manifest.exists()
                    or digest(manifest) != expected_hash
                    or state.get("manifestSha256") != expected_hash
                    or not reference_manifest_intact(base, load(manifest))):
                raise ValueError("reference addition approval must match a complete immutable manifest")
            state.update(phase="validation_authorized", validationStatus="validation_authorized")
            atomic_json(hold, state)
            return {**state, "newApiCalls": 0}
        checksum = verify_generation(base)
        if expected_hash != checksum:
            raise ValueError("approval must match the current generation manifest SHA256")
        state = load(base / "generation_state.json")
        atomic_json(base / "validation_authorization.json", {"schemaVersion": "exercise-validation-approval-v1",
            "class": state["class"], "batch": state["batch"], "manifestSha256": checksum,
            "approvedAt": datetime.now(timezone.utc).isoformat()})
        state.update(phase="validation_authorized", validationStatus="validation_authorized")
        atomic_json(base / "generation_state.json", state)
        return {"class": state["class"], "batch": state["batch"], "manifestSha256": checksum,
                "phase": "validation_authorized", "newApiCalls": 0}
