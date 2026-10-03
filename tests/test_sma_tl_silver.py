import hashlib
import json

import pytest

from app.llm.silver import build_silver_prompt, rubric_file_hash, silver_rubric
from scripts import generate_silver_labels_kelas1 as generator
from scripts.audit_grade_aware_pilot import audit
from tests.test_blind_pilot_audit import question, record


@pytest.mark.parametrize("grade,topics", [(11, ("matriks", "polinomial", "vektor")), (12, ("turunan", "integral", "normal"))])
def test_tl_prompt_uses_advanced_subject_context_without_prediction_leakage(grade, topics):
    item = question("q-tl")
    item.update(cognitive_level="reasoning", tingkat_kesulitan="Hard", agentDifficulty=5)
    prompt = build_silver_prompt(item, grade=grade, track="tl")
    assert "Matematika Tingkat Lanjut" in prompt
    assert all(topic in prompt.lower() for topic in topics)
    assert "maksimal 700 karakter" in prompt
    assert all(key not in prompt for key in ("cognitive_level", "tingkat_kesulitan", "agentDifficulty"))
    assert rubric_file_hash(grade, track="tl") != rubric_file_hash(grade)


def test_tl_cannot_be_selected_for_an_unsupported_grade():
    with pytest.raises(ValueError, match="grade 11 or 12"):
        silver_rubric(10, track="tl")


@pytest.mark.parametrize("grade", [11, 12])
def test_tl_resume_and_audit_preserve_subject_scope(tmp_path, monkeypatch, grade):
    monkeypatch.setattr(generator, "ROOT", tmp_path)
    source = tmp_path / "questions.json"
    item = question("q-tl")
    source.write_text(json.dumps([item]), encoding="utf-8")
    path = tmp_path / "silver.json"
    source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    payload = generator.load_checkpoint(path, source, source_hash, "test-model", 3, grade, track="tl")
    payload["items"] = {"q-tl": record(item)}
    path.write_text(json.dumps(payload), encoding="utf-8")
    assert generator.load_checkpoint(path, source, source_hash, "test-model", 3, grade, track="tl") == payload
    with pytest.raises(ValueError, match="subject track"):
        generator.load_checkpoint(path, source, source_hash, "test-model", 3, grade)
    result = audit(source, path, grade=grade)
    assert result["subjectTrack"] == "tl"
    assert result["gates"]["promptAndRubricVersionMatch"]
    payload["subjectTrack"] = "regular"
    path.write_text(json.dumps(payload), encoding="utf-8")
    assert not audit(source, path, grade=grade)["gates"]["promptAndRubricVersionMatch"]
