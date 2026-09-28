"""
llm_backend.py -- lapisan pemanggilan LLM lokal (Ollama) untuk Tahap 2
lanjutan (`answer_option_generator.py`).

SENGAJA DIPISAH dari answer_option_generator.py:
  - answer_option_generator.py TIDAK PERLU tahu detail HTTP/Ollama sama
    sekali -- dia cuma panggil `extract_answer_llm()` / `generate_distractors_llm()`
    yang ada di sini.
  - Kalau nanti provider LLM ganti (bukan Ollama lagi, atau nambah provider
    cloud), cukup ubah isi modul ini -- signature fungsi publiknya tetap
    sama, jadi answer_option_generator.py tidak perlu disentuh.

TIDAK PAKAI dependency tambahan (`requests`, `ollama` package, dst) --
sengaja pakai `urllib` (stdlib Python) supaya tidak nambah instalasi baru
di project yang sudah ada.

PRINSIP KEAMANAN (harga mati, sama seperti prinsip di answer_option_generator.py):
  - LLM di sini TIDAK PERNAH diminta "jawab soal ini sendiri" -- cuma
    diminta MENUNJUK/MENYALIN jawaban yang sudah ada di teks (ekstraksi),
    atau membuat distractor (yang memang seharusnya baru/salah, beda dengan
    jawaban benar yang wajib verbatim).
  - Jawaban hasil ekstraksi LLM WAJIB lolos verifikasi mekanis (harus
    benar-benar ditemukan di teks sumber) sebelum dipakai -- lihat
    `_verify_verbatim()`. Kalau gagal verifikasi, DIBUANG, bukan dipaksakan.
  - Kalau Ollama tidak jalan / error apapun, fungsi return None (bukan
    exception yang menghentikan seluruh batch) -- pemanggil (
    answer_option_generator.py) akan memperlakukan ini sama seperti "LLM
    tidak berhasil", item tetap `pending_mcq_conversion`, TIDAK CRASH.
"""

from __future__ import annotations

import json
import math
import re
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from typing import List, Optional

OLLAMA_URL = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "qwen3:4b"  # lihat diskusi: dipilih karena muat di GPU 6GB VRAM

# Sama seperti di answer_option_generator.py -- dipakai untuk normalisasi
# saat verifikasi verbatim, supaya beda karakter minus (hyphen vs en dash
# vs minus unicode) tidak bikin verifikasi gagal padahal secara makna sama.
_MINUS_CHARS = "–−—"


@dataclass
class LLMAnswerResult:
    answer: Optional[str]
    confidence: float
    method: str
    flags: List[str] = field(default_factory=list)


def call_ollama(
    prompt: str, model: str = DEFAULT_MODEL, timeout: int = 120, temperature: float = 0.1
) -> Optional[str]:
    """
    Panggil Ollama lokal (endpoint /api/generate), return teks respons
    mentah, atau None kalau gagal (Ollama tidak jalan, timeout, respons
    tidak valid, dst) -- TIDAK melempar exception ke pemanggil, supaya
    batch processing ratusan/ribuan item tidak berhenti gara-gara 1
    kegagalan panggilan.

    `temperature` sengaja RENDAH (0.1) sebagai default -- untuk tugas
    ekstraksi/verifikasi kita mau jawaban yang konsisten & "tidak kreatif",
    beda dengan tugas generate distractor yang butuh sedikit variasi (lihat
    pemanggilannya di `generate_distractors_llm`).
    """
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": temperature},
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        OLLAMA_URL, data=data, headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            return (body.get("response") or "").strip()
    except (urllib.error.URLError, TimeoutError, ValueError, json.JSONDecodeError):
        # ValueError menangkap juga socket.timeout di beberapa versi Python.
        return None


def _normalize_for_match(text: str) -> str:
    t = text.lower()
    for ch in _MINUS_CHARS:
        t = t.replace(ch, "-")
    t = re.sub(r"\s+", " ", t)
    return t.strip()


def _verify_verbatim(candidate: str, source_text: str) -> bool:
    """
    Cek MEKANIS (bukan percaya klaim LLM) apakah `candidate` benar-benar
    muncul di `source_text` -- toleran terhadap beda spasi/kapitalisasi/
    karakter minus, tapi TETAP menolak kalau candidate memang tidak ada
    sama sekali di teks sumber.
    """
    norm_candidate = _normalize_for_match(candidate)
    if not norm_candidate:
        return False
    norm_source = _normalize_for_match(source_text)
    return norm_candidate in norm_source


_NO_ANSWER_MARKER = "TIDAK_DITEMUKAN"

