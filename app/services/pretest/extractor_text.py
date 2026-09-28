"""
extractor_text.py -- Text extractor untuk SOAL pretest dari Buku
Panduan Guru (sumber SIBI).

PEMBAGIAN TIM (3 tugas milik sendiri + 2 tugas tim lain):
  1. extractor_text.py    (modul ini) -- ekstraksi teks mentah soal+jawaban
  2. extractor_image.py   -- ekstraksi & asosiasi gambar
  3. answer_option_generator.py -- pisahkan jawaban bersih dari blok mentah
     modul ini + generate 3 opsi salah (distractor) jadi 4 pilihan MCQ
  (tim lain) cognitive classifier -- klasifikasi C1-C6 / easy-medium-hard
  (tim lain) loader/penghubung   -- insert hasil akhir ke MongoDB

Modul ini TIDAK menyentuh MongoDB sama sekali dan TIDAK men-generate opsi
jawaban -- outputnya adalah data terstruktur (lewat `export_to_json`) yang
jadi kontrak antar tahap di atas.

SCOPE (sesuai kesepakatan):
- Modul ini HANYA melakukan ekstraksi teks murni dari PDF yang sudah
  diubah jadi teks (per halaman). Modul ini TIDAK men-generate soal baru
  dan TIDAK men-generate opsi jawaban (MCQ) -- itu tanggung jawab
  `answer_option_generator.py` yang berjalan setelah tahap ini.
- Hanya bagian "Jawaban Latihan" / "Kunci Jawaban Latihan" /
  "Jawaban Uji Kompetensi" / "Kunci Jawaban Uji Kompetensi" yang jadi target
  utama. Bagian "Eksplorasi"/"Kunci Jawaban Eksplorasi" tetap discan (karena
  strukturnya sama), tapi secara alami akan banyak ter-skip oleh filter
  open-ended karena isinya sering "jawaban bervariasi" / aktivitas kelompok.

KRITERIA "TIDAK MENGAMBANG" (soal layak diambil) -- hasil diskusi sebelumnya:
  1. Teks soal + jawaban ada secara utuh dalam blok ini (bukan cuma nomor
     tanpa konteks).
  2. Jawaban bersifat tertutup/definitif (bukan "jawaban bervariasi", dst).
  3. Bukan soal pembuktian murni (kata kunci "buktikan") -- levelnya
     tinggi (C5) tapi jawabannya berupa proses, bukan nilai akhir, sehingga
     sulit dikonversi ke pilihan ganda secara aman.
  4. Kalau menyebut gambar/diagram/grafik, TETAP diambil tapi ditandai
     `needs_image` -- akan dilengkapi oleh image_extractor.py secara
     terpisah, bukan di-skip total.

CATATAN JUJUR SOAL KUALITAS DATA:
  Teks hasil konversi PDF -> txt untuk buku ini sering "rusak" pada bagian
  notasi matematika (pecahan, simbol >=, <=, sudut, dsb ter-flatten jadi
  karakter acak / baris pendek berisi simbol tunggal). Modul ini TIDAK
  mencoba menebak/memperbaiki notasi itu -- sebagai gantinya, blok yang
  polanya mencurigakan (banyak baris pendek berisi simbol) diberi
  extraction_confidence RENDAH dan flag `possible_formula_garbling`, supaya
  tidak diam-diam dianggap bersih. Pembersihan lebih lanjut / interpretasi
  makna matematisnya didelegasikan ke tahap berikutnya (LLM-assisted parse
  atau review), BUKAN dipaksakan lolos di sini.
"""

from __future__ import annotations

# Penanda versi pipeline -- ditulis ke setiap file output (summary) supaya
# dari JSON-nya saja bisa dipastikan versi kode mana yang dipakai.
PIPELINE_VERSION = "2026-09-26i"

import re
from dataclasses import dataclass, field
from typing import List, Optional, Tuple


# ---------------------------------------------------------------------------
# Regex pattern -- hasil observasi langsung terhadap struktur nyata PDF
# Buku Panduan Guru Matematika Kelas XI (SIBI)
# ---------------------------------------------------------------------------

BAB_HEADING_RE = re.compile(r"^Bab\s+(\d+)\s+([A-Za-z].{2,60})$")
# Diperluas dari A-F ke A-Z: sebagian buku (SD, SMA Kelas 12) punya subbab
# berlabel sampai G/H, dst. Perhatikan: kalau labelnya "Kunci Jawaban" (mis.
# "H.        Kunci Jawaban"), itu harus ditangkap DULU oleh
# LETTERED_KUNCI_JAWABAN_RE di bawah -- bukan diperlakukan sebagai subbab
# biasa -- makanya urutan pengecekan di extract_candidate_blocks penting.
SUBBAB_HEADING_RE = re.compile(r"^([A-Z])\.\s+([A-Za-z].{2,80})$")

# Contoh yang harus match: "Jawaban Latihan 1.4", "Kunci Jawaban Latihan 1.1",
# "Jawaban Uji Kompetensi", "Kunci Jawaban Eksplorasi 3.3 (No. 1-5)",
# "Kunci Jawaban Uji Kompetensi Bab 1" (varian SMA Kelas 12, ada "Bab N"
# tambahan sebelum nomornya), "Kunci Jawaban Latihan A Persamaan Linear Dua
# Variabel" (varian SMP Kelas 9 -- bukan nomor "X.X" tapi label huruf + judul
# subbab, ditangkap lewat alternatif suffix kedua di bawah).
ANSWER_SECTION_RE = re.compile(
    r"^(Kunci\s+)?[Jj]awaban\s+(Latihan|Uji\s+Kompetensi|Eksplorasi|Proyek)"
    r"(\s+(Bab\s+)?\d+(\.\d+)?|\s+[A-Z](\s*[—\-–]\s*|\s+)[A-Za-z].{0,80}|\s+[A-Z])?"
    r"(\s*\(No\.[^)]*\))?\s*$"
)

# Heading section jawaban berlabel huruf, mis. "H.        Kunci Jawaban"
# (SMA Kelas 12) -- whitespace-nya sering tidak rata karena artefak PDF,
# makanya pakai \s+ (bukan spasi tunggal). Dicek SEBELUM SUBBAB_HEADING_RE
# supaya baris ini memicu in_answer_section=True, bukan dianggap subbab biasa.
# Suffix opsional ditambahkan untuk varian SMP Kelas 9: "E. Kunci Jawaban Uji
# Kompetensi", "F. Kunci Jawaban Proyek" -- label huruf yang sama tapi diikuti
# jenis section, bukan cuma "Kunci Jawaban" polos.
LETTERED_KUNCI_JAWABAN_RE = re.compile(
    r"^[A-Z]\.\s+Kunci\s+Jawaban(\s+(Uji\s+Kompetensi|Proyek|Latihan))?\s*$"
)

# "Kunci Jawaban" berdiri sendiri tanpa angka/label -- pola dominan di buku
# SD Kelas 1 (dan juga muncul di SMA Kelas 12 menjelang akhir bab).
PLAIN_KUNCI_JAWABAN_RE = re.compile(r"^Kunci\s+Jawaban\s*$")

# Pola SMP Kelas 8: "Alternatif Jawaban Soal Latihan" -- termasuk varian
# dengan typo asli dari buku ("Alternaif" tanpa 't', "Laihan" tanpa 't').
# Suffix nomor opsional ("1.1", dst) ditambahkan setelah ditemukan nyata data
# aslinya berbentuk "Jawaban Soal Laihan 1.1" (bukan berdiri sendiri tanpa
# nomor seperti dugaan awal) -- tanpa ini, SELURUH buku Kelas 8 gagal
# terdeteksi sama sekali (in_answer_section tidak pernah menyala).
# "Tambahan" dan "Pengayaan" ditambahkan setelah ditemukan nyata di SD Kelas
# 5: "Kunci Jawaban Soal Tambahan", "Kunci Jawaban Soal Pengayaan" -- section
# jawaban ekstra yang formatnya mirip tapi kata terakhirnya beda.
JAWABAN_SOAL_LATIHAN_RE = re.compile(
    r"^(Alterna\w*f\s+)?[Jj]awaban\s+[Ss]oal\s+(La\w*han|Tambahan|Pengayaan)"
    r"(\s+\d+(\.\d+)?)?\s*$"
)

