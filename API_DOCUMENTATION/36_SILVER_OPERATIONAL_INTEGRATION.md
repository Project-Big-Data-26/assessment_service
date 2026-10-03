# Integrasi operasional silver -> API 2.2.0

Semua label operasional memiliki provenance `ai_silver`. Pelabelan manusia, pembentukan gold dan keputusan empiris manual telah dihapus. Authentication operator dan service tetap tersedia untuk integrasi.

## Kontrak yang berubah

- Endpoint assignment, diskusi/adjudikasi pelabel dan workspace annotation dihapus.
- POST `/api/v1/internal/psychometrics/snapshots/{id}/decisions` dihapus; GET mengembalikan keputusan otomatis.
- Registrasi `POST /api/v1/internal/silver/snapshots` menerima `DatasetSnapshot` yang qualified dan immutable.
- Create assessment membaca snapshot SQLite; service integration tidak membutuhkan MongoDB.
- `AssessmentCreate.grade` menjadi 1-12; `subjectTrack=regular|tl`, TL hanya 11-12.
- `TrainingRow` menggantikan nama lama; `DatasetSnapshot.expansionHash` melindungi kelas di luar scope training SD.
- `reviewRequired` berarti pemeriksaan otomatis; `reviewMode=automated_ai`. Field `humanValidation` dan gold labels dihapus dari laporan aktif.
- CLI assessment memakai `--silver-snapshot`; freeze memakai builder silver offline.

## Contoh sambungan

Bekukan snapshot baru:

```powershell
.\.venv\Scripts\python.exe scripts/build_operational_silver.py --snapshot-id silver-next-v1 --output tmp/silver-next.json --assessment-db data/local/assessments.sqlite3
```

Pilihan `--assessment-db` mendaftarkan dataset dan mengecualikan versi yang held. Jika memakai HTTP, kirim JSON snapshot ke endpoint registrasi dengan `X-Internal-API-Key`, lalu kirim blueprint ke `/api/v1/internal/assessments`. Gunakan versi yang tersedia pada `rows` atau `expansionRows` dengan grade/track cocok.

Setelah session siswa selesai, panggil `/api/v1/internal/psychometrics/screen`. Scheduler integrasi menentukan waktu analisis. Feedback otomatis memakai `retain`, `collect_more_events` atau `needs_ai_review`. Hold membutuhkan perbaikan/validasi ulang AI; tidak ada tombol guru untuk memberi label final.

Label domain/knowledge/intended tetap berasal dari AI. IRT menyimpan difficulty empiris terpisah, sehingga pergeseran empiris tidak mengubah dataset awal. Mutu kunci, visual, provenance, split, training dan asumsi IRT tetap diperiksa.

## Data lama dan migrasi

Laporan aktif `output/pretest/kelas*/hasil_validasi/validation_results.json` memakai
`schemaVersion=validated-question-bundle-v1-ai-metadata`. Envelope tetap menyediakan
`summary` dan `items`; setiap item mempertahankan field soal sumber dan menambahkan
`ai_metadata`. Tidak ada soal baru atau perubahan teks, opsi, gambar dan kunci jawaban.

| Field | Sumber / makna |
|---|---|
| `cognitive_level` | Label final AI: knowing, applying, reasoning |
| `ai_metadata.label_provenance` | ai_silver |
| `ai_metadata.knowledge_dimension` | Label final factual, conceptual, procedural, metacognitive |
| `ai_metadata.intended_difficulty` | Label final Easy, Medium, Hard; terpisah dari difficulty empiris |
| `ai_metadata.validation_status` | silver_ready, revision_required, needs_ai_review |
| `ai_metadata.subject_track` | regular atau tl |
| `ai_metadata.decision_id` | Referensi `decisionId` dalam audit lengkap |
| `ai_metadata.question_version_id` | ID immutable yang sama dengan versi snapshot delivery |
| `ai_metadata.content_hash` | Hash konten operasional yang sama dengan snapshot |

`cognitive_score` dan `confidence_score` bernilai null: kode domain kognitif bukan
skor kemampuan, dan confidence IndoBERT tidak mewakili probabilitas kebenaran label
final AI. Item yang ditahan memiliki ID versi/hash operasional null. Filter delivery
harus memakai `ai_metadata.validation_status == "silver_ready"`, bukan `status` lama.

Keputusan lengkap dipertahankan byte demi byte di
`hasil_validasi/bukti_validasi/decision_audit.json`. `decisionAudit` pada envelope
menyimpan path relatif dan SHA-256; manifest juga memverifikasi file tersebut.
Pembaca internal memakai `app.silver.exports.load_decision_bundle`, yang mendukung
format lama serta format ringkas. Builder snapshot tetap memeriksa bukti, kunci,
solusi dan aset. Kontrak HTTP assessment, scoring dan IRT tetap menggunakan snapshot.
JSON ringkas berisi kunci jawaban dan hanya untuk integrasi backend.

Konversi aktif dapat diulang secara offline dengan
`scripts/compact_validation_results.py`; builder blind juga menghasilkan format ini
untuk batch berikutnya. Consumer eksternal yang membaca field
`items[].llmAdvisory` atau `items[].finalRouting` perlu memakai mapping di atas
atau membaca file audit. Format ini bukan payload registrasi `DatasetSnapshot`.

`scripts/migrate_silver_operational.py` memverifikasi dan mengarsipkan laporan sebelum mengganti routing aktif. Label, run, prompt hash, response hash, checkpoint dan sumber tidak diubah. Archive memuat histori kebijakan terdahulu; teks prompt/rubrik lama tetap dipertahankan untuk verifikasi bukti.

Migrasi tidak menjalankan provider, tidak membuat respons siswa, tidak retrain, dan tidak mempromosikan model. Uji integrasi memakai data synthetic serta snapshot silver lokal. Snapshot/model historis tidak diberi provenance baru secara paksa.
