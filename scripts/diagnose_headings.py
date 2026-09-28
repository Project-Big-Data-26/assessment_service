from __future__ import annotations
import fitz
import argparse
import re
from collections import defaultdict
from pathlib import Path

CANDIDATE_KEYWORDS_RE = re.compile(
    r"jawaban|kunci|latihan|uji\s*kompetensi|eksplorasi|^bab\s|evaluasi|"
    r"rangkuman|soal|tugas|penilaian|penyelesaian",
    re.IGNORECASE,
)

MAX_HEADING_LEN = 70


def find_candidate_headings(pdf_path: Path):
    occurrences: dict[str, list[int]] = defaultdict(list)

    with fitz.open(str(pdf_path)) as doc:
        for i, page in enumerate(doc):
            page_no = i + 1
            for raw_line in page.get_text().splitlines():
                line = raw_line.strip()
                if not line or len(line) > MAX_HEADING_LEN:
                    continue
                if CANDIDATE_KEYWORDS_RE.search(line):
                    occurrences[line].append(page_no)

    return occurrences


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", required=True, help="Path ke PDF yang mau didiagnosis")
    parser.add_argument(
        "--min-freq",
        type=int,
        default=2,
        help="Cuma tampilkan baris yang muncul minimal N kali (default 2 -- "
        "fokus ke kandidat heading yang BERULANG, bukan kalimat sekali muncul)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=200,
        help="Maksimal baris unik yang ditampilkan (default 200)",
    )
    args = parser.parse_args()

    pdf_path = Path(args.pdf)
    if not pdf_path.exists():
        print(f"File tidak ditemukan: {pdf_path}")
        return

    occurrences = find_candidate_headings(pdf_path)

    filtered = {
        line: pages for line, pages in occurrences.items() if len(pages) >= args.min_freq
    }
    items = sorted(filtered.items(), key=lambda kv: (-len(kv[1]), kv[0]))

    total_unique = len(occurrences)
    print(f"File: {pdf_path}")
    print(f"Total baris unik (semua frekuensi): {total_unique}")
    print(
        f"Baris dengan frekuensi >= {args.min_freq}: {len(items)} "
        f"(ini yang paling mungkin heading section asli)\n"
    )

    for line, pages in items[: args.limit]:
        pages_preview = ", ".join(str(p) for p in pages[:6])
        more = f", +{len(pages) - 6} lagi" if len(pages) > 6 else ""
        print(f"  [{len(pages):>2}x]  hal. {pages_preview}{more}  |  {line}")

    if len(items) > args.limit:
        print(f"\n... ({len(items) - args.limit} baris lagi, dipotong. Naikkan --limit kalau perlu)")

    if not items:
        print(
            "Tidak ada baris yang berulang >= "
            f"{args.min_freq}x. Coba turunkan --min-freq jadi 1 untuk lihat "
            "semua kandidat (termasuk yang cuma sekali muncul)."
        )


if __name__ == "__main__":
    main()
