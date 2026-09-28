"""Open the frozen test once, evaluate calibrated v2, and leave promotion disabled."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, f1_score
from sklearn.pipeline import Pipeline
from collections import Counter

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.classification.v2.calibration import expected_calibration_error
from app.classification.v2.contracts import HEAD_LABELS
from app.classification.v2.runtime import V2ClassifierRuntime
from app.training.v2.dataset import DatasetSnapshot, serialized_training_examples
from app.classification.v2.model import BASE_MODEL_ID, BASE_MODEL_REVISION
from app.training.v2.baselines import APPLYING_KKO, REASONING_KKO


def frozen_predictions(train_rows, test_rows):
    import torch
    from transformers import AutoModel, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL_ID, revision=BASE_MODEL_REVISION)
    encoder = AutoModel.from_pretrained(BASE_MODEL_ID, revision=BASE_MODEL_REVISION).cpu().eval()

    def embed(rows):
        chunks = []
        with torch.inference_mode():
            for start in range(0, len(rows), 8):
                inputs = tokenizer(
                    [row["text"] for row in rows[start : start + 8]],
                    padding=True,
                    truncation=True,
                    max_length=256,
                    return_tensors="pt",
                )
                chunks.append(encoder(**inputs).last_hidden_state[:, 0].cpu().numpy())
        return np.concatenate(chunks)

    train_features, test_features = embed(train_rows), embed(test_rows)
    result = {}
    for head in HEAD_LABELS:
        classifier = LogisticRegression(max_iter=2000, class_weight="balanced", random_state=42)
        classifier.fit(train_features, [row[head] for row in train_rows])
        result[head] = classifier.predict(test_features)
    return result


def bootstrap_improvement(
    actual: dict[str, np.ndarray],
    model_predictions: dict[str, np.ndarray],
    baseline_predictions: dict[str, np.ndarray],
    *,
    samples: int = 5000,
) -> list[float]:
    generator = np.random.default_rng(42)
    count = len(next(iter(actual.values())))
    improvements = []
    for _ in range(samples):
        indices = generator.integers(0, count, size=count)
        model_score = np.mean(
            [f1_score(actual[head][indices], model_predictions[head][indices], average="macro") for head in HEAD_LABELS]
        )
        baseline_score = np.mean(
            [f1_score(actual[head][indices], baseline_predictions[head][indices], average="macro") for head in HEAD_LABELS]
        )
        improvements.append(model_score - baseline_score)
    return [float(np.percentile(improvements, 2.5)), float(np.percentile(improvements, 97.5))]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot", required=True)
    parser.add_argument("--artifact", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--unlock-frozen-test", action="store_true")
    parser.add_argument("--skip-frozen-indobert", action="store_true")
    args = parser.parse_args()
    if not args.unlock_frozen_test:
        raise SystemExit("frozen test remains locked; pass --unlock-frozen-test only after signed approval")
    destination = Path(args.output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    marker = destination.parent / "FROZEN_TEST_OPENED.json"
    if marker.exists():
        raise SystemExit(f"frozen test was already opened; see {marker}")
    snapshot = DatasetSnapshot.model_validate_json(Path(args.snapshot).read_text(encoding="utf-8"))
    if snapshot.testUnlockStatus != "eligible_to_unlock":
        raise SystemExit("class-count gate failed; frozen test may not be opened")
    runtime = V2ClassifierRuntime(args.artifact)
    representation = runtime.manifest.inputRepresentation
    train_rows = serialized_training_examples(snapshot, "train", representation=representation)
    # From this line onward the test labels are considered opened. Write first so
    # an interrupted evaluation cannot silently be repeated.
    marker.write_text(
        json.dumps(
            {
                "status": "opened_evaluation_incomplete",
                "snapshotId": snapshot.snapshotId,
                "snapshotHash": snapshot.snapshotHash,
                "splitManifestHash": snapshot.splitManifestHash,
                "modelVersion": runtime.manifest.modelVersion,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    test_rows = serialized_training_examples(snapshot, "test", representation=representation)
    rows_by_id = {row.questionVersionId: row for row in snapshot.rows}
    test_ids = [entry.questionVersionId for entry in snapshot.splitManifest if entry.split == "test"]
    actual = {head: np.asarray([row[head] for row in test_rows]) for head in HEAD_LABELS}
    predictions = {head: [] for head in HEAD_LABELS}
    probabilities = {head: [] for head in HEAD_LABELS}
    actions = {head: [] for head in HEAD_LABELS}
    for question_version_id in test_ids:
        response = runtime.predict(rows_by_id[question_version_id].inference_request())
        for head in HEAD_LABELS:
            result = getattr(response, head)
            predictions[head].append(result.label)
            probabilities[head].append([result.probabilities[label] for label in HEAD_LABELS[head]])
            actions[head].append(result.action)
    predictions_np = {head: np.asarray(values) for head, values in predictions.items()}

    tfidf_predictions: dict[str, np.ndarray] = {}
    majority_predictions: dict[str, np.ndarray] = {}
    rules_predictions: dict[str, np.ndarray] = {}
    for head in HEAD_LABELS:
        baseline = Pipeline(
            [
                ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=2, sublinear_tf=True)),
                ("classifier", LogisticRegression(max_iter=2000, class_weight="balanced", random_state=42)),
            ]
        )
        baseline.fit([row["text"] for row in train_rows], [row[head] for row in train_rows])
        tfidf_predictions[head] = baseline.predict([row["text"] for row in test_rows])
        majority = Counter(row[head] for row in train_rows).most_common(1)[0][0]
        majority_predictions[head] = np.asarray([majority] * len(test_rows))
        if head == "mathCognitiveDomain":
            choices = []
            for row in test_rows:
                text = row["text"].casefold()
                choices.append(
                    "reasoning"
                    if any(token in text for token in REASONING_KKO)
                    else "applying"
                    if any(token in text for token in APPLYING_KKO)
                    else "knowing"
                )
            rules_predictions[head] = np.asarray(choices)
        else:
            rules_predictions[head] = majority_predictions[head]
    frozen = None if args.skip_frozen_indobert else frozen_predictions(train_rows, test_rows)
    strongest_predictions: dict[str, np.ndarray] = {}

    report: dict[str, object] = {"split": "frozen_test", "heads": {}}
    technical_gates: list[bool] = []
    for head, labels in HEAD_LABELS.items():
        head_report = classification_report(
            actual[head], predictions_np[head], labels=list(labels), output_dict=True, zero_division=0
        )
        probabilities_np = np.asarray(probabilities[head])
        label_to_index = {label: index for index, label in enumerate(labels)}
        target_indices = np.asarray([label_to_index[label] for label in actual[head]])
        selected = np.asarray(actions[head]) == "predict"
        coverage = float(selected.mean())
        selective_accuracy = float((predictions_np[head][selected] == actual[head][selected]).mean()) if selected.any() else 0.0
        baseline_candidates = {
            "majority": majority_predictions[head],
            "rules": rules_predictions[head],
            "tfidfLogistic": tfidf_predictions[head],
        }
        if frozen is not None:
            baseline_candidates["frozenIndoBERTLinear"] = frozen[head]
        baseline_scores = {
            name: f1_score(actual[head], values, average="macro")
            for name, values in baseline_candidates.items()
        }
        strongest_name = max(baseline_scores, key=baseline_scores.get)
        baseline_macro = baseline_scores[strongest_name]
        strongest_predictions[head] = baseline_candidates[strongest_name]
        threshold = 0.65 if head == "intendedDifficulty" else 0.70
        class_gate = all(head_report[label]["f1-score"] >= 0.50 for label in labels)
        ece = expected_calibration_error(probabilities_np, target_indices)
        technical_gates.extend(
            [
                head_report["macro avg"]["f1-score"] >= threshold,
                class_gate,
                ece <= 0.10,
                head_report["macro avg"]["f1-score"] > baseline_macro,
                selective_accuracy >= 0.80 and coverage >= 0.70,
            ]
        )
        report["heads"][head] = {
            "classification": head_report,
            "ece": ece,
            "baselineMacroF1": baseline_scores,
            "strongestBaseline": strongest_name,
            "coverage": coverage,
            "selectiveAccuracy": selective_accuracy,
        }
    interval = bootstrap_improvement(actual, predictions_np, strongest_predictions)
    technical_gates.append(interval[0] >= 0.0)
    if args.skip_frozen_indobert:
        technical_gates.append(False)
        report["baselineWarning"] = "Frozen IndoBERT baseline skipped; promotion gate forced false."
    report["bootstrap95CIThreeHeadMacroF1ImprovementVsStrongestBaseline"] = interval
    report["technicalGatesPassed"] = all(technical_gates)
    report["approvedForProvisional"] = False
    report["approvalNote"] = "Technical evidence does not replace signed adviser/rubric approval."
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    marker.write_text(
        json.dumps(
            {
                "status": "completed",
                "snapshotId": snapshot.snapshotId,
                "snapshotHash": snapshot.snapshotHash,
                "splitManifestHash": snapshot.splitManifestHash,
                "modelVersion": runtime.manifest.modelVersion,
                "report": str(destination),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"Frozen-test report written once to {destination}; promotion remains disabled.")


if __name__ == "__main__":
    main()
