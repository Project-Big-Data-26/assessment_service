from __future__ import annotations

import fitz
import argparse
import json
import sys
import traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.services.pretest.extractor_text import (
    run_extraction_from_pages_with_bab_tracking,
    summarize,
)


def read_pdf_pages(pdf_path: Path):

    pages = []
    with fitz.open(str(pdf_path)) as doc:
        for i, page in enumerate(doc):
            pages.append((i + 1, page.get_text()))
    return pages


def test_one_pdf(pdf_path: Path) -> dict:
    result = {
        "file": str(pdf_path),
        "ok": False,
        "error": None,
        "stats": None,
    }
    try:
        pages = read_pdf_pages(pdf_path)
        blocks = run_extraction_from_pages_with_bab_tracking(
            pages, source_file=pdf_path.name
        )
        stats = summarize(blocks)
        result["ok"] = True
        result["stats"] = stats

        total = stats.get("_total", 0)
        draft = stats.get("draft", 0)
        if total == 0:
            result["warning"] = (
                "0 kandidat soal ketemu sama sekali -- kemungkinan besar "
                "heading 'Jawaban Latihan'/'Uji Kompetensi' di buku ini "
                "formatnya beda dari yang dipakai regex."
            )
        elif draft == 0:
            result["warning"] = (
                "Ada kandidat ketemu tapi 0 yang lolos jadi 'draft' -- "
                "cek apakah semuanya kena skip/needs_review, atau memang "
                "isinya begitu."
            )
    except Exception as e:  # noqa: BLE001
        result["error"] = f"{type(e).__name__}: {e}"
        result["traceback"] = traceback.format_exc()

    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--data-dir", default="data", help="Folder root berisi PDF (dicari rekursif)"
    )
    parser.add_argument(
        "--out", default="batch_extraction_report.json", help="Path file laporan JSON"
    )
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    pdf_files = sorted(data_dir.rglob("*.pdf"))

    if not pdf_files:
        print(f"Tidak ada file .pdf ditemukan di '{data_dir}'.")
        return

    print(f"Ditemukan {len(pdf_files)} file PDF. Menjalankan extractor_text.py...\n")

    results = []
    for pdf_path in pdf_files:
        r = test_one_pdf(pdf_path)
        results.append(r)

        rel = pdf_path.relative_to(data_dir)
        if not r["ok"]:
            print(f"[ERROR] {rel}\n        {r['error']}")
        else:
            s = r["stats"]
            flag = " <-- PERLU DICEK" if "warning" in r else ""
            print(
                f"[OK]    {rel}  total={s.get('_total', 0)} "
                f"draft={s.get('draft', 0)} needs_image={s.get('needs_image', 0)} "
                f"skipped_open_ended={s.get('skipped_open_ended', 0)} "
                f"skipped_pembuktian={s.get('skipped_pembuktian', 0)} "
                f"needs_review={s.get('needs_review_extraction', 0)}{flag}"
            )
            if "warning" in r:
                print(f"        -> {r['warning']}")

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    # Ringkasan akhir
    n_ok = sum(1 for r in results if r["ok"])
    n_error = sum(1 for r in results if not r["ok"])
    n_warning = sum(1 for r in results if r.get("warning"))
    print(f"\n=== RINGKASAN ===")
    print(f"Total PDF          : {len(results)}")
    print(f"Berhasil diproses  : {n_ok}")
    print(f"Error (exception)  : {n_error}")
    print(f"Perlu dicek (0 hasil / 0 draft) : {n_warning}")
    print(f"\nLaporan lengkap: {args.out}")


if __name__ == "__main__":
    main()
