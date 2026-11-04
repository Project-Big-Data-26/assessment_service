from copy import deepcopy
import json

import pytest

from app.services.exercise.reference_pilot import check_math, export_factor_pilot, factor_candidates
from app.services.exercise.workflow import require_validation, verify_generation


def fixture_sources(root):
    base = root / "exercise/kelas5/batch01"
    rows = []
    for index, candidate in enumerate(factor_candidates()):
        rows.append({"_id": candidate["reference_id"], "kelas_id": "kelas5", "subbab_id": "Faktor",
                     "soal_text": f"Acuan faktor ke {index}", "options": [{"option_id": "A", "text": "1"}],
                     "jawaban": "A", "status": "active", "cognitive_level": "hard", "image_url": []})
    final = base / "hasil_validasi/validation_results.json"
    final.parent.mkdir(parents=True)
    final.write_text(json.dumps(rows), encoding="utf-8")
    (base / "soal_exercise_meta.json").write_text(json.dumps({r["_id"]: {
        "bab_id": "SD5-B2", "subbab_kode": "C", "level_target": "hard"} for r in rows}), encoding="utf-8")
    return final


def test_three_proposed_answers_follow_constraints_and_wrong_key_fails():
    results = [check_math(candidate) for candidate in factor_candidates()]
    assert [r["answer"] for r in results] == ["11", "4", "46"]
    assert results[0]["facts"]["divisors"] == [1, 11, 121]
    assert results[1]["facts"]["valid_container_counts"] == [4, 6, 8, 12]
    assert results[2]["facts"]["sum"] == 72
    changed = deepcopy(factor_candidates()[0])
    changed["answer"] = "12"
    with pytest.raises(ValueError, match="key or distractors"):
        check_math(changed)
    ambiguous = deepcopy(factor_candidates()[0])
    ambiguous["verification"].update(lower=1, upper=10)
    with pytest.raises(ValueError, match="one number"):
        check_math(ambiguous)


def test_reference_pilot_has_frozen_sources_and_cannot_publish_or_overwrite(tmp_path, monkeypatch):
    root = tmp_path / "output"
    source = fixture_sources(root)
    original = source.read_bytes()
    result = export_factor_pilot(root)
    base = root / "exercise/kelas5/batch02"
    assert result["questionCount"] == 3 and result["newApiCalls"] == 0
    assert source.read_bytes() == original
    checksum = verify_generation(base)
    assert checksum == result["manifestSha256"]
    rows = json.loads((base / "soal_exercise_db.json").read_text(encoding="utf-8"))["items"]
    assert len({row["_id"] for row in rows}) == 3
    assert all(row["status"] == "inactive" and row["cognitive_level"] is None for row in rows)
    assert all(len(row["options"]) == 4 and row["jawaban"] in "ABCD" for row in rows)
    assert not (base / "extraction_ready.json").exists()
    with pytest.raises(ValueError, match="validation_pending"):
        require_validation(base)
    before = (base / "soal_exercise_db.json").read_bytes()
    with pytest.raises(ValueError, match="not empty"):
        export_factor_pilot(root)
    from app.services.exercise import config, export
    monkeypatch.setattr(config, "OUT_ROOT", str(root / "exercise"))
    with pytest.raises(ValueError, match="already exported"):
        export.export_batch("kelas5", 2)
    assert (base / "soal_exercise_db.json").read_bytes() == before
    # Standard validation staging accepts the master without requiring PDF input.
    from scripts import validate_exercise_batch as validator
    monkeypatch.setattr(validator, "ROOT", tmp_path)
    assert len(validator.validated_source("kelas5", "batch02")) == 3
    from scripts.plan_exercise_replenishment import pending_generation
    pending, files = pending_generation(root, [])
    assert len(pending) == 3 and files
    assert all(row["level_target"] == "hard" and row["class_key"] == "kelas5" for row in pending)
    # A changed snapshot/plan must invalidate the approval digest.
    plan_path = base / "generation_plan.json"
    plan_path.write_text(plan_path.read_text(encoding="utf-8") + "\n", encoding="utf-8")
    with pytest.raises(ValueError, match="changed"):
        verify_generation(base)


def test_inactive_or_missing_reference_is_rejected_before_generation(tmp_path):
    root = tmp_path / "output"
    source = fixture_sources(root)
    rows = json.loads(source.read_text(encoding="utf-8"))
    rows[0]["status"] = "inactive"
    source.write_text(json.dumps(rows), encoding="utf-8")
    with pytest.raises(ValueError, match="active, labelled"):
        export_factor_pilot(root)
    assert not (root / "exercise/kelas5/batch02").exists()
