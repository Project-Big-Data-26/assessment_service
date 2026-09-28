"""
validate.py -- pemeriksa MEKANIS hasil kerja agen (bab<NN>.json).

Agen boleh pintar, tapi tidak dipercaya begitu saja. File baru dianggap
selesai kalau lolos semua ERROR di bawah; WARNING wajib dibaca agen dan
diperbaiki kalau memang salah.

ERROR (file ditolak):
  - tidak sesuai schema (schema.py), id/nomor ganda
  - pertanyaan/stimulus TIDAK ditemukan di halaman Buku Siswa (bukan
    salinan verbatim) -- dicek di halaman sumber +-1
  - kutipan kunci TIDAK ditemukan di halaman Buku Guru yang disebut
  - 4 opsi tidak unik, atau ada dua opsi yang NILAINYA sama (2/3 vs 4/6)
  - status_kunci tidak konsisten dengan kunci_guru
  - image_refs menunjuk file yang tidak ada
WARNING:
  - halaman latihan di rentang bab yang tidak disentuh (tidak ada di
    `soal` maupun `dilewati`) -> kemungkinan soal terlewat
  - jawaban benar jauh lebih panjang dari distraktor (mudah ditebak)
  - soal di halaman [M] tapi notasi_dari_png=false

Cara pakai:
  python -m app.services.pretest.agentic.validate output/pretest/kelas5/bab01.json
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import re
import sys
from difflib import SequenceMatcher
from typing import Dict, List, Optional, Tuple

from pydantic import ValidationError

from app.services.pretest.agentic import kurikulum
from app.services.pretest.agentic.books import get_book, page_md_path
from app.services.pretest.agentic.schema import BabFile, derive_status
from app.services.pretest.llm_backend import _approx_numeric_value, _normalize_for_match

VERBATIM_MIN = 0.90          # proporsi token pertanyaan yang harus ada berurutan di halaman
VERBATIM_MIN_ADJUSTED = 0.50 # pertanyaan_disesuaikan=true
KUTIPAN_MIN = 0.85

_LATEX_RE = re.compile(r"\$\$.+?\$\$|\$[^$]+\$|\\\(.+?\\\)|\\\[.+?\\\]", re.S)
_TOKEN_RE = re.compile(r"[a-z0-9]+")
# Hanya tag HTML sungguhan & komentar. Regex umum "<[^>]+>" pernah menelan teks
# soal perbandingan ("3/4 < ... atau >") sehingga soal tanda <, >, = selalu gagal.
_HTML_TAG_RE = re.compile(r"<!--.*?-->|</?(?:br|sup|sub|u|b|i|mark|span|em|strong|p|div)\b[^>]*>", re.S | re.I)


def tokens(text: str, strip_latex: bool = False) -> List[str]:
    t = text or ""
    if strip_latex:
        t = _LATEX_RE.sub(" ", t)
    t = _HTML_TAG_RE.sub(" ", t).replace("\xad", "").lower()
    return _TOKEN_RE.findall(t)


def missing_numbers(needle: List[str], hay: List[str]) -> List[str]:
    """Angka yang tidak ada di halaman. Rasio kecocokan saja tidak cukup:
    26.932 -> 26.923 cuma mengubah 1 dari 50 token (98% cocok), padahal
    soalnya jadi salah. Jadi setiap token berangka wajib ada persis."""
    hay_set = set(hay)
    return sorted({t for t in needle if any(c.isdigit() for c in t) and t not in hay_set})


def coverage(needle: List[str], hay: List[str]) -> float:
    if not needle:
        return 1.0
    sm = SequenceMatcher(None, needle, hay, autojunk=False)
    cov = sum(b.size for b in sm.get_matching_blocks()) / len(needle)
    if cov >= VERBATIM_MIN:
        return cov
    # Cadangan tingkat huruf: konversi PDF kadang menghapus spasi/tanda hubung
    # ("KetilangdanJalanJalak", "bilanganbilangan"), sehingga token tidak cocok
    # padahal teksnya sama persis.
    # Hanya potongan >= 4 huruf yang dihitung, supaya parafrase tidak "cocok"
    # lewat huruf-huruf tunggal yang kebetulan sama di halaman panjang.
    n, h = "".join(needle), "".join(hay)
    sm = SequenceMatcher(None, n, h, autojunk=False)
    return max(cov, sum(b.size for b in sm.get_matching_blocks() if b.size >= 4) / len(n))


class Pages:
    """Cache token halaman per buku/jenis."""

    def __init__(self, book):
        self.book = book
        self._cache: Dict[Tuple[str, int], List[str]] = {}

    def toks(self, kind: str, page: int) -> List[str]:
        key = (kind, page)
        if key not in self._cache:
            path = page_md_path(self.book, kind, page)
            text = ""
            if os.path.exists(path):
                with open(path, encoding="utf-8") as f:
                    text = f.read().split("-->", 1)[-1]
            self._cache[key] = tokens(text)
        return self._cache[key]

    def around(self, kind: str, page: int, span: int = 1) -> List[str]:
        out: List[str] = []
        for p in range(page - span, page + span + 1):
            out += self.toks(kind, p)
        return out


def _load_index(book, kind: str) -> dict:
    path = os.path.join(book.md_dir(kind), "index.json")
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as f:
        return json.load(f).get("pages", {})


def validate_file(path: str) -> Tuple[Optional[BabFile], List[str], List[str]]:
    errors: List[str] = []
    warns: List[str] = []
    with open(path, encoding="utf-8") as f:
        try:
            raw = json.load(f)
        except json.JSONDecodeError as e:
            return None, [f"JSON tidak valid: {e}"], []
    try:
        data = BabFile.model_validate(raw)
    except ValidationError as e:
        for err in e.errors():
            loc = ".".join(str(x) for x in err["loc"])
            errors.append(f"schema {loc}: {err['msg']}")
        return None, errors, warns

    book = get_book(data.book)
    pages = Pages(book)
    idx = {k: _load_index(book, k) for k in ("siswa", "guru")}
    start, end = data.halaman_siswa
    kur = kurikulum.get(data.book, data.bab_no)
    if kur is None:
        errors.append(f"bab {kurikulum.bab_id(data.book, data.bab_no)} tidak ada di Prasyarat_Math.xlsx")
    kode_subbab = [k for k, _ in kur.subbab] if kur else []

    seen_id, seen_pos = set(), set()
    for s in data.soal:
        tag = s.id
        if s.id in seen_id:
            errors.append(f"{tag}: id ganda")
        seen_id.add(s.id)
        pos = (s.source_page, s.source_section, s.source_item_no)
        if pos in seen_pos:
            errors.append(f"{tag}: (halaman, section, nomor) ganda")
        seen_pos.add(pos)
        if not s.id.startswith(f"{data.book}-b{data.bab_no:02d}-p{s.source_page:04d}-"):
            errors.append(f"{tag}: id harus diawali '{data.book}-b{data.bab_no:02d}-p{s.source_page:04d}-'")
        src = s.sumber_soal          # "siswa" | "guru": buku tempat teks soal disalin
        if src == "siswa" and not (start <= s.source_page <= end):
            warns.append(f"{tag}: source_page {s.source_page} di luar rentang bab {start}-{end}")

        # --- subbab & tingkat kesulitan (untuk merakit sesi pretest) -------------
        if s.subbab is None:
            errors.append(f"{tag}: subbab wajib diisi (kode dari Prasyarat_Math.xlsx: {', '.join(kode_subbab)})")
        elif kode_subbab and s.subbab not in kode_subbab:
            errors.append(f"{tag}: subbab '{s.subbab}' tidak ada di bab ini (pilihan: {', '.join(kode_subbab)})")
        if s.tingkat_kesulitan is None:
            errors.append(f"{tag}: tingkat_kesulitan (1-5) wajib diisi")

        # --- verbatim terhadap buku sumber ---------------------------------------
        hay = pages.around(src, s.source_page)
        if not hay:
            errors.append(f"{tag}: halaman {src} p{s.source_page:04d}.md tidak ada (sudah convert?)")
        else:
            for field, text in (("pertanyaan", s.pertanyaan), ("stimulus", s.stimulus)):
                if not text:
                    continue
                # tabel/bacaan stimulus kadang 2 halaman sebelum soalnya (SD 5 Bab 8)
                hay = pages.around(src, s.source_page, span=2 if field == "stimulus" else 1)
                need = tokens(text, strip_latex=s.notasi_dari_png)
                if s.notasi_dari_png and len(need) < 3:
                    continue  # hampir seluruhnya rumus -- hanya bisa dicek manusia/PNG
                cov = coverage(need, hay)
                minimum = VERBATIM_MIN_ADJUSTED if (field == "pertanyaan" and s.pertanyaan_disesuaikan) else VERBATIM_MIN
                if cov < minimum:
                    errors.append(f"{tag}: {field} bukan salinan verbatim Buku {src.title()} hal. "
                                  f"{s.source_page}±1 (kecocokan {cov:.0%} < {minimum:.0%})")
                miss = missing_numbers(need, hay)
                if miss:
                    errors.append(f"{tag}: angka di {field} tidak ada di Buku {src.title()} hal. "
                                  f"{s.source_page}±1: {', '.join(miss)}")
        if s.pertanyaan_disesuaikan and not s.catatan_penyesuaian:
            errors.append(f"{tag}: pertanyaan_disesuaikan=true wajib mengisi catatan_penyesuaian")
        meta = idx[src].get(str(s.source_page), {})
        if meta.get("risiko_matematika") and not s.notasi_dari_png:
            warns.append(f"{tag}: hal. {s.source_page} bertanda [M] tapi notasi_dari_png=false "
                         f"-- sudah cek PNG? (abaikan kalau soal ini tanpa rumus)")

        # --- kunci Buku Guru ---------------------------------------------------
        if s.status_kunci in ("cocok", "tidak_cocok"):
            if s.kunci_guru is None:
                errors.append(f"{tag}: status_kunci={s.status_kunci} wajib mengisi kunci_guru")
            else:
                ghay = pages.around("guru", s.kunci_guru.halaman)
                gneed = tokens(s.kunci_guru.kutipan, strip_latex=True)
                cov = coverage(gneed, ghay)
                # Kutipan harus MEMUAT jawaban. Pernah terjadi: kutipan diisi teks lain
                # di halaman Guru "supaya lolos", padahal jawabannya hanya ada di PNG.
                ans_nums = set(re.findall(r"\d+", _LATEX_RE.sub(" ", s.jawaban_benar)))
                kut_nums = set(re.findall(r"\d+", s.kunci_guru.kutipan))
                # (tidak_cocok dikecualikan: di sana kutipan memang berisi angka Guru yang salah)
                if s.status_kunci == "cocok" and ans_nums and not (ans_nums & kut_nums) and not s.kunci_guru.dari_png:
                    warns.append(f"{tag}: kutipan kunci tidak memuat satu pun angka jawaban ({', '.join(sorted(ans_nums))}) "
                                 f"-- kutipan harus berisi jawabannya; kalau jawaban hanya di PNG, pakai dari_png=true")
                if not ghay:
                    errors.append(f"{tag}: halaman guru p{s.kunci_guru.halaman:04d}.md tidak ada")
                elif s.kunci_guru.dari_png:
                    pass   # jawaban hanya di gambar: tidak dicocokkan ke Markdown (soal diberi flag)
                elif not gneed:
                    # seluruh kutipan LaTeX -> tidak ada yang bisa dicocokkan mesin
                    warns.append(f"{tag}: kutipan kunci hanya berisi notasi LaTeX sehingga tidak bisa "
                                 f"diverifikasi otomatis -- pastikan cocok dengan PNG Guru hal. {s.kunci_guru.halaman}")
                elif cov < KUTIPAN_MIN or missing_numbers(gneed, ghay):
                    errors.append(f"{tag}: kutipan kunci tidak ditemukan di Buku Guru hal. "
                                  f"{s.kunci_guru.halaman}±1 (kecocokan {cov:.0%}, angka hilang: "
                                  f"{', '.join(missing_numbers(gneed, ghay)) or '-'})")
        elif s.kunci_guru is not None:
            errors.append(f"{tag}: status_kunci=tidak_ada_di_guru tapi kunci_guru diisi")

        # --- opsi --------------------------------------------------------------
        texts = [s.jawaban_benar] + [d.teks for d in s.distraktor]
        norms = [_normalize_for_match(t) for t in texts]
        if len(set(norms)) < 4:
            errors.append(f"{tag}: ada opsi yang sama persis: {texts}")
        values = [_approx_numeric_value(t) for t in texts]
        for i in range(4):
            for j in range(i + 1, 4):
                if values[i] is not None and values[j] is not None and abs(values[i] - values[j]) < 1e-9:
                    errors.append(f"{tag}: opsi '{texts[i]}' dan '{texts[j]}' bernilai sama")
        lens = [len(t) for t in texts[1:]]
        if len(s.jawaban_benar) > 20 and len(s.jawaban_benar) > 1.8 * (sum(lens) / 3):
            warns.append(f"{tag}: jawaban benar jauh lebih panjang dari distraktor (mudah ditebak)")

        for ref in s.image_refs:
            if not os.path.exists(os.path.join(book.md_dir(src), ref)):
                errors.append(f"{tag}: image_refs '{ref}' tidak ada di {book.md_dir(src)}")

    # --- cakupan subbab: pretest butuh 2 soal/subbab ----------------------------
    per_sub = soal_per_subbab(data)
    if kur and data.mode == "lengkap":
        for kode, nama in kur.subbab:
            if per_sub.get(kode, 0) < SOAL_PER_SUBBAB:
                warns.append(f"subbab {kode} '{nama}' baru {per_sub.get(kode, 0)} soal siap pakai "
                             f"(< {SOAL_PER_SUBBAB}) -- cari di Eksplorasi/Uji Kompetensi/Buku Guru")
    elif kur and data.mode == "prasyarat" and kur.subbab_terakhir:
        kode, nama = kur.subbab_terakhir
        if per_sub.get(kode, 0) < 1:
            errors.append(f"mode prasyarat: subbab terakhir {kode} '{nama}' belum punya soal")

    # --- cakupan: halaman latihan yang tidak disentuh ---------------------------
    if data.mode == "lengkap":
        touched = {s.source_page for s in data.soal if s.sumber_soal == "siswa"} | {d.source_page for d in data.dilewati}
        for p in range(start, end + 1):
            meta = idx["siswa"].get(str(p))
            if meta and meta.get("latihan") and not ({p, p + 1} & touched):
                warns.append(f"hal. {p} ({', '.join(meta['latihan'])}) tidak ada di soal/dilewati -- terlewat?")
    return data, errors, warns


SOAL_PER_SUBBAB = 2


def soal_per_subbab(data: BabFile) -> Dict[str, int]:
    """Soal yang bisa dipakai pretest per subbab (needs_image tanpa file gambar tidak dihitung)."""
    out: Dict[str, int] = {}
    for s in data.soal:
        if s.subbab and derive_status(s)[0] != "needs_image":
            out[s.subbab] = out.get(s.subbab, 0) + 1
    return out


def record_status(path: str, data: BabFile, ok: bool, n_err: int, n_warn: int) -> None:
    status_path = os.path.join(os.path.dirname(path), "_status.json")
    status = {}
    if os.path.exists(status_path):
        with open(status_path, encoding="utf-8") as f:
            status = json.load(f)
    counts: Dict[str, int] = {}
    for s in data.soal:
        st, _ = derive_status(s)
        counts[st] = counts.get(st, 0) + 1
    status[os.path.basename(path)] = {
        "bab": data.bab, "bab_no": data.bab_no, "valid": ok, "errors": n_err, "warnings": n_warn,
        "soal": len(data.soal), "dilewati": len(data.dilewati), "status": counts,
        "mode": data.mode, "per_subbab": soal_per_subbab(data),
        "validated_at": _dt.datetime.now().isoformat(timespec="seconds"),
    }
    with open(status_path, "w", encoding="utf-8") as f:
        json.dump(dict(sorted(status.items())), f, ensure_ascii=False, indent=1)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Validasi file hasil agen (bab<NN>.json).")
    ap.add_argument("files", nargs="+")
    a = ap.parse_args(argv)
    worst = 0
    for path in a.files:
        data, errors, warns = validate_file(path)
        ok = not errors
        print(f"== {path}: {'LOLOS' if ok else 'GAGAL'}  ({len(errors)} error, {len(warns)} warning)")
        for e in errors:
            print(f"  ERROR   {e}")
        for w in warns:
            print(f"  WARNING {w}")
        if data is not None:
            record_status(path, data, ok, len(errors), len(warns))
            counts: Dict[str, int] = {}
            for s in data.soal:
                st = derive_status(s)[0]
                counts[st] = counts.get(st, 0) + 1
            print(f"  soal={len(data.soal)} dilewati={len(data.dilewati)} status={counts}")
            print(f"  per subbab (siap pakai)={soal_per_subbab(data)}")
        worst = max(worst, 0 if ok else 1)
    try:
        from app.services.pretest.agentic.progress import write_progress
        write_progress()
    except Exception as e:  # progres gagal ditulis tidak boleh menutupi hasil validasi
        print(f"(PROGRESS.md tidak diperbarui: {e})")
    return worst


if __name__ == "__main__":
    sys.exit(main())
