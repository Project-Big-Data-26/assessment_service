from concurrent.futures import ThreadPoolExecutor
import json

from fastapi.testclient import TestClient
import numpy as np
import pytest

from app.assessment.contracts import AssessmentCreate, ResponseCreate
from app.assessment.store import AssessmentError, AssessmentStore
from app.classification.v2.serializer import canonical_json_hash
from app.main import app
from app.staff.security import SESSION_COOKIE, hash_secret, password_hash
from app.psychometrics.analysis import load_policy
from app.psychometrics.contracts import ScreeningInput
from app.training.v2.dataset import TrainingRow, build_snapshot


def silver_snapshot():
    rows = [TrainingRow(
        questionId=f"q-{i}", questionVersionId=f"q-{i}:v2", contentVersion=2,
        contentHash=canonical_json_hash({"content": i}), sourceGroup=f"source-{i}", grade=1, topic="Bilangan",
        questionType="multiple_choice", stem=f"Hitung {i} + 1.",
        options=[{"label": "A", "text": str(i + 1)}, {"label": "B", "text": str(i + 2)}],
        verifiedMinimalSolution=f"{i} + 1 = {i + 1}", mathCognitiveDomain="knowing", knowledgeDimension="procedural",
        intendedDifficulty="Medium", rubricVersion="math-rubric-3x4x3-v2",
        decisionProvenance={"decisionId": f"ai-{i}", "kind": "ai_silver", "verifiedAnswerKey": "A", "successfulRuns": 3,
                            "contentStatus": "valid", "answerKeyStatus": "verified", "checkpointHash": "a" * 64,
                            "sourceInputHash": "b" * 64, "sourceResponseHashes": ["c" * 64] * 3},
    ) for i in range(5)]
    return build_snapshot(rows, snapshot_id="ai-silver-test", minimum_per_class=0, minimum_train_per_class=0, required_grades=())


@pytest.fixture
def local_store(tmp_path):
    db = AssessmentStore(tmp_path / "pilot.sqlite3")
    snapshot = silver_snapshot()
    config = AssessmentCreate(assessmentId="pilot-1", snapshotId=snapshot.snapshotId,
                              questionVersionIds=[row.questionVersionId for row in snapshot.rows],
                              populationId="grade-1-school-1", assessmentFamily="math-grade-1", grade=1)
    db.create_assessment(config, snapshot)
    return db


@pytest.fixture
def api(local_store, monkeypatch):
    monkeypatch.setattr(app.state, "assessment_store", local_store)
    monkeypatch.setenv("PSYCHOMETRICS_API_TOKEN", "internal-secret-token-for-tests-123456")
    return TestClient(app)


def headers(token, key=None):
    result = {"Authorization": f"Bearer {token}"}
    if key:
        result["Idempotency-Key"] = key
    return result


def test_delivery_scoring_retry_privacy_and_skipped_missing(api, local_store):
    token = local_store.participant("pilot-1", "participant-1")["participantToken"]
    auth = headers(token, "start-key-1")
    session = api.post("/api/v1/assessments/pilot-1/sessions", headers=auth).json()
    assert api.post("/api/v1/assessments/pilot-1/sessions", headers=auth).json() == session
    sid = session["sessionId"]
    next_url = f"/api/v1/sessions/{sid}/items/next"
    item = api.get(next_url, headers=headers(token)).json()
    assert api.get(next_url, headers=headers(token)).json() == item
    encoded = json.dumps(item)
    assert all(secret not in encoded for secret in ("answerKey", "verifiedMinimalSolution", "contentHash", "intendedDifficulty", "questionVersionId"))
    assert api.post(f"/api/v1/sessions/{sid}/complete", headers=headers(token, "complete-key")).status_code == 409
    response_id = "response-key-1"
    answer = {"responseId": response_id, "deliveryInstanceId": item["deliveryInstanceId"],
              "selectedOptionIds": [item["item"]["options"][0]["id"]], "responseTimeMs": 40000}
    forged = {**answer, "isCorrect": True}
    assert api.post("/api/v1/responses", json=forged, headers=headers(token, response_id)).status_code == 422
    accepted = api.post("/api/v1/responses", json=answer, headers=headers(token, response_id))
    assert accepted.status_code == 201
    assert "scoring" not in accepted.json()
    assert api.post("/api/v1/responses", json=answer, headers=headers(token, response_id)).json() == accepted.json()
    assert api.post("/api/v1/responses", json={**answer, "responseTimeMs": 123}, headers=headers(token, response_id)).status_code == 409
    for i in range(1, 5):
        item = api.get(next_url, headers=headers(token)).json()
        rid = f"response-key-{i + 1}"
        skipped = {"responseId": rid, "deliveryInstanceId": item["deliveryInstanceId"], "skipped": True, "responseTimeMs": 1000}
        assert api.post("/api/v1/responses", json=skipped, headers=headers(token, rid)).status_code == 201
    assert api.post(f"/api/v1/sessions/{sid}/complete", headers=headers(token, "complete-key")).status_code == 200
    assert api.post(f"/api/v1/sessions/{sid}/complete", headers=headers(token, "complete-key")).status_code == 200
    with local_store.connection() as db:
        events = [json.loads(row[0]) for row in db.execute("SELECT document FROM responses")]
    assert all("participant-1" not in json.dumps(event) for event in events)
    assert sum(event["isCorrect"] is None for event in events) == 4
    assert {event["contentVersion"] for event in events} == {2}


