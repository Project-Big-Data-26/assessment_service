"""
soal_merger.py -- Tahap 1b: melengkapi TEKS SOAL dari Buku Siswa untuk
kunci jawaban hasil extractor_text.py (Buku Panduan Guru).

ALUR PIPELINE:
  extractor_text.py (Guru, stage1.json)
      -> soal_merger.py  (+ Buku Siswa)  -> stage1b.json   <-- modul ini
      -> answer_option_generator.py      -> stage2.json

PRINSIP (sama dengan tahap lain):
  - TIDAK ada teks yang dikarang. `soal_text` = salinan verbatim Buku Siswa,
    jawaban tetap dari Buku Guru. Modul ini cuma MEMASANGKAN keduanya.
  - Pemasangan HARUS lolos verifikasi mekanis; kalau bukti lemah, item
    TIDAK dipaksa lolos -- diberi status review, bukan ditebak.
  - Tidak menyentuh MongoDB, tidak memakai LLM.

CARA MEMASANGKAN:
  1. Jawaban Guru dikelompokkan per `activity_seq` (satu grup = satu
     aktivitas, mis. "Ayo Berlatih" ke-3 atau "Latihan 1.2").
  2. Buku Siswa dipecah per section latihan (extractor_siswa.py).
  3. Grup Guru disejajarkan dengan section Siswa memakai ALIGNMENT BERURUTAN
     (dynamic programming, seperti `diff`): urutan bab/latihan di kedua buku
     sama, jadi pasangan harus maju searah; section yang tidak punya kunci
     jawaban (atau sebaliknya) boleh dilewati. Ini yang membuatnya tahan
     terhadap jumlah aktivitas yang tidak sama (terbukti nyata: Bab 1 SD
     Kelas 5 punya 4x "Ayo Berlatih" di Siswa tapi cuma 3 kunci di Guru).
  4. Skor tiap kandidat pasangan:
       - ID label sama persis ("Latihan 1.2" <-> "Latihan 1.2")  -> kuat
       - jenis label sama ("Ayo Berlatih" <-> "Ayo Berlatih")    -> sedang,
         WAJIB didukung kemiripan isi
       - grup Guru tanpa label ("A. Kunci Jawaban")             -> lemah,
         hanya diterima kalau kemiripan isinya tinggi
     Kemiripan isi = proporsi angka/kata penting di JAWABAN yang juga muncul
     di SOAL (mis. "Paket B", "72.135", "persamaan linear").
  5. Per item: dipasangkan berdasarkan nomor soal. Dicek lagi apakah soal
     lain di section yang sama ternyata JAUH lebih cocok dengan jawaban ini
     (tanda salah pasang) -> kalau ya, status review.
"""

from __future__ import annotations

import json
import os
import re
from typing import Dict, List, Optional, Tuple

from app.services.pretest.extractor_siswa import SiswaSection, extract_sections
from app.services.pretest.extractor_text import PIPELINE_VERSION, QUESTION_MARKER_RE, normalize_activity_key

# --- Kemiripan isi -----------------------------------------------------------

_STOPWORDS = {
    "jadi", "adalah", "yang", "dengan", "dari", "untuk", "maka", "sehingga",
    "jawab", "jawaban", "diketahui", "ditanya", "penyelesaian", "alternatif",
    "karena", "atau", "pada", "dalam", "akan", "bukan", "juga", "tersebut",
    "berikut", "dapat", "bisa", "harus", "setiap", "masing", "ini", "itu",
    "nilai", "hasil", "banyak", "kalian", "peserta", "didik", "siswa",
    "benar", "salah", "sama", "tidak", "lebih", "kurang", "semua", "seperti",
    "yaitu", "agar", "oleh", "kita", "kamu", "tentukan", "hitunglah",
    "berapa", "berapakah", "sebagai", "antara", "jika", "tetapi",
}
_NUM_RE = re.compile(r"\d+(?:[.,]\d+)*")
_WORD_RE = re.compile(r"[A-Za-z]{4,}")
_LEADING_NO_RE = re.compile(r"^\s*\d{1,2}\.\s*")


def _norm_num(s: str) -> str:
    # "72.135" -> "72135" (pemisah ribuan), "2,5" -> "2.5" (desimal)
    if re.fullmatch(r"\d{1,3}(\.\d{3})+", s):
        return s.replace(".", "")
    return s.replace(",", ".")


