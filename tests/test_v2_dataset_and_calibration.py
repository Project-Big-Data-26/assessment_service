import numpy as np
from collections import Counter

from app.classification.v2.calibration import (
    fit_temperature,
    negative_log_likelihood,
    normalized_entropy,
    softmax,
)
from app.classification.v2.contracts import QuestionOption
from app.training.v2.dataset import GoldTrainingRow, deterministic_group_split


def row(index: int, source: str, family: str | None = None):
    return GoldTrainingRow(
        questionId=f"q-{index}",
        questionVersionId=f"q-{index}:v1",
        contentVersion=1,
        contentHash=f"{index:064x}",
        sourceGroup=source,
        duplicateFamily=family,
        grade=(index % 6) + 1,
        topic="Bilangan",
        questionType="multiple_choice",
        stem=f"Hitung nilai {index} + 1.",
        options=[QuestionOption(label="A", text=str(index)), QuestionOption(label="B", text=str(index + 1))],
        verifiedMinimalSolution=f"{index} + 1 = {index + 1}",
        mathCognitiveDomain=("knowing", "applying", "reasoning")[index % 3],
        knowledgeDimension=("factual", "conceptual", "procedural", "metacognitive")[index % 4],
        intendedDifficulty=("Easy", "Medium", "Hard")[index % 3],
        rubricVersion="math-rubric-3x4x3-v1",
        decisionProvenance={"kind": "majority"},
    )


def test_group_split_is_deterministic_and_has_no_source_or_family_leakage():
    rows = [row(index, f"exercise-{index // 3}", "shared" if index in (0, 20) else None) for index in range(60)]
    first = deterministic_group_split(rows, seed=42)
    second = deterministic_group_split(rows, seed=42)
    reversed_input = deterministic_group_split(list(reversed(rows)), seed=42)
    assert first == second
    assert first == reversed_input
    split_by_id = {entry.questionVersionId: entry.split for entry in first}
    for left in rows:
        for right in rows:
            if left.sourceGroup == right.sourceGroup or (left.duplicateFamily and left.duplicateFamily == right.duplicateFamily):
                assert split_by_id[left.questionVersionId] == split_by_id[right.questionVersionId]
    counts = Counter(entry.split for entry in first)
    assert abs(counts["train"] / len(rows) - 0.70) <= 0.10
    assert abs(counts["validation"] / len(rows) - 0.15) <= 0.10
    assert abs(counts["test"] / len(rows) - 0.15) <= 0.10


def test_temperature_scaling_never_worsens_validation_nll():
    logits = np.array([[3.0, 1.0, 0.0], [2.0, 0.5, 0.0], [0.1, 2.0, 0.2], [0.2, 0.1, 1.8]])
    labels = np.array([0, 1, 1, 2])
    temperature = fit_temperature(logits, labels)
    before = negative_log_likelihood(softmax(logits), labels)
    after = negative_log_likelihood(softmax(logits, temperature), labels)
    assert after <= before + 1e-12
    assert 0 <= normalized_entropy([0.8, 0.1, 0.1]) <= 1
