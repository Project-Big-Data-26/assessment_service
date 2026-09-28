"""Freeze qualified decisions into a hash-locked model snapshot and split manifest."""

from __future__ import annotations

import argparse
import asyncio
from collections import Counter
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.annotation.repository import MongoAnnotationRepository
from app.classification.v2.contracts import QuestionOption
from app.classification.v2.serializer import canonical_json_hash
from app.classification.v2.kko import detect_kko
from app.annotation.repository import utc_now
from app.training.v2.dataset import GoldTrainingRow, build_snapshot, save_snapshot


def resolved_key_solution(decision: dict) -> tuple[str | None, str | None]:
    if decision["status"] == "gold_ready":
        content = decision["initialConsensus"]["content"]
        return content.get("verifiedAnswerKey"), content.get("verifiedMinimalSolution")
    if decision["status"] == "adjudicated":
        final = decision.get("decision", {})
        return final.get("verifiedAnswerKey"), final.get("verifiedMinimalSolution")
    return None, None


async def ensure_qualified_content_version(repository, question: dict, decision: dict) -> dict:
    existing_id = decision.get("goldQuestionVersionId")
    if existing_id:
        existing = await repository.db.question_versions.find_one(
            {"questionVersionId": existing_id}, {"_id": 0}
        )
        if existing:
            return existing
    key, solution = resolved_key_solution(decision)
    if not key or not solution:
        return question
    content = {
        "grade": question["grade"],
        "stimulus": question.get("stimulus"),
        "stem": question["stem"],
        "options": question["options"],
        "answerKey": key,
        "verifiedMinimalSolution": solution,
        "imageRefs": question.get("imageRefs", []),
        "visualTranscript": question.get("visualTranscript"),
    }
    digest = canonical_json_hash(content)
    equivalent = await repository.db.question_versions.find_one(
        {"questionId": question["questionId"], "contentHash": digest}, {"_id": 0}
    )
    if equivalent:
        qualified = equivalent
    else:
        master = await repository.db.questions.find_one(
            {"questionId": question["questionId"]}, {"_id": 0, "latestContentVersion": 1}
        )
        version = int((master or {}).get("latestContentVersion", question["contentVersion"])) + 1
        qualified = {
            **question,
            "questionVersionId": f"{question['questionId']}:v{version}",
            "contentVersion": version,
            "contentHash": digest,
            "answerKey": key,
            "verifiedMinimalSolution": solution,
            "qualificationStatus": "eligible",
            "qualificationReasons": [],
            "sourceQuestionVersionId": question["questionVersionId"],
            "qualifiedAt": utc_now(),
        }
        async with repository.client.start_session() as session:
            async with await session.start_transaction():
                await repository.db.question_versions.insert_one(qualified, session=session)
                await repository.db.questions.update_one(
                    {"questionId": question["questionId"]},
                    {
                        "$set": {
                            "latestContentVersion": version,
                            "latestQuestionVersionId": qualified["questionVersionId"],
                        }
                    },
                    session=session,
                )
        qualified.pop("_id", None)
    await repository.db.expert_decisions.update_one(
        {"decisionId": decision["decisionId"]},
        {"$set": {"goldQuestionVersionId": qualified["questionVersionId"]}},
    )
    return qualified


