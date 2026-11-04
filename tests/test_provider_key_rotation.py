import json
import os

import pytest

from app.llm import config as gemini_config, groq, providers
from app.llm.credentials import credential_slots, selected_api_key, use_credential_slot
from scripts import nightly_pipeline as nightly, provider_failover as failover
from scripts import validate_exercise_batch as exercise
from tests.test_nightly_pipeline import config
from tests.test_nightly_provider_resume import stopped


@pytest.fixture
def isolated_keys(monkeypatch, tmp_path):
    for provider in ("GEMINI", "GROQ"):
        for name in [f"{provider}_API_KEY", *(f"{provider}_API_KEY_{n}" for n in (1, 2, 3)),
                     f"EXERCISE_{provider}_KEY_SLOT"]:
            monkeypatch.delenv(name, raising=False)
        monkeypatch.setenv(f"{provider}_LIVE_ENABLED", "true")
    monkeypatch.setenv("LLM_PROVIDER", "gemini")
    monkeypatch.setenv("GEMINI_MODEL", "gemini-test")
    monkeypatch.setattr(providers, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(gemini_config, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(groq, "PROJECT_ROOT", tmp_path)
    monkeypatch.setattr(exercise, "ROOT", tmp_path)
    monkeypatch.setattr(exercise, "VALIDATION_NAMESPACE", "failover")
    return tmp_path


def test_empty_numbered_alias_retains_existing_key_even_after_dotenv_load(isolated_keys, monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "legacy-private")
    monkeypatch.setenv("GEMINI_API_KEY_1", "")
    assert credential_slots("gemini", {}) == [1]
    assert gemini_config.GeminiSettings.from_environment().api_key == "legacy-private"
    monkeypatch.setenv("GEMINI_API_KEY_1", "numbered-private")
    assert gemini_config.GeminiSettings.from_environment().api_key == "numbered-private"


def test_empty_duplicate_slots_are_skipped_and_sparse_slot_is_selected(isolated_keys, monkeypatch):
    monkeypatch.setenv("GROQ_API_KEY_2", "second-private")
    monkeypatch.setenv("GROQ_API_KEY_3", "second-private")
    assert providers.key_slots("groq") == [2]
    assert providers.has_credentials("groq")
    assert groq.GroqSettings.from_environment().api_key == "second-private"
    assert "second-private" not in repr(groq.GroqSettings.from_environment())


def test_empty_process_slot_does_not_reload_numbered_key_from_file(isolated_keys, monkeypatch):
    (isolated_keys / ".env").write_text("GROQ_API_KEY_1=file-first\nGROQ_API_KEY_2=file-second\n", encoding="utf-8")
    monkeypatch.setenv("GROQ_API_KEY_1", "")
    assert providers.key_slots("groq") == [2]
    assert groq.GroqSettings.from_environment().api_key == "file-second"


def test_file_slots_and_environment_precedence(isolated_keys, monkeypatch):
    (isolated_keys / ".env").write_text("GEMINI_API_KEY_1=file-first\nGEMINI_API_KEY_2=file-second\n", encoding="utf-8")
    assert providers.key_slots("gemini") == [1, 2]
    monkeypatch.setenv("GEMINI_API_KEY", "process-first")
    assert gemini_config.GeminiSettings.from_environment().api_key == "process-first"
    monkeypatch.setenv("GEMINI_API_KEY_2", "")
    assert providers.key_slots("gemini") == [1]
    monkeypatch.setenv("GEMINI_API_KEY", "")
    assert not providers.has_credentials("gemini")


def test_loader_can_explicitly_avoid_env_file(isolated_keys):
    (isolated_keys / ".env").write_text("GEMINI_API_KEY_2=file-private\n", encoding="utf-8")
    with pytest.raises(ValueError, match="GEMINI_API_KEY"):
        gemini_config.GeminiSettings.from_environment(load_env_file=False)


@pytest.mark.parametrize("slot", ["0", "4", "bad", "2"])
def test_bad_or_empty_slot_errors_never_expose_keys(isolated_keys, monkeypatch, slot):
    monkeypatch.setenv("GEMINI_API_KEY", "hidden-private")
    monkeypatch.setenv("EXERCISE_GEMINI_KEY_SLOT", slot)
    with pytest.raises(ValueError, match="slot is invalid or empty") as exc:
        selected_api_key("gemini", {})
    assert "hidden-private" not in str(exc.value)


def test_slot_selector_is_inherited_and_restored_on_failure(isolated_keys, monkeypatch):
    monkeypatch.setenv("EXERCISE_GROQ_KEY_SLOT", "3")
    with pytest.raises(RuntimeError):
        with use_credential_slot("groq", 2):
            # Child workers inherit this non-secret selection through os.environ.
            assert dict(os.environ)["EXERCISE_GROQ_KEY_SLOT"] == "2"
            raise RuntimeError("test")
    assert os.environ["EXERCISE_GROQ_KEY_SLOT"] == "3"


def test_additional_numbered_slots_are_discovered_and_selectable(isolated_keys, monkeypatch):
    values = {"GEMINI_API_KEY_1": "first-private", "GEMINI_API_KEY_4": "fourth-private",
              "GEMINI_API_KEY_5": "fifth-private", "GEMINI_API_KEY_9": "fifth-private"}
    assert credential_slots("gemini", values) == [1, 4, 5]
    with use_credential_slot("gemini", 5):
        assert selected_api_key("gemini", values) == "fifth-private"
    monkeypatch.setenv("GEMINI_API_KEY_4", "")
    assert credential_slots("gemini", values) == [1, 5]


def setup_rotation(monkeypatch):
    for provider in ("gemini", "groq"):
        for slot in (1, 2, 3):
            monkeypatch.setenv(f"{provider.upper()}_API_KEY_{slot}", f"private-{provider}-{slot}")
    monkeypatch.setattr(failover, "activate_checkpoint", lambda *args: None)
    return {**config(), "provider": "gemini", "fallbackProviders": ["groq"]}


def test_six_key_quota_rotation_has_one_budget_and_no_secret_in_report(isolated_keys, monkeypatch):
    cfg = setup_rotation(monkeypatch)
    calls, updates = [], []
    def validate(job, current, state, budget, directory, **kwargs):
        provider = current["provider"]
        slot = int(os.environ[f"EXERCISE_{provider.upper()}_KEY_SLOT"])
        assert providers.settings_for(provider).api_key == f"private-{provider}-{slot}"
        calls.append((provider, slot))
        return stopped("blocked_provider_quota_or_rate_limit", "ClientError:429"), budget - 1
    monkeypatch.setattr(nightly, "validate_with_provider_retries", validate)
    result, budget = nightly.validate_with_provider_failover({"class": "kelas8", "batch": "batch01"},
        cfg, {}, 10, isolated_keys, on_retry=updates.append)
    assert calls == [(p, slot) for p in ("gemini", "groq") for slot in (1, 2, 3)]
    assert budget == 4 and result["apiCallsThisRun"] == 6
    assert result["activeKeySlot"] == 3 and len(result["providerAttempts"]) == 6
    assert "private-" not in json.dumps([result, updates])
    assert "EXERCISE_GEMINI_KEY_SLOT" not in os.environ
    assert "EXERCISE_GROQ_KEY_SLOT" not in os.environ


def test_rotation_stops_after_success_and_skips_empty_duplicate_slots(isolated_keys, monkeypatch):
    cfg = setup_rotation(monkeypatch)
    monkeypatch.setenv("GEMINI_API_KEY_2", "")
    monkeypatch.setenv("GEMINI_API_KEY_3", "private-gemini-1")
    calls = []
    def validate(job, current, state, budget, directory, **kwargs):
        calls.append((current["provider"], int(os.environ[f"EXERCISE_{current['provider'].upper()}_KEY_SLOT"])))
        return (stopped("blocked_provider_daily_quota", "ClientError:429") if len(calls) == 1 else
                {"status": "completed", "exitCode": 0}), budget - 1
    monkeypatch.setattr(nightly, "validate_with_provider_retries", validate)
    result, budget = nightly.validate_with_provider_failover({"class": "kelas8", "batch": "batch01"},
        cfg, {}, 10, isolated_keys)
    assert calls == [("gemini", 1), ("groq", 1)]
    assert result["status"] == "completed" and budget == 8


def test_auth_failure_does_not_silently_rotate(isolated_keys, monkeypatch):
    cfg = setup_rotation(monkeypatch)
    monkeypatch.setattr(nightly, "validate_with_provider_retries", lambda *a, **kw:
        (stopped("blocked_provider_configuration", "ClientError:401"), a[3] - 1))
    result, budget = nightly.validate_with_provider_failover({"class": "kelas8", "batch": "batch01"},
        cfg, {}, 10, isolated_keys)
    assert budget == 9 and len(result["providerAttempts"]) == 1


def test_shared_budget_exhaustion_stops_before_next_key(isolated_keys, monkeypatch):
    cfg = setup_rotation(monkeypatch)
    monkeypatch.setattr(nightly, "validate_with_provider_retries", lambda *a, **kw:
        (stopped("blocked_provider_quota_or_rate_limit", "ClientError:429"), a[3] - 1))
    result, budget = nightly.validate_with_provider_failover({"class": "kelas8", "batch": "batch01"},
        cfg, {}, 1, isolated_keys)
    assert budget == 0 and len(result["providerAttempts"]) == 1


def test_single_provider_multiple_keys_enable_runner_failover(isolated_keys, monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY_1", "first-private")
    monkeypatch.setenv("GEMINI_API_KEY_2", "second-private")
    assert nightly.uses_key_failover({"provider": "gemini"})


def test_pinned_slot_is_used_by_runner_and_settings(isolated_keys, monkeypatch):
    cfg = setup_rotation(monkeypatch)
    monkeypatch.setenv("EXERCISE_GROQ_KEY_SLOT", "2")
    monkeypatch.setenv("GEMINI_LIVE_ENABLED", "false")
    assert providers.key_slots("groq") == [2]
    assert groq.GroqSettings.from_environment().api_key == "private-groq-2"
    def validate(job, current, state, budget, directory, **kwargs):
        assert current["provider"] == "groq"
        assert os.environ["EXERCISE_GROQ_KEY_SLOT"] == "2"
        return {"status": "completed", "exitCode": 0}, budget - 1
    monkeypatch.setattr(nightly, "validate_with_provider_retries", validate)
    result, budget = nightly.validate_with_provider_failover({"class": "kelas8", "batch": "batch01"},
        cfg, {}, 10, isolated_keys)
    assert budget == 9 and result["activeKeySlot"] == 2
    assert os.environ["EXERCISE_GROQ_KEY_SLOT"] == "2"


def test_recovery_remembers_each_slot_without_retrying_quota_slots(isolated_keys, monkeypatch):
    cfg = setup_rotation(monkeypatch)
    cfg.update(fallbackOn503=True, providerRetryDelaysSeconds=[0])
    calls = []
    monkeypatch.setattr(nightly.time, "sleep", lambda seconds: None)
    def validate(job, current, state, budget, directory, **kwargs):
        pair = (current["provider"], int(os.environ[f"EXERCISE_{current['provider'].upper()}_KEY_SLOT"]))
        calls.append(pair)
        if len(calls) == 7:
            return {"status": "completed", "exitCode": 0}, budget - 1
        error = stopped("blocked_provider_http_503", "ServerError:503") if pair == ("gemini", 1) else stopped(
            "blocked_provider_quota_or_rate_limit", "ClientError:429")
        return error, budget - 1
    monkeypatch.setattr(nightly, "validate_with_provider_retries", validate)
    result, budget = nightly.validate_with_provider_failover({"class": "kelas8", "batch": "batch01"},
        cfg, {}, 10, isolated_keys)
    assert calls == [(p, n) for p in ("gemini", "groq") for n in (1, 2, 3)] + [("gemini", 1)]
    assert result["status"] == "completed" and budget == 3


def test_all_keys_diagnostic_checks_each_slot_offline(isolated_keys, monkeypatch):
    from scripts import check_exercise_providers as probe
    setup_rotation(monkeypatch)
    monkeypatch.setattr(probe, "ROOT", isolated_keys)
    monkeypatch.setattr("sys.argv", ["probe", "--all-keys", "--providers", "gemini", "groq"])
    assert probe.main() == 0
    result = json.loads((isolated_keys / "runs/nightly_pipeline/exercise_provider_connection_check.json").read_text())
    assert [(r["provider"], r["keySlot"]) for r in result["results"]] == [
        (p, n) for p in ("gemini", "groq") for n in (1, 2, 3)]
    assert all(r["apiCalls"] == 0 for r in result["results"])
    assert "private-" not in json.dumps(result)


@pytest.mark.parametrize("answer, verified, expected", [
    ("B", "verified", True), ("5", "verified", True),
    ("A", "verified", False), ("4", "verified", False),
    ("5", "unverifiable", False), (None, "unverifiable", False),
])
def test_probe_accepts_correct_option_or_value_only(answer, verified, expected):
    from types import SimpleNamespace
    from scripts.check_exercise_providers import probe_passed
    response = SimpleNamespace(status="success", output=SimpleNamespace(
        answerKeyStatus=verified, verifiedAnswerKey=answer))
    assert probe_passed(response) is expected
