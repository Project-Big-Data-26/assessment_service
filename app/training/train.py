"""Fine-tune the three-head IndoBERT model on an approved, versioned dataset."""
from __future__ import annotations
import argparse
import hashlib
import json
import random
from datetime import datetime, timezone
from pathlib import Path
import numpy as np
import torch
from sklearn.model_selection import train_test_split
from torch import nn
from torch.optim import AdamW
from torch.utils.data import DataLoader, Dataset
from transformers import AutoTokenizer
from app.classification.indobert import BLOOM_LABELS, DIFFICULTY_LABELS, KNOWLEDGE_LABELS, IndoBERTMultiTaskModel
from app.evaluation import classification_metrics
from app.utils.dataset import load_question_dataset

class EncodedDataset(Dataset):
    def __init__(self, rows, tokenizer, max_length: int = 384):
        self.rows = rows; self.tokenizer = tokenizer; self.max_length = max_length
        self.bloom = {label: index for index, label in enumerate(BLOOM_LABELS)}
        self.knowledge = {label: index for index, label in enumerate(KNOWLEDGE_LABELS)}
        self.difficulty = {label: index for index, label in enumerate(DIFFICULTY_LABELS)}
    def __len__(self): return len(self.rows)
    def __getitem__(self, index):
        row = self.rows[index]
        encoded = self.tokenizer(row["question_text"], truncation=True, max_length=self.max_length, padding="max_length", return_tensors="pt")
        item = {key: value.squeeze(0) for key, value in encoded.items()}
        item.update({"bloom_label": torch.tensor(self.bloom[row["bloom_label"]]), "knowledge_label": torch.tensor(self.knowledge[row["knowledge_label"]]), "difficulty_label": torch.tensor(self.difficulty[row["difficulty_label"]])})
        return item

def seed_everything(seed: int):
    random.seed(seed); np.random.seed(seed); torch.manual_seed(seed)

def evaluate(model, loader, device):
    model.eval(); actual = {"bloom": [], "knowledge": [], "difficulty": []}; predicted = {key: [] for key in actual}
    with torch.inference_mode():
        for batch in loader:
            outputs = model(**{key: value.to(device) for key, value in batch.items() if key in {"input_ids", "attention_mask", "token_type_ids"}})
            for task in actual:
                actual[task].extend(batch[f"{task}_label"].tolist())
                predicted[task].extend(torch.argmax(outputs[f"{task}_logits"], dim=-1).cpu().tolist())
    label_sets = {"bloom": BLOOM_LABELS, "knowledge": KNOWLEDGE_LABELS, "difficulty": DIFFICULTY_LABELS}
    return {task: classification_metrics([label_sets[task][i] for i in actual[task]], [label_sets[task][i] for i in predicted[task]], labels=label_sets[task]) for task in actual}

def train(args):
    seed_everything(args.seed)
    frame = load_question_dataset(args.dataset)
    if len(frame) < 60 and not args.allow_small_demo: raise ValueError("At least 60 approved records are required. Use --allow-small-demo only for pipeline smoke tests.")
    rows = frame.to_dict(orient="records"); strata = [f"{r['bloom_label']}|{r['knowledge_label']}|{r['difficulty_label']}" for r in rows]
    try: train_rows, validation_rows = train_test_split(rows, test_size=args.validation_size, random_state=args.seed, stratify=strata)
    except ValueError: train_rows, validation_rows = train_test_split(rows, test_size=args.validation_size, random_state=args.seed)
    tokenizer = AutoTokenizer.from_pretrained(args.base_model)
    train_loader = DataLoader(EncodedDataset(train_rows, tokenizer), batch_size=args.batch_size, shuffle=True)
    validation_loader = DataLoader(EncodedDataset(validation_rows, tokenizer), batch_size=args.batch_size)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu"); model = IndoBERTMultiTaskModel(args.base_model).to(device)
    optimizer = AdamW(model.parameters(), lr=args.learning_rate); loss_fn = nn.CrossEntropyLoss()
    for _epoch in range(args.epochs):
        model.train()
        for batch in train_loader:
            inputs = {key: value.to(device) for key, value in batch.items() if key in {"input_ids", "attention_mask", "token_type_ids"}}
            outputs = model(**inputs)
            loss = sum(loss_fn(outputs[f"{task}_logits"], batch[f"{task}_label"].to(device)) for task in ("bloom", "knowledge", "difficulty"))
            optimizer.zero_grad(); loss.backward(); torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0); optimizer.step()
    metrics = evaluate(model, validation_loader, device)
    output = Path(args.output_dir); output.mkdir(parents=True, exist_ok=True); tokenizer.save_pretrained(output / "tokenizer")
    torch.save(model.cpu().state_dict(), output / "model.pt")
    digest = hashlib.sha256(Path(args.dataset).read_bytes()).hexdigest()
    manifest = {"model_version": args.model_version, "base_model": args.base_model, "created_at": datetime.now(timezone.utc).isoformat(), "dataset_sha256": digest, "dataset_rows": len(rows), "demo_only": len(rows) < 60, "approved_for_provisional": False, "labels": {"bloom": BLOOM_LABELS, "knowledge": KNOWLEDGE_LABELS, "difficulty": DIFFICULTY_LABELS}, "metrics": metrics}
    (output / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifest

def parse_args():
    parser = argparse.ArgumentParser(); parser.add_argument("--dataset", required=True); parser.add_argument("--output-dir", default="models/indobert-multitask-v1")
    parser.add_argument("--base-model", default="indobenchmark/indobert-base-p1"); parser.add_argument("--model-version", default="indobert-multitask-v1")
    parser.add_argument("--epochs", type=int, default=3); parser.add_argument("--batch-size", type=int, default=8); parser.add_argument("--learning-rate", type=float, default=2e-5)
    parser.add_argument("--validation-size", type=float, default=0.2); parser.add_argument("--seed", type=int, default=42); parser.add_argument("--allow-small-demo", action="store_true")
    return parser.parse_args()

if __name__ == "__main__": print(json.dumps(train(parse_args()), ensure_ascii=False, indent=2))
