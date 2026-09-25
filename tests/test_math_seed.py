from app.seed import build_math_seed

def test_seed_covers_bloom_and_knowledge_matrix() -> None:
    rows = build_math_seed()
    assert len(rows) == 24
    assert {row["bloom_label"] for row in rows} == {"C1", "C2", "C3", "C4", "C5", "C6"}
    assert {row["knowledge_label"] for row in rows} == {"factual", "conceptual", "procedural", "metacognitive"}
    for bloom in {"C1", "C2", "C3", "C4", "C5", "C6"}:
        assert len({row["knowledge_label"] for row in rows if row["bloom_label"] == bloom}) == 4
        assert len({row["difficulty_label"] for row in rows if row["bloom_label"] == bloom}) >= 2
