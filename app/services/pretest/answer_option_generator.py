"""
answer_option_generator.py -- Tahap 2 dari 3 tugas milik sendiri.

INPUT : file JSON hasil `extractor_text.py` (lihat `export_to_json` di modul
        itu) -- daftar item dengan `pertanyaan_text` mentah (soal + langkah
        pengerjaan + jawaban jadi satu blok teks), `correct_answer=None`,
        `options=[]`.
OUTPUT: file JSON dengan struktur SAMA, tapi untuk item yang berhasil
        diproses: `correct_answer` terisi (jawaban asli, verbatim dari buku,
        TIDAK PERNAH dikarang) dan `options` terisi 4 pilihan (1 benar + 3
        distractor).

Modul ini TIDAK menyentuh MongoDB (sama seperti extractor_text.py) --
tetap murni file-to-file, JSON adalah kontraknya.

PRINSIP UTAMA (harga mati, sudah disepakati sejak awal):
  - Jawaban BENAR tidak pernah digenerate/dikarang -- HARUS hasil ekstraksi
    verbatim dari `pertanyaan_text` (yang aslinya berasal dari buku).
  - Kalau jawaban akhir tidak bisa diekstrak dengan yakin (bukan angka,
    polanya tidak ketemu, atau teksnya garbled), item TIDAK dipaksakan jadi
    MCQ asal-asalan -- statusnya diubah jadi "pending_mcq_conversion" dan
    ditandai butuh tahap lanjutan (rencana ke depan: LLM open-source),
    BUKAN dibiarkan diam-diam salah atau ditebak sembarangan di sini.
  - Hanya item berstatus "draft" dari extractor_text.py yang diproses.
    Status lain (needs_image, needs_review_extraction, skipped_*) dilewati
    apa adanya -- itu bukan tanggung jawab tahap ini.

ARSITEKTUR SENGAJA DIBUAT "PLUGGABLE" (bukan cuma satu fungsi monolitik):
  - `extract_final_answer()`   -- strategi ekstraksi jawaban, saat ini
    rule-based (regex/heuristik). Kalau nanti API LLM open-source sudah
    siap, cukup tambah fungsi baru (misal `extract_final_answer_llm()`)
    dengan signature yang sama dan pasang di `generate_options_for_block()`
    sebagai fallback SEBELUM item di-mark pending -- tanpa bongkar ulang
    pipeline/format JSON di bawah ini.
  - `generate_numeric_distractors()` -- strategi bikin 3 opsi salah, saat
    ini cuma untuk jawaban yang berupa angka murni (paling umum di soal
    matematika SD-SMA). Sama seperti di atas, gampang ditambah varian LLM
    nanti untuk jawaban non-angka (deskriptif/multi-bagian).

STATUS PIPELINE YANG DIPAKAI (harus konsisten dengan `questions_pretest.py`
milik rekan tim -- lihat komentar `Settings`/status di sana):
  draft --(modul ini)--> mcq_generated   (berhasil, 4 opsi lengkap)
  draft --(modul ini)--> pending_mcq_conversion  (belum bisa dipastikan,
                                                    ditandai butuh LLM)
"""

from __future__ import annotations

import random
import re
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

# ---------------------------------------------------------------------------
# Tahap A: ekstraksi jawaban akhir (verbatim) dari raw_text
# ---------------------------------------------------------------------------

# Pola paling eksplisit dan paling bisa dipercaya: baris "Jawaban: X" /
# "Jawaban : X" / "Jawaban X" berdiri sendiri. Kadang muncul di buku yang
# section "Uji Kompetensi"-nya memang aslinya sudah pilihan ganda (lihat
# CATATAN SOAL_MCQ_ASLI di bawah).
EXPLICIT_JAWABAN_RE = re.compile(
    r"^\s*[Jj]awaban\s*:?\s+(\S.*)$", re.MULTILINE
)

# Jawaban cuma berupa satu huruf A-E -- ini indikasi soal itu ASLINYA sudah
# pilihan ganda di buku (bukan soal uraian yang perlu kita ubah jadi MCQ),
# tapi teks pilihan aslinya (A/B/C/D/E = apa) TIDAK ada di raw_text kita
# (extractor_text.py cuma ambil section kunci jawaban, bukan soal aslinya).
# Jadi walau "jawaban"-nya ketemu, kita TIDAK bisa bikin 4 opsi yang valid
# dari sini -- harus di-flag terpisah, bukan dipaksakan.
SINGLE_LETTER_ANSWER_RE = re.compile(r"^[A-Ea-e]$")

