"""Validate babNN.json files and emit immutable candidate-version JSONL for Atlas import."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.ingestion.pretest_import import import_directory


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="output/pretest")
    parser.add_argument("--output", default="data/processed/question_versions_v2.jsonl")
    args = parser.parse_args()
    records = import_directory(args.source)
    destination = Path(args.output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        "\n".join(record.model_dump_json() for record in records) + "\n",
        encoding="utf-8",
    )
    counts: dict[str, int] = {}
    for record in records:
        counts[record.qualificationStatus] = counts.get(record.qualificationStatus, 0) + 1
    print(json.dumps({"imported": len(records), "qualification": counts, "output": str(destination)}, indent=2))


if __name__ == "__main__":
    main()
