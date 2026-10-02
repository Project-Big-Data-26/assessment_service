"""Invite-only internal annotation API and minimal server-rendered workspace."""

from __future__ import annotations

import html
import os
from typing import Any

from fastapi import APIRouter, Depends, Header, HTTPException, Request, Response, status
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, ConfigDict, Field

from .contracts import AdjudicationDecisionInput, DiscussionOutcomeInput, ExpertAnnotationInput
from .repository import MongoAnnotationRepository
from .security import (
    SESSION_COOKIE,
    SESSION_TTL_SECONDS,
    create_session_material,
    csrf_matches,
    password_verify,
)
from .assets import PrivateAssetSigner

router = APIRouter(prefix="/internal/v2", tags=["blind-annotation"])


class LoginInput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    username: str = Field(min_length=1, max_length=200)
    password: str = Field(min_length=8, max_length=1024)


def repository(request: Request) -> MongoAnnotationRepository:
    value = getattr(request.app.state, "annotation_repository", None)
    if value is None:
        raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE, "annotation storage is not configured")
    return value


async def active_session(
    request: Request, repo: MongoAnnotationRepository = Depends(repository)
) -> dict[str, Any]:
    token = request.cookies.get(SESSION_COOKIE)
    session = await repo.get_session(token) if token else None
    if session is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "authentication required")
    return session


async def mutation_session(
    session: dict[str, Any] = Depends(active_session),
    x_csrf_token: str | None = Header(default=None),
) -> dict[str, Any]:
    if not csrf_matches(x_csrf_token, session["csrfHash"]):
        raise HTTPException(status.HTTP_403_FORBIDDEN, "invalid CSRF token")
    return session


@router.post("/auth/login")
async def login(payload: LoginInput, response: Response, repo: MongoAnnotationRepository = Depends(repository)):
    normalized = payload.username.strip().casefold()
    if await repo.count_recent_login_failures(normalized) >= 5:
        raise HTTPException(status.HTTP_429_TOO_MANY_REQUESTS, "login temporarily limited")
    user = await repo.find_user_for_login(payload.username)
    if user is None or not password_verify(user["passwordHash"], payload.password):
        await repo.audit("auth.login_failed", None, {"usernameNormalized": normalized})
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "invalid credentials")
    token, token_hash, csrf, csrf_hash = create_session_material()
    await repo.create_session(user, token_hash, csrf_hash)
    await repo.audit("auth.login_succeeded", user["userId"])
    response.delete_cookie(SESSION_COOKIE, path="/internal/v2")
    response.set_cookie(
        SESSION_COOKIE,
        token,
        max_age=SESSION_TTL_SECONDS,
        httponly=True,
        secure=os.getenv("APP_ENV", "development") != "development",
        samesite="lax",
        path="/",
    )
    return {"userId": user["userId"], "roles": user.get("roles", []), "csrfToken": csrf}


@router.post("/auth/logout", status_code=204)
async def logout(
    request: Request,
    response: Response,
    session: dict[str, Any] = Depends(mutation_session),
    repo: MongoAnnotationRepository = Depends(repository),
):
    token = request.cookies.get(SESSION_COOKIE)
    if token:
        await repo.revoke_session(token)
    await repo.audit("auth.logout", session["userId"])
    response.delete_cookie(SESSION_COOKIE, path="/")
    response.delete_cookie(SESSION_COOKIE, path="/internal/v2")


@router.get("/assignments/next")
async def next_assignment(
    session: dict[str, Any] = Depends(active_session),
    repo: MongoAnnotationRepository = Depends(repository),
):
    expert_id = session.get("expertId")
    if not expert_id:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "expert profile required")
    assignment = await repo.next_assignment(expert_id)
    return {"assignment": assignment}


@router.get("/assignments/{assignment_id}")
async def get_assignment(
    assignment_id: str,
    session: dict[str, Any] = Depends(active_session),
    repo: MongoAnnotationRepository = Depends(repository),
):
    assignment = await repo.assignment_for_expert(assignment_id, session.get("expertId", ""))
    if assignment is None:
        # Same response for missing and non-owned assignments prevents IDOR discovery.
        raise HTTPException(status.HTTP_404_NOT_FOUND, "assignment not found")
    question = await repo.reviewer_question(assignment["questionVersionId"])
    if question is None:
        raise HTTPException(status.HTTP_409_CONFLICT, "assigned question version is unavailable")
    return {"assignment": assignment, "question": question}


