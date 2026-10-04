"""Verify a stopped all-grade resume and write offline, secret-free evidence.

No API call, training, model promotion or IRT estimation occurs here. Working
checkpoints, active AI bundles and immutable operational versions are read-only.
Only this final report and the run's IRT readiness sidecars are written.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timedelta, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.llm.silver import silver_rubric
from app.psychometrics.initialization import build_initialization_report
from app.silver.exports import load_decision_bundle, ai_validation_path
from scripts.balance_operational_difficulty import verify_operational_export
from scripts.export_revalidation_progress import current_decision
from scripts.generate_silver_labels_kelas1 import atomic_write, summarize
from scripts.refresh_ai_validation_reports import verify_bundle, verify_evidence
from scripts.revalidate_all_grades import CLASSES

VALIDATION_FIELDS = {"cognitive_level", "cognitive_score", "confidence_score", "status"}
LABELS = ("easy", "medium", "hard")
TOKEN_FIELDS = ("promptTokens", "outputTokens", "thinkingTokens", "totalTokens")


def read(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path, base: Path) -> str:
    return Path(os.path.relpath(path.resolve(), base.resolve())).as_posix()


def canonical_hash(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                     separators=(",", ":")).encode("utf-8")).hexdigest()


def assert_source_shape(originals: list[dict], outputs: list[dict]) -> None:
    """Validation may edit four columns; source content and field order stay exact."""
    if not isinstance(originals, list) or not isinstance(outputs, list) or len(originals) != len(outputs):
        raise ValueError("validation export must preserve the source question array")
    identifiers = [str(row["_id"]) for row in originals]
    if len(set(identifiers)) != len(identifiers):
        raise ValueError("source question IDs must be unique")
    for original, output in zip(originals, outputs):
        if list(original) != list(output) or any(original[key] != output[key]
                                               for key in original if key not in VALIDATION_FIELDS):
            raise ValueError("validation export changed source schema, order or content")


def difficulty_counts(rows: list[dict], *, active_only: bool = False) -> dict[str, int]:
    selected = [row for row in rows if not active_only or row.get("status") == "active"]
    counts = Counter(row.get("cognitive_level") or "undecided" for row in selected)
    return {label: counts[label] for label in (*LABELS, "undecided")}


def retained_failed_usage(checkpoint: dict) -> dict[str, int]:
    """Count known failed-response usage once when an attempt is copied to history."""
    seen, usages = set(), []
    for record in checkpoint.get("items", {}).values():
        candidates = [*record.get("runs", []), *record.get("attemptHistory", []),
                      *record.get("retryHistory", []), *record.get("adjudicationAttemptHistory", [])]
        if record.get("adjudication"):
            candidates.append(record["adjudication"])
        for result in candidates:
            key = canonical_hash(result)
            if result.get("status") == "failed" and key not in seen:
                seen.add(key)
                usages.append(result.get("usage", {}))
    return {field: sum(int(usage.get(field, 0)) for usage in usages) for field in TOKEN_FIELDS}


def sanitized_stop_reason(value: dict | None) -> dict:
    """Copy only structured quota fields; never provider text, URLs or credentials."""
    value = value or {}
    result = {}
    code = value.get("errorCode")
    if code:
        result["errorCode"] = code if re.fullmatch(r"[A-Za-z][A-Za-z0-9_.]*:\d{3}", str(code)) else "redacted"
    reason = value.get("providerFailureReason")
    if reason:
        result["providerFailureReason"] = reason if reason in {
            "api_key_invalid", "invalid_api_key", "permission_denied", "model_not_found", "provider_configuration_error"
        } else "redacted_provider_reason"
    limits = []
    for limit in value.get("quotaLimits", []) or []:
        safe = {}
        for field in ("quotaMetric", "quotaId", "quotaValue"):
            raw = str(limit.get(field, ""))
            patterns = {"quotaMetric": r"generativelanguage\.googleapis\.com/[a-z_]+",
                        "quotaId": r"Generate[A-Za-z0-9-]+", "quotaValue": r"\d+(?:\.\d+)?"}
            if raw and len(raw) <= 240 and re.fullmatch(patterns[field], raw) and "AIza" not in raw:
                safe[field] = raw
        if safe:
            limits.append(safe)
    if limits:
        result["quotaLimits"] = limits
    for key in ("maxApplicationApiCalls", "maxNewApiCalls"):
        if type(value.get(key)) is int:
            result[key] = value[key]
    return result


def verify_retained_evidence(baseline: dict, checkpoints: dict[str, dict]) -> dict:
    """Verify exact selected paid dictionaries without inferring an absent baseline."""
    runs = baseline.get("successfulEvidence", [])
    adjudications = baseline.get("successfulAdjudicationEvidence", [])
    if not runs and not adjudications:
        return {"status": "not_verified_no_baseline_evidence", "verifiedRuns": 0,
                "verifiedAdjudications": 0, "historicalMutationsBeforeBaselineCaptureVerified": False}
    seen = set()
    for entry in runs:
        key = (entry["class"], str(entry["questionId"]), entry["runIndex"])
        if key in seen or entry["run"].get("status") != "success":
            raise ValueError("baseline successful run evidence is duplicated or invalid")
        seen.add(key)
        record = checkpoints[key[0]].get("items", {}).get(key[1], {})
        actual = [run for run in record.get("runs", []) if run["runIndex"] == key[2]]
        if len(actual) != 1 or actual[0] != entry["run"]:
            raise ValueError("a selected baseline successful run was changed or removed")
    if runs and baseline.get("baselineSuccessfulInitialRuns") is not None and len(runs) != baseline["baselineSuccessfulInitialRuns"]:
        raise ValueError("baseline successful evidence does not cover its declared count")
    seen = set()
    for entry in adjudications:
        key = (entry["class"], str(entry["questionId"]))
        if key in seen or entry["adjudication"].get("status") != "success":
            raise ValueError("baseline successful adjudication evidence is duplicated or invalid")
        seen.add(key)
        actual = checkpoints[key[0]].get("items", {}).get(key[1], {}).get("adjudication")
        if actual != entry["adjudication"]:
            raise ValueError("a selected baseline successful adjudication was changed or removed")
    return {"status": "verified_selected_baseline_evidence", "verifiedRuns": len(runs),
            "verifiedAdjudications": len(adjudications),
            "baselineEvidenceSelection": baseline.get("baselineEvidenceSelection", "Explicit baseline dictionaries"),
            "historicalMutationsBeforeBaselineCaptureVerified": False}


def verify_current_operational(source: Path, bundle: Path, export_root: Path, *, grade: int, track: str) -> dict:
    pointer_path = export_root / "current.json"
    pointer = read(pointer_path)
    directory = Path(pointer["directory"]).resolve()
    if not directory.is_relative_to(export_root.resolve()) or directory == export_root.resolve():
        raise ValueError("operational current pointer escapes its export directory")
    if Path(pointer["validationResults"]).resolve() != directory / "validation_results.json":
        raise ValueError("operational current validation path differs")
    manifest = verify_operational_export(directory)
    if manifest["sourceQuestionHash"] != digest(source):
        raise ValueError("operational export source question hash mismatch")
    original_ai_path = ai_validation_path(bundle)
    originals = read(original_ai_path)
    decisions = load_decision_bundle(bundle)
    identity = manifest["identity"]
    if (identity["sourceValidationResultsHash"] != canonical_hash(originals)
            or identity["sourceDecisionAuditHash"] != canonical_hash(decisions)
            or identity["grade"] != grade or identity["subjectTrack"] != track
            or pointer.get("sourceFingerprint") != manifest["sourceFingerprint"]):
        raise ValueError("operational export is stale or refers to another active AI source")
    if ((directory / "ai_validation_results.json").read_bytes() != original_ai_path.read_bytes()
            or read(directory / "ai_decisions.json") != decisions):
        raise ValueError("operational export retained AI evidence differs from the active source")
    rows, audit = read(directory / "validation_results.json"), read(directory / "balance_audit.json")
    assert_source_shape(read(source), rows)
    if audit["usedForTraining"] is not False or audit["empiricalIrtCalibration"] is not False:
        raise ValueError("relative operational labels must not claim training or empirical calibration")
    active_counts = difficulty_counts(rows, active_only=True)
    if ({label: active_counts[label] for label in LABELS} != audit["targets"]
            or pointer["activeDistribution"] != audit["targets"]):
        raise ValueError("operational pointer or audit distribution differs")
    return {"status": "verified_current", "directory": directory,
            "validationResults": directory / "validation_results.json",
            "pointer": pointer_path, "sourceFingerprint": manifest["sourceFingerprint"],
            "allDifficultyCounts": difficulty_counts(rows), "activeDifficultyCounts": active_counts,
            "activeQuestionCount": audit["activeQuestionCount"], "changedLabels": audit["changedLabels"],
            "zeroAiSupportLabels": audit["zeroAiSupportLabels"], "tieBoundaries": audit["tieBoundaries"],
            "provenance": "relative_bank_quota", "usedForTraining": False,
            "empiricalIrtCalibration": False}


def training_inventory(run_dir: Path, state: dict, *, full_complete: bool) -> dict:
    reports = []
    for path in sorted(run_dir.glob("*/readiness.json"), key=lambda candidate: candidate.stat().st_mtime):
        payload = read(path)
        reports.append({"path": relative(path, run_dir), "trainingStatus": payload.get("trainingStatus", "unknown"),
                        "revalidationComplete": payload.get("revalidationComplete", False),
                        "readyForTraining": payload.get("readyForTraining", False),
                        "failures": payload.get("failures", [])})
    actual_training = any(report["trainingStatus"] in {"running", "completed", "completed_candidate", "failed",
                                                        "failed_artifact_verification"} for report in reports)
    return {"status": state.get("trainingStatus") or (reports[-1]["trainingStatus"] if reports else
                                                     "not_started" if full_complete else "not_started_revalidation_incomplete"),
            "actualTrainingAttemptRecorded": actual_training, "readinessReports": reports,
            "revalidationComplete": full_complete, "labelPolicy": "original_verified_ai_silver",
            "operationalQuotaLabelsUsed": False, "productionModelPromoted": False}


def finalize(run_dir: Path, source_root: Path, *, batch_name: str, baseline_path: Path | None = None,
             db_path: Path | None = None, classes=CLASSES) -> dict:
    state_path = run_dir / "execution.json"
    state = read(state_path)
    if state.get("executionStatus") in {"running", "training_preparation"}:
        raise ValueError("finalize only after the API/training process has stopped")
    if state.get("batchName") != batch_name:
        raise ValueError("execution belongs to another batch")
    entries = {entry["name"]: entry for entry in state["classes"]}
    if len(entries) != len(state["classes"]) or set(entries) != {name for name, _, _ in classes}:
        raise ValueError("execution class coverage differs")
    baseline = read(baseline_path) if baseline_path else {}
    if baseline.get("batchName", batch_name) != batch_name:
        raise ValueError("baseline belongs to another batch")
    protected = {state_path, *([baseline_path] if baseline_path else [])}
    old_report = run_dir / "REPORT.md"
    if old_report.exists():
        protected.add(old_report)
    results, checkpoints, irt_reports = [], {}, []
    working_totals = Counter()
    for name, grade, track in classes:
        entry = entries[name]
        if entry.get("grade") != grade or entry.get("subjectTrack", "regular") != track:
            raise ValueError("execution class grade or track differs")
        source = (source_root / name / "soal_pretest_db.json").resolve()
        checkpoint_path = (source.parent / batch_name / "silver_labels.json").resolve()
        bundle = source.parent / "hasil_validasi"
        if Path(entry["source"]).resolve() != source or Path(entry["checkpoint"]).resolve() != checkpoint_path:
            raise ValueError("execution class source or checkpoint path differs")
        protected.update({source, checkpoint_path})
        protected.update(path for path in bundle.rglob("*") if path.is_file())
        source_rows, checkpoint = read(source), read(checkpoint_path)
        protected.update(source.parent / asset for row in source_rows for asset in (row.get("image_url") or []))
        source_hash = digest(source)
        if entry.get("sourceHash") != source_hash or checkpoint.get("sourceHash") != source_hash:
            raise ValueError("execution or checkpoint source hash mismatch")
        expected = silver_rubric(grade, track=track)
        if (checkpoint.get("sourceGrade") != grade or checkpoint.get("subjectTrack", "regular") != track
                or checkpoint["rubricVersion"] != expected.version or checkpoint["promptVersion"] != expected.prompt_version):
            raise ValueError("working checkpoint rubric, prompt, grade or track differs")
        verify_evidence(source, checkpoint_path, grade)
        progress = [current_decision(row, checkpoint.get("items", {}).get(str(row["_id"]), {}), source.parent)[1]
                    for row in source_rows]
        full_complete = all(item["fullComplete"] for item in progress)
        summary = summarize(checkpoint)
        if full_complete != entry.get("fullComplete") or summary != checkpoint.get("summary"):
            raise ValueError("execution completeness or checkpoint summary is stale")
        checkpoints[name] = checkpoint
        missing = sum(len(item["missingRunIndices"]) for item in progress)
        pending_adjudications = sum(item["needsAdjudication"] for item in progress)
        working_totals.update({"questionCount": len(source_rows), "successfulInitialRuns": summary["successfulRuns"],
                               "missingInitialRuns": missing, "pendingAdjudications": pending_adjudications,
                               "finalQuestions": sum(item["fullComplete"] for item in progress),
                               "apiAttempts": int(checkpoint.get("apiAttempts", 0)),
                               **{field: summary[field] for field in TOKEN_FIELDS}})
        verify_bundle(source, bundle)
        active_manifest = read(bundle / "manifest.json")
        active_source = active_manifest["sourceFiles"]["source"]
        if Path(active_source["path"]).resolve() != source or active_source["sha256"] != source_hash:
            raise ValueError("active AI bundle source hash or source path mismatch")
        active_checkpoint_path = Path(active_manifest["sourceFiles"]["blindCheckpoint"]["path"])
        protected.update(Path(info["path"]) for info in active_manifest["sourceFiles"].values())
        active_checkpoint = read(active_checkpoint_path)
        original_ai_path = ai_validation_path(bundle, active_manifest)
        active_rows = read(original_ai_path)
        assert_source_shape(source_rows, active_rows)
        current_rubric = (active_checkpoint.get("rubricVersion") == expected.version
                          and active_checkpoint.get("promptVersion") == expected.prompt_version)
        if full_complete and (not current_rubric or digest(active_checkpoint_path) != digest(checkpoint_path)):
            raise ValueError("complete working validation has not been promoted to the matching active AI bundle")
        active_decisions = load_decision_bundle(bundle)["items"]
        operational = None
        if ((full_complete and state.get("operationalBankPolicy") == "relative_thirds_per_active_class")
                or active_manifest.get("databaseExport", {}).get("operationalBalance")):
            output_name = state.get("operationalBalanceOutputName", "operational_balance_v2")
            if not re.fullmatch(r"[A-Za-z0-9_-]+", output_name):
                raise ValueError("operational export directory name is unsafe")
            operational = verify_current_operational(source, bundle, source.parent / output_name, grade=grade, track=track)
            directory = operational["directory"]
            protected.update(path for path in directory.rglob("*") if path.is_file())
            protected.add(operational["pointer"])
            operational = {key: relative(value, run_dir) if isinstance(value, Path) else value
                           for key, value in operational.items()}
        irt = build_initialization_report(bundle, db_path=db_path)
        if irt["irt"]["calibrated"] is not False or irt["irt"]["parameters"] is not None or irt["irt"]["studentAbility"] is not None:
            raise ValueError("offline IRT readiness must not claim fitted parameters or ability")
        irt_path = run_dir / "irt_readiness" / f"{name}.json"
        irt_reports.append((irt_path, irt))
        results.append({"class": name, "grade": grade, "subjectTrack": track, "questionCount": len(source_rows),
                        "fullComplete": full_complete, "finalQuestions": sum(item["fullComplete"] for item in progress),
                        "successfulInitialRuns": summary["successfulRuns"], "missingInitialRuns": missing,
                        "apiAttempts": int(checkpoint.get("apiAttempts", 0)),
                        "successfulResponseRecordedTokens": {field: summary[field] for field in TOKEN_FIELDS},
                        "workingAiQualifiedDifficultyCounts": summary["difficultyDistribution"],
                        "pendingAdjudications": pending_adjudications, "draftQuestions": sum(not item["fullComplete"] for item in progress),
                        "checkpoint": relative(checkpoint_path, run_dir), "checkpointHash": digest(checkpoint_path),
                        "sourceHash": source_hash, "rubricVersion": expected.version,
                        "activeAiBundle": relative(bundle, run_dir), "activeAiValidationResults": relative(original_ai_path, run_dir),
                        "activeRubricVersion": active_checkpoint["rubricVersion"], "activeCurrentRubric": current_rubric,
                        "activeAiDifficultyCounts": difficulty_counts(active_rows),
                        "activeAiQualifiedDifficultyCounts": difficulty_counts(active_rows, active_only=True),
                        "activeAiRoutingCounts": dict(Counter(item["finalRouting"] for item in active_decisions)),
                        "operationalBalance": operational,
                        "irtReadiness": {"path": relative(irt_path, run_dir), "status": irt["irt"]["status"],
                                         "activeRubricVersions": irt["rubricVersions"], "matchingScoredEvents": irt["localResponseInventory"]["matchingScoredEvents"],
                                         "empiricalCalibrationPerformed": False},
                        "verified": True, "sourceContentAndSchemaPreserved": True})
    if working_totals["apiAttempts"] != state.get("apiAttempts"):
        raise ValueError("execution API accounting differs from the stopped checkpoints")
    baseline_calls = int(baseline.get("baselineApiAttempts", 504))
    if working_totals["apiAttempts"] < baseline_calls:
        raise ValueError("cumulative API calls are below the resume baseline")
    full_complete = all(entry["fullComplete"] for entry in results)
    preservation = verify_retained_evidence(baseline, checkpoints)
    failed_usages = [retained_failed_usage(checkpoint) for checkpoint in checkpoints.values()]
    before = {path: digest(path) for path in protected}
    report = {"schemaVersion": "all-grade-resume-final-verification-v1", "batchName": batch_name,
              "verifiedAt": datetime.now(timezone(timedelta(hours=7))).isoformat(),
              "executionStatus": state["executionStatus"], "phase": state.get("phase"),
              "fullComplete": full_complete, "completedClasses": [item["class"] for item in results if item["fullComplete"]],
              "remainingClasses": [item["class"] for item in results if not item["fullComplete"]],
              "workingTotals": dict(working_totals),
              "apiUsage": {"cumulativeApplicationCalls": working_totals["apiAttempts"], "baselineApplicationCalls": baseline_calls,
                           "newApplicationCallsSinceBaseline": working_totals["apiAttempts"] - baseline_calls,
                           "baseline": relative(baseline_path, run_dir) if baseline_path else None,
                           "baselineCallsSource": "saved_baseline" if baseline_path else "documented_previous_stop_504",
                           "successfulResponseRecordedTokens": {field: working_totals[field] for field in TOKEN_FIELDS},
                           "failedResponseRecordedTokens": {field: sum(usage[field] for usage in failed_usages)
                                                            for field in TOKEN_FIELDS},
                           "providerBillingTotalKnown": False,
                           "accountingMeaning": "Application attempts include adjudication and application retries; SDK HTTP retries and unsuccessful response usage may add provider consumption."},
              "stopReason": sanitized_stop_reason(state.get("stopReason")),
              "blockedByClass": state.get("blockedByClass") if state.get("blockedByClass") in entries else None,
              "successfulEvidencePreservation": preservation,
              "training": training_inventory(run_dir, state, full_complete=full_complete),
              "operationalBankPolicy": "relative_thirds_per_active_class",
              "operationalLabelProvenance": "relative_bank_quota", "newApiCallsDuringFinalization": 0,
              "trainingExecutedDuringFinalization": False, "empiricalIrtCalibrationPerformed": False,
              "classes": results, "protectedInputFilesUnchanged": True, "protectedInputFileCount": len(protected)}
    if baseline.get("baselineSuccessfulInitialRuns") is not None:
        previous_successes = int(baseline["baselineSuccessfulInitialRuns"])
        if working_totals["successfulInitialRuns"] < previous_successes:
            raise ValueError("successful initial runs are below the resume baseline")
        report["apiUsage"].update(baselineSuccessfulInitialRuns=previous_successes,
                                  newSuccessfulInitialRunsSinceBaseline=working_totals["successfulInitialRuns"] - previous_successes)
    if baseline.get("successfulEvidence") and baseline.get("successfulAdjudicationEvidence"):
        usages = [entry["run"].get("usage", {}) for entry in baseline["successfulEvidence"]]
        usages.extend(entry["adjudication"].get("usage", {}) for entry in baseline["successfulAdjudicationEvidence"])
        baseline_tokens = {field: sum(int(usage.get(field, 0)) for usage in usages) for field in TOKEN_FIELDS}
        report["apiUsage"]["selectedBaselineSuccessfulResponseRecordedTokens"] = baseline_tokens
        report["apiUsage"]["newSuccessfulResponseTokensAfterSelectedBaseline"] = {
            field: working_totals[field] - baseline_tokens[field] for field in TOKEN_FIELDS}
    # All validation finishes before any report write, including quota-export hashes.
    for path, payload in irt_reports:
        path.parent.mkdir(parents=True, exist_ok=True)
        atomic_write(payload, path)
    if any(digest(path) != expected_hash for path, expected_hash in before.items()):
        raise ValueError("a protected source, checkpoint, active bundle or immutable export changed during finalization")
    atomic_write(report, run_dir / "resume_final_verification.json")
    (run_dir / "RESUME_REPORT.md").write_text(render_report(report), encoding="utf-8")
    return report


def render_report(report: dict) -> str:
    totals, usage = report["workingTotals"], report["apiUsage"]
    lines = ["# Hasil resume validasi dan bank seimbang", "",
             f"Status proses: `{report['executionStatus']}`; validasi semua kelas selesai: **{report['fullComplete']}**.", "",
             f"Selesai {len(report['completedClasses'])}/{len(report['classes'])} kelas. Run awal sukses "
             f"{totals['successfulInitialRuns']}/{totals['questionCount'] * 3}; tersisa {totals['missingInitialRuns']} run "
             f"dan {totals['pendingAdjudications']} adjudikasi. Soal final: {totals['finalQuestions']}/{totals['questionCount']}.", "",
             f"Panggilan aplikasi kumulatif {usage['cumulativeApplicationCalls']}; tambahan sejak baseline "
             f"{usage['newApplicationCallsSinceBaseline']}. Token tercatat dari respons sukses "
             f"{usage['successfulResponseRecordedTokens']['totalTokens']:,}; angka ini bukan total tagihan provider.", ""]
    if report["stopReason"]:
        lines.extend(["Alasan berhenti yang disanitasi: `" + json.dumps(report["stopReason"], ensure_ascii=False) + "`.", ""])
    lines.extend(["Kolom AI dan operasional berikut hanya menghitung soal aktif. Label operasional memakai ranking profil "
                  "serta kuota relatif tiap kelas; confidence_score tetap memakai dukungan run Gemini asli dan dapat 0. "
                  "Pada kelas belum selesai, AI dan pembagian operasional memakai bukti aktif sebelumnya; revalidasi v8 belum final. "
                  "Label AI asli tetap menjadi sumber training.", "",
                  "| Kelas | Final | AI Easy/Medium/Hard | Operasional Easy/Medium/Hard | Tanpa dukungan AI |",
                  "|---|---:|---:|---:|---:|"])
    for entry in report["classes"]:
        ai = entry["activeAiQualifiedDifficultyCounts"]
        ai_counts = "/".join(str(ai[label]) for label in LABELS)
        balanced = entry["operationalBalance"]
        if balanced:
            operational = "/".join(str(balanced["activeDifficultyCounts"][label]) for label in LABELS)
            link = f"[{entry['class']}]({balanced['validationResults']})"
            zero = str(balanced["zeroAiSupportLabels"])
        else:
            operational, zero = "belum selesai", "—"
            link = f"[{entry['class']}]({entry['activeAiValidationResults']})"
        lines.append(f"| {link} | {entry['finalQuestions']}/{entry['questionCount']} | {ai_counts} | {operational} | {zero} |")
    preservation = report["successfulEvidencePreservation"]
    lines.extend(["", f"Preservasi bukti sukses: `{preservation['status']}`; "
                  f"{preservation['verifiedRuns']} run dan {preservation['verifiedAdjudications']} adjudikasi dibandingkan "
                  "dengan kamus baseline yang dipilih. Pemeriksaan ini tidak membuktikan tidak adanya perubahan sebelum baseline ditangkap.", "",
                  f"Training: `{report['training']['status']}`. Gate data tetap berlaku; label kuota tidak dipakai sebagai AI silver. "
                  "Finalisasi ini tidak menjalankan training dan tidak mempromosikan model.", "",
                  "IRT hanya disiapkan berdasarkan metadata bundle aktif yang benar-benar tersedia. "
                  "Tidak ada parameter item atau kemampuan siswa yang dibuat. [Readiness per kelas](irt_readiness/) "
                  "mencatat kebutuhan respons nyata.", "",
                  "[Bukti verifikasi lengkap](resume_final_verification.json). Checkpoint, isi soal, bundle AI, "
                  "versi operasional immutable, dan REPORT.md lama tidak diubah oleh finalisasi ini."])
    if report["training"]["readinessReports"]:
        lines.extend(["", "Laporan kesiapan training:", ""])
        lines.extend(f"- [{Path(item['path']).parent.name}]({item['path']}): `{item['trainingStatus']}`."
                     for item in report["training"]["readinessReports"])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-name", required=True)
    parser.add_argument("--source-root", type=Path, default=ROOT / "output/pretest")
    parser.add_argument("--baseline", type=Path)
    parser.add_argument("--assessment-db", type=Path, default=ROOT / "data/local/assessments.sqlite3")
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9_-]+", args.batch_name):
        parser.error("batch-name must be one directory name")
    run_dir = ROOT / "runs" / args.batch_name
    candidate = run_dir / "resume_balanced_v2.json"
    baseline = args.baseline or (candidate if candidate.exists() else None)
    report = finalize(run_dir, args.source_root.resolve(), batch_name=args.batch_name,
                      baseline_path=baseline, db_path=args.assessment_db)
    print(json.dumps({key: report[key] for key in ("fullComplete", "completedClasses", "remainingClasses",
                                                  "workingTotals", "apiUsage", "stopReason")}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
