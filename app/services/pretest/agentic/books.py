"""Lokasi buku & folder kerja pipeline agentic (satu sumber kebenaran path)."""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from typing import Dict, Optional

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
DATA_DIR = os.path.join(ROOT, "data")
MD_ROOT = os.path.join(DATA_DIR, "processed", "pretest_md")
OUT_ROOT = os.path.join(ROOT, "output", "pretest")

# Sama dengan konvensi scripts/run_all_books.py:
#   panduan_guru_kelas9.pdf, panduan_siswa_kelas11_peminatan.pdf
NAME_RE = re.compile(
    r"^panduan_(guru|siswa)_kelas(\d{1,2})(_(peminatan|tingkat_lanjut))?\.pdf$", re.I
)


@dataclass
class Book:
    key: str                 # "kelas5", "kelas11_tl"
    kelas: int
    jenjang: str             # "SD" | "SMP" | "SMA"
    siswa_pdf: Optional[str] = None
    guru_pdf: Optional[str] = None

    def md_dir(self, kind: str) -> str:
        return os.path.join(MD_ROOT, self.key, kind)

    def out_dir(self) -> str:
        return os.path.join(OUT_ROOT, self.key)


def jenjang_of(kelas: int) -> str:
    return "SD" if kelas <= 6 else "SMP" if kelas <= 9 else "SMA"


def discover(data_dir: str = DATA_DIR) -> Dict[str, Book]:
    books: Dict[str, Book] = {}
    for jenjang in ("sd", "smp", "sma"):
        base = os.path.join(data_dir, jenjang)
        for root, _dirs, files in os.walk(base):
            for fn in sorted(files):
                m = NAME_RE.match(fn)
                if not m:
                    continue
                kelas = int(m.group(2))
                key = f"kelas{kelas}" + ("_tl" if m.group(3) else "")
                book = books.setdefault(key, Book(key, kelas, jenjang_of(kelas)))
                setattr(book, f"{m.group(1).lower()}_pdf", os.path.join(root, fn))
    return dict(sorted(books.items(), key=lambda kv: (kv[1].kelas, kv[0])))


def get_book(key: str) -> Book:
    books = discover()
    if key not in books:
        raise SystemExit(f"Buku '{key}' tidak ditemukan. Tersedia: {', '.join(books)}")
    return books[key]


def rel(path: str) -> str:
    """Path relatif terhadap root project (garis miring '/'); path absolut
    kalau beda drive (Windows) sehingga relpath tidak mungkin."""
    try:
        return os.path.relpath(path, ROOT).replace("\\", "/")
    except ValueError:
        return path.replace("\\", "/")


def page_md_path(book: Book, kind: str, page: int) -> str:
    return os.path.join(book.md_dir(kind), f"p{page:04d}.md")
