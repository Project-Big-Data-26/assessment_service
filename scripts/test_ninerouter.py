"""
Tes koneksi ke 9Router (endpoint OpenAI-compatible). Dijalankan dari root project:
    venv/Scripts/python scripts/test_ninerouter.py
    venv/Scripts/python scripts/test_ninerouter.py --model <nama-model>
    venv/Scripts/python scripts/test_ninerouter.py --sample   # tes keluaran JSON soal

Kredensial dibaca dari .env (NINEROUTER_*), tidak pernah dicetak.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.llm.ninerouter import NineRouterClient, NineRouterError, NineRouterSettings

SAMPLE_PROMPT = (
    "Buat 1 soal pilihan ganda Matematika SMA tentang eksponen (bilangan bulat, mudah). "
    'Balas HANYA JSON: {"soal": str, "options": {"A": str, "B": str, "C": str, "D": str}, '
    '"jawaban": "A"|"B"|"C"|"D", "pembahasan": str}'
)


def main() -> int:
    # Konsol Windows (cp1252) gagal mencetak simbol matematika dari balasan model.
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", help="override NINEROUTER_MODEL")
    parser.add_argument("--sample", action="store_true", help="minta 1 soal JSON")
    args = parser.parse_args()

    try:
        settings = NineRouterSettings.from_environment()
    except ValueError as exc:
        print(f"[GAGAL] konfigurasi .env: {exc}")
        return 2
    print("Konfigurasi:", json.dumps(settings.public_info(), ensure_ascii=False))

    with NineRouterClient(settings) as client:
        try:
            models = client.list_models()
            print(f"[OK] /models -> {len(models)} model")
            for name in models:
                print("   -", name)
        except NineRouterError as exc:
            print(f"[PERINGATAN] {exc} (lanjut ke tes chat)")

        prompt = SAMPLE_PROMPT if args.sample else "Balas satu kata saja: siap"
        try:
            result = client.chat(
                [{"role": "user", "content": prompt}],
                model=args.model,
                json_mode=args.sample,
            )
        except NineRouterError as exc:
            print(f"[GAGAL] {exc}")
            return 1

    print(
        f"[OK] chat model={result.model} latensi={result.latency_seconds}s "
        f"token masuk/keluar={result.input_tokens}/{result.output_tokens} "
        f"finish={result.finish_reason}"
    )
    print("Balasan:", result.text.strip()[:1500])
    if args.sample:
        try:
            json.loads(result.text)
            print("[OK] balasan adalah JSON valid")
        except ValueError:
            print("[PERINGATAN] balasan bukan JSON valid murni (perlu parser/retry di pipeline)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
