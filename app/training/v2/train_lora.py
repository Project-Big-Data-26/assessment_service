"""CPU-oriented LoRA training; frozen test access requires an explicit final flag."""

from __future__ import annotations

import argparse
import asyncio
import copy
import json
import random
import subprocess
import time
import uuid
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import torch
from sklearn.metrics import classification_report, confusion_matrix
from torch import nn
from torch.optim import AdamW
from torch.utils.data import DataLoader, Dataset
from transformers import AutoTokenizer, DataCollatorWithPadding

from app.classification.v2.artifact import (
    CalibrationSpec,
    GradeCalibrationSpec,
    ModelManifest,
    new_manifest,
    sha256_file,
    write_manifest,
)
from app.classification.v2.calibration import (
    brier_score,
    expected_calibration_error,
    fit_temperature,
    negative_log_likelihood,
    normalized_entropy,
    reliability_bins,
    select_routing_thresholds,
    softmax,
)
from app.classification.v2.contracts import HEAD_LABELS
from app.classification.v2.model import (
    BASE_MODEL_ID,
    BASE_MODEL_REVISION,
    CONDITIONED_DIFFICULTY_ARCHITECTURE,
    GRADE_AWARE_ORDINAL_ARCHITECTURE,
    PARALLEL_ARCHITECTURE,
    ThreeHeadIndoBERT,
)
from app.training.v2.dataset import DatasetSnapshot, serialized_training_examples

HEADS = tuple(HEAD_LABELS)


