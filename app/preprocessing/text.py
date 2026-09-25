"""Conservative preprocessing for Indonesian assessment questions."""

from __future__ import annotations

import re
import unicodedata

_WHITESPACE_PATTERN = re.compile(r"\s+")


def clean_text(text: str, *, unicode_form: str = "NFKC") -> str:
    """Normalize Unicode and whitespace without removing semantic punctuation."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    normalized = unicodedata.normalize(unicode_form, text)
    return _WHITESPACE_PATTERN.sub(" ", normalized).strip()


def normalize_text(text: str, *, lowercase: bool = False) -> str:
    """Clean text and optionally apply Unicode-aware lowercasing."""
    cleaned = clean_text(text)
    return cleaned.casefold() if lowercase else cleaned
