"""Quota exports must disclose unsupported labels and preserve content eligibility."""
from copy import deepcopy
import json
from pathlib import Path

import pytest

import scripts.balance_operational_difficulty as balance
from scripts.balance_operational_difficulty import allocate


def fixture(steps, inactive=False):
    rows, decisions = [], []
    for i, step in enumerate(steps):
        labels = {"mathCognitiveDomain": "Knowing", "knowledgeDimension": "Procedural",
                  "intendedDifficulty": "Easy"}
        profile = {"dependentSteps": step, "routineStatus": "familiar_routine",
                   "strategySelection": False, "representationTransfer": False,
                   "interactingConstraints": 0, "relevantInformationUnits": 1,
                   "calculationLoad": "low", "scaffoldLevel": "none"}
        rows.append({"_id": str(i), "text": f"source {i}", "cognitive_level": "easy",
                     "cognitive_score": 600, "confidence_score": 100,
                     "status": "inactive" if inactive and i == 0 else "active"})
        decisions.append({"questionId": str(i),
                          "finalRouting": "revision_required" if inactive and i == 0 else "silver_ready",
                          "llmAdvisory": {"advisoryLabels": labels, "requestedRuns": 3,
                              "votes": {"intendedDifficulty": {"lockedEvidence": {"profile": profile}}},
                              "runs": [{"runIndex": j, "status": "success",
                                        "heads": {h: {"action": "classify", "label": v}
                                                  for h, v in labels.items()}} for j in range(1, 4)]}})
    return rows, decisions


def test_ranking_quotas_confidence_and_preservation():
    rows, decisions = fixture([9, 1, 8, 2, 7, 3, 6])
    original = deepcopy((rows, decisions))
    result, audit = allocate(rows, decisions)
    assert audit["targets"] == {"easy": 3, "medium": 2, "hard": 2}
    assert [item["cognitive_level"] for item in result] == ["hard", "easy", "hard", "easy", "medium", "easy", "medium"]
    assert all(item["confidence_score"] == (100 if item["cognitive_level"] == "easy" else 0)
               for item in result)
    assert audit["zeroAiSupportLabels"] == 4
    assert (rows, decisions) == original
    assert all(a["text"] == b["text"] and a.keys() == b.keys() for a, b in zip(rows, result))


def test_equal_scores_disclose_arbitrary_boundaries():
    rows, decisions = fixture([1] * 6)
    _, audit = allocate(rows, decisions)
    assert audit["targets"] == {"easy": 2, "medium": 2, "hard": 2}
    assert len(audit["tieBoundaries"]) == 2
    assert all(b["equalProfileScoreSplit"] for b in audit["tieBoundaries"])


def test_inactive_is_preserved_and_excluded_from_quotas():
    rows, decisions = fixture([1, 2, 3, 4], inactive=True)
    result, audit = allocate(rows, decisions)
    assert result[0] == rows[0]
    assert audit["activeQuestionCount"] == 3
    assert audit["targets"] == {"easy": 1, "medium": 1, "hard": 1}


def test_missing_profile_or_duplicate_decision_is_rejected():
    rows, decisions = fixture([1])
    with pytest.raises(ValueError, match="coverage"):
        allocate(rows, decisions + decisions)
    decisions[0]["llmAdvisory"]["votes"]["intendedDifficulty"]["lockedEvidence"]["profile"] = None
    with pytest.raises(ValueError, match="profile"):
        allocate(rows, decisions)


