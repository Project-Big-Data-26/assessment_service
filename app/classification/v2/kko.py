"""Transparent lexical KKO detector; never used as a silver-label rule."""

from __future__ import annotations

import re

# Surface patterns are versioned with code and preserved as an experimental
# feature. They intentionally do not map directly to a cognitive-domain label.
KKO_PATTERNS: dict[str, tuple[str, ...]] = {
    "mengidentifikasi": (r"\bidentifikasi(?:lah)?\b", r"\btentukan\b"),
    "menyebutkan": (r"\bsebutkan\b", r"\btuliskan\b"),
    "menghitung": (r"\bhitung(?:lah)?\b", r"\bberapa\b"),
    "membandingkan": (r"\bbandingkan\b", r"\blebih (?:besar|kecil|banyak|sedikit)\b"),
    "menerapkan": (r"\bgunakan\b", r"\bterapkan\b"),
    "menyelesaikan": (r"\bselesaikan\b", r"\bpecahkan\b"),
    "menganalisis": (r"\banalisis(?:lah)?\b", r"\bhubungan\b"),
    "menjelaskan": (r"\bjelaskan\b", r"\bberi(?:kan)? alasan\b"),
    "membuktikan": (r"\bbuktikan\b", r"\btunjukkan bahwa\b"),
    "menyimpulkan": (r"\bsimpulkan\b", r"\bkesimpulan\b"),
    "mengevaluasi": (r"\bevaluasi(?:lah)?\b", r"\bperiksa (?:kembali|kebenaran)\b"),
}


def detect_kko(*parts: str | None) -> list[str]:
    text = " ".join(part for part in parts if part).casefold()
    return [
        name
        for name, patterns in KKO_PATTERNS.items()
        if any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in patterns)
    ]
