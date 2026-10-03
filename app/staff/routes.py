"""Invite-only operator authentication; labeling is performed by AI."""

from __future__ import annotations

import html
import os
from typing import Any

from fastapi import APIRouter, Depends, Header, HTTPException, Request, Response, status
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, ConfigDict, Field

from .repository import MongoRepository
from .security import (
    SESSION_COOKIE,
    SESSION_TTL_SECONDS,
    create_session_material,
    csrf_matches,
    password_verify,
)
from .assets import PrivateAssetSigner

router = APIRouter(prefix="/internal/v2", tags=["operator-auth"])


class LoginInput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    username: str = Field(min_length=1, max_length=200)
    password: str = Field(min_length=8, max_length=1024)


def repository(request: Request) -> MongoRepository:
    value = getattr(request.app.state, "staff_repository", None)
    if value is None:
        raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE, "staff storage is not configured")
    return value


async def active_session(
    request: Request, repo: MongoRepository = Depends(repository)
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
async def login(payload: LoginInput, response: Response, repo: MongoRepository = Depends(repository)):
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
    repo: MongoRepository = Depends(repository),
):
    token = request.cookies.get(SESSION_COOKIE)
    if token:
        await repo.revoke_session(token)
    await repo.audit("auth.logout", session["userId"])
    response.delete_cookie(SESSION_COOKIE, path="/")
    response.delete_cookie(SESSION_COOKIE, path="/internal/v2")


