import json

import httpx
import pytest

from app.llm import groq
from app.llm.groq import GroqSettings, GroqSilverAdapter
from scripts import generate_silver_labels_kelas1 as generator
from scripts import nightly_pipeline as nightly
from scripts import validate_exercise_batch as exercise
from scripts.refresh_ai_validation_reports import verify_evidence
from tests.test_blind_pilot_audit import question
from tests.test_deepseek_migration import migration
from tests.test_nightly_pipeline import config
from tests.test_silver_grade import silver_output
from tests.test_single_run_exercise import run
from argparse import Namespace


def test_groq_payload_and_schema_do_not_include_deepseek_options_or_reasoning():
    def response(request):
        assert str(request.url) == "https://api.groq.com/openai/v1/chat/completions"
        body = json.loads(request.content)
        assert body["model"] == "openai/gpt-oss-120b"
        assert body["max_completion_tokens"] == 4096
        assert body["include_reasoning"] is False
        assert body["reasoning_effort"] == "low"
        assert body["response_format"] == {"type": "json_object"}
        assert not {"thinking", "max_tokens", "reasoning_format"}.intersection(body)
        return httpx.Response(200, json={"choices": [{"finish_reason": "stop", "message": {
            "content": silver_output("Easy").model_dump_json(), "reasoning": "internal-private"}}],
            "usage": {"prompt_tokens": 20, "completion_tokens": 30, "total_tokens": 50}})
    with httpx.Client(transport=httpx.MockTransport(response)) as client:
        result = GroqSilverAdapter(GroqSettings(api_key="test-private", live_enabled=True), client=client).label_once(
            question("q1"), [], run_index=1, grade=8)
    assert result.status == "success" and result.usage.totalTokens == 50
    assert "internal-private" not in result.model_dump_json()
    assert "test-private" not in repr(GroqSettings(api_key="test-private"))


@pytest.mark.parametrize("code", [401, 429, 503, 504])
def test_groq_errors_are_sanitized(code):
    with httpx.Client(transport=httpx.MockTransport(lambda request: httpx.Response(
            code, json={"error": {"message": "test-private"}}))) as client:
        result = GroqSilverAdapter(GroqSettings(api_key="test-private", live_enabled=True), client=client).label_once(
            question("q1"), [], run_index=1)
    assert result.status == "failed" and result.errorCode.endswith(":" + str(code))
    assert "test-private" not in result.model_dump_json()


@pytest.mark.parametrize("address", ["http://api.groq.com/openai/v1", "https://api.groq.com.evil.test/openai/v1",
    "https://api.groq.com/openai/v1?secret=x", "https://user@api.groq.com/openai/v1"])
def test_groq_credentials_cannot_go_to_another_host(address):
    with pytest.raises(ValueError, match="official Groq"):
        GroqSettings(api_base_url=address)


def test_groq_requires_own_key_and_live_enablement():
    with pytest.raises(ValueError, match="GROQ_API_KEY"):
        GroqSilverAdapter(GroqSettings())
    with pytest.raises(ValueError, match="GROQ_LIVE_ENABLED"):
        GroqSilverAdapter(GroqSettings(api_key="test-private"))


def test_exercise_groq_worker_uses_configured_spacing(migration, monkeypatch):
    monkeypatch.setattr(exercise, "VALIDATION_PROVIDER", "groq")
    exercise.seed_from_gemini("kelas8", "batch01")
    monkeypatch.setenv("GROQ_REQUEST_PAUSE_SECONDS", "65")
    def launch(args, **kwargs):
        assert args[args.index("--pause") + 1] == "65.0"
        assert args[args.index("--workers") + 1] == "1"
        assert args[args.index("--runs") + 1] == "1"
        assert args[args.index("--provider") + 1] == "groq"
        assert "--stop-on-503" in args
        return Namespace(returncode=0)
    monkeypatch.setattr(exercise.subprocess, "run", launch)
    assert exercise.run_labeler("kelas8", "batch01", [], 2, stop_on_503=True) == 0


def test_groq_resume_preserves_gemini_and_only_requests_pending(migration, monkeypatch):
    old, _, rows, before, _ = migration
    monkeypatch.setattr(exercise, "VALIDATION_PROVIDER", "groq")
    assert exercise.seed_from_gemini("kelas8", "batch01")["retainedItems"] == 2
    new = exercise.paths("kelas8", "batch01")
    retained = json.loads(new["checkpoint"].read_text(encoding="utf-8"))["items"]
    class Adapter:
        calls = []
        def label_once(self, item, paths, *, run_index, grade, **kwargs):
            self.calls.append(item["_id"])
            return run(run_index, original=item, grade=grade)
    adapter = Adapter()
    monkeypatch.setattr(groq, "GroqSilverAdapter", lambda *args, **kwargs: adapter)
    monkeypatch.setattr(generator, "parse_args", lambda: Namespace(
        source=new["source"], output=new["checkpoint"], provider="groq", grade=8, track="regular", runs=1,
        execute=True, limit=None, question_id=None, workers=1, attempts=2, pause=0, adjudicate=True,
        max_api_calls=10, stop_on_quota=True, stop_on_503=True, max_consecutive_provider_failures=3))
    assert generator.main() == 0 and generator.main() == 0
    current = json.loads(new["checkpoint"].read_text(encoding="utf-8"))
    assert adapter.calls == ["q3"]
    assert current["items"]["q3"]["provider"] == "groq" and current["apiAttempts"] == 1
    assert all(current["items"][qid] == item for qid, item in retained.items())
    assert old["checkpoint"].read_bytes() == before
    verify_evidence(new["source"], new["checkpoint"], 8)


@pytest.mark.parametrize("key,enabled,status", [("", "false", "waiting_for_credentials"),
    ("test-private", "false", "waiting_for_provider_enablement")])
def test_groq_nightly_waits_without_network(migration, monkeypatch, key, enabled, status):
    for slot in (1, 2, 3):
        monkeypatch.setenv(f"GROQ_API_KEY_{slot}", "")
    monkeypatch.delenv("EXERCISE_GROQ_KEY_SLOT", raising=False)
    monkeypatch.setattr(exercise, "VALIDATION_PROVIDER", "groq")
    exercise.seed_from_gemini("kelas8", "batch01")
    monkeypatch.setenv("GROQ_API_KEY", key)
    monkeypatch.setenv("GROQ_LIVE_ENABLED", enabled)
    monkeypatch.setattr(nightly.subprocess, "run", lambda *args, **kwargs: pytest.fail("unexpected network call"))
    result, budget = nightly.validate_job(nightly.source_identity("kelas8", "batch01"),
        {**config(), "provider": "groq"}, {}, 10, exercise.paths("kelas8", "batch01")["stage"])
    assert result["status"] == status and result["apiCallsThisRun"] == 0 and budget == 10