@router.post("/assignments/{assignment_id}/submit", status_code=201)
async def submit_assignment(
    assignment_id: str,
    payload: ExpertAnnotationInput,
    request: Request,
    session: dict[str, Any] = Depends(mutation_session),
    repo: MongoAnnotationRepository = Depends(repository),
):
    assignment = await repo.assignment_for_expert(assignment_id, session.get("expertId", ""))
    if assignment is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "assignment not found")
    question = await repo.reviewer_question(assignment["questionVersionId"])
    if question is None:
        raise HTTPException(status.HTTP_409_CONFLICT, "assigned question version is unavailable")
    visual_required = "butuh_gambar" in question.get("extractionFlags", [])
    if payload.contentValid == "valid" and visual_required:
        if not question.get("imageRefs"):
            raise HTTPException(status.HTTP_409_CONFLICT, "essential source image is missing")
        if getattr(request.app.state, "asset_signer", None) is None:
            raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE, "private visual preview is unavailable")
    try:
        return await repo.submit_annotation(assignment, payload)
    except RuntimeError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.get("/assignments/{assignment_id}/assets/{asset_key:path}")
async def assignment_asset(
    assignment_id: str,
    asset_key: str,
    request: Request,
    session: dict[str, Any] = Depends(active_session),
    repo: MongoAnnotationRepository = Depends(repository),
):
    assignment = await repo.assignment_for_expert(assignment_id, session.get("expertId", ""))
    if assignment is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "assignment not found")
    question = await repo.reviewer_question(assignment["questionVersionId"])
    if question is None or asset_key not in question.get("imageRefs", []):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "asset not found")
    signer: PrivateAssetSigner | None = getattr(request.app.state, "asset_signer", None)
    if signer is None:
        raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE, "private asset storage is not configured")
    try:
        url = signer.signed_get_url(asset_key)
    except ValueError as exc:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(exc)) from exc
    await repo.audit("asset.signed_url_issued", session["userId"], {"assignmentId": assignment_id})
    return {"url": url, "expiresIn": signer.ttl_seconds}


def require_adjudicator(session: dict[str, Any]) -> None:
    if "senior_adjudicator" not in session.get("roles", []):
        raise HTTPException(status.HTTP_403_FORBIDDEN, "senior adjudicator role required")


@router.post("/adjudications/{adjudication_id}/discussion")
async def record_discussion(
    adjudication_id: str,
    payload: DiscussionOutcomeInput,
    session: dict[str, Any] = Depends(mutation_session),
    repo: MongoAnnotationRepository = Depends(repository),
):
    if not ({"admin", "research_coordinator"} & set(session.get("roles", []))):
        raise HTTPException(status.HTTP_403_FORBIDDEN, "research coordinator role required")
    case = await repo.discussion_case(adjudication_id)
    if case is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "discussion case not found")
    try:
        return await repo.submit_discussion(case, session["userId"], payload)
    except RuntimeError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.get("/adjudications")
async def list_adjudications(
    session: dict[str, Any] = Depends(active_session),
    repo: MongoAnnotationRepository = Depends(repository),
):
    require_adjudicator(session)
    return {"adjudications": await repo.list_adjudications()}


@router.post("/adjudications/{adjudication_id}/decision")
async def decide_adjudication(
    adjudication_id: str,
    payload: AdjudicationDecisionInput,
    session: dict[str, Any] = Depends(mutation_session),
    repo: MongoAnnotationRepository = Depends(repository),
):
    require_adjudicator(session)
    adjudication = await repo.adjudication(adjudication_id)
    if adjudication is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "adjudication not found")
    try:
        return await repo.submit_adjudication(adjudication, session["userId"], payload)
    except RuntimeError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, str(exc)) from exc


