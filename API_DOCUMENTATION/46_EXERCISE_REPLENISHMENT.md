# Penambalan bank latihan berdasarkan kekurangan level

Instruksi terbaru pengguna mengizinkan penambahan kelas 5-12 langsung ke
`batch01`, dengan soal lama dipertahankan. Jalur ini memakai backup dan manifest
penambahan terpisah; bukan menimpa isi batch. Lihat
[laporan generate 2.028 kandidat](47_CODEX_BATCH01_REPLENISHMENT.md).

Gunakan `scripts/plan_exercise_replenishment.py` untuk membangun antrean dari
ekspor validasi resmi dan katalog pada laporan pengguna:

```powershell
.\.venv\Scripts\python.exe -B scripts/plan_exercise_replenishment.py
```

Keluaran:

- `runs/exercise_replenishment/plan.json`: antrean level, kandidat lama, status
  kesiapan sumber, dan hash berkas yang digunakan saat menghitung.
- `runs/exercise_replenishment/plan.md`: rincian yang bisa dibaca per kelas,
  bab, subbab, dan level.

Planner tidak mengakses LLM, tidak mengubah database atau batch, dan tidak
memberikan persetujuan validasi. Antrean ini bukan `generation_plan.json` yang
bisa langsung diberikan kepada generator lama. Acuan soal tervalidasi atau
sumber/halaman buku serta alokasi pilot diverifikasi sebelum membuat manifest.
Jalankan planner ulang setelah hasil validasi atau sumber berubah.

## Urutan penanganan

1. Selesaikan kandidat **batch lama** yang belum selesai divalidasi, menggunakan
   checkpoint yang sudah ada. Jangan mengulang hasil sukses.
2. Hitung ulang jumlah latihan active per level. Jumlah target awal kandidat
   tidak boleh dianggap sama dengan level hasil validasi.
3. Untuk variasi, gunakan soal teks active berlabel dari kelas, bab, dan subbab
   yang sama. Utamakan exercise; pretest active menjadi acuan cadangan jika
   exercise belum tersedia. Mode ini tidak memerlukan PDF untuk materi yang
   sudah tercakup pada acuan tersebut.
4. Prioritaskan kekurangan kecil pada bank kelas 5-12 yang sudah digunakan,
   lalu proyek visual kelas 1-4. Antrean mengurutkan kandidat lama lebih dahulu,
   kemudian bank kelas 5 ke atas, kemudian kelas 1-4.
5. Buat kandidat di batch baru atau jalur append-only `batch01` yang telah
   diminta pengguna, khusus
   level yang kurang. Distribusi global 30/40/30 tidak boleh memaksa penambahan
   level yang sebenarnya sudah cukup atau mengganti label soal lama.
6. Untuk **batch baru**, pertahankan generate dahulu dan validasi belakangan.
   Persetujuan validasi tetap memakai manifest hash dan instruksi pengguna
   `MULAI VALIDASI`, sesuai `PROMPT_CLAUDE_EXERCISE_VISUAL.md`.
7. Lanjutkan bertahap berdasarkan hasil pilot dan audit ulang sampai tiap
   level/subbab memenuhi batas. Penerapan database dilakukan lewat rencana
   pemetaan yang sudah diperiksa, bukan lewat pencocokan nama global.

## Kandidat lama dan soal inactive

`existing_pending` memuat ID soal lama tanpa label final. Kandidat tetap
dihitung satu kali walaupun dapat membantu salah satu dari tiga level.
`pending_credit_towards_active` selalu nol sampai hasil validasi sebenarnya
tersedia. Bila suatu subbab masih memiliki kandidat ini, seluruh level yang
kurang ditandai `await_existing_validation`; kekurangannya tidak dikurangi
secara spekulatif.

`inactive_review` memuat soal berlabel yang ditahan. Itu bukan kandidat yang
boleh otomatis dipublikasikan. Alasan penolakan perlu diperiksa; perbaikan
konten akan memerlukan validasi lagi dan tidak boleh merusak riwayat versi.

## Kesiapan generate

Mode generator berbasis buku memerlukan:

- `data/bab_prasyarat/Prasyarat_Math.xlsx`.
- PDF buku siswa menurut konvensi `data/sd`, `data/smp`, atau `data/sma`.
- `data/processed/pretest_md/<kelas>/siswa/index.json` dan halaman `pNNNN.md`.
- Provider generator yang dikonfigurasi; pipeline visual saat ini menggunakan
  adapter 9Router, terpisah dari Gemini validator.

`ready_for_reference_plan` berarti tersedia acuan teks tervalidasi di kelas/bab/
subbab yang tepat. ID acuan dan jumlah acuan pada level yang sama tercantum pada
setiap job. Label acuan tidak otomatis menjadi label kandidat; mengganti angka
saja tidak otomatis meningkatkan kesulitan. Acuan bergambar tidak dipakai tanpa
gambar melalui mode teks ini.

`blocked_sources` berarti tidak tersedia acuan teks tervalidasi maupun sumber
buku lengkap. `ready_for_generation_plan`
hanya berarti pemeriksaan sumber umum lolos, bukan bukti semua halaman subbab
atau konfigurasi API siap. Planner tidak membuat kurikulum pengganti dari
tebakan dan tidak mengisi kekurangan dengan soal tanpa acuan.

## Pilot dari acuan tervalidasi

```powershell
.\.venv\Scripts\python.exe -B scripts/generate_reference_factor_pilot.py --batch 2
```

Adapter pertama ini khusus membuat **3 kandidat teks Faktor kelas 5 Bab 2 C**,
bukan generator otomatis seluruh kelas. Angka dan konteks bervariasi; acuan
active dan metadata asal dibekukan dalam `generation_plan.json`. Jawaban
usulan diperiksa lewat enumerasi matematika, opsi diperiksa agar berbeda,
dan stem diperiksa terhadap soal kelas yang sudah ada.

Output ada di `output/exercise/kelas5/batch02/`, termasuk `PREVIEW.md`, master,
metadata, state dan manifest. Mode ini tidak memakai API eksternal. Hasilnya
berstatus inactive, label final null, dan validation_pending. Kesulitan hard
adalah target, bukan hasil validasi. Pemeriksaan lokal bukan validasi AI.

Batch tujuan harus baru; pemanggilan ulang ke batch berisi ditolak. Exporter
lama juga menolak menimpa batch acuan ini. Validator standar bisa menerima
master tersebut, tetapi tetap diblokir oleh persetujuan manifest sampai pengguna
meminta `MULAI VALIDASI`. Tidak ada marker yang memicu nightly otomatis.

Planner membaca kandidat baru dari manifest lengkap yang hash-nya masih valid.
`await_new_batch_validation` mencegah generate ulang pada subbab terkait;
kandidat ini belum mengurangi kuota aktif dan tidak memberi izin validasi.

Lihat [audit/import relasi](45_QUESTION_RELATION_REPAIR.md) dan
[prompt workflow visual](../PROMPT_CLAUDE_EXERCISE_VISUAL.md).