# Pola SMA Kelas 11 Peminatan: di dalam satu section "H. Kunci Jawaban" per
# bab, jawabannya dikelompokkan per subbab dengan label "N. Latihan <Huruf>
# <Judul>" (mis. "1. Latihan A Jenis-Jenis Matriks", "2. Latihan B Kesamaan
# Dua Matriks"). Baris ini BUKAN soal -- bentuknya cuma kebetulan cocok
# dengan ITEM_START_RE ("angka. isi") -- melainkan label pengelompokan,
# dan penomoran jawaban ASLI (1, 2, 3, ...) baru dimulai lagi persis
# setelahnya. Kalau tidak difilter, label ini malah tertangkap sebagai
# "soal" nomor 1 palsu (isinya cuma judul subbab), lalu jawaban asli nomor 1
# yang menyusul menimpanya lewat flush -- baris judul palsu itu sendiri
# tetap sempat ter-emit sebagai blok terpisah kalau ada teks lain di
# antaranya (mis. baris "Alternatif Penyelesaian" ikut kebawa).
LATIHAN_SUBGROUP_LABEL_RE = re.compile(r"^\d{1,2}\.\s+Latihan\s+[A-Z]\b.*$")

# Pisah grup kalau penomoran mundur/ulang tanpa heading baru (lihat
# extract_candidate_blocks). Bisa dimatikan untuk perbandingan A/B.
SPLIT_GROUP_ON_NUMBER_RESTART = True

# Heading struktur narasi Buku Guru yang bentuknya kebetulan "N. ..." --
# "2. Subbab B Refleksi (Pencerminan)" (SMP 9). Menandakan kunci jawaban
# sebelumnya SUDAH selesai dan narasi subbab berikutnya dimulai.
GURU_SUBBAB_HEADING_RE = re.compile(r"^\d{1,2}\.\s+Subbab\s+[A-Z]\b.*$")

# --- Label aktivitas (jembatan ke Buku Siswa) --------------------------------
# Di dalam section "Kunci Jawaban", Buku Guru sering mengelompokkan jawaban
# per NAMA AKTIVITAS yang sama persis dengan di Buku Siswa ("Ayo Berlatih",
# "Ayo Berpikir Kritis", "Evaluasi", "Latihan 1.1", "Latihan Soal Lingkaran",
# dst). Label ini dicatat (field `source_activity` / `activity_key`) supaya
# tahap penggabung (soal_merger.py) bisa mencari soal aslinya di Buku Siswa.
# Tanpa ini, nomor jawaban dari aktivitas yang berbeda tercampur (penomoran
# mulai ulang dari 1 di tiap aktivitas), dan baris label itu sendiri malah
# ikut tertempel ke teks jawaban nomor sebelumnya.
ACTIVITY_LABEL_RE = re.compile(
    r"^(Ayo,?\s+[A-Z][a-z]+(\s+[A-Z][a-z]+)?|Evaluasi|Asesmen|"
    r"Uji\s+Kompetensi(\s+Bab\s+\d+)?|Uji\s+Pemahaman|"
    r"(Soal\s+)?La\w*han\s+\d+(\.\d+)?|Latihan\s+[A-Z](\s*[—\-–]\s*|\s+)\S.*|"
    r"Latihan\s+Soal\s+\S.*|Soal\s+(Tambahan|Pengayaan))\s*\??\s*$"
)


def normalize_activity_key(label: Optional[str]) -> Optional[Tuple[str, Optional[str]]]:
    """
    Ubah label aktivitas/section (dari Buku Guru ATAU Buku Siswa) jadi kunci
    pembanding yang seragam: (jenis, id_opsional).

    Contoh:
      "Kunci Jawaban Latihan 1.1"            -> ("latihan", "1.1")
      "Jawaban Soal Laihan 2.3"              -> ("latihan", "2.3")
      "Soal Laihan 2.3"   (Buku Siswa)       -> ("latihan", "2.3")
      "Kunci Jawaban Latihan A Persamaan..." -> ("latihan", "A")
      "1. Latihan B Kesamaan Dua Matriks"    -> ("latihan", "B")
      "Latihan Soal Lingkaran"               -> ("latihan_soal", "lingkaran")
      "A. Kunci Jawaban Uji Kompetensi"      -> ("uji_kompetensi", None)
      "Uji Kompetensi Bab 3"                 -> ("uji_kompetensi", None)
      "Ayo Berlatih"                         -> ("ayo berlatih", None)
      "ASESMEN (KUNCI JAWABAN)"              -> ("asesmen", None)
      "H. Kunci Jawaban"                     -> None  (belum tahu aktivitasnya)
    Fungsi ini dipakai BERSAMA oleh extractor_text.py dan extractor_siswa.py
    supaya kedua sisi pasti memakai aturan normalisasi yang sama.
    """
    if not label:
        return None
    s = label.strip()
    s = re.sub(r"^\d{1,2}\.\s+", "", s)            # "1. Latihan A ..."
    s = re.sub(r"^[A-Z]\.\s+", "", s)              # "A. Kunci Jawaban ..."
    s = re.sub(r"\s*\??\s*$", "", s)
    low = s.lower()
    if re.match(r"^asesmen\b", low):
        return ("asesmen", None)
    low = re.sub(r"^(alterna\w*f\s+)?(kunci\s+)?jawaban\s*", "", low).strip()
    if not low:
        return None
    m = re.match(r"^(soal\s+)?la\w*han\s+(\d+(\.\d+)?)$", low)
    if m:
        return ("latihan", m.group(2))
    m = re.match(r"^latihan\s+soal\s+(.+)$", low)
    if m:
        return ("latihan_soal", m.group(1).strip())
    m = re.match(r"^latihan\s+([a-z])(\s*[—\-–]\s*|\s+|$)", low)
    if m:
        return ("latihan", m.group(1).upper())
    if re.match(r"^uji\s+kompetensi\b", low):
        return ("uji_kompetensi", None)
    if re.match(r"^uji\s+pemahaman\b", low):
        # SMP 9: "Uji Pemahaman" adalah sub-bagian DI DALAM Uji Kompetensi
        # (Siswa: "Uji Kompetensi" lalu langsung "Uji Pemahaman") -- disamakan
        # supaya kedua buku memakai kunci yang sama.
        return ("uji_kompetensi", None)
    m = re.match(r"^soal\s+(tambahan|pengayaan)\b", low)
    if m:
        return (f"soal_{m.group(1)}", None)
    m = re.match(r"^eksplorasi\s+(\d+(\.\d+)?)", low)
    if m:
        return ("eksplorasi", m.group(1))
    if re.match(r"^evaluasi$", low):
        return ("evaluasi", None)
    m = re.match(r"^ayo,?\s+([a-z]+(\s+[a-z]+)?)$", low)
    if m:
        return ("ayo " + m.group(1), None)   # "Ayo, Mengingat Kembali" == "Ayo Mengingat Kembali"
    return None

# Pola SD Kelas 3: "ASESMEN (KUNCI JAWABAN)" -- section per-bab, semua huruf
# besar, muncul persis 1x per bab (5x di buku ini, cocok dengan 5 Bab).
ASESMEN_KUNCI_JAWABAN_RE = re.compile(
    r"^ASESMEN\s*\(\s*KUNCI\s+JAWABAN\s*\)\s*$", re.IGNORECASE
)