# Pola "Jadi, ... adalah <jawaban>." -- kalimat penutup paling umum di buku
# panduan guru matematika SIBI untuk mengakhiri langkah pengerjaan.
# Sengaja pakai .findall (bukan search) supaya kalau ada LEBIH dari satu
# (soal multi-bagian a/b/c/d), kita bisa ambil yang TERAKHIR dan tetap
# menandai confidence lebih rendah (karena jawaban "utuh"-nya sebenarnya
# lebih dari satu, bukan satu nilai tunggal).
# \b sesudah "Jadi" (bukan "jadinya"), dan titik hanya dianggap akhir
# kalimat kalau diikuti spasi/akhir teks -- supaya "112.500" / "4.000 unit"
# tidak terpotong jadi "112" / "4" (ditemukan nyata di review independen:
# 5 dari 23 kunci salah karena ini).
JADI_ADALAH_RE = re.compile(
    r"\b[Jj]adi\b,?\s+.*?\badalah\b\s+(.+?)(?=\.\s|\.$|\n|$)", re.DOTALL
)

# Fallback kedua: pola "<sesuatu> = <nilai>" di akhir baris -- umum untuk
# baris terakhir perhitungan aljabar/aritmetika (mis. "U100 = 6 - 693 = -687").
# Ambil bagian PALING KANAN setelah tanda "=" terakhir di baris tsb.
TRAILING_EQUALS_RE = re.compile(r"=\s*([^=\n]+)\s*$")

# Karakter minus yang sering muncul beda-beda tergantung font PDF (hyphen
# biasa, en dash, minus unicode) -- dinormalisasi ke "-" biasa supaya
# `try_parse_number` konsisten.
_MINUS_CHARS = "–−—"  # en dash, minus sign, em dash

# Deteksi soal MULTI-BAGIAN (mis. "a. ... b. ... c. ... d. ..." -- tiap
# bagian punya jawaban SENDIRI-SENDIRI, bukan satu nilai tunggal). Ketemu
# saat testing: kalau dibiarkan, heuristik ekstraksi jawaban (terutama
# `trailing_equals`) cuma ambil baris/nilai TERAKHIR dan salah menjadikannya
# "jawaban" seluruh soal -- padahal itu cuma jawaban bagian d/h/dst saja.
# Item begini SENGAJA di-pending, bukan dipaksakan jadi MCQ satu-jawaban.
# Label sub-bagian bisa muncul di mana saja -- awal baris ("b. r = 0,5"),
# disambung koma ("a. r=1, b. r=0,5, ..."), atau nempel langsung setelah
# nomor item ("5. a) r = 0,7071") -- semua pola ini ditemukan pas testing.
# Sengaja dibuat LONGGAR (cuma butuh word-boundary sebelum huruf) daripada
# ketat -- risikonya soal single-jawaban yang kebetulan match ikut
# di-pending juga, tapi itu jauh lebih aman daripada soal multi-jawaban
# lolos dan salah digenerate jadi 1 correct_answer.
SUBPART_LABEL_RE = re.compile(r"\b([a-h])[.)]\s+\S")

# Frasa yang menandakan jawaban TIDAK TUNGGAL/BERVARIASI ("ada banyak
# kemungkinan nilai a dan b...", dst) -- mirip semangat OPEN_ENDED_RE di
# extractor_text.py, tapi pola kalimatnya beda dan belum tercakup di sana.
# Dicek lagi di sini sebagai jaring pengaman kedua (defense in depth),
# BUKAN pengganti perbaikan di extractor_text.py -- idealnya pola ini juga
# ditambahkan ke OPEN_ENDED_PATTERNS di sana supaya soal begini sudah
# ke-skip dari tahap 1, bukan baru ketahuan di tahap 2 ini.
MULTIPLE_VALID_ANSWERS_RE = re.compile(
    r"ada\s+banyak\s+kemungkinan|banyak\s+kemungkinan\s+(jawaban|nilai)|"
    r"tidak\s+tunggal|jawaban\s+lain\s+yang\s+mungkin|"
    # dua nilai sekaligus: "x1 = −2 atau x2 = −3", "x = 3 dan x = −6"
    r"\b[a-z]\s*[12₁₂]?\s*=\s*[−–\-]?\s*\d[\d.,/]*\s*(atau|dan)\s+[a-z]\s*[12₁₂]?\s*=",
    re.IGNORECASE,
)


# Baris berisi persamaan hitung ("5–3=", "2 + 6 = ...", "... + 4 = 10").
_EQUATION_LINE_RE = re.compile(r"[\d.…]\s*[+\-–−×x*:÷/]\s*[\d.…]+[^=]*=|=\s*[\d.…]")


_EXPLANATION_WORD_RE = re.compile(
    r"\b(karena|sehingga|yaitu|yakni|maka|dengan demikian|artinya|merupakan|adalah|jika|apabila)\b",
    re.IGNORECASE,
)
_TRUE_FALSE_RE = re.compile(r"^(benar|salah|ya|tidak|bukan|iya)\b[.!]?", re.IGNORECASE)
_LEADING_ITEM_NO_RE = re.compile(r"^\s*\d{1,2}\.\s*")
_SOAL_GARBLED_RE = re.compile(
    r"[\x00-\x08\x0b\x0e-\x1f]"          # karakter kontrol
    r"|\b\d[a-z]{3,}\b"                    # angka menempel huruf: "6ebagai"
    r"|\b[A-Z][a-z]+[A-Z][a-z]+\b"          # huruf besar di tengah kata: "MaZab"
)
_NEEDS_FIGURE_RE = re.compile(
    r"perhatikan\s+(gambar|grafik|diagram|tabel)|gambar\s+(berikut|di\s+(bawah|samping|atas))|"
    r"grafik\s+(berikut|di\s+bawah)|pada\s+gambar|seperti\s+gambar|\bGambar\s+\d",
    re.IGNORECASE,
)
MAX_ANSWER_WORDS = 6


