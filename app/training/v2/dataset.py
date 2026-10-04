"""Silver snapshot construction with deterministic group-aware 70/15/15 splits."""

from __future__ import annotations

import hashlib
import json
import random
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field

from app.classification.v2.contracts import (
    CognitiveDomain,
    IntendedDifficulty,
    KnowledgeDimension,
    ProvenanceStatus,
    QuestionOption,
    V2ClassificationRequest,
)
from app.classification.v2.serializer import INPUT_SCHEMA_VERSION, canonical_json_hash, serialize_question


class TrainingRow(BaseModel):
    model_config = ConfigDict(extra="forbid")

    questionId: str
    questionVersionId: str
    contentVersion: int
    contentHash: str
    sourceGroup: str
    duplicateFamily: str | None = None
    grade: int
    subjectTrack: Literal["regular", "tl"] = "regular"
    topic: str
    subtopic: str | None = None
    questionType: str
    stimulus: str | None = None
    stem: str
    options: list[QuestionOption]
    verifiedMinimalSolution: str
    detectedKko: list[str] = Field(default_factory=list)
    visualTranscript: str | None = None
    mathCognitiveDomain: CognitiveDomain
    knowledgeDimension: KnowledgeDimension
    intendedDifficulty: IntendedDifficulty
    rubricVersion: str
    decisionProvenance: dict[str, Any]

    def inference_request(self) -> V2ClassificationRequest:
        return V2ClassificationRequest(
            questionId=self.questionId,
            contentVersion=self.contentVersion,
            contentHash=self.contentHash,
            grade=self.grade,
            subjectTrack=self.subjectTrack,
            topic=self.topic,
            subtopic=self.subtopic,
            questionType=self.questionType,
            stimulus=self.stimulus,
            stem=self.stem,
            options=self.options,
            verifiedMinimalSolution=self.verifiedMinimalSolution,
            detectedKko=self.detectedKko,
            visualTranscript=self.visualTranscript,
            provenanceStatus=ProvenanceStatus(
                contentQualified=True,
                answerKeyVerified=True,
                solutionVerified=True,
                visualEssential=bool(self.visualTranscript),
                visualTranscriptVerified=bool(self.visualTranscript),
            ),
        )


class SplitEntry(BaseModel):
    questionVersionId: str
    groupId: str
    split: Literal["train", "validation", "test"]


class DatasetSnapshot(BaseModel):
    snapshotId: str
    snapshotHash: str
    inputSchemaVersion: str = INPUT_SCHEMA_VERSION
    seed: int
    splitRatios: dict[str, float]
    rows: list[TrainingRow]
    expansionRows: list[TrainingRow]
    splitManifest: list[SplitEntry]
    splitManifestHash: str
    testUnlockStatus: Literal["locked", "eligible_to_unlock"]
    expansionHash: str | None = None
    researchOnly: bool = False
    labelProvenance: str = "ai_silver"
    gateFailures: list[str] = Field(default_factory=list)
    exclusionSummary: dict[str, int] = Field(default_factory=dict)
    trainingGrades: list[int] = Field(default_factory=lambda: list(range(1, 7)))
    requiredGradeTracks: list[str] = Field(default_factory=list)
    rubricFamily: str | None = None


def normalized_duplicate_text(row: TrainingRow) -> str:
    option_texts = sorted(option.text for option in row.options)
    value = " ".join(filter(None, [row.stimulus, row.stem, *option_texts]))
    value = unicodedata.normalize("NFC", value).casefold()
    return re.sub(r"\s+", " ", value).strip()


def exact_content_family(row: TrainingRow) -> str:
    return hashlib.sha256(normalized_duplicate_text(row).encode("utf-8")).hexdigest()[:20]


def _trigrams(value: str) -> set[str]:
    compact = re.sub(r"\s+", " ", value)
    return {compact[index : index + 3] for index in range(max(0, len(compact) - 2))}