# Heading lain yang menandakan section jawaban SUDAH SELESAI. Kata-kata ini
# adalah judul subbagian TEMPLATE BAKU yang berulang di akhir tiap bab buku
# panduan guru (bukan soal), jadi disatukan di satu daftar supaya dipakai
# ulang baik dalam bentuk TANPA nomor (OTHER_SECTION_RE, mis. "Pengayaan")
# maupun DENGAN nomor (NUMBERED_OTHER_SECTION_RE di bawah, mis.
# "4. Penilaian") -- varian bernomor ini ditemukan nyata di testing manual:
# ITEM_START_RE salah menangkapnya seolah-olah soal nomor 4, padahal isinya
# cuma judul subbagian tanpa konten soal apa pun (dilaporkan user: "4.
# Penilaian" muncul sebagai draft kosong/tidak jelas).
#
# "Rubrik Penilaian" ditambahkan terpisah dari "Penilaian" (bukan cuma opsional
# prefix "Rubrik ") karena ditemukan nyata di data SD Kelas III: pola
# "10.\nRubrik Penilaian" -- nomor bareng "10." sendirian di barisnya (varian
# BARE_ITEM_NO_RE), lalu baris berikutnya persis "Rubrik Penilaian" jadi
# "isi"-nya. Kalau tidak ditangani, ini juga membiarkan section jawaban tetap
# "terbuka" sehingga SELURUH ISI TABEL rubrik penilaian di baliknya (baris
# tabel skor seperti "3. Kalimat", "4. Kerapian") ikut bocor tertangkap
# sebagai draft soal palsu.
# "Interaksi dengan Orang Tua" dibuat fleksibel (Guru opsional, Wali opsional)
# karena ditemukan varian judul asli "Interaksi Guru dengan Orang Tua/Wali"
# di buku SD Kelas II.
_BOILERPLATE_SECTION_WORDS = (
    r"Eksplorasi\s+[\d.]+|Rangkuman|Refleksi|Pengayaan|"
    r"Peta Konsep|Gambaran Umum Bab|Skema Pembelajaran|"
    r"Panduan Pembelajaran|Metode\s*&?\s*Aktivitas Pembelajaran|"
    r"Diferensiasi|Apersepsi|Sarana\s*&\s*Prasarana Pembelajaran|"
    r"Pengalaman Belajar|Rubrik Penilaian(\s+[A-Z][a-z]+)*|Penilaian|"
    r"Interaksi\s+(Guru\s+)?dengan Orang\s*Tua(\s*/\s*Wali)?|"
    r"Sumber Bacaan|Uji Kompetensi|Glosarium|Daftar Pustaka"
)
OTHER_SECTION_RE = re.compile(rf"^({_BOILERPLATE_SECTION_WORDS})\s*$")

# Varian bernomor dari heading di atas, mis. "4. Penilaian",
# "6. Interaksi dengan Orang Tua", "7. Sumber Bacaan" -- ini heading
# subbagian, BUKAN soal, walaupun bentuknya kebetulan cocok dengan
# ITEM_START_RE ("angka. isi"). Dicek terpisah (bukan digabung ke
# OTHER_SECTION_RE) karena butuh prefix "N. " di depannya.
NUMBERED_OTHER_SECTION_RE = re.compile(
    rf"^\d{{1,2}}\.\s+({_BOILERPLATE_SECTION_WORDS})\s*$"
)

# Footer/header berulang di tiap halaman -- dipakai untuk tracking source_page
# DAN untuk tracking bab berjalan (heading bab asli di body sering terpecah
# jadi beberapa baris dekoratif oleh layout PDF, sehingga footer "Bab N | Judul"
# yang berulang tiap halaman justru sumber paling andal untuk tahu sedang di
# bab mana).
PAGE_FOOTER_LEFT_RE = re.compile(
    r"^(\d{1,3})\s+Buku Panduan Guru Matematika untuk SMA/SMK Kelas XI\s*$"
)
# Nomor halaman di ujung footer OPSIONAL: di hasil PyMuPDF (komputer user,
# SD 2/3/5/6) footer terpecah jadi 2 baris -- "Bab 1 | Bilangan Cacah sampai
# 1.000" lalu "61" -- sehingga versi lama (nomor wajib) tidak pernah cocok,
# source_bab kosong semua, dan footer ikut bocor ke teks jawaban.
# Prefix "Panduan Khusus " opsional: footer SMA 12 TL berbentuk "Panduan
# Khusus Bab 1 | Lingkaran, Elips, dan Garis Singgung Lingkaran".
PAGE_FOOTER_RIGHT_RE = re.compile(r"^(?:Panduan\s+Khusus\s+)?Bab\s+(\d+)\s*\|\s*(.+?)(\s+(\d{1,3}))?\s*$")

# Item bernomor level atas, misal "8. Perhatikan f(x)=..." -- BUKAN sub-poin
# "a)" / "b)" yang ada di dalam satu nomor.
ITEM_START_RE = re.compile(r"^(\d{1,2})\.\s+(\S.*)$")

# Varian SMA Kelas 12: layout PDF-nya memecah nomor item ke barisnya sendiri
# ("1." sendirian, isi soalnya baru muncul di baris berikutnya), beda dari
# buku lain yang nomor+isi ada di baris yang sama (ITEM_START_RE di atas).
# Dicek TERPISAH (bukan digabung ke ITEM_START_RE) supaya tidak menangkap
# baris subbagian seperti "1.1"/"1.2" (label Latihan) yang punya digit
# tambahan setelah titik -- di sini setelah titik cuma boleh whitespace lalu
# akhir baris.
BARE_ITEM_NO_RE = re.compile(r"^(\d{1,2})\.\s*$")

# --- Filter kriteria (Tahap 1, ekstraksi teks murni) ------------------------

OPEN_ENDED_PATTERNS = [
    r"jawaban (bisa|dapat)?\s*bervariasi",
    r"jawaban masing[- ]masing siswa",
    r"kebijakan guru",
    r"sesuai kreativitas siswa",
    r"pendapat (bisa|dapat) disampaikan secara bervariasi",
    r"jawaban (siswa )?berbeda[- ]beda",
    r"disesuaikan dengan jawaban siswa",
    # Ditemukan nyata lolos (SMP 7 "Jawaban peserta didik bisa beragam",
    # SMP 9 "Jawaban akan bervariasi tergantung ...") -- pola di atas cuma
    # kenal "jawaban (bisa|dapat) bervariasi".
    r"jawaban (peserta didik |siswa )?(bisa |dapat |akan )?(beragam|bervariasi)",
    # SD 5 "Lengkapilah tabel": "(...) bebas sesuai dengan bilangan yang
    # diambil peserta didik" -- jawabannya dipilih siswa sendiri.
    r"\bbebas sesuai\b|sesuai dengan \w+ yang (diambil|dipilih|dibuat) (oleh )?(peserta didik|siswa)",
]
OPEN_ENDED_RE = re.compile("|".join(OPEN_ENDED_PATTERNS), re.IGNORECASE)

PEMBUKTIAN_RE = re.compile(r"\bbuktikan\b|\bpembuktian\b", re.IGNORECASE)

NEEDS_IMAGE_PATTERNS = [
    r"perhatikan gambar",
    # Sengaja TANPA \b di kiri "gambar" -- kata kerja berimbuhan Indonesia
    # ("menggambar", "digambar", "tergambar", "penggambaran") nempel
    # langsung ke akar katanya tanpa spasi, jadi \bgambar\b (batas kata di
    # kedua sisi) gagal menangkap "Menggambar sudut...", ditemukan nyata
    # bikin soal begitu lolos jadi "draft" padahal seharusnya "needs_image".
    r"gambar(kan)?\b", r"\bdiagram\b", r"\bgrafik\b",
    r"sketsa(kan)?", r"lihat (grafik|gambar)", r"pada (lingkaran|segitiga|"
    r"gambar) berikut",
]
NEEDS_IMAGE_RE = re.compile("|".join(NEEDS_IMAGE_PATTERNS), re.IGNORECASE)

