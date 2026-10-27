from argparse import Namespace
from copy import deepcopy
import json
from pathlib import Path

import pytest

from app.llm import deepseek
from app.llm.silver import SilverRunResult, aggregate_silver_runs
from scripts import generate_silver_labels_kelas1 as generator
from scripts import nightly_pipeline as nightly
from scripts import validate_exercise_batch as exercise
from scripts.refresh_ai_validation_reports import digest, verify_evidence
from tests.test_blind_pilot_audit import question
from tests.test_single_run_exercise import run
from tests.test_nightly_pipeline import config


@pytest.fixture
def migration(tmp_path, monkeypatch):
    for module in (exercise, generator, nightly):
        monkeypatch.setattr(module, "ROOT", tmp_path)
    monkeypatch.setattr(exercise, "VALIDATION_PROVIDER", "gemini")
    monkeypatch.setenv("DEEPSEEK_API_KEY", "")
    monkeypatch.setenv("DEEPSEEK_MODEL", "deepseek-flash")
    monkeypatch.setenv("DEEPSEEK_LIVE_ENABLED", "false")
    p = exercise.paths("kelas8", "batch01")
    p["exercise"].mkdir(parents=True)
    rows = [{**question(qid), "kelas_id": "kelas8", "cognitive_level": None, "cognitive_score": None,
             "confidence_score": None, "status": None} for qid in ("q1", "q2", "q3")]
    generator.atomic_write({"book": "kelas8", "batch": 1, "items": rows}, p["exercise"] / "soal_exercise_db.json")
    generator.atomic_write({q["_id"]: {"batch": 1, "level_target": "easy", "bab_id": "SMP8-B1"}
                            for q in rows}, p["exercise"] / "soal_exercise_meta.json")
    exercise.stage_class("kelas8", "batch01")
    cp = generator.load_checkpoint(p["checkpoint"], p["source"], digest(p["source"]), "gemini-original", 1, 8)
    for original, count in zip(rows[:2], (3, 1)):
        evidence = [run(index, original=original, grade=8) for index in range(1, count + 1)]
        cp["items"][original["_id"]] = {"questionId": original["_id"], "inputHash": generator.input_hash(original),
            "requestedRuns": count, "runs": [r.model_dump(mode="json") for r in evidence], "adjudication": None,
            "aggregate": aggregate_silver_runs(evidence, requested_runs=count)}
    failed = SilverRunResult(runIndex=1, status="failed", latencyMs=1, errorCode="ServerError:503")
    cp["items"]["q3"] = {"questionId": "q3", "inputHash": generator.input_hash(rows[2]), "runs": [failed.model_dump(mode="json")],
                         "aggregate": aggregate_silver_runs([failed], requested_runs=1), "adjudication": None}
    cp.update(apiAttempts=11, summary=generator.summarize(cp))
    generator.atomic_write(cp, p["checkpoint"])
    before = p["checkpoint"].read_bytes()
    monkeypatch.setattr(exercise, "VALIDATION_PROVIDER", "deepseek")
    result = exercise.seed_from_gemini("kelas8", "batch01")
    return p, exercise.paths("kelas8", "batch01"), rows, before, result


def test_only_completed_decisions_are_seeded_with_immutable_provider_identity(migration):
    old, new, rows, before, result = migration
    cp = json.loads(new["checkpoint"].read_text(encoding="utf-8"))
    assert result["retainedItems"] == 2 and result["newApiCalls"] == 0
    assert cp["provider"] == "deepseek" and cp["model"] == "deepseek-flash" and cp.get("apiAttempts", 0) == 0
    assert set(cp["items"]) == {"q1", "q2"}
    assert all(item["provider"] == "gemini" for item in cp["items"].values())
    assert cp["items"]["q1"]["requestedRuns"] == 3
    assert old["checkpoint"].read_bytes() == before
    verify_evidence(new["source"], new["checkpoint"], 8)
    assert exercise.seed_from_gemini("kelas8", "batch01")["seeded"] is False


def test_resume_calls_deepseek_only_for_pending_items(migration, monkeypatch):
    old, new, rows, before, _ = migration
    retained = deepcopy(json.loads(new["checkpoint"].read_text(encoding="utf-8"))["items"])
    class Adapter:
        calls = []
        def label_once(self, item, paths, *, run_index, grade, **kwargs):
            self.calls.append(item["_id"])
            return run(run_index, original=item, grade=grade)
        def adjudicate_once(self, *args, **kwargs):
            pytest.fail("N=1 must not adjudicate")
    adapter = Adapter()
    monkeypatch.setattr(deepseek, "DeepSeekSilverAdapter", lambda *args, **kwargs: adapter)
    monkeypatch.setattr(generator, "parse_args", lambda: Namespace(
        source=new["source"], output=new["checkpoint"], provider="deepseek", grade=8, track="regular", runs=1,
        execute=True, limit=None, question_id=None, workers=1, attempts=2, pause=0, adjudicate=True,
        max_api_calls=10, stop_on_quota=True, stop_on_503=True, max_consecutive_provider_failures=3))
    assert generator.main() == 0 and generator.main() == 0
    assert adapter.calls == ["q3"]
    cp = json.loads(new["checkpoint"].read_text(encoding="utf-8"))
    assert all(cp["items"][qid] == item for qid, item in retained.items())
    assert cp["items"]["q3"]["provider"] == "deepseek"
    assert cp["apiAttempts"] == 1 and old["checkpoint"].read_bytes() == before
    verify_evidence(new["source"], new["checkpoint"], 8)


def test_modified_foreign_decision_is_rejected(migration):
    _, new, _, _, _ = migration
    cp = json.loads(new["checkpoint"].read_text(encoding="utf-8"))
    cp["items"]["q1"]["aggregate"]["contentStatus"] = "concern"
    generator.atomic_write(cp, new["checkpoint"])
    with pytest.raises(ValueError, match="retained paid decision was changed"):
        verify_evidence(new["source"], new["checkpoint"], 8)


def test_modified_archive_is_rejected(migration):
    _, new, _, _, _ = migration
    cp = json.loads(new["checkpoint"].read_text(encoding="utf-8"))
    Path(cp["providerMigration"]["previousCheckpoint"]).write_text("{}", encoding="utf-8")
    with pytest.raises(ValueError, match="checksum"):
        verify_evidence(new["source"], new["checkpoint"], 8)


def test_provider_checkpoint_cannot_be_opened_as_gemini(migration):
    _, new, _, _, _ = migration
    with pytest.raises(ValueError, match="provider differs"):
        generator.load_checkpoint(new["checkpoint"], new["source"], digest(new["source"]), "deepseek-flash", 1, 8)


@pytest.mark.parametrize("key,enabled,status", [("", "false", "waiting_for_credentials"),
    ("private-test-key", "false", "waiting_for_provider_enablement")])
def test_paid_calls_require_credentials_and_live_opt_in(migration, monkeypatch, key, enabled, status):
    _, new, _, _, _ = migration
    monkeypatch.setenv("DEEPSEEK_API_KEY", key)
    monkeypatch.setenv("DEEPSEEK_LIVE_ENABLED", enabled)
    monkeypatch.setattr(nightly.subprocess, "run", lambda *args, **kwargs: pytest.fail("unexpected paid call"))
    job = nightly.source_identity("kelas8", "batch01")
    result, budget = nightly.validate_job(job, {**config(), "provider": "deepseek"}, {}, 10, new["stage"])
    assert result["status"] == status and result["apiCallsThisRun"] == 0 and budget == 10
