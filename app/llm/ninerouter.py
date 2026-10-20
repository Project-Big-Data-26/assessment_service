"""Client for a self-hosted 9Router (OpenAI-compatible chat completions)."""

from __future__ import annotations

import base64
import json
import mimetypes
import os
import time
from dataclasses import dataclass, field
from typing import Any
from urllib.parse import urlparse

import httpx
from dotenv import dotenv_values

from .config import PROJECT_ROOT


# Koneksi putus di tengah jalan (ReadError/ConnectError/timeout) sering terjadi lewat proxy; ulangi otomatis.
NETWORK_RETRIES = 3


class NineRouterError(RuntimeError):
    pass


def _as_bool(value: str) -> bool:
    normalized = value.strip().casefold()
    if normalized in {"1", "true", "yes", "on"}:
        return True
    if normalized in {"0", "false", "no", "off"}:
        return False
    raise ValueError("NINEROUTER_STREAM must be true or false")


@dataclass(frozen=True)
class NineRouterSettings:
    """Runtime settings. The API key is deliberately hidden from repr."""

    api_key: str = field(repr=False)
    base_url: str
    model: str
    timeout_seconds: int = 180
    max_output_tokens: int = 4096
    temperature: float = 0.3
    # Model untuk solver/verifikasi buta; kosong = pakai `model`. Sebaiknya beda keluarga dari generator.
    solver_model: str = ""
    # Streaming menjaga koneksi tetap hidup; tanpa itu proxy Cloudflare memutus permintaan > 100 detik (HTTP 524).
    stream: bool = True

    def __post_init__(self) -> None:
        if not self.api_key.strip():
            raise ValueError("NINEROUTER_API_KEY is required")
        if not self.model.strip():
            raise ValueError("NINEROUTER_MODEL is required")
        parsed = urlparse(self.base_url)
        if parsed.scheme not in {"http", "https"} or not parsed.hostname:
            raise ValueError("NINEROUTER_BASE_URL must be an http(s) URL ending in /v1")
        if not 5 <= self.timeout_seconds <= 600:
            raise ValueError("NINEROUTER_TIMEOUT_SECONDS must be between 5 and 600")
        if not 128 <= self.max_output_tokens <= 32768:
            raise ValueError("NINEROUTER_MAX_OUTPUT_TOKENS must be between 128 and 32768")
        if not 0 <= self.temperature <= 2:
            raise ValueError("NINEROUTER_TEMPERATURE must be between 0 and 2")

    @classmethod
    def from_environment(cls, *, load_env_file: bool = True) -> "NineRouterSettings":
        file_values = dotenv_values(PROJECT_ROOT / ".env") if load_env_file else {}

        def value(name: str, default: str) -> str:
            resolved = os.getenv(name)
            if resolved is None:
                resolved = file_values.get(name)
            return str(resolved) if resolved is not None else default

        return cls(
            api_key=value("NINEROUTER_API_KEY", ""),
            base_url=value("NINEROUTER_BASE_URL", "").rstrip("/"),
            model=value("NINEROUTER_MODEL", ""),
            timeout_seconds=int(value("NINEROUTER_TIMEOUT_SECONDS", "180")),
            max_output_tokens=int(value("NINEROUTER_MAX_OUTPUT_TOKENS", "4096")),
            temperature=float(value("NINEROUTER_TEMPERATURE", "0.3")),
            solver_model=value("NINEROUTER_MODEL_SOLVER", "").strip(),
            stream=_as_bool(value("NINEROUTER_STREAM", "true")),
        )

    def public_info(self) -> dict[str, object]:
        return {
            "baseUrl": self.base_url,
            "model": self.model,
            "solverModel": self.solver_model or self.model,
            "timeoutSeconds": self.timeout_seconds,
            "maxOutputTokens": self.max_output_tokens,
            "temperature": self.temperature,
        }


def image_part(path: str) -> dict[str, Any]:
    """Bagian pesan berisi gambar (data URI) untuk model vision."""
    mime = mimetypes.guess_type(path)[0] or "image/png"
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return {"type": "image_url", "image_url": {"url": f"data:{mime};base64,{data}"}}


