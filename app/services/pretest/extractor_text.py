from __future__ import annotations

import fitz
import json
import re
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

BAB_HEADING_RE = re.compile(r"^Bab\s+(\d+)\s+([A-Za-z].{2,60})$")
SUBBAB_HEADING_RE = re.compile(r"^([A-Z])\.\s+([A-Za-z].{2,80})$")
ANSWER_SECTION_RE = re.compile(
    r"^(Kunci\s+)?[Jj]awaban\s+(Latihan|Uji\s+Kompetensi|Eksplorasi)"
    r"(\s+(Bab\s+)?\d+(\.\d+)?)?(\s*\(No\.[^)]*\))?\s*$"
)

LETTERED_KUNCI_JAWABAN_RE = re.compile(r"^[A-Z]\.\s+Kunci\s+Jawaban\s*$")

PLAIN_KUNCI_JAWABAN_RE = re.compile(r"^Kunci\s+Jawaban\s*$")

JAWABAN_SOAL_LATIHAN_RE = re.compile(
    r"^(Alterna\w*f\s+)?[Jj]awaban\s+[Ss]oal\s+La\w*han\s*$"
)

ASESMEN_KUNCI_JAWABAN_RE = re.compile(
    r"^ASESMEN\s*\(\s*KUNCI\s+JAWABAN\s*\)\s*$", re.IGNORECASE
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

BARE_ITEM_NO_RE = re.compile(r"^(\d{1,2})\.\s*$")

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
class RawSoalBlock:
    """Satu kandidat soal hasil parsing, sebelum/ sesudah difilter."""

    source_file: str
    source_page: Optional[int]
    source_section: str
    source_bab: Optional[str]
    source_subbab: Optional[str]
    source_item_no: str
    raw_text: str
    flags: List[str] = field(default_factory=list)
    status: str = "draft"
    extraction_confidence: float = 1.0

    def to_dict(self) -> dict:
        return {
            "source_file": self.source_file,
            "source_page": self.source_page,
            "source_section": self.source_section,
            "source_bab": self.source_bab,
            "source_subbab": self.source_subbab,
            "source_item_no": self.source_item_no,
            "pertanyaan_text": self.raw_text,
            "pertanyaan_type": "pilihan_ganda",
            "correct_answer": None,
            "options": [],
            "image_url": None,
            "image_urls": [],
            "extraction_flags": self.flags,
            "status": self.status,
            "extraction_confidence": self.extraction_confidence,
        }


def _clean_line(line: str) -> str:
    return line.strip()


def attach_page_numbers(
    pages_text: List[Tuple[int, str]]
) -> List[Tuple[str, int, Optional[str]]]:
    result: List[Tuple[str, int, Optional[str]]] = []
    for page_no, page_text in pages_text:
        for raw_line in page_text.splitlines():
            result.append((_clean_line(raw_line), page_no, None))
    return result


def attach_page_numbers_from_footers(
    raw_text: str,
) -> List[Tuple[str, int, Optional[str]]]:
    result = []
    current_page = 1
    current_bab_label: Optional[str] = None
    for raw_line in raw_text.splitlines():
        line = _clean_line(raw_line)
        m_left = PAGE_FOOTER_LEFT_RE.match(line)
        m_right = PAGE_FOOTER_RIGHT_RE.match(line)
        if m_left:
            current_page = int(m_left.group(1))
            continue
        if m_right:
            current_page = int(m_right.group(3))
            current_bab_label = f"Bab {m_right.group(1)} {m_right.group(2)}".strip()
            continue
        result.append((line, current_page, current_bab_label))
    return result


def attach_page_numbers_with_bab_tracking(
    pages_text: List[Tuple[int, str]]
) -> List[Tuple[str, int, Optional[str]]]:
    result: List[Tuple[str, int, Optional[str]]] = []
    current_bab_label: Optional[str] = None
    for page_no, page_text in pages_text:
        for raw_line in page_text.splitlines():
            line = _clean_line(raw_line)
            if PAGE_FOOTER_LEFT_RE.match(line):
                continue
            m_right = PAGE_FOOTER_RIGHT_RE.match(line)
            if m_right:
                current_bab_label = f"Bab {m_right.group(1)} {m_right.group(2)}".strip()
                continue
            result.append((line, page_no, current_bab_label))
    return result


def run_extraction_from_pages_with_bab_tracking(
    pages_text: List[Tuple[int, str]], source_file: str
) -> List[RawSoalBlock]:
    lines_with_page = attach_page_numbers_with_bab_tracking(pages_text)
    blocks = extract_candidate_blocks(lines_with_page, source_file)
    return [apply_filters(b) for b in blocks]


def _looks_garbled(text: str) -> bool:
    lines = [l for l in text.splitlines() if l.strip()]
    if not lines:
        return False
    symbol_lines = sum(1 for l in lines if SYMBOL_ONLY_LINE_RE.match(l.strip()))
    return len(lines) >= 4 and (symbol_lines / len(lines)) >= 0.25


def extract_candidate_blocks(
    lines_with_page: List[Tuple[str, int, Optional[str]]], source_file: str
) -> List[RawSoalBlock]:
    blocks: List[RawSoalBlock] = []

    current_bab: Optional[str] = None
    current_subbab: Optional[str] = None
    current_section: Optional[str] = None
    in_answer_section = False

    item_no: Optional[str] = None
    item_lines: List[str] = []
    item_start_page: Optional[int] = None

    def flush_item():
        nonlocal item_no, item_lines, item_start_page
        if in_answer_section and item_no is not None and item_lines:
            blocks.append(
                RawSoalBlock(
                    source_file=source_file,
                    source_page=item_start_page,
                    source_section=current_section or "",
                    source_bab=current_bab,
                    source_subbab=current_subbab,
                    source_item_no=item_no,
                    raw_text="\n".join(item_lines).strip(),
                )
            )
        item_no = None
        item_lines = []
        item_start_page = None

    for line, page_no, bab_label in lines_with_page:
        if bab_label and bab_label != current_bab:
            flush_item()
            in_answer_section = False
            current_section = None
            current_bab = bab_label
            current_subbab = None

        if not line:
            continue

        bab_match = BAB_HEADING_RE.match(line)
        if bab_match and current_bab is None:
            flush_item()
            in_answer_section = False
            current_section = None
            current_bab = f"Bab {bab_match.group(1)} {bab_match.group(2)}".strip()
            current_subbab = None
            continue

        if LETTERED_KUNCI_JAWABAN_RE.match(line):
            flush_item()
            current_section = line
            in_answer_section = True
            continue

        subbab_match = SUBBAB_HEADING_RE.match(line)
        if subbab_match:
            flush_item()
            in_answer_section = False
            current_section = None
            current_subbab = f"{subbab_match.group(1)}. {subbab_match.group(2)}".strip()
            continue

        if (
            ANSWER_SECTION_RE.match(line)
            or PLAIN_KUNCI_JAWABAN_RE.match(line)
            or JAWABAN_SOAL_LATIHAN_RE.match(line)
            or ASESMEN_KUNCI_JAWABAN_RE.match(line)
        ):
            flush_item()
            current_section = line
            in_answer_section = True
            continue

        if OTHER_SECTION_RE.match(line):
            flush_item()
            in_answer_section = False
            current_section = None
            continue

        if in_answer_section:
            item_match = ITEM_START_RE.match(line)
            bare_match = None if item_match else BARE_ITEM_NO_RE.match(line)
            if item_match:
                flush_item()
                item_no = item_match.group(1)
                item_lines = [line]
                item_start_page = page_no
            elif bare_match and not (
                current_section and "eksplorasi" in current_section.lower()
            ):
                flush_item()
                item_no = bare_match.group(1)
                item_lines = []
                item_start_page = page_no
            elif item_no is not None:
                item_lines.append(line)
    flush_item()
    return blocks


def apply_filters(block: RawSoalBlock) -> RawSoalBlock:
    text = block.raw_text

    if OPEN_ENDED_RE.search(text):
        block.status = "skipped_open_ended"
        block.flags.append("open_ended")

    if PEMBUKTIAN_RE.search(text):
        block.flags.append("pembuktian")
        if block.status == "draft":
            block.status = "skipped_pembuktian"

    if NEEDS_IMAGE_RE.search(text):
        block.flags.append("needs_image")
        if block.status == "draft":
            block.status = "needs_image"

    if _looks_garbled(text):
        block.flags.append("possible_formula_garbling")
        block.extraction_confidence = min(block.extraction_confidence, 0.4)
        if block.status == "draft":
            block.status = "needs_review_extraction"

    return block


def run_extraction(raw_text: str, source_file: str) -> List[RawSoalBlock]:
    lines_with_page = attach_page_numbers_from_footers(raw_text)
    blocks = extract_candidate_blocks(lines_with_page, source_file)
    return [apply_filters(b) for b in blocks]


def run_extraction_from_pages(
    pages_text: List[Tuple[int, str]], source_file: str
) -> List[RawSoalBlock]:
    lines_with_page = attach_page_numbers(pages_text)
    blocks = extract_candidate_blocks(lines_with_page, source_file)
    return [apply_filters(b) for b in blocks]


def summarize(blocks: List[RawSoalBlock]) -> dict:
    summary: dict = {}
    for b in blocks:
        summary[b.status] = summary.get(b.status, 0) + 1
    summary["_total"] = len(blocks)
    return summary

def export_to_json(blocks: List[RawSoalBlock], output_path: str) -> None:

    payload = {
        "summary": summarize(blocks),
        "items": [b.to_dict() for b in blocks],
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)


def extract_pdf_to_json(pdf_path: str, output_path: str) -> dict:

    source_file = _os_basename(pdf_path)
    pages_text = []
    with fitz.open(pdf_path) as doc:
        for i, page in enumerate(doc):
            pages_text.append((i + 1, page.get_text()))

    blocks = run_extraction_from_pages_with_bab_tracking(pages_text, source_file)
    export_to_json(blocks, output_path)
    return summarize(blocks)


def _os_basename(path: str) -> str:
    import os

    return os.path.basename(path)


def _cli():
    import argparse

    parser = argparse.ArgumentParser(
        description="Ekstraksi teks soal pretest dari PDF Buku Panduan Guru -> JSON "
        "(tidak menyentuh MongoDB -- output ini diserahkan ke tahap/tim berikutnya)."
    )
    parser.add_argument("--pdf", required=True, help="Path ke file PDF buku panduan guru")
    parser.add_argument(
        "--out",
        required=True,
        help="Path file JSON output, misal output/kelas11_bab1_3.json",
    )
    args = parser.parse_args()

    stats = extract_pdf_to_json(args.pdf, args.out)
    print(f"Selesai. Ringkasan status:")
    for status, count in stats.items():
        print(f"  {status}: {count}")
    print(f"\nOutput tersimpan di: {args.out}")


if __name__ == "__main__":
    _cli()
