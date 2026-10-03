# Master Reference Endpoint

Inventaris ini dihasilkan dari `app.main:app` oleh `scripts/export_api_contracts.py`. Versi API: **2.2.0**. Semua path dalam tabel tersedia dalam kode; readiness data, storage, provider, dan model tetap diperiksa pada runtime.

| Method | Path | Akses | Ringkasan |
|---|---|---|---|
| POST | `/api/v1/assessments/{assessment_id}/sessions` | participant Bearer; Idempotency-Key | Start |
| GET | `/api/v1/capabilities` | public diagnostics / advisory | Capabilities |
| GET | `/api/v1/health` | public diagnostics / advisory | Health |
| POST | `/api/v1/internal/assessments` | staff cookie atau X-Internal-API-Key; CSRF untuk cookie | Create Assessment |
| POST | `/api/v1/internal/assessments/{assessment_id}/participants` | staff cookie atau X-Internal-API-Key; CSRF untuk cookie | Create Participant |
| POST | `/api/v1/internal/psychometrics/item-analysis` | staff cookie atau X-Internal-API-Key; CSRF untuk cookie | Item Analysis |
| POST | `/api/v1/internal/psychometrics/screen` | staff cookie atau X-Internal-API-Key; CSRF untuk cookie | Screen |
| GET | `/api/v1/internal/psychometrics/snapshots/{snapshot_id}` | staff cookie atau X-Internal-API-Key | Snapshot |
| GET | `/api/v1/internal/psychometrics/snapshots/{snapshot_id}/decisions` | staff cookie atau X-Internal-API-Key | Decisions |
| POST | `/api/v1/internal/silver/snapshots` | staff cookie atau X-Internal-API-Key; CSRF untuk cookie | Register Silver Snapshot |
| GET | `/api/v1/internal/silver/snapshots/{snapshot_id}` | staff cookie atau X-Internal-API-Key | Silver Snapshot |
| GET | `/api/v1/psychometrics/items/{question_id}/snapshots` | staff cookie atau X-Internal-API-Key | Item Snapshots |
| POST | `/api/v1/responses` | participant Bearer; Idempotency-Key | Response |
| POST | `/api/v1/sessions/{session_id}/complete` | participant Bearer; Idempotency-Key | Complete |
| GET | `/api/v1/sessions/{session_id}/items/next` | participant Bearer | Next Item |
| GET | `/health` | public diagnostics / advisory | Health |
| POST | `/internal/v2/auth/login` | invite-only username/password | Login |
| POST | `/internal/v2/auth/logout` | staff cookie + CSRF | Logout |
| POST | `/v1/classify` | public diagnostics / advisory | Classify |
| POST | `/v1/extract` | public diagnostics / advisory | Extract |
| GET | `/v1/extraction-info` | public diagnostics / advisory | Extraction Info |
| GET | `/v1/model-info` | public diagnostics / advisory | Model Info |
| POST | `/v1/verify-answer` | public diagnostics / advisory | Verify Answer |
| POST | `/v2/classify` | public diagnostics / advisory | Classify |
| GET | `/v2/health/ready` | public diagnostics / advisory | Ready |
| GET | `/v2/llm-info` | public diagnostics / advisory | Llm Info |
| GET | `/v2/model-info` | public diagnostics / advisory | Model Info |
| GET | `/v2/psychometrics-info` | public diagnostics / advisory | Info |

Dokumen operasional: [06 respons](06_STUDENT_RESPONSE_API.md), [07 CTT/IRT](07_PSYCHOMETRICS_API.md), [08 delivery](08_ASSESSMENT_DELIVERY_API.md), [27 runbook](27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md).

Route authoring publik, async jobs/Redis, generation/variants, family/variant psychometrics, CAT, DIF, equating, Claude API, dan promotion otomatis tetap desain lanjutan. Mereka tidak ada dalam inventaris implementasi ini.

OpenAPI aktual: `/openapi.json`; salinan terversi: [schemas/openapi.json](schemas/openapi.json). Bundle kontrak aktual: [schemas/implemented-api.schema.json](schemas/implemented-api.schema.json). `nalar-api.schema.json` menunjuk bundle kontrak aktual untuk kompatibilitas.

HTTP error FastAPI memakai `{"detail": ...}` dengan 401/403/404/409/422/503 sesuai penyebab. `/v2/classify` tetap 503 ketika artefak research-only/unapproved/gagal gate. CTT tetap dihitung jika data IRT kurang; respons analisis membawa `readiness.failures` dan status menunggu.
