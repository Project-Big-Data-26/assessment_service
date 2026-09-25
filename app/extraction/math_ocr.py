"""Detect mathematical formula regions and convert them into renderable LaTeX."""

from __future__ import annotations

import io
import os
import re
import threading
import base64
from pathlib import Path
from typing import Any

from app.extraction.models import ExtractionSettings

_PIPELINE: Any | None = None
_PIPELINE_KEY: tuple[str, str] | None = None
_PIPELINE_LOCK = threading.Lock()


def _clean_latex(value: str) -> str:
    latex = value.strip().strip("$").strip()
    latex = re.sub(r"\\(?:begin|end)\{document\}", "", latex).strip()
    return latex


def _pipeline(settings: ExtractionSettings) -> Any:
    global _PIPELINE, _PIPELINE_KEY
    key = (settings.math_ocr_layout_model, settings.math_ocr_formula_model)
    if _PIPELINE is not None and _PIPELINE_KEY == key:
        return _PIPELINE
    with _PIPELINE_LOCK:
        if _PIPELINE is not None and _PIPELINE_KEY == key:
            return _PIPELINE
        os.environ.setdefault("PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK", "True")
        os.environ.setdefault("PADDLE_PDX_MODEL_SOURCE", "BOS")
        from paddleocr import FormulaRecognitionPipeline

        _PIPELINE = FormulaRecognitionPipeline(
            layout_detection_model_name=settings.math_ocr_layout_model,
            formula_recognition_model_name=settings.math_ocr_formula_model,
            use_doc_orientation_classify=False,
            use_doc_unwarping=False,
        )
        _PIPELINE_KEY = key
        return _PIPELINE


def _inside(center_x: float, center_y: float, bbox: list[float]) -> bool:
    return bbox[0] <= center_x <= bbox[2] and bbox[1] <= center_y <= bbox[3]


def _formula_visual(image: Any, bbox: list[float], scale: float) -> dict[str, Any]:
    left = max(0, int(bbox[0] * scale) - 8)
    top = max(0, int(bbox[1] * scale) - 8)
    right = min(image.width, int(bbox[2] * scale) + 8)
    bottom = min(image.height, int(bbox[3] * scale) + 8)
    crop = image.crop((left, top, right, bottom))
    output = io.BytesIO()
    crop.save(output, format="WEBP", lossless=True, method=4)
    encoded = base64.b64encode(output.getvalue()).decode("ascii")
    return {
        "visual_data_url": f"data:image/webp;base64,{encoded}",
        "visual_width": crop.width,
        "visual_height": crop.height,
    }


def _latex_renderable(latex: str) -> bool:
    return (
        0 < len(latex) <= 600
        and latex.count("{") == latex.count("}")
        and latex.count("{}") < 10
    )


def attach_math_formulas(
    path: str | Path,
    questions: list[dict[str, Any]],
    settings: ExtractionSettings,
) -> list[str]:
    """Attach page-detected formulas to their containing question regions."""
    for question in questions:
        question["math_formulas"] = []
        question["classification_text"] = question.get("question_text", "")
    if not settings.math_ocr_enabled or not questions:
        return []

    import numpy as np
    import pymupdf
    from PIL import Image

    warnings: list[str] = []
    page_regions: dict[int, list[tuple[dict[str, Any], list[float]]]] = {}
    for question in questions:
        for region in question.get("_preview_regions", []):
            page_regions.setdefault(int(region["page_number"]), []).append(
                (question, [float(value) for value in region["bbox"]])
            )
    selected_pages = sorted(page_regions)[: settings.math_ocr_max_pages]
    if len(page_regions) > len(selected_pages):
        warnings.append(
            f"OCR matematika dibatasi hingga {settings.math_ocr_max_pages} halaman."
        )

    recognizer = _pipeline(settings)
    scale = settings.math_ocr_dpi / 72
    with pymupdf.open(path) as document:
        for page_number in selected_pages:
            page = document.load_page(page_number - 1)
            pixmap = page.get_pixmap(
                matrix=pymupdf.Matrix(scale, scale), alpha=False
            )
            image = Image.open(io.BytesIO(pixmap.tobytes("png"))).convert("RGB")
            results = recognizer.predict(input=np.asarray(image))
            if not results:
                continue
            payload = results[0].json.get("res", {})
            for formula in payload.get("formula_res_list", []):
                latex = _clean_latex(str(formula.get("rec_formula", "")))
                polygon = formula.get("dt_polys") or []
                if not latex or not polygon:
                    continue
                values = polygon[0]
                if len(values) == 4:
                    x0, y0, x1, y1 = (float(value) / scale for value in values)
                else:
                    xs = [float(point[0]) / scale for point in values]
                    ys = [float(point[1]) / scale for point in values]
                    x0, y0, x1, y1 = min(xs), min(ys), max(xs), max(ys)
                center_x, center_y = (x0 + x1) / 2, (y0 + y1) / 2
                for question, region_bbox in page_regions[page_number]:
                    if not _inside(center_x, center_y, region_bbox):
                        continue
                    if any(item["latex"] == latex for item in question["math_formulas"]):
                        break
                    question["math_formulas"].append(
                        {
                            "latex": latex,
                            "page_number": page_number,
                            "bbox": [x0, y0, x1, y1],
                            "source": settings.math_ocr_formula_model,
                            "latex_renderable": _latex_renderable(latex),
                            **_formula_visual(image, [x0, y0, x1, y1], scale),
                        }
                    )
                    break

    for question in questions:
        formulas = question.get("math_formulas", [])
        if formulas:
            latex_context = " ".join(f"${item['latex']}$" for item in formulas)
            question["classification_text"] = (
                f"{question.get('question_text', '')} Formula matematika terdeteksi: {latex_context}"
            ).strip()
    return warnings
