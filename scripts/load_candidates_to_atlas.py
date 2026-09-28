"""Idempotently load immutable babNN.json candidate versions into Atlas."""

from __future__ import annotations

import argparse
import asyncio
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.annotation.repository import MongoAnnotationRepository, utc_now
from app.ingestion.pretest_import import import_directory


async def run() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="output/pretest")
    args = parser.parse_args()
    repository = MongoAnnotationRepository.from_environment()
    if repository is None:
        raise SystemExit("MONGODB_URI and MONGODB_DATABASE must be configured")
    inserted = unchanged = 0
    try:
        await repository.ping()
        await repository.ensure_indexes()
        for record in import_directory(args.source):
            document = record.model_dump(mode="json")
            existing = await repository.db.question_versions.find_one(
                {"questionVersionId": record.questionVersionId}, {"_id": 0, "contentHash": 1}
            )
            if existing:
                if existing["contentHash"] != record.contentHash:
                    raise RuntimeError(
                        f"immutable version conflict for {record.questionVersionId}; create a new content version"
                    )
                unchanged += 1
                continue
            async with repository.client.start_session() as session:
                async with await session.start_transaction():
                    await repository.db.questions.update_one(
                        {"questionId": record.questionId},
                        {
                            "$setOnInsert": {
                                "questionId": record.questionId,
                                "createdAt": utc_now(),
                            },
                            "$max": {"latestContentVersion": record.contentVersion},
                            "$set": {"latestQuestionVersionId": record.questionVersionId},
                        },
                        upsert=True,
                        session=session,
                    )
                    await repository.db.question_versions.insert_one(document, session=session)
                    await repository.db.audit_events.insert_one(
                        {
                            "auditEventId": f"candidate-import:{record.questionVersionId}",
                            "eventType": "candidate.version_imported",
                            "actorId": "system:importer",
                            "metadata": {"questionVersionId": record.questionVersionId},
                            "createdAt": utc_now(),
                        },
                        session=session,
                    )
            inserted += 1
        print(f"Imported {inserted}; unchanged {unchanged}.")
    finally:
        await repository.close()


if __name__ == "__main__":
    asyncio.run(run())
