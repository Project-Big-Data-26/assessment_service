# Question Authoring API

## 1. Tujuan

Question API mengelola konten yang ditulis teacher dan transisinya menuju workflow otomatis. Teacher berperan sebagai author: memasukkan, memperbaiki, dan submit soal. Teacher bukan reviewer, annotator, adjudikator, atau pemilik label final.

Base path: `/api/v1/questions`.

## 2. Pemisahan data

```text
authoring content       -> ditulis teacher
canonical content       -> hasil normalisasi sistem
answer verification     -> bukti solver/rules
AI decisions            -> IndoBERT, LLM, adjudicator, risk
psychometric snapshots  -> bukti respons empiris
```

Kelima sumber tidak boleh digabung menjadi satu field. Perubahan authoring content selalu menghasilkan `contentVersion` baru dan menjalankan ulang workflow yang relevan.

## 3. Authoring content

```json
{
  "subject": "Matematika",
  "grade": 10,
  "topic": "Aljabar",
  "subtopic": "Persamaan Kuadrat",
  "learningObjective": "Menerapkan pemfaktoran persamaan kuadrat",
  "questionType": "multiple_choice",
  "questionText": "Jika $x^2+5x+6=0$, tentukan akar-akarnya.",
  "options": [
    {"id": "opt-a", "text": "$-2$ dan $-3$"},
    {"id": "opt-b", "text": "$2$ dan $3$"},
    {"id": "opt-c", "text": "$-1$ dan $-6$"},
    {"id": "opt-d", "text": "$1$ dan $6$"}
  ],
  "answerSpec": {
    "kind": "option_ids",
    "optionIds": ["opt-a"]
  },
  "explanation": "$(x+2)(x+3)=0$.",
  "source": {
    "origin": "manual",
    "reference": "Buku Matematika SMA Kelas X"
  }
}
```

`teacherId`, tenant, dan role tidak diambil dari request body. Tahap lokal menggunakan `LOCAL_TEACHER_ID`; authentication context multi-user adalah target berikutnya. Teacher tidak wajib mengisi Bloom, knowledge dimension, atau difficulty.

## 4. Validasi tanpa menyimpan

```http
POST /api/v1/questions/validate
```

Caller: teacher UI/import adapter. Side effect: tidak ada. Idempotent: ya.

Respons:

```json
{
  "valid": false,
  "errors": [
    {
      "path": "/answerSpec/optionIds/0",
      "code": "unknown_option_id",
      "message": "Jawaban harus merujuk pada opsi yang tersedia."
    }
  ],
  "warnings": []
}
```

Validasi ini memeriksa schema/aturan authoring saja. Ia belum membuktikan kunci atau klasifikasi soal benar.

## 5. Membuat draft

```http
POST /api/v1/questions
Idempotency-Key: <uuid>
```

Body memakai `QuestionAuthoringContent`. Respons `201`:

```json
{
  "questionId": "Q-4a039437-c106-4081-9a7a-cc12a73b6b23",
  "contentVersion": 1,
  "status": "author_draft",
  "workflowRunId": null,
  "authoringContent": {},
  "workflowSummary": null,
  "createdAt": "2026-09-27T10:00:00Z",
  "updatedAt": "2026-09-27T10:00:00Z"
}
```

Server membuat `questionId`; identifier sumber eksternal ditempatkan pada `source.externalId`, bukan dipakai sebagai MongoDB `_id`.

## 6. Mengubah draft atau membuat revision

```http
PUT /api/v1/questions/{questionId}/draft
If-Match: "<contentVersion>"
Idempotency-Key: <uuid>
```

Body adalah replacement penuh `QuestionAuthoringContent`. Replacement penuh dipilih agar perilaku frontend sederhana dan tidak ambigu seperti partial patch nested object.

Aturan:

- `author_draft`: update menghasilkan version berikutnya;
- `revision_required` atau `quarantined`: teacher dapat membuat revision baru berdasarkan warning sistem;
- `provisional`, `empirically_screened`, atau `active`: revision membuat version draft baru; version lama tidak ditimpa;
- teacher tidak dapat mengubah `status`, AI decision, psychometric snapshot, owner, atau timestamps.

