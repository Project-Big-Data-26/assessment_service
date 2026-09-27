# JSON Schema Reference

## 1. Tujuan

JSON Schema publik berada pada:

[`schemas/nalar-api.schema.json`](schemas/nalar-api.schema.json)

Bundle memakai JSON Schema Draft 2020-12 dan `$defs` agar satu sumber dapat dipakai untuk:

- validasi AJV pada Express gateway;
- menghasilkan tipe TypeScript frontend;
- mock server dan fixture QA;
- contract test gateway-internal service;
- dokumentasi OpenAPI;
- validasi payload batch/import.

Schema public DTO berbeda dari MongoDB document schema. Database menambahkan identity, ownership, internal answer mapping, workflow trace, timestamps, dan index yang tidak boleh dikirim mentah ke browser.

## 2. Definisi utama

| `$defs` | Dipakai oleh |
|---|---|
| `QuestionAuthoringContent` | Validate/create/revise draft teacher |
| `QuestionResource` | Teacher read model |
| `ValidationResult` | Hasil validasi authoring tanpa penyimpanan |
| `WorkflowRun` | Status proses otomatis yang dapat dipoll |
| `ExtractionJob` | Polling extraction |
| `AiDecisionSummary` | Safe result untuk authoring UI |
| `GenerationRequest` | Controlled generation command |
| `DeliveredItem` | Student UI tanpa kunci |
| `ResponseCreate` | Submit jawaban terikat delivery |
| `PsychometricSnapshot` | Read-only quality summary |
| `JobAccepted` | Respons async `202` |
| `ErrorEnvelope` | Semua error target |

Reference ke satu definition:

```text
https://nalar.local/schemas/nalar-api.schema.json#/$defs/QuestionAuthoringContent
```

## 3. Aturan authoring

- Teacher identity tidak ada dalam body; gateway mengambilnya dari token.
- `options[].id` stabil dalam satu content version dan digunakan `answerSpec.optionIds`.
- Multiple-choice memerlukan minimal dua opsi dan `answerSpec.kind=option_ids`; aturan conditional diperiksa JSON Schema plus domain validator.
- Teacher tidak mengirim `status`, `contentVersion`, AI label, risk, atau psychometric result.
- LaTeX tetap berupa string dan harus menjalani render/sanitization terpisah.

## 4. Aturan delivery dan response

- `DeliveredItem` tidak memiliki `answerSpec`, internal option ID, explanation, atau solution trace.
- `ResponseCreate` wajib berisi tepat satu bentuk jawaban yang sesuai tipe item.
- `responseId` dan `deliveryInstanceId` wajib agar retry aman dan version join tidak ambigu.
- `isCorrect`, `studentHash`, `questionId`, dan `assessmentId` tidak diterima dari browser sebagai sumber kebenaran.

## 5. Aturan AI dan psychometric

- Bloom enum: `C1`-`C6`.
- Knowledge enum: `factual`, `conceptual`, `procedural`, `metacognitive`.
- Difficulty enum: `Easy`, `Medium`, `Hard`.
- `decisionType` membedakan `model_suggestion`, `ai_consensus`, dan `ai_adjudicated`.
- Intended dan empirical difficulty tidak ditempatkan pada field yang sama.
- Snapshot selalu membawa population dan version join key.

## 6. Schema evolution

- Perubahan additive pada optional field tetap v1.
- Perubahan required field, enum removal, atau perubahan makna memakai v2/schema ID baru.
- Setiap OpenAPI release mengunci hash schema bundle.
- Frontend-generated type tidak diedit manual.
- Unknown response field harus diabaikan; unknown request field ditolak pada boundary dengan `additionalProperties: false`.

## 7. Validasi berlapis

```text
JSON Schema
    -> bentuk, required field, enum, range dasar

domain validator
    -> option reference, ownership, status transition, content version

mathematical validator
    -> answer, formula, unit, unique correctness

AI/risk policy
    -> taxonomy, uncertainty, OOD, agreement

psychometric policy
    -> empirical item behavior
```

JSON Schema tidak boleh dipakai untuk mengklaim soal benar secara matematis atau pedagogis.