def seed_everything(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.use_deterministic_algorithms(True, warn_only=True)


class TokenizedRows(Dataset):
    def __init__(self, rows: list[dict[str, Any]], tokenizer: Any, max_length: int) -> None:
        self.rows = rows
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.label_maps = {head: {label: index for index, label in enumerate(labels)} for head, labels in HEAD_LABELS.items()}

    def __len__(self) -> int:
        return len(self.rows)

    def __getitem__(self, index: int) -> dict[str, Any]:
        row = self.rows[index]
        encoded = self.tokenizer(row["text"], truncation=True, max_length=self.max_length)
        encoded["grades"] = int(row["grade"])
        for head in HEADS:
            encoded[f"label_{head}"] = self.label_maps[head][row[head]]
        return encoded


@dataclass(frozen=True)
class TrialConfig:
    rank: int
    lora_lr: float
    architecture_version: str
    seed: int = 42
    head_lr: float = 1e-3
    batch_size: int = 2
    gradient_accumulation: int = 8
    epochs: int = 12
    patience: int = 2
    weight_decay: float = 0.01
    warmup_ratio: float = 0.10


def _class_weights(rows: list[dict[str, Any]], head: str) -> torch.Tensor:
    counts = Counter(row[head] for row in rows)
    total = len(rows)
    labels = HEAD_LABELS[head]
    missing = [label for label in labels if not counts[label]]
    if missing:
        raise ValueError(
            f"class-balanced loss requires every real class for {head}; "
            f"missing={missing}"
        )
    return torch.tensor(
        [total / (len(labels) * counts[label]) for label in labels],
        dtype=torch.float32,
    )


def label_coverage_failures(rows: list[dict[str, Any]]) -> list[str]:
    failures: list[str] = []
    for head, labels in HEAD_LABELS.items():
        counts = Counter(row[head] for row in rows)
        for label in labels:
            if not counts[label]:
                failures.append(f"train:{head}:{label}=0")
    return failures


def _ordinal_pos_weight(rows: list[dict[str, Any]]) -> torch.Tensor:
    label_to_index = {label: index for index, label in enumerate(HEAD_LABELS["intendedDifficulty"])}
    counts = Counter(row["intendedDifficulty"] for row in rows)
    missing = [label for label in label_to_index if not counts[label]]
    if missing:
        raise ValueError(
            "ordinal class-balanced loss requires Easy, Medium, and Hard; "
            f"missing={missing}"
        )
    values = torch.tensor(
        [label_to_index[row["intendedDifficulty"]] for row in rows], dtype=torch.long
    )
    weights: list[float] = []
    for boundary in (0, 1):
        positives = int((values > boundary).sum())
        negatives = len(values) - positives
        if positives == 0 or negatives == 0:
            weights.append(1.0)
        else:
            weights.append(negatives / positives)
    return torch.tensor(weights, dtype=torch.float32)


def ordinal_difficulty_loss(
    cumulative_logits: torch.Tensor,
    labels: torch.Tensor,
    pos_weight: torch.Tensor,
) -> torch.Tensor:
    targets = torch.stack(((labels > 0).float(), (labels > 1).float()), dim=-1)
    return torch.nn.functional.binary_cross_entropy_with_logits(
        cumulative_logits, targets, pos_weight=pos_weight
    )


def _batch_inputs(batch: dict[str, torch.Tensor]) -> dict[str, torch.Tensor]:
    return {
        key: value
        for key, value in batch.items()
        if key in {"input_ids", "attention_mask", "token_type_ids", "grades"}
    }


def evaluate(model: ThreeHeadIndoBERT, loader: DataLoader) -> tuple[dict[str, Any], dict[str, np.ndarray]]:
    model.eval()
    logits = {head: [] for head in HEADS}
    targets = {head: [] for head in HEADS}
    grades: list[np.ndarray] = []
    with torch.inference_mode():
        for batch in loader:
            output = model(**_batch_inputs(batch))
            grades.append(batch["grades"].cpu().numpy())
            for head in HEADS:
                logits[head].append(output[head].cpu().numpy())
                targets[head].append(batch[f"label_{head}"].cpu().numpy())
    arrays = {head: np.concatenate(logits[head]) for head in HEADS}
    target_arrays = {head: np.concatenate(targets[head]) for head in HEADS}
    grade_array = np.concatenate(grades)
    metrics: dict[str, Any] = {}
    for head, labels in HEAD_LABELS.items():
        predicted = arrays[head].argmax(axis=1)
        metrics[head] = classification_report(
            target_arrays[head],
            predicted,
            labels=list(range(len(labels))),
            target_names=list(labels),
            output_dict=True,
            zero_division=0,
        )
        metrics[head]["confusionMatrix"] = confusion_matrix(
            target_arrays[head], predicted, labels=list(range(len(labels)))
        ).tolist()
        metrics[head]["perGrade"] = {}
        for grade in sorted(set(map(int, grade_array))):
            selected = grade_array == grade
            metrics[head]["perGrade"][str(grade)] = classification_report(
                target_arrays[head][selected],
                predicted[selected],
                labels=list(range(len(labels))),
                target_names=list(labels),
                output_dict=True,
                zero_division=0,
            )
    payload = {
        **{f"logits_{head}": arrays[head] for head in HEADS},
        **{f"targets_{head}": target_arrays[head] for head in HEADS},
        "grades": grade_array,
    }
    return metrics, payload


def mean_macro_f1(metrics: dict[str, Any]) -> float:
    return float(np.mean([metrics[head]["macro avg"]["f1-score"] for head in HEADS]))


def candidate_diagnostics(
    metrics: dict[str, Any], payload: dict[str, np.ndarray]
) -> dict[str, Any]:
    failures: list[str] = []
    macro_f1 = {
        head: float(metrics[head]["macro avg"]["f1-score"]) for head in HEADS
    }
    for head, labels in HEAD_LABELS.items():
        for label in labels:
            report = metrics[head][label]
            if report["support"] > 0 and report["recall"] <= 0:
                failures.append(f"zero_recall:{head}:{label}")
    targets = payload["targets_intendedDifficulty"]
    counts = np.bincount(targets, minlength=len(HEAD_LABELS["intendedDifficulty"]))
    majority = int(np.argmax(counts))
    majority_predictions = np.full_like(targets, majority)
    majority_report = classification_report(
        targets,
        majority_predictions,
        labels=list(range(len(HEAD_LABELS["intendedDifficulty"]))),
        output_dict=True,
        zero_division=0,
    )
    majority_macro = float(majority_report["macro avg"]["f1-score"])
    if macro_f1["intendedDifficulty"] <= majority_macro:
        failures.append("difficulty_does_not_beat_majority_macro_f1")
    return {
        "passed": not failures,
        "failures": failures,
        "macroF1ByHead": macro_f1,
        "minimumHeadMacroF1": min(macro_f1.values()),
        "meanMacroF1": float(np.mean(list(macro_f1.values()))),
        "difficultyMajorityMacroF1": majority_macro,
    }


def candidate_selection_key(diagnostics: dict[str, Any]) -> tuple[int, float, float]:
    return (
        int(diagnostics["passed"]),
        float(diagnostics["minimumHeadMacroF1"]),
        float(diagnostics["meanMacroF1"]),
    )


def _optimizer(model: ThreeHeadIndoBERT, config: TrialConfig) -> AdamW:
    lora = [parameter for name, parameter in model.named_parameters() if parameter.requires_grad and "lora_" in name]
    heads = [parameter for name, parameter in model.named_parameters() if parameter.requires_grad and name.startswith("heads.")]
    if not lora or not heads:
        raise RuntimeError("expected trainable LoRA and head parameters")
    return AdamW(
        [
            {"params": lora, "lr": config.lora_lr, "weight_decay": config.weight_decay},
            {"params": heads, "lr": config.head_lr, "weight_decay": config.weight_decay},
        ]
    )


def run_trial(
    train_rows: list[dict[str, Any]],
    validation_rows: list[dict[str, Any]],
    tokenizer: Any,
    config: TrialConfig,
    *,
    max_length: int,
    output_dir: Path,
    resume: bool,
) -> tuple[ThreeHeadIndoBERT, dict[str, Any], dict[str, np.ndarray]]:
    seed_everything(config.seed)
    collator = DataCollatorWithPadding(tokenizer=tokenizer, return_tensors="pt")
    generator = torch.Generator().manual_seed(config.seed)
    train_loader = DataLoader(
        TokenizedRows(train_rows, tokenizer, max_length),
        batch_size=config.batch_size,
        shuffle=True,
        collate_fn=collator,
        generator=generator,
    )
    validation_loader = DataLoader(
        TokenizedRows(validation_rows, tokenizer, max_length),
        batch_size=config.batch_size,
        shuffle=False,
        collate_fn=collator,
    )
    model = ThreeHeadIndoBERT.from_pretrained_with_lora(
        BASE_MODEL_ID,
        revision=BASE_MODEL_REVISION,
        rank=config.rank,
        alpha=16,
        dropout=0.10,
        architecture_version=config.architecture_version,
        detach_difficulty_conditioning=True,
        grade_embedding_dim=16,
    ).cpu()
    optimizer = _optimizer(model, config)
    losses = {
        head: nn.CrossEntropyLoss(weight=_class_weights(train_rows, head))
        for head in ("mathCognitiveDomain", "knowledgeDimension")
    }
    if config.architecture_version != GRADE_AWARE_ORDINAL_ARCHITECTURE:
        losses["intendedDifficulty"] = nn.CrossEntropyLoss(
            weight=_class_weights(train_rows, "intendedDifficulty")
        )
    ordinal_pos_weight = _ordinal_pos_weight(train_rows)
    updates_per_epoch = max(1, int(np.ceil(len(train_loader) / config.gradient_accumulation)))
    total_updates = updates_per_epoch * config.epochs
    warmup_updates = max(1, int(total_updates * config.warmup_ratio))

    def lr_scale(step: int) -> float:
        if step < warmup_updates:
            return max(step, 1) / warmup_updates
        return max(0.0, (total_updates - step) / max(total_updates - warmup_updates, 1))

    scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_scale)
    checkpoint_path = output_dir / "checkpoint.pt"
    start_epoch = 0
    best_score = -1.0
    best_key: tuple[int, float, float] = (-1, -1.0, -1.0)
    best_state: dict[str, torch.Tensor] | None = None
    stale_epochs = 0
    history: list[dict[str, Any]] = []
    if resume and checkpoint_path.is_file():
        checkpoint = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
        model.load_state_dict(checkpoint["model"])
        optimizer.load_state_dict(checkpoint["optimizer"])
        scheduler.load_state_dict(checkpoint["scheduler"])
        start_epoch = checkpoint["epoch"] + 1
        best_score = checkpoint["bestScore"]
        best_key = tuple(checkpoint.get("bestKey", (0, best_score, best_score)))
        best_state = checkpoint["bestState"]
        stale_epochs = checkpoint["staleEpochs"]
        history = checkpoint["history"]
        random.setstate(checkpoint["pythonRandomState"])
        np.random.set_state(checkpoint["numpyRandomState"])
        torch.set_rng_state(checkpoint["torchRandomState"])
        if "dataLoaderGeneratorState" in checkpoint:
            generator.set_state(checkpoint["dataLoaderGeneratorState"])
    output_dir.mkdir(parents=True, exist_ok=True)
    for epoch in range(start_epoch, config.epochs):
        started = time.perf_counter()
        model.train()
        optimizer.zero_grad(set_to_none=True)
        total_loss = 0.0
        for batch_index, batch in enumerate(train_loader):
            output = model(**_batch_inputs(batch))
            loss = sum(
                losses[head](output[head], batch[f"label_{head}"])
                for head in ("mathCognitiveDomain", "knowledgeDimension")
            )
            if config.architecture_version == GRADE_AWARE_ORDINAL_ARCHITECTURE:
                loss = loss + ordinal_difficulty_loss(
                    output["intendedDifficultyOrdinalLogits"],
                    batch["label_intendedDifficulty"],
                    ordinal_pos_weight,
                )
            else:
                loss = loss + losses["intendedDifficulty"](
                    output["intendedDifficulty"], batch["label_intendedDifficulty"]
                )
            (loss / config.gradient_accumulation).backward()
            total_loss += float(loss.detach())
            if (batch_index + 1) % config.gradient_accumulation == 0 or batch_index + 1 == len(train_loader):
                torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
                optimizer.step()
                scheduler.step()
                optimizer.zero_grad(set_to_none=True)
        validation_metrics, validation_payload = evaluate(model, validation_loader)
        diagnostics = candidate_diagnostics(validation_metrics, validation_payload)
        score = float(diagnostics["meanMacroF1"])
        selection_key = candidate_selection_key(diagnostics)
        history.append(
            {
                "epoch": epoch,
                "trainingLoss": total_loss / max(len(train_loader), 1),
                "validationMeanMacroF1": score,
                "validationMinimumHeadMacroF1": diagnostics["minimumHeadMacroF1"],
                "antiCollapsePassed": diagnostics["passed"],
                "seconds": time.perf_counter() - started,
            }
        )
        if selection_key > best_key:
            best_score = score
            best_key = selection_key
            best_state = copy.deepcopy(model.state_dict())
            stale_epochs = 0
        else:
            stale_epochs += 1
        torch.save(
            {
                "epoch": epoch,
                "model": model.state_dict(),
                "optimizer": optimizer.state_dict(),
                "scheduler": scheduler.state_dict(),
                "bestScore": best_score,
                "bestKey": list(best_key),
                "bestState": best_state,
                "staleEpochs": stale_epochs,
                "history": history,
                "pythonRandomState": random.getstate(),
                "numpyRandomState": np.random.get_state(),
                "torchRandomState": torch.get_rng_state(),
                "dataLoaderGeneratorState": generator.get_state(),
                "config": config.__dict__,
            },
            checkpoint_path,
        )
        if stale_epochs >= config.patience:
            break
    if best_state is None:
        raise RuntimeError("training produced no checkpoint")
    model.load_state_dict(best_state)
    metrics, payload = evaluate(model, validation_loader)
    metrics["trainingHistory"] = history
    metrics["meanMacroF1"] = mean_macro_f1(metrics)
    metrics["candidateDiagnostics"] = candidate_diagnostics(metrics, payload)
    return model, metrics, payload


