"""
llm_pipeline.py -- satu slot (subbab x level) lengkap: generate -> verifikasi buta -> perbaiki -> verifikasi ulang.

Soal yang dijawab BEDA atau "tidak bisa ditentukan" oleh solver dibuang dari berkas, lalu generator menulis
pengganti (dengan alasan solver sebagai umpan balik) dan solver memeriksa ulang. Setelah `maks_perbaikan`
putaran, soal yang masih bermasalah dibuang dan berkas dinyatakan kapasitas_kurang (tidak ada soal yang
belum cocok ikut diekspor).
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import List

from app.llm.ninerouter import NineRouterClient
from app.services.exercise import config as C
from app.services.exercise.llm_generate import GenerateError, Job, _short, _write, generate
from app.services.exercise.llm_verify import verifikasi_buta
from app.services.exercise.refs import soal_text
from app.services.exercise.schema import ExerciseFile
from app.services.exercise.validate import validate_file
from app.services.pretest.agentic.books import get_book

STATUS_SELESAI = "selesai"
STATUS_KURANG = "selesai_kurang"     # sebagian soal dibuang karena tidak lolos verifikasi
STATUS_GAGAL = "gagal"


@dataclass
class SlotResult:
    path: str
    status: str
    soal: int
    kuota: int
    perbaikan: int
    dibuang: int
    errors: List[str] = field(default_factory=list)
    tokens_in: int = 0
    tokens_out: int = 0
    seconds: float = 0.0


def _muat(path: str) -> ExerciseFile:
    with open(path, encoding="utf-8") as f:
        return ExerciseFile.model_validate(json.load(f))


def _solver_catatan(solver_path: str) -> dict:
    try:
        with open(solver_path, encoding="utf-8") as f:
            return json.load(f).get("jawaban", {})
    except (OSError, ValueError):
        return {}


def _buang(job: Job, ids: List[str], solver_path: str) -> List[str]:
    """Hapus soal bermasalah dari berkas; kembalikan umpan balik untuk generator."""
    data = _muat(job.path)
    jawab = _solver_catatan(solver_path)
    umpan: List[str] = []
    for s in data.soal:
        if s.id in ids:
            j = jawab.get(s.id) or {}
            alasan = (j.get("catatan") or j.get("kerja") or "solver tidak menemukan opsi yang benar")
            umpan.append(f"{_short(soal_text(s.stimulus, s.pertanyaan), 110)} -> DITOLAK solver "
                         f"(kunci: {s.jawaban_benar}). Alasan solver: {_short(str(alasan), 220)}. "
                         f"Pastikan data soal konsisten dan tepat satu opsi benar.")
    sisa = [s.model_copy(update={"id": f"{job.id_prefix}{i:03d}"})
            for i, s in enumerate([x for x in data.soal if x.id not in ids], 1)]
    _write(job, data.generator or "", sisa)
    return umpan


def kerjakan_slot(job: Job, client: NineRouterClient, solver_model: str, *, maks_perbaikan: int = 2,
                  progress=print) -> SlotResult:
    kuota = C.KUOTA_GAMBAR_MAKS if job.gambar else C.KUOTA_PER_LEVEL[get_book(job.book).jenjang]
    tok_in = tok_out = 0
    dibuang = 0
    umpan: List[str] = []
    seconds = 0.0
    try:
        for ronde in range(maks_perbaikan + 1):
            gen = generate(job, client, progress=progress, umpan_awal=umpan)
            tok_in, tok_out, seconds = tok_in + gen.tokens_in, tok_out + gen.tokens_out, seconds + gen.seconds
            ver = verifikasi_buta(job.path, client, solver_model, progress=progress)
            tok_in, tok_out, seconds = tok_in + ver.tokens_in, tok_out + ver.tokens_out, seconds + ver.seconds
            bermasalah = ver.tidak_cocok + ver.tidak_terjawab
            progress(f"  ronde {ronde + 1}: {ver.cocok}/{ver.total} cocok, bermasalah {len(bermasalah)}")
            if not bermasalah:
                _data, errors, _w = validate_file(job.path, partial=False)
                status = STATUS_GAGAL if errors else (STATUS_SELESAI if ver.total >= kuota else STATUS_KURANG)
                return SlotResult(job.path, status, ver.total, kuota,
                                  ronde, dibuang, errors, tok_in, tok_out, round(seconds, 1))
            dibuang += len(bermasalah)
            umpan = _buang(job, bermasalah, ver.solver_path)
            if ronde == maks_perbaikan:
                break
        # perbaikan habis: soal yang tersisa sudah bersih (yang bermasalah sudah dibuang)
        sisa = _muat(job.path)
        if not sisa.soal:
            return SlotResult(job.path, STATUS_GAGAL, 0, kuota, maks_perbaikan, dibuang,
                              ["semua soal dibuang solver"], tok_in, tok_out, round(seconds, 1))
        if not job.gambar:
            _write(job, sisa.generator or "", sisa.soal, kapasitas_kurang=len(sisa.soal) < kuota,
                   alasan=(f"{dibuang} soal dibuang karena tidak cocok dengan solver independen setelah "
                           f"{maks_perbaikan} perbaikan otomatis") if len(sisa.soal) < kuota else None)
        _data, errors, _w = validate_file(job.path, partial=False)
        return SlotResult(job.path, STATUS_KURANG if not errors else STATUS_GAGAL, len(sisa.soal), kuota,
                          maks_perbaikan, dibuang, errors, tok_in, tok_out, round(seconds, 1))
    except GenerateError as exc:
        return SlotResult(job.path, STATUS_GAGAL, 0, kuota, 0, dibuang, [str(exc)], tok_in, tok_out,
                          round(seconds, 1))
