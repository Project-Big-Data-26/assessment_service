import json
import sqlite3
from types import SimpleNamespace

import pytest

from app.assessment.store import AssessmentStore
from app.classification.v2.serializer import canonical_json_hash
from scripts import empirical_finetuning as feedback
from tests.test_assessment_empirical_flow import silver_snapshot


def empirical_labels(base):
    row = base.rows[0]
    return {"assessmentId": "pilot-1", "populationId": "school-1", "assessmentFamily": "math-1",
            "grade": 1, "snapshotId": "psy-1", "snapshotHash": "a" * 64,
            "items": [{"questionVersionId": row.questionVersionId, "contentHash": row.contentHash,
                       "intendedDifficulty": row.intendedDifficulty.value, "empiricalDifficulty": "Hard",
                       "difficultySource": "irt", "action": "retain"}]}


def test_empirical_targets_preserve_base_splits_cognitive_labels_and_history():
    base = silver_snapshot()
    original = base.model_dump_json()
    snapshot, report = feedback.prepare_snapshot(base, empirical_labels(base), set())
    assert report["changedLabels"] == 1
    assert snapshot.rows[0].intendedDifficulty.value == "Hard"
    assert base.model_dump_json() == original
    assert snapshot.rows[0].mathCognitiveDomain == base.rows[0].mathCognitiveDomain
    assert snapshot.rows[0].knowledgeDimension == base.rows[0].knowledgeDimension
    assert snapshot.splitManifest == base.splitManifest
    assert snapshot.researchOnly and snapshot.labelProvenance.startswith("irt_empirical")
    assert report["gateFailures"]  # Sparse pilot cannot silently train.
    with pytest.raises(Exception, match="qualified AI silver"):
        AssessmentStore.validate_snapshot(snapshot)


@pytest.mark.parametrize("key,value", [("contentHash", "wrong"), ("intendedDifficulty", "Easy")])
def test_wrong_version_or_initial_label_is_rejected(key, value):
    base = silver_snapshot()
    labels = empirical_labels(base)
    labels["items"][0][key] = value
    with pytest.raises(ValueError, match="immutable training content"):
        feedback.prepare_snapshot(base, labels, set())


@pytest.mark.parametrize("field,value", [("difficultySource", "intended"), ("action", "needs_ai_review")])
def test_unqualified_targets_do_not_relabel(field, value):
    base = silver_snapshot()
    labels = empirical_labels(base)
    labels["items"][0][field] = value
    assert feedback.prepare_snapshot(base, labels, set())[0] is None


def test_held_items_are_excluded_and_population_has_separate_identity():
    base = silver_snapshot()
    labels = empirical_labels(base)
    assert feedback.prepare_snapshot(base, labels, {base.rows[0].questionVersionId})[0] is None
    first, _ = feedback.prepare_snapshot(base, labels, {base.rows[1].questionVersionId})
    assert base.rows[1].questionVersionId not in {row.questionVersionId for row in first.rows}
    labels["populationId"] = "school-2"
    second, _ = feedback.prepare_snapshot(base, labels, {base.rows[1].questionVersionId})
    assert second.snapshotId != first.snapshotId


def test_repeated_evidence_with_same_targets_is_same_training_identity():
    base = silver_snapshot()
    labels = empirical_labels(base)
    first, _ = feedback.prepare_snapshot(base, labels, set())
    labels["snapshotId"] = "psy-new"
    labels["snapshotHash"] = "b" * 64
    second, _ = feedback.prepare_snapshot(base, labels, set())
    assert first.snapshotId == second.snapshotId
    assert first.snapshotHash != second.snapshotHash
    assert feedback.target_identity(first) == feedback.target_identity(second)


@pytest.fixture
def stored(tmp_path):
    path = tmp_path / "assessment.sqlite3"
    store = AssessmentStore(path)
    base = silver_snapshot()
    store.register_snapshot(base)
    row = base.rows[0]
    assessment = {"assessmentId": "pilot-1", "snapshotId": base.snapshotId,
        "snapshotHash": base.snapshotHash, "populationId": "school-1", "assessmentFamily": "math-1", "grade": 1}
    analysis = {"assessmentId": "pilot-1", "populationId": "school-1", "assessmentFamily": "math-1",
        "grade": 1, "dataOrigin": "server_scored", "readiness": {"passed": True},
        "irt": {"status": "estimated"}, "policyHash": "policy",
        "items": [{"questionId": row.questionId, "questionVersionId": row.questionVersionId,
            "contentHash": row.contentHash, "intendedDifficulty": "Medium",
            "irt": {"empiricalDifficulty": "Hard"}, "recommendedRouting": "observation_only", "reviewFlags": []}]}
    analysis["snapshotHash"] = canonical_json_hash(analysis)
    analysis.update(snapshotId="psy-1", createdAt="2026-11-03T00:00:00Z")
    with store.connection() as db:
        db.execute("INSERT INTO assessments VALUES (?,?,?)", ("pilot-1", "hash", json.dumps(assessment)))
        db.execute("INSERT INTO snapshots VALUES (?,?,?,?,?)", ("psy-1", analysis["snapshotHash"], "pilot-1", "now", json.dumps(analysis)))
        AssessmentStore._automated_decisions(db, analysis)
    db = sqlite3.connect(path)
    yield tmp_path, db
    db.close()


def test_sparse_data_writes_version_but_never_trains(stored, monkeypatch):
    root, db = stored
    monkeypatch.setattr(feedback.subprocess, "run", lambda *a, **k: pytest.fail("sparse data must wait"))
    result = feedback.process_assessment(db, "pilot-1", "psy-1", {"enabled": True}, root / "output", root)
    assert result["status"] == "waiting_for_training_data"
    assert result["productionModelUpdated"] is False
    assert list((root / "output").glob("*/snapshot.json"))


def test_qualified_training_runs_once_and_reuses_verified_model(stored, monkeypatch):
    root, db = stored
    monkeypatch.setattr(feedback, "validate_split_minimums", lambda *a, **k: [])
    calls = []
    monkeypatch.setattr(feedback.subprocess, "run", lambda command, **k: calls.append(command) or SimpleNamespace(returncode=0))
    from app.classification.v2 import artifact
    def manifest(path):
        snapshot = json.loads((path.parent / "snapshot.json").read_text())
        return SimpleNamespace(datasetHash=snapshot["snapshotHash"], researchOnly=True, metrics={"validation": {}})
    monkeypatch.setattr(artifact, "load_and_verify_manifest", manifest)
    options = {"enabled": True, "epochs": 3}
    result = feedback.process_assessment(db, "pilot-1", "psy-1", options, root / "output", root)
    assert result["status"] == "trained" and len(calls) == 1
    assert "app.training.v2.train_lora" in calls[0]
    again = feedback.process_assessment(db, "pilot-1", "psy-1", options, root / "output", root)
    assert again["reused"] and len(calls) == 1


def test_without_student_data_no_training_is_started(tmp_path, monkeypatch):
    monkeypatch.delenv("ASSESSMENT_DB_PATH", raising=False)
    monkeypatch.setattr(feedback.subprocess, "run", lambda *a, **k: pytest.fail("no student data"))
    result = feedback.run_feedback({"empiricalFineTuning": {"enabled": True}}, {}, tmp_path / "out", tmp_path)
    assert result["status"] == "waiting_for_qualified_irt"
    assert not (tmp_path / "out").exists()
