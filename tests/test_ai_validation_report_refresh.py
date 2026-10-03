"""Integrity checks must reject incomplete exports even with updated manifests."""

import json
from pathlib import Path

import pytest

from scripts.refresh_ai_validation_reports import digest, verify_bundle


def save(path, value):
    path.write_text(json.dumps(value), encoding="utf-8")


def make_bundle(tmp_path):
    source = tmp_path / "soal_pretest_db.json"
    (tmp_path / "image.png").write_bytes(b"source-image")
    save(source, [{"_id": "q1", "soal_text": "Berapa banyak?", "options": [{"option_id": "A", "text": "2"}],
                   "jawaban": "A", "image_url": ["image.png"]}])
    bundle = tmp_path / "bundle"
    bundle.mkdir()
    question = {"questionId": "q1", "stem": "Berapa banyak?", "options": [{"label": "A", "text": "2"}],
                "privateAnswerSpecification": {"answerKey": "A"}, "visualAssets": ["image.png"],
                "visualAssetHashes": {"image.png": digest(tmp_path / "image.png")}}
    save(bundle / "questions.json", {"items": [question]})
    save(bundle / "validation_results.json", {"items": [{"questionId": "q1"}]})
    save(bundle / "difficulty_groups.json", {"groups": {"Easy": [{"question": question}], "undecided": []}})
    reseal(source, bundle)
    return source, bundle


def reseal(source, bundle):
    save(bundle / "manifest.json", {
        "sourceFiles": {"source": {"path": str(source), "sha256": digest(source)}},
        "outputs": {p.name: {"sha256": digest(p), "bytes": p.stat().st_size}
                    for p in bundle.glob("*.json") if p.name != "manifest.json"},
    })


def test_complete_bundle_matches_source_and_assets(tmp_path):
    verify_bundle(*make_bundle(tmp_path))


@pytest.mark.parametrize("filename", ["questions.json", "validation_results.json"])
def test_duplicate_ids_rejected_even_after_resealing(tmp_path, filename):
    source, bundle = make_bundle(tmp_path)
    value = json.loads((bundle / filename).read_text())
    value["items"].append(value["items"][0])
    save(bundle / filename, value)
    reseal(source, bundle)
    with pytest.raises(AssertionError):
        verify_bundle(source, bundle)


def test_missing_difficulty_export_rejected_even_after_resealing(tmp_path):
    source, bundle = make_bundle(tmp_path)
    save(bundle / "difficulty_groups.json", {"groups": {"Easy": [], "undecided": []}})
    reseal(source, bundle)
    with pytest.raises(AssertionError):
        verify_bundle(source, bundle)


def test_changed_image_invalidates_report_without_source_json_change(tmp_path):
    source, bundle = make_bundle(tmp_path)
    (tmp_path / "image.png").write_bytes(b"changed-source-image")
    with pytest.raises(AssertionError):
        verify_bundle(source, bundle)
