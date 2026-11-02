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
import re
import sqlite3
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from dotenv import load_dotenv
from app.llm.config import GeminiSettings
from app.llm.providers import PROVIDERS, settings_for, has_credentials, key_slots
from app.llm.credentials import use_credential_slot
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
    if config.get("provider", "gemini") not in PROVIDERS:
        raise ValueError("unsupported validation provider")
    fallbacks = config.get("fallbackProviders", [])
    if (not isinstance(fallbacks, list) or any(p not in ("gemini", "groq") for p in fallbacks)
            or len(set([config.get("provider", "gemini"), *fallbacks])) != len(fallbacks) + 1):
        raise ValueError("fallbackProviders must contain unique Gemini/Groq providers excluding the primary")
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
    delays = config.get("providerRetryDelaysSeconds", [15, 30, 60])
    if (not isinstance(delays, list) or len(delays) > 5
            or any(type(delay) is not int or not 1 <= delay <= 60 for delay in delays)):
        raise ValueError("providerRetryDelaysSeconds must contain at most five integer delays of 1..60 seconds")
    if type(config.get("stopOn503", False)) is not bool:
        raise ValueError("stopOn503 must be boolean")
    if type(config.get("fallbackOn503", False)) is not bool:
        raise ValueError("fallbackOn503 must be boolean")
    if config.get("fallbackOn503") and not fallbacks:
        raise ValueError("fallbackOn503 requires fallbackProviders")
    training = config.get("empiricalFineTuning", {})
    if (not isinstance(training, dict) or type(training.get("enabled", False)) is not bool
            or type(training.get("epochs", 3)) is not int or not 1 <= training.get("epochs", 3) <= 12
            or type(training.get("timeoutSeconds", 21600)) is not int
            or not 60 <= training.get("timeoutSeconds", 21600) <= 43200):
        raise ValueError("invalid empiricalFineTuning configuration")
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


def waiting_classes(config, jobs):
    """Distinguish absent exercise data from classes ready for paid validation."""
    discovered = {job["class"] for job in jobs}
    pending = []
    for name in config["classes"]:
        if name in discovered:
            continue
        directory = ROOT / "output/exercise" / name
        paired = any(source.with_name("soal_exercise_meta.json").is_file()
                     for source in directory.glob("batch*/soal_exercise_db.json"))
        pending.append({"class": name, "status": "waiting_for_ready" if paired else "waiting_for_source",
                        "directory": str(directory),
                        "requiredFiles": ["soal_exercise_db.json", "soal_exercise_meta.json", "extraction_ready.json"]})
    return pending


def provider_stop_notice(checkpoint):
    status = checkpoint.get("executionStatus", "")
    if not status.startswith("blocked_provider"):
        return None
    raw_code = str((checkpoint.get("stopReason") or {}).get("errorCode") or "")
    code = raw_code if re.fullmatch(r"[A-Za-z][A-Za-z0-9_.]*:\d{3}", raw_code) else "provider_error"
    label = {"deepseek": "DeepSeek", "groq": "Groq"}.get(checkpoint.get("provider"), "Gemini")
    if status == "blocked_provider_http_503":
        message = "Validasi berhenti pada HTTP 503 Gemini. Hasil sukses dan checkpoint tersimpan."
    elif status == "blocked_provider_daily_quota":
        message = "Validasi berhenti karena kuota harian Gemini habis. Hasil sukses dan checkpoint tersimpan."
    elif status == "blocked_provider_quota_or_rate_limit":
        message = "Validasi berhenti karena batas kuota/rate limit Gemini. Hasil sukses dan checkpoint tersimpan."
    else:
        message = "Validasi berhenti karena konfigurasi/koneksi layanan Gemini. Hasil sukses dan checkpoint tersimpan."
    if (checkpoint.get("stopReason") or {}).get("providerFailureReason") == "insufficient_balance":
        message = f"Validasi berhenti karena saldo/kredit API {label} tidak cukup. Checkpoint tersimpan."
    return {"status": status, "errorCode": code, "message": message.replace("Gemini", label)}


def verify_completed(p):
    verify_bundle(p["source"], p["final"])
    if not load(p["final"] / "export_status.json").get("fullComplete"):
        raise ValueError("validation is incomplete; balanced publication is deferred")


