# Frontend Integration Adapter

UI anotasi blind tersedia pada `/internal/v2/ui/login` dan `/internal/v2/ui`. UI siswa/teacher authoring baru masih target, tetapi backend delivery fixed-form dan CTT/IRT kini tersedia. Frontend memakai kontrak [OpenAPI aktual](schemas/openapi.json).

## Port siswa

```ts
type AssessmentPort = {
  start(assessmentId: string, idempotencyKey: string): Promise<SessionReceipt>;
  nextItem(sessionId: string): Promise<DeliveredItem | DeliveryFinished>;
  submitResponse(input: ResponseCreate): Promise<ResponseReceipt>;
  complete(sessionId: string, idempotencyKey: string): Promise<SessionCompleted>;
};
```

Adapter memakai participant Bearer pada Authorization. Start/complete membawa Idempotency-Key; submit memakai responseId yang sama pada header/body. Saat retry, ID dan body dipertahankan. Pilihan UI memakai opaque public ID, bukan label A/B atau internal key.

Student state hanya berisi session/delivery, teks/stimulus, opsi dan timing. Tidak ada correctAnswer, AI label, intended difficulty atau solution. Receipt tidak menampilkan correctness. Skip merupakan aksi eksplisit dengan skipped=true dan selectedOptionIds kosong.

Alur: start → GET next → pilih satu opsi/skip → submit → next; finished=true → complete. Refresh GET mempertahankan delivery yang sama. Token tidak boleh dipakai lintas assessment. Penanganan 409 menampilkan expired/finalized/held state, bukan membuat jawaban atau opsi baru sendiri.

## Port operator dan ahli

Operator menyediakan assessment dan participant code. Service credential hanya pada backend/operator terpercaya, tidak dipaketkan dalam frontend siswa. Capabilities tersedia pada `/api/v1/capabilities`; psychometrics-info memberi local readiness tanpa network call.

Staff membaca snapshot/agregat; ahli membaca flags/CI/IRT diagnostics lalu memutuskan retain/revise/quarantine dengan cookie + CSRF. UI tidak otomatis mempromosikan item atau model dari estimated status. Gold initial annotation tetap blind: keluaran AI/peer/empirical bukan isi assignment awal.

Cookie auth path kini /, HttpOnly/SameSite lax, Secure di luar development. CSRF disimpan sesuai UI internal yang ada; jangan menyimpan credential pada dokumentasi/artefak publik. Route /api/v1 memakai Cache-Control no-store.

## Batas fitur

Backend aktif mendukung single-choice tekstual, transkripsi visual, fixed form dan completion seluruh item. Aset siswa privat, essay/numeric/grid/matching/multiple-response, CAT, exposure control, public authoring dan controlled generator masih target.

`scripts/review_app.py` tetap UI staging legacy, bukan workflow gold atau delivery. `soal_pretest_db.json` tidak boleh diberikan langsung ke browser karena mengandung kunci. Lihat [06](06_STUDENT_RESPONSE_API.md), [08](08_ASSESSMENT_DELIVERY_API.md), [27](27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md).
