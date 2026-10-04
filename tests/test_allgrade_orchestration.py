"""Verify shared provider stops and preservation of revalidation history."""

import json
from pathlib import Path
import sys

import pytest

from app.llm.config import GeminiSettings
from scripts import generate_silver_labels_kelas1 as generator
from scripts import revalidate_all_grades as orchestration
from tests.test_blind_pilot_audit import question, record


def save(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value), encoding="utf-8")


def setup_main(tmp_path, monkeypatch, *, train=False):
    monkeypatch.setattr(orchestration, "ROOT", tmp_path)
    monkeypatch.setattr(generator, "ROOT", tmp_path)
    monkeypatch.setattr(orchestration, "CLASSES", [("kelas1", 1, "regular"), ("kelas11_tl", 11, "tl")])
    monkeypatch.setattr(orchestration.GeminiSettings, "from_environment",
                        lambda: GeminiSettings(api_key="test-only", model="test-model"))
    monkeypatch.setattr(orchestration, "verify_evidence", lambda *args: None)
    monkeypatch.setattr(orchestration, "write_active_index", lambda *args: None)
    source_root = tmp_path / "output/pretest"
    for name, _, _ in orchestration.CLASSES:
        save(source_root / name / "soal_pretest_db.json", [question("q1")])
        save(source_root / name / "hasil_validasi/validation_results.json",
             [{"_id": "q1", "cognitive_level": "easy"}])
    argv = ["revalidate_all_grades.py", "--source-root", str(source_root), "--batch-name", "revision",
            "--pilot-per-class", "1", "--max-api-calls", "20", "--execute"]
    if train:
        argv.append("--train")
    monkeypatch.setattr(sys, "argv", argv)
    return source_root, tmp_path / "runs/revision/execution.json"


def successful_checkpoint(path: Path, source: Path, *, label="Hard") -> None:
    checkpoint = orchestration.read(path)
    item = record(orchestration.read(source)[0])
    item["aggregate"]["needsAdjudication"] = False
    item["aggregate"]["heads"]["intendedDifficulty"]["label"] = label
    checkpoint["items"] = {"q1": item}
    checkpoint.update(executionStatus="completed_batch", apiAttempts=3)
    checkpoint["summary"] = generator.summarize(checkpoint)
    save(path, checkpoint)


def test_main_stops_all_classes_after_one_shared_provider_429(tmp_path, monkeypatch):
    _, state_path = setup_main(tmp_path, monkeypatch)
    calls = []

    def provider_stop(script, arguments, log, **kwargs):
        calls.append((script, arguments))
        output = Path(arguments[arguments.index("--output") + 1])
        checkpoint = orchestration.read(output)
        checkpoint.update(executionStatus="blocked_provider_quota_or_rate_limit", apiAttempts=1,
                          stopReason={"errorCode": "ClientError:429"})
        save(output, checkpoint)
        return 3

    monkeypatch.setattr(orchestration, "run_script", provider_stop)
    monkeypatch.setattr(orchestration, "package_class",
                        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("no promotion after a provider stop")))
    assert orchestration.main() == 3
    state = orchestration.read(state_path)
    assert len(calls) == state["apiAttempts"] == 1
    assert state["blockedByClass"] == "kelas1"
    assert state["stopReason"]["errorCode"] == "ClientError:429"
    assert "--stop-on-quota" in calls[0][1] and "--question-id" in calls[0][1]
    assert calls[0][1][calls[0][1].index("--workers") + 1] == "1"
    queued = orchestration.read(Path(state["classes"][1]["checkpoint"]))
    assert queued["executionStatus"] == "queued" and not queued["items"]
    assert not any(entry["promoted"] for entry in state["classes"])


def test_main_resume_reuses_paid_pilot_and_keeps_original_before_after_labels(tmp_path, monkeypatch):
    _, state_path = setup_main(tmp_path, monkeypatch)
    calls = []

    def generate(script, arguments, log, **kwargs):
        calls.append(script)
        successful_checkpoint(Path(arguments[arguments.index("--output") + 1]),
                              Path(arguments[arguments.index("--source") + 1]))
        return 0

    def promote(source, working, directory, **kwargs):
        active = source.parent / "hasil_validasi/validation_results.json"
        archive = directory / "final_snapshot_v1/previous_active_report/validation_results.json"
        if not archive.is_file():
            save(archive, orchestration.read(active))
        save(active, [{"_id": "q1", "cognitive_level": "hard"}])

    monkeypatch.setattr(orchestration, "run_script", generate)
    monkeypatch.setattr(orchestration, "package_class", promote)
    assert orchestration.main() == 0
    first = orchestration.read(state_path)
    assert len(calls) == 2 and first["apiAttempts"] == 6
    assert all(result["oldLabel"] == "easy" and result["newLabel"] == "Hard" for result in first["pilotResults"])
    assert orchestration.main() == 0
    resumed = orchestration.read(state_path)
    assert len(calls) == 2 and resumed["apiAttempts"] == 6
    assert resumed["pilotResults"] == first["pilotResults"]
    assert all(entry["pilotBaselineLabels"] == {"q1": "easy"} for entry in resumed["classes"])


