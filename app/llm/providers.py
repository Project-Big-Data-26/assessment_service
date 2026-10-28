"""Provider selection for CLI silver validation; legacy Gemini defaults stay intact."""
import os

from dotenv import dotenv_values

from .config import PROJECT_ROOT, GeminiSettings
from .credentials import credential_slots

PROVIDERS = ("gemini", "deepseek", "groq")


def has_credentials(provider):
    return bool(key_slots(provider))


def key_slots(provider):
    slots = credential_slots(provider, dotenv_values(PROJECT_ROOT / ".env"))
    selected = os.getenv(f"EXERCISE_{provider.upper()}_KEY_SLOT")
    return [slot for slot in slots if str(slot) == selected] if selected is not None else slots


def provider_name():
    values = dotenv_values(PROJECT_ROOT / ".env")
    return (os.getenv("EXERCISE_LLM_PROVIDER") or values.get("EXERCISE_LLM_PROVIDER")
            or os.getenv("LLM_PROVIDER") or values.get("LLM_PROVIDER") or "gemini").strip().lower()


def settings_for(provider):
    if provider == "gemini":
        return GeminiSettings.from_environment()
    if provider == "deepseek":
        from .deepseek import DeepSeekSettings
        return DeepSeekSettings.from_environment()
    if provider == "groq":
        from .groq import GroqSettings
        return GroqSettings.from_environment()
    raise ValueError("silver provider must be gemini, deepseek or groq")
