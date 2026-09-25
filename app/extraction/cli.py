"""Command-line entry point for extracting one file or a directory of sources."""

from __future__ import annotations

import argparse
import json
import mimetypes
import sys
from pathlib import Path
from typing import Any

from app.extraction.adapters import SUPPORTED_EXTENSIONS, extract_document
from app.extraction.models import load_extraction_settings

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG = PROJECT_ROOT / "configs" / "extraction_config.yaml"


def _source_files(source: Path) -> list[Path]:
    if source.is_file():
        return [source]
    if source.is_dir():
        return sorted(
            path
            for path in source.rglob("*")
            if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS
        )
    raise FileNotFoundError(f"Sumber tidak ditemukan: {source}")


def _default_output(source: Path) -> Path:
    name = source.stem if source.is_file() else f"{source.name}-batch"
    return PROJECT_ROOT / "data" / "processed" / f"{name}.extracted.json"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Ekstrak teks dan kandidat soal dari PDF, gambar, atau sumber terstruktur."
    )
    parser.add_argument("source", type=Path, help="Path file atau direktori sumber")
    parser.add_argument("--output", type=Path, help="Path JSON hasil ekstraksi")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--ocr-language", help="Bahasa Tesseract, contoh: ind+eng")
    parser.add_argument("--ocr-dpi", type=int, help="Resolusi render halaman untuk OCR")
    parser.add_argument("--no-ocr", action="store_true", help="Jangan OCR halaman tanpa text layer")
    return parser


def run(args: argparse.Namespace) -> tuple[Path, dict[str, Any]]:
    source = args.source.resolve()
    files = _source_files(source)
    if not files:
        raise ValueError("Tidak ada file dengan format yang didukung di direktori sumber.")

    settings = load_extraction_settings(args.config).with_overrides(
        ocr_enabled=False if args.no_ocr else None,
        ocr_language=args.ocr_language,
        ocr_dpi=args.ocr_dpi,
    )
    documents: list[dict[str, Any]] = []
    for path in files:
        media_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        result = extract_document(path, media_type=media_type, settings=settings)
        documents.append(
            {
                "filename": path.name,
                "source_path": str(path),
                "media_type": media_type,
                **result,
            }
        )

    payload: dict[str, Any]
    if source.is_file():
        payload = documents[0]
    else:
        payload = {"source_directory": str(source), "document_count": len(documents), "documents": documents}

    output = (args.output or _default_output(source)).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return output, payload


def main() -> None:
    try:
        output, payload = run(build_parser().parse_args())
    except (FileNotFoundError, ValueError) as error:
        print(f"Gagal: {error}", file=sys.stderr)
        raise SystemExit(2) from error

    if "documents" in payload:
        question_count = sum(len(item["questions"]) for item in payload["documents"])
    else:
        question_count = len(payload["questions"])
    print(f"Selesai: {question_count} kandidat soal -> {output}")


if __name__ == "__main__":
    main()
