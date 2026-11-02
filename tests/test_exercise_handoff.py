import json
from types import SimpleNamespace

import pytest

from app.services.exercise import handoff
from scripts import nightly_pipeline as nightly


@pytest.fixture
def exported(tmp_path, monkeypatch):
    chapter = SimpleNamespace(bab_id="SMP7-B1", subbab=[("A", "Numbers")])
    monkeypatch.setattr(handoff.kurikulum, "get", lambda book, n: chapter if n == 1 else None)
    rows = [{"_id": level, "image_url": []} for level in handoff.C.LEVELS]
    meta = {level: {"bab_id": chapter.bab_id, "subbab_kode": "A", "level_target": level}
            for level in handoff.C.LEVELS}
    (tmp_path / "soal_exercise_db.json").write_text(json.dumps({"items": rows}), encoding="utf-8")
    (tmp_path / "soal_exercise_meta.json").write_text(json.dumps(meta), encoding="utf-8")
    return tmp_path, rows, meta


def test_complete_export_produces_hash_verified_handoff(exported):
    base, rows, meta = exported
    assert handoff.mark_completed_export(base, "kelas7", 2, rows, meta, [])
    ready = json.loads((base / "extraction_ready.json").read_text())
    assert ready["batch"] == "batch02"
    assert ready["sourceSha256"] == nightly.digest(base / "soal_exercise_db.json")
    assert ready["metadataSha256"] == nightly.digest(base / "soal_exercise_meta.json")
    assert not list(base.glob(".ready-*.tmp"))


@pytest.mark.parametrize("problem", ["missing_level", "skipped", "images", "duplicate"])
def test_incomplete_or_unsupported_export_removes_stale_marker(exported, problem):
    base, rows, meta = exported
    (base / "extraction_ready.json").write_text("stale")
    skipped = []
    if problem == "missing_level":
        meta.pop("hard")
        rows.pop()
    elif problem == "skipped":
        skipped = ["invalid source"]
    elif problem == "images":
        rows[0]["image_url"] = ["image.png"]
    else:
        rows.append(rows[0])
    assert not handoff.mark_completed_export(base, "kelas7", 2, rows, meta, skipped)
    assert not (base / "extraction_ready.json").exists()


def test_queue_only_finalizes_complete_books(monkeypatch):
    from scripts import run_exercise_queue as queue
    from app.services.exercise import export
    monkeypatch.setattr(queue, "antrean", lambda books, batch, lengkapi: [] if books == ["kelas7"] else ["pending"])
    exported = []
    monkeypatch.setattr(export, "export_batch", lambda book, batch: exported.append(book) or {"ready_for_validation": True})
    calls = []
    monkeypatch.setattr(handoff, "run_validation", lambda: calls.append(True) or 0)
    assert queue.finalize_books(["kelas7", "kelas8"], 1) == 0
    assert exported == ["kelas7"] and calls == [True]
