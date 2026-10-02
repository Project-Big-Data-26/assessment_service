from copy import deepcopy

import pytest

from scripts.build_blind_validation_bundle import blind_outcome, difficulty_groups, render_report, select_evidence, verify_probability
from scripts.generate_silver_labels_kelas1 import store_run_result


def valid_record():
    return {
        "aggregate": {
            "contentStatus": "valid",
            "answerKeyStatus": "verified",
            "eligibleForTraining": True,
            "heads": {
                "mathCognitiveDomain": {"label": "applying"},
                "knowledgeDimension": {"label": "procedural"},
                "intendedDifficulty": {"label": "Medium"},
            },
        }
    }


def test_final_difficulty_uses_locked_blind_label_without_a_model_vote():
    labels, route = blind_outcome(valid_record(), {"status": "pass"})
    assert labels["intendedDifficulty"] == "Medium"
    assert route == "pending_expert_review"


@pytest.mark.parametrize("blocker", ["structure", "content", "key"])
def test_content_blockers_cannot_be_hidden_by_three_labels(blocker):
    record = valid_record()
    structure = {"status": "pass"}
    if blocker == "structure":
        structure["status"] = "review"
    elif blocker == "content":
        record["aggregate"]["contentStatus"] = "concern"
    else:
        record["aggregate"]["answerKeyStatus"] = "conflict"
    labels, route = blind_outcome(record, structure)
    assert route == "revision_required"
    assert labels["intendedDifficulty"] == "Medium"


def test_adjudication_evidence_is_used_instead_of_an_earlier_vote():
    record = valid_record()
    record["aggregate"]["adjudicated"] = True
    record["adjudication"] = {"status": "success", "output": {"intendedDifficulty": {"label": "Medium", "rationale": "Two dependent steps", "profile": {"dependentSteps": 2}}}}
    record["runs"] = [{"status": "success", "output": {"intendedDifficulty": {"label": "Easy"}}}]
    evidence = select_evidence(record, "intendedDifficulty", "Medium")
    assert evidence["label"] == "Medium"
    assert evidence["profile"]["dependentSteps"] == 2


def test_unresolved_labels_require_manual_review():
    record = valid_record()
    record["aggregate"]["eligibleForTraining"] = False
    record["aggregate"]["heads"]["intendedDifficulty"]["label"] = None
    labels, route = blind_outcome(record, {"status": "pass"})
    assert labels["intendedDifficulty"] is None
    assert route == "llm_retry_or_manual_review"


def test_diagnostic_probability_check_rejects_fabricated_confidence():
    head = {"label": "Easy", "probabilities": {"Easy": .5, "Medium": .5}, "calibratedConfidence": .5, "normalizedEntropy": 1., "action": "review"}
    verify_probability(head)
    bad = deepcopy(head)
    bad["calibratedConfidence"] = .95
    with pytest.raises(AssertionError):
        verify_probability(bad)


def test_abstained_item_has_no_invented_confidence():
    verify_probability({"label": None, "probabilities": {}, "action": "abstain"})


def test_retry_preserves_failure_without_replacing_successful_votes():
    failed = {"runIndex": 3, "status": "failed", "errorCode": "ServerError:503"}
    first = {"runIndex": 1, "status": "success"}
    record = {"runs": [first, failed]}
    success = {"runIndex": 3, "status": "success"}
    store_run_result(record, success)
    assert record["retryHistory"] == [failed]
    assert record["runs"] == [first, success]
    with pytest.raises(ValueError, match="must not be overwritten"):
        store_run_result(record, {"runIndex": 1, "status": "success"})


def test_grade_two_groups_keep_empty_categories_and_content_blockers():
    questions = [{"questionId": str(i), "grade": 2} for i in range(3)]
    decisions = [
        {"questionId": str(i), "llmAdvisory": {"advisoryLabels": {"intendedDifficulty": label}}, "finalRouting": route}
        for i, (label, route) in enumerate([
            ("Medium", "pending_expert_review"),
            ("Medium", "revision_required"),
            (None, "llm_retry_or_manual_review"),
        ])
    ]
    grouped = difficulty_groups(questions, decisions, 2)
    assert grouped["sourceClass"] == 2
    assert grouped["summary"]["Medium"] == {"advisoryCount": 2, "contentQualifiedCount": 1}
    assert grouped["groups"]["Easy"] == grouped["groups"]["Hard"] == []
    assert len(grouped["groups"]["undecided"]) == 1
    assert all(item["humanReviewRequired"] and not item["isGoldLabel"] for items in grouped["groups"].values() for item in items)
    with pytest.raises(ValueError, match="grade mismatch"):
        difficulty_groups(questions, decisions, 1)


def test_grade_two_report_uses_checkpoint_grade_and_all_difficulty_links():
    summary = {
        "itemCount": 0, "advisoryLabelDistributions": {"intendedDifficulty": {}},
        "contentQualifiedAdvisoryLabelDistributions": {"intendedDifficulty": {}}, "routingCounts": {},
    }
    checkpoint = {
        "sourceGrade": 2, "model": "test", "promptVersion": "blind", "rubricVersion": "grade-aware",
        "summary": {"successfulRuns": 0, "totalTokens": 0},
    }
    model = {"modelVersion": "test", "architectureVersion": "parallel-v1", "inputRepresentation": "metadata"}
    report = render_report([], [], summary, checkpoint, model)
    assert "Validasi ulang soal kelas 2" in report
    assert "rubrik kelas 2" in report
    assert "rubrik kelas 1" not in report
    for label in ("Easy", "Medium", "Hard"):
        assert f"[{label}.json](difficulty/{label}.json)" in report
