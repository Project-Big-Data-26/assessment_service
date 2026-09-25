# Nalar Question Intelligence

Layanan AI untuk ekstraksi sumber soal dan klasifikasi multi-task. Sistem membedakan dengan tegas antara prediksi model, label manusia, dan difficulty empiris.

## Status implementasi

- API FastAPI: health, informasi model, klasifikasi, dan ekstraksi sumber.
- OCR gambar serta fallback OCR untuk halaman PDF tanpa text layer memakai Tesseract (`ind+eng`).
- Parser JSON, CSV, TXT, dan TEX; kandidat LaTeX dipertahankan untuk direview.
- Baseline aturan transparan tersedia agar integrasi dapat diuji tanpa bobot model.
- Arsitektur dan training IndoBERT tiga head sudah tersedia untuk Bloom C1–C6, dimensi pengetahuan 4 kelas, dan intended difficulty 3 kelas.
- Artefak IndoBERT baru dipakai otomatis jika `models/indobert-multitask-v1/model.pt` dan `manifest.json` tersedia.
- Seeder 24 soal mencakup matriks 6 × 4, tetapi **bukan gold dataset**.

## Setup Windows

Setup otomatis (Python dependencies, PyMuPDF, Tesseract, serta data bahasa `ind+eng`):

```powershell
powershell -ExecutionPolicy Bypass -File scripts\setup_windows.ps1
```

Atau setup Python manual:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Tesseract harus tersedia di sistem operasi untuk OCR lokal. Dockerfile proyek sudah memasang paket Tesseract bahasa Indonesia dan Inggris.

## Ekstraksi PDF langsung

Taruh PDF di `data/raw/pdf`, lalu jalankan:

```powershell
.\.venv\Scripts\python.exe -m app.extraction data\raw\pdf\soal.pdf
```

Hasil JSON ditulis ke `data/processed/soal.extracted.json`. Untuk memproses seluruh isi direktori:

```powershell
.\.venv\Scripts\python.exe -m app.extraction data\raw\pdf `
  --output data\processed\pdf-batch.json
```

Periksa kesiapan PyMuPDF/OCR melalui `GET /v1/extraction-info`. Alur lengkap, struktur output, konfigurasi, dan aturan human review dijelaskan di [`EXTRACTION_FLOW.md`](EXTRACTION_FLOW.md).

## Data dan training

Masukkan sumber ke [`data/raw/`](data/raw/README.md). Setelah dua review independen dan adjudikasi selesai, ekspor label yang berstatus `approved`, lalu jalankan:

```powershell
.\.venv\Scripts\python.exe -m app.training.train `
  --dataset data\raw\json\questions-approved.json `
  --output-dir models\indobert-multitask-v1
```

Minimal 60 baris hanya guard teknis, bukan jaminan mutu. Dataset nyata perlu representatif di setiap sel label, bebas kebocoran duplikat, dan mempunyai validation/test set yang dikunci. Gunakan `--allow-small-demo` hanya untuk smoke test; artefaknya ditandai `demo_only`.

Detail arsitektur ada di [`MODEL_SPECIFICATION.md`](MODEL_SPECIFICATION.md).