def gold_from_documents(question: dict, decision: dict) -> GoldTrainingRow | None:
    if "butuh_gambar" in question.get("extractionFlags", []) and not question.get("visualTranscript"):
        # IndoBERT is text-only; a private preview lets experts review content but
        # does not become model input. Transcription is mandatory for snapshot v1.
        return None
    consensus = decision["initialConsensus"]
    if decision["status"] == "gold_ready":
        if not consensus.get("eligibleForGold"):
            return None
        labels = {head: consensus[head]["label"] for head in ("mathCognitiveDomain", "knowledgeDimension", "intendedDifficulty")}
        solution = consensus["content"]["verifiedMinimalSolution"]
        key = consensus["content"]["verifiedAnswerKey"]
    elif decision["status"] == "adjudicated":
        final = decision.get("decision", {})
        if final.get("insufficientEvidence") or not final.get("contentEligible"):
            return None
        labels = {head: final.get(head) for head in ("mathCognitiveDomain", "knowledgeDimension", "intendedDifficulty")}
        solution = final.get("verifiedMinimalSolution")
        key = final.get("verifiedAnswerKey")
    else:
        return None
    if not all(labels.values()) or not solution or not key:
        return None
    if question.get("stimulus"):
        source_group = "stimulus:" + canonical_json_hash({"stimulus": question["stimulus"]})[:20]
    else:
        source_group = "|".join(
            map(str, (question["book"], question["chapterNumber"], question["sourcePage"], question["sourceSection"]))
        )
    return GoldTrainingRow(
        questionId=question["questionId"],
        questionVersionId=question["questionVersionId"],
        contentVersion=question["contentVersion"],
        contentHash=question["contentHash"],
        sourceGroup=source_group,
        grade=question["grade"],
        topic=question["chapter"],
        subtopic=question.get("subchapter"),
        questionType="multiple_choice",
        stimulus=question.get("stimulus"),
        stem=question["stem"],
        options=[QuestionOption.model_validate(option) for option in question["options"]],
        verifiedMinimalSolution=solution,
        detectedKko=detect_kko(question.get("stimulus"), question["stem"]),
        visualTranscript=question.get("visualTranscript"),
        rubricVersion=decision["rubricVersion"],
        decisionProvenance={
            "decisionId": decision["decisionId"],
            "kind": decision["status"],
            "initialAnnotationIds": decision["initialAnnotationIds"],
            "verifiedAnswerKey": key,
        },
        **labels,
    )


async def run() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot-id", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--minimum-per-class", type=int, default=15)
    args = parser.parse_args()
    repository = MongoAnnotationRepository.from_environment()
    if repository is None:
        raise SystemExit("MONGODB_URI and MONGODB_DATABASE must be configured")
    rows = []
    excluded = Counter()
    try:
        cursor = repository.db.expert_decisions.find(
            {"status": {"$in": ["gold_ready", "adjudicated"]}}, {"_id": 0}
        )
        async for decision in cursor:
            question = await repository.db.question_versions.find_one(
                {"questionVersionId": decision["questionVersionId"]}, {"_id": 0}
            )
            if question:
                question = await ensure_qualified_content_version(repository, question, decision)
            row = gold_from_documents(question, decision) if question else None
            if row:
                rows.append(row)
            elif not question:
                excluded["question_version_missing"] += 1
            elif "butuh_gambar" in question.get("extractionFlags", []) and not question.get("visualTranscript"):
                excluded["essential_visual_transcript_missing"] += 1
            else:
                excluded["incomplete_or_quarantined_decision"] += 1
        snapshot = build_snapshot(
            rows,
            snapshot_id=args.snapshot_id,
            seed=42,
            minimum_per_class=args.minimum_per_class,
            exclusion_summary=dict(excluded),
        )
        save_snapshot(snapshot, args.output)
        existing_snapshot = await repository.db.dataset_snapshots.find_one(
            {"snapshotId": snapshot.snapshotId}, {"_id": 0, "snapshotHash": 1}
        )
        if existing_snapshot and existing_snapshot["snapshotHash"] != snapshot.snapshotHash:
            raise RuntimeError("snapshot ID already exists with a different immutable hash")
        if not existing_snapshot:
            await repository.db.dataset_snapshots.insert_one(snapshot.model_dump(mode="json"))
        print(
            f"Frozen {len(snapshot.rows)} SD rows and {len(snapshot.expansionRows)} expansion rows; "
            f"excluded={dict(excluded)}; test={snapshot.testUnlockStatus}."
        )
    finally:
        await repository.close()


if __name__ == "__main__":
    asyncio.run(run())
