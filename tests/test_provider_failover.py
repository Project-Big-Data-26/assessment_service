from argparse import Namespace
import json
from types import SimpleNamespace

import pytest

from app.llm import groq
from scripts import generate_silver_labels_kelas1 as generator
from scripts import nightly_pipeline as nightly
from scripts import provider_failover as failover
from scripts import validate_exercise_batch as exercise
from scripts.refresh_ai_validation_reports import verify_evidence
from tests.test_deepseek_migration import migration
from tests.test_nightly_pipeline import config
from tests.test_nightly_provider_resume import stopped
from tests.test_single_run_exercise import run


@pytest.fixture
def enabled(monkeypatch, tmp_path):
    monkeypatch.setattr(exercise, "ROOT", tmp_path)
    monkeypatch.setattr(exercise, "VALIDATION_NAMESPACE", "failover")
    monkeypatch.setattr(exercise, "VALIDATION_PROVIDER", "gemini")
    monkeypatch.setenv("LLM_PROVIDER", "gemini")
    for provider, model in (("GEMINI", "gemini-next"), ("GROQ", "openai/gpt-oss-120b")):
        monkeypatch.setenv(provider + "_API_KEY", "test-private")
        monkeypatch.setenv(provider + "_LIVE_ENABLED", "true")
        monkeypatch.setenv(provider + "_MODEL", model)


def test_bidirectional_migration_preserves_mixed_provider_and_model_evidence(migration, enabled, monkeypatch):
    old, _, rows, before, _ = migration
    # migration's fixture selected DeepSeek; choose Gemini explicitly for the shared namespace.
    first = failover.activate_checkpoint("kelas8", "batch01", "gemini")
    p = exercise.paths("kelas8", "batch01")
    assert first["model"] == "gemini-next"
    assert len(first["items"]) == 2 and first.get("apiAttempts", 0) == 0
    assert all(r["model"] == "gemini-original" for r in first["items"].values())
    failover.activate_checkpoint("kelas8", "batch01", "groq")
    class Adapter:
        calls = []
        def label_once(self, item, paths, *, run_index, grade, **kwargs):
            self.calls.append(item["_id"])
            return run(run_index, original=item, grade=grade)
    adapter = Adapter()
    monkeypatch.setattr(groq, "GroqSilverAdapter", lambda *args, **kwargs: adapter)
    monkeypatch.setattr(generator, "parse_args", lambda: Namespace(
        source=p["source"], output=p["checkpoint"], provider="groq", grade=8, track="regular", runs=1,
        execute=True, limit=None, question_id=None, workers=1, attempts=2, pause=0, adjudicate=True,
        max_api_calls=10, stop_on_quota=True, stop_on_503=True, max_consecutive_provider_failures=3))
    assert generator.main() == 0
    assert adapter.calls == ["q3"]
    current = failover.activate_checkpoint("kelas8", "batch01", "gemini")
    assert len(current["items"]) == 3
    assert current["items"]["q3"]["provider"] == "groq"
    assert current["items"]["q1"]["provider"] == "gemini"
    assert current["items"]["q1"]["model"] == "gemini-original"
    assert old["checkpoint"].read_bytes() == before
    verify_evidence(p["source"], p["checkpoint"], 8)
    stable = p["checkpoint"].read_bytes()
    failover.activate_checkpoint("kelas8", "batch01", "gemini")
    assert p["checkpoint"].read_bytes() == stable
    # Even same-provider retained decisions must be checked against immutable evidence.
    current["items"]["q1"]["aggregate"]["contentStatus"] = "concern"
    generator.atomic_write(current, p["checkpoint"])
    with pytest.raises(ValueError, match="retained paid decision was changed"):
        verify_evidence(p["source"], p["checkpoint"], 8)


@pytest.mark.parametrize("first", [stopped("blocked_provider_daily_quota", "ClientError:429"),
    stopped("blocked_provider_quota_or_rate_limit", "ClientError:429")])
