"""New upstream chapters can reuse paid results only for identical retained inputs."""
from copy import deepcopy
import json

import pytest

from app.llm.silver import aggregate_silver_runs
from scripts import generate_silver_labels_kelas1 as generator
from scripts import validate_exercise_batch as exercise
from scripts.refresh_ai_validation_reports import digest, verify_evidence
from tests.test_blind_pilot_audit import question
from tests.test_single_run_exercise import run


def prepare(tmp_path, monkeypatch):
    monkeypatch.setattr(exercise, "ROOT", tmp_path)
    monkeypatch.setattr(generator, "ROOT", tmp_path)
    p = exercise.paths("kelas5", "batch01")
    p["exercise"].mkdir(parents=True)
    rows = [{**question(qid), "kelas_id": "kelas5", "cognitive_level": None} for qid in ("q1", "q2")]
    write_source(p, rows)
    exercise.stage_class("kelas5", "batch01")
    checkpoint = generator.load_checkpoint(p["checkpoint"], p["source"], digest(p["source"]), "test", 1, 5)
    evidence = run(original=rows[0], grade=5)
    checkpoint["items"]["q1"] = {"questionId": "q1", "inputHash": generator.input_hash(rows[0]),
        "runs": [evidence.model_dump(mode="json")], "adjudication": None,
        "aggregate": aggregate_silver_runs([evidence], requested_runs=1)}
    checkpoint["apiAttempts"] = 7
    generator.atomic_write(checkpoint, p["checkpoint"])
    return p, rows, checkpoint


def write_source(p, rows):
    generator.atomic_write({"book": "kelas5", "batch": 1, "items": rows}, p["exercise"] / "soal_exercise_db.json")
    generator.atomic_write({str(row["_id"]): {"batch": 1, "level_target": "easy", "bab_id": "SD5-B1"}
                            for row in rows}, p["exercise"] / "soal_exercise_meta.json")


def test_added_questions_reuse_exact_paid_records_and_archive_old_source(tmp_path, monkeypatch):
    p, rows, checkpoint = prepare(tmp_path, monkeypatch)
    previous_bytes = p["source"].read_bytes()
    old_checkpoint = p["checkpoint"].read_bytes()
    added = {**rows[0], "_id": "q3"}
    write_source(p, [rows[0], added, rows[1]])
    with pytest.raises(ValueError, match="source changed"):
        exercise.stage_class("kelas5", "batch01")
    result = exercise.extend_class("kelas5", "batch01")
    assert result["extended"] and result["addedQuestionCount"] == 1
    new = json.loads(p["checkpoint"].read_text(encoding="utf-8"))
    assert new["items"] == checkpoint["items"] and new["apiAttempts"] == 7
    archive = p["stage"] / "history" / ("source_extension_" + result["previousSourceHash"][:12] + "_" + result["sourceHash"][:12])
    assert (archive / "soal_exercise_db.json").read_bytes() == previous_bytes
    assert (archive / "silver_labels.json").read_bytes() == old_checkpoint
    verify_evidence(p["source"], p["checkpoint"], 5)
    assert exercise.extend_class("kelas5", "batch01")["extended"] is False


@pytest.mark.parametrize("change", ["edit", "remove", "reorder"])
def test_edits_deletions_and_reordering_are_rejected_without_writes(tmp_path, monkeypatch, change):
    p, rows, _ = prepare(tmp_path, monkeypatch)
    previous = (p["source"].read_bytes(), p["checkpoint"].read_bytes())
    revised = deepcopy(rows) + [{**rows[0], "_id": "q3"}]
    if change == "edit":
        revised[0]["soal_text"] += " changed"
    elif change == "remove":
        revised = revised[1:]
    else:
        revised[0], revised[1] = revised[1], revised[0]
    write_source(p, revised)
    with pytest.raises(ValueError, match="unchanged old"):
        exercise.extend_class("kelas5", "batch01")
    assert (p["source"].read_bytes(), p["checkpoint"].read_bytes()) == previous


def test_reference_additions_are_blind_without_changing_old_paid_inputs(tmp_path, monkeypatch):
    p, rows, checkpoint = prepare(tmp_path, monkeypatch)
    added = {**rows[0], "_id": "q3"}
    write_source(p, rows + [added])
    meta_path = p["exercise"] / "soal_exercise_meta.json"
    meta = json.loads(meta_path.read_text())
    meta["q3"]["generator"] = "codex:reference-parameterized-v1"
    generator.atomic_write(meta, meta_path)
    generator.atomic_write({}, p["exercise"] / "reference_replenishment_state.json")
    source = exercise.validated_source("kelas5", "batch01")
    assert source[:2] == rows
    assert source[2]["_exerciseBlindInput"] is True
    exercise.extend_class("kelas5", "batch01")
    after = json.loads(p["checkpoint"].read_text())
    assert after["items"] == checkpoint["items"]
    verify_evidence(p["source"], p["checkpoint"], 5)


def test_retained_provider_proof_survives_only_unchanged_source_extension(tmp_path, monkeypatch):
    from app.llm.provenance import verify_retained_record
    from scripts.generate_silver_labels_kelas1 import atomic_write
    from copy import deepcopy
    p, rows, checkpoint = prepare(tmp_path, monkeypatch)
    archive = p["stage"] / "history/provider_original/silver_labels.json"
    archive.parent.mkdir(parents=True)
    atomic_write(checkpoint, archive)
    retained = deepcopy(checkpoint["items"]["q1"])
    retained.update(provider=checkpoint["provider"], model=checkpoint["model"],
                    retainedProviderEvidence={"path": str(archive), "sha256": digest(archive)})
    checkpoint["items"]["q1"] = retained
    atomic_write(checkpoint, p["checkpoint"])
    write_source(p, rows + [{**rows[0], "_id": "q3"}])
    exercise.extend_class("kelas5", "batch01")
    verify_retained_record(p["source"], "q1", retained)
    altered = json.loads(p["source"].read_text())
    altered[0]["soal_text"] += " altered"
    atomic_write(altered, p["source"])
    with pytest.raises(ValueError, match="identity differs"):
        verify_retained_record(p["source"], "q1", retained)
