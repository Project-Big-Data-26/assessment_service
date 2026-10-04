"""Database question exports with a separately verified, lossless decision audit."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from app.classification.v2.serializer import canonical_json_hash

COMPACT_SCHEMA = "validated-question-bundle-v1-ai-metadata"
DATABASE_SCHEMA = "validated-question-array-v2"
AUDIT_FILE = "bukti_validasi/decision_audit.json"
SCORE_POLICY = {"version": "intended-difficulty-score-v1",
                "mapping": {"Easy": 600, "Medium": 1000, "Hard": 1400},
                "meaning": "Initial difficulty score, not student ability or empirical IRT difficulty."}
CONFIDENCE_POLICY = {
    "version": "final-label-run-support-min-v1", "scale": "integer_0_100",
    "heads": ["mathCognitiveDomain", "knowledgeDimension", "intendedDifficulty"],
    "formula": "round(100 * min(final_label_supporting_runs_per_head / requested_runs))",
    "meaning": "AI run agreement with final labels; not a calibrated probability of correctness.",
    "denominator": "Requested initial runs; failures and abstentions do not support a label.",
    "adjudication": "Determines final labels; not counted as an additional vote.",
}


def final_label_support(decision: dict) -> dict[str, int]:
    advisory = decision["llmAdvisory"]
    requested = advisory.get("requestedRuns", 3)
    if not isinstance(requested, int) or isinstance(requested, bool) or requested < 1:
        raise ValueError("requestedRuns must be a positive integer")
    runs = advisory.get("runs", [])
    indices = [run["runIndex"] for run in runs]
    if len(set(indices)) != len(indices) or any(index not in range(1, requested + 1) for index in indices):
        raise ValueError("initial run indices must be unique and within requestedRuns")
    return {head: sum(
        run.get("status") == "success"
        and run.get("heads", {}).get(head, {}).get("action") == "classify"
        and advisory["advisoryLabels"].get(head) is not None
        and run.get("heads", {}).get(head, {}).get("label") == advisory["advisoryLabels"][head]
        for run in runs
    ) for head in CONFIDENCE_POLICY["heads"]}


def database_items(originals: list[dict], decisions: list[dict]) -> list[dict]:
    """Export only source columns, keeping source content and item order intact."""
    by_id = {d["questionId"]: d for d in decisions}
    expected = {str(q["_id"]) for q in originals}
    if len(expected) != len(originals) or len(by_id) != len(decisions) or set(by_id) != expected:
        raise ValueError("source/decision coverage must be one-to-one")
    rows = []
    for original in originals:
        decision = by_id[str(original["_id"])]
        advisory = decision["llmAdvisory"]
        labels = advisory["advisoryLabels"]
        difficulty = labels["intendedDifficulty"]
        if difficulty is not None and difficulty not in SCORE_POLICY["mapping"]:
            raise ValueError(f"unknown intended difficulty: {difficulty}")
        values = {"cognitive_level": labels["mathCognitiveDomain"],
                  "cognitive_score": SCORE_POLICY["mapping"].get(difficulty),
                  "confidence_score": round(100 * min(final_label_support(decision).values())
                                            / advisory.get("requestedRuns", 3)),
                  "status": decision["finalRouting"]}
        # Exact source schema: the database rows have no report/metadata fields.
        rows.append({key: values.get(key, value) for key, value in original.items()})
    return rows


def operational_identity(question: dict, key: str, solution: str, transcript: str | None,
                         namespace: str, track: str) -> tuple[str, str]:
    content = {"stem": question["stem"], "stimulus": question.get("stimulus"),
               "options": question["options"], "answerKey": key, "solution": solution,
               "visualTranscript": transcript, "visualAssetHashes": question.get("visualAssetHashes", {}),
               "grade": question["grade"], "subjectTrack": track}
    content_hash = canonical_json_hash(content)
    return f"{namespace}:{question['questionId']}:silver:{content_hash[:20]}", content_hash


def load_decision_bundle(bundle: Path) -> dict:
    result = json.loads((bundle / "validation_results.json").read_text(encoding="utf-8"))
    if isinstance(result, list):
        manifest = json.loads((bundle / "manifest.json").read_text(encoding="utf-8"))
        export = manifest["databaseExport"]
        if export["schemaVersion"] != DATABASE_SCHEMA:
            raise ValueError("unexpected database export schema")
        reference = export["decisionAudit"]
    elif result.get("schemaVersion") == COMPACT_SCHEMA:
        reference = result["decisionAudit"]
    else:
        return result
    if reference["path"] != AUDIT_FILE:
        raise ValueError("unexpected decision audit path")
    data = (bundle / AUDIT_FILE).read_bytes()
    if hashlib.sha256(data).hexdigest() != reference["sha256"]:
        raise ValueError("decision audit checksum mismatch")
    return json.loads(data)


def compact_items(originals: list[dict], decisions: list[dict], questions: list[dict],
                  checkpoint: dict, namespace: str) -> list[dict]:
    by_id = {d["questionId"]: d for d in decisions}
    exported = {q["questionId"]: q for q in questions}
    expected = {str(q["_id"]) for q in originals}
    if len(expected) != len(originals) or len(by_id) != len(decisions) or set(by_id) != expected:
        raise ValueError("source/decision coverage must be one-to-one")
    if set(exported) != expected or len(exported) != len(questions):
        raise ValueError("source/question coverage must be one-to-one")
    track = checkpoint.get("subjectTrack", "regular")
    items = []
    for original in originals:
        qid = str(original["_id"])
        decision = by_id[qid]
        labels = decision["llmAdvisory"]["advisoryLabels"]
        version, content_hash = None, None
        if decision["finalRouting"] == "silver_ready":
            aggregate = checkpoint["items"][qid]["aggregate"]
            version, content_hash = operational_identity(
                exported[qid], original["jawaban"], aggregate["verifiedMinimalSolution"],
                aggregate.get("visualTranscript"), namespace, track)
        items.append({**original, "cognitive_level": labels["mathCognitiveDomain"],
                      "cognitive_score": None, "confidence_score": None,
                      "ai_metadata": {
                          "label_provenance": "ai_silver",
                          "knowledge_dimension": labels["knowledgeDimension"],
                          "intended_difficulty": labels["intendedDifficulty"],
                          "validation_status": decision["finalRouting"],
                          "subject_track": track,
                          "decision_id": decision["decisionId"],
                          "question_version_id": version,
                          "content_hash": content_hash,
                      }})
    return items