def test_quota_switches_once_and_shares_the_call_budget(tmp_path, enabled, monkeypatch, first):
    calls, activations = [], []
    monkeypatch.setattr(failover, "activate_checkpoint", lambda name, batch, provider: activations.append(provider))
    monkeypatch.setattr(nightly, "settings_for", lambda p: SimpleNamespace(api_key="test-private", live_enabled=True))
    def validate(job, cfg, state, budget, directory, **kwargs):
        calls.append(cfg["provider"])
        return (dict(first) if len(calls) == 1 else {"status": "completed", "exitCode": 0}), budget - 1
    monkeypatch.setattr(nightly, "validate_with_provider_retries", validate)
    cfg = {**config(), "provider": "gemini", "fallbackProviders": ["groq"]}
    result, budget = nightly.validate_with_provider_failover({"class": "kelas8", "batch": "batch01"}, cfg, {}, 10, tmp_path)
    assert calls == activations == ["gemini", "groq"]
    assert budget == 8 and result["apiCallsThisRun"] == 2
    assert result["activeProvider"] == "groq" and result["status"] == "completed"


@pytest.mark.parametrize("code", ["ServerError:503", "ClientError:401", "ClientError:403"])
def test_503_and_auth_errors_never_trigger_provider_switch(tmp_path, enabled, monkeypatch, code):
    calls = []
    monkeypatch.setattr(failover, "activate_checkpoint", lambda *args: None)
    monkeypatch.setattr(nightly, "settings_for", lambda p: SimpleNamespace(api_key="test-private", live_enabled=True))
    def validate(job, cfg, state, budget, directory, **kwargs):
        calls.append(cfg["provider"])
        return stopped("blocked_provider_http_503" if code.endswith(":503") else "blocked_provider_configuration", code), budget - 1
    monkeypatch.setattr(nightly, "validate_with_provider_retries", validate)
    result, budget = nightly.validate_with_provider_failover({"class": "kelas8", "batch": "batch01"},
        {**config(), "provider": "gemini", "fallbackProviders": ["groq"]}, {}, 10, tmp_path)
    assert calls == ["gemini"] and budget == 9
    assert result["providerStop"]["errorCode"] == code


def test_both_quotas_exhausted_do_not_loop_back_to_first_provider(tmp_path, enabled, monkeypatch):
    calls = []
    monkeypatch.setattr(failover, "activate_checkpoint", lambda *args: None)
    monkeypatch.setattr(nightly, "settings_for", lambda p: SimpleNamespace(api_key="test-private", live_enabled=True))
    def validate(job, cfg, state, budget, directory, **kwargs):
        calls.append(cfg["provider"])
        return stopped("blocked_provider_quota_or_rate_limit", "ClientError:429"), budget - 1
    monkeypatch.setattr(nightly, "validate_with_provider_retries", validate)
    result, budget = nightly.validate_with_provider_failover({"class": "kelas8", "batch": "batch01"},
        {**config(), "provider": "gemini", "fallbackProviders": ["groq"]}, {}, 10, tmp_path)
    assert calls == ["gemini", "groq"] and budget == 8 and len(result["providerAttempts"]) == 2


@pytest.mark.parametrize("values", [["gemini"], ["groq", "groq"], ["other"], "groq", None])
def test_invalid_provider_order_is_rejected(tmp_path, values):
    path = tmp_path / "config.json"
    path.write_text(json.dumps({**config(), "provider": "gemini", "fallbackProviders": values}), encoding="utf-8")
    with pytest.raises(ValueError, match="fallbackProviders"):
        nightly.read_config(path)


def test_disabled_primary_is_skipped_before_any_network_call(tmp_path, enabled, monkeypatch):
    calls = []
    monkeypatch.setattr(failover, "activate_checkpoint", lambda *args: None)
    monkeypatch.setattr(nightly, "settings_for", lambda p: SimpleNamespace(api_key="test-private", live_enabled=p == "groq"))
    def validate(job, cfg, state, budget, directory, **kwargs):
        calls.append(cfg["provider"])
        return {"status": "completed", "exitCode": 0}, budget - 1
    monkeypatch.setattr(nightly, "validate_with_provider_retries", validate)
    result, budget = nightly.validate_with_provider_failover({"class": "kelas8", "batch": "batch01"},
        {**config(), "provider": "gemini", "fallbackProviders": ["groq"]}, {}, 10, tmp_path)
    assert calls == ["groq"] and budget == 9
    assert result["providerAttempts"][0]["status"] == "skipped_not_enabled"


