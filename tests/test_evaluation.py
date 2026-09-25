from app.evaluation import classification_metrics


def test_classification_metrics_for_perfect_predictions() -> None:
    metrics = classification_metrics(
        ["C1", "C2", "C3"],
        ["C1", "C2", "C3"],
        labels=["C1", "C2", "C3"],
    )

    assert metrics["accuracy"] == 1.0
    assert metrics["report"]["macro avg"]["f1-score"] == 1.0
    assert metrics["confusion_matrix"] == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
