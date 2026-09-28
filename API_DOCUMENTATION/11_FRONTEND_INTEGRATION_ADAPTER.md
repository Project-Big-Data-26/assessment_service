# Frontend Integration Adapter Copot-Pasang

## 1. Tujuan

Frontend boleh dibangun ulang tanpa mengubah backend selama implementasi baru memenuhi port dan DTO publik. Komponen React tidak boleh memanggil `fetch` langsung, membaca MongoDB shape, atau mengetahui provider/model AI.

```text
UI components
    -> application hooks/use-cases
        -> domain ports
            -> HTTP adapter atau mock adapter
```

## 2. Port utama

```ts
export interface TeacherAuthoringPort {
  validate(content: QuestionAuthoringContent): Promise<ValidationResult>;
  create(content: QuestionAuthoringContent, idempotencyKey: string): Promise<QuestionResource>;
  replaceDraft(questionId: string, version: number, content: QuestionAuthoringContent): Promise<QuestionResource>;
  submit(questionId: string, idempotencyKey: string): Promise<JobAccepted>;
  get(questionId: string): Promise<QuestionResource>;
}

export interface ExtractionPort {
  create(file: File, idempotencyKey: string): Promise<JobAccepted>;
  get(jobId: string): Promise<ExtractionJob>;
  createDraft(input: CreateQuestionFromExtraction): Promise<QuestionResource>;
}

export interface WorkflowPort {
  get(runId: string): Promise<WorkflowRun>;
}

export interface ExpertReviewPort {
  submitBlind(input: BlindAnnotation, idempotencyKey: string): Promise<ExpertAnnotation>;
  reviewAi(annotationId: string, input: AiReview, idempotencyKey: string): Promise<ExpertAnnotation>;
  getDecision(decisionId: string): Promise<ExpertDecision>;
}

export interface AssessmentPort {
  start(assessmentId: string, idempotencyKey: string): Promise<AssessmentSession>;
  nextItem(sessionId: string): Promise<DeliveredItem>;
  submitResponse(input: ResponseCreate, idempotencyKey: string): Promise<ResponseReceipt>;
  complete(sessionId: string, idempotencyKey: string): Promise<SessionResult>;
}
```

## 3. Adapter HTTP

Satu modul menangani:

- base URL;
- bearer token;
- idempotency key;
- `If-Match`;
- JSON parsing;
- common error envelope;
- snake/camel mapping jika internal compatibility masih diperlukan;
- request timeout/cancellation;
- schema validation optional pada development.

Komponen UI hanya menerima domain error:

```ts
type DomainErrorCode =
  | "validation_failed"
  | "version_conflict"
  | "forbidden"
  | "job_failed"
  | "quarantined"
  | "session_expired"
  | "network_unavailable"
  | "unknown";
```

## 4. Teacher authoring state

```text
idle
  -> editing
  -> validating
      -> validation_error
      -> saving
          -> saved(author_draft)
          -> version_conflict
  -> submitting
      -> processing(job polling)
          -> pending_expert_review
          -> needs_expert_adjudication
          -> expert_validated
          -> provisional
          -> revision_required
          -> quarantined
          -> failed
```

`revision_required` menampilkan warning dan membuka editor versi baru. UI teacher tidak menampilkan tombol "approve label" atau "adjudicate". UI khusus pakar menyembunyikan prediksi AI/peer sampai blind submission terkunci, kemudian menampilkan proposal Claude untuk review per head.

## 5. Extraction state

```text
idle -> selecting -> uploading -> processing
                              -> candidates
                                  -> editing authoring content
                                  -> create draft
                              -> failed/quarantined
```

Teacher memperbaiki teks, formula, opsi, dan answer input sebagai author. Hasil ekstraksi tidak langsung disubmit ke AI workflow tanpa teacher command.

## 6. Student state

```text
select assessment
    -> start session
    -> load delivered item
    -> answer locally
    -> submit response
    -> next item
    -> complete session
```

Student state tidak memiliki `correctAnswer`. Feedback hanya berasal dari response receipt jika assessment policy mengizinkan.

## 7. Struktur folder frontend

```text
src/
  domain/
    contracts/
    models/
    errors/
  application/
    teacher/
    extraction/
    assessment/
  infrastructure/
    http/
    adapters/
    generated/
    mock/
  features/
    teacher-authoring/
    extraction-import/
    student-assessment/
    status-dashboard/
    expert-review/
  shared/
    MathText/
    ErrorNotice/
    JobProgress/
```

`infrastructure/generated` berasal dari OpenAPI/JSON Schema dan tidak diedit manual. Feature component tidak mengimpor file dari backend repository.

## 8. Capability-driven UI

Frontend membaca `/capabilities` saat bootstrap. Fitur target yang belum aktif disembunyikan atau menggunakan adapter mock pada development. UI tidak mendeteksi kemampuan berdasarkan error acak atau nama model.

Contoh:

```ts
if (capabilities.features.questionGeneration) {
  registerGenerationStatusPanel();
}
```

## 9. Rendering safety

- Render LaTeX melalui KaTeX dengan konfigurasi aman.
- Jangan memakai raw HTML dari source/LLM tanpa sanitization.
- Diagram menggunakan resource URL/SVG policy yang tervalidasi.
- Preview upload memakai object URL dan direvoke.
- Tampilkan warning sebagai teks, bukan HTML.
- Jangan log token, answer key, raw prompt, atau student identity.

## 10. Cara mengganti frontend

1. Generate/import public types.
2. Implementasikan lima port utama, termasuk ExpertReviewPort pada aplikasi pakar.
3. Jalankan consumer contract tests.
4. Uji state terminal dan error envelope.
5. Uji teacher ownership dan student key isolation.
6. Jalankan against mock lalu staging gateway.
7. Ganti deployment frontend tanpa mengubah internal AI/database.

## 11. Migration dari prototype

Frontend prototype `project_assessment` sudah dihapus; struktur di atas adalah target. Sebelum frontend baru dipasang:

- hapus import seed dari production path;
- pindahkan seluruh network call ke adapter;
- gunakan Question authoring DTO baru;
- gunakan job polling;
- gunakan delivery instance;
- hilangkan `isCorrect` dari request browser;
- jangan bergantung pada field legacy `annotations`, `finalLabels`, atau educator verification; gunakan `expert_annotations` dan `expert_decisions` baru.
