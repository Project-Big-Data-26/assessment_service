"""
Generate soal latihan 1 subbab x 1 level lewat 9Router. Dari root project:

    venv/Scripts/python scripts/generate_exercise_9router.py --book kelas9 --bab 2 --subbab A --level easy
    ... --batch 1 --model gemini/gemini-3.8-flash [--out output/exercise_uji]

Hasil ke output/exercise/ (satu kesatuan dengan batch lain). File yang sudah ada dilanjutkan hanya bila dibuat
pipeline ini dengan model yang sama; selain itu ditolak, tidak pernah ditimpa. Validasi mekanis memakai app.services.exercise.validate.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.llm.ninerouter import NineRouterClient, NineRouterSettings
from app.services.exercise import config as C
from app.services.exercise.llm_generate import GenerateError, Job, generate


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", required=True)
    ap.add_argument("--bab", type=int, required=True)
    ap.add_argument("--subbab", required=True)
    ap.add_argument("--level", required=True, choices=["easy", "medium", "hard"])
    ap.add_argument("--batch", type=int, default=1)
    ap.add_argument("--gambar", action="store_true",
                    help="soal BERGAMBAR: gambar diambil dari soal pretest bergambar subbab itu (butuh model vision)")
    ap.add_argument("--model", help="override NINEROUTER_MODEL")
    ap.add_argument("--out", default=C.OUT_ROOT, help="akar keluaran (default output/exercise; untuk uji pakai folder lain)")
    a = ap.parse_args()

    try:
        settings = NineRouterSettings.from_environment()
    except ValueError as exc:
        print(f"[GAGAL] konfigurasi .env: {exc}")
        return 2
    if a.model:
        settings = NineRouterSettings(**{**settings.__dict__, "model": a.model})
    job = Job(a.book, a.bab, a.subbab.upper(), a.level, a.batch, os.path.abspath(a.out), a.gambar)
    print(f"Job {job.book} bab{job.bab_no} {job.subbab} {job.level} batch{job.batch} model={settings.model}")
    with NineRouterClient(settings) as client:
        try:
            res = generate(job, client)
        except GenerateError as exc:
            print(f"[GAGAL] {exc}")
            return 1
    for e in res.errors:
        print("ERROR  ", e)
    for w in res.warnings:
        print("WARNING", w)
    print(f"{'LOLOS' if res.lolos else 'BELUM LOLOS'}: {res.accepted}/{res.kuota} soal, {res.rounds} putaran, "
          f"{res.seconds}s, token {res.tokens_in}/{res.tokens_out}")
    print("File:", res.path)
    return 0 if res.lolos else 1


if __name__ == "__main__":
    raise SystemExit(main())
