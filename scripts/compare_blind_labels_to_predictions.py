"""Compare locked blind silver labels with model predictions without another LLM call."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

HEADS = ("mathCognitiveDomain", "knowledgeDimension", "intendedDifficulty")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def locked_evidence(record: dict[str, Any], head: str, label: str) -> dict[str, Any]:
    adjudication = record.get("adjudication") or {}
    if adjudication.get("status") == "success":
        decision = (adjudication.get("output") or {}).get(head) or {}
        if decision.get("label") == label:
            return {
                "source": "adjudication",
                "evidenceSpans": decision.get("evidenceSpans") or [],
                "rationale": decision.get("rationale"),
                "profile": decision.get("profile"),
            }
    for run in record.get("runs") or []:
        if run.get("status") != "success":
            continue
        decision = (run.get("output") or {}).get(head) or {}
        if decision.get("label") == label:
            return {
                "source": f"blind_run_{run.get('runIndex')}",
                "evidenceSpans": decision.get("evidenceSpans") or [],
                "rationale": decision.get("rationale"),
                "profile": decision.get("profile"),
            }
    return {"source": None, "evidenceSpans": [], "rationale": None, "profile": None}


def compare(
    silver: dict[str, Any],
    predictions: dict[str, Any],
    audit: dict[str, Any],
    *,
    silver_hash: str,
    predictions_hash: str,
    audit_hash: str,
) -> dict[str, Any]:
    if audit.get("checkpointLockedByAudit") is not True:
        raise ValueError("pilot audit did not lock the blind checkpoint")
    if audit.get("checkpointSha256") != silver_hash:
        raise ValueError("silver checkpoint changed after the blind audit lock")
    gates = audit.get("gates") or {}
    if not gates.get("blindPromptLeakageAbsent"):
        raise ValueError("blind prompt leakage gate did not pass")
    if not gates.get("checkpointSourceAndInputsMatch"):
        raise ValueError("blind checkpoint provenance gate did not pass")
    prediction_created = predictions.get("createdAt")
    audit_created = audit.get("generatedAt")
    if not prediction_created or not audit_created:
        raise ValueError("prediction and audit timestamps are required")
    if parse_time(prediction_created) < parse_time(audit_created):
        raise ValueError("predictions must be generated after blind labels are locked")

    prediction_by_id = {
        str(item["questionId"]): item for item in predictions.get("items") or []
    }
    items: list[dict[str, Any]] = []
    agreement = {head: Counter() for head in HEADS}
    confusion = {head: Counter() for head in HEADS}
    missing_predictions: list[str] = []
    eligible_records = 0
    for question_id, record in (silver.get("items") or {}).items():
        aggregate = record.get("aggregate") or {}
        if not aggregate.get("eligibleForTraining"):
            continue
        eligible_records += 1
        prediction_record = prediction_by_id.get(str(question_id))
        if prediction_record is None:
            missing_predictions.append(str(question_id))
            continue
        prediction = prediction_record.get("prediction") or prediction_record
        compared_heads: dict[str, Any] = {}
        for head in HEADS:
            silver_label = (aggregate.get("heads", {}).get(head) or {}).get("label")
            predicted_head = prediction.get(head) or {}
            predicted_label = predicted_head.get("label")
            agrees = bool(silver_label is not None and predicted_label == silver_label)
            agreement[head]["agree" if agrees else "disagree"] += 1
            confusion[head][f"{silver_label}->{predicted_label}"] += 1
            compared_heads[head] = {
                "blindSilverLabel": silver_label,
                "modelLabel": predicted_label,
                "agreement": agrees,
                "modelProbabilities": predicted_head.get("probabilities") or {},
                "modelAction": predicted_head.get("action"),
                "blindEvidence": locked_evidence(record, head, silver_label),
            }
        items.append(
            {
                "questionId": question_id,
                "blindAggregateStatus": {
                    head: (aggregate.get("heads", {}).get(head) or {}).get("status")
                    for head in HEADS
                },
                "heads": compared_heads,
                "reviewRequired": True,
            }
        )

    compared_count = len(items)
    summary = {
        "eligibleBlindItems": eligible_records,
        "comparedItems": compared_count,
        "missingPredictionIds": missing_predictions,
        "agreement": {
            head: {
                **dict(counts),
                "rate": counts["agree"] / max(compared_count, 1),
            }
            for head, counts in agreement.items()
        },
        "confusion": {head: dict(counts) for head, counts in confusion.items()},
    }
    return {
        "schemaVersion": "blind-silver-model-disagreement-v1",
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "researchOnly": True,
        "reviewRequired": True,
        "comparisonPerformedAfterBlindLock": True,
        "silverCheckpointSha256": silver_hash,
        "predictionsSha256": predictions_hash,
        "pilotAuditSha256": audit_hash,
        "blindDecisionLockedAt": audit_created,
        "modelVersion": (predictions.get("model") or {}).get("modelVersion"),
        "summary": summary,
        "items": items,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--silver", type=Path, required=True)
    parser.add_argument("--predictions", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    paths = {
        "silver": args.silver.resolve(),
        "predictions": args.predictions.resolve(),
        "audit": args.audit.resolve(),
        "output": args.output.resolve(),
    }
    if paths["output"].exists():
        raise FileExistsError(f"refusing to overwrite immutable comparison: {paths['output']}")
    payload = compare(
        json.loads(paths["silver"].read_text(encoding="utf-8")),
        json.loads(paths["predictions"].read_text(encoding="utf-8")),
        json.loads(paths["audit"].read_text(encoding="utf-8")),
        silver_hash=sha256_file(paths["silver"]),
        predictions_hash=sha256_file(paths["predictions"]),
        audit_hash=sha256_file(paths["audit"]),
    )
    paths["output"].parent.mkdir(parents=True, exist_ok=True)
    paths["output"].write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(payload["summary"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
