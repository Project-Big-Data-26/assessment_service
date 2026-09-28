"""
Script kecil buat cek koneksi llm_backend.py ke Ollama -- dijalankan LANGSUNG
dari command line (bukan lewat REPL interaktif), supaya tidak ada masalah
paste multi-baris di PowerShell.

Cara pakai (dari root project ai_services_lms):
    python scripts/test_llm_connection.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.services.pretest.llm_backend import extract_answer_llm, generate_distractors_llm


def main() -> None:
    print("=== Test 1: extract_answer_llm (jawaban angka verbatim) ===")
    text1 = "Diketahui panjang 8 cm dan lebar 5 cm. Jadi, luasnya adalah 40 cm2."
    result1 = extract_answer_llm(text1)
    print(f"  Teks    : {text1!r}")
    print(f"  Hasil   : {result1}")
    if result1.answer is None:
        print("  -> GAGAL/None. Cek apakah Ollama benar-benar merespons "
              "(lihat pesan error/flag di atas).")
    else:
        print("  -> OK, jawaban berhasil diekstrak & lolos verifikasi verbatim.")

    print("\n=== Test 2: extract_answer_llm (jawaban TIDAK ADA di teks -> harus ditolak) ===")
    text2 = "Sebuah kotak memiliki volume yang dihitung dari p, l, t."
    result2 = extract_answer_llm(text2)
    print(f"  Teks    : {text2!r}")
    print(f"  Hasil   : {result2}")
    if result2.answer is None:
        print("  -> OK, LLM tidak memaksakan jawaban yang tidak ada di teks (sesuai harapan).")
    else:
        print("  -> WARNING: ada jawaban dikembalikan padahal seharusnya tidak ada "
              "di teks sumber -- cek _verify_verbatim().")

    print("\n=== Test 3: generate_distractors_llm ===")
    distractors = generate_distractors_llm(
        raw_text="Jadi, bentuk sederhana dari pecahan tersebut adalah dua per tiga.",
        correct_answer="dua per tiga",
    )
    print(f"  Hasil   : {distractors}")
    if distractors is None:
        print("  -> GAGAL/None. Cek format respons LLM (harus JSON list).")
    else:
        print("  -> OK, 3 distractor berhasil digenerate & tidak sama dengan jawaban benar.")

    print("\nSelesai. Kalau Test 1 & 3 menghasilkan None terus, cek:")
    print("  - qwen3:4b beneran ke-load (coba 'ollama run qwen3:4b' manual dulu, ada delay awal load ke GPU)")
    print("  - koneksi ke http://localhost:11434 tidak diblokir firewall/antivirus")


if __name__ == "__main__":
    main()
