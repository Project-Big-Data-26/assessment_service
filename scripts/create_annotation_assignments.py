"""Assign every candidate to exactly three primary experts without exposing peers."""

from __future__ import annotations

import argparse
import asyncio
from pathlib import Path
import sys
import uuid

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.annotation.repository import MongoAnnotationRepository, utc_now


async def run() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expert-id", action="append", required=True)
    parser.add_argument("--rubric-version", default="math-rubric-3x4x3-v1")
    args = parser.parse_args()
    experts = list(dict.fromkeys(args.expert_id))
    if len(experts) != 3:
        raise SystemExit("provide exactly three distinct --expert-id values")
    repository = MongoAnnotationRepository.from_environment()
    if repository is None:
        raise SystemExit("MONGODB_URI and MONGODB_DATABASE must be configured")
    created = 0
    try:
        await repository.ping()
        profiles = await repository.db.expert_profiles.count_documents(
            {"expertId": {"$in": experts}, "active": True, "role": "primary_annotator"}
        )
        if profiles != 3:
            raise SystemExit("all three active primary_annotator expert profiles must exist first")
        cursor = repository.db.question_versions.find({}, {"_id": 0, "questionVersionId": 1})
        async for question in cursor:
            for expert_id in experts:
                result = await repository.db.annotation_assignments.update_one(
                    {
                        "expertId": expert_id,
                        "questionVersionId": question["questionVersionId"],
                        "rubricVersion": args.rubric_version,
                    },
                    {
                        "$setOnInsert": {
                            "assignmentId": str(uuid.uuid4()),
                            "expertId": expert_id,
                            "questionVersionId": question["questionVersionId"],
                            "rubricVersion": args.rubric_version,
                            "status": "assigned",
                            "assignedAt": utc_now(),
                        }
                    },
                    upsert=True,
                )
                created += int(result.upserted_id is not None)
        print(f"Created {created} assignments; existing assignments were preserved.")
    finally:
        await repository.close()


if __name__ == "__main__":
    asyncio.run(run())
