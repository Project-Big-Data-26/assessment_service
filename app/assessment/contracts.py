from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field, model_validator

from app.psychometrics.contracts import StrictRecord


class AssessmentCreate(StrictRecord):
    assessmentId: str = Field(min_length=3, max_length=150)
    snapshotId: str = Field(min_length=1, max_length=200)
    questionVersionIds: list[str] = Field(min_length=1, max_length=200)
    populationId: str = Field(min_length=1, max_length=100)
    assessmentFamily: str = Field(min_length=1, max_length=100)
    grade: int = Field(ge=1, le=12)
    subjectTrack: Literal["regular", "tl"] = "regular"
    sessionTtlMinutes: int = Field(default=120, ge=5, le=1440)
    rapidGuessMs: int | None = Field(default=None, ge=0, le=60000)

    @model_validator(mode="after")
    def unique_versions(self):
        if self.subjectTrack == "tl" and self.grade not in (11, 12):
            raise ValueError("TL assessments require grade 11 or 12")
        if len(set(self.questionVersionIds)) != len(self.questionVersionIds):
            raise ValueError("assessment item versions must be unique")
        return self


class ParticipantCreate(StrictRecord):
    participantCode: str = Field(min_length=3, max_length=200)


class ResponseCreate(StrictRecord):
    responseId: str = Field(min_length=8, max_length=128)
    deliveryInstanceId: str = Field(min_length=1, max_length=150)
    selectedOptionIds: list[str] = Field(default_factory=list, max_length=1)
    skipped: bool = False
    responseTimeMs: int = Field(ge=0, le=86400000)
    answerChanges: int = Field(default=0, ge=0, le=10000)
    clientSubmittedAt: datetime | None = None

    @model_validator(mode="after")
    def exactly_one_answer_or_skip(self):
        if self.skipped == bool(self.selectedOptionIds):
            raise ValueError("select exactly one public option or explicitly skip")
        if self.clientSubmittedAt and self.clientSubmittedAt.utcoffset() is None:
            raise ValueError("clientSubmittedAt requires a timezone")
        return self


class AssessmentReceipt(StrictRecord):
    assessmentId: str
    assessmentHash: str
    itemCount: int
    status: Literal["ready"]


class ParticipantReceipt(StrictRecord):
    assessmentId: str
    participantToken: str
    tokenType: Literal["Bearer"]


class SessionReceipt(StrictRecord):
    sessionId: str
    assessmentId: str
    status: Literal["active", "completed"]
    expiresAt: datetime
    nextItemUrl: str


class PublicOption(StrictRecord):
    id: str
    text: str


class PublicItem(StrictRecord):
    publicItemId: str
    questionType: Literal["multiple_choice"]
    questionText: str
    stimulus: str | None
    options: list[PublicOption]
    media: list[dict]


class DeliveredItem(StrictRecord):
    deliveryInstanceId: str
    sessionId: str
    item: PublicItem
    sequence: dict[str, int]
    timing: dict[str, datetime]


class DeliveryFinished(StrictRecord):
    sessionId: str
    finished: Literal[True]
    item: None


class ResponseReceipt(StrictRecord):
    responseId: str
    accepted: Literal[True]
    nextItemUrl: str


class SessionCompleted(StrictRecord):
    sessionId: str
    status: Literal["completed"]
