"""Configuration and internal value objects for source extraction."""

from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True, slots=True)
class ExtractionSettings:
    """Runtime limits shared by the API and command-line extractor."""

    ocr_enabled: bool = True
    ocr_language: str = "ind+eng"
    ocr_dpi: int = 300
    min_text_characters: int = 20
    max_pdf_pages: int = 200
    question_preview_enabled: bool = True
    question_preview_dpi: int = 144
    max_question_previews: int = 80
    math_ocr_enabled: bool = False
    math_ocr_dpi: int = 180
    math_ocr_max_pages: int = 20
    math_ocr_layout_model: str = "PP-DocLayout_plus-L"
    math_ocr_formula_model: str = "PP-FormulaNet-S"

    def with_overrides(self, **values: Any) -> "ExtractionSettings":
        """Return a copy with CLI- or caller-specific overrides."""
        return replace(self, **{key: value for key, value in values.items() if value is not None})


def load_extraction_settings(path: str | Path) -> ExtractionSettings:
    """Load extraction settings while retaining safe defaults for missing keys."""
    config_path = Path(path)
    if not config_path.is_file():
        return ExtractionSettings()

    payload = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    section = payload.get("extraction", {})
    return ExtractionSettings(
        ocr_enabled=bool(section.get("ocr_enabled", True)),
        ocr_language=str(section.get("ocr_language", "ind+eng")),
        ocr_dpi=int(section.get("ocr_dpi", 300)),
        min_text_characters=int(section.get("min_text_characters", 20)),
        max_pdf_pages=int(section.get("max_pdf_pages", 200)),
        question_preview_enabled=bool(section.get("question_preview_enabled", True)),
        question_preview_dpi=int(section.get("question_preview_dpi", 144)),
        max_question_previews=int(section.get("max_question_previews", 80)),
        math_ocr_enabled=bool(section.get("math_ocr_enabled", False)),
        math_ocr_dpi=int(section.get("math_ocr_dpi", 180)),
        math_ocr_max_pages=int(section.get("math_ocr_max_pages", 20)),
        math_ocr_layout_model=str(
            section.get("math_ocr_layout_model", "PP-DocLayout_plus-L")
        ),
        math_ocr_formula_model=str(
            section.get("math_ocr_formula_model", "PP-FormulaNet-S")
        ),
    )