def write_bundle(tmp_path, monkeypatch):
    """Isolate versioning; production bundle verification is invoked before exports."""
    directory = tmp_path / "kelas1"
    bundle = directory / "hasil_validasi"
    bundle.mkdir(parents=True)
    rows, decisions = fixture([1, 2, 3, 4, 5, 6], inactive=True)
    for decision in decisions:
        decision["llmAdvisory"]["rubricVersion"] = "test-v8"
    source = directory / "soal_pretest_db.json"
    source.write_text(json.dumps(rows), encoding="utf-8")
    (bundle / "validation_results.json").write_text(json.dumps(rows), encoding="utf-8")
    (bundle / "manifest.json").write_text(
        json.dumps({"databaseExport": {"subjectTrack": "regular", "sourceClass": 1}}), encoding="utf-8")
    evidence = bundle / "decisions.json"
    evidence.write_text(json.dumps({"items": decisions}), encoding="utf-8")
    verified = []
    monkeypatch.setattr(balance, "verify_bundle", lambda source, bundle: verified.append((source, bundle)))
    monkeypatch.setattr(balance, "load_decision_bundle", lambda bundle: json.loads((bundle / "decisions.json").read_text()))
    return source, bundle, evidence, verified


def test_versioned_export_reuses_evidence_and_preserves_originals(tmp_path, monkeypatch):
    source, bundle, _, verified = write_bundle(tmp_path, monkeypatch)
    before = {path: path.read_bytes() for path in [source, *bundle.iterdir()]}
    first = balance.export_verified_operational_balance(source, bundle, grade=1, track="regular")
    export = Path(first["directory"])
    output_before = {path: path.read_bytes() for path in export.iterdir()}
    second = balance.export_verified_operational_balance(source, bundle, grade=1, track="regular")
    assert first["created"] is True and second["created"] is False
    assert first["directory"] == second["directory"]
    assert first["activeDistribution"] == {"easy": 2, "medium": 2, "hard": 1}
    assert first["zeroAiSupportLabels"] == 3
    assert {path: path.read_bytes() for path in export.iterdir()} == output_before
    assert {path: path.read_bytes() for path in before} == before
    assert len(verified) == 2
    pointer = json.loads((export.parent / "current.json").read_text())
    assert pointer["validationResults"] == second["validationResults"]
    assert balance.verify_operational_export(export)["sourceFingerprint"] == first["sourceFingerprint"]


def test_changed_ai_profile_creates_new_immutable_version(tmp_path, monkeypatch):
    source, bundle, evidence, _ = write_bundle(tmp_path, monkeypatch)
    first = balance.export_verified_operational_balance(source, bundle, grade=1, track="regular")
    first_contents = {path: path.read_bytes() for path in Path(first["directory"]).iterdir()}
    decisions = json.loads(evidence.read_text())
    decisions["items"][1]["llmAdvisory"]["votes"]["intendedDifficulty"]["lockedEvidence"]["profile"]["dependentSteps"] = 9
    evidence.write_text(json.dumps(decisions), encoding="utf-8")
    second = balance.export_verified_operational_balance(source, bundle, grade=1, track="regular")
    assert second["created"] is True and first["directory"] != second["directory"]
    assert {path: path.read_bytes() for path in first_contents} == first_contents
    assert len(list(Path(first["directory"]).parent.glob("source_*"))) == 2
    balance.verify_operational_export(Path(first["directory"]))
    balance.verify_operational_export(Path(second["directory"]))


def test_resume_rejects_tampering_instead_of_overwriting(tmp_path, monkeypatch):
    source, bundle, _, _ = write_bundle(tmp_path, monkeypatch)
    first = balance.export_verified_operational_balance(source, bundle, grade=1, track="regular")
    output = Path(first["validationResults"])
    output.write_text("[]", encoding="utf-8")
    with pytest.raises(ValueError, match="checksum"):
        balance.export_verified_operational_balance(source, bundle, grade=1, track="regular")
    assert output.read_text() == "[]"


def test_export_rejects_invalid_bundle_track_and_unknown_destination(tmp_path, monkeypatch):
    source, bundle, _, _ = write_bundle(tmp_path, monkeypatch)
    with pytest.raises(ValueError, match="grade differs"):
        balance.export_verified_operational_balance(source, bundle, grade=2, track="regular")
    with pytest.raises(ValueError, match="directory name"):
        balance.export_verified_operational_balance(source, bundle, grade=1, track="regular", output_name="../evidence")
    with pytest.raises(ValueError, match="unsupported grade"):
        balance.export_verified_operational_balance(source, bundle, grade=1, track="tl")