def test_idor_invalid_mapping_and_internal_auth(api, local_store):
    token = local_store.participant("pilot-1", "student-a")["participantToken"]
    other = local_store.participant("pilot-1", "student-b")["participantToken"]
    session = local_store.start("pilot-1", token, "session-key-a")
    item = local_store.next_item(session["sessionId"], token)
    assert api.get(f"/api/v1/sessions/{session['sessionId']}/items/next", headers=headers(other)).status_code == 404
    answer = {"responseId": "response-a", "deliveryInstanceId": item["deliveryInstanceId"], "selectedOptionIds": ["A"], "responseTimeMs": 2}
    assert api.post("/api/v1/responses", json=answer, headers=headers(token, "response-a")).status_code == 422
    assert api.post("/api/v1/responses", json=answer, headers=headers(other, "response-a")).status_code == 404
    assert api.get("/api/v1/sessions/unknown/items/next").status_code == 401
    assert api.post("/api/v1/internal/psychometrics/screen", json={"assessmentId": "pilot-1"}, headers={"X-Internal-API-Key": "bad"}).status_code == 401


def test_qualified_silver_is_delivered_and_modified_snapshot_is_rejected(local_store):
    snapshot = silver_snapshot()
    payload = AssessmentCreate(assessmentId="new-pilot", snapshotId=snapshot.snapshotId,
                               questionVersionIds=[row.questionVersionId for row in snapshot.rows], populationId="p", assessmentFamily="f", grade=1)
    assert local_store.create_assessment(payload, snapshot)["itemCount"] == 5
    with pytest.raises(AssessmentError, match="AI silver"):
        local_store.create_assessment(payload, snapshot.model_copy(update={"labelProvenance": "unqualified"}))
    snapshot.rows[0].stem = "Changed after freeze"
    with pytest.raises(AssessmentError, match="checksum"):
        local_store.create_assessment(payload, snapshot)


def test_concurrent_next_item_returns_one_immutable_delivery(local_store):
    token = local_store.participant("pilot-1", "student-c")["participantToken"]
    sid = local_store.start("pilot-1", token, "start-concurrent")["sessionId"]
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(lambda _: local_store.next_item(sid, token), range(4)))
    assert all(item == results[0] for item in results)


def complete_attempt(db, code, attempt, outcomes):
    token = db.participant("pilot-1", code)["participantToken"]
    sid = db.start("pilot-1", token, f"attempt-{attempt:04d}")["sessionId"]
    for index, correct in enumerate(outcomes):
        item = db.next_item(sid, token)
        with db.connection() as connection:
            private = json.loads(connection.execute("SELECT document FROM deliveries WHERE id=?", (item["deliveryInstanceId"],)).fetchone()[0])
        chosen = next(public for public, internal in private["mapping"].items() if (internal == "A") == bool(correct))
        db.respond(ResponseCreate(responseId=f"response-{sid}-{index}", deliveryInstanceId=item["deliveryInstanceId"], selectedOptionIds=[chosen], responseTimeMs=30000), token)
    db.complete(sid, token)
    return sid


def test_end_to_end_real_server_event_path_calibrates_and_persists_immutable_snapshot(local_store, api):
    rng = np.random.default_rng(17)
    theta = rng.normal(size=130)
    probability = 1 / (1 + np.exp(-(theta[:, None] - np.linspace(-1, 1, 5))))
    outcomes = rng.random((130, 5)) < probability
    for index, answers in enumerate(outcomes):
        complete_attempt(local_store, f"student-{index}", 1, answers)
    request = {"assessmentId": "pilot-1", "assumptionReview": {
        "reviewedBy": "test-statistician", "evidence": "Automated test draws from a single latent trait with independent Bernoulli responses; this is a test fixture.",
        "unidimensional": True, "localIndependence": True, "representativeSample": True}}
    auth = {"X-Internal-API-Key": "internal-secret-token-for-tests-123456"}
    response = api.post("/api/v1/internal/psychometrics/screen", json=request, headers=auth)
    assert response.status_code == 201, response.text
    snapshot = response.json()
    assert snapshot["readiness"]["passed"] and snapshot["irt"]["converged"]
    assert snapshot["cleaning"]["selectedSessions"] == 130
    assert snapshot["normalization"]["coverage"] == 1
    assert api.post("/api/v1/internal/psychometrics/screen", json=request, headers=auth).json() == snapshot
    assert local_store.snapshot(snapshot["snapshotId"])["snapshotHash"] == snapshot["snapshotHash"]
    aggregates = api.get("/api/v1/psychometrics/items/q-0/snapshots", headers=auth).json()
    assert aggregates["snapshots"]
    assert "subjectId" not in json.dumps(aggregates)


