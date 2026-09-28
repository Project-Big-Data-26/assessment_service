"""
Kontrak file hasil kerja agen: output/pretest/<buku>/bab<NN>.json

Agen HANYA menulis fakta (teks soal, jawaban, distraktor, bukti kunci).
Hal yang bisa diturunkan secara deterministik -- status, posisi opsi A-D,
confidence -- dihitung oleh kode (export.py), BUKAN dikarang agen, supaya
tidak ada bias posisi jawaban dan status konsisten antar-sesi.
"""

from __future__ import annotations

from typing import List, Literal, Optional, Tuple

from pydantic import BaseModel, ConfigDict, Field


class _Strict(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Distraktor(_Strict):
    teks: str = Field(min_length=1)
    alasan: str = Field(min_length=3, description="miskonsepsi/kesalahan siswa yang ditiru")


class KunciGuru(_Strict):
    halaman: int = Field(description="halaman PDF Buku Guru")
    kutipan: str = Field(min_length=1, description="potongan VERBATIM kunci dari Buku Guru (harus MEMUAT jawabannya)")
    # Kunci yang hanya tercetak di gambar/PNG (garis, centang, tulisan dalam grafik):
    # kutipan = jawaban seperti terbaca di PNG, tidak dicocokkan ke Markdown, soal diberi flag.
    dari_png: bool = False


StatusKunci = Literal["cocok", "tidak_cocok", "tidak_ada_di_guru"]


class Soal(_Strict):
    id: str = Field(pattern=r"^[a-z0-9_]+-b\d{2}-p\d{4}-[a-z0-9-]+$")
    # Kode subbab sesuai Prasyarat_Math.xlsx ("A", "B", ...). Wajib (dicek validator),
    # Optional di sini hanya agar file lama tetap terbaca untuk dimigrasi.
    subbab: Optional[str] = Field(None, pattern=r"^[A-Z]$")
    # 1 (hitung langsung satu langkah) .. 5 (soal cerita multi-langkah / penalaran).
    # Dipakai memilih soal prasyarat "paling susah" selama cognitive_level belum diisi tim validasi.
    tingkat_kesulitan: Optional[int] = Field(None, ge=1, le=5)
    alasan_kesulitan: Optional[str] = None
    # "guru": soal asli dari Buku Guru (Soal Pengayaan/Remedial/Tambahan) -- source_page = halaman Guru
    sumber_soal: Literal["siswa", "guru"] = "siswa"
    source_page: int
    source_section: str
    source_item_no: str
    stimulus: Optional[str] = Field(None, description="bacaan/tabel/data bersama yang dibutuhkan soal (verbatim)")
    pertanyaan: str = Field(min_length=3)
    pertanyaan_disesuaikan: bool = False
    catatan_penyesuaian: Optional[str] = None
    notasi_dari_png: bool = Field(False, description="notasi matematika disalin dari render PNG (LaTeX)")
    butuh_gambar: bool = False
    image_refs: List[str] = []
    jawaban_benar: str = Field(min_length=1)
    alasan_benar: Optional[str] = Field(None, description="alasan singkat opsi benar (-> options.alasan); kosong = pakai jawaban_agen")
    distraktor: List[Distraktor] = Field(min_length=3, max_length=3)
    kunci_guru: Optional[KunciGuru] = None
    jawaban_agen: str = Field(min_length=1, description="hasil pengerjaan mandiri agen (untuk cross-check)")
    status_kunci: StatusKunci
    catatan: Optional[str] = None


AlasanLewati = Literal[
    "soal_terbuka",        # jawaban bervariasi / pendapat / "jelaskan dengan kata-katamu"
    "pembuktian",
    "menggambar_atau_mengukur",
    "proyek_atau_aktivitas",
    "isian_banyak",        # tabel isian/titik-titik banyak yang tidak bisa jadi satu soal PG
    "butuh_alat_peraga",
    "duplikat",
    "teks_tidak_terbaca",
    "lainnya",
]


class Dilewati(_Strict):
    source_page: int
    source_section: str
    source_item_no: str
    alasan: AlasanLewati
    keterangan: str = ""


class BabFile(_Strict):
    book: str
    bab: str
    bab_no: int
    halaman_siswa: Tuple[int, int]
    # "prasyarat": bab ini baru diekstrak untuk SUBBAB TERAKHIR saja (sumber soal
    # prasyarat bab lain); cek cakupan per subbab/halaman dilonggarkan.
    mode: Literal["lengkap", "prasyarat"] = "lengkap"
    soal: List[Soal] = []
    dilewati: List[Dilewati] = []


def derive_status(s: Soal) -> Tuple[str, List[str]]:
    """Status & flag ditentukan kode, bukan agen."""
    flags: List[str] = []
    if s.notasi_dari_png:
        flags.append("notasi_dari_png")
    if s.stimulus:
        flags.append("ada_stimulus")
    if s.pertanyaan_disesuaikan:
        flags.append("pertanyaan_disesuaikan_untuk_pg")
    if s.status_kunci == "tidak_ada_di_guru":
        flags.append("kunci_dari_agen")
    if s.status_kunci == "tidak_cocok":
        flags.append("kunci_guru_beda_dengan_agen")
    if s.butuh_gambar:
        flags.append("butuh_gambar")
    if s.kunci_guru and s.kunci_guru.dari_png:
        flags.append("kunci_guru_dari_png")

    if s.butuh_gambar and not s.image_refs:
        return "needs_image", flags
    if s.status_kunci != "cocok":
        return "needs_review_kunci", flags
    if s.pertanyaan_disesuaikan:
        return "needs_review_soal", flags
    return "draft", flags
