"""Pembaca data acuan: soal pretest, dan soal exercise yang sudah ada (batch lain)."""

from __future__ import annotations

import glob
import json
import os
import re
from dataclasses import dataclass
from typing import Dict, List, Optional

from app.services.exercise.config import OUT_ROOT
from app.services.pretest.agentic.books import OUT_ROOT as PRETEST_ROOT

# 64.000.000 / 1.250,5 dibaca satu angka (titik ribuan), bukan "64.000" + "000"
_NUM_RE = re.compile(r"\d{1,3}(?:\.\d{3})+(?:,\d+)?|\d+(?:[.,]\d+)?")
_HTML_RE = re.compile(r"<!--.*?-->|</?(?:br|sup|sub|u|b|i|mark|span|em|strong|p|div)\b[^>]*>", re.S | re.I)


def numbers(text: str) -> List[str]:
    """Token angka dalam teks (urut muncul). 13.578 dan 13,578 dianggap token berbeda dari 13578."""
    return _NUM_RE.findall(_HTML_RE.sub(" ", text or ""))


def soal_text(stimulus: Optional[str], pertanyaan: str) -> str:
    return f"{stimulus.strip()}\n\n{pertanyaan.strip()}" if stimulus else pertanyaan.strip()


def norm_answer(text: str) -> str:
    return re.sub(r"[\s$]+", "", (text or "").lower()).replace(",", ".")


@dataclass
class Ref:
    id: str
    asal: str                  # "pretest" | "exercise:<path>"
    subbab: Optional[str]
    bab_no: int
    teks: str                  # stimulus + pertanyaan
    jawaban: str
    acuan_key: Optional[str] = None
    tipe: Optional[str] = None


def load_pretest(book: str) -> Dict[str, Ref]:
    out: Dict[str, Ref] = {}
    for path in sorted(glob.glob(os.path.join(PRETEST_ROOT, book, "bab[0-9][0-9].json"))):
        with open(path, encoding="utf-8") as f:
            d = json.load(f)
        for s in d.get("soal", []):
            out[s["id"]] = Ref(s["id"], "pretest", s.get("subbab"), d["bab_no"],
                               soal_text(s.get("stimulus"), s["pertanyaan"]), s["jawaban_benar"])
    return out


def acuan_key(acuan: dict) -> str:
    if acuan.get("sumber") == "pretest":
        return f"pretest:{acuan.get('id')}"
    return f"{acuan.get('sumber')}:{acuan.get('halaman')}:{acuan.get('nomor') or (acuan.get('teks') or acuan.get('kutipan') or '')[:40]}"


def load_exercise(book: str, bab_no: int, subbab: str, exclude: Optional[str] = None) -> List[Ref]:
    """Semua soal exercise untuk subbab ini di semua batch/level, kecuali file `exclude`."""
    out: List[Ref] = []
    pat = os.path.join(OUT_ROOT, book, "batch*", f"bab{bab_no:02d}", f"{subbab}_*.json")
    ex = os.path.abspath(exclude) if exclude else None
    for path in sorted(glob.glob(pat)):
        if ex and os.path.abspath(path) == ex:
            continue
        if path.endswith((".solver.json", ".verifikasi.json", ".blind.json")):
            continue
        try:
            with open(path, encoding="utf-8") as f:
                d = json.load(f)
        except (OSError, ValueError):
            continue
        for s in d.get("soal", []):
            out.append(Ref(s["id"], f"exercise:{os.path.basename(os.path.dirname(os.path.dirname(path)))}/{os.path.basename(path)}",
                           subbab, bab_no, soal_text(s.get("stimulus"), s["pertanyaan"]), s["jawaban_benar"],
                           acuan_key(s["acuan"]), s["tipe_generate"]))
    return out
