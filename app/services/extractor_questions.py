from __future__ import annotations
import re
from dataclasses import dataclass
from typing import List, Optional

bab_heading_re = re.compile(r"^Bab\s+(\d+)\s+([A-Za-z].{2,60})$")
bab_subheading_re = re.compile(r"^([A-F])\.\s+([A-Za-z].{2,80})$")

answer_section_re = re.compile(
    r"^(Kunci\s+)?[Jj]awaban\s+(Latihan|Uji\s+Kompetensi|Eksplorasi)"
    r"(\s+\d+(\.\d+)?)?(\s*\(No\.[^)]*\))?\s*$"
)

other_section_re = re.compile(
    r"^(Eksplorasi\s+[\d.]+|Rangkuman|Refleksi|Pengayaan|"
    r"Peta Konsep|Gambaran Umum Bab|Skema Pembelajaran|"
    r"Panduan Pembelajaran|Metode\s*&?\s*Aktivitas Pembelajaran|"
    r"Diferensiasi|Apersepsi|Sarana\s*&\s*Prasarana Pembelajaran|"
    r"Pengalaman Belajar)\s*$"
)

