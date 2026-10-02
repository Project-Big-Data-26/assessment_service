from pathlib import Path

from scripts.build_validation_bundle_kelas1 import build_decision, HEADS


def decision(action="confirm", *, bad_key=False):
    source = {"soal_text": "2 + 3 = ...", "options": [
        {"option_id": "A", "text": "5"}, {"option_id": "B", "text": "6"}
    ], "jawaban": "X" if bad_key else "A"}
    row = {"questionId": "kelas3:q", "questionVersionId": "kelas3:q:1",
           "contentVersion": 1, "contentHash": "a" * 64, "grade": 3,
           "questionType": "multiple_choice"}
    prediction = {head: {"label": "example"} for head in HEADS}
    prediction.update({"trace": {"modelVersion": "fixture"},
                       "scopeStatus": "in_scope", "reviewRequired": True})
    record = {"prediction": prediction, "serializedInput": "2+3",
              "untruncatedTokenCount": 5, "maxLength": 256,
              "wouldTruncate": False, "latencyMs": 1}
    review = {"contentStatus": "valid", "contentConcerns": []}
    review.update({head: {"action": action, "proposedLabel": None,
                          "rationale": "test", "evidenceSpans": ["2+3"]}
                   for head in HEADS})
    runs = [{"runIndex": i, "status": "success", "review": review}
            for i in range(1, 4)]
    payload = {"requestedRuns": 3, "provider": "gemini", "model": "fixture",
               "promptVersion": "fixture", "rubricVersion": "fixture"}
    return build_decision(source, row, record, {"runs": runs}, payload,
                          Path("."), "2026-10-02T00:00:00+07:00")


def test_three_abstentions_do_not_create_complete_advisory_labels():
    result = decision("abstain")
    assert result["finalRouting"] == "llm_retry_or_manual_review"
    assert result["decisionType"] == "llm_advisory_incomplete"
    assert all(label is None for label in result["llmAdvisory"]["advisoryLabels"].values())


def test_invalid_answer_key_blocks_even_unanimous_ai_votes():
    assert decision(bad_key=True)["finalRouting"] == "revision_required"


def test_complete_votes_still_require_human_review():
    result = decision()
    assert result["finalRouting"] == "pending_expert_review"
    assert result["humanValidation"]["goldLabels"] is None
