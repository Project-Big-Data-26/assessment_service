"""Source adapters that preserve provenance and degrade safely."""

from __future__ import annotations

import csv
import io
import json
import os
import re
import shutil
from pathlib import Path
from typing import Any

from app.extraction.models import ExtractionSettings
from app.extraction.math_ocr import attach_math_formulas
from app.extraction.previews import attach_question_previews
from app.extraction.questions import segment_questions

SUPPORTED_EXTENSIONS = frozenset(
    {".pdf", ".png", ".jpg", ".jpeg", ".tif", ".tiff", ".json", ".csv", ".txt", ".tex"}
)


def _latex_candidates(text: str) -> list[str]:
    patterns = re.findall(r"\$([^$]+)\$|\\\((.+?)\\\)|\\\[(.+?)\\\]", text, flags=re.DOTALL)
    return [next(part for part in match if part).strip() for match in patterns]


def _configure_tesseract():
    import pytesseract

    configured_command = os.getenv("TESSERACT_CMD") or shutil.which("tesseract")
    if not configured_command and os.name == "nt":
        for candidate in (
            Path(os.environ.get("ProgramFiles", "C:/Program Files")) / "Tesseract-OCR" / "tesseract.exe",
            Path(os.environ.get("LOCALAPPDATA", "")) / "Programs" / "Tesseract-OCR" / "tesseract.exe",
        ):
            if candidate.is_file():
                configured_command = str(candidate)
                break
    if configured_command:
        pytesseract.pytesseract.tesseract_cmd = configured_command

    tessdata_dir = os.getenv("NALAR_TESSDATA_DIR")
    if not tessdata_dir and os.name == "nt":
        local_tessdata = (
            Path(os.environ.get("LOCALAPPDATA", ""))
            / "NalarQuestionIntelligence"
            / "tessdata"
        )
        if local_tessdata.is_dir():
            tessdata_dir = str(local_tessdata)
    if tessdata_dir:
        # Tesseract reads this environment variable without command-line quoting
        # problems on Windows paths containing spaces.
        os.environ["TESSDATA_PREFIX"] = tessdata_dir
    return pytesseract


def extraction_capabilities() -> dict[str, Any]:
    """Report installed PDF/OCR runtime support without processing user content."""
    capabilities: dict[str, Any] = {
        "pymupdf_ready": False,
        "pymupdf_version": None,
        "tesseract_ready": False,
        "tesseract_version": None,
        "tesseract_languages": [],
    }
    try:
        import pymupdf

        capabilities["pymupdf_ready"] = True
        capabilities["pymupdf_version"] = pymupdf.__version__
    except ImportError:
        pass

    try:
        pytesseract = _configure_tesseract()
        capabilities["tesseract_version"] = str(pytesseract.get_tesseract_version())
        capabilities["tesseract_languages"] = sorted(pytesseract.get_languages(config=""))
        capabilities["tesseract_ready"] = True
    except (RuntimeError, OSError):
        pass
    return capabilities


