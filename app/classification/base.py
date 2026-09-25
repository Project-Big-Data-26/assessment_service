"""Stable classification contracts independent of a concrete ML framework."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True, slots=True)
class ClassificationPrediction:
    """Prediction envelope shared by placeholder and future classifiers."""

    bloom_level: str | None
    bloom_confidence: float | None
    knowledge_dimension: str | None
    knowledge_confidence: float | None
    difficulty_level: str | None
    difficulty_confidence: float | None
    model_version: str | None
    status: str
    prediction_source: str = "model"
    rationale: tuple[str, ...] = ()


class QuestionClassifier(Protocol):
    """Interface that every future question classifier must implement."""

    def predict(self, question_text: str) -> ClassificationPrediction:
        """Predict Bloom and difficulty outputs for normalized question text."""
        ...
