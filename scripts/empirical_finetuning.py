"""Versioned population-scoped IRT targets and automatic IndoBERT challengers."""
from contextlib import closing
import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys

from app.assessment.store import AssessmentStore
from app.classification.v2.serializer import canonical_json_hash
from app.training.v2.dataset import (DatasetSnapshot, save_snapshot,
                                      validate_split_integrity, validate_split_minimums)
from scripts.generate_silver_labels_kelas1 import atomic_write


def target_identity(snapshot):
    payload = snapshot.model_dump(mode="json")
    for row in payload["rows"]:
        evidence = row["decisionProvenance"].get("empiricalTrainingTarget", {})
        evidence.pop("analysisSnapshotId", None)
        evidence.pop("analysisSnapshotHash", None)
    payload.pop("snapshotHash", None)
    return canonical_json_hash(payload)


def prepare_snapshot(base, labels, held):
    """Keep original splits and cognitive labels; qualify every empirical join."""
    AssessmentStore.validate_snapshot(base)
    by_version = {row.questionVersionId: row for row in base.rows}
    targets = {}
    for item in labels["items"]:
        if item["difficultySource"] != "irt" or item.get("action") != "retain":
            continue
        version = item["questionVersionId"]
        if version in held:
            continue
        original = by_version.get(version)
        if original is None:
            # Expansion/held-out-grade rows never enter training implicitly.
            continue
        if (original.contentHash != item["contentHash"] or original.grade != labels["grade"]
                or original.intendedDifficulty.value != item["intendedDifficulty"]):
            raise ValueError("empirical target does not match immutable training content")
        target = item.get("empiricalDifficulty")
        if target not in ("Easy", "Medium", "Hard"):
            raise ValueError("unsupported empirical difficulty")
        if version in targets and targets[version] != target:
            raise ValueError("conflicting empirical targets")
        targets[version] = target
    changed = {version: target for version, target in targets.items()
               if by_version[version].intendedDifficulty.value != target}
    if not changed:
        return None, {"status": "no_label_changes", "qualifiedTargets": len(targets)}
    identity = canonical_json_hash({"base": base.snapshotHash, "splits": base.splitManifestHash,
        "assessmentId": labels["assessmentId"], "populationId": labels["populationId"],
        "assessmentFamily": labels["assessmentFamily"], "targets": targets, "held": sorted(held)})
    snapshot = base.model_copy(deep=True)
    rows = []
    for row in snapshot.rows:
        if row.questionVersionId in held:
            continue
        if row.questionVersionId in targets:
            original = row.intendedDifficulty.value
            # This is an explicitly empirical research target in the legacy
            # trainer's difficulty field, never an AI-silver delivery label.
            payload = row.model_dump(mode="json")
            payload["intendedDifficulty"] = targets[row.questionVersionId]
            payload["decisionProvenance"] = {**payload["decisionProvenance"],
                "kind": "irt_empirical_difficulty_with_ai_cognitive_labels",
                "originalAiProvenance": row.decisionProvenance,
                "empiricalTrainingTarget": {"originalIntendedDifficulty": original,
                    "empiricalDifficulty": targets[row.questionVersionId],
                    "assessmentId": labels["assessmentId"], "populationId": labels["populationId"],
                    "analysisSnapshotId": labels["snapshotId"], "analysisSnapshotHash": labels["snapshotHash"],
                    "contentHash": row.contentHash}}
            row = type(row).model_validate(payload)
        rows.append(row)
    retained = {row.questionVersionId for row in rows}
    snapshot.rows = rows
    snapshot.splitManifest = [entry for entry in snapshot.splitManifest if entry.questionVersionId in retained]
    snapshot.expansionRows = []
    snapshot.expansionHash = canonical_json_hash([])
    snapshot.snapshotId = f"irt-training-{identity[:24]}"
    snapshot.snapshotHash = canonical_json_hash([row.model_dump(mode="json")
        for row in sorted(rows, key=lambda row: row.questionVersionId)])
    snapshot.splitManifestHash = canonical_json_hash([entry.model_dump(mode="json") for entry in snapshot.splitManifest])
    snapshot.labelProvenance = "irt_empirical_difficulty_with_ai_cognitive_labels"
    snapshot.researchOnly = True
    snapshot.gateFailures = list(dict.fromkeys([*base.gateFailures,
        *validate_split_integrity(rows, snapshot.splitManifest),
        *validate_split_minimums(rows, snapshot.splitManifest,
            required_grades=tuple(snapshot.trainingGrades),
            required_grade_tracks=tuple(snapshot.requiredGradeTracks))]))
    snapshot.testUnlockStatus = "locked"
    return snapshot, {"status": "prepared", "identity": identity,
                      "qualifiedTargets": len(targets), "changedLabels": len(changed),
                      "excludedHeldVersions": len(set(by_version) & held),
                      "gateFailures": snapshot.gateFailures}


