"""Versioned, checksum-verified model artifact manifest."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, model_validator

from .contracts import HEAD_LABELS
from .model import (
    BASE_MODEL_ID,
    BASE_MODEL_REVISION,
    CONDITIONED_DIFFICULTY_ARCHITECTURE,
    GRADE_AWARE_ORDINAL_ARCHITECTURE,
    PARALLEL_ARCHITECTURE,
)
from .serializer import INPUT_SCHEMA_VERSION


class GradeCalibrationSpec(BaseModel):
    temperature: float = Field(gt=0)
    confidenceThreshold: float = Field(gt=0, le=1)
    entropyThreshold: float = Field(ge=0, le=1)


class CalibrationSpec(BaseModel):
    temperature: float = Field(gt=0)
    confidenceThreshold: float | None = Field(default=None, ge=0, le=1)
    entropyThreshold: float | None = Field(default=None, ge=0, le=1)
    perGrade: dict[str, GradeCalibrationSpec] = Field(default_factory=dict)


class ModelManifest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    artifactFormatVersion: str = "indobert-3x4x3-artifact-v1"
    modelVersion: str
    createdAt: str
    baseModel: str = BASE_MODEL_ID
    baseRevision: str = BASE_MODEL_REVISION
    datasetSnapshot: str
    datasetHash: str
    splitManifestHash: str
    rubricVersion: str
    calibrationVersion: str
    inputSchemaVersion: str = INPUT_SCHEMA_VERSION
    inputRepresentation: str = Field(pattern=r"^(stem_options|metadata|solution|kko)$")
    architectureVersion: str = Field(
        default=PARALLEL_ARCHITECTURE,
        pattern=(
            rf"^({PARALLEL_ARCHITECTURE}|{CONDITIONED_DIFFICULTY_ARCHITECTURE}|"
            rf"{GRADE_AWARE_ORDINAL_ARCHITECTURE})$"
        ),
    )
    detachDifficultyConditioning: bool = True
    difficultyHeadType: str = Field(default="multiclass", pattern=r"^(multiclass|ordinal)$")
    gradeEmbeddingDimension: int = Field(default=0, ge=0, le=128)
    routingPolicyVersion: str = Field(
        default="confidence-only-v1",
        pattern=r"^(confidence-only-v1|confidence-entropy-v1)$",
    )
    labels: dict[str, list[str]]
    calibration: dict[str, CalibrationSpec]
    maxLength: int = Field(default=256, ge=64, le=512)
    loraRank: int
    files: dict[str, str]
    metrics: dict[str, Any] = Field(default_factory=dict)
    promotionGates: dict[str, Any] = Field(default_factory=dict)
    approvedForProvisional: bool = False
    researchOnly: bool = False
    dataGatesPassed: bool = False
    antiCollapsePassed: bool = False
    promptVersion: str | None = None
    labelProvenance: str = "unknown"
    gitCommit: str
    contentRegistry: dict[str, dict[str, Any]] = Field(default_factory=dict)

    @model_validator(mode="after")
    def labels_are_exact(self) -> "ModelManifest":
        expected = {name: list(labels) for name, labels in HEAD_LABELS.items()}
        if self.labels != expected:
            raise ValueError("manifest label maps do not match the frozen 3x4x3 contract")
        if set(self.calibration) != set(HEAD_LABELS):
            raise ValueError("calibration must exist for all three heads")
        if self.routingPolicyVersion == "confidence-entropy-v1":
            for head, calibration in self.calibration.items():
                has_confidence = calibration.confidenceThreshold is not None
                has_entropy = calibration.entropyThreshold is not None
                if has_confidence != has_entropy:
                    raise ValueError(
                        f"confidence and entropy thresholds must both exist or both be null: {head}"
                    )
                invalid_grades = sorted(
                    grade
                    for grade in calibration.perGrade
                    if grade not in {"1", "2", "3", "4", "5", "6"}
                )
                if invalid_grades:
                    raise ValueError(
                        f"per-grade calibration contains unsupported grades for {head}: "
                        f"{invalid_grades}"
                    )
        ordinal = self.architectureVersion == GRADE_AWARE_ORDINAL_ARCHITECTURE
        if ordinal != (self.difficultyHeadType == "ordinal"):
            raise ValueError("ordinal difficulty metadata does not match architecture")
        if ordinal and self.gradeEmbeddingDimension <= 0:
            raise ValueError("grade-aware ordinal artifacts require a grade embedding")
        return self

    @property
    def servable(self) -> bool:
        return bool(
            self.approvedForProvisional
            and not self.researchOnly
            and self.dataGatesPassed
            and self.antiCollapsePassed
            and self.promotionGates.get("passed") is True
        )


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_and_verify_manifest(artifact_dir: str | Path) -> ModelManifest:
    directory = Path(artifact_dir)
    path = directory / "manifest.json"
    if not path.is_file():
        raise FileNotFoundError(f"missing v2 model manifest: {path}")
    manifest = ModelManifest.model_validate_json(path.read_text(encoding="utf-8"))
    for relative, expected in manifest.files.items():
        candidate = directory / relative
        if not candidate.is_file():
            raise FileNotFoundError(f"artifact file is missing: {candidate}")
        actual = sha256_file(candidate)
        if actual != expected:
            raise ValueError(f"artifact checksum mismatch: {relative}")
    return manifest


def new_manifest(**values: Any) -> ModelManifest:
    return ModelManifest(
        createdAt=datetime.now(timezone.utc).isoformat(),
        labels={name: list(labels) for name, labels in HEAD_LABELS.items()},
        approvedForProvisional=False,
        **values,
    )


def write_manifest(manifest: ModelManifest, artifact_dir: str | Path) -> None:
    path = Path(artifact_dir) / "manifest.json"
    path.write_text(json.dumps(manifest.model_dump(mode="json"), ensure_ascii=False, indent=2), encoding="utf-8")
