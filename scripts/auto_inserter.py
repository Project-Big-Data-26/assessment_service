"""
auto_inserter.py — Pemantau Otomatis & Auto-Import Soal ke MongoDB
===================================================================
Skrip ini berjalan secara kontinu di latar belakang untuk memantau direktori `output/`.
Fitur:
  1. Filter Khusus 'hasil_validasi': hanya memproses file `validation_results.json`
     yang berada langsung di dalam direktori `hasil_validasi/`. File lain (audit,
     bundle, operational_balance, backup) diabaikan secara otomatis.
  2. Sinkronisasi Awal Super Cepat (Initial Sync): memeriksa berkas resmi yang sudah ada
     dan meng-insert soal yang belum ada di database tanpa hambatan.
  3. Batch Duplicate Check & Auto-Update: mencegah duplikasi berbasis _id secara instan (0.05 detik),
     serta otomatis memperbarui skor kognitif jika ada hasil validasi baru dari LLM.
  4. Dynamic Kelas & Subbab Lookup: memetakan kelas_id dan subbab_id langsung dari memori.
  5. Real-time Continuous Watcher: memantau berkas baru / pembaruan dari LLM dengan
     indikator heartbeat agar terminal tidak terlihat stuck/membeku.

Jalankan:
    python scripts/auto_inserter.py
    python scripts/auto_inserter.py --watch-only  (lewati sinkronisasi berkas lama)
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

# -- Path setup agar import `app.*` berjalan mulus dari root proyek ---
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from bson import ObjectId                             # noqa: E402
from pymongo import UpdateOne                         # noqa: E402
from motor.motor_asyncio import AsyncIOMotorClient    # noqa: E402
from beanie import init_beanie                        # noqa: E402

from app.db.questions_pretest import Pertanyaan, Option  # noqa: E402
from app.db.subbab_model import Subbab                   # noqa: E402

# ───────────────────────────── Konfigurasi ─────────────────────────────────

MONGO_URI = (
    "mongodb+srv://romadhonim1_db_user:cEaG3NBp2wKc99VF"
    "@cluster0.nn1euxs.mongodb.net/project_assessment?appName=Cluster0"
)
DB_NAME = "math_learning_db"

WATCH_DIR = _PROJECT_ROOT / "output"
TARGET_FILENAME = "validation_results.json"
TARGET_PARENT_DIR = "hasil_validasi"  # Hanya proses file di dalam folder hasil_validasi
POLL_INTERVAL_SEC = 5
HEARTBEAT_INTERVAL_SEC = 30  # Tampilkan sinyal aktif tiap 30 detik jika standby

# ─────────────────────────────── Logging ───────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("auto_inserter")

_KELAS_RE = re.compile(r"kelas(\d+)(_tl)?", re.IGNORECASE)


# ═══════════════════════════════════════════════════════════════════════════
#  Lookup Helpers (In-Memory untuk Kecepatan Maksimal)
# ═══════════════════════════════════════════════════════════════════════════

async def load_kelas_map(db: Any) -> Dict[str, ObjectId]:
    """
    Memuat seluruh data kelas (14 dokumen) dari database ke memori.
    Menggunakan raw motor collection untuk menghindari issue skema Pydantic.
    Memetakan variasi penamaan folder (e.g. 'kelas5', 'kelas11_tl') langsung ke ObjectId.
    """
    docs = await db.kelas.find({}).to_list(100)
    kelas_map: Dict[str, ObjectId] = {}

    for doc in docs:
        cid = doc["_id"]
        nomor = doc.get("nomor_kelas")
        name = doc.get("name", "")

        if nomor is None:
            continue

        # SD / SMP (Kelas 1 - 9) & Kelas 10 SMA
        if nomor < 11:
            kelas_map[f"kelas{nomor}"] = cid

        # Kelas 11 & 12 SMA (dibagi Umum dan Lanjut)
        elif nomor in (11, 12):
            if "Lanjut" in name:
                kelas_map[f"kelas{nomor}_tl"] = cid
            elif "Umum" in name:
                kelas_map[f"kelas{nomor}"] = cid
            else:
                kelas_map.setdefault(f"kelas{nomor}", cid)

    log.info("Memuat %d pemetaan kelas ke memori", len(kelas_map))
    return kelas_map


async def load_subbab_map() -> Dict[str, ObjectId]:
    """Memuat seluruh data Subbab ke memori {nama_subbab: ObjectId}."""
    docs = await Subbab.find_all().to_list()
    log.info("Memuat %d subbab dari database", len(docs))
    return {s.name: s.id for s in docs}


def _extract_kelas_folder(path: Path) -> Optional[str]:
    """Mendeteksi nama folder kelas dari path berkas."""
    for part in path.parts:
        m = _KELAS_RE.match(part)
        if m:
            return part.lower()
    return None


def _resolve_kelas_id(folder_name: Optional[str], kelas_map: Dict[str, ObjectId]) -> Optional[ObjectId]:
    """Mencari ObjectId kelas secara instan dari memori."""
    if not folder_name:
        return None
    return kelas_map.get(folder_name)


# ═══════════════════════════════════════════════════════════════════════════
#  Pemeriksaan Duplikasi Cepat (Batch $in)
# ═══════════════════════════════════════════════════════════════════════════

async def get_existing_ids(raw_ids: List[str]) -> Set[str]:
    """
    Mengecek duplikasi ribuan soal sekaligus dalam 1 query batch.
    Selesai dalam < 0.05 detik tanpa N+1 query.
    """
    valid_oids = [ObjectId(r) for r in raw_ids if isinstance(r, str) and ObjectId.is_valid(r)]
    if not valid_oids:
        return set()

    existing: Set[str] = set()
    # Batch chunk per 1000 ID agar aman dari batasan payload MongoDB
    chunk_size = 1000
    for i in range(0, len(valid_oids), chunk_size):
        chunk = valid_oids[i : i + chunk_size]
        docs = await Pertanyaan.find({"_id": {"$in": chunk}}).to_list()
        for d in docs:
            existing.add(str(d.id))
    return existing


# ═══════════════════════════════════════════════════════════════════════════
#  Proses Berkas JSON
# ═══════════════════════════════════════════════════════════════════════════

def _build_soal(
    item: Dict[str, Any],
    kelas_id: Optional[ObjectId],
    subbab_id: Optional[ObjectId],
) -> Pertanyaan:
    """Mengubah dictionary JSON menjadi model Pertanyaan."""
    options = [
        Option(
            option_id=str(o.get("option_id", "")),
            text=str(o.get("text", "")),
            alasan=o.get("alasan"),
        )
        for o in item.get("options", [])
    ]

    raw_img = item.get("image_url")
    if isinstance(raw_img, list):
        image_url = [str(x) for x in raw_img]
    elif isinstance(raw_img, str) and raw_img.strip():
        image_url = [raw_img.strip()]
    else:
        image_url = []

    kwargs: Dict[str, Any] = {
        "soal_text": str(item.get("soal_text", "")),
        "image_url": image_url,
        "options": options,
        "jawaban": item.get("jawaban"),
        "cognitive_level": item.get("cognitive_level"),
        "cognitive_score": item.get("cognitive_score"),
        "confidence_score": item.get("confidence_score"),
        "kelas_id": kelas_id,
        "subbab_id": subbab_id,
        "status": "active",
    }

    raw_id = item.get("_id")
    if raw_id and ObjectId.is_valid(str(raw_id)):
        kwargs["id"] = ObjectId(str(raw_id))

    return Pertanyaan(**kwargs)

async def process_file(
    file_path: Path,
    subbab_map: Dict[str, ObjectId],
    kelas_map: Dict[str, ObjectId],
    silent_if_no_new: bool = False,
) -> int:
    """
    Membaca berkas validation_results.json, mengecek duplikasi,
    meng-insert soal baru, dan memperbarui skor kognitif soal lama.
    """
    rel_path = file_path.relative_to(_PROJECT_ROOT) if file_path.is_relative_to(_PROJECT_ROOT) else file_path

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as exc:
        log.error("Gagal membaca %s: %s", rel_path, exc)
        return 0

    if not isinstance(data, list) or not data:
        return 0

    # 1. Resolusi Kelas ID
    kelas_folder = _extract_kelas_folder(file_path)
    kelas_id = _resolve_kelas_id(kelas_folder, kelas_map)

    # 2. Cek Duplikasi Massal (Batch)
    raw_ids = [str(item["_id"]) for item in data if item.get("_id")]
    existing_ids = await get_existing_ids(raw_ids)

    # 3. Filter Soal Baru & Siapkan Update untuk Soal yang Berubah
    new_soal: List[Pertanyaan] = []
    updates: List[UpdateOne] = []
    seen_in_file: Set[str] = set()
    skipped = 0

    for item in data:
        soal_id = str(item.get("_id", ""))

        if soal_id and (soal_id in existing_ids or soal_id in seen_in_file):
            # Jika soal sudah ada di DB, periksa apakah file JSON memiliki data validasi kognitif
            cog_level = item.get("cognitive_level")
            if soal_id in existing_ids and cog_level is not None and ObjectId.is_valid(soal_id):
                updates.append(
                    UpdateOne(
                        {"_id": ObjectId(soal_id)},
                        {"$set": {
                            "cognitive_level": cog_level,
                            "cognitive_score": item.get("cognitive_score"),
                            "confidence_score": item.get("confidence_score"),
                            "status": "active",
                        }}
                    )
                )
            skipped += 1
            continue

        if soal_id:
            seen_in_file.add(soal_id)

        # Resolusi Subbab ID
        nama_subbab = item.get("subbab_id")
        subbab_id = subbab_map.get(nama_subbab) if nama_subbab else None

        new_soal.append(_build_soal(item, kelas_id, subbab_id))

    # 4. Terapkan Update untuk Soal yang Diperbarui oleh LLM
    updated_count = 0
    if updates:
        try:
            coll = Pertanyaan.get_motor_collection()
            res = await coll.bulk_write(updates, ordered=False)
            updated_count = res.modified_count
        except Exception as exc:
            log.warning("Gagal bulk update data kognitif (%s)", exc)

    # 5. Simpan Soal Baru ke Database
    if not new_soal:
        if updated_count > 0:
            log.info("🔄 [Auto-Update] %d soal diperbarui skor kognitifnya di DB dari %s", updated_count, rel_path)
            return updated_count
        if not silent_if_no_new:
            log.info("⏩ Dilewati: %s (semua %d soal sudah ada di DB)", rel_path, skipped)
        return 0

    try:
        await Pertanyaan.insert_many(new_soal)
        update_msg = f", {updated_count} diperbarui" if updated_count > 0 else ""
        log.info(
            "⚡ [Auto-Import] %d soal baru berhasil di-insert dari %s (duplikat: %d%s)",
            len(new_soal), rel_path, skipped, update_msg
        )
        return len(new_soal) + updated_count
    except Exception as exc:
        log.warning("insert_many gagal (%s), beralih ke fallback satu per satu...", exc)
        inserted = 0
        for s in new_soal:
            try:
                await s.insert()
                inserted += 1
            except Exception:
                pass
        log.info("⚡ [Auto-Import] %d/%d soal berhasil di-insert (fallback) dari %s", inserted, len(new_soal), rel_path)
        return inserted


# ═══════════════════════════════════════════════════════════════════════════
#  Pemindai Direktori (Hanya Memantau Folder 'hasil_validasi')
# ═══════════════════════════════════════════════════════════════════════════

def scan_all_targets(root: Path) -> Dict[Path, float]:
    """
    Menemukan semua path dan mtime validation_results.json yang berada
    langsung di dalam folder TARGET_PARENT_DIR ('hasil_validasi').
    File validation_results.json di folder lain (seperti audit, bundle, operational_balance, dll.)
    secara otomatis diabaikan.
    """
    targets: Dict[Path, float] = {}
    try:
        for dirpath, _, filenames in os.walk(root):
            if TARGET_FILENAME in filenames:
                dir_path = Path(dirpath)
                # Hanya sertakan file jika folder induknya bernama 'hasil_validasi'
                if dir_path.name.lower() == TARGET_PARENT_DIR.lower():
                    fp = dir_path / TARGET_FILENAME
                    try:
                        targets[fp] = fp.stat().st_mtime
                    except OSError:
                        pass
    except Exception as exc:
        log.warning("Gagal memindai direktori %s: %s", root, exc)
    return targets


# ═══════════════════════════════════════════════════════════════════════════
#  Loop Utama Pemantau (Watcher Loop)
# ═══════════════════════════════════════════════════════════════════════════

async def run_watcher(skip_initial_sync: bool = False) -> None:
    """Inisialisasi DB, sinkronisasi awal, dan loop pemantau berkas."""
    log.info("Menghubungkan ke MongoDB Atlas...")
    client = AsyncIOMotorClient(MONGO_URI)
    db = client[DB_NAME]
    await init_beanie(database=db, document_models=[Pertanyaan, Subbab])
    log.info("Terhubung ke database '%s'", DB_NAME)

    # Muat pemetaan kelas & subbab langsung ke RAM
    kelas_map = await load_kelas_map(db)
    subbab_map = await load_subbab_map()

    # Temukan semua file resmi di dalam folder 'hasil_validasi'
    known_files = scan_all_targets(WATCH_DIR)
    total_found = len(known_files)

    # ── Tahap 1: Sinkronisasi Awal ──────────────────────────────────────────
    if not skip_initial_sync and total_found > 0:
        log.info("=" * 60)
        log.info("🔍 [Sinkronisasi Awal] Ditemukan %d berkas hasil_validasi/validation_results.json", total_found)
        log.info("   Memeriksa dan mengimpor soal yang belum tersimpan di DB...")
        log.info("=" * 60)

        total_inserted = 0
        for idx, fp in enumerate(known_files.keys(), start=1):
            inserted = await process_file(fp, subbab_map, kelas_map, silent_if_no_new=True)
            total_inserted += inserted
            # Tampilkan progress setiap file baru / kelipatan
            if inserted > 0 or idx % 5 == 0 or idx == total_found:
                log.info("📊 Progress Sinkronisasi: [%d/%d berkas] | +%d soal baru/diperbarui", idx, total_found, total_inserted)

        log.info("=" * 60)
        log.info("✅ [Sinkronisasi Selesai] Total %d soal diproses ke DB!", total_inserted)
        log.info("=" * 60)
    else:
        log.info("Melewati sinkronisasi awal (%d berkas existing dicatat).", total_found)

    # ── Tahap 2: Pemantauan Real-time ───────────────────────────────────────
    log.info("👀 [Watcher Aktif] Memantau berkas 'hasil_validasi/%s' di folder '%s' (setiap %ds)", TARGET_FILENAME, WATCH_DIR.name, POLL_INTERVAL_SEC)
    log.info("💡 Tekan Ctrl+C di terminal kapan saja untuk menghentikan.")

    heartbeat_counter = 0

    while True:
        try:
            await asyncio.sleep(POLL_INTERVAL_SEC)
            current_files = scan_all_targets(WATCH_DIR)

            any_change = False

            # Deteksi file baru / termodifikasi
            for fp, mtime in current_files.items():
                prev_mtime = known_files.get(fp)
                if prev_mtime is None or mtime > prev_mtime:
                    any_change = True
                    is_new = prev_mtime is None
                    action = "🆕 Berkas baru terdeteksi" if is_new else "🔄 Berkas diperbarui"
                    log.info("%s: %s", action, fp.relative_to(_PROJECT_ROOT))

                    await process_file(fp, subbab_map, kelas_map, silent_if_no_new=False)
                    known_files[fp] = mtime

            # Deteksi file dihapus
            deleted = set(known_files.keys()) - set(current_files.keys())
            for fp in deleted:
                log.info("🗑️  Berkas dihapus: %s", fp.relative_to(_PROJECT_ROOT))
                del known_files[fp]
                any_change = True

            # Heartbeat agar terminal tidak tampak membeku
            if not any_change:
                heartbeat_counter += POLL_INTERVAL_SEC
                if heartbeat_counter >= HEARTBEAT_INTERVAL_SEC:
                    log.info("💓 [Standby] Pemantau aktif, menunggu berkas baru di hasil_validasi/ ...")
                    heartbeat_counter = 0
            else:
                heartbeat_counter = 0

        except asyncio.CancelledError:
            log.info("🛑 Pemantau dihentikan.")
            break
        except Exception as exc:
            log.exception("⚠️ Terjadi kesalahan di loop pemantau (tetap berjalan): %s", exc)
            await asyncio.sleep(POLL_INTERVAL_SEC)


# ═══════════════════════════════════════════════════════════════════════════
#  Entry Point
# ═══════════════════════════════════════════════════════════════════════════

def main() -> None:
    parser = argparse.ArgumentParser(description="Auto Inserter & File Watcher")
    parser.add_argument(
        "--watch-only",
        action="store_true",
        help="Lewati pemeriksaan awal berkas yang sudah ada, hanya pantau berkas baru.",
    )
    args = parser.parse_args()

    print(
        "\n"
        "╔══════════════════════════════════════════════════════════╗\n"
        "║     🚀 AUTO-INSERTER & CONTINUOUS FILE WATCHER           ║\n"
        "║     Khusus folder: hasil_validasi/validation_results.json║\n"
        "╚══════════════════════════════════════════════════════════╝\n"
    )

    try:
        asyncio.run(run_watcher(skip_initial_sync=args.watch_only))
    except KeyboardInterrupt:
        log.info("👋 Dihentikan oleh pengguna (Ctrl+C).")


if __name__ == "__main__":
    main()
