"""Compatibility entry point for the scoped, dry-run-first question importer.

Use --file output/.../hasil_validasi/validation_results.json for one export.
Connection settings are read from MONGODB_URI and MONGODB_DATABASE.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.auto_inserter import main  # noqa: E402


if __name__ == "__main__":
    raise SystemExit(main())