def _ocr_image(
    image: Any, *, language: str
) -> tuple[str, float | None, list[dict[str, Any]]]:
    pytesseract = _configure_tesseract()

    data = pytesseract.image_to_data(
        image,
        lang=language,
        output_type=pytesseract.Output.DICT,
    )
    text_values = data.get("text", [])
    grouped_lines: dict[tuple[int, int, int, int], dict[str, Any]] = {}
    for index, raw_token in enumerate(text_values):
        token = raw_token.strip()
        if not token:
            continue
        key = tuple(
            int(data.get(field, [0] * len(text_values))[index])
            for field in ("page_num", "block_num", "par_num", "line_num")
        )
        left = int(data.get("left", [0] * len(text_values))[index])
        top = int(data.get("top", [0] * len(text_values))[index])
        width = int(data.get("width", [0] * len(text_values))[index])
        height = int(data.get("height", [0] * len(text_values))[index])
        line = grouped_lines.setdefault(
            key,
            {"tokens": [], "left": left, "top": top, "right": left + width, "bottom": top + height},
        )
        line["tokens"].append(token)
        line["left"] = min(line["left"], left)
        line["top"] = min(line["top"], top)
        line["right"] = max(line["right"], left + width)
        line["bottom"] = max(line["bottom"], top + height)
    confidences = [
        float(value)
        for value in data.get("conf", [])
        if str(value) not in {"-1", ""} and float(value) >= 0
    ]
    confidence = sum(confidences) / len(confidences) / 100 if confidences else None
    layout_lines = [
        {
            "text": " ".join(line["tokens"]),
            "bbox": [line["left"], line["top"], line["right"], line["bottom"]],
        }
        for line in grouped_lines.values()
    ]
    # Tesseract may emit an isolated question number and its neighboring scanned
    # sentence as separate blocks. Merge vertically overlapping fragments so the
    # parser receives e.g. ``15. Diketahui ...`` as one numbered line.
    layout_lines.sort(key=lambda line: (line["bbox"][1], line["bbox"][0]))
    rows: list[list[dict[str, Any]]] = []
    for line in layout_lines:
        top, bottom = line["bbox"][1], line["bbox"][3]
        if rows:
            row_top = min(item["bbox"][1] for item in rows[-1])
            row_bottom = max(item["bbox"][3] for item in rows[-1])
            overlap = min(bottom, row_bottom) - max(top, row_top)
            min_height = min(bottom - top, row_bottom - row_top)
            if overlap > 0 and overlap >= min_height * 0.35:
                rows[-1].append(line)
                continue
        rows.append([line])
    layout_lines = []
    for row in rows:
        row.sort(key=lambda line: line["bbox"][0])
        layout_lines.append(
            {
                "text": " ".join(line["text"] for line in row),
                "bbox": [
                    min(line["bbox"][0] for line in row),
                    min(line["bbox"][1] for line in row),
                    max(line["bbox"][2] for line in row),
                    max(line["bbox"][3] for line in row),
                ],
            }
        )
    text = "\n".join(line["text"] for line in layout_lines)
    return text, confidence, layout_lines


def _page_is_image_dominant(page: Any, text: str) -> bool:
    """Detect scanned pages that happen to contain a sparse, misleading text layer."""
    page_area = max(float(page.rect.width * page.rect.height), 1.0)
    image_areas: list[float] = []
    for block in page.get_text("dict").get("blocks", []):
        if block.get("type") != 1:
            continue
        x0, y0, x1, y1 = block.get("bbox", (0, 0, 0, 0))
        area = max(0.0, float(x1 - x0)) * max(0.0, float(y1 - y0))
        image_areas.append(area)
    meaningful_characters = len(re.sub(r"\s+", "", text))
    image_coverage = sum(image_areas) / page_area
    return (
        meaningful_characters < 500
        and (
            any(area / page_area >= 0.5 for area in image_areas)
            or (len(image_areas) >= 3 and image_coverage >= 0.2)
        )
    )


def _page_has_two_columns(page: Any) -> bool:
    midpoint = float(page.rect.width) / 2
    image_centers = []
    for block in page.get_text("dict").get("blocks", []):
        if block.get("type") == 1:
            x0, _y0, x1, _y1 = block.get("bbox", (0, 0, 0, 0))
            image_centers.append((float(x0) + float(x1)) / 2)
    left_count = sum(center < midpoint for center in image_centers)
    right_count = sum(center >= midpoint for center in image_centers)
    return left_count >= 2 and right_count >= 2


def _pdf_question_labels(page: Any) -> list[dict[str, Any]]:
    labels: list[dict[str, Any]] = []
    for block in page.get_text("dict", sort=True).get("blocks", []):
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            text = "".join(span.get("text", "") for span in line.get("spans", [])).strip()
            match = re.fullmatch(r"(\d{1,3})\s*[.)]", text)
            if match:
                labels.append({"number": int(match.group(1)), "bbox": line["bbox"]})
    midpoint = float(page.rect.width) / 2
    labels.sort(key=lambda item: (item["bbox"][0] >= midpoint, item["bbox"][1]))
    monotonic: list[dict[str, Any]] = []
    last_number = -1
    for label in labels:
        if label["number"] > last_number:
            monotonic.append(label)
            last_number = label["number"]
    return monotonic


