"""Offline-only v2 inference with calibrated probabilities and abstention."""

from __future__ import annotations

import math
from pathlib import Path
from typing import Any

import numpy as np
import torch

from .artifact import ModelManifest, load_and_verify_manifest
from .calibration import normalized_entropy, softmax
from .contracts import HEAD_LABELS, HeadResult, ModelTrace, V2ClassificationRequest, V2ClassificationResponse
from .model import ThreeHeadIndoBERT
from .serializer import classification_input_hash, serialize_question


class ContentConflictError(ValueError):
    pass


class V2ClassifierRuntime:
    def __init__(self, artifact_dir: str | Path) -> None:
        self.artifact_dir = Path(artifact_dir)
        self.manifest = load_and_verify_manifest(self.artifact_dir)
        self.tokenizer: Any = None
        self.model: ThreeHeadIndoBERT | None = None
        self.failed_reason: str | None = None
        self._load()

    def _load(self) -> None:
        from peft import PeftModel
        from safetensors.torch import load_file
        from transformers import AutoConfig, AutoModel, AutoTokenizer

        tokenizer_path = self.artifact_dir / "tokenizer"
        base_path = self.artifact_dir / "base_model"
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_path, local_files_only=True)
        config = AutoConfig.from_pretrained(base_path, local_files_only=True)
        base = AutoModel.from_pretrained(base_path, config=config, local_files_only=True)
        encoder = PeftModel.from_pretrained(base, self.artifact_dir / "adapter", is_trainable=False)
        self.model = ThreeHeadIndoBERT(
            encoder,
            config.hidden_size,
            architecture_version=self.manifest.architectureVersion,
            detach_difficulty_conditioning=self.manifest.detachDifficultyConditioning,
            grade_embedding_dim=(
                self.manifest.gradeEmbeddingDimension
                if self.manifest.difficultyHeadType == "ordinal"
                else 16
            ),
            num_grades=self.manifest.gradeEmbeddingCount,
        )
        weights = load_file(str(self.artifact_dir / "heads.safetensors"), device="cpu")
        self.model.heads.load_state_dict(weights, strict=True)
        self.model.eval()

    def _trace(self, request: V2ClassificationRequest) -> ModelTrace:
        manifest = self.manifest
        return ModelTrace(
            modelVersion=manifest.modelVersion,
            baseModel=manifest.baseModel,
            baseRevision=manifest.baseRevision,
            datasetSnapshot=manifest.datasetSnapshot,
            rubricVersion=manifest.rubricVersion,
            calibrationVersion=manifest.calibrationVersion,
            inputSchemaVersion=manifest.inputSchemaVersion,
            inputHash=classification_input_hash(request, representation=manifest.inputRepresentation),
            architectureVersion=manifest.architectureVersion,
            routingPolicyVersion=manifest.routingPolicyVersion,
        )

    @staticmethod
    def _empty_head(reason: str) -> HeadResult:
        return HeadResult(label=None, probabilities={}, action="abstain", reasons=[reason])

    def _precondition_reasons(self, request: V2ClassificationRequest) -> list[str]:
        reasons: list[str] = []
        provenance = request.provenanceStatus
        if not provenance.contentQualified:
            reasons.append("content_not_qualified")
        if not provenance.answerKeyVerified:
            reasons.append("answer_key_not_verified")
        if not provenance.solutionVerified or not request.verifiedMinimalSolution:
            reasons.append("minimal_solution_not_verified")
        if provenance.visualEssential and (not provenance.visualTranscriptVerified or not request.visualTranscript):
            reasons.append("essential_visual_transcript_missing")
        return reasons

    def _validate_registered_version(self, request: V2ClassificationRequest) -> None:
        registered = self.manifest.contentRegistry.get(request.questionId)
        if not registered:
            return
        if registered.get("contentVersion") != request.contentVersion or registered.get("contentHash") != request.contentHash:
            raise ContentConflictError("content version/hash does not match the registered immutable version")

    def predict(self, request: V2ClassificationRequest) -> V2ClassificationResponse:
        self._validate_registered_version(request)
        trace = self._trace(request)
        if request.grade not in self.manifest.supportedGrades:
            reason = ("grade_outside_sd_v1" if self.manifest.supportedGrades == list(range(1, 7))
                      else "grade_outside_model_scope")
            empty = self._empty_head(reason)
            return V2ClassificationResponse(
                questionId=request.questionId,
                contentVersion=request.contentVersion,
                contentHash=request.contentHash,
                scopeStatus="out_of_scope",
                mathCognitiveDomain=empty,
                knowledgeDimension=empty.model_copy(deep=True),
                intendedDifficulty=empty.model_copy(deep=True),
                reasons=[reason],
                trace=trace,
            )
        if request.subjectTrack not in self.manifest.supportedSubjectTracks:
            empty = self._empty_head("subject_track_outside_model_scope")
            return V2ClassificationResponse(
                questionId=request.questionId, contentVersion=request.contentVersion,
                contentHash=request.contentHash, scopeStatus="out_of_scope",
                mathCognitiveDomain=empty, knowledgeDimension=empty.model_copy(deep=True),
                intendedDifficulty=empty.model_copy(deep=True),
                reasons=["subject_track_outside_model_scope"], trace=trace,
            )
        reasons = self._precondition_reasons(request)
        if reasons:
            empty = self._empty_head(";".join(reasons))
            return V2ClassificationResponse(
                questionId=request.questionId,
                contentVersion=request.contentVersion,
                contentHash=request.contentHash,
                scopeStatus="in_scope",
                mathCognitiveDomain=empty,
                knowledgeDimension=empty.model_copy(deep=True),
                intendedDifficulty=empty.model_copy(deep=True),
                reasons=reasons,
                trace=trace,
            )
        assert self.model is not None
        encoded = self.tokenizer(
            serialize_question(request, representation=self.manifest.inputRepresentation),
            return_tensors="pt",
            truncation=True,
            max_length=self.manifest.maxLength,
        )
        if int(encoded["input_ids"].shape[1]) >= self.manifest.maxLength:
            reasons.append("input_reached_truncation_limit")
        encoded["grades"] = torch.tensor([request.grade], dtype=torch.long)
        with torch.inference_mode():
            outputs = self.model(**encoded)
        head_results: dict[str, HeadResult] = {}
        for head, labels in HEAD_LABELS.items():
            logits = outputs[head].detach().cpu().numpy()
            global_calibration = self.manifest.calibration[head]
            calibration = global_calibration.perGradeTrack.get(
                f"{request.grade}:{request.subjectTrack}",
                global_calibration.perGrade.get(str(request.grade), global_calibration)
                if request.subjectTrack == "regular" else global_calibration,
            )
            probabilities = softmax(logits, calibration.temperature)[0]
            if not np.all(np.isfinite(probabilities)) or not math.isclose(float(probabilities.sum()), 1.0, abs_tol=1e-6):
                self.failed_reason = f"invalid_probability:{head}"
                raise FloatingPointError(self.failed_reason)
            index = int(np.argmax(probabilities))
            confidence = float(probabilities[index])
            entropy = normalized_entropy(probabilities)
            threshold = calibration.confidenceThreshold
            head_reasons = list(reasons)
            if self.manifest.routingPolicyVersion == "confidence-entropy-v1":
                entropy_threshold = calibration.entropyThreshold
                if threshold is None or threshold <= 0 or entropy_threshold is None:
                    head_reasons.append("selective_threshold_gate_not_met")
                else:
                    if confidence < threshold:
                        head_reasons.append("confidence_below_validation_threshold")
                    if entropy > entropy_threshold:
                        head_reasons.append("entropy_above_validation_threshold")
            else:
                if threshold is None or threshold <= 0:
                    head_reasons.append("selective_threshold_gate_not_met")
                elif confidence < threshold:
                    head_reasons.append("confidence_below_validation_threshold")
            action = "predict" if not head_reasons else "review"
            head_results[head] = HeadResult(
                label=labels[index],
                probabilities={label: float(probabilities[pos]) for pos, label in enumerate(labels)},
                calibratedConfidence=confidence,
                normalizedEntropy=entropy,
                action=action,
                reasons=head_reasons,
            )
        return V2ClassificationResponse(
            questionId=request.questionId,
            contentVersion=request.contentVersion,
            contentHash=request.contentHash,
            scopeStatus="in_scope",
            reasons=reasons,
            trace=trace,
            **head_results,
        )