def calibration_from_validation(payload: dict[str, np.ndarray]) -> tuple[dict[str, CalibrationSpec], dict[str, Any]]:
    calibration: dict[str, CalibrationSpec] = {}
    metrics: dict[str, Any] = {}
    for head in HEADS:
        logits = payload[f"logits_{head}"]
        targets = payload[f"targets_{head}"]
        temperature = fit_temperature(logits, targets)
        probabilities = softmax(logits, temperature)
        confidence_threshold, entropy_threshold = select_routing_thresholds(
            probabilities,
            targets,
            require_all_classes=True,
            minimum_class_support=10,
            allow_zero_threshold=False,
        )
        grade_calibration: dict[str, GradeCalibrationSpec] = {}
        grade_metrics: dict[str, Any] = {}
        grades = payload["grades"]
        for grade in sorted(set(map(int, grades))):
            selected_grade = grades == grade
            grade_logits = logits[selected_grade]
            grade_targets = targets[selected_grade]
            counts = np.bincount(grade_targets, minlength=logits.shape[1])
            supported = bool(np.all(counts >= 10))
            grade_record: dict[str, Any] = {
                "supportByClass": counts.tolist(),
                "minimumClassSupportRequired": 10,
                "activated": False,
            }
            if supported:
                grade_temperature = fit_temperature(grade_logits, grade_targets)
                grade_probabilities = softmax(grade_logits, grade_temperature)
                grade_confidence, grade_entropy = select_routing_thresholds(
                    grade_probabilities,
                    grade_targets,
                    require_all_classes=True,
                    minimum_class_support=10,
                    allow_zero_threshold=False,
                )
                if grade_confidence is not None and grade_entropy is not None:
                    grade_calibration[str(grade)] = GradeCalibrationSpec(
                        temperature=grade_temperature,
                        confidenceThreshold=grade_confidence,
                        entropyThreshold=grade_entropy,
                    )
                    grade_record.update(
                        {
                            "activated": True,
                            "temperature": grade_temperature,
                            "confidenceThreshold": grade_confidence,
                            "entropyThreshold": grade_entropy,
                        }
                    )
            grade_metrics[str(grade)] = grade_record
        calibration[head] = CalibrationSpec(
            temperature=temperature,
            confidenceThreshold=confidence_threshold,
            entropyThreshold=entropy_threshold,
            perGrade=grade_calibration,
        )
        if confidence_threshold is None or entropy_threshold is None:
            selective_coverage = 0.0
            selective_accuracy = None
        else:
            confidence = probabilities.max(axis=1)
            entropy = np.asarray([normalized_entropy(row) for row in probabilities])
            selected = (confidence >= confidence_threshold) & (entropy <= entropy_threshold)
            selective_coverage = float(selected.mean())
            selective_accuracy = float(
                (probabilities.argmax(axis=1)[selected] == targets[selected]).mean()
            ) if selected.any() else None
        metrics[head] = {
            "temperature": temperature,
            "nllBefore": negative_log_likelihood(softmax(logits), targets),
            "nllAfter": negative_log_likelihood(probabilities, targets),
            "brier": brier_score(probabilities, targets),
            "ece": expected_calibration_error(probabilities, targets),
            "reliabilityBins": reliability_bins(probabilities, targets),
            "selectiveThreshold": confidence_threshold,
            "selectiveConfidenceThreshold": confidence_threshold,
            "selectiveEntropyThreshold": entropy_threshold,
            "selectiveCoverage": selective_coverage,
            "selectiveAccuracy": selective_accuracy,
            "perGrade": grade_metrics,
        }
    return calibration, metrics