# Deteksi mekanis apakah blok ini benar-benar memuat TEKS SOAL, bukan cuma
# jawaban murni. Ditemukan nyata di buku SMP Kelas 9 (dan kemungkinan buku
# Kurikulum Merdeka lain): section "Kunci Jawaban Latihan ..." di Buku
# Panduan Guru TIDAK mengulang soal aslinya sama sekali -- soal aslinya
# HANYA ada di Buku Siswa (tidak kita punya), dan yang dicetak di Panduan
# Guru cuma jawaban langsung bernomor (mis. "1. Persamaan-persamaan yang
# merupakan persamaan linear dua variabel adalah persamaan b, c, dan e.").
# Tanpa pengecekan ini, blok semacam itu lolos sebagai "draft" seolah-olah
# lengkap soal+jawaban -- padahal itu MELANGGAR kriteria "tidak mengambang"
# #1 di docstring modul ini (soal harus ada utuh, bukan cuma nomor+jawaban).
#
# Heuristik: soal biasanya mengandung tanda tanya ATAU kata kerja
# instruksi/pertanyaan matematika yang umum. Kalau TIDAK ADA satu pun
# penanda ini di blok, kemungkinan besar itu jawaban murni tanpa soal.
# Ini heuristik, BUKAN jaminan sempurna -- makanya hasilnya berupa flag +
# status baru untuk direview manual, bukan langsung dibuang permanen.
QUESTION_MARKER_PATTERNS = [
    r"\?",
    # Kata kerja imperatif spesifik yang umum di soal matematika Indonesia.
    r"\btentukan(lah)?\b", r"\bhitung(lah)?\b", r"\bcari(lah)?\b",
    r"\bjelaskan\b", r"\bbuktikan\b", r"\bsederhanakan(lah)?\b",
    r"\bgambar(lah|kan)?\b", r"\blengkapi(lah)?\b", r"\bselesaikan\b",
    r"\btuliskan\b", r"\bnyatakan\b", r"\bperiksa(lah)?\b",
    r"\bmanakah\b", r"\bsebutkan\b", r"\bbandingkan\b", r"\burutkan\b",
    r"\bberapa(kah)?\b", r"\bapakah\b", r"\bdiketahui\b", r"\bperhatikan\b",
    r"\bisilah\b", r"\bkerjakan(lah)?\b", r"\buraikan\b", r"\bbentuklah\b",
    r"\bsusunlah\b", r"\bbuatlah\b", r"\bubahlah\b", r"\btemukan(lah)?\b",
    r"\btunjukkan\b", r"\bnilai dari\b", r"\bmaka\b.{0,30}\badalah\b",
    # Catch-all: kata berimbuhan "-lah" (partikel imperatif Indonesia) --
    # ditemukan nyata bahwa daftar kata kerja tetap di atas TIDAK PERNAH
    # lengkap (mis. "bentuklah" awalnya tidak masuk daftar, menyebabkan soal
    # ASLI yang jelas-jelas ada isinya ikut salah kena flag). "-lah" adalah
    # partikel yang jarang muncul di luar konteks perintah/pertanyaan, jadi
    # risiko false-positive DARI pola ini sendiri rendah.
    # KECUALI kata yang akhiran "-lah"-nya bagian dari kata dasar / bukan
    # perintah. Ditemukan nyata: 454 dari 2.027 item (hasil PyMuPDF user)
    # lolos sebagai "punya soal" HANYA karena kata seperti "adalah" (589x),
    # "salah", "jumlah", "setelah" -- padahal itu jawaban tanpa soal.
    r"\b(?!(adalah|ialah|salah|jumlah|berjumlah|setelah|telah|sekolah|masalah|"
    r"istilah|olah|kalah|belah|sebelah|terbelah|lelah|malah|pilah|wilayah|"
    r"sejarah|ramah|rumah|bersalah|kesalahan|pengolah|pengolahan)\b)\w+lah\b",
    # Kata kerja perintah tanpa "-lah" yang umum di SD -- ditemukan nyata
    # (hasil PyMuPDF SD 4): "Ubahkan pecahan biasa berikut...", "Tulis nilai
    # tempat..." salah dianggap bukan soal.
    # Hanya dihitung kalau jadi KATA PERTAMA (posisi kalimat perintah) --
    # di tengah kalimat kata-kata ini sering berfungsi lain ("alat ukur",
    # "isi kotak"), ditemukan nyata lolos sebagai "soal" di SD 2.
    r"^\s*(\d{1,2}\.\s*)?(tulis|lingkari|warnai|pasangkan|hubungkan|cermati|amati|urai|salin|"
    r"pilih|isi|ubah|arsir|gunakan|tandai|ukur|bandingkan|kelompokkan|lanjutkan)\b",
    # Kata pertama berakhiran "-kan" = kata perintah ("Ubahkan", "Pasangkan"),
    # KECUALI "akan"/"bukan", dan kecuali kata berawalan me-/di-/ber-/ter-/
    # pe-/ke-/se- (bentuk aktif/pasif/kata benda, BUKAN perintah) -- ditemukan
    # nyata: judul narasi "2. Membandingkan Peluang dalam Kejadian Sehari-hari"
    # sempat lolos sebagai soal.
    r"^\s*(\d{1,2}\.\s*)?(?!(akan|bukan)\b)(?!(me|di|ber|ter|pe|ke|se)[a-z])[A-Za-z]+kan\b",
]
QUESTION_MARKER_RE = re.compile("|".join(QUESTION_MARKER_PATTERNS), re.IGNORECASE)

# Baris yang isinya cuma simbol/angka pendek -- gejala notasi matematika yang
# "pecah" jadi baris sendiri-sendiri akibat konversi PDF -> teks.
SYMBOL_ONLY_LINE_RE = re.compile(r"^[^\w]{0,2}[\d\W]{1,4}[^\w]{0,2}$")


@dataclass
class RawSoalBlock:
    """Satu kandidat soal hasil parsing, sebelum/ sesudah difilter."""

    source_file: str
    source_page: Optional[int]
    source_section: str            # contoh: "Jawaban Latihan 1.4"
    source_bab: Optional[str]
    source_subbab: Optional[str]
    source_item_no: str            # nomor asli di buku, misal "8"
    raw_text: str
    flags: List[str] = field(default_factory=list)
    status: str = "draft"
    extraction_confidence: float = 1.0
    # Jembatan ke Buku Siswa (dipakai soal_merger.py). `activity_seq` naik
    # tiap kali grup jawaban berganti (section baru ATAU sub-label aktivitas
    # baru), jadi item dengan activity_seq sama = satu kelompok soal di Buku
    # Siswa. `source_line_index` = posisi baris di dokumen, untuk urutan.
    source_activity: Optional[str] = None
    activity_seq: Optional[int] = None
    source_line_index: Optional[int] = None

    def to_dict(self) -> dict:
        """
        Kontrak output modul ini -- field yang BUKAN tanggung jawab
        `extractor_text.py` (correct_answer, image_url, cognitive_level,
        dst) sengaja tetap ditulis sebagai None/kosong di sini, supaya
        skema outputnya eksplisit dan konsisten untuk tahap berikutnya
        (answer_option_generator.py, extractor_image.py, lalu loader tim
        lain), bukan diam-diam hilang dari record.
        """
        return {
            "source_file": self.source_file,
            "source_page": self.source_page,
            "source_section": self.source_section,
            "source_bab": self.source_bab,
            "source_subbab": self.source_subbab,
            "source_item_no": self.source_item_no,
            "pertanyaan_text": self.raw_text,   # masih mentah, soal+jawaban menyatu
            # Pretest hanya memakai satu tipe soal: pilihan ganda. Field ini
            # sengaja di-hardcode "pilihan_ganda" (bukan dibuat opsional
            # multi-tipe) karena itu yang disepakati untuk scope pretest.
            "pertanyaan_type": "pilihan_ganda",
            "correct_answer": None,             # diisi answer_option_generator.py
            "options": [],                      # diisi answer_option_generator.py
            "image_url": None,                  # diisi extractor_image.py (1 gambar utama, kalau ada)
            "image_urls": [],                   # diisi extractor_image.py (kalau 1 soal butuh >1 gambar)
            # Nama key ini SENGAJA disamakan persis dengan field
            # `extraction_flags` di model Mongo (questions_pretest.py) --
            # supaya loader tim lain bisa map JSON -> field model 1:1 tanpa
            # perlu tabel terjemahan nama field tambahan.
            "extraction_flags": self.flags,
            "status": self.status,
            "extraction_confidence": self.extraction_confidence,
            # Field tambahan (baru) -- untuk soal_merger.py. Aman untuk
            # loader tim lain: cuma key tambahan, tidak ada key lama berubah.
            "source_activity": self.source_activity,
            "activity_seq": self.activity_seq,
            "source_line_index": self.source_line_index,
        }


