from app.evaluation.psychometrics import analyze_item, weighted_kappa, wilson_interval

def test_weighted_kappa_respects_ordered_labels() -> None:
    value = weighted_kappa(["C1", "C2", "C3", "C4"], ["C1", "C2", "C4", "C4"], ["C1", "C2", "C3", "C4", "C5", "C6"])
    assert 0.7 < value <= 1

def test_item_analysis_reports_measured_parameters() -> None:
    responses = [{"is_correct": index < 60, "selected_answer": "B" if index < 60 else ["A", "C", "D"][index % 3], "response_time_ms": 20_000 + index * 100, "total_score": 100 - index} for index in range(100)]
    result = analyze_item(responses, ["A", "B", "C", "D"])
    assert result["difficulty_index"] == 0.6
    assert result["empirical_difficulty"] == "Medium"
    assert result["distractor_efficiency"] == 1
    assert result["discrimination_index"] > 0.2

def test_wilson_interval_contains_observed_proportion() -> None:
    lower, upper = wilson_interval(60, 100)
    assert lower < 0.6 < upper
