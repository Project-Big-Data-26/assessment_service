"""Materialize 3-0/2-1 gold or a blind-vote adjudication queue."""

from __future__ import annotations

import argparse
import asyncio
from collections import defaultdict
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.annotation.consensus import build_consensus
from app.annotation.contracts import ExpertAnnotationRecord
from app.annotation.repository import MongoAnnotationRepository, utc_now


async def run() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rubric-version", default="math-rubric-3x4x3-v1")
    args = parser.parse_args()
    repository = MongoAnnotationRepository.from_environment()
    if repository is None:
        raise SystemExit("MONGODB_URI and MONGODB_DATABASE must be configured")
    grouped = defaultdict(list)
    try:
        cursor = repository.db.expert_annotations.find(
            {"rubricVersion": args.rubric_version}, {"_id": 0}
        )
        async for document in cursor:
            grouped[document["questionVersionId"]].append(ExpertAnnotationRecord.model_validate(document))
        ready = pending = incomplete = 0
        for question_version_id, records in grouped.items():
            if len(records) != 3:
                incomplete += 1
                continue
            consensus = build_consensus(records)
            status = "discussion_required" if consensus.requiresAdjudication else "gold_ready"
            decision_id = f"consensus:{args.rubric_version}:{question_version_id}"
            await repository.db.expert_decisions.update_one(
                {"decisionId": decision_id},
                {
                    "$setOnInsert": {
                        "decisionId": decision_id,
                        "questionVersionId": question_version_id,
                        "rubricVersion": args.rubric_version,
                        "initialConsensus": consensus.model_dump(mode="json"),
                        "initialAnnotationIds": [record.annotationId for record in records],
                        "status": status,
                        "createdAt": utc_now(),
                    }
                },
                upsert=True,
            )
            if status == "gold_ready":
                ready += 1
            else:
                pending += 1
        print(f"Gold-ready {ready}; adjudication {pending}; incomplete {incomplete}.")
    finally:
        await repository.close()


if __name__ == "__main__":
    asyncio.run(run())
