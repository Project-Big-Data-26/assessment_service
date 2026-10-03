"""Freeze qualified active AI bundles for training and student delivery, offline."""
from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.assessment.store import AssessmentStore
from app.classification.v2.kko import detect_kko
from app.silver.policy import LABEL_PROVENANCE, qualification, resolve_answer_key
from app.silver.exports import load_decision_bundle, operational_identity
from app.training.v2.dataset import TrainingRow, build_snapshot, save_snapshot
from scripts.build_validation_bundle_kelas1 import structural_validation
from scripts.refresh_ai_validation_reports import load, verify_bundle, verify_evidence


def rows_from_bundle(source: Path, bundle: Path) -> tuple[list[TrainingRow], Counter]:
    verify_bundle(source, bundle)
    manifest = load(bundle / "manifest.json")
    checkpoint_path = Path(manifest["sourceFiles"]["blindCheckpoint"]["path"])
    verify_evidence(source, checkpoint_path, manifest["class"])
    checkpoint = load(checkpoint_path)
    originals = load(source)
    expected = [str(q["_id"]) for q in originals]
    if len(expected) != len(set(expected)) or set(expected) != set(checkpoint["items"]):
        raise ValueError("source/checkpoint coverage is not one-to-one")
    exported = {q["questionId"]: q for q in load(bundle / "questions.json")["items"]}
    decisions = {q["questionId"]: q for q in load_decision_bundle(bundle)["items"]}
    rows, excluded = [], Counter()
    for original in originals:
        qid = str(original["_id"])
        record = checkpoint["items"][qid]
        question, decision = exported[qid], decisions[qid]
        labels, route = qualification(record, structural_validation(original, source.parent), original)
        if route != "silver_ready":
            excluded[route] += 1
            continue
        successful = [r for r in record.get("runs", []) if r.get("status") == "success"]
        if len(successful) != 3 or {r["runIndex"] for r in successful} != {1, 2, 3}:
            excluded["three_blind_runs_required"] += 1
            continue
        aggregate = record["aggregate"]
        raw_key = aggregate.get("verifiedAnswerKey")
        key, solution = resolve_answer_key(raw_key, original["options"]), aggregate.get("verifiedMinimalSolution")
        transcript = aggregate.get("visualTranscript")
        if (aggregate.get("contentStatus") != "valid" or aggregate.get("answerKeyStatus") != "verified"
                or key != original.get("jawaban") or not solution):
            excluded["content_key_or_solution_unqualified"] += 1
            continue
        if original.get("image_url") and not transcript:
            excluded["visual_transcript_missing"] += 1
            continue
        if labels != decision["llmAdvisory"]["advisoryLabels"]:
            raise ValueError(f"locked labels and exported decision disagree: {qid}")
        track, namespace = checkpoint.get("subjectTrack", "regular"), source.parent.name
        identity = f"{namespace}:{qid}"
        version_id, content_hash = operational_identity(question, key, solution, transcript, namespace, track)
        rows.append(TrainingRow(
            questionId=identity, questionVersionId=version_id,
            contentVersion=question["contentVersion"], contentHash=content_hash,
            sourceGroup=f"{namespace}:{original.get('source_family') or original.get('subbab_id') or qid}",
            grade=question["grade"], subjectTrack=track, topic=question["topic"],
            subtopic=question.get("subtopic"), questionType="multiple_choice",
            stimulus=question.get("stimulus"), stem=question["stem"], options=question["options"],
            verifiedMinimalSolution=solution, visualTranscript=transcript,
            detectedKko=detect_kko(question["stem"]), rubricVersion=checkpoint["rubricVersion"],
            decisionProvenance={"kind": LABEL_PROVENANCE, "decisionId": decision["decisionId"],
                "provider": checkpoint["provider"], "model": checkpoint["model"],
                "promptVersion": checkpoint["promptVersion"], "checkpointHash": manifest["sourceFiles"]["blindCheckpoint"]["sha256"],
                "sourceInputHash": record["inputHash"], "sourceResponseHashes": [r["responseHash"] for r in successful],
                "successfulRuns": 3, "contentStatus": "valid", "answerKeyStatus": "verified",
                "verifiedAnswerKey": key, "rawVerifiedAnswerKey": raw_key, "visualEssential": bool(original.get("image_url")),
                "sourceContentHash": question["contentHash"], "visualAssetHashes": question.get("visualAssetHashes", {}),
                "adjudicated": bool(aggregate.get("adjudicated"))}, **labels))
    return rows, excluded


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=ROOT / "output/pretest")
    parser.add_argument("--class-name", action="append", help="kelas1 .. kelas12, kelas11_tl, kelas12_tl; default all")
    parser.add_argument("--snapshot-id", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--assessment-db", type=Path, help="Register for API delivery; held versions are excluded")
    args = parser.parse_args()
    if args.output.exists():
        parser.error("choose a new immutable output path")
    sources = sorted(args.source_root.glob("kelas*/soal_pretest_db.json"))
    if args.class_name:
        sources = [p for p in sources if p.parent.name in args.class_name]
        if {p.parent.name for p in sources} != set(args.class_name):
            parser.error("a selected class does not have a source dataset")
    if not sources:
        parser.error("no class datasets found")
    rows, excluded = [], Counter()
    db = AssessmentStore(args.assessment_db) if args.assessment_db else None
    for source in sources:
        qualified, rejected = rows_from_bundle(source, source.parent / "hasil_validasi")
        excluded.update(rejected)
        for row in qualified:
            if db and db.is_held(row.questionVersionId):
                excluded["empirical_ai_hold"] += 1
            else:
                rows.append(row)
    snapshot = build_snapshot(rows, snapshot_id=args.snapshot_id, exclusion_summary=dict(excluded))
    AssessmentStore.validate_snapshot(snapshot)
    save_snapshot(snapshot, args.output)
    if db:
        db.register_snapshot(snapshot)
    print(f"Frozen {len(rows)} AI silver items; excluded={dict(excluded)}; training test={snapshot.testUnlockStatus}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
