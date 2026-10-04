import hashlib
import json
import sqlite3

import pytest

from app.classification.v2.serializer import canonical_json_hash
from app.psychometrics.initialization import build_initialization_report, finalize_irt_sidecar, prepare_pilot_configs
from app.silver.exports import DATABASE_SCHEMA, LEVEL_POLICY, SCORE_POLICY
from app.training.v2.dataset import TrainingRow, build_snapshot


def validation_bundle(tmp_path, *, grade=11, track="regular"):
    bundle = tmp_path / f"bundle-{grade}-{track}"
    (bundle / "bukti_validasi").mkdir(parents=True)
    rows, decisions, metadata = [], [], {}
    for index, difficulty in enumerate(("Easy", "Medium", "Hard")):
        identifier = f"q{index}"
        active = difficulty != "Hard"
        rows.append({"_id": identifier, "cognitive_level": LEVEL_POLICY["mapping"][difficulty],
                     "cognitive_score": SCORE_POLICY["mapping"][difficulty],
                     "status": "active" if active else "inactive"})
        decisions.append({"questionId": identifier, "finalRouting": "silver_ready" if active else "needs_ai_review",
                          "llmAdvisory": {"rubricVersion": "new-rubric-v1",
                                          "advisoryLabels": {"intendedDifficulty": difficulty}}})
        metadata[identifier] = {"intended_difficulty": difficulty, "subject_track": track,
                                "question_version_id": f"{track}:{identifier}:v1" if active else None,
                                "content_hash": str(index) * 64 if active else None}
    validation = json.dumps(rows).encode()
    audit = json.dumps({"items": decisions}).encode()
    (bundle / "validation_results.json").write_bytes(validation)
    (bundle / "bukti_validasi" / "decision_audit.json").write_bytes(audit)
    manifest = {"outputs": {"validation_results.json": {"sha256": hashlib.sha256(validation).hexdigest()}},
                "databaseExport": {"schemaVersion": DATABASE_SCHEMA, "sourceClass": grade, "subjectTrack": track,
                    "metadataByQuestionId": metadata,
                    "decisionAudit": {"path": "bukti_validasi/decision_audit.json", "sha256": hashlib.sha256(audit).hexdigest()}}}
    (bundle / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    return bundle


def test_initialization_preserves_scores_does_not_create_database_or_fake_calibration(tmp_path):
    bundle = validation_bundle(tmp_path)
    original = (bundle / "validation_results.json").read_bytes()
    database = tmp_path / "missing" / "pilot.sqlite3"
    report = build_initialization_report(bundle, db_path=database)
    assert not database.exists() and not database.parent.exists()
    assert (bundle / "validation_results.json").read_bytes() == original
    assert report["irt"]["status"] == "waiting_for_data"
    assert report["irt"]["calibrated"] is False and report["irt"]["parameters"] is None
    assert [item["initialCognitiveScore"] for item in report["items"]] == [600, 1000, 1400]
    assert all(item["irt"] is None and item["empiricalDifficulty"] is None for item in report["items"])
    assert report["summary"]["activeDifficultyCounts"] == {"Easy": 1, "Medium": 1, "Hard": 0}
    assert report["readiness"]["passed"] is False
    assert report["requirements"]["minimumPersons"] == 100
    assert report["reportHash"] == canonical_json_hash({key: value for key, value in report.items() if key != "reportHash"})


def test_initialization_rejects_tampered_export_and_audit(tmp_path):
    bundle = validation_bundle(tmp_path)
    path = bundle / "validation_results.json"
    original = path.read_bytes()
    path.write_bytes(original + b" ")
    with pytest.raises(ValueError, match="validation results checksum"):
        build_initialization_report(bundle)
    path.write_bytes(original)
    audit = bundle / "bukti_validasi" / "decision_audit.json"
    audit.write_bytes(audit.read_bytes() + b" ")
    with pytest.raises(ValueError, match="decision audit checksum"):
        build_initialization_report(bundle)


def test_finalize_sidecar_updates_manifest_and_preserves_old_rubric_and_questions(tmp_path):
    bundle = validation_bundle(tmp_path)
    original = (bundle / "validation_results.json").read_bytes()
    report = finalize_irt_sidecar(bundle, db_path=tmp_path / "absent.sqlite3")
    evidence = (bundle / "bukti_validasi" / "irt_initialization.json").read_bytes()
    manifest = json.loads((bundle / "manifest.json").read_text())
    assert manifest["irtInitialization"]["sha256"] == hashlib.sha256(evidence).hexdigest()
    assert manifest["outputs"]["bukti_validasi/irt_initialization.json"]["bytes"] == len(evidence)
    assert manifest["irtInitialization"]["empiricalCalibrationPerformed"] is False
    assert report["rubricVersions"] == ["new-rubric-v1"]
    assert (bundle / "validation_results.json").read_bytes() == original
    # A second inspection remains valid after adding evidence to the manifest.
    assert build_initialization_report(bundle)["decisionAuditHash"] == report["decisionAuditHash"]


def test_event_inventory_separates_track_version_and_only_counts_completed_valid_responses(tmp_path):
    bundle = validation_bundle(tmp_path, track="tl")
    database = tmp_path / "pilot.sqlite3"
    with sqlite3.connect(database) as db:
        db.executescript("""CREATE TABLE assessments(id TEXT,document TEXT);
                            CREATE TABLE sessions(id TEXT,assessment_id TEXT,status TEXT);
                            CREATE TABLE responses(session_id TEXT,document TEXT);
                            CREATE TABLE snapshots(id TEXT);""")
        for track in ("regular", "tl"):
            assessment = {"grade": 11, "subjectTrack": track,
                          "items": [{"questionVersionId": f"{track}:q0:v1", "contentHash": "0" * 64}]}
            db.execute("INSERT INTO assessments VALUES (?,?)", (track, json.dumps(assessment)))
            db.execute("INSERT INTO sessions VALUES (?,?,?)", (track, track, "completed"))
            event = {"questionVersionId": f"{track}:q0:v1", "contentHash": "0" * 64,
                     "grade": 11, "subjectTrack": track, "validForAnalysis": True,
                     "scoringStatus": "scored", "isCorrect": True, "flags": []}
            db.execute("INSERT INTO responses VALUES (?,?)", (track, json.dumps(event)))
            if track == "tl":
                for update in ({"contentHash": "b" * 64}, {"isCorrect": None}, {"flags": ["rapid_guess_candidate"]}):
                    db.execute("INSERT INTO responses VALUES (?,?)", (track, json.dumps({**event, **update})))
                db.execute("INSERT INTO sessions VALUES ('incomplete','tl','active')")
                db.execute("INSERT INTO responses VALUES ('incomplete',?)", (json.dumps(event),))
    before = database.read_bytes()
    report = build_initialization_report(bundle, db_path=database)
    inventory = report["localResponseInventory"]
    assert database.read_bytes() == before
    assert inventory["completedSessions"] == 1 and inventory["matchingScoredEvents"] == 1
    assert inventory["matchingScoredEventsByVersion"] == {"tl:q0:v1": 1}
    assert inventory["matchingAssessments"][0]["assessmentId"] == "tl"
    assert report["irt"]["status"] == "analysis_required" and report["irt"]["calibrated"] is False
    assert report["crossGradeOrTrackPooling"] is False
    assert "subjectHash" not in json.dumps(report) and "isCorrect" not in json.dumps(report)


def test_pilot_preparation_keeps_grade_and_track_separate_without_registration():
    rows = []
    for grade, track in ((1, "regular"), (11, "regular"), (11, "tl"), (12, "tl")):
        identifier = f"g{grade}-{track}"
        rows.append(TrainingRow(questionId=identifier, questionVersionId=f"{identifier}:v1", contentVersion=1,
            contentHash=canonical_json_hash({"id": identifier}), sourceGroup=identifier, grade=grade, subjectTrack=track,
            topic="Bilangan", questionType="multiple_choice", stem="1 + 1 = ...",
            options=[{"label": "A", "text": "2"}, {"label": "B", "text": "3"}], verifiedMinimalSolution="1 + 1 = 2",
            mathCognitiveDomain="knowing", knowledgeDimension="procedural", intendedDifficulty="Easy", rubricVersion="new-rubric-v1",
            decisionProvenance={"decisionId": identifier, "kind": "ai_silver", "verifiedAnswerKey": "A", "successfulRuns": 3,
                "contentStatus": "valid", "answerKeyStatus": "verified", "checkpointHash": "a" * 64,
                "sourceInputHash": "b" * 64, "sourceResponseHashes": ["c" * 64] * 3}))
    snapshot = build_snapshot(rows, snapshot_id="pilot-test", minimum_per_class=0, minimum_train_per_class=0, required_grades=())
    result = prepare_pilot_configs(snapshot, run_id="20261005")
    assert result["status"] == "configured_not_registered" and result["studentResponsesCreated"] == 0
    configs = [entry["assessmentConfig"] for entry in result["assessments"]]
    assert {(config["grade"], config["subjectTrack"]) for config in configs} == {(1, "regular"), (11, "regular"), (11, "tl"), (12, "tl")}
    assert len({config["populationId"] for config in configs}) == 4
    assert all(len(config["questionVersionIds"]) == 1 for config in configs)
    with pytest.raises(ValueError, match="run_id"):
        prepare_pilot_configs(snapshot, run_id="../bad")
