"""
Tes koneksi MongoDB (hanya membaca: ping + daftar koleksi). Dari root project:
    venv/bin/python scripts/test_mongodb.py        # Linux (mini PC)
    venv/Scripts/python scripts/test_mongodb.py    # Windows

Membaca MONGODB_URI dan MONGODB_DATABASE dari .env / environment. URI (berisi password) tidak pernah dicetak.
Gagal "timed out" hampir selalu berarti IP mesin ini belum diizinkan di Atlas (Network Access).
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

from dotenv import dotenv_values

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    file_values = dotenv_values(ROOT / ".env")
    uri = os.getenv("MONGODB_URI") or file_values.get("MONGODB_URI")
    database = os.getenv("MONGODB_DATABASE") or file_values.get("MONGODB_DATABASE")
    if not uri or not database:
        print("[GAGAL] MONGODB_URI dan MONGODB_DATABASE harus diisi di .env")
        return 2

    from pymongo import MongoClient
    from pymongo.errors import PyMongoError

    client = MongoClient(uri, appname="exercise-pipeline-test", serverSelectionTimeoutMS=8000)
    try:
        client.admin.command("ping")
        names = sorted(client[database].list_collection_names())
    except PyMongoError as exc:
        kind = type(exc).__name__
        hint = ("IP mesin ini kemungkinan belum diizinkan di Atlas (Network Access)"
                if "ServerSelection" in kind else "periksa user/password dan hak akses user")
        print(f"[GAGAL] {kind}: {hint}")
        return 1
    finally:
        client.close()

    print(f"[OK] terhubung ke database '{database}'")
    print(f"Koleksi ({len(names)}):", ", ".join(names) if names else "(kosong)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
