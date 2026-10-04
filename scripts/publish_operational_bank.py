"""Expose relative labels in the active database array, retaining blind AI rows."""
from __future__ import annotations

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.llm.silver import silver_rubric
from app.silver.exports import ai_validation_path, load_decision_bundle
from scripts.balance_operational_difficulty import (
    CLASSES, allocate, export_verified_operational_balance, verify_operational_export,
)
from scripts.generate_silver_labels_kelas1 import atomic_write
from scripts.refresh_ai_validation_reports import verify_bundle


def info(data: bytes) -> dict:
    return {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}


def write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".publish.tmp")
    temporary.write_bytes(data)
    temporary.replace(path)


def publish(source: Path, bundle: Path, version: dict, *, grade: int, track: str) -> dict:
    verify_bundle(source, bundle)
    directory = Path(version["directory"])
    version_manifest = verify_operational_export(directory)
    old_manifest_bytes = (bundle / "manifest.json").read_bytes()
    old_manifest = json.loads(old_manifest_bytes)
    source_bytes = source.read_bytes()
    original = ai_validation_path(bundle, old_manifest).read_bytes()
    if (directory / "ai_validation_results.json").read_bytes() != original:
        raise ValueError("operational export is stale; original AI rows differ")
    decisions = load_decision_bundle(bundle)
    if json.loads((directory / "ai_decisions.json").read_text(encoding="utf-8")) != decisions:
        raise ValueError("operational export is stale; original AI decisions differ")
    if version_manifest["sourceQuestionHash"] != info(source_bytes)["sha256"]:
        raise ValueError("operational export source hash differs")
    balanced = (directory / "validation_results.json").read_bytes()
    expected, allocation = allocate(json.loads(original), decisions["items"])
    if json.loads(balanced) != expected:
        raise ValueError("operational array differs from original evidence")
    rows = json.loads(source_bytes)
    if len(rows) != len(expected) or any(list(a) != list(b) or any(
            a[key] != b[key] for key in a if key not in
            {"cognitive_level", "cognitive_score", "confidence_score", "status"})
            for a, b in zip(rows, expected)):
        raise ValueError("operational array changed source schema or content")
    audit_bytes = (directory / "balance_audit.json").read_bytes()
    ai_file = bundle / "ai_validation_results.json"
    if old_manifest["databaseExport"].get("operationalBalance") and ai_file.read_bytes() != original:
        raise ValueError("original AI archive differs")
    manifest = deepcopy(old_manifest)
    ai_reference = {"path": "ai_validation_results.json", **info(original)}
    audit_reference = {"path": "bukti_validasi/operational_balance_audit.json", **info(audit_bytes)}
    versions = sorted({d["llmAdvisory"]["rubricVersion"] for d in decisions["items"]})
    policy = {"provenance": "relative_bank_quota", "schemaVersion": version_manifest["schemaVersion"],
              "aiValidationResults": ai_reference, "audit": audit_reference,
              "activeDistribution": allocation["targets"], "sourceFingerprint": version["sourceFingerprint"],
              "versionDirectory": str(directory), "sourceRubricVersions": versions,
              "newRubricValidationComplete": versions == [silver_rubric(grade, track=track).version],
              "trainingLabelSource": "ai_validation_results.json", "empiricalIrtCalibration": False}
    manifest["databaseExport"]["operationalBalance"] = policy
    manifest["activeDatabaseLabelProvenance"] = "relative_bank_quota"
    manifest["outputs"]["validation_results.json"] = info(balanced)
    manifest["outputs"]["ai_validation_results.json"] = info(original)
    manifest["outputs"][audit_reference["path"]] = info(audit_bytes)
    backup_manifest = bundle / "bukti_validasi/ai_export_manifest.json"
    if not old_manifest["databaseExport"].get("operationalBalance"):
        write_bytes(backup_manifest, old_manifest_bytes)
    manifest["outputs"]["bukti_validasi/ai_export_manifest.json"] = info(backup_manifest.read_bytes())
    old_active = (bundle / "validation_results.json").read_bytes()
    write_bytes(ai_file, original)
    write_bytes(bundle / audit_reference["path"], audit_bytes)
    try:
        write_bytes(bundle / "validation_results.json", balanced)
        atomic_write(manifest, bundle / "manifest.json")
        verify_bundle(source, bundle)
        if source.read_bytes() != source_bytes:
            raise ValueError("question source changed during publication")
    except Exception:
        write_bytes(bundle / "validation_results.json", old_active)
        write_bytes(bundle / "manifest.json", old_manifest_bytes)
        raise
    return {"class": source.parent.name, "validationResults": str(bundle / "validation_results.json"),
            "activeDistribution": allocation["targets"], "newRubricValidationComplete": policy["newRubricValidationComplete"],
            "sourceSchemaAndContentPreserved": True, "aiEvidencePreserved": True, "newApiCalls": 0}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=ROOT / "output/pretest")
    args = parser.parse_args()
    plans = []
    # Check and version every input before publishing the first active array.
    for name, grade, track in CLASSES:
        source = args.source_root / name / "soal_pretest_db.json"
        bundle = source.parent / "hasil_validasi"
        version = export_verified_operational_balance(source, bundle, grade=grade, track=track)
        plans.append((source, bundle, version, grade, track))
    results = [publish(source, bundle, version, grade=grade, track=track)
               for source, bundle, version, grade, track in plans]
    atomic_write({"classes": results, "newApiCalls": 0, "provenance": "relative_bank_quota"},
                 args.source_root / "active_operational_balance_summary.json")
    print(json.dumps(results, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
