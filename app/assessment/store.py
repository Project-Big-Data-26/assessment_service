"""Transactional SQLite store for the local pilot; no raw student identity.

MongoDB remains the source of human gold. A reviewed frozen snapshot is copied
into an immutable assessment. SQLite permits operation without provisioning a
second remote service. One connection per transaction works across threads.
"""
from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
import hashlib
import hmac
import json
from pathlib import Path
import secrets
import sqlite3
import uuid

from app.classification.v2.serializer import canonical_json_hash
from app.psychometrics.analysis import analyze_matrix, normalize_events
from app.psychometrics.contracts import AnalysisPolicy, ScreeningInput
from app.training.v2.dataset import DatasetSnapshot
from .contracts import AssessmentCreate, EmpiricalDecisionInput, ResponseCreate


def now():
    return datetime.now(timezone.utc)


def encode(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def token_hash(token):
    return hashlib.sha256(token.encode()).hexdigest()


class AssessmentError(ValueError):
    def __init__(self, message, status_code=409):
        super().__init__(message)
        self.status_code = status_code


class AssessmentStore:
    def __init__(self, path: str | Path, *, subject_secret: str | None = None):
        self.path = Path(path).resolve()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.connection() as db:
            db.executescript("""
                CREATE TABLE IF NOT EXISTS metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS assessments (id TEXT PRIMARY KEY, hash TEXT NOT NULL, document TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS participants (token_hash TEXT PRIMARY KEY, assessment_id TEXT NOT NULL, subject_hash TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS sessions (id TEXT PRIMARY KEY, assessment_id TEXT NOT NULL, subject_hash TEXT NOT NULL,
                    idempotency_key TEXT NOT NULL, request_hash TEXT NOT NULL, status TEXT NOT NULL, started_at TEXT NOT NULL,
                    expires_at TEXT NOT NULL, completed_at TEXT, UNIQUE(assessment_id, subject_hash, idempotency_key));
                CREATE TABLE IF NOT EXISTS deliveries (id TEXT PRIMARY KEY, session_id TEXT NOT NULL, sequence INTEGER NOT NULL,
                    document TEXT NOT NULL, UNIQUE(session_id, sequence));
                CREATE TABLE IF NOT EXISTS responses (id TEXT PRIMARY KEY, delivery_id TEXT NOT NULL UNIQUE,
                    session_id TEXT NOT NULL, request_hash TEXT NOT NULL, document TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS snapshots (id TEXT PRIMARY KEY, hash TEXT NOT NULL UNIQUE, assessment_id TEXT NOT NULL,
                    created_at TEXT NOT NULL, document TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS empirical_decisions (id TEXT PRIMARY KEY, snapshot_id TEXT NOT NULL,
                    question_version_id TEXT NOT NULL, idempotency_key TEXT NOT NULL UNIQUE, document TEXT NOT NULL,
                    UNIQUE(snapshot_id, question_version_id));
                CREATE INDEX IF NOT EXISTS sessions_assessment ON sessions(assessment_id, status, subject_hash);
                CREATE INDEX IF NOT EXISTS responses_session ON responses(session_id);
                CREATE INDEX IF NOT EXISTS snapshots_assessment ON snapshots(assessment_id, created_at);
            """)
            db.execute("INSERT OR IGNORE INTO metadata VALUES ('subject_secret', ?)", (subject_secret or secrets.token_hex(32),))
            stored_secret = db.execute("SELECT value FROM metadata WHERE key='subject_secret'").fetchone()[0]
            if subject_secret and not hmac.compare_digest(subject_secret, stored_secret):
                raise ValueError("subject pseudonym secret changed; use an explicit migration or a new store")
            self.subject_secret = stored_secret.encode()

    @contextmanager
    def connection(self):
        db = sqlite3.connect(self.path, timeout=30)
        db.row_factory = sqlite3.Row
        try:
            db.execute("PRAGMA foreign_keys=ON")
            # Serializes mutations, including concurrent retries/next-item calls.
            db.execute("BEGIN IMMEDIATE")
            yield db
            db.commit()
        except BaseException:
            db.rollback()
            raise
        finally:
            db.close()

    @staticmethod
    def _document(db, table, record_id):
        # Table names are internal constants, never interpolated from a request.
        row = db.execute(f"SELECT document FROM {table} WHERE id=?", (record_id,)).fetchone()
        if row is None:
            raise AssessmentError("record not found", 404)
        return json.loads(row[0])

    def create_assessment(self, payload: AssessmentCreate, snapshot: DatasetSnapshot) -> dict:
        if snapshot.snapshotId != payload.snapshotId:
            raise AssessmentError("snapshot ID mismatch")
        rows = [row.model_dump(mode="json") for row in sorted(snapshot.rows, key=lambda row: row.questionVersionId)]
        if canonical_json_hash(rows) != snapshot.snapshotHash:
            raise AssessmentError("gold snapshot checksum mismatch")
        if snapshot.researchOnly or snapshot.labelProvenance != "human_gold":
            raise AssessmentError("pilot delivery requires a human-gold snapshot; silver/research artifacts are ineligible")
        row_by_id = {row["questionVersionId"]: row for row in rows}
        items = []
        for version in payload.questionVersionIds:
            row = row_by_id.get(version)
            if row is None or row["grade"] != payload.grade:
                raise AssessmentError("item is missing or outside the assessment grade")
            provenance = row["decisionProvenance"]
            if provenance.get("kind") not in {"gold_ready", "adjudicated"} or not provenance.get("decisionId"):
                raise AssessmentError("every delivered version requires a completed human decision")
            key = provenance.get("verifiedAnswerKey")
            option_ids = [option["label"] for option in row["options"]]
            if row["questionType"] != "multiple_choice" or key not in option_ids or len(option_ids) < 2 or len(set(option_ids)) != len(option_ids):
                raise AssessmentError("this pilot supports single-answer multiple_choice with a verified key")
            if not row["verifiedMinimalSolution"].strip():
                raise AssessmentError("a verified solution is required")
            # Text-only delivery is explicit: visual items need expert transcription.
            if row.get("visualTranscript"):
                question_text = row["stem"] + "\n" + row["visualTranscript"]
            else:
                question_text = row["stem"]
            items.append({
                "questionId": row["questionId"], "questionVersionId": version, "contentVersion": row["contentVersion"],
                "contentHash": row["contentHash"], "intendedDifficulty": row["intendedDifficulty"],
                "optionIds": option_ids, "answerKey": key, "stem": question_text,
                "stimulus": row.get("stimulus"), "options": row["options"],
                "expertDecisionId": provenance["decisionId"],
            })
        if len({item["questionId"] for item in items}) != len(items):
            raise AssessmentError("an assessment cannot contain two versions of the same question")
        document = {**payload.model_dump(mode="json"), "items": items, "snapshotHash": snapshot.snapshotHash,
                    "scoringPolicyVersion": "single-choice-dichotomous-v1", "deliveryPolicyVersion": "fixed-form-pilot-v1"}
        digest = canonical_json_hash(document)
        with self.connection() as db:
            if any(self._held(db, item["questionVersionId"]) for item in items):
                raise AssessmentError("assessment contains an item version held by an empirical expert decision")
            existing = db.execute("SELECT hash FROM assessments WHERE id=?", (payload.assessmentId,)).fetchone()
            if existing and existing[0] != digest:
                raise AssessmentError("assessment ID already refers to a different immutable blueprint")
            db.execute("INSERT OR IGNORE INTO assessments VALUES (?,?,?)", (payload.assessmentId, digest, encode(document)))
        return {"assessmentId": payload.assessmentId, "assessmentHash": digest, "itemCount": len(items), "status": "ready"}

    def participant(self, assessment_id: str, participant_code: str) -> dict:
        with self.connection() as db:
            assessment = self._document(db, "assessments", assessment_id)
            subject = hmac.new(self.subject_secret, (assessment["populationId"] + "\0" + participant_code).encode(), hashlib.sha256).hexdigest()
            token = secrets.token_urlsafe(32)
            db.execute("INSERT INTO participants VALUES (?,?,?)", (token_hash(token), assessment_id, subject))
        return {"assessmentId": assessment_id, "participantToken": token, "tokenType": "Bearer"}

    @staticmethod
    def _participant(db, token):
        row = db.execute("SELECT * FROM participants WHERE token_hash=?", (token_hash(token),)).fetchone()
        if row is None:
            raise AssessmentError("participant authentication required", 401)
        return row

    @staticmethod
    def _owned_session(db, session_id, participant, *, require_active=True):
        row = db.execute("SELECT * FROM sessions WHERE id=? AND subject_hash=? AND assessment_id=?",
                         (session_id, participant["subject_hash"], participant["assessment_id"])).fetchone()
        if row is None:
            raise AssessmentError("session not found", 404)
        if require_active and (row["status"] != "active" or datetime.fromisoformat(row["expires_at"]) <= now()):
            raise AssessmentError("session is completed or expired")
        return row

    def start(self, assessment_id: str, token: str, idempotency_key: str):
        with self.connection() as db:
            participant = self._participant(db, token)
            if participant["assessment_id"] != assessment_id:
                raise AssessmentError("assessment not found", 404)
            assessment = self._document(db, "assessments", assessment_id)
            row = db.execute("SELECT * FROM sessions WHERE assessment_id=? AND subject_hash=? AND idempotency_key=?",
                             (assessment_id, participant["subject_hash"], idempotency_key)).fetchone()
            if row is None:
                timestamp = now(); session_id = str(uuid.uuid4())
                expires = timestamp + timedelta(minutes=assessment["sessionTtlMinutes"])
                db.execute("INSERT INTO sessions VALUES (?,?,?,?,?,?,?,?,?)",
                           (session_id, assessment_id, participant["subject_hash"], idempotency_key,
                            canonical_json_hash({"assessmentId": assessment_id}), "active", timestamp.isoformat(), expires.isoformat(), None))
                row = db.execute("SELECT * FROM sessions WHERE id=?", (session_id,)).fetchone()
        return {"sessionId": row["id"], "assessmentId": assessment_id, "status": row["status"], "expiresAt": row["expires_at"],
                "nextItemUrl": f"/api/v1/sessions/{row['id']}/items/next"}

    def next_item(self, session_id: str, token: str):
        with self.connection() as db:
            participant = self._participant(db, token)
            session = self._owned_session(db, session_id, participant)
            assessment = self._document(db, "assessments", session["assessment_id"])
            pending = db.execute("SELECT d.document FROM deliveries d LEFT JOIN responses r ON r.delivery_id=d.id WHERE d.session_id=? AND r.id IS NULL",
                                 (session_id,)).fetchone()
            if pending:
                delivery = json.loads(pending[0])
                if self._held(db, delivery["item"]["questionVersionId"]):
                    raise AssessmentError("item version is held for expert revision")
                return delivery["public"]
            sequence = db.execute("SELECT COUNT(*) FROM deliveries WHERE session_id=?", (session_id,)).fetchone()[0]
            if sequence >= len(assessment["items"]):
                return {"sessionId": session_id, "finished": True, "item": None}
            item = assessment["items"][sequence]
            if self._held(db, item["questionVersionId"]):
                raise AssessmentError("item version is held for expert revision; this assessment needs a new blueprint")
            options = list(item["options"]); secrets.SystemRandom().shuffle(options)
            mapping = {secrets.token_urlsafe(12): option["label"] for option in options}
            public_options = [{"id": public, "text": option["text"]} for public, option in zip(mapping, options, strict=True)]
            delivery_id = str(uuid.uuid4())
            public = {"deliveryInstanceId": delivery_id, "sessionId": session_id,
                      "item": {"publicItemId": secrets.token_urlsafe(12), "questionType": "multiple_choice",
                               "questionText": item["stem"], "stimulus": item["stimulus"], "options": public_options, "media": []},
                      "sequence": {"current": sequence + 1, "total": len(assessment["items"])},
                      "timing": {"deliveredAt": now().isoformat(), "expiresAt": session["expires_at"]}}
            document = {"public": public, "mapping": mapping, "item": item}
            db.execute("INSERT INTO deliveries VALUES (?,?,?,?)", (delivery_id, session_id, sequence, encode(document)))
            return public

    def respond(self, payload: ResponseCreate, token: str):
        digest = canonical_json_hash(payload.model_dump(mode="json"))
        with self.connection() as db:
            participant = self._participant(db, token)
            delivery = db.execute("SELECT * FROM deliveries WHERE id=?", (payload.deliveryInstanceId,)).fetchone()
            if delivery is None:
                raise AssessmentError("delivery not found", 404)
            session = self._owned_session(db, delivery["session_id"], participant, require_active=False)
            existing = db.execute("SELECT * FROM responses WHERE id=?", (payload.responseId,)).fetchone()
            if existing:
                if existing["session_id"] != session["id"] or existing["request_hash"] != digest:
                    raise AssessmentError("response ID was already used with different content")
                return self._receipt(payload.responseId, session["id"])
            self._owned_session(db, delivery["session_id"], participant)
            if db.execute("SELECT 1 FROM responses WHERE delivery_id=?", (payload.deliveryInstanceId,)).fetchone():
                raise AssessmentError("delivery already has a final response")
            document = json.loads(delivery["document"])
            mapping = document["mapping"]; item = document["item"]
            if any(option not in mapping for option in payload.selectedOptionIds):
                raise AssessmentError("option ID is not part of this delivery", 422)
            assessment = self._document(db, "assessments", session["assessment_id"])
            selected = [mapping[option] for option in payload.selectedOptionIds]
            correct = None if payload.skipped else selected[0] == item["answerKey"]
            cutoff = assessment["rapidGuessMs"]
            elapsed_ms = max(0, int((now() - datetime.fromisoformat(document["public"]["timing"]["deliveredAt"])).total_seconds() * 1000))
            # Client timing is advisory; rapid guess exclusion uses server timing.
            flags = ["rapid_guess_candidate"] if cutoff is not None and elapsed_ms < cutoff and not payload.skipped else []
            if self._held(db, item["questionVersionId"]):
                flags.append("item_held_after_delivery")
            event = {"responseId": payload.responseId, "deliveryInstanceId": payload.deliveryInstanceId, "sessionId": session["id"],
                     "assessmentId": session["assessment_id"], "populationId": assessment["populationId"],
                     "assessmentFamily": assessment["assessmentFamily"], "grade": assessment["grade"],
                     "subjectHash": session["subject_hash"],
                     **{key: item[key] for key in ("questionId", "questionVersionId", "contentVersion", "contentHash")},
                     "selectedInternalOptionIds": selected, "isCorrect": correct, "score": None if correct is None else int(correct),
                     "scoringStatus": "skipped" if payload.skipped else "scored", "scoringPolicyVersion": assessment["scoringPolicyVersion"],
                     "responseTimeMs": elapsed_ms, "clientResponseTimeMs": payload.responseTimeMs,
                     "answerChanges": payload.answerChanges, "flags": flags, "validForAnalysis": not flags,
                     "submittedAt": now().isoformat()}
            db.execute("INSERT INTO responses VALUES (?,?,?,?,?)", (payload.responseId, payload.deliveryInstanceId, session["id"], digest, encode(event)))
        return self._receipt(payload.responseId, session["id"])

    @staticmethod
    def _receipt(response_id, session_id):
        # No correctness feedback is exposed during the pilot.
        return {"responseId": response_id, "accepted": True, "nextItemUrl": f"/api/v1/sessions/{session_id}/items/next"}

    def complete(self, session_id: str, token: str):
        with self.connection() as db:
            participant = self._participant(db, token)
            session = self._owned_session(db, session_id, participant, require_active=False)
            if session["status"] != "completed":
                self._owned_session(db, session_id, participant)
                assessment = self._document(db, "assessments", session["assessment_id"])
                response_count = db.execute("SELECT COUNT(*) FROM responses WHERE session_id=?", (session_id,)).fetchone()[0]
                if response_count != len(assessment["items"]):
                    raise AssessmentError("answer or explicitly skip every item before completing the session")
                db.execute("UPDATE sessions SET status='completed', completed_at=? WHERE id=?", (now().isoformat(), session_id))
        return {"sessionId": session_id, "status": "completed"}

    def screen(self, payload: ScreeningInput, policy: AnalysisPolicy):
        with self.connection() as db:
            assessment = self._document(db, "assessments", payload.assessmentId)
            sessions = db.execute("SELECT * FROM sessions WHERE assessment_id=? AND status='completed' ORDER BY started_at, id", (payload.assessmentId,)).fetchall()
            chosen = {}
            for session in sessions:
                completed = datetime.fromisoformat(session["completed_at"])
                if (payload.fromTime and completed < payload.fromTime) or (payload.toTime and completed >= payload.toTime):
                    continue
                if payload.attemptPolicy == "last" or session["subject_hash"] not in chosen:
                    chosen[session["subject_hash"]] = session
            if not chosen:
                raise AssessmentError("no completed sessions in this assessment/time window; collect student responses first")
            events = []
            for session in chosen.values():
                events.extend(json.loads(row[0]) for row in db.execute("SELECT document FROM responses WHERE session_id=? ORDER BY id", (session["id"],)))
        item_references = [{key: item[key] for key in ("questionId", "questionVersionId", "contentVersion", "contentHash", "intendedDifficulty", "optionIds", "answerKey")} for item in assessment["items"]]
        matrix, cleaning = normalize_events(events, items=item_references, subject_ids=sorted(chosen),
                                            population_id=assessment["populationId"], assessment_family=assessment["assessmentFamily"],
                                            grade=assessment["grade"], model=payload.model, attempt_policy=payload.attemptPolicy,
                                            assumption_review=payload.assumptionReview)
        selected = cleaning.pop("events")
        result = analyze_matrix(matrix, policy, events=selected)
        result["cleaning"] = {**cleaning, "selectedSessions": len(chosen), "completedSessions": len(sessions),
                              "selectionUnit": "whole_completed_session", "timeWindowBasis": "session_completed_at"}
        result["assessmentId"] = payload.assessmentId
        result["timeWindow"] = {"from": payload.fromTime.isoformat() if payload.fromTime else None,
                                "to": payload.toTime.isoformat() if payload.toTime else None}
        result["sampleManifestHash"] = canonical_json_hash({"sessions": sorted(session["id"] for session in chosen.values()),
                                                           "responses": sorted(event["responseId"] for event in selected)})
        result["snapshotHash"] = canonical_json_hash(result)
        digest = result["snapshotHash"]
        result["snapshotId"] = f"psy-{digest[:24]}"
        result["createdAt"] = now().isoformat()
        with self.connection() as db:
            existing = db.execute("SELECT document FROM snapshots WHERE hash=?", (digest,)).fetchone()
            if existing:
                return json.loads(existing[0])
            db.execute("INSERT INTO snapshots VALUES (?,?,?,?,?)", (result["snapshotId"], digest, payload.assessmentId, result["createdAt"], encode(result)))
        return result

    def snapshot(self, snapshot_id):
        with self.connection() as db:
            return self._document(db, "snapshots", snapshot_id)

    def list_snapshots(self, question_id: str | None = None):
        with self.connection() as db:
            documents = [json.loads(row[0]) for row in db.execute("SELECT document FROM snapshots ORDER BY created_at DESC LIMIT 100")]
        results = []
        for document in documents:
            items = [item for item in document["items"] if question_id is None or item["questionId"] == question_id]
            if items:
                results.append({key: document[key] for key in ("snapshotId", "assessmentId", "populationId", "assessmentFamily", "grade", "createdAt", "policyVersion", "researchOnly")} | {"items": items, "irtStatus": document["irt"]["status"]})
        return results

    @staticmethod
    def _held(db, question_version_id):
        row = db.execute("SELECT document FROM empirical_decisions WHERE question_version_id=? ORDER BY rowid DESC LIMIT 1", (question_version_id,)).fetchone()
        return row is not None and json.loads(row[0])["action"] in {"revise", "quarantine"}

    def is_held(self, question_version_id: str) -> bool:
        with self.connection() as db:
            return self._held(db, question_version_id)

    def decisions(self, snapshot_id: str):
        with self.connection() as db:
            self._document(db, "snapshots", snapshot_id)
            return [json.loads(row[0]) for row in db.execute("SELECT document FROM empirical_decisions WHERE snapshot_id=? ORDER BY rowid", (snapshot_id,))]

    def decide(self, snapshot_id: str, payload: EmpiricalDecisionInput, expert_id: str):
        with self.connection() as db:
            snapshot = self._document(db, "snapshots", snapshot_id)
            if payload.questionVersionId not in {item["questionVersionId"] for item in snapshot["items"]}:
                raise AssessmentError("item version is not part of the snapshot", 404)
            document = {**payload.model_dump(mode="json"), "snapshotId": snapshot_id, "snapshotHash": snapshot["snapshotHash"],
                        "expertId": expert_id, "affectsGoldLabels": False,
                        "nextStep": "new_content_version_and_blind_expert_review" if payload.action == "revise" else "hold_delivery" if payload.action == "quarantine" else "retain_current_labels"}
            existing = db.execute("SELECT document FROM empirical_decisions WHERE idempotency_key=?", (payload.idempotencyKey,)).fetchone()
            if existing:
                original = json.loads(existing[0])
                if any(original.get(key) != value for key, value in document.items()):
                    raise AssessmentError("decision idempotency key conflicts with another decision")
                return original
            if db.execute("SELECT 1 FROM empirical_decisions WHERE snapshot_id=? AND question_version_id=?", (snapshot_id, payload.questionVersionId)).fetchone():
                raise AssessmentError("this snapshot/item already has an immutable expert decision")
            document.update(decisionId=str(uuid.uuid4()), createdAt=now().isoformat())
            db.execute("INSERT INTO empirical_decisions VALUES (?,?,?,?,?)", (document["decisionId"], snapshot_id, payload.questionVersionId, payload.idempotencyKey, encode(document)))
        return document
