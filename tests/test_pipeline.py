from app.pipeline import QuestionIntelligencePipeline


def test_pipeline_runs_without_fabricating_a_prediction() -> None:
    result = QuestionIntelligencePipeline().run(
        {
            "question_id": "Q-TEST",
            "question_text": "  Jelaskan   proses fotosintesis. ",
        }
    )

    assert result.question_id == "Q-TEST"
    assert result.normalized_text == "Jelaskan proses fotosintesis."
    assert result.features["word_count"] == 3
    assert result.prediction.status == "not_configured"
    assert result.prediction.bloom_level is None
    assert result.prediction.difficulty_level is None