Jika `If-Match` tidak sama dengan current version, server mengembalikan `409 content_version_conflict`.
Retry request yang sama harus memakai `Idempotency-Key` yang sama; untuk edit baru gunakan key baru.

## 7. Submit ke workflow otomatis

```http
POST /api/v1/questions/{questionId}/submit
Idempotency-Key: <uuid>
```

Teacher hanya menjalankan command submit. Teacher tidak memilih hasil klasifikasi atau jalur adjudikasi.
Retry jaringan dengan key yang sama mengembalikan workflow ID semula. Setelah workflow `failed`, submit ulang dengan key baru membuat run baru untuk versi konten yang sama.

Respons `202`:

```json
{
  "questionId": "Q-4a039437-c106-4081-9a7a-cc12a73b6b23",
  "contentVersion": 2,
  "status": "submitted",
  "workflowRunId": "WF-2e75fe51-7c80-4b6a-978b-fcfbbed58f89",
  "statusUrl": "/api/v1/workflow-runs/WF-2e75fe51-7c80-4b6a-978b-fcfbbed58f89"
}
```

Pipeline target:

```text
submitted
  -> canonicalization
  -> deterministic validation
  -> answer verification
  -> IndoBERT and independent LLM screening
  -> agreement/risk
      -> LLM adjudication jika konflik
  -> provisional atau quarantine/revision_required
```

## 8. Membaca resource

```http
GET /api/v1/questions/{questionId}
GET /api/v1/questions?status=author_draft&cursor=...
```

Teacher menerima authoring content miliknya, `workflowRunId` terakhir untuk polling/retry, dan safe workflow summary. Internal prompts, solver secret, correct-option mapping untuk delivery aktif, dan raw model trace tidak dikirim.

Contoh potongan resource (field `authoringContent`, `createdAt`, dan `updatedAt` tidak ditampilkan di sini):

```json
{
  "questionId": "Q-4a039437-c106-4081-9a7a-cc12a73b6b23",
  "contentVersion": 2,
  "status": "provisional",
  "workflowSummary": {
    "answerVerified": true,
    "decisionType": "ai_consensus",
    "taxonomy": {
      "bloom": "C3",
      "knowledgeDimension": "procedural",
      "intendedDifficulty": "Medium"
    },
    "warnings": []
  }
}
```

## 9. Lifecycle authoring

```text
author_draft
    -> submitted
    -> processing
        -> revision_required -> teacher creates new version -> submitted
        -> quarantined       -> teacher may create new version
        -> provisional
            -> pilot_active
            -> empirically_screened
            -> active
            -> retired
```

`revision_required` adalah machine feedback untuk authoring revision, bukan permintaan teacher melakukan pedagogical review.

## 10. Tipe soal

Target enum:

```text
multiple_choice | multiple_response | true_false | numeric
short_answer | essay | matching
```

MVP generation dan server-side scoring sebaiknya memprioritaskan `multiple_choice`, `numeric`, dan `true_false`. Tipe lain membutuhkan scoring policy tambahan.

## 11. Status implementasi tahap lokal

Endpoint authoring pada dokumen ini sudah berjalan dengan `FileQuestionRepository` di `data/local/`: identitas soal, versi konten immutable, workflow run, dan AI decision disimpan terpisah. `If-Match` dan `Idempotency-Key` dipakai untuk perubahan. Submit membuat run yang dapat dipoll dan worker lokal memproses satu per satu serta memulihkan run yang tertunda setelah restart.

Identitas teacher saat ini berasal dari `LOCAL_TEACHER_ID`, bukan autentikasi multi-user. Artefak IndoBERT yang belum disetujui untuk provisional, LLM yang belum dikonfigurasi, atau risk policy yang belum dikalibrasi menghasilkan workflow `failed`, sedangkan draft tetap tersimpan. Ambang pada `configs/ai_risk_policy.json` harus ditentukan dari evaluasi per-head sebelum status provisional diaktifkan. MongoDB, delivery siswa, psikometrik, dan generation masih target berikutnya. Endpoint legacy prototype di luar jalur authoring ini belum dimigrasikan.
