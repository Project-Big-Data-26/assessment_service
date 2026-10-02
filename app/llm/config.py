"""Validated Gemini configuration loaded from environment variables."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlparse

from dotenv import dotenv_values

PROJECT_ROOT = Path(__file__).resolve().parents[2]
OFFICIAL_GEMINI_HOST = "generativelanguage.googleapis.com"


def _as_bool(value: str | None, *, default: bool = False) -> bool:
    if value is None:
        return default
    normalized = value.strip().casefold()
    if normalized in {"1", "true", "yes", "on"}:
        return True
    if normalized in {"0", "false", "no", "off"}:
        return False
    raise ValueError("boolean environment value must be true or false")


@dataclass(frozen=True)
class GeminiSettings:
    """Runtime settings. The API key is deliberately hidden from repr."""

    api_key: str = field(repr=False)
    model: str
    provider: str = "gemini"
    api_base_url: str = f"https://{OFFICIAL_GEMINI_HOST}"
    live_enabled: bool = False
    review_runs: int = 3
    timeout_seconds: int = 45
    max_output_tokens: int = 1200
    temperature: float = 0.2

    def __post_init__(self) -> None:
        if self.provider != "gemini":
            raise ValueError("LLM_PROVIDER must be gemini for GeminiSettings")
        if not self.api_key.strip():
            raise ValueError("GEMINI_API_KEY is required")
        if not self.model.strip():
            raise ValueError("GEMINI_MODEL is required")
        parsed = urlparse(self.api_base_url)
        if parsed.scheme != "https" or parsed.hostname != OFFICIAL_GEMINI_HOST:
            raise ValueError("GEMINI_API_BASE_URL must use the official Google Gemini HTTPS host")
        if not 1 <= self.review_runs <= 5:
            raise ValueError("GEMINI_REVIEW_RUNS must be between 1 and 5")
        if not 5 <= self.timeout_seconds <= 120:
            raise ValueError("GEMINI_TIMEOUT_SECONDS must be between 5 and 120")
        if not 128 <= self.max_output_tokens <= 4096:
            raise ValueError("GEMINI_MAX_OUTPUT_TOKENS must be between 128 and 4096")
        if not 0 <= self.temperature <= 1:
            raise ValueError("GEMINI_TEMPERATURE must be between 0 and 1")

    @classmethod
    def from_environment(cls, *, load_env_file: bool = True) -> "GeminiSettings":
        file_values = dotenv_values(PROJECT_ROOT / ".env") if load_env_file else {}

        def value(name: str, default: str) -> str:
            # Process/secret-manager variables win. Reading the file must not
            # mutate global os.environ or alter unrelated application config.
            resolved = os.getenv(name)
            if resolved is None:
                resolved = file_values.get(name)
            return str(resolved) if resolved is not None else default

        return cls(
            provider=value("LLM_PROVIDER", "gemini").strip().casefold(),
            api_key=value("GEMINI_API_KEY", ""),
            model=value("GEMINI_MODEL", ""),
            api_base_url=value(
                "GEMINI_API_BASE_URL", f"https://{OFFICIAL_GEMINI_HOST}"
            ).rstrip("/"),
            live_enabled=_as_bool(value("GEMINI_LIVE_ENABLED", "false"), default=False),
            review_runs=int(value("GEMINI_REVIEW_RUNS", "3")),
            timeout_seconds=int(value("GEMINI_TIMEOUT_SECONDS", "45")),
            max_output_tokens=int(value("GEMINI_MAX_OUTPUT_TOKENS", "1200")),
            temperature=float(value("GEMINI_TEMPERATURE", "0.2")),
        )

    def public_info(self) -> dict[str, object]:
        return {
            "provider": self.provider,
            "model": self.model,
            "liveEnabled": self.live_enabled,
            "reviewRuns": self.review_runs,
            "timeoutSeconds": self.timeout_seconds,
            "maxOutputTokens": self.max_output_tokens,
            "temperature": self.temperature,
        }
