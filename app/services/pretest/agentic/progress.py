"""
progress.py -- MEMORI agen lintas sesi.

Agen tidak mengingat apa pun antar-sesi, dan konteksnya harus tetap kecil.
Jadi "ingatan" disimpan di file, bukan di percakapan:
  output/pretest/PROGRESS.md        -- papan progres semua buku x bab
                                       (dibuat ulang otomatis oleh validate.py)
  output/pretest/<buku>/_status.json -- hasil validasi terakhir per bab
  output/pretest/<buku>/CATATAN.md   -- temuan khusus buku yang ditulis agen
                                       (mis. "kunci Bab 3 ada di hal. 180-195
                                       Buku Guru, judulnya 'Alternatif
                                       Penyelesaian'") supaya sesi berikutnya
                                       tidak perlu mencari ulang

Cara pakai:
  python -m app.services.pretest.agentic.progress           # tulis & tampilkan PROGRESS.md
  python -m app.services.pretest.agentic.progress next      # bab berikutnya yang belum selesai
  python -m app.services.pretest.agentic.progress next --book kelas5
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from typing import List, Optional

from app.services.pretest.agentic.books import OUT_ROOT, discover, rel
from app.services.pretest.agentic.convert import bab_ranges


def _rows():
    for key, book in discover().items():
        idx_path = os.path.join(book.md_dir("siswa"), "index.json")
        converted = {k: os.path.exists(os.path.join(book.md_dir(k), "index.json")) for k in ("siswa", "guru")}
        status = {}
        st_path = os.path.join(book.out_dir(), "_status.json")
        if os.path.exists(st_path):
            with open(st_path, encoding="utf-8") as f:
                status = json.load(f)
        babs = []
        if converted["siswa"]:
            with open(idx_path, encoding="utf-8") as f:
                pages = json.load(f)["pages"]
            babs = [b for b in bab_ranges(pages) if b["bab_no"]]
        yield key, book, converted, babs, status


def bab_filename(bab_no: int) -> str:
    return f"bab{bab_no:02d}.json"


def write_progress() -> str:
    lines = ["# Progres ekstraksi soal pretest (dibuat otomatis -- jangan diedit manual)", "",
             "Status bab: `-` belum | `GAGAL` ada error validasi | `OK` lolos validasi", ""]
    total = {"soal": 0, "draft": 0}
    for key, book, conv, babs, status in _rows():
        lines.append(f"## {key} ({book.jenjang})")
        if not conv["siswa"] or not conv["guru"]:
            lines.append(f"- BELUM DIKONVERSI (siswa={conv['siswa']}, guru={conv['guru']}) -> "
                         f"`python -m app.services.pretest.agentic.convert --book {key}`")
            lines.append("")
            continue
        catatan = os.path.join(book.out_dir(), "CATATAN.md")
        if os.path.exists(catatan):
            lines.append(f"- catatan buku: `{rel(catatan)}` (BACA dulu)")
        lines.append("| bab | hal. siswa | status | soal | draft | review | dilewati |")
        lines.append("|---|---|---|---|---|---|---|")
        for b in babs:
            st = status.get(bab_filename(b["bab_no"]))
            if st:
                draft = st["status"].get("draft", 0)
                review = st["soal"] - draft
                total["soal"] += st["soal"]
                total["draft"] += draft
                mark = "OK" if st["valid"] else "GAGAL"
                cells = [mark, st["soal"], draft, review, st["dilewati"]]
            else:
                cells = ["-", "", "", "", ""]
            lines.append(f"| {b['bab']} | {b['start']}-{b['end']} | " + " | ".join(str(c) for c in cells) + " |")
        lines.append("")
    lines.append(f"**Total: {total['soal']} soal, {total['draft']} siap (draft)**")
    text = "\n".join(lines) + "\n"
    os.makedirs(OUT_ROOT, exist_ok=True)
    with open(os.path.join(OUT_ROOT, "PROGRESS.md"), "w", encoding="utf-8") as f:
        f.write(text)
    return text


def next_bab(only_book: Optional[str] = None) -> Optional[dict]:
    for key, book, conv, babs, status in _rows():
        if only_book and key != only_book:
            continue
        if not (conv["siswa"] and conv["guru"]):
            continue
        for b in babs:
            st = status.get(bab_filename(b["bab_no"]))
            if not st or not st["valid"]:
                return {"book": key, **b, "file": rel(os.path.join(book.out_dir(), bab_filename(b["bab_no"])))}
    return None


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", nargs="?", default="show", choices=["show", "next"])
    ap.add_argument("--book")
    a = ap.parse_args(argv)
    if a.cmd == "next":
        nb = next_bab(a.book)
        print(json.dumps(nb, ensure_ascii=False) if nb else "SEMUA BAB SELESAI")
        return 0
    print(write_progress())
    return 0


if __name__ == "__main__":
    sys.exit(main())
