# Master Reference Endpoint

## 1. Legenda

| Visibility | Arti |
|---|---|
| `public-teacher` | Dipanggil teacher frontend dengan auth/ownership |
| `public-student` | Dipanggil student assessment frontend dengan session |
| `public-read` | Read-only sesuai authorization |
| `internal` | Service-to-service; tidak masuk public frontend SDK |

Status: `implemented`, `prototype`, atau `target`.

## 2. Foundation

| Method | Path | Visibility | Status | Fungsi |
|---|---|---|---|---|
| GET | `/api/v1/health` | public-read | target | Liveness gateway baru; FastAPI prototype memiliki health sendiri |
| GET | `/api/v1/capabilities` | public-read | target | Feature flags dan contract URLs |

## 3. Teacher authoring

| Method | Path | Visibility | Status | Side effect/idempotency |
|---|---|---|---|---|
| POST | `/api/v1/questions/validate` | public-teacher | target | Tidak menyimpan; aman diulang |
| POST | `/api/v1/questions` | public-teacher | target | Membuat draft; wajib idempotency key |
| GET | `/api/v1/questions` | public-teacher | target | List milik teacher; cursor pagination |
| GET | `/api/v1/questions/{questionId}` | public-teacher | target | Read authoring + safe summary |
| PUT | `/api/v1/questions/{questionId}/draft` | public-teacher | target | Version baru; wajib `If-Match` |
| POST | `/api/v1/questions/{questionId}/submit` | public-teacher | target | Membuat workflow job; idempotent by key/version |

Teacher tidak mempunyai endpoint approve, annotation, final label, atau adjudication.

## 4. Extraction

| Method | Path | Visibility | Status | Fungsi |
|---|---|---|---|---|
| POST | `/api/v1/extractions` | public-teacher | target | Upload dan queue extraction |
| GET | `/api/v1/extractions/{jobId}` | public-teacher | target | Poll result/candidate |
| POST | `/api/v1/questions/from-extraction` | public-teacher | target | Membuat author draft dengan lineage |
| POST | `/api/v1/ai/extract` | public-teacher | removed legacy | Ada hanya pada gateway yang telah dihapus |

## 5. Workflow dan AI read model

| Method | Path | Visibility | Status | Fungsi |
|---|---|---|---|---|
| GET | `/api/v1/workflow-runs/{runId}` | public-read | target | Poll pipeline status |
| GET | `/api/v1/questions/{questionId}/ai-decisions` | public-read | target | Safe decision history sesuai role |
| GET | `/api/v1/ai-decisions/{decisionId}` | public-read | target | Safe/restricted view berdasarkan role |
| GET | `/api/v1/ai/model-info` | public-read | target | Kemampuan classifier/verifier |
| POST | `/api/v1/ai/classify-question` | internal/debug | target | Direct screening; normal flow via submit |

## 6. Internal AI orchestration

| Method | Path | Visibility | Status | Fungsi |
|---|---|---|---|---|
| POST | `/api/v1/internal/ai/verify-answer` | internal | target | SymPy/rule/LLM verification |
| POST | `/api/v1/internal/ai-decisions/screen` | internal | target | IndoBERT lalu Claude, per head |

## 6A. Validasi tiga pakar

| Method | Path | Visibility | Status | Fungsi |
|---|---|---|---|---|
| POST | `/api/v1/expert-annotations/initial` | expert-only | target | Simpan penilaian blind immutable |
| POST | `/api/v1/expert-annotations/{annotationId}/ai-review` | expert-only | target | Review usulan Claude setelah blind lock |
| GET | `/api/v1/expert-decisions/{decisionId}` | expert/admin | target | Keputusan manusia per head |
| POST | `/api/v1/internal/expert-decisions/{questionId}/resolve` | internal | target | Voting 3-0/2-1 dan eskalasi 1-1-1 |

## 7. Controlled generation

| Method | Path | Visibility | Status | Fungsi |
|---|---|---|---|---|
| POST | `/api/v1/internal/item-models` | internal | target | Membuat versioned item model |
| POST | `/api/v1/internal/item-models/{id}/validate` | internal | target | Dry-run/property validation |
| POST | `/api/v1/internal/generation/jobs` | internal | target | Batch generate variants |
| GET | `/api/v1/generation/jobs/{jobId}` | public-read/internal | target | Status generation |
| GET | `/api/v1/item-families/{familyId}/variants` | public-read/internal | target | Variant list sesuai redaction |
| GET | `/api/v1/variants/{variantId}` | public-read/internal | target | Variant DTO sesuai role |
| POST | `/api/v1/internal/variants/{variantId}/screen` | internal | target | Quality/taxonomy gate |
| POST | `/api/v1/internal/variants/{variantId}/regenerate` | internal | target | Regeneration command |

Generation dipicu policy/workflow, bukan teacher mengedit parameter internal atau memilih output yang melewati gate.

## 8. Assessment delivery

| Method | Path | Visibility | Status | Fungsi |
|---|---|---|---|---|
| POST | `/api/v1/assessments/{assessmentId}/sessions` | public-student | target | Membuka session |
| GET | `/api/v1/sessions/{sessionId}/items/next` | public-student | target | Immutable public item DTO |
| POST | `/api/v1/responses` | public-student | target | Server-scored response event |
| POST | `/api/v1/sessions/{sessionId}/complete` | public-student | target | Finalize session |

## 9. Psychometrics

| Method | Path | Visibility | Status | Fungsi |
|---|---|---|---|---|
| GET | `/api/v1/psychometrics/items/{questionId}/snapshots` | public-read | target | Question-version quality summary |
| GET | `/api/v1/psychometrics/variants/{variantId}/snapshots` | public-read | target | Variant metrics |
| GET | `/api/v1/psychometrics/families/{familyId}/snapshots` | public-read | target | Family stability |
| POST | `/api/v1/internal/psychometrics/item-analysis` | internal | prototype/target | Stateless analysis |
| POST | `/api/v1/internal/psychometrics/items/{questionId}/screen` | internal | target | Persist snapshot dan route |

## 10. Alur teacher

```text
manual input atau extraction
    -> validate
    -> create author_draft
    -> revise jika perlu
    -> submit
    -> poll workflow
        -> pending_expert_review
        -> expert_validated
        -> provisional
        -> revision_required: teacher membuat content version baru
        -> quarantined: tidak dipaksa lolos
```

## 11. Alur otomatis

```text
submit
  -> canonicalize
  -> deterministic validate
  -> verify answer
  -> feature/KKO extraction
  -> IndoBERT 3 head
  -> Claude proposal
  -> three blind expert annotations + AI review
  -> 3-0/2-1 atau adjudikasi manusia
  -> expert_validated/provisional atau quarantine
  -> optional controlled generation
  -> delivery/pilot
  -> psychometrics
```

## 12. Alur student

```text
start session
    -> receive delivered item without key
    -> submit response by deliveryInstanceId
    -> server-side score
    -> next item
    -> complete
```

## 13. Endpoint legacy yang dihapus dari target

```text
POST /verifications/educator
GET  /verifications/educator/demo
POST /api/v1/internal/ai-decisions/{decisionId}/adjudicate
```

Endpoint tersebut berasal dari gateway lama yang sudah dihapus, bukan bagian arsitektur target. Endpoint `expert-annotations` baru berbeda karena mewajibkan tiga identitas pakar, blind lock, dan version binding.
