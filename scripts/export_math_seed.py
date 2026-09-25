"""Export the demonstration seed; use approved labels for real model training."""
from __future__ import annotations
import json
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
from app.seed import build_math_seed
OUTPUT = PROJECT_ROOT / "data" / "sample" / "math_questions_seed.json"

if __name__ == "__main__":
    OUTPUT.write_text(json.dumps(build_math_seed(), ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(build_math_seed())} demo records to {OUTPUT}")
