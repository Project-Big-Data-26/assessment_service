from pathlib import Path

from app.annotation.consensus import apply_adjudication, build_consensus
from app.annotation.contracts import ExpertAnnotationRecord, HeadAnnotation
from app.ingestion.pretest_import import import_bab_file, next_content_version


def annotation(expert: str, cognitive: str, knowledge: str, difficulty: str):
    head = lambda label: HeadAnnotation(label=label, evidence="Bukti proses penyelesaian.")
    return ExpertAnnotationRecord(
        idempotencyKey=f"idem-{expert}-1234",
        contentValid="valid",
        answerKeyStatus="verified",
        verifiedAnswerKey="B",
        minimalSolution="Hitung dan bandingkan hasilnya.",
        mathCognitiveDomain=head(cognitive),
        knowledgeDimension=head(knowledge),
        intendedDifficulty=head(difficulty),
        annotationId=f"annotation-{expert}",
        assignmentId=f"assignment-{expert}",
        expertId=expert,
        questionVersionId="q:v1",
        rubricVersion="math-rubric-3x4x3-v1",
    )


def test_bab_import_is_immutable_and_agent_judgments_are_evidence_not_gold():
    path = Path("output/pretest/kelas1/bab01.json")
    records = import_bab_file(path)
    assert records
    first = records[0]
    assert first.questionVersionId.endswith(":v1")
    assert len(first.contentHash) == 64
    assert first.extractionEvidence["agentDifficulty"] is not None
    dumped = first.model_dump()
    assert "mathCognitiveDomain" not in dumped
    assert "knowledgeDimension" not in dumped
    assert "intendedDifficulty" not in dumped
    assert {option.label for option in first.options} == {"A", "B", "C", "D"}

    unchanged_version, _ = next_content_version(first, {
        "grade": first.grade,
        "stimulus": first.stimulus,
        "stem": first.stem,
        "options": [option.model_dump() for option in first.options],
        "answerKey": first.answerKey,
        "imageRefs": first.imageRefs,
    })
    changed_version, changed_hash = next_content_version(first, {"stem": first.stem + " Direvisi."})
    assert unchanged_version == 1
    assert changed_version == 2
    assert changed_hash != first.contentHash


def test_consensus_handles_unanimous_majority_and_one_one_one_per_head():
    records = [
        annotation("e1", "knowing", "factual", "Easy"),
        annotation("e2", "knowing", "conceptual", "Easy"),
        annotation("e3", "applying", "procedural", "Easy"),
    ]
    result = build_consensus(records)
    assert result.mathCognitiveDomain.status == "majority"
    assert result.mathCognitiveDomain.label == "knowing"
    assert result.intendedDifficulty.status == "unanimous"
    assert result.knowledgeDimension.status == "discussion_required"
    assert result.requiresAdjudication is True
    assert result.eligibleForGold is False

    decided = apply_adjudication(
        result,
        {"knowledgeDimension": "conceptual"},
        insufficient_evidence=False,
    )
    assert decided.knowledgeDimension.status == "adjudicated"
    assert decided.eligibleForGold is True


def test_fourth_expert_can_quarantine_insufficient_evidence():
    result = build_consensus(
        [
            annotation("e1", "knowing", "factual", "Easy"),
            annotation("e2", "applying", "conceptual", "Medium"),
            annotation("e3", "reasoning", "procedural", "Hard"),
        ]
    )
    decided = apply_adjudication(result, {}, insufficient_evidence=True)
    assert decided.eligibleForGold is False
    assert decided.mathCognitiveDomain.status == "quarantined"
    assert decided.knowledgeDimension.label is None
