"""Database question exports with a separately verified, lossless decision audit."""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

from app.classification.v2.serializer import canonical_json_hash

COMPACT_SCHEMA = "validated-question-bundle-v1-ai-metadata"
LEGACY_DATABASE_SCHEMA = "validated-question-array-v2"
PREVIOUS_DATABASE_SCHEMA = "validated-question-array-v3-difficulty"
DATABASE_SCHEMA = "validated-question-array-v4-active-status"
STATUS_POLICY = {"version": "database-active-status-v1", "source": "finalRouting",
                 "mapping": {"silver_ready": "active", "revision_required": "inactive",
                             "needs_ai_review": "inactive"}}
LEVEL_POLICY = {"version": "database-difficulty-level-v1", "sourceHead": "intendedDifficulty",
                "mapping": {"Easy": "easy", "Medium": "medium", "Hard": "hard"}}
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


def confidence_policy_for(decisions: list[dict], *, legacy_single_run_null: bool = False) -> dict:
    if any(decision["llmAdvisory"].get("requestedRuns", 3) == 1 for decision in decisions):
        if legacy_single_run_null:
            return {**CONFIDENCE_POLICY, "version": "final-label-run-support-with-single-run-null-v2",
                    "singleRun": "null when a final label exists; one run cannot measure inter-run consistency",
                    "draft": "0 when final labels are not available"}
        return {**CONFIDENCE_POLICY, "version": "mixed-run-agreement-and-model-label-support-v3",
                "singleRun": {
                    "source": "indobert.heads.probabilities[final Gemini label]",
                    "formula": "round(100 * min(final_label_probability_per_head))",
                    "meaning": "IndoBERT support for locked Gemini labels; not inter-run consistency or measured accuracy.",
                    "unavailable": "0 with confidence_available=false when a label or model probability is unavailable"},
                "draft": "0 when final labels or model probabilities are not available"}
    return CONFIDENCE_POLICY


def confidence_details(decision: dict) -> dict:
    advisory = decision["llmAdvisory"]
    if advisory.get("requestedRuns", 3) != 1:
        return {"score": round(100 * min(final_label_support(decision).values())
                               / advisory.get("requestedRuns", 3)),
                "method": "inter_run_support", "available": True}
    heads = decision.get("indobert", {}).get("heads", {})
    probabilities = {}
    for head in CONFIDENCE_POLICY["heads"]:
        label = advisory["advisoryLabels"].get(head)
        distribution = heads.get(head, {}).get("probabilities", {})
        if distribution:
            values = list(distribution.values())
            if (any(isinstance(v, bool) or not isinstance(v, (int, float))
                    or not math.isfinite(v) or not 0 <= v <= 1 for v in values)
                    or not math.isclose(sum(values), 1, abs_tol=1e-5)):
                raise ValueError("invalid model probability distribution")
        probabilities[head] = distribution.get(label) if label is not None else None
    available = all(value is not None for value in probabilities.values())
    return {"score": round(100 * min(probabilities.values())) if available else 0,
            "method": "indobert_final_label_support_min", "available": available,
            "final_label_probabilities": probabilities}


def ai_validation_path(bundle: Path, manifest: dict | None = None) -> Path:
    """Resolve original AI rows when the main array exposes relative bank labels."""
    manifest = manifest or json.loads((bundle / "manifest.json").read_text(encoding="utf-8"))
    operational = manifest.get("databaseExport", {}).get("operationalBalance")
    if not operational:
        return bundle / "validation_results.json"
    reference = operational["aiValidationResults"]
    if reference["path"] != "ai_validation_results.json":
        raise ValueError("unexpected original AI validation path")
    path = bundle / reference["path"]
    if hashlib.sha256(path.read_bytes()).hexdigest() != reference["sha256"]:
        raise ValueError("original AI validation checksum mismatch")
    return path


def final_label_support(decision: dict) -> dict[str, int]:
    advisory = decision["llmAdvisory"]
    requested = advisory.get("requestedRuns", 3)
    if not isinstance(requested, int) or isinstance(requested, bool) or requested < 1:
        raise ValueError("requestedRuns must be a positive integer")
    runs = advisory.get("runs", [])
    indices = [run["runIndex"] for run in runs]
    required_indices = advisory.get("requestedRunIndices", list(range(1, requested + 1)))
    if (len(set(required_indices)) != requested or len(required_indices) != requested
            or len(set(indices)) != len(indices) or any(index not in required_indices for index in indices)):
        raise ValueError("initial run indices must be unique and within requestedRuns")
    return {head: sum(
        run.get("status") == "success"
        and run.get("heads", {}).get(head, {}).get("action") == "classify"
        and advisory["advisoryLabels"].get(head) is not None
        and run.get("heads", {}).get(head, {}).get("label") == advisory["advisoryLabels"][head]
        for run in runs
    ) for head in CONFIDENCE_POLICY["heads"]}


def database_items(originals: list[dict], decisions: list[dict], *, legacy_domain_level: bool = False,
                   legacy_routing_status: bool = False, legacy_single_run_null: bool = False) -> list[dict]:
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
        route = decision["finalRouting"]
        if route not in STATUS_POLICY["mapping"]:
            raise ValueError(f"unknown validation routing: {route}")
        values = {"cognitive_level": (labels["mathCognitiveDomain"] if legacy_domain_level
                                       else LEVEL_POLICY["mapping"].get(difficulty)),
                  "cognitive_score": SCORE_POLICY["mapping"].get(difficulty),
                  "confidence_score": (None if legacy_single_run_null and advisory.get("requestedRuns", 3) == 1 and any(labels.values())
                                       else confidence_details(decision)["score"]),
                  "status": route if legacy_routing_status else STATUS_POLICY["mapping"][route]}
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
        if export["schemaVersion"] not in (DATABASE_SCHEMA, PREVIOUS_DATABASE_SCHEMA, LEGACY_DATABASE_SCHEMA):
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
                  checkpoint: dict, namespace: str, *, legacy_single_run_null: bool = False) -> list[dict]:
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
        if checkpoint.get("requestedRuns", 3) == 1:
            requested = decision["llmAdvisory"].get("requestedRuns", 3)
            items[-1]["ai_metadata"].update(
                requested_runs=requested,
                validation_method="blind_n1" if requested == 1 else "blind_n3_with_ai_adjudication",
                confidence_status=("single_run_unmeasured" if legacy_single_run_null else
                                   "indobert_label_support" if confidence_details(decision)["available"] else
                                   "model_support_unavailable") if requested == 1 else "inter_run_support",
                training_evidence_qualified=bool(requested == 3 and decision["finalRouting"] == "silver_ready"))
            if requested == 1 and not legacy_single_run_null:
                details = confidence_details(decision)
                items[-1]["ai_metadata"].update(
                    confidence_method=details["method"], confidence_available=details["available"],
                    confidence_final_label_probabilities=details["final_label_probabilities"])
    return items
