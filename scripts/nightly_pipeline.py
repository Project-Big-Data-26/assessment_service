"""Daily extraction handoff -> blind N=1 -> balanced bank -> empirical screening.

`ready` is the extraction completion handshake. `run --execute` resumes paid
validation; successful calls are reused by validate_exercise_batch. Only
completed bundles are balanced. Student responses never come from the LLM.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager, closing
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from dotenv import load_dotenv
from app.llm.config import GeminiSettings
from app.llm.silver import silver_rubric
from app.assessment.store import AssessmentError, AssessmentStore
from app.psychometrics.analysis import load_policy
from app.psychometrics.contracts import ScreeningInput
from app.psychometrics.initialization import build_initialization_report
from scripts import validate_exercise_batch as exercise
from scripts.balance_operational_difficulty import export_verified_operational_balance, verify_operational_export
from scripts.generate_silver_labels_kelas1 import atomic_write
from scripts.publish_operational_bank import publish
from scripts.refresh_ai_validation_reports import digest, load, verify_bundle


def timestamp():
    return datetime.now(timezone.utc).isoformat()


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def local_path(value):
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


@contextmanager
def run_lock(path):
    """OS releases the lock even after a crash; the file is not a stale PID gate."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a+b") as handle:
        handle.seek(0)
        if os.fstat(handle.fileno()).st_size == 0:
            handle.write(b"0")
            handle.flush()
        handle.seek(0)
        if os.name == "nt":
            import msvcrt
            try:
                msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
            except OSError:
                raise RuntimeError("another nightly pipeline is running") from None
            try:
                yield
            finally:
                handle.seek(0)
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
        else:
            import fcntl
            try:
                fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError:
                raise RuntimeError("another nightly pipeline is running") from None
            try:
                yield
            finally:
                fcntl.flock(handle, fcntl.LOCK_UN)


def read_config(path):
    config = load(path)
    if config.get("schemaVersion") != "nightly-exercise-v1":
        raise ValueError("unsupported nightly config")
    if config.get("timezone") != "Asia/Jakarta" or config.get("schedule") != "01:00":
        raise ValueError("this scheduler uses 01:00 Asia/Jakarta")
    if not config.get("classes") or not set(config["classes"]) <= set(exercise.CLASSES):
        raise ValueError("unsupported exercise class")
    if type(config.get("maxApiCalls")) is not int or config["maxApiCalls"] < 1:
        raise ValueError("maxApiCalls must be a positive integer")
    if type(config.get("maxOutputTokens")) is not int or not 128 <= config["maxOutputTokens"] <= 4096:
        raise ValueError("maxOutputTokens must be 128..4096")
    if config.get("irtModel") not in ("rasch", "2pl", "3pl"):
        raise ValueError("unsupported IRT model")
    return config


def source_identity(name, batch):
    p = exercise.paths(name, batch)
    return {"class": name, "batch": batch,
            "sourceSha256": digest(p["exercise"] / "soal_exercise_db.json"),
            "metadataSha256": digest(p["exercise"] / "soal_exercise_meta.json")}


def mark_ready(name, batch):
    # Validate the complete handoff, not just the existence of its JSON files.
    exercise.stage_class(name, batch)
    document = {"schemaVersion": "extraction-ready-v1", "completedAt": timestamp(),
                **source_identity(name, batch)}
    atomic_write(document, exercise.paths(name, batch)["exercise"] / "extraction_ready.json")
    return document


def discover_jobs(config):
    jobs, problems = {}, []
    for entry in config.get("bootstrapJobs", []):
        if entry["class"] not in config["classes"]:
            raise ValueError("bootstrap class must be enabled")
        try:
            identity = source_identity(entry["class"], entry["batch"])
            jobs[(identity["class"], identity["batch"])] = identity
        except (ValueError, OSError) as exc:
            problems.append({"class": entry["class"], "batch": entry["batch"], "error": type(exc).__name__})
    for name in config["classes"]:
        for marker in sorted((ROOT / "output/exercise" / name).glob("batch*/extraction_ready.json")):
            try:
                ready = load(marker)
                identity = source_identity(name, marker.parent.name)
                if ready.get("schemaVersion") != "extraction-ready-v1" or any(
                        ready.get(key) != value for key, value in identity.items()):
                    raise ValueError("extraction marker hashes or identity differ")
                completed = datetime.fromisoformat(ready["completedAt"])
                if completed.utcoffset() is None:
                    raise ValueError("completedAt must include a timezone")
                jobs[(name, marker.parent.name)] = identity
            except (ValueError, KeyError, OSError, TypeError) as exc:
                # A bad marker blocks its job, including a configured bootstrap.
                jobs.pop((name, marker.parent.name), None)
                problems.append({"marker": str(marker.relative_to(ROOT)), "error": type(exc).__name__})
    return list(jobs.values()), problems


