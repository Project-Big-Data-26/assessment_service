"""
Kontrak file kerja agen: output/exercise/<buku>/batch<NN>/bab<NN>/<KODE>_<level>.json

Agen HANYA menulis fakta (soal, jawaban, distraktor, acuan, tingkat kognitif).
Posisi opsi A-D, confidence, status dihitung KODE, bukan agen.
"""

from __future__ import annotations

from typing import List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator
from .visual_assets import VisualSpec

Level = Literal["easy", "medium", "hard"]
Kognitif = Literal["C1", "C2", "C3", "C4", "C5", "C6"]


class _Strict(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Distraktor(_Strict):
    teks: str = Field(min_length=1)
    alasan: str = Field(min_length=3, description="miskonsepsi/kesalahan siswa yang ditiru")


class Acuan(_Strict):
    """Dasar soal.
    variasi : sumber "pretest" -> cukup `id` soal pretest (teks diambil kode);
              sumber "siswa"/"guru" -> `halaman`, `teks` (soal asal VERBATIM), `jawaban`.
    orisinal: sumber "siswa"/"guru" -> `halaman` + `kutipan` (potongan VERBATIM materi
              buku yang menjadi dasar soal; harus memuat konsep/rumus yang diuji).
    """
    sumber: Literal["pretest", "siswa", "guru", "exercise_validated", "pretest_validated"]
    id: Optional[str] = None
    halaman: Optional[int] = None
    bagian: Optional[str] = None
    nomor: Optional[str] = None
    teks: Optional[str] = None
    jawaban: Optional[str] = None
    kutipan: Optional[str] = None
    snapshot: Optional[str] = None
    source_sha256: Optional[str] = None


class Soal(_Strict):
    id: str = Field(pattern=r"^[a-z0-9_]+-b\d{2}-[a-z]-(easy|medium|hard)-bt\d{2}-g?\d{3}$")
    tipe_generate: Literal["variasi", "orisinal"]
    variasi_cara: Optional[Literal["angka", "konteks"]] = None
    acuan: Acuan
    cognitive_c: Kognitif
    # label bebas jenis pertanyaan ("menyusun model", "menentukan nilai variabel", ...);
    # dipakai validator untuk membatasi dominasi satu jenis dalam satu level.
    jenis_soal: Optional[str] = Field(None, min_length=3, max_length=60)
    jumlah_langkah: int = Field(ge=1, le=8, description="langkah penyelesaian minimal yang dibutuhkan siswa")
    alasan_level: str = Field(min_length=5, description="satu kalimat kenapa soal ini pantas di level ini")
    stimulus: Optional[str] = None
    # Soal bergambar: path gambar relatif terhadap data/processed/pretest_md/<buku>/siswa/ (mis. "img/xxx.png").
    # deskripsi_gambar = fakta yang dibaca generator dari gambar (angka, label, bentuk); TIDAK diberikan ke solver.
    gambar: List[str] = []
    deskripsi_gambar: Optional[str] = Field(None, min_length=10)
    visual_spec: Optional[VisualSpec] = None
    pertanyaan: str = Field(min_length=3)
    jawaban_benar: str = Field(min_length=1)
    alasan_benar: str = Field(min_length=3)
    distraktor: List[Distraktor] = Field(min_length=3, max_length=3)
    pembahasan: str = Field(min_length=5, description="pengerjaan singkat langkah demi langkah")
    catatan: Optional[str] = None
    # True = soal tambahan agar kuota penuh padahal bahan subbab sudah tipis (kemiripan/jarak dari materi
    # lebih longgar); diteruskan ke meta supaya validator manusia memberi perhatian ekstra.
    dipaksa_kuota: bool = False

    @model_validator(mode="after")
    def _cek_acuan(self):
        a = self.acuan
        if self.gambar and not self.deskripsi_gambar:
            raise ValueError("soal bergambar wajib mengisi deskripsi_gambar")
        if self.deskripsi_gambar and not self.gambar:
            raise ValueError("deskripsi_gambar diisi tetapi gambar kosong")
        if self.visual_spec and not self.gambar:
            raise ValueError("visual_spec requires a rendered image")
        if self.tipe_generate == "variasi":
            if self.variasi_cara is None:
                raise ValueError("variasi wajib mengisi variasi_cara ('angka' atau 'konteks')")
            if a.sumber in ("pretest", "exercise_validated", "pretest_validated"):
                if not a.id:
                    raise ValueError("acuan pretest wajib punya id")
                if a.sumber.endswith("_validated") and not (a.snapshot and a.source_sha256 and a.teks and a.jawaban):
                    raise ValueError("validated reference requires frozen snapshot, hash, original text and key")
            elif not (a.halaman and a.teks and a.jawaban):
                raise ValueError("acuan siswa/guru untuk variasi wajib halaman + teks + jawaban")
        else:
            if self.variasi_cara is not None:
                raise ValueError("orisinal tidak boleh punya variasi_cara")
            if a.sumber in ("pretest", "exercise_validated", "pretest_validated") or not (a.halaman and a.kutipan):
                raise ValueError("acuan orisinal wajib sumber siswa/guru + halaman + kutipan materi")
        return self


class ExerciseFile(_Strict):
    book: str
    bab_no: int
    subbab: str = Field(pattern=r"^[A-Z]$")
    level: Level
    batch: int = Field(ge=1)
    # versi SKILL.md yang menghasilkan file ini (kosong = dibuat sebelum v1)
    skill_versi: Optional[str] = Field(None, pattern=r"^v\d+$")
    # Pembuat file: "9router:<model>" untuk pipeline otomatis; kosong = agen Claude Code / sebelum field ini ada.
    generator: Optional[str] = Field(None, min_length=3, max_length=120)
    # True = berkas soal BERGAMBAR (<K>_<level>_gambar.json): id memakai awalan "g", semua soal wajib punya gambar.
    bergambar: bool = False
    # Kapasitas kurang: bahan subbab tidak cukup untuk kuota tanpa soal nyaris kembar / di luar materi.
    # Harus DINYATAKAN di sini (bukan kebetulan kurang), lengkap dengan alasan.
    kapasitas_kurang: bool = False
    alasan_kapasitas: Optional[str] = Field(None, min_length=10)
    soal: List[Soal] = []
