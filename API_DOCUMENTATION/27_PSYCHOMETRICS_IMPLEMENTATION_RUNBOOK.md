# Runbook Operasional CTT, IRT dan Pilot

Pembaruan 2 Oktober 2026 menambahkan analisis matriks CTT/Rasch/2PL/3PL, delivery fixed-form, scoring server, snapshot immutable dan keputusan empiris ahli. Semua keluaran analisis tetap research/advisory. Perubahan ini tidak mempromosikan model IndoBERT atau mengubah gold otomatis.

## 1. Menjalankan IRT sekarang tanpa database atau provider

```powershell
.\.venv\Scripts\python.exe scripts\psychometrics.py demo --model rasch --output output\psychometrics\demo-rasch-v1.json
.\.venv\Scripts\python.exe scripts\psychometrics.py demo --model 2pl --output output\psychometrics\demo-2pl-v1.json
.\.venv\Scripts\python.exe scripts\psychometrics.py demo --model 3pl --output output\psychometrics\demo-3pl-v1.json
```

Demo menghasilkan data **sintetis berlabel eksplisit**, parameter pembangkit, matriks dan hasil analisis. Tidak ada token LLM, upload, gold palsu atau response event siswa yang dibuat. Pilih path versi baru untuk setiap run; output menolak overwrite. Default: Rasch 180×12, 2PL 400×16, 3PL 1200×24. Jika sample/gate gagal, hasil tetap disimpan dengan status menunggu.

Data penelitian nyata dapat dianalisis dari JSON `MatrixAnalysisInput`:

```powershell
.\.venv\Scripts\python.exe scripts\psychometrics.py analyze --input data\local\responses-matrix-v1.json --output output\psychometrics\analysis-v1.json
```

Gunakan `dataOrigin=external_scored`. Matriks harus sudah dinilai oleh sistem sumber terpercaya, diikat ke versi/populasi/grade, tanpa identitas langsung. Lengkapi `assumptionReview` dengan bukti yang benar-benar ditinjau. Tanpa review, CTT tetap dihitung dan IRT tidak fit. `dataOrigin=server_scored` hanya digunakan aggregator event pilot.

## 2. Menjalankan API

```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --env-file .env --port 8000
```

Swagger: `http://127.0.0.1:8000/docs`; OpenAPI: `/openapi.json`. `--env-file` memastikan konfigurasi assessment/Atlas/auth dibaca sebelum module import. Isi hanya `.env` privat, mengikuti [template](../.env.example):

- `ASSESSMENT_DB_PATH=data/local/assessments.sqlite3`;
- `PSYCHOMETRICS_POLICY_PATH=configs/psychometrics_policy.json`;
- `PSYCHOMETRICS_API_TOKEN`: token acak ≥32 karakter untuk operator/service;
- `ASSESSMENT_SUBJECT_SECRET`: opsional, HMAC key stabil. Jika kosong, store menyimpan random key sendiri;
- `MONGODB_URI`, `MONGODB_DATABASE`, `SESSION_SECRET`: diperlukan untuk jalur anotasi/gold MongoDB dan keputusan ahli melalui cookie.

Path SQLite sama harus digunakan API dan semua CLI. Setelah database dibuat, penggantian HMAC key ditolak agar identitas pseudonim tidak terpecah tanpa migrasi. Default SQLite adalah backend pilot lokal satu host; deployment multi-host memerlukan shared transactional backend atau migrasi repository. Respons/estimasi individual bukan artefak untuk di-commit atau dibagikan ke publik.

`GET /v2/psychometrics-info` memeriksa fitur/policy/storage lokal tanpa kontak provider. `GET /api/v1/capabilities` melaporkan kontrak aktif. Kesiapan model IndoBERT tetap terpisah pada `/v2/model-info` dan `/v2/health/ready`.

## 3. Membuat assessment dari gold manusia

Selesaikan anotasi tiga ahli, consensus/discussion/adjudication, lalu freeze menggunakan [22](22_INDOBERT_V2_IMPLEMENTATION_RUNBOOK.md). Dataset silver dan bundle `hasil_validasi` tidak boleh diberikan sebagai sumber pilot.

Buat file konfigurasi assessment, misalnya `data/local/assessment-kelas1-v1.json`:

```json
{
  "assessmentId": "pilot-kelas1-v1",
  "snapshotId": "<ID snapshot human_gold>",
  "questionVersionIds": ["<versi gold 1>", "<versi gold 2>", "<versi gold 3>", "<versi gold 4>", "<versi gold 5>"],
  "populationId": "kelas1-sekolah-a-2026",
  "assessmentFamily": "numerasi-kelas1-v1",
  "grade": 1,
  "sessionTtlMinutes": 120,
  "rapidGuessMs": null
}
```

Local CLI, tanpa MongoDB/network:

