"""Parameter bank soal latihan -- satu tempat, supaya mudah disetel."""

from __future__ import annotations

import os

from app.services.pretest.agentic.books import ROOT

OUT_ROOT = os.path.join(ROOT, "output", "exercise")

LEVELS = ("easy", "medium", "hard")

# Soal per LEVEL per subbab per batch (= ukuran sesi latihan; bank per batch = 3x).
# SD: sesi 10 -> bank 30 | SMP: sesi 15 -> bank 45 | SMA: sesi 20 -> bank 60
KUOTA_PER_LEVEL = {"SD": 10, "SMP": 15, "SMA": 20}

# Level -> tingkat kognitif yang boleh (C1-C6) dan rentang langkah pengerjaan.
# C1-C2 easy, C3-C4 medium, C5-C6 hard (sesuai tabel mendapatkan_difficulty).
LEVEL_SPEC = {
    "easy":   {"c": ("C1", "C2"), "langkah": (1, 2), "score": 600},
    "medium": {"c": ("C3", "C4"), "langkah": (2, 4), "score": 1000},
    "hard":   {"c": ("C5", "C6"), "langkah": (3, 8), "score": 1400},
}

# Porsi tipe "variasi" (meniru soal acuan, angka/konteks beda) dalam satu level.
# Sisanya "orisinal". Toleransi dalam jumlah soal.
PORSI_VARIASI = {"easy": 0.6, "medium": 0.5, "hard": 0.3}
TOLERANSI_PORSI = 2

MAKS_JENIS_PER_LEVEL = 1 / 3           # satu jenis_soal maks sepertiga kuota level
MAKS_VARIASI_PER_ACUAN = 2          # satu soal acuan maksimal dipakai N kali per level
VARIASI_ANGKA_MAKS_SAMA = 0.5       # maks. porsi angka soal baru yang sama dengan acuan
VARIASI_KONTEKS_MAKS_MIRIP = 0.6    # maks. kemiripan kata (SequenceMatcher) untuk variasi konteks
SIM_DUPLIKAT = 0.97                 # >= ini = soal kembar (ERROR)
SIM_MIRIP = 0.85                    # >= ini dan acuan beda = WARNING

CONFIDENCE_SAMPLING_BATAS = 80      # soal di bawah ini WAJIB dikoreksi manusia
SAMPLING_ACAK_PERSEN = 0.10         # + sebagian kecil acak dari yang di atas batas
PIPELINE_VERSION = "exercise-2026-10-01"
SKILL_VERSI = "v1"                  # versi .claude/skills/generate-soal-exercise/SKILL.md
