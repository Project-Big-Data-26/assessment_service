import json
from collections import Counter

import pytest

from app.services.pretest.agentic import books, export, kurikulum, validate
from app.services.pretest.agentic.books import Book
from app.services.pretest.agentic.schema import Soal, derive_status

SISWA_P23 = """<!-- kelas5 siswa hal.23 -->

## **Ayo Berpikir Kritis**

Kecamatan Kayu Tanam terletak di Kabupaten Padang Pariaman, Provinsi Sumatra Barat. Pada tahun 2018,
penduduk kecamatan ini berjumlah 26.932 jiwa yang terdiri atas 13.354 jiwa laki-laki.

1. Tuliskan jumlah seluruh penduduk Kecamatan Kayu Tanam dan tentukan nilai tempatnya.

2. Joko membeli 1<sup>1</sup> kg gula jawa dan 2<sup>1</sup> 2 2 kg tepung. Berapa kg berat seluruh belanjaan Joko?
"""
GURU_P45 = """<!-- kelas5 guru hal.45 -->
1. Jumlah seluruh penduduk Kecamatan Kayu Tanam adalah 26.932 Jiwa.
"""


@pytest.fixture
def fake_book(tmp_path, monkeypatch):
    monkeypatch.setattr(books, "MD_ROOT", str(tmp_path / "md"))
    monkeypatch.setattr(books, "OUT_ROOT", str(tmp_path / "out"))
    book = Book("kelas5", 5, "SD", siswa_pdf="panduan_siswa_kelas5.pdf", guru_pdf="panduan_guru_kelas5.pdf")
    for kind, page, text in (("siswa", 23, SISWA_P23), ("guru", 45, GURU_P45)):
        d = tmp_path / "md" / "kelas5" / kind
        d.mkdir(parents=True, exist_ok=True)
        (d / f"p{page:04d}.md").write_text(text, encoding="utf-8")
    (tmp_path / "md" / "kelas5" / "siswa" / "index.json").write_text(json.dumps({"pages": {
        "23": {"latihan": ["Ayo Berpikir Kritis"], "risiko_matematika": ["sup/sub"]}}}), encoding="utf-8")
    monkeypatch.setattr(validate, "get_book", lambda key: book)
    fake_bab = kurikulum.Bab("SD5-B1", "kelas5", 1, "Bilangan Cacah", [("A", "Membaca"), ("B", "Membandingkan")], ["SD4-B1"])
    monkeypatch.setattr(kurikulum, "get", lambda b, n: fake_bab)
    monkeypatch.setattr(export, "discover", lambda: {"kelas5": book})
    return book


def _soal(**over):
    base = {
        "id": "kelas5-b01-p0023-ayo-berpikir-kritis-1",
        "subbab": "A", "tingkat_kesulitan": 2,
        "source_page": 23, "source_section": "Ayo Berpikir Kritis", "source_item_no": "1",
        "stimulus": "Kecamatan Kayu Tanam terletak di Kabupaten Padang Pariaman, Provinsi Sumatra Barat.",
        "pertanyaan": "Tuliskan jumlah seluruh penduduk Kecamatan Kayu Tanam dan tentukan nilai tempatnya.",
        "jawaban_benar": "26.932; angka 2 menempati puluh ribuan",
        "distraktor": [
            {"teks": "13.354; angka 1 menempati puluh ribuan", "alasan": "hanya laki-laki"},
            {"teks": "26.932; angka 2 menempati ribuan", "alasan": "salah nilai tempat"},
            {"teks": "40.286; angka 4 menempati puluh ribuan", "alasan": "menjumlah dua kali"},
        ],
        "kunci_guru": {"halaman": 45, "kutipan": "Jumlah seluruh penduduk Kecamatan Kayu Tanam adalah 26.932"},
        "jawaban_agen": "26.932",
        "status_kunci": "cocok",
    }
    base.update(over)
    return base


def _write(tmp_path, soal_list, dilewati=()):
    out = tmp_path / "out" / "kelas5"
    out.mkdir(parents=True, exist_ok=True)
    path = out / "bab01.json"
    path.write_text(json.dumps({
        "book": "kelas5", "bab": "Bab 1 - Bilangan Cacah", "bab_no": 1, "halaman_siswa": [19, 46],
        "soal": soal_list, "dilewati": list(dilewati)}), encoding="utf-8")
    return str(path)


