import json

from app.services.exercise import llm_verify as V
from app.services.exercise.options import susun
from app.services.exercise.schema import ExerciseFile


class _Res:
    def __init__(self, text):
        self.text, self.input_tokens, self.output_tokens = text, 10, 5


class _Client:
    """Solver palsu: menjawab sesuai kunci, kecuali id yang diminta salah / tidak dijawab."""

    def __init__(self, data, salah=(), kosong=()):
        self.opsi, self.salah, self.kosong = susun(data), set(salah), set(kosong)

    def chat(self, messages, **kw):
        soal = json.loads(messages[1]["content"].split("\n", 1)[1])
        out = {}
        for s in soal:
            if s["id"] in self.kosong:
                continue
            benar = self.opsi[s["id"]][1]
            pilih = next(o for o in "ABCD" if o != benar) if s["id"] in self.salah else benar
            out[s["id"]] = {"kerja": "x", "pilihan": pilih, "langkah": 1, "catatan": None}
        return _Res(json.dumps({"jawaban": out}))


def _soal(i):
    return {"id": f"kelas9-b02-a-easy-bt01-{i:03d}", "tipe_generate": "orisinal", "variasi_cara": None,
            "acuan": {"sumber": "siswa", "halaman": 63, "kutipan": "Klasifikasi Bangun Ruang"},
            "cognitive_c": "C1", "jumlah_langkah": 1, "jenis_soal": f"jenis {i}", "alasan_level": "satu langkah",
            "stimulus": None, "pertanyaan": f"Berapa {i} + {i}?", "jawaban_benar": str(2 * i),
            "alasan_benar": "dijumlahkan",
            "distraktor": [{"teks": str(2 * i + k), "alasan": "salah hitung"} for k in (1, 2, 3)],
            "pembahasan": "jumlahkan", "catatan": None}


def _file(tmp_path, n=10):
    data = {"book": "kelas9", "bab_no": 2, "subbab": "A", "level": "easy", "batch": 1, "skill_versi": "v1",
            "soal": [_soal(i) for i in range(1, n + 1)]}
    path = tmp_path / "A_easy.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    return str(path), ExerciseFile.model_validate(data)


def test_semua_cocok(tmp_path):
    path, data = _file(tmp_path)
    res = V.verifikasi_buta(path, _Client(data), "solver-x", progress=lambda *_: None)
    assert (res.cocok, res.total, res.tidak_cocok, res.tidak_terjawab) == (10, 10, [], [])
    assert json.loads(open(res.solver_path, encoding="utf-8").read())["model"] == "solver-x"


def test_blind_file_tidak_membocorkan_kunci(tmp_path):
    path, data = _file(tmp_path)
    V.verifikasi_buta(path, _Client(data), "solver-x", progress=lambda *_: None)
    blind = open(path.replace(".json", ".blind.json"), encoding="utf-8").read()
    assert "alasan" not in blind and "pembahasan" not in blind and "jawaban_benar" not in blind


def test_tidak_cocok_dan_tidak_terjawab_dibedakan(tmp_path):
    path, data = _file(tmp_path)
    ids = [s.id for s in data.soal]
    res = V.verifikasi_buta(path, _Client(data, salah=[ids[0]], kosong=[ids[9]]), "solver-x",
                            progress=lambda *_: None)
    assert res.tidak_cocok == [ids[0]] and res.tidak_terjawab == [ids[9]] and res.cocok == 8


class _ClientRusak(_Client):
    def chat(self, messages, **kw):
        from app.llm.ninerouter import NineRouterError
        raise NineRouterError("HTTP 502 gateway")


def test_solver_gagal_jaringan_bukan_penolakan_soal(tmp_path):
    path, data = _file(tmp_path)
    res = V.verifikasi_buta(path, _ClientRusak(data), "solver-x", progress=lambda *_: None)
    assert len(res.tidak_diverifikasi) == 10
    assert res.tidak_terjawab == [] and res.tidak_cocok == []