def promotion_gate_failures(
    validation_metrics: dict[str, Any],
    calibration_metrics: dict[str, Any],
) -> list[str]:
    failures: list[str] = []
    for head in ("mathCognitiveDomain", "knowledgeDimension"):
        value = float(validation_metrics[head]["macro avg"]["f1-score"])
        if value < 0.70:
            failures.append(f"macro_f1:{head}={value:.4f}<0.70")
    difficulty_f1 = float(
        validation_metrics["intendedDifficulty"]["macro avg"]["f1-score"]
    )
    if difficulty_f1 < 0.65:
        failures.append(f"macro_f1:intendedDifficulty={difficulty_f1:.4f}<0.65")
    for head, labels in HEAD_LABELS.items():
        for label in labels:
            value = float(validation_metrics[head][label]["f1-score"])
            if value < 0.50:
                failures.append(f"class_f1:{head}:{label}={value:.4f}<0.50")
        ece = float(calibration_metrics[head]["ece"])
        if ece > 0.10:
            failures.append(f"ece:{head}={ece:.4f}>0.10")
        accuracy = calibration_metrics[head]["selectiveAccuracy"]
        coverage = float(calibration_metrics[head]["selectiveCoverage"])
        if accuracy is None or accuracy < 0.80:
            failures.append(f"selective_accuracy:{head}={accuracy}<0.80")
        if coverage < 0.70:
            failures.append(f"selective_coverage:{head}={coverage:.4f}<0.70")
    failures.extend(validation_metrics.get("candidateDiagnostics", {}).get("failures", []))
    stability = validation_metrics.get("threeSeedStability")
    if not stability or len(stability) != 3:
        failures.append("three_seed_stability_missing")
    else:
        values = [float(item["difficultyMacroF1"]) for item in stability]
        if min(values) < 0.65:
            failures.append(f"three_seed_min_difficulty_macro_f1={min(values):.4f}<0.65")
        if max(values) - min(values) > 0.10:
            failures.append(
                f"three_seed_difficulty_macro_f1_spread={max(values) - min(values):.4f}>0.10"
            )
        if not all(item["candidateDiagnostics"]["passed"] for item in stability):
            failures.append("three_seed_anti_collapse_failed")
    return list(dict.fromkeys(failures))


