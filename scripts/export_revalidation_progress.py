"""Export current blind revalidation progress offline without promoting drafts.

The source-shaped arrays live beside the working checkpoint. Missing decisions
have null difficulty/score, confidence zero and inactive status; old labels are
never carried forward. Active reports and paid checkpoints remain unchanged.
"""
from __future__ import annotations

import argparse
from collections import Counter
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.llm.silver import (SilverAdjudicationResult, SilverRunResult, aggregate_silver_runs,
                           requested_runs_for, requested_run_indices)
from app.silver.exports import DATABASE_SCHEMA, database_items
from app.silver.policy import qualification
from scripts.build_validation_bundle_kelas1 import structural_validation
from scripts.generate_silver_labels_kelas1 import atomic_write, input_hash
from scripts.refresh_ai_validation_reports import verify_bundle, verify_evidence
from scripts.revalidate_all_grades import CLASSES

HEADS = ("mathCognitiveDomain", "knowledgeDimension", "intendedDifficulty")


def read(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def current_decision(original: dict, record: dict, source_dir: Path, *, requested_runs: int = 3) -> tuple[dict, dict]:
    """Recompute stored evidence using the item's explicit N=1 or N=3 policy."""
    runs = [SilverRunResult.model_validate(run) for run in record.get("runs", [])]
    indices = [run.runIndex for run in runs]
    required = set(requested_run_indices(record, requested_runs))
    if len(set(indices)) != len(indices) or any(index not in required for index in indices):
        raise ValueError("checkpoint run indices must be unique and match the evaluation mode")
    successful = {run.runIndex for run in runs if run.status == "success"}
    missing = sorted(required - successful)
    adjudication = record.get("adjudication") or None
    typed_adjudication = SilverAdjudicationResult.model_validate(adjudication) if adjudication else None
    aggregate = aggregate_silver_runs(runs, typed_adjudication if not missing else None,
                                      requested_runs=requested_runs)
    final = not missing and aggregate["needsAdjudication"] is False
    conservative = deepcopy(record)
    conservative["aggregate"] = aggregate
    if not final:
        conservative["aggregate"]["eligibleForTraining"] = False
        for head in HEADS:
            conservative["aggregate"].setdefault("heads", {}).setdefault(head, {})["label"] = None
    labels, route = qualification(conservative, structural_validation(original, source_dir), original)
    serialized_runs = []
    for run in runs:
        payload = run.model_dump(mode="json")
        output = payload.pop("output") or {}
        serialized_runs.append({**payload, "heads": {head: output.get(head, {}) for head in HEADS}})
    decision = {"questionId": str(original["_id"]), "finalRouting": route,
                "llmAdvisory": {"advisoryLabels": labels, "requestedRuns": requested_runs,
                                "runs": serialized_runs}}
    if "requestedRunIndices" in record:
        decision["llmAdvisory"]["requestedRunIndices"] = sorted(required)
    progress = {"questionId": str(original["_id"]), "inputHash": input_hash(original),
                "status": "final" if final else "draft", "fullComplete": final,
                "successfulRunIndices": sorted(successful), "missingRunIndices": missing,
                "needsAdjudication": bool(not missing and aggregate["needsAdjudication"]),
                "adjudicationStatus": adjudication.get("status") if adjudication else None,
                "finalRouting": route, "eligibleForTraining": bool(final and aggregate["eligibleForTraining"]),
                "contentStatus": aggregate["contentStatus"], "answerKeyStatus": aggregate["answerKeyStatus"]}
    progress.update(requestedRuns=requested_runs, validationMethod="blind_n1" if requested_runs == 1 else "blind_n3_with_ai_adjudication",
                    consistencyMeasured=bool(final and requested_runs == 3))
    return decision, progress


def export_class(source: Path, checkpoint: Path, output_dir: Path, *, grade: int, track: str) -> dict:
    source_bytes, checkpoint_bytes = source.read_bytes(), checkpoint.read_bytes()
    payload = json.loads(checkpoint_bytes)
    if payload.get("subjectTrack", "regular") != track:
        raise ValueError("checkpoint track differs from the requested class")
    verify_evidence(source, checkpoint, grade)
    originals = json.loads(source_bytes)
    if not originals or len({str(row["_id"]) for row in originals}) != len(originals):
        raise ValueError("source must contain unique questions")
    required_fields = {"cognitive_level", "cognitive_score", "confidence_score", "status"}
    if any(not required_fields <= set(row) for row in originals):
        raise ValueError("source-shaped export requires the four validation columns")
    decisions, item_progress = [], []
    for original in originals:
        record = payload["items"].get(str(original["_id"]), {})
        decision, progress = current_decision(original, record, source.parent,
                                              requested_runs=requested_runs_for(payload, record))
        decisions.append(decision)
        item_progress.append(progress)
    # Reuse only diagnostics locked to this exact checkpoint. Progress exports
    # without model evidence report numeric 0 with unavailable metadata.
    if payload.get("requestedRuns", 3) == 1 and (output_dir / "manifest.json").is_file():
        diagnostic_manifest = read(output_dir / "manifest.json")
        if diagnostic_manifest["sourceFiles"]["blindCheckpoint"]["sha256"] == hashlib.sha256(checkpoint_bytes).hexdigest():
            verify_bundle(source, output_dir)
            from app.silver.exports import load_decision_bundle
            locked = {d["questionId"]: d for d in load_decision_bundle(output_dir)["items"]}
            for decision in decisions:
                if decision["llmAdvisory"].get("requestedRuns", 3) == 1:
                    evidence = locked[decision["questionId"]]
                    if evidence["llmAdvisory"]["advisoryLabels"] != decision["llmAdvisory"]["advisoryLabels"]:
                        raise ValueError("model diagnostics refer to different locked labels")
                    decision["indobert"] = evidence["indobert"]
    rows = database_items(originals, decisions)
    full_complete = all(item["fullComplete"] for item in item_progress)
    encoded = (json.dumps(rows, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode("utf-8")
    active = source.parent / "hasil_validasi"
    active_matches = False
    if full_complete and (active / "manifest.json").is_file():
        manifest = read(active / "manifest.json")
        active_checkpoint = Path(manifest["sourceFiles"]["blindCheckpoint"]["path"])
        active_rubric = read(active_checkpoint).get("rubricVersion")
        if active_rubric == payload["rubricVersion"]:
            verify_bundle(source, active)
            from app.silver.exports import ai_validation_path
            original_ai_path = ai_validation_path(active, manifest)
            if read(original_ai_path) != rows:
                raise ValueError("complete export disagrees with the verified active array on this rubric")
            encoded = original_ai_path.read_bytes()
            active_matches = encoded == (active / "validation_results.json").read_bytes()
    if source.read_bytes() != source_bytes or checkpoint.read_bytes() != checkpoint_bytes:
        raise ValueError("source or checkpoint changed during offline export")
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "validation_results.json"
    if destination.resolve() == (active / "validation_results.json").resolve():
        raise ValueError("progress export must not replace active validation results")
    temporary = destination.with_suffix(".json.tmp")
    temporary.write_bytes(encoded)
    temporary.replace(destination)
    sidecar = {"schemaVersion": "revalidation-progress-export-v1", "databaseSchemaVersion": DATABASE_SCHEMA,
               "createdAt": datetime.now(timezone.utc).isoformat(), "class": source.parent.name,
               "grade": grade, "subjectTrack": track, "status": "final" if full_complete else "draft",
               "fullComplete": full_complete, "researchOnly": True, "newApiCalls": 0,
               "activeOutputsModified": False, "checkpointsModified": False,
               "model": payload["model"], "rubricVersion": payload["rubricVersion"],
               "rubricHash": payload["rubricHash"], "promptVersion": payload["promptVersion"],
               "source": str(source), "sourceHash": hashlib.sha256(source_bytes).hexdigest(),
               "checkpoint": str(checkpoint), "checkpointHash": hashlib.sha256(checkpoint_bytes).hexdigest(),
               "checkpointExecutionStatus": payload.get("executionStatus"),
               "sourceInputPromptResponseAndRubricHashesVerified": True,
               "validationResultsHash": hashlib.sha256(encoded).hexdigest(),
               "byteIdenticalToVerifiedActiveArray": active_matches,
               "summary": {"questionCount": len(rows), "finalItems": sum(item["fullComplete"] for item in item_progress),
                           "draftItems": sum(not item["fullComplete"] for item in item_progress),
                           "missingInitialRuns": sum(len(item["missingRunIndices"]) for item in item_progress),
                           "pendingAdjudications": sum(item["needsAdjudication"] for item in item_progress),
                           "difficultyDistribution": dict(Counter(row["cognitive_level"] or "undecided" for row in rows)),
                           "statusDistribution": dict(Counter(row["status"] for row in rows))},
               "draftPolicy": "Unfinished items have null difficulty/score, confidence 0 and inactive status; final content blockers remain inactive.",
               "items": item_progress}
    atomic_write(sidecar, output_dir / "export_status.json")
    return sidecar


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-name", required=True)
    parser.add_argument("--source-root", type=Path, default=ROOT / "output/pretest")
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9_-]+", args.batch_name):
        parser.error("batch-name must be one directory name")
    results = []
    for name, grade, track in CLASSES:
        source = args.source_root.resolve() / name / "soal_pretest_db.json"
        directory = source.parent / args.batch_name
        report = export_class(source, directory / "silver_labels.json", directory, grade=grade, track=track)
        results.append({key: report[key] for key in ("class", "grade", "subjectTrack", "status", "fullComplete", "summary",
                                                  "validationResultsHash", "byteIdenticalToVerifiedActiveArray")})
        print(json.dumps(results[-1], ensure_ascii=False), flush=True)
    run_dir = ROOT / "runs" / args.batch_name
    run_dir.mkdir(parents=True, exist_ok=True)
    atomic_write({"schemaVersion": "all-grade-progress-exports-v1", "newApiCalls": 0,
                  "activeOutputsModified": False, "checkpointsModified": False, "classes": results},
                 run_dir / "progress_exports.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
