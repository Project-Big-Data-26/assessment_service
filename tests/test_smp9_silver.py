import hashlib
import json

import pytest

from app.llm.silver import build_silver_prompt, rubric_file_hash, silver_rubric
from scripts import generate_silver_labels_kelas1 as generator
from scripts.audit_grade_aware_pilot import audit
from tests.test_blind_pilot_audit import question, record


def test_grade9_context_is_blind_and_distinct_from_previous_grades():
    item = question("q-9")
    item.update(cognitive_level="reasoning", tingkat_kesulitan="Hard", agentDifficulty=5)
    prompt = build_silver_prompt(item, grade=9)
    assert "SMP kelas 9" in prompt and "SPLDV" in prompt
    assert "faktor skala luas k^2 dan volume k^3" in prompt
    assert "frekuensi harapan" in prompt and "maksimal 700 karakter" in prompt
    assert all(key not in prompt for key in ("cognitive_level", "tingkat_kesulitan", "agentDifficulty", "PREDIKSI INDOBERT"))
    assert "kelas 8" not in prompt
    assert silver_rubric(9).path != silver_rubric(8).path
    assert rubric_file_hash(9) != rubric_file_hash(8)


def test_grade9_resume_rejects_grade8_rubric(tmp_path, monkeypatch):
    monkeypatch.setattr(generator, "ROOT", tmp_path)
    source = tmp_path / "questions.json"
    source.write_text(json.dumps([question("q-9")]), encoding="utf-8")
    source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    checkpoint = tmp_path / "silver.json"
    payload = generator.load_checkpoint(checkpoint, source, source_hash, "test-model", 3, 9)
    assert payload["educationLevel"] == "SMP" and payload["sourceGrade"] == 9
    checkpoint.write_text(json.dumps(payload), encoding="utf-8")
    assert generator.load_checkpoint(checkpoint, source, source_hash, "test-model", 3, 9) == payload
    payload["rubricHash"] = rubric_file_hash(8)
    checkpoint.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(ValueError, match="rubric hash"):
        generator.load_checkpoint(checkpoint, source, source_hash, "test-model", 3, 9)


def test_grade9_audit_rejects_a_grade8_rubric(tmp_path):
    item = question("q-9")
    source = tmp_path / "questions.json"
    source.write_text(json.dumps([item]), encoding="utf-8")
    checkpoint = tmp_path / "silver.json"
    spec = silver_rubric(9)
    payload = {
        "sourceGrade": 9, "sourceHash": hashlib.sha256(source.read_bytes()).hexdigest(),
        "promptVersion": spec.prompt_version, "rubricVersion": spec.version,
        "rubricHash": rubric_file_hash(9), "items": {"q-9": record(item)},
    }
    checkpoint.write_text(json.dumps(payload), encoding="utf-8")
    assert audit(source, checkpoint, grade=9)["gates"]["promptAndRubricVersionMatch"]
    previous = silver_rubric(8)
    payload.update(promptVersion=previous.prompt_version, rubricVersion=previous.version, rubricHash=rubric_file_hash(8))
    checkpoint.write_text(json.dumps(payload), encoding="utf-8")
    report = audit(source, checkpoint, grade=9)
    assert not report["gates"]["promptAndRubricVersionMatch"]
    assert not report["readyForExpansion"]
