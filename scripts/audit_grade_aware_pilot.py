"""Audit and cryptographically lock a blind silver pilot before expansion."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.llm.silver import (  # noqa: E402
    SUPPORTED_SILVER_GRADES,
    build_silver_prompt,
    rubric_file_hash,
    requested_runs_for,
    silver_rubric,
)

HEADS = ("mathCognitiveDomain", "knowledgeDimension", "intendedDifficulty")
FORBIDDEN_BLIND_TEXT = ("PREDIKSI INDOBERT", "tingkat_kesulitan", "cognitive_level")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def input_hash(item: dict) -> str:
    encoded = json.dumps(item, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def audit(
    source: Path,
    checkpoint: Path,
    *,
    grade: int,
    boundary_analysis: Path | None = None,
) -> dict:
    questions = json.loads(source.read_text(encoding="utf-8"))
    silver = json.loads(checkpoint.read_text(encoding="utf-8"))
    track = silver.get("subjectTrack", "regular")
    rubric = silver_rubric(grade, track=track)
    records_by_id = silver.get("items") or {}
    question_by_id = {str(item["_id"]): item for item in questions}
    missing_ids = sorted(set(question_by_id) - set(records_by_id))
    extra_ids = sorted(set(records_by_id) - set(question_by_id))
    records = [
        records_by_id[question_id]
        for question_id in question_by_id
        if question_id in records_by_id
    ]

    source_hash = sha256_file(source)
    checkpoint_hash = sha256_file(checkpoint)
    input_hash_failures = sorted(
        question_id
        for question_id, item in question_by_id.items()
        if question_id in records_by_id
        and records_by_id[question_id].get("inputHash") != input_hash(item)
    )
    checkpoint_source_matches = silver.get("sourceHash") == source_hash
    versions_match = bool(
        silver.get("promptVersion") == rubric.prompt_version
        and silver.get("rubricVersion") == rubric.version
        and silver.get("rubricHash") == rubric_file_hash(grade, track=track)
        and silver.get("sourceGrade", grade) == grade
    )

    rendered = [build_silver_prompt(item, grade=grade, track=track) for item in questions]
    leakage = sorted(
        token
        for token in FORBIDDEN_BLIND_TEXT
        if any(token.casefold() in prompt.casefold() for prompt in rendered)
    )
    three_success = 0
    insufficient = len(missing_ids)
    evidence_failures: list[str] = []
    distributions = {head: Counter() for head in HEADS}
    for record in records:
        runs = record.get("runs") or []
        if sum(run.get("status") == "success" for run in runs) == 3:
            three_success += 1
        aggregate = record.get("aggregate") or {}
        if (
            not aggregate.get("eligibleForTraining")
            or aggregate.get("contentStatus") != "valid"
        ):
            insufficient += 1
        for head in HEADS:
            label = (aggregate.get("heads", {}).get(head) or {}).get("label")
            if label:
                distributions[head][label] += 1
                if aggregate.get("adjudicated"):
                    decision = (
                        (record.get("adjudication") or {}).get("output") or {}
                    ).get(head) or {}
                    consistent = bool(
                        decision.get("label") == label
                        and decision.get("evidenceSpans")
                        and decision.get("rationale")
                    )
                else:
                    decisions = [
                        ((run.get("output") or {}).get(head) or {})
                        for run in runs
                        if run.get("status") == "success"
                    ]
                    consistent = bool(
                        len(decisions) == requested_runs_for(silver, record)
                        and all(
                            decision.get("label") == label
                            and decision.get("evidenceSpans")
                            and decision.get("rationale")
                            for decision in decisions
                        )
                    )
                if not consistent:
                    evidence_failures.append(
                        f"{record.get('questionId')}:{head}:inconsistent_label_evidence"
                    )
        for run in runs:
            if run.get("status") != "success":
                continue
            output = run.get("output") or {}
            if not run.get("promptHash") or not run.get("responseHash"):
                evidence_failures.append(
                    f"{record.get('questionId')}:missing_prompt_or_response_hash"
                )
            if not output.get("verifiedMinimalSolution"):
                evidence_failures.append(f"{record.get('questionId')}:missing_solution")
            if (
                output.get("answerKeyStatus") != "verified"
                or not output.get("verifiedAnswerKey")
            ):
                evidence_failures.append(
                    f"{record.get('questionId')}:answer_key_not_verified"
                )
            difficulty = output.get("intendedDifficulty") or {}
            if difficulty.get("action") == "classify" and not difficulty.get("profile"):
                evidence_failures.append(
                    f"{record.get('questionId')}:missing_difficulty_profile"
                )
        adjudication = record.get("adjudication") or {}
        if adjudication.get("status") == "success":
            output = adjudication.get("output") or {}
            if not adjudication.get("promptHash") or not adjudication.get("responseHash"):
                evidence_failures.append(
                    f"{record.get('questionId')}:adjudication_missing_hash"
                )
            if not output.get("verifiedMinimalSolution"):
                evidence_failures.append(
                    f"{record.get('questionId')}:adjudication_missing_solution"
                )
            if (
                output.get("answerKeyStatus") != "verified"
                or not output.get("verifiedAnswerKey")
            ):
                evidence_failures.append(
                    f"{record.get('questionId')}:adjudication_answer_key_not_verified"
                )
            difficulty = output.get("intendedDifficulty") or {}
            if difficulty.get("action") == "classify" and not difficulty.get("profile"):
                evidence_failures.append(
                    f"{record.get('questionId')}:adjudication_missing_difficulty_profile"
                )

    difficulty = distributions["intendedDifficulty"]
    eligible = max(sum(difficulty.values()), 1)
    dominant_share = max(difficulty.values(), default=0) / eligible
    boundary_reasons: list[str] = []
    if dominant_share > 0.90:
        boundary_reasons.append(f"dominant_difficulty_share={dominant_share:.3f}>0.90")
    for label in ("Medium", "Hard"):
        if difficulty[label] == 0:
            boundary_reasons.append(f"difficulty_{label}_absent")

    boundary_accepted = False
    boundary_rationale = None
    if boundary_analysis is not None:
        analysis = json.loads(boundary_analysis.read_text(encoding="utf-8"))
        boundary_accepted = bool(
            analysis.get("accepted") is True
            and analysis.get("checkpointSha256") == checkpoint_hash
            and str(analysis.get("rationale") or "").strip()
            and str(analysis.get("reviewedBy") or "").strip()
            and str(analysis.get("createdAt") or "").strip()
        )
        boundary_rationale = analysis.get("rationale")

    expected_count = len(questions)
    successful_share = three_success / max(expected_count, 1)
    insufficient_share = insufficient / max(expected_count, 1)
    gates = {
        "allExpectedItemsPresent": not missing_ids and not extra_ids,
        "threeSuccessfulRunsAtLeast90Percent": successful_share >= 0.90,
        "insufficientOrAbstainedBelow10Percent": insufficient_share < 0.10,
        "blindPromptLeakageAbsent": not leakage,
        "checkpointSourceAndInputsMatch": bool(
            checkpoint_source_matches and not input_hash_failures
        ),
        "promptAndRubricVersionMatch": versions_match,
        "requiredEvidenceComplete": not evidence_failures,
        "boundaryAnalysisClear": not boundary_reasons or boundary_accepted,
    }
    return {
        "schemaVersion": "grade-aware-pilot-audit-v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "source": source.as_posix(),
        "sourceSha256": source_hash,
        "checkpoint": checkpoint.as_posix(),
        "checkpointSha256": checkpoint_hash,
        "checkpointLockedByAudit": True,
        "grade": grade,
        "subjectTrack": track,
        "promptVersion": silver.get("promptVersion"),
        "expectedPromptVersion": rubric.prompt_version,
        "rubricVersion": silver.get("rubricVersion"),
        "expectedRubricVersion": rubric.version,
        "rubricHash": silver.get("rubricHash"),
        "expectedRubricHash": rubric_file_hash(grade, track=track),
        "expectedItemCount": expected_count,
        "itemCount": len(records),
        "missingQuestionIds": missing_ids,
        "extraQuestionIds": extra_ids,
        "inputHashFailures": input_hash_failures,
        "threeSuccessfulRuns": three_success,
        "threeSuccessfulRunsShare": successful_share,
        "insufficientOrAbstained": insufficient,
        "insufficientOrAbstainedShare": insufficient_share,
        "labelDistributions": {
            head: dict(values) for head, values in distributions.items()
        },
        "dominantDifficultyShare": dominant_share,
        "blindLeakageTokens": leakage,
        "evidenceFailures": evidence_failures,
        "boundaryAnalysisRequired": bool(boundary_reasons),
        "boundaryAnalysisReasons": boundary_reasons,
        "boundaryAnalysisAccepted": boundary_accepted,
        "boundaryAnalysisRationale": boundary_rationale,
        "gates": gates,
        "readyForExpansion": all(gates.values()),
    }


def markdown(report: dict) -> str:
    status = "LOLOS" if report["readyForExpansion"] else "BERHENTI UNTUK ANALISIS"
    lines = [
        "# Audit Pilot Klasifikasi Grade-Aware",
        "",
        f"Status: **{status}**",
        "",
        f"- Item diproses: {report['itemCount']}/{report['expectedItemCount']}",
        f"- Tiga run sukses: {report['threeSuccessfulRunsShare']:.1%}",
        f"- Insufficient/abstain: {report['insufficientOrAbstainedShare']:.1%}",
        f"- Dominasi difficulty: {report['dominantDifficultyShare']:.1%}",
        f"- Distribusi difficulty: `{json.dumps(report['labelDistributions']['intendedDifficulty'], ensure_ascii=False)}`",
        "",
        "## Gate",
        "",
    ]
    lines.extend(
        f"- {'PASS' if passed else 'FAIL'} -- `{name}`"
        for name, passed in report["gates"].items()
    )
    if report["boundaryAnalysisReasons"]:
        lines.extend(["", "## Boundary analysis wajib", ""])
        lines.extend(f"- `{reason}`" for reason in report["boundaryAnalysisReasons"])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--grade", type=int, choices=SUPPORTED_SILVER_GRADES, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument(
        "--boundary-analysis",
        type=Path,
        help=(
            "Optional JSON with accepted=true, checkpointSha256, and a rationale. "
            "reviewedBy and createdAt are also required. It documents a natural "
            "boundary and never changes labels."
        ),
    )
    args = parser.parse_args()
    destination = args.output_dir.resolve()
    report_path = destination / "pilot_audit.json"
    markdown_path = destination / "PILOT_AUDIT.md"
    if report_path.exists() or markdown_path.exists():
        raise FileExistsError("refusing to overwrite immutable pilot audit")
    report = audit(
        args.source.resolve(),
        args.checkpoint.resolve(),
        grade=args.grade,
        boundary_analysis=(args.boundary_analysis.resolve() if args.boundary_analysis else None),
    )
    destination.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    markdown_path.write_text(markdown(report), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["readyForExpansion"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
