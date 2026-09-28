"""Bounded N-run self-consistency orchestration for Gemini advisory review."""

from __future__ import annotations

import time
from collections import Counter
from typing import Any

from app.classification.v2.contracts import V2ClassificationRequest, V2ClassificationResponse

from .config import GeminiSettings
from .contracts import (
    GeminiAdvisoryResult,
    GeminiRunResult,
    SelfConsistencyHead,
)
from .gemini import PROMPT_VERSION, GeminiProviderError, GeminiReviewAdapter


class GeminiLiveCallsDisabled(RuntimeError):
    pass


def _outcome(reviewed: Any, original_label: str | None) -> tuple[str, str | None]:
    if reviewed.action == "confirm":
        return "confirm", original_label
    if reviewed.action == "revise":
        proposed = reviewed.proposedLabel
        return "revise", proposed.value if hasattr(proposed, "value") else str(proposed)
    return "abstain", None


def _aggregate(
    runs: list[GeminiRunResult], *, head_name: str, original_label: str | None
) -> SelfConsistencyHead:
    outcomes = [
        _outcome(getattr(run.review, head_name), original_label)
        for run in runs
        if run.status == "success" and run.review is not None
    ]
    if len(outcomes) < 2:
        return SelfConsistencyHead(status="insufficient_runs")
    (action, label), count = Counter(outcomes).most_common(1)[0]
    required = len(outcomes) // 2 + 1
    if count < required:
        return SelfConsistencyHead(status="no_consensus", supportingRuns=count)
    return SelfConsistencyHead(
        status="consistent",
        suggestedAction=action,
        suggestedLabel=label,
        supportingRuns=count,
    )


class GeminiReviewRuntime:
    def __init__(
        self, settings: GeminiSettings, *, adapter: GeminiReviewAdapter | None = None
    ) -> None:
        self.settings = settings
        self.adapter = adapter or GeminiReviewAdapter(settings)

    @classmethod
    def from_environment(cls) -> "GeminiReviewRuntime":
        return cls(GeminiSettings.from_environment())

    def review(
        self,
        question: V2ClassificationRequest,
        prediction: V2ClassificationResponse,
        *,
        rubric_version: str,
        runs: int | None = None,
    ) -> GeminiAdvisoryResult:
        if not self.settings.live_enabled:
            raise GeminiLiveCallsDisabled(
                "Gemini generation is disabled; set GEMINI_LIVE_ENABLED=true explicitly"
            )
        run_count = self.settings.review_runs if runs is None else runs
        if not 1 <= run_count <= 5:
            raise ValueError("runs must be between 1 and 5")

        results: list[GeminiRunResult] = []
        for index in range(1, run_count + 1):
            started = time.perf_counter()
            try:
                results.append(
                    self.adapter.review_once(
                        question,
                        prediction,
                        rubric_version=rubric_version,
                        run_index=index,
                    )
                )
            except GeminiProviderError as exc:
                results.append(
                    GeminiRunResult(
                        runIndex=index,
                        status="failed",
                        errorCode=exc.code,
                        latencyMs=int((time.perf_counter() - started) * 1000),
                    )
                )

        return GeminiAdvisoryResult(
            model=self.settings.model,
            promptVersion=PROMPT_VERSION,
            rubricVersion=rubric_version,
            runs=results,
            mathCognitiveDomain=_aggregate(
                results,
                head_name="mathCognitiveDomain",
                original_label=prediction.mathCognitiveDomain.label,
            ),
            knowledgeDimension=_aggregate(
                results,
                head_name="knowledgeDimension",
                original_label=prediction.knowledgeDimension.label,
            ),
            intendedDifficulty=_aggregate(
                results,
                head_name="intendedDifficulty",
                original_label=prediction.intendedDifficulty.label,
            ),
        )
