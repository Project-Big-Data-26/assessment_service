"""Shared IndoBERT encoder with trainable LoRA adapters and three heads."""

from __future__ import annotations

from typing import Any

import torch
from torch import nn

from .contracts import HEAD_LABELS

BASE_MODEL_ID = "indobenchmark/indobert-base-p1"
# This commit contains the actual PyTorch checkpoint.  The previously pinned
# 789e955... commit contains only config.json and cannot be loaded by
# AutoModel.from_pretrained.
BASE_MODEL_REVISION = "c2cd0b51ddce6580eb35263b39b0a1e5fb0a39e2"


class ThreeHeadIndoBERT(nn.Module):
    def __init__(self, encoder: nn.Module, hidden_size: int, dropout: float = 0.10) -> None:
        super().__init__()
        self.encoder = encoder
        self.dropout = nn.Dropout(dropout)
        self.heads = nn.ModuleDict(
            {
                name: nn.Linear(hidden_size, len(labels))
                for name, labels in HEAD_LABELS.items()
            }
        )

    @classmethod
    def from_pretrained_with_lora(
        cls,
        model_name_or_path: str,
        *,
        revision: str | None = None,
        rank: int = 8,
        alpha: int = 16,
        dropout: float = 0.10,
        local_files_only: bool = False,
    ) -> "ThreeHeadIndoBERT":
        from peft import LoraConfig, TaskType, get_peft_model
        from transformers import AutoConfig, AutoModel

        config = AutoConfig.from_pretrained(
            model_name_or_path, revision=revision, local_files_only=local_files_only
        )
        base = AutoModel.from_pretrained(
            model_name_or_path,
            revision=revision,
            config=config,
            local_files_only=local_files_only,
        )
        lora = LoraConfig(
            task_type=TaskType.FEATURE_EXTRACTION,
            r=rank,
            lora_alpha=alpha,
            lora_dropout=dropout,
            target_modules=["query", "value"],
            bias="none",
        )
        encoder = get_peft_model(base, lora)
        model = cls(encoder, config.hidden_size, dropout=dropout)
        model.assert_trainable_parameters()
        return model

    def assert_trainable_parameters(self) -> None:
        unexpected = [
            name
            for name, parameter in self.named_parameters()
            if parameter.requires_grad and "lora_" not in name and not name.startswith("heads.")
        ]
        if unexpected:
            raise RuntimeError(f"base encoder parameters unexpectedly trainable: {unexpected[:5]}")
        if not any(parameter.requires_grad for parameter in self.heads.parameters()):
            raise RuntimeError("classification heads are not trainable")

    def forward(
        self,
        input_ids: torch.Tensor,
        attention_mask: torch.Tensor,
        token_type_ids: torch.Tensor | None = None,
    ) -> dict[str, torch.Tensor]:
        inputs: dict[str, Any] = {"input_ids": input_ids, "attention_mask": attention_mask}
        if token_type_ids is not None:
            inputs["token_type_ids"] = token_type_ids
        outputs = self.encoder(**inputs)
        pooled = self.dropout(outputs.last_hidden_state[:, 0])
        return {name: head(pooled) for name, head in self.heads.items()}