```powershell
.\.venv\Scripts\python.exe scripts\psychometrics.py create-assessment --gold-snapshot data\processed\gold-v1.json --assessment-config data\local\assessment-kelas1-v1.json --output data\local\assessment-receipt-v1.json
.\.venv\Scripts\python.exe scripts\psychometrics.py create-participant --assessment-id pilot-kelas1-v1 --participant-code kode-001 --output data\local\participant-001-private.json
```

Receipt peserta mengandung bearer token privat; CLI tidak mencetak token ke console. API alternatif: `POST /api/v1/internal/assessments` membaca snapshot MongoDB, kemudian `POST /api/v1/internal/assessments/{assessment_id}/participants`. Keduanya memakai token operator atau staff cookie. CLI adalah operasi operator terpercaya; provenance JSON lokal tidak membuktikan identitas manusia secara kriptografis, sehingga sumber snapshot harus hasil workflow ahli yang dikelola operator.

Frontend memakai token peserta untuk start → GET next → POST response → complete. Header `Idempotency-Key` wajib pada POST; response key harus identik dengan `responseId`. Lihat [08](08_ASSESSMENT_DELIVERY_API.md) dan [06](06_STUDENT_RESPONSE_API.md).

## 4. Menjalankan screening respons nyata

Setelah session selesai, kirim `ScreeningInput` ke `POST /api/v1/internal/psychometrics/screen`, atau simpan JSON request untuk CLI:

```powershell
.\.venv\Scripts\python.exe scripts\psychometrics.py screen --request data\local\screening-request-v1.json --output output\psychometrics\pilot-screen-v1.json
```

Request memuat assessment ID, model, first/last attempt, time window opsional dengan timezone, dan assumption review. Contoh di [07](07_PSYCHOMETRICS_API.md). Window memakai completion time. Tanpa respons nyata lengkap, screening menolak dengan 409; sistem tidak mengisi kekosongan dengan simulasi.

Policy default: Rasch ≥100 peserta/5 item; 2PL ≥300/10; 3PL ≥1000/20. Semua model memerlukan ≥50 respons serta ≥5 outcome benar/salah per item, coverage eligible ≥70%, missing peserta ≤30%, desain terhubung dan asumsi didukung. Ini ambang kebijakan proyek, bukan jaminan validitas. Data belum cukup → CTT observation + alasan gate; tidak ada fit IRT palsu.

Screening menyimpan snapshot/hash deterministik beserta policy lengkap, matrix hash, manifest sampel, exclusions dan hasil. Rerun identik mengambil snapshot lama; perubahan data/policy menghasilkan snapshot baru. Endpoint full snapshot hanya staff. Endpoint agregat per question tidak memuat subject atau EAP.

## 5. Review ahli dan pembaruan dataset

Ahli login melalui `/internal/v2/auth/login`, lalu memakai cookie dan `X-CSRF-Token` untuk:

```http
POST /api/v1/internal/psychometrics/snapshots/{snapshot_id}/decisions
```

```json
{
  "idempotencyKey": "expert-empirical-decision-001",
  "questionVersionId": "<versi pada snapshot>",
  "action": "revise",
  "rationale": "<bukti dan alasan review ahli yang dapat diaudit>"
}
```

Role `primary_annotator|expert_reviewer|senior_adjudicator|psychometrician` memerlukan `expertId`. Service token/admin tanpa profil ahli tidak dapat membuat keputusan ini. Retain mempertahankan label; revise/quarantine menahan delivery versi terkait. Keputusan immutable satu per snapshot/item, dengan actor, rationale dan hash bukti. Tidak ada perubahan label model atau content in-place.

`freeze_dataset_v2.py` kini membaca store empiris bila file ada. `--assessment-db` atau `ASSESSMENT_DB_PATH` menentukan store. Versi yang ditahan pada sumber maupun gold version dikeluarkan dengan alasan `empirical_expert_hold`. Jika konten direvisi, selesaikan versioning/qualification dan validasi manusia baru sebelum snapshot/model berikutnya; keputusan empiris sendiri bukan gold baru.

## 6. Kontrak dan verifikasi

```powershell
.\.venv\Scripts\python.exe scripts\export_api_contracts.py
.\.venv\Scripts\python.exe scripts\export_api_contracts.py --check
.\.venv\Scripts\python.exe -m pytest tests\test_empirical_analysis.py tests\test_assessment_empirical_flow.py -q
```

Export memperbarui [inventaris endpoint](12_ENDPOINT_MASTER_REFERENCE.md), [OpenAPI](schemas/openapi.json), dan [schema implementasi](schemas/implemented-api.schema.json) dari kode aktual. `nalar-api.schema.json` tetap bundle desain gateway luas; jangan memakainya sebagai validator pilot aktif. Error API aktif berbentuk `detail`, mengikuti FastAPI.

Tes memeriksa recovery parameter simulasi tiga model, NA, gate/asumsi, data invalid, desain disconnected, scoring server, idempotency, IDOR, concurrent delivery, whole-attempt selection, persist/replay snapshot dan expert hold. Demo maupun fixture test tidak membuktikan validitas terhadap siswa nyata.