def process_assessment(db, assessment_id, analysis_id, options, output, root):
    # Read authoritative stored analysis rather than trusting exported JSON.
    from scripts.nightly_pipeline import effective_labels
    record = db.execute("SELECT document FROM assessments WHERE id=?", (assessment_id,)).fetchone()
    if not record:
        return {"status": "waiting_for_data"}
    assessment = json.loads(record[0])
    record = db.execute("SELECT document FROM snapshots WHERE id=? AND assessment_id=?",
                        (analysis_id, assessment_id)).fetchone()
    if not record:
        return {"status": "waiting_for_data"}
    analysis = json.loads(record[0])
    evidence = {key: value for key, value in analysis.items()
                if key not in ("snapshotHash", "snapshotId", "createdAt")}
    if canonical_json_hash(evidence) != analysis.get("snapshotHash"):
        raise ValueError("empirical analysis checksum mismatch")
    if (analysis.get("dataOrigin") != "server_scored" or not analysis["readiness"]["passed"]
            or analysis["irt"]["status"] != "estimated"):
        return {"status": "waiting_for_qualified_irt"}
    if any(analysis[key] != assessment[key] for key in ("assessmentId", "populationId", "assessmentFamily", "grade")):
        raise ValueError("empirical assessment scope mismatch")
    decisions = [json.loads(row[0]) for row in db.execute(
        "SELECT document FROM empirical_decisions WHERE snapshot_id=?", (analysis_id,))]
    labels = effective_labels(analysis, decisions)
    record = db.execute("SELECT document FROM dataset_snapshots WHERE id=?", (assessment["snapshotId"],)).fetchone()
    if not record:
        return {"status": "waiting_for_training_snapshot"}
    base = DatasetSnapshot.model_validate_json(record[0])
    if base.snapshotHash != assessment["snapshotHash"]:
        raise ValueError("assessment training snapshot checksum mismatch")
    held = {row.questionVersionId for row in base.rows if AssessmentStore._held(db, row.questionVersionId)}
    snapshot, result = prepare_snapshot(base, labels, held)
    if snapshot is None:
        return result
    # Hyperparameter changes produce a separate immutable training attempt.
    run_id = canonical_json_hash({"identity": result["identity"], "options": options})[:24]
    destination = output / run_id
    destination.mkdir(parents=True, exist_ok=True)
    state_path = destination / "status.json"
    dataset = destination / "snapshot.json"
    if not dataset.exists():
        save_snapshot(snapshot, dataset)
    else:
        existing = DatasetSnapshot.model_validate_json(dataset.read_text(encoding="utf-8"))
        # Same labels can have newer analysis evidence; reuse first locked evidence.
        if (target_identity(existing) != target_identity(snapshot)
                or canonical_json_hash([row.model_dump(mode="json") for row in
                    sorted(existing.rows, key=lambda row: row.questionVersionId)]) != existing.snapshotHash):
            raise ValueError("immutable empirical dataset identity mismatch")
        snapshot = existing
    if state_path.exists():
        previous = json.loads(state_path.read_text(encoding="utf-8"))
        if previous.get("status") == "trained":
            from app.classification.v2.artifact import load_and_verify_manifest
            manifest = load_and_verify_manifest(destination / "model")
            if manifest.datasetHash != snapshot.snapshotHash or not manifest.researchOnly:
                raise ValueError("reused empirical model dataset checksum mismatch")
            return {**previous, "reused": True}
    result.update(dataset=str(dataset), assessmentId=assessment_id,
                  populationId=labels["populationId"], productionModelUpdated=False,
                  artifact=str(destination / "model"), labelTarget="empiricalDifficulty")
    if result["gateFailures"]:
        result["status"] = "waiting_for_training_data"
    elif not options.get("enabled", False):
        result["status"] = "training_disabled"
    else:
        result["status"] = "training"
        atomic_write(result, state_path)
        rubric = snapshot.rubricFamily or next(iter({row.rubricVersion for row in snapshot.rows}))
        if not snapshot.rubricFamily and len({row.rubricVersion for row in snapshot.rows}) != 1:
            raise ValueError("mixed training rubrics require a declared family")
        command = [sys.executable, "-X", "utf8", "-m", "app.training.v2.train_lora",
            "--snapshot", str(dataset), "--output-dir", str(destination / "model"),
            "--work-dir", str(destination / "work"), "--model-version", f"irt-challenger-{run_id}",
            "--rubric-version", rubric, "--single-trial", "--epochs", str(options.get("epochs", 3)),
            "--patience", "2"]
        with (destination / "training.log").open("a", encoding="utf-8") as log:
            try:
                code = subprocess.run(command, cwd=root, stdout=log, stderr=subprocess.STDOUT,
                    timeout=options.get("timeoutSeconds", 21600)).returncode
                result.update(status="trained" if code == 0 else "training_failed", exitCode=code)
                if code == 0:
                    from app.classification.v2.artifact import load_and_verify_manifest
                    manifest = load_and_verify_manifest(destination / "model")
                    if manifest.datasetHash != snapshot.snapshotHash or not manifest.researchOnly:
                        raise ValueError("empirical training artifact provenance mismatch")
                    result["evaluation"] = manifest.metrics
            except subprocess.TimeoutExpired:
                result["status"] = "training_timeout"
    atomic_write(result, state_path)
    return result


def run_feedback(config, psychometrics, output, root):
    options = config.get("empiricalFineTuning", {})
    if not options.get("enabled", False):
        return {"status": "disabled", "assessments": []}
    db_path = Path(os.getenv("ASSESSMENT_DB_PATH", "data/local/assessments.sqlite3"))
    if not db_path.is_absolute():
        db_path = root / db_path
    results = []
    if db_path.is_file():
        with closing(sqlite3.connect(db_path.resolve().as_uri() + "?mode=ro", uri=True)) as db:
            for entry in psychometrics.get("assessments", []):
                if entry.get("status") != "estimated":
                    continue
                try:
                    result = process_assessment(db, entry["assessmentId"], entry["snapshotId"], options, output, root)
                except Exception as exc:
                    result = {"status": "failed", "errorType": type(exc).__name__}
                results.append({"assessmentId": entry["assessmentId"], **result})
    return {"status": "processed" if results else "waiting_for_qualified_irt", "assessments": results}
