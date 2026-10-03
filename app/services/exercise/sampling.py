"""
sampling.py -- pilih soal yang WAJIB dikoreksi manusia sebelum push ke DB.

  - semua soal dengan confidence_score < CONFIDENCE_SAMPLING_BATAS
  - + SAMPLING_ACAK_PERSEN dari sisanya (acak, seed tetap) untuk menguji apakah skor bisa dipercaya

  python -m app.services.exercise.sampling --book kelas9 --batch 1
Hasil: output/exercise/<buku>/batch<NN>/sampling.json
"""

from __future__ import annotations

import argparse
import json
import math
import os
import random
import sys

from app.services.exercise import config as C


def pilih(book: str, batch: int) -> dict:
    base = os.path.join(C.OUT_ROOT, book, f"batch{batch:02d}")
    with open(os.path.join(base, "soal_exercise_db.json"), encoding="utf-8") as f:
        rows = json.load(f)["items"]
    with open(os.path.join(base, "soal_exercise_meta.json"), encoding="utf-8") as f:
        meta = json.load(f)
    def skor(r):
        return meta[r["_id"]]["confidence_hitung"]

    rendah = [r for r in rows if skor(r) < C.CONFIDENCE_SAMPLING_BATAS]
    sisa = [r for r in rows if r not in rendah]
    k = math.ceil(len(sisa) * C.SAMPLING_ACAK_PERSEN) if sisa else 0
    acak = random.Random(f"sampling-{book}-{batch}").sample(sisa, k)
    out = {"batas": C.CONFIDENCE_SAMPLING_BATAS, "total": len(rows),
           "wajib_cek": [{"_id": r["_id"], "id": meta[r["_id"]]["id"], "confidence_score": skor(r),
                          "alasan": "confidence rendah"} for r in rendah],
           "acak": [{"_id": r["_id"], "id": meta[r["_id"]]["id"], "confidence_score": skor(r),
                     "alasan": "sampel acak"} for r in acak]}
    with open(os.path.join(base, "sampling.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"total {len(rows)} | wajib cek {len(rendah)} | sampel acak {len(acak)}")
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", required=True)
    ap.add_argument("--batch", type=int, default=1)
    a = ap.parse_args(argv)
    pilih(a.book, a.batch)
    return 0


if __name__ == "__main__":
    sys.exit(main())
