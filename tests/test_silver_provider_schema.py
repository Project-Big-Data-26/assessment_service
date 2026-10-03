"""The provider must enforce evidence requirements without preventing abstention."""

from types import SimpleNamespace

import pytest
from pydantic import ValidationError

from app.llm.config import GeminiSettings
from app.llm.silver import GeminiSilverAdapter, SilverLabelOutput, SilverRunResult, silver_provider_schema
from tests.test_silver_grade import silver_output


@pytest.mark.parametrize("head", ["SilverCognitiveHead", "SilverKnowledgeHead", "SilverDifficultyHead"])
def test_provider_requires_evidence_only_for_classification(head):
    classify, abstain = silver_provider_schema()["$defs"][head]["anyOf"]
    assert classify["properties"]["action"]["enum"] == ["classify"]
    assert classify["properties"]["evidenceSpans"]["minItems"] == 1
    assert {"label", "evidenceSpans"} <= set(classify["required"])
    assert classify["properties"]["label"].get("type") != "null"
    assert abstain["properties"]["action"]["enum"] == ["abstain"]
    assert abstain["properties"]["label"] == {"type": "null"}
    assert abstain["properties"]["evidenceSpans"].get("minItems", 0) == 0
    if head == "SilverDifficultyHead":
        assert "profile" in classify["required"]
        assert abstain["properties"]["profile"] == {"type": "null"}


def test_empty_classification_evidence_remains_invalid_locally():
    payload = silver_output("Medium").model_dump(mode="json")
    for head in ("mathCognitiveDomain", "knowledgeDimension", "intendedDifficulty"):
        payload[head]["evidenceSpans"] = []
    with pytest.raises(ValidationError, match="classification requires evidence"):
        SilverLabelOutput.model_validate(payload)


def test_abstention_without_evidence_still_valid():
    payload = silver_output("Medium").model_dump(mode="json")
    for head in ("mathCognitiveDomain", "knowledgeDimension", "intendedDifficulty"):
        payload[head].update(action="abstain", label=None, evidenceSpans=[])
    payload["intendedDifficulty"]["profile"] = None
    assert SilverLabelOutput.model_validate(payload).intendedDifficulty.action == "abstain"


def test_initial_runs_and_adjudication_send_conditional_evidence_schema():
    calls = []
    output = silver_output("Medium")

    def generate_content(**kwargs):
        calls.append(kwargs)
        return SimpleNamespace(parsed=output.model_dump(mode="json"), usage_metadata=None)

    adapter = object.__new__(GeminiSilverAdapter)
    adapter.settings = GeminiSettings(api_key="unit-test-key", model="unit-test-model")
    adapter.client = SimpleNamespace(models=SimpleNamespace(generate_content=generate_content))
    question = {"_id": "q", "soal_text": "Hitung 2 + 3", "options": [], "jawaban": "5"}
    assert adapter.label_once(question, [], run_index=1, grade=5).status == "success"
    runs = [SilverRunResult(runIndex=i, status="success", output=output, latencyMs=1) for i in (1, 2, 3)]
    assert adapter.adjudicate_once(question, [], runs, grade=5).status == "success"
    assert len(calls) == 2
    for call in calls:
        schema = call["config"].response_json_schema
        classify = schema["$defs"]["SilverCognitiveHead"]["anyOf"][0]
        assert classify["properties"]["evidenceSpans"]["minItems"] == 1
