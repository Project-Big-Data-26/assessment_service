# Validasi exercise memakai Groq

Untuk prioritas Gemini dan perpindahan otomatis ke Groq, gunakan
[panduan failover](42_GEMINI_GROQ_FAILOVER.md). Saat mode tersebut aktif,
checkpoint bersama berada di namespace `failover`; folder hasil tetap sama.

Provider exercise dipilih melalui `EXERCISE_LLM_PROVIDER=groq` dan
`configs/nightly_pipeline.json` (`provider: groq`). Provider rute aplikasi lain
tetap mengikuti `LLM_PROVIDER`. Fokus sementara: `kelas8/batch01`, N=1,
satu worker, jeda 65 detik antarsoal. DeepSeek tidak diaktifkan.

## Akun dan kuota

Groq menyediakan Free tier dengan batas permintaan dan token. Dokumentasi
[rate limits](https://console.groq.com/docs/rate-limits) mencantumkan
`openai/gpt-oss-120b`: 30 RPM, 1.000 RPD, 8.000 TPM, dan 200.000 TPD pada Free.
Periksa batas aktual di console akun. Penyelesaian satu kelas dapat memerlukan
beberapa hari karena input, output, dan reasoning memakai kuota token.
Developer tier berbayar; kode ini tidak dapat memastikan paket akun pengguna.
Lihat [billing](https://console.groq.com/docs/billing-faqs).

1. Buat akun Groq dan key melalui <https://console.groq.com/keys>.
2. Pastikan akun memakai Free jika hanya ingin kuota gratis.
3. Isi `.env` lokal, jangan kirim key melalui chat:

   ```dotenv
   EXERCISE_LLM_PROVIDER=groq
   GROQ_API_KEY=isi-key-pribadi-di-sini
   GROQ_MODEL=openai/gpt-oss-120b
   GROQ_API_BASE_URL=https://api.groq.com/openai/v1
   GROQ_LIVE_ENABLED=true
   GROQ_TIMEOUT_SECONDS=120
   GROQ_MAX_OUTPUT_TOKENS=4096
   GROQ_REASONING_EFFORT=low
   GROQ_REQUEST_PAUSE_SECONDS=65
   ```

`GROQ_LIVE_ENABLED` bawaan `false`. API key Gemini/DeepSeek tidak bisa digunakan
sebagai key Groq. Nama model `openai/gpt-oss-120b` di sini dilayani oleh Groq;
tidak memerlukan API key OpenAI.

## Pemeriksaan dan resume

Periksa konfigurasi tanpa jaringan:

```powershell
.\.venv\Scripts\python.exe -X utf8 scripts/check_groq_connection.py
```

Uji satu permintaan dengan soal diagnostik kecil setelah key dan live mode siap:

```powershell
.\.venv\Scripts\python.exe -X utf8 scripts/check_groq_connection.py --execute
```

Uji ini memakai kuota akun dan memeriksa schema; hasilnya bukan evaluasi akurasi
seluruh bank. Setelah sukses, beri jeda setidaknya 65 detik sebelum resume:

```powershell
.\.venv\Scripts\python.exe -X utf8 scripts/nightly_pipeline.py run --execute
```

Runner terjadwal pukul 01.00 WIB membaca konfigurasi provider yang sama.
Tanpa key/live mode, runner mencatat status menunggu dengan nol API call.
Pada mode provider tunggal, HTTP 503 menghentikan run; mode failover mengikuti
pengaturan `fallbackOn503` di panduan 42. HTTP 504/error sementara mencoba ulang
secara terbatas lalu meninggalkan draft. HTTP 429, kegagalan autentikasi, dan
batas anggaran menghentikan run; lanjutkan setelah penyebabnya teratasi.

## Bukti dan keluaran

Checkpoint Groq terpisah:
`runs/exercise_validation/groq/batch01/kelas8_exercise_batch01/silver_labels.json`.
Perintah persiapan offline menyalin hanya keputusan Gemini yang sudah lengkap:

```powershell
.\.venv\Scripts\python.exe -X utf8 scripts/validate_exercise_batch.py seed --provider groq --classes kelas8 --runs 1
.\.venv\Scripts\python.exe -X utf8 scripts/validate_exercise_batch.py progress --provider groq --classes kelas8 --runs 1
```

Sumber dan checkpoint Gemini asli tidak ditimpa. Arsip ber-checksum menyimpan
bukti asal; metadata per soal mencatat provider/model yang benar. Runner hanya
memanggil Groq untuk soal yang belum selesai. Keluaran tetap di
`output/exercise/kelas8/batch01/hasil_validasi/`, termasuk `validation_results.json`.

Groq memakai JSON object mode, rubric yang sama, dan validasi schema lokal;
JSON valid belum membuktikan jawaban matematika benar. Reasoning internal tidak
disimpan. Uji kualitas pada sampel sebelum mengandalkan hasil penuh.
IndoBERT tetap diagnostik sesuai scope artifact; artifact di luar scope kelas 8
tidak dipakai sebagai bukti confidence. Proses ini tidak melakukan fine-tuning
IndoBERT. Pembagian operasional kesulitan tetap dicatat terpisah dari label AI
asli dan tidak mengarang confidence untuk mengejar proporsi.

Rujukan: [quickstart](https://console.groq.com/docs/quickstart),
[JSON output](https://console.groq.com/docs/structured-outputs),
[reasoning](https://console.groq.com/docs/reasoning).
