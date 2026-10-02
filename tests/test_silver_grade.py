from app.llm.silver import (
    SilverAdjudicationResult,
    SilverLabelOutput,
    SilverRunResult,
    aggregate_silver_runs,
    build_silver_prompt,
)
import pytest
import re


@pytest.mark.parametrize("grade", [2, 3, 7, 8, 9, 10, 11, 12])
def test_silver_prompt_uses_the_actual_grade_for_difficulty(grade):
    item = {"_id": "q", "options": [], "soal_text": "12 x 3 = ..."}
    prompt = build_silver_prompt(item, grade=grade)
    assert f"matematika kelas {grade}" in prompt
    assert f"bagi siswa kelas {grade}" in prompt
    assert not re.search(r"\bkelas 1\b", prompt)
    assert "PREDIKSI INDOBERT" not in prompt
    assert "tingkat_kesulitan" not in prompt
    assert "agentDifficulty" not in prompt
    assert "verifiedMinimalSolution" in prompt
    assert "answerKeyStatus=verified" in prompt


@pytest.mark.parametrize("grade", [-1, 0, 13, 15])
def test_silver_rejects_an_unsupported_grade(grade):
    with pytest.raises(ValueError, match="grade 1-6"):
        build_silver_prompt({}, grade=grade)


def silver_output(difficulty: str) -> SilverLabelOutput:
    head = {
        "action": "classify",
        "evidenceSpans": ["Hitung 2 + 3"],
        "rationale": "Bukti cukup untuk klasifikasi.",
    }
    return SilverLabelOutput.model_validate(
        {
            "contentStatus": "valid",
            "contentConcerns": [],
            "answerKeyStatus": "verified",
            "verifiedAnswerKey": "B",
            "visualTranscript": None,
            "verifiedMinimalSolution": "2 + 3 = 5.",
            "mathCognitiveDomain": {**head, "label": "knowing"},
            "knowledgeDimension": {**head, "label": "factual"},
            "intendedDifficulty": {
                **head,
                "label": difficulty,
                "profile": {
                    "expectedPrerequisite": "Penjumlahan bilangan kecil.",
                    "dependentSteps": 1,
                    "routineStatus": "familiar_routine",
                    "strategySelection": False,
                    "representationTransfer": False,
                    "relevantInformationUnits": 2,
                    "interactingConstraints": 0,
                    "calculationLoad": "low",
                    "scaffoldLevel": "none",
                    "distractorQuality": "plausible",
                    "gradeRelativeRationale": "Langsung untuk kelas sasaran.",
                },
            },
        }
    )


def test_silver_requires_unanimity_or_separate_adjudication():
    runs = [
        SilverRunResult(runIndex=1, status="success", output=silver_output("Easy"), latencyMs=1),
        SilverRunResult(runIndex=2, status="success", output=silver_output("Easy"), latencyMs=1),
        SilverRunResult(runIndex=3, status="success", output=silver_output("Medium"), latencyMs=1),
    ]
    pending = aggregate_silver_runs(runs)
    assert pending["needsAdjudication"] is True
    assert pending["eligibleForTraining"] is False
    adjudication = SilverAdjudicationResult(
        status="success", output=silver_output("Medium"), latencyMs=1
    )
    resolved = aggregate_silver_runs(runs, adjudication)
    assert resolved["adjudicated"] is True
    assert resolved["heads"]["intendedDifficulty"]["label"] == "Medium"
    assert resolved["eligibleForTraining"] is True


def test_three_way_label_conflict_waits_for_adjudication():
    runs = [
        SilverRunResult(
            runIndex=index,
            status="success",
            output=silver_output(label),
            latencyMs=1,
        )
        for index, label in enumerate(("Easy", "Medium", "Hard"), start=1)
    ]
    aggregate = aggregate_silver_runs(runs)
    assert aggregate["heads"]["intendedDifficulty"]["label"] is None
    assert aggregate["heads"]["intendedDifficulty"]["status"] == "needs_adjudication"
    assert aggregate["eligibleForTraining"] is False


def test_content_concern_is_not_training_eligible_even_when_votes_are_unanimous():
    output = silver_output("Easy").model_copy(update={"contentStatus": "concern"})
    runs = [
        SilverRunResult(runIndex=index, status="success", output=output, latencyMs=1)
        for index in (1, 2, 3)
    ]
    aggregate = aggregate_silver_runs(runs)
    assert aggregate["heads"]["intendedDifficulty"]["status"] == "unanimous"
    assert aggregate["eligibleForTraining"] is False


def test_three_zero_is_directly_eligible_but_provider_failure_is_not():
    successful = [
        SilverRunResult(
            runIndex=index,
            status="success",
            output=silver_output("Hard"),
            latencyMs=1,
        )
        for index in (1, 2, 3)
    ]
    unanimous = aggregate_silver_runs(successful)
    assert unanimous["needsAdjudication"] is False
    assert unanimous["heads"]["intendedDifficulty"]["label"] == "Hard"
    assert unanimous["eligibleForTraining"] is True

    failed = SilverRunResult(
        runIndex=3,
        status="failed",
        errorCode="ClientError:429",
        latencyMs=1,
    )
    incomplete = aggregate_silver_runs([successful[0], successful[1], failed])
    assert incomplete["successfulRuns"] == 2
    assert incomplete["needsAdjudication"] is True
    assert incomplete["eligibleForTraining"] is False


def test_abstain_and_answer_key_conflict_require_adjudication():
    abstained_payload = silver_output("Easy").model_dump(mode="json")
    abstained_payload["intendedDifficulty"] = {
        "action": "abstain",
        "label": None,
        "evidenceSpans": [],
        "rationale": "Informasi tidak cukup.",
        "profile": None,
    }
    abstained = SilverLabelOutput.model_validate(abstained_payload)
    abstain_runs = [
        SilverRunResult(runIndex=index, status="success", output=abstained, latencyMs=1)
        for index in (1, 2, 3)
    ]
    assert aggregate_silver_runs(abstain_runs)["needsAdjudication"] is True

    conflict = silver_output("Easy").model_copy(
        update={"answerKeyStatus": "conflict", "verifiedAnswerKey": "A"}
    )
    conflict_runs = [
        SilverRunResult(runIndex=index, status="success", output=conflict, latencyMs=1)
        for index in (1, 2, 3)
    ]
    conflict_result = aggregate_silver_runs(conflict_runs)
    assert conflict_result["answerKeyStatus"] == "conflict"
    assert conflict_result["needsAdjudication"] is True
    assert conflict_result["eligibleForTraining"] is False
