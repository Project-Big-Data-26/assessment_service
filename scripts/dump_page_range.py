from __future__ import annotations
import fitz
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", required=True, help="Path ke PDF")
    parser.add_argument("--start", type=int, required=True, help="Halaman awal (1-based, inklusif)")
    parser.add_argument("--end", type=int, required=True, help="Halaman akhir (1-based, inklusif)")
    args = parser.parse_args()

    pdf_path = Path(args.pdf)
    if not pdf_path.exists():
        print(f"File tidak ditemukan: {pdf_path}")
        return

    with fitz.open(str(pdf_path)) as doc:
        for i, page in enumerate(doc):
            page_no = i + 1
            if page_no < args.start or page_no > args.end:
                continue
            print(f"\n=== Halaman {page_no} ===")
            for raw_line in page.get_text().splitlines():
                line = raw_line.strip()
                if line:
                    print(f"  {line!r}")


if __name__ == "__main__":
    main()