def _answer_shape_problem(answer: str) -> Optional[str]:
    """None kalau jawaban layak jadi opsi pilihan ganda (singkat). Kalau
    tidak, kembalikan nama flag alasannya:
      answer_true_false_not_mcq4 -- Benar/Salah/Ya/Tidak: cuma 2 pilihan
                                    bermakna, tidak bisa jadi 4 opsi A-D
      answer_not_short           -- kalimat/penjelasan, bukan nilai akhir
    """
    a = (answer or "").strip().rstrip(".")
    if not a:
        return "answer_not_short"
    if _TRUE_FALSE_RE.match(a):
        return "answer_true_false_not_mcq4"
    words = re.findall(r"[A-Za-z]{2,}", a)          # kata alfabet (bukan variabel 1 huruf)
    if len(words) > MAX_ANSWER_WORDS or len(a) > 80:
        return "answer_not_short"
    if len(words) >= 3 and _EXPLANATION_WORD_RE.search(a):
        return "answer_not_short"
    return None


_BARE_NUM_LINE_RE = re.compile(r"^\s*-?\d+([.,]\d+)?\s*\.?\s*$")


def _final_side(candidate: str) -> str:
    """"2.430 – 450 = 1.980" -> "1.980" (ambil ruas paling kanan)."""
    if candidate and "=" in candidate:
        candidate = candidate.rsplit("=", 1)[1].strip()
    return candidate


def _looks_split_fraction(raw_text: str, match, candidate: str) -> bool:
    """Angka tunggal yang tepat diikuti/didahului baris angka tunggal lain =
    kemungkinan besar pecahan bersusun yang dipecah PDF jadi 2 baris."""
    if not re.fullmatch(r"-?\d+", candidate.strip()):
        return False
    after = [l for l in raw_text[match.end():].splitlines() if l.strip()][:1]
    if after and _BARE_NUM_LINE_RE.match(after[0]):
        return True
    return False


def _looks_multi_part(raw_text: str) -> bool:
    """True kalau ada >= 2 label sub-bagian huruf (a./b./c./dst) di awal
    baris -- indikasi soal ini punya beberapa jawaban terpisah, bukan satu
    nilai tunggal yang bisa dijadikan 1 correct_answer MCQ."""
    labels = {m.group(1).lower() for m in SUBPART_LABEL_RE.finditer(raw_text)}
    return len(labels) >= 2


@dataclass
class AnswerExtractionResult:
    answer: Optional[str]
    confidence: float
    method: str                     # "explicit_jawaban" | "jadi_adalah" | "trailing_equals" | "none"
    flags: List[str] = field(default_factory=list)


def _clean_answer_text(text: str) -> str:
    text = text.strip()
    # buang tanda baca penutup kalimat yang ikut kebawa ("...adalah 5,3")
    text = text.rstrip(" .,;")
    for ch in _MINUS_CHARS:
        text = text.replace(ch, "-")
    return text.strip()


