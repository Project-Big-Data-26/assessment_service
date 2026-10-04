"""Prepare one verified all-grade dataset; train only after unchanged data gates pass.

Missing or old validation bundles produce a readiness report and no mixed-rubric
snapshot. An optional --bundle-root can point to staged class/bundle directories.
No Gemini calls or model promotion occur here.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.assessment.store import AssessmentStore  # noqa: E402
from app.classification.v2.artifact import load_and_verify_manifest  # noqa: E402
from app.training.v2.dataset import build_snapshot, save_snapshot  # noqa: E402
from app.llm.silver import RUBRIC_VERSION, silver_rubric  # noqa: E402
from app.silver.policy import LABEL_PROVENANCE  # noqa: E402
from app.silver.exports import ai_validation_path
from scripts.build_operational_silver import rows_from_bundle  # noqa: E402
from scripts.refresh_ai_validation_reports import verify_bundle  # noqa: E402

CLASSES = tuple(f"kelas{grade}" for grade in range(1, 13)) + ("kelas11_tl", "kelas12_tl")
GRADE_TRACKS = tuple(f"{grade}:regular" for grade in range(1, 13)) + ("11:tl", "12:tl")


def bundle_path(source_root: Path, bundle_root: Path | None, class_name: str) -> Path:
    if bundle_root is None:
        return source_root / class_name / "hasil_validasi"
    candidates = (
        bundle_root / class_name / "bundle",
        bundle_root / class_name / "hasil_validasi",
        bundle_root / class_name,
    )
    return next((path for path in candidates if (path / "manifest.json").is_file()), candidates[0])


def prepare(args: argparse.Namespace) -> dict[str, Any]:
    report: dict[str, Any] = {
        "rubricVersion": args.rubric_version,
        "requiredClasses": list(CLASSES),
        "trainingGrades": list(range(1, 13)),
        "minimumTrainEachLabel": 30,
        "minimumValidationAndTestEachLabel": 15,
        "requiredGradeTracksEachSplit": list(GRADE_TRACKS),
        "revalidationComplete": False,
        "readyForTraining": False,
        "trainingStatus": "not_started",
        "classes": {},
        "failures": [],
        "trackConditioning": "TL text marker and grade embedding; separate grade-track metrics and calibration",
        "promotion": "new artifact only; no automatic production promotion",
    }
    rows, excluded = [], Counter()
    for class_name in CLASSES:
        grade = int(class_name.removeprefix("kelas").removesuffix("_tl"))
        track = "tl" if class_name.endswith("_tl") else "regular"
        expected = silver_rubric(grade, track=track)
        source = args.source_root / class_name / "soal_pretest_db.json"
        bundle = bundle_path(args.source_root, args.bundle_root, class_name)
        entry: dict[str, Any] = {
            "source": str(source), "bundle": str(bundle),
            "expectedRubricVersion": expected.version,
            "expectedPromptVersion": expected.prompt_version,
        }
        report["classes"][class_name] = entry
        try:
            if not source.is_file():
                raise ValueError("source_missing")
            manifest_file = bundle / "manifest.json"
            if not manifest_file.is_file():
                raise ValueError("validation_bundle_missing")
            manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
            checkpoint = Path(manifest["sourceFiles"]["blindCheckpoint"]["path"])
            checkpoint_meta = json.loads(checkpoint.read_text(encoding="utf-8"))
            entry["rubricVersion"] = checkpoint_meta.get("rubricVersion")
            if entry["rubricVersion"] != expected.version:
                raise ValueError(f"rubric_mismatch:{entry['rubricVersion']}!={expected.version}")
            if checkpoint_meta.get("promptVersion") != expected.prompt_version:
                raise ValueError("prompt_mismatch:new_blind_validation_required")
            records = checkpoint_meta.get("items", {})
            if not records or any(
                len(successful := [run for run in record.get("runs", []) if run.get("status") == "success"]) != 3
                or {run["runIndex"] for run in successful} != {1, 2, 3}
                or record.get("aggregate", {}).get("needsAdjudication") is not False
                for record in records.values()
            ):
                raise ValueError("revalidation_incomplete:three_runs_and_resolved_adjudication_required")
            qualified, rejected = rows_from_bundle(source, bundle)
            if {row.rubricVersion for row in qualified} - {expected.version}:
                raise ValueError("qualified_rows_have_mixed_rubrics")
            if any(row.grade != grade or row.subjectTrack != track for row in qualified):
                raise ValueError("qualified_rows_have_wrong_grade_or_track")
            rows.extend(qualified)
            excluded.update(rejected)
            entry.update({
                "verified": True,
                "sourceItems": len(json.loads(source.read_text(encoding="utf-8"))),
                "qualifiedItems": len(qualified),
                "difficulty": dict(Counter(row.intendedDifficulty.value for row in qualified)),
                "excluded": dict(rejected),
            })
        except (OSError, ValueError, KeyError, AssertionError) as exc:
            entry.update({"verified": False, "failure": str(exc)})
            report["failures"].append(f"{class_name}:{exc}")
    report["qualifiedRowsFromVerifiedClasses"] = len(rows)
    report["exclusionSummary"] = dict(excluded)
    if report["failures"]:
        report["trainingStatus"] = "blocked_revalidation_incomplete"
        return report

    report["revalidationComplete"] = True
    snapshot = build_snapshot(
        rows, snapshot_id=args.snapshot_id or f"{args.output_dir.parent.name}-{args.output_dir.name}-allgrades",
        training_grades=tuple(range(1, 13)), required_grades=tuple(range(1, 13)),
        required_grade_tracks=GRADE_TRACKS, exclusion_summary=dict(excluded),
        label_provenance=LABEL_PROVENANCE, rubric_family=args.rubric_version,
    )
    # This verifies delivery provenance, keys, hashes and every item version in
    # addition to the trainer's own leakage and coverage checks.
    AssessmentStore.validate_snapshot(snapshot)
    snapshot_file = args.output_dir / "dataset_snapshot.json"
    save_snapshot(snapshot, snapshot_file)
    split_by_id = {entry.questionVersionId: entry.split for entry in snapshot.splitManifest}
    report.update({
        "snapshot": str(snapshot_file),
        "snapshotHash": snapshot.snapshotHash,
        "splitManifestHash": snapshot.splitManifestHash,
        "readyForTraining": not snapshot.gateFailures,
        "failures": snapshot.gateFailures,
        "splits": {
            split: {
                "count": sum(split_by_id[row.questionVersionId] == split for row in snapshot.rows),
                "difficulty": dict(Counter(row.intendedDifficulty.value for row in snapshot.rows
                                           if split_by_id[row.questionVersionId] == split)),
                "gradeTracks": dict(Counter(f"{row.grade}:{row.subjectTrack}" for row in snapshot.rows
                                            if split_by_id[row.questionVersionId] == split)),
            } for split in ("train", "validation", "test")
        },
    })
    command = [
        sys.executable, "-m", "app.training.v2.train_lora",
        "--snapshot", str(snapshot_file), "--output-dir", str(args.output_dir / "artifact"),
        "--work-dir", str(args.output_dir / "work"),
        "--model-version", args.model_version or f"{args.output_dir.parent.name}-{args.output_dir.name}-allgrades",
        "--rubric-version", args.rubric_version, "--representation", "solution",
        "--architecture", "grade-aware-ordinal-v2", "--resume",
    ]
    report["trainingCommand"] = command
    report["trainingStatus"] = "ready" if not snapshot.gateFailures else "blocked_data_gates"
    return report


def build_trained_diagnostics(report: dict[str, Any], output_dir: Path) -> list[dict[str, Any]]:
    """Stage diagnostics and verify source-shaped arrays remain exactly identical."""
    results = []
    for class_name, entry in report["classes"].items():
        source, original_bundle = Path(entry["source"]), Path(entry["bundle"])
        manifest = json.loads((original_bundle / "manifest.json").read_text(encoding="utf-8"))
        destination = output_dir / "diagnostics" / class_name
        destination.parent.mkdir(parents=True, exist_ok=True)
        command = [
            sys.executable, str(ROOT / "scripts/build_blind_validation_bundle.py"),
            "--source", str(source),
            "--checkpoint", manifest["sourceFiles"]["blindCheckpoint"]["path"],
            "--audit", manifest["sourceFiles"]["blindAudit"]["path"],
            "--artifact", str(output_dir / "artifact"), "--output-dir", str(destination),
        ]
        with (destination.parent / f"{class_name}.log").open("w", encoding="utf-8") as log:
            completed = subprocess.run(command, cwd=ROOT, stdout=log, stderr=subprocess.STDOUT)
        if completed.returncode:
            raise ValueError(f"offline_diagnostics_failed:{class_name}:exit={completed.returncode}")
        verify_bundle(source, destination)
        original_rows = json.loads(ai_validation_path(original_bundle).read_text(encoding="utf-8"))
        updated_rows = json.loads((destination / "validation_results.json").read_text(encoding="utf-8"))
        if not isinstance(original_rows, list) or updated_rows != original_rows:
            raise ValueError(f"offline_diagnostics_changed_locked_export:{class_name}")
        results.append({"class": class_name, "bundle": str(destination),
                        "verified": True, "databaseArrayUnchanged": True,
                        "promotedToActive": False, "newLlmCalls": 0})
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=ROOT / "output/pretest")
    parser.add_argument("--bundle-root", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--rubric-version", default=RUBRIC_VERSION.replace("-sd-grade-aware", "-grade-aware"))
    parser.add_argument("--snapshot-id")
    parser.add_argument("--model-version")
    parser.add_argument("--execute-training", action="store_true")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    report_file = args.output_dir / "readiness.json"
    if report_file.exists() or (args.output_dir / "dataset_snapshot.json").exists():
        parser.error("choose a new output directory; readiness reports and snapshots are immutable")
    try:
        report = prepare(args)
    except (OSError, ValueError, AssertionError) as exc:
        report = {"readyForTraining": False, "trainingStatus": "blocked_dataset_verification", "failures": [str(exc)]}
    report_file.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({key: report.get(key) for key in
                      ("revalidationComplete", "readyForTraining", "trainingStatus", "failures")},
                     ensure_ascii=False, indent=2))
    if not report.get("readyForTraining"):
        return 2
    if args.execute_training:
        # Capture training output as a local artifact, allowing the caller to
        # poll readiness.json while a long CPU run is in progress.
        report["trainingStatus"] = "running"
        report_file.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        with (args.output_dir / "training.log").open("w", encoding="utf-8") as log:
            completed = subprocess.run(report["trainingCommand"], cwd=ROOT, stdout=log, stderr=subprocess.STDOUT)
        report["trainingStatus"] = "completed" if completed.returncode == 0 else "failed"
        report["trainingExitCode"] = completed.returncode
        return_code = completed.returncode
        if return_code == 0:
            try:
                artifact = args.output_dir / "artifact"
                model = load_and_verify_manifest(artifact)
                if (model.datasetHash != report["snapshotHash"]
                        or model.splitManifestHash != report["splitManifestHash"]):
                    raise ValueError("trained artifact does not reference this frozen dataset")
                report["trainedArtifact"] = {
                    "path": str(artifact), "modelVersion": model.modelVersion,
                    "dataGatesPassed": model.dataGatesPassed,
                    "antiCollapsePassed": model.antiCollapsePassed,
                    "promotionGatesPassed": model.promotionGates.get("passed", False),
                    "promotionGateFailures": model.promotionGates.get("failures", []),
                    "researchOnly": model.researchOnly,
                    "approvedForProvisional": model.approvedForProvisional,
                    "servable": model.servable,
                }
                report["trainingStatus"] = "completed_candidate"
                report["diagnosticBundles"] = build_trained_diagnostics(report, args.output_dir)
            except (OSError, ValueError) as exc:
                report["trainingStatus"] = "failed_artifact_verification"
                report["failures"].append(str(exc))
                return_code = 2
        report_file.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        return return_code
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
