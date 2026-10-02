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

from app.annotation.consensus import fleiss_kappa, krippendorff_alpha_nominal, percent_agreement
from app.annotation.repository import MongoAnnotationRepository
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


async def run() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rubric-version", default="math-rubric-3x4x3-v1")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    repository = MongoAnnotationRepository.from_environment()
    if repository is None:
        raise SystemExit("MONGODB_URI and MONGODB_DATABASE must be configured")
    grouped = defaultdict(list)
    try:
        cursor = repository.db.expert_annotations.find(
            {"rubricVersion": args.rubric_version}, {"_id": 0}
        ).sort([("questionVersionId", 1), ("expertId", 1)])
        async for document in cursor:
            grouped[document["questionVersionId"]].append(document)
        report = {"rubricVersion": args.rubric_version, "itemsWithThreeInitialVotes": 0, "heads": {}}
        complete = [records for records in grouped.values() if len(records) == 3]
        report["itemsWithThreeInitialVotes"] = len(complete)
        for head, labels in HEAD_LABELS.items():
            matrix = [
                [None if record[head]["abstain"] else record[head]["label"] for record in records]
                for records in complete
            ]
            patterns = Counter(
                "-".join(sorted(str(value or "abstain") for value in row)) for row in matrix
            )
            report["heads"][head] = {
                **metrics(matrix, labels),
                "bootstrap95CI": bootstrap(matrix, labels),
                "disagreementPatterns": dict(patterns),
            }
        destination = Path(args.output)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(
            json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False), encoding="utf-8"
        )
        print(f"Agreement report written to {destination}.")
    finally:
        await repository.close()


if __name__ == "__main__":
    asyncio.run(run())