def extract_final_answer(raw_text: str) -> AnswerExtractionResult:
    """
    Coba ekstrak jawaban akhir dari `raw_text`, URUTAN PRIORITAS dari yang
    paling eksplisit/bisa dipercaya ke yang paling heuristik:

      1. "Jawaban: X" eksplisit          (confidence tinggi)
      2. "Jadi, ... adalah X."           (confidence sedang -- kalimat
                                           penutup umum, tapi bisa salah
                                           potong kalau kalimatnya rumit)
      3. "... = X" di baris terakhir     (confidence rendah -- cuma tebakan
                                           struktural, bukan makna)
      4. Tidak ketemu pola apa pun       -> None, confidence 0.0

    TIDAK PERNAH mengarang isi jawaban -- kalau tidak ketemu pola, kembalikan
    None supaya pemanggil menandai item ini `pending_mcq_conversion`.
    """
    flags: List[str] = []

    explicit_matches = EXPLICIT_JAWABAN_RE.findall(raw_text)
    if explicit_matches:
        candidate = _clean_answer_text(explicit_matches[-1])
        if SINGLE_LETTER_ANSWER_RE.match(candidate):
            # Soal ini kemungkinan ASLINYA sudah pilihan ganda di buku, tapi
            # teks opsi A/B/C/D aslinya tidak kita punya -- tidak bisa
            # dipakai untuk generate 4 opsi yang valid dari sini.
            return AnswerExtractionResult(
                answer=candidate,
                confidence=0.3,
                method="explicit_jawaban_letter_only",
                flags=["possible_original_mcq_no_option_text"],
            )
        if len(explicit_matches) > 1:
            flags.append("multiple_jawaban_lines_found")
        return AnswerExtractionResult(
            answer=candidate, confidence=0.9, method="explicit_jawaban", flags=flags
        )

    jadi = list(JADI_ADALAH_RE.finditer(raw_text))
    if jadi:
        cands = [_final_side(_clean_answer_text(m.group(1))) for m in jadi]
        if len({c for c in cands if c}) > 1:
            # Beberapa kesimpulan "Jadi ... adalah" dengan nilai BERBEDA =
            # soal multi-bagian -> tidak bisa jadi satu kunci.
            return AnswerExtractionResult(None, 0.0, "none", ["multiple_final_statements"])
        m = jadi[-1]
        candidate = cands[-1]
        if candidate and _looks_split_fraction(raw_text, m, candidate):
            # "adalah 63\n38" = pecahan 38/63 yang terpecah dua baris oleh
            # PDF -- mengambil satu angkanya saja = kunci SALAH.
            return AnswerExtractionResult(None, 0.0, "none", ["possible_split_fraction"])
        if candidate:
            return AnswerExtractionResult(
                answer=candidate, confidence=0.6, method="jadi_adalah", flags=flags
            )

    lines = [l.strip() for l in raw_text.splitlines() if l.strip()]
    # Tebakan "angka setelah = di baris terakhir" cuma aman kalau persamaannya
    # SATU. Ditemukan nyata (hasil PyMuPDF SD 1): "5–3= / 1–0= 1 / 2–0= 2 /
    # 3–0= 3" sempat dijadikan SATU jawaban "3" -- padahal itu beberapa soal
    # hitung sekaligus tanpa label a./b. (lolos dari _looks_multi_part).
    if sum(1 for l in lines if _EQUATION_LINE_RE.search(l)) >= 2:
        return AnswerExtractionResult(
            answer=None, confidence=0.0, method="none",
            flags=["multiple_equations_no_final_statement"],
        )
    if lines:
        m = TRAILING_EQUALS_RE.search(lines[-1])
        if m:
            candidate = _clean_answer_text(m.group(1))
            if candidate:
                return AnswerExtractionResult(
                    answer=candidate,
                    confidence=0.35,
                    method="trailing_equals",
                    flags=["low_confidence_structural_guess"],
                )

    return AnswerExtractionResult(
        answer=None, confidence=0.0, method="none", flags=["no_answer_pattern_found"]
    )


# ---------------------------------------------------------------------------
# Tahap B: parse angka dari jawaban yang berhasil diekstrak
# ---------------------------------------------------------------------------

# Menangkap angka termasuk format Indonesia (titik ribuan, koma desimal)
# dan opsional prefix "Rp"/"Rp." di depan.
NUMBER_TOKEN_RE = re.compile(
    r"(?P<prefix>Rp\.?\s*)?(?P<sign>-)?(?P<num>\d{1,3}(?:\.\d{3})*(?:,\d+)?|\d+(?:[.,]\d+)?)(?P<suffix>\s*%)?"
)


def try_parse_number(answer_text: str) -> Optional[Tuple[float, str, str]]:
    """
    Coba parse `answer_text` sebagai satu angka tunggal (boleh ada prefix
    "Rp"/suffix "%", format Indonesia titik-ribuan/koma-desimal).

    PENTING: hanya menerima kalau SELURUH `answer_text` (setelah dibersihkan
    dari prefix/suffix umum) adalah representasi satu angka -- kalau ada
    teks lain yang menyertainya (mis. "38 unit" atau "Domain: [0, 3)"),
    dianggap GAGAL parse, bukan dipotong paksa. Ini supaya distractor numerik
    tidak dibikin dari jawaban yang sebenarnya bukan angka murni.

    Return (nilai_float, prefix_asli, suffix_asli) kalau berhasil, else None.
    """
    text = answer_text.strip()
    m = NUMBER_TOKEN_RE.fullmatch(text)
    if not m:
        return None

    num_str = m.group("num")
    # format Indonesia: "1.234,56" -> hilangkan titik ribuan, koma jadi titik
    if "," in num_str and "." in num_str:
        num_str = num_str.replace(".", "").replace(",", ".")
    elif "," in num_str:
        num_str = num_str.replace(",", ".")
    # kalau cuma ada titik dan itu titik ribuan (mis. "20.000.000", "112.500",
    # "1.980"), hilangkan. Buku Indonesia menulis desimal dengan KOMA, jadi
    # "angka.3-digit" = ribuan (versi lama membaca "112.500" sebagai 112,5).
    elif num_str.count(".") > 1 or re.fullmatch(r"\d{1,3}(\.\d{3})+", num_str):
        num_str = num_str.replace(".", "")

    try:
        value = float(num_str)
    except ValueError:
        return None

    if m.group("sign") == "-":
        value = -value

    prefix = (m.group("prefix") or "").strip()
    suffix = (m.group("suffix") or "").strip()
    return value, prefix, suffix


