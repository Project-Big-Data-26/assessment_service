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

from app.classification.v2.artifact import CalibrationSpec, ModelManifest, new_manifest, sha256_file, write_manifest
from app.classification.v2.calibration import (
    brier_score,
    expected_calibration_error,
    fit_temperature,
    negative_log_likelihood,
    reliability_bins,
    select_confidence_threshold,
    softmax,
)
from app.classification.v2.contracts import HEAD_LABELS
from app.classification.v2.model import BASE_MODEL_ID, BASE_MODEL_REVISION, ThreeHeadIndoBERT
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
        for head in HEADS:
            encoded[f"label_{head}"] = self.label_maps[head][row[head]]
        return encoded


@dataclass(frozen=True)
class TrialConfig:
    rank: int
    lora_lr: float
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
    # A bootstrap/silver snapshot may not yet contain every frozen 3x4x3
    # class.  Keep the output head intact, but give absent targets zero loss
    # weight instead of dividing by zero.  The snapshot gate still records
    # the missing-class limitation and prevents research promotion.
    present_classes = sum(counts[label] > 0 for label in labels)
    if present_classes == 0:
        raise ValueError(f"training split has no labels for {head}")
    return torch.tensor(
        [
            total / (present_classes * counts[label]) if counts[label] else 0.0
            for label in labels
        ],
        dtype=torch.float32,
    )


def _batch_inputs(batch: dict[str, torch.Tensor]) -> dict[str, torch.Tensor]:
    return {key: value for key, value in batch.items() if key in {"input_ids", "attention_mask", "token_type_ids"}}


def evaluate(model: ThreeHeadIndoBERT, loader: DataLoader) -> tuple[dict[str, Any], dict[str, np.ndarray]]:
    model.eval()
    logits = {head: [] for head in HEADS}
    targets = {head: [] for head in HEADS}
    with torch.inference_mode():
        for batch in loader:
            output = model(**_batch_inputs(batch))
            for head in HEADS:
                logits[head].append(output[head].cpu().numpy())
                targets[head].append(batch[f"label_{head}"].cpu().numpy())
    arrays = {head: np.concatenate(logits[head]) for head in HEADS}
    target_arrays = {head: np.concatenate(targets[head]) for head in HEADS}
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
    payload = {**{f"logits_{head}": arrays[head] for head in HEADS}, **{f"targets_{head}": target_arrays[head] for head in HEADS}}
    return metrics, payload


def mean_macro_f1(metrics: dict[str, Any]) -> float:
    return float(np.mean([metrics[head]["macro avg"]["f1-score"] for head in HEADS]))


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
    ).cpu()
    optimizer = _optimizer(model, config)
    losses = {head: nn.CrossEntropyLoss(weight=_class_weights(train_rows, head)) for head in HEADS}
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
            loss = sum(losses[head](output[head], batch[f"label_{head}"]) for head in HEADS)
            (loss / config.gradient_accumulation).backward()
            total_loss += float(loss.detach())
            if (batch_index + 1) % config.gradient_accumulation == 0 or batch_index + 1 == len(train_loader):
                torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
                optimizer.step()
                scheduler.step()
                optimizer.zero_grad(set_to_none=True)
        validation_metrics, validation_payload = evaluate(model, validation_loader)
        score = mean_macro_f1(validation_metrics)
        history.append(
            {
                "epoch": epoch,
                "trainingLoss": total_loss / max(len(train_loader), 1),
                "validationMeanMacroF1": score,
                "seconds": time.perf_counter() - started,
            }
        )
        if score > best_score:
            best_score = score
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
    return model, metrics, payload


