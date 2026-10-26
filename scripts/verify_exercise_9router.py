"""
Verifikasi buta file latihan lewat 9Router (model solver beda keluarga dari generator). Dari root project:

    venv/Scripts/python scripts/verify_exercise_9router.py output/exercise/kelas9/batch01/bab02/A_easy.json
    ... --model cx/gpt-6-luna      # override NINEROUTER_MODEL_SOLVER

Menulis <file>.blind.json, .solver.json, .verifikasi.json di samping file soal. File soal TIDAK diubah.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.llm.ninerouter import NineRouterClient, NineRouterSettings
from app.services.exercise.llm_verify import cek_butuh_gambar, verifikasi_buta


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--model", help="override NINEROUTER_MODEL_SOLVER")
    ap.add_argument("--tanpa-gambar", action="store_true",
                    help="berkas bergambar: kerjakan TANPA gambar; soal yang tetap benar ditandai (gambar hanya hiasan)")
    ap.add_argument("--allow-same-model", action="store_true",
                    help="izinkan solver = generator (TIDAK independen; hanya untuk uji)")
    a = ap.parse_args()

    try:
        settings = NineRouterSettings.from_environment()
    except ValueError as exc:
        print(f"[GAGAL] konfigurasi .env: {exc}")
        return 2
    model = a.model or settings.solver_model
    if not model:
        print("[GAGAL] NINEROUTER_MODEL_SOLVER belum diisi di .env (atau pakai --model)")
        return 2
    with open(a.file, encoding="utf-8") as f:
        generator = (json.load(f).get("generator") or "")
    if generator == f"9router:{model}" and not a.allow_same_model:
        print(f"[GAGAL] solver {model} sama dengan generator; verifikasi tidak independen "
              f"(pakai model lain, atau --allow-same-model untuk uji)")
        return 2

    if a.tanpa_gambar:
        with NineRouterClient(settings) as client:
            r = cek_butuh_gambar(a.file, client, model)
        print(f"\nCEK TANPA GAMBAR ({model}): {len(r.butuh_gambar)}/{r.total} soal memang butuh gambar")
        for sid in r.tanpa_gambar_cocok:
            print("  TIDAK BUTUH GAMBAR (tetap benar tanpa gambar) ", sid)
        print("Detail:", r.path)
        return 0
    print(f"Verifikasi buta {a.file}\n  generator={generator or 'tidak tercatat'}  solver={model}")
    with NineRouterClient(settings) as client:
        res = verifikasi_buta(a.file, client, model)
    print(f"\nHASIL: {res.cocok}/{res.total} cocok dengan kunci generator "
          f"({res.seconds}s, token {res.tokens_in}/{res.tokens_out})")
    for sid in res.tidak_cocok:
        print("  TIDAK COCOK  ", sid)
    for sid in res.tidak_terjawab:
        print("  TIDAK TERJAWAB (null/ambigu/gagal)", sid)
    print("Detail:", res.verifikasi_path)
    return 0 if res.cocok == res.total else 1


if __name__ == "__main__":
    raise SystemExit(main())
