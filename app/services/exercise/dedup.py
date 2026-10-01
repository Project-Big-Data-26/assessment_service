"""Deteksi soal kembar: terhadap soal pretest, batch lain, dan sesama soal dalam file."""

from __future__ import annotations

from difflib import SequenceMatcher
from typing import List, Tuple

from app.services.exercise import config as C
from app.services.exercise.refs import Ref, numbers, soal_text
from app.services.pretest.agentic.validate import tokens


def sim(a: str, b: str) -> float:
    ta, tb = tokens(a), tokens(b)
    if not ta or not tb:
        return 0.0
    return SequenceMatcher(None, ta, tb, autojunk=False).ratio()


def cek_kembar(soal: list, pool: List[Ref]) -> Tuple[List[str], List[str]]:
    """soal: daftar objek Soal. Return (errors, warnings)."""
    errors: List[str] = []
    warns: List[str] = []
    from app.services.exercise.refs import acuan_key

    items = [(s.id, soal_text(s.stimulus, s.pertanyaan) + " " + s.jawaban_benar,
              acuan_key(s.acuan.model_dump()), s.tipe_generate) for s in soal]

    for i, (sid, txt, ak, _t) in enumerate(items):
        for j in range(i + 1, len(items)):
            oid, otxt, oak, _ot = items[j]
            r = sim(txt, otxt)
            if r >= C.SIM_DUPLIKAT and numbers(txt) == numbers(otxt):
                errors.append(f"{sid} kembar dengan {oid} (kemiripan {r:.2f})")
            elif r >= C.SIM_MIRIP and ak != oak:
                warns.append(f"{sid} sangat mirip dengan {oid} ({r:.2f}) padahal acuan beda")
        for ref in pool:
            r = sim(txt, ref.teks + " " + ref.jawaban)
            if r >= C.SIM_DUPLIKAT and numbers(txt) == numbers(ref.teks + " " + ref.jawaban):
                errors.append(f"{sid} kembar dengan {ref.id} [{ref.asal}] (kemiripan {r:.2f})")
            elif r >= C.SIM_MIRIP and ak != ref.acuan_key and ref.asal != "pretest":
                warns.append(f"{sid} sangat mirip dengan {ref.id} [{ref.asal}] ({r:.2f})")
    return errors, warns


def jarak_terdekat(s, pool: List[Ref], sesama: list) -> float:
    """1 - kemiripan tertinggi terhadap pool + soal lain (0 = kembar, 1 = unik). Untuk confidence."""
    txt = soal_text(s.stimulus, s.pertanyaan) + " " + s.jawaban_benar
    best = 0.0
    for ref in pool:
        best = max(best, sim(txt, ref.teks + " " + ref.jawaban))
    for o in sesama:
        if o.id != s.id:
            best = max(best, sim(txt, soal_text(o.stimulus, o.pertanyaan) + " " + o.jawaban_benar))
    return 1.0 - best
