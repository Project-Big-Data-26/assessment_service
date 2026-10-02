# Nalar — ekstraksi dan validasi soal matematika

Repo ini menyediakan FastAPI untuk ekstraksi soal, klasifikasi legacy, riset IndoBERT 3×4×3 grade-aware ordinal, serta pilot server-scored dan analisis CTT/IRT. Implementasi mencakup import candidate, Atlas, anotasi blind, konsensus/adjudikasi, snapshot dataset, LoRA training, kalibrasi, delivery fixed-form, SQLite response events dan snapshot empiris immutable.

Hasil riset belum boleh diklaim: gold manusia, deployment cloud, dan artefak model final belum ada sampai intervensi eksternal diselesaikan.

Hasil validasi kelas 1-6 tersedia di [indeks hasil validasi](output/pretest/README.md). Gunakan `output/pretest/kelasN/hasil_validasi/` untuk laporan dan label final tiap kelas; checkpoint serta audit final berada di subfolder `bukti_validasi/`.

## Menjalankan lokal

Prasyarat: Python 3.12 dan dependensi dalam [requirements.txt](requirements.txt).

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --env-file .env --port 8000
```

Buka `http://127.0.0.1:8000/docs`. Route legacy tetap berada pada `/v1`. Route baru adalah:

- `POST /v2/classify`;
- `GET /v2/model-info`;
- `GET /v2/health/ready`;
- `GET /v2/llm-info` dan `/v2/psychometrics-info`;
- delivery/respons `/api/v1/assessments`, `/api/v1/sessions`, `/api/v1/responses`;
- analisis internal `/api/v1/internal/psychometrics`;
- UI/API tertutup `/internal/v2`.

Tanpa artefak terverifikasi, classify/readiness v2 sengaja menjawab HTTP 503 dan tidak memakai rules sebagai fallback.

## Arsitektur fase IndoBERT

Candidate dari `babNN.json` diperiksa kontennya, lalu tiga ahli memberi label blind pada:

- domain kognitif matematika `knowing | applying | reasoning`;
- dimensi pengetahuan `factual | conceptual | procedural | metacognitive`;
- intended difficulty `Easy | Medium | Hard`.

KKO hanya fitur eksperimen. Konflik yang tidak selesai masuk ahli senior keempat. Training v2 memakai snapshot gold yang terkunci dan LoRA pada IndoBERT.

Kode [indobert.py](app/classification/indobert.py) dan [train.py](app/training/train.py) tetap legacy C1–C6 khusus `/v1`. Implementasi baru berada di `app/classification/v2`, `app/training/v2`, `app/annotation`, dan `app/ingestion`. Output v2 tidak menetapkan gold atau publish otomatis; `reviewRequired` selalu benar pada fase ini.

## Atlas dan fase berikutnya

[.env.example](.env.example) memuat nama variabel Atlas, session, allowed host/origin, artefak, dan private object storage. Repository memakai satu `AsyncMongoClient` sepanjang lifecycle aplikasi. Jangan commit `.env`, token, atau URI berkredensial.

Gemini blind N=3 tersedia untuk silver advisory sebelum comparison IndoBERT. Pipeline baru memakai Head 3 ordinal + grade embedding; Claude API tetap target. Delivery single-choice, CTT batch, Rasch/2PL/3PL dan review empiris tersedia. Gold manusia, respons siswa memadai dan asumsi yang didukung tetap diperlukan untuk pilot nyata.

Jalankan IRT sekarang pada simulasi eksplisit, tanpa provider/database:

```powershell
.\.venv\Scripts\python.exe scripts\psychometrics.py demo --model rasch --output output\psychometrics\demo-rasch-v1.json
```

Demo juga mendukung `--model 2pl` dan `--model 3pl`. Semua output menolak overwrite. Perintah pilot/analisis nyata ada di [runbook CTT/IRT](API_DOCUMENTATION/27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md), training pada [runbook IndoBERT v2](API_DOCUMENTATION/22_INDOBERT_V2_IMPLEMENTATION_RUNBOOK.md). [Endpoint](API_DOCUMENTATION/12_ENDPOINT_MASTER_REFERENCE.md) dan [schema aktual](API_DOCUMENTATION/schemas/implemented-api.schema.json) dihasilkan dari kode melalui `scripts/export_api_contracts.py`.

## Tes

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```
