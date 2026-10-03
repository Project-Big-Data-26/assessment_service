"""Initial blind-vote agreement with bootstrap uncertainty intervals."""

from __future__ import annotations

import argparse
import asyncio
from collections import Counter, defaultdict
import json
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.evaluation.agreement import fleiss_kappa, krippendorff_alpha_nominal, percent_agreement
from app.staff.repository import MongoRepository
from app.classification.v2.contracts import HEAD_LABELS


def metrics(matrix: list[list[str | None]], labels: tuple[str, ...]) -> dict[str, float | None]:
    raw = {
        "percentAgreement": percent_agreement(matrix),
        "fleissKappa": fleiss_kappa(matrix, labels),
        "krippendorffAlphaNominal": krippendorff_alpha_nominal(matrix),
    }
    return {key: float(value) if np.isfinite(value) else None for key, value in raw.items()}


def bootstrap(matrix: list[list[str | None]], labels: tuple[str, ...], samples: int = 2000) -> dict[str, list[float] | None]:
    if not matrix:
        return {key: None for key in metrics(matrix, labels)}
    generator = np.random.default_rng(42)
    values = {key: [] for key in metrics(matrix, labels)}
    for _ in range(samples):
        indices = generator.integers(0, len(matrix), size=len(matrix))
        result = metrics([matrix[index] for index in indices], labels)
        for key, value in result.items():
            if value is not None and np.isfinite(value):
                values[key].append(value)
    return {
        key: [float(np.percentile(numbers, 2.5)), float(np.percentile(numbers, 97.5))]
        if numbers
        else None
        for key, numbers in values.items()
    }


def run() -> None:
    parser = argparse.ArgumentParser(description="Agreement among three blind AI runs")
    parser.add_argument("--checkpoint", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    cp = json.loads(Path(args.checkpoint).read_text(encoding="utf-8"))
    complete = [[r for r in item["runs"] if r["status"] == "success"] for item in cp["items"].values()]
    complete = [runs for runs in complete if len(runs) == 3]
    report = {"labelProvenance": "ai_silver", "itemsWithThreeInitialVotes": len(complete), "heads": {}}
    for head, labels in HEAD_LABELS.items():
        matrix = [[r["output"][head].get("label") for r in runs] for runs in complete]
        report["heads"][head] = {**metrics(matrix, labels), "bootstrap95CI": bootstrap(matrix, labels)}
    destination = Path(args.output)
    if destination.exists():
        raise FileExistsError("choose a new immutable report path")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False), encoding="utf-8")


if __name__ == "__main__":
    run()
