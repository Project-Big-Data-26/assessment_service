import argparse
import json

import pymupdf

from app.extraction.cli import DEFAULT_CONFIG, run


def test_cli_writes_structured_json_for_pdf(tmp_path):
    source = tmp_path / "source.pdf"
    output = tmp_path / "result.json"
    document = pymupdf.open()
    page = document.new_page()
    page.insert_text((72, 72), "1. Hitung 6 x 7.\nA. 42\nB. 48")
    document.save(source)
    document.close()

    written_to, payload = run(
        argparse.Namespace(
            source=source,
            output=output,
            config=DEFAULT_CONFIG,
            ocr_language=None,
            ocr_dpi=None,
            no_ocr=True,
        )
    )

    assert written_to == output.resolve()
    assert payload["questions"][0]["question_number"] == "1"
    assert json.loads(output.read_text(encoding="utf-8"))["questions"][0]["options"][0]["label"] == "A"