def _format_like(value: float, original_num_str: str, prefix: str, suffix: str) -> str:
    """Format ulang `value` supaya gaya penulisannya semirip mungkin dengan
    jawaban asli (pakai titik ribuan & koma desimal ala Indonesia kalau
    aslinya begitu, jumlah desimal yang sama, prefix/suffix yang sama)."""
    is_decimal_comma = "," in original_num_str
    decimals = 0
    if is_decimal_comma:
        decimals = len(original_num_str.split(",")[-1])
    elif "." in original_num_str and original_num_str.count(".") == 1 and len(
        original_num_str.split(".")[-1]
    ) <= 2:
        # kemungkinan titik desimal (bukan ribuan), misal "47,5" sudah
        # ditangani di atas; ini untuk kasus format non-Indonesia longgar.
        decimals = len(original_num_str.split(".")[-1])

    if decimals:
        text = f"{value:,.{decimals}f}"
    else:
        text = f"{int(round(value)):,}"
    text = text.replace(",", "#").replace(".", ",").replace("#", ".")

    out = f"{prefix}{text}{suffix}".strip()
    return out if prefix or suffix else text


def generate_numeric_distractors(
    value: float, original_num_str: str, prefix: str, suffix: str, count: int = 3
) -> List[str]:
    """
    Generate `count` pengecoh numerik yang MASUK AKAL untuk jawaban `value`:
      - tanda SAMA dengan jawaban benar (versi lama membalik tanda -> muncul
        panjang/peluang/jari-jari negatif, ditemukan oleh review independen)
      - jarak "wajar" sesuai besaran angka (1, 2, 5, 10, 50, 100, ...), jadi
        pengecoh terlihat seperti hasil salah hitung, bukan angka acak
      - banyak desimal sama dengan jawaban benar
      - nilai 0 < x <= 1 (peluang, dst) tetap di rentang (0, 1]
    Pengecoh yang sama nilainya dengan jawaban benar / satu sama lain dibuang.
    """
    import math

    dec = 0
    num = original_num_str or ""
    if "," in num:
        dec = len(num.split(",")[-1])
    elif "." in num and not re.fullmatch(r"\d{1,3}(\.\d{3})+", num):
        dec = len(num.split(".")[-1])
    mag = abs(value)
    unit_interval = 0 < value <= 1 and dec > 0

    if unit_interval:
        step = 10 ** (-dec) * (5 if dec >= 2 and value >= 0.2 else 1)
        step = max(step, 10 ** (-dec))
    elif dec > 0:
        step = max(10 ** (-dec), round(mag * 0.1, dec) or 10 ** (-dec))
    else:
        if mag < 20:
            step = 1
        else:
            p = 10 ** (int(math.log10(mag)) - 1)          # 57 -> 1, 687 -> 10, 112500 -> 10000
            step = p if mag / p < 30 else p * 5
            step = max(1, step)

    seen = {round(value, 9)}
    out: List[float] = []
    k = 1
    while len(out) < count and k < 60:
        for c in (value + k * step, value - k * step):
            c = round(c, dec)
            if round(c, 9) in seen:
                continue
            if value >= 0 and c < 0:
                # jawaban 0 atau positif -> pengecoh tidak boleh negatif
                # (jawaban 0 sering berupa banyak benda / peluang)
                continue
            if value > 0 and c == 0:
                continue
            if value < 0 and c >= 0:
                continue
            if unit_interval and not (0 < c <= 1):
                continue
            seen.add(round(c, 9))
            out.append(c)
            if len(out) == count:
                break
        k += 1
    return [_format_like(v, original_num_str, prefix, suffix) for v in out[:count]]


def _extract_num_str_for_format(answer_text: str) -> str:
    m = NUMBER_TOKEN_RE.fullmatch(answer_text.strip())
    return m.group("num") if m else answer_text


# ---------------------------------------------------------------------------
# Tahap C: rakit 4 opsi (1 benar + 3 distractor), acak posisinya
# ---------------------------------------------------------------------------

OPTION_IDS = ["A", "B", "C", "D"]


def build_options(correct_answer: str, distractors: List[str]) -> List[dict]:
    """Susun 4 opsi dengan posisi jawaban benar DIACAK (bukan selalu di
    posisi A), supaya tidak ada bias posisi untuk sistem yang memakainya
    nanti."""
    texts = [correct_answer] + distractors
    random.shuffle(texts)
    return [{"option_id": oid, "text": t} for oid, t in zip(OPTION_IDS, texts)]


# ---------------------------------------------------------------------------
# Tahap D: pipeline per-item & batch (baca/tulis JSON hasil extractor_text.py)
# ---------------------------------------------------------------------------

