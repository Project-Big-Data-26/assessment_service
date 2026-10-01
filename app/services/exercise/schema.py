"""
Kontrak file kerja agen: output/exercise/<buku>/batch<NN>/bab<NN>/<KODE>_<level>.json

Agen HANYA menulis fakta (soal, jawaban, distraktor, acuan, tingkat kognitif).
Posisi opsi A-D, confidence, status dihitung KODE, bukan agen.
"""

from __future__ import annotations

from typing import List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator

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
    sumber: Literal["pretest", "siswa", "guru"]
    id: Optional[str] = None
    halaman: Optional[int] = None
    bagian: Optional[str] = None
    nomor: Optional[str] = None
    teks: Optional[str] = None
    jawaban: Optional[str] = None
    kutipan: Optional[str] = None


class Soal(_Strict):
    id: str = Field(pattern=r"^[a-z0-9_]+-b\d{2}-[a-z]-(easy|medium|hard)-bt\d{2}-\d{3}$")
    tipe_generate: Literal["variasi", "orisinal"]
    variasi_cara: Optional[Literal["angka", "konteks"]] = None
    acuan: Acuan
    cognitive_c: Kognitif
    jumlah_langkah: int = Field(ge=1, le=8, description="langkah penyelesaian minimal yang dibutuhkan siswa")
    alasan_level: str = Field(min_length=5, description="satu kalimat kenapa soal ini pantas di level ini")
    stimulus: Optional[str] = None
    pertanyaan: str = Field(min_length=3)
    jawaban_benar: str = Field(min_length=1)
    alasan_benar: str = Field(min_length=3)
    distraktor: List[Distraktor] = Field(min_length=3, max_length=3)
    pembahasan: str = Field(min_length=5, description="pengerjaan singkat langkah demi langkah")
    catatan: Optional[str] = None

    @model_validator(mode="after")
    def _cek_acuan(self):
        a = self.acuan
        if self.tipe_generate == "variasi":
            if self.variasi_cara is None:
                raise ValueError("variasi wajib mengisi variasi_cara ('angka' atau 'konteks')")
            if a.sumber == "pretest":
                if not a.id:
                    raise ValueError("acuan pretest wajib punya id")
            elif not (a.halaman and a.teks and a.jawaban):
                raise ValueError("acuan siswa/guru untuk variasi wajib halaman + teks + jawaban")
        else:
            if self.variasi_cara is not None:
                raise ValueError("orisinal tidak boleh punya variasi_cara")
            if a.sumber == "pretest" or not (a.halaman and a.kutipan):
                raise ValueError("acuan orisinal wajib sumber siswa/guru + halaman + kutipan materi")
        return self


class ExerciseFile(_Strict):
    book: str
    bab_no: int
    subbab: str = Field(pattern=r"^[A-Z]$")
    level: Level
    batch: int = Field(ge=1)
    soal: List[Soal] = []