# Dipakai HANYA untuk pengecekan kesamaan NILAI antara distractor dan jawaban
# benar (bukan untuk parsing jawaban utama -- itu tugas try_parse_number di
# answer_option_generator.py). Sengaja dibuat mandiri di sini (bukan import
# dari sana) supaya llm_backend.py tetap tidak bergantung ke modul lain --
# lihat catatan di kepala file.
_FRACTION_RE = re.compile(
    r"^\s*(-?\d+(?:[.,]\d+)?)\s*(?:/|per)\s*(-?\d+(?:[.,]\d+)?)\s*$", re.IGNORECASE
)
_PLAIN_NUMBER_RE = re.compile(
    r"^\s*(?:Rp\.?\s*)?(-?\d{1,3}(?:\.\d{3})*(?:,\d+)?|-?\d+(?:[.,]\d+)?)\s*(%)?\s*$"
)

# Jawaban soal SD-SMA sering ditulis dalam KATA, bukan angka ("dua per
# tiga", bukan "2/3") -- terutama hasil generate LLM. Tanpa ini,
# _approx_numeric_value tidak akan mendeteksi "dua per tiga" == "empat per
# enam" (kasus nyata yang ditemukan saat testing manual). Cuma menangani
# rentang umum 0-99 (cukup untuk konteks pecahan/bilangan sederhana SD-SMA)
# -- di luar itu dibiarkan tidak dikenali, BUKAN dianggap otomatis salah.
_UNIT_WORDS = {
    "nol": 0, "satu": 1, "dua": 2, "tiga": 3, "empat": 4, "lima": 5,
    "enam": 6, "tujuh": 7, "delapan": 8, "sembilan": 9,
}
_TEEN_WORDS = {"sepuluh": 10, "sebelas": 11}
_TEEN_WORDS.update({f"{w}belas": 10 + v for w, v in _UNIT_WORDS.items() if v >= 2})
_TENS_WORDS = {f"{w}puluh": v * 10 for w, v in _UNIT_WORDS.items() if v >= 2}
_WORD_FRACTION_RE = re.compile(r"^\s*([a-zA-Z\s]+?)\s+per\s+([a-zA-Z\s]+?)\s*$", re.IGNORECASE)


def _word_to_number(word: str) -> Optional[int]:
    """Parse kata bilangan Indonesia sederhana (0-99) jadi angka, mis.
    "dua" -> 2, "dua puluh lima" -> 25. Return None kalau tidak dikenali
    (bukan berarti salah -- cuma di luar cakupan parser sederhana ini)."""
    w = re.sub(r"\s+", "", word.strip().lower())
    if not w:
        return None
    if w in _UNIT_WORDS:
        return _UNIT_WORDS[w]
    if w in _TEEN_WORDS:
        return _TEEN_WORDS[w]
    if w in _TENS_WORDS:
        return _TENS_WORDS[w]
    for tens_word, tens_val in _TENS_WORDS.items():
        if w.startswith(tens_word) and w[len(tens_word):] in _UNIT_WORDS:
            return tens_val + _UNIT_WORDS[w[len(tens_word):]]
    return None


def _approx_numeric_value(text: str) -> Optional[float]:
    """
    Coba parse `text` sebagai satu nilai numerik ATAU pecahan ("a/b" atau
    "a per b"). Dipakai untuk MENDETEKSI distractor yang NILAINYA SAMA
    dengan jawaban benar walau ditulisnya beda (mis. jawaban "2/3" vs
    distractor "4/6" -- secara matematis identik, jadi TIDAK BOLEH lolos
    jadi opsi salah).

    Return None kalau `text` tidak bisa diparse sebagai angka/pecahan
    tunggal -- ini BUKAN berarti otomatis dianggap "aman"/valid, cuma di
    luar jangkauan pengecekan numerik ini (mis. jawaban deskriptif seperti
    "segitiga siku-siku"), jadi distractor begitu dibiarkan lolos apa
    adanya dari cek numerik ini (tetap lolos cek "sama persis secara teks"
    di tempat lain).
    """
    t = text.strip()
    frac = _FRACTION_RE.match(t)
    if frac:
        try:
            num = float(frac.group(1).replace(",", "."))
            den = float(frac.group(2).replace(",", "."))
            return None if den == 0 else num / den
        except ValueError:
            return None

    plain = _PLAIN_NUMBER_RE.match(t)
    if plain:
        num_str = plain.group(1)
        is_percent = bool(plain.group(2))
        if "," in num_str and "." in num_str:
            num_str = num_str.replace(".", "").replace(",", ".")
        elif "," in num_str:
            num_str = num_str.replace(",", ".")
        elif num_str.count(".") > 1:
            num_str = num_str.replace(".", "")
        try:
            value = float(num_str)
        except ValueError:
            return None
        return value / 100 if is_percent else value

    word_frac = _WORD_FRACTION_RE.match(t)
    if word_frac:
        num = _word_to_number(word_frac.group(1))
        den = _word_to_number(word_frac.group(2))
        if num is not None and den not in (None, 0):
            return num / den

    word_value = _word_to_number(t)
    if word_value is not None:
        return float(word_value)

    return None


