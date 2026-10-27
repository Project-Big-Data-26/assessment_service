"""One schema probe per exercise provider; no private key or response text is printed."""
import argparse
from dataclasses import replace
from datetime import datetime, timezone
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.llm.providers import settings_for, has_credentials, key_slots
from app.llm.credentials import use_credential_slot
from scripts.generate_silver_labels_kelas1 import atomic_write


def check(provider, *, execute=False, model=None):
    if not has_credentials(provider):
        return {"provider": provider, "keyPresent": False, "liveEnabled": False,
                "apiCalls": 0, "passed": False if execute else None, "errorCode": "missing_credentials"}
    settings = settings_for(provider)
    if model:
        settings = replace(settings, model=model)
    result = {"provider": provider, "model": settings.model, "keyPresent": bool(settings.api_key.strip()),
              "liveEnabled": settings.live_enabled, "apiCalls": 0, "passed": None}
    if not execute or not result["keyPresent"]:
        return result
    # --execute is explicit authorization for this single diagnostic request.
    settings = replace(settings, live_enabled=True, max_output_tokens=4096)
    if provider == "gemini":
        from app.llm.silver import GeminiSilverAdapter
        adapter = GeminiSilverAdapter(settings, stop_on_503=True)
    else:
        from app.llm.groq import GroqSilverAdapter
        adapter = GroqSilverAdapter(settings, stop_on_503=True)
    item = {"_id": "provider-connection-probe", "soal_text": "Berapakah hasil 2 + 3?",
            "soal_type": "Pilihan Ganda", "kelas_id": "kelas8", "image_url": [], "jawaban": "B",
            "subbab_id": "Uji koneksi", "options": [{"option_id": "A", "text": "4"}, {"option_id": "B", "text": "5"}]}
    try:
        response = adapter.label_once(item, [], run_index=1, grade=8)
    finally:
        adapter.client.close()
    # A verified option value (5) is also correct; the schema permits either
    # the option identifier or the independently computed answer text.
    result.update(apiCalls=1, passed=probe_passed(response),
                  errorCode=response.errorCode, providerFailureReason=response.providerFailureReason,
                  quotaDailyExhausted=response.quotaDailyExhausted, quotaLimits=response.quotaLimits,
                  tokenUsage=response.usage.model_dump(mode="json"))
    return result


def probe_passed(response):
    output = response.output
    return bool(response.status == "success" and output and output.answerKeyStatus == "verified"
                and str(output.verifiedAnswerKey).strip().casefold() in {"b", "5"})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--providers", nargs="+", choices=("gemini", "groq"), default=["gemini", "groq"])
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--all-keys", action="store_true", help="Check each configured distinct key slot")
    parser.add_argument("--gemini-model", help="Optional diagnostic model override; does not edit .env")
    args = parser.parse_args()
    results = []
    for provider in args.providers:
        if args.all_keys and key_slots(provider):
            for slot in key_slots(provider):
                with use_credential_slot(provider, slot):
                    result = check(provider, execute=args.execute, model=args.gemini_model if provider == "gemini" else None)
                results.append({**result, "keySlot": slot})
                if str(result.get("errorCode", "")).endswith(":503"):
                    break
        else:
            results.append(check(provider, execute=args.execute, model=args.gemini_model if provider == "gemini" else None))
        if str(results[-1].get("errorCode", "")).endswith(":503"):
            break
    result = {"checkedAt": datetime.now(timezone.utc).isoformat(), "diagnosticOnly": True, "results": results}
    path = ROOT / "runs/nightly_pipeline/exercise_provider_connection_check.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    atomic_write(result, path)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not args.execute or all(r["passed"] is True for r in results) else 2


if __name__ == "__main__":
    raise SystemExit(main())