def _ocr_numbered_regions(
    page: Any, image: Any, *, scale: float, language: str
) -> tuple[str, float | None, list[dict[str, Any]]] | None:
    """OCR each numbered region using exact PDF labels as segmentation anchors."""
    labels = _pdf_question_labels(page)
    if len(labels) < 2:
        return None
    page_width = float(page.rect.width)
    midpoint = page_width / 2
    has_columns = _page_has_two_columns(page)
    text_parts: list[str] = []
    all_lines: list[dict[str, Any]] = []
    confidences: list[float] = []
    for label in labels:
        number = label["number"]
        x0, y0, x1, _y1 = (float(value) for value in label["bbox"])
        column = 0 if x0 < midpoint else 1
        column_left = 0.0 if not has_columns or column == 0 else midpoint
        column_right = page_width if not has_columns or column == 1 else midpoint
        later = [
            float(other["bbox"][1])
            for other in labels
            if float(other["bbox"][1]) > y0 + 2
            and (not has_columns or (float(other["bbox"][0]) < midpoint) == (column == 0))
        ]
        bottom = min(later, default=float(page.rect.height))
        crop = (
            max(int((x1 - 1) * scale), int(column_left * scale)),
            max(0, int((y0 - 3) * scale)),
            min(image.width, int(column_right * scale)),
            min(image.height, int((bottom - 2) * scale)),
        )
        if crop[2] <= crop[0] or crop[3] <= crop[1]:
            continue
        region_text, confidence, region_lines = _ocr_image(
            image.crop(crop), language=language
        )
        region_text = re.sub(
            rf"^\s*{number}\s*[.)]\s*", "", region_text.strip(), count=1
        )
        text_parts.append(f"{number}. {region_text}".rstrip())
        if confidence is not None:
            confidences.append(confidence)
        for line in region_lines:
            all_lines.append(
                {
                    **line,
                    "bbox": [
                        line["bbox"][0] + crop[0],
                        line["bbox"][1] + crop[1],
                        line["bbox"][2] + crop[0],
                        line["bbox"][3] + crop[1],
                    ],
                }
            )
    average_confidence = sum(confidences) / len(confidences) if confidences else None
    return "\n".join(text_parts), average_confidence, all_lines


def _structured_text(path: Path) -> str:
    raw = path.read_text(encoding="utf-8-sig")
    if path.suffix.lower() in {".txt", ".tex"}:
        return raw
    if path.suffix.lower() == ".json":
        payload = json.loads(raw)
        rows = payload if isinstance(payload, list) else [payload]
    else:
        rows = list(csv.DictReader(io.StringIO(raw)))
    fragments: list[str] = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        for field in (
            "question_text",
            "questionText",
            "options",
            "explanation",
            "learning_objective",
        ):
            value = row.get(field)
            if isinstance(value, list):
                fragments.extend(str(item) for item in value)
            elif value:
                fragments.append(str(value))
    return "\n".join(fragments)


