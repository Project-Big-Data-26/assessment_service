# Adapter frontend silver

Frontend operator mengelola snapshot, assessment, peserta dan pekerjaan analisis. Frontend siswa hanya mengirim pilihan opaque, waktu jawaban dan skip. Pelabelan pedagogis dilakukan AI; halaman assignment dan adjudikasi pelabel manusia sudah dihapus.

| Operasi | Endpoint | Kredensial |
|---|---|---|
| Registrasi silver | `POST /api/v1/internal/silver/snapshots` | Service key atau cookie operator + CSRF |
| Blueprint | `POST /api/v1/internal/assessments` | Service key atau cookie operator + CSRF |
| Peserta | `POST /api/v1/internal/assessments/{id}/participants` | Service key atau cookie operator + CSRF |
| Mulai sesi | `POST /api/v1/assessments/{id}/sessions` | Participant Bearer + Idempotency-Key |
| Ambil soal | `GET /api/v1/sessions/{id}/items/next` | Participant Bearer |
| Jawaban | `POST /api/v1/responses` | Participant Bearer + Idempotency-Key=responseId |
| Selesai | `POST /api/v1/sessions/{id}/complete` | Participant Bearer + Idempotency-Key |
| Analisis | `POST /api/v1/internal/psychometrics/screen` | Service key atau cookie operator + CSRF |
| Feedback sistem | `GET /api/v1/internal/psychometrics/snapshots/{id}/decisions` | Service key atau cookie operator |

Service key disimpan di backend integrasi, bukan pada browser siswa. Respons API error memakai `detail`. Retry mengirim body dan idempotency key yang sama. Snapshot yang sama tidak dapat didaftarkan dengan isi berbeda.

Tampilkan kesulitan awal silver dan kesulitan empiris sebagai field berbeda pada UI operator. UI siswa tidak menerima kunci, solusi, label internal atau identity version. `reviewRequired` berarti kebutuhan pemeriksaan otomatis AI/teknis dan tidak membuka tugas guru.