def test_legacy_resume_recovers_original_pilot_label_from_archive(tmp_path):
    source = tmp_path / "kelas1/soal_pretest_db.json"
    directory = source.parent / "revision"
    save(source, [question("q1")])
    save(source.parent / "hasil_validasi/validation_results.json", [{"_id": "q1", "cognitive_level": "hard"}])
    save(directory / "final_snapshot_v1/previous_active_report/validation_results.json",
         [{"_id": "q1", "cognitive_level": "medium"}])
    assert orchestration.pilot_baseline(source, directory, ["q1"], {"promoted": True}, []) == {"q1": "medium"}


def test_balance_exports_only_completed_classes_and_stop_refreshes_drafts(tmp_path, monkeypatch):
    _, state_path = setup_main(tmp_path, monkeypatch)
    sys.argv.extend(["--balance-bank", "--export-progress"])
    balanced, exports = [], []

    def execute(script, arguments, log, **kwargs):
        output = Path(arguments[arguments.index("--output") + 1])
        source = Path(arguments[arguments.index("--source") + 1])
        if source.parent.name == "kelas1":
            successful_checkpoint(output, source)
            return 0
        cp = orchestration.read(output)
        cp.update(executionStatus="blocked_provider_daily_quota", apiAttempts=1,
                  stopReason={"errorCode": "ClientError:429"})
        save(output, cp)
        return 3

    monkeypatch.setattr(orchestration, "run_script", execute)
    monkeypatch.setattr(orchestration, "package_class", lambda *args, **kwargs: None)
    monkeypatch.setattr(orchestration, "balance_completed_class",
                        lambda entry, name: balanced.append(entry["name"]))
    monkeypatch.setattr(orchestration, "export_batch_progress", lambda *args: exports.append(args))
    assert orchestration.main() == 3
    # Pilot stops before any full-class export; stale old-class evidence must not be presented as new.
    assert balanced == [] and len(exports) == 1
    state = orchestration.read(state_path)
    assert state["operationalBankPolicy"] == "relative_thirds_per_active_class"
    assert state["blockedByClass"] == "kelas11_tl"


def test_balancing_is_applied_per_promoted_class_and_summarized(tmp_path, monkeypatch):
    _, state_path = setup_main(tmp_path, monkeypatch)
    sys.argv.append("--balance-bank")
    calls = []

    def execute(script, arguments, log, **kwargs):
        successful_checkpoint(Path(arguments[arguments.index("--output") + 1]),
                              Path(arguments[arguments.index("--source") + 1]))
        return 0

    monkeypatch.setattr(orchestration, "run_script", execute)
    monkeypatch.setattr(orchestration, "package_class", lambda *args, **kwargs: None)

    def balanced(entry, name):
        assert entry["promoted"] is True
        calls.append((entry["name"], name))
        return {"activeDistribution": {"easy": 1, "medium": 0, "hard": 0}, "provenance": "relative_bank_quota"}

    monkeypatch.setattr(orchestration, "balance_completed_class", balanced)
    assert orchestration.main() == 0
    assert calls == [("kelas1", "operational_balance_v2"), ("kelas11_tl", "operational_balance_v2")]
    summary = orchestration.read(state_path.parent / "operational_balance_summary.json")
    assert all(e["validationComplete"] and e["operationalBalance"]["provenance"] == "relative_bank_quota"
               for e in summary["classes"])


def test_missing_aggregate_or_duplicate_run_index_is_not_complete():
    runs = [{"runIndex": index, "status": "success"} for index in (1, 2, 3)]
    item = {"runs": runs}
    assert not orchestration.complete({"items": {"q1": item}}, ["q1"])
    item["aggregate"] = {"needsAdjudication": False}
    assert orchestration.complete({"items": {"q1": item}}, ["q1"])
    item["runs"] = [*runs, runs[0]]
    assert not orchestration.complete({"items": {"q1": item}}, ["q1"])


