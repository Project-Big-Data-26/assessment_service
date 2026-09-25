from app.classification.baseline import RuleBasedBaselineClassifier

def test_baseline_is_explicitly_advisory() -> None:
    result = RuleBasedBaselineClassifier().predict("Analisis hubungan antara gradien dan persamaan garis.")
    assert result.bloom_level == "C4"
    assert result.status == "baseline_advisory"
    assert result.prediction_source == "rules_baseline"
    assert result.knowledge_dimension == "conceptual"
