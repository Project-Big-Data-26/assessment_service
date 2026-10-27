"""Grade 11/12 regular and TL use distinct sources and never borrow pretest data."""
import json

import pytest

from app.llm.silver import silver_rubric
from scripts import nightly_pipeline as nightly
from scripts import validate_exercise_batch as exercise


@pytest.mark.parametrize("name,grade,track", [
    ("kelas11", 11, "regular"), ("kelas11_tl", 11, "tl"),
    ("kelas12", 12, "regular"), ("kelas12_tl", 12, "tl"),
])
def test_each_track_stages_exact_source_with_its_own_rubric(tmp_path, monkeypatch, name, grade, track):
    monkeypatch.setattr(exercise, "ROOT", tmp_path)
    assert exercise.CLASSES[name] == (grade, track)
    assert silver_rubric(grade, track=track).path.is_file()
    p = exercise.paths(name, "batch01")
    p["exercise"].mkdir(parents=True)
    row = {"_id": "q1", "kelas_id": name, "cognitive_level": None, "jawaban": "A", "image_url": []}
    (p["exercise"] / "soal_exercise_db.json").write_text(
        json.dumps({"book": name, "batch": 1, "items": [row]}), encoding="utf-8")
    (p["exercise"] / "soal_exercise_meta.json").write_text(
        json.dumps({"q1": {"batch": 1, "level_target": "easy"}}), encoding="utf-8")
    assert exercise.stage_class(name, "batch01") == [row]
    assert json.loads(p["source"].read_text(encoding="utf-8")) == [row]
    assert p["final"] == tmp_path / "output/exercise" / name / "batch01/hasil_validasi"
    other = ("kelas" + str(grade) + "_tl") if track == "regular" else ("kelas" + str(grade))
    assert exercise.paths(other, "batch01")["stage"] != p["stage"]


def test_available_defaults_ignore_absent_or_unpaired_sources_and_pretest(tmp_path, monkeypatch):
    monkeypatch.setattr(exercise, "ROOT", tmp_path)
    p = exercise.paths("kelas7", "batch01")["exercise"]
    p.mkdir(parents=True)
    (p / "soal_exercise_db.json").write_text("{}", encoding="utf-8")
    assert exercise.available_classes("batch01") == []
    (p / "soal_exercise_meta.json").write_text("{}", encoding="utf-8")
    pretest = tmp_path / "output/pretest/kelas11"
    pretest.mkdir(parents=True)
    (pretest / "soal_pretest_db.json").write_text("[]", encoding="utf-8")
    assert exercise.available_classes("batch01") == ["kelas7"]
    assert not (tmp_path / "output/exercise/kelas11").exists()


def test_missing_exercise_tracks_are_visible_without_blocking_existing_jobs(tmp_path, monkeypatch):
    monkeypatch.setattr(exercise, "ROOT", tmp_path)
    monkeypatch.setattr(nightly, "ROOT", tmp_path)
    config = {"classes": ["kelas7", "kelas11", "kelas12_tl"], "bootstrapJobs": []}
    jobs = [{"class": "kelas7", "batch": "batch01"}]
    pending = nightly.waiting_classes(config, jobs)
    assert [(entry["class"], entry["status"]) for entry in pending] == [
        ("kelas11", "waiting_for_source"), ("kelas12_tl", "waiting_for_source")]
    directory = exercise.paths("kelas11", "batch01")["exercise"]
    directory.mkdir(parents=True)
    for name in ("soal_exercise_db.json", "soal_exercise_meta.json"):
        (directory / name).write_text("{}", encoding="utf-8")
    assert nightly.waiting_classes(config, jobs)[0]["status"] == "waiting_for_ready"
    assert nightly.waiting_classes(config, jobs + [{"class": "kelas11", "batch": "batch01"}])[0]["class"] == "kelas12_tl"


@pytest.mark.parametrize("status,code", [
    ("blocked_provider_daily_quota", "ClientError:429"),
    ("blocked_provider_quota_or_rate_limit", "ClientError:429"),
    ("blocked_provider_temporarily_unavailable", "ConnectTimeout:0"),
])
def test_provider_stop_notice_keeps_reason_and_never_echoes_secrets(status, code):
    notice = nightly.provider_stop_notice({"executionStatus": status, "stopReason": {
        "errorCode": code, "providerFailureReason": "private", "api_key": "secret"}})
    assert notice["status"] == status and "checkpoint tersimpan" in notice["message"]
    assert "secret" not in json.dumps(notice) and "private" not in json.dumps(notice)
    assert nightly.provider_stop_notice({"executionStatus": "running"}) is None


def test_provider_error_code_is_redacted_when_it_contains_private_text():
    notice = nightly.provider_stop_notice({"executionStatus": "blocked_provider_configuration",
                                          "stopReason": {"errorCode": "API key=private"}})
    assert notice["errorCode"] == "provider_error"
