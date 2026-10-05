from copy import deepcopy
import json
from pathlib import Path

import pytest

from scripts import validate_exercise_batch as exercise
from scripts.build_blind_validation_bundle import source_class_matches


@pytest.mark.parametrize("value,grade,track,expected", [
    (None, 1, "regular", True), (5, 5, "regular", True),
    ("kelas5", 5, "regular", True), ("kelas11_tl", 11, "tl", True),
    ("kelas12", 1, "regular", False), ("kelas11_tl", 11, "regular", False),
    ("kelas11", 11, "tl", False), (True, 1, "regular", False),
])
def test_class_identity_includes_exact_grade_and_track(value, grade, track, expected):
    assert source_class_matches(value, grade, track) is expected


def prepare(tmp_path, monkeypatch):
    monkeypatch.setattr(exercise, "ROOT", tmp_path)
    folder = tmp_path / "output/exercise/kelas5/batch01"
    folder.mkdir(parents=True)
    item = {"_id": "exercise-a", "kelas_id": "kelas5", "soal_text": "3 + 2",
            "image_url": [], "cognitive_level": None, "jawaban": "A"}
    envelope = {"book": "kelas5", "batch": 1, "items": [item]}
    meta = {"exercise-a": {"batch": 1, "level_target": "easy", "pembahasan": "3 + 2 = 5"}}
    for filename, payload in [("soal_exercise_db.json", envelope), ("soal_exercise_meta.json", meta)]:
        (folder / filename).write_text(json.dumps(payload), encoding="utf-8")
    return folder, envelope, meta


def test_staging_preserves_source_and_keeps_generator_metadata_out_of_labeling(tmp_path, monkeypatch):
    folder, envelope, meta = prepare(tmp_path, monkeypatch)
    before = {p.name: p.read_bytes() for p in folder.glob("*.json")}
    rows = exercise.stage_class("kelas5", "batch01")
    assert rows == envelope["items"]
    staged = exercise.paths("kelas5", "batch01")["source"]
    assert json.loads(staged.read_text(encoding="utf-8")) == envelope["items"]
    assert "level_target" not in staged.read_text(encoding="utf-8")
    assert "pembahasan" not in staged.read_text(encoding="utf-8")
    assert before == {p.name: p.read_bytes() for p in folder.glob("*.json")}
    exercise.paths("kelas5", "batch01")["checkpoint"].write_text("{}", encoding="utf-8")
    envelope["items"][0]["soal_text"] = "3 + 4"
    (folder / "soal_exercise_db.json").write_text(json.dumps(envelope), encoding="utf-8")
    with pytest.raises(ValueError, match="source changed"):
        exercise.stage_class("kelas5", "batch01")


def test_metadata_requires_one_to_one_source_identity(tmp_path, monkeypatch):
    folder, envelope, meta = prepare(tmp_path, monkeypatch)
    meta["unrelated"] = deepcopy(meta["exercise-a"])
    (folder / "soal_exercise_meta.json").write_text(json.dumps(meta), encoding="utf-8")
    with pytest.raises(AssertionError, match="meta/db mismatch"):
        exercise.stage_class("kelas5", "batch01")


@pytest.mark.parametrize("batch", ["../pretest", "batch01/other", "batch", "batch-1"])
def test_batch_paths_stay_inside_exercise(batch):
    with pytest.raises(ValueError):
        exercise.paths("kelas5", batch)


def test_quota_stops_phase_without_retrying_or_repeating_successes(tmp_path, monkeypatch):
    folder, envelope, meta = prepare(tmp_path, monkeypatch)
    exercise.stage_class("kelas5", "batch01")
    p = exercise.paths("kelas5", "batch01")
    p["checkpoint"].write_text(json.dumps({"items": {}, "apiAttempts": 9}), encoding="utf-8")
    calls = []

    def blocked(name, batch, extra, budget, output_tokens):
        calls.append((extra, budget, output_tokens))
        p["checkpoint"].write_text(json.dumps({"items": {}, "apiAttempts": 10,
                "executionStatus": "blocked_provider_daily_quota"}), encoding="utf-8")
        return 3

    monkeypatch.setattr(exercise, "run_labeler", blocked)
    assert exercise.label_phase("kelas5", "batch01", ["exercise-a"], 20, 4096) == (3, 19)
    assert calls == [([], 20, 4096)]


def test_invalid_responses_remain_drafts_after_bounded_retries(tmp_path, monkeypatch):
    folder, envelope, meta = prepare(tmp_path, monkeypatch)
    exercise.stage_class("kelas5", "batch01")
    p = exercise.paths("kelas5", "batch01")
    p["checkpoint"].write_text(json.dumps({"items": {}, "apiAttempts": 0}), encoding="utf-8")
    calls = []

    def invalid(name, batch, extra, budget, output_tokens):
        calls.append(budget)
        p["checkpoint"].write_text(json.dumps({"items": {}, "apiAttempts": len(calls),
                "executionStatus": "completed_batch"}), encoding="utf-8")
        return 0

    monkeypatch.setattr(exercise, "run_labeler", invalid)
    assert exercise.label_phase("kelas5", "batch01", ["exercise-a"], 20, 4096) == (5, 17)
    assert len(calls) == 3


def test_global_quota_stop_publishes_all_classes_without_next_live_call(monkeypatch):
    monkeypatch.setattr(exercise, "CLASSES", {"kelas5": (5, "regular"), "kelas7": (7, "regular")})
    monkeypatch.setattr(exercise, "stage_class", lambda *args: None)
    monkeypatch.setattr(exercise, "init_checkpoint", lambda *args: None)
    monkeypatch.setattr(exercise, "paths", lambda name, batch: {
        "source": Path(f"{name}/source.json"), "checkpoint": Path(f"{name}/checkpoint.json"), "exercise": Path(name)})
    monkeypatch.setattr(exercise, "load", lambda path: [{"_id": "a"}] if path.name == "source.json" else {"items": {}})
    monkeypatch.setattr(exercise, "pilot_ids", lambda *args: ["a"])
    calls, published = [], []

    def blocked(name, batch, ids, budget, max_output_tokens):
        calls.append(name)
        return 3, budget - 1

    monkeypatch.setattr(exercise, "label_phase", blocked)
    monkeypatch.setattr(exercise, "publish_progress", lambda names, batch: published.append((names, batch)))
    monkeypatch.setattr(exercise.sys, "argv", ["validate_exercise_batch.py", "run", "--execute"])
    assert exercise.main() == 3
    assert calls == ["kelas5"]
    assert published == [(["kelas5", "kelas7"], "batch01")]
