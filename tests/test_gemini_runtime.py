from __future__ import annotations

from types import SimpleNamespace

import pytest

from app.classification.v2.contracts import (
    HeadResult,
    ModelTrace,
    V2ClassificationRequest,
    V2ClassificationResponse,
)
from app.llm.config import GeminiSettings
from app.llm.contracts import GeminiReviewOutput, GeminiRunResult
from app.llm.gemini import GeminiReviewAdapter
from app.llm.runtime import GeminiLiveCallsDisabled, GeminiReviewRuntime


def question() -> V2ClassificationRequest:
    return V2ClassificationRequest.model_validate(
        {
            "questionId": "q-1",
            "contentVersion": 1,
            "contentHash": "a" * 64,
            "grade": 4,
            "topic": "Pecahan",
            "subtopic": "Perbandingan",
            "questionType": "multiple_choice",
            "stem": "Pecahan manakah yang paling besar?",
            "options": [
                {"label": "A", "text": "1/2"},
                {"label": "B", "text": "3/4"},
            ],
            "verifiedMinimalSolution": "Samakan penyebut; 3/4 lebih besar.",
            "detectedKko": ["menentukan"],
            "provenanceStatus": {
                "contentQualified": True,
                "answerKeyVerified": True,
                "solutionVerified": True,
            },
        }
    )


def prediction() -> V2ClassificationResponse:
    def head(label: str, probabilities: dict[str, float]) -> HeadResult:
        return HeadResult(
            label=label,
            probabilities=probabilities,
            calibratedConfidence=max(probabilities.values()),
            normalizedEntropy=0.3,
            action="review",
        )

    return V2ClassificationResponse(
        questionId="q-1",
        contentVersion=1,
        contentHash="a" * 64,
        scopeStatus="in_scope",
        mathCognitiveDomain=head(
            "applying", {"knowing": 0.1, "applying": 0.8, "reasoning": 0.1}
        ),
        knowledgeDimension=head(
            "procedural",
            {"factual": 0.05, "conceptual": 0.15, "procedural": 0.75, "metacognitive": 0.05},
        ),
        intendedDifficulty=head("Medium", {"Easy": 0.2, "Medium": 0.7, "Hard": 0.1}),
        trace=ModelTrace(
            modelVersion="test-v1",
            baseModel="indobert",
            baseRevision="revision",
            datasetSnapshot="snapshot",
            rubricVersion="rubric-v1",
            calibrationVersion="cal-v1",
            inputSchemaVersion="schema-v1",
            inputHash="b" * 64,
        ),
    )


def review_payload(*, difficulty: str = "Hard") -> GeminiReviewOutput:
    return GeminiReviewOutput.model_validate(
        {
            "contentStatus": "valid",
            "contentConcerns": [],
            "mathCognitiveDomain": {
                "action": "confirm",
                "proposedLabel": None,
                "evidenceSpans": ["Pecahan manakah yang paling besar?"],
                "rationale": "Memakai prosedur membandingkan pecahan.",
            },
            "knowledgeDimension": {
                "action": "confirm",
                "proposedLabel": None,
                "evidenceSpans": ["Samakan penyebut"],
                "rationale": "Menuntut pengetahuan prosedural.",
            },
            "intendedDifficulty": {
                "action": "revise",
                "proposedLabel": difficulty,
                "evidenceSpans": ["1/2", "3/4"],
                "rationale": "Kompleksitas tuntutan perlu ditinjau ulang.",
            },
        }
    )


def settings(*, live: bool = False) -> GeminiSettings:
    return GeminiSettings(
        api_key="secret-not-real",
        model="gemini-3.8-flash",
        live_enabled=live,
    )


def test_settings_hide_key_and_reject_non_google_base_url():
    assert "secret-not-real" not in repr(settings())
    with pytest.raises(ValueError, match="official Google"):
        GeminiSettings(
            api_key="secret",
            model="gemini-3.8-flash",
            api_base_url="https://attacker.example",
        )


def test_live_calls_are_disabled_by_default_without_touching_adapter():
    class NeverCalled:
        def review_once(self, *args, **kwargs):
            raise AssertionError("network-capable adapter must not be called")

    runtime = GeminiReviewRuntime(settings(), adapter=NeverCalled())
    with pytest.raises(GeminiLiveCallsDisabled):
        runtime.review(question(), prediction(), rubric_version="rubric-v1")


def test_adapter_uses_structured_schema_and_returns_sanitized_record():
    parsed = review_payload()

    class FakeModels:
        def __init__(self):
            self.kwargs = None

        def generate_content(self, **kwargs):
            self.kwargs = kwargs
            return SimpleNamespace(
                parsed=parsed,
                response_id="response-1",
                usage_metadata=SimpleNamespace(
                    prompt_token_count=100,
                    candidates_token_count=40,
                    thoughts_token_count=10,
                    total_token_count=150,
                ),
            )

    fake_models = FakeModels()
    adapter = GeminiReviewAdapter(settings(live=True), client=SimpleNamespace(models=fake_models))
    result = adapter.review_once(
        question(), prediction(), rubric_version="rubric-v1", run_index=1
    )
    assert result.status == "success"
    assert result.usage.totalTokens == 150
    assert result.responseHash and len(result.responseHash) == 64
    config = fake_models.kwargs["config"]
    assert config.response_mime_type == "application/json"
    assert config.response_json_schema == GeminiReviewOutput.model_json_schema()
    assert config.max_output_tokens == 1200
    assert config.thinking_config.include_thoughts is False


def test_three_runs_are_self_consistency_not_gold_or_human_majority():
    outputs = [review_payload(), review_payload(), review_payload(difficulty="Easy")]

    class FakeAdapter:
        def review_once(self, *args, run_index: int, **kwargs):
            return GeminiRunResult(
                runIndex=run_index,
                status="success",
                review=outputs[run_index - 1],
                latencyMs=1,
            )

    result = GeminiReviewRuntime(
        settings(live=True), adapter=FakeAdapter()
    ).review(question(), prediction(), rubric_version="rubric-v1")
    assert result.reviewRequired is True
    assert result.mathCognitiveDomain.status == "consistent"
    assert result.mathCognitiveDomain.suggestedAction == "confirm"
    assert result.intendedDifficulty.status == "consistent"
    assert result.intendedDifficulty.suggestedLabel == "Hard"
    assert result.intendedDifficulty.supportingRuns == 2


def test_revise_must_have_a_different_label():
    invalid = review_payload(difficulty="Medium")

    class FakeModels:
        def generate_content(self, **kwargs):
            return SimpleNamespace(parsed=invalid, response_id=None, usage_metadata=None)

    adapter = GeminiReviewAdapter(
        settings(live=True), client=SimpleNamespace(models=FakeModels())
    )
    with pytest.raises(Exception, match="revision_must_change_label"):
        adapter.review_once(question(), prediction(), rubric_version="rubric-v1", run_index=1)


def test_llm_info_never_exposes_key_or_calls_generation():
    from fastapi.testclient import TestClient

    from app.main import app

    response = TestClient(app).get("/v2/llm-info")
    assert response.status_code == 200
    payload = response.json()
    assert "api_key" not in str(payload).casefold()
    assert "apiKey" not in payload
    assert payload["provider"] == "gemini"
    assert payload.get("networkChecked") is False