def verify_completed(p):
    verify_bundle(p["source"], p["final"])
    if not load(p["final"] / "export_status.json").get("fullComplete"):
        raise ValueError("validation is incomplete; balanced publication is deferred")


def publish_balance(name, batch):
    p = exercise.paths(name, batch)
    verify_completed(p)
    grade, track = exercise.CLASSES[name]
    version = export_verified_operational_balance(p["source"], p["final"], grade=grade, track=track)
    publish(p["source"], p["final"], version, grade=grade, track=track)
    # Metadata and the main DB export must expose the same operational labels.
    meta_path = p["final"] / "validation_results_meta.json"
    meta = load(meta_path)
    for row in load(p["final"] / "validation_results.json"):
        result = meta[str(row["_id"])]["validasi"]
        result.setdefault("ai_cognitive_level", result["cognitive_level"])
        result.setdefault("ai_confidence_score", result["confidence_score"])
        result.update({key: row[key] for key in ("cognitive_level", "cognitive_score", "confidence_score", "status")})
        result["difficulty_provenance"] = "relative_bank_quota" if row["status"] == "active" else "ai_silver"
        result["level_sesuai_target"] = (None if row["cognitive_level"] is None else
                                        row["cognitive_level"] == meta[str(row["_id"])]["level_target"])
    atomic_write(meta, meta_path)
    manifest = load(p["final"] / "manifest.json")
    manifest["outputs"][meta_path.name] = {"sha256": digest(meta_path), "bytes": meta_path.stat().st_size}
    atomic_write(manifest, p["final"] / "manifest.json")
    # Public handoff lives with the original batch, even though evidence is staged.
    atomic_write(version, p["exercise"] / "operational_balance.json")
    verify_completed(p)
    return version


def job_identity(job, config):
    grade, track = exercise.CLASSES[job["class"]]
    rubric = silver_rubric(grade, track=track)
    return fingerprint({**job, "model": GeminiSettings.from_environment().model, "runs": 1,
                        "rubricHash": digest(rubric.path), "promptVersion": rubric.prompt_version,
                        "maxOutputTokens": config["maxOutputTokens"]})


def validate_job(job, config, state, budget, directory):
    name, batch = job["class"], job["batch"]
    key = f"{name}/{batch}"
    p = exercise.paths(name, batch)
    identity = job_identity(job, config)
    previous = state.get(key, {})
    if previous.get("identity") == identity and previous.get("status") == "completed":
        verify_completed(p)
        verify_operational_export(Path(previous["operational"]["directory"]))
        return {**previous, "reused": True}, budget
    if budget <= 0:
        return {"status": "waiting_for_budget", "identity": identity}, budget
    before = load(p["checkpoint"]).get("apiAttempts", 0) if p["checkpoint"].exists() else 0
    with (directory / f"{name}_{batch}.log").open("a", encoding="utf-8") as log:
        process = subprocess.run([sys.executable, "-X", "utf8", str(ROOT / "scripts/validate_exercise_batch.py"),
            "run", "--classes", name, "--batch", batch, "--runs", "1", "--max-api-calls", str(budget),
            "--max-output-tokens", str(config["maxOutputTokens"]), "--execute"], cwd=ROOT,
            stdout=log, stderr=subprocess.STDOUT)
    after = load(p["checkpoint"]).get("apiAttempts", 0) if p["checkpoint"].exists() else before
    budget -= max(0, after - before)
    if source_identity(name, batch) != job:
        raise ValueError("source changed during validation; publish a new batch")
    result = {"identity": identity, "updatedAt": timestamp(), "exitCode": process.returncode,
              "apiCallsThisRun": max(0, after - before), "status": "validation_incomplete"}
    if process.returncode == 0:
        result.update(status="completed", operational=publish_balance(name, batch))
    return result, budget


