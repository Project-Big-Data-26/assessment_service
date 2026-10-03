from pathlib import Path
from app.ingestion.pretest_import import import_bab_file, next_content_version


def test_bab_import_is_immutable_and_agent_judgments_are_evidence_not_gold():
    path = Path("output/pretest/kelas1/bab01.json")
    records = import_bab_file(path)
    assert records
    first = records[0]
    assert first.questionVersionId.endswith(":v1")
    assert len(first.contentHash) == 64
    assert first.extractionEvidence["agentDifficulty"] is not None
    dumped = first.model_dump()
    assert "mathCognitiveDomain" not in dumped
    assert "knowledgeDimension" not in dumped
    assert "intendedDifficulty" not in dumped
    assert {option.label for option in first.options} == {"A", "B", "C", "D"}

    unchanged_version, _ = next_content_version(first, {
        "grade": first.grade,
        "stimulus": first.stimulus,
        "stem": first.stem,
        "options": [option.model_dump() for option in first.options],
        "answerKey": first.answerKey,
        "imageRefs": first.imageRefs,
    })
    changed_version, changed_hash = next_content_version(first, {"stem": first.stem + " Direvisi."})
    assert unchanged_version == 1
    assert changed_version == 2
    assert changed_hash != first.contentHash