def assign_near_duplicate_families(rows: list[TrainingRow], threshold: float = 0.90) -> dict[str, str]:
    """Cluster within source group using transitive Jaccard similarity."""
    parents = list(range(len(rows)))

    def find(index: int) -> int:
        while parents[index] != index:
            parents[index] = parents[parents[index]]
            index = parents[index]
        return index

    def union(left: int, right: int) -> None:
        left_root, right_root = find(left), find(right)
        if left_root != right_root:
            parents[right_root] = left_root

    shingles = []
    for index, row in enumerate(rows):
        shingles.append(_trigrams(normalized_duplicate_text(row)))
    for left in range(len(rows)):
        for right in range(left + 1, len(rows)):
            smaller = min(len(shingles[left]), len(shingles[right]))
            larger = max(len(shingles[left]), len(shingles[right]))
            if larger and smaller / larger < threshold:
                continue
            union_size = len(shingles[left] | shingles[right])
            similarity = len(shingles[left] & shingles[right]) / union_size if union_size else 1.0
            if similarity >= threshold:
                union(left, right)
    members_by_root: dict[int, list[str]] = defaultdict(list)
    for index, row in enumerate(rows):
        members_by_root[find(index)].append(row.questionVersionId)
    family_by_root = {
        root: "family-" + hashlib.sha256("|".join(sorted(members)).encode()).hexdigest()[:12]
        for root, members in members_by_root.items()
    }
    return {row.questionVersionId: family_by_root[find(index)] for index, row in enumerate(rows)}


def _leakage_safe_group_ids(rows: list[TrainingRow], family_map: dict[str, str]) -> dict[str, str]:
    """Union rows sharing a source, stimulus, exact, or near-duplicate family."""
    parents = list(range(len(rows)))

    def find(index: int) -> int:
        while parents[index] != index:
            parents[index] = parents[parents[index]]
            index = parents[index]
        return index

    def union(left: int, right: int) -> None:
        left_root, right_root = find(left), find(right)
        if left_root != right_root:
            parents[right_root] = left_root

    first_by_source: dict[str, int] = {}
    first_by_family: dict[str, int] = {}
    first_by_stimulus: dict[str, int] = {}
    for index, row in enumerate(rows):
        family = row.duplicateFamily or family_map[row.questionVersionId]
        if row.sourceGroup in first_by_source:
            union(index, first_by_source[row.sourceGroup])
        else:
            first_by_source[row.sourceGroup] = index
        if family in first_by_family:
            union(index, first_by_family[family])
        else:
            first_by_family[family] = index
        if row.stimulus:
            normalized_stimulus = re.sub(
                r"\s+",
                " ",
                unicodedata.normalize("NFC", row.stimulus).casefold(),
            ).strip()
            stimulus_family = hashlib.sha256(
                normalized_stimulus.encode("utf-8")
            ).hexdigest()[:20]
            if stimulus_family in first_by_stimulus:
                union(index, first_by_stimulus[stimulus_family])
            else:
                first_by_stimulus[stimulus_family] = index
    members: dict[int, list[str]] = defaultdict(list)
    for index, row in enumerate(rows):
        members[find(index)].append(row.questionVersionId)
    labels = {
        root: "group-" + hashlib.sha256("|".join(sorted(ids)).encode()).hexdigest()[:16]
        for root, ids in members.items()
    }
    return {row.questionVersionId: labels[find(index)] for index, row in enumerate(rows)}


def _label_counts(rows: list[TrainingRow]) -> Counter[str]:
    values: Counter[str] = Counter()
    for row in rows:
        values.update(
            (
                f"cognitive={row.mathCognitiveDomain.value}",
                f"knowledge={row.knowledgeDimension.value}",
                f"difficulty={row.intendedDifficulty.value}",
                f"grade={row.grade}",
            )
        )
        if row.subjectTrack == "tl":
            values.update((f"gradeTrack={row.grade}:{row.subjectTrack}",))
    return values