def generate_options_for_block(
    item: dict, use_llm: bool = False, llm_model: Optional[str] = None
) -> dict:
    """
    Proses SATU item (dict, format sama seperti `RawSoalBlock.to_dict()`
    dari extractor_text.py). Mengubah item IN-PLACE dan juga
    mengembalikannya untuk kemudahan chaining.

    Item yang statusnya BUKAN "draft" (needs_image, needs_review_extraction,
    skipped_open_ended, skipped_pembuktian) dilewati apa adanya -- bukan
    tanggung jawab tahap ini untuk memutuskan soal itu layak/tidak, itu
    sudah keputusan `extractor_text.py`.

    `use_llm=False` (default): PERILAKU SAMA PERSIS seperti sebelum LLM
    dipasang -- murni rule-based, tanpa panggilan jaringan sama sekali.
    Ini penting supaya kode lama/hasil testing sebelumnya tidak berubah
    kalau parameter ini tidak disebut secara eksplisit.

    `use_llm=True`: dua titik yang sebelumnya langsung divonis
    "pending_mcq_conversion" (ekstraksi jawaban gagal, ATAU distractor
    numerik tidak bisa dibuat karena jawabannya bukan angka) SEKARANG
    dicoba dulu lewat LLM lokal (Ollama) sebagai lapis kedua -- lihat
    `llm_backend.py`. Kalau LLM juga gagal (Ollama tidak jalan, atau
    hasilnya gagal verifikasi verbatim), item tetap jatuh ke
    "pending_mcq_conversion" seperti biasa -- TIDAK ADA PERUBAHAN PERILAKU
    untuk kasus gagal, cuma nambah satu kesempatan sebelum menyerah.
    Soal multi-bagian & "banyak kemungkinan jawaban" TETAP langsung
    di-pending tanpa dicoba LLM -- itu masalah struktural soal itu sendiri,
    bukan masalah "regex kurang pintar", jadi LLM tidak akan membantu.
    """
    if item.get("status") != "draft":
        return item

    extraction_flags: List[str] = list(item.get("extraction_flags", []))
    # Sumber KUNCI JAWABAN = teks Buku Guru. Sejak ada soal_merger.py
    # (stage1b), untuk item yang soalnya dilengkapi dari Buku Siswa,
    # `pertanyaan_text` berisi SOAL (Buku Siswa) sedangkan teks Guru aslinya
    # dipindah ke `jawaban_text_guru`. Jawaban tetap HARUS diambil (dan
    # diverifikasi verbatim) dari teks Guru, bukan dari teks soal. Untuk
    # input stage1 lama (tanpa field ini) perilakunya sama persis seperti
    # sebelumnya.
    raw_text = item.get("jawaban_text_guru") or item.get("pertanyaan_text", "")
    soal_stem = item.get("pertanyaan_text", "")
    llm_context = raw_text if soal_stem == raw_text else f"SOAL:\n{soal_stem}\n\nKUNCI JAWABAN (Buku Guru):\n{raw_text}"

    if _TRUE_FALSE_RE.match(_LEADING_ITEM_NO_RE.sub("", raw_text).strip()):
        # "1. Salah. Ada persamaan ... misalnya x = 1." -- soal Benar/Salah;
        # angka di penjelasannya BUKAN kunci (ditemukan nyata jadi kunci "1").
        item["status"] = "pending_mcq_conversion"
        extraction_flags.append("answer_true_false_not_mcq4")
        item["extraction_flags"] = extraction_flags
        item["mcq_generation_confidence"] = 0.0
        return item

    if soal_stem != raw_text and _SOAL_GARBLED_RE.search(soal_stem):
        # Huruf rusak akibat encoding font PDF ("6ebagai", "MaZab") atau
        # karakter kontrol -- soal tidak layak dibaca siswa.
        item["status"] = "pending_mcq_conversion"
        extraction_flags.append("soal_text_garbled")
        item["extraction_flags"] = extraction_flags
        item["mcq_generation_confidence"] = 0.0
        return item

    if soal_stem != raw_text and (_looks_multi_part(soal_stem) or _NEEDS_FIGURE_RE.search(soal_stem)):
        # Soal Siswa punya sub-soal a/b/c atau butuh gambar/grafik yang tidak ikut.
        item["status"] = "pending_mcq_conversion"
        extraction_flags.append("soal_multi_part_or_needs_figure")
        item["extraction_flags"] = extraction_flags
        item["mcq_generation_confidence"] = 0.0
        return item

    if _looks_multi_part(raw_text):
        # Soal punya beberapa sub-bagian (a/b/c/d...), masing-masing jawaban
        # sendiri -- tidak bisa direduksi jadi 1 correct_answer MCQ tanpa
        # memecah soal itu sendiri (di luar scope tahap ini). Di-pending,
        # bukan asal ambil salah satu bagian sebagai "jawabannya".
        item["status"] = "pending_mcq_conversion"
        extraction_flags.append("multi_part_item_cannot_auto_mcq")
        item["extraction_flags"] = extraction_flags
        item["mcq_generation_confidence"] = 0.0
        return item

    if MULTIPLE_VALID_ANSWERS_RE.search(raw_text):
        item["status"] = "pending_mcq_conversion"
        extraction_flags.append("multiple_valid_answers_suspected")
        item["extraction_flags"] = extraction_flags
        item["mcq_generation_confidence"] = 0.0
        return item

    result = extract_final_answer(raw_text)
    extraction_flags.extend(result.flags)

    answer_text: Optional[str] = result.answer
    answer_confidence = result.confidence
    used_llm_for_answer = False

    if answer_text is None or "possible_original_mcq_no_option_text" in result.flags:
        # Kasus 1: tidak ketemu pola jawaban sama sekali (rule-based).
        # Kasus 2: jawaban ketemu tapi cuma huruf A-E tanpa teks opsi asli
        #          -- rule-based tidak bisa apa-apa untuk kasus 2 (LLM juga
        #          tidak bisa membantu -- masalahnya teks opsi aslinya
        #          memang tidak ada di data kita, bukan soal ekstraksi).
        if use_llm and "possible_original_mcq_no_option_text" not in result.flags:
            from app.services.pretest.llm_backend import extract_answer_llm, DEFAULT_MODEL

            llm_result = extract_answer_llm(raw_text, model=llm_model or DEFAULT_MODEL)
            extraction_flags.extend(llm_result.flags)
            if llm_result.answer is not None:
                answer_text = llm_result.answer
                answer_confidence = llm_result.confidence
                used_llm_for_answer = True
                # Ditandai LANGSUNG di sini (bukan cuma di cabang distraktor-LLM
                # di bawah) supaya jejak "correct_answer ini asalnya dari LLM,
                # bukan rule-based" tetap ada walau jalur setelahnya numeric
                # distractor (rule-based) berhasil -- penting untuk prioritas
                # review manual nanti, jangan sampai item begini keliatan
                # "murni rule-based" padahal jawabannya lewat LLM.
                extraction_flags.append("answer_extracted_by_llm")

        if answer_text is None:
            item["correct_answer"] = result.answer  # tetap simpan kalau ada (kasus 2), verbatim
            item["status"] = "pending_mcq_conversion"
            if "needs_llm_answer_extraction" not in extraction_flags:
                extraction_flags.append("needs_llm_answer_extraction")
            item["extraction_flags"] = extraction_flags
            item["mcq_generation_confidence"] = result.confidence
            return item

    # FORMAT PRETEST: jawaban benar (dan karenanya opsi A-D) harus berupa
    # NILAI SINGKAT -- angka, ekspresi, simbol, himpunan, atau kata/frasa
    # pendek -- bukan kalimat penjelasan. Dicek mekanis di sini untuk SEMUA
    # jalur (rule-based maupun LLM).
    shape_problem = _answer_shape_problem(answer_text)
    if shape_problem:
        item["correct_answer"] = answer_text
        item["status"] = "pending_mcq_conversion"
        extraction_flags.append(shape_problem)
        item["extraction_flags"] = extraction_flags
        item["mcq_generation_confidence"] = 0.0
        return item

    parsed = try_parse_number(answer_text)
    if parsed is not None:
        value, prefix, suffix = parsed
        original_num_str = _extract_num_str_for_format(answer_text)
        distractors = generate_numeric_distractors(value, original_num_str, prefix, suffix)

        item["correct_answer"] = answer_text
        item["options"] = build_options(answer_text, distractors)
        item["status"] = "mcq_generated"
        item["extraction_flags"] = extraction_flags
        item["mcq_generation_confidence"] = answer_confidence
        return item

    # Jawaban berhasil diekstrak (rule-based atau LLM), tapi bukan angka
    # murni (deskriptif / formula / mengandung satuan-teks) -- distractor
    # numerik tidak bisa diterapkan dengan aman. Coba distractor via LLM
    # kalau diizinkan.
    distractors_llm: Optional[List[str]] = None
    if use_llm:
        from app.services.pretest.llm_backend import generate_distractors_llm, DEFAULT_MODEL

        distractors_llm = generate_distractors_llm(
            llm_context, answer_text, model=llm_model or DEFAULT_MODEL
        )
        if distractors_llm is not None:
            extraction_flags.append("distractors_generated_by_llm")
            # "answer_extracted_by_llm" (kalau relevan) sudah ditambahkan di
            # atas segera setelah LLM berhasil ekstrak jawabannya -- tidak
            # perlu ditambahkan lagi di sini.

    if distractors_llm is None:
        item["correct_answer"] = answer_text
        item["status"] = "pending_mcq_conversion"
        if "needs_llm_distractor_generation" not in extraction_flags:
            extraction_flags.append("needs_llm_distractor_generation")
        item["extraction_flags"] = extraction_flags
        item["mcq_generation_confidence"] = answer_confidence
        return item

    item["correct_answer"] = answer_text
    item["options"] = build_options(answer_text, distractors_llm)
    item["status"] = "mcq_generated"
    item["extraction_flags"] = extraction_flags
    item["mcq_generation_confidence"] = answer_confidence
    return item


