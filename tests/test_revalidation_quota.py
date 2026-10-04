from argparse import Namespace
import json
from types import SimpleNamespace

from app.llm.config import GeminiSettings
from app.llm.silver import SilverRunResult, SilverLabelOutput, failed_response_evidence
import pytest
from pydantic import ValidationError
from scripts import generate_silver_labels_kelas1 as generator
from scripts.revalidate_all_grades import complete, select_pilot
from tests.test_blind_pilot_audit import question
from tests.test_silver_grade import silver_output


def setup_runner(tmp_path, monkeypatch, adapter, **options):
    monkeypatch.setattr(generator, "ROOT", tmp_path)
    source = tmp_path / "questions.json"
    source.write_text(json.dumps([question("q1"), question("q2")]), encoding="utf-8")
    output = tmp_path / "checkpoint.json"
    args = dict(source=source, output=output, grade=1, track="regular", runs=3, execute=True,
                limit=None, workers=1, attempts=2, pause=0, adjudicate=True,
                question_id=None, max_api_calls=30, stop_on_quota=True)
    args.update(options)
    monkeypatch.setattr(generator, "parse_args", lambda: Namespace(**args))
    monkeypatch.setattr(generator.GeminiSettings, "from_environment",
                        lambda: GeminiSettings(api_key="test-only", model="test-model"))
    monkeypatch.setattr(generator, "GeminiSilverAdapter", lambda settings: adapter)
    monkeypatch.setattr(generator.time, "sleep", lambda _: None)
    return output


def test_any_429_stops_before_retry_or_next_question(tmp_path, monkeypatch):
    class Adapter:
        calls = 0

        def label_once(self, *args, run_index, **kwargs):
            self.calls += 1
            return SilverRunResult(runIndex=run_index, status="failed", errorCode="ClientError:429", latencyMs=1)

    adapter = Adapter()
    output = setup_runner(tmp_path, monkeypatch, adapter)
    assert generator.main() == 3
    cp = json.loads(output.read_text(encoding="utf-8"))
    assert adapter.calls == cp["apiAttempts"] == 1
    assert cp["executionStatus"] == "blocked_provider_quota_or_rate_limit"
    assert "q2" not in cp["items"]


def test_budget_keeps_paid_run_and_resume_completes_pilot_without_repeating_it(tmp_path, monkeypatch):
    class Adapter:
        calls = []

        def label_once(self, item, paths, *, run_index, **kwargs):
            self.calls.append((item["_id"], run_index))
            return SilverRunResult(runIndex=run_index, status="success", output=silver_output("Easy"), latencyMs=1)

    adapter = Adapter()
    output = setup_runner(tmp_path, monkeypatch, adapter, question_id=["q2"], max_api_calls=1)
    assert generator.main() == 4
    cp = json.loads(output.read_text(encoding="utf-8"))
    assert cp["items"]["q2"]["runs"][0]["status"] == "success"
    setup_runner(tmp_path, monkeypatch, adapter, question_id=["q2"], max_api_calls=3)
    assert generator.main() == 0
    cp = json.loads(output.read_text(encoding="utf-8"))
    assert adapter.calls == [("q2", 1), ("q2", 2), ("q2", 3)]
    assert complete(cp, ["q2"])
    assert not complete(cp, ["q1", "q2"])


def test_pilot_selection_and_completion_do_not_require_hard():
    questions = [question("q1"), question("q2")]
    old = [{"_id": "q1", "cognitive_level": "easy"}, {"_id": "q2", "cognitive_level": "medium"}]
    assert select_pilot(questions, old, 2) == ["q1", "q2"]
    cp = {"items": {"q1": {"runs": [{"runIndex": i, "status": "success"} for i in (1, 2, 3)],
                                  "aggregate": {"needsAdjudication": True}}}}
    assert not complete(cp, ["q1"])


def test_failed_paid_response_keeps_usage_but_never_error_inputs_or_raw_text():
    with pytest.raises(ValidationError) as raised:
        SilverLabelOutput.model_validate({"api_key": "secret-sentinel"})
    response = SimpleNamespace(text="secret-sentinel", response_id="response-1",
                               candidates=[SimpleNamespace(finish_reason="MAX_TOKENS")],
                               usage_metadata=SimpleNamespace(prompt_token_count=50, candidates_token_count=20,
                                                              thoughts_token_count=5, total_token_count=75))
    evidence = failed_response_evidence(raised.value, response)
    assert evidence["usage"].totalTokens == 75
    assert evidence["responseId"] == "response-1" and len(evidence["responseHash"]) == 64
    assert "secret-sentinel" not in json.dumps({k: v for k, v in evidence.items() if k != "usage"})
    assert all(set(error) == {"location", "type"} for error in evidence["errorDetails"])