# Ligatur font yang GAGAL diterjemahkan PDF -> teks (PyMuPDF): huruf "fl"/"ti"
# hilang. Ditemukan nyata: "Refleksi" -> "Releksi" (heading tidak dikenali,
# ikut menempel ke jawaban), "Latihan" -> "Laihan", "Alternatif" ->
# "Alternaif" (SMP 8 -- dulu dikira salah ketik dari buku). Perbaikan HANYA
# untuk kata-kata tertentu yang pasti (daftar tertutup), bukan tebakan umum.
_LIGATURE_LOSS_FIXES = {
    "Releksi": "Refleksi", "releksi": "refleksi",
    "Laihan": "Latihan", "laihan": "latihan",
    "Alternaif": "Alternatif", "alternaif": "alternatif",
}
_LIGATURE_LOSS_RE = re.compile(r"\b(" + "|".join(_LIGATURE_LOSS_FIXES) + r")\b")


def _clean_line(line: str) -> str:
    import unicodedata

    # Karakter ligatur yang terbaca utuh (U+FB00-FB06: ﬀ ﬁ ﬂ ﬃ ﬄ) -> huruf biasa.
    line = "".join(unicodedata.normalize("NFKC", ch) if "\ufb00" <= ch <= "\ufb06" else ch for ch in line)
    line = _LIGATURE_LOSS_RE.sub(lambda m: _LIGATURE_LOSS_FIXES[m.group(1)], line)
    return line.strip()


# Baris berisi cuma 1 karakter tanda baca/bullet -- ditemukan nyata di
# testing manual sebagai ARTEFAK: ikon bullet/kotak centang di PDF asli yang
# ter-convert jadi 1 karakter aneh berdiri sendiri (mis. "." sendirian di
# satu baris), bukan bagian isi soal. Sengaja SANGAT SEMPIT (cuma 1 karakter
# tanda baca, TANPA huruf/angka) supaya tidak ikut membuang konten asli yang
# kebetulan pendek (mis. jawaban satu digit "5" tetap lolos, karena itu
# bukan tanda baca).
_STRAY_BULLET_LINE_RE = re.compile(r"^[.•∙ꞏo\-–—]$")

# Baris berisi HANYA angka (1-4 digit) -- dicek terpisah apakah ini nomor
# halaman (footer/header) yang bocor, BUKAN konten soal. Dianggap nomor
# halaman kalau nilainya DEKAT dengan nomor halaman asli PDF (page_no dari
# PyMuPDF), bukan asal semua baris angka dibuang -- soalnya banyak soal
# matematika SD-SMA yang jawabannya memang cuma 1 angka pendek per baris
# (mis. tabel nilai tempat "2\n6\n9\n3\n2"), itu HARUS tetap dipertahankan.
_BARE_NUMBER_LINE_RE = re.compile(r"^\d{1,4}$")
_PAGE_NUMBER_PROXIMITY_TOLERANCE = 3


def _looks_like_leaked_page_number(line: str, page_no: int) -> bool:
    m = _BARE_NUMBER_LINE_RE.match(line)
    if not m:
        return False
    try:
        value = int(line)
    except ValueError:
        return False
    return abs(value - page_no) <= _PAGE_NUMBER_PROXIMITY_TOLERANCE


def attach_page_numbers(
    pages_text: List[Tuple[int, str]]
) -> List[Tuple[str, int, Optional[str]]]:
    """
    Menerima list (page_number, page_text) -- misal langsung dari PyMuPDF
    (fitz), lalu meratakan jadi list (line, page_number, bab_label=None).

    Jalur ini TIDAK mencoba menebak bab dari footer (karena kalau kamu sudah
    punya halaman per-page dari PyMuPDF, footer/header biasanya masih ikut
    tercampur di teksnya) -- bab akan di-fallback ke BAB_HEADING_RE di body
    oleh `extract_candidate_blocks`. Kalau footer bukunya ternyata konsisten
    seperti pada txt hasil konversi, pertimbangkan tetap memakai
    `attach_page_numbers_from_footers` terhadap gabungan semua halaman.
    """
    result: List[Tuple[str, int, Optional[str]]] = []
    for page_no, page_text in pages_text:
        for raw_line in page_text.splitlines():
            result.append((_clean_line(raw_line), page_no, None))
    return result


def attach_page_numbers_from_footers(
    raw_text: str,
) -> List[Tuple[str, int, Optional[str]]]:
    """
    Dipakai kalau sumbernya adalah satu blob teks tanpa page-break eksplisit
    (misal hasil `pdftotext` polos). Nomor halaman ditebak dari footer yang
    berulang di tiap halaman buku ini:
        "<n> Buku Panduan Guru Matematika untuk SMA/SMK Kelas XI"   (halaman genap)
        "Bab <n> | <judul bab> <n>"                                   (halaman ganjil)
    Footer "Bab N | Judul" juga dipakai untuk tracking bab berjalan, karena
    heading bab asli di body sering terpecah jadi beberapa baris dekoratif
    oleh layout PDF dan tidak bisa diandalkan sebagai penanda tunggal.
    Baris footer itu sendiri TIDAK ikut jadi konten (di-drop).

    Return: list of (line, page_number, bab_label_kalau_berubah)
    """
    result = []
    current_page = 1
    current_bab_label: Optional[str] = None
    for raw_line in raw_text.splitlines():
        line = _clean_line(raw_line)
        m_left = PAGE_FOOTER_LEFT_RE.match(line)
        m_right = PAGE_FOOTER_RIGHT_RE.match(line)
        if m_left:
            current_page = int(m_left.group(1))
            continue
        if m_right and m_right.group(4):
            current_page = int(m_right.group(4))
        if m_right:
            current_bab_label = f"Bab {m_right.group(1)} {m_right.group(2)}".strip()
            continue
        result.append((line, current_page, current_bab_label))
    return result


def attach_page_numbers_with_bab_tracking(
    pages_text: List[Tuple[int, str]]
) -> List[Tuple[str, int, Optional[str]]]:
    """
    Dipakai kalau kamu SUDAH punya nomor halaman yang akurat per halaman
    (misal langsung dari PyMuPDF `page.number`), tapi tetap ingin tracking
    bab dari footer "Bab N | Judul" yang berulang tiap halaman (lebih andal
    daripada heading bab di body yang sering terpecah oleh layout dekoratif).

    Beda dengan `attach_page_numbers_from_footers`: di sini nomor halaman
    TIDAK ditebak dari footer -- dipakai apa adanya dari `pages_text` --
    footer hanya dipakai untuk label bab. Baris footer tetap di-drop dari
    konten karena bukan bagian dari soal.
    """
    result: List[Tuple[str, int, Optional[str]]] = []
    current_bab_label: Optional[str] = None
    last_appended_line: Optional[str] = None
    offset = _learn_printed_page_offset(pages_text)
    for page_no, page_text in pages_text:
        for raw_line in page_text.splitlines():
            line = _clean_line(raw_line)
            if PAGE_FOOTER_LEFT_RE.match(line) or GENERIC_FOOTER_RE.match(line):
                continue
            # Nomor halaman CETAK yang berdiri sendiri (PyMuPDF memisahkannya
            # dari teks footer). Nomor cetak beda dengan indeks halaman PDF
            # (mis. PDF hal 70 = cetak "61"), jadi selisihnya dipelajari
            # per dokumen (lihat _learn_printed_page_offset).
            if offset is not None and _BARE_NUMBER_LINE_RE.match(line) and int(line) == page_no + offset:
                continue
            m_right = PAGE_FOOTER_RIGHT_RE.match(line)
            if m_right:
                current_bab_label = f"Bab {m_right.group(1)} {m_right.group(2)}".strip()
                continue
            # Artefak konversi PDF: ikon bullet yang jadi 1 karakter nyasar,
            # atau nomor halaman footer/header yang bocor ikut masuk konten.
            # Lihat catatan di _STRAY_BULLET_LINE_RE / _looks_like_leaked_page_number.
            if _STRAY_BULLET_LINE_RE.match(line):
                continue
            if _looks_like_leaked_page_number(line, page_no):
                continue
            # Baris yang PERSIS SAMA dengan baris tepat sebelumnya --
            # ditemukan nyata terjadi (mis. "atau\natau", heading yang
            # ter-render dobel karena elemen dekoratif tumpang tindih di
            # PDF asli). Cukup collapse yang BERURUTAN LANGSUNG, bukan
            # dedupe global, supaya konten berulang yang memang sengaja
            # (mis. dua soal berbeda kebetulan sama) tidak salah terbuang.
            if line and line == last_appended_line:
                continue
            result.append((line, page_no, current_bab_label))
            last_appended_line = line
    return _merge_split_headings(result)


