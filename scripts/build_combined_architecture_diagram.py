"""Compatibility entry point for the current silver operational diagram."""
from pathlib import Path
from build_empirical_diagrams import empirical

if __name__ == "__main__":
    empirical()
    directory = Path(__file__).resolve().parents[1] / "API_DOCUMENTATION"
    (directory / "20_END_TO_END_VALIDATION_FLOW.svg").write_bytes((directory / "23_EMPIRICAL_VALIDATION_FEEDBACK_FLOW.svg").read_bytes())
