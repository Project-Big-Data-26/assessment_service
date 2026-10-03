"""Compact database exports with a separately verified, lossless decision audit."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from app.classification.v2.serializer import canonical_json_hash

COMPACT_SCHEMA = "validated-question-bundle-v1-ai-metadata"
AUDIT_FILE = "bukti_validasi/decision_audit.json"


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
    if result.get("schemaVersion") != COMPACT_SCHEMA:
        return result
    reference = result["decisionAudit"]
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
