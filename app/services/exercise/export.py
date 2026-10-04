"""
export.py -- gabungkan file exercise yang LOLOS validate (cek format/kuota/duplikat milik generator) menjadi baris
tabel `soal` backend (Daftar Collections - Big Data.xlsx).

Hasil per batch:
  output/exercise/<buku>/batch<NN>/soal_exercise_db.json    baris tabel soal (hanya kolom resmi)
  output/exercise/<buku>/batch<NN>/soal_exercise_meta.json  info internal (tipe_generate, acuan, flag, ...)
  output/exercise/<buku>/batch<NN>/per_subbab/              turunan per subbab: .json (kolom tabel) + .md (lembar koreksi)
  (hanya turunan: koreksi dilakukan di file kerja <K>_<level>.json lalu export dijalankan ulang)

Penanda sementara (dipetakan ke ObjectId oleh Backend):
  subbab_id = NAMA subbab di buku panduan, kelas_id = kunci buku ("kelas9"), berkas_id = null.
cognitive_level, cognitive_score, confidence_score, status = null: diisi tahap validasi sistem berikutnya.
Nilai usulan kita (level target, skor target) disimpan di soal_exercise_meta.json.

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
from app.services.exercise.options import susun
from app.services.exercise.refs import soal_text
from app.services.exercise.validate import validate_file
from app.services.pretest.agentic import kurikulum
from app.services.pretest.agentic.books import get_book


def _oid(sid: str) -> str:
    return hashlib.sha1(sid.encode()).hexdigest()[:24]


def export_batch(book: str, batch: int) -> dict:
    base = os.path.join(C.OUT_ROOT, book, f"batch{batch:02d}")
    rows, meta, dilewati = [], {}, []
    now = dt.datetime.now(dt.timezone(dt.timedelta(hours=7))).isoformat(timespec="seconds")
    prev = {}   # export sebelumnya: timestamp dipertahankan bila isi soal tidak berubah (file stabil, hash tidak bergeser)
    try:
        with open(os.path.join(base, "soal_exercise_db.json"), encoding="utf-8") as f:
            prev = {r["_id"]: r for r in json.load(f)["items"]}
    except (OSError, ValueError, KeyError):
        pass
    for path in sorted(glob.glob(os.path.join(base, "bab[0-9][0-9]", "*_*.json"))):
        if path.endswith((".blind.json", ".solver.json", ".verifikasi.json")):
            continue
        name = os.path.relpath(path, base)
        data, errors, warns = validate_file(path)
        if errors or data is None:
            dilewati.append(f"{name}: validasi GAGAL ({len(errors)} error)")
            continue
        bab = kurikulum.get(book, data.bab_no)
        opsi = susun(data)
        spec = C.LEVEL_SPEC[data.level]
        kuota = C.KUOTA_PER_LEVEL[get_book(book).jenjang]
        kurang = ({"jumlah": len(data.soal), "kuota": kuota, "alasan": data.alasan_kapasitas}
                  if data.kapasitas_kurang else None)
        for s in data.soal:
            options, benar = opsi[s.id]
            row = {
                "_id": _oid(s.id), "berkas_id": None, "subbab_id": bab.subbab_nama(data.subbab),
                "kelas_id": book, "soal_text": soal_text(s.stimulus, s.pertanyaan), "image_url": [],
                "soal_type": "Pilihan Ganda", "options": options, "matching_pairs": None, "jawaban": benar,
                "cognitive_level": None, "cognitive_score": None, "status": None,
                "created_at": now, "updated_at": now, "confidence_score": None,
            }
            lama = prev.get(row["_id"])
            if lama:
                row["created_at"] = lama.get("created_at", now)
                row["updated_at"] = lama.get("updated_at", now) if all(
                    lama.get(k) == v for k, v in row.items() if k not in ("created_at", "updated_at")) else now
            rows.append(row)
            meta[_oid(s.id)] = {
                "id": s.id, "batch": data.batch, "bab_id": bab.bab_id, "subbab_kode": data.subbab,
                "level_target": data.level, "cognitive_score_target": spec["score"], "tipe_generate": s.tipe_generate, "variasi_cara": s.variasi_cara,
                "acuan": s.acuan.model_dump(exclude_none=True), "cognitive_c": s.cognitive_c,
                "jumlah_langkah": s.jumlah_langkah, "jenis_soal": s.jenis_soal,
                "pembahasan": s.pembahasan, "catatan": s.catatan, "dipaksa_kuota": s.dipaksa_kuota,
                "kapasitas_kurang": kurang, "skill_versi": data.skill_versi or "pra-v1",
                "warning": [w for w in warns if s.id in w],
            }
    with open(os.path.join(base, "soal_exercise_db.json"), "w", encoding="utf-8") as f:
        json.dump({"pipeline_version": C.PIPELINE_VERSION, "book": book, "batch": batch, "items": rows},
                  f, ensure_ascii=False, indent=2)
    with open(os.path.join(base, "soal_exercise_meta.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
    from app.services.exercise.review import tulis_per_subbab, tulis_readme
    n_sub = tulis_per_subbab(base, book, rows, meta)
    tulis_readme(base, book, batch, rows, meta)
    ringkas = {"total": len(rows), "file_per_subbab": n_sub, "file_dilewati": dilewati}
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
