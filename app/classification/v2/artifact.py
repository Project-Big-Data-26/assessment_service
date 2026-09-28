"""Versioned, checksum-verified model artifact manifest."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, model_validator

from .contracts import HEAD_LABELS
from .model import BASE_MODEL_ID, BASE_MODEL_REVISION
from .serializer import INPUT_SCHEMA_VERSION


class CalibrationSpec(BaseModel):
    temperature: float = Field(gt=0)
    confidenceThreshold: float | None = Field(default=None, ge=0, le=1)


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
    labels: dict[str, list[str]]
    calibration: dict[str, CalibrationSpec]
    maxLength: int = Field(default=256, ge=64, le=512)
    loraRank: int
    files: dict[str, str]
    metrics: dict[str, Any] = Field(default_factory=dict)
    promotionGates: dict[str, Any] = Field(default_factory=dict)
    approvedForProvisional: bool = False
    gitCommit: str
    contentRegistry: dict[str, dict[str, Any]] = Field(default_factory=dict)

    @model_validator(mode="after")
    def labels_are_exact(self) -> "ModelManifest":
        expected = {name: list(labels) for name, labels in HEAD_LABELS.items()}
        if self.labels != expected:
            raise ValueError("manifest label maps do not match the frozen 3x4x3 contract")
        if set(self.calibration) != set(HEAD_LABELS):
            raise ValueError("calibration must exist for all three heads")
        return self


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
