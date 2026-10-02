import hashlib
import json

import pytest

from app.llm.silver import (
    RUBRIC_PATH, RUBRIC_VERSION, SILVER_PROMPT_VERSION,
    build_silver_prompt, rubric_file_hash, silver_rubric,
)
from scripts import generate_silver_labels_kelas1 as generator
from scripts.audit_grade_aware_pilot import audit
from tests.test_blind_pilot_audit import question, record


def test_smp7_context_is_blind_and_sd_rubric_identity_is_preserved():
    sd, smp = silver_rubric(4), silver_rubric(7)
    assert sd.version == RUBRIC_VERSION and sd.prompt_version == SILVER_PROMPT_VERSION
    assert rubric_file_hash(4) == hashlib.sha256(RUBRIC_PATH.read_bytes()).hexdigest()
    assert smp.education_level == "SMP" and smp.path != sd.path
    assert rubric_file_hash(7) != rubric_file_hash(4)
    item = question("q-7")
    item.update(cognitive_level="reasoning", tingkat_kesulitan="Hard", agentDifficulty=5)
    prompt = build_silver_prompt(item, grade=7)
    assert "SMP kelas 7" in prompt and "bilangan bulat dan rasional" in prompt
    assert "tidak otomatis Hard" in prompt
    assert "cognitive_level" not in prompt and "tingkat_kesulitan" not in prompt
    assert "agentDifficulty" not in prompt and "PREDIKSI INDOBERT" not in prompt
    assert "Jenjang sasaran" not in build_silver_prompt(item, grade=4)


def test_grade7_checkpoint_resume_requires_the_smp_rubric(tmp_path, monkeypatch):
    monkeypatch.setattr(generator, "ROOT", tmp_path)
    source = tmp_path / "questions.json"
    source.write_text(json.dumps([question("q-7")]), encoding="utf-8")
    source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    checkpoint = tmp_path / "silver.json"
    payload = generator.load_checkpoint(checkpoint, source, source_hash, "test-model", 3, 7)
    assert payload["educationLevel"] == "SMP"
    assert payload["rubricVersion"] == silver_rubric(7).version
    assert payload["rubricHash"] == rubric_file_hash(7)
    checkpoint.write_text(json.dumps(payload), encoding="utf-8")
    assert generator.load_checkpoint(checkpoint, source, source_hash, "test-model", 3, 7) == payload
    payload["rubricHash"] = rubric_file_hash(1)
    checkpoint.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(ValueError, match="rubric hash"):
        generator.load_checkpoint(checkpoint, source, source_hash, "test-model", 3, 7)


def test_grade7_audit_rejects_an_sd_rubric_even_with_matching_inputs(tmp_path):
    item = question("q-7")
    source = tmp_path / "questions.json"
    source.write_text(json.dumps([item]), encoding="utf-8")
    checkpoint = tmp_path / "silver.json"
    spec = silver_rubric(7)
    payload = {
        "sourceGrade": 7, "sourceHash": hashlib.sha256(source.read_bytes()).hexdigest(),
        "promptVersion": spec.prompt_version, "rubricVersion": spec.version,
        "rubricHash": rubric_file_hash(7), "items": {"q-7": record(item)},
    }
    checkpoint.write_text(json.dumps(payload), encoding="utf-8")
    assert audit(source, checkpoint, grade=7)["gates"]["promptAndRubricVersionMatch"]
    payload.update(promptVersion=SILVER_PROMPT_VERSION, rubricVersion=RUBRIC_VERSION, rubricHash=rubric_file_hash(1))
    checkpoint.write_text(json.dumps(payload), encoding="utf-8")
    report = audit(source, checkpoint, grade=7)
    assert not report["gates"]["promptAndRubricVersionMatch"]
    assert not report["readyForExpansion"]
