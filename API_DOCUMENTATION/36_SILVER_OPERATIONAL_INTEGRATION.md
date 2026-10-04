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
format **array dokumen**, sama seperti `soal_pretest_db.json`: tidak ada envelope
`items`/`summary` atau field tambahan `ai_metadata` pada baris database. Setiap dokumen
mempertahankan seluruh 16 field sumber, urutan soal, teks, opsi, gambar dan kunci jawaban.
Identitas format `validated-question-array-v4-active-status`, summary, provenance, track, identitas
snapshot dan profil head 2/3 berada di `manifest.json.databaseExport`.

| Field | Sumber / makna |
|---|---|
| `cognitive_level` | Label difficulty final AI dalam huruf kecil: easy, medium, hard |
| `cognitive_score` | Skor awal dari intended difficulty: Easy=600, Medium=1000, Hard=1400 |
| `confidence_score` | Integer 0-100: dukungan run awal terhadap label final, minimum dari tiga head |
| `status` | active untuk silver_ready; inactive untuk revision_required atau needs_ai_review |

Metadata per soal ada di `manifest.json.databaseExport.metadataByQuestionId["<_id>"]`:
`label_provenance`, `knowledge_dimension`, `intended_difficulty`, `validation_status`,
`subject_track`, `decision_id`, `question_version_id`, `content_hash`, dan
`final_label_supporting_runs`, serta `math_cognitive_domain` untuk knowing/applying/reasoning.
Item yang ditahan tetap memiliki ID versi/hash operasional null. Field database
`cognitive_level` adalah difficulty sesuai kontrak integrasi; head domain kognitif
tetap terpisah dalam metadata dan audit, bukan diganti dalam model atau dataset training.

`cognitive_score` memakai skala yang sama dengan target skor generator exercise. Skor
ini **bukan** nomor kategori knowing/applying/reasoning, skor kemampuan siswa, hasil
kalibrasi IRT, atau confidence. Head kognitif dan skor kesulitan tetap berbeda.

Untuk setiap head `h`, hitung `n_h` dari run awal berstatus `success`, action `classify`,
dan label yang sama dengan **label final setelah adjudikasi**. Dengan `N=requestedRuns`:

```text
confidence_score = round(100 × min(n_domain/N, n_knowledge/N, n_difficulty/N))
```

Contoh label final knowing/procedural/Easy, dukungan 3/1/3, N=3: confidence=33.
Dukungan minimum 2/3 menghasilkan 67; 3/3 menghasilkan 100. Denominator tetap run
yang diminta: run gagal, abstain atau belum tersedia tidak menambah dukungan.
Adjudikasi menentukan label final tetapi tidak dihitung sebagai suara keempat.
`votes.supportingVotes` tidak dipakai karena dapat menunjuk mayoritas awal yang
berbeda dari label final. Confidence ini mengukur **konsistensi AI**, bukan probabilitas
akurasi atau confidence IndoBERT. Nilai 100 tidak menjamin isi/kunci benar; routing
tetap penentu kelayakan. Tidak ada threshold baru atau penggabungan skor model 40/60.

Untuk delivery, filter `status == "active"`. Semua 580 soal tetap diekspor:
571 active dan 9 inactive. Routing validasi asli (`silver_ready`, `revision_required`,
`needs_ai_review`) tetap ada pada metadata `validation_status` dan audit. Soal inactive disimpan sebagai held,
tetapi tidak boleh diberikan kepada siswa meskipun ketiga kolom klasifikasi terisi.
Jika label difficulty belum tersedia pada batch berikutnya, score tetap null dan
item harus ditahan; tidak ada label/skor pengganti yang dibuat-buat.

Keputusan lengkap dipertahankan byte demi byte di
`hasil_validasi/bukti_validasi/decision_audit.json`. `databaseExport.decisionAudit` pada manifest
menyimpan path relatif dan SHA-256; manifest juga memverifikasi file tersebut.
Pembaca internal memakai `app.silver.exports.load_decision_bundle`, yang mendukung
format laporan lama, envelope ringkas lama, array v2 (domain), v3 (difficulty),
serta v4 (active/inactive). Builder snapshot tetap memeriksa bukti, kunci,
solusi dan aset. Kontrak HTTP assessment, scoring dan IRT tetap menggunakan snapshot.
JSON ringkas berisi kunci jawaban dan hanya untuk integrasi backend.

Konversi aktif dapat diulang secara offline dengan
`scripts/compact_validation_results.py`; builder blind juga menghasilkan format ini
untuk batch berikutnya. Consumer database membaca array langsung, tanpa `.items`.
Consumer laporan yang membaca `items[].llmAdvisory` atau `items[].finalRouting`
perlu memakai loader audit. Format ini bukan payload registrasi `DatasetSnapshot`.

Seeder backend melakukan upsert by `_id` dan tetap memetakan `kelas_id`, `berkas_id`,
serta nama `subbab_id` ke ID collection bila diperlukan; nilai tersebut mengikuti
sumber dan tidak ditebak exporter. `image_url` tetap relatif terhadap folder kelas
sumber, bukan `hasil_validasi`. Backend perlu mendukung string easy/medium/hard dan
status active/inactive, integer skor 600/1000/1400, dan confidence integer 0-100. Ekspor ini
tidak melakukan insert database atau mengubah model backend.

`output/pretest/silver_operational/database_format_verification.json` mencatat
verifikasi seluruh kelas: cakupan, field, sumber, audit, label, skor dan manifest.

`scripts/migrate_silver_operational.py` memverifikasi dan mengarsipkan laporan sebelum mengganti routing aktif. Label, run, prompt hash, response hash, checkpoint dan sumber tidak diubah. Archive memuat histori kebijakan terdahulu; teks prompt/rubrik lama tetap dipertahankan untuk verifikasi bukti.

Migrasi tidak menjalankan provider, tidak membuat respons siswa, tidak retrain, dan tidak mempromosikan model. Uji integrasi memakai data synthetic serta snapshot silver lokal. Snapshot/model historis tidak diberi provenance baru secara paksa.
