"""MongoDB Atlas repository with one application-scoped async client."""

from __future__ import annotations

import os
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any

from .contracts import AdjudicationDecisionInput, DiscussionOutcomeInput, ExpertAnnotationInput
from .security import SESSION_TTL_SECONDS, hash_secret

COLLECTIONS = (
    "users",
    "expert_profiles",
    "questions",
    "question_versions",
    "annotation_assignments",
    "expert_annotations",
    "expert_decisions",
    "dataset_snapshots",
    "training_runs",
    "model_versions",
    "audit_events",
    "sessions",
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class MongoAnnotationRepository:
    """Repository created once during application startup and reused by all requests."""

    def __init__(self, client: Any, database_name: str) -> None:
        self.client = client
        self.db = client[database_name]

    @classmethod
    def from_environment(cls) -> "MongoAnnotationRepository | None":
        uri = os.getenv("MONGODB_URI")
        database = os.getenv("MONGODB_DATABASE")
        if not uri or not database:
            return None
        if os.getenv("APP_ENV", "development") != "development" and len(os.getenv("SESSION_SECRET", "")) < 32:
            raise RuntimeError("production annotation service requires SESSION_SECRET with at least 32 characters")
        try:
            from pymongo import AsyncMongoClient
        except ImportError as exc:  # pragma: no cover - deployment dependency guard
            raise RuntimeError("pymongo>=4.9 is required when MONGODB_URI is configured") from exc
        client = AsyncMongoClient(uri, appname="nalar-annotation-v2", serverSelectionTimeoutMS=5000)
        return cls(client, database)

    async def ping(self) -> None:
        await self.db.command("ping")

    async def close(self) -> None:
        await self.client.close()

    async def ensure_indexes(self) -> None:
        from pymongo import ASCENDING

        await self.db.users.create_index("userId", unique=True)
        await self.db.users.create_index("usernameNormalized", unique=True)
        await self.db.expert_profiles.create_index("expertId", unique=True)
        await self.db.questions.create_index("questionId", unique=True)
        await self.db.question_versions.create_index("questionVersionId", unique=True)
        await self.db.question_versions.create_index("contentHash")
        await self.db.question_versions.create_index(
            [("questionId", ASCENDING), ("contentHash", ASCENDING)], unique=True
        )
        await self.db.annotation_assignments.create_index("assignmentId", unique=True)
        await self.db.annotation_assignments.create_index(
            [("expertId", ASCENDING), ("questionVersionId", ASCENDING), ("rubricVersion", ASCENDING)],
            unique=True,
        )
        await self.db.annotation_assignments.create_index(
            [("expertId", ASCENDING), ("status", ASCENDING), ("assignedAt", ASCENDING)]
        )
        await self.db.expert_annotations.create_index("annotationId", unique=True)
        await self.db.expert_annotations.create_index(
            [("expertId", ASCENDING), ("questionVersionId", ASCENDING), ("rubricVersion", ASCENDING)],
            unique=True,
        )
        await self.db.expert_annotations.create_index("idempotencyKey", unique=True)
        await self.db.expert_decisions.create_index("decisionId", unique=True)
        await self.db.expert_decisions.create_index("idempotencyKey", unique=True, sparse=True)
        await self.db.dataset_snapshots.create_index("snapshotId", unique=True)
        await self.db.training_runs.create_index("trainingRunId", unique=True)
        await self.db.model_versions.create_index("modelVersion", unique=True)
        await self.db.audit_events.create_index("auditEventId", unique=True)
        await self.db.audit_events.create_index(
            [("eventType", ASCENDING), ("metadata.usernameNormalized", ASCENDING), ("createdAt", ASCENDING)]
        )
        await self.db.sessions.create_index("tokenHash", unique=True)
        await self.db.sessions.create_index("expiresAt", expireAfterSeconds=0)

    async def audit(self, event_type: str, actor_id: str | None, metadata: dict[str, Any] | None = None) -> None:
        await self.db.audit_events.insert_one(
            {
                "auditEventId": str(uuid.uuid4()),
                "eventType": event_type,
                "actorId": actor_id,
                "metadata": metadata or {},
                "createdAt": utc_now(),
            }
        )

    async def find_user_for_login(self, username: str) -> dict[str, Any] | None:
        return await self.db.users.find_one(
            {"usernameNormalized": username.strip().casefold(), "active": True},
            {"_id": 0},
        )

    async def count_recent_login_failures(self, username: str, window_minutes: int = 15) -> int:
        return await self.db.audit_events.count_documents(
            {
                "eventType": "auth.login_failed",
                "metadata.usernameNormalized": username.strip().casefold(),
                "createdAt": {"$gte": utc_now() - timedelta(minutes=window_minutes)},
            }
        )

    async def create_session(self, user: dict[str, Any], token_hash: str, csrf_hash: str) -> None:
        now = utc_now()
        await self.db.sessions.insert_one(
            {
                "sessionId": str(uuid.uuid4()),
                "tokenHash": token_hash,
                "csrfHash": csrf_hash,
                "userId": user["userId"],
                "expertId": user.get("expertId"),
                "roles": user.get("roles", []),
                "createdAt": now,
                "expiresAt": now + timedelta(seconds=SESSION_TTL_SECONDS),
                "revokedAt": None,
            }
        )

    async def get_session(self, raw_token: str) -> dict[str, Any] | None:
        return await self.db.sessions.find_one(
            {"tokenHash": hash_secret(raw_token), "expiresAt": {"$gt": utc_now()}, "revokedAt": None},
            {"_id": 0},
        )

    async def revoke_session(self, raw_token: str) -> None:
        await self.db.sessions.update_one(
            {"tokenHash": hash_secret(raw_token)}, {"$set": {"revokedAt": utc_now()}}
        )

    async def next_assignment(self, expert_id: str) -> dict[str, Any] | None:
        return await self.db.annotation_assignments.find_one(
            {"expertId": expert_id, "status": "assigned"},
            sort=[("assignedAt", 1)],
            projection={"_id": 0},
        )

    async def assignment_for_expert(self, assignment_id: str, expert_id: str) -> dict[str, Any] | None:
        return await self.db.annotation_assignments.find_one(
            {"assignmentId": assignment_id, "expertId": expert_id}, {"_id": 0}
        )

    async def reviewer_question(self, question_version_id: str) -> dict[str, Any] | None:
        # Agent judgments and peer/consensus data are deliberately excluded.
        return await self.db.question_versions.find_one(
            {"questionVersionId": question_version_id},
            {
                "_id": 0,
                "extractionEvidence.agentAnswer": 0,
                "extractionEvidence.agentDifficulty": 0,
                "extractionEvidence.agentDifficultyReason": 0,
                "extractionEvidence.sourceKeyStatus": 0,
                "modelPrediction": 0,
                "consensus": 0,
            },
        )

    async def submit_annotation(
        self, assignment: dict[str, Any], payload: ExpertAnnotationInput
    ) -> dict[str, Any]:
        annotation_id = str(uuid.uuid4())
        record = {
            **payload.model_dump(mode="json"),
            "annotationId": annotation_id,
            "assignmentId": assignment["assignmentId"],
            "expertId": assignment["expertId"],
            "questionVersionId": assignment["questionVersionId"],
            "rubricVersion": assignment["rubricVersion"],
            "submittedAt": utc_now(),
            "immutable": True,
        }
        async with self.client.start_session() as session:
            async with await session.start_transaction():
                existing = await self.db.expert_annotations.find_one(
                    {"idempotencyKey": payload.idempotencyKey}, {"_id": 0}, session=session
                )
                if existing:
                    return existing
                lock = await self.db.annotation_assignments.update_one(
                    {"assignmentId": assignment["assignmentId"], "status": "assigned"},
                    {"$set": {"status": "submitted", "submittedAt": utc_now()}},
                    session=session,
                )
                if lock.modified_count != 1:
                    raise RuntimeError("assignment is already locked")
                await self.db.expert_annotations.insert_one(record, session=session)
                await self.db.audit_events.insert_one(
                    {
                        "auditEventId": str(uuid.uuid4()),
                        "eventType": "annotation.submitted",
                        "actorId": assignment["expertId"],
                        "metadata": {"assignmentId": assignment["assignmentId"]},
                        "createdAt": utc_now(),
                    },
                    session=session,
                )
        record.pop("_id", None)
        return record

    async def list_adjudications(self) -> list[dict[str, Any]]:
        cursor = self.db.expert_decisions.find(
            {"status": "pending_adjudication"}, {"_id": 0, "initialAnnotations": 0}
        ).sort("createdAt", 1)
        return await cursor.to_list(length=100)

    async def discussion_case(self, decision_id: str) -> dict[str, Any] | None:
        return await self.db.expert_decisions.find_one(
            {"decisionId": decision_id, "status": "discussion_required"}, {"_id": 0}
        )

    @staticmethod
    def _validate_resolved_labels(case: dict[str, Any], payload: Any) -> None:
        consensus = case.get("initialConsensus", {})
        for head in ("mathCognitiveDomain", "knowledgeDimension", "intendedDifficulty"):
            initial = consensus.get(head, {})
            if initial.get("status") != "discussion_required":
                if getattr(payload, head, None) != initial.get("label"):
                    raise RuntimeError(f"resolved discussion may not replace settled {head} vote")
        content = consensus.get("content", {})
        if content.get("status") == "eligible":
            if (
                getattr(payload, "verifiedAnswerKey", None) != content.get("verifiedAnswerKey")
                or getattr(payload, "verifiedMinimalSolution", None) != content.get("verifiedMinimalSolution")
            ):
                raise RuntimeError("resolved discussion may not replace already verified content")

    async def submit_discussion(
        self, case: dict[str, Any], actor_id: str, payload: DiscussionOutcomeInput
    ) -> dict[str, Any]:
        cursor = self.db.expert_annotations.find(
            {"annotationId": {"$in": case.get("initialAnnotationIds", [])}},
            {"_id": 0, "expertId": 1},
        )
        initial_experts = {document["expertId"] async for document in cursor}
        if initial_experts != set(payload.participantExpertIds):
            raise RuntimeError("discussion participants must be the three original blind reviewers")
        if payload.unresolvedAfterDiscussion:
            status = "pending_adjudication"
            decision = None
        else:
            if not payload.insufficientEvidence:
                self._validate_resolved_labels(case, payload)
            status = "quarantined" if payload.insufficientEvidence else "adjudicated"
            decision = payload.model_dump(mode="json")
        result = await self.db.expert_decisions.find_one_and_update(
            {"decisionId": case["decisionId"], "status": "discussion_required"},
            {
                "$set": {
                    "status": status,
                    "discussionOutcome": payload.model_dump(mode="json"),
                    "decision": decision,
                    "discussionRecordedBy": actor_id,
                    "discussionRecordedAt": utc_now(),
                }
            },
            return_document=True,
            projection={"_id": 0},
        )
        if result is None:
            raise RuntimeError("discussion case is already resolved")
        await self.audit(
            "annotation.discussion_recorded",
            actor_id,
            {"decisionId": case["decisionId"], "status": status},
        )
        return result

    async def adjudication(self, adjudication_id: str) -> dict[str, Any] | None:
        return await self.db.expert_decisions.find_one(
            {"decisionId": adjudication_id, "status": "pending_adjudication"}, {"_id": 0}
        )

    async def submit_adjudication(
        self, adjudication: dict[str, Any], actor_id: str, payload: AdjudicationDecisionInput
    ) -> dict[str, Any]:
        if not payload.insufficientEvidence:
            self._validate_resolved_labels(adjudication, payload)
        outcome = "quarantined" if payload.insufficientEvidence else "adjudicated"
        update = {
            "status": outcome,
            "decision": payload.model_dump(mode="json"),
            "idempotencyKey": payload.idempotencyKey,
            "decidedBy": actor_id,
            "decidedAt": utc_now(),
        }
        result = await self.db.expert_decisions.find_one_and_update(
            {"decisionId": adjudication["decisionId"], "status": "pending_adjudication"},
            {"$set": update},
            return_document=True,
            projection={"_id": 0},
        )
        if result is None:
            existing = await self.db.expert_decisions.find_one(
                {"idempotencyKey": payload.idempotencyKey}, {"_id": 0}
            )
            if existing:
                return existing
            raise RuntimeError("adjudication is already decided")
        await self.audit(
            "annotation.adjudicated",
            actor_id,
            {"decisionId": adjudication["decisionId"], "status": outcome},
        )
        return result
