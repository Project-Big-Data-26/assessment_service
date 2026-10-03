"""Strict contracts for dichotomous response matrices and empirical policies."""
from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, StrictInt, model_validator

from app.classification.v2.contracts import IntendedDifficulty


class StrictRecord(BaseModel):
    model_config = ConfigDict(extra="forbid", allow_inf_nan=False)


class ItemReference(StrictRecord):
    questionId: str = Field(min_length=1, max_length=200)
    questionVersionId: str = Field(min_length=1, max_length=250)
    contentVersion: int = Field(ge=1)
    contentHash: str = Field(pattern=r"^[a-f0-9]{64}$")
    intendedDifficulty: IntendedDifficulty | None = None
    optionIds: list[str] = Field(default_factory=list, max_length=20)
    answerKey: str | None = None

    @model_validator(mode="after")
    def consistent_options(self):
        if len(set(self.optionIds)) != len(self.optionIds):
            raise ValueError("optionIds must be unique")
        if self.answerKey is not None and self.answerKey not in self.optionIds:
            raise ValueError("answerKey must refer to an optionId")
        return self


class AssumptionReview(StrictRecord):
    reviewedBy: str = Field(min_length=3, max_length=200)
    evidence: str = Field(min_length=20, max_length=4000)
    unidimensional: bool
    localIndependence: bool
    representativeSample: bool


class MatrixAnalysisInput(StrictRecord):
    populationId: str = Field(min_length=1, max_length=100)
    assessmentFamily: str = Field(min_length=1, max_length=100)
    grade: int = Field(ge=1, le=12)
    items: list[ItemReference] = Field(min_length=1, max_length=200)
    subjectIds: list[str] = Field(min_length=1, max_length=10000)
    matrix: list[list[StrictInt | None]] = Field(min_length=1, max_length=10000)
    model: Literal["rasch", "2pl", "3pl"] = "rasch"
    dataOrigin: Literal["server_scored", "external_scored", "synthetic"] = "external_scored"
    assumptionReview: AssumptionReview | None = None

    @model_validator(mode="after")
    def rectangular_binary_matrix(self):
        if len(self.subjectIds) != len(self.matrix) or len(set(self.subjectIds)) != len(self.subjectIds):
            raise ValueError("matrix requires one row per unique subjectId")
        versions = [item.questionVersionId for item in self.items]
        if len(set(versions)) != len(versions):
            raise ValueError("item versions must be unique")
        if len({item.questionId for item in self.items}) != len(self.items):
            raise ValueError("different versions of the same question cannot share a calibration")
        for row in self.matrix:
            if len(row) != len(self.items) or any(value not in (0, 1, None) for value in row):
                raise ValueError("matrix must be rectangular with 0, 1, or null; missing is never zero")
        if len(self.matrix) * len(self.items) > 500000:
            raise ValueError("analysis is limited to 500000 response cells")
        return self


class AnalysisPolicy(StrictRecord):
    policyVersion: str = "empirical-dichotomous-v1"
    minPersons: dict[str, int] = Field(default_factory=lambda: {"rasch": 100, "2pl": 300, "3pl": 1000})
    minItems: dict[str, int] = Field(default_factory=lambda: {"rasch": 5, "2pl": 10, "3pl": 20})
    minResponsesPerItem: int = Field(default=50, ge=8)
    minOutcomeCount: int = Field(default=5, ge=2)
    minCoverage: float = Field(default=0.7, gt=0, le=1)
    maxPersonMissingRate: float = Field(default=0.3, ge=0, lt=1)
    easyP: float = Field(default=0.7, gt=0, lt=1)
    hardP: float = Field(default=0.3, gt=0, lt=1)
    easyB: float = -1.0
    hardB: float = 1.0
    maxCiWidth: float = Field(default=0.3, gt=0, le=1)
    distractorMinRate: float = Field(default=0.05, gt=0, lt=1)
    quadraturePoints: int = Field(default=41, ge=21, le=81)
    maxIterations: int = Field(default=300, ge=1, le=1000)
    tolerance: float = Field(default=1e-6, gt=0, le=0.01)

    @model_validator(mode="after")
    def valid_thresholds(self):
        for values in (self.minPersons, self.minItems):
            if set(values) != {"rasch", "2pl", "3pl"} or any(value < 1 for value in values.values()):
                raise ValueError("all three IRT models require positive readiness thresholds")
        if self.hardP >= self.easyP or self.easyB >= self.hardB:
            raise ValueError("difficulty thresholds must be ordered")
        return self


