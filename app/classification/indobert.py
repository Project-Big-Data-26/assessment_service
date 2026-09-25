"""Multi-task IndoBERT architecture for Bloom, knowledge, and difficulty heads."""
from __future__ import annotations
import json
from pathlib import Path
import torch
from torch import nn
from transformers import AutoConfig, AutoModel, AutoTokenizer
from app.classification.base import ClassificationPrediction

BLOOM_LABELS = ("C1", "C2", "C3", "C4", "C5", "C6")
KNOWLEDGE_LABELS = ("factual", "conceptual", "procedural", "metacognitive")
DIFFICULTY_LABELS = ("Easy", "Medium", "Hard")

class IndoBERTMultiTaskModel(nn.Module):
    """One shared Indonesian encoder with three independently evaluated heads."""
    def __init__(self, model_name: str = "indobenchmark/indobert-base-p1", dropout: float = 0.15) -> None:
        super().__init__()
        config = AutoConfig.from_pretrained(model_name)
        self.encoder = AutoModel.from_pretrained(model_name, config=config)
        hidden = config.hidden_size
        self.dropout = nn.Dropout(dropout)
        self.bloom_head = nn.Linear(hidden, len(BLOOM_LABELS))
        self.knowledge_head = nn.Linear(hidden, len(KNOWLEDGE_LABELS))
        self.difficulty_head = nn.Linear(hidden, len(DIFFICULTY_LABELS))

    def forward(self, input_ids, attention_mask, token_type_ids=None):
        outputs = self.encoder(input_ids=input_ids, attention_mask=attention_mask, token_type_ids=token_type_ids)
        pooled = self.dropout(outputs.last_hidden_state[:, 0])
        return {"bloom_logits": self.bloom_head(pooled), "knowledge_logits": self.knowledge_head(pooled), "difficulty_logits": self.difficulty_head(pooled)}

class IndoBERTClassifier:
    """Load a locally trained artifact; never downloads during ordinary inference."""
    def __init__(self, artifact_dir: str | Path, *, confidence_threshold: float = 0.7) -> None:
        self.artifact_dir = Path(artifact_dir)
        manifest_path, weights_path = self.artifact_dir / "manifest.json", self.artifact_dir / "model.pt"
        if not manifest_path.is_file() or not weights_path.is_file(): raise FileNotFoundError(f"IndoBERT artifact is incomplete: {self.artifact_dir}")
        self.manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        model_name = self.manifest["base_model"]
        self.tokenizer = AutoTokenizer.from_pretrained(self.artifact_dir / "tokenizer")
        self.model = IndoBERTMultiTaskModel(model_name=model_name)
        self.model.load_state_dict(torch.load(weights_path, map_location="cpu", weights_only=True))
        self.model.eval(); self.confidence_threshold = confidence_threshold

    def predict(self, question_text: str) -> ClassificationPrediction:
        encoded = self.tokenizer(question_text, return_tensors="pt", truncation=True, max_length=384)
        with torch.inference_mode(): outputs = self.model(**encoded)
        bloom, bloom_conf = self._decode(outputs["bloom_logits"], BLOOM_LABELS)
        knowledge, knowledge_conf = self._decode(outputs["knowledge_logits"], KNOWLEDGE_LABELS)
        difficulty, difficulty_conf = self._decode(outputs["difficulty_logits"], DIFFICULTY_LABELS)
        minimum = min(bloom_conf, knowledge_conf, difficulty_conf)
        return ClassificationPrediction(
            bloom_level=bloom, bloom_confidence=bloom_conf, knowledge_dimension=knowledge, knowledge_confidence=knowledge_conf,
            difficulty_level=difficulty, difficulty_confidence=difficulty_conf,
            model_version=self.manifest.get("model_version", "indobert-multitask-v1"),
            status="completed" if minimum >= self.confidence_threshold else "pending_review", prediction_source="indobert_multitask",
            rationale=(f"Minimum head confidence={minimum:.3f}",),
        )

    @staticmethod
    def _decode(logits: torch.Tensor, labels: tuple[str, ...]) -> tuple[str, float]:
        probabilities = torch.softmax(logits, dim=-1)[0]; index = int(torch.argmax(probabilities))
        return labels[index], float(probabilities[index])
