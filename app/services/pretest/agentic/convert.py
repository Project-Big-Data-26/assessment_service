"""
convert.py -- PDF Buku Siswa/Guru -> Markdown PER HALAMAN + indeks, supaya
AI agent bisa membaca buku dengan hemat token.

KENAPA PER HALAMAN (bukan satu .md besar per buku):
  Satu buku = 200-440 halaman (~150 ribu token). Agen cukup membuka halaman
  yang relevan (lewat INDEX.md atau Grep), jadi konteksnya tetap kecil.

HASIL (data/processed/pretest_md/<buku>/<siswa|guru>/):
  p0023.md     teks halaman (tabel sudah jadi tabel Markdown, gambar jadi
               link ![](img/...)), diawali satu baris komentar metadata
  img/         gambar yang tertanam di halaman (untuk soal bergambar)
  png/         render halaman utuh -- DIBUAT SAAT DIMINTA (`render`), untuk
               halaman yang notasi matematikanya rusak di Markdown
  index.json   metadata semua halaman (bab, heading, penanda risiko)
  INDEX.md     ringkasan yang dibaca agen PERTAMA KALI (per bab: rentang
               halaman, heading latihan/kunci, penanda [M]/[G])

PENANDA RISIKO [M] (notasi matematika kemungkinan rusak):
  Teks PDF tidak menyimpan struktur rumus: pecahan bersusun jadi "1<sup>1</sup>
  2", garis pecahan hilang, simbol font khusus jadi karakter acak. Halaman
  dengan tanda-tanda ini WAJIB dicek agen lewat render PNG sebelum soalnya
  disalin (notasi lalu ditulis ulang dalam LaTeX).

Cara pakai (dari root project, venv aktif):
  python -m app.services.pretest.agentic.convert --all            # semua buku
  python -m app.services.pretest.agentic.convert --book kelas5    # satu buku
  python -m app.services.pretest.agentic.convert render kelas5 siswa 118
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from typing import Dict, List, Optional

from app.services.pretest.agentic.books import Book, discover, get_book, page_md_path, rel

CHUNK_PAGES = 20

_ROMAN = {"I": 1, "V": 5, "X": 10}

# Footer/heading bab. Contoh nyata:
#   "Bab 1 - Bilangan Cacah Sampai 100.000"      (SD 5, Siswa)
#   "Bab 1 | Barisan dan Deret 11"               (SMA 12, Siswa)
#   "Panduan Khusus Bab 1 | Barisan dan Deret"   (Buku Guru)
#   "Bab 1 Pecahan dan Desimal"                  (SD 6 -- tanpa pemisah, judul huruf besar)
#   "Panduan Khusus | Bab 1 Matriks"             (Guru SMA 11 peminatan)
# Sengaja TANPA re.I: "Bab 4 ini ..." (kalimat biasa) tidak boleh cocok.
BAB_LINE_RE = re.compile(
    r"^(?:\d{1,3}\s+)?(?:Panduan\s+Khusus\s*\|?\s*)?(?:Bab|BAB)\s+(\d{1,2}|[IVX]{1,5})"
    r"(?:\s*[|\-–—:.]\s*|\s+(?=[A-Z]))(.+?)(?:\s+\d{1,3})?\s*$"
)
BAB_ONLY_RE = re.compile(r"^Bab\s+(\d{1,2}|[IVX]{1,5})\s*$", re.I)
# Judul yang bukan nama bab (halaman pembuka SMP 9, bagian "Panduan Umum" Guru SMA 10)
GENERIC_TITLE_RE = re.compile(
    r"^(tujuan pembelajaran|panduan( umum| khusus)?|peta konsep|kata kunci|pendahuluan|pengantar)$", re.I
)
# Footer tanpa kata "Bab" (SD kelas 1-2): "1 Ayo Membilang sampai dengan 10    3"
# = nomor bab, judul, SPASI LEBAR, nomor halaman.
BAB_RUNNING_RE = re.compile(r"^(\d{1,2})\s+([A-Z][^|.:]{3,70}?)\s{2,}(\d{1,3})$")

EXERCISE_RE = re.compile(
    r"^(\d{1,2}\.\s*|[A-H]\.\s*)?("
    r"ayo,?\s+(berlatih|mencoba|berpikir|mengerjakan|menalar|menyelesaikan|mengasah)|"
    r"mari\s+(berlatih|mencoba)|(soal\s+)?la\w{0,3}han\b|uji\s+(kompetensi|pemahaman)|"
    r"evaluasi|asesmen|soal\s+(tambahan|pengayaan)|pengayaan|kerjakan\b)",
    re.I,
)
KUNCI_RE = re.compile(
    r"kunci\s+jawaban|alternatif\s+(jawaban|penyelesaian)|pembahasan\s+(soal|latihan|uji)|"
    r"jawaban\s+(latihan|uji\s+kompetensi|soal|asesmen|evaluasi)",
    re.I,
)
PRIVATE_USE_RE = re.compile(r"[-]")
TOC_RE = re.compile(r"(\.\s?){4,}|…{2,}")
FIG_CAPTION_RE = re.compile(r"\b(Gambar|Grafik|Diagram)\s+\d+(\.\d+)?", re.I)
IMG_LINK_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
BOLD_LINE_RE = re.compile(r"^\*\*(.{3,90}?)\*\*\s*$")


def _roman_to_int(s: str) -> int:
    if s.isdigit():
        return int(s)
    total, prev = 0, 0
    for ch in reversed(s.upper()):
        v = _ROMAN[ch]
        total = total - v if v < prev else total + v
        prev = max(prev, v)
    return total


def _clean_md_inline(s: str) -> str:
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("**", "").replace("__", "").replace("_", " ")
    return re.sub(r"\s+", " ", s).strip(" #")


def _headings(md: str) -> List[str]:
    out = []
    for line in md.splitlines():
        m = HEADING_RE.match(line.strip()) or BOLD_LINE_RE.match(line.strip())
        if m:
            text = _clean_md_inline(m.group(m.lastindex))
            if 2 < len(text) <= 90 and text not in out:
                out.append(text)
    return out


_NUMERIC_WORD_RE = re.compile(r"^[\d…a-zA-Z()+\-−.,]{1,6}$")


def _fraction_bars(page) -> int:
    """Hitung pecahan bersusun: garis horizontal pendek (3-45pt) yang punya
    token angka/variabel TEPAT di atas DAN di bawahnya. Garis dekorasi
    (bingkai halaman, garis tabel) tidak memenuhi syarat ini."""
    bars = []
    try:
        for path in page.get_drawings():
            for item in path.get("items", []):
                if item[0] == "l":
                    p1, p2 = item[1], item[2]
                    if abs(p1.y - p2.y) < 0.6 and 3 < abs(p1.x - p2.x) < 45:
                        bars.append((min(p1.x, p2.x), max(p1.x, p2.x), p1.y))
                elif item[0] == "re":
                    r = item[1]
                    if r.height < 1.3 and 3 < r.width < 45:
                        bars.append((r.x0, r.x1, (r.y0 + r.y1) / 2))
        if not bars:
            return 0
        words = [w for w in page.get_text("words") if _NUMERIC_WORD_RE.match(w[4])]
    except Exception:  # PDF rusak -- bukan fatal, cukup tidak ditandai
        return 0
    n = 0
    for x0, x1, y in bars:
        above = below = False
        for wx0, wy0, wx1, wy1, *_ in words:
            cx = (wx0 + wx1) / 2
            if not (x0 - 2 <= cx <= x1 + 2):
                continue
            if 0 <= y - wy1 <= 6:
                above = True
            elif 0 <= wy0 - y <= 6:
                below = True
        n += above and below
    return n


def _math_risk(md: str, raw_text: str, bars: int) -> List[str]:
    reasons = []
    if "<sup>" in md or "<sub>" in md:
        reasons.append("sup/sub")
    if PRIVATE_USE_RE.search(raw_text):
        reasons.append("glyph_font_khusus")
    if bars:
        reasons.append(f"pecahan_bersusun~{bars}")
    return reasons


def _detect_bab(raw_text: str, headings: List[str]):
    # baris daftar isi ("Bab 7 - Bangun Datar ........ 201") bukan penanda bab halaman ini
    lines = [l.strip() for l in raw_text.splitlines() if l.strip() and not TOC_RE.search(l)]
    # urutan prioritas: footer lengkap "Bab N | Judul" > footer tanpa "Bab" > "Bab N" + baris judul
    for l in lines:
        m = BAB_LINE_RE.match(l)
        title = m.group(2).strip(" |") if m else ""
        if m and len(title) >= 3 and not GENERIC_TITLE_RE.match(title):
            return _roman_to_int(m.group(1)), title
    for l in lines:
        m = BAB_RUNNING_RE.match(l)
        if m and len(m.group(2).strip()) >= 5:  # "Pecahan" (SD 2) cukup satu kata
            return int(m.group(1)), m.group(2).strip()
    # >= 2 nomor bab berbeda berdiri sendiri = daftar isi/peta konsep, bukan pembuka bab (SMA 12)
    if len({BAB_ONLY_RE.match(l).group(1) for l in lines if BAB_ONLY_RE.match(l)}) >= 2:
        return None
    for i, l in enumerate(lines):
        m = BAB_ONLY_RE.match(l)
        # "Bab 1" langsung diikuti "Bab 2" = daftar, bukan judul bab (Guru kelas 3)
        if m and i + 1 < len(lines) and len(lines[i + 1]) > 3 and not re.match(r"(?i)bab\s", lines[i + 1]):
            title = "" if GENERIC_TITLE_RE.match(lines[i + 1]) else lines[i + 1]
            # di puncak halaman = halaman pembuka bab (cukup muncul sekali, SMP 9)
            return _roman_to_int(m.group(1)), title, ("pembuka" if i <= 2 else "")
    for h in headings:
        m = BAB_LINE_RE.match(h)
        if m:
            return _roman_to_int(m.group(1)), m.group(2).strip()
    return None


PICTURE_TEXT_RE = re.compile(r"<!-- Start of picture text -->(.*?)<!-- End of picture text -->", re.S)


def _picture_text_chars(md: str) -> int:
    """Banyak teks yang tercetak DI DALAM gambar (soal/tabel/kunci yang
    didesain sebagai grafik). Urutan & pasangannya sering kacau di Markdown
    (contoh nyata: kunci menjodohkan yang garisnya hanya ada di gambar)."""
    return sum(len(re.sub(r"<br>|\s|\d{1,3}(?=<br>|$)", "", m)) for m in PICTURE_TEXT_RE.findall(md))


def _page_meta(md: str, page) -> dict:
    raw = page.get_text()
    heads = _headings(md)
    bab = _detect_bab(raw, heads)
    return {
        "bab_detected": list(bab) if bab else None,
        "headings": heads,
        "latihan": [h for h in heads if EXERCISE_RE.match(h)],
        "kunci": bool(KUNCI_RE.search(raw)),
        "risiko_matematika": _math_risk(md, raw, _fraction_bars(page)),
        "teks_dalam_gambar": _picture_text_chars(md) >= 40,
        "gambar": len(IMG_LINK_RE.findall(md)),
        "caption_gambar": sorted(set(m.group(0) for m in FIG_CAPTION_RE.finditer(raw)))[:6],
        "chars": len(md),
    }


def _read_page_body(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        text = f.read()
    return text.split("-->", 1)[-1].lstrip("\n") if text.startswith("<!--") else text


def refresh_meta(book: Book, kind: str) -> dict:
    """Hitung ulang metadata dari .md yang sudah ada (tanpa konversi ulang --
    cepat, dipakai kalau heuristik bab/risiko diperbaiki)."""
    import pymupdf

    pdf = getattr(book, f"{kind}_pdf")
    index: Dict[str, dict] = {}
    with pymupdf.open(pdf) as doc:
        for pno in range(doc.page_count):
            path = page_md_path(book, kind, pno + 1)
            if os.path.exists(path):
                index[str(pno + 1)] = _page_meta(_read_page_body(path), doc[pno])
    return finalize_index(book, kind, index, pdf)


def _write_page(path: str, header: str, md: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"<!-- {header} -->\n\n{md.strip()}\n")


def convert_book(book: Book, kind: str, force: bool = False, log=print) -> Optional[dict]:
    import pymupdf
    import pymupdf4llm

    pdf = getattr(book, f"{kind}_pdf")
    if not pdf:
        log(f"[{book.key}/{kind}] PDF tidak ada, dilewati")
        return None
    out_dir = book.md_dir(kind)
    img_dir = os.path.join(out_dir, "img")
    os.makedirs(img_dir, exist_ok=True)
    index_path = os.path.join(out_dir, "index.json")
    index: Dict[str, dict] = {}
    if os.path.exists(index_path) and not force:
        with open(index_path, encoding="utf-8") as f:
            index = json.load(f).get("pages", {})

    doc = pymupdf.open(pdf)
    todo = [i for i in range(doc.page_count) if force or str(i + 1) not in index]
    t0 = time.time()
    for c in range(0, len(todo), CHUNK_PAGES):
        chunk = todo[c:c + CHUNK_PAGES]
        chunks = pymupdf4llm.to_markdown(
            doc, pages=chunk, page_chunks=True, write_images=True,
            image_path=img_dir, image_format="png", dpi=110, show_progress=False,
        )
        for pno, ch in zip(chunk, chunks):
            page = doc[pno]
            md = ch["text"]
            # path gambar absolut -> relatif terhadap folder halaman
            md = IMG_LINK_RE.sub(lambda m: f"![](img/{os.path.basename(m.group(1))})", md)
            index[str(pno + 1)] = _page_meta(md, page)
            _write_page(page_md_path(book, kind, pno + 1), "", md)  # header diisi di finalize
        done = min(c + CHUNK_PAGES, len(todo))
        log(f"[{book.key}/{kind}] {done}/{len(todo)} halaman ({time.time() - t0:.0f}s)")
    doc.close()
    return finalize_index(book, kind, index, pdf)


def _assign_babs(index: Dict[str, dict]) -> None:
    """Bab dideteksi dari footer (tidak ada di tiap halaman) -> diteruskan ke
    halaman sesudahnya. Nomor bab tidak boleh mundur (footer bab lain yang
    terkutip di teks, mis. "lihat Bab 1", diabaikan)."""
    from collections import Counter

    pages = sorted(index, key=int)
    seen = {}    # bab_no -> daftar halaman terdeteksi
    titles = {}  # bab_no -> Counter judul (judul terbanyak = footer berulang, bukan salah baca)
    for p in pages:
        det = index[p].get("bab_detected")
        if det:
            seen.setdefault(det[0], []).append(int(p))
            if det[1]:
                titles.setdefault(det[0], Counter())[det[1]] += 1

    def name(no: int) -> str:
        t = titles.get(no)
        return f"Bab {no} - {t.most_common(1)[0][0]}" if t else f"Bab {no}"

    def confirmed(det: list, page: int) -> bool:
        # footer asli berulang; sebutan sekali lewat ("lihat Bab 4" di petunjuk buku) tidak.
        # Halaman pembuka bab cukup sekali.
        return (len(det) > 2 and det[2] == "pembuka") or any(page < q <= page + 15 for q in seen.get(det[0], []))

    cur, cur_no = None, 0
    for p in pages:
        det = index[p].get("bab_detected")
        if det and det[0] > cur_no and confirmed(det, int(p)):
            cur, cur_no = name(det[0]), det[0]
        index[p]["bab"] = cur
        index[p]["bab_no"] = cur_no or None


def _detect_bab_from_siswa_titles(book: Book, index: Dict[str, dict]) -> None:
    """Buku Guru yang footernya hanya judul tanpa nomor (SD 6: "Pecahan dan
    Desimal"): nomor bab diambil dari judul bab Buku Siswa yang sama persis."""
    siswa_idx = os.path.join(book.md_dir("siswa"), "index.json")
    if not os.path.exists(siswa_idx):
        return
    with open(siswa_idx, encoding="utf-8") as f:
        ranges = bab_ranges(json.load(f)["pages"])
    titles = {r["bab"].split(" - ", 1)[1].lower(): (r["bab_no"], r["bab"].split(" - ", 1)[1])
              for r in ranges if r["bab_no"] and " - " in r["bab"]}
    for p, meta in index.items():
        path = page_md_path(book, "guru", int(p))
        if not os.path.exists(path):
            continue
        for line in _read_page_body(path).splitlines():
            hit = titles.get(_clean_md_inline(line).lower())
            if hit:
                meta["bab_detected"] = list(hit)
                break


def finalize_index(book: Book, kind: str, index: Dict[str, dict], pdf: str) -> dict:
    if kind == "guru" and not any(m.get("bab_detected") for m in index.values()):
        _detect_bab_from_siswa_titles(book, index)
    _assign_babs(index)
    out_dir = book.md_dir(kind)
    # tulis ulang header metadata tiap halaman (bab baru diketahui setelah semua halaman)
    for p, meta in index.items():
        path = page_md_path(book, kind, int(p))
        if not os.path.exists(path):
            continue
        body = _read_page_body(path)
        flags = []
        if meta["risiko_matematika"]:
            flags.append("RISIKO_MATEMATIKA=" + ",".join(meta["risiko_matematika"]) + " (cek PNG)")
        if meta.get("teks_dalam_gambar"):
            flags.append("TEKS_DALAM_GAMBAR (urutan/pasangan bisa kacau, cek PNG)")
        if meta["gambar"]:
            flags.append(f"gambar={meta['gambar']}")
        header = f"{book.key} {kind} hal.{p} | {meta['bab'] or '-'}" + (" | " + " | ".join(flags) if flags else "")
        _write_page(path, header, body)

    data = {"book": book.key, "kind": kind, "pdf": rel(pdf), "n_pages": len(index),
            "pages": dict(sorted(index.items(), key=lambda kv: int(kv[0])))}
    with open(os.path.join(out_dir, "index.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    with open(os.path.join(out_dir, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write(render_index_md(book, kind, data))
    return data


def bab_ranges(pages: Dict[str, dict]) -> List[dict]:
    babs: List[dict] = []
    for p in sorted(pages, key=int):
        name = pages[p].get("bab") or "Pendahuluan"
        if not babs or babs[-1]["bab"] != name:
            babs.append({"bab": name, "bab_no": pages[p].get("bab_no") or 0, "start": int(p), "end": int(p)})
        babs[-1]["end"] = int(p)
    return babs


def render_index_md(book: Book, kind: str, data: dict) -> str:
    pages = data["pages"]
    title = "Buku Siswa (sumber SOAL)" if kind == "siswa" else "Buku Guru (sumber KUNCI JAWABAN)"
    lines = [
        f"# Indeks {book.key} ({book.jenjang}) -- {title}",
        f"PDF: `{data['pdf']}` ({data['n_pages']} halaman). File halaman: `p0001.md` ... (nomor = halaman PDF).",
        "Legenda: [M] notasi matematika mungkin rusak -> WAJIB lihat PNG | "
        "[T] soal/kunci tercetak di dalam gambar -> lihat PNG | [G] ada gambar | "
        + ("★ heading latihan" if kind == "siswa" else "[K] ada kunci/alternatif jawaban"),
        "",
    ]
    for b in bab_ranges(pages):
        lines.append(f"## {b['bab']}  (hal. {b['start']}-{b['end']})")
        for p in range(b["start"], b["end"] + 1):
            meta = pages.get(str(p))
            if not meta:
                continue
            tags = (("[M]" if meta["risiko_matematika"] else "") + ("[T]" if meta.get("teks_dalam_gambar") else "")
                    + ("[G]" if meta["caption_gambar"] else ""))
            if kind == "siswa":
                if not meta["latihan"]:
                    continue
                desc = " · ".join("★" + h for h in meta["latihan"])
            else:
                if not meta["kunci"]:
                    continue
                tags += "[K]"
                desc = " · ".join(meta["headings"][:4])
            lines.append(f"- p{p:04d} {tags} {desc}".rstrip())
        lines.append("")
    return "\n".join(lines)


def render_page(book: Book, kind: str, page: int, dpi: int = 130) -> str:
    """Render halaman PDF jadi PNG (di-cache) -- dipakai agen untuk membaca
    notasi matematika/tabel/gambar yang rusak di Markdown."""
    import pymupdf

    pdf = getattr(book, f"{kind}_pdf")
    out = os.path.join(book.md_dir(kind), "png", f"p{page:04d}.png")
    if not os.path.exists(out):
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with pymupdf.open(pdf) as doc:
            doc[page - 1].get_pixmap(dpi=dpi).save(out)
    return out


def _job(args):
    key, kind, force = args
    book = get_book(key)
    convert_book(book, kind, force=force, log=lambda m: print(m, flush=True))
    return key, kind


def main(argv=None):
    ap = argparse.ArgumentParser(description="PDF -> Markdown per halaman untuk AI agent.")
    sub = ap.add_subparsers(dest="cmd")
    r = sub.add_parser("render", help="render halaman jadi PNG")
    r.add_argument("book")
    r.add_argument("kind", choices=["siswa", "guru"])
    r.add_argument("pages", nargs="+", type=int)
    r.add_argument("--dpi", type=int, default=130)
    ap.add_argument("--book", action="append", help="kunci buku (boleh diulang), mis. kelas5")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--kind", choices=["siswa", "guru"], action="append")
    ap.add_argument("--force", action="store_true", help="konversi ulang walau sudah ada")
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--reindex", action="store_true",
                    help="hitung ulang metadata & INDEX.md dari .md yang sudah ada (tanpa konversi ulang)")
    a = ap.parse_args(argv)

    if a.cmd == "render":
        book = get_book(a.book)
        for p in a.pages:
            print(render_page(book, a.kind, p, a.dpi))
        return

    books = discover()
    keys = list(books) if a.all else (a.book or [])
    if not keys:
        ap.error("pakai --all atau --book <kunci>. Buku tersedia: " + ", ".join(books))
    kinds = a.kind or ["siswa", "guru"]

    if a.reindex:
        for k in keys:
            for kind in kinds:
                if os.path.exists(os.path.join(books[k].md_dir(kind), "index.json")):
                    refresh_meta(books[k], kind)
                    print(f"[{k}/{kind}] indeks dibangun ulang")
        return

    jobs = [(k, kind, a.force) for k in keys for kind in kinds if getattr(books[k], f"{kind}_pdf")]
    if a.workers <= 1 or len(jobs) == 1:
        for j in jobs:
            _job(j)
    else:
        from concurrent.futures import ProcessPoolExecutor

        with ProcessPoolExecutor(max_workers=a.workers) as ex:
            for key, kind in ex.map(_job, jobs):
                print(f"SELESAI {key}/{kind}", flush=True)


if __name__ == "__main__":
    sys.exit(main())
