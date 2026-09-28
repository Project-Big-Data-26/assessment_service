"""
pretest.py -- merakit soal PRETEST per bab dan mengekspornya ke format tabel
`soal` milik tim backend (data/tabel_database/Daftar Collections - Big Data.xlsx,
sheet "Log 1227 25092026").

ATURAN SESI PRETEST (dari tim, acuan Prasyarat_Math.xlsx):
  - 2 soal untuk SETIAP subbab bab tersebut
  - 1 soal untuk SETIAP bab prasyarat, diambil dari SUBBAB TERAKHIR bab
    prasyarat itu, yaitu soal yang PALING SUSAH
Hanya soal Pilihan Ganda. Hanya soal pretest yang diekspor (bukan seluruh bank).

PEMILIHAN (deterministik, bisa diaudit):
  - Prioritas status: draft (kunci Guru cocok) > needs_review_soal > needs_review_kunci.
    Soal needs_image tanpa file gambar tidak pernah dipilih.
  - 2 soal subbab: dari kelompok status terbaik, ambil yang tingkat kesulitannya
    paling tinggi dan paling rendah (sebaran, bukan dua soal yang mirip).
  - Soal prasyarat: status terbaik, lalu tingkat_kesulitan tertinggi.
    `tingkat_kesulitan` adalah penilaian agen (1-5), dipakai sementara karena
    cognitive_level/score baru diisi tim validasi.

FIELD YANG SENGAJA NULL (diisi pihak lain): berkas_id, kelas_id (seeder backend),
matching_pairs (hanya untuk latihan tipe matching), cognitive_level,
cognitive_score, confidence_score (tim validasi), status (tim backend).

HASIL (output/pretest/<buku>/):
  soal_pretest_db.json  daftar dokumen tabel `soal` (unik per _id; seeder: upsert by _id)
  sesi_pretest.json     per bab: _id soal tiap subbab & tiap prasyarat + kekurangan + jejak audit
  images/               gambar soal yang dirujuk image_url

Cara pakai:
  python -m app.services.pretest.agentic.pretest --book kelas5
"""

from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import os
import random
import shutil
import sys
from typing import Dict, List, Optional, Tuple

from app.services.pretest.agentic import kurikulum
from app.services.pretest.agentic.books import discover, rel
from app.services.pretest.agentic.schema import BabFile, Soal, derive_status
from app.services.pretest.agentic.validate import SOAL_PER_SUBBAB, validate_file

OPTION_IDS = ["A", "B", "C", "D"]
_STATUS_RANK = {"draft": 0, "needs_review_soal": 1, "needs_review_kunci": 2}


def object_id(soal_id: str) -> str:
    """ObjectId 24-hex DETERMINISTIK dari id soal -> ekspor ulang tidak membuat duplikat."""
    return hashlib.md5(soal_id.encode("utf-8")).hexdigest()[:24]


def _rank(s: Soal) -> Optional[int]:
    return _STATUS_RANK.get(derive_status(s)[0])   # None = tidak boleh dipakai (needs_image)


def _load_bab(bab: kurikulum.Bab, cache: Dict[str, Optional[BabFile]]) -> Optional[BabFile]:
    if bab.bab_id not in cache:
        cache[bab.bab_id] = None
        books = discover()
        if bab.book in books:
            path = os.path.join(books[bab.book].out_dir(), f"bab{bab.bab_no:02d}.json")
            if os.path.exists(path):
                data, errors, _ = validate_file(path)
                cache[bab.bab_id] = data if data is not None and not errors else None
    return cache[bab.bab_id]


def pick_subbab(soal: List[Soal], n: int = SOAL_PER_SUBBAB) -> List[Soal]:
    usable = [s for s in soal if _rank(s) is not None]
    chosen: List[Soal] = []
    for rank in sorted({_rank(s) for s in usable}):
        pool = sorted((s for s in usable if _rank(s) == rank), key=lambda s: (-(s.tingkat_kesulitan or 0), s.id))
        # tersulit, termudah, lalu sisanya -> 2 soal yang kesulitannya tersebar
        for s in [pool[0]] + pool[-1:] * (len(pool) > 1) + pool[1:-1]:
            if len(chosen) < n:
                chosen.append(s)
    return chosen


def pick_hardest(soal: List[Soal]) -> Optional[Soal]:
    usable = [s for s in soal if _rank(s) is not None]
    return min(usable, key=lambda s: (_rank(s), -(s.tingkat_kesulitan or 0), s.id)) if usable else None


def _options(s: Soal, pos: int, rng: random.Random) -> Tuple[List[dict], str]:
    distraktor = list(s.distraktor)
    rng.shuffle(distraktor)
    benar = {"text": s.jawaban_benar, "alasan": f"Benar: {s.alasan_benar or s.jawaban_agen}"}
    salah = [{"text": d.teks, "alasan": f"Salah: {d.alasan}"} for d in distraktor]
    ordered = salah[:pos] + [benar] + salah[pos:]
    return [{"option_id": o, **x} for o, x in zip(OPTION_IDS, ordered)], OPTION_IDS[pos]