class ScreeningInput(StrictRecord):
    assessmentId: str = Field(min_length=1, max_length=150)
    model: Literal["rasch", "2pl", "3pl"] = "rasch"
    attemptPolicy: Literal["first", "last"] = "first"
    fromTime: datetime | None = None
    toTime: datetime | None = None
    assumptionReview: AssumptionReview | None = None

    @model_validator(mode="after")
    def time_window(self):
        for value in (self.fromTime, self.toTime):
            if value is not None and value.utcoffset() is None:
                raise ValueError("time window requires timezone-aware timestamps")
        if self.fromTime and self.toTime and self.fromTime >= self.toTime:
            raise ValueError("fromTime must precede toTime")
        return self


class CttItemMetrics(StrictRecord):
    validResponseCount: int
    correctCount: int
    difficultyIndex: float | None
    difficultyCi95: list[float] | None
    empiricalDifficulty: IntendedDifficulty | None
    discrimination: float | None
    correctedPointBiserial: float | None
    totalScoreJoin: Literal["complete_cases_only"]
    totalScoreSample: int
    missingRate: float
    optionSelectionCounts: dict[str, int] | None
    distractorEfficiency: float | None
    nonFunctioningDistractors: list[str]
    medianResponseTimeMs: float | None
    responseTimeIqrMs: float | None


class IrtItemParameters(StrictRecord):
    a: float
    b: float
    c: float
    bPosteriorSd: float | None
    bInterval95: list[float] | None
    infit: float
    outfit: float
    empiricalDifficulty: IntendedDifficulty


class EmpiricalItemResult(StrictRecord):
    questionId: str
    questionVersionId: str
    contentVersion: int
    contentHash: str
    intendedDifficulty: IntendedDifficulty | None
    ctt: CttItemMetrics
    irt: IrtItemParameters | None
    reviewFlags: list[str]
    recommendedRouting: Literal["collect_more_events", "ai_review", "observation_only"]


class PersonEstimate(StrictRecord):
    thetaEap: float
    posteriorSd: float
    answeredItems: int
    subjectId: str


class IrtResult(StrictRecord):
    status: Literal["estimated", "estimated_with_warnings", "waiting_for_data", "waiting_for_assumption_review", "failed"]
    model: Literal["rasch", "2pl", "3pl"]
    items: list[IrtItemParameters]
    persons: list[PersonEstimate]
    warnings: list[str]
    method: str | None = None
    scale: str | None = None
    priors: dict[str, str | None] | None = None
    converged: bool | None = None
    iterations: int | None = None
    logLikelihood: float | None = None
    aic: float | None = None
    bic: float | None = None
    informationCriteriaCaveat: str | None = None
    testInformation: dict[str, list[float]] | None = None
    localDependenceScreen: dict | None = None


class EmpiricalAnalysisResult(StrictRecord):
    schemaVersion: Literal["empirical-analysis-v1"]
    policyVersion: str
    policyHash: str
    policy: AnalysisPolicy
    populationId: str
    assessmentFamily: str
    grade: int
    dataOrigin: Literal["server_scored", "external_scored", "synthetic"]
    researchOnly: Literal[True]
    reviewRequired: bool
    reviewMode: Literal["automated_ai"]
    labelProvenance: Literal["ai_silver"]
    matrixHash: str
    normalization: dict
    readiness: dict
    ctt: dict
    items: list[EmpiricalItemResult]
    irt: IrtResult
    cleaning: dict | None = None
    assessmentId: str | None = None
    timeWindow: dict[str, str | None] | None = None
    sampleManifestHash: str | None = None
    snapshotHash: str | None = None
    snapshotId: str | None = None
    createdAt: datetime | None = None
    persisted: bool | None = None
