# Student Response API

## 1. Tujuan

Response API target menerima event jawaban yang selalu terikat pada `deliveryInstanceId`. Hanya versi item yang lolos tiga pakar dan policy pilot yang boleh diberikan. Browser tidak mengirim `isCorrect`; server mengambil immutable delivery snapshot dan menghitung correctness sendiri.

## 2. Endpoint

```http
POST /api/v1/responses
Idempotency-Key: <responseId>
```

## 3. Request

```json
{
  "responseId": "RESP-001",
  "deliveryInstanceId": "DLV-001",
  "selectedOptionIds": ["pub-opt-2"],
  "responseTimeMs": 42000,
  "answerChanges": 1,
  "clientSubmittedAt": "2026-09-27T10:20:00Z"
}
```

Identity siswa, assessment, session, question/variant version, dan option mapping berasal dari authenticated session serta delivery instance, bukan body.

Untuk tipe `numeric` atau `short_answer`, request memakai salah satu field sesuai schema:

```json
{
  "responseId": "RESP-002",
  "deliveryInstanceId": "DLV-002",
  "numericAnswer": 78,
  "responseTimeMs": 35000,
  "answerChanges": 0
}
```

Untuk `matching`, body memakai `matchingPairs: [{"leftId":"pub-left-1","rightId":"pub-right-2"}, ...]`; untuk `interactive_grid`/click-the-box memakai `selectedGridCellIds: ["pub-cell-3"]`. `true_false` memakai satu `selectedOptionIds`, sedangkan checkbox/`multiple_response` dapat memakai beberapa. `essay` memakai `textAnswer` dan status scoring menunggu penilai manusia. Seluruh ID dari browser adalah ID publik dalam delivery snapshot; server memetakan dan memvalidasinya.

## 4. Processing

```text
validate schema and idempotency
    -> resolve authenticated session
    -> load delivery snapshot
    -> ensure item not expired/already finalized
    -> map public option IDs to internal option IDs
    -> server-side score
    -> derive timing/anomaly flags
    -> append response event
```

## 5. Respons

```json
{
  "responseId": "RESP-001",
  "accepted": true,
  "scoring": {
    "status": "scored",
    "isCorrect": true,
    "score": 1
  },
  "nextItemUrl": "/api/v1/sessions/SES-001/items/next"
}
```

Feedback benar/salah dapat ditunda sesuai assessment policy. Untuk tes formal, response boleh hanya mengembalikan `accepted`.

## 6. Stored event

```json
{
  "responseId": "RESP-001",
  "deliveryInstanceId": "DLV-001",
  "sessionId": "SES-001",
  "assessmentId": "ASM-001",
  "assessmentFamily": "PILOT-SMP8-GEO",
  "populationId": "GRADE-8-REFERENCE",
  "subjectHash": "hmac:...",
  "questionId": "Q-001",
  "contentVersion": 2,
  "variantId": "VAR-014",
  "variantVersion": 1,
  "selectedInternalOptionIds": ["opt-correct"],
  "isCorrect": true,
  "score": 1,
  "responseTimeMs": 42000,
  "answerChanges": 1,
  "flags": [],
  "submittedAt": "2026-09-27T10:20:00Z"
}
```

Event tersimpan bersifat append-only. Koreksi administratif membuat compensating event, bukan mengubah histori tanpa jejak.

## 7. Validasi timing

Sistem mencatat tetapi tidak langsung membuang berdasarkan satu cutoff global. Flag dapat meliputi:

- `rapid_guess_candidate` berdasarkan item/time policy;
- `inactive_session`;
- `duplicate_submission`;
- `late_submission`;
- `invalid_option_mapping`;
- `automation_pattern_suspected`.

Psychometric worker menentukan inclusion policy berversi dan menyimpan jumlah event yang dikeluarkan.

## 8. Privacy

- `subjectHash` dibuat server dengan keyed HMAC/rotating policy;
- NISN, nama, email, dan token tidak disimpan pada response event;
- population metadata cukup untuk analisis tetapi tidak mengidentifikasi individu;
- retention dan access policy wajib dibedakan antara response raw dan aggregate.

## 9. Status implementasi

Backend gateway prototype yang dahulu menerima `questionId`, `studentHash`, dan `isCorrect` dari browser sudah tidak ada di worktree. FastAPI Python belum menyediakan delivery-bound response event. Target migration wajib menambahkan delivery instance, server-side identity/scoring, unique response ID, dan immutable version join.

## 10. Batas terhadap artefak pretest lokal

`soal_pretest_db.json` dan `sesi_pretest.json` adalah hasil perakitan authoring lokal, bukan log administrasi siswa. Keduanya tidak berisi `deliveryInstanceId`, option mapping per siswa, identity pseudonim, response ID, timing, atau server-scored correctness. File tersebut tidak boleh dipakai langsung untuk menghitung CTT/IRT dan tidak boleh dikirim sebagai respons siswa karena memuat kunci/alasan opsi. Setelah import dan validasi ahli, delivery service membuat snapshot baru sesuai dokumen 08.
