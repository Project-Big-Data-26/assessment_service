"""N=1 must save calls without inventing agreement or replacing paid N=3 evidence."""
import hashlib
import json
from pathlib import Path

import pytest

from app.llm.silver import SilverRunResult, aggregate_silver_runs, build_silver_prompt
from app.silver.exports import database_items
from app.silver.policy import validate_provenance
from scripts import export_revalidation_progress as exporter
from scripts import generate_silver_labels_kelas1 as generator
from scripts import validate_exercise_batch as exercise
from scripts.revalidate_all_grades import complete
from tests.test_blind_pilot_audit import question
from tests.test_revalidation_quota import setup_runner
from tests.test_silver_grade import silver_output


def run(index=1, output=None, original=None, grade=1):
    output = output or silver_output("Easy")
    prompt = build_silver_prompt(original or question("q1"), grade=grade)
    return SilverRunResult(runIndex=index, status="success", output=output, latencyMs=1,
        promptHash=hashlib.sha256(prompt.encode()).hexdigest(),
        responseHash=hashlib.sha256(output.model_dump_json().encode()).hexdigest())


def test_single_run_completes_without_adjudication_but_default_n3_stays_partial():
    evidence = [run()]
    assert aggregate_silver_runs(evidence)["needsAdjudication"]
    outcome = aggregate_silver_runs(evidence, requested_runs=1)
    assert outcome["needsAdjudication"] is False
    assert outcome["contentQualified"] is True
    assert outcome["eligibleForTraining"] is False
    assert outcome["heads"]["intendedDifficulty"]["status"] == "single_run"
    record = {"runs": [evidence[0].model_dump(mode="json")], "aggregate": outcome}
    assert complete({"requestedRuns": 1, "items": {"q1": record}}, ["q1"])
    assert not complete({"requestedRuns": 3, "items": {"q1": record}}, ["q1"])


@pytest.mark.parametrize("blocker", ["content", "key", "abstain"])
def test_single_run_blockers_finish_the_assessment_but_stay_inactive(tmp_path, blocker):
    output = silver_output("Easy")
    if blocker == "content":
        output = output.model_copy(update={"contentStatus": "concern", "contentConcerns": ["Ambiguous."]})
    elif blocker == "key":
        output = output.model_copy(update={"answerKeyStatus": "conflict", "verifiedAnswerKey": "A"})
    else:
        output = output.model_copy(update={"knowledgeDimension": output.knowledgeDimension.model_copy(
            update={"action": "abstain", "label": None})})
    evidence = run(output=output)
    record = {"runs": [evidence.model_dump(mode="json")], "adjudication": None}
    decision, progress = exporter.current_decision(question("q1"), record, tmp_path, requested_runs=1)
    assert progress["fullComplete"] and not progress["needsAdjudication"]
    assert decision["finalRouting"] != "silver_ready"
    original = {**question("q1"), "cognitive_level": None, "cognitive_score": None,
                "confidence_score": None, "status": None}
    assert database_items([original], [decision])[0]["status"] == "inactive"


def test_single_run_runner_makes_one_call_per_item_and_resume_reuses_it(tmp_path, monkeypatch):
    class Adapter:
        calls = []

        def label_once(self, item, paths, *, run_index, **kwargs):
            self.calls.append((item["_id"], run_index))
            return run(index=run_index, original=item)

        def adjudicate_once(self, *args, **kwargs):
            pytest.fail("N=1 must not call adjudication")

    adapter = Adapter()
    path = setup_runner(tmp_path, monkeypatch, adapter, runs=1)
    assert generator.main() == 0
    first = json.loads(path.read_text(encoding="utf-8"))
    assert adapter.calls == [("q1", 1), ("q2", 1)]
    assert complete(first, ["q1", "q2"])
    assert generator.main() == 0
    assert adapter.calls == [("q1", 1), ("q2", 1)]