def _extract_pdf(
    path: Path, settings: ExtractionSettings
) -> tuple[list[dict[str, Any]], dict[str, Any], list[str]]:
    import pymupdf
    from PIL import Image

    warnings: list[str] = []
    pages: list[dict[str, Any]] = []
    metadata: dict[str, Any] = {}
    try:
        with pymupdf.open(path) as document:
            metadata = {
                "page_count": document.page_count,
                "title": (document.metadata or {}).get("title") or None,
                "author": (document.metadata or {}).get("author") or None,
                "is_encrypted": bool(document.needs_pass),
            }
            if document.needs_pass:
                warnings.append("PDF dilindungi kata sandi dan tidak dapat diekstrak.")
                return pages, metadata, warnings

            page_limit = min(document.page_count, settings.max_pdf_pages)
            if document.page_count > page_limit:
                warnings.append(
                    f"PDF memiliki {document.page_count} halaman; hanya {page_limit} halaman pertama yang diproses."
                )

            for index in range(page_limit):
                page = document.load_page(index)
                page_number = index + 1
                page_warnings: list[str] = []
                text = page.get_text("text", sort=True).strip()
                method = "text_layer"
                confidence: float | None = None

                meaningful_characters = len(re.sub(r"\s+", "", text))
                requires_ocr = (
                    meaningful_characters < settings.min_text_characters
                    or _page_is_image_dominant(page, text)
                )
                layout_lines: list[dict[str, Any]] = []
                if requires_ocr:
                    if settings.ocr_enabled:
                        try:
                            scale = settings.ocr_dpi / 72
                            pixmap = page.get_pixmap(
                                matrix=pymupdf.Matrix(scale, scale), alpha=False
                            )
                            image = Image.open(io.BytesIO(pixmap.tobytes("png")))
                            numbered_result = _ocr_numbered_regions(
                                page,
                                image,
                                scale=scale,
                                language=settings.ocr_language,
                            )
                            if numbered_result is not None:
                                ocr_text, confidence, pixel_lines = numbered_result
                            elif _page_has_two_columns(page):
                                split = image.width // 2
                                left_result = _ocr_image(
                                    image.crop((0, 0, split, image.height)),
                                    language=settings.ocr_language,
                                )
                                right_result = _ocr_image(
                                    image.crop((split, 0, image.width, image.height)),
                                    language=settings.ocr_language,
                                )
                                ocr_text = "\n".join(
                                    value for value in (left_result[0], right_result[0]) if value.strip()
                                )
                                available_confidences = [
                                    value
                                    for value in (left_result[1], right_result[1])
                                    if value is not None
                                ]
                                confidence = (
                                    sum(available_confidences) / len(available_confidences)
                                    if available_confidences
                                    else None
                                )
                                pixel_lines = left_result[2] + [
                                    {
                                        **line,
                                        "bbox": [
                                            line["bbox"][0] + split,
                                            line["bbox"][1],
                                            line["bbox"][2] + split,
                                            line["bbox"][3],
                                        ],
                                    }
                                    for line in right_result[2]
                                ]
                            else:
                                ocr_text, confidence, pixel_lines = _ocr_image(
                                    image, language=settings.ocr_language
                                )
                            if ocr_text.strip():
                                text = ocr_text.strip()
                                method = "ocr"
                                layout_lines = [
                                    {
                                        "text": line["text"],
                                        "bbox": [float(value) / scale for value in line["bbox"]],
                                    }
                                    for line in pixel_lines
                                ]
                            else:
                                method = "ocr_empty"
                                page_warnings.append("OCR tidak menemukan teks pada halaman ini.")
                        except (RuntimeError, OSError) as error:
                            method = "ocr_unavailable"
                            page_warnings.append(f"OCR tidak tersedia: {error}")
                    else:
                        method = "empty"
                        page_warnings.append("Text layer kosong dan OCR dinonaktifkan.")

                pages.append(
                    {
                        "page_number": page_number,
                        "text": text,
                        "method": method,
                        "confidence": confidence,
                        "warnings": page_warnings,
                        "_layout_lines": layout_lines,
                    }
                )
                warnings.extend(f"Halaman {page_number}: {item}" for item in page_warnings)
    except (pymupdf.FileDataError, pymupdf.EmptyFileError, RuntimeError, ValueError) as error:
        warnings.append(f"PDF tidak dapat dibuka: {error}")

    if any(page["method"] == "ocr" for page in pages):
        warnings.append(
            "Halaman tanpa text layer diproses dengan OCR; simbol dan rumus wajib diperiksa manual."
        )
    return pages, metadata, warnings


def _extract_image(
    path: Path, settings: ExtractionSettings
) -> tuple[list[dict[str, Any]], list[str]]:
    from PIL import Image

    warnings = ["OCR gambar berorientasi teks; periksa simbol matematika terhadap sumber asli."]
    if not settings.ocr_enabled:
        return [], warnings + ["OCR dinonaktifkan melalui konfigurasi."]
    try:
        with Image.open(path) as image:
            text, confidence, _layout_lines = _ocr_image(
                image, language=settings.ocr_language
            )
        return [
            {
                "page_number": 1,
                "text": text,
                "method": "ocr" if text.strip() else "ocr_empty",
                "confidence": confidence,
                "warnings": [],
            }
        ], warnings
    except (RuntimeError, OSError) as error:
        return [], warnings + [f"OCR tidak tersedia: {error}"]