def publish_balance(name, batch):
    p = exercise.paths(name, batch)
    verify_completed(p)
    grade, track = exercise.CLASSES[name]
    meta = load(p["exercise"] / "soal_exercise_meta.json")
    allocation_policy = {"version": "chapter-relative-30-40-30-v1", "groupBy": "bab_id",
                         "weights": {"easy": 3, "medium": 4, "hard": 3},
                         "groupsByQuestionId": {qid: info.get("bab_id") for qid, info in meta.items()}}
    version = export_verified_operational_balance(p["source"], p["final"], grade=grade, track=track,
                                                 allocation_policy=allocation_policy)
    publish(p["source"], p["final"], version, grade=grade, track=track)
    # Metadata and the main DB export must expose the same operational labels.
    meta_path = p["final"] / "validation_results_meta.json"
    meta = load(meta_path)
    audit = load(p["final"] / "bukti_validasi/operational_balance_audit.json")
    evidence = {str(item["questionId"]): item for item in audit["items"]}
    for row in load(p["final"] / "validation_results.json"):
        result = meta[str(row["_id"])]["validasi"]
        result.setdefault("ai_cognitive_level", result["cognitive_level"])
        result.setdefault("ai_confidence_score", result["confidence_score"])
        result.update({key: row[key] for key in ("cognitive_level", "cognitive_score", "confidence_score", "status")})
        result["difficulty_provenance"] = "relative_bank_quota" if row["status"] == "active" else "ai_silver"
        result["level_sesuai_target"] = (None if row["cognitive_level"] is None else
                                        row["cognitive_level"] == meta[str(row["_id"])]["level_target"])
        detail = evidence.get(str(row["_id"]), {})
        if "confidenceMethod" in detail:
            result.setdefault("ai_confidence_final_label_probabilities", result.get("confidence_final_label_probabilities"))
            result.update(confidence_method=detail["confidenceMethod"],
                          confidence_available=detail["confidenceAvailable"],
                          confidence_final_label_probabilities=detail["finalLabelProbabilities"],
                          confidence_status="indobert_label_support" if detail["confidenceAvailable"] else "model_support_unavailable")
    atomic_write(meta, meta_path)
    manifest = load(p["final"] / "manifest.json")
    manifest["outputs"][meta_path.name] = {"sha256": digest(meta_path), "bytes": meta_path.stat().st_size}
    summary_path = p["final"] / "RINGKASAN_VALIDASI.md"
    marker = "\n<!-- operational-chapter-balance -->"
    summary = summary_path.read_text(encoding="utf-8").split(marker)[0]
    lines = [marker, "", "## Distribusi operasional per bab", "",
             "Array utama memakai sekitar 30% easy, 40% medium, 30% hard per bab, diranking dari profil bukti. "
             "Label AI asli tetap ada di `ai_validation_results.json`. Soal inactive tidak masuk kuota. "
             "Confidence N=1 memakai dukungan IndoBERT untuk label operasional (0 jika tidak tersedia), bukan konsistensi satu run.", "",
             "| Bab | Active | Easy | Medium | Hard |", "|---|---:|---:|---:|---:|"]
    for chapter, group in audit["groups"].items():
        targets = group["targets"]
        lines.append(f"| {chapter} | {group['activeQuestionCount']} | {targets['easy']} | {targets['medium']} | {targets['hard']} |")
    summary_path.write_text(summary + "\n".join(lines) + "\n", encoding="utf-8")
    manifest["outputs"][summary_path.name] = {"sha256": digest(summary_path), "bytes": summary_path.stat().st_size}
    atomic_write(manifest, p["final"] / "manifest.json")
    # Public handoff lives with the original batch, even though evidence is staged.
    atomic_write(version, p["exercise"] / "operational_balance.json")
    verify_completed(p)
    return version