@dataclass(frozen=True)
class ChatResult:
    text: str
    model: str
    input_tokens: int | None
    output_tokens: int | None
    latency_seconds: float
    finish_reason: str | None


class NineRouterClient:
    def __init__(
        self,
        settings: NineRouterSettings,
        *,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        self.settings = settings
        self._http = httpx.Client(
            base_url=settings.base_url,
            headers={"Authorization": f"Bearer {settings.api_key}"},
            timeout=settings.timeout_seconds,
            transport=transport,
        )

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> "NineRouterClient":
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()

    def list_models(self) -> list[str]:
        try:
            response = self._http.get("/models")
            response.raise_for_status()
        except httpx.HTTPError as exc:
            raise NineRouterError(f"gagal mengambil daftar model: {_describe(exc)}") from exc
        return sorted(item["id"] for item in response.json().get("data", []))

    def chat(
        self,
        messages: list[dict[str, Any]],
        *,
        model: str | None = None,
        max_output_tokens: int | None = None,
        temperature: float | None = None,
        json_mode: bool = False,
    ) -> ChatResult:
        payload: dict[str, Any] = {
            "model": model or self.settings.model,
            "messages": messages,
            "max_tokens": max_output_tokens or self.settings.max_output_tokens,
            "temperature": self.settings.temperature if temperature is None else temperature,
            "stream": self.settings.stream,
        }
        if self.settings.stream:
            payload["stream_options"] = {"include_usage": True}
        if json_mode:
            payload["response_format"] = {"type": "json_object"}
        started = time.monotonic()
        for attempt in range(NETWORK_RETRIES + 1):
            try:
                return self._chat_once(payload, started)
            except NineRouterError as exc:
                if not isinstance(exc.__cause__, httpx.TransportError) or attempt == NETWORK_RETRIES:
                    raise
                time.sleep(3 * (attempt + 1))
        raise NineRouterError("tidak tercapai")    # pragma: no cover

    def _chat_once(self, payload: dict[str, Any], started: float) -> ChatResult:
        try:
            if self.settings.stream:
                text, model_name, usage, finish = self._read_stream(payload)
            else:
                response = self._http.post("/chat/completions", json=payload)
                response.raise_for_status()
                body = response.json()
                choice = body["choices"][0]
                text = choice["message"].get("content") or ""
                model_name, usage, finish = body.get("model"), body.get("usage") or {}, choice.get("finish_reason")
        except httpx.HTTPError as exc:
            raise NineRouterError(f"permintaan ke 9Router gagal: {_describe(exc)}") from exc
        except (KeyError, IndexError, ValueError) as exc:
            raise NineRouterError("respons 9Router tidak berformat chat completions") from exc
        return ChatResult(
            text=text,
            model=str(model_name or payload["model"]),
            input_tokens=usage.get("prompt_tokens"),
            output_tokens=usage.get("completion_tokens"),
            latency_seconds=round(time.monotonic() - started, 2),
            finish_reason=finish,
        )

    def _read_stream(self, payload: dict[str, Any]) -> tuple[str, str | None, dict[str, Any], str | None]:
        parts: list[str] = []
        model_name: str | None = None
        usage: dict[str, Any] = {}
        finish: str | None = None
        with self._http.stream("POST", "/chat/completions", json=payload) as response:
            if response.status_code >= 400:
                response.read()
                response.raise_for_status()
            for line in response.iter_lines():
                if not line.startswith("data:"):
                    continue          # komentar keep-alive (": ...") dan baris kosong
                data = line[5:].strip()
                if data == "[DONE]":
                    break
                chunk = json.loads(data)
                model_name = chunk.get("model") or model_name
                usage = chunk.get("usage") or usage
                for choice in chunk.get("choices") or []:
                    parts.append((choice.get("delta") or {}).get("content") or "")
                    finish = choice.get("finish_reason") or finish
        return "".join(parts), model_name, usage, finish


def _describe(exc: httpx.HTTPError) -> str:
    """Error text without request headers, so the key never reaches logs."""
    if isinstance(exc, httpx.HTTPStatusError):
        return f"HTTP {exc.response.status_code}: {exc.response.text[:300]}"
    return f"{type(exc).__name__}: {exc}"
