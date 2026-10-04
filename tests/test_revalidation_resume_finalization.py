"""Offline resume reports must distinguish completed evidence from quota drafts."""
from copy import deepcopy
import json

import pytest

from scripts import balance_operational_difficulty as balance
from scripts import finalize_revalidation_resume as finalizer
from tests.test_operational_balance import fixture


def save(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def make_fixture(tmp_path, monkeypatch, *, partial=False):
    batch = "fixture_resume"
    run_dir = tmp_path / "runs" / batch
    source_root = tmp_path / "output/pretest"
    source = source_root / "kelas1/soal_pretest_db.json"
    bundle = source.parent / "hasil_validasi"
    checkpoint_path = source.parent / batch / "silver_labels.json"
    frozen = source.parent / batch / "final_snapshot_v1/silver_labels.json"
    rows, decisions = fixture([1, 2, 3, 4, 5, 6], inactive=True)
    rubric = finalizer.silver_rubric(1, track="regular")
    for decision in decisions:
        decision["llmAdvisory"]["rubricVersion"] = rubric.version
    save(source, rows)
    save(bundle / "validation_results.json", rows)
    save(bundle / "decisions.json", {"items": decisions})
    checkpoint = {"sourceGrade": 1, "sourceHash": finalizer.digest(source), "subjectTrack": "regular",
                  "rubricVersion": rubric.version, "promptVersion": rubric.prompt_version,
                  "executionStatus": "completed_batch", "apiAttempts": 18, "items": {}}
    for index, row in enumerate(rows):
        checkpoint["items"][row["_id"]] = {
            "runs": [{"runIndex": j, "status": "success", "responseHash": f"paid-{index}-{j}",
                      "usage": {"promptTokens": 4, "outputTokens": 2, "thinkingTokens": 1, "totalTokens": 7}}
                     for j in range(1, 4)],
            "aggregate": {"needsAdjudication": False, "eligibleForTraining": index != 0,
                          "heads": {"intendedDifficulty": {"label": "Easy"}}}, "adjudication": None}
    checkpoint["summary"] = finalizer.summarize(checkpoint)
    save(frozen, checkpoint)
    manifest = {"databaseExport": {"subjectTrack": "regular", "sourceClass": 1},
                "sourceFiles": {"source": {"path": str(source), "sha256": finalizer.digest(source)},
                                "blindCheckpoint": {"path": str(frozen), "sha256": finalizer.digest(frozen)}}}
    save(bundle / "manifest.json", manifest)
    monkeypatch.setattr(balance, "verify_bundle", lambda *_: None)
    monkeypatch.setattr(balance, "load_decision_bundle", lambda p: finalizer.read(p / "decisions.json"))
    operational = balance.export_verified_operational_balance(source, bundle, grade=1, track="regular")
    monkeypatch.setattr(finalizer, "verify_bundle", lambda *_: None)
    monkeypatch.setattr(finalizer, "verify_evidence", lambda *_: None)
    monkeypatch.setattr(finalizer, "load_decision_bundle", lambda p: finalizer.read(p / "decisions.json"))
    monkeypatch.setattr(finalizer, "current_decision", lambda row, record, directory: ({}, {
        "fullComplete": len(record.get("runs", [])) == 3 and record.get("aggregate", {}).get("needsAdjudication") is False,
        "missingRunIndices": sorted({1, 2, 3} - {run["runIndex"] for run in record.get("runs", [])}),
        "needsAdjudication": len(record.get("runs", [])) == 3 and record.get("aggregate", {}).get("needsAdjudication") is True}))
    monkeypatch.setattr(finalizer, "build_initialization_report", lambda *a, **kw: {
        "irt": {"calibrated": False, "parameters": None, "studentAbility": None, "status": "waiting_for_data"},
        "rubricVersions": ["old-test-rubric" if partial else rubric.version],
        "localResponseInventory": {"matchingScoredEvents": 0}})
    if partial:
        checkpoint["items"]["5"]["runs"].pop()
        checkpoint["apiAttempts"] = 17
        checkpoint["executionStatus"] = "blocked_provider_daily_quota"
        checkpoint["summary"] = finalizer.summarize(checkpoint)
        old_checkpoint = finalizer.read(frozen)
        old_checkpoint["rubricVersion"] = "old-test-rubric"
        save(frozen, old_checkpoint)
        manifest["sourceFiles"]["blindCheckpoint"]["sha256"] = finalizer.digest(frozen)
        save(bundle / "manifest.json", manifest)
    save(checkpoint_path, checkpoint)
    state = {"batchName": batch, "executionStatus": "blocked_provider_daily_quota" if partial else "completed",
             "phase": "full", "apiAttempts": checkpoint["apiAttempts"],
             "operationalBankPolicy": "relative_thirds_per_active_class",
             "operationalBalanceOutputName": "operational_balance_v2",
             "classes": [{"name": "kelas1", "grade": 1, "subjectTrack": "regular",
                          "source": str(source), "sourceHash": finalizer.digest(source),
                          "checkpoint": str(checkpoint_path), "fullComplete": not partial}],
             "stopReason": {"errorCode": "ClientError:429", "quotaLimits": [
                 {"quotaId": "GenerateRequestsPerDayPerProjectPerModel-FreeTier", "quotaValue": "500"}],
                 "message": "Never include the credential in a report: secret-test-key"} if partial else None}
    save(run_dir / "execution.json", state)
    (run_dir / "REPORT.md").write_text("keep original report\n", encoding="utf-8")
    baseline_path = run_dir / "resume_balanced_v2.json"
    save(baseline_path, {"batchName": batch, "baselineApiAttempts": 0,
                         "baselineSuccessfulInitialRuns": 1,
                         "baselineEvidenceSelection": "selected before capture; not historical proof",
                         "successfulEvidence": [{"class": "kelas1", "questionId": "1", "runIndex": 1,
                                                 "run": deepcopy(checkpoint["items"]["1"]["runs"][0])}]})
    return {"run_dir": run_dir, "source_root": source_root, "batch_name": batch,
            "baseline_path": baseline_path, "classes": [("kelas1", 1, "regular")]}, source, bundle, checkpoint_path, operational


def test_completed_report_preserves_paid_inputs_and_separates_relative_labels(tmp_path, monkeypatch):
    kwargs, source, bundle, checkpoint, operational = make_fixture(tmp_path, monkeypatch)
    protected = [source, checkpoint, kwargs["baseline_path"], kwargs["run_dir"] / "execution.json",
                 kwargs["run_dir"] / "REPORT.md", *bundle.rglob("*.json")]
    before = {path: path.read_bytes() for path in protected}
    report = finalizer.finalize(**kwargs)
    assert report["fullComplete"] and report["completedClasses"] == ["kelas1"]
    assert report["workingTotals"]["successfulInitialRuns"] == 18
    assert report["apiUsage"]["newApplicationCallsSinceBaseline"] == 18
    assert report["apiUsage"]["successfulResponseRecordedTokens"]["totalTokens"] == 126
    assert report["successfulEvidencePreservation"]["verifiedRuns"] == 1
    assert not report["successfulEvidencePreservation"]["historicalMutationsBeforeBaselineCaptureVerified"]
    entry = report["classes"][0]
    assert entry["activeAiQualifiedDifficultyCounts"]["easy"] == 5
    assert entry["operationalBalance"]["activeDifficultyCounts"] == {"easy": 2, "medium": 2, "hard": 1, "undecided": 0}
    assert entry["operationalBalance"]["zeroAiSupportLabels"] == 3
    assert entry["operationalBalance"]["validationResults"].startswith("../../output/pretest/")
    assert entry["irtReadiness"]["status"] == "waiting_for_data"
    assert report["newApiCallsDuringFinalization"] == 0
    assert {path: path.read_bytes() for path in before} == before
    assert (kwargs["run_dir"] / "RESUME_REPORT.md").exists()
    assert (kwargs["run_dir"] / "irt_readiness/kelas1.json").exists()
    assert "original_verified_ai_silver" in (kwargs["run_dir"] / "resume_final_verification.json").read_text(encoding="utf-8")


def test_quota_partial_report_leaves_old_active_rubric_and_skips_its_balanced_pointer(tmp_path, monkeypatch):
    kwargs, _, _, _, _ = make_fixture(tmp_path, monkeypatch, partial=True)
    report = finalizer.finalize(**kwargs)
    assert not report["fullComplete"] and report["remainingClasses"] == ["kelas1"]
    assert report["workingTotals"]["missingInitialRuns"] == 1
    assert report["workingTotals"]["finalQuestions"] == 5
    assert report["classes"][0]["activeRubricVersion"] == "old-test-rubric"
    assert report["classes"][0]["operationalBalance"] is None
    assert report["classes"][0]["irtReadiness"]["activeRubricVersions"] == ["old-test-rubric"]
    assert report["stopReason"]["errorCode"] == "ClientError:429"
    assert "secret-test-key" not in json.dumps(report)
    assert report["training"]["status"] == "not_started_revalidation_incomplete"
    assert not report["training"]["actualTrainingAttemptRecorded"]


def test_finalization_refuses_a_running_process_before_writing(tmp_path, monkeypatch):
    kwargs, _, _, _, _ = make_fixture(tmp_path, monkeypatch)
    path = kwargs["run_dir"] / "execution.json"
    state = finalizer.read(path)
    state["executionStatus"] = "running"
    save(path, state)
    with pytest.raises(ValueError, match="process has stopped"):
        finalizer.finalize(**kwargs)
    assert not (kwargs["run_dir"] / "resume_final_verification.json").exists()
    assert not (kwargs["run_dir"] / "irt_readiness").exists()


def test_stale_operational_source_hash_is_rejected(tmp_path, monkeypatch):
    kwargs, source, bundle, _, _ = make_fixture(tmp_path, monkeypatch)
    rows = finalizer.read(source)
    rows[1]["text"] = "edited source"
    save(source, rows)
    with pytest.raises(ValueError, match="source question hash mismatch"):
        finalizer.verify_current_operational(source, bundle, source.parent / "operational_balance_v2", grade=1, track="regular")


def test_current_pointer_with_old_ai_evidence_is_rejected(tmp_path, monkeypatch):
    _, source, bundle, _, _ = make_fixture(tmp_path, monkeypatch)
    path = bundle / "decisions.json"
    decisions = finalizer.read(path)
    decisions["items"][1]["llmAdvisory"]["votes"]["intendedDifficulty"]["lockedEvidence"]["profile"]["dependentSteps"] = 9
    save(path, decisions)
    with pytest.raises(ValueError, match="stale or refers to another"):
        finalizer.verify_current_operational(source, bundle, source.parent / "operational_balance_v2", grade=1, track="regular")


def test_three_initial_runs_with_pending_adjudication_are_still_partial(tmp_path, monkeypatch):
    kwargs, _, _, checkpoint_path, _ = make_fixture(tmp_path, monkeypatch, partial=True)
    checkpoint = finalizer.read(checkpoint_path)
    frozen = checkpoint_path.parent / "final_snapshot_v1/silver_labels.json"
    checkpoint["items"]["5"]["runs"] = finalizer.read(frozen)["items"]["5"]["runs"]
    checkpoint["items"]["5"]["aggregate"]["needsAdjudication"] = True
    checkpoint["apiAttempts"] = 18
    checkpoint["summary"] = finalizer.summarize(checkpoint)
    save(checkpoint_path, checkpoint)
    state_path = kwargs["run_dir"] / "execution.json"
    state = finalizer.read(state_path)
    state["apiAttempts"] = 18
    save(state_path, state)
    report = finalizer.finalize(**kwargs)
    assert not report["fullComplete"]
    assert report["workingTotals"]["missingInitialRuns"] == 0
    assert report["workingTotals"]["pendingAdjudications"] == 1
    assert report["workingTotals"]["finalQuestions"] == 5
    assert report["classes"][0]["operationalBalance"] is None


def test_export_schema_content_changes_and_changed_paid_baseline_fail_without_reports(tmp_path, monkeypatch):
    kwargs, _, bundle, _, _ = make_fixture(tmp_path, monkeypatch)
    validation = bundle / "validation_results.json"
    rows = finalizer.read(validation)
    rows[1]["extra_field"] = "not from source"
    save(validation, rows)
    with pytest.raises(ValueError, match="source schema"):
        finalizer.finalize(**kwargs)
    assert not (kwargs["run_dir"] / "resume_final_verification.json").exists()
    rows[1].pop("extra_field")
    save(validation, rows)
    baseline = finalizer.read(kwargs["baseline_path"])
    baseline["successfulEvidence"][0]["run"]["responseHash"] = "changed paid evidence"
    save(kwargs["baseline_path"], baseline)
    with pytest.raises(ValueError, match="successful run was changed"):
        finalizer.finalize(**kwargs)
    assert not (kwargs["run_dir"] / "resume_final_verification.json").exists()
    assert not (kwargs["run_dir"] / "irt_readiness").exists()


def test_retention_without_an_evidence_baseline_is_not_claimed_and_errors_are_secret_free():
    result = finalizer.verify_retained_evidence({}, {})
    assert result["status"] == "not_verified_no_baseline_evidence"
    result = finalizer.sanitized_stop_reason({"errorCode": "secret via arbitrary text", "providerFailureReason": "secret-key",
                                             "quotaLimits": [{"quotaId": "AIza-private-key", "quotaValue": "500", "token": "secret"}]})
    assert result == {"errorCode": "redacted", "providerFailureReason": "redacted_provider_reason",
                      "quotaLimits": [{"quotaValue": "500"}]}


def test_failed_paid_usage_copied_to_retry_history_is_counted_once():
    result = {"status": "failed", "runIndex": 2, "responseId": "same-paid-response",
              "usage": {"promptTokens": 12, "outputTokens": 3, "totalTokens": 15}}
    checkpoint = {"items": {"q1": {"runs": [result], "attemptHistory": [deepcopy(result)],
                                    "retryHistory": [deepcopy(result)]}}}
    assert finalizer.retained_failed_usage(checkpoint) == {"promptTokens": 12, "outputTokens": 3,
                                                         "thinkingTokens": 0, "totalTokens": 15}