def tokens(text: str) -> set:
    text = _LEADING_NO_RE.sub("", text or "")
    nums = {_norm_num(n) for n in _NUM_RE.findall(text)}
    # angka satu digit terlalu umum (nomor sub-poin, dsb) -- bukan bukti
    nums = {n for n in nums if len(n.replace(".", "")) >= 2}
    words = {w.lower() for w in _WORD_RE.findall(text)} - _STOPWORDS
    return nums | words


def overlap(answer_tokens: set, soal_tokens: set) -> float:
    if not answer_tokens:
        return 0.0
    return len(answer_tokens & soal_tokens) / len(answer_tokens)


# --- Grup Guru ---------------------------------------------------------------

class GuruGroup:
    def __init__(self, seq: int, label: Optional[str], items: List[dict]):
        self.seq = seq
        self.label = label
        self.key = normalize_activity_key(label)
        self.items = items
        self.tok = set().union(*(tokens(i.get("jawaban_text_guru") or i.get("pertanyaan_text", "")) for i in items))


def build_guru_groups(items: List[dict]) -> List[GuruGroup]:
    groups: Dict[int, List[dict]] = {}
    labels: Dict[int, Optional[str]] = {}
    for it in items:
        seq = it.get("activity_seq")
        if seq is None:
            raise ValueError(
                "stage1 JSON tidak punya field `activity_seq`. Jalankan ulang "
                "extractor_text.py versi terbaru untuk buku ini dulu."
            )
        groups.setdefault(seq, []).append(it)
        labels[seq] = it.get("source_activity")
    ordered = sorted(groups, key=lambda s: min(
        (i.get("source_line_index") or 0) for i in groups[s]))
    return [GuruGroup(s, labels[s], groups[s]) for s in ordered]


# --- Skor pasangan grup <-> section ------------------------------------------

WILDCARD_OK_TYPES = {
    "uji_kompetensi", "evaluasi", "asesmen", "ayo berlatih", "latihan",
    "uji_pemahaman", "soal_tambahan", "soal_pengayaan",
}
MIN_SIM_TYPE_MATCH = 0.20     # jenis label sama, tanpa ID
MIN_SIM_WILDCARD = 0.35       # grup Guru tanpa label


def pair_score(g: GuruGroup, s: SiswaSection, s_tok: set) -> Optional[Tuple[float, str, float]]:
    """Return (skor, metode, kemiripan) atau None kalau tidak boleh dipasangkan."""
    sim = overlap(g.tok, s_tok)
    n, m = len(g.items), len(s.items)
    count_term = -0.5 * abs(n - m) / max(n, m, 1)
    gk, sk = g.key, s.key
    if gk is not None:
        if gk[0] != sk[0]:
            return None
        if gk[1] is not None and sk[1] is not None:
            if gk[1] != sk[1]:
                return None
            return (6.0 + 4 * sim + count_term, "section_id", sim)
        if sim < MIN_SIM_TYPE_MATCH:
            return None
        return (2.0 + 4 * sim + count_term, "section_type+content", sim)
    if sk[0] not in WILDCARD_OK_TYPES or sim < MIN_SIM_WILDCARD:
        return None
    return (0.5 + 4 * sim + count_term, "content_only", sim)


def align(groups: List[GuruGroup], sections: List[SiswaSection]):
    """DP alignment berurutan (maksimalkan total skor, boleh melewati)."""
    s_toks = [set().union(*(tokens(t) for _, t, _ in s.items)) for s in sections]
    n, m = len(groups), len(sections)
    NEG = float("-inf")
    dp = [[0.0] * (m + 1) for _ in range(n + 1)]
    back = [[None] * (m + 1) for _ in range(n + 1)]
    cache: Dict[Tuple[int, int], Optional[Tuple[float, str, float]]] = {}
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            best, arg = dp[i - 1][j], ("up",)
            if dp[i][j - 1] > best:
                best, arg = dp[i][j - 1], ("left",)
            sc = pair_score(groups[i - 1], sections[j - 1], s_toks[j - 1])
            cache[(i - 1, j - 1)] = sc
            if sc is not None and dp[i - 1][j - 1] + sc[0] > best:
                best, arg = dp[i - 1][j - 1] + sc[0], ("diag",)
            dp[i][j] = best
            back[i][j] = arg
    pairs = {}
    i, j = n, m
    while i > 0 and j > 0:
        a = back[i][j]
        if a[0] == "diag":
            pairs[i - 1] = (j - 1, cache[(i - 1, j - 1)])
            i, j = i - 1, j - 1
        elif a[0] == "up":
            i -= 1
        else:
            j -= 1
    return pairs


