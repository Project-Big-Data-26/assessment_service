"""Exercise stops immediately on 503 while other transient failures stay resumable."""
import json
from types import SimpleNamespace

import pytest

from app.llm import silver
from app.llm.config import GeminiSettings
from app.llm.silver import GeminiSilverAdapter, SilverRunResult
from scripts import generate_silver_labels_kelas1 as generator
from scripts import nightly_pipeline as nightly
from scripts import validate_exercise_batch as exercise
from scripts.revalidate_all_grades import complete
from tests.test_nightly_pipeline import config, workspace
from tests.test_nightly_provider_resume import stopped
from tests.test_revalidation_quota import setup_runner
from tests.test_silver_grade import silver_output


def test_503_stops_after_one_request_before_next_question(tmp_path, monkeypatch):
    class Adapter:
        calls = []
        def label_once(self, item, paths, *, run_index, **kwargs):
            self.calls.append(item["_id"])
            return SilverRunResult(runIndex=run_index, status="failed", errorCode="ServerError:503", latencyMs=1)
    adapter = Adapter()
    path = setup_runner(tmp_path, monkeypatch, adapter, runs=1, stop_on_503=True,
                        max_consecutive_provider_failures=3)
    assert generator.main() == 3
    cp = json.loads(path.read_text(encoding="utf-8"))
    assert adapter.calls == ["q1"] and cp["apiAttempts"] == 1
    assert cp["executionStatus"] == "blocked_provider_http_503"
    assert cp["stopReason"]["stopCategory"] == "http_503"
    assert "q2" not in cp["items"]


@pytest.mark.parametrize("code", ["ServerError:504", "ServerError:500", "ConnectTimeout:unknown"])
def test_other_transient_errors_leave_draft_and_continue_to_next_question(tmp_path, monkeypatch, code):
    class Adapter:
        calls = []
        def label_once(self, item, paths, *, run_index, **kwargs):
            self.calls.append(item["_id"])
            if item["_id"] == "q1":
                return SilverRunResult(runIndex=run_index, status="failed", errorCode=code, latencyMs=1)
            return SilverRunResult(runIndex=run_index, status="success", output=silver_output("Easy"), latencyMs=1)
    adapter = Adapter()
    path = setup_runner(tmp_path, monkeypatch, adapter, runs=1, stop_on_503=True,
                        max_consecutive_provider_failures=1)
    assert generator.main() == 0
    cp = json.loads(path.read_text(encoding="utf-8"))
    assert adapter.calls == ["q1", "q1", "q2"] and cp["apiAttempts"] == 3
    assert not complete(cp, ["q1"]) and complete(cp, ["q2"])
    assert cp["items"]["q1"]["runs"][0]["status"] == "failed"
    assert not cp.get("stopReason")


def test_503_after_504_prevents_second_question(tmp_path, monkeypatch):
    class Adapter:
        calls = 0
        def label_once(self, *args, run_index, **kwargs):
            self.calls += 1
            return SilverRunResult(runIndex=run_index, status="failed", latencyMs=1,
                                   errorCode="ServerError:504" if self.calls == 1 else "ServerError:503")
    adapter = Adapter()
    path = setup_runner(tmp_path, monkeypatch, adapter, runs=1, stop_on_503=True)
    assert generator.main() == 3
    cp = json.loads(path.read_text(encoding="utf-8"))
    assert adapter.calls == 2 and "q2" not in cp["items"]
    assert cp["stopReason"]["errorCode"] == "ServerError:503"


@pytest.mark.parametrize("code,reason,quota", [
    ("ClientError:429", None, True), ("ClientError:401", "api_key_invalid", False),
])
def test_quota_and_rejected_credentials_remain_explicit_blockers(tmp_path, monkeypatch, code, reason, quota):
    class Adapter:
        calls = 0
        def label_once(self, *args, run_index, **kwargs):
            self.calls += 1
            return SilverRunResult(runIndex=run_index, status="failed", latencyMs=1, errorCode=code,
                                   providerFailureReason=reason, quotaDailyExhausted=quota)
    adapter = Adapter()
    path = setup_runner(tmp_path, monkeypatch, adapter, runs=1, stop_on_503=True)
    assert generator.main() == 3 and adapter.calls == 1
    cp = json.loads(path.read_text(encoding="utf-8"))
    assert cp["stopReason"]["errorCode"] == code and "q2" not in cp["items"]


