# Pipeline Agentic Pretest dan Integrasinya ke API Nalar

Dokumen ini mengkalibrasi dokumentasi API terhadap merge commit `42647a4`. Ia menjelaskan kode dan artefak pretest yang benar-benar ada di repository, batasnya, serta adapter yang diperlukan sebelum hasil ekstraksi masuk ke arsitektur target pada dokumen 01–20.

## 1. Status implementasi

| Bagian | Status | Bukti repository |
|---|---|---|
| PDF ke Markdown per halaman, indeks dan gambar | `prototype` | `app/services/pretest/agentic/convert.py` |
| Kontrak ketat hasil ekstraksi per bab | `implemented_local` | `agentic/schema.py` |
| Validator verbatim, angka, kunci, opsi dan gambar | `implemented_local`, diuji unit | `agentic/validate.py`, 23 tes lulus |
| Ekstraksi semantik oleh Claude Code per bab | `development_workflow` | `.claude/agents/` dan `.claude/skills/` |
| Ekspor bank soal dan perakitan sesi pretest | `implemented_local` | `agentic/export.py`, `agentic/pretest.py` |
| Import hasil ke MongoDB | `implemented_unprovisioned` | `app/ingestion/pretest_import.py`, `scripts/load_candidates_to_atlas.py` dan Atlas repository |
| Endpoint agentic di FastAPI/gateway | `target` | Belum ada route; modul dipanggil melalui CLI |
| Claude API untuk audit hasil IndoBERT | `target` | Berbeda dari Claude Code yang menjalankan ekstraksi |
| Tiga ahli dan gold | `implemented_unprovisioned` | Blind annotation, consensus/discussion/adjudication; data manusia tetap diperlukan |
| Delivery, server-scored response, CTT dan Rasch/2PL/3PL | `implemented_local` | `app/assessment`, `app/psychometrics`; gold → pilot → empirical snapshot, lihat [27](27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md) |

`implemented_local` berarti fungsi tersedia untuk batch lokal, bukan layanan produksi, endpoint publik, atau proses yang aman untuk multi-tenant.

## 2. Tiga alur yang tidak boleh dicampur

### 2.1 Pipeline agentic pretest — jalur baru yang dipilih

```text
Buku Siswa PDF + Buku Guru PDF + Prasyarat_Math.xlsx
    -> convert.py
    -> Markdown per halaman + INDEX + gambar/PNG bila perlu
    -> Claude Code skill, satu agen per bab
    -> output/pretest/<book>/babNN.json
    -> validate.py sampai tanpa ERROR
    -> export.py untuk seluruh bank soal, atau
    -> pretest.py untuk memilih 2 soal/subbab + 1 soal/bab prasyarat
```

Kode menangani operasi deterministik. Agen menangani interpretasi batas soal, stimulus, notasi dari gambar, pengerjaan mandiri, pencarian kunci guru dan pembuatan distraktor.

### 2.2 Pipeline pretest lama — masih ada, tetapi bukan jalur kanonis

```text
extractor_text.py
    -> extractor_siswa.py
    -> soal_merger.py
    -> answer_option_generator.py
    -> llm_backend.py -> Ollama qwen3:4b
```

Kode ini belum dihapus dan `scripts/review_app.py` masih membaca bentuk output lama. Ia harus diberi status `legacy/deprecated` atau dimigrasikan secara eksplisit; keberadaannya tidak berarti Ollama masih menjadi provider target arsitektur Nalar.

### 2.3 Pipeline klasifikasi v2 — fondasi terimplementasi, belum memiliki gold/model final

```text
canonical question version
    -> validasi format dan kunci
    -> IndoBERT tiga head 3 x 4 x 3
    -> Claude API confirm/revise/abstain, opsional N_claude=3
    -> tiga ahli matematika: blind pass lalu review AI
    -> pilot siswa
    -> CTT dan IRT bila layak
```

Claude Code pada 2.1 adalah alat kerja ekstraksi lokal. Claude API pada 2.3 adalah komponen runtime terkontrol. `jawaban_agen` pada file bab juga bukan suara pakar dan bukan salah satu run `N_claude`.

## 3. Kontrak `babNN.json`

Unit sumber adalah satu bab buku. Pydantic memakai `extra="forbid"` sehingga field yang tidak dikenal ditolak.

