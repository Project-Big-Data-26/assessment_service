"""Regression coverage for the versioned, grade-relative difficulty revision."""

from dataclasses import replace
import hashlib
import json

import pytest
import yaml

from app.llm import silver
from scripts import generate_silver_labels_kelas1 as generator
from tests.test_blind_pilot_audit import question


SCOPES = [(grade, "regular") for grade in range(1, 13)] + [(11, "tl"), (12, "tl")]


@pytest.mark.parametrize("grade,track", SCOPES)
def test_every_scope_uses_the_revised_yaml_and_its_own_examples(grade, track):
    rubric = silver.silver_rubric(grade, track=track)
    configuration = yaml.safe_load(rubric.path.read_text(encoding="utf-8"))
    assert configuration["rubric_version"] == rubric.version
    assert configuration["subject_track"] == track
    assert grade in configuration["supported_grades"]
    assert "-v8-" in rubric.version and "-v10-" in rubric.prompt_version
    assert silver.rubric_file_hash(grade, track=track) == hashlib.sha256(rubric.path.read_bytes()).hexdigest()
    prompt = silver.build_silver_prompt(question("q"), grade=grade, track=track)
    for label in ("Easy", "Medium", "Hard"):
        assert f"{label} = {configuration['intendedDifficulty'][label]}" in prompt
    examples = configuration.get("difficulty_examples_by_grade", {}).get(grade)
    if examples is None:
        examples = configuration["difficulty_examples"]
    assert all(example in prompt for example in examples.values())
    if grade <= 6:
        other_examples = configuration["difficulty_examples_by_grade"]
        assert all(other_examples[other]["Hard"] not in prompt for other in other_examples if other != grade)
    assert all(rule in prompt for rule in configuration["difficulty_boundary_rules"])
    assert "kebaruan strategi bukan syarat wajib" in prompt
    assert "Kategori kosong tetap sah" in prompt
    assert "empirical difficulty CTT/IRT" in prompt
    assert "answerKeyStatus=verified" in prompt and "gunakan abstain" in prompt


def test_prompt_reads_modified_definition_from_yaml_without_a_code_edit(tmp_path, monkeypatch):
    original = silver.silver_rubric(1)
    configuration = yaml.safe_load(original.path.read_text(encoding="utf-8"))
    configuration["intendedDifficulty"]["Hard"] = "Definisi tunggal dari YAML untuk uji batas."
    path = tmp_path / "rubric.yaml"
    path.write_text(yaml.safe_dump(configuration, allow_unicode=True), encoding="utf-8")
    monkeypatch.setattr(silver, "silver_rubric", lambda grade, *, track: replace(original, path=path))
    prompt = silver.build_silver_prompt(question("q"))
    assert "Hard = Definisi tunggal dari YAML untuk uji batas." in prompt
    assert "Hard = strategi nonrutin" not in prompt


def test_prompt_rejects_a_yaml_identity_that_disagrees_with_dispatch(tmp_path, monkeypatch):
    original = silver.silver_rubric(1)
    configuration = yaml.safe_load(original.path.read_text(encoding="utf-8"))
    configuration["rubric_version"] = "another-version"
    path = tmp_path / "rubric.yaml"
    path.write_text(yaml.safe_dump(configuration), encoding="utf-8")
    monkeypatch.setattr(silver, "silver_rubric", lambda grade, *, track: replace(original, path=path))
    with pytest.raises(ValueError, match="rubric file version"):
        silver.build_silver_prompt(question("q"))


def test_legacy_paid_checkpoint_cannot_be_mixed_into_the_new_rubric(tmp_path, monkeypatch):
    monkeypatch.setattr(generator, "ROOT", tmp_path)
    source = tmp_path / "questions.json"
    source.write_text(json.dumps([question("q")]), encoding="utf-8")
    source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    checkpoint = tmp_path / "silver.json"
    payload = generator.load_checkpoint(checkpoint, source, source_hash, "test-model", 3, 1)
    payload["promptVersion"] = "gemini-silver-math-3x4x3-v4-blind-key-verified"
    payload["rubricVersion"] = "math-rubric-3x4x3-v2-grade-aware"
    checkpoint.write_text(json.dumps(payload), encoding="utf-8")
    original_bytes = checkpoint.read_bytes()
    with pytest.raises(ValueError, match="grade/prompt version"):
        generator.load_checkpoint(checkpoint, source, source_hash, "test-model", 3, 1)
    assert checkpoint.read_bytes() == original_bytes
