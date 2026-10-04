"""Shared IndoBERT encoder with trainable LoRA adapters and three heads."""

from __future__ import annotations

import math
from typing import Any

import torch
from torch import nn

from .contracts import HEAD_LABELS

BASE_MODEL_ID = "indobenchmark/indobert-base-p1"
# This commit contains the actual PyTorch checkpoint.  The previously pinned
# 789e955... commit contains only config.json and cannot be loaded by
# AutoModel.from_pretrained.
BASE_MODEL_REVISION = "c2cd0b51ddce6580eb35263b39b0a1e5fb0a39e2"

PARALLEL_ARCHITECTURE = "parallel-v1"
CONDITIONED_DIFFICULTY_ARCHITECTURE = "conditioned-difficulty-v1"
GRADE_AWARE_ORDINAL_ARCHITECTURE = "grade-aware-ordinal-v2"
SUPPORTED_ARCHITECTURES = {
    PARALLEL_ARCHITECTURE,
    CONDITIONED_DIFFICULTY_ARCHITECTURE,
    GRADE_AWARE_ORDINAL_ARCHITECTURE,
}


class GradeAwareOrdinalDifficultyHead(nn.Module):
    """Cumulative-link head with ordered cutpoints for Easy < Medium < Hard."""

    def __init__(self, hidden_size: int, grade_embedding_dim: int = 16, num_grades: int = 6) -> None:
        super().__init__()
        self.in_features = hidden_size + grade_embedding_dim
        self.grade_embedding_dim = grade_embedding_dim
        if not 1 <= num_grades <= 12:
            raise ValueError("num_grades must be between 1 and 12")
        self.num_grades = num_grades
        self.grade_embedding = nn.Embedding(num_grades, grade_embedding_dim)
        self.scorer = nn.Linear(self.in_features, 1)
        self.first_cutpoint = nn.Parameter(torch.tensor(-0.5))
        # Start with a two-logit-unit interval so the middle category has a
        # meaningful decision region instead of being dominated by both tails.
        self.cutpoint_gap = nn.Parameter(torch.tensor(math.log(math.expm1(2.0))))

    def ordered_cutpoints(self) -> torch.Tensor:
        second = self.first_cutpoint + torch.nn.functional.softplus(self.cutpoint_gap) + 1e-4
        return torch.stack((self.first_cutpoint, second))

    def forward(
        self, pooled: torch.Tensor, grades: torch.Tensor
    ) -> tuple[torch.Tensor, torch.Tensor]:
        if grades.ndim != 1 or grades.shape[0] != pooled.shape[0]:
            raise ValueError("grades must be a one-dimensional tensor matching the batch")
        if bool(((grades < 1) | (grades > self.num_grades)).any()):
            raise ValueError(f"grade-aware ordinal head supports grades 1-{self.num_grades}")
        embedded_grade = self.grade_embedding(grades.long() - 1)
        score = self.scorer(torch.cat((pooled, embedded_grade), dim=-1)).squeeze(-1)
        cumulative_logits = score.unsqueeze(-1) - self.ordered_cutpoints().unsqueeze(0)
        above = torch.sigmoid(cumulative_logits)
        probabilities = torch.stack(
            (1.0 - above[:, 0], above[:, 0] - above[:, 1], above[:, 1]), dim=-1
        )
        probabilities = probabilities.clamp_min(torch.finfo(probabilities.dtype).eps)
        probabilities = probabilities / probabilities.sum(dim=-1, keepdim=True)
        return probabilities.log(), cumulative_logits


class ThreeHeadIndoBERT(nn.Module):
    def __init__(
        self,
        encoder: nn.Module,
        hidden_size: int,
        dropout: float = 0.10,
        *,
        architecture_version: str = PARALLEL_ARCHITECTURE,
        detach_difficulty_conditioning: bool = True,
        grade_embedding_dim: int = 16,
        num_grades: int = 6,
    ) -> None:
        super().__init__()
        if architecture_version not in SUPPORTED_ARCHITECTURES:
            raise ValueError(f"unsupported architecture: {architecture_version}")
        self.encoder = encoder
        self.dropout = nn.Dropout(dropout)
        self.architecture_version = architecture_version
        self.detach_difficulty_conditioning = detach_difficulty_conditioning
        difficulty_input_size = hidden_size
        if architecture_version == CONDITIONED_DIFFICULTY_ARCHITECTURE:
            difficulty_input_size += len(HEAD_LABELS["mathCognitiveDomain"])
            difficulty_input_size += len(HEAD_LABELS["knowledgeDimension"])
        difficulty_head: nn.Module
        if architecture_version == GRADE_AWARE_ORDINAL_ARCHITECTURE:
            difficulty_head = GradeAwareOrdinalDifficultyHead(
                hidden_size, grade_embedding_dim=grade_embedding_dim, num_grades=num_grades
            )
        else:
            difficulty_head = nn.Linear(
                difficulty_input_size, len(HEAD_LABELS["intendedDifficulty"])
            )
        self.heads = nn.ModuleDict(
            {
                "mathCognitiveDomain": nn.Linear(
                    hidden_size, len(HEAD_LABELS["mathCognitiveDomain"])
                ),
                "knowledgeDimension": nn.Linear(
                    hidden_size, len(HEAD_LABELS["knowledgeDimension"])
                ),
                "intendedDifficulty": difficulty_head,
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
        architecture_version: str = PARALLEL_ARCHITECTURE,
        detach_difficulty_conditioning: bool = True,
        grade_embedding_dim: int = 16,
        num_grades: int = 6,
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
        model = cls(
            encoder,
            config.hidden_size,
            dropout=dropout,
            architecture_version=architecture_version,
            detach_difficulty_conditioning=detach_difficulty_conditioning,
            grade_embedding_dim=grade_embedding_dim,
            num_grades=num_grades,
        )
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
        grades: torch.Tensor | None = None,
    ) -> dict[str, torch.Tensor]:
        inputs: dict[str, Any] = {"input_ids": input_ids, "attention_mask": attention_mask}
        if token_type_ids is not None:
            inputs["token_type_ids"] = token_type_ids
        outputs = self.encoder(**inputs)
        pooled = self.dropout(outputs.last_hidden_state[:, 0])
        cognitive_logits = self.heads["mathCognitiveDomain"](pooled)
        knowledge_logits = self.heads["knowledgeDimension"](pooled)
        difficulty_input = pooled
        if self.architecture_version == CONDITIONED_DIFFICULTY_ARCHITECTURE:
            cognitive_probabilities = torch.softmax(cognitive_logits, dim=-1)
            knowledge_probabilities = torch.softmax(knowledge_logits, dim=-1)
            if self.detach_difficulty_conditioning:
                cognitive_probabilities = cognitive_probabilities.detach()
                knowledge_probabilities = knowledge_probabilities.detach()
            difficulty_input = torch.cat(
                [pooled, cognitive_probabilities, knowledge_probabilities], dim=-1
            )
        result = {
            "mathCognitiveDomain": cognitive_logits,
            "knowledgeDimension": knowledge_logits,
        }
        if self.architecture_version == GRADE_AWARE_ORDINAL_ARCHITECTURE:
            if grades is None:
                raise ValueError("grades are required by grade-aware-ordinal-v2")
            difficulty_logits, ordinal_logits = self.heads["intendedDifficulty"](
                pooled, grades
            )
            result["intendedDifficultyOrdinalLogits"] = ordinal_logits
        else:
            difficulty_logits = self.heads["intendedDifficulty"](difficulty_input)
        result["intendedDifficulty"] = difficulty_logits
        return result
