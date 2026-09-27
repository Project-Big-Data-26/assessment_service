# Penjelasan Sistem Nalar per Aspek

## 1. Ringkasan posisi sistem

Nalar adalah target sistem untuk:

1. menerima soal manual atau sumber file dari teacher;
2. membentuk canonical question berversi;
3. memverifikasi struktur dan jawaban secara otomatis;
4. melakukan taxonomy screening melalui IndoBERT dan LLM;
5. memakai LLM adjudicator bila model berbeda;
6. menghasilkan variasi soal secara terkontrol;
7. menyajikan item melalui secure delivery;
8. mengukur kualitasnya dari response events;
9. memperbaiki generator dan model dengan bukti empiris.

Teacher tetap berada dalam sistem sebagai author, tetapi tidak menjadi reviewer atau adjudikator.

## 2. Mengapa teacher hanya author

Teacher memahami soal yang ingin dimasukkan, sehingga teacher boleh:

- menulis atau mengimpor konten;
- memperbaiki OCR/formula/options;
- memberi learning objective, topic, grade, kunci, dan penjelasan;
- membuat revision setelah menerima warning sistem.

Teacher tidak diminta menilai output model agar:

- frontend authoring tetap sederhana;
- label tidak bergantung pada jumlah/ketersediaan reviewer;
- keputusan otomatis dapat direplay dan diaudit;
- peran input content tidak tercampur dengan sumber bukti klasifikasi.

Konsekuensinya, sistem tidak mempunyai expert gold label runtime. Klaimnya dibatasi menjadi `model_suggestion`, `ai_consensus`, `ai_adjudicated`, `provisional`, dan `empirically_screened`.

## 3. Sumber bukti yang dipisahkan

```text
teacher authoring content
    -> apa soal yang dimasukkan

deterministic validation
    -> apakah bentuk/constraint pasti terpenuhi

answer verification
    -> apakah kunci konsisten dengan solver/rules

IndoBERT + LLM
    -> klasifikasi teoretis dan uncertainty

psychometrics
    -> perilaku item pada populasi/assessment tertentu
```

Tidak ada satu sumber yang menjawab semua pertanyaan. Agreement AI tidak membuktikan kebenaran absolut; psikometrik tidak membuktikan Bloom; teacher input tidak menjadi label final.

## 4. Authoring dan extraction

Teacher mempunyai dua jalur:

```text
manual authoring
    -> author_draft

file upload
    -> extraction candidate
    -> teacher corrects authoring content
    -> author_draft
```

OCR adalah transformasi probabilistik. Teacher memperbaiki hasil sebagai penulis karena hanya teacher yang mengetahui teks yang ingin dimasukkan; tindakan ini bukan proses validasi pedagogis akhir.

Setelah submit, version dibekukan untuk satu workflow run. Perubahan berikutnya membuat content version baru.

## 5. Validasi otomatis berlapis

```text
Layer 1: API/schema/security
Layer 2: canonicalization dan deterministic structure
Layer 3: answer verification
Layer 4: IndoBERT dan independent LLM screening
Layer 5: agreement/risk dan LLM adjudication
Layer 6: provisional delivery/pilot
Layer 7: empirical psychometric screening
Layer 8: drift dan model/generator monitoring
```

Contoh routing:

- schema salah dan dapat diperbaiki teacher -> `revision_required`;
- key tidak cocok dengan SymPy -> `quarantine_answer_conflict`;
- IndoBERT/LLM berbeda -> automated adjudication;
- adjudication tidak stabil -> `quarantine_ai_conflict`;
- item lolos seluruh gate -> `provisional`;
- discrimination negatif setelah pilot -> auto-unpublish/quarantine.

## 6. Klasifikasi taksonomi

Model memprediksi tiga head:

```text
Bloom:       C1-C6
Knowledge:   factual/conceptual/procedural/metacognitive
Difficulty:  Easy/Medium/Hard (intended)
```

Input harus mencakup teks, opsi, objective, topic/subtopic, grade, formula, dan metadata relevan. KKO saja tidak cukup karena kata seperti “tentukan” dapat muncul pada proses kognitif berbeda.

IndoBERT menyediakan probabilitas/uncertainty. LLM memakai rubric dan evidence span. Keduanya diproses independen sebelum agreement.

## 7. LLM adjudicator

LLM adjudicator bukan manusia digital yang selalu benar. Ia adalah tahap arbitration terkontrol:

- dijalankan hanya jika ada disagreement/risk tertentu;
- memakai prompt/rubric/model alternatif;
- melihat bukti yang terversi;
- mempunyai batas percobaan;
- dapat abstain;
- menghasilkan decision event dan provenance;
- unresolved case selalu quarantine.

Sistem tidak memilih label hanya berdasarkan confidence terbesar.

## 8. Controlled generation

Generasi soal dimulai dari `verified_parent_item`, bukan OCR mentah.

```text
verified parent
    -> item model
    -> parameter generator atau isomorphic candidate generator
    -> recompute answer
    -> misconception distractors
    -> deterministic/construct gate
    -> AI screen
    -> provisional variant
```

Parameter generator bersifat deterministic-first. LLM dipakai untuk konteks/redaksi dan proposal miskonsepsi, bukan sebagai otoritas jawaban. Detail terdapat pada dokumen 16.