def test_single_run_quota_stop_does_not_retry_or_visit_next_item(tmp_path, monkeypatch):
    class Adapter:
        calls = 0

        def label_once(self, *args, run_index, **kwargs):
            self.calls += 1
            return SilverRunResult(runIndex=run_index, status="failed", latencyMs=1,
                                   errorCode="ClientError:429", quotaDailyExhausted=True)

    adapter = Adapter()
    path = setup_runner(tmp_path, monkeypatch, adapter, runs=1)
    assert generator.main() == 3
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert adapter.calls == 1 and payload["apiAttempts"] == 1
    assert "q2" not in payload["items"]
    assert not complete(payload, ["q1"])


def test_migration_retains_n3_and_reuses_original_index_without_changing_response(tmp_path, monkeypatch):
    monkeypatch.setattr(exercise, "ROOT", tmp_path)
    monkeypatch.setattr(generator, "ROOT", tmp_path)
    p = exercise.paths("kelas5", "batch01")
    p["stage"].mkdir(parents=True)
    originals = [{**question(qid), "kelas_id": "kelas5", "cognitive_level": None,
                  "cognitive_score": None, "confidence_score": None, "status": None}
                 for qid in ("q1", "q2", "q3")]
    p["source"].write_text(json.dumps(originals), encoding="utf-8")
    payload = generator.load_checkpoint(p["checkpoint"], p["source"], exporter.digest(p["source"]), "test", 3, 5)
    payload["apiAttempts"] = 6
    for original, indices in zip(originals, [(1, 2, 3), (2, 3), ()]):
        evidence = [run(index, original=original, grade=5) for index in indices]
        payload["items"][original["_id"]] = {
            "questionId": original["_id"], "inputHash": generator.input_hash(original),
            "runs": [r.model_dump(mode="json") for r in evidence], "adjudication": None,
            "aggregate": aggregate_silver_runs(evidence)}
    payload["summary"] = generator.summarize(payload)
    p["checkpoint"].write_text(json.dumps(payload), encoding="utf-8")
    previous_bytes = p["checkpoint"].read_bytes()
    migrated = exercise.migrate_to_single_run("kelas5", "batch01")
    assert migrated["requestedRuns"] == 1
    assert migrated["items"]["q1"]["requestedRuns"] == 3
    for field in ("runs", "aggregate", "adjudication"):
        assert migrated["items"]["q1"][field] == payload["items"]["q1"][field]
    assert migrated["items"]["q2"]["requestedRunIndices"] == [2]
    assert migrated["items"]["q2"]["runs"] == payload["items"]["q2"]["runs"][:1]
    assert migrated["items"]["q2"]["previousN3Evidence"]["runs"] == payload["items"]["q2"]["runs"][1:]
    assert complete(migrated, ["q1", "q2"]) and not complete(migrated, ["q3"])
    assert exercise.migrate_to_single_run("kelas5", "batch01") == migrated
    assert migrated["apiAttempts"] == 6
    assert migrated["summary"]["totalTokens"] == payload["summary"]["totalTokens"]
    assert Path(migrated["runPolicyMigration"]["previousCheckpoint"]).read_bytes() == previous_bytes
    report = exporter.export_class(p["source"], p["checkpoint"], p["stage"], grade=5, track="regular")
    rows = exporter.read(p["stage"] / "validation_results.json")
    assert report["summary"]["finalItems"] == 2
    assert [r["confidence_score"] for r in rows] == [100, 0, 0]  # No model diagnostics in this progress fixture.
    assert [r["status"] for r in rows] == ["active", "active", "inactive"]
    assert rows[1]["cognitive_level"] == "easy"
    assert report["items"][1]["successfulRunIndices"] == [2]
    assert report["items"][1]["consistencyMeasured"] is False


def test_single_run_does_not_weaken_training_provenance():
    with pytest.raises(ValueError, match="three successful"):
        validate_provenance({"kind": "ai_silver", "contentStatus": "valid", "answerKeyStatus": "verified",
                             "successfulRuns": 1, "decisionId": "single"})
