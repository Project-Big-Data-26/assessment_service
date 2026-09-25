"""Generate platform-ready visual crops for extracted PDF questions."""

from __future__ import annotations

import base64
import io
import re
from pathlib import Path
from typing import Any

from app.extraction.models import ExtractionSettings

_QUESTION_PREFIX = re.compile(r"^\s*(?:(?:soal|nomor)\s+)?\d{1,3}\s*[.)]\s*", re.IGNORECASE)


def _normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip().casefold()


def _page_lines(page: Any) -> list[tuple[float, float, float, float, str]]:
    lines: list[tuple[float, float, float, float, str]] = []
    payload = page.get_text("dict", sort=True)
    for block in payload.get("blocks", []):
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            text = "".join(span.get("text", "") for span in line.get("spans", [])).strip()
            if text:
                bbox = line.get("bbox", (0, 0, 0, 0))
                lines.append(tuple(float(value) for value in bbox) + (text,))
    return lines


def _question_start_box(
    page: Any,
    question_text: str,
    layout_lines: list[dict[str, Any]] | None = None,
) -> tuple[float, float, float, float] | None:
    target = _normalize(question_text)
    if not target:
        return None
    target_prefix = target[:48]
    candidate_lines = [
        (*[float(value) for value in line.get("bbox", (0, 0, 0, 0))], str(line.get("text", "")))
        for line in (layout_lines or [])
    ] or _page_lines(page)
    for left, top, right, bottom, raw_text in candidate_lines:
        line = _normalize(_QUESTION_PREFIX.sub("", raw_text))
        if not line:
            continue
        comparable = line[:48]
        if target_prefix.startswith(comparable) or comparable.startswith(target_prefix[: min(24, len(target_prefix))]):
            return left, top, right, bottom
    return None


def _content_bottom(page: Any, start_y: float, end_y: float) -> float:
    bottoms = []
    for block in page.get_text("dict", sort=True).get("blocks", []):
        bbox = block.get("bbox", (0, 0, 0, 0))
        top = float(bbox[1])
        bottom = float(bbox[3])
        if bottom >= start_y and top < end_y:
            bottoms.append(min(bottom, end_y))
    return max(bottoms, default=min(end_y, start_y + 180))


def _render_clip(page: Any, clip: Any, dpi: int) -> dict[str, Any]:
    import pymupdf
    from PIL import Image

    scale = dpi / 72
    pixmap = page.get_pixmap(matrix=pymupdf.Matrix(scale, scale), clip=clip, alpha=False)
    image = Image.open(io.BytesIO(pixmap.tobytes("png")))
    output = io.BytesIO()
    mime_type = "image/webp"
    try:
        image.save(output, format="WEBP", lossless=True, method=4)
    except (KeyError, OSError):
        mime_type = "image/png"
        image.save(output, format="PNG", optimize=True)
    encoded = base64.b64encode(output.getvalue()).decode("ascii")
    return {
        "mime_type": mime_type,
        "data_url": f"data:{mime_type};base64,{encoded}",
        "width": image.width,
        "height": image.height,
    }


def attach_question_previews(
    path: str | Path,
    questions: list[dict[str, Any]],
    settings: ExtractionSettings,
    *,
    page_layouts: dict[int, list[dict[str, Any]]] | None = None,
) -> list[str]:
    """Attach lossless image crops while keeping textual extraction separate."""
    if not settings.question_preview_enabled or not questions:
        return []

    import pymupdf

    warnings: list[str] = []
    preview_budget = settings.max_question_previews
    with pymupdf.open(path) as document:
        starts: dict[tuple[int, int], tuple[float, float, float, float] | None] = {}
        for index, question in enumerate(questions):
            first_page = int(question["page_numbers"][0])
            page = document.load_page(first_page - 1)
            starts[(index, first_page)] = _question_start_box(
                page,
                question["question_text"],
                (page_layouts or {}).get(first_page),
            )

        for index, question in enumerate(questions):
            question["visual_previews"] = []
            question["_preview_regions"] = []
            if preview_budget <= 0:
                continue
            page_numbers = [int(value) for value in question.get("page_numbers", [])]
            for page_offset, page_number in enumerate(page_numbers):
                if preview_budget <= 0 or not 1 <= page_number <= document.page_count:
                    break
                page = document.load_page(page_number - 1)
                fallback = False
                page_width = float(page.rect.width)
                if page_offset == 0:
                    start_box = starts.get((index, page_number))
                    if start_box is None:
                        start_y = 0.0
                        fallback = True
                    else:
                        start_y = start_box[1]
                else:
                    start_box = None
                    start_y = 0.0

                page_starts = [
                    box
                    for (question_index, start_page), box in starts.items()
                    if start_page == page_number and box is not None
                ]
                x_positions = [box[0] for box in page_starts]
                has_columns = bool(x_positions) and max(x_positions) - min(x_positions) > page_width * 0.25
                column = None
                left, right = 12.0, page_width - 12.0
                if has_columns and start_box is not None:
                    column = 0 if start_box[0] < page_width / 2 else 1
                    if column == 0:
                        right = page_width / 2 - 4
                    else:
                        left = page_width / 2 + 4

                next_candidates = []
                for other_box in page_starts:
                    other_column = 0 if other_box[0] < page_width / 2 else 1
                    if other_box[1] > start_y + 2 and (column is None or other_column == column):
                        next_candidates.append(other_box[1])
                next_y = min(next_candidates, default=None)

                page_bottom = float(page.rect.height)
                boundary = next_y if next_y is not None else page_bottom
                content_bottom = _content_bottom(page, start_y, boundary)
                bottom = boundary - 6 if next_y is not None else min(page_bottom, content_bottom + 12)
                top = max(0.0, start_y - 8)
                if bottom <= top + 24:
                    top, bottom, fallback = 0.0, page_bottom, True

                clip = pymupdf.Rect(left, top, right, bottom)
                question["_preview_regions"].append(
                    {
                        "page_number": page_number,
                        "bbox": [clip.x0, clip.y0, clip.x1, clip.y1],
                    }
                )
                preview = _render_clip(page, clip, settings.question_preview_dpi)
                preview.update(
                    {
                        "page_number": page_number,
                        "crop_method": "full_page_fallback" if fallback else "question_bounds",
                    }
                )
                question["visual_previews"].append(preview)
                preview_budget -= 1

    if preview_budget <= 0 and sum(len(item.get("page_numbers", [])) for item in questions) > settings.max_question_previews:
        warnings.append(
            f"Preview visual dibatasi hingga {settings.max_question_previews} gambar untuk menjaga ukuran respons."
        )
    return warnings