# --- Penggabungan per item ---------------------------------------------------

# --- Perapian teks soal (TANPA mengubah isi) ---------------------------------

_SUBITEM_START_RE = re.compile(
    # label sub-soal harus diikuti spasi/akhir baris -- "1.1?" (nomor definisi)
    # BUKAN awal sub-soal "1."
    r"^(\(?[a-h][.)](\s|$)|\d{1,2}[.)](\s|$)|[ⓐ-ⓩ]|[•►▪●◦]|[\-–]\s|Penyelesaian\b|Diketahui\b|Ditanya\b)",
    re.IGNORECASE,
)
_SENT_END_RE = re.compile(r"[.?!:]$")
_PLACEHOLDER_RE = re.compile(r"…+|\.{3,}|\(\s*\.{3,}\s*\)")


def clean_soal_text(text: str) -> str:
    """
    Rapikan teks soal hasil PDF supaya enak dibaca siswa, TANPA mengubah
    kata/angka apa pun:
      - buang tanda hubung tersembunyi (soft hyphen, "merupa\xadkan") & tab
      - buang baris footer/halaman yang ikut terbawa
      - sambung baris yang terpotong layout PDF menjadi kalimat utuh
      - sub-soal ("a.", "b)", "ⓐ", butir "►") tetap mulai di baris baru
    Teks mentah aslinya tetap disimpan di field `soal_text` untuk audit.
    """
    if not text:
        return text
    # \xad (soft hyphen) & \x02 = tanda pemenggalan kata dari PDF ("men\x02jatuhkan")
    t = text.replace("\xad", "").replace("\x02", "").replace("\t", " ")
    lines = [re.sub(r"\s+", " ", l).strip() for l in t.splitlines()]
    lines = [l for l in lines if l and not _FOOTERISH_RE.match(l)]
    out: List[str] = []
    for l in lines:
        if not out:
            out.append(l)
            continue
        prev = out[-1]
        if _SUBITEM_START_RE.match(l) or _SENT_END_RE.search(prev):
            out.append(l)
        else:
            out[-1] = f"{prev} {l}"
    return "\n".join(out).strip()


def _norm_text(t: str) -> str:
    t = _LEADING_NO_RE.sub("", t or "").lower()
    return re.sub(r"\s+", " ", t).strip()


_FOOTERISH_RE = re.compile(
    r"^(\d{1,3}\s+)?(Buku Panduan Guru\s+)?Matematika(\s+Tingkat\s+Lanjut)?\s+untuk\s+(SD|SMP|SMA).*$"
    r"|^\d{1,2}\s+[A-Z][A-Za-z ,\-]{2,60}\s\d{1,3}$"      # "5 Pecahan 141"
    r"|^[a-h][.)]?$",                                        # label sub-poin kosong
)


def _strip_noise(t: str) -> str:
    return "\n".join(l for l in (t or "").splitlines() if l.strip() and not _FOOTERISH_RE.match(l.strip()))


def _answer_restates_soal(answer: str, soal: str) -> Optional[str]:
    """
    Cek apakah jawaban Guru benar-benar berisi JAWABAN. Return:
      None                    -> ada isi jawaban
      "answer_restates_soal"  -> jawaban ~ identik dengan soal (tidak ada isi
                                 jawaban sama sekali) -- SD 1/2, jawabannya
                                 ditandai di gambar, bukan ditulis
      "answer_is_label_list"  -> perintah soal diulang + daftar kata pendek
                                 tanpa angka. BISA jawaban asli ("kubus,
                                 tabung, balok") BISA JUGA cuma label gambar
                                 ("lebih tinggi, lebih rendah") -- dari teks
                                 saja TIDAK bisa dibedakan, jadi wajib dicek
                                 manusia, tidak diloloskan otomatis.
    """
    from difflib import SequenceMatcher

    a_clean, q_clean = _strip_noise(answer), _strip_noise(soal)
    a, q = _norm_text(a_clean), _norm_text(q_clean)
    if not a:
        return "answer_restates_soal"
    if re.match(r"^(benar|salah|ya|tidak)\b", a):
        return None
    sm = SequenceMatcher(None, a, q, autojunk=False)
    matched = "".join(a[b.a:b.a + b.size] for b in sm.get_matching_blocks())
    covered = sum(b.size for b in sm.get_matching_blocks())
    uncovered = len(re.sub(r"[\W_]+", "", a)) - len(re.sub(r"[\W_]+", "", matched))
    if covered / len(a) >= 0.9 and uncovered < 3:
        return "answer_restates_soal"
    a_lines = [_norm_text(l) for l in a_clean.splitlines() if l.strip()]
    q_lines = {_norm_text(l) for l in q_clean.splitlines() if l.strip()}
    q_first = _norm_text((q_clean.splitlines() or [""])[0])
    if a_lines and len(q_first) >= 12 and a_lines[0] == q_first:
        rest = " ".join(l for l in a_lines[1:] if l not in q_lines)
        if rest and not re.search(r"[\d=+×÷<>%]", rest) and len(rest.split()) <= 8:
            return "answer_is_label_list"
    return None


