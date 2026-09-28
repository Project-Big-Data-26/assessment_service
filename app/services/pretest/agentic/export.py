"""
export.py -- gabungkan bab<NN>.json (hasil agen, sudah lolos validate.py)
menjadi satu file per buku dengan format model `Pertanyaan`
(app/db/questions_pretest.py), siap untuk tahap berikutnya (validasi taksonomi
Bloom, dsb).

Yang dikerjakan KODE di sini (bukan agen):
  - posisi jawaban benar A/B/C/D diacak SEIMBANG per buku (deterministik,
    hasil sama setiap dijalankan) -- LLM cenderung menaruh jawaban benar di
    posisi tertentu, jadi posisi tidak diserahkan ke agen
  - status & flag diturunkan dari fakta (schema.derive_status)
  - file bab yang GAGAL validasi tidak ikut diekspor

Cara pakai:
  python -m app.services.pretest.agentic.export --book kelas5
  python -m app.services.pretest.agentic.export --all
Hasil: output/pretest/<buku>/soal_pretest.json
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import random
import sys
from typing import List

from app.services.pretest.agentic.books import discover, rel
from app.services.pretest.agentic.schema import derive_status
from app.services.pretest.agentic.validate import validate_file

PIPELINE_VERSION = "agentic-2026-09-27"
OPTION_IDS = ["A", "B", "C", "D"]
_CONFIDENCE = {"cocok": 0.95, "tidak_ada_di_guru": 0.6, "tidak_cocok": 0.3}


def export_book(key: str) -> dict:
    book = discover()[key]
    files = sorted(glob.glob(os.path.join(book.out_dir(), "bab[0-9][0-9].json")))
    records: List[dict] = []
    skipped_files = []
    for path in files:
        data, errors, _warns = validate_file(path)
        if data is None or errors:
            skipped_files.append(os.path.basename(path))
            continue
        for s in data.soal:
            status, flags = derive_status(s)
            text = f"{s.stimulus.strip()}\n\n{s.pertanyaan.strip()}" if s.stimulus else s.pertanyaan.strip()
            img_urls = [rel(os.path.join(book.md_dir("siswa"), r)) for r in s.image_refs]
            records.append({
                "id": s.id,
                "pertanyaan_text": text,
                "image_url": img_urls[0] if img_urls else None,
                "image_urls": img_urls,
                "pertanyaan_type": "pilihan_ganda",
                "_jawaban_benar": s.jawaban_benar,
                "_distraktor": [d.teks for d in s.distraktor],
                "correct_answer": s.jawaban_benar,
                "status": status,
                "source_file": os.path.basename(book.siswa_pdf),
                "source_page": s.source_page,
                "source_section": s.source_section,
                "source_bab": data.bab,
                "source_item_no": s.source_item_no,
                "extraction_confidence": _CONFIDENCE[s.status_kunci],
                "extraction_flags": flags,
                "validation_result": {
                    "status_kunci": s.status_kunci,
                    "kunci_guru": s.kunci_guru.model_dump() if s.kunci_guru else None,
                    "kunci_guru_file": os.path.basename(book.guru_pdf) if s.kunci_guru else None,
                    "jawaban_agen": s.jawaban_agen,
                    "alasan_distraktor": {d.teks: d.alasan for d in s.distraktor},
                    "catatan": s.catatan,
                    "catatan_penyesuaian": s.catatan_penyesuaian,
                },
                "pipeline_version": PIPELINE_VERSION,
            })

    # Posisi jawaban benar: kelipatan [0,1,2,3] diacak dengan seed tetap ->
    # sebaran A/B/C/D seimbang & hasil ekspor stabil.
    rng = random.Random(f"{key}-{PIPELINE_VERSION}")
    positions = [i % 4 for i in range(len(records))]
    rng.shuffle(positions)
    for rec, pos in zip(records, positions):
        distractors = rec.pop("_distraktor")
        correct = rec.pop("_jawaban_benar")
        rng.shuffle(distractors)
        texts = distractors[:pos] + [correct] + distractors[pos:]
        rec["options"] = [{"option_id": o, "text": t} for o, t in zip(OPTION_IDS, texts)]
        rec["correct_option_id"] = OPTION_IDS[pos]

    summary = {"total": len(records), "bab_diekspor": len(files) - len(skipped_files),
               "bab_gagal_validasi_tidak_diekspor": skipped_files}
    for r in records:
        summary[r["status"]] = summary.get(r["status"], 0) + 1
    out = os.path.join(book.out_dir(), "soal_pretest.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump({"pipeline_version": PIPELINE_VERSION, "book": key, "summary": summary, "items": records},
                  f, ensure_ascii=False, indent=2)
    print(f"[{key}] {summary} -> {rel(out)}")
    return summary


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", action="append")
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args(argv)
    keys = [k for k, b in discover().items() if os.path.isdir(b.out_dir())] if a.all else (a.book or [])
    if not keys:
        ap.error("pakai --all atau --book <kunci>")
    for k in keys:
        export_book(k)
    return 0


if __name__ == "__main__":
    sys.exit(main())
