# Assessment Delivery API

## 1. Tujuan

Delivery API adalah satu-satunya jalur soal menuju student UI. Ia membentuk snapshot tetap, mengacak opsi di server, menyembunyikan kunci, dan menghubungkan response ke versi konten yang tepat.

Teacher authoring UI tidak mengirim Question langsung ke student UI. Hanya item `provisional` atau `empirically_screened` yang memenuhi assessment policy dapat dipilih assembly service.

## 2. Membuka session

```http
POST /api/v1/assessments/{assessmentId}/sessions
Idempotency-Key: <uuid>
```

```json
{
  "sessionId": "SES-001",
  "assessmentId": "ASM-001",
  "status": "active",
  "expiresAt": "2026-09-27T13:00:00Z",
  "nextItemUrl": "/api/v1/sessions/SES-001/items/next"
}
```

Subject identity dan population assignment ditentukan server/session policy.

## 3. Mengambil item berikutnya

```http
GET /api/v1/sessions/{sessionId}/items/next
```

Public DTO:

```json
{
  "deliveryInstanceId": "DLV-001",
  "sessionId": "SES-001",
  "item": {
    "publicItemId": "PUB-001",
    "questionType": "multiple_choice",
    "questionText": "Hitung luas trapesium berikut.",
    "options": [
      {"id": "pub-opt-1", "text": "156 cm²"},
      {"id": "pub-opt-2", "text": "78 cm²"},
      {"id": "pub-opt-3", "text": "18 cm²"},
      {"id": "pub-opt-4", "text": "60 cm²"}
    ],
    "media": []
  },
  "sequence": {"current": 3, "total": 10},
  "timing": {"deliveredAt": "2026-09-27T10:15:00Z", "timeLimitMs": null}
}
```

DTO tidak memuat:

- correct answer;
- internal option ID;
- solution trace;
- distractor misconception code;
- parent/family relation yang dapat membocorkan pola;
- AI decision/raw confidence;
- generator seed/parameter jika tidak dibutuhkan siswa.

## 4. Delivery snapshot internal

Server menyimpan:

```text
deliveryInstanceId
session/assessment/population
questionId + contentVersion
variantId + variantVersion
public-to-internal option mapping
option order
scoring policy version
delivery timestamp/expiry
```

Refresh halaman mengambil snapshot yang sama. Sistem tidak membuat parameter atau urutan baru di tengah attempt.

## 5. Assembly policy

Pemilihan item mempertimbangkan:

- grade/topic/subtopic blueprint;
- target taxonomy dan intended difficulty;
- empirical information jika tersedia;
- item-family diversity;
- exposure limit;
- status/risk;
- larangan menampilkan terlalu banyak sibling dari satu family.

Assembly policy berversi dan tidak ditentukan komponen React.

## 6. Menyelesaikan session

```http
POST /api/v1/sessions/{sessionId}/complete
```

Command ini finalizes session setelah response yang diperlukan diterima. Retry memakai idempotency key.

## 7. Frontend interface

```ts
type AssessmentPort = {
  start(assessmentId: string): Promise<AssessmentSession>;
  nextItem(sessionId: string): Promise<DeliveredItem>;
  submitResponse(input: ResponseCreate): Promise<ResponseReceipt>;
  complete(sessionId: string): Promise<SessionResult>;
};
```

Student UI hanya bergantung pada interface tersebut. Ia tidak mengimpor seed lokal atau membandingkan jawaban dengan `correctAnswer` di browser.

## 8. Status implementasi

Student UI prototype masih memakai seed lokal dan client-side correctness. Session, delivery instance, public option mapping, server-side scoring, exposure control, dan assembly policy adalah target.

