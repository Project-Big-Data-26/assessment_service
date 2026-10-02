from __future__ import annotations

import hashlib
import json
from datetime import datetime, timedelta, timezone

import pytest

from app.llm.silver import RUBRIC_VERSION, SILVER_PROMPT_VERSION, rubric_file_hash
from scripts.audit_grade_aware_pilot import audit, input_hash
from scripts.compare_blind_labels_to_predictions import compare
from tests.test_silver_grade import silver_output


def question(identifier: str) -> dict:
    return {
        "_id": identifier,
        "subbab_id": "Bilangan",
        "soal_type": "Pilihan Ganda",
        "soal_text": "Hitung 2 + 3.",
        "options": [
            {"option_id": "A", "text": "4", "alasan": None},
            {"option_id": "B", "text": "5", "alasan": None},
        ],
        "jawaban": "B",
        "image_url": [],
    }


def record(item: dict) -> dict:
    output = silver_output("Easy").model_dump(mode="json")
    return {
        "questionId": item["_id"],
        "inputHash": input_hash(item),
        "runs": [
            {
                "runIndex": index,
                "status": "success",
                "output": output,
                "promptHash": f"prompt-{index}",
                "responseHash": f"response-{index}",
            }
            for index in (1, 2, 3)
        ],
        "adjudication": None,
        "aggregate": {
            "contentStatus": "valid",
            "eligibleForTraining": True,
            "heads": {
                "mathCognitiveDomain": {"label": "knowing", "status": "unanimous"},
                "knowledgeDimension": {"label": "factual", "status": "unanimous"},
                "intendedDifficulty": {"label": "Easy", "status": "unanimous"},
            },
        },
    }


def test_partial_pilot_uses_expected_60_style_denominator(tmp_path):
    questions = [question("q-1"), question("q-2")]
    source = tmp_path / "questions.json"
    source.write_text(json.dumps(questions), encoding="utf-8")
    checkpoint = tmp_path / "silver.json"
    checkpoint.write_text(
        json.dumps(
            {
                "sourceHash": hashlib.sha256(source.read_bytes()).hexdigest(),
                "promptVersion": SILVER_PROMPT_VERSION,
                "rubricVersion": RUBRIC_VERSION,
                "rubricHash": rubric_file_hash(),
                "items": {"q-1": record(questions[0])},
            }
        ),
        encoding="utf-8",
    )
    report = audit(source, checkpoint, grade=1)
    assert report["expectedItemCount"] == 2
    assert report["itemCount"] == 1
    assert report["threeSuccessfulRunsShare"] == 0.5
    assert report["insufficientOrAbstainedShare"] == 0.5
    assert report["gates"]["allExpectedItemsPresent"] is False
    assert report["readyForExpansion"] is False


def test_prediction_comparison_requires_a_prior_matching_blind_lock():
    item = question("q-1")
    silver = {"items": {"q-1": record(item)}}
    locked_at = datetime.now(timezone.utc)
    audit_payload = {
        "generatedAt": locked_at.isoformat(),
        "checkpointLockedByAudit": True,
        "checkpointSha256": "silver-hash",
        "gates": {
            "blindPromptLeakageAbsent": True,
            "checkpointSourceAndInputsMatch": True,
        },
    }
    predictions = {
        "createdAt": (locked_at + timedelta(seconds=1)).isoformat(),
        "model": {"modelVersion": "fixture-v2"},
        "items": [
            {
                "questionId": "q-1",
                "prediction": {
                    "mathCognitiveDomain": {"label": "knowing"},
                    "knowledgeDimension": {"label": "conceptual"},
                    "intendedDifficulty": {"label": "Easy"},
                },
            }
        ],
    }
    result = compare(
        silver,
        predictions,
        audit_payload,
        silver_hash="silver-hash",
        predictions_hash="prediction-hash",
        audit_hash="audit-hash",
    )
    assert result["comparisonPerformedAfterBlindLock"] is True
    assert result["summary"]["agreement"]["intendedDifficulty"]["rate"] == 1.0
    assert result["summary"]["agreement"]["knowledgeDimension"]["rate"] == 0.0

    predictions["createdAt"] = (locked_at - timedelta(seconds=1)).isoformat()
    with pytest.raises(ValueError, match="after blind labels are locked"):
        compare(
            silver,
            predictions,
            audit_payload,
            silver_hash="silver-hash",
            predictions_hash="prediction-hash",
            audit_hash="audit-hash",
        )
