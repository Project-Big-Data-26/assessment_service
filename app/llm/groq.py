"""GroqCloud JSON validation; Free/Developer billing depends on the user's account."""
from dataclasses import dataclass, field
import os
from urllib.parse import urlparse

from dotenv import dotenv_values

from .config import PROJECT_ROOT, _as_bool
from .deepseek import DeepSeekSilverAdapter
from .credentials import selected_api_key


@dataclass(frozen=True)
class GroqSettings:
    api_key: str = field(default="", repr=False)
    model: str = "openai/gpt-oss-120b"
    provider: str = "groq"
    api_base_url: str = "https://api.groq.com/openai/v1"
    live_enabled: bool = False
    timeout_seconds: int = 120
    max_output_tokens: int = 4096
    reasoning_effort: str = "low"
    request_pause_seconds: float = 65

    def __post_init__(self):
        address = urlparse(self.api_base_url)
        if (address.scheme != "https" or address.hostname != "api.groq.com"
                or address.username or address.password or address.query or address.fragment
                or address.port not in (None, 443) or address.path.rstrip("/") != "/openai/v1"):
            raise ValueError("GROQ_API_BASE_URL must use the official Groq HTTPS endpoint")
        if self.provider != "groq" or not self.model.strip():
            raise ValueError("invalid Groq provider/model")
        if not 5 <= self.timeout_seconds <= 600 or not 128 <= self.max_output_tokens <= 32768:
            raise ValueError("invalid Groq timeout or output token limit")
        if self.reasoning_effort not in ("low", "medium", "high") or not 0 <= self.request_pause_seconds <= 300:
            raise ValueError("invalid Groq reasoning effort or request pause")

    @classmethod
    def from_environment(cls):
        values = dotenv_values(PROJECT_ROOT / ".env")
        def value(name, default):
            return str(os.environ.get(name, values.get(name) or default))
        return cls(api_key=selected_api_key("groq", values), model=value("GROQ_MODEL", "openai/gpt-oss-120b"),
                   api_base_url=value("GROQ_API_BASE_URL", "https://api.groq.com/openai/v1").rstrip("/"),
                   live_enabled=_as_bool(value("GROQ_LIVE_ENABLED", "false"), default=False),
                   timeout_seconds=int(value("GROQ_TIMEOUT_SECONDS", "120")),
                   max_output_tokens=int(value("GROQ_MAX_OUTPUT_TOKENS", "4096")),
                   reasoning_effort=value("GROQ_REASONING_EFFORT", "low"),
                   request_pause_seconds=float(value("GROQ_REQUEST_PAUSE_SECONDS", "65")))


class GroqSilverAdapter(DeepSeekSilverAdapter):
    """Reuse schema validation/audit handling while sending only Groq parameters."""
    def _request_payload(self, prompt):
        body = super()._request_payload(prompt)
        body.pop("thinking")
        body["max_completion_tokens"] = body.pop("max_tokens")
        body["include_reasoning"] = False
        return body
