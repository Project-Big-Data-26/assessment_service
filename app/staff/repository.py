"""MongoDB Atlas repository with one application-scoped async client."""

from __future__ import annotations

import os
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any

from .security import SESSION_TTL_SECONDS, hash_secret

COLLECTIONS = ("users", "questions", "question_versions", "silver_decisions", "dataset_snapshots",
               "training_runs", "model_versions", "audit_events", "sessions")


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class MongoRepository:
    """Repository created once during application startup and reused by all requests."""

    def __init__(self, client: Any, database_name: str) -> None:
        self.client = client
        self.db = client[database_name]

    @classmethod
    def from_environment(cls) -> "MongoRepository | None":
        uri = os.getenv("MONGODB_URI")
        database = os.getenv("MONGODB_DATABASE")
        if not uri or not database:
            return None
        if os.getenv("APP_ENV", "development") != "development" and len(os.getenv("SESSION_SECRET", "")) < 32:
            raise RuntimeError("production staff service requires SESSION_SECRET with at least 32 characters")
        try:
            from pymongo import AsyncMongoClient
        except ImportError as exc:  # pragma: no cover - deployment dependency guard
            raise RuntimeError("pymongo>=4.9 is required when MONGODB_URI is configured") from exc
        client = AsyncMongoClient(uri, appname="nalar-silver-v2", serverSelectionTimeoutMS=5000)
        return cls(client, database)

    async def ping(self) -> None:
        await self.db.command("ping")

    async def close(self) -> None:
        await self.client.close()

    async def ensure_indexes(self) -> None:
        from pymongo import ASCENDING

        await self.db.users.create_index("userId", unique=True)
        await self.db.users.create_index("usernameNormalized", unique=True)
        await self.db.questions.create_index("questionId", unique=True)
        await self.db.question_versions.create_index("questionVersionId", unique=True)
        await self.db.question_versions.create_index("contentHash")
        await self.db.question_versions.create_index(
            [("questionId", ASCENDING), ("contentHash", ASCENDING)], unique=True
        )
        await self.db.silver_decisions.create_index("decisionId", unique=True)
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

