# Validasi N=1 dengan pergantian Gemini dan Groq

Runner mendukung prioritas provider di `configs/nightly_pipeline.json`:

```json
{
  "provider": "gemini",
  "fallbackProviders": ["groq"],
  "stopOn503": false,
  "fallbackOn503": true
}
```

Field di atas bagian dari konfigurasi lengkap yang sudah ada. Scope saat ini
tetap `kelas8/batch01`. Urutan ini tidak menggabungkan suara dua model untuk
satu soal: setiap soal baru cukup satu hasil valid (N=1). Jika hasil pertama
gagal schema, retry dibatasi dan soal tetap draft bila belum berhasil.

## Key dan pemeriksaan

Simpan key hanya di `.env` lokal dengan nama `GEMINI_API_KEY` dan `GROQ_API_KEY`.
Gunakan model yang tersedia untuk masing-masing akun. Jalankan satu probe schema
per provider dengan soal diagnostik kecil:

```powershell
.\.venv\Scripts\python.exe -X utf8 scripts/check_exercise_providers.py --providers gemini groq --execute
```

`--execute` mengizinkan permintaan diagnostik, termasuk ketika live mode massal
masih false. Output hanya menampilkan status/usage, tidak menampilkan key atau
isi respons. Probe juga memeriksa kunci soal uji. HTTP 503 menghentikan probe
sebelum mencoba provider berikutnya. JSON hasil ada di
`runs/nightly_pipeline/exercise_provider_connection_check.json`.

Aktifkan provider yang sudah berhasil diuji melalui `GEMINI_LIVE_ENABLED=true`
atau `GROQ_LIVE_ENABLED=true`. Provider tanpa key atau dengan live mode false
dilewati sebelum membuat permintaan. Probe 27 Oktober 2026: Groq berhasil,
Gemini `gemini-3.8-flash` mengembalikan 504. Uji berikutnya dengan
`gemini-3.1-flash-lite` berhasil dan model itulah yang diaktifkan untuk run ini.
Hasil ini bukan status layanan permanen.

Pada kelanjutan sesi, model 3.1 mengalami 503 berulang. Probe
`gemini-3-flash-preview` berhasil dan model ini dipilih untuk melanjutkan batch.
Model aktual tiap keputusan tetap tersimpan dalam metadata; mengganti model
tidak mengulang atau mengganti label soal yang sudah selesai.

`EXERCISE_LLM_PROVIDER` memilih provider untuk CLI manual. Urutan scheduler
ditentukan konfigurasi JSON di atas. `EXERCISE_CHECKPOINT_NAMESPACE=failover`
memilih checkpoint bersama untuk CLI manual; berikan `--provider` sesuai provider
aktif yang tercatat pada checkpoint untuk perintah `progress`/`full`.

## Kapan berpindah atau berhenti

- HTTP 429 atau sinyal kuota harian: simpan semua hasil, lanjut ke provider
  berikutnya yang diaktifkan, hanya untuk soal yang belum selesai.
- HTTP 503 dengan `fallbackOn503=true`: hentikan panggilan ke provider tersebut
  dan lanjut ke provider cadangan. `stopOn503=true` menjadi batas per provider,
  bukan penghentian seluruh alur. Tanpa opsi baru ini, kebijakan lama tetap berlaku.
  Konfigurasi aktif memakai `stopOn503=false`: satu respons gagal tetap draft dan
  soal lain boleh dilanjutkan; tiga kegagalan layanan berturut-turut memicu
  pemulihan/pergantian provider. Hasil valid mereset hitungan kegagalan berturut-turut.
- Error autentikasi/izin/konfigurasi setelah panggilan live: berhenti agar masalah
  tidak tersembunyi sebagai kegagalan kuota.
- HTTP 504/error sementara mengikuti retry terbatas yang sudah ada.
- Semua provider terkena kuota, tidak ada provider aktif, atau anggaran run habis:
  berhenti dengan checkpoint. Provider yang terkena kuota tidak diulang dalam run
  yang sama. Provider yang gagal sementara boleh dicoba ulang dengan jeda
  `providerRetryDelaysSeconds` (15, 30, 60 detik), memakai anggaran panggilan bersama.
  Batas retry dihitung untuk putaran berturut-turut tanpa soal baru yang selesai.
  Jika masih ada hasil valid baru, penghitung pemulihan direset agar proses tetap
  melanjutkan pekerjaan. Anggaran API keseluruhan tetap berlaku.

HTTP 429 sendiri belum membedakan batas harian dan batas sementara. Mengganti
key dalam organisasi/proyek yang sama tidak menjamin tambahan kuota.

Mulai/resume:

```powershell
.\.venv\Scripts\python.exe -X utf8 scripts/nightly_pipeline.py run --execute
```

Scheduler pukul 01.00 WIB memakai konfigurasi yang sama. Tetap satu worker;
jeda Groq mengikuti `GROQ_REQUEST_PAUSE_SECONDS` (default 65 detik).
Jeda Gemini mengikuti `GEMINI_REQUEST_PAUSE_SECONDS`; sesi ini memakai 15 detik.
Anggaran API dibagi sepanjang perpindahan, bukan direset per provider.

## Bukti dan berkas hasil

Checkpoint bersama:
`runs/exercise_validation/failover/batch01/kelas8_exercise_batch01/silver_labels.json`.
Checkpoint lama Gemini dan Groq tetap utuh. Persiapan namespace memilih checkpoint
lama dengan keputusan lengkap terbanyak, lalu menyimpan salinan bukti ber-checksum.
Hanya keputusan lengkap yang dibawa; kegagalan lama tetap ada di arsip.

Sebelum berpindah, checkpoint aktif diarsipkan. Record yang dibawa tetap mencatat
provider/model asli, termasuk hasil Gemini dengan model lama. Keputusan tersebut
diverifikasi terhadap arsip dan tidak dihitung ulang. `providerFailover.transitions`
mencatat setiap pergantian, model, panggilan sebelumnya, dan asal bukti.

Hasil tetap di `output/exercise/kelas8/batch01/hasil_validasi/`, dengan schema
database yang sama. `validation_results_meta.json` menyimpan provider/model per
soal. `export_status.json` membedakan keputusan lengkap dan draft.
IndoBERT tetap diagnostik sesuai scope; pergantian provider tidak melatih model
atau mengarang confidence. Label AI asli dan pembagian operasional tetap terpisah.