def _same_numeric_value(a: str, b: str) -> bool:
    """True kalau `a` dan `b` bisa diparse sebagai angka/pecahan DAN
    nilainya sama (dalam toleransi kecil) -- BUKAN cuma beda tulisan.
    Kalau salah satu/keduanya tidak bisa diparse, return False (dianggap
    beda -- pengecekan teks biasa yang menangani kasus non-numerik)."""
    va, vb = _approx_numeric_value(a), _approx_numeric_value(b)
    if va is None or vb is None:
        return False
    return math.isclose(va, vb, rel_tol=1e-9, abs_tol=1e-9)


def extract_answer_llm(raw_text: str, model: str = DEFAULT_MODEL) -> LLMAnswerResult:
    """
    Minta LLM MENEMUKAN & MENYALIN (bukan menghitung ulang) jawaban akhir
    dari `raw_text`. Hasilnya WAJIB lolos `_verify_verbatim` sebelum
    dianggap valid -- kalau tidak, dianggap gagal (None), item pemanggil
    akan tetap `pending_mcq_conversion`.
    """
    prompt = f"""Kamu adalah asisten yang membaca kunci jawaban dari buku matematika Indonesia (SD-SMA).

TUGAS: temukan JAWABAN AKHIR yang SUDAH TERTULIS di teks di bawah, lalu SALIN PERSIS seperti tertulis di teks. JANGAN menghitung ulang, JANGAN memperbaiki, JANGAN mengarang jawaban yang tidak ada di teks.

ATURAN:
- Kalau teks berisi BEBERAPA jawaban terpisah untuk beberapa sub-bagian (a, b, c, d, dst yang jawabannya beda-beda), balas persis: {_NO_ANSWER_MARKER}
- Kalau teks berisi TABEL MENJODOHKAN atau beberapa skenario/pertanyaan
  berbeda yang masing-masing punya jawabannya sendiri (mis. "Kolom A/Kolom
  B", beberapa nama orang dengan harga/hasil masing-masing), itu BUKAN satu
  jawaban tunggal -- balas persis: {_NO_ANSWER_MARKER}. JANGAN asal pilih
  salah satu dari beberapa jawaban yang ada.
- Kalau teks HANYA berisi narasi/panduan untuk GURU (refleksi, rubrik
  penilaian, catatan miskonsepsi siswa, instruksi pembelajaran, dsb) TANPA
  ada soal-dan-jawaban yang jelas, itu artinya TIDAK ADA jawaban di teks
  ini -- balas persis: {_NO_ANSWER_MARKER}. JANGAN comot potongan kalimat
  acak dari narasi itu hanya karena kata/frasanya ada di teks.
- Jawaban harus berupa NILAI AKHIR YANG SINGKAT: angka (boleh dengan satuan), ekspresi/persamaan, himpunan/koordinat, atau kata/frasa pendek (maksimal 6 kata). Kalau jawaban di teks berupa KALIMAT PENJELASAN atau uraian panjang, balas persis: {_NO_ANSWER_MARKER}
- Kalau jawaban akhirnya tidak jelas atau tidak ada, balas persis: {_NO_ANSWER_MARKER}
- Balas HANYA dengan jawabannya saja (atau {_NO_ANSWER_MARKER}), TANPA penjelasan, TANPA tanda kutip, TANPA kalimat tambahan.

TEKS:
\"\"\"
{raw_text}
\"\"\"

JAWABAN AKHIR:
/no_think"""

    raw_response = call_ollama(prompt, model=model, temperature=0.1)
    if raw_response is None:
        return LLMAnswerResult(None, 0.0, "llm_unavailable", ["llm_call_failed"])

    candidate = raw_response.strip().strip('"').strip("'").strip()
    # LLM kadang bungkus jawabannya dengan reasoning/markdown walau sudah
    # dilarang -- ambil baris terakhir yang tidak kosong sebagai fallback
    # parsing kalau responsnya multi-baris.
    if "\n" in candidate:
        lines = [l.strip() for l in candidate.splitlines() if l.strip()]
        if lines:
            candidate = lines[-1]

    if not candidate or candidate.upper().replace(" ", "_") == _NO_ANSWER_MARKER:
        return LLMAnswerResult(None, 0.0, "llm_none", ["llm_no_answer_found"])

    if not _verify_verbatim(candidate, raw_text):
        return LLMAnswerResult(None, 0.0, "llm_unverified", ["llm_verification_failed"])

    return LLMAnswerResult(candidate, 0.7, "llm_extracted", [])