| Kelompok | Field penting | Makna |
|---|---|---|
| Identitas | `book`, `bab`, `bab_no`, `halaman_siswa`, `mode` | Ruang lingkup ekstraksi |
| Lokasi item | `id`, `subbab`, `sumber_soal`, `source_page`, `source_section`, `source_item_no` | Provenance ke Buku Siswa/Guru |
| Konten | `stimulus`, `pertanyaan`, `image_refs` | Teks yang dibutuhkan siswa untuk menjawab |
| Penyesuaian | `pertanyaan_disesuaikan`, `catatan_penyesuaian`, `notasi_dari_png`, `butuh_gambar` | Perubahan format dan risiko ekstraksi |
| Jawaban | `jawaban_benar`, `alasan_benar`, tiga `distraktor` + alasan | Candidate pilihan ganda |
| Bukti kunci | `kunci_guru`, `jawaban_agen`, `status_kunci` | Perbandingan kunci buku dengan pengerjaan agen |
| Seleksi sementara | `tingkat_kesulitan` 1–5 dan alasan | Heuristik agen untuk merakit pretest, bukan label Head 3 |
| Coverage | `dilewati` + alasan terkontrol | Soal yang sengaja tidak dipaksakan menjadi PG |

Aturan identitas saat ini memakai ID berbasis buku, bab dan halaman. Saat diimpor ke API target, ID ini disimpan sebagai `source.externalId`; server tetap membuat `questionId` dan `questionVersionId` sendiri.

## 4. Validasi mekanis dan arti status

Validator menolak file bila schema gagal, ID/posisi ganda, teks atau angka tidak cocok dengan halaman sumber, bukti kunci tidak ditemukan, status kunci tidak konsisten, opsi duplikat/senilai, gambar hilang, subbab tidak sah, atau tingkat kesulitan kosong. Warning mencakup latihan yang mungkin terlewat, panjang opsi yang mudah ditebak, serta halaman berisiko matematika yang belum dicek melalui PNG.

Status hasil `derive_status` adalah **status staging ekstraksi**, bukan lifecycle API:

| Status staging | Arti | Pemetaan target |
|---|---|---|
| `draft` | Verbatim dan kunci guru cocok dengan pengerjaan agen | `extraction_candidate_ready`; tetap belum dinilai pakar |
| `needs_review_kunci` | Kunci tidak ada atau berbeda | `answer_key_review_required`; blokir klasifikasi/pilot |
| `needs_review_soal` | Pertanyaan diubah agar menjadi PG | `content_review_required`; buat/versioning perubahan |
| `needs_image` | Gambar wajib belum tersedia | `extraction_incomplete`; blokir import kanonis |

Nama `draft` tidak boleh diterjemahkan menjadi `expert_validated`, `active`, atau “siap diberikan ke siswa”. Confidence `0.95/0.60/0.30` pada exporter adalah mapping heuristik dari `status_kunci`, bukan probabilitas kebenaran terkalibrasi.

## 5. Dua bentuk ekspor

### 5.1 `soal_pretest.json`

`export.py` menggabungkan seluruh bab yang lolos validasi, mempertahankan provenance dan `validation_result`, lalu menyeimbangkan posisi jawaban A–D secara deterministik. Ini bentuk paling dekat dengan staging import record, tetapi belum sama dengan public DTO atau MongoDB document target.

### 5.2 `soal_pretest_db.json` dan `sesi_pretest.json`

`pretest.py` memilih subset sesi secara deterministik:

- dua soal setiap subbab;
- satu soal untuk setiap bab prasyarat, dari subbab terakhir;
- prioritas `draft`, kemudian review soal, kemudian review kunci;
- soal prasyarat dipilih berdasarkan `tingkat_kesulitan` agen tertinggi;
- `_id` 24-heksadesimal berasal dari MD5 ID sumber agar ekspor ulang stabil;
- opsi A–D diacak dengan seed tetap.

`sesi_pretest.json` menyimpan susunan sesi dan audit. `soal_pretest_db.json` memakai field tabel backend lama (`soal_text`, `soal_type`, `jawaban`, `image_url[]`) dan **belum kompatibel langsung** dengan `app/db/questions_pretest.py`, yang memakai `pertanyaan_text`, `pertanyaan_type`, `correct_answer`, `image_url` string dan `subbab_id` ObjectId.

