# Arsitektur dan Konvensi API

## 1. Prinsip boundary

Frontend hanya mengakses **Express API Gateway**. Browser tidak memanggil FastAPI, model provider, Redis worker, atau MongoDB secara langsung.

```text
Teacher UI / Student UI / Future Frontend
                  |
                  | HTTPS /api/v1
                  v
          Express API Gateway
 auth | authorization | AJV | rate limit | public DTO | error mapping
          |              |               |
          v              v               v
       MongoDB      Redis job queue   Internal services
                                      FastAPI AI
                                      generation worker
                                      psychometric worker
                                      object storage
```

Konsekuensinya:

- frontend dapat diganti selama mematuhi OpenAPI/JSON Schema;
- nama provider/model, lokasi service, dan credential tidak bocor ke browser;
- response MongoDB tidak dikirim mentah sebagai public DTO;
- perubahan implementasi AI tidak memaksa perubahan komponen UI;
- proses lambat dikembalikan sebagai job/resource, bukan koneksi HTTP panjang.

## 2. Aktor dan kewenangan

| Aktor | Boleh | Tidak boleh |
|---|---|---|
| `teacher` | Membuat, mengubah, mengimpor, dan submit authoring draft miliknya; melihat status | Menetapkan label final, adjudikasi, override gate, mengirim item langsung ke siswa |
| `student` | Membuka assessment session dan mengirim jawaban | Membaca kunci, internal option mapping, solution trace, atau AI decision |
| `ai_service` | Ekstraksi, answer verification, klasifikasi, agreement, adjudikasi otomatis | Mengubah authoring content tanpa provenance/version |
| `psychometric_worker` | Mengagregasi response dan membuat immutable snapshot | Mengubah response event lama |
| `system_admin` | Operasional service/model, quarantine inspection, rollback | Menjadi sumber label pedagogis hanya karena role admin |

Identity diperoleh dari access token/session. Field seperti `teacherId`, `role`, dan `studentId` tidak dipercaya dari body request.

## 3. Topologi resource

| Resource | Prefix | Fungsi |
|---|---|---|
| Health/capabilities | `/api/v1/health`, `/api/v1/capabilities` | Liveness dan kemampuan kontrak aktif |
| Questions | `/api/v1/questions` | Teacher authoring, revision, submit, status |
| Extractions | `/api/v1/extractions` | Import file menjadi authoring candidate |
| AI screens | `/api/v1/ai` | Screening/debug dan informasi model |
| Workflow runs | `/api/v1/workflow-runs` | Status pipeline otomatis |
| AI decisions | `/api/v1/ai-decisions` | Agreement, risk, dan adjudication result |
| Item models/families/variants | `/api/v1/item-models`, `/item-families`, `/variants` | Controlled generation |
| Assessments/sessions | `/api/v1/assessments`, `/sessions` | Assembly dan delivery snapshot |
| Responses | `/api/v1/responses` | Event jawaban yang terikat delivery instance |
| Psychometrics | `/api/v1/psychometrics` | Snapshot kualitas item/family |

## 4. Base URL

| Lingkungan | Gateway publik | Internal AI |
|---|---|---|
| Lokal | `http://localhost:5000/api/v1` | `http://localhost:8000` |
| Docker | `http://backend:5000/api/v1` | `http://ai:8000` |
| Frontend | `VITE_API_URL` atau `/api/v1` | tidak digunakan browser |

## 5. Public DTO dan penamaan

- Public API memakai `camelCase` secara konsisten.
- Internal FastAPI/model record boleh memakai `snake_case`.
- Mapping hanya dilakukan pada gateway/adapter.
- `_id`, provider prompt, model credential, internal correct-option mapping, dan stack trace tidak masuk public DTO.
- Penambahan field bersifat backward-compatible; frontend wajib mengabaikan field yang tidak dikenal.

## 6. Request headers

```http
Authorization: Bearer <token>
Accept: application/json
Content-Type: application/json
Idempotency-Key: <uuid>          # command create/submit/response
If-Match: "<contentVersion>"    # revision concurrency control
X-Request-Id: <uuid>             # opsional dari client
```

Upload menggunakan `multipart/form-data`; browser tidak menetapkan boundary secara manual.

## 7. Asynchronous job

Extraction, submit workflow, batch generation, screening, dan psychometric calibration dapat mengembalikan `202 Accepted`:

```json
{
  "jobId": "JOB-001",
  "jobType": "question_screening",
  "status": "queued",
  "statusUrl": "/api/v1/workflow-runs/JOB-001"
}
```

Status job:

```text
queued -> running -> succeeded
                  -> failed
                  -> quarantined
                  -> cancelled
```

Frontend melakukan polling dengan backoff atau menggunakan event transport tambahan. Business result tetap dibaca dari resource URL; frontend tidak bergantung pada Redis/Celery.

## 8. Error envelope

Semua endpoint target memakai bentuk yang sama:

```json
{
  "error": {
    "code": "content_version_conflict",
    "message": "Draft telah berubah. Muat versi terbaru sebelum menyimpan.",
    "details": {
      "expectedVersion": 2,
      "actualVersion": 3
    },
    "traceId": "TRC-001"
  }
}
```

| Code HTTP | Makna |
|---:|---|
| `200` | Read/validate/analysis sinkron berhasil |
| `201` | Resource dibuat |
| `202` | Command diterima sebagai job |
| `400` | Request tidak dapat dipahami |
| `401` | Belum terautentikasi |
| `403` | Role/ownership tidak mengizinkan |
| `404` | Resource tidak ditemukan |
| `409` | Version/state/idempotency conflict |
| `413` | Upload terlalu besar |
| `415` | Media type tidak didukung |
| `422` | Schema valid secara JSON tetapi melanggar kontrak/domain |
| `429` | Rate limit |
| `502` | Dependency memberi respons invalid |
| `503` | Dependency wajib tidak siap |

## 9. Versioning dan immutability

- Breaking API change memakai prefix baru.
- Authoring revision menaikkan `contentVersion`.
- Setiap workflow, AI decision, delivery, response, dan psychometric snapshot menyimpan versi konten yang dipakai.
- Active item tidak ditimpa. Revisi membuat version baru; delivery lama tetap dapat direproduksi.
- Response event dan decision event bersifat append-only.

Join key minimum:

```text
questionId + contentVersion
variantId + variantVersion
deliveryInstanceId
populationId + assessmentFamily
```

## 10. Security dan privacy target

- authentication dan role/ownership authorization pada gateway;
- server-side identity, scoring, option mapping, dan idempotency;
- MIME signature, checksum, antivirus, size limit, dan object-storage policy;
- pseudonymous subject hash; tidak menyimpan NISN/nama siswa pada response event;
- field-level redaction untuk kunci dan internal AI trace;
- rate limit, audit event, retention, encryption in transit/at rest;
- teacher hanya dapat mengubah soal miliknya kecuali ada policy tenancy lain.

Implementasi prototype saat ini belum memenuhi seluruh kontrol tersebut dan tidak boleh dibuka ke internet tanpa hardening.

## 11. Health dan capabilities

```http
GET /api/v1/health
GET /api/v1/capabilities
```

`health` menunjukkan liveness/readiness. `capabilities` membantu frontend memasang fitur secara dinamis:

```json
{
  "apiVersion": "v1",
  "features": {
    "extraction": true,
    "questionGeneration": false,
    "llmAdjudication": false,
    "psychometrics": true
  },
  "contracts": {
    "openApiUrl": "/api-docs/openapi.json",
    "jsonSchemaUrl": "/api-docs/schemas/nalar-api.schema.json"
  }
}
```