# Heading yang oleh PyMuPDF dipecah jadi 2 baris: "Kunci Jawaban Latihan" /
# "1.1" (SD 6), "Eksplorasi" / "1.2". Tanpa digabung, ID-nya hilang: label
# tidak bisa dicocokkan ke Buku Siswa, dan "Eksplorasi 1.2" tidak menutup
# section jawaban (narasi guru sesudahnya ikut tertangkap).
_SPLIT_HEADING_HEAD_RE = re.compile(
    r"^(((Alterna\w*f\s+|Kunci\s+)?Jawaban\s+)?(Soal\s+)?(La\w*han|Eksplorasi|Uji\s+Kompetensi(\s+Bab)?))$"
)
# ID bisa angka ("1.1") ATAU huruf ("A", "A Persamaan Linear Dua Variabel")
# -- versi huruf ditemukan nyata di hasil PyMuPDF SMP 9: "Kunci Jawaban
# Latihan" / "A" / judul, sehingga 115 jawaban kehilangan label.
_SPLIT_HEADING_ID_RE = re.compile(r"^(\d{1,2}(\.\d{1,2})?|[A-H](\s*[—\-–]\s*|\s+)\S.*|[A-H])$")


def _merge_split_headings(rows: List[Tuple[str, int, Optional[str]]]) -> List[Tuple[str, int, Optional[str]]]:
    out: List[Tuple[str, int, Optional[str]]] = []
    i = 0
    while i < len(rows):
        line, pg, bab = rows[i]
        if _SPLIT_HEADING_HEAD_RE.match(line):
            j = i + 1
            while j < len(rows) and not rows[j][0]:
                j += 1
            if j < len(rows) and _SPLIT_HEADING_ID_RE.match(rows[j][0]):
                out.append((f"{line} {rows[j][0]}", pg, bab))
                i = j + 1
                continue
        out.append(rows[i])
        i += 1
    return out


def _learn_printed_page_offset(pages_text: List[Tuple[int, str]]) -> Optional[int]:
    """Selisih (nomor halaman cetak - indeks halaman PDF) yang paling sering,
    dilihat dari baris angka tunggal di 3 baris pertama/terakhir tiap halaman.
    None kalau tidak ada pola yang konsisten (mis. input 1 blob teks)."""
    from collections import Counter

    if len(pages_text) < 5:
        return None
    votes: Counter = Counter()
    for page_no, text in pages_text:
        ls = [l.strip() for l in text.splitlines() if l.strip()]
        for l in ls[:3] + ls[-3:]:
            if _BARE_NUMBER_LINE_RE.match(l):
                votes[int(l) - page_no] += 1
    if not votes:
        return None
    off, n = votes.most_common(1)[0]
    return off if n >= max(3, len(pages_text) * 0.3) else None


def run_extraction_from_pages_with_bab_tracking(
    pages_text: List[Tuple[int, str]], source_file: str
) -> List[RawSoalBlock]:
    """Pipeline lengkap Tahap 1 untuk sumber per-halaman (PyMuPDF) DENGAN
    tracking bab dari footer -- ini jalur yang dipakai `sibi_loader.py`."""
    lines_with_page = attach_page_numbers_with_bab_tracking(pages_text)
    blocks = extract_candidate_blocks(lines_with_page, source_file)
    return [apply_filters(b) for b in blocks]


_PURE_NUMBER_RE = re.compile(r"\d+([.,]\d+)*")
_ORPHAN_OP_RE = re.compile(r"[−\-=+×÷:<>≤≥]+")


def _looks_garbled(text: str) -> bool:
    """Heuristik kasar: banyak baris pendek berisi simbol -> kemungkinan
    notasi matematika yang pecah akibat ekstraksi PDF."""
    lines = [l for l in text.splitlines() if l.strip()]
    if not lines:
        return False
    # Baris ANGKA MURNI ("231", "2,5") tidak dihitung: PyMuPDF memecah tiap
    # sel tabel jadi baris sendiri, sehingga tabel angka yang bersih (SD 3,
    # "Ratusan / 2 / Puluhan / 3") salah dianggap rumus rusak. Yang dihitung
    # cuma baris simbol/operator yatim ("−", "=", "+ =", "!").
    symbol_lines = sum(
        1 for l in lines
        if SYMBOL_ONLY_LINE_RE.match(l.strip()) and not _PURE_NUMBER_RE.fullmatch(l.strip())
    )
    # Dua baris operator yatim atau lebih ("+", "=", "−" berdiri sendiri) =
    # notasi yang terpecah, walau rasionya kecil karena banyak baris angka.
    orphan_ops = sum(1 for l in lines if _ORPHAN_OP_RE.fullmatch(l.strip()))
    return (len(lines) >= 4 and (symbol_lines / len(lines)) >= 0.25) or orphan_ops >= 2


