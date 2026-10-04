"""
validate.py -- pemeriksa MEKANIS file exercise (<KODE>_<level>.json).

ERROR (file ditolak):
  - tidak sesuai schema; id ganda / tidak cocok dengan buku-bab-subbab-level-batch
  - jumlah soal != kuota level (kecuali --partial, atau kapasitas_kurang=true + alasan_kapasitas); porsi variasi di luar toleransi
  - cognitive_c / jumlah_langkah tidak cocok dengan level target
  - acuan tidak ditemukan (soal pretest tidak ada; teks/kutipan tidak ada di halaman buku)
  - variasi: angka terlalu banyak yang sama dengan acuan / konteks terlalu mirip / jawaban sama
  - satu acuan dipakai > MAKS_VARIASI_PER_ACUAN kali
  - opsi tidak unik atau ada dua opsi bernilai sama; soal merujuk gambar yang tidak ada
  - jenis_soal: satu jenis > 1/3 kuota, atau < 3 jenis berbeda (bila diisi)
  - soal kembar dengan pretest / batch lain / soal lain di file ini
WARNING: jawaban benar jauh lebih panjang dari distraktor, soal mirip (acuan beda), dsb.

  python -m app.services.exercise.validate output/exercise/kelas9/batch01/bab01/A_easy.json [--partial]
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from difflib import SequenceMatcher
from typing import List, Optional, Tuple

from pydantic import ValidationError

from app.services.exercise import config as C
from app.services.exercise.dedup import cek_kembar
from app.services.exercise.refs import (acuan_key, load_exercise, load_pretest, norm_answer,
                                        numbers, soal_text)
from app.services.exercise.schema import ExerciseFile
from app.services.pretest.agentic import kurikulum
from app.services.pretest.agentic.books import get_book
from app.services.pretest.agentic.validate import KUTIPAN_MIN, Pages, coverage, missing_numbers, tokens
from app.services.pretest.llm_backend import _approx_numeric_value

_GAMBAR_RE = re.compile(r"\b(gambar|diagram|grafik|sketsa)\s+(berikut|di\s+bawah|di\s+atas|ini|tersebut)\b|"
                        r"\bperhatikan\s+(gambar|diagram|grafik)\b|\bpada\s+(gambar|buku)\b", re.I)
_SEMUA_RE = re.compile(r"semua\s+(jawaban\s+)?(di\s+atas\s+)?(benar|salah)|tidak\s+ada\s+jawaban", re.I)


_RIBUAN_RE = re.compile(r"^-?\d{1,3}(?:\.\d{3})+(?:,\d+)?$")
_DESIMAL_KOMA_RE = re.compile(r"^-?\d+,\d+$")


def _nilai(text: str) -> Optional[float]:
    """Nilai numerik opsi dengan format Indonesia: 80.000 = delapan puluh ribu (bukan 80,0), 3,5 = tiga setengah.
    _approx_numeric_value milik pretest membaca titik sebagai desimal, jadi dipakai hanya untuk selain itu."""
    t = re.sub(r"[\s$]+", "", (text or "").lower())
    t = re.sub(r"^rp\.?", "", t).rstrip(".")
    if _RIBUAN_RE.match(t):
        return float(t.replace(".", "").replace(",", "."))
    if _DESIMAL_KOMA_RE.match(t):
        return float(t.replace(",", "."))
    if re.match(r"^-?\d+\.\d{1,2}$", t):      # 12.5 (titik desimal gaya internasional, 1-2 digit)
        return float(t)
    if re.match(r"^-?\d+$", t):
        return float(t)
    return _approx_numeric_value(text)


def _opsi_unik(s, errors: List[str], warns: List[str]) -> None:
    texts = [s.jawaban_benar] + [d.teks for d in s.distraktor]
    norm = [norm_answer(t) for t in texts]
    if len(set(norm)) != 4:
        errors.append(f"{s.id}: 4 opsi tidak unik")
    vals = [_nilai(t) for t in texts]
    known = [v for v in vals if v is not None]
    if len(known) >= 2 and len({round(v, 9) for v in known}) != len(known):
        errors.append(f"{s.id}: dua opsi bernilai sama secara numerik")
    if any(_SEMUA_RE.search(t) for t in texts):
        errors.append(f"{s.id}: opsi 'semua benar/salah/tidak ada jawaban' dilarang")
    dl = [len(d.teks) for d in s.distraktor]
    if len(s.jawaban_benar) > 40 and len(s.jawaban_benar) > 2 * (sum(dl) / 3):
        warns.append(f"{s.id}: jawaban benar jauh lebih panjang dari distraktor (mudah ditebak)")


def _cek_acuan(s, pages: Pages, pretest: dict, errors: List[str]) -> Tuple[str, str]:
    """Verifikasi acuan; return (teks_acuan, jawaban_acuan) untuk cek variasi."""
    a = s.acuan
    if a.sumber == "pretest":
        ref = pretest.get(a.id or "")
        if not ref:
            errors.append(f"{s.id}: acuan pretest '{a.id}' tidak ada di output/pretest")
            return "", ""
        return ref.teks, ref.jawaban
    needle_src = a.teks if s.tipe_generate == "variasi" else a.kutipan
    kind = "siswa" if a.sumber == "siswa" else "guru"
    hay = pages.around(kind, a.halaman)
    nt = tokens(needle_src or "")
    cov = coverage(nt, hay)
    miss = missing_numbers(nt, hay)
    if not hay:
        errors.append(f"{s.id}: halaman acuan {kind} p{a.halaman} tidak ada")
    elif cov < KUTIPAN_MIN or miss:
        label = "teks" if s.tipe_generate == "variasi" else "kutipan"
        extra = f", angka hilang: {','.join(miss)}" if miss else ""
        errors.append(f"{s.id}: {label} acuan tidak ditemukan di {kind} hal.{a.halaman} ±1 (cocok {cov:.0%}{extra})")
    return (a.teks or ""), (a.jawaban or "")


def _cek_variasi(s, teks_acuan: str, jawab_acuan: str, errors: List[str]) -> None:
    if not teks_acuan:
        return
    baru = numbers(soal_text(s.stimulus, s.pertanyaan))
    lama = numbers(teks_acuan)
    if norm_answer(s.jawaban_benar) == norm_answer(jawab_acuan):
        errors.append(f"{s.id}: jawaban variasi SAMA dengan jawaban acuan ('{s.jawaban_benar}')")
    if s.variasi_cara == "angka":
        if not lama:
            errors.append(f"{s.id}: acuan tanpa angka, pakai variasi_cara='konteks'")
        elif baru:
            sama = len(set(baru) & set(lama)) / len(set(baru))
            if sama > C.VARIASI_ANGKA_MAKS_SAMA:
                errors.append(f"{s.id}: {sama:.0%} angka soal sama dengan acuan (maks {C.VARIASI_ANGKA_MAKS_SAMA:.0%})")
    else:
        mirip = SequenceMatcher(None, tokens(soal_text(s.stimulus, s.pertanyaan)), tokens(teks_acuan),
                                autojunk=False).ratio()
        if mirip > C.VARIASI_KONTEKS_MAKS_MIRIP:
            errors.append(f"{s.id}: konteks terlalu mirip dengan acuan ({mirip:.2f} > {C.VARIASI_KONTEKS_MAKS_MIRIP})")


def validate_file(path: str, partial: bool = False):
    errors: List[str] = []
    warns: List[str] = []
    try:
        with open(path, encoding="utf-8") as f:
            data = ExerciseFile.model_validate(json.load(f))
    except (OSError, ValueError, ValidationError) as e:
        return None, [f"schema/JSON: {e}"], []

    bab = kurikulum.get(data.book, data.bab_no)
    if not bab:
        return data, [f"bab {data.book} no.{data.bab_no} tidak ada di kurikulum"], []
    if bab.subbab_nama(data.subbab) is None:
        return data, [f"subbab {data.subbab} tidak ada di {bab.bab_id}: {[k for k, _ in bab.subbab]}"], []

    book = get_book(data.book)
    kuota = C.KUOTA_PER_LEVEL[book.jenjang]
    spec = C.LEVEL_SPEC[data.level]
    prefix = f"{data.book}-b{data.bab_no:02d}-{data.subbab.lower()}-{data.level}-bt{data.batch:02d}-"

    ids = [s.id for s in data.soal]
    if len(set(ids)) != len(ids):
        errors.append("id soal ganda")
    n = len(data.soal)
    if data.kapasitas_kurang:
        if not data.alasan_kapasitas:
            errors.append("kapasitas_kurang=true wajib disertai alasan_kapasitas")
        if n >= kuota:
            errors.append(f"kapasitas_kurang=true padahal jumlah soal {n} sudah memenuhi kuota {kuota}")
        elif n == 0:
            errors.append("kapasitas_kurang=true tetapi tidak ada soal")
    elif data.alasan_kapasitas:
        errors.append("alasan_kapasitas diisi tetapi kapasitas_kurang tidak true")
    if n > kuota or (n != kuota and not partial and not data.kapasitas_kurang):
        errors.append(f"jumlah soal {n} != kuota {kuota} ({book.jenjang}, level {data.level})")
    n_var = sum(1 for s in data.soal if s.tipe_generate == "variasi")
    target_var = round(C.PORSI_VARIASI[data.level] * kuota)
    # Batas bawah variasi tidak berlaku di hard: acuan layak habis dipakai easy/medium, dan memaksa label
    # "variasi" membuat soal orisinal yang bagus diubah hanya demi lolos validator.
    batas_bawah = 0 if data.level == "hard" else target_var - C.TOLERANSI_PORSI
    if not partial and not (batas_bawah <= n_var <= target_var + C.TOLERANSI_PORSI):
        errors.append(f"variasi {n_var} soal, target {target_var} ±{C.TOLERANSI_PORSI} dari {kuota}"
                      f"{' (hard: tanpa batas bawah)' if data.level == 'hard' else ''}")

    pages = Pages(book)
    pretest = load_pretest(data.book)
    pakai: dict = {}
    for s in data.soal:
        if not s.id.startswith(prefix):
            errors.append(f"{s.id}: id harus diawali '{prefix}'")
        if s.cognitive_c not in spec["c"]:
            errors.append(f"{s.id}: {s.cognitive_c} bukan level {data.level} (harus {'/'.join(spec['c'])})")
        lo, hi = spec["langkah"]
        if not lo <= s.jumlah_langkah <= hi:
            errors.append(f"{s.id}: jumlah_langkah {s.jumlah_langkah} di luar {lo}-{hi} untuk {data.level}")
        if _GAMBAR_RE.search(soal_text(s.stimulus, s.pertanyaan)):
            errors.append(f"{s.id}: soal merujuk gambar/buku, padahal gambar belum didukung -- tulis datanya di stimulus")
        _opsi_unik(s, errors, warns)
        teks_a, jaw_a = _cek_acuan(s, pages, pretest, errors)
        if s.tipe_generate == "variasi":
            _cek_variasi(s, teks_a, jaw_a, errors)
            k = acuan_key(s.acuan.model_dump())
            pakai[k] = pakai.get(k, 0) + 1
    for k, v in pakai.items():
        if v > C.MAKS_VARIASI_PER_ACUAN:
            errors.append(f"acuan {k} dipakai {v}x (maks {C.MAKS_VARIASI_PER_ACUAN})")

    jenis = [s.jenis_soal.strip().lower() for s in data.soal if s.jenis_soal]
    if jenis:   # file lama (easy pertama) belum punya jenis_soal -> lewati
        if len(jenis) != len(data.soal):
            errors.append("jenis_soal harus diisi di SEMUA soal (atau tidak sama sekali)")
        batas = max(1, math.ceil(kuota * C.MAKS_JENIS_PER_LEVEL))
        for j in sorted(set(jenis)):
            if jenis.count(j) > batas:
                errors.append(f"jenis_soal '{j}' muncul {jenis.count(j)}x (maks {batas} dari {kuota}); variasikan jenis soal")
        if len(set(jenis)) < 3 and len(data.soal) >= 6:
            errors.append(f"hanya {len(set(jenis))} jenis_soal berbeda; minimal 3")

    pool = [r for r in pretest.values() if r.bab_no == data.bab_no and r.subbab == data.subbab]
    pool += load_exercise(data.book, data.bab_no, data.subbab, exclude=path)
    e2, w2 = cek_kembar(data.soal, pool)
    return data, errors + e2, warns + w2


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--partial", action="store_true", help="file belum lengkap: jangan error karena jumlah/porsi")
    a = ap.parse_args(argv)
    data, errors, warns = validate_file(a.file, a.partial)
    for e in errors:
        print("ERROR  ", e)
    for w in warns:
        print("WARNING", w)
    n = len(data.soal) if data else 0
    print(f"{'LOLOS' if not errors else 'GAGAL'}: {n} soal, {len(errors)} error, {len(warns)} warning")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