def test_attempt_policy_and_automatic_feedback_preserve_initial_labels(local_store):
    complete_attempt(local_store, "retry-subject", 1, [1, 0, 1, 0, 1])
    complete_attempt(local_store, "retry-subject", 2, [0, 1, 0, 1, 0])
    first = local_store.screen(ScreeningInput(assessmentId="pilot-1", attemptPolicy="first"), load_policy())
    last = local_store.screen(ScreeningInput(assessmentId="pilot-1", attemptPolicy="last"), load_policy())
    assert first["normalization"]["persons"] == 1
    assert first["items"][0]["ctt"]["difficultyIndex"] == 1
    assert last["items"][0]["ctt"]["difficultyIndex"] == 0
    decisions = local_store.decisions(first["snapshotId"])
    assert len(decisions) == 5
    assert all(d["actorType"] == "system" and d["affectsSilverLabels"] is False for d in decisions)
    assert all(d["action"] == "collect_more_events" for d in decisions)
    assert local_store.snapshot(first["snapshotId"])["items"][0]["intendedDifficulty"] == "Medium"


def test_human_labeling_and_manual_empirical_decision_routes_are_absent(api, local_store):
    paths = api.get("/openapi.json").json()["paths"]
    assert not any("assignments" in path or "adjudications" in path for path in paths)
    assert all("post" not in operations for path, operations in paths.items() if path.endswith("/decisions"))
    assert api.post("/api/v1/internal/psychometrics/snapshots/unknown/decisions", json={}).status_code == 405


def test_service_can_register_silver_and_create_assessment_without_mongo(api, monkeypatch):
    monkeypatch.setattr(app.state, "staff_repository", None)
    auth = {"X-Internal-API-Key": "internal-secret-token-for-tests-123456"}
    snapshot = silver_snapshot()
    path = "/api/v1/internal/silver/snapshots"
    assert api.post(path, json=snapshot.model_dump(mode="json")).status_code == 503
    assert api.post(path, json=snapshot.model_dump(mode="json"), headers=auth).status_code == 201
    body = {"assessmentId": "api-silver-pilot", "snapshotId": snapshot.snapshotId,
            "questionVersionIds": [r.questionVersionId for r in snapshot.rows], "populationId": "p", "assessmentFamily": "f", "grade": 1}
    assert api.post("/api/v1/internal/assessments", json=body, headers=auth).status_code == 201


def test_store_survives_restart_and_rejects_secret_rotation(local_store):
    complete_attempt(local_store, "persisted-subject", 1, [1, 1, 0, 0, 1])
    result = local_store.screen(ScreeningInput(assessmentId="pilot-1"), load_policy())
    reopened = AssessmentStore(local_store.path)
    assert reopened.snapshot(result["snapshotId"]) == result
    assert reopened.subject_secret == local_store.subject_secret
    with pytest.raises(ValueError, match="secret changed"):
        AssessmentStore(local_store.path, subject_secret="different-secret")


def test_lifespan_initializes_default_assessment_backend_without_mongo(tmp_path, monkeypatch):
    import app.main as main_module
    monkeypatch.setattr(main_module, "staff_repository", None)
    monkeypatch.setattr(app.state, "assessment_store", None)
    monkeypatch.setenv("ASSESSMENT_DB_PATH", str(tmp_path / "startup.sqlite3"))
    with TestClient(app) as client:
        response = client.get("/v2/psychometrics-info")
        assert response.status_code == 200
        assert response.json()["storageReady"] is True
        assert client.get("/api/v1/capabilities").json()["assessmentStorageReady"] is True


def test_login_migrates_legacy_cookie_path_for_empirical_review(api, monkeypatch):
    user = {"userId": "staff-1", "roles": ["operator"],
            "passwordHash": password_hash("test-password-123")}

    class FakeLogin:
        async def count_recent_login_failures(self, username):
            return 0

        async def find_user_for_login(self, username):
            return user

        async def create_session(self, record, token_hash, csrf_hash):
            assert record["userId"] == "staff-1"

        async def audit(self, *args):
            pass

    monkeypatch.setattr(app.state, "staff_repository", FakeLogin())
    response = api.post("/internal/v2/auth/login", json={"username": "operator", "password": "test-password-123"})
    assert response.status_code == 200
    cookies = response.headers.get_list("set-cookie")
    assert any("Path=/internal/v2" in cookie and "Max-Age=0" in cookie for cookie in cookies)
    assert any("Path=/;" in cookie and "HttpOnly" in cookie and "Max-Age=28800" in cookie for cookie in cookies)
