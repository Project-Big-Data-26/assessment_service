import hashlib
import json
from argparse import Namespace
from types import SimpleNamespace

import pytest

from app.llm.silver import build_silver_prompt, rubric_file_hash, silver_rubric
from app.llm.config import GeminiSettings
from app.llm.silver import SilverRunResult
from scripts import generate_silver_labels_kelas1 as generator
from scripts import generate_silver_labels_sma as batch_runner
from scripts.audit_grade_aware_pilot import audit
from tests.test_blind_pilot_audit import question, record
from tests.test_silver_grade import silver_output


@pytest.mark.parametrize("grade,topic", [(10, "trigonometri"), (11, "regresi"), (12, "anuitas")])
def test_sma_context_is_grade_specific_and_blind(grade, topic):
    item = question(f"q-{grade}")
    item.update(cognitive_level="reasoning", tingkat_kesulitan="Hard", agentDifficulty=5)
    prompt = build_silver_prompt(item, grade=grade)
    assert f"SMA kelas {grade}" in prompt and topic in prompt.lower()
    assert "maksimal 700 karakter" in prompt
    assert all(key not in prompt for key in ("cognitive_level", "tingkat_kesulitan", "agentDifficulty", "PREDIKSI INDOBERT"))
    assert silver_rubric(grade).education_level == "SMA"
    assert rubric_file_hash(grade) != rubric_file_hash(9)
    assert "Jenjang sasaran: SMP" not in prompt


@pytest.mark.parametrize("grade", [10, 11, 12])
def test_sma_resume_rejects_another_grade_rubric(tmp_path, monkeypatch, grade):
    monkeypatch.setattr(generator, "ROOT", tmp_path)
    source = tmp_path / "questions.json"
    source.write_text(json.dumps([question("q-sma")]), encoding="utf-8")
    source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    checkpoint = tmp_path / "silver.json"
    payload = generator.load_checkpoint(checkpoint, source, source_hash, "test-model", 3, grade)
    assert payload["educationLevel"] == "SMA" and payload["sourceGrade"] == grade
    checkpoint.write_text(json.dumps(payload), encoding="utf-8")
    assert generator.load_checkpoint(checkpoint, source, source_hash, "test-model", 3, grade) == payload
    other_grade = 12 if grade != 12 else 10
    payload["rubricHash"] = rubric_file_hash(other_grade)
    checkpoint.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(ValueError, match="rubric hash"):
        generator.load_checkpoint(checkpoint, source, source_hash, "test-model", 3, grade)


@pytest.mark.parametrize("grade", [10, 11, 12])
def test_sma_audit_rejects_a_junior_school_rubric(tmp_path, grade):
    item = question("q-sma")
    source = tmp_path / "questions.json"
    source.write_text(json.dumps([item]), encoding="utf-8")
    checkpoint = tmp_path / "silver.json"
    spec = silver_rubric(grade)
    payload = {
        "sourceGrade": grade, "sourceHash": hashlib.sha256(source.read_bytes()).hexdigest(),
        "promptVersion": spec.prompt_version, "rubricVersion": spec.version,
        "rubricHash": rubric_file_hash(grade), "items": {"q-sma": record(item)},
    }
    checkpoint.write_text(json.dumps(payload), encoding="utf-8")
    assert audit(source, checkpoint, grade=grade)["gates"]["promptAndRubricVersionMatch"]
    previous = silver_rubric(9)
    payload.update(promptVersion=previous.prompt_version, rubricVersion=previous.version, rubricHash=rubric_file_hash(9))
    checkpoint.write_text(json.dumps(payload), encoding="utf-8")
    result = audit(source, checkpoint, grade=grade)
    assert not result["gates"]["promptAndRubricVersionMatch"] and not result["readyForExpansion"]


def test_sma_batches_stop_after_shared_quota_and_queue_other_grades(tmp_path, monkeypatch):
    monkeypatch.setattr(generator, "ROOT", tmp_path)
    monkeypatch.setattr(batch_runner, "ROOT", tmp_path)
    for grade in (10, 11, 12):
        directory = tmp_path / f"kelas{grade}"
        directory.mkdir()
        (directory / "soal_pretest_db.json").write_text(json.dumps([question(f"q-{grade}")]), encoding="utf-8")
    calls = []

    def fake_run(command, **kwargs):
        calls.append(command)
        path = tmp_path / "kelas10/test-batch/silver_labels.json"
        payload = batch_runner.read(path)
        payload["executionStatus"] = "blocked_provider_daily_quota"
        payload["stopReason"] = {"errorCode": "ClientError:429", "quotaLimits": []}
        batch_runner.save(payload, path)
        return SimpleNamespace(returncode=3)

    monkeypatch.setattr(batch_runner.subprocess, "run", fake_run)
    assert batch_runner.run_batches(tmp_path, "test-batch", [10, 11, 12], model="test-model") == 3
    assert len(calls) == 1
    for grade in (11, 12):
        pending = batch_runner.read(tmp_path / f"kelas{grade}/test-batch/silver_labels.json")
        assert pending["executionStatus"] == "waiting_provider_daily_quota"
        assert pending["blockedByGrade"] == 10 and not pending["items"]
        assert pending["summary"]["successfulRuns"] == 0


def test_resume_clears_shared_block_pointer_and_preserves_paid_runs(tmp_path, monkeypatch):
    monkeypatch.setattr(generator, "ROOT", tmp_path)
    item = question("q-11")
    source = tmp_path / "questions.json"
    source.write_text(json.dumps([item]), encoding="utf-8")
    output = tmp_path / "silver.json"
    source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    checkpoint = generator.load_checkpoint(output, source, source_hash, "test-model", 3, 11)
    paid_runs = [SilverRunResult(
        runIndex=i, status="success", output=silver_output("Easy"), latencyMs=1,
    ).model_dump(mode="json") for i in (1, 2, 3)]
    checkpoint["items"] = {"q-11": {
        "index": 1, "questionId": "q-11", "inputHash": generator.input_hash(item),
        "runs": paid_runs, "aggregate": {}, "adjudication": None,
    }}
    checkpoint["executionStatus"] = "waiting_provider_daily_quota"
    checkpoint["blockedByGrade"] = 10
    checkpoint["stopReason"] = {"errorCode": "ClientError:429"}
    generator.atomic_write(checkpoint, output)
    monkeypatch.setattr(generator, "parse_args", lambda: Namespace(
        source=source, output=output, grade=11, runs=3, execute=True, limit=None,
        workers=1, attempts=1, pause=0, adjudicate=True,
    ))
    monkeypatch.setattr(generator.GeminiSettings, "from_environment", lambda: GeminiSettings(api_key="test-only-key", model="test-model"))
    # Any provider call would fail: all three paid runs are already present.
    monkeypatch.setattr(generator, "GeminiSilverAdapter", lambda settings: object())
    assert generator.main() == 0
    resumed = json.loads(output.read_text(encoding="utf-8"))
    assert "blockedByGrade" not in resumed and "stopReason" not in resumed
    assert resumed["executionStatus"] == "completed_batch"
    assert resumed["items"]["q-11"]["runs"] == paid_runs
