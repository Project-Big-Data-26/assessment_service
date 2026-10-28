# Validasi exercise dengan DeepSeek

Alternatif ini tidak diaktifkan. Provider exercise saat ini disiapkan memakai
[Groq](41_GROQ_EXERCISE_VALIDATION.md), sesuai perubahan pilihan pengguna.

API DeepSeek **berbayar berdasarkan token**. Akses aplikasi chat tidak menjadi
saldo API. Lihat [tarif resmi](https://api-docs.deepseek.com/quick_start/pricing/?model_version=DeepSeek-V4-Pro-0813).
Integrasi tidak membutuhkan SDK OpenAI; transport memakai `httpx` yang sudah ada.

## Menyiapkan akun dan key

1. Buka [platform DeepSeek](https://platform.deepseek.com), masuk/buat akun,
   periksa saldo/kredit API, dan buat API key.
2. Isi key di `.env` lokal, bukan di chat atau file dokumentasi:

   ```dotenv
   EXERCISE_LLM_PROVIDER=deepseek
   DEEPSEEK_API_KEY=isi-key-api-deepseek
   DEEPSEEK_MODEL=deepseek-flash
   DEEPSEEK_LIVE_ENABLED=false
   DEEPSEEK_TIMEOUT_SECONDS=120
   DEEPSEEK_MAX_OUTPUT_TOKENS=4096
   DEEPSEEK_REASONING_EFFORT=low
   ```

   Key Gemini tidak bisa dipakai untuk DeepSeek. `LLM_PROVIDER` untuk route
   Gemini lain tetap terpisah; runner exercise memakai provider pada konfigurasi
   nightly dan `EXERCISE_LLM_PROVIDER` untuk CLI manual.
3. Cek konfigurasi tanpa panggilan API:

   ```powershell
   .\.venv\Scripts\python.exe -X utf8 scripts/check_deepseek_connection.py
   .\.venv\Scripts\python.exe -X utf8 scripts/nightly_pipeline.py status
   ```

4. Setelah menyetujui biaya API, ubah `DEEPSEEK_LIVE_ENABLED=true`. Uji satu
   permintaan berbayar yang memakai schema validasi sebenarnya:

   ```powershell
   .\.venv\Scripts\python.exe -X utf8 scripts/check_deepseek_connection.py --execute
   ```

   Hanya `passed=true` menandakan respons lolos schema lokal. Probe bukan soal
   database dan tidak dimasukkan ke hasil exercise/training.
5. Lanjutkan kelas 8 sesuai batas anggaran konfigurasi:

   ```powershell
   .\.venv\Scripts\python.exe -X utf8 scripts/nightly_pipeline.py run --execute
   ```

## Checkpoint dan hasil lama

`scripts/validate_exercise_batch.py seed --provider deepseek --classes kelas8 --runs 1`
menyiapkan migrasi offline. Hanya keputusan Gemini yang sudah lengkap disalin.
Checkpoint dan laporan Gemini diarsipkan dengan SHA-256; checkpoint lama tetap
utuh. Sebanyak 89 keputusan kelas 8 yang sudah selesai dapat dipertahankan,
dan sisanya dikerjakan DeepSeek N=1. N=3 lama tetap memakai tiga run aslinya.

| Lokasi | Fungsi |
|---|---|
| `runs/exercise_validation/batch01/kelas8_exercise_batch01/` | Checkpoint Gemini asli. |
| `runs/exercise_validation/deepseek/batch01/kelas8_exercise_batch01/` | Target checkpoint DeepSeek dan arsip migrasi. |
| `output/exercise/kelas8/batch01/hasil_validasi/validation_results.json` | Format database tetap sama, seluruh ID sumber ada. |
| `hasil_validasi/validation_results_meta.json` | `validation_provider` dan `validation_model` mencatat asal tiap hasil. |
| `hasil_validasi/bukti_validasi/decision_audit.json` | Bukti, provider/model, hash dan keputusan per soal. |
| `runs/nightly_pipeline/deepseek_connection_check.json` | Hasil pemeriksaan konfigurasi/probe yang tidak menyimpan key. |

Provider/model asli pada keputusan Gemini tidak diganti menjadi DeepSeek.
Keputusan lama yang berubah atau arsip yang tidak cocok ditolak. Prompt/rubrik
bersama mempertahankan ID versi historis berawalan `gemini-`; asal model selalu
mengikuti kolom provider/model dan arsip bukti, bukan nama versi prompt.

DeepSeek diminta memberi JSON melalui `response_format=json_object`; JSON tetap
divalidasi oleh `SilverLabelOutput`, termasuk evidence span, profil difficulty,
kunci dan solusi. Respons kosong, terpotong, atau tidak sesuai schema tetap
gagal/draft. `reasoning_content` tidak disimpan; hanya ringkasan keputusan dan
jumlah token yang dicatat. Harga dapat mencakup reasoning tokens.

Kelas 8 tetap satu worker, N=1, dengan balancing operasional 30/40/30 per bab
setelah seluruh batch lengkap. IndoBERT tetap diagnostik dan berada di luar
cakupan SMP; migrasi ini tidak melakukan fine-tuning. Aturan stop 503, retry 504,
blocker key/saldo/kuota, dan batas anggaran tetap berlaku. Saldo kurang HTTP 402
menghentikan panggilan dan menghasilkan laporan, bukan percobaan tanpa batas.
