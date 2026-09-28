# OpenAPI, Swagger, Postman, dan Contract Testing

FastAPI aktif menerbitkan OpenAPI di `/openapi.json` dan Swagger UI di `/docs`. Kontrak implementasi `/v2/*` dan `/internal/v2/*` berasal langsung dari Pydantic; bundle schema dokumentasi mencakup arsitektur target yang lebih luas. Endpoint anotasi tetap 503 sampai Atlas dikonfigurasi, dan endpoint klasifikasi tetap 503 sampai artefak model checksum-valid tersedia.

## 1. Sumber kontrak

Target kontrak harus mempunyai tiga representasi yang sinkron:

```text
OpenAPI 3.1
    ↕
JSON Schema Draft 2020-12
    ↕
runtime validator + generated frontend types
```

Lokasi target:

```text
GET /api-docs/openapi.json
GET /api-docs
GET /api-docs/redoc
GET /api-docs/schemas/nalar-api.schema.json
```

Bundle sumber repository: [`schemas/nalar-api.schema.json`](schemas/nalar-api.schema.json).

## 2. Aturan publikasi OpenAPI

- Public gateway menjadi sumber OpenAPI frontend; OpenAPI internal FastAPI tidak dipakai langsung browser.
- Endpoint internal memakai security scheme service-to-service dan tidak dimasukkan ke SDK frontend publik.
- Example tidak boleh mengandung credential, raw prompt, PII, atau kunci delivery aktif.
- Setiap operation memiliki `operationId` stabil agar SDK/type generation tidak berubah karena judul.
- Response harus memakai error envelope bersama.
- Status implementasi endpoint ditandai extension `x-nalar-status`: `implemented`, `prototype`, `target`, atau `future`.

## 3. Postman environment

```json
{
  "baseUrl": "http://localhost:5000/api/v1",
  "teacherToken": "",
  "studentToken": "",
  "questionId": "",
  "contentVersion": "",
  "workflowRunId": "",
  "assessmentId": "",
  "sessionId": "",
  "deliveryInstanceId": ""
}
```

Token kosong hanya diperbolehkan pada prototype lokal yang belum mengaktifkan auth.

## 4. Collection teacher authoring

Urutan request:

```text
GET capabilities
    -> POST question validate
    -> POST create question draft
    -> PUT revise draft dengan If-Match
    -> POST submit
    -> GET workflow run sampai terminal
    -> GET question safe summary
```

Test minimum:

- create menghasilkan `questionId`, `contentVersion=1`, `author_draft`;
- revision version conflict menghasilkan `409`;
- submit memakai idempotency key dan mengembalikan job/status URL;
- teacher tidak dapat mengirim `status` atau AI label;
- question milik teacher lain menghasilkan `403/404` sesuai disclosure policy.

## 5. Collection extraction

```text
POST multipart /extractions
    -> save jobId
    -> poll GET /extractions/{jobId}
    -> choose candidate
    -> POST /questions/from-extraction
```

Test file:

- PDF text layer;
- scanned image;
- source dengan formula;
- unsupported extension;
- file melebihi size limit;
- candidate dengan warning.

## 6. Collection student delivery

```text
POST assessment session
    -> GET next delivered item
    -> assert response tidak mengandung answerSpec/correctAnswer
    -> POST response dengan deliveryInstanceId
    -> repeat responseId untuk menguji idempotency
    -> complete session
```

Client tidak boleh menghitung atau mengirim `isCorrect`.

## 7. Collection generation/AI internal

Collection internal menggunakan service token terpisah:

```text
submit workflow
    -> answer verification
    -> IndoBERT/LLM screen
    -> Claude mengolah prediksi IndoBERT
    -> tiga expert initial annotation blind
    -> tiga AI review
    -> voting/adjudikasi manusia
    -> create generation job
    -> inspect variant
    -> psychometric screen
```

Jangan menaruh service credential dalam collection yang dibagikan ke frontend.

## 8. Contract test

Minimum CI checks:

1. Parse OpenAPI dan JSON Schema.
2. Validate request/response fixtures dengan schema.
3. Pastikan public `DeliveredItem` tidak memiliki forbidden fields.
4. Pastikan semua endpoint target memakai common error envelope.
5. Pastikan enum status sama antara docs, schema, dan backend.
6. Pastikan proposal Claude tidak dapat menaikkan status menjadi `expert_validated` tanpa tiga pakar, dan initial annotation terkunci sebelum AI/peer ditampilkan.
7. Jalankan consumer contract test untuk `TeacherAuthoringPort`, `ExpertReviewPort`, dan `AssessmentPort`.
8. Bandingkan schema hash; breaking change tanpa API version baru menggagalkan CI.

## 9. Mock frontend

Frontend baru dapat dikembangkan sebelum backend selesai menggunakan OpenAPI mock/fixture yang tervalidasi schema. Mock harus mensimulasikan:

- success dan validation error;
- job polling;
- quarantine/revision required;
- content version conflict;
- expired session;
- duplicate response.

Mock tidak boleh menjadi sumber kontrak kedua. Fixture harus divalidasi terhadap schema bundle yang sama.

## 10. Kondisi repository

FastAPI Python mempunyai Swagger/ReDoc bawaan. Express Swagger lama berada di `project_assessment` yang sudah dihapus. OpenAPI gateway baru, schema 3 × 4 × 3, reviewer endpoints, generated types dan CI schema check adalah target migrasi. Collection Postman pada dokumen ini belum merupakan artefak yang dapat dijalankan.

## 11. Kalibrasi untuk pipeline batch

Modul `agentic.convert`, `validate`, `export`, dan `pretest` adalah CLI, sehingga tidak dimasukkan ke Swagger/Postman seolah-olah endpoint. Tesnya dijalankan melalui `.venv/Scripts/python -m pytest tests/test_pretest_agentic.py -q`; snapshot audit menghasilkan 23 tes lulus. Tes tersebut memakai fixture sintetis dan belum menggantikan integration test terhadap PDF/Markdown fixture mini.

Jika nanti dibuat import API, contract test minimum harus menguji dry-run, checksum sumber, idempotency ID eksternal, mapping schema, stale output detection, penolakan `needs_image`/kunci konflik, serta bahwa field kunci tidak bocor ke DTO publik.