def _answer_matches_only_tail(a_tok: set, soal: str) -> bool:
    lines = [l for l in soal.splitlines() if l.strip()]
    if len(lines) < 6 or len(a_tok) < 3:
        return False
    cut = max(2, len(lines) // 3)
    head = tokens("\n".join(lines[:cut]))
    tail = tokens("\n".join(lines[cut:]))
    return overlap(a_tok, head) == 0.0 and overlap(a_tok, tail) >= 0.4


def _group_confidence(method: str, sim: float) -> float:
    if method == "section_id":
        return 0.9
    if method == "section_type+content":
        return min(0.9, 0.4 + sim)
    return min(0.8, sim)


def merge(stage1: dict, sections: List[SiswaSection]) -> dict:
    items = stage1["items"]
    for it in items:
        # Teks Guru asli selalu disimpan (sumber kunci jawaban untuk tahap 2),
        # SEBELUM pertanyaan_text mungkin diganti soal dari Buku Siswa.
        it.setdefault("jawaban_text_guru", it.get("pertanyaan_text", ""))
    groups = build_guru_groups(items)
    pairs = align(groups, sections)

    for gi, g in enumerate(groups):
        match = pairs.get(gi)
        for it in g.items:
            it.setdefault("soal_text", None)
            it.setdefault("soal_source", None)
            it.setdefault("soal_match_confidence", None)
            it.setdefault("soal_match_method", None)
        if match is None:
            continue
        sj, (score, method, gsim) = match
        s = sections[sj]
        s_by_no: Dict[str, Tuple[str, int]] = {}
        for no, txt, li in s.items:
            s_by_no.setdefault(no, (txt, li))
        s_item_toks = {no: tokens(t) for no, (t, _) in s_by_no.items()}
        seen_no = set()
        base_conf = _group_confidence(method, gsim)
        g_nos = [str(i.get("source_item_no")) for i in g.items]
        g_contiguous = g_nos == [str(k) for k in range(1, len(g_nos) + 1)]

        for it in g.items:
            no = it.get("source_item_no")
            if no in seen_no or no not in s_by_no:
                # nomor ganda di grup Guru / nomor tidak ada di Siswa ->
                # tidak dipasangkan (lebih baik kosong daripada salah)
                continue
            seen_no.add(no)
            soal, li = s_by_no[no]
            a_tok = tokens(it.get("jawaban_text_guru") or it.get("pertanyaan_text", ""))
            own = overlap(a_tok, s_item_toks[no])
            others = [overlap(a_tok, t) for k, t in s_item_toks.items() if k != no]
            best_other = max(others) if others else 0.0
            conf = base_conf
            flags = it.setdefault("extraction_flags", [])
            if best_other >= 0.5 and best_other - own >= 0.25:
                # Soal lain di section ini JAUH lebih cocok dengan jawaban
                # ini -> kemungkinan salah pasang nomor.
                conf *= 0.5
                flags.append("soal_match_ambiguous")
            elif len(a_tok) >= 3 and own == 0.0 and method != "section_id":
                conf *= 0.8
            # Pengaman 1: soal hasil Buku Siswa sendiri harus terlihat seperti
            # soal (kriteria yang SAMA dengan deteksi missing_soal_text di
            # extractor_text.py). Ditemukan nyata: layout 2 kolom membuat
            # "soal" terbaca cuma "24 3. 54 5. 96" -- itu bukan soal.
            if not QUESTION_MARKER_RE.search(soal):
                conf *= 0.6
                flags.append("soal_text_weak")
            # Pengaman 2: jumlah soal di section Siswa jauh beda dengan jumlah
            # jawaban di grup Guru -> hasil parsing salah satu sisi patut
            # dicurigai (kecuali ID label-nya sama persis).
            n_g, n_s = len(g.items), len(s.items)
            if method != "section_id" and abs(n_g - n_s) / max(n_g, n_s) > 0.4:
                conf *= 0.7
                flags.append("soal_count_mismatch")
            # Pengaman 4: Siswa punya LEBIH SEDIKIT soal daripada jawaban Guru
            # -> ada soal yang hilang/tergabung saat parsing, jadi nomor
            # sesudahnya bisa bergeser. Terbukti nyata di review independen
            # (SMP 9 & SD 6). Berlaku untuk SEMUA metode, termasuk ID sama.
            if n_s < n_g:
                conf *= 0.6
                flags.append("soal_fewer_than_answers")
            # Penomoran berbasis urutan (font ikon SMP 9) cuma aman kalau
            # jumlahnya persis sama -- satu soal gambar yang tidak terbaca
            # sudah cukup menggeser SEMUA nomor sesudahnya.
            if s.numbering == "glyph_ordinal" and (n_s != n_g or not g_contiguous):
                # Syarat kedua (ditemukan nyata): jumlah bisa kebetulan sama
                # padahal nomor Guru bolong -- grup [1,2,3,6,7] vs 5 soal
                # Siswa membuat jawaban "3. Iya" terpasang ke soal yang salah
                # ("Dapatkah kita membuat jaring-jaring bola?").
                conf *= 0.5
                flags.append("ordinal_count_mismatch")
            # Pengaman 5: isi jawaban cuma cocok dengan EKOR soal, bukan
            # bagian awalnya -> kemungkinan soal berikutnya ikut tergabung ke
            # teks soal ini (kasus nyata: soal kain Rina + tabel suhu BPS
            # milik soal sesudahnya, lalu jawaban "urutan provinsi" tampak
            # cocok). Dicek hanya kalau soalnya cukup panjang.
            if _answer_matches_only_tail(a_tok, soal):
                conf *= 0.5
                flags.append("soal_boundary_suspect")

            # Pengaman 3 (sisi jawaban): "jawaban" Guru ternyata cuma
            # MENGULANG soal tanpa isi jawaban -- ditemukan nyata di SD 1/2,
            # karena di sana jawabannya ditandai di gambar, bukan ditulis.
            # Pasangannya benar, tapi tidak ada kunci jawaban yang bisa dipakai.
            ans_problem = _answer_restates_soal(it.get("jawaban_text_guru") or it.get("pertanyaan_text", ""), soal)
            if ans_problem:
                flags.append(ans_problem)
                it["soal_text"] = soal
                it["soal_source"] = {"file": s.source_file, "section_label": s.label,
                                     "section_line_index": s.line_index, "item_no": no,
                                     "item_line_index": li, "numbering": s.numbering}
                it["soal_match_confidence"] = round(conf, 3)
                it["soal_match_method"] = method
                if not str(it.get("status", "")).startswith("skipped"):
                    it["status"] = "needs_review_answer"
                continue

            it["soal_text"] = soal
            it["soal_source"] = {
                "file": s.source_file,
                "section_label": s.label,
                "section_line_index": s.line_index,
                "item_no": no,
                "item_line_index": li,
                "numbering": s.numbering,
            }
            it["soal_match_confidence"] = round(conf, 3)
            it["soal_match_method"] = method
            flags.append("soal_from_buku_siswa")
            st = it.get("status")
            # Soal ISIAN BANYAK TITIK-TITIK (tabel isian, "Lengkapilah
            # tabel berikut" dengan belasan "…") tidak bisa jadi SATU soal
            # pilihan ganda -- ditemukan nyata lolos sebagai draft (SD 5).
            if len(_PLACEHOLDER_RE.findall(soal)) >= 3:
                flags.append("soal_is_multi_blank_fill_in")
                it["soal_text"] = soal
                it["pertanyaan_text"] = clean_soal_text(soal)
                if st in ("draft", "needs_review_missing_soal"):
                    it["status"] = "needs_review_soal_format"
                continue
            if conf >= 0.5:
                # ATURAN SUMBER SOAL: teks pertanyaan SELALU dari Buku Siswa
                # (verbatim, cuma dirapikan spasi/pemenggalan barisnya). Buku
                # Guru hanya sumber kunci jawaban (`jawaban_text_guru`). Ini
                # berlaku juga untuk item yang teks Gurunya kebetulan sudah
                # memuat soal -- teks Guru itu campur dengan jawabannya, jadi
                # tidak boleh jadi teks soal yang dilihat siswa.
                it["pertanyaan_text"] = clean_soal_text(soal)
                if st == "needs_review_missing_soal":
                    it["status"] = "draft"
            elif st in ("needs_review_missing_soal", "draft"):
                it["status"] = "needs_review_soal_match"

    # Item yang tetap "draft" tapi TIDAK dapat soal dari Buku Siswa: teks
    # soalnya cuma ada di teks Guru (campur dengan jawaban/penyelesaian) --
    # tidak boleh lolos, karena jawabannya akan ikut terlihat di teks soal.
    for it in items:
        if it.get("status") == "draft" and not it.get("soal_text"):
            it.setdefault("extraction_flags", []).append("soal_only_in_guru_text")
            it["status"] = "needs_review_soal_source"

    summary: Dict[str, int] = {}
    for it in items:
        summary[it["status"]] = summary.get(it["status"], 0) + 1
    summary["_total"] = len(items)
    summary["_soal_from_siswa"] = sum(1 for it in items if it.get("soal_text"))
    # Diagnostik: apa saja yang terbaca dari Buku Siswa & grup Guru mana yang
    # tidak menemukan pasangan -- supaya kalau hasil sebuah buku jelek, sebab-
    # nya bisa dilihat langsung dari JSON ini tanpa perlu teks mentahnya.
    from collections import Counter

    matched = set(pairs)
    diagnostics = {
        "siswa_sections_per_jenis": dict(Counter(s.key[0] for s in sections)),
        "siswa_sections": [
            {"label": s.label[:60], "key": list(s.key), "n_soal": len(s.items), "numbering": s.numbering}
            for s in sections
        ],
        "guru_groups_tanpa_pasangan": [
            {"label": (g.label or "-")[:60], "n_jawaban": len(g.items),
             "nomor": [i.get("source_item_no") for i in g.items][:15]}
            for gi, g in enumerate(groups) if gi not in matched
        ],
    }
    return {"summary": summary, "diagnostics": diagnostics, "items": items}


def build_siswa_centric(guru_items: List[dict], sections: List[SiswaSection]):
    """Balik arah hasil `merge`: dari "per jawaban Guru" menjadi "per soal
    Buku Siswa". Pencocokan & semua pengecekannya tetap hasil `merge`."""
    by_siswa: Dict[Tuple[int, str], dict] = {}
    for it in guru_items:
        src = it.get("soal_source")
        if src and it.get("soal_text"):
            # Kunci pencarian = POSISI soal (baris) di Buku Siswa, BUKAN nomornya:
            # nomor bisa ganda dalam satu section (ditemukan nyata: judul
            # subbab "2. Barisan Geometri" ikut terbaca sebagai soal no. 2),
            # dan kalau dicari lewat nomor, satu kunci Guru terpasang ke dua soal.
            by_siswa.setdefault((src["section_line_index"], src["item_line_index"]), it)

    records: List[dict] = []
    used = set()
    for s in sections:
        for no, txt, li in s.items:
            page, bab = s.item_meta.get(li, (s.page, s.bab))
            rec = {
                "source_file": s.source_file,
                "source_page": page,
                "source_bab": bab,
                "source_section": s.label,
                "source_item_no": no,
                "pertanyaan_text": clean_soal_text(txt),
                "pertanyaan_type": "pilihan_ganda",
                "correct_answer": None,
                "options": [],
                "image_url": None,
                "image_urls": [],
                "soal_text": txt,
            }
            g = by_siswa.get((s.line_index, li))
            if g is not None and id(g) in used:
                g = None   # pengaman: satu kunci Guru hanya boleh dipakai SATU soal
            if g is None:
                rec.update({
                    "jawaban_text_guru": None,
                    "kunci_source": None,
                    "extraction_flags": ["kunci_tidak_ditemukan_di_buku_guru"],
                    "status": "needs_review_no_answer_key",
                    "extraction_confidence": 0.0,
                    "soal_match_confidence": None,
                    "soal_match_method": None,
                })
            else:
                used.add(id(g))
                flags = [f for f in g.get("extraction_flags", []) if f != "soal_from_buku_siswa"]
                rec.update({
                    "jawaban_text_guru": g.get("jawaban_text_guru"),
                    "kunci_source": {
                        "file": g.get("source_file"),
                        "page": g.get("source_page"),
                        "section": g.get("source_section"),
                        "activity": g.get("source_activity"),
                        "item_no": g.get("source_item_no"),
                    },
                    "extraction_flags": flags,
                    "status": g.get("status"),
                    "extraction_confidence": g.get("extraction_confidence"),
                    "soal_match_confidence": g.get("soal_match_confidence"),
                    "soal_match_method": g.get("soal_match_method"),
                })
                # Kalau Guru-nya sudah berisi soal (status draft sebelum
                # merge) tapi pasangannya lemah, statusnya sudah diturunkan
                # di `merge` -- dipertahankan apa adanya di sini.
            records.append(rec)
    guru_orphans = [
        {k: it.get(k) for k in ("source_file", "source_page", "source_section", "source_activity",
                                "source_item_no", "jawaban_text_guru", "status", "extraction_flags")}
        for it in guru_items if id(it) not in used
    ]
    return records, guru_orphans


def merge_files(guru_json: str, siswa_path: str, out_path: str) -> dict:
    with open(guru_json, encoding="utf-8") as f:
        stage1 = json.load(f)
    if siswa_path.lower().endswith(".pdf"):
        from app.services.pretest.extractor_siswa import extract_pdf_sections
        sections = extract_pdf_sections(siswa_path)
    else:
        with open(siswa_path, encoding="utf-8") as f:
            sections = extract_sections(f.read(), os.path.basename(siswa_path))
    result = merge(stage1, sections)
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)

    # OUTPUT BERBASIS BUKU SISWA: setiap soal latihan di Buku Siswa = satu
    # item (halaman, bab, section, nomor dari Buku Siswa). Buku Guru hanya
    # dipakai sebagai SUMBER KUNCI JAWABAN (`jawaban_text_guru`, `kunci_source`).
    # Soal Siswa yang kuncinya tidak ketemu di Buku Guru -> ditolak dengan
    # alasan "kunci tidak ditemukan". Jawaban Guru yang soalnya tidak ketemu
    # di Buku Siswa tidak dijadikan item (tidak ada soal untuk ditampilkan),
    # hanya dicatat di file _ditolak untuk audit.
    records, guru_orphans = build_siswa_centric(result["items"], sections)
    lolos = [r for r in records if r.get("status") == "draft"]
    ditolak = [r for r in records if r.get("status") != "draft"]

    summary: Dict[str, int] = {"_total_soal_buku_siswa": len(records)}
    for r in records:
        summary[r["status"]] = summary.get(r["status"], 0) + 1
    summary["_lolos"] = len(lolos)
    summary["_ditolak"] = len(ditolak)
    summary["_jawaban_guru_tanpa_soal_siswa"] = len(guru_orphans)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump({"pipeline_version": PIPELINE_VERSION, "stage1_version": stage1.get("pipeline_version", "LAMA (tanpa penanda versi)"),
                   "summary": summary, "items": lolos}, f, indent=2, ensure_ascii=False)
    rejected_path = out_path[:-5] + "_ditolak.json" if out_path.endswith(".json") else out_path + "_ditolak.json"
    with open(rejected_path, "w", encoding="utf-8") as f:
        json.dump({"pipeline_version": PIPELINE_VERSION, "summary": summary,
                   "diagnostics": result.get("diagnostics"), "items": ditolak,
                   "jawaban_guru_tanpa_soal_siswa": guru_orphans},
                  f, indent=2, ensure_ascii=False)
    return summary


def _cli():
    import argparse

    p = argparse.ArgumentParser(
        description="Tahap 1b: lengkapi teks soal dari Buku Siswa (tidak menyentuh MongoDB)."
    )
    p.add_argument("--guru-json", required=True, help="output extractor_text.py (stage1)")
    p.add_argument("--siswa", required=True, help="PDF (atau .txt) Buku Siswa buku yang sama")
    p.add_argument("--out", required=True, help="path JSON output, mis. output/kelas9_stage1b.json")
    a = p.parse_args()
    summary = merge_files(a.guru_json, a.siswa, a.out)
    print("Selesai. Ringkasan:")
    for k, v in summary.items():
        print(f"  {k}: {v}")
    print(f"\nOutput tersimpan di: {a.out}")


if __name__ == "__main__":
    _cli()