def effective_labels(analysis, decisions):
    """Version/population-scoped view; never rewrites initial silver labels."""
    actions = {d["questionVersionId"]: d["action"] for d in decisions}
    rows = []
    for item in analysis["items"]:
        usable = (analysis["dataOrigin"] == "server_scored" and analysis["readiness"]["passed"]
                  and analysis["irt"]["status"] == "estimated"
                  and item.get("irt") is not None and item["recommendedRouting"] == "observation_only"
                  and actions.get(item["questionVersionId"]) == "retain")
        empirical = item["irt"]["empiricalDifficulty"] if usable else None
        rows.append({"questionId": item["questionId"], "questionVersionId": item["questionVersionId"],
                     "contentHash": item["contentHash"], "intendedDifficulty": item["intendedDifficulty"],
                     "empiricalDifficulty": empirical,
                     "effectiveDifficulty": empirical or item["intendedDifficulty"],
                     "difficultySource": "irt" if usable else "intended",
                     "reviewFlags": item["reviewFlags"], "action": actions.get(item["questionVersionId"]),
                     "deliveryAllowed": actions.get(item["questionVersionId"]) in ("retain", "collect_more_events")})
    return {"schemaVersion": "effective-difficulty-v1", "assessmentId": analysis["assessmentId"],
            "populationId": analysis["populationId"], "assessmentFamily": analysis["assessmentFamily"],
            "grade": analysis["grade"], "snapshotId": analysis["snapshotId"],
            "snapshotHash": analysis["snapshotHash"], "policyHash": analysis["policyHash"],
            "irtStatus": analysis["irt"]["status"], "researchOnly": True, "items": rows}


def screen_assessments(config, output):
    db_path = local_path(os.getenv("ASSESSMENT_DB_PATH", "data/local/assessments.sqlite3"))
    if not db_path.is_file():
        return {"status": "waiting_for_data", "reason": "database_missing", "assessments": []}
    scopes = {exercise.CLASSES[name] for name in config["classes"]}
    with closing(sqlite3.connect(db_path.resolve().as_uri() + "?mode=ro", uri=True)) as db:
        assessments = [json.loads(row[0]) for row in db.execute("SELECT document FROM assessments")]
    selected = [a for a in assessments if (a["grade"], a.get("subjectTrack", "regular")) in scopes]
    if not selected:
        return {"status": "waiting_for_data", "reason": "no_matching_assessments", "assessments": []}
    requests = {}
    for path in config.get("screeningRequests", []):
        request = ScreeningInput.model_validate(load(local_path(path)))
        if request.assessmentId in requests:
            raise ValueError("duplicate screening request for assessment")
        requests[request.assessmentId] = request
    store = AssessmentStore(db_path, subject_secret=os.getenv("ASSESSMENT_SUBJECT_SECRET") or None)
    results = []
    for assessment in selected:
        identifier = assessment["assessmentId"]
        request = requests.get(identifier) or ScreeningInput(assessmentId=identifier, model=config["irtModel"])
        try:
            analysis = store.screen(request, load_policy())
            labels = effective_labels(analysis, store.decisions(analysis["snapshotId"]))
            # No person estimates or response events are exported to the handoff.
            destination = output / "empirical" / fingerprint(identifier)[:24]
            destination.mkdir(parents=True, exist_ok=True)
            version = destination / f"{analysis['snapshotId']}.json"
            if version.exists() and load(version) != labels:
                raise ValueError("immutable empirical label artifact differs")
            if not version.exists():
                atomic_write(labels, version)
            atomic_write(labels, destination / "current.json")
            results.append({"assessmentId": identifier, "status": analysis["irt"]["status"],
                            "snapshotId": analysis["snapshotId"], "labels": str(destination / "current.json"),
                            "updatedLabels": sum(i["difficultySource"] == "irt" for i in labels["items"])})
        except AssessmentError as exc:
            results.append({"assessmentId": identifier, "status": "waiting_for_data" if exc.status_code == 409 else "failed",
                            "errorType": type(exc).__name__, "httpStatus": exc.status_code})
        except Exception as exc:
            results.append({"assessmentId": identifier, "status": "failed", "errorType": type(exc).__name__})
    return {"status": "screened", "assessments": results}


