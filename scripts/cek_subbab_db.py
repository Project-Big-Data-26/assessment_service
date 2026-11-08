"""
Diagnosa READ-ONLY: apakah ID subbab di MongoDB bentrok karena nama subbab kembar? Dari root project:
    venv/Scripts/python scripts/cek_subbab_db.py            # Windows
    venv/bin/python scripts/cek_subbab_db.py                # Linux

Membaca MONGODB_URI dan MONGODB_DATABASE dari .env. TIDAK menulis apa pun, dan tidak mencetak URI.
Hasilnya aman dibagikan (tanpa password): hanya nama koleksi, nama field, nama subbab, dan jumlah.
"""

from __future__ import annotations

import collections
import os
import sys
from pathlib import Path

from dotenv import dotenv_values

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    env = dotenv_values(ROOT / ".env")
    uri = os.getenv("MONGODB_URI") or env.get("MONGODB_URI")
    database = os.getenv("MONGODB_DATABASE") or env.get("MONGODB_DATABASE") or "math_learning_db"
    if not uri:
        print("[GAGAL] MONGODB_URI belum diisi di .env")
        return 2
    from pymongo import MongoClient

    client = MongoClient(uri, appname="diagnosa-subbab", serverSelectionTimeoutMS=8000)
    db = client[database]
    from pymongo.errors import PyMongoError
    try:
        names = sorted(db.list_collection_names())
    except PyMongoError as exc:
        kind = type(exc).__name__
        print(f"[GAGAL] tidak bisa terhubung ke MongoDB ({kind}).")
        if "ServerSelection" in kind:
            print("Penyebab paling umum: IP komputer ini belum diizinkan di Atlas.")
            print("  1. Cek IP publik: PowerShell -> (Invoke-WebRequest https://api.ipify.org).Content")
            print("  2. Atlas -> Security -> Network Access -> Add IP Address -> tempel IP itu (atau Add Current IP).")
            print("  3. Tunggu 1-2 menit, jalankan ulang. Cek juga cluster tidak berstatus Paused (paket gratis berhenti sendiri).")
            print("  4. Coba jaringan lain (hotspot HP) untuk memastikan ISP/kampus tidak memblokir port 27017.")
        else:
            print("Periksa username/password di MONGODB_URI dan hak akses user database.")
        return 1
    print(f"Database '{database}': {len(names)} koleksi")
    for n in names:
        print(f"  - {n}: {db[n].estimated_document_count()} dokumen")

    sub_name = next((n for n in names if "subbab" in n.lower()), None)
    if not sub_name:
        print("[!] Tidak ada koleksi bernama subbab")
        return 1
    sub = db[sub_name]
    sample = sub.find_one() or {}
    print(f"\nKoleksi subbab '{sub_name}': field = {sorted(sample.keys())}")
    print("Contoh dokumen:", {k: str(v)[:60] for k, v in sample.items()})

    docs = list(sub.find({}))
    by_name = collections.defaultdict(list)
    for d in docs:
        by_name[str(d.get("name"))].append(d)
    dup = {n: v for n, v in by_name.items() if len(v) > 1}
    print(f"\nSubbab di DB: {len(docs)} | nama unik: {len(by_name)} | nama KEMBAR: {len(dup)}")
    soal_name = next((n for n in names if n.lower() in ("soal", "pertanyaan", "questions")), None)
    for n, v in list(dup.items())[:15]:
        print(f"\n  '{n}' muncul {len(v)}x:")
        for d in v:
            extra = {k: str(x)[:24] for k, x in d.items() if k not in ("name", "_id") and "id" in k.lower()}
            jml = db[soal_name].count_documents({"subbab_id": d["_id"]}) if soal_name else "?"
            print(f"     _id={d['_id']} {extra} -> soal yang menunjuk ke ID ini: {jml}")
    if soal_name:
        tanpa = db[soal_name].count_documents({"$or": [{"subbab_id": None}, {"subbab_id": {"$exists": False}}]})
        print(f"\nKoleksi soal '{soal_name}': soal TANPA subbab_id = {tanpa}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
