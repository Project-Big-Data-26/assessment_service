"""Create an Argon2id admin document; writes only to configured Atlas."""

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
    parser.add_argument("--username", required=True)
    args = parser.parse_args()
    repository = MongoAnnotationRepository.from_environment()
    if repository is None:
        raise SystemExit("MONGODB_URI and MONGODB_DATABASE must be configured")
    password = getpass.getpass("Bootstrap password: ")
    confirmation = getpass.getpass("Repeat password: ")
    if password != confirmation or len(password) < 12:
        raise SystemExit("passwords must match and contain at least 12 characters")
    try:
        await repository.ping()
        await repository.ensure_indexes()
        await repository.db.users.insert_one(
            {
                "userId": str(uuid.uuid4()),
                "usernameNormalized": args.username.strip().casefold(),
                "displayName": args.username.strip(),
                "passwordHash": password_hash(password),
                "roles": ["admin"],
                "active": True,
                "createdAt": utc_now(),
            }
        )
        print("Bootstrap admin created.")
    finally:
        await repository.close()


if __name__ == "__main__":
    asyncio.run(run())
