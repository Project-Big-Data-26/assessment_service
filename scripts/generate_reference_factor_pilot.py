"""Create three text variants from active validated references; no API calls."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.services.exercise.reference_pilot import export_factor_pilot


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "output")
    parser.add_argument("--batch", type=int, default=2)
    args = parser.parse_args()
    print(json.dumps(export_factor_pilot(args.output, args.batch), ensure_ascii=False))


if __name__ == "__main__":
    main()
