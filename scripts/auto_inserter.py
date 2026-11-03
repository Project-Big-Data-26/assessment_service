"""Plan Mongo question imports/repairs; writes require --execute explicitly."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import sys
import time
import uuid

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.ingestion.question_sync import (  # noqa: E402
    SYNC_FIELDS, coverage, identifier, load_sources, mongo_catalog,
    plan_sync, read_json, report_catalog, source_files,
)


def write_report(path: Path, report: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + "." + uuid.uuid4().hex + ".tmp")
    try:
        temporary.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def write_inventory_markdown(path: Path, report: dict) -> None:
    inventory = report["coverage"]
    lines = ["# Audit latihan lokal berdasarkan kelas dan bab", "",
             "Sumber: ekspor hasil_validasi resmi. Bukan audit database production.",
             "Pretest, soal inactive, dan soal tanpa label tidak dihitung sebagai latihan tersedia.",
             "Ketersediaan belum dikurangi riwayat soal masing-masing siswa.", "",
             "Batas PER LEVEL dalam setiap subbab: SD 10, SMP 15, SMA 20.",
             "Bab cukup hanya jika seluruh level pada seluruh subbab memenuhi batas.", "",
             f"Bab belum cukup: {inventory['under_threshold_chapters']}/{inventory['chapters']}.",
             f"Subbab dengan level kurang: {inventory['under_threshold']}/{inventory['subchapters']}.",
             f"Kombinasi subbab-level kurang: {inventory['under_threshold_levels']}/{inventory['level_slots']}.",
             f"Total kekurangan per level: {inventory['shortfall_questions']} soal aktif.", "",
             "## Ringkasan per bab", "",
             "| Kelas | Bab | Subbab | Subbab belum cukup | Level kurang | Kekurangan soal |",
             "|---|---:|---:|---:|---:|---:|"]
    for row in inventory["chapter_rows"]:
        lines.append(f"| {row['class_key']} | {row['chapter_no']} | {row['subchapters']} | "
                     f"{row['deficient_subchapters']} | {row['deficient_levels']} | {row['shortfall']} |")
    lines += ["", "## Rincian per subbab dan level", "",
              "| Kelas | Bab | Kode | Subbab | Minimum per level | Easy tersedia | Kurang E | Medium tersedia | Kurang M | Hard tersedia | Kurang H |",
              "|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|"]
    for row in inventory["rows"]:
        levels, deficits = row["levels"], row["level_shortfalls"]
        name = row["name"].replace("|", "\\|")
        lines.append(f"| {row['class_key']} | {row['chapter_no']} | {row['code']} | {name} | "
                     f"{row['required']} | {levels['easy']} | {deficits['easy']} | "
                     f"{levels['medium']} | {deficits['medium']} | {levels['hard']} | {deficits['hard']} |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def live_snapshot(db) -> dict:
    return {"kelas": list(db.kelas.find({})), "bab": list(db.bab.find({})),
            "subbab": list(db.subbab.find({})),
            "soal": list(db.soal.find({}, {key: 1 for key in SYNC_FIELDS}))}


def apply_plan(db, plan: dict, questions) -> dict:
    """Update controlled fields only; never replace/delete an existing question."""
    from bson import ObjectId
    from pymongo import UpdateOne

    if plan["blocked"]:
        raise ValueError("Rencana diblokir: selesaikan semua kesalahan pemetaan terlebih dahulu")
    sources = {question.qid: question.item for question in questions}
    operations = []

    def db_fields(fields):
        return {key: ObjectId(value) if key in ("kelas_id", "subbab_id") and value else value
                for key, value in fields.items()}

    for change in plan["changes"]:
        qid = change["_id"]
        values = db_fields(change["after"])
        if change["action"] == "insert":
            source = sources[qid]
            allowed = ("berkas_id", "soal_text", "image_url", "options", "jawaban",
                       "soal_type", "matching_pairs")
            document = {key: source[key] for key in allowed if key in source}
            document.update(values)
            document["_id"] = ObjectId(qid)
            for field in ("created_at", "updated_at"):
                raw = source.get(field)
                document[field] = (datetime.fromisoformat(raw.replace("Z", "+00:00"))
                                   if isinstance(raw, str) else datetime.now(timezone.utc))
            operations.append(UpdateOne({"_id": ObjectId(qid)}, {"$setOnInsert": document}, upsert=True))
        else:
            # Compare-and-set prevents silently overwriting a concurrent edit.
            expected = {"_id": ObjectId(qid), **db_fields(change["before"])}
            operations.append(UpdateOne(expected, {"$set": values}, upsert=False))
    if not operations:
        return {"matched": 0, "modified": 0, "inserted": 0}
    result = db.soal.bulk_write(operations, ordered=True)
    if result.matched_count != plan["updates"] or result.upserted_count != plan["inserts"]:
        raise ValueError("Data berubah saat penerapan; sebagian operasi mungkin selesai. Audit ulang memakai rencana tersimpan")
    return {"matched": result.matched_count, "modified": result.modified_count,
            "inserted": result.upserted_count}


def sync_once(args, db=None) -> dict:
    questions = load_sources(args.output)
    if args.file:
        target = args.file.resolve().relative_to(args.output.resolve()).as_posix()
        if args.file.resolve() not in {p.resolve() for p in source_files(args.output)}:
            raise ValueError("--file harus berupa ekspor hasil_validasi resmi")
        questions = [question for question in questions if question.source == target]
        if not questions:
            raise ValueError("Tidak ada soal utama pada --file")
    if args.local:
        report = {"mode": "local_inventory", "unique_questions": len(questions),
                  "exercise": sum(q.kind == "exercise" for q in questions),
                  "pretest": sum(q.kind == "pretest" for q in questions),
                  "coverage": coverage(questions, report_catalog(args.curriculum_report))}
    else:
        snapshot = read_json(args.snapshot) if args.snapshot else live_snapshot(db)
        catalog = read_json(args.catalog) if args.catalog else snapshot.get("catalog")
        if catalog is None:
            catalog = mongo_catalog(snapshot["kelas"], snapshot["bab"], snapshot["subbab"], args.chapter_number_field)
        report = plan_sync(questions, catalog, snapshot["soal"])
        report["mode"] = "execute" if args.execute else "dry_run"
        report["database"] = db.name if db is not None else "offline_snapshot"
        known = {q.qid for q in questions}
        report["unmatched_database_ids"] = [identifier(q["_id"]) for q in snapshot["soal"]
                                            if identifier(q["_id"]) not in known]
        report["plan_sha256"] = hashlib.sha256(
            json.dumps(report, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    report["created_at"] = datetime.now(timezone.utc).isoformat()
    # Save before-values and IDs BEFORE database mutation.
    write_report(args.report, report)
    if args.local:
        write_inventory_markdown(args.report.with_suffix(".md"), report)
    if args.execute:
        report["execution"] = apply_plan(db, report, questions)
        write_report(args.report, report)
    summary = {k: v for k, v in report.items() if k in (
        "mode", "questions", "unique_questions", "exercise", "pretest", "inserts", "updates", "blocked", "unchanged", "execution")}
    if args.local:
        summary["under_threshold"] = report["coverage"]["under_threshold"]
        summary["under_threshold_levels"] = report["coverage"]["under_threshold_levels"]
        summary["under_threshold_chapters"] = report["coverage"]["under_threshold_chapters"]
    print(json.dumps(summary, ensure_ascii=False))
    print(f"Report: {args.report}")
    return report


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "output")
    parser.add_argument("--file", type=Path, help="Batasi ke satu ekspor resmi")
    parser.add_argument("--local", action="store_true", help="Inventaris lokal tanpa koneksi MongoDB")
    parser.add_argument("--curriculum-report", type=Path, default=ROOT / "API_DOCUMENTATION/Pesan_eror.md")
    parser.add_argument("--snapshot", type=Path, help="JSON: kelas, bab, subbab, soal; atau catalog dan soal")
    parser.add_argument("--catalog", type=Path, help="Pemetaan ID eksplisit jika skema katalog berbeda")
    parser.add_argument("--chapter-number-field", default="nomor_bab")
    parser.add_argument("--execute", action="store_true", help="Terapkan rencana ke DB tujuan")
    parser.add_argument("--watch", action="store_true", help="Pantau perubahan; tanpa --execute hanya audit")
    parser.add_argument("--watch-only", action="store_true", help="Pantau tanpa sinkronisasi awal")
    parser.add_argument("--once", action="store_true", help="Satu kali proses (mode bawaan)")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args(argv)
    if args.execute and (args.local or args.snapshot):
        parser.error("--execute tidak dapat digunakan bersama --local/--snapshot")
    if args.watch_only:
        args.watch = True
    if args.watch and (args.snapshot or args.local or args.once):
        parser.error("--watch tidak dapat digabung dengan --local/--snapshot/--once")
    if args.local and (args.snapshot or args.catalog):
        parser.error("--local tidak menggunakan snapshot/katalog ID database")
    client = db = None
    try:
        if not args.local and not args.snapshot:
            from dotenv import load_dotenv
            from pymongo import MongoClient

            load_dotenv(ROOT / ".env")
            uri, database = os.getenv("MONGODB_URI", ""), os.getenv("MONGODB_DATABASE", "")
            if not uri or not database or any(token in uri.casefold() for token in ("replace-me", "example.mongodb.net")):
                raise ValueError("MONGODB_URI/MONGODB_DATABASE belum dikonfigurasi untuk database tujuan; gunakan --local atau --snapshot")
            client = MongoClient(uri, serverSelectionTimeoutMS=10000)
            db = client[database]
        requested_report = args.report

        def run():
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
            args.report = (requested_report.with_name(f"{requested_report.stem}_{stamp}{requested_report.suffix}")
                           if requested_report and args.watch else requested_report)
            args.report = args.report or ROOT / "runs/question_sync" / f"plan_{stamp}.json"
            return sync_once(args, db)

        def signatures():
            watched = source_files(args.output)
            watched += list(args.output.glob("exercise/kelas*/batch*/soal_exercise_meta.json"))
            watched += list(args.output.glob("pretest/kelas*/sesi_pretest.json"))
            if args.catalog:
                watched.append(args.catalog)
            return {p: p.stat().st_mtime_ns for p in watched}

        previous = signatures()
        report = None if args.watch_only else run()
        if not args.watch:
            return 2 if report and report.get("blocked") else 0
        print("Watcher aktif; setiap siklus memuat ulang katalog dan seluruh sumber resmi.")
        while True:
            time.sleep(5)
            current = signatures()
            if current != previous:
                run()
                previous = current
    except KeyboardInterrupt:
        return 0
    except ValueError as error:
        print(str(error), file=sys.stderr)
        return 2
    except Exception as error:
        # Driver exceptions can embed connection details. Never echo their text.
        print(f"Sinkronisasi berhenti ({type(error).__name__}); periksa skema/koneksi dan rencana tersimpan.", file=sys.stderr)
        return 2
    finally:
        if client is not None:
            client.close()


if __name__ == "__main__":
    raise SystemExit(main())