def calibration_from_validation(payload: dict[str, np.ndarray]) -> tuple[dict[str, CalibrationSpec], dict[str, Any]]:
    calibration: dict[str, CalibrationSpec] = {}
    metrics: dict[str, Any] = {}
    for head in HEADS:
        logits = payload[f"logits_{head}"]
        targets = payload[f"targets_{head}"]
        temperature = fit_temperature(logits, targets)
        probabilities = softmax(logits, temperature)
        threshold = select_confidence_threshold(probabilities, targets)
        calibration[head] = CalibrationSpec(temperature=temperature, confidenceThreshold=threshold)
        metrics[head] = {
            "temperature": temperature,
            "nllBefore": negative_log_likelihood(softmax(logits), targets),
            "nllAfter": negative_log_likelihood(probabilities, targets),
            "brier": brier_score(probabilities, targets),
            "ece": expected_calibration_error(probabilities, targets),
            "reliabilityBins": reliability_bins(probabilities, targets),
            "selectiveThreshold": threshold,
        }
    return calibration, metrics


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
) -> ModelManifest:
    from safetensors.torch import save_file
    from transformers import AutoModel

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
    manifest = new_manifest(
        modelVersion=model_version,
        datasetSnapshot=snapshot.snapshotId,
        datasetHash=snapshot.snapshotHash,
        splitManifestHash=snapshot.splitManifestHash,
        rubricVersion=rubric_version,
        inputRepresentation=input_representation,
        calibrationVersion=f"{model_version}-temperature-v1",
        calibration=calibration,
        maxLength=max_length,
        loraRank=config.rank,
        files=files,
        metrics={"validation": validation_metrics, "calibration": calibration_metrics},
        promotionGates={
            "macroF1Head1And2": 0.70,
            "macroF1Head3": 0.65,
            "perClassF1": 0.50,
            "eceEachHead": 0.10,
            "selectiveAccuracy": 0.80,
            "minimumCoverage": 0.70,
        },
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
    from app.annotation.repository import MongoAnnotationRepository, utc_now

    repository = MongoAnnotationRepository.from_environment()
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
    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL_ID, revision=BASE_MODEL_REVISION)
    max_length = recommended_max_length([*train_rows, *validation_rows], tokenizer)
    trials = [
        TrialConfig(rank=rank, lora_lr=learning_rate, seed=42)
        for rank in (8, 16)
        for learning_rate in (1e-4, 2e-4)
    ]
    if args.single_trial:
        trials = [
            TrialConfig(
                rank=args.rank,
                lora_lr=args.lora_lr,
                seed=args.seed,
                epochs=args.epochs,
                patience=args.patience,
            )
        ]
    summaries: list[dict[str, Any]] = []
    best: tuple[ThreeHeadIndoBERT, TrialConfig, dict[str, Any], dict[str, np.ndarray]] | None = None
    for trial in trials:
        trial_dir = Path(args.work_dir) / f"r{trial.rank}-lr{trial.lora_lr:g}-seed{trial.seed}"
        model, metrics, payload = run_trial(
            train_rows,
            validation_rows,
            tokenizer,
            trial,
            max_length=max_length,
            output_dir=trial_dir,
            resume=args.resume,
        )
        summaries.append({"config": trial.__dict__, "validationMeanMacroF1": metrics["meanMacroF1"]})
        if best is None or metrics["meanMacroF1"] > best[2]["meanMacroF1"]:
            best = (model, trial, metrics, payload)
    assert best is not None
    model, config, metrics, payload = best
    final_seed_summaries: list[dict[str, Any]] = []
    if not args.single_trial:
        primary: tuple[ThreeHeadIndoBERT, TrialConfig, dict[str, Any], dict[str, np.ndarray]] | None = None
        for final_seed in (13, 42, 73):
            final_config = TrialConfig(rank=config.rank, lora_lr=config.lora_lr, seed=final_seed)
            final_dir = Path(args.work_dir) / f"final-r{config.rank}-lr{config.lora_lr:g}-seed{final_seed}"
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
                {"seed": final_seed, "validationMeanMacroF1": final_metrics["meanMacroF1"]}
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
    parser.add_argument("--output-dir", default="models/indobert-3x4x3-v1")
    parser.add_argument("--work-dir", default="runs/indobert-3x4x3-v1")
    parser.add_argument("--model-version", default="indobert-3x4x3-v1")
    parser.add_argument("--rubric-version", default="math-rubric-3x4x3-v1")
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
    return parser.parse_args()


if __name__ == "__main__":
    print(json.dumps(train(parse_args()), ensure_ascii=False, indent=2))
