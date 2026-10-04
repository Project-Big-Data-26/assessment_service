"""Versioned pilot and N=3 revalidation with a shared Gemini stop condition.

No target class distribution is sent to the reviewer. Successful pilot calls are
reused by the full batch; incomplete classes never replace their active results.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.llm.config import GeminiSettings
from app.llm.silver import silver_rubric
from app.psychometrics.initialization import finalize_irt_sidecar, prepare_pilot_configs
from app.training.v2.dataset import DatasetSnapshot
from scripts.generate_silver_labels_kelas1 import atomic_write, load_checkpoint, summarize
from scripts.refresh_ai_validation_reports import verify_bundle, verify_evidence, write_active_index

CLASSES = [(f"kelas{grade}", grade, "regular") for grade in range(1, 13)] + [
    ("kelas11_tl", 11, "tl"), ("kelas12_tl", 12, "tl")]


def read(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def complete(checkpoint: dict, ids: list[str]) -> bool:
    for qid in ids:
        item = checkpoint.get("items", {}).get(qid, {})
        runs = item.get("runs", [])
        successful = [r for r in runs if r.get("status") == "success"]
        if len(successful) != 3 or {r["runIndex"] for r in successful} != {1, 2, 3}:
            return False
        # A paid response saved just before aggregate creation is not complete.
        if item.get("aggregate", {}).get("needsAdjudication") is not False:
            return False
    return True


def select_pilot(questions: list[dict], old_rows: list[dict], count: int) -> list[str]:
    """Sample common and boundary items; labels are used for selection only."""
    old = {str(row["_id"]): row for row in old_rows}
    by_level = {level: [q for q in questions if old.get(str(q["_id"]), {}).get("cognitive_level") == level]
                for level in ("easy", "medium", "hard")}
    selected = []
    if by_level["easy"]:
        selected.append(by_level["easy"][len(by_level["easy"]) // 2])
    if by_level["medium"]:
        selected.append(max(by_level["medium"], key=lambda q: len(q["soal_text"])))
    if by_level["hard"]:
        selected.append(by_level["hard"][0])
    unique = {str(q["_id"]): q for q in selected}
    for q in sorted(questions, key=lambda q: len(q["soal_text"]), reverse=True):
        if len(unique) >= count:
            break
        unique.setdefault(str(q["_id"]), q)
    return list(unique)[:count]


def pilot_baseline(source: Path, directory: Path, pilot: list[str], old_entry: dict,
                   previous_results: list[dict]) -> dict[str, str | None]:
    """Preserve original labels even when a resumed class was already promoted."""
    labels = dict(old_entry.get("pilotBaselineLabels", {}))
    for result in previous_results:
        if result.get("class") == source.parent.name:
            labels.setdefault(str(result["questionId"]), result.get("oldLabel"))
    archive = directory / "final_snapshot_v1/previous_active_report/validation_results.json"
    baseline_file = archive if archive.is_file() else source.parent / "hasil_validasi/validation_results.json"
    rows = read(baseline_file) if baseline_file.is_file() else []
    original = {str(row["_id"]): row.get("cognitive_level") for row in rows}
    for qid in pilot:
        labels.setdefault(qid, original.get(qid))
    return {qid: labels[qid] for qid in pilot}


def next_training_directory(run_dir: Path) -> Path:
    """Keep all readiness reports, snapshots and model attempts reviewable."""
    candidate = run_dir / "training"
    attempt = 1
    while candidate.exists():
        attempt += 1
        candidate = run_dir / f"training_attempt_{attempt}"
    return candidate


def configure_irt_pilot(training_dir: Path, batch_name: str) -> dict | None:
    snapshot_path = training_dir / "dataset_snapshot.json"
    if not snapshot_path.is_file():
        return None
    snapshot = DatasetSnapshot.model_validate_json(snapshot_path.read_text(encoding="utf-8"))
    output = training_dir / "irt_pilot_configs.json"
    if output.is_file():
        existing = read(output)
        if existing.get("snapshotHash") != snapshot.snapshotHash:
            raise ValueError("IRT pilot configs refer to another snapshot")
        return {"path": str(output), "status": existing["status"], "snapshotHash": snapshot.snapshotHash}
    run_id = batch_name if len(batch_name) <= 40 else batch_name[:28] + "-" + hashlib.sha256(batch_name.encode()).hexdigest()[:10]
    report = prepare_pilot_configs(snapshot, run_id=run_id)
    atomic_write(report, output)
    return {"path": str(output), "status": report["status"], "snapshotHash": snapshot.snapshotHash}


def run_script(script: str, arguments: list[str], log: Path, accepted=(0,)) -> int:
    log.parent.mkdir(parents=True, exist_ok=True)
    with log.open("a", encoding="utf-8") as stream:
        result = subprocess.run([sys.executable, str(ROOT / "scripts" / script), *arguments],
                                cwd=ROOT, stdout=stream, stderr=subprocess.STDOUT)
    if result.returncode not in accepted:
        raise RuntimeError(f"{script} exited {result.returncode}; see {log}")
    return result.returncode


def package_class(source: Path, working: Path, directory: Path, *, promote: bool) -> Path:
    grade = int(read(working)["sourceGrade"])
    verify_evidence(source, working, grade)
    snapshot = directory / "final_snapshot_v1"
    bundle = snapshot / "bundle"
    locked = snapshot / "silver_labels.json"
    if locked.exists() and digest(locked) != digest(working):
        raise ValueError("locked checkpoint differs; use a fresh batch name")
    if not (bundle / "manifest.json").exists():
        snapshot.mkdir(parents=True, exist_ok=True)
        shutil.copy2(working, locked)
        run_script("audit_grade_aware_pilot.py", ["--source", str(source), "--checkpoint", str(locked),
                   "--grade", str(grade), "--output-dir", str(snapshot / "audit")],
                   directory / "audit.log", accepted=(0, 2))
        run_script("build_blind_validation_bundle.py", ["--source", str(source), "--checkpoint", str(locked),
                   "--audit", str(snapshot / "audit/pilot_audit.json"), "--output-dir", str(bundle)],
                   directory / "package.log")
    verify_bundle(source, bundle)
    evidence = bundle / "bukti_validasi"
    evidence.mkdir(exist_ok=True)
    shutil.copy2(snapshot / "silver_labels.json", evidence / "silver_labels.json")
    for name in ("pilot_audit.json", "PILOT_AUDIT.md"):
        shutil.copy2(snapshot / "audit" / name, evidence / name)
    if (not (bundle / "bukti_validasi/irt_initialization.json").is_file()
            or not read(bundle / "manifest.json").get("irtInitialization")):
        finalize_irt_sidecar(bundle, db_path=ROOT / "data/local/assessments.sqlite3")
    verify_bundle(source, bundle)
    if promote:
        active = source.parent / "hasil_validasi"
        archive = snapshot / "previous_active_report"
        if active.exists() and not archive.exists():
            verify_bundle(source, active)
            shutil.copytree(active, archive)
        shutil.copytree(bundle, active, dirs_exist_ok=True)
        verify_bundle(source, active)
    return bundle


def balance_completed_class(entry: dict, output_name: str) -> dict:
    """Relative bank tiers stay in a provenance-aware export beside blind silver."""
    from scripts.balance_operational_difficulty import export_verified_operational_balance
    from scripts.publish_operational_bank import publish

    source = Path(entry["source"])
    bundle = source.parent / "hasil_validasi"
    version = export_verified_operational_balance(source, bundle, grade=entry["grade"],
                                                  track=entry["subjectTrack"], output_name=output_name)
    version["activePublication"] = publish(source, bundle, version, grade=entry["grade"], track=entry["subjectTrack"])
    return version


def export_batch_progress(source_root: Path, batch_name: str, run_dir: Path) -> None:
    from scripts.export_revalidation_progress import export_class

    results = []
    for name, grade, track in CLASSES:
        source = source_root / name / "soal_pretest_db.json"
        directory = source.parent / batch_name
        report = export_class(source, directory / "silver_labels.json", directory, grade=grade, track=track)
        results.append({key: report[key] for key in ("class", "grade", "subjectTrack", "status",
                       "fullComplete", "summary", "validationResultsHash", "byteIdenticalToVerifiedActiveArray")})
    atomic_write({"schemaVersion": "all-grade-progress-exports-v1", "newApiCalls": 0,
                  "activeOutputsModified": False, "checkpointsModified": False, "classes": results},
                 run_dir / "progress_exports.json")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-name", required=True)
    parser.add_argument("--source-root", type=Path, default=ROOT / "output/pretest")
    parser.add_argument("--pilot-per-class", type=int, default=2)
    parser.add_argument("--max-api-calls", type=int, default=2500,
                        help="Session-wide application request ceiling including retries and adjudication.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--train", action="store_true", help="Train the new artifact after all classes and dataset gates complete.")
    parser.add_argument("--pilot-only", action="store_true")
    parser.add_argument("--balance-bank", action="store_true", help="Export relative thirds after each completed class; preserve blind silver.")
    parser.add_argument("--balance-output-name", default="operational_balance_v2")
    parser.add_argument("--export-progress", action="store_true", help="Refresh final/draft JSON arrays after completion or any stop.")
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9_-]+", args.batch_name):
        parser.error("batch-name must be one directory name")
    if not re.fullmatch(r"[A-Za-z0-9_-]+", args.balance_output_name):
        parser.error("balance-output-name must be one directory name")
    if args.pilot_per_class < 1 or args.max_api_calls < 1:
        parser.error("pilot count and API ceiling must be positive")
    settings = GeminiSettings.from_environment()
    run_dir = ROOT / "runs" / args.batch_name
    run_dir.mkdir(parents=True, exist_ok=True)
    state_path = run_dir / "execution.json"
    previous = read(state_path) if state_path.exists() else {}
    training_attempts = list(previous.get("trainingAttempts", []))
    legacy_training = run_dir / "training/readiness.json"
    if not training_attempts and legacy_training.is_file():
        training_attempts.append({"outputDirectory": str(legacy_training.parent),
                                  "status": read(legacy_training).get("trainingStatus", "unknown")})
    state = {"schemaVersion": "all-grade-rubric-revalidation-v1", "batchName": args.batch_name,
             "model": settings.model, "serialExecution": True, "requestedRunsPerQuestion": 3,
             "stopAllOnAnyQuotaOrProviderBlock": True, "maxApplicationApiCalls": args.max_api_calls,
             "apiCallAccounting": "SDK retries on transient 5xx may create extra HTTP requests; 429 is not retried.",
             "distributionPolicy": "Evidence-based labels without target proportions; empty categories are permitted.",
             "operationalBankPolicy": "relative_thirds_per_active_class" if args.balance_bank else "unchanged",
             "operationalBalanceOutputName": args.balance_output_name if args.balance_bank else None,
             "startedAt": previous.get("startedAt", datetime.now(timezone.utc).isoformat()),
             "executionStatus": "prepared", "phase": "pilot", "classes": [],
             "pilotResults": previous.get("pilotResults", []),
             "trainingAttempts": training_attempts}
    for name, grade, track in CLASSES:
        source = args.source_root.resolve() / name / "soal_pretest_db.json"
        questions = read(source)
        if len({str(q["_id"]) for q in questions}) != len(questions):
            raise ValueError(f"duplicate IDs within {name}")
        for question in questions:
            for ref in question.get("image_url") or []:
                if not (source.parent / ref).is_file():
                    raise FileNotFoundError(f"missing visual asset in {name}")
        directory = source.parent / args.batch_name
        directory.mkdir(exist_ok=True)
        working = directory / "silver_labels.json"
        checkpoint = load_checkpoint(working, source, digest(source), settings.model, 3, grade, track=track)
        if not working.exists():
            checkpoint.update(executionStatus="queued", summary=summarize(checkpoint))
            atomic_write(checkpoint, working)
        old_path = source.parent / "hasil_validasi/validation_results.json"
        old = read(old_path) if old_path.exists() else []
        old_entry = next((e for e in previous.get("classes", []) if e["name"] == name), {})
        pilot = old_entry.get("pilotQuestionIds") or select_pilot(questions, old, args.pilot_per_class)
        if not set(pilot) <= {str(q["_id"]) for q in questions}:
            raise ValueError("saved pilot IDs changed")
        state["classes"].append({"name": name, "grade": grade, "subjectTrack": track,
            "questionCount": len(questions), "source": str(source), "sourceHash": digest(source),
            "checkpoint": str(working), "rubricVersion": silver_rubric(grade, track=track).version,
            "pilotQuestionIds": pilot,
            "pilotBaselineLabels": pilot_baseline(source, directory, pilot, old_entry, state["pilotResults"]),
            "baselineDistribution": old_entry.get("baselineDistribution") or
                dict(Counter(row.get("cognitive_level") for row in old)),
            "operationalBalance": old_entry.get("operationalBalance"),
            "promoted": bool(old_entry.get("promoted", False))})

    def save() -> None:
        state["updatedAt"] = datetime.now(timezone.utc).isoformat()
        calls = 0
        for entry in state["classes"]:
            cp = read(Path(entry["checkpoint"]))
            entry["executionStatus"] = cp.get("executionStatus")
            entry["summary"] = cp.get("summary", {})
            entry["apiAttempts"] = cp.get("apiAttempts", 0)
            entry["pilotComplete"] = complete(cp, entry["pilotQuestionIds"])
            entry["fullComplete"] = complete(cp, [str(q["_id"]) for q in read(Path(entry["source"]))])
            calls += entry["apiAttempts"]
        state["apiAttempts"] = calls
        atomic_write(state, state_path)
        if args.balance_bank:
            atomic_write({"schemaVersion": "all-grade-relative-bank-v2", "batchName": args.batch_name,
                          "policy": "relative_thirds_per_active_class", "trainingLabelPolicy": "original_verified_ai_silver",
                          "classes": [{"class": e["name"], "validationComplete": e["fullComplete"],
                                       "operationalBalance": e.get("operationalBalance")}
                                      for e in state["classes"]]}, run_dir / "operational_balance_summary.json")
        lines = ["# Revalidasi rubrik semua kelas", "", f"Status: `{state['executionStatus']}`. Fase: `{state['phase']}`.",
                 f"Gemini: `{settings.model}`; N=3 blind + adjudikasi. Panggilan aplikasi: {calls}/{args.max_api_calls}.",
                 "Distribusi mengikuti bukti; tidak ada kuota label. Hasil aktif lama dipertahankan untuk kelas belum selesai.", "",
                 "| Kelas | Soal | Run sukses | Pilot selesai | Validasi selesai | Hasil diperbarui |", "|---|---:|---:|---|---|---|"]
        for entry in state["classes"]:
            lines.append(f"| {entry['name']} | {entry['questionCount']} | {entry['summary'].get('successfulRuns', 0)} | "
                         f"{entry['pilotComplete']} | {entry['fullComplete']} | {entry['promoted']} |")
        if args.balance_bank:
            lines.extend(["", "## Bank operasional relatif", "",
                          "Soal aktif dibagi mendekati sepertiga per kategori setelah validasi kelas selesai. Label blind Gemini tetap tersedia untuk audit dan training.",
                          "", "| Kelas | Easy | Medium | Hard |", "|---|---:|---:|---:|"])
            for entry in state["classes"]:
                balanced = entry.get("operationalBalance")
                if balanced:
                    counts = balanced["activeDistribution"]
                    lines.append(f"| {entry['name']} | {counts['easy']} | {counts['medium']} | {counts['hard']} |")
        if state.get("stopReason"):
            lines.extend(["", "Alasan berhenti: `" + json.dumps(state["stopReason"], ensure_ascii=False) + "`."])
        if state.get("pilotResults"):
            lines.extend(["", "## Perbandingan pilot", "", "| Kelas | ID soal | Label lama | Label baru | Qualified |", "|---|---|---|---|---|"])
            for result in state["pilotResults"]:
                lines.append(f"| {result['class']} | {result['questionId']} | {result['oldLabel']} | {result['newLabel']} | {result['eligibleForTraining']} |")
        (run_dir / "REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    save()
    if not args.execute:
        print(f"Prepared {sum(e['questionCount'] for e in state['classes'])} questions; no API calls. {state_path}")
        return 0

    def finish(code: int) -> int:
        if args.export_progress:
            export_batch_progress(args.source_root.resolve(), args.batch_name, run_dir)
        return code

    for phase in ("pilot", "full"):
        if phase == "full" and args.pilot_only:
            break
        state.update(phase=phase, executionStatus="running")
        for entry in state["classes"]:
            state["currentClass"] = entry["name"]
            save()
            source, output = Path(entry["source"]), Path(entry["checkpoint"])
            selected = entry["pilotQuestionIds"] if phase == "pilot" else [str(q["_id"]) for q in read(source)]
            if not complete(read(output), selected):
                remaining = args.max_api_calls - state["apiAttempts"]
                if remaining <= 0:
                    state.update(executionStatus="stopped_api_call_budget", stopReason={"maxApplicationApiCalls": args.max_api_calls})
                    save()
                    return finish(4)
                arguments = ["--source", str(source), "--output", str(output), "--grade", str(entry["grade"]),
                             "--track", entry["subjectTrack"], "--runs", "3", "--workers", "1", "--attempts", "2",
                             "--pause", "0.5", "--stop-on-quota", "--max-api-calls", str(remaining), "--execute"]
                if phase == "pilot":
                    for qid in selected:
                        arguments.extend(["--question-id", qid])
                print(f"phase={phase} class={entry['name']} selected={len(selected)} remaining_api_calls={remaining}", flush=True)
                code = run_script("generate_silver_labels_kelas1.py", arguments, output.parent / f"{phase}.log", accepted=(0, 3, 4))
                if code in (3, 4):
                    blocked = read(output)
                    state.update(executionStatus=blocked["executionStatus"], stopReason=blocked.get("stopReason"),
                                 blockedByClass=entry["name"])
                    save()
                    print(f"Stopped all Gemini calls: {state['executionStatus']}; progress={state_path}", flush=True)
                    return finish(code)
            if not complete(read(output), selected):
                state.update(executionStatus="stopped_incomplete_provider_evidence", stopReason={"class": entry["name"], "phase": phase})
                save()
                return finish(2)
            verify_evidence(source, output, entry["grade"])
            if phase == "full":
                package_class(source, output, output.parent, promote=True)
                entry["promoted"] = True
                write_active_index(args.source_root.resolve())
                if args.balance_bank:
                    entry["operationalBalance"] = balance_completed_class(entry, args.balance_output_name)
            save()
        if phase == "pilot":
            results = []
            for entry in state["classes"]:
                cp = read(Path(entry["checkpoint"]))
                for qid in entry["pilotQuestionIds"]:
                    aggregate = cp["items"][qid]["aggregate"]
                    results.append({"class": entry["name"], "questionId": qid,
                                    "oldLabel": entry["pilotBaselineLabels"].get(qid),
                                    "newLabel": aggregate.get("heads", {}).get("intendedDifficulty", {}).get("label"),
                                    "eligibleForTraining": aggregate.get("eligibleForTraining", False)})
            state["pilotResults"] = results
            atomic_write({"schemaVersion": "rubric-boundary-pilot-v1", "results": results,
                          "humanValidationPerformed": False, "distributionQuotaUsed": False}, run_dir / "pilot_comparison.json")
            save()
    state.update(executionStatus="pilot_completed" if args.pilot_only else "revalidation_completed")
    save()
    if args.train and not args.pilot_only:
        for attempt in reversed(state["trainingAttempts"]):
            readiness = Path(attempt["outputDirectory"]) / "readiness.json"
            training_status = read(readiness).get("trainingStatus") if readiness.is_file() else None
            if training_status in ("completed", "completed_candidate"):
                attempt["status"] = training_status
                state.update(trainingStatus=training_status, productionModelPromoted=False)
                state["irtPilotPreparation"] = configure_irt_pilot(readiness.parent, args.batch_name)
                state.update(phase="training", executionStatus="completed")
                save()
                return finish(0)
        training_dir = next_training_directory(run_dir)
        training_attempt = {"outputDirectory": str(training_dir), "status": "preparing"}
        state["trainingAttempts"].append(training_attempt)
        state.update(phase="training", executionStatus="training_preparation")
        save()
        code = run_script("prepare_allgrade_retraining.py", ["--source-root", str(args.source_root.resolve()),
                          "--output-dir", str(training_dir), "--execute-training"],
                          training_dir / "preparation.log", accepted=(0, 2))
        readiness = training_dir / "readiness.json"
        training_status = read(readiness).get("trainingStatus") if readiness.is_file() else None
        training_attempt["status"] = training_status or ("completed" if code == 0 else "blocked_quality_gates")
        state.update(trainingStatus=training_attempt["status"], productionModelPromoted=False)
        training_attempt["exitCode"] = code
        state["irtPilotPreparation"] = configure_irt_pilot(training_dir, args.batch_name)
        state["executionStatus"] = "completed" if code == 0 else "training_blocked_quality_gates"
        save()
        return finish(code)
    return finish(0)


if __name__ == "__main__":
    raise SystemExit(main())
