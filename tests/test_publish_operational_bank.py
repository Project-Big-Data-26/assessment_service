from copy import deepcopy
import json

import pytest

from scripts import balance_operational_difficulty as balance
from scripts import publish_operational_bank as publisher
from app.silver.exports import ai_validation_path
from tests.test_operational_balance import write_bundle


def fixture(tmp_path, monkeypatch):
    source, bundle, evidence, _ = write_bundle(tmp_path, monkeypatch)
    manifest = json.loads((bundle / "manifest.json").read_text(encoding="utf-8"))
    manifest["outputs"] = {"validation_results.json": publisher.info((bundle / "validation_results.json").read_bytes())}
    (bundle / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    monkeypatch.setattr(publisher, "verify_bundle", lambda *args: None)
    monkeypatch.setattr(publisher, "load_decision_bundle", balance.load_decision_bundle)
    version = balance.export_verified_operational_balance(source, bundle, grade=1, track="regular")
    return source, bundle, evidence, version


def test_active_array_is_balanced_and_original_ai_is_preserved_on_repeat(tmp_path, monkeypatch):
    source, bundle, evidence, version = fixture(tmp_path, monkeypatch)
    before_source = source.read_bytes()
    before_ai = (bundle / "validation_results.json").read_bytes()
    before_evidence = evidence.read_bytes()
    result = publisher.publish(source, bundle, version, grade=1, track="regular")
    assert result["activeDistribution"] == {"easy": 2, "medium": 2, "hard": 1}
    originals = json.loads(before_ai)
    active = json.loads((bundle / "validation_results.json").read_text(encoding="utf-8"))
    assert active[0] == originals[0]  # Inactive content is never promoted.
    assert any(r["cognitive_level"] == "hard" and r["confidence_score"] == 0 for r in active)
    assert ai_validation_path(bundle).read_bytes() == before_ai
    assert source.read_bytes() == before_source and evidence.read_bytes() == before_evidence
    before = {p: p.read_bytes() for p in bundle.rglob("*") if p.is_file()}
    publisher.publish(source, bundle, version, grade=1, track="regular")
    assert {p: p.read_bytes() for p in before} == before


def test_ai_archive_checksum_is_enforced(tmp_path, monkeypatch):
    source, bundle, _, version = fixture(tmp_path, monkeypatch)
    publisher.publish(source, bundle, version, grade=1, track="regular")
    (bundle / "ai_validation_results.json").write_text("[]", encoding="utf-8")
    with pytest.raises(ValueError, match="checksum"):
        ai_validation_path(bundle)


def test_failed_publication_rolls_back_array_and_manifest(tmp_path, monkeypatch):
    source, bundle, _, version = fixture(tmp_path, monkeypatch)
    old_array = (bundle / "validation_results.json").read_bytes()
    old_manifest = (bundle / "manifest.json").read_bytes()
    calls = []

    def verify(*args):
        calls.append(args)
        if len(calls) == 2:
            raise ValueError("failed final verification")

    monkeypatch.setattr(publisher, "verify_bundle", verify)
    with pytest.raises(ValueError, match="failed final"):
        publisher.publish(source, bundle, version, grade=1, track="regular")
    assert (bundle / "validation_results.json").read_bytes() == old_array
    assert (bundle / "manifest.json").read_bytes() == old_manifest


def test_stale_version_is_rejected_before_any_active_write(tmp_path, monkeypatch):
    source, bundle, _, version = fixture(tmp_path, monkeypatch)
    rows = json.loads((bundle / "validation_results.json").read_text(encoding="utf-8"))
    rows[1]["confidence_score"] = 0
    (bundle / "validation_results.json").write_text(json.dumps(rows), encoding="utf-8")
    old = (bundle / "validation_results.json").read_bytes()
    with pytest.raises(ValueError, match="stale"):
        publisher.publish(source, bundle, version, grade=1, track="regular")
    assert (bundle / "validation_results.json").read_bytes() == old
    assert not (bundle / "ai_validation_results.json").exists()
