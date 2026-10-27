"""Provider selection for CLI silver validation; legacy Gemini defaults stay intact."""
import os

from dotenv import dotenv_values

from .config import PROJECT_ROOT, GeminiSettings

PROVIDERS = ("gemini", "deepseek", "groq")


def has_credentials(provider):
    values = dotenv_values(PROJECT_ROOT / ".env")
    name = provider.upper() + "_API_KEY"
    value = os.environ.get(name, values.get(name) or "")
    return bool(str(value).strip())


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
