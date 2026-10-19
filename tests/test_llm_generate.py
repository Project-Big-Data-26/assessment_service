import json

import pytest

from app.services.exercise import llm_generate as G
from app.services.exercise.schema import ExerciseFile


class _Settings:
    model = "m1"


class _Client:
    settings = _Settings()

    def chat(self, *a, **k):   # tidak boleh dipanggil
        raise AssertionError("tidak boleh memanggil LLM")


def _file(generator):
    return {"book": "kelas9", "bab_no": 2, "subbab": "A", "level": "easy", "batch": 1,
            "skill_versi": "v1", "generator": generator, "soal": []}


def test_subbab_pages_kelas9():
    assert G.subbab_pages("kelas9", 2, "A") == (63, 69)


def test_subbab_pages_unknown_subbab():
    with pytest.raises(G.GenerateError):
        G.subbab_pages("kelas9", 2, "Z")


def test_extract_json_handles_fence():
    assert G._extract_json('teks ```json\n{"soal": []}\n``` selesai') == {"soal": []}


@pytest.mark.parametrize("generator", [None, "9router:model-lain"])
def test_existing_file_from_other_source_is_never_overwritten(tmp_path, generator):
    job = G.Job("kelas9", 2, "A", "easy", 1, str(tmp_path))
    job_path = tmp_path / "kelas9" / "batch01" / "bab02" / "A_easy.json"
    job_path.parent.mkdir(parents=True)
    job_path.write_text(json.dumps(_file(generator)), encoding="utf-8")
    before = job_path.read_text(encoding="utf-8")
    with pytest.raises(G.GenerateError, match="tidak ditimpa"):
        G.generate(job, _Client())
    assert job_path.read_text(encoding="utf-8") == before


def test_schema_accepts_generator_field():
    assert ExerciseFile.model_validate(_file("9router:m1")).generator == "9router:m1"
