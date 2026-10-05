"""Validate exercise batches with Gemini blind N=1 or N=3 and IndoBERT diagnostics.

The exercise source is an envelope (`items`) in `batch01/soal_exercise_db.json`; the pretest scripts read a
plain array. Each class is staged under `runs/exercise_validation/<batch>/<class>_exercise_<batch>/`, validated
with the shared pretest workflow, and the verified bundle is copied to
`output/exercise/<class>/<batch>/hasil_validasi/`. A meta-oriented view keyed by `_id`
(same keys as `soal_exercise_meta.json`) is written beside it.

Subcommands: run (pilot + full + publication), stage, pilot, full, package,
progress (publish complete and draft items), meta, status. Live commands require --execute.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.llm.config import GeminiSettings
from app.silver.exports import confidence_policy_for
from app.llm.silver import (silver_rubric, SilverRunResult, aggregate_silver_runs,
                           requested_runs_for, requested_run_indices)
from scripts.generate_silver_labels_kelas1 import atomic_write, load_checkpoint, summarize
from scripts.refresh_ai_validation_reports import digest, load, verify_evidence, verify_bundle
from scripts.revalidate_all_grades import complete, run_script
from scripts.export_revalidation_progress import export_class
from scripts.build_blind_validation_bundle import source_class_matches

CLASSES = {"kelas5": (5, "regular"), "kelas7": (7, "regular"), "kelas8": (8, "regular"),
           "kelas9": (9, "regular"), "kelas10": (10, "regular"), "kelas11_tl": (11, "tl"),
           "kelas12": (12, "regular")}
LEVELS = ("easy", "medium", "hard")


def paths(name: str, batch: str) -> dict[str, Path]:
    if name not in CLASSES or not re.fullmatch(r"batch[0-9]+", batch):
        raise ValueError("class must be supported and batch must have the form batch01")
    exercise = ROOT / "output/exercise" / name / batch
    stage = ROOT / "runs/exercise_validation" / batch / f"{name}_exercise_{batch}"
    return {"exercise": exercise, "stage": stage, "source": stage / "soal_exercise_db.json",
            "checkpoint": stage / "silver_labels.json", "final": exercise / "hasil_validasi"}


def stage_class(name: str, batch: str) -> list[dict]:
    p = paths(name, batch)
    envelope = load(p["exercise"] / "soal_exercise_db.json")
    items = envelope["items"]
    grade, track = CLASSES[name]
    if envelope.get("book") != name or envelope.get("batch") != int(batch[5:]):
        raise ValueError("exercise envelope class/batch differs from its directory")
    if any(not source_class_matches(i.get("kelas_id"), grade, track) for i in items):
        raise ValueError("exercise rows have a different grade or track")
    ids = [str(i["_id"]) for i in items]
    assert len(ids) == len(set(ids)), f"duplicate IDs in {name}"
    assert all(not i.get("image_url") for i in items), "exercise validation expects text-only items"
    assert all(i.get("cognitive_level") is None and i.get("jawaban") for i in items)
    meta = load(p["exercise"] / "soal_exercise_meta.json")
    assert set(meta) == set(ids), f"meta/db mismatch in {name}"
    if any(info.get("batch") != int(batch[5:]) or info.get("level_target") not in LEVELS for info in meta.values()):
        raise ValueError("exercise metadata has an invalid batch or target level")
    p["stage"].mkdir(parents=True, exist_ok=True)
    target = p["source"]
    text = json.dumps(items, ensure_ascii=False, indent=2) + "\n"
    if not target.exists() or target.read_text(encoding="utf-8") != text:
        if p["checkpoint"].exists():
            raise ValueError("source changed after checkpoint creation; use a new batch name")
        target.write_text(text, encoding="utf-8")
    return items


def pilot_ids(items: list[dict], meta: dict, count: int) -> list[str]:
    """One median-length item per target level; targets never enter the Gemini prompt."""
    chosen = []
    for level in LEVELS:
        pool = sorted((i for i in items if meta[str(i["_id"])]["level_target"] == level),
                      key=lambda i: len(i["soal_text"]), reverse=True)
        if pool:
            chosen.append(str(pool[len(pool) // 2]["_id"]))
    return chosen[:count]


def run_labeler(name: str, batch: str, extra: list[str], max_calls: int, max_output_tokens: int = 4096) -> int:
    grade, track = CLASSES[name]
    p = paths(name, batch)
    args = [sys.executable, str(ROOT / "scripts/generate_silver_labels_kelas1.py"), "--source", str(p["source"]),
            "--output", str(p["checkpoint"]), "--grade", str(grade), "--track", track,
            "--runs", str(load(p["checkpoint"]).get("requestedRuns", 3)),
            "--workers", "1", "--attempts", "2", "--pause", "0.5", "--stop-on-quota",
            "--max-consecutive-provider-failures", "3",
            "--max-api-calls", str(max_calls), "--execute", *extra]
    log = p["stage"] / "labeling.log"
    # Higher-grade reasoning consumed the previous 1200-token cap before JSON
    # was complete. Keep this override local to exercise, without editing .env.
    environment = dict(os.environ, GEMINI_MAX_OUTPUT_TOKENS=str(max_output_tokens))
    with log.open("a", encoding="utf-8") as stream:
        return subprocess.run(args, cwd=ROOT, env=environment, stdout=stream, stderr=subprocess.STDOUT).returncode


def label_phase(name: str, batch: str, selected: list[str], budget: int, max_output_tokens: int) -> tuple[int, int]:
    """Retry incomplete responses without repeating paid successes or crossing quota stops."""
    p = paths(name, batch)
    all_ids = [str(item["_id"]) for item in load(p["source"])]
    # Avoid passing thousands of IDs beyond Windows' command-line limit.
    extra = [] if selected == all_ids else [a for qid in selected for a in ("--question-id", qid)]
    for pass_index in range(1, 4):
        before = load(p["checkpoint"])
        if complete(before, selected):
            return 0, budget
        if budget <= 0:
            return 4, budget
        code = run_labeler(name, batch, extra, budget, max_output_tokens)
        after = load(p["checkpoint"])
        spent = after.get("apiAttempts", 0) - before.get("apiAttempts", 0)
        budget -= spent
        print(f"{name}: pass={pass_index} exit={code} status={after.get('executionStatus')} remainingCalls={budget}", flush=True)
        if code != 0:
            return code, budget
        if complete(after, selected):
            return 0, budget
        if spent == 0:
            break
    # A provider invocation may exit 0 with invalid JSON still pending. This
    # is not a completed class; retain drafts and continue other classes.
    return 5, budget


def migrate_to_single_run(name: str, batch: str) -> dict:
    """Archive N=3 evidence; preserve final decisions and reuse one paid pending run."""
    p = paths(name, batch)
    grade, track = CLASSES[name]
    previous_bytes = p["checkpoint"].read_bytes()
    previous = json.loads(previous_bytes)
    if previous.get("requestedRuns", 3) == 1:
        return previous
    verify_evidence(p["source"], p["checkpoint"], grade)
    if (p["final"] / "manifest.json").exists():
        verify_bundle(p["source"], p["final"])
    archive = p["stage"] / "history" / ("before_n1_" + hashlib.sha256(previous_bytes).hexdigest()[:20])
    archive.mkdir(parents=True, exist_ok=True)
    locked = archive / "silver_labels.json"
    if not locked.exists():
        locked.write_bytes(previous_bytes)
    if locked.read_bytes() != previous_bytes:
        raise ValueError("N=3 archive differs from the paid checkpoint")
    if p["final"].exists() and not (archive / "hasil_validasi").exists():
        shutil.copytree(p["final"], archive / "hasil_validasi")
    checkpoint = deepcopy(previous)
    retained, reused = 0, 0
    for qid, record in checkpoint["items"].items():
        if complete(previous, [qid]):
            record["requestedRuns"] = 3
            retained += 1
            continue
        runs = record.get("runs", [])
        chosen = next((run for run in runs if run.get("status") == "success"),
                      next((run for run in runs if run["runIndex"] == 1), None))
        record["previousN3Evidence"] = {"runs": [run for run in runs if run is not chosen],
                                       "adjudication": record.get("adjudication")}
        record["runs"] = [chosen] if chosen else []
        record["adjudication"] = None
        record["requestedRuns"] = 1
        record["requestedRunIndices"] = [chosen["runIndex"] if chosen else 1]
        record["aggregate"] = aggregate_silver_runs(
            [SilverRunResult.model_validate(run) for run in record["runs"]], requested_runs=1)
        reused += bool(chosen and chosen.get("status") == "success")
    checkpoint.update(requestedRuns=1, executionStatus="queued_single_run_resume",
                      updatedAt=datetime.now(timezone.utc).isoformat())
    checkpoint.pop("stopReason", None)
    checkpoint["runPolicyMigration"] = {
        "fromRuns": 3, "toRuns": 1, "createdAt": checkpoint["updatedAt"],
        "previousCheckpoint": str(locked), "previousCheckpointSha256": digest(locked),
        "retainedFinalN3Items": retained, "reusedPendingPaidRuns": reused,
        "singleRunConfidence": "null", "automaticSingleRunAdjudication": False}
    checkpoint["summary"] = summarize(checkpoint)
    atomic_write(checkpoint, p["checkpoint"])
    verify_evidence(p["source"], p["checkpoint"], grade)
    return checkpoint


def init_checkpoint(name: str, batch: str, runs: int | None = None) -> dict:
    grade, track = CLASSES[name]
    p = paths(name, batch)
    settings = GeminiSettings.from_environment()
    existing = load(p["checkpoint"]) if p["checkpoint"].exists() else {}
    requested = runs if runs is not None else existing.get("requestedRuns", 3)
    if requested == 1 and existing.get("requestedRuns") == 3:
        if existing.get("model") != settings.model:
            raise ValueError("model differs from the existing paid checkpoint")
        migrate_to_single_run(name, batch)
    checkpoint = load_checkpoint(p["checkpoint"], p["source"], digest(p["source"]), settings.model, requested, grade, track=track)
    if not p["checkpoint"].exists():
        checkpoint.update(executionStatus="queued", summary=summarize(checkpoint))
        atomic_write(checkpoint, p["checkpoint"])
    return checkpoint


def meta_view(name: str, batch: str) -> dict:
    """Per-_id view in the shape of soal_exercise_meta.json plus the validation outcome."""
    p = paths(name, batch)
    meta = load(p["exercise"] / "soal_exercise_meta.json")
    rows = {str(r["_id"]): r for r in load(p["final"] / "validation_results.json")}
    export = load(p["final"] / "manifest.json")["databaseExport"]
    progress = load(p["final"] / "export_status.json") if (p["final"] / "export_status.json").exists() else None
    progress_by_id = {item["questionId"]: item for item in progress["items"]} if progress else {}
    out, crosstab = {}, defaultdict(Counter)
    for qid, info in meta.items():
        row, extra = rows[qid], export["metadataByQuestionId"][qid]
        level = row["cognitive_level"]
        match = None if level is None else level == info["level_target"]
        crosstab[info["level_target"]][level or "undecided"] += 1
        item_progress = progress_by_id.get(qid, {})
        out[qid] = {**info, "validasi": {
            "cognitive_level": level, "cognitive_score": row["cognitive_score"],
            "confidence_score": row["confidence_score"], "status": row["status"],
            "validation_status": extra["validation_status"], "level_sesuai_target": match,
            "math_cognitive_domain": extra["math_cognitive_domain"],
            "knowledge_dimension": extra["knowledge_dimension"],
            "intended_difficulty": extra["intended_difficulty"],
            "final_label_supporting_runs": extra["final_label_supporting_runs"],
            "decision_id": extra["decision_id"], "label_provenance": extra["label_provenance"],
            "full_complete": item_progress.get("fullComplete", True),
            "successful_run_indices": item_progress.get("successfulRunIndices", [1, 2, 3]),
            "missing_run_indices": item_progress.get("missingRunIndices", []),
            "needs_adjudication": item_progress.get("needsAdjudication", False)}}
        requested = item_progress.get("requestedRuns", 3)
        out[qid]["validasi"].update(
            requested_runs=requested, validation_method=item_progress.get("validationMethod", "blind_n3_with_ai_adjudication"),
            consistency_measured=item_progress.get("consistencyMeasured", False),
            confidence_status=("draft" if not item_progress.get("fullComplete", True) else
                               extra.get("confidence_status", "model_support_unavailable") if requested == 1 else "inter_run_support"),
            training_evidence_qualified=bool(requested == 3 and row["status"] == "active"))
        if requested == 1:
            for key in ("confidence_method", "confidence_available", "confidence_final_label_probabilities"):
                out[qid]["validasi"][key] = extra[key]
    atomic_write(out, p["final"] / "validation_results_meta.json")
    total = len(out)
    lines = [f"# Ringkasan validasi exercise {name} {batch}", "",
             f"Soal: {total}. Metode per soal tercatat di validasi.requested_runs: N=1 satu penilaian; N=3 + adjudikasi AI; IndoBERT sebagai diagnostik "
             "dengan scope sesuai manifest artifact. `level_target` dari generator hanya dipakai untuk "
             "perbandingan setelah label dikunci; ia tidak dikirim ke penilai.", "",
             "## level_target (generator) vs cognitive_level (validasi AI)", "",
             "| Target | easy | medium | hard | undecided | Sesuai |", "|---|---:|---:|---:|---:|---:|"]
    for level in LEVELS:
        row = crosstab[level]
        n = sum(row.values())
        lines.append(f"| {level} | {row['easy']} | {row['medium']} | {row['hard']} | {row['undecided']} | "
                     f"{row[level]}/{n} |")
    status = Counter(v["validasi"]["status"] for v in out.values())
    routing = Counter(v["validasi"]["validation_status"] for v in out.values())
    lines += ["", f"Status: {dict(status)}. Routing: {dict(routing)}.", "",
              f"Keputusan lengkap: {sum(v['validasi']['full_complete'] for v in out.values())}/{total}. "
              "Soal yang belum lengkap tetap inactive dengan label/score null dan confidence 0; "
              "0 menyatakan belum ada dukungan untuk label final, bukan probabilitas IndoBERT. "
              "Confidence N=1 memakai round(100 * min(probabilitas IndoBERT untuk label akhir Gemini tiap head)); "
              "ini dukungan model, bukan konsistensi antar-run atau akurasi terukur. Nilai 0 saat probabilitas tidak tersedia "
              "ditandai confidence_available=false; dukungan sangat kecil juga dapat dibulatkan menjadi 0. "
              "Hasil N=3 terdahulu dipertahankan.", "",
              "`level_sesuai_target` false bukan kesalahan: level generator adalah perkiraan awal; "
              "label validasi memakai rubrik relatif kelas. Hanya `status == active` boleh dipakai delivery.", ""]
    (p["final"] / "RINGKASAN_VALIDASI.md").write_text("\n".join(lines), encoding="utf-8")
    return {"class": name, "total": total, "status": dict(status), "routing": dict(routing),
            "crosstab": {k: dict(v) for k, v in crosstab.items()}}


def package(name: str, batch: str, *, allow_partial: bool = False) -> dict:
    grade, _ = CLASSES[name]
    p = paths(name, batch)
    checkpoint_bytes = p["checkpoint"].read_bytes()
    checkpoint = json.loads(checkpoint_bytes)
    checkpoint_hash = hashlib.sha256(checkpoint_bytes).hexdigest()
    items = load(p["source"])
    if not allow_partial and not complete(checkpoint, [str(i["_id"]) for i in items]):
        raise SystemExit(f"{name}: penilaian sesuai mode tiap soal belum lengkap; jalankan `full` dahulu")
    # Each paid checkpoint gets an immutable snapshot; progress reports can be resumed.
    snapshot = p["stage"] / "snapshots" / checkpoint_hash[:20]
    bundle, locked = snapshot / "bundle", snapshot / "silver_labels.json"
    for previous in sorted(snapshot.glob("bundle_retry_*")):
        if (previous / "manifest.json").is_file():
            bundle = previous
            break
    if not locked.exists():
        snapshot.mkdir(parents=True, exist_ok=True)
        temporary = locked.with_suffix(".json.tmp")
        temporary.write_bytes(checkpoint_bytes)
        temporary.replace(locked)
    if digest(locked) != checkpoint_hash:
        raise ValueError("locked exercise checkpoint differs from the captured bytes")
    verify_evidence(p["source"], locked, grade)
    if not (bundle / "manifest.json").exists():
        if not (snapshot / "audit/pilot_audit.json").exists():
            run_script("audit_grade_aware_pilot.py", ["--source", str(p["source"]), "--checkpoint", str(locked),
                       "--grade", str(grade), "--output-dir", str(snapshot / "audit")], p["stage"] / "audit.log", accepted=(0, 2))
        if bundle.exists() and any(bundle.iterdir()):
            index = 1
            while (snapshot / f"bundle_retry_{index}").exists():
                index += 1
            bundle = snapshot / f"bundle_retry_{index}"
        run_script("build_blind_validation_bundle.py", ["--source", str(p["source"]), "--checkpoint", str(locked),
                   "--audit", str(snapshot / "audit/pilot_audit.json"), "--output-dir", str(bundle)], p["stage"] / "package.log")
    verify_bundle(p["source"], bundle)
    if checkpoint.get("requestedRuns", 3) == 1:
        from app.silver.exports import load_decision_bundle
        from scripts.compact_validation_results import compact_bundle
        expected_policy = confidence_policy_for(load_decision_bundle(bundle)["items"])
        if load(bundle / "manifest.json")["databaseExport"]["confidencePolicy"] != expected_policy:
            # Preserve the historical export alongside a separately versioned
            # numeric-confidence bundle; paid evidence and predictions stay intact.
            numeric_bundle = snapshot / "bundle_numeric_confidence_v3"
            if not numeric_bundle.exists():
                shutil.copytree(bundle, numeric_bundle)
            compact_bundle(p["source"], numeric_bundle)
            bundle = numeric_bundle
            verify_bundle(p["source"], bundle)
    if (p["final"] / "manifest.json").exists():
        verify_bundle(p["source"], p["final"])
    shutil.copytree(bundle, p["final"], dirs_exist_ok=True)
    evidence = p["final"] / "bukti_validasi"
    shutil.copy2(locked, evidence / "silver_labels.json")
    for filename in ("pilot_audit.json", "PILOT_AUDIT.md"):
        shutil.copy2(snapshot / "audit" / filename, evidence / filename)
    progress = export_class(p["source"], locked, p["final"], grade=grade, track=CLASSES[name][1])
    progress["class"] = name
    progress["exerciseBatch"] = batch
    atomic_write(progress, p["final"] / "export_status.json")
    result = meta_view(name, batch)
    readme = p["final"] / "README.md"
    if readme.exists():
        readme.write_text(readme.read_text(encoding="utf-8").replace("soal_pretest_db.json", "soal_exercise_db.json (items)") +
                          "\n\nExercise: lihat `RINGKASAN_VALIDASI.md`, `validation_results_meta.json` dan `export_status.json`. "
                          "Metadata asli terhubung lewat `_id`. Periksa fullComplete sebelum menyatakan batch selesai.\n", encoding="utf-8")
    manifest = load(p["final"] / "manifest.json")
    manifest["fullComplete"] = progress["fullComplete"]
    manifest["status"] = progress["status"]
    manifest["exercise"] = {"batch": batch, "class": name, "origin": "exercise",
                            "metaJoinKey": "_id", "generatorTargetsUsedForVoting": False,
                            "generatorExplanationIsVerifiedEvidence": False}
    manifest["exercise"]["defaultRequestedRuns"] = checkpoint.get("requestedRuns", 3)
    if checkpoint.get("runPolicyMigration"):
        migration = checkpoint["runPolicyMigration"]
        manifest["exercise"]["runPolicyMigration"] = migration
        manifest["sourceFiles"]["previousN3Checkpoint"] = {
            "path": migration["previousCheckpoint"], "sha256": migration["previousCheckpointSha256"]}
    for key, filename in (("exerciseEnvelope", "soal_exercise_db.json"), ("exerciseMetadata", "soal_exercise_meta.json")):
        original = p["exercise"] / filename
        manifest["sourceFiles"][key] = {"path": str(original), "sha256": digest(original)}
    for filename in ("validation_results.json", "validation_results_meta.json", "RINGKASAN_VALIDASI.md", "export_status.json",
                     "bukti_validasi/silver_labels.json", "bukti_validasi/pilot_audit.json", "bukti_validasi/PILOT_AUDIT.md", "README.md"):
        target = p["final"] / filename
        manifest["outputs"][filename] = {"sha256": digest(target), "bytes": target.stat().st_size}
    atomic_write(manifest, p["final"] / "manifest.json")
    verify_bundle(p["source"], p["final"])
    return {**result, "fullComplete": progress["fullComplete"], "progress": progress["summary"],
            "checkpointExecutionStatus": checkpoint.get("executionStatus"),
            "apiAttempts": checkpoint.get("apiAttempts", 0), "stopReason": checkpoint.get("stopReason"),
            "labelingSummary": checkpoint.get("summary", {}),
            "outputDirectory": str(p["final"].relative_to(ROOT))}


def publish_progress(classes: list[str], batch: str) -> None:
    reports = []
    for name in classes:
        report = package(name, batch, allow_partial=True)
        reports.append(report)
        print(json.dumps(report, ensure_ascii=False), flush=True)
    destination = ROOT / "runs/exercise_validation" / batch
    previous_path = destination / "progress.json"
    if previous_path.exists():
        previous = {r["class"]: r for r in load(previous_path).get("classes", [])}
        previous.update({r["class"]: r for r in reports})
        reports = [previous[name] for name in CLASSES if name in previous]
    atomic_write({"batch": batch, "classes": reports,
                  "summary": {"questionCount": sum(r["total"] for r in reports),
                              "finalItems": sum(r["progress"]["finalItems"] for r in reports),
                              "draftItems": sum(r["progress"]["draftItems"] for r in reports),
                              "apiAttempts": sum(r["apiAttempts"] for r in reports),
                              "allClassesComplete": all(r["fullComplete"] for r in reports)}}, destination / "progress.json")
    lines = [f"# Progres validasi exercise {batch}", "", "Gemini blind sesuai mode per soal (N=1 atau N=3) → qualification → IndoBERT diagnostik.", "",
             "| Kelas | Soal | Final | Draft | Active | Status checkpoint |", "|---|---:|---:|---:|---:|---|"]
    for report in reports:
        folder = ROOT / report["outputDirectory"]
        link = Path(os.path.relpath(folder / "RINGKASAN_VALIDASI.md", destination)).as_posix()
        lines.append(f"| [{report['class']}]({link}) | {report['total']} | {report['progress']['finalItems']} | "
                     f"{report['progress']['draftItems']} | {report['status'].get('active', 0)} | {report['checkpointExecutionStatus']} |")
    lines += ["", "Final berarti run sesuai mode tiap soal dan adjudikasi N=3 yang diperlukan sudah lengkap; soal final dengan blocker konten tetap inactive. N=1 tidak menambah adjudikasi otomatis; confidence numeriknya mengukur dukungan IndoBERT untuk label Gemini. Konsistensi antar-run tetap tidak terukur.",
              "Draft bukan hasil validasi selesai. Label/score null dan confidence 0 menandai keputusan yang belum lengkap.",
              "Status checkpoint completed_batch dapat hanya mencakup sampel; kolom Final menunjukkan kelengkapan seluruh kelas.",
              "IndoBERT yang tersedia hanya mencakup kelas 1–6 reguler. Kelas di luar scope mencatat abstain/out_of_scope.", "",
              ]
    for report in reports:
        if report["stopReason"]:
            lines += [f"Provider stop pada {report['class']}: `{json.dumps(report['stopReason'], ensure_ascii=False)}`.", ""]
    lines += ["Melanjutkan dengan kredensial/kuota yang tersedia:", "", "```powershell",
              r".\.venv\Scripts\python.exe -X utf8 scripts/validate_exercise_batch.py run --max-api-calls 20000 --execute", "```", ""]
    (destination / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=("stage", "pilot", "full", "package", "progress", "run", "meta", "status"))
    ap.add_argument("--classes", nargs="+", default=list(CLASSES), choices=list(CLASSES))
    ap.add_argument("--batch", default="batch01")
    ap.add_argument("--max-api-calls", type=int, default=2500)
    ap.add_argument("--max-output-tokens", type=int, default=4096, choices=range(128, 4097), metavar="128..4096")
    ap.add_argument("--pilot-count", type=int, default=3)
    ap.add_argument("--runs", type=int, choices=(1, 3),
                    help="Initial evaluations per new item; preserve the current checkpoint mode when omitted. N=1 retains completed N=3 history.")
    ap.add_argument("--execute", action="store_true", help="Required for live Gemini calls")
    args = ap.parse_args()
    live = args.command in ("pilot", "full", "run")
    if live and not args.execute:
        ap.error("pilot/full make paid Gemini calls and require --execute")
    budget = args.max_api_calls
    if live and budget < 1:
        ap.error("max-api-calls must be positive")
    if args.command in ("run", "progress"):
        for name in args.classes:
            stage_class(name, args.batch)
            init_checkpoint(name, args.batch, args.runs)
        if args.command == "run":
            code = 0
            unresolved = False
            for phase in ("pilot", "full"):
                for name in args.classes:
                    p = paths(name, args.batch)
                    items = load(p["source"])
                    ids = [str(i["_id"]) for i in items]
                    selected = pilot_ids(items, load(p["exercise"] / "soal_exercise_meta.json"), args.pilot_count) if phase == "pilot" else ids
                    if complete(load(p["checkpoint"]), selected):
                        continue
                    code, budget = label_phase(name, args.batch, selected, budget, args.max_output_tokens)
                    if code == 5:
                        print(f"{name}: {phase} remains incomplete after bounded retries; retained as draft", flush=True)
                        unresolved = True
                        code = 0
                        continue
                    if code != 0 or budget <= 0:
                        code = code or 4
                        break
                    if phase == "full":
                        print(json.dumps(package(name, args.batch), ensure_ascii=False), flush=True)
                if code:
                    break
            publish_progress(args.classes, args.batch)
            if code:
                return code
            if unresolved:
                for name in args.classes:
                    p = paths(name, args.batch)
                    if not complete(load(p["checkpoint"]), [str(i["_id"]) for i in load(p["source"])]):
                        return 5
            return 0
        publish_progress(args.classes, args.batch)
        return 0
    for name in args.classes:
        grade, track = CLASSES[name]
        silver_rubric(grade, track=track)
        items = stage_class(name, args.batch)
        p = paths(name, args.batch)
        ids = [str(i["_id"]) for i in items]
        if args.command == "stage":
            init_checkpoint(name, args.batch, args.runs)
            print(f"{name}: staged {len(items)} soal -> {p['source'].relative_to(ROOT)}")
        elif args.command == "status":
            cp = load(p["checkpoint"]) if p["checkpoint"].exists() else {"items": {}}
            done = sum(complete(cp, [i]) for i in ids)
            print(f"{name}: {done}/{len(ids)} lengkap, apiAttempts={cp.get('apiAttempts', 0)}, "
                  f"status={cp.get('executionStatus')}, hasil_validasi={p['final'].exists()}")
        elif live:
            init_checkpoint(name, args.batch, args.runs)
            meta = load(p["exercise"] / "soal_exercise_meta.json")
            selected = pilot_ids(items, meta, args.pilot_count) if args.command == "pilot" else ids
            extra = [a for qid in selected for a in ("--question-id", qid)] if args.command == "pilot" else []
            if complete(load(p["checkpoint"]), selected):
                print(f"{name}: {args.command} sudah lengkap")
                continue
            before = load(p["checkpoint"]).get("apiAttempts", 0)
            code = run_labeler(name, args.batch, extra, budget, args.max_output_tokens)
            after = load(p["checkpoint"])
            budget -= after.get("apiAttempts", 0) - before
            print(f"{name}: exit={code} status={after.get('executionStatus')} apiAttempts={after.get('apiAttempts')}")
            if code != 0 or budget <= 0:
                return code or 4
        elif args.command == "package":
            print(json.dumps(package(name, args.batch), ensure_ascii=False))
        elif args.command == "meta":
            print(json.dumps(meta_view(name, args.batch), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
