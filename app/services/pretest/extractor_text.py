from __future__ import annotations
import re
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

BAB_HEADING_RE = re.compile(r"^BAB\s++(\d+)\s+([A-Za-z].{2,60})$")
SUBBAB_HEADING_RE = re.compile(r"^([A-F])\.\s+([A-Za-z].{2,80})$")

ANSWER_SECTION_RE = re.compile(
    r"^(Kunci\s+)?[Jj]awaban\s+(Latihan|Uji\s+Kompetensi|Eksplorasi)"
    r"(\s+\d+(\.\d+)?)?(\s*\(No\.[^)]*\))?\s*$"
)

OTHER_SECTION_RE = re.compile(
    r"^(Eksplorasi\s+[\d.]+|Rangkuman|Refleksi|Pengayaan|"
    r"Peta Konsep|Gambaran Umum Bab|Skema Pembelajaran|"
    r"Panduan Pembelajaran|Metode\s*&?\s*Aktivitas Pembelajaran|"
    r"Diferensiasi|Apersepsi|Sarana\s*&\s*Prasarana Pembelajaran|"
    r"Pengalaman Belajar)\s*$"
)

PAGE_FOOTER_LEFT_RE = re.compile(
    r"^(\d{1,3})\s+Buku Panduan Guru Matematika untuk SMA/SMK Kelas XI\s*$"
)
PAGE_FOOTER_RIGHT_RE = re.compile(r"^Bab\s+(\d+)\s*\|\s*(.+?)\s+(\d{1,3})\s*$")

ITEM_START_RE = re.compile(r"^(\d{1,2})\.\s+(\S.*)$")

OPEN_ENDED_PATTERNS = [
    r"jawaban (bisa|dapat)?\s*bervariasi",
    r"jawaban masing[- ]masing siswa",
    r"kebijakan guru",
    r"sesuai kreativitas siswa",
    r"pendapat (bisa|dapat) disampaikan secara bervariasi",
    r"jawaban (siswa )?berbeda[- ]beda",
    r"disesuaikan dengan jawaban siswa",
]
OPEN_ENDED_RE = re.compile("|".join(OPEN_ENDED_PATTERNS), re.IGNORECASE)

PEMBUKTIAN_RE = re.compile(r"\bbuktikan\b|\bpembuktian\b", re.IGNORECASE)

NEEDS_IMAGE_PATTERNS = [
    r"perhatikan gambar", r"\bgambar(kan)?\b", r"\bdiagram\b", r"\bgrafik\b",
    r"sketsa(kan)?", r"lihat (grafik|gambar)", r"pada (lingkaran|segitiga|"
    r"gambar) berikut",
]
NEEDS_IMAGE_RE = re.compile("|".join(NEEDS_IMAGE_PATTERNS), re.IGNORECASE)

SYMBOL_ONLY_LINE_RE = re.compile(r"^[^\w]{0,2}[\d\W]{1,4}[^\w]{0,2}$")

@dataclass
class RawQuestionBlock:
    source_file: str
    source_page: Optional[int]
    source_section: str
    source_bab: Optional[str]
    source_subbab: Optional[str]
    source_item_no: str
    raw_text: str
    flags: List[str] = field(default_factory=list)
    status: str = "draft"
    extraction_confidence: float = 0.0

    def to_dict(self) -> dict:
        return {
            "source_file": self.source_file,
            "source_page": self.source_page,
            "source_section": self.source_section,
            "source_bab": self.source_bab,
            "source_subbab": self.source_subbab,
            "source_item_no": self.source_item_no,
            "pertanyaan_text": self.raw_text,
            "correct_answer": None,
            "options": [],
            "image_url": None,
            "flags": self.flags,
            "status": self.status,
            "extraction_confidence": self.extraction_confidence,
        }

    