def extract_candidate_blocks(
    lines_with_page: List[Tuple[str, int, Optional[str]]], source_file: str
) -> List[RawSoalBlock]:
    """
    Langkah 1 (murni struktural, tanpa filter kualitas):
    - Tracking bab (dari footer, elemen ke-3 tiap baris) / subbab berjalan.
    - Deteksi mulai/berakhirnya section jawaban ("Jawaban Latihan X.X", dst).
    - Di dalam section jawaban, pecah jadi per-nomor soal (item bernomor
      level atas: "1.", "2.", dst -- BUKAN sub-poin "a)"/"b)").
    Mengembalikan blok mentah, BELUM difilter (filter ada di `apply_filters`).

    `lines_with_page` berisi (line, page_number, bab_label_dari_footer).
    Elemen bab_label boleh None terus kalau sumbernya tidak melewati
    `attach_page_numbers_from_footers` -- di kondisi itu, heading "Bab N ..."
    di body (BAB_HEADING_RE) dipakai sebagai fallback.
    """
    blocks: List[RawSoalBlock] = []

    current_bab: Optional[str] = None
    current_subbab: Optional[str] = None
    current_section: Optional[str] = None
    in_answer_section = False

    item_no: Optional[str] = None
    item_lines: List[str] = []
    item_start_page: Optional[int] = None
    item_start_line: Optional[int] = None

    # Label aktivitas yang sedang berjalan di dalam section jawaban (lihat
    # ACTIVITY_LABEL_RE) + nomor urut grup, untuk soal_merger.py.
    current_activity: Optional[str] = None
    activity_seq = 0

    group_last_no: Optional[int] = None

    def start_group(label: Optional[str]):
        nonlocal current_activity, activity_seq, group_last_no
        current_activity = label if normalize_activity_key(label) else None
        activity_seq += 1
        group_last_no = None

    item_note_cut = False

    def flush_item():
        nonlocal item_no, item_lines, item_start_page, item_start_line, item_note_cut
        item_note_cut_local = item_note_cut
        item_note_cut = False
        if in_answer_section and item_no is not None and item_lines:
            blocks.append(
                RawSoalBlock(
                    source_file=source_file,
                    source_page=item_start_page,
                    source_section=current_section or "",
                    source_bab=current_bab,
                    source_subbab=current_subbab,
                    source_item_no=item_no,
                    raw_text="\n".join(item_lines).strip(),
                    source_activity=current_activity,
                    activity_seq=activity_seq,
                    source_line_index=item_start_line,
                    flags=["teacher_note_trimmed"] if item_note_cut_local else [],
                )
            )
        item_no = None
        item_lines = []
        item_start_page = None
        item_start_line = None

    for line_idx, (line, page_no, bab_label) in enumerate(lines_with_page):
        # Footer "Bab N | Judul" adalah sumber bab paling andal (berulang
        # tiap halaman); kalau tersedia dan berbeda dari yang tercatat,
        # perbarui current_bab dan reset subbab/section karena ganti bab.
        if bab_label and bab_label != current_bab:
            flush_item()
            in_answer_section = False
            current_section = None
            current_bab = bab_label
            current_subbab = None

        if not line:
            continue

        bab_match = BAB_HEADING_RE.match(line)
        if bab_match and current_bab is None:
            # Fallback: dipakai hanya kalau tidak ada info bab dari footer
            # sama sekali (misal sumber per-halaman dari PyMuPDF tanpa
            # footer di-strip terlebih dahulu).
            flush_item()
            in_answer_section = False
            current_section = None
            current_bab = f"Bab {bab_match.group(1)} {bab_match.group(2)}".strip()
            current_subbab = None
            continue

        # Dicek SEBELUM SUBBAB_HEADING_RE: "H.        Kunci Jawaban" secara
        # bentuk cocok juga dengan pola subbab huruf biasa, tapi maknanya
        # adalah section jawaban, bukan subbab baru -- jadi prioritasnya
        # harus menang duluan.
        if LETTERED_KUNCI_JAWABAN_RE.match(line):
            flush_item()
            current_section = line
            in_answer_section = True
            start_group(line)
            continue

        subbab_match = SUBBAB_HEADING_RE.match(line)
        if subbab_match:
            flush_item()
            in_answer_section = False
            current_section = None
            current_subbab = f"{subbab_match.group(1)}. {subbab_match.group(2)}".strip()
            continue

        if (
            ANSWER_SECTION_RE.match(line)
            or PLAIN_KUNCI_JAWABAN_RE.match(line)
            or JAWABAN_SOAL_LATIHAN_RE.match(line)
            or ASESMEN_KUNCI_JAWABAN_RE.match(line)
        ):
            flush_item()
            current_section = line
            in_answer_section = True
            start_group(line)
            continue

        if (
            OTHER_SECTION_RE.match(line)
            or NUMBERED_OTHER_SECTION_RE.match(line)
            or GURU_SUBBAB_HEADING_RE.match(line)
        ):
            flush_item()
            in_answer_section = False
            current_section = None
            continue

        if in_answer_section:
            if LATIHAN_SUBGROUP_LABEL_RE.match(line):
                # Label pengelompokan ("1. Latihan A Jenis-Jenis Matriks"),
                # BUKAN soal -- buang tanpa membuka item_no baru, dan JANGAN
                # tutup in_answer_section (jawaban asli menyusul langsung
                # sesudahnya, bernomor ulang dari 1).
                flush_item()
                start_group(line)
                continue

            if ACTIVITY_LABEL_RE.match(line):
                # Sub-label aktivitas di dalam Kunci Jawaban ("Ayo Berlatih",
                # "Latihan 1.2", "Latihan Soal Lingkaran", ...) -- tutup item
                # berjalan, mulai grup baru. JANGAN ditempel ke teks item.
                flush_item()
                start_group(line)
                continue

            item_match = ITEM_START_RE.match(line)
            bare_match = None if item_match else BARE_ITEM_NO_RE.match(line)
            if item_match or bare_match:
                new_no = int((item_match or bare_match).group(1))
                if (
                    SPLIT_GROUP_ON_NUMBER_RESTART
                    and group_last_no is not None
                    and new_no <= group_last_no
                ):
                    # Nomor MUNDUR/ULANG tanpa heading/label baru = daftar
                    # bernomor LAIN. Ditemukan nyata di SMP 9: grup "Latihan A"
                    # berisi nomor [1..10, 2, 1, 2, ...] -- sesudah 10 bukan
                    # lagi jawaban Latihan A. Item-nya TIDAK dibuang (A/B test
                    # membuktikan sebagian adalah jawaban asli), tapi dipisah
                    # ke grup baru TANPA label supaya grup "Latihan A" tidak
                    # tercemar dan jumlah soalnya akurat untuk soal_merger.
                    flush_item()
                    start_group(None)
                group_last_no = new_no
            if item_match:
                flush_item()
                item_no = item_match.group(1)
                item_lines = [line]
                item_start_page = page_no
                item_start_line = line_idx
            elif bare_match and not (
                current_section and "eksplorasi" in current_section.lower()
            ):
                # Nomor sendirian di barisnya (varian SMA Kelas 12) -- isi
                # soalnya baru menyusul di baris-baris berikutnya, jadi
                # item_lines mulai kosong (bukan [line] seperti di atas,
                # karena baris ini cuma nomor, tidak ada teks lain).
                # Sengaja DIKECUALIKAN untuk section "Eksplorasi": di situ
                # baris "N." sering cuma nomor baris tabel/data aktivitas,
                # bukan soal tertutup -- kalau ikut ditangkap, isinya cuma
                # angka mentah tanpa konteks (melanggar kriteria "tidak
                # mengambang").
                flush_item()
                item_no = bare_match.group(1)
                item_lines = []
                item_start_page = page_no
                item_start_line = line_idx
            elif item_no is not None and not item_note_cut:
                if GENERIC_FOOTER_RE.match(line):
                    # Footer halaman (termasuk footer halaman Buku Siswa yang
                    # direproduksi di Buku Guru SD, mis. "32 Matematika untuk
                    # SD/MI Kelas I") -- bukan isi jawaban.
                    continue
                if TEACHER_NOTE_START_RE.match(line):
                    # Catatan untuk guru di EKOR jawaban ("Kembangkan soal-soal
                    # ... bagi peserta didik yang kecepatan belajarnya tinggi")
                    # -- ditemukan nyata oleh review independen. Jawaban di
                    # depannya tetap dipakai, sisanya sampai nomor berikutnya
                    # dibuang (bukan bagian kunci jawaban).
                    item_note_cut = True
                    continue
                item_lines.append(line)
            # baris di dalam section jawaban SEBELUM nomor pertama muncul
            # (jarang terjadi) sengaja diabaikan -- tidak ada nomor soal
            # untuk ditempeli.

    flush_item()
    return blocks


