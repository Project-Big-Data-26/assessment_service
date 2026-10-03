import numpy as np
import pytest
from pydantic import ValidationError

from app.psychometrics.analysis import analyze_matrix, load_policy, normalize_events
from app.psychometrics.contracts import MatrixAnalysisInput
from app.psychometrics.irt import response_probability
from scripts.psychometrics import simulated_matrix


def test_rasch_recovers_item_order_and_finite_person_estimates_with_missing():
    payload, truth = simulated_matrix(persons=500, items=12)
    payload.matrix[0] = [1] * 12
    payload.matrix[1] = [0] * 12
    result = analyze_matrix(payload)
    assert result["readiness"]["passed"] is True
    assert result["irt"]["converged"] is True
    estimates = [item["b"] for item in result["irt"]["items"]]
    assert np.corrcoef(truth["b"], estimates)[0, 1] > .98
    assert np.mean(np.abs(np.array(estimates) - truth["b"])) < .35
    assert all(item["a"] == 1 and item["c"] == 0 for item in result["irt"]["items"])
    assert all(np.isfinite(person["thetaEap"]) and person["posteriorSd"] > 0 for person in result["irt"]["persons"])
    assert result["researchOnly"] and result["labelProvenance"] == "ai_silver"
    assert result["normalization"]["missingCells"] > 0


@pytest.mark.parametrize("model", ["2pl", "3pl"])
def test_other_models_recover_difficulty_and_produce_bounded_parameters(model):
    payload, truth = simulated_matrix(model)
    result = analyze_matrix(payload)
    assert result["readiness"]["passed"]
    assert result["irt"]["converged"]
    estimates = result["irt"]["items"]
    assert np.corrcoef(truth["b"], [item["b"] for item in estimates])[0, 1] > .9
    assert all(.2 <= item["a"] <= 4 for item in estimates)
    assert all(0 <= item["c"] <= .35 for item in estimates)


def test_insufficient_sample_does_not_fit_and_reports_ctt():
    payload, _ = simulated_matrix(persons=20)
    result = analyze_matrix(payload)
    assert result["readiness"]["passed"] is False
    assert "insufficient_persons" in result["readiness"]["failures"]
    assert result["irt"]["items"] == []
    assert result["items"][0]["ctt"]["validResponseCount"] <= 20


def test_missing_assumption_review_and_homogeneous_items_fail_gate():
    payload, _ = simulated_matrix()
    payload.assumptionReview = None
    for row in payload.matrix:
        row[0] = 1
    result = analyze_matrix(payload)
    assert "assumptions_not_reviewed" in result["readiness"]["failures"]
    assert "item_0:insufficient_outcome_variation" in result["readiness"]["failures"]
    assert result["items"][0]["ctt"]["difficultyCi95"][1] == 1


def test_ctt_uses_complete_cases_and_preserves_missing_as_null():
    payload, _ = simulated_matrix(persons=40)
    payload.matrix[0][0] = None
    result = analyze_matrix(payload)
    actual = sum(row[0] is not None for row in payload.matrix)
    assert result["items"][0]["ctt"]["validResponseCount"] == actual
    assert result["ctt"]["completeCaseCount"] == sum(all(value is not None for value in row) for row in payload.matrix)


@pytest.mark.parametrize("replacement", [2, -1, "1", True, float("nan")])
def test_contract_rejects_invalid_binary_values(replacement):
    payload, _ = simulated_matrix(persons=10)
    document = payload.model_dump(mode="json")
    document["matrix"][0][0] = replacement
    with pytest.raises(ValidationError):
        MatrixAnalysisInput.model_validate(document)


def test_disconnected_forms_and_excess_missing_cannot_be_calibrated():
    payload, _ = simulated_matrix(persons=300, items=10)
    for index, row in enumerate(payload.matrix):
        row[:5] = [None] * 5 if index < 150 else row[:5]
        row[5:] = [None] * 5 if index >= 150 else row[5:]
    policy = load_policy().model_copy(update={"maxPersonMissingRate": .6, "minCoverage": .4})
    result = analyze_matrix(payload, policy)
    assert "disconnected_response_design" in result["readiness"]["failures"]
    assert result["irt"]["items"] == []


def test_normalization_excludes_duplicate_invalid_version_rapid_guess_and_conflict():
    payload, _ = simulated_matrix(persons=10, items=5)
    item = payload.items[0].model_dump(mode="json")
    base = {"responseId": "response-1", "subjectHash": "s1", "populationId": "p1", "assessmentFamily": "f1", "grade": 1,
            **{key: item[key] for key in ("questionId", "questionVersionId", "contentVersion", "contentHash")},
            "isCorrect": True, "scoringStatus": "scored", "validForAnalysis": True, "flags": [], "submittedAt": "2026-10-02T00:00:00+00:00"}
    events = [base, dict(base), {**base, "responseId": "bad-version", "contentVersion": 2},
              {**base, "responseId": "rapid", "flags": ["rapid_guess_candidate"]},
              {**base, "responseId": "conflict"}, {**base, "responseId": "conflict", "isCorrect": False}]
    matrix, cleaning = normalize_events(events, items=[item], subject_ids=["s1", "s2"], population_id="p1", assessment_family="f1", grade=1)
    assert matrix.matrix == [[1], [None]]
    assert cleaning["exclusions"]["duplicate_event"] == 1
    assert cleaning["exclusions"]["version_mismatch"] == 1
    assert cleaning["exclusions"]["invalid_or_rapid_guess"] == 1
    assert cleaning["exclusions"]["conflicting_response_id"] == 1


def test_probability_and_information_are_monotone_and_nonnegative():
    probabilities = response_probability(np.array([-3., 0., 3.]), 1.2, .5, .2)
    assert .2 < probabilities[0] < probabilities[1] < probabilities[2] < 1