def generate_distractors_llm(
    raw_text: str, correct_answer: str, count: int = 3, model: str = DEFAULT_MODEL
) -> Optional[List[str]]:
    """
    Minta LLM membuat `count` distractor yang masuk akal (meniru
    miskonsepsi/kesalahan umum siswa) untuk jawaban non-angka (deskriptif/
    formula/multi-konsep) yang tidak bisa disentuh oleh
    `generate_numeric_distractors` rule-based.

    Return None kalau gagal apapun alasannya (Ollama down, respons bukan
    JSON valid, jumlah distractor kurang dari `count` setelah dibuang yang
    duplikat/sama dengan jawaban benar) -- pemanggil akan anggap ini
    "belum bisa", item tetap `pending_mcq_conversion`.
    """
    prompt = f"""Kamu adalah pembuat soal matematika untuk siswa SD-SMA Indonesia.

Diberikan konteks soal dan JAWABAN YANG BENAR di bawah, buatkan {count} PILIHAN JAWABAN SALAH (distractor) yang MASUK AKAL -- meniru kesalahan yang biasa dilakukan siswa (salah konsep, salah langkah, salah rumus), BUKAN jawaban acak yang jelas-jelas tidak masuk akal.

ATURAN:
- {count} distractor harus BEDA NILAI/MAKNA dari jawaban benar, BUKAN cuma beda cara penulisan.
  Contoh SALAH (dilarang): kalau jawaban benar "2/3", JANGAN buat distractor "4/6" atau "6/9"
  -- itu NILAINYA SAMA (pecahan senilai), cuma ditulis beda, jadi tetap "benar" kalau dipilih.
  Kalau jawaban berupa pecahan/desimal/persen, SEDERHANAKAN dulu di kepala kamu dan pastikan
  tiap distractor punya NILAI SEDERHANA yang benar-benar berbeda dari jawaban benar.
- {count} distractor juga harus beda nilai satu sama lain (bukan cuma beda tulisan).
- Format/gaya penulisan harus konsisten dengan jawaban benar.
- Balas HANYA dalam format JSON list, contoh persis: ["distractor 1", "distractor 2", "distractor 3"]
- JANGAN ada teks lain di luar JSON list itu.

KONTEKS SOAL:
\"\"\"
{raw_text}
\"\"\"

JAWABAN BENAR: {correct_answer}

{count} DISTRACTOR (JSON list):
/no_think"""

    raw_response = call_ollama(prompt, model=model, temperature=0.7)
    if raw_response is None:
        return None

    match = re.search(r"\[.*\]", raw_response, re.DOTALL)
    if not match:
        return None

    try:
        parsed = json.loads(match.group(0))
    except json.JSONDecodeError:
        return None

    if not isinstance(parsed, list):
        return None

    distractors = [str(d).strip() for d in parsed if str(d).strip()]
    correct_str = str(correct_answer)
    correct_norm = _normalize_for_match(correct_str)
    # Buang yang SAMA PERSIS secara teks dengan jawaban benar...
    distractors = [d for d in distractors if _normalize_for_match(d) != correct_norm]
    # ...DAN buang yang nilainya sama secara matematis walau tulisannya beda
    # (mis. jawaban "2/3", distractor "4/6" -- ditemukan nyata terjadi saat
    # testing manual, LLM kadang menganggap pecahan senilai itu "beda").
    distractors = [d for d in distractors if not _same_numeric_value(d, correct_str)]

    # dedupe sambil pertahankan urutan -- baik secara teks maupun nilai
    # numerik (supaya 2 distractor tidak diam-diam sama, mis. "4/8" & "1/2").
    seen_text = set()
    seen_values: List[float] = []
    unique_distractors = []
    for d in distractors:
        key = _normalize_for_match(d)
        if key in seen_text:
            continue
        d_value = _approx_numeric_value(d)
        if d_value is not None and any(
            math.isclose(d_value, v, rel_tol=1e-9, abs_tol=1e-9) for v in seen_values
        ):
            continue
        seen_text.add(key)
        if d_value is not None:
            seen_values.append(d_value)
        unique_distractors.append(d)

    if len(unique_distractors) < count:
        return None

    return unique_distractors[:count]