def deterministic_group_split(
    rows: list[TrainingRow], *, seed: int = 42
) -> list[SplitEntry]:
    if not rows:
        return []
    rows = sorted(rows, key=lambda item: item.questionVersionId)
    family_map = assign_near_duplicate_families(rows)
    group_map = _leakage_safe_group_ids(rows, family_map)
    groups: dict[str, list[TrainingRow]] = defaultdict(list)
    for row in rows:
        groups[group_map[row.questionVersionId]].append(row)
    rng = random.Random(seed)
    group_items = list(groups.items())
    rng.shuffle(group_items)
    group_items.sort(key=lambda item: len(item[1]), reverse=True)
    targets = {"train": 0.70 * len(rows), "validation": 0.15 * len(rows), "test": 0.15 * len(rows)}
    global_labels = _label_counts(rows)
    assigned: dict[str, list[TrainingRow]] = {name: [] for name in targets}
    split_groups: dict[str, str] = {}
    for group_id, members in group_items:
        group_labels = _label_counts(members)
        scores: dict[str, float] = {}
        for split, target in targets.items():
            remaining_ratio = (target - len(assigned[split])) / max(target, 1.0)
            label_need = 0.0
            current_labels = _label_counts(assigned[split])
            ratio = {"train": 0.70, "validation": 0.15, "test": 0.15}[split]
            represented = 0
            for label, count_in_group in group_labels.items():
                if not count_in_group:
                    continue
                desired = global_labels[label] * ratio
                label_need += max(0.0, desired - current_labels[label]) / max(desired, 1.0)
                represented += 1
            label_need /= max(represented, 1)
            overflow = max(0.0, len(assigned[split]) + len(members) - target) / max(target, 1.0)
            scores[split] = remaining_ratio + 0.20 * label_need - 5.0 * overflow
        priority = {"train": 2, "validation": 1, "test": 0}
        chosen = max(scores, key=lambda name: (scores[name], priority[name]))
        assigned[chosen].extend(members)
        split_groups[group_id] = chosen
    return [
        SplitEntry(
            questionVersionId=row.questionVersionId,
            groupId=group_map[row.questionVersionId],
            split=split_groups[group_map[row.questionVersionId]],
        )
        for row in rows
    ]


def validate_split_minimums(
    rows: list[TrainingRow],
    manifest: list[SplitEntry],
    *,
    minimum_train_per_class: int = 30,
    minimum_evaluation_per_class: int = 15,
    required_grades: tuple[int, ...] = (1, 2, 3, 4, 5, 6),
    required_grade_tracks: tuple[str, ...] = (),
) -> list[str]:
    by_id = {row.questionVersionId: row for row in rows}
    failures: list[str] = []
    dimensions = {
        "mathCognitiveDomain": tuple(item.value for item in CognitiveDomain),
        "knowledgeDimension": tuple(item.value for item in KnowledgeDimension),
        "intendedDifficulty": tuple(item.value for item in IntendedDifficulty),
    }
    for split in ("train", "validation", "test"):
        selected = [by_id[entry.questionVersionId] for entry in manifest if entry.split == split]
        minimum = (
            minimum_train_per_class if split == "train" else minimum_evaluation_per_class
        )
        for field, labels in dimensions.items():
            counts = Counter(getattr(row, field).value for row in selected)
            for label in labels:
                if counts[label] < minimum:
                    failures.append(f"{split}:{field}:{label}={counts[label]}<{minimum}")
        grade_counts = Counter(row.grade for row in selected)
        for grade in required_grades:
            if grade_counts[grade] == 0:
                failures.append(f"{split}:grade:{grade}=0<1")
        track_counts = Counter(f"{row.grade}:{row.subjectTrack}" for row in selected)
        for grade_track in required_grade_tracks:
            if track_counts[grade_track] == 0:
                failures.append(f"{split}:gradeTrack:{grade_track}=0<1")
    return failures


def validate_split_integrity(
    rows: list[TrainingRow], manifest: list[SplitEntry]
) -> list[str]:
    failures: list[str] = []
    expected_ids = {row.questionVersionId for row in rows}
    manifest_ids = [entry.questionVersionId for entry in manifest]
    counts = Counter(manifest_ids)
    for question_id, count in sorted(counts.items()):
        if count > 1:
            failures.append(f"split_manifest_duplicate:{question_id}={count}")
    for question_id in sorted(expected_ids - set(manifest_ids)):
        failures.append(f"split_manifest_missing:{question_id}")
    for question_id in sorted(set(manifest_ids) - expected_ids):
        failures.append(f"split_manifest_unknown:{question_id}")
    if failures:
        return failures

    split_by_id = {entry.questionVersionId: entry.split for entry in manifest}
    family_map = assign_near_duplicate_families(rows)
    leakage_groups = _leakage_safe_group_ids(rows, family_map)
    splits_by_group: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        splits_by_group[leakage_groups[row.questionVersionId]].add(
            split_by_id[row.questionVersionId]
        )
    for group_id, splits in sorted(splits_by_group.items()):
        if len(splits) > 1:
            failures.append(
                f"split_leakage:{group_id}={','.join(sorted(splits))}"
            )
    return failures


