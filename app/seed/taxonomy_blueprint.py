"""Machine-readable blueprint for the complete 6 x 4 x 3 label space.

The 72 records are coverage cells, not validated questions or training data.
"""
from __future__ import annotations

BLOOM_LEVELS = (
    ("C1", "Mengingat"), ("C2", "Memahami"), ("C3", "Menerapkan"),
    ("C4", "Menganalisis"), ("C5", "Mengevaluasi"), ("C6", "Mencipta"),
)
KNOWLEDGE_DIMENSIONS = (
    ("FAC", "factual", "Faktual"),
    ("CON", "conceptual", "Konseptual"),
    ("PRO", "procedural", "Prosedural"),
    ("MET", "metacognitive", "Metakognitif"),
)
DIFFICULTY_LEVELS = (
    ("E", "Easy"), ("M", "Medium"), ("H", "Hard"),
)


def build_taxonomy_blueprint() -> list[dict[str, str]]:
    """Return all unique cognitive x knowledge x intended-difficulty cells."""
    return [
        {
            "cell_id": f"{bloom_code}-{knowledge_code}-{difficulty_code}",
            "bloom_label": bloom_code,
            "bloom_name": bloom_name,
            "knowledge_label": knowledge_label,
            "knowledge_name": knowledge_name,
            "difficulty_label": difficulty_label,
            "difficulty_type": "intended",
            "status": "coverage_blueprint_not_question",
        }
        for bloom_code, bloom_name in BLOOM_LEVELS
        for knowledge_code, knowledge_label, knowledge_name in KNOWLEDGE_DIMENSIONS
        for difficulty_code, difficulty_label in DIFFICULTY_LEVELS
    ]
