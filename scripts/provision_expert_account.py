"""Provision one invite-only expert user and auditable profile in Atlas."""

from __future__ import annotations

import argparse
import asyncio
import getpass
from pathlib import Path
import sys
import uuid

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.annotation.repository import MongoAnnotationRepository, utc_now
from app.annotation.security import password_hash


async def run() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expert-id", required=True)
    parser.add_argument("--username", required=True)
    parser.add_argument("--display-name", required=True)
    parser.add_argument("--contact", required=True)
    parser.add_argument("--expertise-evidence", required=True)
    parser.add_argument("--grades", required=True, help="comma-separated grades")
    parser.add_argument("--role", choices=("primary_annotator", "senior_adjudicator"), required=True)
    parser.add_argument("--conflict-declaration", required=True)
    parser.add_argument("--consent-reference", required=True)
    args = parser.parse_args()
    password = getpass.getpass("Temporary invite password (minimum 12 characters): ")
    if len(password) < 12:
        raise SystemExit("password must contain at least 12 characters")
    repository = MongoAnnotationRepository.from_environment()
    if repository is None:
        raise SystemExit("MONGODB_URI and MONGODB_DATABASE must be configured")
    user_id = str(uuid.uuid4())
    now = utc_now()
    try:
        async with repository.client.start_session() as session:
            async with await session.start_transaction():
                await repository.db.users.insert_one(
                    {
                        "userId": user_id,
                        "usernameNormalized": args.username.strip().casefold(),
                        "displayName": args.display_name,
                        "passwordHash": password_hash(password),
                        "expertId": args.expert_id,
                        "roles": [args.role],
                        "active": True,
                        "mustRotatePassword": True,
                        "createdAt": now,
                    },
                    session=session,
                )
                await repository.db.expert_profiles.insert_one(
                    {
                        "expertId": args.expert_id,
                        "userId": user_id,
                        "displayName": args.display_name,
                        "contact": args.contact,
                        "expertiseEvidence": args.expertise_evidence,
                        "gradeCoverage": [int(value) for value in args.grades.split(",")],
                        "role": args.role,
                        "conflictDeclaration": args.conflict_declaration,
                        "consentReference": args.consent_reference,
                        "active": True,
                        "createdAt": now,
                    },
                    session=session,
                )
        print(f"Provisioned {args.expert_id}; deliver the temporary password out of band.")
    finally:
        await repository.close()


if __name__ == "__main__":
    asyncio.run(run())