## 6. Snapshot hasil merge

Snapshot repository pada 28 September 2026:

| Metrik | Nilai |
|---|---:|
| File bab | 46 |
| Bab valid menurut `_status.json` | 45 |
| Bab gagal | 1 (`kelas7/bab06.json`) |
| Soal terekstrak | 1.254 |
| `draft` | 951 |
| `needs_review_kunci` | 109 |
| `needs_review_soal` | 170 |
| `needs_image` | 24 |
| Dokumen pada kumpulan `soal_pretest_db.json` | 251 |
| Gambar hasil ekspor | 162 |

Kelas 1–6 memiliki hasil rakitan, tetapi hasil kelas 4 tertinggal dari file bab terbarunya. Kelas 7 dan 10 belum mempunyai rakitan DB. Kelas 8–12 belum lengkap. Angka ini adalah snapshot artefak, bukan metrik akurasi atau coverage kurikulum final.

## 7. Kesenjangan reproduksibilitas

PDF sumber, Markdown hasil konversi, `Prasyarat_Math.xlsx` dan tabel database berada pada path yang diabaikan Git dan tidak tersedia pada workspace hasil pull. Karena itu file output dapat dibaca dan tes unit dapat berjalan, tetapi validasi nyata tidak dapat diulang sampai aset tersebut dipasang melalui storage/manifest yang disepakati.

Dependensi juga perlu diselaraskan:

- `pymupdf4llm` sudah tercantum di `requirements.txt`, tetapi environment lokal perlu di-install ulang;
- `openpyxl` digunakan `kurikulum.py` tetapi belum tercantum;
- `beanie` digunakan model MongoDB tetapi belum tercantum;
- skill memakai `venv/Scripts/python`, sedangkan workspace saat audit memakai `.venv/Scripts/python`.

## 8. Adapter staging ke canonical API

Import yang aman tidak memasukkan JSON lama langsung ke MongoDB. Gunakan adapter berikut:

```text
babNN.json yang lolos validator
    -> verifikasi manifest sumber + hash PDF/halaman
    -> map ID sumber ke source.externalId
    -> map stimulus + pertanyaan ke content.stem
    -> map opsi ke content.options dan jawaban ke private answerSpec
    -> salin source page/section/image sebagai provenance
    -> map status staging ke extraction/content review flags
    -> buat question identity + immutable question version
    -> jalankan canonical format/answer gate
    -> baru submit ke IndoBERT
```

Field yang tidak boleh dipromosikan langsung:

- `tingkat_kesulitan` 1–5 tidak menjadi `intendedDifficulty` tanpa rubrik/pakar;
- `status_kunci=cocok` tidak menjadi validasi ahli;
- `jawaban_agen` tidak menjadi human gold;
- alasan distraktor agen tetap candidate sampai ditinjau;
- `_id` MD5 ekspor bukan public `questionId`;
- `subbab_id` berupa nama harus di-resolve ke entitas kurikulum yang stabil.

## 9. Acceptance gate sebelum integrasi produksi

1. Tetapkan pipeline agentic sebagai jalur kanonis dan tandai/hapus jalur Ollama lama.
2. Sediakan manifest aset sumber dengan checksum, lisensi, kelas, jenis buku dan versi.
3. Selaraskan `requirements.txt`, path virtual environment dan setup lintas mesin.
4. Putuskan satu schema staging dan satu adapter ke `QuestionVersion`; jangan mempertahankan dua format DB yang berbeda.
5. Regenerasi seluruh `soal_pretest_db.json`/`sesi_pretest.json` dari bab valid dan tolak rakitan yang stale.
6. Tambahkan integration test terhadap buku fixture mini, bukan hanya fixture teks sintetis.
7. Tambahkan seeder/upsert MongoDB dengan dry-run, conflict report dan idempotency.
8. Hubungkan hasil import ke format gate, IndoBERT tiga head, Claude API dan tiga ahli sesuai dokumen 04–05.
9. Jangan membuka output kepada siswa sebelum delivery snapshot dan server-side scoring pada dokumen 06–08 tersedia.
