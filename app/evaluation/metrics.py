"""Classification metrics kept separate for Bloom and difficulty tasks."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


def classification_metrics(
    expected: Sequence[str],
    predicted: Sequence[str],
    *,
    labels: Sequence[str],
) -> dict[str, Any]:
    """Calculate accuracy, per-class metrics, macro average, and confusion matrix."""
    if len(expected) != len(predicted):
        raise ValueError("expected and predicted must have the same length")
    if not expected:
        raise ValueError("at least one classification is required")

    report = classification_report(
        expected,
        predicted,
        labels=list(labels),
        output_dict=True,
        zero_division=0,
    )
    matrix = confusion_matrix(expected, predicted, labels=list(labels))

    return {
        "accuracy": float(accuracy_score(expected, predicted)),
        "report": report,
        "confusion_matrix": matrix.tolist(),
        "labels": list(labels),
    }
