"""Prepare an offline readiness report; never relabel, train, or call Gemini."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(snapshot_path: Path, checkpoint_path: Path, output: Path) -> dict:
    if output.exists():
        raise ValueError("choose a new immutable report path")
    snapshot, checkpoint = load(snapshot_path), load(checkpoint_path)
    rows = snapshot["rows"]
    split_by_version = {
        entry["questionVersionId"]: entry["split"]
        for entry in snapshot["splitManifest"]
    }
    candidates = []
    for qid, record in checkpoint["items"].items():
        aggregate = record.get("aggregate") or {}
        labels = {
            head: detail.get("label")
            for head, detail in aggregate.get("heads", {}).items()
        }
        if labels.get("intendedDifficulty") != "Hard":
            continue
        successful = [run for run in record["runs"] if run["status"] == "success"]
        requested_runs = record.get("requestedRuns", checkpoint.get("requestedRuns"))
        if len(successful) != 1 or requested_runs != 1:
            continue
        candidates.append({
            "questionId": qid,
            "inputHash": record["inputHash"],
            "labels": labels,
            "successfulRuns": 1,
            "existingResponseHashes": [run["responseHash"] for run in successful],
            "existingRunIndices": [run["runIndex"] for run in successful],
            "additionalRunsForN3": 2,
            "contentStatus": aggregate.get("contentStatus"),
            "answerKeyStatus": aggregate.get("answerKeyStatus"),
            "currentlyEligibleForTraining": aggregate.get("eligibleForTraining", False),
        })
    head_names = ("mathCognitiveDomain", "knowledgeDimension", "intendedDifficulty")
    report = {
        "purpose": "SD Hard training readiness; existing evidence only",
        "inputs": {
            "snapshot": {"path": str(snapshot_path), "sha256": digest(snapshot_path)},
            "exerciseCheckpoint": {"path": str(checkpoint_path), "sha256": digest(checkpoint_path)},
        },
        "qualifiedN3Rows": len(rows),
        "qualifiedLabelCounts": {
            head: dict(Counter(row[head] for row in rows)) for head in head_names
        },
        "difficultyBySplit": {
            split: dict(Counter(
                row["intendedDifficulty"] for row in rows
                if split_by_version[row["questionVersionId"]] == split
            )) for split in ("train", "validation", "test")
        },
        "gateFailures": snapshot["gateFailures"],
        "fullThreeHeadTrainingReady": not snapshot["gateFailures"],
        "singleRunHardCandidates": candidates,
        "singleRunHardCandidateCount": len(candidates),
        "additionalBlindCallsForCandidates": sum(c["additionalRunsForN3"] for c in candidates),
        "possibleAdditionalAdjudicationCalls": len(candidates),
        "limitations": [
            "N=1 candidates are excluded from the normal N=3 training dataset.",
            "Completing N=3 may change candidate labels; Hard is not guaranteed.",
            "Even if all candidates remain Hard, full three-head coverage gates remain unmet.",
            "Repeated or augmented copies do not count as independent evaluation examples.",
            "Confidence must come from evaluated model probabilities, without a fabricated floor.",
        ],
        "modelTrainingExecuted": False,
        "newApiCalls": 0,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot", required=True, type=Path)
    parser.add_argument("--checkpoint", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    report = prepare(args.snapshot, args.checkpoint, args.output)
    print(json.dumps({key: report[key] for key in (
        "qualifiedN3Rows", "singleRunHardCandidateCount", "additionalBlindCallsForCandidates",
        "fullThreeHeadTrainingReady", "newApiCalls",
    )}))


if __name__ == "__main__":
    main()
