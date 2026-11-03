import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from app.services.exercise import config as C, workflow as flow
from app.services.exercise import generation, llm_generate, export
from app.services.exercise.schema import ExerciseFile
from app.services.exercise.allocation import modality_quotas
from app.services.exercise.visual_plan import verify_plan, preflight


def test_source_bound_plan_rejects_changed_sources(tmp_path):
    source = tmp_path / "curriculum.txt"
    source.write_text("real fixture source")
    plan = {"schemaVersion": "exercise-visual-plan-v1", "generationOnly": True, "total": 1,
            "sources": {str(source): flow.digest(source)},
            "slots": [{"bab_no": 1, "subbab": "A", "level": "easy", "visual": True, "count": 1}]}
    assert verify_plan(plan) == plan
    source.write_text("changed source")
    with pytest.raises(ValueError, match="source|changed"):
        verify_plan(plan)


def test_generator_renders_exports_defers_and_resumes_without_a_solver(tmp_path, monkeypatch):
    monkeypatch.setattr(C, "OUT_ROOT", str(tmp_path / "output/exercise"))
    base = Path(C.OUT_ROOT) / "kelas1/batch02"
    flow.begin_generation(base, "kelas1", 2)
    source = tmp_path / "source.txt"
    source.write_text("Fixture curriculum evidence, not production curriculum.")
    quotas = modality_quotas(10)
    plan = {"schemaVersion": "exercise-visual-plan-v1", "class": "kelas1", "batch": "batch02",
        "generationOnly": True, "total": 10, "sources": {str(source): flow.digest(source)},
        "slots": [{"bab_no": 1, "bab_id": "SD1-B1", "subbab": "A", "level": level,
                   "visual": modality == "visual", "count": count}
                  for level, counts in quotas.items() for modality, count in counts.items() if count]}
    flow.atomic_json(base / "generation_plan.json", plan)
    chapter = SimpleNamespace(bab_id="SD1-B1", subbab=[("A", "Counting")], subbab_nama=lambda code: "Counting")
    monkeypatch.setattr(export.kurikulum, "get", lambda book, n: chapter if n == 1 else None)
    monkeypatch.setattr(export, "get_book", lambda book: SimpleNamespace(jenjang="SD"))
    def schema_check(path, **kwargs):
        return ExerciseFile.model_validate(flow.load(path)), [], []
    monkeypatch.setattr(export, "validate_file", schema_check)
    monkeypatch.setattr(llm_generate, "validate_file", schema_check)
    class Context:
        def __init__(self, job):
            self.job = job
            self.kuota = job.planned_count
            self.target_variasi = 0
        def prompt(self, need, *args):
            return json.dumps({"need": need, "visual": self.job.generated_visuals})
    monkeypatch.setattr(llm_generate, "_Context", Context)
    calls = []
    class Client:
        def __init__(self, settings, *args):
            self.settings = settings
            self.attempts = len(calls)
        def __enter__(self):
            return self
        def __exit__(self, *args):
            pass
        def chat(self, messages, **kwargs):
            calls.append("generation_only")
            self.attempts += 1
            request = json.loads(messages[-1]["content"])
            rows = []
            for i in range(request["need"]):
                row = {"tipe_generate": "orisinal", "acuan": {"sumber": "siswa", "halaman": 1,
                    "kutipan": "Fixture material used only in this test"}, "cognitive_c": "C1",
                    "jenis_soal": "count groups", "jumlah_langkah": 1, "alasan_level": "Fixture target only",
                    "pertanyaan": f"Perhatikan kelompok pada gambar {len(calls)} urutan {i}." if request["visual"] else f"Hitung contoh {len(calls)} urutan {i}.",
                    "jawaban_benar": "3", "alasan_benar": "Fixture answer",
                    "distraktor": [{"teks": str(n), "alasan": "Fixture error"} for n in (2, 4, 5)],
                    "pembahasan": "Fixture solution, not a verified answer."}
                if request["visual"]:
                    row["visual_spec"] = {"kind": "object_groups", "groups": [
                        {"label": "A", "shape": "circle", "count": len(calls) + i}]}
                rows.append(row)
            return SimpleNamespace(text=json.dumps({"soal": rows}), input_tokens=1, output_tokens=1,
                                   latency_seconds=0, finish_reason="stop", model="fixture")
    monkeypatch.setattr(generation, "BudgetedGenerator", Client)
    from app.services.exercise import llm_verify, handoff
    monkeypatch.setattr(llm_verify, "verifikasi_buta", lambda *a, **k: pytest.fail("no solver during generation"))
    monkeypatch.setattr(handoff, "run_validation", lambda: pytest.fail("no validation auto-hook"))
    result = generation.generate_plan(base, SimpleNamespace(model="fixture"))
    assert result["generation"]["complete"]
    assert result["total"] == 10 and result["validationApiCalls"] == 0
    assert result["generation"]["visualQuestions"] == 7
    assert result["generation"]["targetDifficultyDistribution"] == {"easy": 3, "medium": 4, "hard": 3}
    assert not (base / "extraction_ready.json").exists()
    assert not (base / "hasil_validasi").exists()
    assert flow.load(base / "generation_state.json")["phase"] == "generation_complete"
    assert not flow.validation_allowed(base)
    rows = flow.load(base / "soal_exercise_db.json")["items"]
    assert all(row["cognitive_level"] is None for row in rows)
    for row in rows:
        for ref in row["image_url"]:
            assert flow.safe_asset(base, ref).is_file()
    first_calls = len(calls)
    digest = result["generation"]["manifestSha256"]
    again = generation.generate_plan(base, SimpleNamespace(model="fixture"))
    assert len(calls) == first_calls
    assert again["generation"]["manifestSha256"] == digest


def test_preflight_never_invents_missing_curriculum(tmp_path, monkeypatch):
    from app.services.exercise import visual_plan
    monkeypatch.setattr(visual_plan.kurikulum, "EXCEL_PATH", str(tmp_path / "missing.xlsx"))
    monkeypatch.setattr(visual_plan, "MD_ROOT", str(tmp_path / "pages"))
    def no_book(book):
        raise SystemExit("book missing")
    monkeypatch.setattr(visual_plan, "get_book", no_book)
    report = preflight("kelas1")
    assert report["status"] == "waiting_for_sources" and report["newApiCalls"] == 0
    assert len(report["missingInputs"]) == 4