def test_coverage_accepts_verbatim_and_rejects_paraphrase():
    page = validate.tokens(SISWA_P23)
    assert validate.coverage(validate.tokens("Tuliskan jumlah seluruh penduduk Kecamatan Kayu Tanam"), page) == 1.0
    assert validate.coverage(validate.tokens("Hitung total warga di desa Kayu Tanam sekarang"), page) < 0.9


def test_comparison_signs_are_not_mistaken_for_html_tags():
    page = validate.tokens("Karena 3 < 5 maka pecahan pertama lebih kecil <br> 7 > 2 atau sama")
    assert "maka" in page and "lebih" in page and "br" not in page


def test_words_glued_by_pdf_conversion_still_count_as_verbatim():
    page = validate.tokens("Burung KetilangdanJalanJalak hinggap di dahan.")
    assert validate.coverage(validate.tokens("Burung Ketilang dan Jalan Jalak hinggap di dahan."), page) >= 0.9


def test_latex_is_ignored_when_notation_came_from_png():
    page = validate.tokens(SISWA_P23)
    q = r"Joko membeli $1\frac{1}{2}$ kg gula jawa dan $2\frac{1}{2}$ kg tepung. Berapa kg berat seluruh belanjaan Joko?"
    assert validate.coverage(validate.tokens(q, strip_latex=True), page) >= 0.9


def test_valid_file_passes(fake_book, tmp_path):
    _data, errors, warns = validate.validate_file(_write(tmp_path, [_soal()]))
    assert errors == []
    assert any("[M]" in w for w in warns)  # halaman 23 bertanda risiko matematika


@pytest.mark.parametrize("override, expected", [
    ({"pertanyaan": "Berapa total warga Kayu Tanam menurut data sensus terbaru tahun ini?"}, "verbatim"),
    ({"kunci_guru": {"halaman": 45, "kutipan": "Jumlah penduduk adalah 99.999 orang dewasa"}}, "kutipan kunci"),
    ({"kunci_guru": None}, "wajib mengisi kunci_guru"),
    ({"status_kunci": "tidak_ada_di_guru"}, "kunci_guru diisi"),
    ({"jawaban_benar": "2/3", "distraktor": [
        {"teks": "4/6", "alasan": "senilai"}, {"teks": "1/3", "alasan": "salah"}, {"teks": "3/2", "alasan": "terbalik"}]}, "bernilai sama"),
    ({"id": "kelas5-b02-p0023-x-1"}, "id harus diawali"),
    ({"subbab": None}, "subbab wajib diisi"),
    ({"subbab": "Z"}, "tidak ada di bab ini"),
    ({"tingkat_kesulitan": None}, "tingkat_kesulitan"),
    # satu angka berubah = 98% token cocok, tapi soal jadi salah -> wajib ditolak
    ({"stimulus": "penduduk kecamatan ini berjumlah 26.923 jiwa yang terdiri atas 13.354 jiwa laki-laki."},
     "angka di stimulus"),
])
def test_invalid_files_are_rejected(fake_book, tmp_path, override, expected):
    _data, errors, _warns = validate.validate_file(_write(tmp_path, [_soal(**override)]))
    assert any(expected in e for e in errors), errors


def test_untouched_exercise_page_is_warned(fake_book, tmp_path):
    skipped = {"source_page": 23, "source_section": "Ayo Berpikir Kritis", "source_item_no": "1",
               "alasan": "soal_terbuka"}
    _data, errors, warns = validate.validate_file(_write(tmp_path, [], [skipped]))
    assert errors == [] and not any("terlewat" in w for w in warns)
    _data, errors, warns = validate.validate_file(_write(tmp_path, []))
    assert any("terlewat" in w for w in warns)


def test_derive_status():
    s = Soal.model_validate(_soal())
    assert derive_status(s)[0] == "draft"
    assert derive_status(Soal.model_validate(_soal(status_kunci="tidak_cocok")))[0] == "needs_review_kunci"
    no_key = _soal(status_kunci="tidak_ada_di_guru", kunci_guru=None)
    assert "kunci_dari_agen" in derive_status(Soal.model_validate(no_key))[1]
    assert derive_status(Soal.model_validate(_soal(butuh_gambar=True)))[0] == "needs_image"


