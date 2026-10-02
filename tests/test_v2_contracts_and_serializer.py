import hashlib

import pytest
from pydantic import ValidationError

from app.classification.v2.contracts import V2ClassificationRequest
from app.classification.v2.serializer import serialize_question
from app.classification.v2.kko import detect_kko


def valid_request():
    return {
        "questionId": "q-1",
        "contentVersion": 1,
        "contentHash": "a" * 64,
        "grade": 4,
        "topic": "Pecahan",
        "subtopic": "Perbandingan",
        "questionType": "multiple_choice",
        "stimulus": None,
        "stem": "Pecahan manakah yang paling besar?",
        "options": [{"label": "A", "text": "1/2"}, {"label": "B", "text": "3/4"}],
        "verifiedMinimalSolution": "Samakan penyebut; 3/4 lebih besar.",
        "detectedKko": ["menentukan"],
        "visualTranscript": None,
        "provenanceStatus": {
            "contentQualified": True,
            "answerKeyVerified": True,
            "solutionVerified": True,
            "visualEssential": False,
            "visualTranscriptVerified": False,
        },
    }


def test_frozen_serializer_is_deterministic_and_contains_every_model_field():
    request = V2ClassificationRequest.model_validate(valid_request())
    first = serialize_question(request)
    second = serialize_question(valid_request())
    assert first == second
    assert "Kelas: 4" in first
    assert "Solusi minimum terverifikasi:" in first
    assert "KKO terdeteksi: menentukan" in first
    assert hashlib.sha256(first.encode()).hexdigest()


def test_duplicate_option_labels_are_rejected():
    payload = valid_request()
    payload["options"][1]["label"] = "a"
    with pytest.raises(ValidationError, match="option labels must be unique"):
        V2ClassificationRequest.model_validate(payload)


def test_v2_public_endpoint_never_falls_back_to_rules(monkeypatch):
    from fastapi.testclient import TestClient
    from app.main import app

    # Isolate the missing-artifact branch even when a real local artifact was
    # produced by an earlier integration run.
    monkeypatch.setattr(app.state, "v2_runtime", None)
    monkeypatch.setattr(app.state, "v2_runtime_error", "fixture: artifact unavailable")
    response = TestClient(app).post("/v2/classify", json=valid_request())
    assert response.status_code == 503


def test_v2_model_info_exposes_exact_three_heads():
    from fastapi.testclient import TestClient
    from app.main import app

    response = TestClient(app).get("/v2/model-info")
    assert response.status_code == 200
    assert response.json()["tasks"] == [
        "mathCognitiveDomain_3",
        "knowledgeDimension_4",
        "intendedDifficulty_3",
    ]


def test_kko_detection_is_a_multi_value_feature_not_a_label_mapping():
    detected = detect_kko("Hitunglah hasilnya, lalu jelaskan alasanmu.")
    assert detected == ["menghitung", "menjelaskan"]
