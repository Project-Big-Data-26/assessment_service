"""Versioned IRT preparation alongside an unchanged database question export.

An intended difficulty label is an initial classification, never an empirical
IRT estimate. Reading local event availability must not create an assessment
database or register a pilot. Calibration remains in the existing screen flow.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from contextlib import closing
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sqlite3
import uuid

from app.assessment.contracts import AssessmentCreate
from app.classification.v2.serializer import canonical_json_hash
from app.silver.exports import LEVEL_POLICY, SCORE_POLICY, STATUS_POLICY, load_decision_bundle, ai_validation_path
from app.training.v2.dataset import DatasetSnapshot
from .analysis import load_policy
from .contracts import AnalysisPolicy


def _local_event_inventory(path: str | Path | None, *, grade: int, track: str,
                           versions: dict[str, str]) -> dict:
    """Read only aggregate availability for matching grade, track and versions.

    Counts are descriptive, not the cleaned matrix readiness decision. Session
    retries, missingness and assumptions are checked by the existing screen CLI.
    No bearer token, subject hash or response answer is returned here.
    """
    result = {"status": "not_configured", "readOnly": True, "matchingAssessments": [],
              "completedSessions": 0, "matchingScoredEvents": 0,
              "matchingScoredEventsByVersion": {}, "calibrationPerformed": False}
    if path is None:
        return result
    source = Path(path).resolve()
    result["path"] = source.as_posix()
    if not source.is_file():
        result["status"] = "database_missing"
        return result
    try:
        with closing(sqlite3.connect(source.as_uri() + "?mode=ro", uri=True)) as db:
            tables = {row[0] for row in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
            required = {"assessments", "sessions", "responses", "snapshots"}
            if not required <= tables:
                result["status"] = "incompatible_database"
                return result
            result["totalCounts"] = {
                name: db.execute(f"SELECT COUNT(*) FROM {name}").fetchone()[0]
                for name in sorted(required)
            }
            assessments = []
            for identifier, encoded in db.execute("SELECT id, document FROM assessments"):
                document = json.loads(encoded)
                if document.get("grade") != grade or document.get("subjectTrack", "regular") != track:
                    continue
                matching = {item["questionVersionId"] for item in document.get("items", [])
                            if versions.get(item["questionVersionId"]) == item.get("contentHash")}
                if matching:
                    assessments.append((identifier, matching))
            event_counts = Counter()
            for identifier, matching in assessments:
                completed = db.execute(
                    "SELECT COUNT(*) FROM sessions WHERE assessment_id=? AND status='completed'", (identifier,)
                ).fetchone()[0]
                counts = Counter()
                query = """SELECT r.document FROM responses r JOIN sessions s ON r.session_id=s.id
                           WHERE s.assessment_id=? AND s.status='completed'"""
                for (encoded,) in db.execute(query, (identifier,)):
                    event = json.loads(encoded)
                    version = event.get("questionVersionId")
                    if (version in matching and event.get("contentHash") == versions[version]
                            and event.get("grade") == grade and event.get("subjectTrack", "regular") == track
                            and event.get("validForAnalysis") is True
                            and event.get("scoringStatus") == "scored"
                            and type(event.get("isCorrect")) is bool
                            and "rapid_guess_candidate" not in event.get("flags", [])):
                        counts[version] += 1
                result["matchingAssessments"].append({"assessmentId": identifier,
                    "matchingItemVersions": len(matching), "completedSessions": completed,
                    "matchingScoredEvents": sum(counts.values())})
                result["completedSessions"] += completed
                event_counts.update(counts)
            result["matchingScoredEventsByVersion"] = dict(sorted(event_counts.items()))
            result["matchingScoredEvents"] = sum(event_counts.values())
            result["status"] = "events_available_for_screening" if event_counts else "no_matching_student_responses"
    except (sqlite3.DatabaseError, ValueError, KeyError, TypeError):
        # Do not leak private row contents through database parsing failures.
        result["status"] = "inventory_failed"
    return result


def build_initialization_report(bundle: str | Path, *, policy: AnalysisPolicy | None = None,
                                db_path: str | Path | None = None, model: str = "rasch") -> dict:
    """Bind initial labels and IRT readiness policy to a verified export bundle.

    This returns a sidecar; it does not modify the bundle or estimate parameters.
    Only active, content-qualified versions are candidates for student delivery.
    """
    if model not in {"rasch", "2pl", "3pl"}:
        raise ValueError("unsupported IRT model")
    policy = policy or load_policy()
    directory = Path(bundle)
    manifest = json.loads((directory / "manifest.json").read_text(encoding="utf-8"))
    validation_path = ai_validation_path(directory, manifest)
    validation_bytes = validation_path.read_bytes()
    rows = json.loads(validation_bytes)
    export = manifest["databaseExport"]
    expected_hash = manifest["outputs"][validation_path.name]["sha256"]
    validation_hash = hashlib.sha256(validation_bytes).hexdigest()
    if validation_hash != expected_hash:
        raise ValueError("validation results checksum mismatch")
    if not isinstance(rows, list):
        raise ValueError("IRT initialization requires the database question array")
    audit = load_decision_bundle(directory)
    decisions = {item["questionId"]: item for item in audit["items"]}
    metadata = export["metadataByQuestionId"]
    identifiers = [str(row["_id"]) for row in rows]
    if len(set(identifiers)) != len(rows) or set(identifiers) != set(decisions) or set(identifiers) != set(metadata):
        raise ValueError("source/decision/metadata coverage must be one-to-one")
    grade, track = export["sourceClass"], export.get("subjectTrack", "regular")
    if grade not in range(1, 13) or track not in {"regular", "tl"} or (track == "tl" and grade not in {11, 12}):
        raise ValueError("invalid grade or subject track")
    items = []
    for row in rows:
        identifier = str(row["_id"])
        decision, reference = decisions[identifier], metadata[identifier]
        difficulty = decision["llmAdvisory"]["advisoryLabels"]["intendedDifficulty"]
        if (row.get("cognitive_level") != LEVEL_POLICY["mapping"].get(difficulty)
                or row.get("cognitive_score") != SCORE_POLICY["mapping"].get(difficulty)
                or row.get("status") != STATUS_POLICY["mapping"][decision["finalRouting"]]
                or reference.get("intended_difficulty") != difficulty
                or reference.get("subject_track", "regular") != track):
            raise ValueError("export labels or initial score disagree with audited decisions")
        active = row.get("status") == "active"
        version, content_hash = reference.get("question_version_id"), reference.get("content_hash")
        if active and (not version or not content_hash):
            raise ValueError("active item requires an immutable version and content hash")
        items.append({"questionId": identifier, "questionVersionId": version, "contentHash": content_hash,
                      "grade": grade, "subjectTrack": track,
                      "rubricVersion": decision["llmAdvisory"]["rubricVersion"],
                      "intendedDifficulty": difficulty, "initialCognitiveScore": row.get("cognitive_score"),
                      "status": row.get("status"), "eligibleForPilot": active,
                      "empiricalDifficulty": None, "irt": None})
    versions = {item["questionVersionId"]: item["contentHash"] for item in items if item["eligibleForPilot"]}
    inventory = _local_event_inventory(db_path, grade=grade, track=track, versions=versions)
    requirements = {"model": model, "minimumPersons": policy.minPersons[model],
                    "minimumItems": policy.minItems[model], "minimumResponsesPerItem": policy.minResponsesPerItem,
                    "minimumCorrectAndIncorrectPerItem": policy.minOutcomeCount,
                    "minimumCoverage": policy.minCoverage, "maximumPersonMissingRate": policy.maxPersonMissingRate,
                    "assumptionReviewRequired": True, "connectedResponseDesignRequired": True}
    counts = {label: sum(item["intendedDifficulty"] == label for item in items)
              for label in ("Easy", "Medium", "Hard")}
    active_counts = {label: sum(item["eligibleForPilot"] and item["intendedDifficulty"] == label for item in items)
                     for label in ("Easy", "Medium", "Hard")}
    failures = []
    if len(versions) < policy.minItems[model]:
        failures.append("insufficient_active_items")
    if not inventory["matchingScoredEvents"]:
        failures.append("no_matching_student_responses")
    failures.append("empirical_matrix_and_assumptions_not_yet_screened")
    result = {"schemaVersion": "irt-initialization-v1", "createdAt": datetime.now(timezone.utc).isoformat(),
              "grade": grade, "subjectTrack": track, "labelProvenance": "ai_silver",
              "researchOnly": True,
              "rubricVersions": sorted({item["rubricVersion"] for item in items}),
              "validationResultsHash": validation_hash,
              "decisionAuditHash": export["decisionAudit"]["sha256"],
              "policyVersion": policy.policyVersion, "policyHash": canonical_json_hash(policy.model_dump(mode="json")),
              "policy": policy.model_dump(mode="json"), "initialScorePolicy": SCORE_POLICY,
              "summary": {"itemCount": len(items), "activeItems": len(versions),
                          "difficultyCounts": counts, "activeDifficultyCounts": active_counts,
                          "undecidedItems": sum(item["intendedDifficulty"] is None for item in items)},
              "requirements": requirements, "localResponseInventory": inventory,
              "readiness": {"passed": False, "failures": failures,
                            "meaning": "Initial preparation only; run screen on each assessment to evaluate empirical readiness."},
              "irt": {"model": model, "status": "analysis_required" if inventory["matchingScoredEvents"] else "waiting_for_data",
                      "calibrated": False, "parameters": None, "studentAbility": None},
              "calibrationUnit": ["assessmentId", "populationId", "assessmentFamily", "grade", "subjectTrack",
                                  "questionVersionId", "contentHash", "timeWindow"],
              "crossGradeOrTrackPooling": False, "affectsValidationResults": False,
              "nextStep": "screen_matching_completed_sessions" if inventory["matchingScoredEvents"] else "prepare_pilot_and_collect_student_responses",
              "items": items}
    result["reportHash"] = canonical_json_hash(result)
    return result


def finalize_irt_sidecar(bundle: str | Path, *, db_path: str | Path | None = None,
                         policy: AnalysisPolicy | None = None, model: str = "rasch") -> dict:
    """Write readiness evidence and its manifest link without editing questions.

    Both a newly produced bundle and an older active bundle can be inspected.
    The sidecar identifies the rubric actually used by that bundle, so a quota
    stop cannot make prior labels appear to have been validated on a new rubric.
    """
    directory = Path(bundle)
    report = build_initialization_report(directory, db_path=db_path, policy=policy, model=model)
    relative = "bukti_validasi/irt_initialization.json"
    destination = directory / relative
    manifest_path = directory / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    encoded = (json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode("utf-8")
    reference = {"path": relative, "sha256": hashlib.sha256(encoded).hexdigest(),
                 "schemaVersion": report["schemaVersion"], "reportHash": report["reportHash"],
                 "status": report["irt"]["status"], "empiricalCalibrationPerformed": False}
    manifest.setdefault("outputs", {})[relative] = {"sha256": reference["sha256"], "bytes": len(encoded)}
    manifest["irtInitialization"] = reference
    manifest_bytes = (json.dumps(manifest, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode("utf-8")
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary_report = destination.with_name(f".{destination.name}.{uuid.uuid4().hex}.tmp")
    temporary_manifest = manifest_path.with_name(f".{manifest_path.name}.{uuid.uuid4().hex}.tmp")
    try:
        temporary_report.write_bytes(encoded)
        temporary_manifest.write_bytes(manifest_bytes)
        temporary_report.replace(destination)
        temporary_manifest.replace(manifest_path)
    finally:
        temporary_report.unlink(missing_ok=True)
        temporary_manifest.unlink(missing_ok=True)
    return report


def prepare_pilot_configs(snapshot: DatasetSnapshot, *, run_id: str) -> dict:
    """Prepare separate grade/track blueprints without registering or delivering.

    Default population IDs name future pilot cohorts. They are not claims that
    respondents exist. The caller can edit cohort IDs before registering them.
    """
    from app.assessment.store import AssessmentStore

    AssessmentStore.validate_snapshot(snapshot)
    if not run_id or len(run_id) > 40 or not all(character.isalnum() or character in "-_" for character in run_id):
        raise ValueError("run_id must contain 1-40 letters, digits, hyphens or underscores")
    groups = defaultdict(list)
    excluded = Counter()
    for row in [*snapshot.rows, *snapshot.expansionRows]:
        if row.questionType != "multiple_choice":
            excluded["unsupported_question_type"] += 1
            continue
        groups[(row.grade, row.subjectTrack)].append(row)
    assessments = []
    for (grade, track), rows in sorted(groups.items()):
        # One form cannot repeat a question or exceed the API's 200-item bound.
        if len({row.questionId for row in rows}) != len(rows):
            raise ValueError("pilot group contains different versions of the same question")
        for index in range(0, len(rows), 200):
            chunk = rows[index:index + 200]
            identifier = f"pretest-g{grade}-{track}-{run_id}-f{index // 200 + 1}"
            config = AssessmentCreate(assessmentId=identifier, snapshotId=snapshot.snapshotId,
                questionVersionIds=[row.questionVersionId for row in chunk],
                populationId=f"pilot-g{grade}-{track}-{run_id}", assessmentFamily=f"math-pretest-g{grade}-{track}",
                grade=grade, subjectTrack=track)
            assessments.append({"assessmentConfig": config.model_dump(mode="json"), "itemCount": len(chunk),
                "difficultyCounts": {label: sum(row.intendedDifficulty.value == label for row in chunk)
                                     for label in ("Easy", "Medium", "Hard")}})
    result = {"schemaVersion": "irt-pilot-preparation-v1", "runId": run_id,
              "snapshotId": snapshot.snapshotId, "snapshotHash": snapshot.snapshotHash,
              "status": "configured_not_registered", "studentResponsesCreated": 0,
              "crossGradeOrTrackPooling": False, "assessments": assessments, "exclusions": dict(excluded),
              "populationIdMeaning": "Planned cohort identifier; replace before registration when a real cohort is identified."}
    result["reportHash"] = canonical_json_hash(result)
    return result
