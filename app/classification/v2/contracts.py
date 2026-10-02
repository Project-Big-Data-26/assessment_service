"""Strict public and internal contracts for the 3x4x3 classifier."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, StringConstraints, model_validator


class CognitiveDomain(StrEnum):
    KNOWING = "knowing"
    APPLYING = "applying"
    REASONING = "reasoning"


class KnowledgeDimension(StrEnum):
    FACTUAL = "factual"
    CONCEPTUAL = "conceptual"
    PROCEDURAL = "procedural"
    METACOGNITIVE = "metacognitive"


class IntendedDifficulty(StrEnum):
    EASY = "Easy"
    MEDIUM = "Medium"
    HARD = "Hard"


HEAD_LABELS: dict[str, tuple[str, ...]] = {
    "mathCognitiveDomain": tuple(item.value for item in CognitiveDomain),
    "knowledgeDimension": tuple(item.value for item in KnowledgeDimension),
    "intendedDifficulty": tuple(item.value for item in IntendedDifficulty),
}

NonBlank = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


class QuestionOption(BaseModel):
    model_config = ConfigDict(extra="forbid")

    label: NonBlank
    text: NonBlank


class ProvenanceStatus(BaseModel):
    model_config = ConfigDict(extra="forbid")

    contentQualified: bool
    answerKeyVerified: bool
    solutionVerified: bool
    visualEssential: bool = False
    visualTranscriptVerified: bool = False


class V2ClassificationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    questionId: NonBlank
    contentVersion: Annotated[int, Field(ge=1)]
    contentHash: Annotated[str, StringConstraints(pattern=r"^[a-f0-9]{64}$")]
    grade: Annotated[int, Field(ge=1, le=12)]
    topic: str | None = None
    subtopic: str | None = None
    questionType: NonBlank
    stimulus: str | None = None
    stem: NonBlank
    options: list[QuestionOption] = Field(default_factory=list, max_length=8)
    verifiedMinimalSolution: str | None = None
    detectedKko: list[str] = Field(default_factory=list, max_length=20)
    visualTranscript: str | None = None
    provenanceStatus: ProvenanceStatus

    @model_validator(mode="after")
    def require_unique_option_labels(self) -> "V2ClassificationRequest":
        labels = [option.label.casefold() for option in self.options]
        if len(labels) != len(set(labels)):
            raise ValueError("option labels must be unique")
        return self


class HeadResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    label: str | None
    probabilities: dict[str, float]
    calibratedConfidence: float | None = Field(default=None, ge=0, le=1)
    normalizedEntropy: float | None = Field(default=None, ge=0, le=1)
    action: Literal["predict", "review", "abstain"]
    reasons: list[str] = Field(default_factory=list)


class ModelTrace(BaseModel):
    model_config = ConfigDict(extra="forbid")

    modelVersion: str
    baseModel: str
    baseRevision: str
    datasetSnapshot: str
    rubricVersion: str
    calibrationVersion: str
    inputSchemaVersion: str
    inputHash: str
    architectureVersion: str = "parallel-v1"
    routingPolicyVersion: str = "confidence-only-v1"


class V2ClassificationResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    questionId: str
    contentVersion: int
    contentHash: str
    scopeStatus: Literal["in_scope", "out_of_scope"]
    mathCognitiveDomain: HeadResult
    knowledgeDimension: HeadResult
    intendedDifficulty: HeadResult
    reviewRequired: Literal[True] = True
    reasons: list[str] = Field(default_factory=list)
    trace: ModelTrace
