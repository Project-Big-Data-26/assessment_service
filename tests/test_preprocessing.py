import pytest

from app.preprocessing import clean_text, normalize_text


def test_clean_text_normalizes_unicode_and_whitespace() -> None:
    assert clean_text("  Ａnalisis\n\tdata  ") == "Analisis data"


def test_normalize_text_can_lowercase() -> None:
    assert normalize_text("Jelaskan Proses", lowercase=True) == "jelaskan proses"


def test_clean_text_rejects_non_string_input() -> None:
    with pytest.raises(TypeError):
        clean_text(None)  # type: ignore[arg-type]