def job_identity(job, config):
    grade, track = exercise.CLASSES[job["class"]]
    rubric = silver_rubric(grade, track=track)
    settings = settings_for(config.get("provider", "gemini"))
    return fingerprint({**job, **({"provider": settings.provider} if settings.provider != "gemini" else {}),
                        "model": settings.model, "runs": 1,
                        "balancePolicy": "chapter-relative-30-40-30-v1",
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
    # A policy-only publication change does not need any more paid calls.
    if p["checkpoint"].exists():
        checkpoint = load(p["checkpoint"])
        ids = [str(item["_id"]) for item in load(p["source"])]
        if exercise.complete(checkpoint, ids):
            exercise.package(name, batch)
            return {"identity": identity, "updatedAt": timestamp(), "exitCode": 0,
                    "apiCallsThisRun": 0, "status": "completed",
                    "operational": publish_balance(name, batch)}, budget
    if budget <= 0:
        return {"status": "waiting_for_budget", "identity": identity}, budget
    provider = config.get("provider", "gemini")
    if provider in ("deepseek", "groq"):
        settings = settings_for(provider)
        if not settings.api_key.strip():
            return {"status": "waiting_for_credentials", "identity": identity, "provider": provider,
                    "reason": f"{provider.upper()}_API_KEY is missing", "apiCallsThisRun": 0}, budget
        if not settings.live_enabled:
            return {"status": "waiting_for_provider_enablement", "identity": identity, "provider": provider,
                    "reason": f"Set {provider.upper()}_LIVE_ENABLED=true after reviewing account limits and billing", "apiCallsThisRun": 0}, budget
    before = load(p["checkpoint"]).get("apiAttempts", 0) if p["checkpoint"].exists() else 0
    with (directory / f"{name}_{batch}.log").open("a", encoding="utf-8") as log:
        process = subprocess.run([sys.executable, "-X", "utf8", str(ROOT / "scripts/validate_exercise_batch.py"),
            "run", "--classes", name, "--batch", batch, "--runs", "1", "--max-api-calls", str(budget),
            "--max-output-tokens", str(config["maxOutputTokens"]), "--execute",
            "--provider", provider,
            *(["--checkpoint-namespace", exercise.VALIDATION_NAMESPACE] if exercise.VALIDATION_NAMESPACE else []),
            *(["--stop-on-503"] if config.get("stopOn503", False) else [])], cwd=ROOT,
            stdout=log, stderr=subprocess.STDOUT)
    after = load(p["checkpoint"]).get("apiAttempts", 0) if p["checkpoint"].exists() else before
    budget -= max(0, after - before)
    if source_identity(name, batch) != job:
        raise ValueError("source changed during validation; publish a new batch")
    result = {"identity": identity, "updatedAt": timestamp(), "exitCode": process.returncode,
              "apiCallsThisRun": max(0, after - before), "status": "validation_incomplete"}
    if p["checkpoint"].exists():
        checkpoint = load(p["checkpoint"])
        notice = provider_stop_notice(checkpoint)
        if notice:
            result["providerStop"] = notice
    if process.returncode == 0:
        result.update(status="completed", operational=publish_balance(name, batch))
    return result, budget


def validate_with_provider_retries(job, config, state, budget, directory, *, on_retry=None):
    """Resume transient provider failures; quota/auth stops never enter this loop."""
    delays = config.get("providerRetryDelaysSeconds", [15, 30, 60])
    initial_budget, retries = budget, []
    for attempt in range(len(delays) + 1):
        result, budget = validate_job(job, config, state, budget, directory)
        result = {**result, "apiCallsThisRun": initial_budget - budget}
        if retries:
            result["transientRetries"] = list(retries)
        if config.get("stopOn503", False) and result.get("providerStop", {}).get("errorCode", "").endswith(":503"):
            return result, budget
        temporary = (result.get("exitCode") == 3 and
                     result.get("providerStop", {}).get("status") == "blocked_provider_temporarily_unavailable"
                     and not result["providerStop"]["errorCode"].endswith(":429"))
        if not temporary or budget <= 0 or attempt == len(delays):
            return result, budget
        retry = {"retryIndex": attempt + 1, "delaySeconds": delays[attempt],
                 "errorCode": result["providerStop"]["errorCode"], "scheduledAt": timestamp()}
        retries.append(retry)
        if on_retry is not None:
            on_retry({**result, "status": "retrying_provider", "transientRetries": list(retries),
                      "retryInSeconds": delays[attempt]})
        time.sleep(delays[attempt])
    raise AssertionError("unreachable retry loop")


def uses_key_failover(config):
    return bool(config.get("fallbackProviders")) or len(key_slots(config.get("provider", "gemini"))) > 1


def validate_with_provider_failover(job, config, state, budget, directory, *, on_retry=None):
    """Switch on quota or configured service errors; retry only temporarily unavailable providers."""
    from scripts.provider_failover import activate_checkpoint, select_provider, ProviderFailoverError
    if budget <= 0:
        return {"status": "waiting_for_budget", "apiCallsThisRun": 0}, budget
    initial_budget, attempts = budget, []
    order = [config.get("provider", "gemini"), *config.get("fallbackProviders", [])]
    delays = config.get("providerRetryDelaysSeconds", [15, 30, 60]) if config.get("fallbackOn503") else []
    result = None
    candidates = [(provider, slot) for provider in order for slot in (key_slots(provider) or [1])]
    round_index, no_progress_rounds = 0, 0
    while candidates:
        temporary_providers = []
        made_progress = False
        for provider, key_slot in candidates:
            with use_credential_slot(provider, key_slot):
                select_provider(provider)
                if not has_credentials(provider):
                    attempts.append({"provider": provider, "keySlot": key_slot, "status": "skipped_not_enabled", "apiCalls": 0})
                    continue
                try:
                    settings = settings_for(provider)
                except Exception as exc:
                    raise ProviderFailoverError(budget) from exc
                if not settings.api_key.strip() or not settings.live_enabled:
                    attempts.append({"provider": provider, "keySlot": key_slot, "status": "skipped_not_enabled", "apiCalls": 0})
                    continue
                if budget <= 0:
                    break
                try:
                    activate_checkpoint(job["class"], job["batch"], provider)
                except Exception as exc:
                    raise ProviderFailoverError(budget) from exc
                current = {**config, "provider": provider}
                before = budget
                checkpoint = exercise.paths(job["class"], job["batch"])["checkpoint"]
                previous_state = load(checkpoint) if checkpoint.exists() else {}
                previous_calls = previous_state.get("apiAttempts", 0)
                previous_complete = sum(exercise.complete(previous_state, [qid]) for qid in previous_state.get("items", {}))
                if on_retry is not None:
                    on_retry({"status": "running", "activeProvider": provider, "activeKeySlot": key_slot, "providerAttempts": list(attempts),
                              "apiCallsThisRun": initial_budget - budget})
                try:
                    result, budget = validate_with_provider_retries(job, current, state, budget, directory, on_retry=on_retry)
                except Exception as exc:
                    current_calls = load(checkpoint).get("apiAttempts", 0) if checkpoint.exists() else previous_calls
                    raise ProviderFailoverError(budget - max(0, current_calls - previous_calls)) from exc
                current_state = load(checkpoint) if checkpoint.exists() else {}
                current_complete = sum(exercise.complete(current_state, [qid]) for qid in current_state.get("items", {}))
                made_progress = made_progress or current_complete > previous_complete
                attempts.append({"provider": provider, "keySlot": key_slot, "status": result["status"], "round": round_index + 1,
                                 "apiCalls": before - budget, "providerStop": result.get("providerStop")})
                result.update(activeProvider=provider, activeKeySlot=key_slot, providerAttempts=list(attempts), apiCallsThisRun=initial_budget - budget)
                if result.get("status") == "completed":
                    return result, budget
                stop = result.get("providerStop", {})
                quota = (result.get("exitCode") == 3 and
                         (stop.get("errorCode", "").endswith(":429") or stop.get("status") == "blocked_provider_daily_quota"))
                temporary = bool(config.get("fallbackOn503") and result.get("exitCode") == 3 and
                                 (stop.get("errorCode", "").endswith(":503") or
                                  stop.get("status") == "blocked_provider_temporarily_unavailable"))
                if not (quota or temporary) or budget <= 0:
                    return result, budget
                if temporary:
                    temporary_providers.append((provider, key_slot))
                if on_retry is not None:
                    on_retry({**result, "status": "switching_provider_after_service_error" if temporary else "switching_provider_after_quota"})
        if not temporary_providers or not delays or budget <= 0:
            break
        # Backoff limits consecutive rounds with no completed questions. A recovered
        # service that still adds valid results should continue working toward completion.
        no_progress_rounds = 0 if made_progress else no_progress_rounds + 1
        if no_progress_rounds > len(delays):
            break
        delay = delays[max(0, no_progress_rounds - 1)]
        if on_retry is not None:
            on_retry({**(result or {}), "status": "waiting_for_provider_recovery", "retryInSeconds": delay,
                      "retryProviders": list(dict.fromkeys(p for p, _ in temporary_providers)),
                      "retryKeySlots": [{"provider": p, "keySlot": slot} for p, slot in temporary_providers], "providerAttempts": list(attempts)})
        time.sleep(delay)
        candidates = temporary_providers
        round_index += 1
    if any(a["status"] != "skipped_not_enabled" for a in attempts):
        result.update(providerAttempts=attempts, apiCallsThisRun=initial_budget - budget)
        return result, budget
    return {"status": "waiting_for_provider", "providerAttempts": attempts, "apiCallsThisRun": 0}, budget


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
                  "provider": config.get("provider", "gemini"), "requestedRuns": 1, "jobs": {}, "handoffErrors": problems,
                  "stopOn503": config.get("stopOn503", False),
                  "waitingClasses": waiting_classes(config, jobs)}
        if config.get("fallbackProviders"):
            report["providerOrder"] = [config.get("provider", "gemini"), *config["fallbackProviders"]]
            report["fallbackOn503"] = config.get("fallbackOn503", False)
        budget = config["maxApiCalls"]
        for job in jobs:
            key = f"{job['class']}/{job['batch']}"
            checkpoint = exercise.paths(job['class'], job['batch'])["checkpoint"]
            before = load(checkpoint).get("apiAttempts", 0) if checkpoint.exists() else 0
            budget_before = budget
            report["jobs"][key] = {"status": "running", "startedAt": timestamp()}
            atomic_write(report, output / "latest.json")
            try:
                def report_retry(result):
                    report["jobs"][key] = result
                    atomic_write(report, output / "latest.json")

                validator = validate_with_provider_failover if uses_key_failover(config) else validate_with_provider_retries
                result, budget = validator(
                    job, config, state["jobs"], budget, directory, on_retry=report_retry)
                if result["status"] == "completed":
                    p = exercise.paths(job["class"], job["batch"])
                    initialization = build_initialization_report(p["final"],
                        db_path=local_path(os.getenv("ASSESSMENT_DB_PATH", "data/local/assessments.sqlite3")),
                        model=config["irtModel"])
                    atomic_write(initialization, directory / f"{job['class']}_{job['batch']}_irt.json")
            except Exception as exc:
                after = load(checkpoint).get("apiAttempts", 0) if checkpoint.exists() else before
                budget = getattr(exc, "remaining_budget", budget_before - max(0, after - before))
                result = {"status": "failed", "errorType": type(exc).__name__}
                # Technical traceback remains local; reports do not echo private rows/keys.
                import traceback
                with (directory / f"{job['class']}_{job['batch']}_error.log").open("w", encoding="utf-8") as log:
                    traceback.print_exc(file=log)
            state["jobs"][key] = result
            report["jobs"][key] = result
            atomic_write(state, state_path)
            atomic_write(report, output / "latest.json")
            stop = result.get("providerStop", {})
            hard_stop = (not config.get("stopOn503", False)
                         or stop.get("errorCode", "").endswith((":503", ":429", ":401", ":403"))
                         or stop.get("status") in {"blocked_provider_daily_quota", "blocked_provider_configuration"})
            if result.get("exitCode") == 3 and hard_stop:
                # A shared provider stop must not trigger calls for later classes.
                report["providerStoppedAt"] = key
                report["stopNotice"] = result.get("providerStop", {
                    "message": "Validasi Gemini berhenti; periksa stopReason pada checkpoint kelas terkait."})
                for pending in jobs[jobs.index(job) + 1:]:
                    report["jobs"][f"{pending['class']}/{pending['batch']}"] = {"status": "waiting_for_provider"}
                break
        # Response-based analysis runs even when extraction/LLM validation is blocked.
        try:
            report["psychometrics"] = screen_assessments(config, output)
        except Exception as exc:
            report["psychometrics"] = {"status": "failed", "errorType": type(exc).__name__}
        try:
            from scripts.empirical_finetuning import run_feedback
            report["fineTuning"] = run_feedback(config, report["psychometrics"], output / "fine_tuning", ROOT)
        except Exception as exc:
            report["fineTuning"] = {"status": "failed", "errorType": type(exc).__name__}
        report.update(finishedAt=timestamp(), remainingApiCalls=budget)
        report["success"] = (not problems and not report["waitingClasses"]
                             and all(j["status"] == "completed" for j in report["jobs"].values())
                             and report["psychometrics"]["status"] != "failed"
                             and report["fineTuning"]["status"] != "failed"
                             and all(a["status"] not in ("failed", "training_failed", "training_timeout")
                                     for a in report["fineTuning"].get("assessments", []))
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
        exercise.set_namespace("failover" if uses_key_failover(config) else None)
        exercise.set_provider(config.get("provider", "gemini"))
        os.environ["LLM_PROVIDER"] = config.get("provider", "gemini")
        if args.command == "run":
            if not args.execute:
                parser.error("run makes live provider calls and requires --execute")
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
                        "apiAttempts": checkpoint.get("apiAttempts", 0),
                        "updatedAt": checkpoint.get("updatedAt"),
                        "tokenUsage": {field: checkpoint.get("summary", {}).get(field, 0)
                                       for field in ("promptTokens", "outputTokens", "thinkingTokens", "totalTokens")},
                        "providerStop": provider_stop_notice(checkpoint)}
            result = {"jobs": jobs, "handoffErrors": problems, "schedule": "01:00 Asia/Jakarta",
                      "provider": config.get("provider", "gemini"),
                      "stopOn503": config.get("stopOn503", False),
                      "waitingClasses": waiting_classes(config, jobs),
                      "latestReport": str(local_path(args.output) / "latest.json")}
            result["checkedAt"] = timestamp()
            status_directory = local_path(args.output)
            status_directory.mkdir(parents=True, exist_ok=True)
            atomic_write(result, status_directory / "status.json")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("success", True) else 1


if __name__ == "__main__":
    raise SystemExit(main())
