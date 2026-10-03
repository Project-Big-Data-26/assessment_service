"""Nominal agreement diagnostics for repeated AI judgments."""
from collections import Counter
from typing import Iterable, Sequence
import numpy as np

def percent_agreement(vote_matrix: Sequence[Sequence[str | None]]) -> float:
    agreements: list[float] = []
    for row in vote_matrix:
        values = [value for value in row if value is not None]
        if len(values) < 2:
            continue
        pairs = len(values) * (len(values) - 1) / 2
        same = sum(count * (count - 1) / 2 for count in Counter(values).values())
        agreements.append(same / pairs)
    return float(np.mean(agreements)) if agreements else float("nan")


def fleiss_kappa(vote_matrix: Sequence[Sequence[str | None]], labels: Iterable[str]) -> float:
    labels = tuple(labels)
    complete = [row for row in vote_matrix if len(row) >= 2 and all(value in labels for value in row)]
    if not complete:
        return float("nan")
    n_raters = len(complete[0])
    if any(len(row) != n_raters for row in complete):
        raise ValueError("Fleiss kappa requires a constant number of raters")
    counts = np.asarray([[row.count(label) for label in labels] for row in complete], dtype=float)
    observed = np.mean((np.square(counts).sum(axis=1) - n_raters) / (n_raters * (n_raters - 1)))
    category_rates = counts.sum(axis=0) / counts.sum()
    expected = float(np.square(category_rates).sum())
    return 1.0 if expected == 1.0 and observed == 1.0 else float((observed - expected) / (1.0 - expected))


def krippendorff_alpha_nominal(vote_matrix: Sequence[Sequence[str | None]]) -> float:
    rows = [[value for value in row if value is not None] for row in vote_matrix]
    rows = [row for row in rows if len(row) >= 2]
    if not rows:
        return float("nan")
    observed_disagreement = 1.0 - percent_agreement(rows)
    counts = Counter(value for row in rows for value in row)
    total = sum(counts.values())
    if total < 2:
        return float("nan")
    expected_agreement = sum(count * (count - 1) for count in counts.values()) / (total * (total - 1))
    expected_disagreement = 1.0 - expected_agreement
    if expected_disagreement == 0:
        return 1.0 if observed_disagreement == 0 else float("nan")
    return float(1.0 - observed_disagreement / expected_disagreement)
