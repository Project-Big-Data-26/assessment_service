"""Run the packaged IndoBERT 3x4x3 artifact over the silver snapshot."""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.classification.v2.runtime import V2ClassifierRuntime  # noqa: E402
from app.classification.v2.serializer import serialize_question  # noqa: E402
from app.training.v2.dataset import DatasetSnapshot  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--snapshot",
        type=Path,
        default=ROOT / "output/pretest/kelas1/dataset_snapshot_silver.json",
    )
    parser.add_argument(
        "--artifact", type=Path, default=ROOT / "models/indobert-3x4x3-v1"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "output/pretest/kelas1/indobert_predictions_silver.json",
    )
    parser.add_argument(
        "--allow-research-artifact",
        action="store_true",
        help="Required when running an unapproved or research-only artifact.",
    )
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(
            f"refusing to overwrite immutable research batch: {args.output}"
        )

    snapshot = DatasetSnapshot.model_validate_json(args.snapshot.read_text(encoding="utf-8"))
    runtime = V2ClassifierRuntime(args.artifact)
    if not runtime.manifest.servable and not args.allow_research_artifact:
        raise SystemExit(
            "artifact is not publicly servable; pass --allow-research-artifact for an explicit research batch"
        )
    items = []
    latency = []
    for index, row in enumerate(snapshot.rows, start=1):
        request = row.inference_request()
        serialized = serialize_question(
            request, representation=runtime.manifest.inputRepresentation
        )
        untruncated_tokens = len(
            runtime.tokenizer(serialized, truncation=False)["input_ids"]
        )
        started = time.perf_counter()
        prediction = runtime.predict(request)
        elapsed = int((time.perf_counter() - started) * 1000)
        latency.append(elapsed)
        items.append(
            {
                "index": index,
                "questionId": row.questionId,
                "questionVersionId": row.questionVersionId,
                "contentHash": row.contentHash,
                "silverLabels": {
                    "mathCognitiveDomain": row.mathCognitiveDomain.value,
                    "knowledgeDimension": row.knowledgeDimension.value,
                    "intendedDifficulty": row.intendedDifficulty.value,
                },
                "serializedInput": serialized,
                "untruncatedTokenCount": untruncated_tokens,
                "maxLength": runtime.manifest.maxLength,
                "wouldTruncate": untruncated_tokens > runtime.manifest.maxLength,
                "latencyMs": elapsed,
                "prediction": prediction.model_dump(mode="json"),
            }
        )
        print(f"item={index}/{len(snapshot.rows)} latency_ms={elapsed}", flush=True)

    label_counts = {
        head: dict(
            Counter(item["prediction"][head]["label"] for item in items)
        )
        for head in ("mathCognitiveDomain", "knowledgeDimension", "intendedDifficulty")
    }
    payload = {
        "schemaVersion": "indobert-silver-predictions-v1",
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "researchOnlyRun": not runtime.manifest.servable,
        "reviewRequired": True,
        "snapshotId": snapshot.snapshotId,
        "snapshotHash": snapshot.snapshotHash,
        "artifact": args.artifact.as_posix(),
        "model": runtime.manifest.model_dump(mode="json", exclude={"contentRegistry"}),
        "summary": {
            "itemCount": len(items),
            "latencyMs": {
                "minimum": min(latency) if latency else None,
                "mean": sum(latency) / len(latency) if latency else None,
                "maximum": max(latency) if latency else None,
            },
            "predictionDistribution": label_counts,
        },
        "items": items,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(payload["summary"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
