"""Read checkpoints and published results for the 2,028 replenishment candidates."""
from collections import Counter
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.revalidate_all_grades import complete
from app.services.exercise.workflow import atomic_json

RUN = ROOT / "runs/exercise_replenishment/codex_batch01"


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def snapshot():
    progress = read(RUN / "progress.json")
    rows, shortages = [], []
    jobs = read(RUN / "jobs.json")
    for name in progress["classes"]:
        ids = {hashlib.md5(i.encode()).hexdigest()[:24]
               for key, job in progress["jobs"].items() if key.startswith(name + "-") for i in job["ids"]}
        candidates = []
        for namespace in ("", "failover/", "groq/"):
            path = ROOT / f"runs/exercise_validation/{namespace}batch01/{name}_exercise_batch01/silver_labels.json"
            if path.exists():
                cp = read(path)
                candidates.append((sum(complete(cp, [qid]) for qid in ids), cp))
        done, cp = max(candidates, key=lambda pair: pair[0]) if candidates else (0, {})
        base = ROOT / "output/exercise" / name / "batch01"
        final = base / "hasil_validasi/validation_results.json"
        published = read(final) if final.exists() else []
        final_meta_path = base / "hasil_validasi/validation_results_meta.json"
        final_meta = read(final_meta_path) if final_meta_path.exists() else {}
        new = [q for q in published if str(q["_id"]) in ids]
        counts = Counter(q.get("status") for q in new)
        labeled = sum(final_meta.get(str(q["_id"]), {}).get("validasi", {}).get("full_complete") is True for q in new)
        rows.append({"class": name, "target": len(ids), "completed": done,
                     "pending": len(ids)-done, "publishedActive": counts["active"],
                     "publishedInactiveDecisions": max(0, labeled-counts["active"]),
                     "unpublishedDecisions": max(0, done-labeled),
                     "checkpointStatus": cp.get("executionStatus", "not_started")})
        meta = read(base / "soal_exercise_meta.json")
        stock = Counter((meta[str(q["_id"])]["bab_id"], meta[str(q["_id"])]["subbab_kode"], q.get("cognitive_level"))
                        for q in published if q.get("status") == "active")
        for job in jobs:
            if job["class_key"] != name:
                continue
            chapter = f"{'SD' if name in ('kelas5','kelas6') else 'SMP' if name in ('kelas7','kelas8','kelas9') else 'SMA'}{name[5:].replace('_tl','TL')}-B{job['chapter_no']}"
            # Metadata is authoritative for chapter identity, including TL naming.
            matching = {info["bab_id"] for info in meta.values()
                        if str(info.get("id", "")).startswith(f"{name}-b{job['chapter_no']:02d}-")}
            if len(matching) == 1:
                chapter = next(iter(matching))
            available = stock[(chapter, job["code"], job["level_target"])]
            if available < job["required"]:
                shortages.append({"class": name, "chapter": job["chapter_no"], "subchapter": job["code"],
                                  "level": job["level_target"], "active": available,
                                  "required": job["required"], "shortfall": job["required"]-available})
    report = {"updatedAt": datetime.now(timezone.utc).isoformat(), "scope": "new_batch01_candidates_only",
              "target": sum(r["target"] for r in rows), "completed": sum(r["completed"] for r in rows),
              "pending": sum(r["pending"] for r in rows), "classes": rows,
              "targetSlotsStillUnderThreshold": shortages,
              "note": "Local published stock; production and student attempt history are not verified. Drafts are excluded."}
    atomic_json(RUN / "validation_progress.json", report)
    lines = ["# Progres validasi soal tambahan", "", f"Diperbarui: {report['updatedAt']}", "",
             f"Selesai divalidasi: **{report['completed']} / {report['target']}**. Tersisa: **{report['pending']}**.", "",
             "Selesai divalidasi mencakup keputusan valid maupun bermasalah. Hanya active yang dihitung tersedia.", "",
             "| Kelas | Target | Selesai | Tersisa | Active terbit | Keputusan belum terbit |",
             "|---|---:|---:|---:|---:|---:|"]
    lines += [f"| {r['class']} | {r['target']} | {r['completed']} | {r['pending']} | {r['publishedActive']} | {r['unpublishedDecisions']} |" for r in rows]
    lines += ["", "Publikasi dilakukan per kelompok soal. Stok dan kekurangan masih berubah selama validasi berlangsung.",
              "Batas per subbab–level: SD 10, SMP 15, SMA 20. Level memakai hasil validator.",
              "Hasil ini berasal dari file lokal; sinkronisasi database production belum dilakukan."]
    target = RUN / "VALIDATION_PROGRESS.md"
    temp = target.with_suffix(".tmp")
    temp.write_text("\n".join(lines)+"\n", encoding="utf-8")
    temp.replace(target)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--watch", action="store_true")
    args = parser.parse_args()
    for _ in range(720 if args.watch else 1):
        report = snapshot()
        if report["pending"] == 0 and all(row["unpublishedDecisions"] == 0 for row in report["classes"]):
            subprocess.run([sys.executable, str(ROOT / "scripts/auto_inserter.py"), "--local", "--once",
                            "--report", str(RUN / "availability_after_validation.json")], cwd=ROOT, check=True)
            break
        if args.watch:
            time.sleep(60)
    if not args.watch:
        print(json.dumps({k: report[k] for k in ("target", "completed", "pending")}))


if __name__ == "__main__":
    main()