## 9. Range dan difficulty

Range angka bukan angka arbitrer. Allowed domain merupakan irisan:

```text
mathematical rules
∩ construct policy
∩ grade number profile
∩ intended-difficulty profile
∩ operational constraints
```

Generator memakai constructive strategy, misalnya memilih akar dahulu untuk membentuk persamaan kuadrat. Random hanya memilih dari domain yang sudah valid.

Difficulty dibedakan:

- `intendedDifficulty`: target desain/AI sebelum digunakan;
- `empiricalDifficulty`: hasil response pada populasi dan assessment tertentu.

Mismatch adalah informasi perbaikan, bukan alasan otomatis mengganti Bloom.

## 10. Item family dan variant

```text
Question parent
    -> Item family
        -> Item model v1
            -> Variant A
            -> Variant B
        -> Item model v2
            -> Variant C
```

Setiap variant menyimpan parameter snapshot, seed, generator version, transformation trace, answer verification, dan decision. Statistik per variant tidak boleh hilang karena family aggregation.

Seluruh sibling satu family ditempatkan pada split dataset yang sama untuk mencegah leakage.

## 11. Delivery dan scoring

Student UI hanya menerima public item DTO:

- delivery instance;
- question text/media;
- public option IDs;
- sequence/timing.

Kunci, solution trace, misconception code, internal option ID, family relation, dan model trace tidak dikirim. Response menggunakan `deliveryInstanceId`; correctness dihitung server.

## 12. Response dan privacy

Response event menyimpan pseudonymous subject hash, version join, selected internal mapping, score, timing, answer changes, dan flags. Ia tidak menyimpan NISN/nama/email siswa.

Idempotency mencegah retry menggandakan event. Event dan decision history append-only.

## 13. Psychometrics

MVP memakai Classical Test Theory:

- difficulty index dan confidence interval;
- upper-lower discrimination;
- corrected point-biserial jika total score tersedia;
- distractor selection/efficiency;
- median/IQR response time;
- rapid-guess/anomaly rate.

Analisis selalu terikat population, assessment family, content/variant version, dan time window. IRT adalah future extension setelah linking design dan data memadai.

## 14. Feedback loop

Psychometric evidence dapat memperbaiki:

- range dan probability parameter;
- difficulty profile;
- distractor rule;
- transformation policy;
- item-quality/difficulty model heads.

Ia tidak digunakan secara buta untuk mengubah Bloom/knowledge. Snapshot dengan bukti lemah tetap `observation_only`.

## 15. Frontend copot-pasang

Frontend hanya bergantung pada gateway, generated DTO, dan empat port:

- teacher authoring;
- extraction;
- workflow status;
- assessment delivery/response.

UI prototype boleh dibongkar setelah consumer contract test tersedia. Internal service dan MongoDB tidak berubah ketika frontend diganti.

## 16. MongoDB

MongoDB sesuai untuk aggregate document dan event yang berkembang, tetapi fleksibilitasnya tidak menggantikan schema. Prinsip penyimpanan:

- embed data kecil dan bounded;
- reference history/event yang unbounded;
- question identity dipisahkan dari immutable versions;
- response/decision/snapshot append-only;
- index unik dan compound mengikuti join key;
- public DTO tidak sama dengan database document.

Detail terdapat pada dokumen 17.

## 17. Security

Sebelum production diperlukan:

- authentication/authorization dan ownership;
- service identity internal;
- MIME signature, antivirus, checksum, size limit;
- server-side scoring dan identity;
- rate limit/idempotency;
- audit, retention, encryption, secret management;
- prompt/input/output logging dengan redaction;
- dependency/model supply-chain policy.

## 18. Status implementasi

| Area | Status |
|---|---|
| FastAPI extraction/classification | Prototype tersedia |
| Express gateway dan MongoDB Question/Response | Prototype tersedia, schema lama |
| Rules baseline | Tersedia sebagai advisory |
| IndoBERT definition/training code | Ada; production artifact belum menjadi bukti siap |
| CTT dasar | Prototype tersedia |
| Teacher/student UI | Prototype/debug surface |
| Human annotation/educator verification | Legacy; dikeluarkan dari target |
| Async job, answer verifier, LLM ensemble/adjudicator | Target |
| Controlled generation | Target |
| Secure delivery/server scoring | Target |
| Immutable version/event model | Target |
| Psychometric feedback training/deployment automation | Target/future |

## 19. MVP yang disarankan

```text
teacher authoring + versioning
    -> submit job
    -> deterministic validation + SymPy answer verification
    -> limited taxonomy screening
    -> 2-3 deterministic item families
    -> delivery instance + server scoring
    -> response events
    -> CTT per version/variant
```

LLM isomorphic generation, full adjudication, multi-provider, IRT, and automated champion-challenger ditambahkan setelah vertical slice stabil.

## 20. Klaim yang aman

Sistem boleh disebut prototype controlled generation dan automated screening. Hindari klaim:

- menggantikan pakar secara absolut;
- menghasilkan gold label;
- semua variant isomorfik;
- difficulty universal;
- semua 72 kombinasi telah valid;
- psychometrics membuktikan Bloom;
- semua endpoint target sudah terimplementasi.

