import json

from app.services.exercise import llm_generate as G
from app.services.exercise import llm_pipeline as P
from app.services.exercise.schema import ExerciseFile


def _soal(i):
    return {"id": f"kelas9-b02-a-easy-bt01-{i:03d}", "tipe_generate": "orisinal", "variasi_cara": None,
            "acuan": {"sumber": "siswa", "halaman": 63, "kutipan": "Klasifikasi Bangun Ruang"},
            "cognitive_c": "C1", "jumlah_langkah": 1, "jenis_soal": f"jenis {i}", "alasan_level": "satu langkah",
            "stimulus": None, "pertanyaan": f"Berapa {i} + {i}?", "jawaban_benar": str(2 * i),
            "alasan_benar": "dijumlahkan",
            "distraktor": [{"teks": str(2 * i + k), "alasan": "salah hitung"} for k in (1, 2, 3)],
            "pembahasan": "jumlahkan", "catatan": None}


def test_buang_menghapus_dan_menomori_ulang(tmp_path):
    job = G.Job("kelas9", 2, "A", "easy", 1, str(tmp_path))
    G._write(job, "9router:m1", [ExerciseFile.model_validate(
        {"book": "kelas9", "bab_no": 2, "subbab": "A", "level": "easy", "batch": 1,
         "soal": [_soal(i) for i in (1, 2, 3, 4)]}).soal[i] for i in range(4)])
    solver = tmp_path / "solver.json"
    solver.write_text(json.dumps({"jawaban": {job.id_prefix + "002": {"catatan": "data tidak konsisten"}}}),
                      encoding="utf-8")
    umpan = P._buang(job, [job.id_prefix + "002", job.id_prefix + "004"], str(solver))
    sisa = P._muat(job.path)
    assert [s.id for s in sisa.soal] == [job.id_prefix + "001", job.id_prefix + "002"]
    assert [s.pertanyaan for s in sisa.soal] == ["Berapa 1 + 1?", "Berapa 3 + 3?"]
    assert len(umpan) == 2 and "data tidak konsisten" in umpan[0]
    assert sisa.generator == "9router:m1"


def test_write_mengulang_saat_berkas_terkunci(tmp_path, monkeypatch):
    import os

    job = G.Job("kelas9", 2, "A", "easy", 1, str(tmp_path))
    soal = ExerciseFile.model_validate(
        {"book": "kelas9", "bab_no": 2, "subbab": "A", "level": "easy", "batch": 1, "soal": [_soal(1)]}).soal
    asli, kali = os.replace, {"n": 0}

    def replace_terkunci(src, dst):
        kali["n"] += 1
        if kali["n"] < 3:
            raise PermissionError(5, "Access is denied")
        return asli(src, dst)

    monkeypatch.setattr(G.os, "replace", replace_terkunci)
    monkeypatch.setattr(G.time, "sleep", lambda *_: None)
    G._write(job, "9router:m1", soal)
    assert kali["n"] == 3 and len(P._muat(job.path).soal) == 1
