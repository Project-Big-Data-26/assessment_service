"""Required non-neural baselines evaluated independently for each head."""

from __future__ import annotations

from collections import Counter
from typing import Any

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline

HEADS = ("mathCognitiveDomain", "knowledgeDimension", "intendedDifficulty")

KNOWING_KKO = {"menyebutkan", "mengidentifikasi", "mengenali", "menghitung", "membaca"}
APPLYING_KKO = {"menggunakan", "menentukan", "menyelesaikan", "menerapkan", "menghitung"}
REASONING_KKO = {"menganalisis", "menjelaskan", "membuktikan", "menyimpulkan", "mengevaluasi"}


def majority_baseline(train_rows: list[dict[str, Any]], evaluation_rows: list[dict[str, Any]]) -> dict[str, Any]:
    results: dict[str, Any] = {}
    for head in HEADS:
        label = Counter(row[head] for row in train_rows).most_common(1)[0][0]
        actual = [row[head] for row in evaluation_rows]
        predicted = [label] * len(actual)
        results[head] = classification_report(actual, predicted, output_dict=True, zero_division=0)
    return results


def tfidf_logistic_baseline(
    train_rows: list[dict[str, Any]], evaluation_rows: list[dict[str, Any]], *, seed: int = 42
) -> dict[str, Any]:
    results: dict[str, Any] = {}
    for head in HEADS:
        model = Pipeline(
            [
                ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=2, sublinear_tf=True)),
                ("classifier", LogisticRegression(max_iter=2000, class_weight="balanced", random_state=seed)),
            ]
        )
        model.fit([row["text"] for row in train_rows], [row[head] for row in train_rows])
        predicted = model.predict([row["text"] for row in evaluation_rows])
        results[head] = classification_report(
            [row[head] for row in evaluation_rows], predicted, output_dict=True, zero_division=0
        )
    return results


def cognitive_rules_baseline(evaluation_rows: list[dict[str, Any]]) -> dict[str, Any]:
    """Deliberately simple KKO baseline; it is not a gold-label generator."""
    actual: list[str] = []
    predicted: list[str] = []
    for row in evaluation_rows:
        text = row["text"].casefold()
        if any(token in text for token in REASONING_KKO):
            label = "reasoning"
        elif any(token in text for token in APPLYING_KKO):
            label = "applying"
        else:
            label = "knowing"
        actual.append(row["mathCognitiveDomain"])
        predicted.append(label)
    return classification_report(actual, predicted, output_dict=True, zero_division=0)


def frozen_indobert_linear_baseline(
    train_rows: list[dict[str, Any]],
    evaluation_rows: list[dict[str, Any]],
    *,
    model_id: str,
    revision: str,
    max_length: int = 256,
    seed: int = 42,
) -> dict[str, Any]:
    """Frozen encoder embeddings plus independent linear classifiers."""
    import torch
    from transformers import AutoModel, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)
    encoder = AutoModel.from_pretrained(model_id, revision=revision).cpu().eval()

    def embed(rows: list[dict[str, Any]]) -> np.ndarray:
        chunks = []
        with torch.inference_mode():
            for start in range(0, len(rows), 8):
                encoded = tokenizer(
                    [row["text"] for row in rows[start : start + 8]],
                    padding=True,
                    truncation=True,
                    max_length=max_length,
                    return_tensors="pt",
                )
                chunks.append(encoder(**encoded).last_hidden_state[:, 0].cpu().numpy())
        return np.concatenate(chunks)

    train_features = embed(train_rows)
    evaluation_features = embed(evaluation_rows)
    results: dict[str, Any] = {}
    for head in HEADS:
        classifier = LogisticRegression(
            max_iter=2000, class_weight="balanced", random_state=seed
        ).fit(train_features, [row[head] for row in train_rows])
        predicted = classifier.predict(evaluation_features)
        results[head] = classification_report(
            [row[head] for row in evaluation_rows], predicted, output_dict=True, zero_division=0
        )
    return results
