import json

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_model_info_exposes_three_tasks_and_honest_runtime_status():
    response = client.get("/v1/model-info")
    assert response.status_code == 200
    assert response.json()["tasks"] == ["bloom_6", "knowledge_4", "difficulty_3"]
    assert response.json()["classifier"] in {"RuleBasedBaselineClassifier", "IndoBERTClassifier"}
    if response.json()["classifier"] == "RuleBasedBaselineClassifier":
        assert response.json()["artifact_ready"] is False
        assert response.json()["provisional_eligible"] is False


def test_extraction_info_reports_pdf_runtime_and_supported_formats():
    response = client.get("/v1/extraction-info")

    assert response.status_code == 200
    assert response.json()["pymupdf_ready"] is True
    assert ".pdf" in response.json()["supported_extensions"]


def test_classification_requires_human_review_for_baseline():
    response = client.post("/v1/classify", json={
        "question_id": "API-1",
        "question_text": "Analisislah hubungan antara gradien dan arah sebuah garis lurus.",
        "subject": "Matematika",
        "grade": 10,
    })
    assert response.status_code == 200
    assert response.json()["bloom"]["label"] == "C4"
    assert response.json()["review_required"] is True


def test_json_upload_is_parsed_without_disk_locking():
    payload = json.dumps([{"question_text": "Hitung $2+2$.", "options": ["3", "4"]}]).encode()
    response = client.post("/v1/extract", files={"file": ("questions.json", payload, "application/json")})
    assert response.status_code == 200
    assert "Hitung" in response.json()["extracted_text"]
    assert response.json()["latex_candidates"] == ["2+2"]
    assert len(response.json()["pages"]) == 1
    assert len(response.json()["questions"]) == 1


def test_pdf_upload_returns_platform_ready_question_image():
    import pymupdf

    document = pymupdf.open()
    page = document.new_page()
    page.insert_text((72, 72), "1. Hitung 8 + 5.\nA. 12\nB. 13")
    payload = document.tobytes()
    document.close()

    response = client.post(
        "/v1/extract",
        files={"file": ("question.pdf", payload, "application/pdf")},
    )

    assert response.status_code == 200
    preview = response.json()["questions"][0]["visual_previews"][0]
    assert preview["mime_type"] in {"image/webp", "image/png"}
    assert preview["data_url"].startswith(f'data:{preview["mime_type"]};base64,')
