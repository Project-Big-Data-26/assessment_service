"""Lock, audit and package completed TL validation without any provider calls."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.refresh_ai_validation_reports import (  # noqa: E402
    digest, load, run_script, verify_bundle, verify_evidence, write, write_active_index,
)


def package(grade: int, batch_name: str, snapshot_name: str) -> dict:
    directory = ROOT / f"output/pretest/kelas{grade}_tl"
    source = directory / "soal_pretest_db.json"
    working = directory / batch_name / "silver_labels.json"
    checkpoint = load(working)
    count = len(load(source))
    summary = checkpoint["summary"]
    if checkpoint.get("subjectTrack") != "tl" or checkpoint.get("sourceGrade") != grade:
        raise ValueError("checkpoint is not for the selected TL class")
    if (summary["successfulRuns"] != count * 3 or summary["failedRuns"]
            or summary["pendingAdjudication"]):
        raise ValueError("complete all three runs and adjudications before final packaging")
    verify_evidence(source, working, grade)
    snapshot = working.parent / snapshot_name
    if snapshot.exists():
        raise FileExistsError("use a new snapshot name; audited snapshots are immutable")
    snapshot.mkdir()
    locked = snapshot / "silver_labels.json"
    shutil.copy2(working, locked)
    run_script("audit_grade_aware_pilot.py", "--source", str(source), "--checkpoint", str(locked),
               "--grade", str(grade), "--output-dir", str(snapshot / "audit"), accepted=(0, 2))
    bundle = snapshot / "bundle"
    run_script("build_blind_validation_bundle.py", "--source", str(source), "--checkpoint", str(locked),
               "--audit", str(snapshot / "audit/pilot_audit.json"), "--output-dir", str(bundle))
    verify_bundle(source, bundle)
    active = directory / "hasil_validasi"
    if active.exists():
        verify_bundle(source, active)
        shutil.copytree(active, snapshot / "previous_active_report")
    shutil.copytree(bundle, active, dirs_exist_ok=True)
    evidence = active / "bukti_validasi"
    evidence.mkdir(exist_ok=True)
    shutil.copy2(locked, evidence / "silver_labels.json")
    for name in ("pilot_audit.json", "PILOT_AUDIT.md"):
        shutil.copy2(snapshot / "audit" / name, evidence / name)
    verify_bundle(source, active)
    audit = load(snapshot / "audit/pilot_audit.json")
    result = {
        "verifiedAt": datetime.now(timezone.utc).isoformat(), "grade": grade, "subjectTrack": "tl",
        "questionCount": count, "successfulRuns": summary["successfulRuns"],
        "adjudicatedItems": summary["adjudicatedItems"], "recordedTokens": summary["totalTokens"],
        "promptAndResponseHashesVerified": True, "sourceAndAssetsPreserved": True,
        "activeAndVersionedOutputHashesMatch": True, "newLlmCalls": 0,
        "readyForExpansion": audit["readyForExpansion"],
        "failedAuditGates": [key for key, passed in audit["gates"].items() if not passed],
        "lockedCheckpointSha256": digest(locked),
        "report": active.relative_to(ROOT).as_posix(),
    }
    write(snapshot / "execution_verification.json", result)
    print(json.dumps(result, ensure_ascii=False), flush=True)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--grades", nargs="+", type=int, choices=(11, 12), default=[11, 12])
    parser.add_argument("--batch-name", required=True)
    parser.add_argument("--snapshot-name", default="final_snapshot_v1")
    args = parser.parse_args()
    for name in (args.batch_name, args.snapshot_name):
        if not name or Path(name).name != name or name in (".", ".."):
            parser.error("batch and snapshot names must be single directory names")
    for grade in args.grades:
        package(grade, args.batch_name, args.snapshot_name)
    write_active_index()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