def test_training_retry_chooses_new_directory_and_keeps_existing_report(tmp_path):
    previous = tmp_path / "training/readiness.json"
    save(previous, {"trainingStatus": "blocked_data_gates", "failures": ["hard_train_support"]})
    before = previous.read_bytes()
    assert orchestration.next_training_directory(tmp_path) == tmp_path / "training_attempt_2"
    (tmp_path / "training_attempt_2").mkdir()
    assert orchestration.next_training_directory(tmp_path) == tmp_path / "training_attempt_3"
    assert previous.read_bytes() == before


@pytest.mark.parametrize("training_status", ["completed", "completed_candidate"])
def test_completed_training_is_reused_on_resume_including_legacy_state(tmp_path, monkeypatch, training_status):
    _, state_path = setup_main(tmp_path, monkeypatch, train=True)
    calls = []

    def execute(script, arguments, log, **kwargs):
        calls.append(script)
        if script == "generate_silver_labels_kelas1.py":
            successful_checkpoint(Path(arguments[arguments.index("--output") + 1]),
                                  Path(arguments[arguments.index("--source") + 1]))
        elif script == "prepare_allgrade_retraining.py":
            output = Path(arguments[arguments.index("--output-dir") + 1])
            save(output / "readiness.json", {"trainingStatus": training_status, "trainingExitCode": 0})
        else:
            raise AssertionError(script)
        return 0

    monkeypatch.setattr(orchestration, "run_script", execute)
    monkeypatch.setattr(orchestration, "package_class", lambda *args, **kwargs: None)
    assert orchestration.main() == 0
    state = orchestration.read(state_path)
    assert calls.count("prepare_allgrade_retraining.py") == 1
    assert state["trainingAttempts"][0]["status"] == training_status
    assert state["trainingStatus"] == training_status and state["productionModelPromoted"] is False
    # The current runner must reuse the candidate with its saved attempt history.
    assert orchestration.main() == 0
    assert calls.count("prepare_allgrade_retraining.py") == 1
    state = orchestration.read(state_path)
    # Recover completion from the immutable readiness report of an older runner.
    state.pop("trainingAttempts")
    save(state_path, state)
    assert orchestration.main() == 0
    assert calls.count("prepare_allgrade_retraining.py") == 1
    assert calls.count("generate_silver_labels_kelas1.py") == 2
    resumed = orchestration.read(state_path)
    assert resumed["executionStatus"] == "completed"
    assert resumed["trainingStatus"] == training_status
    assert resumed["trainingAttempts"][0]["status"] == training_status
    assert resumed["productionModelPromoted"] is False


def test_irt_sidecar_is_finalized_before_new_results_are_promoted(tmp_path, monkeypatch):
    monkeypatch.setattr(orchestration, "ROOT", tmp_path)
    source = tmp_path / "kelas1/soal_pretest_db.json"
    directory = source.parent / "revision"
    working = directory / "silver_labels.json"
    snapshot = directory / "final_snapshot_v1"
    bundle = snapshot / "bundle"
    save(source, [question("q1")])
    save(working, {"sourceGrade": 1})
    save(snapshot / "silver_labels.json", {"sourceGrade": 1})
    save(bundle / "manifest.json", {})
    save(bundle / "validation_results.json", [{"_id": "q1", "cognitive_level": "hard"}])
    save(snapshot / "audit/pilot_audit.json", {})
    (snapshot / "audit/PILOT_AUDIT.md").write_text("Audit", encoding="utf-8")
    monkeypatch.setattr(orchestration, "verify_evidence", lambda *args: None)
    monkeypatch.setattr(orchestration, "verify_bundle", lambda *args: None)
    calls = []

    def finalize(path, *, db_path):
        calls.append((path, db_path))
        assert not (source.parent / "hasil_validasi").exists()
        save(path / "bukti_validasi/irt_initialization.json", {"irt": {"status": "waiting_for_data"}})

    monkeypatch.setattr(orchestration, "finalize_irt_sidecar", finalize)
    orchestration.package_class(source, working, directory, promote=True)
    active = source.parent / "hasil_validasi"
    assert calls == [(bundle, tmp_path / "data/local/assessments.sqlite3")]
    assert (active / "bukti_validasi/irt_initialization.json").is_file()
    assert orchestration.read(active / "validation_results.json") == orchestration.read(bundle / "validation_results.json")
