# Nalar — ekstraksi dan validasi soal matematika

Repo ini menyediakan FastAPI untuk ekstraksi soal, klasifikasi legacy, dan fondasi riset IndoBERT 3×4×3. Implementasi v2 mencakup import candidate, penyimpanan Atlas, anotasi blind, konsensus/adjudikasi, snapshot dataset, baseline, LoRA training, kalibrasi, artefak, dan API advisory.

Hasil riset belum boleh diklaim: gold manusia, deployment cloud, dan artefak model final belum ada sampai intervensi eksternal diselesaikan.

## Menjalankan lokal

Prasyarat: Python 3.12 dan dependensi dalam [requirements.txt](requirements.txt).

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --port 8000
```

Buka `http://127.0.0.1:8000/docs`. Route legacy tetap berada pada `/v1`. Route baru adalah:

- `POST /v2/classify`;
- `GET /v2/model-info`;
- `GET /v2/health/ready`;
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

Claude N=3, delivery siswa, CTT, dan IRT berada di fase berikutnya dan tidak diaktifkan oleh implementasi ini. Urutan operasional dan seluruh perintah ada di [runbook IndoBERT v2](API_DOCUMENTATION/22_INDOBERT_V2_IMPLEMENTATION_RUNBOOK.md).

## Tes

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```
