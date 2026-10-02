"""
verify.py -- verifikasi BUTA oleh penyelesai independen.

Alur:
  1. prepare : tulis <KODE>_<level>.blind.json = soal + 4 opsi (posisi diacak kode),
               TANPA kunci, alasan, pembahasan, atau level.
  2. (agen penyelesai-soal-exercise mengerjakan file itu, menulis <KODE>_<level>.solver.json)
        {"jawaban": {"<id>": {"pilihan": "B", "langkah": 2}, ...}}
  3. compare : cocokkan dengan kunci -> <KODE>_<level>.verifikasi.json

  python -m app.services.exercise.verify prepare output/exercise/kelas9/batch01/bab01/A_easy.json
  python -m app.services.exercise.verify compare output/exercise/kelas9/batch01/bab01/A_easy.json
"""

from __future__ import annotations

import argparse
import json
import os
import sys

from app.services.exercise.options import susun
from app.services.exercise.refs import soal_text
from app.services.exercise.schema import ExerciseFile


def _load(path: str) -> ExerciseFile:
    with open(path, encoding="utf-8") as f:
        return ExerciseFile.model_validate(json.load(f))


def _side(path: str, suffix: str) -> str:
    return path[:-len(".json")] + suffix


def prepare(path: str) -> str:
    data = _load(path)
    opsi = susun(data)
    out = {"petunjuk": "Kerjakan setiap soal sendiri. Tulis pilihan (A-D) dan jumlah langkah penyelesaianmu.",
           "soal": [{"id": s.id, "soal": soal_text(s.stimulus, s.pertanyaan),
                     "opsi": {o["option_id"]: o["text"] for o in opsi[s.id][0]}} for s in data.soal]}
    dest = _side(path, ".blind.json")
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"{len(data.soal)} soal -> {dest}")
    return dest


def compare(path: str) -> dict:
    data = _load(path)
    opsi = susun(data)
    sp = _side(path, ".solver.json")
    with open(sp, encoding="utf-8") as f:
        jawab = json.load(f).get("jawaban", {})
    hasil, cocok = {}, 0
    for s in data.soal:
        benar = opsi[s.id][1]
        j = jawab.get(s.id) or {}
        ok = j.get("pilihan") == benar
        cocok += ok
        hasil[s.id] = {"cocok": ok, "pilihan_solver": j.get("pilihan"), "kunci": benar,
                       "langkah_solver": j.get("langkah"), "langkah_agen": s.jumlah_langkah}
    dest = _side(path, ".verifikasi.json")
    with open(dest, "w", encoding="utf-8") as f:
        json.dump({"cocok": cocok, "total": len(data.soal), "hasil": hasil}, f, ensure_ascii=False, indent=2)
    for sid, h in hasil.items():
        if not h["cocok"]:
            print(f"TIDAK COCOK {sid}: solver={h['pilihan_solver']} kunci={h['kunci']}")
    print(f"verifikasi buta: {cocok}/{len(data.soal)} cocok -> {dest}")
    return hasil


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("aksi", choices=["prepare", "compare"])
    ap.add_argument("file")
    a = ap.parse_args(argv)
    (prepare if a.aksi == "prepare" else compare)(a.file)
    return 0


if __name__ == "__main__":
    sys.exit(main())