def validate_test_minimums(
    rows: list[TrainingRow], manifest: list[SplitEntry], minimum: int = 15
) -> list[str]:
    """Backward-compatible validation/test gate used by older callers."""
    failures = validate_split_minimums(
        rows,
        manifest,
        minimum_train_per_class=0,
        minimum_evaluation_per_class=minimum,
        required_grades=(),
    )
    return [failure for failure in failures if not failure.startswith("train:")]


def build_snapshot(
    rows: list[TrainingRow],
    *,
    snapshot_id: str,
    seed: int = 42,
    minimum_per_class: int = 15,
    minimum_train_per_class: int = 30,
    required_grades: tuple[int, ...] = (1, 2, 3, 4, 5, 6),
    research_only: bool = False,
    label_provenance: str = "ai_silver",
    exclusion_summary: dict[str, int] | None = None,
    training_grades: tuple[int, ...] = (1, 2, 3, 4, 5, 6),
    required_grade_tracks: tuple[str, ...] = (),
    rubric_family: str | None = None,
) -> DatasetSnapshot:
    if (not training_grades or len(set(training_grades)) != len(training_grades)
            or any(grade not in range(1, 13) for grade in training_grades)):
        raise ValueError("training_grades must be distinct grades 1-12")
    if len({row.questionVersionId for row in rows}) != len(rows):
        raise ValueError("duplicate questionVersionId in training rows")
    main = sorted(
        (row for row in rows if row.grade in training_grades), key=lambda item: item.questionVersionId
    )
    expansion = sorted(
        (row for row in rows if row.grade not in training_grades), key=lambda item: item.questionVersionId
    )
    manifest = deterministic_group_split(main, seed=seed)
    failures = validate_split_minimums(
        main,
        manifest,
        minimum_train_per_class=minimum_train_per_class,
        minimum_evaluation_per_class=minimum_per_class,
        required_grades=required_grades,
        required_grade_tracks=required_grade_tracks,
    )
    failures.extend(validate_split_integrity(main, manifest))
    snapshot_payload = [row.model_dump(mode="json") for row in sorted(main, key=lambda item: item.questionVersionId)]
    manifest_payload = [entry.model_dump(mode="json") for entry in manifest]
    return DatasetSnapshot(
        snapshotId=snapshot_id,
        snapshotHash=canonical_json_hash(snapshot_payload),
        expansionHash=canonical_json_hash([row.model_dump(mode="json") for row in expansion]),
        seed=seed,
        splitRatios={"train": 0.70, "validation": 0.15, "test": 0.15},
        rows=main,
        expansionRows=expansion,
        splitManifest=manifest,
        splitManifestHash=canonical_json_hash(manifest_payload),
        testUnlockStatus="eligible_to_unlock" if not failures else "locked",
        researchOnly=research_only or bool(failures),
        labelProvenance=label_provenance,
        gateFailures=failures,
        exclusionSummary=exclusion_summary or {},
        trainingGrades=list(training_grades),
        requiredGradeTracks=list(required_grade_tracks),
        rubricFamily=rubric_family,
    )


def save_snapshot(snapshot: DatasetSnapshot, path: str | Path) -> None:
    destination = Path(path)
    if destination.exists():
        raise FileExistsError(f"refusing to overwrite immutable snapshot: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(snapshot.model_dump_json(indent=2), encoding="utf-8")


def serialized_training_examples(
    snapshot: DatasetSnapshot, split: str, *, representation: str = "kko"
) -> list[dict[str, Any]]:
    split_ids = {entry.questionVersionId for entry in snapshot.splitManifest if entry.split == split}
    return [
        {
            "questionVersionId": row.questionVersionId,
            "grade": row.grade,
            "subjectTrack": row.subjectTrack,
            "text": serialize_question(row.inference_request(), representation=representation),
            "mathCognitiveDomain": row.mathCognitiveDomain.value,
            "knowledgeDimension": row.knowledgeDimension.value,
            "intendedDifficulty": row.intendedDifficulty.value,
        }
        for row in snapshot.rows
        if row.questionVersionId in split_ids
    ]
