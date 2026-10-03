"""Password and opaque-session primitives; secrets are never persisted verbatim."""

from __future__ import annotations

import hashlib
import hmac
import os
import secrets


SESSION_COOKIE = "nalar_session"
SESSION_TTL_SECONDS = 8 * 60 * 60


def hash_secret(value: str) -> str:
    pepper = os.getenv("SESSION_SECRET")
    if pepper:
        return hmac.new(pepper.encode("utf-8"), value.encode("utf-8"), hashlib.sha256).hexdigest()
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def create_session_material() -> tuple[str, str, str, str]:
    token = secrets.token_urlsafe(48)
    csrf = secrets.token_urlsafe(32)
    return token, hash_secret(token), csrf, hash_secret(csrf)


def csrf_matches(provided: str | None, stored_hash: str) -> bool:
    return bool(provided) and hmac.compare_digest(hash_secret(provided), stored_hash)


def password_hash(password: str) -> str:
    try:
        from argon2 import PasswordHasher
    except ImportError as exc:  # pragma: no cover - deployment dependency guard
        raise RuntimeError("argon2-cffi is required for operator authentication") from exc
    return PasswordHasher(time_cost=3, memory_cost=65536, parallelism=2).hash(password)


def password_verify(stored_hash: str, password: str) -> bool:
    try:
        from argon2 import PasswordHasher
        from argon2.exceptions import InvalidHashError, VerifyMismatchError
    except ImportError as exc:  # pragma: no cover - deployment dependency guard
        raise RuntimeError("argon2-cffi is required for operator authentication") from exc
    try:
        return PasswordHasher().verify(stored_hash, password)
    except (InvalidHashError, VerifyMismatchError):
        return False