def summarize_by_status(items: List[dict]) -> dict:
    summary: dict = {}
    for it in items:
        summary[it["status"]] = summary.get(it["status"], 0) + 1
    summary["_total"] = len(items)
    return summary


def process_export_file(
    input_path: str,
    output_path: str,
    use_llm: bool = False,
    llm_model: Optional[str] = None,
    show_progress: bool = True,
) -> dict:
    """
    Baca file JSON hasil `export_to_json()` dari extractor_text.py, proses
    tiap item lewat `generate_options_for_block`, tulis ulang ke
    `output_path` (bisa sama dengan input_path kalau mau overwrite).

    `use_llm=False` (default) -- perilaku lama, murni rule-based, tanpa
    panggilan jaringan. Set `use_llm=True` untuk mengaktifkan fallback
    Ollama pada item yang gagal di tahap rule-based (lihat docstring
    `generate_options_for_block`).

    `show_progress=True` (default) -- cetak progres per-item ke stdout
    ("[12/37] draft -> mcq_generated"). PENTING terutama saat `use_llm=True`,
    karena tiap item yang butuh LLM bisa makan beberapa detik-puluhan detik
    (panggilan jaringan ke Ollama) -- tanpa ini, proses batch bisa kelihatan
    seperti macet padahal sebenarnya jalan normal, cuma tidak ada output
    apapun sampai semuanya selesai. Set False untuk pemakaian non-interaktif
    (mis. dipanggil dari script lain yang sudah punya progress sendiri).
    """
    import json
    import os

    raw_items = _load_items(input_path)
    total = len(raw_items)
    items = []
    for idx, it in enumerate(raw_items, start=1):
        original_status = it.get("status")
        processed = generate_options_for_block(it, use_llm=use_llm, llm_model=llm_model)
        items.append(processed)
        if show_progress:
            print(
                f"  [{idx}/{total}] {original_status} -> {processed.get('status')}",
                flush=True,
            )
    payload = _load_payload(input_path)
    summary = summarize_by_status(items)

    parent_dir = os.path.dirname(output_path)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)

    # File UTAMA (untuk diserahkan ke loader tim) HANYA berisi soal yang
    # benar-benar jadi pilihan ganda (status "mcq_generated"). Sisanya
    # (pending_mcq_conversion, needs_review_*, dst) disimpan di
    # *_ditolak.json untuk audit -- tidak ikut dipakai.
    final = [it for it in items if it.get("status") == "mcq_generated"]
    rest = [it for it in items if it.get("status") != "mcq_generated"]
    summary["_final_mcq"] = len(final)
    summary["_ditolak"] = len(rest)
    main_payload = {k: v for k, v in payload.items() if k not in ("items", "summary", "diagnostics")}
    main_payload.update({"summary": summary, "items": final})
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(main_payload, f, indent=2, ensure_ascii=False)
    rejected_path = output_path[:-5] + "_ditolak.json" if output_path.endswith(".json") else output_path + "_ditolak.json"
    with open(rejected_path, "w", encoding="utf-8") as f:
        json.dump({"summary": summary, "items": rest}, f, indent=2, ensure_ascii=False)

    return summary