def package_artifact(
    model: ThreeHeadIndoBERT,
    tokenizer: Any,
    snapshot: DatasetSnapshot,
    validation_metrics: dict[str, Any],
    calibration: dict[str, CalibrationSpec],
    calibration_metrics: dict[str, Any],
    *,
    config: TrialConfig,
    max_length: int,
    output_dir: Path,
    model_version: str,
    rubric_version: str,
    input_representation: str,
    research_only: bool,
) -> ModelManifest:
    from safetensors.torch import save_file
    from transformers import AutoModel

    if (output_dir / "manifest.json").is_file():
        raise FileExistsError(
            f"refusing to overwrite immutable model artifact: {output_dir / 'manifest.json'}"
        )
    output_dir.mkdir(parents=True, exist_ok=True)
    tokenizer.save_pretrained(output_dir / "tokenizer")
    model.encoder.save_pretrained(output_dir / "adapter", safe_serialization=True)
    # Save a clean pinned encoder so ordinary inference is fully offline and does not
    # serialize PEFT wrapper names into the base checkpoint.
    clean_base = AutoModel.from_pretrained(BASE_MODEL_ID, revision=BASE_MODEL_REVISION)
    clean_base.save_pretrained(output_dir / "base_model", safe_serialization=True)
    del clean_base
    save_file({name: value.detach().cpu().contiguous() for name, value in model.heads.state_dict().items()}, str(output_dir / "heads.safetensors"))
    import matplotlib.pyplot as plt

    report_dir = output_dir / "reports"
    report_dir.mkdir(exist_ok=True)
    for head in HEADS:
        bins = calibration_metrics[head]["reliabilityBins"]
        confidence = [entry["meanConfidence"] for entry in bins if entry["count"]]
        accuracy = [entry["accuracy"] for entry in bins if entry["count"]]
        figure, axis = plt.subplots(figsize=(5, 5))
        axis.plot([0, 1], [0, 1], linestyle="--", color="gray", label="perfect")
        axis.plot(confidence, accuracy, marker="o", label=head)
        axis.set(xlabel="Calibrated confidence", ylabel="Empirical accuracy", xlim=(0, 1), ylim=(0, 1))
        axis.legend()
        figure.tight_layout()
        figure.savefig(report_dir / f"reliability-{head}.png", dpi=160)
        plt.close(figure)
    tracked = [
        path
        for path in output_dir.rglob("*")
        if path.is_file() and path.name not in {"manifest.json", "checkpoint.pt"}
    ]
    files = {path.relative_to(output_dir).as_posix(): sha256_file(path) for path in tracked}
    try:
        git_commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        git_commit = "unknown"
    provenance_kinds = sorted(
        {str(row.decisionProvenance.get("kind", "unknown")) for row in snapshot.rows}
    )
    prompt_versions = sorted(
        {
            str(row.decisionProvenance["promptVersion"])
            for row in snapshot.rows
            if row.decisionProvenance.get("promptVersion")
        }
    )
    split_by_id = {entry.questionVersionId: entry.split for entry in snapshot.splitManifest}
    data_distribution: dict[str, Any] = {}
    for split in ("train", "validation", "test"):
        selected = [
            row for row in snapshot.rows if split_by_id.get(row.questionVersionId) == split
        ]
        data_distribution[split] = {
            "count": len(selected),
            "grades": dict(Counter(str(row.grade) for row in selected)),
            "intendedDifficulty": dict(
                Counter(row.intendedDifficulty.value for row in selected)
            ),
        }
    anti_collapse = validation_metrics.get("candidateDiagnostics", {})
    data_gates_passed = not snapshot.gateFailures
    anti_collapse_passed = bool(anti_collapse.get("passed"))
    promotion_failures = promotion_gate_failures(
        validation_metrics, calibration_metrics
    )
    manifest = new_manifest(
        modelVersion=model_version,
        datasetSnapshot=snapshot.snapshotId,
        datasetHash=snapshot.snapshotHash,
        splitManifestHash=snapshot.splitManifestHash,
        rubricVersion=rubric_version,
        inputRepresentation=input_representation,
        architectureVersion=config.architecture_version,
        detachDifficultyConditioning=True,
        difficultyHeadType=(
            "ordinal"
            if config.architecture_version == GRADE_AWARE_ORDINAL_ARCHITECTURE
            else "multiclass"
        ),
        gradeEmbeddingDimension=(
            16 if config.architecture_version == GRADE_AWARE_ORDINAL_ARCHITECTURE else 0
        ),
        routingPolicyVersion="confidence-entropy-v1",
        calibrationVersion=f"{model_version}-temperature-v1",
        calibration=calibration,
        maxLength=max_length,
        loraRank=config.rank,
        files=files,
        metrics={
            "validation": validation_metrics,
            "calibration": calibration_metrics,
            "dataDistribution": data_distribution,
        },
        promotionGates={
            "macroF1Head1And2": 0.70,
            "macroF1Head3": 0.65,
            "perClassF1": 0.50,
            "eceEachHead": 0.10,
            "selectiveAccuracy": 0.80,
            "minimumCoverage": 0.70,
            "passed": not promotion_failures,
            "failures": promotion_failures,
        },
        researchOnly=research_only,
        dataGatesPassed=data_gates_passed,
        antiCollapsePassed=anti_collapse_passed,
        promptVersion=prompt_versions[0] if len(prompt_versions) == 1 else None,
        labelProvenance=";".join(provenance_kinds),
        gitCommit=git_commit,
        contentRegistry={
            row.questionId: {"contentVersion": row.contentVersion, "contentHash": row.contentHash}
            for row in snapshot.rows
        },
    )
    write_manifest(manifest, output_dir)
    return manifest


