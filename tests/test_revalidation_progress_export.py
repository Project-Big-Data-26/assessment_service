"""Draft exports must preserve source content without reusing old labels."""

from copy import deepcopy
import hashlib
import json

import pytest

from app.llm.silver import (
    SilverAdjudicationResult, SilverRunResult, aggregate_silver_runs, build_silver_prompt,
)
from scripts import export_revalidation_progress as exporter
from scripts import generate_silver_labels_kelas1 as generator
from tests.test_blind_pilot_audit import question
from tests.test_silver_grade import silver_output


def make_export_fixture(tmp_path, monkeypatch, run_count, *, content_blocker=False):
    monkeypatch.setattr(generator, "ROOT", tmp_path)
    source = tmp_path / "kelas1/soal_pretest_db.json"
    source.parent.mkdir()
    original = {**question("q1"), "cognitive_level": "hard", "cognitive_score": 1400,
                "confidence_score": 100, "status": "active"}
    source.write_text(json.dumps([original]), encoding="utf-8")
    directory = source.parent / "revision"
    directory.mkdir()
    checkpoint = directory / "silver_labels.json"
    payload = generator.load_checkpoint(checkpoint, source, exporter.digest(source), "test-model", 3, 1)
    output = silver_output("Easy")
    if content_blocker:
        output = output.model_copy(update={"contentStatus": "concern", "contentConcerns": ["Ambiguitas konteks sumber."]})
    prompt_hash = hashlib.sha256(build_silver_prompt(original).encode("utf-8")).hexdigest()
    runs = [SilverRunResult(runIndex=index, status="success", output=output, latencyMs=1,
                            promptHash=prompt_hash, responseHash=hashlib.sha256(output.model_dump_json().encode()).hexdigest())
            for index in range(1, run_count + 1)]
    record = {"questionId": "q1", "inputHash": generator.input_hash(original),
              "runs": [run.model_dump(mode="json") for run in runs],
              "adjudication": None, "aggregate": aggregate_silver_runs(runs)}
    if run_count:
        payload["items"] = {"q1": record}
    if content_blocker:
        evidence = [{"runIndex": run.runIndex, "contentStatus": output.contentStatus,
                     "answerKeyStatus": output.answerKeyStatus, "verifiedAnswerKey": output.verifiedAnswerKey,
                     "verifiedMinimalSolution": output.verifiedMinimalSolution,
                     **{head: getattr(output, head).model_dump(mode="json") for head in exporter.HEADS}}
                    for run in runs]
        prompt = (build_silver_prompt(original)
                  + "\n\nADJUDIKASI SILVER: nilai ulang soal secara independen, lalu gunakan bukti run blind "
                  "berikut hanya untuk menemukan sumber perbedaan. Jangan melakukan voting mekanis. "
                  "Tidak ada prediksi IndoBERT atau estimasi kesulitan agen di dalam data ini.\n"
                  + json.dumps(evidence, ensure_ascii=False, sort_keys=True))
        adjudication = SilverAdjudicationResult(status="success", output=output, latencyMs=1,
            promptHash=hashlib.sha256(prompt.encode()).hexdigest(),
            responseHash=hashlib.sha256(output.model_dump_json().encode()).hexdigest())
        record["adjudication"] = adjudication.model_dump(mode="json")
        record["aggregate"] = aggregate_silver_runs(runs, adjudication)
    checkpoint.write_text(json.dumps(payload), encoding="utf-8")
    return source, checkpoint, directory, original


@pytest.mark.parametrize("run_count", [0, 1, 2])
def test_no_ai_or_incomplete_runs_have_no_old_label_and_are_inactive(tmp_path, monkeypatch, run_count):
    source, checkpoint, directory, original = make_export_fixture(tmp_path, monkeypatch, run_count)
    source_bytes, checkpoint_bytes = source.read_bytes(), checkpoint.read_bytes()
    report = exporter.export_class(source, checkpoint, directory, grade=1, track="regular")
    row = exporter.read(directory / "validation_results.json")[0]
    assert row["cognitive_level"] is row["cognitive_score"] is None
    assert row["confidence_score"] == 0 and row["status"] == "inactive"
    assert list(row) == list(original)
    assert {key: value for key, value in row.items() if key not in
            ("cognitive_level", "cognitive_score", "confidence_score", "status")} == {
            key: value for key, value in original.items() if key not in
            ("cognitive_level", "cognitive_score", "confidence_score", "status")}
    assert report["status"] == "draft" and not report["fullComplete"]
    assert report["items"][0]["missingRunIndices"] == list(range(run_count + 1, 4))
    assert report["summary"]["missingInitialRuns"] == 3 - run_count
    assert report["newApiCalls"] == 0
    assert source.read_bytes() == source_bytes and checkpoint.read_bytes() == checkpoint_bytes
    assert not (source.parent / "hasil_validasi").exists()


