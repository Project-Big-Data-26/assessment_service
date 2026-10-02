"""
export.py -- gabungkan file exercise yang LOLOS validate + verifikasi buta menjadi baris
tabel `soal` backend (Daftar Collections - Big Data.xlsx).

Hasil per batch:
  output/exercise/<buku>/batch<NN>/soal_exercise_db.json    baris tabel soal (hanya kolom resmi)
  output/exercise/<buku>/batch<NN>/soal_exercise_meta.json  info internal (tipe_generate, acuan, flag, ...)

Penanda sementara (dipetakan ke ObjectId oleh Backend):
  subbab_id = NAMA subbab di buku panduan, kelas_id = kunci buku ("kelas9"), berkas_id = null.
cognitive_level, cognitive_score, confidence_score, status = null: diisi tahap validasi sistem berikutnya.
Nilai usulan kita (level target, skor target, confidence_hitung) disimpan di soal_exercise_meta.json.

  python -m app.services.exercise.export --book kelas9 --batch 1
"""

from __future__ import annotations

import argparse
import datetime as dt
import glob
import hashlib
import json
import os
import sys

from app.services.exercise import config as C
from app.services.exercise.confidence import hitung
from app.services.exercise.dedup import jarak_terdekat
from app.services.exercise.options import susun
from app.services.exercise.refs import load_exercise, load_pretest, soal_text
from app.services.exercise.validate import validate_file
from app.services.pretest.agentic import kurikulum


def _oid(sid: str) -> str:
    return hashlib.sha1(sid.encode()).hexdigest()[:24]


def export_batch(book: str, batch: int) -> dict:
    base = os.path.join(C.OUT_ROOT, book, f"batch{batch:02d}")
    rows, meta, dilewati = [], {}, []
    now = dt.datetime.now(dt.timezone(dt.timedelta(hours=7))).isoformat(timespec="seconds")
    pretest = load_pretest(book)
    for path in sorted(glob.glob(os.path.join(base, "bab[0-9][0-9]", "*_*.json"))):
        if path.endswith((".blind.json", ".solver.json", ".verifikasi.json")):
            continue
        name = os.path.relpath(path, base)
        data, errors, warns = validate_file(path)
        vp = path[:-5] + ".verifikasi.json"
        if errors or data is None:
            dilewati.append(f"{name}: validasi GAGAL ({len(errors)} error)")
            continue
        if not os.path.exists(vp):
            dilewati.append(f"{name}: belum ada verifikasi buta")
            continue
        with open(vp, encoding="utf-8") as f:
            verif = json.load(f)["hasil"]
        bab = kurikulum.get(book, data.bab_no)
        opsi = susun(data)
        pool = [r for r in pretest.values() if r.bab_no == data.bab_no and r.subbab == data.subbab]
        pool += load_exercise(book, data.bab_no, data.subbab, exclude=path)
        spec = C.LEVEL_SPEC[data.level]
        for s in data.soal:
            v = verif.get(s.id)
            skor = hitung(s, v, jarak_terdekat(s, pool, data.soal), warns)
            options, benar = opsi[s.id]
            rows.append({
                "_id": _oid(s.id), "berkas_id": None, "subbab_id": bab.subbab_nama(data.subbab),
                "kelas_id": book, "soal_text": soal_text(s.stimulus, s.pertanyaan), "image_url": [],
                "soal_type": "Pilihan Ganda", "options": options, "matching_pairs": None, "jawaban": benar,
                "cognitive_level": None, "cognitive_score": None, "status": None,
                "created_at": now, "updated_at": now, "confidence_score": None,
            })
            meta[_oid(s.id)] = {
                "id": s.id, "batch": data.batch, "bab_id": bab.bab_id, "subbab_kode": data.subbab,
                "level_target": data.level, "cognitive_score_target": spec["score"], "confidence_hitung": skor, "tipe_generate": s.tipe_generate, "variasi_cara": s.variasi_cara,
                "acuan": s.acuan.model_dump(exclude_none=True), "cognitive_c": s.cognitive_c,
                "jumlah_langkah": s.jumlah_langkah, "solver_cocok": bool(v and v["cocok"]),
                "pembahasan": s.pembahasan, "catatan": s.catatan,
                "warning": [w for w in warns if s.id in w],
            }
    with open(os.path.join(base, "soal_exercise_db.json"), "w", encoding="utf-8") as f:
        json.dump({"pipeline_version": C.PIPELINE_VERSION, "book": book, "batch": batch, "items": rows},
                  f, ensure_ascii=False, indent=2)
    with open(os.path.join(base, "soal_exercise_meta.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
    ringkas = {"total": len(rows), "file_dilewati": dilewati}
    print(ringkas)
    return ringkas


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", required=True)
    ap.add_argument("--batch", type=int, default=1)
    a = ap.parse_args(argv)
    export_batch(a.book, a.batch)
    return 0


if __name__ == "__main__":
    sys.exit(main())
