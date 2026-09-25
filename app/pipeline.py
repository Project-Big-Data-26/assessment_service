"""Minimal end-to-end pipeline without a trained model."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from app.classification import ClassificationPrediction, PlaceholderClassifier, QuestionClassifier
from app.preprocessing import normalize_text
from app.utils import load_question_dataset, load_yaml_config

PROJECT_ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True, slots=True)
class PipelineResult:
    """Traceable output from preprocessing through inference."""

    question_id: str
    normalized_text: str
    features: dict[str, int]
    prediction: ClassificationPrediction


def prepare_features(question_text: str) -> dict[str, int]:
    """Create transparent structural features for future experiments."""
    return {
        "character_count": len(question_text),
        "word_count": len(question_text.split()),
    }


class QuestionIntelligencePipeline:
    """Orchestrate preprocessing, feature preparation, and classification."""

    def __init__(self, classifier: QuestionClassifier | None = None) -> None:
        self.classifier = classifier or PlaceholderClassifier()

    def run(self, question: dict[str, Any], *, lowercase: bool = False) -> PipelineResult:
        """Process one question record using the configured classifier."""
        question_id = str(question.get("question_id", "")).strip()
        raw_text = question.get("question_text")
        if not question_id:
            raise ValueError("question_id must not be empty")
        if not isinstance(raw_text, str):
            raise TypeError("question_text must be a string")

        normalized_text = normalize_text(raw_text, lowercase=lowercase)
        if not normalized_text:
            raise ValueError("question_text must not be empty")

        return PipelineResult(
            question_id=question_id,
            normalized_text=normalized_text,
            features=prepare_features(normalized_text),
            prediction=self.classifier.predict(normalized_text),
        )


def main() -> None:
    """Run one sample through the pipeline as a local smoke test."""
    config = load_yaml_config(PROJECT_ROOT / "configs" / "dataset_config.yaml")
    dataset_path = PROJECT_ROOT / config["dataset"]["sample_path"]
    questions = load_question_dataset(dataset_path)
    first_question = questions.iloc[0].to_dict()
    lowercase = bool(config["preprocessing"].get("lowercase", False))
    result = QuestionIntelligencePipeline().run(first_question, lowercase=lowercase)
    print(json.dumps(asdict(result), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