def apply_filters(block: RawSoalBlock) -> RawSoalBlock:
    """
    Langkah 2: terapkan kriteria "layak diekstrak" yang sudah disepakati.
    Mengubah `status`, `flags`, dan `extraction_confidence` pada block
    (in-place, dan juga return block yang sama untuk kemudahan chaining).
    """
    text = block.raw_text

    if OPEN_ENDED_RE.search(text):
        block.status = "skipped_open_ended"
        block.flags.append("open_ended")

    if PEMBUKTIAN_RE.search(text):
        block.flags.append("pembuktian")
        # Soal pembuktian murni di-skip untuk pretest (lihat kriteria no. 3).
        # Kalau sudah kena open_ended duluan, status itu yang menang -- tapi
        # umumnya pembuktian bukan open_ended, jadi kita set di sini.
        if block.status == "draft":
            block.status = "skipped_pembuktian"

    if NEEDS_IMAGE_RE.search(text):
        block.flags.append("needs_image")
        if block.status == "draft":
            block.status = "needs_image"

    if _looks_garbled(text):
        block.flags.append("possible_formula_garbling")
        block.extraction_confidence = min(block.extraction_confidence, 0.4)
        if block.status == "draft":
            block.status = "needs_review_extraction"

    if not QUESTION_MARKER_RE.search(text):
        # Flag SELALU ditambahkan (informational) apa pun status saat ini,
        # supaya bisa difilter di review tool terlepas dari status lain yang
        # sudah kena. Status HANYA diturunkan kalau masih "draft" -- kalau
        # sudah kena needs_image/skipped_*/needs_review_extraction duluan,
        # blok itu memang sudah masuk jalur review, jadi status itu
        # dipertahankan (tidak ditimpa) supaya makna status lain tidak hilang.
        block.flags.append("missing_soal_text")
        if block.status == "draft":
            block.status = "needs_review_missing_soal"

    # Pengecekan SISI JAWABAN -- ditemukan oleh review independen terhadap
    # hasil penggabungan dengan Buku Siswa: yang tertangkap sebagai
    # "jawaban" kadang bukan jawaban sama sekali (rubrik penilaian, catatan
    # untuk guru, atau cuma "2. a." tanpa isi). Masalah ini FATAL (tidak ada
    # kunci jawaban yang bisa dipakai), jadi statusnya menimpa status review
    # lain -- kecuali yang memang sudah di-skip.
    answer_problem = None
    if TEACHER_NOTE_RE.search(text):
        answer_problem = "answer_is_teacher_note"
    elif _answer_is_empty(text):
        answer_problem = "answer_empty"
    if answer_problem:
        block.flags.append(answer_problem)
        if not block.status.startswith("skipped"):
            block.status = "needs_review_answer"

    return block


# Baris yang MEMULAI catatan untuk guru (dipotong dari ekor jawaban).
TEACHER_NOTE_START_RE = re.compile(
    r"^(Kembangkan soal|Guru (juga )?(dapat|memberikan|meminta|mengarahkan|perlu)\b|"
    r"Bapak/Ibu Guru|Bagi peserta didik|Untuk melakukan Eksplorasi|Diferensiasi\b|"
    r"Catatan untuk guru)",
    re.IGNORECASE,
)

# Footer halaman yang bisa bocor ke teks jawaban (Guru maupun halaman Siswa
# yang direproduksi di Buku Guru SD).
GENERIC_FOOTER_RE = re.compile(
    r"^(\d{1,3}\s+)?(Buku Panduan Guru\s+)?Matematika(\s+Tingkat\s+Lanjut)?\s+untuk\s+"
    r"(SD|SMP|SMA)\S*.*$"
    # Footer halaman Buku Siswa yang direproduksi di Buku Guru SD (PyMuPDF):
    # "1 Ayo Membilang sampai dengan 10    13" = nomor bab + judul + SPASI
    # LEBAR + nomor halaman. Spasi lebar (>=2) jadi syarat supaya kalimat
    # biasa yang kebetulan diawali angka tidak ikut terbuang.
    r"|^\d{1,2}\s+[A-Z][A-Za-z ,\-]{2,60}\s{2,}\d{1,3}$"
)

# Catatan untuk guru / rubrik yang nyasar ke posisi jawaban.
TEACHER_NOTE_RE = re.compile(
    r"rubrik penilaian|pedoman penskoran|\bguru dapat\b|diserahkan kepada|"
    r"bapak/ibu guru|kecepatan belajar(nya)? (tinggi|rendah)|\btindak lanjut\b",
    re.IGNORECASE,
)
_ANSWER_SCAFFOLD_RE = re.compile(
    r"^\s*\d{1,2}\.\s*|\b[a-h][.)]\s*|"
    # "Alternatif penyelesaian. a. b." -- ditemukan nyata lolos (review ronde 3)
    r"\balterna\w*f\s+(jawaban|penyelesaian)\s*:?\.?|\b(jawab|penyelesaian)\s*:",
    re.IGNORECASE,
)


def _answer_is_empty(text: str) -> bool:
    """True kalau setelah nomor soal & label sub-poin ("a.", "b)") dibuang,
    tidak tersisa isi apa pun (mis. "2. a." atau "1. a. b. / c. d.")."""
    rest = _ANSWER_SCAFFOLD_RE.sub(" ", text)
    return len(re.sub(r"[\W_]+", "", rest)) < 2


def run_extraction(raw_text: str, source_file: str) -> List[RawSoalBlock]:
    """Pipeline lengkap Tahap 1 (untuk sumber tanpa page-break eksplisit)."""
    lines_with_page = attach_page_numbers_from_footers(raw_text)
    blocks = extract_candidate_blocks(lines_with_page, source_file)
    return [apply_filters(b) for b in blocks]


def run_extraction_from_pages(
    pages_text: List[Tuple[int, str]], source_file: str
) -> List[RawSoalBlock]:
    """Pipeline lengkap Tahap 1 untuk sumber yang SUDAH punya info halaman
    per-page (misal langsung dari PyMuPDF `page.get_text()` per halaman)."""
    lines_with_page = attach_page_numbers(pages_text)
    blocks = extract_candidate_blocks(lines_with_page, source_file)
    return [apply_filters(b) for b in blocks]


def summarize(blocks: List[RawSoalBlock]) -> dict:
    """Ringkasan cepat untuk log/monitoring -- bukan untuk audit satu-satu,
    tapi metrik agregat sesuai prinsip yang sudah didiskusikan."""
    summary: dict = {}
    for b in blocks:
        summary[b.status] = summary.get(b.status, 0) + 1
    summary["_total"] = len(blocks)
    return summary


# ---------------------------------------------------------------------------
# Export -- kontrak output ke tahap berikutnya (image extraction, answer/
# option generation, lalu loader tim lain). TIDAK ada kode MongoDB di sini
# sama sekali -- modul ini berhenti di "tulis file JSON".
# ---------------------------------------------------------------------------

def export_to_json(blocks: List[RawSoalBlock], output_path: str) -> None:
    """Tulis hasil ekstraksi ke satu file JSON, siap dibaca modul/tim lain."""
    import json
    import os

    payload = {
        "pipeline_version": PIPELINE_VERSION,
        "summary": summarize(blocks),
        "items": [b.to_dict() for b in blocks],
    }
    # Buat folder tujuan otomatis kalau belum ada (mis. "output/") --
    # supaya pemanggil CLI tidak perlu `mkdir` manual dulu tiap kali pakai
    # path output baru.
    parent_dir = os.path.dirname(output_path)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)


def extract_pdf_to_json(pdf_path: str, output_path: str) -> dict:
    """
    Pipeline end-to-end TANPA MongoDB: PDF -> teks per halaman (PyMuPDF)
    -> extractor -> file JSON. Ini yang dipanggil dari CLI di bawah.
    """
    import fitz  # PyMuPDF

    source_file = _os_basename(pdf_path)
    pages_text = []
    with fitz.open(pdf_path) as doc:
        for i, page in enumerate(doc):
            pages_text.append((i + 1, page.get_text()))

    blocks = run_extraction_from_pages_with_bab_tracking(pages_text, source_file)
    export_to_json(blocks, output_path)
    return summarize(blocks)


def _os_basename(path: str) -> str:
    import os

    return os.path.basename(path)


def _cli():
    import argparse

    parser = argparse.ArgumentParser(
        description="Ekstraksi teks soal pretest dari PDF Buku Panduan Guru -> JSON "
        "(tidak menyentuh MongoDB -- output ini diserahkan ke tahap/tim berikutnya)."
    )
    parser.add_argument("--pdf", required=True, help="Path ke file PDF buku panduan guru")
    parser.add_argument(
        "--out",
        required=True,
        help="Path file JSON output, misal output/kelas11_bab1_3.json",
    )
    args = parser.parse_args()

    stats = extract_pdf_to_json(args.pdf, args.out)
    print(f"Selesai. Ringkasan status:")
    for status, count in stats.items():
        print(f"  {status}: {count}")
    print(f"\nOutput tersimpan di: {args.out}")


if __name__ == "__main__":
    _cli()
