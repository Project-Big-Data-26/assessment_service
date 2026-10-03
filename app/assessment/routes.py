"""Pilot API: staff-controlled blueprints, opaque participant bearer tokens."""
from __future__ import annotations

import hmac
import os

from fastapi import APIRouter, Depends, Header, HTTPException, Request
from starlette.concurrency import run_in_threadpool

from app.staff.routes import active_session, mutation_session, repository
from app.psychometrics.analysis import analyze_matrix
from app.psychometrics.contracts import EmpiricalAnalysisResult, MatrixAnalysisInput, ScreeningInput
from app.training.v2.dataset import DatasetSnapshot
from .contracts import (AssessmentCreate, ParticipantCreate, ResponseCreate,
                        AssessmentReceipt, ParticipantReceipt, SessionReceipt, DeliveredItem,
                        DeliveryFinished, ResponseReceipt, SessionCompleted)
from .store import AssessmentError, AssessmentStore

router = APIRouter(prefix="/api/v1", tags=["empirical-assessment"])
info_router = APIRouter(prefix="/v2", tags=["empirical-assessment"])


def store(request: Request) -> AssessmentStore:
    value = getattr(request.app.state, "assessment_store", None)
    if value is None:
        raise HTTPException(503, "assessment storage is unavailable")
    return value


async def staff(request: Request, x_internal_api_key: str | None = Header(default=None),
                x_csrf_token: str | None = Header(default=None)):
    configured = os.getenv("PSYCHOMETRICS_API_TOKEN", "")
    if x_internal_api_key is not None:
        if len(configured) < 32 or not hmac.compare_digest(x_internal_api_key, configured):
            raise HTTPException(401, "invalid internal API credential")
        return {"userId": "psychometrics-service", "roles": ["service_account"]}
    # Reuse invite-only staff sessions and CSRF for cookie-authenticated writes.
    repo = repository(request)
    session = await active_session(request, repo)
    allowed = {"admin", "operator", "research_coordinator", "psychometrician"}
    if not (allowed & set(session.get("roles", []))):
        raise HTTPException(403, "empirical assessment staff role required")
    if request.method != "GET":
        session = await mutation_session(session, x_csrf_token)
    return session


def participant_token(authorization: str | None = Header(default=None)):
    if not authorization or not authorization.startswith("Bearer ") or len(authorization[7:]) < 32:
        raise HTTPException(401, "participant bearer token required")
    return authorization[7:]


def idempotency_key(idempotency_key: str = Header(min_length=8, max_length=128)):
    return idempotency_key


async def call_store(function, *args):
    try:
        return await run_in_threadpool(function, *args)
    except AssessmentError as exc:
        raise HTTPException(exc.status_code, str(exc)) from exc


@info_router.get("/psychometrics-info")
def info(request: Request):
    policy = request.app.state.psychometrics_policy
    return {"implemented": True, "storageReady": getattr(request.app.state, "assessment_store", None) is not None,
            "models": ["rasch", "2pl", "3pl"], "policyVersion": policy.policyVersion,
            "minimumPersons": policy.minPersons, "minimumItems": policy.minItems,
            "scoring": "server_scored_single_choice", "researchOnly": True,
            "reviewRequired": False, "reviewMode": "automated_ai", "labelProvenance": "ai_silver"}


@router.get("/health")
def health():
    return {"status": "ok", "service": "question-intelligence"}


@router.get("/capabilities")
def capabilities(request: Request):
    return {"apiVersion": "2.2.0", "openApiUrl": "/openapi.json", "delivery": "fixed_form_single_choice",
            "studentResponses": "server_scored", "psychometrics": ["ctt", "rasch", "2pl", "3pl"],
            "assessmentStorageReady": getattr(request.app.state, "assessment_store", None) is not None,
            "questionAuthoring": "silver_validation_and_cli", "variantGeneration": False,
            "modelPromotion": "silver_and_technical_gates_required"}