def test_no_ready_provider_or_budget_never_starts_validation(tmp_path, enabled, monkeypatch):
    monkeypatch.setattr(nightly, "settings_for", lambda p: SimpleNamespace(api_key="", live_enabled=False))
    monkeypatch.setattr(nightly, "validate_with_provider_retries", lambda *a, **k: pytest.fail("unexpected call"))
    cfg = {**config(), "provider": "gemini", "fallbackProviders": ["groq"]}
    result, budget = nightly.validate_with_provider_failover({}, cfg, {}, 10, tmp_path)
    assert result["status"] == "waiting_for_provider" and budget == 10
    result, budget = nightly.validate_with_provider_failover({}, cfg, {}, 0, tmp_path)
    assert result["status"] == "waiting_for_budget" and budget == 0


def test_gemini_without_a_key_is_skipped_before_settings_validation(tmp_path, enabled, monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "")
    monkeypatch.setattr(failover, "activate_checkpoint", lambda *args: None)
    def settings(provider):
        assert provider == "groq"
        return SimpleNamespace(api_key="test-private", live_enabled=True)
    monkeypatch.setattr(nightly, "settings_for", settings)
    monkeypatch.setattr(nightly, "validate_with_provider_retries", lambda *a, **k: ({"status": "completed"}, 9))
    result, budget = nightly.validate_with_provider_failover({"class": "kelas8", "batch": "batch01"},
        {**config(), "provider": "gemini", "fallbackProviders": ["groq"]}, {}, 10, tmp_path)
    assert result["activeProvider"] == "groq" and budget == 9


def test_error_after_switch_preserves_the_budget_spent_by_first_provider(tmp_path, enabled, monkeypatch):
    monkeypatch.setattr(exercise, "ROOT", tmp_path)
    monkeypatch.setattr(failover, "activate_checkpoint", lambda *args: None)
    monkeypatch.setattr(nightly, "settings_for", lambda p: SimpleNamespace(api_key="test-private", live_enabled=True))
    def validate(job, cfg, state, budget, directory, **kwargs):
        if cfg["provider"] == "gemini":
            return stopped("blocked_provider_quota_or_rate_limit", "ClientError:429"), budget - 2
        raise ValueError("local failure after provider switch")
    monkeypatch.setattr(nightly, "validate_with_provider_retries", validate)
    with pytest.raises(failover.ProviderFailoverError) as error:
        nightly.validate_with_provider_failover({"class": "kelas8", "batch": "batch01"},
            {**config(), "provider": "gemini", "fallbackProviders": ["groq"]}, {}, 10, tmp_path)
    assert error.value.remaining_budget == 8


def test_gemini_worker_receives_explicit_provider_and_request_spacing(migration, monkeypatch):
    monkeypatch.setattr(exercise, "VALIDATION_PROVIDER", "gemini")
    monkeypatch.setenv("GEMINI_REQUEST_PAUSE_SECONDS", "15")
    def launch(args, **kwargs):
        assert args[args.index("--pause") + 1] == "15.0"
        assert args[args.index("--provider") + 1] == "gemini"
        assert args[args.index("--runs") + 1] == "1"
        return SimpleNamespace(returncode=0)
    monkeypatch.setattr(exercise.subprocess, "run", launch)
    assert exercise.run_labeler("kelas8", "batch01", [], 3) == 0


def test_enabled_503_policy_switches_to_the_healthy_provider(tmp_path, enabled, monkeypatch):
    calls = []
    monkeypatch.setattr(failover, "activate_checkpoint", lambda *args: None)
    monkeypatch.setattr(nightly, "settings_for", lambda p: SimpleNamespace(api_key="test-private", live_enabled=True))
    monkeypatch.setattr(nightly.time, "sleep", lambda *a: pytest.fail("healthy fallback must run immediately"))
    def validate(job, cfg, state, budget, directory, **kwargs):
        calls.append(cfg["provider"])
        if cfg["provider"] == "gemini":
            return stopped("blocked_provider_http_503", "ServerError:503"), budget - 1
        return {"status": "completed", "exitCode": 0}, budget - 1
    monkeypatch.setattr(nightly, "validate_with_provider_retries", validate)
    result, budget = nightly.validate_with_provider_failover({"class": "kelas8", "batch": "batch01"},
        {**config(), "provider": "gemini", "fallbackProviders": ["groq"], "fallbackOn503": True}, {}, 10, tmp_path)
    assert calls == ["gemini", "groq"] and budget == 8
    assert result["activeProvider"] == "groq" and result["apiCallsThisRun"] == 2


