"""Check Groq configuration offline; --execute makes one schema validation request."""
from datetime import datetime, timezone
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.llm.groq import GroqSettings, GroqSilverAdapter
from scripts.generate_silver_labels_kelas1 import atomic_write


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execute", action="store_true", help="Make one Groq request using the account's quota")
    args = parser.parse_args()
    settings = GroqSettings.from_environment()
    result = {"checkedAt": datetime.now(timezone.utc).isoformat(), "provider": "groq", "model": settings.model,
              "keyPresent": bool(settings.api_key.strip()), "liveEnabled": settings.live_enabled,
              "apiCalls": 0, "passed": None, "diagnosticOnly": True, "accountTierVerified": False}
    if args.execute and result["keyPresent"] and result["liveEnabled"]:
        item = {"_id": "groq-connection-probe", "soal_text": "Berapakah hasil 2 + 3?", "soal_type": "Pilihan Ganda",
                "kelas_id": "kelas8", "image_url": [], "jawaban": "B", "subbab_id": "Uji koneksi",
                "options": [{"option_id": "A", "text": "4"}, {"option_id": "B", "text": "5"}]}
        adapter = GroqSilverAdapter(settings)
        try:
            response = adapter.label_once(item, [], run_index=1, grade=8)
        finally:
            adapter.client.close()
        result.update(apiCalls=1, passed=response.status == "success", errorCode=response.errorCode,
                      providerFailureReason=response.providerFailureReason,
                      tokenUsage=response.usage.model_dump(mode="json"))
    elif args.execute:
        result.update(passed=False, reason="Set GROQ_API_KEY and GROQ_LIVE_ENABLED=true after checking the account plan")
    directory = ROOT / "runs/nightly_pipeline"
    directory.mkdir(parents=True, exist_ok=True)
    atomic_write(result, directory / "groq_connection_check.json")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["passed"] is not False else 2


if __name__ == "__main__":
    raise SystemExit(main())