@pytest.mark.parametrize("enabled", [False, True])
def test_sdk_retries_504_but_503_policy_reaches_transport(monkeypatch, enabled):
    captured = {}
    def client(**kwargs):
        captured.update(kwargs)
        return object()
    monkeypatch.setattr(silver.genai, "Client", client)
    GeminiSilverAdapter(GeminiSettings(api_key="test-only", model="test-model"), stop_on_503=enabled)
    codes = captured["http_options"].retry_options.http_status_codes
    assert 504 in codes and (503 in codes) is (not enabled)


def test_nightly_does_not_retry_503_in_selected_policy(tmp_path, monkeypatch):
    calls = []
    def validate(*args):
        calls.append(True)
        return stopped(), 9
    monkeypatch.setattr(nightly, "validate_job", validate)
    monkeypatch.setattr(nightly.time, "sleep", lambda *args: pytest.fail("503 must stop immediately"))
    result, budget = nightly.validate_with_provider_retries({}, {**config(), "stopOn503": True}, {}, 10, tmp_path)
    assert calls == [True] and budget == 9 and result["exitCode"] == 3


def test_nightly_passes_policy_to_the_exercise_process(workspace, monkeypatch):
    root, _ = workspace
    monkeypatch.setattr(nightly, "job_identity", lambda *args: "503-policy")
    commands = []
    def process(command, **kwargs):
        commands.append(command)
        return SimpleNamespace(returncode=5)
    monkeypatch.setattr(nightly.subprocess, "run", process)
    job = nightly.source_identity("kelas7", "batch01")
    nightly.validate_job(job, {**config(), "stopOn503": True}, {}, 10, root)
    assert "--stop-on-503" in commands[0]


def test_exercise_passes_policy_to_gemini_labeler(tmp_path, monkeypatch):
    monkeypatch.setattr(exercise, "ROOT", tmp_path)
    p = exercise.paths("kelas8", "batch01")
    p["stage"].mkdir(parents=True)
    p["checkpoint"].write_text('{"requestedRuns": 1}', encoding="utf-8")
    commands = []
    def process(command, **kwargs):
        commands.append(command)
        return SimpleNamespace(returncode=0)
    monkeypatch.setattr(exercise.subprocess, "run", process)
    assert exercise.run_labeler("kelas8", "batch01", [], 10, stop_on_503=True) == 0
    assert "--stop-on-503" in commands[0]
    assert commands[0][commands[0].index("--runs") + 1] == "1"


def test_nightly_continues_later_class_after_504_but_stops_on_503(workspace, monkeypatch):
    root, _ = workspace
    jobs = [{"class": "kelas7", "batch": "batch01"}, {"class": "kelas8", "batch": "batch01"},
            {"class": "kelas9", "batch": "batch01"}]
    monkeypatch.setattr(nightly, "discover_jobs", lambda cfg: (jobs, []))
    monkeypatch.setattr(nightly, "validate_with_provider_retries", lambda job, *args, **kwargs: (
        stopped(code="ServerError:504" if job["class"] == "kelas7" else "ServerError:503"),
        9 if job["class"] == "kelas7" else 8))
    monkeypatch.setattr(nightly, "screen_assessments", lambda *args: {"status": "waiting_for_data"})
    report = nightly.run({**config(), "classes": ["kelas7", "kelas8", "kelas9"], "stopOn503": True}, root / "runs/nightly")
    assert report["jobs"]["kelas7/batch01"]["status"] == "validation_incomplete"
    assert report["providerStoppedAt"] == "kelas8/batch01"
    assert report["jobs"]["kelas9/batch01"]["status"] == "waiting_for_provider"
