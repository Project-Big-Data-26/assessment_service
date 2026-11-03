"""Publish a complete text batch to the scheduled validator, then reuse its lock."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

from app.services.exercise import config as C
from app.services.pretest.agentic import kurikulum


def mark_completed_export(base, book, batch, rows, meta, skipped):
    marker = base / "extraction_ready.json"
    marker.unlink(missing_ok=True)
    from .workflow import managed, validation_allowed
    if managed(base) and not validation_allowed(base):
        return False
    expected = set()
    for number in range(1, 40):
        chapter = kurikulum.get(book, number)
        if chapter:
            expected.update((chapter.bab_id, code, level)
                            for code, _ in chapter.subbab for level in C.LEVELS)
    actual = {(m["bab_id"], m["subbab_kode"], m["level_target"]) for m in meta.values()}
    ids = [str(row["_id"]) for row in rows]
    if (not expected or actual != expected or not rows or skipped
            or len(ids) != len(set(ids)) or set(ids) != set(meta)
            or any(row.get("image_url") for row in rows)):
        return False
    payload = {"schemaVersion": "extraction-ready-v1", "class": book,
               "batch": f"batch{batch:02d}", "completedAt": datetime.now(timezone.utc).isoformat(),
               "sourceSha256": hashlib.sha256((base / "soal_exercise_db.json").read_bytes()).hexdigest(),
               "metadataSha256": hashlib.sha256((base / "soal_exercise_meta.json").read_bytes()).hexdigest()}
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=base,
                                     prefix=".ready-", suffix=".tmp", delete=False) as stream:
        temporary = Path(stream.name)
        json.dump(payload, stream, ensure_ascii=False, indent=2)
    try:
        os.replace(temporary, marker)
    finally:
        temporary.unlink(missing_ok=True)
    return True


def run_validation():
    root = Path(C.OUT_ROOT).resolve().parent.parent
    # The nightly runner prevents concurrent validation and reuses paid results.
    return subprocess.run([sys.executable, "-X", "utf8", str(root / "scripts/nightly_pipeline.py"),
                           "run", "--execute"], cwd=root).returncode