@router.get("/ui", response_class=HTMLResponse)
async def annotation_ui(session: dict[str, Any] = Depends(active_session)):
    """No-build reviewer UI; owned-assignment APIs remain the sole data source."""
    actor = html.escape(session.get("expertId") or session["userId"])
    return HTMLResponse(
        "<!doctype html><html lang='id'><meta charset='utf-8'>"
        "<meta name='viewport' content='width=device-width,initial-scale=1'>"
        "<title>Validasi Soal Matematika</title>"
        "<style>body{font:16px system-ui;max-width:1000px;margin:2rem auto;padding:0 1rem;color:#18212f}"
        "article,fieldset{border:1px solid #ccd4e0;border-radius:12px;padding:1.2rem;margin:1rem 0}"
        "button{padding:.7rem 1rem;background:#075985;color:white;border:0;border-radius:8px}"
        "textarea,input[type=text]{width:100%;box-sizing:border-box;padding:.6rem;margin:.3rem 0 .8rem}"
        ".muted{color:#52606d}.error{color:#b91c1c}.option{padding:.35rem 0}.grid{display:grid;grid-template-columns:1fr 1fr;gap:1rem}"
        "@media(max-width:700px){.grid{grid-template-columns:1fr}}</style>"
        f"<h1>🧮 Validasi blind</h1><p class='muted'>Reviewer: {actor}. "
        "Prediksi AI, suara reviewer lain, dan konsensus tidak ditampilkan.</p>"
        "<p id='status'>Memuat assignment…</p><article id='question' hidden></article>"
        "<form id='review' hidden><fieldset><legend>1. Qualification konten</legend>"
        "<label>Status konten <select name='contentValid'><option value='valid'>Valid</option>"
        "<option value='revision_required'>Perlu revisi</option><option value='excluded'>Dikeluarkan</option>"
        "<option value='insufficient_evidence'>Bukti kurang</option></select></label><br>"
        "<label>Status kunci <select name='answerKeyStatus'><option value='verified'>Terverifikasi</option>"
        "<option value='incorrect'>Salah</option><option value='ambiguous'>Ambigu</option>"
        "<option value='insufficient_evidence'>Bukti kurang</option></select></label>"
        "<label>Kunci terverifikasi<input name='verifiedAnswerKey' type='text'></label>"
        "<label>Solusi minimum terverifikasi<textarea name='minimalSolution' required></textarea></label></fieldset>"
        "<div class='grid' id='heads'></div><button type='submit'>🔒 Kunci dan kirim suara</button></form>"
        "<script>let assignment=null;const csrf=sessionStorage.getItem('csrfToken');"
        "const heads={mathCognitiveDomain:['knowing','applying','reasoning'],"
        "knowledgeDimension:['factual','conceptual','procedural','metacognitive'],"
        "intendedDifficulty:['Easy','Medium','Hard']};"
        "const labels={mathCognitiveDomain:'Domain kognitif matematika',knowledgeDimension:'Dimensi pengetahuan',intendedDifficulty:'Kesulitan yang dimaksud'};"
        "function txt(tag,value){const e=document.createElement(tag);e.textContent=value;return e}"
        "function renderHead(name,values){const f=document.createElement('fieldset');f.append(txt('legend','2. '+labels[name]));"
        "values.forEach(v=>{const l=document.createElement('label');const r=document.createElement('input');r.type='radio';r.name=name;r.value=v;l.append(r,document.createTextNode(' '+v+' '));f.append(l)});"
        "const ev=document.createElement('textarea');ev.name=name+'Evidence';ev.placeholder='Bukti dari tuntutan proses penyelesaian';f.append(ev);"
        "const a=document.createElement('label');const c=document.createElement('input');c.type='checkbox';c.name=name+'Abstain';a.append(c,document.createTextNode(' Abstain'));f.append(a);"
        "const reason=document.createElement('textarea');reason.name=name+'AbstainReason';reason.placeholder='Alasan abstain';f.append(reason);return f}"
        "Object.entries(heads).forEach(([n,v])=>document.querySelector('#heads').append(renderHead(n,v)));"
        "async function load(){if(!csrf){location.href='/internal/v2/ui/login';return}"
        "const next=await fetch('/internal/v2/assignments/next').then(r=>r.json());assignment=next.assignment;"
        "if(!assignment){document.querySelector('#status').textContent='Tidak ada assignment tersisa.';return}"
        "const data=await fetch('/internal/v2/assignments/'+encodeURIComponent(assignment.assignmentId)).then(r=>r.json());const q=data.question;"
        "const box=document.querySelector('#question');box.hidden=false;box.append(txt('h2',q.stem));"
        "if(q.stimulus)box.append(txt('p',q.stimulus));(q.options||[]).forEach(o=>box.append(txt('div',o.label+'. '+o.text)));"
        "box.append(txt('hr',''),txt('p','Sumber: '+q.book+', '+q.chapter+', halaman '+q.sourcePage),txt('p','Kunci yang harus diperiksa: '+q.answerKey));"
        "const teacher=q.extractionEvidence&&q.extractionEvidence.teacherKey;if(teacher)box.append(txt('p','Bukti Buku Guru halaman '+teacher.halaman+': '+teacher.kutipan));"
        "(q.imageRefs||[]).forEach(async key=>{const safe=key.split('/').map(encodeURIComponent).join('/');const r=await fetch('/internal/v2/assignments/'+encodeURIComponent(assignment.assignmentId)+'/assets/'+safe);"
        "if(r.ok){const d=await r.json();const img=document.createElement('img');img.src=d.url;img.alt='Visual soal privat';img.style.maxWidth='100%';box.append(img)}});"
        "document.querySelector('#status').textContent='Assignment '+assignment.assignmentId;document.querySelector('#review').hidden=false}"
        "document.querySelector('#review').addEventListener('submit',async e=>{e.preventDefault();const f=new FormData(e.target);"
        "const result={idempotencyKey:crypto.randomUUID(),contentValid:f.get('contentValid'),answerKeyStatus:f.get('answerKeyStatus'),"
        "verifiedAnswerKey:f.get('verifiedAnswerKey')||null,minimalSolution:f.get('minimalSolution')||null};"
        "const ineligible=result.contentValid!=='valid'||result.answerKeyStatus!=='verified';Object.keys(heads).forEach(n=>{const abstain=ineligible||f.get(n+'Abstain')==='on';"
        "result[n]={label:abstain?null:f.get(n),evidence:abstain?null:f.get(n+'Evidence'),abstain,abstainReason:abstain?(f.get(n+'AbstainReason')||'content_not_eligible'):null}});"
        "const r=await fetch('/internal/v2/assignments/'+encodeURIComponent(assignment.assignmentId)+'/submit',{method:'POST',headers:{'Content-Type':'application/json','X-CSRF-Token':csrf},body:JSON.stringify(result)});"
        "if(r.ok)location.reload();else document.querySelector('#status').textContent='Gagal: '+await r.text()});load();</script></html>"
    )