def _load_payload(input_path: str) -> dict:
    import json

    with open(input_path, encoding="utf-8") as f:
        return json.load(f)


def _load_items(input_path: str) -> List[dict]:
    return _load_payload(input_path).get("items", [])


def _cli():
    import argparse

    parser = argparse.ArgumentParser(
        description="Tahap 2: pisahkan jawaban bersih + generate 4 opsi MCQ "
        "dari file JSON hasil extractor_text.py."
    )
    parser.add_argument("--in", dest="input_path", required=True, help="Path JSON input (hasil extractor_text.py)")
    parser.add_argument("--out", dest="output_path", required=True, help="Path JSON output")
    parser.add_argument(
        "--use-llm",
        action="store_true",
        help="Aktifkan fallback LLM lokal (Ollama) untuk item yang gagal di rule-based. "
        "Butuh Ollama jalan di localhost:11434 dengan model yang sudah di-pull.",
    )
    parser.add_argument(
        "--llm-model",
        default=None,
        help="Nama model Ollama (default: qwen3:4b, lihat llm_backend.DEFAULT_MODEL)",
    )
    args = parser.parse_args()

    summary = process_export_file(
        args.input_path, args.output_path, use_llm=args.use_llm, llm_model=args.llm_model
    )
    print("Selesai. Ringkasan status setelah tahap 2:")
    for status, count in summary.items():
        print(f"  {status}: {count}")
    print(f"\nOutput tersimpan di: {args.output_path}")


if __name__ == "__main__":
    _cli()
