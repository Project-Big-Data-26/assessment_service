import json

from app.llm.silver import silver_rubric
from scripts import nightly_pipeline as nightly
from scripts import validate_exercise_batch as exercise


def test_grade6_stages_its_own_exercise_source_and_rubric(tmp_path, monkeypatch):
    monkeypatch.setattr(exercise, "ROOT", tmp_path)
    assert exercise.CLASSES["kelas6"] == (6, "regular")
    assert silver_rubric(6).path.is_file()
    paths = exercise.paths("kelas6", "batch01")
    paths["exercise"].mkdir(parents=True)
    item = {"_id": "grade6-q1", "kelas_id": "kelas6", "soal_text": "2 + 3", "jawaban": "A", "cognitive_level": None, "image_url": []}
    (paths["exercise"] / "soal_exercise_db.json").write_text(json.dumps({"book": "kelas6", "batch": 1, "items": [item]}), encoding="utf-8")
    (paths["exercise"] / "soal_exercise_meta.json").write_text(json.dumps({"grade6-q1": {"batch": 1, "level_target": "easy"}}), encoding="utf-8")
    assert exercise.stage_class("kelas6", "batch01") == [item]
    assert exercise.available_classes("batch01") == ["kelas6"]
    assert json.loads(paths["source"].read_text(encoding="utf-8")) == [item]


def test_discovery_retains_requested_queue_priority(tmp_path, monkeypatch):
    monkeypatch.setattr(nightly, "ROOT", tmp_path)
    order = ["kelas6", "kelas10", "kelas11_tl"]
    monkeypatch.setattr(nightly, "source_identity", lambda name, batch: {"class": name, "batch": batch})
    jobs, errors = nightly.discover_jobs({"classes": order, "bootstrapJobs": [{"class": name, "batch": "batch01"} for name in order]})
    assert errors == []
    assert [job["class"] for job in jobs] == order
