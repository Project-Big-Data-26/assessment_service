"""Classical item analysis with explicit assumptions and review flags."""
from __future__ import annotations
from math import sqrt
from statistics import median
from typing import Any
import numpy as np

def wilson_interval(correct: int, total: int, z: float = 1.96) -> tuple[float, float]:
    if total <= 0: raise ValueError("total must be positive")
    p = correct / total; denominator = 1 + z**2 / total
    center = (p + z**2 / (2 * total)) / denominator
    margin = z * sqrt((p * (1 - p) + z**2 / (4 * total)) / total) / denominator
    return max(0.0, center - margin), min(1.0, center + margin)

def weighted_kappa(left: list[str], right: list[str], labels: list[str]) -> float:
    if len(left) != len(right) or not left: raise ValueError("paired non-empty labels are required")
    index = {label: position for position, label in enumerate(labels)}; size = len(labels)
    observed = np.zeros((size, size), dtype=float)
    for a, b in zip(left, right, strict=True): observed[index[a], index[b]] += 1
    observed /= observed.sum(); row = observed.sum(axis=1); column = observed.sum(axis=0); expected = np.outer(row, column)
    weights = np.fromfunction(lambda i, j: ((i - j) / max(1, size - 1)) ** 2, (size, size))
    denominator = float((weights * expected).sum())
    return 1.0 if denominator == 0 else 1 - float((weights * observed).sum()) / denominator

def analyze_item(responses: list[dict[str, Any]], option_ids: list[str] | None = None) -> dict[str, Any]:
    valid = [response for response in responses if response.get("valid_for_analysis", True) and not response.get("rapid_guess", False)]
    if not valid: raise ValueError("at least one valid response is required")
    correct = sum(bool(response["is_correct"]) for response in valid); total = len(valid); p = correct / total
    lower, upper = wilson_interval(correct, total)
    ranked = sorted([response for response in valid if "total_score" in response], key=lambda item: item["total_score"], reverse=True)
    discrimination = None
    if len(ranked) >= 8:
        group = max(1, int(len(ranked) * 0.27)); top, bottom = ranked[:group], ranked[-group:]
        discrimination = sum(item["is_correct"] for item in top) / group - sum(item["is_correct"] for item in bottom) / group
    selections = {option: sum(response.get("selected_answer") == option for response in valid) for option in option_ids or []}
    key = next((response.get("selected_answer") for response in valid if response["is_correct"]), None)
    distractors = [option for option in option_ids or [] if option != key]
    functioning = [option for option in distractors if selections[option] / total >= 0.05]
    return {
        "valid_response_count": total, "difficulty_index": p, "difficulty_ci95": {"lower": lower, "upper": upper},
        "empirical_difficulty": "Easy" if p > 0.7 else "Hard" if p < 0.3 else "Medium",
        "discrimination_index": discrimination,
        "distractor_efficiency": len(functioning) / len(distractors) if distractors else None,
        "non_functioning_distractors": [option for option in distractors if option not in functioning],
        "median_response_time_ms": median(response["response_time_ms"] for response in valid),
        "rapid_guess_rate": sum(response.get("rapid_guess", False) for response in responses) / len(responses),
    }
