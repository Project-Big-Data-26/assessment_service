from copy import deepcopy
import json

import pytest

from app.services.exercise.local_review import review_question, assess_level
from app.services.exercise.workflow import atomic_json, require_validation
from scripts import review_replenishment_local as local


def question():
    return {"_id": "b"*24, "kelas_id": "kelas6", "subbab_id": "Bilangan Desimal",
            "soal_text": "Massa sebuah paket 3,4 kg. Setelah ditambah kemasan, massanya bertambah 0,5 kg. Berapa massa paket beserta kemasan?",
            "options": [{"option_id": k, "text": v, "alasan": "catatan"}
                        for k, v in zip("ABCD", ["3,9", "2,9", "8,4", "3,45"])],
            "jawaban": "A", "image_url": [], "cognitive_level": None,
            "cognitive_score": None, "confidence_score": None, "status": "inactive"}


def metadata():
    return {"id": "kelas6-b01-c-hard-bt01-900", "bab_id": "SD6-B1", "subbab_kode": "C",
            "jenis_soal": "operasi_desimal", "level_target": "hard", "pembahasan": "3,4 + 0,5 = 3,9.",
            "local_math_check": {"check": "exact_value_and_four_distinct_options", "value": "39/10",
                                 "options": ["39/10", "29/10", "42/5", "69/20"]}}


def test_assessment_does_not_force_target_or_invent_ai_confidence():
    original = question()
    result = review_question(original, metadata(), {"operasi_desimal"})
    assert result["assessedLevel"] == "easy" and result["originalTarget"] == "hard"
    assert result["publishedQuestion"]["confidence_score"] == 0
    assert result["apiCalls"] == 0 and result["trainingEvidenceQualified"] is False
    assert "stem_calculation_recomputed" in result["checks"]
    assert original == question()


def test_arithmetic_proof_cannot_override_the_actual_stem():
    changed = question()
    changed["soal_text"] = changed["soal_text"].replace("3,4", "4,4")
    with pytest.raises(AssertionError, match="Independent stem"):
        review_question(changed, metadata(), {"operasi_desimal"})


def test_local_mode_blocks_paid_validation(tmp_path):
    atomic_json(tmp_path/"reference_replenishment_state.json", {"reviewMode": "local_without_external_api"})
    with pytest.raises(ValueError, match="external API validation is disabled"):
        require_validation(tmp_path)


def prepare(tmp_path, monkeypatch):
    monkeypatch.setattr(local, "ROOT", tmp_path)
    monkeypatch.setattr(local, "LOCAL", tmp_path/"local")
    local.LOCAL.mkdir()
    base = tmp_path/"output/exercise/kelas6/batch01"
    old = {**question(), "_id": "a"*24, "confidence_score": 97,
           "cognitive_level": "medium", "cognitive_score": 1000, "status": "active"}
    new = question()
    meta = {old["_id"]: {"id": "paid", "validasi": {"validation_method": "blind_n3"}}, new["_id"]: metadata()}
    atomic_json(base/"soal_exercise_db.json", {"book": "kelas6", "items": [old, new]})
    atomic_json(base/"soal_exercise_meta.json", meta)
    final = base/"hasil_validasi"
    atomic_json(final/"validation_results.json", [old])
    atomic_json(final/"validation_results_meta.json", {old["_id"]: meta[old["_id"]]})
    atomic_json(final/"manifest.json", {"outputs": {n: {"sha256": local.digest(final/n), "bytes": (final/n).stat().st_size}
                for n in ("validation_results.json", "validation_results_meta.json")}})
    decision = review_question(new, metadata(), {"operasi_desimal"})
    return base, old, new, meta, decision


def test_local_publication_preserves_paid_rows_and_keeps_auditable_local_provenance(tmp_path, monkeypatch):
    base, old, new, meta, decision = prepare(tmp_path, monkeypatch)
    source = (base/"soal_exercise_db.json").read_bytes()
    result = local.publish_class("kelas6", [old, new], meta, [decision], {})
    assert result["reviewed"] == result["active"] == 1
    final = base/"hasil_validasi"
    local.verify_local_publication(final)
    rows = local.load(final/"validation_results.json")
    assert rows[0] == old and rows[1]["confidence_score"] == 0
    assert (base/"soal_exercise_db.json").read_bytes() == source
    info = local.load(final/"validation_results_meta.json")[new["_id"]]["validasi"]
    assert info["label_provenance"] == "codex_local_assessment" and info["api_runs"] == 0
    assert info["confidence_available"] is False and info["training_evidence_qualified"] is False
    assert local.publish_class("kelas6", [old, new], meta, [decision], {})["alreadyPublished"]
    # Updating hashes cannot authorize changes to a retained old decision.
    rows[0]["cognitive_level"] = "hard"
    atomic_json(final/"validation_results.json", rows)
    manifest = local.load(final/"manifest.json")
    manifest["outputs"]["validation_results.json"] = {"sha256": local.digest(final/"validation_results.json"),
                                                     "bytes": (final/"validation_results.json").stat().st_size}
    atomic_json(final/"manifest.json", manifest)
    with pytest.raises(AssertionError, match="previously published"):
        local.verify_local_publication(final)


def test_failed_final_verification_restores_previous_publication(tmp_path, monkeypatch):
    base, old, new, meta, decision = prepare(tmp_path, monkeypatch)
    final = base/"hasil_validasi"
    before = {p.name: p.read_bytes() for p in final.iterdir()}
    verify = local.verify_local_publication
    def fail_after_move(path):
        if path == final:
            raise RuntimeError("simulated publication check failure")
        verify(path)
    monkeypatch.setattr(local, "verify_local_publication", fail_after_move)
    with pytest.raises(RuntimeError, match="simulated"):
        local.publish_class("kelas6", [old, new], meta, [decision], {})
    assert {p.name: p.read_bytes() for p in final.iterdir()} == before


def test_loan_repayment_cannot_exceed_outstanding_principal():
    row = question()
    row.update(kelas_id="kelas12", soal_text="Pinjaman Rp3.600.000,00 berbunga 2% pada periode pertama. Anuitas akhir periode sebesar Rp12.000.000,00 terdiri atas bunga dan angsuran pokok. Berapa angsuran pokok periode pertama?")
    values = [11928000, 11928001, 11927999, 11928002]
    row["options"] = [{"option_id": k, "text": f"${v}$", "alasan": "catatan"} for k, v in zip("ABCD", values)]
    meta = metadata()
    meta.update(jenis_soal="pinjaman_anuitas", local_math_check={"check": "exact_value_and_four_distinct_options",
                "value": str(values[0]), "options": list(map(str, values))})
    result = review_question(row, meta, {"pinjaman_anuitas"})
    assert result["repairs"] and "Rp1.872.000,00" in result["publishedQuestion"]["soal_text"]
    assert result["publishedQuestion"]["options"][0]["text"] == "$1800000$"
    assert row["options"][0]["text"] == "$11928000$"
