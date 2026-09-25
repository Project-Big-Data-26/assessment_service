"""Safe inference placeholder used before a trained model exists."""

from __future__ import annotations

from app.classification.base import ClassificationPrediction


class PlaceholderClassifier:
    """Return an explicit unconfigured state instead of fabricated labels."""

    def predict(self, question_text: str) -> ClassificationPrediction:
        if not question_text:
            raise ValueError("question_text must not be empty")

        return ClassificationPrediction(
            bloom_level=None,
            bloom_confidence=None,
            knowledge_dimension=None,
            knowledge_confidence=None,
            difficulty_level=None,
            difficulty_confidence=None,
            model_version=None,
            status="not_configured",
            prediction_source="none",
        )
