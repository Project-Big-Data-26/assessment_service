"""Pydantic records persisted by the expert annotation workflow."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

from app.classification.v2.contracts import (
    CognitiveDomain,
    IntendedDifficulty,
    KnowledgeDimension,
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class HeadAnnotation(BaseModel):
    model_config = ConfigDict(extra="forbid")

    label: str | None = None
    evidence: str | None = Field(default=None, max_length=4000)
    abstain: bool = False
    abstainReason: str | None = Field(default=None, max_length=1000)


class ExpertAnnotationInput(BaseModel):
    model_config = ConfigDict(extra="forbid")

    idempotencyKey: str = Field(min_length=8, max_length=128)
    contentValid: Literal["valid", "revision_required", "excluded", "insufficient_evidence"]
    answerKeyStatus: Literal["verified", "incorrect", "ambiguous", "insufficient_evidence"]
    verifiedAnswerKey: str | None = Field(default=None, max_length=100)
    minimalSolution: str | None = Field(default=None, max_length=8000)
    mathCognitiveDomain: HeadAnnotation
    knowledgeDimension: HeadAnnotation
    intendedDifficulty: HeadAnnotation

    @model_validator(mode="after")
    def validated_heads(self) -> "ExpertAnnotationInput":
        enums = {
            "mathCognitiveDomain": CognitiveDomain,
            "knowledgeDimension": KnowledgeDimension,
            "intendedDifficulty": IntendedDifficulty,
        }
        content_eligible = self.contentValid == "valid" and self.answerKeyStatus == "verified"
        for name, enum_type in enums.items():
            answer = getattr(self, name)
            if not content_eligible and not answer.abstain:
                raise ValueError(f"{name}: ineligible content must abstain before label assignment")
            if answer.abstain:
                if answer.label is not None or not answer.abstainReason:
                    raise ValueError(f"{name}: abstain requires reason and no label")
            else:
                if answer.label is None or not answer.evidence:
                    raise ValueError(f"{name}: label and evidence are required")
                enum_type(answer.label)
        if self.answerKeyStatus == "verified" and (not self.verifiedAnswerKey or not self.minimalSolution):
            raise ValueError("verified key requires verifiedAnswerKey and minimalSolution")
        return self


class ExpertAnnotationRecord(ExpertAnnotationInput):
    model_config = ConfigDict(extra="forbid")

    annotationId: str
    assignmentId: str
    expertId: str
    questionVersionId: str
    rubricVersion: str
    submittedAt: datetime = Field(default_factory=utc_now)
    immutable: Literal[True] = True


class AdjudicationDecisionInput(BaseModel):
    model_config = ConfigDict(extra="forbid")

    idempotencyKey: str = Field(min_length=8, max_length=128)
    mathCognitiveDomain: CognitiveDomain | None = None
    knowledgeDimension: KnowledgeDimension | None = None
    intendedDifficulty: IntendedDifficulty | None = None
    contentEligible: bool | None = None
    verifiedAnswerKey: str | None = Field(default=None, max_length=100)
    verifiedMinimalSolution: str | None = Field(default=None, max_length=8000)
    rationale: str = Field(min_length=3, max_length=8000)
    insufficientEvidence: bool = False

    @model_validator(mode="after")
    def require_complete_adjudication(self) -> "AdjudicationDecisionInput":
        if not self.insufficientEvidence:
            required = (
                self.mathCognitiveDomain,
                self.knowledgeDimension,
                self.intendedDifficulty,
                self.contentEligible,
                self.verifiedAnswerKey,
                self.verifiedMinimalSolution,
            )
            if any(value is None for value in required):
                raise ValueError("a non-quarantine decision must resolve content, key, solution, and all heads")
        return self


class DiscussionOutcomeInput(BaseModel):
    model_config = ConfigDict(extra="forbid")

    idempotencyKey: str = Field(min_length=8, max_length=128)
    mathCognitiveDomain: CognitiveDomain | None = None
    knowledgeDimension: KnowledgeDimension | None = None
    intendedDifficulty: IntendedDifficulty | None = None
    contentEligible: bool | None = None
    verifiedAnswerKey: str | None = Field(default=None, max_length=100)
    verifiedMinimalSolution: str | None = Field(default=None, max_length=8000)
    rationale: str = Field(min_length=3, max_length=8000)
    insufficientEvidence: bool = False
    participantExpertIds: list[str] = Field(min_length=3, max_length=3)
    unresolvedAfterDiscussion: bool

    @model_validator(mode="after")
    def discussion_state_is_consistent(self) -> "DiscussionOutcomeInput":
        if len(set(self.participantExpertIds)) != 3:
            raise ValueError("structured discussion requires three distinct primary experts")
        if self.unresolvedAfterDiscussion and any(
            value is not None
            for value in (self.mathCognitiveDomain, self.knowledgeDimension, self.intendedDifficulty)
        ):
            raise ValueError("unresolved discussion must not store a final label")
        if not self.unresolvedAfterDiscussion and not self.insufficientEvidence:
            required = (
                self.mathCognitiveDomain,
                self.knowledgeDimension,
                self.intendedDifficulty,
                self.contentEligible,
                self.verifiedAnswerKey,
                self.verifiedMinimalSolution,
            )
            if any(value is None for value in required):
                raise ValueError("resolved discussion must settle content, key, solution, and all heads")
        return self


class HeadConsensus(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: Literal["unanimous", "majority", "discussion_required", "adjudicated", "quarantined"]
    label: str | None
    voteCounts: dict[str, int]
    dissentingExpertIds: list[str] = Field(default_factory=list)
    reasons: list[str] = Field(default_factory=list)


class ContentConsensus(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: Literal["eligible", "discussion_required", "adjudicated", "quarantined"]
    verifiedAnswerKey: str | None = None
    verifiedMinimalSolution: str | None = None
    reasons: list[str] = Field(default_factory=list)


class ConsensusResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    questionVersionId: str
    content: ContentConsensus
    mathCognitiveDomain: HeadConsensus
    knowledgeDimension: HeadConsensus
    intendedDifficulty: HeadConsensus
    eligibleForGold: bool
    requiresAdjudication: bool
