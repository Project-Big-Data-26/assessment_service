import numpy as np
from collections import Counter
from sklearn.metrics import classification_report

from app.classification.v2.calibration import (
    fit_temperature,
    negative_log_likelihood,
    normalized_entropy,
    select_routing_thresholds,
    softmax,
)
from app.classification.v2.contracts import IntendedDifficulty, QuestionOption
from app.training.v2.dataset import (
    TrainingRow,
    SplitEntry,
    build_snapshot,
    deterministic_group_split,
    validate_split_integrity,
)
from app.training.v2.train_lora import (
    _class_weights,
    calibration_from_validation,
    candidate_diagnostics,
    label_coverage_failures,
)


def row(index: int, source: str, family: str | None = None):
    return TrainingRow(
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


def test_shared_stimulus_never_crosses_splits_even_with_different_sources():
    rows = [row(index, f"exercise-{index}") for index in range(30)]
    rows[3] = rows[3].model_copy(update={"stimulus": "Tabel harga yang sama."})
    rows[24] = rows[24].model_copy(update={"stimulus": "  tabel HARGA yang sama.  "})
    manifest = deterministic_group_split(rows, seed=42)
    split_by_id = {entry.questionVersionId: entry.split for entry in manifest}
    assert split_by_id[rows[3].questionVersionId] == split_by_id[rows[24].questionVersionId]


def test_explicit_split_leakage_is_a_hard_gate_failure():
    rows = [row(1, "shared-source"), row(2, "shared-source")]
    manifest = [
        SplitEntry(
            questionVersionId=rows[0].questionVersionId,
            groupId="tampered-a",
            split="train",
        ),
        SplitEntry(
            questionVersionId=rows[1].questionVersionId,
            groupId="tampered-b",
            split="test",
        ),
    ]
    failures = validate_split_integrity(rows, manifest)
    assert any(value.startswith("split_leakage:") for value in failures)


def test_temperature_scaling_never_worsens_validation_nll():
    logits = np.array([[3.0, 1.0, 0.0], [2.0, 0.5, 0.0], [0.1, 2.0, 0.2], [0.2, 0.1, 1.8]])
    labels = np.array([0, 1, 1, 2])
    temperature = fit_temperature(logits, labels)
    before = negative_log_likelihood(softmax(logits), labels)
    after = negative_log_likelihood(softmax(logits, temperature), labels)
    assert after <= before + 1e-12
    assert 0 <= normalized_entropy([0.8, 0.1, 0.1]) <= 1


def test_joint_confidence_entropy_routing_thresholds_meet_validation_gate():
    probabilities = np.array(
        [
            [0.95, 0.03, 0.02],
            [0.90, 0.06, 0.04],
            [0.85, 0.10, 0.05],
            [0.80, 0.15, 0.05],
            [0.45, 0.40, 0.15],
            [0.40, 0.35, 0.25],
        ]
    )
    labels = np.array([0, 0, 0, 0, 1, 1])
    confidence_threshold, entropy_threshold = select_routing_thresholds(
        probabilities,
        labels,
        target_accuracy=0.80,
        minimum_coverage=0.60,
    )
    assert confidence_threshold is not None
    assert entropy_threshold is not None
    confidence = probabilities.max(axis=1)
    entropy = np.asarray([normalized_entropy(row) for row in probabilities])
    selected = (confidence >= confidence_threshold) & (entropy <= entropy_threshold)
    assert selected.mean() >= 0.60
    assert (probabilities.argmax(axis=1)[selected] == labels[selected]).mean() >= 0.80


def test_strict_routing_rejects_missing_class_and_trivial_zero_threshold():
    probabilities = np.array([[0.9, 0.1, 0.0], [0.8, 0.2, 0.0]])
    labels = np.array([0, 1])
    assert select_routing_thresholds(
        probabilities,
        labels,
        require_all_classes=True,
        minimum_class_support=1,
        allow_zero_threshold=False,
    ) == (None, None)


def test_majority_collapse_is_rejected_despite_high_accuracy():
    targets = np.array([0] * 18 + [1] * 2 + [2])
    predicted = np.zeros_like(targets)
    report = classification_report(
        targets,
        predicted,
        labels=[0, 1, 2],
        target_names=["Easy", "Medium", "Hard"],
        output_dict=True,
        zero_division=0,
    )
    metrics = {}
    for head, labels in {
        "mathCognitiveDomain": ("knowing", "applying", "reasoning"),
        "knowledgeDimension": ("factual", "conceptual", "procedural", "metacognitive"),
        "intendedDifficulty": ("Easy", "Medium", "Hard"),
    }.items():
        if head == "intendedDifficulty":
            metrics[head] = report
        else:
            y = np.arange(len(targets)) % len(labels)
            metrics[head] = classification_report(
                y,
                y,
                labels=list(range(len(labels))),
                target_names=list(labels),
                output_dict=True,
                zero_division=0,
            )
    diagnostics = candidate_diagnostics(
        metrics,
        {"targets_intendedDifficulty": targets},
    )
    assert diagnostics["passed"] is False
    assert "zero_recall:intendedDifficulty:Medium" in diagnostics["failures"]
    assert "difficulty_does_not_beat_majority_macro_f1" in diagnostics["failures"]


def test_training_coverage_reports_every_missing_label():
    rows = [
        {
            "mathCognitiveDomain": "knowing",
            "knowledgeDimension": "factual",
            "intendedDifficulty": "Easy",
        }
    ]
    failures = label_coverage_failures(rows)
    assert "train:intendedDifficulty:Medium=0" in failures
    assert "train:intendedDifficulty:Hard=0" in failures
    import pytest

    with pytest.raises(ValueError, match="requires every real class"):
        _class_weights(rows, "intendedDifficulty")


def test_per_grade_calibration_activates_only_with_sufficient_support():
    sample_count = 120
    grades = np.ones(sample_count, dtype=int)
    payload = {"grades": grades}
    dimensions = {
        "mathCognitiveDomain": 3,
        "knowledgeDimension": 4,
        "intendedDifficulty": 3,
    }
    for head, class_count in dimensions.items():
        targets = np.arange(sample_count) % class_count
        logits = np.full((sample_count, class_count), -2.0)
        logits[np.arange(sample_count), targets] = 2.0
        payload[f"targets_{head}"] = targets
        payload[f"logits_{head}"] = logits
    calibration, metrics = calibration_from_validation(payload)
    for head in dimensions:
        assert "1" in calibration[head].perGrade
        assert calibration[head].perGrade["1"].confidenceThreshold > 0
        assert metrics[head]["perGrade"]["1"]["activated"] is True


def test_snapshot_stays_locked_when_grades_or_classes_are_missing():
    rows = [row(index, f"exercise-{index}") for index in range(24)]
    rows = [
        item.model_copy(update={"grade": 1, "intendedDifficulty": IntendedDifficulty.EASY})
        for item in rows
    ]
    snapshot = build_snapshot(rows, snapshot_id="locked-fixture")
    assert snapshot.testUnlockStatus == "locked"
    assert snapshot.researchOnly is True
    assert any("intendedDifficulty:Hard" in failure for failure in snapshot.gateFailures)
    assert any("grade:6=0<1" in failure for failure in snapshot.gateFailures)
