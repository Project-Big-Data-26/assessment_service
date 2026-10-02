# Assessment Delivery API

Delivery fixed-form sudah tersedia di FastAPI. SQLite menyimpan assessment immutable, token hash peserta, session, delivery dengan mapping privat, response event, snapshot psikometrik dan keputusan empiris ahli. MongoDB tetap menyimpan anotasi/gold snapshot. UI siswa belum dibangun; API tersedia untuk frontend atau Swagger.

## Membekukan assessment

```http
POST /api/v1/internal/assessments
X-Internal-API-Key: <token operator>
```

```json
{
  "assessmentId": "pilot-kelas1-v1",
  "snapshotId": "<snapshot human_gold>",
  "questionVersionIds": ["<questionVersionId pertama>", "<questionVersionId kedua>"],
  "populationId": "kelas1-sekolah-a-2026",
  "assessmentFamily": "numerasi-kelas1-pilot-v1",
  "grade": 1,
  "sessionTtlMinutes": 120,
  "rapidGuessMs": null
}
```

API membaca snapshot MongoDB; CLI [27](27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md) dapat membaca JSON lokal. Keduanya memvalidasi SHA-256 isi, `human_gold`, keputusan `gold_ready|adjudicated`, key/solusi, grade, versi unik dan opsi single-choice. Silver/`researchOnly` ditolak. Gate training/test model terpisah dari kelayakan konten pilot.

Satu assessment berisi satu grade/populasi. Blueprint, urutan soal, versi/kunci dan scoring policy immutable. ID sama dengan konten berbeda menghasilkan 409. Versi yang ditahan ahli ditolak. Opsi diacak per delivery; urutan soal mengikuti blueprint.

## Provision peserta

```http
POST /api/v1/internal/assessments/{assessment_id}/participants
X-Internal-API-Key: <token operator>
Content-Type: application/json
```

```json
{"participantCode": "kode-pseudonim-001"}
```

Receipt berisi `participantToken` acak. Operator memberikan token kepada peserta yang sesuai. Database menyimpan hash token dan HMAC kode; kode sama dalam populasi sama mengenali subject yang sama. Token terikat satu assessment. Integrasi identity provider dan rotasi/revokasi invite masih target.

## Session dan item

```http
POST /api/v1/assessments/{assessment_id}/sessions
Authorization: Bearer <participantToken>
Idempotency-Key: start-0001

GET /api/v1/sessions/{session_id}/items/next
Authorization: Bearer <participantToken>
```

TTL 5–1440 menit, default 120. Retry start mengambil session yang sama; key baru membuat attempt baru. Refresh GET mempertahankan pending delivery/opsi/urutan. Transaksi mencegah request paralel membuat dua delivery.

```json
{
  "deliveryInstanceId": "<opaque ID>",
  "sessionId": "<session ID>",
  "item": {
    "publicItemId": "<opaque ID>",
    "questionType": "multiple_choice",
    "questionText": "Hitung 2 + 1.",
    "stimulus": null,
    "options": [{"id": "<opaque option ID>", "text": "3"}, {"id": "<opaque option ID>", "text": "4"}],
    "media": []
  },
  "sequence": {"current": 1, "total": 5},
  "timing": {"deliveredAt": "2026-10-02T03:00:00Z", "expiresAt": "2026-10-02T05:00:00Z"}
}
```

DTO tidak berisi key, label, solusi, hash/version internal atau mapping opsi. Delivery saat ini tekstual; transkripsi visual terverifikasi dapat disertakan. Rendering aset privat siswa, exposure budget, assembly adaptif/CAT dan varian belum diimplementasikan.

## Completion dan hold

```http
POST /api/v1/sessions/{session_id}/complete
Authorization: Bearer <participantToken>
Idempotency-Key: complete-0001
```

Semua item harus dijawab atau di-skip. Completion adalah transisi satu kali dan aman diulang. GET setelah seluruh respons menghasilkan `finished=true, item=null`. Detail: [06](06_STUDENT_RESPONSE_API.md).

Keputusan empiris `revise|quarantine` menahan delivery versi tersebut, termasuk refresh pending item. Blueprint tidak diganti diam-diam. Revisi memerlukan versi konten, validasi manusia dan assessment baru.

`sesi_pretest.json` adalah blueprint candidate, bukan delivery session. Resolve staging ID ke gold `questionVersionId` sebelum pilot.
