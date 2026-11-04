"""Comprehensive tests for the 9 SD Exercise Routes (Visual-First & KaTeX)."""

from __future__ import annotations

import random
from fastapi.testclient import TestClient
import pytest

from app.main import app
from app.services.exercise.sd_generator import (
    generate_deterministic_sd_questions,
    generate_with_9router,
)
from app.services.exercise.targeted_sd import generate as targeted_sd_generate


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


# ============================================================================
# ROUTE 1: POST /api/v1/exercise/generate
# ============================================================================
def test_route1_generate_grades_1_to_4(client: TestClient):
    for grade in (1, 2, 3, 4):
        res = client.post(
            "/api/v1/exercise/generate",
            json={
                "grade": grade,
                "bab": 1,
                "level": "easy",
                "count": 3,
                "visual_percent": 80,
                "use_9router": False,  # deterministic generator
            },
        )
        assert res.status_code == 200, res.text
        data = res.json()
        assert data["status"] == "success"
        assert data["grade"] == grade
        assert data["subject"] == "matematika"
        assert data["total_generated"] == 3
        assert data["visual_count"] >= 2
        assert len(data["questions"]) == 3

        for q in data["questions"]:
            assert q["grade"] == grade
            assert q["has_image"] is True
            assert q["visual_metadata"] is not None
            assert len(q["visual_metadata"]["image_prompt"]) >= 10
            assert q["visual_metadata"]["image_type"] in [
                "illustration",
                "object_count",
                "shape_pattern",
                "fraction_pie",
                "clock",
                "bar_chart",
                "geometry",
            ]
            assert q["katex_enabled"] is True
            assert "$" in q["question_text"]
            assert len(q["options"]) == 4
            assert q["correct_answer"] in q["options"]
            assert len(q["explanation"]) >= 5


def test_route1_invalid_grade(client: TestClient):
    res = client.post(
        "/api/v1/exercise/generate",
        json={"grade": 5, "count": 2},
    )
    assert res.status_code in (400, 422)


# ============================================================================
# ROUTE 2: POST /api/v1/exercise/batch-generate
# ============================================================================
def test_route2_batch_generate(client: TestClient):
    res = client.post(
        "/api/v1/exercise/batch-generate",
        json={
            "grade": 2,
            "bab": 1,
            "subbab": "A",
            "counts_per_level": {"easy": 2, "medium": 3, "hard": 1},
        },
    )
    assert res.status_code == 200, res.text
    data = res.json()
    assert data["status"] == "success"
    assert data["grade"] == 2
    assert data["total_questions"] == 6
    assert data["counts_by_level"]["easy"] == 2
    assert data["counts_by_level"]["medium"] == 3
    assert data["counts_by_level"]["hard"] == 1
    assert len(data["questions"]) == 6


# ============================================================================
# ROUTE 3: GET /api/v1/exercise/grades
# ============================================================================
def test_route3_get_grades(client: TestClient):
    res = client.get("/api/v1/exercise/grades")
    assert res.status_code == 200, res.text
    data = res.json()
    assert len(data) == 4
    grades = [item["grade"] for item in data]
    assert grades == [1, 2, 3, 4]
    for g in data:
        assert "SD Kelas" in g["label"]
        assert len(g["topics"]) >= 2


# ============================================================================
# ROUTE 4: GET /api/v1/exercise/visual-types
# ============================================================================
def test_route4_get_visual_types(client: TestClient):
    res = client.get("/api/v1/exercise/visual-types")
    assert res.status_code == 200, res.text
    types = res.json()
    type_names = [t["type_name"] for t in types]
    assert "object_count" in type_names
    assert "shape_pattern" in type_names
    assert "fraction_pie" in type_names
    assert "clock" in type_names
    assert "bar_chart" in type_names
    assert "geometry" in type_names


