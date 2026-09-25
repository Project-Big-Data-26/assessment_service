"""Question dataset loading and schema validation."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

REQUIRED_COLUMNS = (
    "question_id",
    "question_text",
    "subject",
    "material_id",
    "bloom_label",
    "knowledge_label",
    "difficulty_label",
)
BLOOM_LABELS = frozenset({"C1", "C2", "C3", "C4", "C5", "C6"})
KNOWLEDGE_LABELS = frozenset({"factual", "conceptual", "procedural", "metacognitive"})
DIFFICULTY_LABELS = frozenset({"Easy", "Medium", "Hard"})


class DatasetValidationError(ValueError):
    """Raised when a question dataset violates the expected contract."""


def load_question_dataset(path: str | Path) -> pd.DataFrame:
    """Load a JSON or CSV dataset and validate its required schema."""
    dataset_path = Path(path)
    if not dataset_path.is_file():
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")

    suffix = dataset_path.suffix.lower()
    if suffix == ".json":
        frame = pd.read_json(dataset_path, orient="records")
    elif suffix == ".csv":
        frame = pd.read_csv(dataset_path)
    else:
        raise DatasetValidationError("Dataset format must be .json or .csv")

    validate_question_dataset(frame)
    return frame


def validate_question_dataset(frame: pd.DataFrame) -> None:
    """Validate columns, identifiers, text content, and supported labels."""
    missing_columns = [column for column in REQUIRED_COLUMNS if column not in frame.columns]
    if missing_columns:
        raise DatasetValidationError(f"Missing required columns: {missing_columns}")
    if frame.empty:
        raise DatasetValidationError("Dataset must contain at least one question")
    if frame["question_id"].duplicated().any():
        raise DatasetValidationError("question_id values must be unique")

    for column in REQUIRED_COLUMNS:
        values = frame[column]
        if values.isna().any() or values.astype(str).str.strip().eq("").any():
            raise DatasetValidationError(f"Column {column!r} contains empty values")

    invalid_bloom = sorted(set(frame["bloom_label"]) - BLOOM_LABELS)
    if invalid_bloom:
        raise DatasetValidationError(f"Unsupported Bloom labels: {invalid_bloom}")

    invalid_knowledge = sorted(set(frame["knowledge_label"]) - KNOWLEDGE_LABELS)
    if invalid_knowledge:
        raise DatasetValidationError(f"Unsupported knowledge labels: {invalid_knowledge}")

    invalid_difficulty = sorted(set(frame["difficulty_label"]) - DIFFICULTY_LABELS)
    if invalid_difficulty:
        raise DatasetValidationError(f"Unsupported difficulty labels: {invalid_difficulty}")
