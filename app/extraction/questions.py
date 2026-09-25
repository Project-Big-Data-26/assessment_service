"""Conservative question segmentation for extracted page text."""

from __future__ import annotations

import re
from collections.abc import Iterable
from typing import Any

_QUESTION_START = re.compile(
    r"^\s*(?:(?:soal|nomor)\s+)?(?P<number>\d{1,3})\s*[.)]\s+(?P<text>.+)$",
    flags=re.IGNORECASE,
)
_OPTION_START = re.compile(r"^\s*(?P<label>[A-Ha-h])\s*[.)]\s*(?P<text>\S.*)$")


def _clean_lines(text: str) -> list[str]:
    return [re.sub(r"\s+", " ", line).strip() for line in text.splitlines() if line.strip()]


def _page_method(page_numbers: list[int], methods: dict[int, str]) -> str:
    selected = {methods[number] for number in page_numbers if number in methods}
    if len(selected) > 1:
        return "mixed"
    return next(iter(selected), "unknown")


def segment_questions(pages: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Turn numbered PDF/OCR text into reviewable question candidates.

    The parser intentionally does not infer answer keys. Ambiguous, unnumbered text is
    returned as one candidate and marked for review instead of silently discarded.
    """
    page_list = list(pages)
    page_methods = {int(page["page_number"]): str(page["method"]) for page in page_list}
    numbered_found = any(
        _QUESTION_START.match(line)
        for page in page_list
        for line in _clean_lines(str(page.get("text", "")))
    )

    candidates: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    current_option: dict[str, str] | None = None
    last_question_number: int | None = None

    def start_candidate(number: str | None, text: str, page_number: int) -> dict[str, Any]:
        return {
            "question_number": number,
            "question_lines": [text] if text else [],
            "options": [],
            "page_numbers": [page_number],
        }

    def finish_candidate() -> None:
        nonlocal current, current_option
        if current is None:
            return
        question_text = " ".join(current.pop("question_lines")).strip()
        if not question_text and not current["options"]:
            current = None
            current_option = None
            return
        index = len(candidates) + 1
        page_numbers = sorted(set(current["page_numbers"]))
        extraction_method = _page_method(page_numbers, page_methods)
        reasons: list[str] = []
        if current["question_number"] is None:
            reasons.append("Nomor soal tidak terdeteksi; periksa batas soal secara manual.")
        if not question_text:
            reasons.append("Teks pertanyaan tidak terdeteksi dengan jelas.")
        if extraction_method in {"ocr", "mixed"}:
            reasons.append("Kandidat memuat hasil OCR; periksa angka, simbol, dan rumus.")
        candidates.append(
            {
                "candidate_id": f"Q-{index:03d}",
                "question_number": current["question_number"],
                "question_text": question_text,
                "options": current["options"],
                "page_numbers": page_numbers,
                "extraction_method": extraction_method,
                "needs_review": bool(reasons),
                "review_reasons": reasons,
            }
        )
        current = None
        current_option = None

    for page in page_list:
        page_number = int(page["page_number"])
        for line in _clean_lines(str(page.get("text", ""))):
            question_match = _QUESTION_START.match(line)
            if question_match:
                detected_number = int(question_match.group("number"))
                if last_question_number is not None and detected_number <= last_question_number:
                    question_match = None
            if question_match:
                finish_candidate()
                current = start_candidate(
                    question_match.group("number"), question_match.group("text"), page_number
                )
                last_question_number = int(question_match.group("number"))
                continue

            if current is None:
                if numbered_found:
                    # Headers and instructions before the first explicit number are not
                    # promoted to a question candidate.
                    continue
                current = start_candidate(None, "", page_number)

            if page_number not in current["page_numbers"]:
                current["page_numbers"].append(page_number)

            option_match = _OPTION_START.match(line)
            if option_match:
                current_option = {
                    "label": option_match.group("label").upper(),
                    "text": option_match.group("text").strip(),
                }
                current["options"].append(current_option)
            elif current_option is not None:
                current_option["text"] = f'{current_option["text"]} {line}'.strip()
            else:
                current["question_lines"].append(line)

    finish_candidate()
    return candidates