def test_export_balances_correct_option_positions(fake_book, tmp_path):
    soal = [_soal(id=f"kelas5-b01-p0023-ayo-berpikir-kritis-{i}", source_item_no=str(i)) for i in range(1, 13)]
    _write(tmp_path, soal)
    summary = export.export_book("kelas5")
    assert summary["total"] == 12 and summary["draft"] == 12
    items = json.loads((tmp_path / "out" / "kelas5" / "soal_pretest.json").read_text(encoding="utf-8"))["items"]
    assert Counter(i["correct_option_id"] for i in items) == {"A": 3, "B": 3, "C": 3, "D": 3}
    for it in items:
        correct = next(o for o in it["options"] if o["option_id"] == it["correct_option_id"])
        assert correct["text"] == it["correct_answer"]
        assert it["pertanyaan_text"].startswith("Kecamatan Kayu Tanam")


def test_subbab_with_fewer_than_two_soal_is_warned(fake_book, tmp_path):
    _data, errors, warns = validate.validate_file(_write(tmp_path, [_soal()]))
    assert errors == []
    assert any("subbab A" in w for w in warns) and any("subbab B" in w for w in warns)
    two = [_soal(), _soal(id="kelas5-b01-p0023-ayo-berpikir-kritis-2", source_item_no="2")]
    _data, errors, warns = validate.validate_file(_write(tmp_path, two))
    assert not any("subbab A" in w for w in warns) and any("subbab B" in w for w in warns)


def test_pick_subbab_prefers_verified_and_spreads_difficulty():
    from app.services.pretest.agentic.pretest import pick_hardest, pick_subbab

    def mk(i, diff, status_kunci="cocok"):
        extra = {} if status_kunci == "cocok" else {"kunci_guru": None}
        return Soal.model_validate(_soal(id=f"kelas5-b01-p0023-x-{i}", source_item_no=str(i),
                                         tingkat_kesulitan=diff, status_kunci=status_kunci, **extra))
    pool = [mk(1, 2), mk(2, 5), mk(3, 3), mk(4, 5, "tidak_ada_di_guru"), mk(5, 1)]
    chosen = pick_subbab(pool)
    assert [s.tingkat_kesulitan for s in chosen] == [5, 1]            # tersebar, dari yang terverifikasi
    assert all(s.status_kunci == "cocok" for s in chosen)
    assert pick_hardest(pool).id == "kelas5-b01-p0023-x-2"           # tersulit & terverifikasi
    assert pick_subbab([mk(4, 5, "tidak_ada_di_guru")]) != []          # boleh turun kelas kalau terpaksa


def test_latex_only_key_quote_is_flagged_for_human_check(fake_book, tmp_path):
    soal = _soal(kunci_guru={"halaman": 45, "kutipan": r"$\frac{3}{4}$"})
    _data, errors, warns = validate.validate_file(_write(tmp_path, [soal]))
    assert errors == [] and any("hanya berisi notasi LaTeX" in w for w in warns)


def test_key_quote_without_the_answer_is_flagged(fake_book, tmp_path):
    # kutipan diambil dari halaman Guru tapi tidak memuat jawaban (26.932) -> harus ketahuan
    soal = _soal(jawaban_benar="26.932 jiwa", kunci_guru={"halaman": 45, "kutipan": "Jumlah seluruh penduduk Kecamatan Kayu Tanam adalah"})
    _data, _errors, warns = validate.validate_file(_write(tmp_path, [soal]))
    assert any("tidak memuat satu pun angka jawaban" in w for w in warns)


def test_key_read_from_png_is_allowed_but_flagged(fake_book, tmp_path):
    soal = _soal(kunci_guru={"halaman": 45, "kutipan": "tercetak di gambar: 26.932", "dari_png": True})
    data, errors, _warns = validate.validate_file(_write(tmp_path, [soal]))
    assert errors == []
    assert "kunci_guru_dari_png" in derive_status(data.soal[0])[1]
