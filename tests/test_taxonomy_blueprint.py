from collections import Counter

from app.seed.taxonomy_blueprint import build_taxonomy_blueprint


def test_blueprint_contains_all_72_unique_cells():
    records = build_taxonomy_blueprint()
    assert len(records) == 6 * 4 * 3 == 72
    assert len({record["cell_id"] for record in records}) == 72


def test_blueprint_is_balanced_across_all_three_axes():
    records = build_taxonomy_blueprint()
    assert set(Counter(record["bloom_label"] for record in records).values()) == {12}
    assert set(Counter(record["knowledge_label"] for record in records).values()) == {18}
    assert set(Counter(record["difficulty_label"] for record in records).values()) == {24}
    assert {record["status"] for record in records} == {"coverage_blueprint_not_question"}
