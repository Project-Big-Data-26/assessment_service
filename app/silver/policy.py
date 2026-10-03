"""Operational qualification is independent of frozen provider prompts."""
from __future__ import annotations

from app.classification.v2.contracts import HEAD_LABELS
import re
import unicodedata

POLICY_VERSION = "ai-silver-operational-v1"
LABEL_PROVENANCE = "ai_silver"


def qualification(record: dict, structure: dict, question: dict | None = None) -> tuple[dict, str]:
    aggregate = record.get("aggregate") or {}
    labels = {head: (aggregate.get("heads", {}).get(head) or {}).get("label") for head in HEAD_LABELS}
    if (structure["status"] != "pass" or aggregate.get("contentStatus") == "concern"
            or aggregate.get("answerKeyStatus") == "conflict"):
        return labels, "revision_required"
    if aggregate.get("eligibleForTraining") and all(labels.values()):
        if question is not None:
            key = resolve_answer_key(aggregate.get("verifiedAnswerKey"), question["options"])
            if (key is None or key != question.get("jawaban") or aggregate.get("contentStatus") != "valid"
                    or aggregate.get("answerKeyStatus") != "verified"
                    or not (aggregate.get("verifiedMinimalSolution") or "").strip()
                    or (question.get("image_url") and not aggregate.get("visualTranscript"))):
                return labels, "needs_ai_review"
        return labels, "silver_ready"
    return labels, "needs_ai_review"


def validate_provenance(provenance: dict) -> None:
    """Reject staging, unresolved AI output, and label-only relabeling."""
    if provenance.get("kind") != LABEL_PROVENANCE:
        raise ValueError("an AI silver decision is required")
    if (provenance.get("contentStatus") != "valid"
            or provenance.get("answerKeyStatus") != "verified"
            or provenance.get("successfulRuns") != 3
            or not provenance.get("decisionId")):
        raise ValueError("silver content, key, and three successful blind runs must be qualified")
    hashes = provenance.get("sourceResponseHashes") or []
    if len(hashes) != 3 or any(not _sha256(value) for value in hashes):
        raise ValueError("three response hashes are required for silver provenance")
    if not _sha256(provenance.get("checkpointHash")) or not _sha256(provenance.get("sourceInputHash")):
        raise ValueError("silver provenance requires checkpoint and input hashes")


def _sha256(value: object) -> bool:
    return isinstance(value, str) and len(value) == 64 and all(c in "0123456789abcdef" for c in value)


def resolve_answer_key(value: str | None, options: list[dict]) -> str | None:
    """Map an AI answer to an option only when the mapping is unambiguous."""
    if not value:
        return None
    by_label = {option["option_id"]: option["text"] for option in options}
    if value.strip().upper() in by_label:
        return value.strip().upper()

    def normalize(text: str) -> str:
        text = unicodedata.normalize("NFKC", text).casefold().replace("−", "-")
        text = re.sub(r"\\(?:text|mathrm)\{([^{}]*)\}", r"\1", text)
        text = re.sub(r"\\(?:d?frac)\{([^{}]*)\}\{([^{}]*)\}", r"\1/\2", text)
        return re.sub(r"\s+", "", text.replace("$", "").replace("\\,", "").replace("\\!", ""))

    matches = [label for label, text in by_label.items() if normalize(text) == normalize(value)]
    if len(matches) == 1:
        return matches[0]
    picture = re.match(r"^gambar\s+(\d+)\b", value.strip(), re.IGNORECASE)
    if picture:
        matches = [label for label, text in by_label.items()
                   if re.match(rf"^gambar\s+{picture[1]}\b", text.strip(), re.IGNORECASE)]
        return matches[0] if len(matches) == 1 else None
    # Count units and explicit alternate representations are not part of an option ID.
    numeric = r"[-+]?\d+(?:[.,]\d+)?(?:/\d+)?%?"
    first = value.split(", ")[0].strip().strip("$")
    if re.fullmatch(numeric, first):
        matches = []
        for label, text in by_label.items():
            plain = text.replace("$", "").strip()
            part = re.fullmatch(rf"({numeric})(?:\s+(?:cara|kupon|satuan luas)|\s+\(atau .+\))?", plain)
            if part and part[1] == first:
                matches.append(label)
        if len(matches) == 1:
            return matches[0]
    return None