def test_three_successful_runs_export_final_qualified_label(tmp_path, monkeypatch):
    source, checkpoint, directory, _ = make_export_fixture(tmp_path, monkeypatch, 3)
    report = exporter.export_class(source, checkpoint, directory, grade=1, track="regular")
    row = exporter.read(directory / "validation_results.json")[0]
    assert (row["cognitive_level"], row["cognitive_score"], row["confidence_score"], row["status"]) == (
        "easy", 600, 100, "active")
    assert report["status"] == "final" and report["fullComplete"]
    assert report["items"][0]["missingRunIndices"] == []
    assert report["items"][0]["eligibleForTraining"]


def test_content_blocker_keeps_source_and_final_label_but_is_inactive(tmp_path, monkeypatch):
    source, checkpoint, directory, original = make_export_fixture(tmp_path, monkeypatch, 3, content_blocker=True)
    report = exporter.export_class(source, checkpoint, directory, grade=1, track="regular")
    row = exporter.read(directory / "validation_results.json")[0]
    assert row["soal_text"] == original["soal_text"] and row["options"] == original["options"]
    assert row["cognitive_level"] == "easy" and row["confidence_score"] == 100
    assert row["status"] == "inactive"
    assert report["fullComplete"] and report["items"][0]["contentStatus"] == "concern"
    assert report["items"][0]["finalRouting"] == "revision_required"
    assert not report["items"][0]["eligibleForTraining"]


def test_stale_complete_aggregate_cannot_activate_two_run_draft(tmp_path, monkeypatch):
    source, checkpoint, directory, _ = make_export_fixture(tmp_path, monkeypatch, 2)
    payload = exporter.read(checkpoint)
    payload["items"]["q1"]["aggregate"].update(eligibleForTraining=True, needsAdjudication=False)
    payload["items"]["q1"]["aggregate"]["heads"]["intendedDifficulty"]["label"] = "Hard"
    checkpoint.write_text(json.dumps(payload), encoding="utf-8")
    exporter.export_class(source, checkpoint, directory, grade=1, track="regular")
    row = exporter.read(directory / "validation_results.json")[0]
    assert row["cognitive_level"] is None and row["status"] == "inactive"


def test_input_tampering_is_rejected_before_export(tmp_path, monkeypatch):
    source, checkpoint, directory, _ = make_export_fixture(tmp_path, monkeypatch, 3)
    payload = exporter.read(checkpoint)
    payload["items"]["q1"]["inputHash"] = "a" * 64
    checkpoint.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(AssertionError):
        exporter.export_class(source, checkpoint, directory, grade=1, track="regular")
    assert not (directory / "validation_results.json").exists()


def test_final_array_reuses_verified_active_bytes_without_modifying_active(tmp_path, monkeypatch):
    source, checkpoint, directory, _ = make_export_fixture(tmp_path, monkeypatch, 3)
    exporter.export_class(source, checkpoint, directory, grade=1, track="regular")
    rows = exporter.read(directory / "validation_results.json")
    active = source.parent / "hasil_validasi"
    active.mkdir()
    # Distinct formatting proves the comparison reuses exactly the verified bytes.
    encoded = json.dumps(rows, separators=(",", ":")).encode("utf-8")
    (active / "validation_results.json").write_bytes(encoded)
    (active / "manifest.json").write_text(json.dumps({"sourceFiles": {"blindCheckpoint": {"path": str(checkpoint)}}}), encoding="utf-8")
    verified = []
    monkeypatch.setattr(exporter, "verify_bundle", lambda *args: verified.append(args))
    manifest_before = (active / "manifest.json").read_bytes()
    report = exporter.export_class(source, checkpoint, directory, grade=1, track="regular")
    assert verified == [(source, active)]
    assert (directory / "validation_results.json").read_bytes() == encoded
    assert (active / "validation_results.json").read_bytes() == encoded
    assert (active / "manifest.json").read_bytes() == manifest_before
    assert report["byteIdenticalToVerifiedActiveArray"]
