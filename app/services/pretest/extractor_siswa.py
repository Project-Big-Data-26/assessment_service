"""
extractor_siswa.py -- ekstraksi TEKS SOAL dari Buku Siswa (sumber SIBI),
dikelompokkan per section latihan, supaya bisa dipasangkan dengan kunci
jawaban dari Buku Panduan Guru oleh `soal_merger.py`.

KENAPA MODUL INI ADA:
  Untuk sebagian besar buku (terbukti di SMP Kelas 9, SD Kelas 5, SMA Kelas
  11, dst), section "Kunci Jawaban" di Buku Panduan Guru TIDAK mencetak ulang
  soalnya -- cuma "1. <jawaban>", "2. <jawaban>". Soal aslinya hanya ada di
  Buku Siswa. Modul ini mengambil soal itu apa adanya (verbatim), TANPA
  mengarang/menulis ulang apa pun.

SCOPE:
  - Hanya membaca teks Buku Siswa, per section latihan ("Ayo Berlatih",
    "Latihan 1.1", "Soal Laihan 2.3", "Latihan A ...", "Latihan Soal
    Lingkaran", "Uji Kompetensi", "Evaluasi", "ASESMEN", dst).
  - Tidak menyentuh MongoDB, tidak menyentuh LLM. Output = struktur data
    Python / JSON untuk soal_merger.py.

Penamaan label section memakai `normalize_activity_key` dari
extractor_text.py -- SENGAJA fungsi yang sama, supaya label Buku Guru dan
Buku Siswa dijamin dinormalisasi dengan aturan yang identik.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

from app.services.pretest.extractor_text import (
    BARE_ITEM_NO_RE,
    ITEM_START_RE,
    OTHER_SECTION_RE,
    _STRAY_BULLET_LINE_RE,
    normalize_activity_key,
)

# Heading section latihan di Buku Siswa. Mirip ACTIVITY_LABEL_RE di
# extractor_text.py, tapi "Asesmen/Evaluasi/Uji Kompetensi" dicek
# case-insensitive (SD Kelas 3 menulis "ASESMEN" huruf besar semua).
SISWA_HEADING_RE = re.compile(
    r"^(Ayo,?\s+[A-Z][a-z]+(\s+[A-Z][a-z]+)?|"
    r"(Soal\s+)?La\w*han\s+\d+(\.\d+)?|"
    # Judul sesudah huruf OPSIONAL: "Latihan A" bisa berdiri sendiri dengan
    # judul di baris berikutnya (varian hasil PyMuPDF).
    r"Latihan\s+[A-Z]((\s*[—\-–]\s*|\s+)\S.*)?|"
    r"Latihan\s+Soal\s+\S.*|"
    r"Soal\s+(Tambahan|Pengayaan)|"
    r"Eksplorasi\s+\d+(\.\d+)?)\s*\??\s*$"
)
SISWA_HEADING_CI_RE = re.compile(
    r"^(Asesmen|Evaluasi|Uji\s+Kompetensi(\s+Bab\s+\d+)?|Uji\s+Pemahaman|"
    r"LATIHAN\s+([A-H]|\d{1,2}\.\d{1,2})\b.*)\s*$",
    re.IGNORECASE,
)

# Varian SMP Kelas 9 (hasil konversi PDF): heading terpecah jadi beberapa
# baris -- "Latihan" / "B" / "Sistem Persamaan Linear Dua Variabel".
LATIHAN_BARE_RE = re.compile(r"^Latihan\s*$")
SINGLE_LETTER_RE = re.compile(r"^[A-H]\s*$")
LATIHAN_ID_LINE_RE = re.compile(r"^\d{1,2}\.\d{1,2}\s*$")
LETTER_TITLE_LINE_RE = re.compile(r"^[A-H](\s*[—\-–]\s*|\s+)[A-Z][a-z]")

# Penanda section latihan SUDAH SELESAI (selain heading latihan berikutnya).
SISWA_TERMINATOR_RE = re.compile(
    r"^(Tujuan Pembelajaran|Peta Konsep|Kata Kunci|Rangkuman|Refleksi|"
    r"Proyek(\s+.*)?|Pengayaan|Glosarium|Daftar Pustaka|Indeks|"
    r"Mari Mengomunikasikan|Mari Berkolaborasi|Contoh(\s+Soal)?(\s+\d+(\.\d+)?)?|"
    r"Pemetaan Pikiran|Bab|BAB|Asesmen Diri|Eksplorasi)\s*:?\s*$"
)

# Footer/header berulang -- dibuang, bukan isi soal.
#   "28 Matematika untuk SD/MI Kelas V"
#   "Matematika Tingkat Lanjut untuk SMA Kelas XI (Edisi Revisi)"
#   "Bab 1 | Matriks 37", "Bab 1 - Bilangan Cacah Sampai 100.000 9",
#   "Bab I - Sistem Persamaan Linear Dua Variabel"
SISWA_FOOTER_RE = re.compile(
    r"^(\d{1,3}\s+)?Matematika(\s+Tingkat\s+Lanjut)?\s+untuk\s+(SD|SMP|SMA)\S*.*$"
    r"|^(Panduan\s+Khusus\s+)?Bab\s+([0-9]+|[IVX]+)\s*[|\-–]\s*.+$"
    r"|^\d{1,3}\s+Bab\s+([0-9]+|[IVX]+)\s*[|\-–]\s*.+$"
)

# Varian SMP Kelas 9: nomor soal dirender dengan FONT IKON, sehingga hasil
# ekstraksinya jadi huruf besar tunggal ("B Di antara ...", "C Tentukan ...")
# dan penomorannya MULAI ULANG per sub-bagian (Pemahaman/Penerapan Konsep),
# sementara Buku Guru menomori terus 1, 2, 3, ... . Dipakai HANYA untuk
# section yang sama sekali tidak punya nomor digit; nomornya lalu diambil
# dari URUTAN kemunculan (ordinal), bukan dari hurufnya.
GLYPH_ITEM_RE = re.compile(r"^([B-Z])\s+(\S.*)$")

TOC_LINE_RE = re.compile(r"(\.\s?){5,}|…{3,}")

# Ditemukan oleh review independen: teks section BERIKUTNYA ikut menempel di
# ujung soal terakhir (mis. "B. Peluang Empiris", "Eksplorasi 9.3A ...").
# Judul subbab = huruf kapital + titik + minimal 2 kata alfabet (tanpa angka)
# -- sengaja tidak menangkap opsi pilihan ganda pendek seperti "A. 12" atau
# "B. Paket B". Kalau ada opsi PG yang kebetulan berbentuk judul, yang
# terjadi cuma soal sesudahnya tidak ikut diambil (aman: kosong, bukan salah).
SUBBAB_TITLE_RE = re.compile(r"^[A-H]\.\s+[A-Z][a-z]+(\s+[A-Za-z][a-z]+)+\s*$")
EKSPLORASI_ANY_RE = re.compile(r"^Eksplorasi\s+\d+(\.\d+)?[A-Z]?\b")


@dataclass
class SiswaSection:
    source_file: str
    label: str                                  # teks heading asli
    key: Tuple[str, Optional[str]]              # hasil normalize_activity_key
    line_index: int                             # posisi heading di dokumen
    bab: Optional[str] = None
    items: List[Tuple[str, str, int]] = field(default_factory=list)
    # items: (nomor, teks_soal_verbatim, line_index)
    numbering: str = "digit"                    # "digit" | "glyph_ordinal"
    page: Optional[int] = None                  # halaman PDF heading section
    # line_index item -> (halaman PDF, label bab) -- metadata Buku Siswa per soal
    item_meta: Dict[int, Tuple[Optional[int], Optional[str]]] = field(default_factory=dict)


def _is_heading(line: str) -> bool:
    return bool(SISWA_HEADING_RE.match(line) or SISWA_HEADING_CI_RE.match(line))


_BAB_FOOTER_RE = re.compile(
    r"^(?:\d{1,3}\s+)?(?:Panduan\s+Khusus\s+)?Bab\s+([0-9]+|[IVX]+)\s*[|\-–]\s*(.+?)(\s+\d{1,3})?$"
)


def _clean_lines(raw_text: str):
    """Return (lines, pages, babs): baris bersih + halaman PDF (dari pemisah
    halaman "\\f") + label bab berjalan (dari footer "Bab N | Judul") untuk
    tiap baris -- supaya setiap soal tahu halaman & bab asalnya di Buku Siswa."""
    out: List[str] = []
    pages: List[Optional[int]] = []
    babs: List[Optional[str]] = []
    last = None
    cur_bab: Optional[str] = None
    from app.services.pretest.extractor_text import _clean_line

    for page_no, page_text in enumerate(raw_text.split("\f"), start=1):
        for raw in page_text.splitlines():
            line = _clean_line(raw)
            if not line:
                out.append(""); pages.append(page_no); babs.append(cur_bab)
                continue
            m_bab = _BAB_FOOTER_RE.match(line)
            if m_bab:
                cur_bab = f"Bab {m_bab.group(1)} {m_bab.group(2).strip()}"
            if SISWA_FOOTER_RE.match(line) or _STRAY_BULLET_LINE_RE.match(line):
                continue
            # Baris daftar isi ("Latihan A—Persamaan Linear ........ 11") --
            # ditemukan nyata di SMP 9: tanpa ini, daftar isi ikut terbaca
            # sebagai section latihan berisi "soal" judul-judul subbab.
            if TOC_LINE_RE.search(line):
                continue
            if line == last:
                continue
            out.append(line); pages.append(page_no); babs.append(cur_bab)
            last = line
    return out, pages, babs


def _next_nonempty(lines: List[str], i: int, k: int = 1) -> List[Tuple[int, str]]:
    res = []
    j = i + 1
    while j < len(lines) and len(res) < k:
        if lines[j]:
            res.append((j, lines[j]))
        j += 1
    return res


def extract_sections(raw_text: str, source_file: str) -> List[SiswaSection]:
    """
    Pecah teks Buku Siswa jadi daftar section latihan (berurutan sesuai
    dokumen), masing-masing berisi soal bernomor verbatim.
    """
    lines, line_pages, line_babs = _clean_lines(raw_text)
    sections: List[SiswaSection] = []

    def new_section(label: str, key, i: int) -> SiswaSection:
        sec = SiswaSection(source_file, label, key, i)
        sec.page, sec.bab = line_pages[i], line_babs[i]
        return sec
    cur: Optional[SiswaSection] = None
    item_no: Optional[str] = None
    item_lines: List[str] = []
    item_line: Optional[int] = None
    glyph_mode = False
    glyph_count = 0
    skip_until = -1

    def flush_item():
        nonlocal item_no, item_lines, item_line
        if cur is not None and item_no is not None:
            text = "\n".join(l for l in item_lines if l).strip()
            if text:
                cur.items.append((item_no, text, item_line))
                if item_line is not None:
                    cur.item_meta[item_line] = (line_pages[item_line], line_babs[item_line])
        item_no, item_lines, item_line = None, [], None

    def close_section():
        nonlocal cur, glyph_mode, glyph_count
        flush_item()
        if cur is not None and cur.items:
            sections.append(cur)
        cur = None
        glyph_mode = False
        glyph_count = 0

    for i, line in enumerate(lines):
        if i <= skip_until:
            continue
        if not line:
            continue

        # Heading latihan terpecah:
        #   SMP 9 : "Latihan" / "B" / "Sistem Persamaan ..."
        #   SD 6  : "Latihan" / "1.1"
        if LATIHAN_BARE_RE.match(line):
            nxt = _next_nonempty(lines, i, 2)
            if nxt and LATIHAN_ID_LINE_RE.match(nxt[0][1]):
                close_section()
                lid = nxt[0][1].strip()
                cur = new_section(f"Latihan {lid}", ("latihan", lid), i)
                skip_until = nxt[0][0]
                continue
            # "Latihan" / "A Polinomial dan Fungsi Polinomial" (huruf + judul
            # di baris berikutnya)
            if nxt and LETTER_TITLE_LINE_RE.match(nxt[0][1]):
                close_section()
                letter = nxt[0][1].strip()[0]
                cur = new_section(f"Latihan {nxt[0][1].strip()}", ("latihan", letter), i)
                skip_until = nxt[0][0]
                continue
            if nxt and SINGLE_LETTER_RE.match(nxt[0][1]):
                close_section()
                letter = nxt[0][1].strip()
                title = nxt[1][1] if len(nxt) > 1 else ""
                label = f"Latihan {letter} {title}".strip()
                cur = new_section(label, ("latihan", letter), i)
                skip_until = nxt[1][0] if len(nxt) > 1 else nxt[0][0]
                continue

        if _is_heading(line):
            key = normalize_activity_key(line)
            # SD 6: "Latihan 1.1" langsung diikuti "Ayo Mencoba" -- itu sub-
            # label DI DALAM latihan (belum ada soal sama sekali), bukan
            # section baru. Kalau ditutup di sini, soal Latihan 1.1 hilang.
            if (
                cur is not None and not cur.items and item_no is None
                and cur.key[0] == "latihan" and cur.key[1] is not None
                and key is not None and key[0].startswith("ayo ")
            ):
                continue
            # Heading berulang dengan kunci sama sebelum ada soal (mis.
            # "Uji Kompetensi" lalu "Uji Pemahaman") = satu section.
            if cur is not None and not cur.items and item_no is None and key == cur.key:
                continue
            close_section()
            if key:
                cur = new_section(line, key, i)
            continue

        if cur is None:
            continue

        if (
            SISWA_TERMINATOR_RE.match(line)
            or OTHER_SECTION_RE.match(line)
            or SUBBAB_TITLE_RE.match(line)
            or EKSPLORASI_ANY_RE.match(line)
        ):
            close_section()
            continue

        m_item = ITEM_START_RE.match(line)
        m_bare = None if m_item else BARE_ITEM_NO_RE.match(line)
        if m_item or m_bare:
            no = (m_item or m_bare).group(1)
            # Nomor mundur ke 1 lagi di tengah section tanpa heading baru
            # = daftar bernomor lain (mis. contoh/aktivitas berikutnya yang
            # headingnya tidak terdeteksi). Section ini ditutup, JANGAN
            # disambung, supaya soal dari tempat lain tidak tercampur.
            # Nomor MUNDUR/ULANG (bukan cuma kembali ke 1) tanpa heading baru =
            # daftar bernomor lain, mis. judul subbab "2. Barisan Geometri"
            # sesudah soal no. 1-5 (ditemukan nyata di SMA 12). Section ditutup.
            last_no = cur.items[-1][0] if cur.items else item_no
            if last_no is not None and last_no.isdigit() and no.isdigit() and int(no) <= int(last_no) \
                    and (cur.items or item_no is not None):
                close_section()
                continue
            flush_item()
            item_no = no
            item_lines = [m_item.group(2)] if m_item else []
            item_line = i
            continue

        m_glyph = GLYPH_ITEM_RE.match(line)
        if m_glyph and (glyph_mode or (not cur.items and item_no is None)):
            flush_item()
            glyph_mode = True
            cur.numbering = "glyph_ordinal"
            glyph_count += 1
            item_no = str(glyph_count)
            item_lines = [m_glyph.group(2)]
            item_line = i
            continue

        if item_no is not None:
            item_lines.append(line)

    close_section()
    return sections


def sections_to_dicts(sections: List[SiswaSection]) -> List[dict]:
    return [
        {
            "source_file": s.source_file,
            "label": s.label,
            "key": list(s.key),
            "line_index": s.line_index,
            "numbering": s.numbering,
            "items": [
                {"no": no, "soal_text": txt, "line_index": li}
                for no, txt, li in s.items
            ],
        }
        for s in sections
    ]


def extract_pdf_sections(pdf_path: str) -> List[SiswaSection]:
    """PDF Buku Siswa -> section (pakai PyMuPDF, sama seperti extractor_text)."""
    import os

    import fitz  # PyMuPDF

    from app.services.pretest.extractor_text import _BARE_NUMBER_LINE_RE, _learn_printed_page_offset

    with fitz.open(pdf_path) as doc:
        pages = [(i + 1, page.get_text()) for i, page in enumerate(doc)]
    # Nomor halaman cetak yang berdiri sendiri (PyMuPDF memisahkannya dari
    # footer) dibuang supaya tidak menempel di ujung teks soal.
    offset = _learn_printed_page_offset(pages)
    parts = []
    for page_no, text in pages:
        if offset is not None:
            text = "\n".join(
                l for l in text.splitlines()
                if not (_BARE_NUMBER_LINE_RE.match(l.strip()) and int(l.strip()) == page_no + offset)
            )
        parts.append(text)
    return extract_sections("\f".join(parts), os.path.basename(pdf_path))
