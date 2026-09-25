from pathlib import Path

from app.utils.dataset import REQUIRED_COLUMNS, load_question_dataset

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_sample_dataset_can_be_loaded() -> None:
    dataset = load_question_dataset(PROJECT_ROOT / "data" / "sample" / "questions.json")

    assert len(dataset) == 6
    assert set(REQUIRED_COLUMNS).issubset(dataset.columns)
    assert set(dataset["bloom_label"]) == {"C1", "C2", "C3", "C4", "C5", "C6"}
    assert set(dataset["difficulty_label"]) == {"Easy", "Medium", "Hard"}
