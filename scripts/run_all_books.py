"""
run_all_books.py -- jalankan Tahap 1 (Buku Guru) + Tahap 1b (gabung soal dari
Buku Siswa) untuk SEMUA buku di satu folder, sekali jalan.

TIDAK menyentuh MongoDB. Output hanya file JSON di folder output.

Folder input boleh berisi subfolder (mis. data/sd, data/smp, data/sma/kelas12)
-- semua dibaca rekursif. Guru & Siswa boleh satu folder atau terpisah.
Konvensi nama file (sesuai file yang sudah kamu punya):
    panduan_guru_kelas9.pdf              <->  panduan_siswa_kelas9.pdf
    panduan_guru_kelas11_peminatan.pdf   <->  panduan_siswa_kelas11_tingkat_lanjut.pdf
("peminatan" dan "tingkat_lanjut" dianggap sama.) File .txt hasil konversi
juga diterima sebagai pengganti .pdf.

Cara pakai (dari root project, venv aktif):
    python -m scripts.run_all_books --in data --out output

Hasil per buku:
    output/kelas9_stage1.json           -- hasil mentah extractor_text.py (Buku Guru)
    output/kelas9_stage1b.json          -- HANYA item yang lolos (soal Siswa + kunci Guru)
    output/kelas9_stage1b_ditolak.json  -- item yang tidak lolos + alasannya (audit saja)
Lanjutkan ke tahap 2 seperti biasa, pakai file *_stage1b.json:
    python -m app.services.pretest.answer_option_generator --in output/kelas9_stage1b.json --out output/kelas9_stage2.json
"""

from __future__ import annotations

import argparse
import os
import re
import sys

from app.services.pretest.extractor_text import (
    PIPELINE_VERSION,
    attach_page_numbers_with_bab_tracking,
    export_to_json,
    extract_candidate_blocks,
    apply_filters,
    extract_pdf_to_json,
    summarize,
)
from app.services.pretest.soal_merger import merge_files

NAME_RE = re.compile(r"^panduan_(guru|siswa)_kelas(\d{1,2})(_(peminatan|tingkat_lanjut))?\.(pdf|txt)$", re.I)


def _book_key(m: re.Match) -> str:
    return f"kelas{m.group(2)}" + ("_tl" if m.group(3) else "")


def _stage1(path: str, out_json: str) -> dict:
    if path.lower().endswith(".pdf"):
        return extract_pdf_to_json(path, out_json)
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    blocks = [apply_filters(b) for b in extract_candidate_blocks(
        attach_page_numbers_with_bab_tracking([(1, raw)]), os.path.basename(path))]
    export_to_json(blocks, out_json)
    return summarize(blocks)


def main():
    ap = argparse.ArgumentParser(description="Tahap 1 + 1b untuk semua buku di satu folder.")
    ap.add_argument("--in", dest="in_dir", required=True, help="folder berisi PDF Buku Guru & Buku Siswa")
    ap.add_argument("--out", dest="out_dir", default="output", help="folder output JSON")
    a = ap.parse_args()

    # Scan REKURSIF: Buku Guru & Buku Siswa boleh di folder yang sama maupun
    # di subfolder per jenjang/kelas (mis. data/sma/kelas12/...). Pasangan
    # ditentukan dari NAMA file, bukan dari lokasi folder.
    import app.services.pretest.extractor_text as _et
    import app.services.pretest.extractor_siswa as _es
    import app.services.pretest.soal_merger as _sm
    print(f"Versi pipeline: {PIPELINE_VERSION}")
    for mod in (_et, _es, _sm):
        print(f"  pakai {mod.__file__}")
    books: dict = {}
    for root, _dirs, files in os.walk(a.in_dir):
        for fn in sorted(files):
            m = NAME_RE.match(fn)
            if not m:
                continue
            slot = books.setdefault(_book_key(m), {})
            kind = m.group(1).lower()
            path = os.path.join(root, fn)
            if kind in slot and slot[kind].lower().endswith(".pdf") and fn.lower().endswith(".pdf"):
                print(f"PERINGATAN: {kind} {_book_key(m)} ada lebih dari satu -- dipakai {slot[kind]}, "
                      f"diabaikan {path}")
                continue
            # .pdf diutamakan kalau ada .pdf dan .txt untuk buku yang sama
            if kind not in slot or fn.lower().endswith(".pdf"):
                slot[kind] = path

    if not books:
        print("Tidak ada file dengan pola nama panduan_guru_kelasN / panduan_siswa_kelasN.")
        sys.exit(1)

    os.makedirs(a.out_dir, exist_ok=True)
    grand = {"total": 0, "draft": 0, "dari_siswa": 0}
    for key in sorted(books, key=lambda k: (int(re.search(r"\d+", k).group()), k)):
        slot = books[key]
        if "guru" not in slot:
            print(f"[{key}] dilewati: Buku Guru tidak ada")
            continue
        s1 = os.path.join(a.out_dir, f"{key}_stage1.json")
        print(f"[{key}] Tahap 1  <- {os.path.basename(slot['guru'])}")
        _stage1(slot["guru"], s1)
        if "siswa" not in slot:
            print(f"[{key}] Tahap 1b dilewati: Buku Siswa tidak ada (pakai {s1} apa adanya)")
            continue
        s1b = os.path.join(a.out_dir, f"{key}_stage1b.json")
        print(f"[{key}] Tahap 1b <- {os.path.basename(slot['siswa'])}")
        summ = merge_files(s1, slot["siswa"], s1b)
        grand["total"] += summ["_total_soal_buku_siswa"]
        grand["draft"] += summ.get("_lolos", 0)
        grand["ditolak"] = grand.get("ditolak", 0) + summ.get("_ditolak", 0)
        print(f"         soal Buku Siswa={summ['_total_soal_buku_siswa']}  LOLOS={summ.get('_lolos', 0)} -> {os.path.basename(s1b)}  "
              f"ditolak={summ.get('_ditolak', 0)} -> {os.path.basename(s1b)[:-5]}_ditolak.json")
    print(f"\nSELESAI. Semua buku: soal Buku Siswa={grand['total']}  LOLOS (siap tahap 2)={grand['draft']}  "
          f"ditolak={grand.get('ditolak', 0)}")
    print("Tahap 2 cukup dijalankan pada file *_stage1b.json (isinya hanya item yang lolos).")


if __name__ == "__main__":
    main()