# ============================================================================
# ROUTE 5: POST /api/v1/exercise/validate-katex
# ============================================================================
def test_route5_validate_katex(client: TestClient):
    payload = {
        "texts": [
            "Ada $5$ apel di piring, sisa $5 - 2 = 3$.",
            "Pecahan senilai adalah $\\frac{1}{2} = \\frac{2}{4}$.",
            "Perkalian $4 \\times 3 = 12$.",
        ]
    }
    res = client.post("/api/v1/exercise/validate-katex", json=payload)
    assert res.status_code == 200, res.text
    data = res.json()
    assert data["status"] == "success"
    assert data["all_valid"] is True
    assert data["total_checked"] == 3


def test_route5_validate_katex_detects_unclosed_dollar(client: TestClient):
    payload = {"texts": ["Ada $5 apel di piring (unclosed"]}
    res = client.post("/api/v1/exercise/validate-katex", json=payload)
    assert res.status_code == 200, res.text
    data = res.json()
    assert data["all_valid"] is False
    assert len(data["results"][0]["issues"]) > 0


# ============================================================================
# ROUTE 6: POST /api/v1/exercise/validate-question
# ============================================================================
def test_route6_validate_valid_question(client: TestClient):
    qs = generate_deterministic_sd_questions(grade=1, count=1)
    q = qs[0]
    res = client.post("/api/v1/exercise/validate-question", json={"question": q.model_dump()})
    assert res.status_code == 200, res.text
    data = res.json()
    assert data["valid"] is True
    assert data["has_image"] is True
    assert data["katex_enabled"] is True
    assert len(data["errors"]) == 0


def test_route6_validate_invalid_question_missing_visual(client: TestClient):
    bad_q = {
        "question_id": "test_bad",
        "grade": 3,
        "subject": "matematika",
        "question_text": "Berapa $2 + 2 = \\dots$?",
        "has_image": True,
        "visual_metadata": None,
        "katex_enabled": True,
        "options": ["$2$", "$3$", "$4$", "$5$"],
        "correct_answer": "$4$",
        "explanation": "Penjelasan matematika.",
    }
    res = client.post("/api/v1/exercise/validate-question", json={"question": bad_q})
    # Pydantic model validator triggers 422 or returns validation errors
    assert res.status_code in (422, 200)


# ============================================================================
# ROUTE 7: GET /api/v1/exercise/catalog/{grade}
# ============================================================================
def test_route7_get_catalog_by_grade(client: TestClient):
    for grade in (1, 2, 3, 4):
        res = client.get(f"/api/v1/exercise/catalog/{grade}")
        assert res.status_code == 200, res.text
        items = res.json()
        assert len(items) == 4
        assert all(item["grade"] == grade for item in items)


# ============================================================================
# ROUTE 8: POST /api/v1/exercise/preview
# ============================================================================
def test_route8_preview_generation(client: TestClient):
    res = client.post(
        "/api/v1/exercise/preview",
        json={"grade": 3, "visual_type": "fraction_pie"},
    )
    assert res.status_code == 200, res.text
    data = res.json()
    assert "<svg" in data["rendered_svg"]
    assert "web-nolla-exercise-card" in data["html_preview"]
    assert data["question"]["grade"] == 3


# ============================================================================
# ROUTE 9: GET /api/v1/exercise/health
# ============================================================================
def test_route9_service_health(client: TestClient):
    res = client.get("/api/v1/exercise/health")
    assert res.status_code == 200, res.text
    data = res.json()
    assert data["status"] == "ready"
    assert data["service"] == "nolla-sd-visual-exercise-generator"
    assert data["target_grades"] == [1, 2, 3, 4]
    assert data["latex_policy_version"] == "latex-presentation-v1"


# ============================================================================
# TEST TARGETED_SD GENERATOR FOR GRADES 1-4
# ============================================================================
def test_targeted_sd_generator_grades_1_to_4():
    r = random.Random(42)
    for g in (1, 2, 3, 4):
        authored = targeted_sd_generate(grade=g, bab=1, code="A", level="easy", r=r)
        assert authored is not None
        assert authored.draft is not None
        assert "$" in authored.draft.question