def run(config, output):
    output.mkdir(parents=True, exist_ok=True)
    with run_lock(output / "pipeline.lock"):
        jobs, problems = discover_jobs(config)
        run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        directory = output / "history" / run_id
        directory.mkdir(parents=True)
        state_path = output / "state.json"
        state = load(state_path) if state_path.exists() else {"jobs": {}}
        report = {"schemaVersion": "nightly-report-v1", "startedAt": timestamp(), "timezone": "Asia/Jakarta",
                  "provider": "gemini", "requestedRuns": 1, "jobs": {}, "handoffErrors": problems}
        budget = config["maxApiCalls"]
        for job in jobs:
            key = f"{job['class']}/{job['batch']}"
            checkpoint = exercise.paths(job['class'], job['batch'])["checkpoint"]
            before = load(checkpoint).get("apiAttempts", 0) if checkpoint.exists() else 0
            budget_before = budget
            try:
                result, budget = validate_job(job, config, state["jobs"], budget, directory)
                if result["status"] == "completed":
                    p = exercise.paths(job["class"], job["batch"])
                    initialization = build_initialization_report(p["final"],
                        db_path=local_path(os.getenv("ASSESSMENT_DB_PATH", "data/local/assessments.sqlite3")),
                        model=config["irtModel"])
                    atomic_write(initialization, directory / f"{job['class']}_{job['batch']}_irt.json")
            except Exception as exc:
                after = load(checkpoint).get("apiAttempts", 0) if checkpoint.exists() else before
                budget = budget_before - max(0, after - before)
                result = {"status": "failed", "errorType": type(exc).__name__}
                # Technical traceback remains local; reports do not echo private rows/keys.
                import traceback
                with (directory / f"{job['class']}_{job['batch']}_error.log").open("w", encoding="utf-8") as log:
                    traceback.print_exc(file=log)
            state["jobs"][key] = result
            report["jobs"][key] = result
            atomic_write(state, state_path)
        # Response-based analysis runs even when extraction/LLM validation is blocked.
        try:
            report["psychometrics"] = screen_assessments(config, output)
        except Exception as exc:
            report["psychometrics"] = {"status": "failed", "errorType": type(exc).__name__}
        report.update(finishedAt=timestamp(), remainingApiCalls=budget)
        report["success"] = (not problems and all(j["status"] == "completed" for j in report["jobs"].values())
                             and report["psychometrics"]["status"] != "failed"
                             and all(a["status"] != "failed" for a in report["psychometrics"].get("assessments", [])))
        atomic_write(report, directory / "report.json")
        atomic_write(report, output / "latest.json")
        return report


def main():
    load_dotenv(ROOT / ".env", override=False)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("run", "status", "ready", "balance"))
    parser.add_argument("--config", default="configs/nightly_pipeline.json")
    parser.add_argument("--output", default="runs/nightly_pipeline")
    parser.add_argument("--class", dest="name", choices=exercise.CLASSES)
    parser.add_argument("--batch", default="batch01")
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()
    if args.command in ("ready", "balance"):
        if not args.name:
            parser.error("ready/balance require --class")
        result = mark_ready(args.name, args.batch) if args.command == "ready" else publish_balance(args.name, args.batch)
    else:
        config = read_config(local_path(args.config))
        if args.command == "run":
            if not args.execute:
                parser.error("run makes live Gemini calls and requires --execute")
            result = run(config, local_path(args.output))
        else:
            jobs, problems = discover_jobs(config)
            for job in jobs:
                p = exercise.paths(job["class"], job["batch"])
                if p["checkpoint"].exists():
                    checkpoint = load(p["checkpoint"])
                    ids = [str(item["_id"]) for item in load(p["exercise"] / "soal_exercise_db.json")["items"]]
                    job["validation"] = {"total": len(ids),
                        "complete": sum(exercise.complete(checkpoint, [qid]) for qid in ids),
                        "requestedRuns": checkpoint.get("requestedRuns", 3),
                        "executionStatus": checkpoint.get("executionStatus"),
                        "apiAttempts": checkpoint.get("apiAttempts", 0)}
            result = {"jobs": jobs, "handoffErrors": problems, "schedule": "01:00 Asia/Jakarta",
                      "latestReport": str(local_path(args.output) / "latest.json")}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("success", True) else 1


if __name__ == "__main__":
    raise SystemExit(main())