def test_temporary_provider_can_recover_after_other_provider_exhausts_quota(tmp_path, enabled, monkeypatch):
    calls, waits = [], []
    monkeypatch.setattr(failover, "activate_checkpoint", lambda *args: None)
    monkeypatch.setattr(nightly, "settings_for", lambda p: SimpleNamespace(api_key="test-private", live_enabled=True))
    monkeypatch.setattr(nightly.time, "sleep", waits.append)
    def validate(job, cfg, state, budget, directory, **kwargs):
        calls.append(cfg["provider"])
        if len(calls) == 1:
            return stopped("blocked_provider_http_503", "ServerError:503"), budget - 1
        if len(calls) == 2:
            return stopped("blocked_provider_quota_or_rate_limit", "ClientError:429"), budget - 1
        return {"status": "completed", "exitCode": 0}, budget - 1
    monkeypatch.setattr(nightly, "validate_with_provider_retries", validate)
    result, budget = nightly.validate_with_provider_failover({"class": "kelas8", "batch": "batch01"},
        {**config(), "provider": "gemini", "fallbackProviders": ["groq"], "fallbackOn503": True}, {}, 10, tmp_path)
    assert calls == ["gemini", "groq", "gemini"] and waits == [15]
    assert budget == 7 and result["status"] == "completed" and result["apiCallsThisRun"] == 3


def test_all_service_failures_have_bounded_recovery_and_one_shared_budget(tmp_path, enabled, monkeypatch):
    calls, waits = [], []
    monkeypatch.setattr(failover, "activate_checkpoint", lambda *args: None)
    monkeypatch.setattr(nightly, "settings_for", lambda p: SimpleNamespace(api_key="test-private", live_enabled=True))
    monkeypatch.setattr(nightly.time, "sleep", waits.append)
    def validate(job, cfg, state, budget, directory, **kwargs):
        calls.append(cfg["provider"])
        return stopped("blocked_provider_http_503", "ServerError:503"), budget - 1
    monkeypatch.setattr(nightly, "validate_with_provider_retries", validate)
    result, budget = nightly.validate_with_provider_failover({"class": "kelas8", "batch": "batch01"},
        {**config(), "provider": "gemini", "fallbackProviders": ["groq"], "fallbackOn503": True}, {}, 10, tmp_path)
    assert calls == ["gemini", "groq"] * 4 and waits == [15, 30, 60]
    assert budget == 2 and result["apiCallsThisRun"] == 8


@pytest.mark.parametrize("value", [None, "true", 1, []])
def test_invalid_503_policy_is_rejected(tmp_path, value):
    path = tmp_path / "config.json"
    path.write_text(json.dumps({**config(), "provider": "gemini", "fallbackProviders": ["groq"],
                                "fallbackOn503": value}), encoding="utf-8")
    with pytest.raises(ValueError, match="fallbackOn503"):
        nightly.read_config(path)


def test_service_recovery_keeps_running_while_completed_questions_increase(tmp_path, enabled, monkeypatch):
    calls, waits = [], []
    monkeypatch.setattr(failover, "activate_checkpoint", lambda *args: None)
    monkeypatch.setattr(nightly, "settings_for", lambda p: SimpleNamespace(api_key="test-private", live_enabled=p == "gemini"))
    monkeypatch.setattr(nightly.time, "sleep", waits.append)
    p = exercise.paths("kelas8", "batch01")["checkpoint"]
    p.parent.mkdir(parents=True)
    def validate(job, cfg, state, budget, directory, **kwargs):
        calls.append(cfg["provider"])
        cp = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {"items": {}, "requestedRuns": 1}
        cp["items"][str(len(calls))] = {"runs": [{"runIndex": 1, "status": "success"}],
                                      "aggregate": {"needsAdjudication": False}}
        cp["apiAttempts"] = len(calls)
        generator.atomic_write(cp, p)
        return ({"status": "completed", "exitCode": 0} if len(calls) == 5 else
                stopped("blocked_provider_http_503", "ServerError:503")), budget - 1
    monkeypatch.setattr(nightly, "validate_with_provider_retries", validate)
    result, budget = nightly.validate_with_provider_failover({"class": "kelas8", "batch": "batch01"},
        {**config(), "provider": "gemini", "fallbackProviders": ["groq"], "fallbackOn503": True}, {}, 10, tmp_path)
    assert calls == ["gemini"] * 5 and waits == [15] * 4
    assert budget == 5 and result["status"] == "completed" and result["apiCallsThisRun"] == 5
