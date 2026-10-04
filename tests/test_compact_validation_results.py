"""Compact exports preserve identity, adjudicated labels and auditable evidence."""
from copy import deepcopy
import json

import pytest

from app.silver.exports import (AUDIT_FILE, COMPACT_SCHEMA, compact_items, database_items,
                               load_decision_bundle)
from scripts.refresh_ai_validation_reports import digest, verify_bundle
from scripts.compact_validation_results import compact_bundle


def fixture_data():
    source = [{"_id": "q1", "soal_text": "Hitung benda", "jawaban": "A",
               "options": [{"option_id": "A", "text": "6"}], "kelas_id": 1,
               "cognitive_level": "applying", "cognitive_score": None,
               "confidence_score": .999, "status": None}]
    labels = {"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}
    decisions = [{"questionId": "q1", "decisionId": "d1", "finalRouting": "silver_ready",
                  "llmAdvisory": {"advisoryLabels": labels, "requestedRuns": 3,
                                  "runs": [{"runIndex": i, "status": "success", "heads": {
                                      h: {"action": "classify", "label": label} for h, label in labels.items()}}
                                           for i in (1, 2, 3)]}}]
    questions = [{"questionId": "q1", "stem": "Hitung benda", "options": [{"label": "A", "text": "6"}], "grade": 1}]
    cp = {"items": {"q1": {"aggregate": {"verifiedMinimalSolution": "Ada 6 benda.", "visualTranscript": None}}}}
    return source, decisions, questions, cp


def test_final_adjudicated_labels_replace_diagnostics_without_fabricated_scores():
    data = fixture_data()
    source_before = deepcopy(data[0])
    row = compact_items(*data, "kelas1")[0]
    assert row["cognitive_level"] == "knowing"
    assert row["ai_metadata"]["knowledge_dimension"] == "procedural"
    assert row["cognitive_score"] is None and row["confidence_score"] is None
    assert row["ai_metadata"]["question_version_id"].startswith("kelas1:q1:silver:")
    assert data[0] == source_before


def test_held_items_have_no_delivery_version_and_tl_identity_is_distinct():
    data = fixture_data()
    regular = compact_items(*data, "kelas1")[0]
    data[3]["subjectTrack"] = "tl"
    tl = compact_items(*data, "kelas11_tl")[0]
    assert regular["ai_metadata"]["content_hash"] != tl["ai_metadata"]["content_hash"]
    data[1][0]["finalRouting"] = "revision_required"
    held = compact_items(*data, "kelas11_tl")[0]
    assert held["ai_metadata"]["question_version_id"] is None
    assert held["ai_metadata"]["content_hash"] is None


def test_audit_tampering_is_rejected_and_legacy_bundles_still_load(tmp_path):
    old = {"items": [{"questionId": "q1"}]}
    path = tmp_path / "validation_results.json"
    path.write_text(json.dumps(old), encoding="utf-8")
    assert load_decision_bundle(tmp_path) == old
    audit = tmp_path / AUDIT_FILE
    audit.parent.mkdir()
    audit.write_text(json.dumps(old), encoding="utf-8")
    path.write_text(json.dumps({"schemaVersion": COMPACT_SCHEMA,
                               "decisionAudit": {"path": AUDIT_FILE, "sha256": digest(audit)}}), encoding="utf-8")
    assert load_decision_bundle(tmp_path) == old
    audit.write_text("{}", encoding="utf-8")
    with pytest.raises(ValueError, match="checksum"):
        load_decision_bundle(tmp_path)


def test_conversion_is_idempotent_and_resealed_label_changes_are_rejected(tmp_path):
    sources, decisions, questions, cp = fixture_data()
    questions[0].update(privateAnswerSpecification={"answerKey": "A"}, visualAssets=[], visualAssetHashes={})
    source = tmp_path / "soal_pretest_db.json"
    checkpoint = tmp_path / "checkpoint.json"
    bundle = tmp_path / "hasil_validasi"
    bundle.mkdir()
    audit = {"createdAt": "2026-10-04", "sourceClass": 1,
             "summary": {"itemCount": 1, "routingCounts": {"silver_ready": 1}}, "items": decisions}
    payloads = {source: sources, checkpoint: cp, bundle / "validation_results.json": audit,
                bundle / "questions.json": {"items": questions},
                bundle / "difficulty_groups.json": {"groups": {"Easy": [{"question": questions[0]}]}}}
    for path, payload in payloads.items():
        path.write_text(json.dumps(payload), encoding="utf-8")
    (bundle / "README.md").write_text("Report\n", encoding="utf-8")
    manifest = {"sourceFiles": {"source": {"path": str(source), "sha256": digest(source)},
                                "blindCheckpoint": {"path": str(checkpoint), "sha256": digest(checkpoint)}},
                "outputs": {p.name: {"sha256": digest(p), "bytes": p.stat().st_size} for p in bundle.iterdir()}}
    manifest_path = bundle / "manifest.json"
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    audit_bytes = (bundle / "validation_results.json").read_bytes()
    compact_bundle(source, bundle)
    assert (bundle / AUDIT_FILE).read_bytes() == audit_bytes
    assert compact_bundle(source, bundle)["alreadyDatabaseArray"]
    compact_path = bundle / "validation_results.json"
    doc = json.loads(compact_path.read_text(encoding="utf-8"))
    doc[0]["cognitive_level"] = "reasoning"
    compact_path.write_text(json.dumps(doc), encoding="utf-8")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["outputs"]["validation_results.json"] = {"sha256": digest(compact_path), "bytes": compact_path.stat().st_size}
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    with pytest.raises(AssertionError, match="database export"):
        verify_bundle(source, bundle)


def test_database_schema_and_difficulty_score_are_independent_of_domain():
    sources, decisions, *_ = fixture_data()
    original = deepcopy(sources)
    for difficulty, score in (("Easy", 600), ("Medium", 1000), ("Hard", 1400)):
        decisions[0]["llmAdvisory"]["advisoryLabels"]["intendedDifficulty"] = difficulty
        row = database_items(sources, decisions)[0]
        assert list(row) == list(sources[0])
        assert row["cognitive_level"] == "knowing"
        assert row["cognitive_score"] == score
        assert row["status"] == "silver_ready"
        assert {k: v for k, v in row.items() if k not in ("cognitive_level", "cognitive_score", "confidence_score", "status")} == {
            k: v for k, v in sources[0].items() if k not in ("cognitive_level", "cognitive_score", "confidence_score", "status")}
    assert sources == original


def test_confidence_counts_final_label_support_after_majority_override():
    sources, decisions, *_ = fixture_data()
    advisory = decisions[0]["llmAdvisory"]
    assert database_items(sources, decisions)[0]["confidence_score"] == 100
    for run in advisory["runs"][:2]:
        run["heads"]["knowledgeDimension"]["label"] = "factual"
    advisory["votes"] = {"knowledgeDimension": {"supportingVotes": 2, "initialMajorityLabel": "factual"}}
    advisory["adjudication"] = {"status": "success"}
    # The final procedural label has one supporting initial run, despite two majority votes.
    assert database_items(sources, decisions)[0]["confidence_score"] == 33
    advisory["runs"][1]["heads"]["knowledgeDimension"]["label"] = "procedural"
    assert database_items(sources, decisions)[0]["confidence_score"] == 67


def test_failed_abstaining_and_missing_runs_do_not_inflate_confidence():
    sources, decisions, *_ = fixture_data()
    advisory = decisions[0]["llmAdvisory"]
    advisory["runs"][0]["status"] = "error"
    assert database_items(sources, decisions)[0]["confidence_score"] == 67
    advisory["runs"][1]["heads"]["intendedDifficulty"]["action"] = "abstain"
    assert database_items(sources, decisions)[0]["confidence_score"] == 33
    advisory["runs"].pop()
    assert database_items(sources, decisions)[0]["confidence_score"] == 0


def test_duplicate_runs_and_unknown_difficulty_are_rejected():
    sources, decisions, *_ = fixture_data()
    advisory = decisions[0]["llmAdvisory"]
    advisory["runs"][1]["runIndex"] = 1
    with pytest.raises(ValueError, match="indices"):
        database_items(sources, decisions)
    advisory["runs"][1]["runIndex"] = 2
    advisory["advisoryLabels"]["intendedDifficulty"] = "unknown"
    with pytest.raises(ValueError, match="difficulty"):
        database_items(sources, decisions)


def test_held_database_rows_keep_their_blocking_status():
    sources, decisions, *_ = fixture_data()
    decisions[0]["finalRouting"] = "revision_required"
    row = database_items(sources, decisions)[0]
    assert row["cognitive_score"] == 600
    assert row["confidence_score"] == 100
    assert row["status"] == "revision_required"
