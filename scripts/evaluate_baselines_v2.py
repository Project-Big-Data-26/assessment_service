"""Evaluate all preregistered baselines on validation only."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.classification.v2.model import BASE_MODEL_ID, BASE_MODEL_REVISION
from app.training.v2.baselines import (
    cognitive_rules_baseline,
    frozen_indobert_linear_baseline,
    majority_baseline,
    tfidf_logistic_baseline,
)
from app.training.v2.dataset import DatasetSnapshot, serialized_training_examples


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--skip-frozen-indobert", action="store_true")
    parser.add_argument(
        "--representation", choices=("stem_options", "metadata", "solution", "kko"), default="solution"
    )
    args = parser.parse_args()
    snapshot = DatasetSnapshot.model_validate_json(Path(args.snapshot).read_text(encoding="utf-8"))
    train = serialized_training_examples(snapshot, "train", representation=args.representation)
    validation = serialized_training_examples(snapshot, "validation", representation=args.representation)
    report = {
        "evaluationSplit": "validation",
        "inputRepresentation": args.representation,
        "majority": majority_baseline(train, validation),
        "cognitiveRules": cognitive_rules_baseline(validation),
        "tfidfLogistic": tfidf_logistic_baseline(train, validation),
    }
    if not args.skip_frozen_indobert:
        report["frozenIndoBERTLinear"] = frozen_indobert_linear_baseline(
            train,
            validation,
            model_id=BASE_MODEL_ID,
            revision=BASE_MODEL_REVISION,
        )
    destination = Path(args.output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Validation baseline report written to {destination}.")


if __name__ == "__main__":
    main()
