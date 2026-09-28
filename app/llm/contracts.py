"""Strict contracts for Gemini's advisory review of IndoBERT output."""

from __future__ import annotations

from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, StringConstraints, model_validator

from app.classification.v2.contracts import (
    CognitiveDomain,
    IntendedDifficulty,
    KnowledgeDimension,
)

ShortText = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=600)]
EvidenceText = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=240)]


class _HeadReviewBase(BaseModel):
    model_config = ConfigDict(extra="forbid")

    action: Literal["confirm", "revise", "abstain"]
    evidenceSpans: list[EvidenceText] = Field(default_factory=list, max_length=4)
    rationale: ShortText

    def _validate_action(self, proposed_label: object | None) -> None:
        if self.action == "revise" and proposed_label is None:
            raise ValueError("revise requires proposedLabel")
        if self.action != "revise" and proposed_label is not None:
            raise ValueError("proposedLabel is allowed only for revise")
        if self.action != "abstain" and not self.evidenceSpans:
            raise ValueError("confirm/revise requires at least one evidence span")


class CognitiveHeadReview(_HeadReviewBase):
    proposedLabel: CognitiveDomain | None = None

    @model_validator(mode="after")
    def validate_action_and_label(self) -> "CognitiveHeadReview":
        self._validate_action(self.proposedLabel)
        return self


class KnowledgeHeadReview(_HeadReviewBase):
    proposedLabel: KnowledgeDimension | None = None

    @model_validator(mode="after")
    def validate_action_and_label(self) -> "KnowledgeHeadReview":
        self._validate_action(self.proposedLabel)
        return self


class DifficultyHeadReview(_HeadReviewBase):
    proposedLabel: IntendedDifficulty | None = None

    @model_validator(mode="after")
    def validate_action_and_label(self) -> "DifficultyHeadReview":
        self._validate_action(self.proposedLabel)
        return self


class GeminiReviewOutput(BaseModel):
    model_config = ConfigDict(extra="forbid")

    contentStatus: Literal["valid", "concern", "insufficient_evidence"]
    contentConcerns: list[ShortText] = Field(default_factory=list, max_length=6)
    mathCognitiveDomain: CognitiveHeadReview
    knowledgeDimension: KnowledgeHeadReview
    intendedDifficulty: DifficultyHeadReview


class TokenUsage(BaseModel):
    model_config = ConfigDict(extra="forbid")

    promptTokens: int = Field(default=0, ge=0)
    outputTokens: int = Field(default=0, ge=0)
    thinkingTokens: int = Field(default=0, ge=0)
    totalTokens: int = Field(default=0, ge=0)


class GeminiRunResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    runIndex: int = Field(ge=1)
    status: Literal["success", "failed"]
    review: GeminiReviewOutput | None = None
    errorCode: str | None = None
    responseId: str | None = None
    responseHash: str | None = None
    latencyMs: int = Field(ge=0)
    usage: TokenUsage = Field(default_factory=TokenUsage)


class SelfConsistencyHead(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: Literal["consistent", "no_consensus", "insufficient_runs"]
    suggestedAction: Literal["confirm", "revise", "abstain"] | None = None
    suggestedLabel: str | None = None
    supportingRuns: int = Field(default=0, ge=0)


class GeminiAdvisoryResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    provider: Literal["gemini"] = "gemini"
    model: str
    promptVersion: str
    rubricVersion: str
    runs: list[GeminiRunResult]
    mathCognitiveDomain: SelfConsistencyHead
    knowledgeDimension: SelfConsistencyHead
    intendedDifficulty: SelfConsistencyHead
    reviewRequired: Literal[True] = True
