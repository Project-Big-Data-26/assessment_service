
import pytest

from app.assessment.contracts import AssessmentCreate
from app.assessment.store import AssessmentError, AssessmentStore
from app.classification.v2.serializer import canonical_json_hash
from app.psychometrics.analysis import load_policy
from app.psychometrics.contracts import ScreeningInput
from app.silver.policy import qualification, resolve_answer_key
from app.training.v2.dataset import build_snapshot
from tests.test_assessment_empirical_flow import silver_snapshot, complete_attempt


@pytest.mark.parametrize("raw,text", [
    ("5", "$5$"), ("512", "512 cara"), ("21", "21 kupon"),
    ("18", "$18$ satuan luas"), ("10/125", "10/125 (atau 0,08)"),
    ("Gambar 2 (segi enam) adalah jawaban.", "Gambar 2 (segi enam memanjang)"),
])
def test_ai_answer_is_mapped_to_a_unique_source_option(raw, text):
    assert resolve_answer_key(raw, [{"option_id": "A", "text": "Tidak cocok"},
                                    {"option_id": "B", "text": text}]) == "B"


def test_ambiguous_or_unknown_answer_is_not_assigned_an_option():
    assert resolve_answer_key("5", [{"option_id": "A", "text": "5"},
                                    {"option_id": "B", "text": "$5$"}]) is None
    assert resolve_answer_key("Mungkin yang kedua", [{"option_id": "A", "text": "5"}]) is None


def test_report_qualification_holds_ai_answer_that_disagrees_with_the_source_key():
    question = {"options": [{"option_id": "A", "text": "5"}, {"option_id": "B", "text": "6"}], "jawaban": "A"}
    record = {"aggregate": {"eligibleForTraining": True, "contentStatus": "valid",
                           "answerKeyStatus": "verified", "verifiedAnswerKey": "6",
                           "verifiedMinimalSolution": "A solution was provided.",
                           "heads": {"mathCognitiveDomain": {"label": "applying"},
                                     "knowledgeDimension": {"label": "procedural"},
                                     "intendedDifficulty": {"label": "Medium"}}}}
    labels, route = qualification(record, {"status": "pass"}, question)
    assert route == "needs_ai_review" and labels["intendedDifficulty"] == "Medium"


def test_tl_delivery_checks_track_and_expansion_integrity(tmp_path):
    rows = [r.model_copy(update={"grade": 11, "subjectTrack": "tl"}) for r in silver_snapshot().rows]
    snapshot = build_snapshot(rows, snapshot_id="tl-silver", required_grades=())
    db = AssessmentStore(tmp_path / "tl.sqlite3")
    db.register_snapshot(snapshot)
    payload = AssessmentCreate(assessmentId="tl-pilot", snapshotId=snapshot.snapshotId,
                               questionVersionIds=[r.questionVersionId for r in rows],
                               populationId="tl-pop", assessmentFamily="math-tl", grade=11, subjectTrack="tl")
    assert db.create_assessment(payload, snapshot)["itemCount"] == 5
    with pytest.raises(AssessmentError, match="outside"):
        db.create_assessment(payload.model_copy(update={"subjectTrack": "regular"}), snapshot)
    snapshot.expansionRows[0].stem = "Modified after freezing"
    with pytest.raises(AssessmentError, match="expansion checksum"):
        db.register_snapshot(snapshot)


def test_silver_registration_rejects_missing_blind_evidence_after_rehash(tmp_path):
    snapshot = silver_snapshot()
    snapshot.rows[0].decisionProvenance["sourceResponseHashes"] = ["a" * 64]
    snapshot.snapshotHash = canonical_json_hash([r.model_dump(mode="json") for r in snapshot.rows])
    with pytest.raises(AssessmentError, match="three response hashes"):
        AssessmentStore(tmp_path / "bad.sqlite3").register_snapshot(snapshot)


def test_silver_registry_id_is_immutable_even_with_valid_content_checksum(tmp_path):
    db = AssessmentStore(tmp_path / "registry.sqlite3")
    snapshot = silver_snapshot()
    receipt = db.register_snapshot(snapshot)
    assert db.register_snapshot(snapshot) == receipt
    changed = snapshot.model_copy(deep=True)
    changed.rows[0].decisionProvenance["decisionId"] = "another-ai-decision"
    changed.snapshotHash = canonical_json_hash([r.model_dump(mode="json") for r in changed.rows])
    with pytest.raises(AssessmentError, match="immutable silver"):
        db.register_snapshot(changed)


def test_negative_discrimination_automatically_holds_delivery_without_relabeling(tmp_path):
    db = AssessmentStore(tmp_path / "feedback.sqlite3")
    snapshot = silver_snapshot()
    payload = AssessmentCreate(assessmentId="pilot-1", snapshotId=snapshot.snapshotId,
                               questionVersionIds=[r.questionVersionId for r in snapshot.rows],
                               populationId="pop", assessmentFamily="math", grade=1)
    db.create_assessment(payload, snapshot)
    for i in range(60):
        high = int(i % 2 == 0)
        complete_attempt(db, f"synthetic-{i}", 1, [1 - high, high, high, high, high])
        complete_attempt(db, f"synthetic-{i}", 2, [high] * 5)
    result = db.screen(ScreeningInput(assessmentId="pilot-1"), load_policy())
    assert "negative_discrimination" in result["items"][0]["reviewFlags"]
    decision = next(d for d in db.decisions(result["snapshotId"]) if d["questionVersionId"] == "q-0:v2")
    assert decision["actorType"] == "system" and decision["action"] == "needs_ai_review"
    assert decision["affectsSilverLabels"] is False
    assert result["items"][0]["intendedDifficulty"] == "Medium"
    assert db.is_held("q-0:v2")
    with pytest.raises(AssessmentError, match="held"):
        db.create_assessment(payload.model_copy(update={"assessmentId": "another-pilot"}), snapshot)
    token = db.participant("pilot-1", "blocked-student")["participantToken"]
    session = db.start("pilot-1", token, "blocked-session-1")
    with pytest.raises(AssessmentError, match="held"):
        db.next_item(session["sessionId"], token)
    # Improved follow-up statistics do not qualify the content/key again.
    followup = db.screen(ScreeningInput(assessmentId="pilot-1", attemptPolicy="last"), load_policy())
    assert followup["items"][0]["recommendedRouting"] == "observation_only"
    decision = next(d for d in db.decisions(followup["snapshotId"]) if d["questionVersionId"] == "q-0:v2")
    assert decision["action"] == "needs_ai_review" and db.is_held("q-0:v2")
