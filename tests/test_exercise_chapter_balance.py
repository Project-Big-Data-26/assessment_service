"""Chapter quotas must preserve qualification and retain honest N=1 confidence."""
from copy import deepcopy
import json
from pathlib import Path

import pytest

from scripts import balance_operational_difficulty as balance
from scripts import publish_operational_bank as publisher
from tests.test_operational_balance import fixture, write_bundle


def policy(rows, chapters):
    return {"version": "chapter-relative-30-40-30-v1", "groupBy": "bab_id",
            "weights": {"easy": 3, "medium": 4, "hard": 3},
            "groupsByQuestionId": {str(row["_id"]): chapter for row, chapter in zip(rows, chapters)}}


def test_each_chapter_gets_its_own_quotas_and_source_order_is_preserved():
    rows, decisions = fixture(list(range(20)), inactive=True)
    before = deepcopy((rows, decisions))
    result, audit = balance.allocate(rows, decisions, allocation_policy=policy(rows, ["a"] * 10 + ["b"] * 10))
    assert audit["groups"]["a"]["targets"] == {"easy": 3, "medium": 3, "hard": 3}
    assert audit["groups"]["b"]["targets"] == {"easy": 3, "medium": 4, "hard": 3}
    assert audit["targets"] == {"easy": 6, "medium": 7, "hard": 6}
    assert result[0] == rows[0]
    assert [row["_id"] for row in result] == [row["_id"] for row in rows]
    assert before == (rows, decisions)
    assert all(set(row) == set(original) for row, original in zip(result, rows))


def test_single_run_uses_indobert_probability_for_the_operational_label():
    rows, decisions = fixture(list(range(10)))
    for decision in decisions:
        decision["llmAdvisory"]["requestedRuns"] = 1
        decision["llmAdvisory"]["runs"] = decision["llmAdvisory"]["runs"][:1]
        decision["indobert"] = {"heads": {
            "mathCognitiveDomain": {"probabilities": {"Knowing": .7, "Applying": .2, "Reasoning": .1}},
            "knowledgeDimension": {"probabilities": {"Procedural": .9, "Factual": .1}},
            "intendedDifficulty": {"probabilities": {"Easy": .8, "Medium": .15, "Hard": .05}}}}
    result, audit = balance.allocate(rows, decisions, allocation_policy=policy(rows, ["a"] * 10))
    assert [row["confidence_score"] for row in result] == [70] * 3 + [15] * 4 + [5] * 3
    assert all(item["confidenceAvailable"] for item in audit["items"])
    for decision in decisions:
        decision["indobert"] = {"scopeStatus": "out_of_scope", "heads": {}}
    result, audit = balance.allocate(rows, decisions, allocation_policy=policy(rows, ["a"] * 10))
    assert all(row["confidence_score"] == 0 for row in result)
    assert all(item["confidenceAvailable"] is False for item in audit["items"])


@pytest.mark.parametrize("count", [0, 1, 2, 3, 4, 7, 11])
def test_small_chapters_round_deterministically_without_inventing_items(count):
    rows, decisions = fixture(list(range(count)))
    result, audit = balance.allocate(rows, decisions, allocation_policy=policy(rows, ["a"] * count))
    assert len(result) == sum(audit["targets"].values()) == count
    assert balance.allocate(rows, decisions, allocation_policy=policy(rows, ["a"] * count)) == (result, audit)
    if count == 1:
        assert result[0]["cognitive_level"] == "medium"


def test_missing_chapter_mapping_is_rejected():
    rows, decisions = fixture([1, 2])
    config = policy(rows, ["a", None])
    with pytest.raises(ValueError, match="coverage"):
        balance.allocate(rows, decisions, allocation_policy=config)


def test_weight_key_order_cannot_reverse_the_difficulty_ranking():
    rows, decisions = fixture(list(range(10)))
    config = policy(rows, ["a"] * 10)
    expected, _ = balance.allocate(rows, decisions, allocation_policy=config)
    config["weights"] = {"hard": 3, "medium": 4, "easy": 3}
    actual, _ = balance.allocate(rows, decisions, allocation_policy=config)
    assert actual == expected


def test_chapter_policy_is_verified_versioned_and_published(tmp_path, monkeypatch):
    source, bundle, _, _ = write_bundle(tmp_path, monkeypatch)
    manifest = json.loads((bundle / "manifest.json").read_text(encoding="utf-8"))
    manifest["outputs"] = {}
    (bundle / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    monkeypatch.setattr(publisher, "verify_bundle", lambda *args: None)
    monkeypatch.setattr(publisher, "load_decision_bundle", balance.load_decision_bundle)
    rows = json.loads(source.read_text(encoding="utf-8"))
    config = policy(rows, ["a"] * 3 + ["b"] * 3)
    first = balance.export_verified_operational_balance(source, bundle, grade=1, track="regular", allocation_policy=config)
    balance.verify_operational_export(Path(first["directory"]))
    publisher.publish(source, bundle, first, grade=1, track="regular")
    published = json.loads((bundle / "manifest.json").read_text(encoding="utf-8"))["databaseExport"]["operationalBalance"]
    assert published["allocationPolicy"] == config
    assert set(published["chapterDistributions"]) == {"a", "b"}
    repeat = balance.export_verified_operational_balance(source, bundle, grade=1, track="regular", allocation_policy=config)
    assert repeat["directory"] == first["directory"] and repeat["created"] is False
    changed = balance.export_verified_operational_balance(source, bundle, grade=1, track="regular",
                                                         allocation_policy=policy(rows, ["a"] * 6))
    assert changed["directory"] != first["directory"]
