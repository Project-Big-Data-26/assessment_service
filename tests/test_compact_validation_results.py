"""Compact exports preserve identity, adjudicated labels and auditable evidence."""
from copy import deepcopy
import json

import pytest

from app.silver.exports import (AUDIT_FILE, COMPACT_SCHEMA, LEGACY_DATABASE_SCHEMA, PREVIOUS_DATABASE_SCHEMA,
                               compact_items, database_items,
                               load_decision_bundle, confidence_details, confidence_policy_for,
                               final_label_support)
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


@pytest.mark.parametrize("upgrade_legacy", [None, LEGACY_DATABASE_SCHEMA, PREVIOUS_DATABASE_SCHEMA, "single_run_null"])
def test_conversion_is_idempotent_and_resealed_label_changes_are_rejected(tmp_path, upgrade_legacy):
    sources, decisions, questions, cp = fixture_data()
    if upgrade_legacy == "single_run_null":
        cp["requestedRuns"] = 1
        decisions[0]["llmAdvisory"].update(requestedRuns=1, runs=decisions[0]["llmAdvisory"]["runs"][:1])
        decisions[0]["indobert"] = {"heads": model_support_heads()}
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
    if upgrade_legacy == "single_run_null":
        old = json.loads(manifest_path.read_text(encoding="utf-8"))
        old["databaseExport"]["confidencePolicy"] = confidence_policy_for(decisions, legacy_single_run_null=True)
        metadata = compact_items(sources, decisions, questions, cp, source.parent.name, legacy_single_run_null=True)
        old["databaseExport"]["metadataByQuestionId"] = {row["_id"]: {**row["ai_metadata"],
            "math_cognitive_domain": decisions[0]["llmAdvisory"]["advisoryLabels"]["mathCognitiveDomain"],
            "final_label_supporting_runs": final_label_support(decisions[0])} for row in metadata}
        previous = database_items(sources, decisions, legacy_single_run_null=True)
        (bundle / "validation_results.json").write_text(json.dumps(previous), encoding="utf-8")
        old["outputs"]["validation_results.json"] = {"sha256": digest(bundle / "validation_results.json"),
            "bytes": (bundle / "validation_results.json").stat().st_size}
        manifest_path.write_text(json.dumps(old), encoding="utf-8")
        verify_bundle(source, bundle)
        compact_bundle(source, bundle)
        assert (bundle / AUDIT_FILE).read_bytes() == audit_bytes
        assert json.loads((bundle / "validation_results.json").read_text())[0]["confidence_score"] == 20
    elif upgrade_legacy:
        # Previous exports used the domain in the same database column.
        old = json.loads(manifest_path.read_text(encoding="utf-8"))
        old["databaseExport"]["schemaVersion"] = upgrade_legacy
        old["validationResultsSchemaVersion"] = upgrade_legacy
        old["databaseExport"].pop("statusPolicy")
        if upgrade_legacy == LEGACY_DATABASE_SCHEMA:
            old["databaseExport"].pop("cognitiveLevelPolicy")
            for metadata in old["databaseExport"]["metadataByQuestionId"].values():
                metadata.pop("math_cognitive_domain")
        previous = database_items(sources, decisions,
            legacy_domain_level=upgrade_legacy == LEGACY_DATABASE_SCHEMA, legacy_routing_status=True)
        (bundle / "validation_results.json").write_text(json.dumps(previous), encoding="utf-8")
        old["outputs"]["validation_results.json"] = {
            "sha256": digest(bundle / "validation_results.json"),
            "bytes": (bundle / "validation_results.json").stat().st_size}
        manifest_path.write_text(json.dumps(old), encoding="utf-8")
        verify_bundle(source, bundle)
        compact_bundle(source, bundle)
        assert (bundle / AUDIT_FILE).read_bytes() == audit_bytes
        assert json.loads((bundle / "validation_results.json").read_text())[0]["cognitive_level"] == "easy"
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
        assert row["cognitive_level"] == difficulty.lower()
        assert row["cognitive_score"] == score
        assert row["status"] == "active"
        assert {k: v for k, v in row.items() if k not in ("cognitive_level", "cognitive_score", "confidence_score", "status")} == {
            k: v for k, v in sources[0].items() if k not in ("cognitive_level", "cognitive_score", "confidence_score", "status")}
    assert sources == original


def model_support_heads():
    return {"mathCognitiveDomain": {"probabilities": {"knowing": .2, "applying": .7, "reasoning": .1}},
            "knowledgeDimension": {"probabilities": {"factual": .3, "conceptual": .2, "procedural": .4, "metacognitive": .1}},
            "intendedDifficulty": {"probabilities": {"Easy": .8, "Medium": .15, "Hard": .05}}}


def test_single_run_confidence_supports_final_labels_instead_of_model_argmax():
    source, decisions, *_ = fixture_data()
    decision = decisions[0]
    decision["indobert"] = {"heads": model_support_heads()}
    assert database_items(source, decisions)[0]["confidence_score"] == 100  # Historical N=3 policy.
    decision["llmAdvisory"].update(requestedRuns=1, runs=decision["llmAdvisory"]["runs"][:1])
    details = confidence_details(decision)
    assert details["available"] and details["score"] == 20
    assert details["final_label_probabilities"]["mathCognitiveDomain"] == .2
    assert database_items(source, decisions)[0]["confidence_score"] == 20
    assert database_items(source, decisions, legacy_single_run_null=True)[0]["confidence_score"] is None
    decision["indobert"]["heads"]["mathCognitiveDomain"]["probabilities"] = {"knowing": .0001, "applying": .9999, "reasoning": 0}
    assert confidence_details(decision)["score"] == 0
    assert confidence_details(decision)["available"] is True
    decision["indobert"]["heads"] = {}
    assert database_items(source, decisions)[0]["confidence_score"] == 0
    assert confidence_details(decision)["available"] is False


def test_single_run_rejects_invalid_probability_evidence():
    _, decisions, *_ = fixture_data()
    decision = decisions[0]
    decision["llmAdvisory"]["requestedRuns"] = 1
    decision["indobert"] = {"heads": model_support_heads()}
    decision["indobert"]["heads"]["intendedDifficulty"]["probabilities"]["Hard"] = -1
    with pytest.raises(ValueError, match="probability distribution"):
        confidence_details(decision)


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


@pytest.mark.parametrize("route", ["revision_required", "needs_ai_review"])
def test_held_database_rows_keep_their_blocking_status(route):
    sources, decisions, *_ = fixture_data()
    decisions[0]["finalRouting"] = route
    row = database_items(sources, decisions)[0]
    assert row["cognitive_score"] == 600
    assert row["confidence_score"] == 100
    assert row["status"] == "inactive"


def test_unknown_routing_cannot_silently_activate_an_item():
    sources, decisions, *_ = fixture_data()
    decisions[0]["finalRouting"] = "unknown"
    with pytest.raises(ValueError, match="routing"):
        database_items(sources, decisions)
