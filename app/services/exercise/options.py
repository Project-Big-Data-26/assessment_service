"""Posisi opsi A-D diacak OLEH KODE (deterministik, sebaran jawaban benar seimbang),
bukan oleh agen -- LLM cenderung menaruh jawaban benar di posisi tertentu."""

from __future__ import annotations

import random
from typing import Dict, List, Tuple

OPTION_IDS = ["A", "B", "C", "D"]


def susun(data) -> Dict[str, Tuple[List[dict], str]]:
    """data: ExerciseFile. Return {soal_id: (options, correct_option_id)}."""
    rng = random.Random(f"opsi-v1-{data.book}-{data.bab_no}-{data.subbab}-{data.level}-{data.batch}")
    positions = [i % 4 for i in range(len(data.soal))]
    rng.shuffle(positions)
    out: Dict[str, Tuple[List[dict], str]] = {}
    for s, pos in zip(data.soal, positions):
        distr = [{"text": d.teks, "alasan": f"Salah: {d.alasan}"} for d in s.distraktor]
        rng.shuffle(distr)
        benar = {"text": s.jawaban_benar, "alasan": f"Benar: {s.alasan_benar}"}
        urut = distr[:pos] + [benar] + distr[pos:]
        out[s.id] = ([{"option_id": o, **x} for o, x in zip(OPTION_IDS, urut)], OPTION_IDS[pos])
    return out
