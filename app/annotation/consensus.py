"""Consensus and inter-rater agreement computed from initial blind votes."""

from __future__ import annotations

from collections import Counter
from collections.abc import Iterable, Mapping, Sequence

import numpy as np

from .contracts import ConsensusResult, ContentConsensus, ExpertAnnotationRecord, HeadConsensus

HEADS = ("mathCognitiveDomain", "knowledgeDimension", "intendedDifficulty")


def _head_consensus(records: Sequence[ExpertAnnotationRecord], head: str) -> HeadConsensus:
    usable: list[tuple[str, str]] = []
    reasons: list[str] = []
    for record in records:
        value = getattr(record, head)
        if value.abstain or value.label is None:
            reasons.append(f"{record.expertId}:abstain")
        else:
            usable.append((record.expertId, value.label))
    counts = Counter(label for _, label in usable)
    if len(records) != 3 or len(usable) != 3:
        return HeadConsensus(
            status="discussion_required", label=None, voteCounts=dict(counts), reasons=[*reasons, "three_complete_votes_required"]
        )
    label, count = counts.most_common(1)[0]
    if count == 3:
        return HeadConsensus(status="unanimous", label=label, voteCounts=dict(counts))
    if count == 2:
        dissent = [expert_id for expert_id, choice in usable if choice != label]
        return HeadConsensus(status="majority", label=label, voteCounts=dict(counts), dissentingExpertIds=dissent)
    return HeadConsensus(
        status="discussion_required", label=None, voteCounts=dict(counts), reasons=["one_one_one_split"]
    )


def build_consensus(records: Sequence[ExpertAnnotationRecord]) -> ConsensusResult:
    if not records:
        raise ValueError("at least one annotation is required")
    question_ids = {record.questionVersionId for record in records}
    if len(question_ids) != 1:
        raise ValueError("annotations must refer to one question version")
    if len({record.expertId for record in records}) != len(records):
        raise ValueError("each expert may vote once")
    content_reasons: list[str] = []
    if len(records) != 3:
        content_reasons.append("three_complete_reviews_required")
    if any(record.contentValid != "valid" for record in records):
        content_reasons.append("content_not_unanimously_valid")
    if any(record.answerKeyStatus != "verified" for record in records):
        content_reasons.append("answer_key_not_unanimously_verified")
    answer_keys = {record.verifiedAnswerKey for record in records if record.verifiedAnswerKey}
    if len(answer_keys) != 1:
        content_reasons.append("verified_answer_key_disagreement")
    if any(not record.minimalSolution for record in records):
        content_reasons.append("verified_minimal_solution_missing")
    if content_reasons:
        content = ContentConsensus(status="discussion_required", reasons=content_reasons)
    else:
        # Preserve every source solution in provenance; choose deterministically for the serializer.
        canonical = sorted(records, key=lambda item: item.expertId)[0]
        content = ContentConsensus(
            status="eligible",
            verifiedAnswerKey=next(iter(answer_keys)),
            verifiedMinimalSolution=canonical.minimalSolution,
        )
    results = {head: _head_consensus(records, head) for head in HEADS}
    requires = content.status == "discussion_required" or any(
        result.status == "discussion_required" for result in results.values()
    )
    return ConsensusResult(
        questionVersionId=next(iter(question_ids)),
        content=content,
        eligibleForGold=not requires,
        requiresAdjudication=requires,
        **results,
    )


def apply_adjudication(
    consensus: ConsensusResult,
    labels: Mapping[str, str | None],
    *,
    insufficient_evidence: bool,
    content_eligible: bool | None = None,
    verified_answer_key: str | None = None,
    verified_minimal_solution: str | None = None,
) -> ConsensusResult:
    updated = consensus.model_copy(deep=True)
    if updated.content.status == "discussion_required":
        if insufficient_evidence or not content_eligible:
            updated.content = updated.content.model_copy(update={"status": "quarantined"})
        else:
            updated.content = updated.content.model_copy(
                update={
                    "status": "adjudicated",
                    "verifiedAnswerKey": verified_answer_key,
                    "verifiedMinimalSolution": verified_minimal_solution,
                }
            )
    for head in HEADS:
        current = getattr(updated, head)
        if current.status != "discussion_required":
            continue
        label = labels.get(head)
        if insufficient_evidence or label is None:
            replacement = current.model_copy(update={"status": "quarantined", "label": None})
        else:
            replacement = current.model_copy(update={"status": "adjudicated", "label": label})
        setattr(updated, head, replacement)
    updated.requiresAdjudication = False
    updated.eligibleForGold = (
        updated.content.status in {"eligible", "adjudicated"}
        and bool(updated.content.verifiedAnswerKey)
        and bool(updated.content.verifiedMinimalSolution)
        and all(getattr(updated, head).label is not None for head in HEADS)
    )
    return updated


def percent_agreement(vote_matrix: Sequence[Sequence[str | None]]) -> float:
    agreements: list[float] = []
    for row in vote_matrix:
        values = [value for value in row if value is not None]
        if len(values) < 2:
            continue
        pairs = len(values) * (len(values) - 1) / 2
        same = sum(count * (count - 1) / 2 for count in Counter(values).values())
        agreements.append(same / pairs)
    return float(np.mean(agreements)) if agreements else float("nan")


def fleiss_kappa(vote_matrix: Sequence[Sequence[str | None]], labels: Iterable[str]) -> float:
    labels = tuple(labels)
    complete = [row for row in vote_matrix if len(row) >= 2 and all(value in labels for value in row)]
    if not complete:
        return float("nan")
    n_raters = len(complete[0])
    if any(len(row) != n_raters for row in complete):
        raise ValueError("Fleiss kappa requires a constant number of raters")
    counts = np.asarray([[row.count(label) for label in labels] for row in complete], dtype=float)
    observed = np.mean((np.square(counts).sum(axis=1) - n_raters) / (n_raters * (n_raters - 1)))
    category_rates = counts.sum(axis=0) / counts.sum()
    expected = float(np.square(category_rates).sum())
    return 1.0 if expected == 1.0 and observed == 1.0 else float((observed - expected) / (1.0 - expected))


def krippendorff_alpha_nominal(vote_matrix: Sequence[Sequence[str | None]]) -> float:
    rows = [[value for value in row if value is not None] for row in vote_matrix]
    rows = [row for row in rows if len(row) >= 2]
    if not rows:
        return float("nan")
    observed_disagreement = 1.0 - percent_agreement(rows)
    counts = Counter(value for row in rows for value in row)
    total = sum(counts.values())
    if total < 2:
        return float("nan")
    expected_agreement = sum(count * (count - 1) for count in counts.values()) / (total * (total - 1))
    expected_disagreement = 1.0 - expected_agreement
    if expected_disagreement == 0:
        return 1.0 if observed_disagreement == 0 else float("nan")
    return float(1.0 - observed_disagreement / expected_disagreement)
