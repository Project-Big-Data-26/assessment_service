# Ekstraksi Soal Pretest: Pipeline Agentic

Pipeline ini menggantikan alur lama `extractor_text.py` → `soal_merger.py` →
`answer_option_generator.py` (regex + Ollama qwen3:4b).

## Masalah pipeline lama

| Masalah | Penyebab | Solusi di pipeline agentic |
|---|---|---|
| Soal tidak sesuai konteks | Stimulus (bacaan, tabel, data) tidak ikut; hanya kalimat bernomor yang diambil | Agen membaca halaman utuh dan menyalin stimulus ke field `stimulus` |
| Batas soal bocor | Regex tidak tahu kapan section berakhir | Agen menentukan batas soal dari pemahaman isi |
| Kunci salah pasang | Regex memasangkan Buku Guru ↔ Siswa lewat nomor/heading | Agen mencari kunci dengan Grep isi khas soal, lalu mengerjakan sendiri untuk cross-check |
| Pecahan/rumus rusak | Teks PDF tidak menyimpan struktur rumus | Halaman bertanda `[M]` dibaca dari PNG dan ditulis dalam LaTeX |
| Model 4B mengarang | Model kecil, tanpa verifikasi | Model kuat + validator mekanis (verbatim, angka, opsi, kunci) |
| ~450 dari ~3.600 soal lolos | Kombinasi semua masalah di atas | Soal yang tidak bisa jadi PG dicatat alasannya di `dilewati` |

## Alur

```
PDF ──convert.py──► Markdown per halaman + INDEX.md (+ PNG sesuai permintaan)
                        │
                        ▼
      AI Agent (skill /ekstrak-soal-pretest, 1 subagent per bab)
                        │  menulis output/pretest/<buku>/bab<NN>.json
                        ▼
               validate.py  ◄── agen memperbaiki sampai LOLOS
                        │
                        ▼
               export.py ──► output/pretest/<buku>/soal_pretest.json
                             (format model Pertanyaan, opsi A-D diacak seimbang)
```

Pembagian kerja: **kode** menangani hal yang deterministik (konversi, cek, pengacakan
posisi opsi, status). **Agen** menangani hal yang butuh pemahaman (batas soal, stimulus,
membaca notasi, mencari kunci, distraktor).

## Cara pakai

```bash
# 1. Konversi PDF (sekali; ±2 detik/halaman, bisa dilanjutkan kalau terputus)
python -m app.services.pretest.agentic.convert --all --workers 3

# 2. Di Claude Code, dari root project:
/ekstrak-soal-pretest lanjut              # bab berikutnya yang belum selesai
/ekstrak-soal-pretest kelas9 bab 2        # bab tertentu
/ekstrak-soal-pretest kelas9 semua        # semua bab satu buku

# 3. Cek & export (agen juga menjalankannya)
python -m app.services.pretest.agentic.validate output/pretest/kelas9/bab02.json
python -m app.services.pretest.agentic.progress          # papan progres -> output/pretest/PROGRESS.md
python -m app.services.pretest.agentic.export --book kelas9

# 4. Rakit pretest -> format tabel `soal` backend (2 soal/subbab + 1 soal/bab prasyarat)
python -m app.services.pretest.agentic.pretest --book kelas9
```

## Pretest (aturan tim)

- Satu sesi per bab = **2 soal PG per subbab** + **1 soal PG per bab prasyarat**. Soal
  prasyarat diambil dari **subbab terakhir** bab prasyarat, yaitu yang paling susah
  (`tingkat_kesulitan` 1-5, dinilai agen). Soal dengan kunci Guru terverifikasi
  diutamakan.
- Subbab dan prasyarat hanya diambil dari `data/bab_prasyarat/Prasyarat_Math.xlsx`
  (`kurikulum.py`).
- Bab prasyarat dari buku lain cukup diekstrak subbab terakhirnya
  (`"mode": "prasyarat"`).
- Output di `output/pretest/<buku>/`:
  - `soal_pretest_db.json`: dokumen tabel `soal` (sheet *Log 1227 25092026*).
    `berkas_id`, `kelas_id`, `matching_pairs`, `cognitive_*`, `confidence_score`, dan
    `status` = `null`. `subbab_id` = nama subbab. `_id` deterministik, jadi seeder
    melakukan upsert berdasarkan `_id`.
  - `sesi_pretest.json`: `_id` soal per subbab dan per prasyarat, beserta jejak audit
    (halaman sumber, status verifikasi).
  - `images/`: gambar yang dirujuk `image_url`.

## Hemat token & memori agen

- Buku tidak pernah dibaca utuh. Agen membaca `INDEX.md` (ringkasan per bab), lalu hanya
  membuka halaman latihan di rentang bab tersebut.
- Kunci dicari dengan Grep (kata/angka khas soal), bukan dengan membaca seluruh Buku Guru.
- PNG dirender hanya untuk halaman `[M]` (rumus) / `[T]` (teks di dalam gambar) / soal
  bergambar.
- Satu bab dikerjakan oleh satu subagent dengan konteks baru, sehingga sesi utama tetap kecil.
- Memori lintas sesi disimpan di file, tidak di percakapan:
  - `output/pretest/PROGRESS.md`: bab mana yang sudah selesai
  - `output/pretest/<buku>/CATATAN.md`: temuan per buku (letak kunci, salah ketik di
    Buku Guru, dll.)
  - `bab<NN>.json` disimpan bertahap, jadi bisa dilanjutkan

## Status soal (dihitung `schema.derive_status`, bukan oleh agen)

| status | arti |
|---|---|
| `draft` | Kunci Guru cocok dengan pengerjaan agen dan soal verbatim. Siap untuk tahap berikutnya (validasi Bloom, dll.) |
| `needs_review_kunci` | Kunci Guru ≠ agen, atau kunci tidak ada di Buku Guru |
| `needs_review_soal` | Kalimat soal disesuaikan agar bisa jadi PG |
| `needs_image` | Soal butuh gambar yang belum tersedia filenya |

Contoh hasil nyata: `output/pretest/kelas5/bab01.json` berisi 42 soal (29 draft, 13 review)
dan 12 dilewati. Salah satu yang tertangkap: salah ketik kunci di Buku Guru (Rp15.590 vs
Rp15.950).
