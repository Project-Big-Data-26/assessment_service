import json
import os

import pytest

from app.services.exercise import config as C
from app.services.exercise import export, validate
from app.services.exercise.schema import ExerciseFile, Soal

REL = "img/panduan_siswa_kelas5.pdf-0024-03.png"
PRETEST_ID = "kelas5-b01-p0024-ayo-berlatih-1a"
ADA_DATA = os.path.exists(os.path.join(C.GAMBAR_ROOT, "kelas5", "siswa", REL)) and \
    os.path.exists(os.path.join("output", "pretest", "kelas5", "bab01.json"))
butuh_data = pytest.mark.skipif(not ADA_DATA, reason="data gambar/pretest lokal tidak ada")


def _soal(i=1, gambar=(REL,), prefix="kelas5-b01-a-easy-bt01-g"):
    return {"id": f"{prefix}{i:03d}", "tipe_generate": "variasi", "variasi_cara": "konteks",
            "acuan": {"sumber": "pretest", "id": PRETEST_ID},
            "cognitive_c": "C1", "jumlah_langkah": 1, "jenis_soal": "nilai tempat dari label harga",
            "alasan_level": "satu langkah membaca label harga",
            "gambar": list(gambar), "deskripsi_gambar": "gelang dengan label harga Rp15.950,00" if gambar else None,
            "pertanyaan": "Perhatikan label harga pada gambar. Angka 9 menempati nilai tempat ....",
            "jawaban_benar": "ratusan", "alasan_benar": "angka 9 pada 15.950 ada di tempat ratusan",
            "distraktor": [{"teks": "puluhan", "alasan": "salah menghitung posisi"},
                           {"teks": "ribuan", "alasan": "menyangka 9 ribuan"},
                           {"teks": "satuan", "alasan": "tertukar dengan nol"}],
            "pembahasan": "Pada 15.950, angka 9 di posisi ratusan."}


def _file(soal, bergambar=True):
    return {"book": "kelas5", "bab_no": 1, "subbab": "A", "level": "easy", "batch": 1, "skill_versi": "v1",
            "generator": "9router:m1", "bergambar": bergambar, "soal": soal}


def test_schema_gambar_butuh_deskripsi():
    bad = _soal()
    bad["deskripsi_gambar"] = None
    with pytest.raises(ValueError):
        Soal.model_validate(bad)


def test_id_awalan_g_diterima_dan_tanpa_g_untuk_teks():
    assert Soal.model_validate(_soal()).id.endswith("-g001")
    teks = _soal(gambar=(), prefix="kelas5-b01-a-easy-bt01-")
    assert Soal.model_validate(teks).gambar == []


@butuh_data
def test_validate_berkas_bergambar_lolos(tmp_path):
    path = tmp_path / "A_easy_gambar.json"
    path.write_text(json.dumps(_file([_soal()])), encoding="utf-8")
    _data, errors, _warns = validate.validate_file(str(path))
    assert not [e for e in errors if "kembar" not in e and "jawaban variasi SAMA" not in e], errors


@butuh_data
def test_validate_menolak_gambar_di_berkas_teks_dan_berkas_hilang(tmp_path):
    path = tmp_path / "A_easy.json"
    teks = _soal(prefix="kelas5-b01-a-easy-bt01-")
    path.write_text(json.dumps(_file([teks], bergambar=False)), encoding="utf-8")
    _d, errors, _w = validate.validate_file(str(path), partial=True)
    assert any("gambar hanya boleh di berkas bergambar" in e for e in errors)

    hilang = _soal(gambar=("img/tidak-ada.png",))
    path2 = tmp_path / "B_easy_gambar.json"
    path2.write_text(json.dumps(_file([hilang])), encoding="utf-8")
    _d, errors, _w = validate.validate_file(str(path2))
    assert any("berkas gambar tidak ada" in e for e in errors)


@butuh_data
def test_validate_menolak_gambar_terpakai_lebih_dari_maks(tmp_path):
    soal = [_soal(i) for i in range(1, C.MAKS_PAKAI_GAMBAR + 2)]
    path = tmp_path / "A_easy_gambar.json"
    path.write_text(json.dumps(_file(soal)), encoding="utf-8")
    _d, errors, _w = validate.validate_file(str(path))
    assert any("dipakai" in e and "maks" in e for e in errors)


@butuh_data
def test_ekspor_mengisi_image_url(tmp_path, monkeypatch):
    base = tmp_path / "kelas5" / "batch01" / "bab01"
    base.mkdir(parents=True)
    s = _soal()
    s["jawaban_benar"] = "ratusan (angka 9)"      # beda dari jawaban acuan agar lolos validator
    (base / "A_easy_gambar.json").write_text(json.dumps(_file([s])), encoding="utf-8")
    monkeypatch.setattr(C, "OUT_ROOT", str(tmp_path))
    export.export_batch("kelas5", 1)
    db = json.loads((tmp_path / "kelas5" / "batch01" / "soal_exercise_db.json").read_text(encoding="utf-8"))
    meta = json.loads((tmp_path / "kelas5" / "batch01" / "soal_exercise_meta.json").read_text(encoding="utf-8"))
    assert len(db["items"]) == 1
    assert db["items"][0]["image_url"] == [f"{C.GAMBAR_ROOT}/kelas5/siswa/{REL}"]
    only = next(iter(meta.values()))
    assert only["bergambar"] is True and only["gambar"] == [REL]


def test_exercisefile_bergambar_default_false():
    assert ExerciseFile.model_validate(_file([], bergambar=False)).bergambar is False
