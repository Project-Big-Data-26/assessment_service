import hashlib
import json

import pytest

from app.llm.silver import build_silver_prompt, rubric_file_hash, silver_rubric
from scripts import generate_silver_labels_kelas1 as generator
from scripts.audit_grade_aware_pilot import audit
from tests.test_blind_pilot_audit import question, record


def test_grade8_context_is_blind_and_distinct_from_grade7():
    item = question("q-8")
    item.update(cognitive_level="reasoning", tingkat_kesulitan="Hard", agentDifficulty=5)
    prompt = build_silver_prompt(item, grade=8)
    assert "SMP kelas 8" in prompt and "Teorema Pythagoras" in prompt
    assert "konvensi kuartil" in prompt and "maksimal 700 karakter" in prompt
    assert "cognitive_level" not in prompt and "tingkat_kesulitan" not in prompt
    assert "agentDifficulty" not in prompt and "PREDIKSI INDOBERT" not in prompt
    assert "kelas 7" not in prompt
    assert silver_rubric(8).path != silver_rubric(7).path
    assert rubric_file_hash(8) != rubric_file_hash(7)


def test_grade8_resume_rejects_grade7_rubric(tmp_path, monkeypatch):
    monkeypatch.setattr(generator, "ROOT", tmp_path)
    source = tmp_path / "questions.json"
    source.write_text(json.dumps([question("q-8")]), encoding="utf-8")
    source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    checkpoint = tmp_path / "silver.json"
    payload = generator.load_checkpoint(checkpoint, source, source_hash, "test-model", 3, 8)
    assert payload["educationLevel"] == "SMP" and payload["sourceGrade"] == 8
    checkpoint.write_text(json.dumps(payload), encoding="utf-8")
    assert generator.load_checkpoint(checkpoint, source, source_hash, "test-model", 3, 8) == payload
    payload["rubricHash"] = rubric_file_hash(7)
    checkpoint.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(ValueError, match="rubric hash"):
        generator.load_checkpoint(checkpoint, source, source_hash, "test-model", 3, 8)


def test_grade8_audit_rejects_a_grade7_rubric(tmp_path):
    item = question("q-8")
    source = tmp_path / "questions.json"
    source.write_text(json.dumps([item]), encoding="utf-8")
    checkpoint = tmp_path / "silver.json"
    spec = silver_rubric(8)
    payload = {
        "sourceGrade": 8, "sourceHash": hashlib.sha256(source.read_bytes()).hexdigest(),
        "promptVersion": spec.prompt_version, "rubricVersion": spec.version,
        "rubricHash": rubric_file_hash(8), "items": {"q-8": record(item)},
    }
    checkpoint.write_text(json.dumps(payload), encoding="utf-8")
    assert audit(source, checkpoint, grade=8)["gates"]["promptAndRubricVersionMatch"]
    sd = silver_rubric(7)
    payload.update(promptVersion=sd.prompt_version, rubricVersion=sd.version, rubricHash=rubric_file_hash(7))
    checkpoint.write_text(json.dumps(payload), encoding="utf-8")
    report = audit(source, checkpoint, grade=8)
    assert not report["gates"]["promptAndRubricVersionMatch"]
    assert not report["readyForExpansion"]