@router.post("/internal/assessments", status_code=201, response_model=AssessmentReceipt)
async def create_assessment(payload: AssessmentCreate, request: Request, actor=Depends(staff), db=Depends(store)):
    snapshot = await call_store(db.dataset_snapshot, payload.snapshotId)
    result = await call_store(db.create_assessment, payload, snapshot)
    return result


@router.post("/internal/assessments/{assessment_id}/participants", status_code=201, response_model=ParticipantReceipt)
async def create_participant(assessment_id: str, payload: ParticipantCreate, actor=Depends(staff), db=Depends(store)):
    return await call_store(db.participant, assessment_id, payload.participantCode)


@router.post("/assessments/{assessment_id}/sessions", status_code=201, response_model=SessionReceipt)
async def start(assessment_id: str, token=Depends(participant_token), key=Depends(idempotency_key), db=Depends(store)):
    return await call_store(db.start, assessment_id, token, key)


@router.get("/sessions/{session_id}/items/next", response_model=DeliveredItem | DeliveryFinished)
async def next_item(session_id: str, token=Depends(participant_token), db=Depends(store)):
    return await call_store(db.next_item, session_id, token)


@router.post("/responses", status_code=201, response_model=ResponseReceipt)
async def response(payload: ResponseCreate, token=Depends(participant_token), key=Depends(idempotency_key), db=Depends(store)):
    if key != payload.responseId:
        raise HTTPException(422, "Idempotency-Key must equal responseId")
    return await call_store(db.respond, payload, token)


@router.post("/sessions/{session_id}/complete", response_model=SessionCompleted)
async def complete(session_id: str, token=Depends(participant_token), key=Depends(idempotency_key), db=Depends(store)):
    return await call_store(db.complete, session_id, token)


@router.post("/internal/psychometrics/item-analysis", response_model=EmpiricalAnalysisResult, response_model_exclude_unset=True)
async def item_analysis(payload: MatrixAnalysisInput, request: Request, actor=Depends(staff)):
    # External matrices cannot claim server provenance. Only delivery aggregation
    # inside AssessmentStore.screen can construct a server_scored matrix.
    if payload.dataOrigin == "server_scored":
        raise HTTPException(422, "use the screen endpoint for server-scored response events")
    result = await run_in_threadpool(analyze_matrix, payload, request.app.state.psychometrics_policy)
    result["persisted"] = False
    return result


@router.post("/internal/psychometrics/screen", status_code=201, response_model=EmpiricalAnalysisResult, response_model_exclude_unset=True)
async def screen(payload: ScreeningInput, request: Request, actor=Depends(staff), db=Depends(store)):
    return await call_store(db.screen, payload, request.app.state.psychometrics_policy)


@router.get("/internal/psychometrics/snapshots/{snapshot_id}", response_model=EmpiricalAnalysisResult, response_model_exclude_unset=True)
async def snapshot(snapshot_id: str, actor=Depends(staff), db=Depends(store)):
    return await call_store(db.snapshot, snapshot_id)


@router.get("/psychometrics/items/{question_id}/snapshots")
async def item_snapshots(question_id: str, actor=Depends(staff), db=Depends(store)):
    # Authenticated aggregate only; subject EAPs appear only in the staff snapshot.
    return {"snapshots": await call_store(db.list_snapshots, question_id)}


@router.get("/internal/psychometrics/snapshots/{snapshot_id}/decisions")
async def decisions(snapshot_id: str, actor=Depends(staff), db=Depends(store)):
    return {"decisions": await call_store(db.decisions, snapshot_id)}


@router.post("/internal/silver/snapshots", status_code=201)
async def register_silver_snapshot(payload: DatasetSnapshot, actor=Depends(staff), db=Depends(store)):
    return await call_store(db.register_snapshot, payload)


@router.get("/internal/silver/snapshots/{snapshot_id}", response_model=DatasetSnapshot)
async def silver_snapshot(snapshot_id: str, actor=Depends(staff), db=Depends(store)):
    return await call_store(db.dataset_snapshot, snapshot_id)
