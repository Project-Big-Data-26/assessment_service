import json

import pymupdf

from app.extraction.adapters import extract_document
from app.extraction.models import ExtractionSettings
from app.extraction.questions import segment_questions


def test_extracts_question_fields_from_json(tmp_path):
    source = tmp_path / "questions.json"
    source.write_text(json.dumps([{
        "question_text": "Hitung nilai $2 + 3$.",
        "options": ["$4$", "$5$"],
        "explanation": "Gunakan penjumlahan bilangan bulat.",
    }]), encoding="utf-8")

    result = extract_document(source, media_type="application/json")

    assert result["status"] == "completed"
    assert "Hitung nilai" in result["extracted_text"]
    assert "2 + 3" in result["latex_candidates"]


def test_extracts_latex_source(tmp_path):
    source = tmp_path / "question.tex"
    source.write_text(r"Tentukan $x$ jika $2x=8$.", encoding="utf-8")

    result = extract_document(source, media_type="text/x-tex")

    assert result["latex_candidates"] == ["x", "2x=8"]


def test_extracts_numbered_questions_and_options_from_pdf_text_layer(tmp_path):
    source = tmp_path / "questions.pdf"
    document = pymupdf.open()
    page = document.new_page()
    page.insert_text(
        (72, 72),
        "1. Berapakah hasil 2 + 3?\nA. 4\nB. 5\n2. Jelaskan arti gradien.",
        fontsize=11,
    )
    document.save(source)
    document.close()

    result = extract_document(
        source,
        media_type="application/pdf",
        settings=ExtractionSettings(ocr_enabled=False),
    )

    assert result["status"] == "completed"
    assert result["document_metadata"]["page_count"] == 1
    assert result["pages"][0]["method"] == "text_layer"
    assert [item["question_number"] for item in result["questions"]] == ["1", "2"]
    assert result["questions"][0]["options"] == [
        {"label": "A", "text": "4"},
        {"label": "B", "text": "5"},
    ]
    assert result["questions"][0]["visual_previews"][0]["data_url"].startswith("data:image/")
    assert result["questions"][0]["visual_previews"][0]["crop_method"] == "question_bounds"
    assert result["questions"][0]["visual_previews"][0]["height"] > 0
    assert result["questions"][1]["visual_previews"][0]["data_url"].startswith("data:image/")
    assert result["review_required"] is False


def test_corrupt_pdf_returns_review_status_instead_of_crashing(tmp_path):
    source = tmp_path / "broken.pdf"
    source.write_bytes(b"%PDF-not-a-real-document")

    result = extract_document(source, media_type="application/pdf")

    assert result["status"] == "needs_manual_review"
    assert result["review_required"] is True
    assert "PDF tidak dapat dibuka" in result["warnings"][0]


def test_unnumbered_text_is_preserved_as_review_candidate():
    result = segment_questions(
        [{"page_number": 1, "text": "Hitung luas persegi dengan sisi 4 cm.", "method": "text_layer"}]
    )

    assert len(result) == 1
    assert result[0]["question_number"] is None
    assert result[0]["needs_review"] is True


def test_ocr_option_without_space_after_separator_is_still_segmented():
    result = segment_questions(
        [{"page_number": 1, "text": "1. Hitung 2 + 3.\nA. 4\nB.5", "method": "ocr"}]
    )

    assert result[0]["options"] == [
        {"label": "A", "text": "4"},
        {"label": "B", "text": "5"},
    ]
    assert result[0]["needs_review"] is True
    assert "hasil OCR" in result[0]["review_reasons"][-1]
