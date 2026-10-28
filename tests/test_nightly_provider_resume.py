"""Transient retries share a budget and never cross a quota/auth stop."""
import json

import pytest

from scripts import nightly_pipeline as nightly
from tests.test_nightly_pipeline import config, workspace


def stopped(status="blocked_provider_temporarily_unavailable", code="ServerError:503"):
    return {"status": "validation_incomplete", "exitCode": 3,
            "providerStop": {"status": status, "errorCode": code, "message": "checkpoint saved"}}


def test_transient_retries_resume_same_job_and_count_all_attempts(tmp_path, monkeypatch):
    job = {"class": "kelas8", "batch": "batch01"}
    calls, waits, updates = [], [], []
    results = [stopped(), stopped(), {"status": "completed", "exitCode": 0}]
    costs = [2, 3, 1]
    def validate(current, cfg, state, budget, directory):
        index = len(calls)
        calls.append((current, budget))
        return results[index], budget - costs[index]
    monkeypatch.setattr(nightly, "validate_job", validate)
    monkeypatch.setattr(nightly.time, "sleep", waits.append)
    result, budget = nightly.validate_with_provider_retries(job, config(), {}, 10, tmp_path,
                                                           on_retry=updates.append)
    assert calls == [(job, 10), (job, 8), (job, 5)]
    assert waits == [15, 30] and budget == 4
    assert result["status"] == "completed" and result["apiCallsThisRun"] == 6
    assert len(result["transientRetries"]) == 2
    assert [value["status"] for value in updates] == ["retrying_provider"] * 2


@pytest.mark.parametrize("result", [
    stopped("blocked_provider_daily_quota", "ClientError:429"),
    stopped("blocked_provider_quota_or_rate_limit", "ClientError:429"),
    stopped("blocked_provider_configuration", "ClientError:401"),
    stopped("blocked_provider_temporarily_unavailable", "ClientError:429"),
    {"status": "validation_incomplete", "exitCode": 5},
    {"status": "completed", "exitCode": 0},
])
def test_quota_auth_nonprovider_and_success_results_never_retry(tmp_path, monkeypatch, result):
    calls = []
    def validate(*args):
        calls.append(True)
        return result, 9
    monkeypatch.setattr(nightly, "validate_job", validate)
    monkeypatch.setattr(nightly.time, "sleep", lambda *args: pytest.fail("must not retry this result"))
    actual, budget = nightly.validate_with_provider_retries({}, config(), {}, 10, tmp_path)
    assert calls == [True] and budget == 9 and actual["apiCallsThisRun"] == 1


def test_persistent_503_stops_after_configured_retries(tmp_path, monkeypatch):
    calls, waits = [], []
    def validate(job, cfg, state, budget, directory):
        calls.append(budget)
        return stopped(), budget - 1
    monkeypatch.setattr(nightly, "validate_job", validate)
    monkeypatch.setattr(nightly.time, "sleep", waits.append)
    result, budget = nightly.validate_with_provider_retries({}, config(), {}, 10, tmp_path)
    assert calls == [10, 9, 8, 7] and waits == [15, 30, 60]
    assert budget == 6 and result["exitCode"] == 3 and result["apiCallsThisRun"] == 4


def test_exhausted_shared_budget_prevents_another_retry(tmp_path, monkeypatch):
    monkeypatch.setattr(nightly, "validate_job", lambda *args: (stopped(), 0))
    monkeypatch.setattr(nightly.time, "sleep", lambda *args: pytest.fail("budget exhausted"))
    result, budget = nightly.validate_with_provider_retries({}, config(), {}, 1, tmp_path)
    assert budget == 0 and result["apiCallsThisRun"] == 1


@pytest.mark.parametrize("delays", [[0], [True], [-1], [61], ["15"], [1] * 6, None])
def test_invalid_retry_configuration_is_rejected(tmp_path, delays):
    cfg = {**config(), "providerRetryDelaysSeconds": delays}
    path = tmp_path / "config.json"
    path.write_text(json.dumps(cfg), encoding="utf-8")
    with pytest.raises(ValueError, match="providerRetryDelaysSeconds"):
        nightly.read_config(path)


def test_retry_status_is_published_before_waiting_and_quota_still_stops_run(workspace, monkeypatch):
    root, _ = workspace
    cfg = config()
    cfg["bootstrapJobs"] = [{"class": "kelas7", "batch": "batch01"}]
    calls = []
    def validate(job, config, state, budget, directory):
        calls.append(job["class"])
        return (stopped() if len(calls) == 1 else stopped("blocked_provider_daily_quota", "ClientError:429")), budget - 1
    def wait(delay):
        report = json.loads((root / "runs/nightly/latest.json").read_text(encoding="utf-8"))
        assert report["jobs"]["kelas7/batch01"]["status"] == "retrying_provider"
        assert delay == 15
    monkeypatch.setattr(nightly, "validate_job", validate)
    monkeypatch.setattr(nightly.time, "sleep", wait)
    monkeypatch.setattr(nightly, "screen_assessments", lambda *args: {"status": "waiting_for_data"})
    report = nightly.run(cfg, root / "runs/nightly")
    assert calls == ["kelas7", "kelas7"] and report["remainingApiCalls"] == 8
    assert report["stopNotice"]["status"] == "blocked_provider_daily_quota"
