"""Run SMA blind batches serially and stop all batches on a shared provider block."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.llm.config import GeminiSettings  # noqa: E402
from scripts.generate_silver_labels_kelas1 import (  # noqa: E402
    atomic_write, load_checkpoint, summarize,
)


def read(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def complete(checkpoint: dict, count: int) -> bool:
    summary = checkpoint.get("summary") or {}
    return bool(
        summary.get("successfulRuns") == count * 3
        and not summary.get("failedRuns")
        and not summary.get("pendingAdjudication")
    )


def save(checkpoint: dict, path: Path) -> None:
    checkpoint["updatedAt"] = datetime.now(timezone.utc).isoformat()
    checkpoint["summary"] = summarize(checkpoint)
    atomic_write(checkpoint, path)


def run_batches(source_base: Path, batch_name: str, grades: list[int], *, model: str) -> int:
    if not re.fullmatch(r"[A-Za-z0-9_-]+", batch_name):
        raise ValueError("batch name must be a single directory name")
    if not grades or len(set(grades)) != len(grades) or any(g not in (10, 11, 12) for g in grades):
        raise ValueError("select unique SMA grades 10, 11, and/or 12")
    source_base = source_base.resolve()
    batches = []
    for grade in grades:
        source = source_base / f"kelas{grade}/soal_pretest_db.json"
        questions = json.loads(source.read_text(encoding="utf-8"))
        output = source.parent / batch_name / "silver_labels.json"
        output.parent.mkdir(parents=True, exist_ok=True)
        checkpoint = load_checkpoint(
            output, source, hashlib.sha256(source.read_bytes()).hexdigest(), model, 3, grade
        )
        if not output.exists():
            checkpoint["executionStatus"] = "queued"
            save(checkpoint, output)
        batches.append((grade, source, output, len(questions)))

    def save_execution() -> None:
        atomic_write({
            "schemaVersion": "sma-blind-batch-execution-v1",
            "updatedAt": datetime.now(timezone.utc).isoformat(),
            "model": model, "serialExecution": True,
            "stopAllOnSharedProviderBlock": True,
            "batches": [{
                "grade": grade, "questionCount": count, "requestedRuns": count * 3,
                "checkpoint": output.as_posix(),
                "executionStatus": read(output).get("executionStatus"),
                "summary": read(output).get("summary"),
                "blockedByGrade": read(output).get("blockedByGrade"),
            } for grade, _, output, count in batches],
        }, source_base / f"{batch_name}_sma_execution.json")

    save_execution()
    for index, (grade, source, output, count) in enumerate(batches):
        if complete(read(output), count):
            continue
        print(f"Starting SMA grade={grade} questions={count}", flush=True)
        result = subprocess.run([
            sys.executable, str(ROOT / "scripts/generate_silver_labels_kelas1.py"),
            "--source", str(source), "--grade", str(grade), "--output", str(output),
            "--runs", "3", "--workers", "1", "--pause", "3", "--attempts", "3", "--execute",
        ], check=False)
        checkpoint = read(output)
        status = checkpoint.get("executionStatus", "")
        if status.startswith("blocked_provider_"):
            for _, _, pending_output, pending_count in batches[index + 1:]:
                pending = read(pending_output)
                if complete(pending, pending_count):
                    continue
                pending["executionStatus"] = status.replace("blocked_", "waiting_", 1)
                pending["stopReason"] = checkpoint.get("stopReason")
                pending["blockedByGrade"] = grade
                save(pending, pending_output)
            save_execution()
            return 3
        save_execution()
        if result.returncode and status != "completed_batch":
            raise RuntimeError(f"grade {grade} stopped unexpectedly; checkpoint preserved")
    save_execution()
    return 0 if all(complete(read(output), count) for _, _, output, count in batches) else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-base", type=Path, default=ROOT / "output/pretest")
    parser.add_argument("--batch-name", required=True)
    parser.add_argument("--grades", type=int, nargs="+", choices=(10, 11, 12), default=[10, 11, 12])
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()
    if not args.execute:
        parser.error("live generation requires --execute")
    return run_batches(args.source_base, args.batch_name, args.grades, model=GeminiSettings.from_environment().model)


if __name__ == "__main__":
    raise SystemExit(main())
