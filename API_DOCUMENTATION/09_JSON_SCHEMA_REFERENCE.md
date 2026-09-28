# JSON Schema Reference

## 1. Tujuan

JSON Schema publik berada pada:

[`schemas/nalar-api.schema.json`](schemas/nalar-api.schema.json)

Bundle memakai JSON Schema Draft 2020-12 dan `$defs` agar satu sumber dapat dipakai untuk:

- validasi pada gateway target (AJV bila memilih Node);
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
| `MathCognitiveDomain` | Enum Head 1: knowing/applying/reasoning |
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
- `multiple_response` memakai beberapa `optionIds`; `true_false` memakai tepat dua opsi dan satu `optionId`. `matching` memakai `matchingLeft/matchingRight` serta `matching_pairs`; `interactive_grid` memakai `gridAssetId/gridCells` terkoordinat relatif 0–1 dan `grid_cell_ids`. `essay` memakai rubrik dan penilaian manusia, bukan key otomatis. Tipe dan konstruk kognitif tidak berkorespondensi satu-ke-satu.
- Domain validator tetap wajib memeriksa ID unik, referensi jawaban yang ada, keunikan pasangan, batas `x+width`/`y+height`, jumlah pilihan benar, dan keamanan aset; JSON Schema tidak membuktikan hal tersebut.
- Teacher tidak mengirim `status`, `contentVersion`, AI label, risk, atau psychometric result.
- LaTeX tetap berupa string dan harus menjalani render/sanitization terpisah.

## 4. Aturan delivery dan response

- `DeliveredItem` tidak memiliki `answerSpec`, internal option ID, explanation, atau solution trace.
- `ResponseCreate` wajib berisi tepat satu bentuk jawaban yang sesuai tipe item: `selectedOptionIds`, `numericAnswer`, `textAnswer`, `matchingPairs`, atau `selectedGridCellIds`. Keselarasan dengan tipe item dan ID publik diperiksa server-side.
- `responseId` dan `deliveryInstanceId` wajib agar retry aman dan version join tidak ambigu.
- `isCorrect`, `studentHash`, `questionId`, dan `assessmentId` tidak diterima dari browser sebagai sumber kebenaran.

## 5. Aturan AI dan psychometric

- Math cognitive domain enum: `knowing`, `applying`, `reasoning`.
- Knowledge enum: `factual`, `conceptual`, `procedural`, `metacognitive`.
- Difficulty enum: `Easy`, `Medium`, `Hard`.
- `decisionType` membedakan `indobert_prediction`, `claude_proposal`, `expert_validated`, dan `quarantined`.
- `expert_validated` mensyaratkan keputusan tiga ahli terpisah yang mengikat `contentVersion`; AI summary tidak boleh menjadi sumber status tersebut.
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
    -> IndoBERT, Claude proposal, uncertainty, OOD

expert decision
    -> tiga blind annotations, review AI, voting/adjudication per head

psychometric policy
    -> empirical item behavior
```

JSON Schema tidak boleh dipakai untuk mengklaim soal benar secara matematis atau pedagogis.

Bundle JSON di folder ini mencakup schema arsitektur lebih luas. FastAPI `/v2` kini memiliki kontrak Pydantic 3×4×3 sendiri, sedangkan `/v1` tetap Bloom C1–C6. Endpoint fase lanjut yang belum ada tetap berstatus target; OpenAPI runtime adalah sumber kebenaran endpoint yang benar-benar aktif.

## 8. Schema staging pretest

Output agentic tidak divalidasi oleh `schemas/nalar-api.schema.json`. Sumber kebenarannya saat ini adalah Pydantic strict model pada `app/services/pretest/agentic/schema.py`, sedangkan validasi lintas-file/sumber berada pada `validate.py`. Pemisahan ini disengaja:

```text
BabFile/Soal (internal staging, snake_case)
    -> validator evidence terhadap halaman buku
    -> import adapter
    -> QuestionCreate/QuestionVersion (public/target, camelCase)
```

Importer `app/ingestion/pretest_import.py` menolak unknown field melalui Pydantic staging, menyimpan pipeline version, hash/provenance, dan menghasilkan content version dari `babNN.json`. `soal_pretest_db.json` tidak menjadi sumber kanonis dan model Beanie lama tidak dipakai oleh workflow v2. Rincian kontrak ada pada [dokumen 21](21_PRETEST_AGENTIC_PIPELINE_INTEGRATION.md).