@router.get("/ui/login", response_class=HTMLResponse)
async def annotation_login_ui():
    return HTMLResponse(
        "<!doctype html><html lang='id'><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
        "<title>Masuk Validasi</title><style>body{font:16px system-ui;max-width:430px;margin:5rem auto;padding:1rem}"
        "form{border:1px solid #ccd4e0;border-radius:12px;padding:1.5rem}input{width:100%;box-sizing:border-box;padding:.7rem;margin:.3rem 0 1rem}"
        "button{padding:.7rem 1rem;background:#075985;color:white;border:0;border-radius:8px}</style>"
        "<h1>🔐 Masuk reviewer</h1><form id='login'><label>Username<input name='username' autocomplete='username' required></label>"
        "<label>Password<input name='password' type='password' autocomplete='current-password' required></label>"
        "<button>Masuk</button><p id='status'></p></form><script>document.querySelector('#login').addEventListener('submit',async e=>{e.preventDefault();"
        "const f=new FormData(e.target);const r=await fetch('/internal/v2/auth/login',{method:'POST',headers:{'Content-Type':'application/json'},"
        "body:JSON.stringify({username:f.get('username'),password:f.get('password')})});if(r.ok){const d=await r.json();sessionStorage.setItem('csrfToken',d.csrfToken);"
        "location.href='/internal/v2/ui'}else document.querySelector('#status').textContent='Login gagal'});</script></html>"
    )