def extract_document(
    path: str | Path,
    *,
    media_type: str = "application/octet-stream",
    settings: ExtractionSettings | None = None,
) -> dict[str, Any]:
    """Extract text, page provenance, and reviewable question candidates."""
    del media_type  # Retained as part of the stable adapter contract.
    source_path = Path(path)
    runtime = settings or ExtractionSettings()
    suffix = source_path.suffix.lower()
    warnings: list[str] = []
    metadata: dict[str, Any] = {
        "page_count": None,
        "title": None,
        "author": None,
        "is_encrypted": False,
    }
    pages: list[dict[str, Any]] = []

    if suffix not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported file type: {suffix or '<none>'}")

    if suffix in {".json", ".csv", ".txt", ".tex"}:
        try:
            text = _structured_text(source_path)
            pages = [
                {
                    "page_number": 1,
                    "text": text,
                    "method": "structured",
                    "confidence": None,
                    "warnings": [],
                }
            ]
            metadata["page_count"] = 1
        except (UnicodeDecodeError, json.JSONDecodeError, csv.Error) as error:
            warnings.append(f"Sumber terstruktur tidak dapat diparsing: {error}")
    elif suffix == ".pdf":
        try:
            pages, metadata, warnings = _extract_pdf(source_path, runtime)
        except ImportError as error:
            warnings.append(f"Dependency PDF/OCR belum terpasang: {error}")
    else:
        try:
            pages, warnings = _extract_image(source_path, runtime)
            metadata["page_count"] = 1
        except ImportError as error:
            warnings.append(f"Dependency gambar/OCR belum terpasang: {error}")

    extracted_text = "\n\n".join(
        page["text"].strip() for page in pages if page["text"].strip()
    )
    ocr_confidences = [
        float(page["confidence"])
        for page in pages
        if page.get("method") == "ocr" and page.get("confidence") is not None
    ]
    confidence = sum(ocr_confidences) / len(ocr_confidences) if ocr_confidences else None
    questions = segment_questions(pages) if extracted_text else []
    if suffix == ".pdf" and questions:
        try:
            page_layouts = {
                int(page["page_number"]): page.get("_layout_lines", []) for page in pages
            }
            warnings.extend(
                attach_question_previews(
                    source_path, questions, runtime, page_layouts=page_layouts
                )
            )
        except (ImportError, OSError, RuntimeError, ValueError) as error:
            warnings.append(f"Preview visual soal tidak dapat dibuat: {error}")
        if any(page.get("method") == "ocr" for page in pages):
            try:
                warnings.extend(attach_math_formulas(source_path, questions, runtime))
            except (ImportError, OSError, RuntimeError, ValueError) as error:
                warnings.append(
                    f"OCR matematika tidak tersedia; formula tetap ditampilkan lewat gambar: {error}"
                )
                for question in questions:
                    question.setdefault("math_formulas", [])
                    question.setdefault(
                        "classification_text", question.get("question_text", "")
                    )
        else:
            for question in questions:
                question.setdefault("math_formulas", [])
                question.setdefault("classification_text", question.get("question_text", ""))
    for question in questions:
        question.pop("_preview_regions", None)
    for page in pages:
        page.pop("_layout_lines", None)
    review_required = (
        not extracted_text
        or any(page.get("method") not in {"text_layer", "structured"} for page in pages)
        or any(question["needs_review"] for question in questions)
    )

    math_latex = [
        formula["latex"]
        for question in questions
        for formula in question.get("math_formulas", [])
    ]
    return {
        "extracted_text": extracted_text,
        "latex_candidates": list(
            dict.fromkeys(_latex_candidates(extracted_text) + math_latex)
        ),
        "confidence": confidence,
        "status": "completed" if extracted_text else "needs_manual_review",
        "warnings": warnings,
        "review_required": review_required,
        "document_metadata": metadata,
        "pages": pages,
        "questions": questions,
    }
