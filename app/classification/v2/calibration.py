"""Per-head temperature scaling and selective-prediction utilities."""

from __future__ import annotations

import math
from collections.abc import Iterable

import numpy as np


def softmax(logits: np.ndarray, temperature: float = 1.0) -> np.ndarray:
    if not math.isfinite(temperature) or temperature <= 0:
        raise ValueError("temperature must be finite and positive")
    values = np.asarray(logits, dtype=np.float64) / temperature
    values -= np.max(values, axis=-1, keepdims=True)
    probabilities = np.exp(values)
    probabilities /= probabilities.sum(axis=-1, keepdims=True)
    if not np.all(np.isfinite(probabilities)):
        raise FloatingPointError("calibration produced invalid probabilities")
    return probabilities


def normalized_entropy(probabilities: Iterable[float]) -> float:
    values = np.asarray(tuple(probabilities), dtype=np.float64)
    if values.ndim != 1 or len(values) < 2 or not np.all(np.isfinite(values)):
        raise ValueError("probabilities must be a finite one-dimensional distribution")
    total = float(values.sum())
    if total <= 0:
        raise ValueError("probabilities must have a positive sum")
    values = values / total
    entropy = -float(np.sum(np.where(values > 0, values * np.log(values), 0.0)))
    return min(1.0, max(0.0, entropy / math.log(len(values))))


def negative_log_likelihood(probabilities: np.ndarray, labels: np.ndarray) -> float:
    chosen = probabilities[np.arange(len(labels)), labels]
    return float(-np.log(np.clip(chosen, 1e-12, 1.0)).mean())


def brier_score(probabilities: np.ndarray, labels: np.ndarray) -> float:
    targets = np.eye(probabilities.shape[1], dtype=np.float64)[labels]
    return float(np.square(probabilities - targets).sum(axis=1).mean())


def expected_calibration_error(
    probabilities: np.ndarray, labels: np.ndarray, *, bins: int = 15
) -> float:
    confidence = probabilities.max(axis=1)
    correct = probabilities.argmax(axis=1) == labels
    boundaries = np.linspace(0.0, 1.0, bins + 1)
    score = 0.0
    for index in range(bins):
        lower, upper = boundaries[index], boundaries[index + 1]
        included = (confidence > lower) & (confidence <= upper)
        if included.any():
            score += included.mean() * abs(float(correct[included].mean()) - float(confidence[included].mean()))
    return float(score)


def reliability_bins(
    probabilities: np.ndarray, labels: np.ndarray, *, bins: int = 15
) -> list[dict[str, float | int]]:
    confidence = probabilities.max(axis=1)
    correct = probabilities.argmax(axis=1) == labels
    boundaries = np.linspace(0.0, 1.0, bins + 1)
    result: list[dict[str, float | int]] = []
    for index in range(bins):
        lower, upper = float(boundaries[index]), float(boundaries[index + 1])
        included = (confidence > lower) & (confidence <= upper)
        result.append(
            {
                "lower": lower,
                "upper": upper,
                "count": int(included.sum()),
                "meanConfidence": float(confidence[included].mean()) if included.any() else 0.0,
                "accuracy": float(correct[included].mean()) if included.any() else 0.0,
            }
        )
    return result


def fit_temperature(logits: np.ndarray, labels: np.ndarray) -> float:
    """Fit one positive scalar on validation data only via bounded search."""
    logits = np.asarray(logits, dtype=np.float64)
    labels = np.asarray(labels, dtype=np.int64)
    if logits.ndim != 2 or len(logits) != len(labels) or len(labels) == 0:
        raise ValueError("logits and labels have incompatible shapes")
    candidates = np.geomspace(0.05, 10.0, 400)
    losses = [negative_log_likelihood(softmax(logits, value), labels) for value in candidates]
    best = float(candidates[int(np.argmin(losses))])
    # Never keep scaling if it makes validation NLL worse than the unscaled model.
    return best if min(losses) <= negative_log_likelihood(softmax(logits), labels) else 1.0


def select_confidence_threshold(
    probabilities: np.ndarray,
    labels: np.ndarray,
    *,
    target_accuracy: float = 0.80,
    minimum_coverage: float = 0.70,
) -> float | None:
    """Choose the lowest validation confidence threshold satisfying both gates."""
    confidence = probabilities.max(axis=1)
    correct = probabilities.argmax(axis=1) == labels
    candidates = sorted({0.0, *map(float, confidence)})
    feasible: list[float] = []
    for threshold in candidates:
        selected = confidence >= threshold
        if selected.mean() >= minimum_coverage and selected.any() and correct[selected].mean() >= target_accuracy:
            feasible.append(threshold)
    return min(feasible) if feasible else None


def select_routing_thresholds(
    probabilities: np.ndarray,
    labels: np.ndarray,
    *,
    target_accuracy: float = 0.80,
    minimum_coverage: float = 0.70,
    require_all_classes: bool = False,
    minimum_class_support: int = 1,
    allow_zero_threshold: bool = True,
) -> tuple[float | None, float | None]:
    """Select a joint confidence floor and normalized-entropy ceiling on validation only.

    The feasible pair with the highest coverage wins. Ties prefer the less
    restrictive pair so routing does not reject extra items without evidence.
    """
    probabilities = np.asarray(probabilities, dtype=np.float64)
    labels = np.asarray(labels, dtype=np.int64)
    if probabilities.ndim != 2 or len(probabilities) != len(labels) or len(labels) == 0:
        raise ValueError("probabilities and labels have incompatible shapes")
    if require_all_classes:
        supports = np.bincount(labels, minlength=probabilities.shape[1])
        if bool((supports < minimum_class_support).any()):
            return None, None
    confidence = probabilities.max(axis=1)
    entropy = np.asarray([normalized_entropy(row) for row in probabilities])
    correct = probabilities.argmax(axis=1) == labels
    confidence_candidates = sorted({0.0, *map(float, confidence)})
    if not allow_zero_threshold:
        confidence_candidates = [value for value in confidence_candidates if value > 0.0]
    # Use observed validation entropies rather than a universal ceiling of 1.0.
    # This keeps the policy data-derived and makes the entropy gate meaningful
    # for future samples that are more ambiguous than every accepted example.
    entropy_candidates = sorted(set(map(float, entropy)), reverse=True)
    feasible: list[tuple[float, float, float, float]] = []
    for confidence_threshold in confidence_candidates:
        for entropy_threshold in entropy_candidates:
            selected = (confidence >= confidence_threshold) & (entropy <= entropy_threshold)
            coverage = float(selected.mean())
            if coverage < minimum_coverage or not selected.any():
                continue
            accuracy = float(correct[selected].mean())
            if accuracy >= target_accuracy:
                feasible.append(
                    (coverage, -confidence_threshold, entropy_threshold, accuracy)
                )
    if not feasible:
        return None, None
    _, negative_confidence, entropy_threshold, _ = max(feasible)
    return -negative_confidence, entropy_threshold