async def record_training_run(
    manifest: ModelManifest,
    *,
    trials: list[dict[str, Any]],
    final_seeds: list[dict[str, Any]],
    selected: TrialConfig,
) -> None:
    """Persist metadata only when Atlas is configured; never logs dataset content or secrets."""
    from app.staff.repository import MongoRepository, utc_now

    repository = MongoRepository.from_environment()
    if repository is None:
        return
    try:
        run_id = str(uuid.uuid4())
        await repository.db.training_runs.insert_one(
            {
                "trainingRunId": run_id,
                "modelVersion": manifest.modelVersion,
                "datasetSnapshot": manifest.datasetSnapshot,
                "datasetHash": manifest.datasetHash,
                "splitManifestHash": manifest.splitManifestHash,
                "selectedConfig": selected.__dict__,
                "searchTrials": trials,
                "finalSeeds": final_seeds,
                "metrics": manifest.metrics,
                "createdAt": utc_now(),
            }
        )
        await repository.db.model_versions.update_one(
            {"modelVersion": manifest.modelVersion},
            {"$setOnInsert": {**manifest.model_dump(mode="json"), "trainingRunId": run_id}},
            upsert=True,
        )
    finally:
        await repository.close()


def recommended_max_length(rows: list[dict[str, Any]], tokenizer: Any) -> int:
    lengths = [len(tokenizer(row["text"], truncation=False)["input_ids"]) for row in rows]
    return 384 if lengths and np.mean(np.asarray(lengths) > 256) > 0.05 else 256