def _doc(s: Soal, bab: kurikulum.Bab, pos: int, rng: random.Random, img_dir: str, now: str) -> dict:
    books = discover()
    src_dir = books[bab.book].md_dir(s.sumber_soal)
    image_url = []
    for ref in s.image_refs:
        name = f"{bab.book}_{os.path.basename(ref)}"
        shutil.copyfile(os.path.join(src_dir, ref), os.path.join(img_dir, name))
        image_url.append(f"images/{name}")
    options, jawaban = _options(s, pos, rng)
    text = f"{s.stimulus.strip()}\n\n{s.pertanyaan.strip()}" if s.stimulus else s.pertanyaan.strip()
    return {
        "_id": object_id(s.id),
        "berkas_id": None,
        "subbab_id": bab.subbab_nama(s.subbab),
        "kelas_id": None,
        "soal_text": text,
        "image_url": image_url,
        "soal_type": "Pilihan Ganda",
        "options": options,
        "matching_pairs": None,
        "jawaban": jawaban,
        "cognitive_level": None,
        "cognitive_score": None,
        "status": None,
        "created_at": now,
        "updated_at": now,
        "confidence_score": None,
    }


def build(book: str) -> dict:
    all_babs = kurikulum.load()
    target = sorted((b for b in all_babs.values() if b.book == book), key=lambda b: b.bab_no)
    cache: Dict[str, Optional[BabFile]] = {}
    out_dir = discover()[book].out_dir()
    img_dir = os.path.join(out_dir, "images")
    os.makedirs(img_dir, exist_ok=True)

    picks: List[Tuple[Soal, kurikulum.Bab]] = []    # urutan tetap untuk pengacakan posisi
    sesi = []
    for bab in target:
        data = _load_bab(bab, cache)
        entry = {"bab_id": bab.bab_id, "bab": bab.nama, "subbab": [], "prasyarat": [], "kekurangan": []}
        if data is None or data.mode != "lengkap":
            entry["kekurangan"].append(f"bab{bab.bab_no:02d}.json belum ada / belum lolos validasi / belum lengkap")
        for kode, nama in bab.subbab:
            chosen = pick_subbab([s for s in data.soal if s.subbab == kode]) if data else []
            picks += [(s, bab) for s in chosen]
            entry["subbab"].append({"kode": kode, "subbab_id": nama, "soal": [object_id(s.id) for s in chosen]})
            if data and len(chosen) < SOAL_PER_SUBBAB:
                entry["kekurangan"].append(f"subbab {kode} '{nama}': {len(chosen)}/{SOAL_PER_SUBBAB} soal")
        for pid in bab.prasyarat:
            pbab = all_babs.get(pid)
            pdata = _load_bab(pbab, cache) if pbab else None
            last = pbab.subbab_terakhir if pbab else None
            s = pick_hardest([x for x in pdata.soal if x.subbab == last[0]]) if pdata and last else None
            if s:
                picks.append((s, pbab))
            else:
                entry["kekurangan"].append(f"prasyarat {pid}: belum ada soal subbab terakhir"
                                           f"{f' {last[0]} {last[1]!r}' if last else ''} (ekstrak bab itu dulu)")
            entry["prasyarat"].append({"bab_id": pid, "subbab_id": last[1] if last else None,
                                       "soal": object_id(s.id) if s else None,
                                       "tingkat_kesulitan": s.tingkat_kesulitan if s else None})
        sesi.append(entry)

    # dokumen unik (satu soal bisa dipakai 2 sesi) + posisi jawaban benar seimbang
    unique: Dict[str, Tuple[Soal, kurikulum.Bab]] = {}
    for s, b in picks:
        unique.setdefault(object_id(s.id), (s, b))
    rng = random.Random(f"pretest-{book}")
    positions = [i % 4 for i in range(len(unique))]
    rng.shuffle(positions)
    now = _dt.datetime.now().astimezone().isoformat(timespec="seconds")
    docs, audit = [], {}
    for (oid, (s, b)), pos in zip(unique.items(), positions):
        docs.append(_doc(s, b, pos, rng, img_dir, now))
        audit[oid] = {"soal": s.id, "bab_id": b.bab_id, "subbab": s.subbab, "status_ekstraksi": derive_status(s)[0],
                      "flags": derive_status(s)[1], "sumber": f"Buku {s.sumber_soal.title()} hal. {s.source_page}",
                      "tingkat_kesulitan": s.tingkat_kesulitan, "alasan_kesulitan": s.alasan_kesulitan}

    with open(os.path.join(out_dir, "soal_pretest_db.json"), "w", encoding="utf-8") as f:
        json.dump(docs, f, ensure_ascii=False, indent=2)
    with open(os.path.join(out_dir, "sesi_pretest.json"), "w", encoding="utf-8") as f:
        json.dump({"book": book, "dibuat": now, "sesi": sesi, "audit": audit}, f, ensure_ascii=False, indent=2)
    kurang = sum(len(e["kekurangan"]) for e in sesi)
    summary = {"book": book, "bab": len(sesi), "soal_db": len(docs), "kekurangan": kurang}
    print(f"[{book}] {summary} -> {rel(os.path.join(out_dir, 'soal_pretest_db.json'))}")
    for e in sesi:
        for k in e["kekurangan"]:
            print(f"  KURANG {e['bab_id']}: {k}")
    return summary


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Rakit soal pretest (2/subbab + prasyarat) ke format tabel soal.")
    ap.add_argument("--book", action="append", required=True)
    a = ap.parse_args(argv)
    for b in a.book:
        build(b)
    return 0


if __name__ == "__main__":
    sys.exit(main())
