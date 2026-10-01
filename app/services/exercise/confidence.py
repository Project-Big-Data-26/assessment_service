"""confidence_score (int 0-100) dihitung KODE dari bukti, bukan ditebak LLM.

  50  penyelesai independen memilih jawaban yang sama dengan kunci
  10  jumlah langkah penyelesai == jumlah_langkah agen (6 kalau selisih 1)
  15  variasi (acuan terverifikasi) | 10 orisinal (grounded di kutipan buku)
  15  keunikan: 1 - kemiripan tertinggi dengan soal lain (>=0.30 penuh)
  10  tidak ada warning validator untuk soal ini
"""

from __future__ import annotations

from typing import List, Optional


def hitung(s, verif: Optional[dict], jarak: float, warns: List[str]) -> int:
    skor = 0.0
    if verif:
        if verif.get("cocok"):
            skor += 50
        ls, la = verif.get("langkah_solver"), verif.get("langkah_agen")
        if isinstance(ls, int) and isinstance(la, int):
            selisih = abs(ls - la)
            skor += 10 if selisih == 0 else 6 if selisih == 1 else 0
    skor += 15 if s.tipe_generate == "variasi" else 10
    skor += 15 * min(1.0, max(0.0, jarak) / 0.30)
    if not any(s.id in w for w in warns):
        skor += 10
    return int(round(skor))