def train(args: argparse.Namespace) -> dict[str, Any]:
    snapshot = DatasetSnapshot.model_validate_json(Path(args.snapshot).read_text(encoding="utf-8"))
    train_rows = serialized_training_examples(snapshot, "train", representation=args.representation)
    validation_rows = serialized_training_examples(snapshot, "validation", representation=args.representation)
    if not train_rows or not validation_rows:
        raise ValueError("snapshot must contain non-empty train and validation splits")
    coverage_failures = label_coverage_failures(train_rows)
    if coverage_failures:
        raise ValueError(
            "training class coverage gate failed: " + "; ".join(coverage_failures)
        )
    if snapshot.gateFailures and not args.allow_research_incomplete:
        raise ValueError(
            "snapshot is locked; pass --allow-research-incomplete only for diagnostics: "
            + "; ".join(snapshot.gateFailures)
        )
    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL_ID, revision=BASE_MODEL_REVISION)
    max_length = recommended_max_length([*train_rows, *validation_rows], tokenizer)
    trials = [
        TrialConfig(
            rank=rank,
            lora_lr=learning_rate,
            seed=42,
            architecture_version=args.architecture,
        )
        for rank in (8, 16)
        for learning_rate in (1e-4, 2e-4)
    ]
    if args.single_trial:
        trials = [
            TrialConfig(
                rank=args.rank,
                lora_lr=args.lora_lr,
                architecture_version=args.architecture,
                seed=args.seed,
                epochs=args.epochs,
                patience=args.patience,
            )
        ]
    summaries: list[dict[str, Any]] = []
    best: tuple[ThreeHeadIndoBERT, TrialConfig, dict[str, Any], dict[str, np.ndarray]] | None = None
    for trial in trials:
        trial_dir = (
            Path(args.work_dir)
            / f"{trial.architecture_version}-r{trial.rank}-lr{trial.lora_lr:g}-seed{trial.seed}"
        )
        model, metrics, payload = run_trial(
            train_rows,
            validation_rows,
            tokenizer,
            trial,
            max_length=max_length,
            output_dir=trial_dir,
            resume=args.resume,
        )
        summaries.append(
            {
                "config": trial.__dict__,
                "validationMeanMacroF1": metrics["meanMacroF1"],
                "candidateDiagnostics": metrics["candidateDiagnostics"],
            }
        )
        if best is None or candidate_selection_key(
            metrics["candidateDiagnostics"]
        ) > candidate_selection_key(best[2]["candidateDiagnostics"]):
            best = (model, trial, metrics, payload)
    assert best is not None
    model, config, metrics, payload = best
    final_seed_summaries: list[dict[str, Any]] = []
    if not args.single_trial:
        primary: tuple[ThreeHeadIndoBERT, TrialConfig, dict[str, Any], dict[str, np.ndarray]] | None = None
        for final_seed in (13, 42, 73):
            final_config = TrialConfig(
                rank=config.rank,
                lora_lr=config.lora_lr,
                architecture_version=config.architecture_version,
                seed=final_seed,
            )
            final_dir = (
                Path(args.work_dir)
                / f"final-{config.architecture_version}-r{config.rank}-lr{config.lora_lr:g}-seed{final_seed}"
            )
            final_model, final_metrics, final_payload = run_trial(
                train_rows,
                validation_rows,
                tokenizer,
                final_config,
                max_length=max_length,
                output_dir=final_dir,
                resume=args.resume,
            )
            final_seed_summaries.append(
                {
                    "seed": final_seed,
                    "validationMeanMacroF1": final_metrics["meanMacroF1"],
                    "difficultyMacroF1": final_metrics["intendedDifficulty"]["macro avg"]["f1-score"],
                    "candidateDiagnostics": final_metrics["candidateDiagnostics"],
                }
            )
            if final_seed == 42:
                primary = (final_model, final_config, final_metrics, final_payload)
        assert primary is not None
        model, config, metrics, payload = primary
        metrics["threeSeedStability"] = final_seed_summaries
    calibration, calibration_metrics = calibration_from_validation(payload)
    manifest = package_artifact(
        model,
        tokenizer,
        snapshot,
        metrics,
        calibration,
        calibration_metrics,
        config=config,
        max_length=max_length,
        output_dir=Path(args.output_dir),
        model_version=args.model_version,
        rubric_version=args.rubric_version,
        input_representation=args.representation,
        research_only=bool(
            args.allow_research_incomplete
            or snapshot.researchOnly
            or snapshot.gateFailures
            or not metrics.get("candidateDiagnostics", {}).get("passed", False)
        ),
    )
    asyncio.run(
        record_training_run(
            manifest,
            trials=summaries,
            final_seeds=final_seed_summaries,
            selected=config,
        )
    )
    return {
        "trials": summaries,
        "selected": config.__dict__,
        "finalSeeds": final_seed_summaries,
        "artifact": args.output_dir,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot", required=True)
    parser.add_argument("--output-dir", default="models/indobert-3x4x3-grade-aware-v2")
    parser.add_argument("--work-dir", default="runs/indobert-3x4x3-grade-aware-v2")
    parser.add_argument("--model-version", default="indobert-3x4x3-grade-aware-v2")
    parser.add_argument("--rubric-version", default="math-rubric-3x4x3-v2-grade-aware")
    parser.add_argument(
        "--representation",
        choices=("stem_options", "metadata", "solution", "kko"),
        default="solution",
        help="Use kko only after it wins validation and the same-KKO challenge set.",
    )
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--single-trial", action="store_true")
    parser.add_argument("--rank", type=int, choices=(8, 16), default=8)
    parser.add_argument("--lora-lr", type=float, choices=(1e-4, 2e-4), default=1e-4)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--epochs", type=int, default=12)
    parser.add_argument("--patience", type=int, default=2)
    parser.add_argument(
        "--allow-research-incomplete",
        action="store_true",
        help="Allow a diagnostic research-only artifact despite failed data gates.",
    )
    parser.add_argument(
        "--architecture",
        choices=(
            PARALLEL_ARCHITECTURE,
            CONDITIONED_DIFFICULTY_ARCHITECTURE,
            GRADE_AWARE_ORDINAL_ARCHITECTURE,
        ),
        default=GRADE_AWARE_ORDINAL_ARCHITECTURE,
        help=(
            "grade-aware-ordinal-v2 is the default research architecture; legacy and "
            "conditioned variants remain available only for controlled ablations"
        ),
    )
    return parser.parse_args()


if __name__ == "__main__":
    print(json.dumps(train(parse_args()), ensure_ascii=False, indent=2))
