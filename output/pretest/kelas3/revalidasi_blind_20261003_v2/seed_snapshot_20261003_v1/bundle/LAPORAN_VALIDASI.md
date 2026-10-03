# Validasi ulang soal kelas 3 — Gemini blind N=3 dan diagnostik IndoBERT

**Batch belum selesai:** 93/126 run awal sukses; 0 item tercatat membutuhkan adjudikasi setelah run lengkap. Distribusi berikut masih sementara; item tanpa keputusan ditampilkan sebagai undecided.

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v4-blind-key-verified`. Rubrik: `math-rubric-3x4x3-v2-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 3 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan bukan keputusan ahli manusia.

Checkpoint dikunci dengan SHA-256 sebelum inferensi IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Prediksi model lama dipakai untuk menunjukkan ketidaksepakatan; tidak diberikan kembali ke Gemini.

Jumlah soal: 42; distribusi label advisory: `{"mathCognitiveDomain": {"undecided": 11, "knowing": 5, "applying": 26, "reasoning": 0}, "knowledgeDimension": {"undecided": 11, "factual": 4, "procedural": 17, "conceptual": 10, "metacognitive": 0}, "intendedDifficulty": {"undecided": 11, "Easy": 22, "Medium": 9, "Hard": 0}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"knowing": 5, "applying": 25, "reasoning": 0}, "knowledgeDimension": {"factual": 4, "procedural": 16, "conceptual": 10, "metacognitive": 0}, "intendedDifficulty": {"Easy": 21, "Medium": 9, "Hard": 0}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"llm_retry_or_manual_review": 11, "pending_expert_review": 30, "revision_required": 1}`.
Run awal sukses: 93/126; adjudikasi: 15; token sukses tercatat: 220,776.

Seluruh label masih silver/advisory, gold manusia tetap null, dan publishing otomatis tidak diaktifkan. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

IndoBERT aktif: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Artifact belum disetujui; tidak ada training ulang dalam batch ini. Difficulty model lama dapat mengalami class collapse. Confidence dari kalibrasi kelas 1 yang kecil belum membuktikan ketepatan label.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten tetap memerlukan pemeriksaan ahli.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 22 | 21 | [Easy.json](difficulty/Easy.json) |
| Medium | 9 | 9 | [Medium.json](difficulty/Medium.json) |
| Hard | 0 | 0 | [Hard.json](difficulty/Hard.json) |

## Perhitungan yang dipakai

Encoder menghasilkan representasi [CLS], lalu tiga head menghasilkan logits. Probabilitas adalah pᵢ = exp(zᵢ/T) / Σⱼ exp(zⱼ/T), dengan temperature sesuai manifest. Confidence = max(pᵢ). Entropy H = −Σᵢ pᵢ ln(pᵢ) / ln(K). Probabilitas, confidence, entropy, dan action di bawah berasal dari inferensi lokal; tidak dibuat oleh Gemini.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

## 1. Soal `8de4f21dafd4452f79f06e71`

Perhatikan bilangan berikut: 239, 912, 821, 168.<br><br>Tentukan bilangan mana yang memiliki angka puluhan kurang dari 3?

| Opsi | Isi |
|---|---|
| A | 168 dan 821 |
| B | 239 dan 912 |
| C | 821 dan 912 |
| D | 239 dan 168 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2f8997b44bd2cc4490d0da1da62fe6065115c6319a93eac839b84febe776f3de`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 94/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |

<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Bilangan dan Lambang Bilangan Cacah sampai 1.000
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan bilangan berikut: 239, 912, 821, 168.

Tentukan bilangan mana yang memiliki angka puluhan kurang dari 3?
Pilihan: A. 168 dan 821
B. 239 dan 912
C. 821 dan 912
D. 239 dan 168
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `80e0cb21740609959b756bf3`

Tuliskan lambang bilangan dan cara membaca bilangan yang terdapat pada gambar berikut.

| Opsi | Isi |
|---|---|
| A | 236 dibaca dua ratus tiga puluh enam |
| B | 326 dibaca tiga ratus dua puluh enam |
| C | 263 dibaca dua ratus enam puluh tiga |
| D | 236 dibaca dua ratus tiga enam |

![Gambar sumber soal 2](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0026-02.png>)


Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas3_panduan_siswa_kelas3.pdf-0026-02.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menyebutkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d36e45baf9c0ac12d13093c80cfe69f9d20f24105b475371c82ab00c7702c7a5`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 91/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |

<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Bilangan dan Lambang Bilangan Cacah sampai 1.000
Tipe soal: multiple_choice
Stimulus: -
Soal: Tuliskan lambang bilangan dan cara membaca bilangan yang terdapat pada gambar berikut.
Pilihan: A. 236 dibaca dua ratus tiga puluh enam
B. 326 dibaca tiga ratus dua puluh enam
C. 263 dibaca dua ratus enam puluh tiga
D. 236 dibaca dua ratus tiga enam
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `0c970a6aff64277c753f7671`

Tuliskan bilangan yang terdiri atas 3 angka dan letakkan setiap angka sesuai nilai tempatnya. Ratusan 8, Puluhan 1, Satuan 2.

| Opsi | Isi |
|---|---|
| A | 182 |
| B | 821 |
| C | 128 |
| D | 812 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menyebutkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `40298dfaccf442c90eda9a5f3cc56f00d0311da77065bf68da178134cda432e1`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 79/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |

<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Nilai Tempat Bilangan Cacah sampai 1.000
Tipe soal: multiple_choice
Stimulus: -
Soal: Tuliskan bilangan yang terdiri atas 3 angka dan letakkan setiap angka sesuai nilai tempatnya. Ratusan 8, Puluhan 1, Satuan 2.
Pilihan: A. 182
B. 821
C. 128
D. 812
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `a33c3cd30e2555b8f613b155`

Lengkapi tabel berikut dengan bilangan yang sesuai dengan nilai tempatnya! Lambang Bilangan 328.

| Opsi | Isi |
|---|---|
| A | 2 ratusan, 3 puluhan, 8 satuan |
| B | 3 ratusan, 8 puluhan, 2 satuan |
| C | 3 ratusan, 2 puluhan, 8 satuan |
| D | 8 ratusan, 2 puluhan, 3 satuan |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d80f34def300f7f747f87b94d23d06aa2cf334f1b541eac31ce6b89ed6deb676`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 96/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |

<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Nilai Tempat Bilangan Cacah sampai 1.000
Tipe soal: multiple_choice
Stimulus: -
Soal: Lengkapi tabel berikut dengan bilangan yang sesuai dengan nilai tempatnya! Lambang Bilangan 328.
Pilihan: A. 2 ratusan, 3 puluhan, 8 satuan
B. 3 ratusan, 8 puluhan, 2 satuan
C. 3 ratusan, 2 puluhan, 8 satuan
D. 8 ratusan, 2 puluhan, 3 satuan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `076b46a03e171eb8019de109`

Urutkan bilangan 537, 590, 518, dan 601 dari yang terkecil ke terbesar.

| Opsi | Isi |
|---|---|
| A | 518, 537, 590, 601 |
| B | 537, 518, 590, 601 |
| C | 601, 590, 537, 518 |
| D | 518, 590, 537, 601 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c91dd18eee313bee5d59aa0b2ba4e5a9f8bac8f19b649adc9130a95b0843d14d`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 116/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |

<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Membandingkan dan Mengurutkan Bilangan Cacah sampai 1.000
Tipe soal: multiple_choice
Stimulus: -
Soal: Urutkan bilangan 537, 590, 518, dan 601 dari yang terkecil ke terbesar.
Pilihan: A. 518, 537, 590, 601
B. 537, 518, 590, 601
C. 601, 590, 537, 518
D. 518, 590, 537, 601
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `95b3dddf90876e587a0dc101`

Isilah titik-titik dengan tanda >, <, atau =!<br><br>705 ..... 705

| Opsi | Isi |
|---|---|
| A | 700 = 705 |
| B | 705 = 705 |
| C | 705 < 705 |
| D | 705 > 705 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Bilangan 705 sama dengan 705, sehingga tanda yang tepat adalah =.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4b7680ce7bdbd942bc8b385f02d1383a261a7373695af9e9670808eae5f9b297`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 1304 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 1307 |
| 3 | success | valid / verified | knowing | factual | Easy | 1305 |

Run 1 — solusi: Kedua bilangan adalah 705. Karena 705 sama dengan 705, maka tanda yang tepat adalah =.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali kesamaan nilai antara dua bilangan yang identik dan memilih simbol relasi yang sesuai.. Bukti: 705 ..... 705
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang simbol relasi matematika (=, <, >) dan identitas bilangan.. Bukti: 705 ..... 705
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan pengamatan visual langsung tanpa perhitungan atau langkah prosedural yang kompleks.. Bukti: 705 ..... 705

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang nilai tempat dan simbol perbandingan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah sangat familiar dengan perbandingan bilangan cacah hingga 1.000. |

Run 2 — solusi: Kedua bilangan adalah 705. Karena 705 sama dengan 705, maka tanda yang tepat adalah =.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali nilai bilangan dan menerapkan relasi kesamaan dasar.. Bukti: 705 ..... 705
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep kesamaan (equality) pada bilangan cacah.. Bukti: 705 ..... 705
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan pengenalan identitas bilangan tanpa langkah prosedural yang kompleks.. Bukti: 705 ..... 705

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dan konsep perbandingan bilangan (lebih besar, lebih kecil, sama dengan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, membandingkan dua bilangan yang identik adalah tugas rutin yang sangat dasar. |

Run 3 — solusi: Bilangan 705 sama dengan 705, sehingga tanda yang tepat adalah =.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali kesamaan nilai antara dua bilangan identik dan memilih simbol relasi yang sesuai.. Bukti: 705 ..... 705
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual mengenai simbol relasi perbandingan bilangan.. Bukti: 705 ..... 705
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya melibatkan perbandingan dua bilangan yang identik tanpa langkah tambahan.. Bukti: 705 ..... 705

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep nilai tempat dan simbol perbandingan (<, >, =). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 diharapkan sudah fasih membandingkan bilangan hingga 1.000 sebagai materi dasar. |

Histori retry: run 1 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 2 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 3 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2433`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu mengenali kesamaan nilai antara dua bilangan yang identik dan memilih simbol relasi yang sesuai. Ini adalah proses pengenalan langsung.
- Dimensi pengetahuan `factual`: Soal ini menguji pemahaman faktual tentang simbol relasi matematika (=, <, >) dan identitas bilangan.
- Intended difficulty `Easy`: Soal ini sangat mendasar, hanya memerlukan pengamatan visual langsung tanpa perhitungan atau langkah prosedural yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang nilai tempat dan simbol perbandingan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah sangat familiar dengan perbandingan bilangan cacah hingga 1.000. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 93/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.879887; applying=0.120113; reasoning=0.000000 | knowing | 0.879887 | 0.334194 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.396662; conceptual=0.569934; procedural=0.033405; metacognitive=0.000000 | conceptual | 0.569934 | 0.577629 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.903009; Medium=0.095230; Hard=0.001761 | Easy | 0.903009 | 0.297853 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.879887; −Σp ln(p) = 0.367150; H = 0.367150/ln(3) = 0.334194; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.569934; −Σp ln(p) = 0.800764; H = 0.800764/ln(4) = 0.577629; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.903009; −Σp ln(p) = 0.327225; H = 0.327225/ln(3) = 0.297853; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Membandingkan dan Mengurutkan Bilangan Cacah sampai 1.000
Tipe soal: multiple_choice
Stimulus: -
Soal: Isilah titik-titik dengan tanda >, <, atau =!

705 ..... 705
Pilihan: A. 700 = 705
B. 705 = 705
C. 705 < 705
D. 705 > 705
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `53e94d84aab7a547c9b05a51`

Andi membeli beberapa barang untuk dibagikan ke temannya. Andi membeli buku sebanyak 25 buah dan membeli pensil sebanyak 36 buah.<br><br>Berapakah jumlah barang yang dibeli Andi?

| Opsi | Isi |
|---|---|
| A | 51 buah |
| B | 11 buah |
| C | 61 buah |
| D | 60 buah |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: 25 + 36 = 61
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `20969c5ffb4a8968c2a7332d415ae970356d38e61ee99df868b1e789a2397e2c`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1297 |
| 2 | success | valid / verified | applying | procedural | Easy | 1316 |
| 3 | success | valid / verified | applying | procedural | Easy | 1371 |

Run 1 — solusi: 25 + 36 = 61
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur penjumlahan bilangan dua angka yang sudah dipelajari di kelas 3 untuk menyelesaikan masalah rutin.. Bukti: Berapakah jumlah barang yang dibeli Andi?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman algoritma penjumlahan bersusun dengan teknik menyimpan.. Bukti: 25 buah; 36 buah; jumlah barang
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar penjumlahan dua bilangan dua angka dengan teknik menyimpan, yang merupakan materi rutin kelas 3.. Bukti: 25 + 36

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah sampai 100 dengan teknik menyimpan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan dua bilangan dua angka adalah kompetensi dasar kelas 3 yang sudah sering dilatih. |

Run 2 — solusi: 25 + 36 = 61
- Domain kognitif `classify/applying`: Siswa diminta menerapkan operasi penjumlahan dasar pada situasi rutin (menjumlahkan dua kuantitas yang diketahui).. Bukti: Berapakah jumlah barang yang dibeli Andi?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma penjumlahan bersusun atau penjumlahan bilangan cacah yang merupakan prosedur standar.. Bukti: 25 buah; 36 buah; jumlah barang
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin satu langkah yang sesuai dengan kurikulum kelas 3, melibatkan penjumlahan dengan teknik menyimpan.. Bukti: 25 buah; 36 buah; Berapakah jumlah barang

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah sampai 100 dengan teknik menyimpan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan dua bilangan dua digit adalah standar kompetensi kelas 3. Soal ini langsung dan tidak memerlukan strategi kompleks. |

Run 3 — solusi: 25 + 36 = 61
- Domain kognitif `classify/applying`: Siswa diminta melakukan operasi penjumlahan dasar dua bilangan dua angka, yang merupakan prosedur rutin yang sudah dipelajari di kelas 3.. Bukti: Andi membeli buku sebanyak 25 buah dan membeli pensil sebanyak 36 buah.; Berapakah jumlah barang yang dibeli Andi?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma penjumlahan bersusun (prosedural) untuk menyelesaikan masalah penjumlahan bilangan cacah.. Bukti: 25 buah dan membeli pensil sebanyak 36 buah; jumlah barang yang dibeli
- Intended difficulty `classify/Easy`: Soal ini melibatkan operasi penjumlahan dua bilangan dua angka dengan teknik menyimpan, yang merupakan standar kompetensi kelas 3.. Bukti: 25 buah; 36 buah; jumlah barang

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah sampai 100 dengan teknik menyimpan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan 25+36 adalah operasi dasar yang diharapkan dikuasai siswa kelas 3 tanpa kesulitan berarti. |

Histori retry: run 1 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 2 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 3 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 83/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000006 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.232041; conceptual=0.752967; procedural=0.014992; metacognitive=0.000000 | conceptual | 0.752967 | 0.444052 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.871820; Medium=0.124954; Hard=0.003226 | Easy | 0.871820 | 0.362255 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000007; H = 0.000007/ln(3) = 0.000006; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.752967; −Σp ln(p) = 0.615587; H = 0.615587/ln(4) = 0.444052; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.871820; −Σp ln(p) = 0.397977; H = 0.397977/ln(3) = 0.362255; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Penjumlahan Bilangan Cacah sampai 100
Tipe soal: multiple_choice
Stimulus: -
Soal: Andi membeli beberapa barang untuk dibagikan ke temannya. Andi membeli buku sebanyak 25 buah dan membeli pensil sebanyak 36 buah.

Berapakah jumlah barang yang dibeli Andi?
Pilihan: A. 51 buah
B. 11 buah
C. 61 buah
D. 60 buah
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `a5652daac47c0bfd276b6692`

70 + 13 = ......

| Opsi | Isi |
|---|---|
| A | 93 |
| B | 80 |
| C | 73 |
| D | 83 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: 70 + 13 = (70 + 10) + 3 = 80 + 3 = 83.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e8f5012c459ff4c6fdbfa1ed3222ced32982fb83a8340afcac9bb1dcaffb87ac`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 1318 |
| 2 | success | valid / verified | knowing | procedural | Easy | 1323 |
| 3 | success | valid / verified | knowing | procedural | Easy | 1300 |

Run 1 — solusi: 70 + 13 = (70 + 10) + 3 = 80 + 3 = 83.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa melakukan operasi penjumlahan dasar secara langsung tanpa konteks cerita atau langkah tambahan, sehingga masuk dalam kategori knowing.. Bukti: 70 + 13 = ......
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menerapkan algoritma penjumlahan bilangan cacah (prosedur) untuk mendapatkan hasil yang tepat.. Bukti: 70 + 13
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi penjumlahan dasar yang familiar bagi siswa kelas 3 dengan satu langkah pengerjaan dan beban kognitif yang rendah.. Bukti: 70 + 13 = ......

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat puluhan dan satuan serta operasi penjumlahan dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sesuai dengan standar kompetensi kelas 3 untuk penjumlahan bilangan cacah hingga 100. |

Run 2 — solusi: 70 + 13 = 70 + (10 + 3) = (70 + 10) + 3 = 80 + 3 = 83.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa melakukan operasi penjumlahan dasar secara langsung tanpa konteks atau langkah tambahan, yang termasuk dalam kategori knowing.. Bukti: 70 + 13 = ......
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma penjumlahan bilangan cacah, yang merupakan prosedur standar.. Bukti: 70 + 13 = ......
- Intended difficulty `classify/Easy`: Soal ini adalah operasi penjumlahan satu langkah yang sangat rutin dan familiar bagi siswa kelas 3, dengan beban kognitif yang rendah.. Bukti: 70 + 13 = ......

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat puluhan dan satuan serta penjumlahan dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan bilangan dua digit dengan kelipatan sepuluh adalah standar kompetensi kelas 3 yang bersifat rutin. |

Run 3 — solusi: 70 + 13 = (70 + 10) + 3 = 80 + 3 = 83.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi penjumlahan bilangan dua angka secara langsung tanpa konteks cerita atau masalah yang memerlukan strategi khusus.. Bukti: 70 + 13 = ......
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma penjumlahan dasar (prosedural) untuk bilangan cacah.. Bukti: 70 + 13
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi penjumlahan dasar yang sangat rutin bagi siswa kelas 3, dengan beban kognitif rendah.. Bukti: 70 + 13 = ......

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dan penjumlahan dasar bilangan cacah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan bilangan dua angka adalah materi standar kelas 3 yang bersifat prosedural langsung. |

Histori retry: run 1 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 2 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 60/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999709; applying=0.000291; reasoning=0.000000 | knowing | 0.999709 | 0.002418 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.877368; conceptual=0.103577; procedural=0.019054; metacognitive=0.000000 | factual | 0.877368 | 0.306647 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.922444; Medium=0.075678; Hard=0.001877 | Easy | 0.922444 | 0.256323 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999709; −Σp ln(p) = 0.002656; H = 0.002656/ln(3) = 0.002418; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.877368; −Σp ln(p) = 0.425104; H = 0.425104/ln(4) = 0.306647; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.922444; −Σp ln(p) = 0.281599; H = 0.281599/ln(3) = 0.256323; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Penjumlahan Bilangan Cacah sampai 100
Tipe soal: multiple_choice
Stimulus: -
Soal: 70 + 13 = ......
Pilihan: A. 93
B. 80
C. 73
D. 83
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 9. Soal `13af70c61db0c35f9ece2f68`

Bia memiliki 19 stiker mobil. Aldo memiliki 8 stiker robot.<br><br>Berapa selisih stiker milik Bia dan Aldo?

| Opsi | Isi |
|---|---|
| A | 27 stiker |
| B | 11 stiker |
| C | 9 stiker |
| D | 12 stiker |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Selisih adalah hasil pengurangan jumlah stiker Bia (19) dengan jumlah stiker Aldo (8). 19 - 8 = 11.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `86f203704d3910558652f0b45fa6ce33281630f31ea314ae72ff7c40403bd739`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1307 |
| 2 | success | valid / verified | applying | procedural | Easy | 1321 |
| 3 | success | valid / verified | applying | procedural | Easy | 1327 |

Run 1 — solusi: Selisih adalah hasil pengurangan jumlah stiker Bia (19) dengan jumlah stiker Aldo (8). 19 - 8 = 11.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep pengurangan untuk menyelesaikan masalah rutin dalam konteks sehari-hari.. Bukti: Berapa selisih stiker milik Bia dan Aldo?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi pengurangan bilangan cacah.. Bukti: 19 stiker; 8 stiker; selisih
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar pengurangan dua bilangan di bawah 20 yang familiar bagi siswa kelas 3.. Bukti: 19 stiker; 8 stiker; Berapa selisih

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan bilangan cacah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan 19-8 adalah materi dasar kelas 3 yang bersifat rutin dan langsung. |

Run 2 — solusi: Selisih adalah hasil pengurangan jumlah stiker Bia (19) dengan jumlah stiker Aldo (8). 19 - 8 = 11.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan operasi pengurangan dasar untuk menyelesaikan masalah selisih dua bilangan yang diberikan secara langsung.. Bukti: Berapa selisih stiker milik Bia dan Aldo?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi pengurangan bilangan cacah.. Bukti: 19 stiker mobil; 8 stiker robot
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar pengurangan bilangan dua digit dengan satu digit tanpa teknik meminjam yang kompleks, sesuai untuk tingkat kelas 3.. Bukti: 19 stiker; 8 stiker; selisih

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan nilai tempat satuan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan 19-8 adalah keterampilan dasar yang diharapkan dikuasai siswa kelas 3 secara rutin. |

Run 3 — solusi: Selisih stiker Bia dan Aldo adalah 19 - 8 = 11.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan operasi pengurangan dasar untuk mencari selisih dua bilangan, yang merupakan prosedur rutin dalam konteks soal cerita sederhana.. Bukti: Berapa selisih stiker milik Bia dan Aldo?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi pengurangan bilangan cacah untuk menyelesaikan masalah selisih.. Bukti: 19 stiker; 8 stiker; selisih
- Intended difficulty `classify/Easy`: Soal ini melibatkan operasi pengurangan satu langkah dengan bilangan di bawah 20, yang merupakan standar kompetensi dasar kelas 3.. Bukti: 19 stiker; 8 stiker; Berapa selisih

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan bilangan cacah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan 19-8 adalah prosedur standar yang diharapkan dikuasai siswa kelas 3 dengan lancar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 76/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.006971; applying=0.993029; reasoning=0.000000 | applying | 0.993029 | 0.037833 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.764947; conceptual=0.170236; procedural=0.064818; metacognitive=0.000000 | factual | 0.764947 | 0.493209 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.842131; Medium=0.153894; Hard=0.003974 | Easy | 0.842131 | 0.413864 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.993029; −Σp ln(p) = 0.041564; H = 0.041564/ln(3) = 0.037833; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.764947; −Σp ln(p) = 0.683733; H = 0.683733/ln(4) = 0.493209; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.842131; −Σp ln(p) = 0.454676; H = 0.454676/ln(3) = 0.413864; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Pengurangan Bilangan Cacah sampai 100
Tipe soal: multiple_choice
Stimulus: -
Soal: Bia memiliki 19 stiker mobil. Aldo memiliki 8 stiker robot.

Berapa selisih stiker milik Bia dan Aldo?
Pilihan: A. 27 stiker
B. 11 stiker
C. 9 stiker
D. 12 stiker
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `618b8db11b04736854c11a46`

Pak Doni memiliki kolam ikan yang diisi dengan 23 ekor ikan gurami dan 42 ekor ikan nila.<br><br>Berapa selisih jumlah ikan gurami dan ikan nila milik Pak Doni?

| Opsi | Isi |
|---|---|
| A | 21 ekor |
| B | 65 ekor |
| C | 19 ekor |
| D | 20 ekor |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Selisih adalah 42 - 23 = 19.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1c2db2f0bc7d7acabd1b8ae4d7a5fb47f9bc21f0ff6a216323fcd07e8359f1c2`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1353 |
| 2 | success | valid / verified | applying | procedural | Easy | 1304 |
| 3 | success | valid / verified | applying | procedural | Easy | 1368 |

Run 1 — solusi: Selisih adalah 42 - 23 = 19.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pengurangan standar untuk mencari selisih dua bilangan cacah yang sudah diketahui.. Bukti: Berapa selisih jumlah ikan gurami dan ikan nila
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pengurangan (teknik meminjam) untuk menyelesaikan masalah selisih.. Bukti: 23 ekor ikan gurami dan 42 ekor ikan nila; Berapa selisih
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur rutin pengurangan dua bilangan dua angka dengan teknik meminjam yang umum diajarkan di kelas 3.. Bukti: 23 ekor ikan gurami dan 42 ekor ikan nila; Berapa selisih

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dan algoritma pengurangan dengan meminjam. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pengurangan bilangan dua angka dengan meminjam adalah standar kompetensi kelas 3 SD. |

Run 2 — solusi: Selisih adalah 42 - 23 = 19.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pengurangan standar untuk menyelesaikan masalah rutin yang sudah didefinisikan dengan jelas.. Bukti: Berapa selisih jumlah ikan gurami dan ikan nila
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pengurangan (teknik meminjam) yang merupakan prosedur standar.. Bukti: 23 ekor ikan gurami dan 42 ekor ikan nila; Berapa selisih
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin satu langkah yang sesuai untuk kelas 3, dengan beban kognitif rendah.. Bukti: 23 ekor; 42 ekor; Berapa selisih

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dan teknik pengurangan dengan meminjam. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan dua bilangan dua angka dengan teknik meminjam adalah standar kompetensi kelas 3. |

Run 3 — solusi: Selisih ikan nila dan gurami adalah 42 - 23 = 19.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pengurangan standar untuk menyelesaikan masalah selisih dalam konteks rutin.. Bukti: Berapa selisih jumlah ikan gurami dan ikan nila
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pengurangan (teknik meminjam) yang merupakan pengetahuan prosedural.. Bukti: 23 ekor ikan gurami dan 42 ekor ikan nila; Berapa selisih
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin satu langkah yang melibatkan pengurangan bilangan dua angka dengan teknik meminjam, sesuai dengan standar kompetensi kelas 3.. Bukti: 23 ekor ikan gurami dan 42 ekor ikan nila; Berapa selisih

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dan teknik pengurangan bersusun dengan meminjam. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pengurangan bilangan cacah sampai 100 dengan teknik meminjam adalah materi standar kelas 3. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 86/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000066; applying=0.999934; reasoning=0.000000 | applying | 0.999934 | 0.000636 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.403513; conceptual=0.558779; procedural=0.037709; metacognitive=0.000000 | conceptual | 0.558779 | 0.587914 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.860042; Medium=0.135623; Hard=0.004335 | Easy | 0.860042 | 0.386140 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999934; −Σp ln(p) = 0.000699; H = 0.000699/ln(3) = 0.000636; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.558779; −Σp ln(p) = 0.815021; H = 0.815021/ln(4) = 0.587914; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.860042; −Σp ln(p) = 0.424219; H = 0.424219/ln(3) = 0.386140; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Pengurangan Bilangan Cacah sampai 100
Tipe soal: multiple_choice
Stimulus: -
Soal: Pak Doni memiliki kolam ikan yang diisi dengan 23 ekor ikan gurami dan 42 ekor ikan nila.

Berapa selisih jumlah ikan gurami dan ikan nila milik Pak Doni?
Pilihan: A. 21 ekor
B. 65 ekor
C. 19 ekor
D. 20 ekor
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `0b7434eea7cad7663b154cc2`

Isilah titik-titik berikut dengan bilangan yang tepat sesuai gambar! (c)

| Opsi | Isi |
|---|---|
| A | 4 x 9 = 36 (dihitung sebagai 4 kelompok isi 9) |
| B | 9 x 4 = 32 |
| C | 9 x 4 = 36 |
| D | 8 x 4 = 32 |

![Gambar sumber soal 11](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0072-02.png>)


Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas3_panduan_siswa_kelas3.pdf-0072-02.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `83ca5810f07f61546b9aeaed7cbe61f1f6a9af7855887e7d96c7cce8734f06dc`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 90/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |

<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Perkalian Bilangan Cacah sampai 100
Tipe soal: multiple_choice
Stimulus: -
Soal: Isilah titik-titik berikut dengan bilangan yang tepat sesuai gambar! (c)
Pilihan: A. 4 x 9 = 36 (dihitung sebagai 4 kelompok isi 9)
B. 9 x 4 = 32
C. 9 x 4 = 36
D. 8 x 4 = 32
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 12. Soal `ea6784174a435a89a237b709`

Hitunglah hasil perkalian berikut! 5 x 7 = .....

| Opsi | Isi |
|---|---|
| A | 12 |
| B | 42 |
| C | 30 |
| D | 35 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: 5 x 7 = 35
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a2d56353f14e05928d55ddbb75b3e38d7adc41e5be18c6b57d07d441e545c0dc`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 1267 |
| 2 | success | valid / verified | knowing | procedural | Easy | 1275 |
| 3 | success | valid / verified | knowing | factual | Easy | 1272 |

Run 1 — solusi: 5 x 7 = 35
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengingat fakta perkalian dasar (tabel perkalian) untuk menjawab soal ini.. Bukti: Hitunglah hasil perkalian berikut! 5 x 7 = .....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji ingatan siswa terhadap fakta dasar perkalian.. Bukti: 5 x 7
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur yang sangat familiar dan langsung bagi siswa kelas 3, dengan beban kognitif yang rendah.. Bukti: 5 x 7 = .....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep perkalian sebagai penjumlahan berulang atau hafalan tabel perkalian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Perkalian dasar 5x7 adalah materi standar kelas 3 yang bersifat prosedural langsung. |

Run 2 — solusi: 5 x 7 = 35
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk melakukan operasi perkalian dasar secara langsung tanpa konteks atau strategi tambahan.. Bukti: Hitunglah hasil perkalian berikut! 5 x 7 = .....
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menerapkan fakta perkalian dasar (tabel perkalian) yang merupakan bagian dari pengetahuan prosedural untuk mendapatkan hasil.. Bukti: 5 x 7
- Intended difficulty `classify/Easy`: Soal ini adalah operasi perkalian satu langkah yang sangat mendasar dan familiar bagi siswa kelas 3.. Bukti: 5 x 7 = .....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep perkalian sebagai penjumlahan berulang atau hafalan tabel perkalian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Perkalian 5x7 adalah standar kompetensi dasar kelas 3 yang bersifat rutin dan langsung. |

Run 3 — solusi: 5 x 7 = 35
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi perkalian dasar yang sudah dipelajari sebagai fakta perkalian.. Bukti: Hitunglah hasil perkalian berikut! 5 x 7 = .....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji ingatan siswa terhadap fakta dasar perkalian (tabel perkalian).. Bukti: 5 x 7
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung dan sangat familiar bagi siswa kelas 3, dengan beban kognitif yang rendah.. Bukti: 5 x 7 = .....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep perkalian sebagai penjumlahan berulang atau hafalan tabel perkalian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Perkalian 5x7 adalah standar kompetensi dasar kelas 3 yang bersifat rutin dan langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2338`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini menuntut siswa untuk mengingat atau memanggil kembali fakta perkalian dasar yang sudah dipelajari, yang termasuk dalam kategori knowing.
- Dimensi pengetahuan `factual`: Soal ini menguji penguasaan fakta dasar perkalian (tabel perkalian) yang merupakan pengetahuan faktual.
- Intended difficulty `Easy`: Soal ini adalah operasi perkalian satu langkah yang sangat mendasar, rutin, dan familiar bagi siswa kelas 3, dengan beban kognitif yang rendah.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep perkalian sebagai penjumlahan berulang atau hafalan tabel perkalian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Perkalian 5x7 adalah materi standar kelas 3 yang bersifat prosedural langsung dan rutin. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 65/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999561; applying=0.000439; reasoning=0.000000 | knowing | 0.999561 | 0.003491 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.572667; conceptual=0.392155; procedural=0.035178; metacognitive=0.000000 | factual | 0.572667 | 0.580022 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.912429; Medium=0.085720; Hard=0.001851 | Easy | 0.912429 | 0.278399 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999561; −Σp ln(p) = 0.003835; H = 0.003835/ln(3) = 0.003491; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.572667; −Σp ln(p) = 0.804081; H = 0.804081/ln(4) = 0.580022; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.912429; −Σp ln(p) = 0.305853; H = 0.305853/ln(3) = 0.278399; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Perkalian Bilangan Cacah sampai 100
Tipe soal: multiple_choice
Stimulus: -
Soal: Hitunglah hasil perkalian berikut! 5 x 7 = .....
Pilihan: A. 12
B. 42
C. 30
D. 35
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 13. Soal `d8e3e19d701550680f504300`

Tulislah pembagian berikut sebagai pengurangan berulang!<br><br>16 : 4 = .....

| Opsi | Isi |
|---|---|
| A | 4 kali (16-4-4-4-4=0) |
| B | 12 kali (16-4=12, dianggap tiap kali kurang 1) |
| C | 3 kali (16-4-4-4=4) |
| D | 5 kali (20-4-4-4-4-4=0) |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Pembagian 16 : 4 berarti 16 dikurangi 4 secara berulang sampai hasilnya 0. Langkahnya: 16 - 4 = 12, 12 - 4 = 8, 8 - 4 = 4, 4 - 4 = 0. Terdapat 4 kali pengurangan.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `796d9641bad8693b60b62e6976178463772a247611df2808e87828dde1b3e89e`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1398 |
| 2 | success | valid / verified | applying | procedural | Easy | 1415 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1377 |

Run 1 — solusi: Pembagian 16 : 4 berarti 16 dikurangi 4 secara berulang sampai hasilnya 0. Langkahnya: 16 - 4 = 12, 12 - 4 = 8, 8 - 4 = 4, 4 - 4 = 0. Ada 4 kali pengurangan.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep pembagian sebagai pengurangan berulang, yang merupakan prosedur rutin dalam kurikulum kelas 3.. Bukti: Tulislah pembagian berikut sebagai pengurangan berulang! 16 : 4 = .....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau teknik pengurangan berulang untuk menyelesaikan operasi pembagian.. Bukti: Tulislah pembagian berikut sebagai pengurangan berulang!
- Intended difficulty `classify/Easy`: Soal ini menggunakan prosedur yang sangat familiar bagi siswa kelas 3, dengan angka kecil dan satu konsep utama (pengurangan berulang).. Bukti: 16 : 4 = .....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dan pembagian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 3 karena pembagian sebagai pengurangan berulang adalah materi standar yang diajarkan secara eksplisit. |

Run 2 — solusi: Pembagian 16 : 4 berarti mengurangi 16 dengan 4 secara berulang sampai hasilnya 0. Langkahnya: 16 - 4 = 12, 12 - 4 = 8, 8 - 4 = 4, 4 - 4 = 0. Ada 4 kali pengurangan.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep pembagian sebagai pengurangan berulang, yang merupakan prosedur rutin yang diajarkan di kelas 3.. Bukti: Tulislah pembagian berikut sebagai pengurangan berulang! 16 : 4 = .....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau teknik pengurangan berulang sebagai representasi dari operasi pembagian.. Bukti: Tulislah pembagian berikut sebagai pengurangan berulang!
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin, menggunakan angka kecil, dan langsung menguji pemahaman dasar pembagian sebagai pengurangan berulang tanpa kompleksitas tambahan.. Bukti: 16 : 4 = .....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan konsep pembagian sebagai pengurangan berulang. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 3 karena pembagian sebagai pengurangan berulang adalah materi standar yang diajarkan pada tingkat ini. |

Run 3 — solusi: Pembagian 16 : 4 berarti mengurangi 16 dengan 4 secara berulang sampai hasilnya 0. Langkahnya: 16 - 4 = 12, 12 - 4 = 8, 8 - 4 = 4, 4 - 4 = 0. Ada 4 kali pengurangan.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep pembagian sebagai pengurangan berulang, yang merupakan prosedur standar dalam kurikulum kelas 3.. Bukti: Tulislah pembagian berikut sebagai pengurangan berulang!; 16 : 4 = .....
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara operasi pembagian dan prosedur pengurangan berulang.. Bukti: Tulislah pembagian berikut sebagai pengurangan berulang!
- Intended difficulty `classify/Easy`: Soal ini menggunakan angka kecil dan prosedur yang sangat familiar bagi siswa kelas 3, dengan satu langkah logika utama.. Bukti: 16 : 4 = .....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dan pembagian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 3 karena pembagian sebagai pengurangan berulang adalah materi inti pada tingkat ini. |

Histori retry: run 2 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 3 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2731`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan prosedur pengurangan berulang untuk menyelesaikan operasi pembagian, yang merupakan penerapan konsep rutin di kelas 3.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang teknik atau algoritma pengurangan berulang sebagai representasi dari operasi pembagian.
- Intended difficulty `Easy`: Soal ini bersifat rutin, menggunakan angka kecil, dan langsung menguji pemahaman dasar pembagian sebagai pengurangan berulang tanpa kompleksitas tambahan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan konsep pembagian sebagai pengurangan berulang. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 3 karena pembagian sebagai pengurangan berulang adalah materi standar yang diajarkan secara eksplisit pada tingkat ini. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 123/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000286; applying=0.999714; reasoning=0.000000 | applying | 0.999714 | 0.002387 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.033069; conceptual=0.953338; procedural=0.013593; metacognitive=0.000000 | conceptual | 0.953338 | 0.156329 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.866888; Medium=0.130900; Hard=0.002212 | Easy | 0.866888 | 0.367296 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999714; −Σp ln(p) = 0.002622; H = 0.002622/ln(3) = 0.002387; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.953338; −Σp ln(p) = 0.216718; H = 0.216718/ln(4) = 0.156329; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.866888; −Σp ln(p) = 0.403516; H = 0.403516/ln(3) = 0.367296; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Pembagian Bilangan Cacah sampai 100
Tipe soal: multiple_choice
Stimulus: -
Soal: Tulislah pembagian berikut sebagai pengurangan berulang!

16 : 4 = .....
Pilihan: A. 4 kali (16-4-4-4-4=0)
B. 12 kali (16-4=12, dianggap tiap kali kurang 1)
C. 3 kali (16-4-4-4=4)
D. 5 kali (20-4-4-4-4-4=0)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `ea7d38ffd5b2b15fbd33446e`

Ayah memelihara beberapa ekor ayam. Ayam-ayam tersebut bertelur dan menghasilkan 24 telur. Ayah ingin memasukkan telur-telur itu ke dalam 3 kotak dengan sama banyak.<br><br>Berapa jumlah telur dalam setiap kotak?

| Opsi | Isi |
|---|---|
| A | 8 butir |
| B | 7 butir |
| C | 6 butir |
| D | 21 butir |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: 24 telur dibagi ke dalam 3 kotak sama banyak berarti 24 : 3 = 8 telur per kotak.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `371b40a9a01c6d423bf67348725936721b3d1f216a7a8036f789292967c3a047`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1336 |
| 2 | success | valid / verified | applying | procedural | Easy | 1359 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1338 |

Run 1 — solusi: 24 dibagi 3 sama dengan 8.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan operasi pembagian dasar yang sudah dipelajari untuk menyelesaikan masalah pembagian kelompok yang rutin.. Bukti: Ayah ingin memasukkan telur-telur itu ke dalam 3 kotak dengan sama banyak; Berapa jumlah telur dalam setiap kotak?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa tentang konsep pembagian sebagai pembagian rata (partitive division) dan penggunaan algoritma pembagian dasar.. Bukti: 24 telur; 3 kotak; sama banyak
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah satu langkah yang sangat rutin bagi siswa kelas 3, menggunakan angka kecil dan konteks yang familiar.. Bukti: 24 telur; 3 kotak; sama banyak

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pembagian dasar dan hafal perkalian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pembagian bilangan cacah adalah materi standar kelas 3. Soal ini bersifat langsung tanpa jebakan atau langkah tambahan. |

Run 2 — solusi: 24 telur dibagi ke dalam 3 kotak sama banyak berarti 24 : 3 = 8 telur per kotak.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pembagian dasar yang sudah dipelajari di kelas 3 untuk menyelesaikan masalah pembagian sederhana.. Bukti: Ayah ingin memasukkan telur-telur itu ke dalam 3 kotak dengan sama banyak; Berapa jumlah telur dalam setiap kotak?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa mengenai konsep pembagian sebagai pembagian rata (partitive division) dan penggunaan algoritma pembagian dasar.. Bukti: 24 telur; 3 kotak; sama banyak
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin satu langkah yang menggunakan angka kecil dan operasi dasar yang sesuai dengan kurikulum kelas 3.. Bukti: 24 telur; 3 kotak; sama banyak

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pembagian dasar dan tabel perkalian 3. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah pembagian 24:3 adalah standar kompetensi kelas 3 yang bersifat langsung dan rutin. |

Run 3 — solusi: 24 telur dibagi ke dalam 3 kotak sama banyak berarti 24 : 3 = 8 telur per kotak.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan operasi pembagian dasar yang sudah dipelajari untuk menyelesaikan masalah rutin pembagian sama rata.. Bukti: Ayah ingin memasukkan telur-telur itu ke dalam 3 kotak dengan sama banyak
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang konsep pembagian sebagai pembagian kelompok sama rata (partitive division).. Bukti: 24 telur; 3 kotak; sama banyak
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin satu langkah yang menggunakan fakta dasar pembagian, sangat sesuai dengan kurikulum kelas 3.. Bukti: 24 telur; 3 kotak; sama banyak

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pembagian dasar dan hafal perkalian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah pembagian sederhana dengan angka di bawah 100 adalah standar kompetensi kelas 3. |

Histori retry: run 1 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 2 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2535`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan prosedur pembagian dasar yang sudah dipelajari untuk menyelesaikan masalah rutin pembagian kelompok sama rata.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman siswa tentang konsep pembagian sebagai pembagian rata (partitive division) dan penggunaan algoritma pembagian dasar.
- Intended difficulty `Easy`: Soal ini merupakan masalah rutin satu langkah yang menggunakan angka kecil dan operasi dasar yang sesuai dengan kurikulum kelas 3.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pembagian dasar dan tabel perkalian 3. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah pembagian 24:3 adalah standar kompetensi kelas 3 yang bersifat langsung dan rutin. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 92/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000001; applying=0.999999; reasoning=0.000000 | applying | 0.999999 | 0.000011 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.129711; conceptual=0.847574; procedural=0.022715; metacognitive=0.000000 | conceptual | 0.847574 | 0.354230 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.848646; Medium=0.147216; Hard=0.004138 | Easy | 0.848646 | 0.404171 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999999; −Σp ln(p) = 0.000012; H = 0.000012/ln(3) = 0.000011; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.847574; −Σp ln(p) = 0.491066; H = 0.491066/ln(4) = 0.354230; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.848646; −Σp ln(p) = 0.444027; H = 0.444027/ln(3) = 0.404171; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Pembagian Bilangan Cacah sampai 100
Tipe soal: multiple_choice
Stimulus: -
Soal: Ayah memelihara beberapa ekor ayam. Ayam-ayam tersebut bertelur dan menghasilkan 24 telur. Ayah ingin memasukkan telur-telur itu ke dalam 3 kotak dengan sama banyak.

Berapa jumlah telur dalam setiap kotak?
Pilihan: A. 8 butir
B. 7 butir
C. 6 butir
D. 21 butir
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 15. Soal `86ef303fdabf175f3223919d`

Di atas bunga hinggap kupu-kupu merah, kuning, dan hijau. Ada 5 kupu-kupu merah. Ada 6 kupu-kupu hijau. Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.<br><br>Berapa jumlah semua kupu-kupu?

| Opsi | Isi |
|---|---|
| A | 18 |
| B | 12 |
| C | 13 |
| D | 11 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Kuning = 5 + 2 = 7. Total = 5 (merah) + 6 (hijau) + 7 (kuning) = 18.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9a7a9e53c0f35840db25adfa6655d1700b2d91a6530e4c01adc4cdba38312c46`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 1493 |
| 2 | success | valid / verified | applying | procedural | Medium | 1487 |
| 3 | success | valid / verified | applying | conceptual | Medium | 1488 |

Run 1 — solusi: Kupu-kupu merah = 5. Kupu-kupu hijau = 6. Kupu-kupu kuning = 5 + 2 = 7. Total = 5 + 6 + 7 = 18.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi informasi yang diberikan, melakukan satu langkah perhitungan untuk menentukan jumlah kupu-kupu kuning, dan kemudian menjumlahkan ketiga kelompok kupu-kupu tersebut.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.; Berapa jumlah semua kupu-kupu?
- Dimensi pengetahuan `classify/conceptual`: Soal ini memerlukan pemahaman konsep penjumlahan dan hubungan antar kuantitas (lebih dari) untuk menyelesaikan masalah.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.; Berapa jumlah semua kupu-kupu?
- Intended difficulty `classify/Medium`: Soal ini melibatkan beberapa langkah rutin (menentukan nilai kuning, lalu menjumlahkan ketiganya) yang sesuai untuk tingkat kelas 3.. Bukti: Ada 5 kupu-kupu merah.; Ada 6 kupu-kupu hijau.; Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar dan pemahaman konsep 'lebih dari'. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal cerita dua langkah adalah standar untuk kelas 3, menuntut ketelitian dalam mengidentifikasi semua variabel sebelum menjumlahkan. |

Run 2 — solusi: Kupu-kupu merah = 5. Kupu-kupu hijau = 6. Kupu-kupu kuning = 5 + 2 = 7. Total = 5 + 6 + 7 = 18.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi informasi, melakukan operasi penjumlahan sederhana untuk menentukan jumlah kupu-kupu kuning, lalu menjumlahkan ketiga kelompok kupu-kupu. Ini adalah penerapan prosedur rutin.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.; Berapa jumlah semua kupu-kupu?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan antar kuantitas (konseptual) dan penerapan algoritma penjumlahan (prosedural) untuk menyelesaikan masalah.. Bukti: 5 kupu-kupu merah; 6 kupu-kupu hijau; 2 lebihnya dari banyak kupu-kupu merah
- Intended difficulty `classify/Medium`: Soal ini melibatkan beberapa langkah rutin (menentukan nilai kuning, lalu menjumlahkan ketiganya) yang sesuai untuk kelas 3.. Bukti: 5 kupu-kupu merah; 6 kupu-kupu hijau; 2 lebihnya dari banyak kupu-kupu merah; Berapa jumlah semua kupu-kupu?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar dan pemahaman konsep 'lebih dari'. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal cerita dua langkah adalah standar untuk kelas 3, menuntut ketelitian dalam mengidentifikasi semua variabel sebelum menjumlahkan. |

Run 3 — solusi: Kupu-kupu merah = 5. Kupu-kupu hijau = 6. Kupu-kupu kuning = 5 + 2 = 7. Total = 5 + 6 + 7 = 18.
- Domain kognitif `classify/applying`: Siswa perlu melakukan dua langkah: menentukan jumlah kupu-kupu kuning berdasarkan informasi relasional, kemudian menjumlahkan ketiga kelompok kupu-kupu. Ini adalah penerapan prosedur rutin pada situasi cerita.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah; Berapa jumlah semua kupu-kupu?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan kuantitas (konsep 'lebih dari') dan penerapan algoritma penjumlahan dasar.. Bukti: 5 kupu-kupu merah; 6 kupu-kupu hijau; 2 lebihnya dari banyak kupu-kupu merah
- Intended difficulty `classify/Medium`: Soal ini melibatkan dua langkah operasi (penjumlahan untuk mencari nilai kuning, lalu penjumlahan total) yang merupakan standar rutin untuk kelas 3.. Bukti: 5 kupu-kupu merah; 6 kupu-kupu hijau; 2 lebihnya dari banyak kupu-kupu merah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar dan pemahaman konsep 'lebih dari'. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal cerita dua langkah adalah standar kompetensi kelas 3 untuk menguji pemahaman operasi hitung campuran atau bertahap. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `2953`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi informasi, melakukan satu langkah perhitungan relasional untuk menentukan nilai variabel yang belum diketahui (kuning), dan menerapkan prosedur penjumlahan rutin untuk mendapatkan total.
- Dimensi pengetahuan `conceptual`: Soal ini menuntut pemahaman konsep hubungan antar kuantitas ('2 lebihnya dari') dan penerapan algoritma penjumlahan dasar.
- Intended difficulty `Medium`: Soal ini melibatkan dua langkah rutin yang saling terkait (menentukan nilai kuning, lalu menjumlahkan ketiganya), yang merupakan standar kompetensi kelas 3.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar dan pemahaman konsep 'lebih dari'. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal cerita dua langkah adalah standar untuk kelas 3, menuntut ketelitian dalam mengidentifikasi semua variabel sebelum menjumlahkan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 112/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000209; applying=0.999791; reasoning=0.000000 | applying | 0.999791 | 0.001802 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.291642; conceptual=0.693791; procedural=0.014567; metacognitive=0.000000 | conceptual | 0.693791 | 0.486630 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.865333; Medium=0.131663; Hard=0.003004 | Easy | 0.865333 | 0.372795 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999791; −Σp ln(p) = 0.001980; H = 0.001980/ln(3) = 0.001802; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.693791; −Σp ln(p) = 0.674612; H = 0.674612/ln(4) = 0.486630; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.865333; −Σp ln(p) = 0.409558; H = 0.409558/ln(3) = 0.372795; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Soal Cerita Penjumlahan dan Pengurangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Di atas bunga hinggap kupu-kupu merah, kuning, dan hijau. Ada 5 kupu-kupu merah. Ada 6 kupu-kupu hijau. Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.

Berapa jumlah semua kupu-kupu?
Pilihan: A. 18
B. 12
C. 13
D. 11
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `f366f15007b61b27653bdf58`

Kira menuliskan satu bilangan.<br><br>Kira berkata, 'Jika aku tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55.' Berapa bilangan yang ditulis Kira?

| Opsi | Isi |
|---|---|
| A | 92 |
| B | 81 |
| C | 29 |
| D | 12 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Misalkan bilangan adalah 10a + b. Diketahui (a+4) puluhan dan (b+3) satuan menghasilkan 55. Maka 10(a+4) + (b+3) = 55, sehingga 10a + 40 + b + 3 = 55, 10a + b + 43 = 55, 10a + b = 12.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `46ab698c29605da354806834ae548e872c9cc377808ceea63b4a3e6319b78f67`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 1462 |
| 2 | success | valid / verified | applying | conceptual | Medium | 1431 |
| 3 | success | valid / verified | applying | conceptual | Medium | 1439 |

Run 1 — solusi: Misalkan bilangan adalah 10a + b. Diketahui (a+4) puluhan dan (b+3) satuan menghasilkan 55. Maka 10(a+4) + (b+3) = 55, sehingga 10a + 40 + b + 3 = 55, 10a + b + 43 = 55, 10a + b = 12.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep nilai tempat (puluhan dan satuan) dan melakukan operasi invers untuk menemukan bilangan awal, yang merupakan penerapan konsep dalam situasi rutin.. Bukti: Jika aku tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur bilangan (nilai tempat) dan bagaimana operasi aritmatika mempengaruhi digit puluhan dan satuan.. Bukti: tambahkan 4 pada puluhan dan 3 pada satuan
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa kelas 3 harus melakukan pembalikan operasi (invers) dari deskripsi verbal ke bentuk numerik, bukan sekadar operasi penjumlahan langsung.. Bukti: tambahkan 4 pada puluhan dan 3 pada satuan; hasilnya adalah 55

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan dua angka dan operasi penjumlahan/pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, konsep nilai tempat sudah diajarkan, namun membalikkan operasi dari hasil akhir ke awal memerlukan penalaran prosedural yang sedikit lebih kompleks dibanding soal rutin satu langkah. |

Run 2 — solusi: Misalkan bilangan tersebut adalah ab (10a + b). Persamaan: (10a + b) + 40 + 3 = 55. Maka 10a + b = 55 - 43 = 12.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep nilai tempat (puluhan dan satuan) dan melakukan operasi invers untuk menemukan bilangan awal, yang merupakan penerapan konsep dalam situasi rutin.. Bukti: Jika aku tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur bilangan (nilai tempat) dan bagaimana operasi aritmatika memengaruhi posisi digit tersebut.. Bukti: tambahkan 4 pada puluhan dan 3 pada satuan
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium untuk kelas 3 karena siswa tidak bisa langsung menghitung, melainkan harus melakukan operasi invers (pengurangan) dari hasil akhir untuk mendapatkan bilangan awal, yang melibatkan pemahaman nilai tempat.. Bukti: tambahkan 4 pada puluhan dan 3 pada satuan; hasilnya adalah 55

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat (puluhan dan satuan) dan operasi pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah mempelajari nilai tempat, namun membalikkan proses (dari hasil ke asal) memerlukan penalaran yang sedikit lebih tinggi daripada sekadar menjumlahkan. |

Run 3 — solusi: Misalkan bilangan tersebut adalah AB (10A + B). Diketahui (A+4) puluhan dan (B+3) satuan = 55. Maka A+4 = 5 dan B+3 = 5. Didapat A=1 dan B=2. Bilangan tersebut adalah 12.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep nilai tempat (puluhan dan satuan) dan melakukan operasi invers (pengurangan) untuk menemukan bilangan awal, yang merupakan penerapan konsep pada situasi rutin.. Bukti: Jika aku tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur nilai tempat bilangan dua angka (puluhan dan satuan) sebagai sebuah konsep.. Bukti: tambahkan 4 pada puluhan dan 3 pada satuan
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena siswa kelas 3 harus melakukan operasi invers (pengurangan) pada nilai tempat yang berbeda secara simultan, bukan sekadar operasi hitung langsung.. Bukti: tambahkan 4 pada puluhan dan 3 pada satuan; hasilnya adalah 55

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan dua angka (puluhan dan satuan) dan operasi pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, membalikkan operasi pada nilai tempat (puluhan dan satuan) memerlukan penalaran lebih daripada sekadar penjumlahan langsung, namun masih dalam lingkup kurikulum. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 77/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.986888; applying=0.013112; reasoning=0.000000 | knowing | 0.986888 | 0.063585 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.110817; conceptual=0.830592; procedural=0.058591; metacognitive=0.000000 | conceptual | 0.830592 | 0.406976 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.751435; Medium=0.245294; Hard=0.003271 | Easy | 0.751435 | 0.526272 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.986888; −Σp ln(p) = 0.069855; H = 0.069855/ln(3) = 0.063585; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.830592; −Σp ln(p) = 0.564188; H = 0.564188/ln(4) = 0.406976; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.751435; −Σp ln(p) = 0.578169; H = 0.578169/ln(3) = 0.526272; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Membandingkan Bilangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Kira menuliskan satu bilangan.

Kira berkata, 'Jika aku tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55.' Berapa bilangan yang ditulis Kira?
Pilihan: A. 92
B. 81
C. 29
D. 12
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 17. Soal `134652ea27846439dcee22e8`

Pak Budi sedang panen buah durian. Hasil panennya itu diletakkan dalam dua keranjang sebelum dijual di pasar. Keranjang pertama berisi 42 buah durian. Sementara jumlah durian yang ada pada kedua keranjang tersebut adalah 78 buah.<br><br>Berapa banyak durian yang ada di keranjang kedua ?

| Opsi | Isi |
|---|---|
| A | 120 buah |
| B | 36 buah |
| C | 46 buah |
| D | 42 buah |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Total durian adalah 78. Keranjang pertama berisi 42. Maka keranjang kedua = 78 - 42 = 36.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f271025d2365028676fe523837ced91274945efade2259f16fc8da1bd082e4f7`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1463 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1440 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1468 |

Run 1 — solusi: Total durian adalah 78. Keranjang pertama berisi 42. Maka keranjang kedua = 78 - 42 = 36.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi hubungan antara bagian dan keseluruhan, lalu memilih operasi pengurangan yang tepat untuk menyelesaikan masalah rutin.. Bukti: jumlah durian yang ada pada kedua keranjang tersebut adalah 78 buah; Keranjang pertama berisi 42 buah durian; Berapa banyak durian yang ada di keranjang kedua
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep penjumlahan sebagai bagian dari keseluruhan (part-part-whole) dan penggunaan operasi pengurangan untuk mencari nilai yang hilang.. Bukti: jumlah durian yang ada pada kedua keranjang tersebut adalah 78 buah; Berapa banyak durian yang ada di keranjang kedua
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin satu langkah yang sesuai dengan kurikulum kelas 3, di mana siswa hanya perlu melakukan operasi pengurangan dasar.. Bukti: Keranjang pertama berisi 42 buah durian; jumlah durian yang ada pada kedua keranjang tersebut adalah 78 buah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dan pengurangan bilangan cacah hingga 100. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah terbiasa dengan soal cerita sederhana yang melibatkan operasi hitung dasar. |

Run 2 — solusi: Diketahui total durian = 78 dan keranjang pertama = 42. Maka keranjang kedua = 78 - 42 = 36.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi hubungan antara bagian dan keseluruhan (part-part-whole) untuk menentukan operasi pengurangan yang tepat guna menyelesaikan masalah rutin.. Bukti: Hasil panennya itu diletakkan dalam dua keranjang; Keranjang pertama berisi 42 buah durian. Sementara jumlah durian yang ada pada kedua keranjang tersebut adalah 78 buah.
- Dimensi pengetahuan `classify/conceptual`: Siswa menerapkan pemahaman konseptual tentang hubungan penjumlahan dan pengurangan untuk memecahkan masalah.. Bukti: jumlah durian yang ada pada kedua keranjang tersebut adalah 78 buah; Berapa banyak durian yang ada di keranjang kedua
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin satu langkah yang sesuai untuk kelas 3, dengan angka yang mudah dikelola dan konteks yang familiar.. Bukti: Keranjang pertama berisi 42 buah durian; jumlah durian yang ada pada kedua keranjang tersebut adalah 78 buah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dan pengurangan bilangan cacah hingga 100. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah ini adalah aplikasi langsung dari operasi pengurangan dasar yang diharapkan dikuasai siswa kelas 3. |

Run 3 — solusi: Jumlah durian di keranjang kedua adalah total durian dikurangi jumlah durian di keranjang pertama: 78 - 42 = 36.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi hubungan antara bagian dan keseluruhan (part-part-whole) dan menerapkan operasi pengurangan yang sesuai untuk menyelesaikan masalah rutin.. Bukti: Hasil panennya itu diletakkan dalam dua keranjang; Keranjang pertama berisi 42 buah durian; jumlah durian yang ada pada kedua keranjang tersebut adalah 78 buah; Berapa banyak durian yang ada di keranjang kedua
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan penjumlahan dan pengurangan dalam konteks cerita.. Bukti: jumlah durian yang ada pada kedua keranjang tersebut adalah 78 buah; Berapa banyak durian yang ada di keranjang kedua
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah satu langkah yang melibatkan operasi pengurangan standar, yang sangat familiar bagi siswa kelas 3.. Bukti: Keranjang pertama berisi 42 buah durian; jumlah durian yang ada pada kedua keranjang tersebut adalah 78 buah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dan pengurangan bilangan cacah hingga 100. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah ini adalah aplikasi langsung dari operasi pengurangan yang sesuai dengan kurikulum kelas 3. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 105/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000001 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.078325; conceptual=0.908014; procedural=0.013660; metacognitive=0.000000 | conceptual | 0.908014 | 0.249407 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.877228; Medium=0.119608; Hard=0.003164 | Easy | 0.877228 | 0.352363 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000001; H = 0.000001/ln(3) = 0.000001; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.908014; −Σp ln(p) = 0.345751; H = 0.345751/ln(4) = 0.249407; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.877228; −Σp ln(p) = 0.387110; H = 0.387110/ln(3) = 0.352363; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Kalimat Matematika Berkaitan dengan Penjumlahan Bilangan Cacah
Tipe soal: multiple_choice
Stimulus: -
Soal: Pak Budi sedang panen buah durian. Hasil panennya itu diletakkan dalam dua keranjang sebelum dijual di pasar. Keranjang pertama berisi 42 buah durian. Sementara jumlah durian yang ada pada kedua keranjang tersebut adalah 78 buah.

Berapa banyak durian yang ada di keranjang kedua ?
Pilihan: A. 120 buah
B. 36 buah
C. 46 buah
D. 42 buah
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `4083151b80c126b0090bb512`

Jawablah pertanyaan berikut dengan tepat!<br><br>38 + … = 67

| Opsi | Isi |
|---|---|
| A | 39 |
| B | 29 |
| C | 38 |
| D | 105 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Untuk mencari bilangan yang hilang, kurangi hasil penjumlahan dengan bilangan yang diketahui: 67 - 38 = 29.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `51827218c618a2054d3aa85e15cc852746890395886ce4e0f08aee30408c22c1`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1305 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1279 |
| 3 | success | valid / verified | applying | procedural | Easy | 1316 |

Run 1 — solusi: Untuk mencari bilangan yang hilang, kurangi hasil penjumlahan dengan bilangan yang diketahui: 67 - 38 = 29.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pengurangan untuk menemukan nilai yang hilang dalam kalimat matematika penjumlahan.. Bukti: 38 + … = 67
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan antara penjumlahan dan pengurangan (invers operasi) serta teknik pengurangan bersusun.. Bukti: 38 + … = 67
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar yang familiar bagi siswa kelas 3, melibatkan satu langkah operasi (pengurangan) dengan beban kognitif rendah.. Bukti: 38 + … = 67

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dan pengurangan bilangan cacah hingga 100. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 diharapkan sudah lancar melakukan operasi pengurangan bilangan dua angka dengan teknik meminjam. |

Run 2 — solusi: Untuk mencari angka yang hilang, kurangi hasil dengan angka yang diketahui: 67 - 38 = 29.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pengurangan untuk menemukan nilai yang tidak diketahui dalam kalimat matematika penjumlahan.. Bukti: 38 + … = 67
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara operasi penjumlahan dan pengurangan (invers).. Bukti: 38 + … = 67
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur rutin bagi siswa kelas 3 untuk mencari nilai yang hilang dalam kalimat matematika sederhana.. Bukti: 38 + … = 67

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dan pengurangan bilangan cacah hingga 100. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari nilai yang hilang dalam kalimat matematika adalah standar kompetensi kelas 3 yang bersifat rutin. |

Run 3 — solusi: Untuk mencari bilangan yang hilang, kurangi hasil penjumlahan dengan bilangan yang diketahui: 67 - 38 = 29.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pengurangan untuk menemukan nilai yang hilang dalam kalimat matematika penjumlahan. Ini adalah penerapan prosedur rutin.. Bukti: 38 + … = 67
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pengurangan (teknik meminjam) untuk menyelesaikan kalimat matematika.. Bukti: 38 + … = 67
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar yang familiar bagi siswa kelas 3, melibatkan satu operasi pengurangan dengan teknik meminjam.. Bukti: 38 + … = 67

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dan operasi pengurangan bersusun dengan teknik meminjam. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan bilangan dua digit dengan teknik meminjam adalah materi standar kelas 3. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2406`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur pengurangan untuk menemukan nilai yang hilang dalam kalimat matematika penjumlahan. Ini adalah penerapan prosedur rutin.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang algoritma pengurangan (teknik meminjam) untuk menyelesaikan kalimat matematika.
- Intended difficulty `Easy`: Soal ini merupakan prosedur standar yang familiar bagi siswa kelas 3, melibatkan satu operasi pengurangan dengan teknik meminjam.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dan operasi pengurangan bersusun dengan teknik meminjam. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan bilangan dua digit dengan teknik meminjam adalah materi standar kelas 3. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 64/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.997427; applying=0.002573; reasoning=0.000000 | knowing | 0.997427 | 0.016301 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.808877; conceptual=0.116948; procedural=0.074175; metacognitive=0.000000 | factual | 0.808877 | 0.443987 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.932819; Medium=0.064504; Hard=0.002676 | Easy | 0.932819 | 0.234415 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.997427; −Σp ln(p) = 0.017909; H = 0.017909/ln(3) = 0.016301; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.808877; −Σp ln(p) = 0.615496; H = 0.615496/ln(4) = 0.443987; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.932819; −Σp ln(p) = 0.257532; H = 0.257532/ln(3) = 0.234415; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Kalimat Matematika Berkaitan dengan Penjumlahan Bilangan Cacah
Tipe soal: multiple_choice
Stimulus: -
Soal: Jawablah pertanyaan berikut dengan tepat!

38 + … = 67
Pilihan: A. 39
B. 29
C. 38
D. 105
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 19. Soal `15c4621ae2b13cb48dc0c3b9`

Pak Budi panen buah manggis. Manggis yang dipanen sebanyak 78 buah. Hasil panen tersebut sebagian besar dibagikan kepada saudara dan tetangganya. Sisa manggis yang tersedia sebanyak 42 buah.<br><br>Berapa banyak manggis yang dibagikan oleh Pak Budi ?

| Opsi | Isi |
|---|---|
| A | 36 buah |
| B | 46 buah |
| C | 120 buah |
| D | 42 buah |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Jumlah manggis yang dibagikan adalah total panen dikurangi sisa manggis: 78 - 42 = 36.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f9192c2ced80afdadbc10afefab8a500a4dd6059ce842eb60408c2f39429832a`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1368 |
| 2 | success | valid / verified | applying | procedural | Easy | 1351 |
| 3 | success | valid / verified | applying | procedural | Easy | 1343 |

Run 1 — solusi: Jumlah manggis yang dibagikan adalah total panen dikurangi sisa manggis: 78 - 42 = 36.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi operasi pengurangan yang tepat dari konteks cerita untuk menyelesaikan masalah rutin.. Bukti: Berapa banyak manggis yang dibagikan oleh Pak Budi ?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa tentang algoritma pengurangan bilangan cacah.. Bukti: 78 - 42 = 36
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah pengurangan satu langkah yang standar untuk kelas 3 dengan angka yang tidak memerlukan teknik meminjam yang kompleks.. Bukti: Manggis yang dipanen sebanyak 78 buah; Sisa manggis yang tersedia sebanyak 42 buah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan bilangan cacah hingga 100. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 3 SD mengenai operasi hitung pengurangan bilangan cacah dalam soal cerita sederhana. |

Run 2 — solusi: Jumlah manggis yang dibagikan = Total panen - Sisa manggis = 78 - 42 = 36.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi operasi pengurangan yang tepat dari konteks cerita untuk menyelesaikan masalah rutin.. Bukti: Berapa banyak manggis yang dibagikan oleh Pak Budi ?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi pengurangan bilangan cacah dalam konteks kehidupan sehari-hari.. Bukti: 78 buah; Sisa manggis yang tersedia sebanyak 42 buah
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah satu langkah yang menggunakan prosedur pengurangan standar yang familiar bagi siswa kelas 3.. Bukti: 78 buah; 42 buah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan bilangan cacah hingga 100. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan dua digit tanpa teknik meminjam yang rumit adalah standar kompetensi kelas 3. |

Run 3 — solusi: 78 - 42 = 36
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi operasi pengurangan yang tepat dari konteks cerita untuk menyelesaikan masalah rutin.. Bukti: Berapa banyak manggis yang dibagikan oleh Pak Budi ?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi pengurangan bilangan cacah dua angka.. Bukti: 78 buah; Sisa manggis yang tersedia sebanyak 42 buah
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin satu langkah yang sesuai untuk kelas 3, dengan beban kognitif rendah dan distractor yang mencerminkan kesalahan umum.. Bukti: 78 buah; 42 buah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan bilangan cacah dua angka tanpa teknik meminjam. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan dua angka adalah standar kompetensi kelas 3. Soal ini langsung dan tidak memerlukan strategi kompleks. |

Histori retry: run 2 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 3 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 97/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000008; applying=0.999992; reasoning=0.000000 | applying | 0.999992 | 0.000092 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.210876; conceptual=0.712573; procedural=0.076551; metacognitive=0.000000 | conceptual | 0.712573 | 0.552853 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.908157; Medium=0.088649; Hard=0.003194 | Easy | 0.908157 | 0.291864 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999992; −Σp ln(p) = 0.000101; H = 0.000101/ln(3) = 0.000092; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.712573; −Σp ln(p) = 0.766417; H = 0.766417/ln(4) = 0.552853; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.908157; −Σp ln(p) = 0.320646; H = 0.320646/ln(3) = 0.291864; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Kalimat Matematika Berkaitan dengan Pengurangan Bilangan Cacah
Tipe soal: multiple_choice
Stimulus: -
Soal: Pak Budi panen buah manggis. Manggis yang dipanen sebanyak 78 buah. Hasil panen tersebut sebagian besar dibagikan kepada saudara dan tetangganya. Sisa manggis yang tersedia sebanyak 42 buah.

Berapa banyak manggis yang dibagikan oleh Pak Budi ?
Pilihan: A. 36 buah
B. 46 buah
C. 120 buah
D. 42 buah
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `4c4a8d5909026263b43d6f5c`

Jawablah pertanyaan berikut dengan tepat!<br><br>83 – … = 38

| Opsi | Isi |
|---|---|
| A | 121 |
| B | 38 |
| C | 35 |
| D | 45 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Untuk mencari bilangan yang hilang, hitung 83 - 38 = 45.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5f682f0116c741794832586ca75d12be58f7088a7a15a9762a075750fc2b0f27`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1283 |
| 2 | success | valid / verified | applying | procedural | Easy | 1299 |
| 3 | success | valid / verified | applying | procedural | Easy | 1276 |

Run 1 — solusi: Untuk mencari bilangan yang hilang, hitung 83 - 38 = 45.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pengurangan bilangan cacah untuk menemukan nilai yang hilang dalam kalimat matematika.. Bukti: 83 – … = 38
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pengurangan (teknik meminjam) yang merupakan prosedur standar.. Bukti: 83 – … = 38
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur rutin pengurangan dua angka dengan teknik meminjam yang sesuai untuk kelas 3.. Bukti: 83 – … = 38

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman pengurangan bilangan cacah dua angka dengan teknik meminjam. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pengurangan dua angka dengan meminjam adalah materi standar kelas 3. Soal ini langsung dan tidak memerlukan strategi kompleks. |

Run 2 — solusi: Untuk mencari bilangan yang hilang, hitung 83 - 38. 83 - 38 = 45.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pengurangan bilangan cacah untuk menemukan nilai yang hilang dalam kalimat matematika.. Bukti: 83 – … = 38
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pengurangan (teknik meminjam) yang merupakan prosedur standar.. Bukti: 83 – … = 38
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur rutin pengurangan dua bilangan dua angka dengan teknik meminjam yang umum diajarkan di kelas 3.. Bukti: 83 – … = 38

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dan teknik pengurangan bersusun dengan meminjam. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pengurangan bilangan dua angka dengan meminjam adalah materi standar kelas 3 SD. |

Run 3 — solusi: Untuk mencari bilangan yang hilang dalam 83 - x = 38, kita hitung 83 - 38 = 45.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pengurangan bilangan cacah untuk menemukan nilai yang tidak diketahui dalam kalimat matematika.. Bukti: 83 – … = 38
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pengurangan (teknik meminjam) yang merupakan prosedur standar.. Bukti: 83 – … = 38
- Intended difficulty `classify/Easy`: Soal ini adalah prosedur rutin pengurangan dua angka dengan teknik meminjam yang sesuai untuk kelas 3.. Bukti: 83 – … = 38

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dan teknik pengurangan bersusun dengan meminjam. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pengurangan bilangan dua angka dengan meminjam adalah materi standar kelas 3. |

Histori retry: run 1 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 2 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 3 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 64/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999791; applying=0.000209; reasoning=0.000000 | knowing | 0.999791 | 0.001806 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.842066; conceptual=0.086418; procedural=0.071516; metacognitive=0.000000 | factual | 0.842066 | 0.393131 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.932862; Medium=0.064064; Hard=0.003074 | Easy | 0.932862 | 0.235437 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999791; −Σp ln(p) = 0.001984; H = 0.001984/ln(3) = 0.001806; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.842066; −Σp ln(p) = 0.544995; H = 0.544995/ln(4) = 0.393131; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.932862; −Σp ln(p) = 0.258654; H = 0.258654/ln(3) = 0.235437; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Kalimat Matematika Berkaitan dengan Pengurangan Bilangan Cacah
Tipe soal: multiple_choice
Stimulus: -
Soal: Jawablah pertanyaan berikut dengan tepat!

83 – … = 38
Pilihan: A. 121
B. 38
C. 35
D. 45
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 21. Soal `fdf4f64afe025be58e0fbd08`

Ibu Meutia membeli kain untuk seragam. Terdapat 3 pesanan seragam dari sekolah kebangsaan. Ukuran panjang kain yang dibutuhkan untuk setiap seragam adalah 200 cm. Ibu Meutia memiliki kain dengan panjang 850 cm.<br><br>Berapakah panjang sisa kain Ibu Meutia?

| Opsi | Isi |
|---|---|
| A | 250 cm |
| B | 150 cm |
| C | 350 cm |
| D | 600 cm |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Total kebutuhan = 3 x 200 cm = 600 cm. Sisa kain = 850 cm - 600 cm = 250 cm.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ea8f034c9a8dee94d2415872a19de78afce493b3eff10626ab53325d29ff4260`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 1424 |
| 2 | success | valid / verified | applying | procedural | Medium | 1467 |
| 3 | success | valid / verified | applying | procedural | Easy | 1443 |

Run 1 — solusi: Total kebutuhan kain = 3 seragam x 200 cm/seragam = 600 cm. Sisa kain = 850 cm - 600 cm = 250 cm.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan operasi perkalian dan pengurangan dalam konteks masalah sehari-hari yang rutin.. Bukti: 3 pesanan seragam; panjang kain yang dibutuhkan untuk setiap seragam adalah 200 cm; Ibu Meutia memiliki kain dengan panjang 850 cm
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma perkalian dan pengurangan dalam konteks pengukuran panjang.. Bukti: 3 pesanan seragam; 200 cm; 850 cm
- Intended difficulty `classify/Medium`: Soal melibatkan dua langkah operasi aritmatika dasar (perkalian dan pengurangan) yang umum untuk kelas 3.. Bukti: 3 pesanan seragam; 200 cm; 850 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian dasar dan pengurangan bilangan ratusan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah diajarkan perkalian dan pengurangan bilangan ratusan dalam konteks satuan panjang. |

Run 2 — solusi: Total kebutuhan kain = 3 seragam x 200 cm/seragam = 600 cm. Sisa kain = 850 cm - 600 cm = 250 cm.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur perkalian dan pengurangan dalam konteks masalah sehari-hari yang rutin.. Bukti: 3 pesanan seragam; panjang kain yang dibutuhkan untuk setiap seragam adalah 200 cm; Ibu Meutia memiliki kain dengan panjang 850 cm
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut pemahaman tentang algoritma perkalian dan pengurangan untuk menyelesaikan masalah pengukuran.. Bukti: 3 pesanan seragam; panjang kain yang dibutuhkan untuk setiap seragam adalah 200 cm; 850 cm - (3 x 200 cm)
- Intended difficulty `classify/Medium`: Soal ini melibatkan dua langkah operasi hitung rutin (perkalian dan pengurangan) yang sesuai dengan kurikulum kelas 3.. Bukti: 3 pesanan seragam; 200 cm; 850 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian bilangan satu angka dengan ratusan dan pengurangan bilangan ratusan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi hitung dua langkah (perkalian lalu pengurangan) adalah standar kompetensi kelas 3 untuk pemecahan masalah. |

Run 3 — solusi: Total kebutuhan kain = 3 seragam x 200 cm = 600 cm. Sisa kain = 850 cm - 600 cm = 250 cm.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi informasi, melakukan operasi perkalian sederhana untuk total kebutuhan, dan pengurangan untuk mencari sisa. Ini adalah penerapan prosedur rutin pada situasi kontekstual.. Bukti: 3 pesanan seragam; panjang kain yang dibutuhkan untuk setiap seragam adalah 200 cm; Ibu Meutia memiliki kain dengan panjang 850 cm
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penggunaan algoritma perkalian dan pengurangan (prosedural) untuk menyelesaikan masalah pengukuran panjang.. Bukti: 3 pesanan seragam; 200 cm; 850 cm
- Intended difficulty `classify/Easy`: Soal ini melibatkan dua langkah operasi hitung dasar (perkalian dan pengurangan) yang familiar bagi siswa kelas 3, dengan konteks yang jelas.. Bukti: 3 pesanan seragam; 200 cm; 850 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman perkalian dasar dan pengurangan bilangan ratusan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi hitung dua langkah (perkalian dan pengurangan) adalah standar kompetensi kelas 3 SD. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `2781`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa harus menerapkan prosedur perkalian dan pengurangan dalam konteks masalah sehari-hari yang rutin.
- Dimensi pengetahuan `procedural`: Soal ini menguji penggunaan algoritma perkalian dan pengurangan untuk menyelesaikan masalah pengukuran.
- Intended difficulty `Medium`: Soal ini melibatkan dua langkah operasi hitung rutin (perkalian dan pengurangan) yang sesuai dengan kurikulum kelas 3.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian bilangan satu angka dengan ratusan dan pengurangan bilangan ratusan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi hitung dua langkah (perkalian lalu pengurangan) adalah standar kompetensi kelas 3 untuk pemecahan masalah. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 102/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000020; applying=0.999980; reasoning=0.000000 | applying | 0.999980 | 0.000210 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.228600; conceptual=0.760225; procedural=0.011175; metacognitive=0.000000 | conceptual | 0.760225 | 0.429917 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.880127; Medium=0.115650; Hard=0.004224 | Easy | 0.880127 | 0.350399 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999980; −Σp ln(p) = 0.000231; H = 0.000231/ln(3) = 0.000210; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.760225; −Σp ln(p) = 0.595992; H = 0.595992/ln(4) = 0.429917; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.880127; −Σp ln(p) = 0.384953; H = 0.384953/ln(3) = 0.350399; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Pengukuran Panjang dengan Satuan Baku
Tipe soal: multiple_choice
Stimulus: -
Soal: Ibu Meutia membeli kain untuk seragam. Terdapat 3 pesanan seragam dari sekolah kebangsaan. Ukuran panjang kain yang dibutuhkan untuk setiap seragam adalah 200 cm. Ibu Meutia memiliki kain dengan panjang 850 cm.

Berapakah panjang sisa kain Ibu Meutia?
Pilihan: A. 250 cm
B. 150 cm
C. 350 cm
D. 600 cm
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 22. Soal `08ecea23df04cbe525f37e73`

Ibu Meutia membeli kain untuk seragam. Terdapat 3 pesanan seragam dari sekolah kebangsaan. Ukuran panjang kain yang dibutuhkan untuk setiap seragam adalah 200 cm. Ibu Meutia memiliki kain dengan panjang 850 cm.<br><br>Apakah ada sisa kain yang dimiliki Ibu Meutia?

| Opsi | Isi |
|---|---|
| A | Tidak ada |
| B | Tidak dapat ditentukan |
| C | Ada, tetapi kurang dari kebutuhan satu seragam |
| D | Ada |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Total kebutuhan kain = 3 seragam x 200 cm = 600 cm. Sisa kain = 850 cm - 600 cm = 250 cm. Karena 250 cm > 0, maka ada sisa kain.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4b76075100c00e63cafbfa5cb5089cfbcbca9b58684f0d66beb4271420dfc12a`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 1398 |
| 2 | success | valid / verified | applying | procedural | Easy | 1442 |
| 3 | success | valid / verified | applying | conceptual | Medium | 1383 |

Run 1 — solusi: Total kebutuhan kain = 3 seragam x 200 cm = 600 cm. Sisa kain = 850 cm - 600 cm = 250 cm. Karena 250 cm > 0, maka ada sisa kain.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur perkalian sederhana untuk menentukan total kebutuhan, kemudian melakukan pengurangan untuk membandingkan dengan persediaan.. Bukti: 3 pesanan seragam; 200 cm; 850 cm
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penggunaan algoritma perkalian dan pengurangan (prosedural) untuk menyelesaikan masalah pengukuran.. Bukti: 3 pesanan seragam; 200 cm; 850 cm
- Intended difficulty `classify/Medium`: Soal ini melibatkan dua langkah rutin (perkalian dan pengurangan) yang sesuai untuk tingkat kelas 3, dengan konteks yang familiar.. Bukti: 3 pesanan seragam; 200 cm; 850 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian dasar dan pengurangan bilangan ratusan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tingkat kesulitan menengah karena siswa harus melakukan dua operasi hitung berurutan (perkalian lalu pengurangan) untuk mendapatkan jawaban akhir. |

Run 2 — solusi: Total kebutuhan kain = 3 seragam x 200 cm/seragam = 600 cm. Sisa kain = 850 cm - 600 cm = 250 cm. Karena 250 cm > 0, maka ada sisa kain.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan informasi (jumlah seragam dan kebutuhan per seragam) untuk menghitung total kebutuhan, lalu membandingkannya dengan persediaan untuk menjawab pertanyaan.. Bukti: 3 pesanan seragam; panjang kain yang dibutuhkan untuk setiap seragam adalah 200 cm; Ibu Meutia memiliki kain dengan panjang 850 cm
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan prosedur perkalian sederhana dan pengurangan untuk menyelesaikan masalah kontekstual.. Bukti: 3 pesanan seragam; 200 cm; 850 cm
- Intended difficulty `classify/Easy`: Soal melibatkan operasi hitung dasar (perkalian dan pengurangan) dalam konteks sehari-hari yang rutin bagi siswa kelas 3.. Bukti: 3 pesanan seragam; 200 cm; 850 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian dasar dan pengurangan bilangan ratusan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi hitung yang diminta sesuai dengan kurikulum kelas 3, yaitu perkalian dan pengurangan bilangan hingga 1000. |

Run 3 — solusi: Total kebutuhan kain = 3 seragam x 200 cm = 600 cm. Sisa kain = 850 cm - 600 cm = 250 cm. Karena 250 cm > 0, maka ada sisa kain.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan operasi perkalian dan pengurangan pada situasi kontekstual rutin untuk menentukan sisa.. Bukti: 3 pesanan seragam; 200 cm; 850 cm
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman tentang hubungan antara jumlah unit dan total panjang (konsep perkalian) serta operasi pengurangan.. Bukti: 3 pesanan seragam; 200 cm
- Intended difficulty `classify/Medium`: Soal melibatkan dua langkah rutin (perkalian dan pengurangan) yang sesuai dengan kurikulum kelas 3.. Bukti: 3 pesanan seragam; 200 cm; 850 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian dasar dan pengurangan bilangan ratusan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah mempelajari perkalian dan pengurangan bilangan hingga 1000, soal ini menguji aplikasi konsep tersebut dalam konteks sehari-hari. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `2779`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur perkalian untuk menghitung total kebutuhan kain, kemudian melakukan pengurangan untuk membandingkan dengan persediaan yang ada. Ini adalah penerapan konsep matematika dalam situasi rutin.
- Dimensi pengetahuan `procedural`: Soal ini menuntut penggunaan algoritma perkalian dan pengurangan (prosedural) untuk menyelesaikan masalah pengukuran.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena memerlukan dua langkah operasi hitung berurutan (perkalian lalu pengurangan) yang harus dilakukan secara akurat oleh siswa kelas 3.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian dasar dan pengurangan bilangan ratusan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tingkat kesulitan menengah karena siswa harus melakukan dua operasi hitung berurutan (perkalian lalu pengurangan) untuk mendapatkan jawaban akhir. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 110/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000001; applying=0.999999; reasoning=0.000000 | applying | 0.999999 | 0.000009 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.041531; conceptual=0.942972; procedural=0.015497; metacognitive=0.000000 | conceptual | 0.942972 | 0.181830 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.825719; Medium=0.168748; Hard=0.005533 | Easy | 0.825719 | 0.443415 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999999; −Σp ln(p) = 0.000010; H = 0.000010/ln(3) = 0.000009; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.942972; −Σp ln(p) = 0.252069; H = 0.252069/ln(4) = 0.181830; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.825719; −Σp ln(p) = 0.487141; H = 0.487141/ln(3) = 0.443415; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Pengukuran Panjang dengan Satuan Baku
Tipe soal: multiple_choice
Stimulus: -
Soal: Ibu Meutia membeli kain untuk seragam. Terdapat 3 pesanan seragam dari sekolah kebangsaan. Ukuran panjang kain yang dibutuhkan untuk setiap seragam adalah 200 cm. Ibu Meutia memiliki kain dengan panjang 850 cm.

Apakah ada sisa kain yang dimiliki Ibu Meutia?
Pilihan: A. Tidak ada
B. Tidak dapat ditentukan
C. Ada, tetapi kurang dari kebutuhan satu seragam
D. Ada
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 23. Soal `1c5670f69b8db58e4f5e09c6`

Pada lomba 17 Agustusan, warga RT 005 mengadakan lomba balap karung. Panjang lintasan yang harus ditempuh 900 cm. Syarat pemenang lomba adalah peserta yang tercepat kembali ke tempat semula.<br><br>Berapa total panjang lintasan yang harus dilalui peserta lomba balap karung?

| Opsi | Isi |
|---|---|
| A | 450 cm |
| B | 1.800 cm |
| C | 900 cm |
| D | 2.700 cm |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Lintasan pergi 900 cm dan kembali 900 cm. Total = 900 cm + 900 cm = 1.800 cm.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `01a4bb3676b88b087fbfd727060669408b3cb67a26b60d5e49dd4930a2d0e53d`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1409 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1424 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1426 |

Run 1 — solusi: Lintasan pergi 900 cm dan kembali 900 cm. Total = 900 cm + 900 cm = 1.800 cm.
- Domain kognitif `classify/applying`: Siswa perlu memahami konteks soal (pergi dan kembali) dan menerapkan operasi perkalian atau penjumlahan berulang yang rutin.. Bukti: Panjang lintasan yang harus ditempuh 900 cm; peserta yang tercepat kembali ke tempat semula
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep jarak tempuh pulang-pergi yang merupakan prinsip dasar dalam situasi pengukuran.. Bukti: Panjang lintasan yang harus ditempuh 900 cm; kembali ke tempat semula
- Intended difficulty `classify/Easy`: Soal ini melibatkan situasi rutin yang memerlukan satu langkah logika sederhana (mengalikan dua) tanpa kompleksitas tambahan.. Bukti: Panjang lintasan yang harus ditempuh 900 cm; kembali ke tempat semula

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep jarak dan operasi perkalian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah terbiasa dengan soal cerita sederhana yang melibatkan operasi hitung dasar dan logika sehari-hari. |

Run 2 — solusi: Total lintasan = 2 x 900 cm = 1.800 cm.
- Domain kognitif `classify/applying`: Siswa perlu memahami situasi kontekstual (pergi dan kembali) dan menerapkan operasi perkalian dasar untuk menyelesaikan masalah rutin.. Bukti: Panjang lintasan yang harus ditempuh 900 cm; peserta yang tercepat kembali ke tempat semula
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang jarak tempuh pulang-pergi yang melibatkan operasi perkalian sederhana.. Bukti: 900 cm; kembali ke tempat semula
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin satu langkah yang sesuai untuk kelas 3, di mana siswa hanya perlu mengidentifikasi bahwa perjalanan pulang-pergi berarti dua kali jarak satu arah.. Bukti: Panjang lintasan yang harus ditempuh 900 cm; kembali ke tempat semula

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep jarak pulang-pergi dan perkalian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah terbiasa dengan operasi perkalian dasar dan masalah cerita sederhana yang melibatkan konteks sehari-hari. |

Run 3 — solusi: Lintasan balap karung adalah pergi dan kembali, sehingga total jarak adalah 900 cm + 900 cm = 1.800 cm.
- Domain kognitif `classify/applying`: Siswa perlu memahami konteks soal (pergi dan kembali) dan menerapkan operasi perkalian atau penjumlahan berulang yang sederhana.. Bukti: Panjang lintasan yang harus ditempuh 900 cm; peserta yang tercepat kembali ke tempat semula
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang jarak tempuh pulang-pergi.. Bukti: Panjang lintasan yang harus ditempuh 900 cm; kembali ke tempat semula
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya melibatkan satu operasi hitung dasar (perkalian dua atau penjumlahan) dengan konteks yang sangat familiar bagi siswa kelas 3.. Bukti: Panjang lintasan yang harus ditempuh 900 cm; kembali ke tempat semula

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang operasi perkalian atau penjumlahan bilangan ratusan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah terbiasa dengan operasi hitung dasar dan soal cerita sederhana yang melibatkan logika sehari-hari. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 104/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000000 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.236612; conceptual=0.740796; procedural=0.022592; metacognitive=0.000000 | conceptual | 0.740796 | 0.468101 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.857178; Medium=0.139315; Hard=0.003508 | Easy | 0.857178 | 0.388235 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000000; H = 0.000000/ln(3) = 0.000000; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.740796; −Σp ln(p) = 0.648926; H = 0.648926/ln(4) = 0.468101; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.857178; −Σp ln(p) = 0.426520; H = 0.426520/ln(3) = 0.388235; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Hubungan Antarsatuan Baku Panjang
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada lomba 17 Agustusan, warga RT 005 mengadakan lomba balap karung. Panjang lintasan yang harus ditempuh 900 cm. Syarat pemenang lomba adalah peserta yang tercepat kembali ke tempat semula.

Berapa total panjang lintasan yang harus dilalui peserta lomba balap karung?
Pilihan: A. 450 cm
B. 1.800 cm
C. 900 cm
D. 2.700 cm
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 24. Soal `8daba6059f9c3edf55ee4254`

Pada lomba 17 Agustusan, warga RT 005 mengadakan lomba balap karung. Panjang lintasan yang harus ditempuh 900 cm. Syarat pemenang lomba adalah peserta yang tercepat kembali ke tempat semula.<br><br>Ubahlah satuan cm menjadi m!

| Opsi | Isi |
|---|---|
| A | 1,8 m |
| B | 9 m |
| C | 18 m |
| D | 180 m |

Kunci sumber: `C`; status AI: `conflict`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: 900 cm = 900 / 100 m = 9 m. Kunci jawaban C (18 m) salah karena tidak sesuai dengan angka 900 cm yang tertera pada soal.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f6c067a21e1dd3a52c5d91a6815517b963b9770d7e5067fb45f158a06f8ffb9c`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | concern / conflict | applying | conceptual | Easy | 1426 |
| 2 | success | concern / conflict | applying | procedural | Easy | 1439 |
| 3 | success | concern / conflict | applying | procedural | Easy | 1440 |

Run 1 — solusi: Soal meminta konversi 900 cm ke meter. Karena 100 cm = 1 m, maka 900 cm = 900 / 100 = 9 m. Kunci jawaban C (18 m) tidak sesuai dengan data soal.
- Domain kognitif `classify/applying`: Siswa diminta melakukan konversi satuan panjang sederhana, yang merupakan proses rutin dalam matematika dasar.. Bukti: Ubahlah satuan cm menjadi m!
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang hubungan antara satuan sentimeter dan meter (konsep konversi).. Bukti: Hubungan Antarsatuan Baku Panjang
- Intended difficulty `classify/Easy`: Tugas ini adalah prosedur konversi standar yang familiar bagi siswa kelas 3, melibatkan satu langkah pembagian sederhana.. Bukti: Ubahlah satuan cm menjadi m!

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman hubungan 1 m = 100 cm |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konversi satuan panjang dasar adalah materi standar kelas 3 SD. |

Run 2 — solusi: Jika soal adalah 900 cm, maka 900 cm / 100 = 9 m. Jika soal adalah 1.800 cm, maka 1.800 cm / 100 = 18 m. Kunci C (18 m) tidak sesuai dengan angka 900 cm pada teks soal.
- Domain kognitif `classify/applying`: Siswa diminta melakukan konversi satuan panjang baku (cm ke m) yang merupakan prosedur rutin.. Bukti: Ubahlah satuan cm menjadi m!
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menerapkan algoritma pembagian dengan 100 untuk mengonversi satuan panjang.. Bukti: Ubahlah satuan cm menjadi m!
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung bagi siswa kelas 3 yang sudah mempelajari hubungan antarsatuan panjang.. Bukti: Panjang lintasan yang harus ditempuh 900 cm; Ubahlah satuan cm menjadi m!

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman hubungan 1 m = 100 cm. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konversi satuan panjang dasar adalah materi standar kelas 3 SD. |

Run 3 — solusi: Jika soal adalah 900 cm, maka 900 cm = 9 m. Jika soal adalah 1.800 cm, maka 1.800 cm = 18 m. Kunci jawaban C (18 m) tidak sesuai dengan angka 900 cm yang tertulis di soal.
- Domain kognitif `classify/applying`: Siswa diminta melakukan konversi satuan panjang sederhana, yang merupakan prosedur rutin.. Bukti: Ubahlah satuan cm menjadi m!
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma konversi satuan panjang (cm ke m).. Bukti: Ubahlah satuan cm menjadi m!
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, hanya memerlukan satu langkah konversi satuan dasar (membagi dengan 100).. Bukti: Panjang lintasan yang harus ditempuh 900 cm; Ubahlah satuan cm menjadi m!

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman hubungan 100 cm = 1 m. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konversi satuan panjang dasar adalah materi standar kelas 3 SD. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2675`.
Konten: `concern`; kunci: `conflict`; masalah: Terdapat ketidaksesuaian antara data numerik dalam soal (900 cm) dengan kunci jawaban yang disediakan (18 m).; Kunci jawaban C (18 m) mengasumsikan nilai 1.800 cm, yang tidak ada dalam teks soal.; Soal mengandung informasi yang tidak relevan (lomba balap karung, RT 005) yang tidak mempengaruhi perhitungan konversi satuan..
- Domain kognitif `applying`: Siswa diminta menerapkan prosedur konversi satuan panjang yang merupakan tugas rutin.
- Dimensi pengetahuan `procedural`: Soal menguji penerapan algoritma konversi satuan panjang (cm ke m).
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung, hanya memerlukan satu langkah konversi satuan dasar (membagi dengan 100).

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman hubungan 100 cm = 1 m. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konversi satuan panjang dasar adalah materi standar kelas 3 SD. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 97/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |

<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Hubungan Antarsatuan Baku Panjang
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada lomba 17 Agustusan, warga RT 005 mengadakan lomba balap karung. Panjang lintasan yang harus ditempuh 900 cm. Syarat pemenang lomba adalah peserta yang tercepat kembali ke tempat semula.

Ubahlah satuan cm menjadi m!
Pilihan: A. 1,8 m
B. 9 m
C. 18 m
D. 180 m
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `revision_required`.
Status konten: `concern`. Catatan konten: Terdapat ketidaksesuaian antara data numerik dalam soal (900 cm) dengan kunci jawaban yang disediakan (18 m).; Kunci jawaban C (18 m) mengasumsikan nilai 1.800 cm, yang tidak ada dalam teks soal.; Soal mengandung informasi yang tidak relevan (lomba balap karung, RT 005) yang tidak mempengaruhi perhitungan konversi satuan..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 25. Soal `a258009ba2d7730a91f12d2e`

Meutia menimbang tepung untuk bahan membuat kue. Timbangan yang digunakan adalah timbangan duduk dengan satuan kg. Meutia meletakkan tepung dan jarum timbangan menunjuk angka 4 kurang 3 garis. Berapa berat tepung yang ditimbang Meutia?

| Opsi | Isi |
|---|---|
| A | 3 kg 970 gram |
| B | 4 kg 300 gram |
| C | 3 kg 700 gram |
| D | 3 kg 300 gram |

![Gambar sumber soal 25](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0151-11.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Setiap 1 kg terbagi menjadi 10 garis kecil, sehingga 1 garis = 100 gram. Posisi jarum 3 garis sebelum 4 kg adalah 4 kg - (3 x 100 gram) = 4 kg - 300 gram = 3 kg 700 gram.
Gambar sumber: images/kelas3_panduan_siswa_kelas3.pdf-0151-11.png. Transkripsi visual: Timbangan analog dengan piringan di atas berisi tepung. Dial timbangan memiliki angka 0 sampai 11. Jarum menunjuk ke posisi sebelum angka 4, tepatnya 3 garis kecil sebelum angka 4. Antara angka 3 dan 4 terdapat 10 garis kecil.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `313da751289d7718d5fc9589f5ac6c02bb1081085b9abe03edc9bb47f0232ed4`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2710 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2708 |
| 3 | success | valid / verified | applying | procedural | Medium | 2762 |

Run 1 — solusi: Setiap 1 kg terbagi menjadi 10 garis, sehingga 1 garis = 100 gram. Posisi jarum 3 garis sebelum 4 kg adalah 4 kg - (3 x 100 gram) = 4 kg - 300 gram = 3 kg 700 gram.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasikan skala timbangan (membaca representasi visual) dan menerapkan prosedur konversi satuan berat (kg ke gram) untuk menyelesaikan masalah rutin.. Bukti: jarum timbangan menunjuk angka 4 kurang 3 garis; Setiap 1 kg pada dial terbagi 10 garis kecil
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami hubungan antara satuan kg dan gram serta struktur skala pada alat ukur (konsep pengukuran).. Bukti: timbangan duduk dengan satuan kg; Setiap 1 kg pada dial terbagi 10 garis kecil
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemahaman tentang pembacaan skala timbangan yang melibatkan pengurangan dari angka bulat terdekat, yang merupakan prosedur standar namun memerlukan ketelitian.. Bukti: angka 4 kurang 3 garis; timbangan duduk dengan satuan kg

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang satuan berat (kg ke gram) dan cara membaca skala timbangan analog. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah diajarkan pengukuran berat dengan timbangan. Membaca skala yang tidak tepat pada angka bulat (kurang dari angka tertentu) adalah tantangan yang sesuai untuk tingkat ini. |

Run 2 — solusi: Setiap 1 kg terbagi menjadi 10 garis, sehingga 1 garis = 100 gram. Posisi jarum 3 garis sebelum 4 kg berarti 4 kg - (3 x 100 gram) = 4 kg - 300 gram = 3 kg 700 gram.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasikan skala timbangan (membaca representasi) dan menerapkan prosedur pengurangan sederhana untuk menentukan berat yang tepat.. Bukti: jarum timbangan menunjuk angka 4 kurang 3 garis; Setiap 1 kg pada dial terbagi 10 garis kecil
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara satuan kilogram dan pembagian skala pada alat ukur.. Bukti: timbangan duduk dengan satuan kg; Setiap 1 kg pada dial terbagi 10 garis kecil
- Intended difficulty `classify/Medium`: Soal ini memerlukan interpretasi visual terhadap skala alat ukur yang tidak tepat pada angka utama, yang merupakan langkah rutin dalam pembelajaran pengukuran kelas 3.. Bukti: jarum timbangan menunjuk angka 4 kurang 3 garis; Setiap 1 kg pada dial terbagi 10 garis kecil

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konversi 1 kg = 1000 gram dan kemampuan membaca skala timbangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah diajarkan membaca timbangan, namun interpretasi 'kurang dari' angka tertentu memerlukan ketelitian lebih dibanding membaca angka bulat. |

Run 3 — solusi: Timbangan menunjukkan angka 4 kg dikurangi 3 garis kecil. Karena 1 kg = 1000 gram dan terbagi 10 garis, maka 1 garis = 100 gram. 4 kg - (3 x 100 gram) = 4000 gram - 300 gram = 3700 gram = 3 kg 700 gram.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasikan skala timbangan (membaca representasi visual) dan menerapkan prosedur konversi satuan berat (kg ke gram) untuk menyelesaikan masalah rutin ini.. Bukti: jarum timbangan menunjuk angka 4 kurang 3 garis; Setiap 1 kg pada dial terbagi 10 garis kecil
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara membaca skala timbangan analog dan melakukan operasi pengurangan sederhana dengan konversi satuan.. Bukti: timbangan duduk dengan satuan kg; Setiap 1 kg pada dial terbagi 10 garis kecil
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium untuk kelas 3 karena memerlukan interpretasi visual skala (membaca 'kurang 3 garis') dan pemahaman hubungan antar satuan berat, bukan sekadar membaca angka bulat.. Bukti: jarum timbangan menunjuk angka 4 kurang 3 garis; Setiap 1 kg pada dial terbagi 10 garis kecil

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar satuan berat (kg ke gram) dan kemampuan membaca skala analog. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah diajarkan pengukuran berat, namun membaca skala dengan presisi 'kurang dari' memerlukan ketelitian lebih dibanding membaca angka tepat. |

Histori retry: run 2 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 3 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4241`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menginterpretasikan representasi visual skala timbangan dan menerapkan prosedur pengurangan sederhana untuk menentukan nilai berat yang tepat.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara satuan kilogram dan pembagian skala pada alat ukur (skala analog).
- Intended difficulty `Medium`: Soal ini memerlukan interpretasi visual terhadap skala alat ukur yang tidak tepat pada angka utama, yang merupakan langkah rutin dalam pembelajaran pengukuran kelas 3.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konversi 1 kg = 1000 gram dan kemampuan membaca skala timbangan analog. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah diajarkan membaca timbangan, namun interpretasi 'kurang dari' angka tertentu memerlukan ketelitian lebih dibanding membaca angka bulat. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 149/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000022; applying=0.999978; reasoning=0.000000 | applying | 0.999978 | 0.000237 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.044080; conceptual=0.925193; procedural=0.030727; metacognitive=0.000000 | conceptual | 0.925193 | 0.228346 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.755825; Medium=0.237994; Hard=0.006182 | Easy | 0.755825 | 0.532193 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999978; −Σp ln(p) = 0.000261; H = 0.000261/ln(3) = 0.000237; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.925193; −Σp ln(p) = 0.316555; H = 0.316555/ln(4) = 0.228346; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.755825; −Σp ln(p) = 0.584673; H = 0.584673/ln(3) = 0.532193; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Pengukuran Berat dengan Satuan Baku
Tipe soal: multiple_choice
Stimulus: -
Soal: Meutia menimbang tepung untuk bahan membuat kue. Timbangan yang digunakan adalah timbangan duduk dengan satuan kg. Meutia meletakkan tepung dan jarum timbangan menunjuk angka 4 kurang 3 garis. Berapa berat tepung yang ditimbang Meutia?
Pilihan: A. 3 kg 970 gram
B. 4 kg 300 gram
C. 3 kg 700 gram
D. 3 kg 300 gram
Transkripsi visual: Timbangan analog dengan piringan di atas berisi tepung. Dial timbangan memiliki angka 0 sampai 11. Jarum menunjuk ke posisi sebelum angka 4, tepatnya 3 garis kecil sebelum angka 4. Antara angka 3 dan 4 terdapat 10 garis kecil.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 26. Soal `e35b2320cf47f2b1b2b92fc9`

Drio memiliki 10 kantong plastik berisi buah apel untuk dijual. Setiap plastik memiliki berat 3 kg. Buah apel yang terjual sebanyak 18 kg. Berapa sisa buah apel yang belum terjual?

| Opsi | Isi |
|---|---|
| A | 12 kg |
| B | 17 kg |
| C | 15 kg |
| D | 30 kg |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Total berat = 10 kantong * 3 kg/kantong = 30 kg. Sisa = 30 kg - 18 kg = 12 kg.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e14e376e006d5269e5afcbdb71986a54d3965a9a74566d59c8bd82ee4c1e3970`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1975 |
| 2 | success | valid / verified | applying | procedural | Easy | 1974 |
| 3 | success | valid / verified | applying | procedural | Medium | 1450 |

Run 1 — solusi: Total berat = 10 kantong * 3 kg/kantong = 30 kg. Sisa = 30 kg - 18 kg = 12 kg.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dan menerapkan operasi perkalian untuk mencari total berat, kemudian pengurangan untuk mencari sisa, yang merupakan penerapan konsep dalam situasi rutin.. Bukti: 10 kantong plastik berisi buah apel; Setiap plastik memiliki berat 3 kg; Buah apel yang terjual sebanyak 18 kg
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang konsep berat dan penggunaan algoritma perkalian serta pengurangan dasar.. Bukti: 10 kantong plastik; 3 kg; 18 kg
- Intended difficulty `classify/Easy`: Soal ini melibatkan dua langkah operasi aritmatika dasar (perkalian dan pengurangan) yang umum untuk kelas 3.. Bukti: 10 kantong plastik; 3 kg; 18 kg

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian dasar dan pengurangan bilangan dua digit. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi dua langkah (perkalian dan pengurangan) adalah standar untuk kelas 3. |

Run 2 — solusi: Total berat = 10 kantong * 3 kg/kantong = 30 kg. Sisa = 30 kg - 18 kg = 12 kg.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi operasi perkalian untuk menentukan total berat dan pengurangan untuk menentukan sisa, yang merupakan penerapan konsep berat dalam situasi rutin.. Bukti: 10 kantong plastik berisi buah apel; Setiap plastik memiliki berat 3 kg; Buah apel yang terjual sebanyak 18 kg
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma perkalian dan pengurangan dalam konteks pengukuran berat.. Bukti: 10 kantong plastik; berat 3 kg; terjual sebanyak 18 kg
- Intended difficulty `classify/Easy`: Soal ini melibatkan dua langkah operasi dasar (perkalian dan pengurangan) yang umum untuk kelas 3.. Bukti: 10 kantong plastik; 3 kg; 18 kg

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian dasar dan pengurangan bilangan dua digit. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi dua langkah (perkalian dan pengurangan) adalah standar untuk kelas 3. |

Run 3 — solusi: Total berat = 10 kantong x 3 kg/kantong = 30 kg. Sisa = 30 kg - 18 kg = 12 kg.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan operasi perkalian untuk mencari total berat dan pengurangan untuk mencari sisa, yang merupakan prosedur rutin dalam konteks soal cerita.. Bukti: 10 kantong plastik berisi buah apel; Setiap plastik memiliki berat 3 kg; Buah apel yang terjual sebanyak 18 kg
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma perkalian dan pengurangan dalam konteks pengukuran berat.. Bukti: 10 kantong plastik berisi buah apel; Setiap plastik memiliki berat 3 kg; Buah apel yang terjual sebanyak 18 kg
- Intended difficulty `classify/Medium`: Soal melibatkan dua langkah rutin (perkalian dan pengurangan) dengan angka yang sederhana, sesuai untuk tingkat kelas 3.. Bukti: 10 kantong plastik; 3 kg; 18 kg

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian dasar (10x3) dan pengurangan bilangan dua digit. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tingkat kesulitan sesuai untuk kelas 3 karena melibatkan dua operasi dasar yang sudah dipelajari (perkalian dan pengurangan) dalam satu konteks cerita. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 2, "Medium": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2726`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi dan menerapkan dua operasi aritmatika rutin (perkalian untuk total berat dan pengurangan untuk sisa) dalam konteks soal cerita.
- Dimensi pengetahuan `procedural`: Soal ini menguji penguasaan algoritma perkalian dan pengurangan dasar dalam konteks pengukuran berat.
- Intended difficulty `Easy`: Soal ini melibatkan dua langkah operasi aritmatika dasar yang rutin dan familiar bagi siswa kelas 3, dengan beban kognitif yang rendah.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian dasar (terutama perkalian dengan 10) dan pengurangan bilangan dua digit. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi dua langkah (perkalian dan pengurangan) adalah standar kurikulum kelas 3. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 88/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.063860; applying=0.936140; reasoning=0.000000 | applying | 0.936140 | 0.216144 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.290610; conceptual=0.692167; procedural=0.017223; metacognitive=0.000000 | conceptual | 0.692167 | 0.493220 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.866309; Medium=0.130889; Hard=0.002802 | Easy | 0.866309 | 0.370420 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.936140; −Σp ln(p) = 0.237459; H = 0.237459/ln(3) = 0.216144; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.692167; −Σp ln(p) = 0.683748; H = 0.683748/ln(4) = 0.493220; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.866309; −Σp ln(p) = 0.406948; H = 0.406948/ln(3) = 0.370420; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Pengukuran Berat dengan Satuan Baku
Tipe soal: multiple_choice
Stimulus: -
Soal: Drio memiliki 10 kantong plastik berisi buah apel untuk dijual. Setiap plastik memiliki berat 3 kg. Buah apel yang terjual sebanyak 18 kg. Berapa sisa buah apel yang belum terjual?
Pilihan: A. 12 kg
B. 17 kg
C. 15 kg
D. 30 kg
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 27. Soal `1a9d9923445f71c78d74086d`

Sebuah karung berisi 90 kg 460 gram beras dan karung lainnya berisi 25 kg 380 gram beras. Berapa berat beras dalam kedua karung tersebut?

| Opsi | Isi |
|---|---|
| A | 65 kg 840 gram |
| B | 115 kg 740 gram |
| C | 115 kg 840 gram |
| D | 116 kg 840 gram |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Penjumlahan satuan sejenis: (90 kg + 25 kg) = 115 kg dan (460 g + 380 g) = 840 g. Total: 115 kg 840 g.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0de1c8f3305b9fe0fe7d4239bde6b33af6f46a6a5e1cf80834ad79b2e89f927c`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1445 |
| 2 | success | valid / verified | applying | procedural | Medium | 1482 |
| 3 | success | valid / verified | applying | procedural | Easy | 1466 |

Run 1 — solusi: 90 kg + 25 kg = 115 kg; 460 g + 380 g = 840 g. Total: 115 kg 840 g.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur penjumlahan pada satuan berat yang berbeda (kg dan gram) secara terpisah, yang merupakan prosedur rutin di kelas 3.. Bukti: 90 kg 460 gram; 25 kg 380 gram; Berapa berat beras dalam kedua karung tersebut?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma penjumlahan satuan berat (kg dan gram) yang merupakan prosedur standar.. Bukti: 90 kg 460 gram; 25 kg 380 gram
- Intended difficulty `classify/Easy`: Soal ini melibatkan penjumlahan dua satuan yang berbeda namun tidak memerlukan konversi antar satuan (karena jumlah gram < 1000), sehingga termasuk kategori mudah.. Bukti: 90 kg 460 gram; 25 kg 380 gram; Berapa berat beras dalam kedua karung tersebut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah dan pemahaman satuan berat kg dan gram. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan satuan berat tanpa konversi (tanpa carry-over ke kg) adalah standar kompetensi kelas 3. |

Run 2 — solusi: Penjumlahan satuan sejenis: (90 kg + 25 kg) = 115 kg dan (460 g + 380 g) = 840 g. Hasilnya 115 kg 840 g.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur penjumlahan standar pada satuan berat yang berbeda (kg dan gram) dalam situasi rutin.. Bukti: 90 kg 460 gram beras dan karung lainnya berisi 25 kg 380 gram beras; Berapa berat beras dalam kedua karung tersebut?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma penjumlahan bilangan dengan satuan campuran (kg dan gram).. Bukti: 90 kg 460 gram; 25 kg 380 gram
- Intended difficulty `classify/Medium`: Soal ini melibatkan penjumlahan dua besaran dengan satuan campuran. Meskipun angkanya sederhana, siswa harus mengelola dua satuan secara terpisah namun simultan.. Bukti: 90 kg 460 gram; 25 kg 380 gram; Berapa berat beras dalam kedua karung tersebut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah dan pemahaman satuan berat (kg dan gram). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, penjumlahan dengan satuan campuran (kg dan gram) merupakan tantangan menengah karena memerlukan ketelitian dalam memisahkan dan menjumlahkan dua jenis satuan. |

Run 3 — solusi: Penjumlahan satuan sejenis: (90 kg + 25 kg) = 115 kg dan (460 g + 380 g) = 840 g. Hasilnya 115 kg 840 g.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur penjumlahan pada satuan berat yang berbeda (kg dan gram) dalam situasi rutin.. Bukti: 90 kg 460 gram beras dan karung lainnya berisi 25 kg 380 gram beras; Berapa berat beras dalam kedua karung tersebut?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma penjumlahan satuan berat yang terpisah namun terkait.. Bukti: 90 kg 460 gram; 25 kg 380 gram
- Intended difficulty `classify/Easy`: Soal ini melibatkan penjumlahan dua satuan berat yang berbeda secara terpisah tanpa perlu konversi antar satuan (karena jumlah gram < 1000), sehingga termasuk kategori mudah untuk kelas 3.. Bukti: 90 kg 460 gram; 25 kg 380 gram

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah hingga ratusan dan pemahaman satuan berat kg dan gram. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi penjumlahan dua satuan berat tanpa konversi (carry-over ke kg) adalah standar kompetensi kelas 3. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 2, "Medium": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2908`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur penjumlahan pada satuan berat yang berbeda (kg dan gram) secara terpisah, yang merupakan prosedur rutin di kelas 3.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang algoritma penjumlahan satuan berat (kg dan gram) yang merupakan prosedur standar.
- Intended difficulty `Easy`: Soal ini melibatkan penjumlahan dua satuan berat yang berbeda secara terpisah tanpa perlu konversi antar satuan (karena jumlah gram < 1000), sehingga termasuk kategori mudah untuk kelas 3.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah dan pemahaman satuan berat kg dan gram. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan satuan berat tanpa konversi (tanpa carry-over ke kg) adalah standar kompetensi kelas 3. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 93/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.007821; applying=0.992179; reasoning=0.000000 | applying | 0.992179 | 0.041626 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.221338; conceptual=0.763077; procedural=0.015585; metacognitive=0.000000 | conceptual | 0.763077 | 0.436402 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.905865; Medium=0.091473; Hard=0.002662 | Easy | 0.905865 | 0.295026 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.992179; −Σp ln(p) = 0.045731; H = 0.045731/ln(3) = 0.041626; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.763077; −Σp ln(p) = 0.604981; H = 0.604981/ln(4) = 0.436402; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.905865; −Σp ln(p) = 0.324119; H = 0.324119/ln(3) = 0.295026; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Hubungan Antarsatuan Baku Berat
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah karung berisi 90 kg 460 gram beras dan karung lainnya berisi 25 kg 380 gram beras. Berapa berat beras dalam kedua karung tersebut?
Pilihan: A. 65 kg 840 gram
B. 115 kg 740 gram
C. 115 kg 840 gram
D. 116 kg 840 gram
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 28. Soal `23dc07e9d3dc8f5423d3bb7e`

Meutia memiliki satu pohon mangga. Dari hasil panennya, Meutia mendapatkan 8.000 gram mangga. Kemudian Meutia menjual mangga tersebut sebanyak 4 kg. Berapa sisa mangga yang belum terjual?

| Opsi | Isi |
|---|---|
| A | 8.000 gram |
| B | 4.000 gram (4 kg) |
| C | 4.400 gram |
| D | 12.000 gram |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: 8.000 gram = 8 kg. Sisa = 8 kg - 4 kg = 4 kg atau 4.000 gram.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0b863e325c9720e5e4efba1621922f61acae38905fc63a173e40975fc0c8c4ca`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1420 |
| 2 | success | valid / verified | applying | procedural | Easy | 1431 |
| 3 | success | valid / verified | applying | procedural | Easy | 1463 |

Run 1 — solusi: 8.000 gram = 8 kg. Sisa = 8 kg - 4 kg = 4 kg atau 4.000 gram.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur konversi satuan berat (gram ke kg) dan melakukan operasi pengurangan dasar dalam situasi rutin.. Bukti: 8.000 gram; menjual mangga tersebut sebanyak 4 kg; Berapa sisa mangga yang belum terjual?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman tentang hubungan antarsatuan berat (konversi) dan penggunaan algoritma pengurangan.. Bukti: 8.000 gram; 4 kg
- Intended difficulty `classify/Easy`: Soal melibatkan konversi satuan dasar dan pengurangan satu langkah, yang merupakan prosedur standar untuk kelas 3.. Bukti: 8.000 gram; 4 kg

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konversi 1 kg = 1.000 gram dan operasi pengurangan bilangan ribuan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 3 mengenai pengukuran berat dan konversi satuan sederhana. |

Run 2 — solusi: 8.000 gram = 8 kg. Sisa = 8 kg - 4 kg = 4 kg atau 4.000 gram.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur konversi satuan berat (gram ke kg) dan menerapkan operasi pengurangan dasar dalam situasi rutin.. Bukti: 8.000 gram; 4 kg; Berapa sisa mangga yang belum terjual?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma konversi satuan berat dan urutan langkah penyelesaian masalah pengurangan.. Bukti: 8.000 gram; 4 kg
- Intended difficulty `classify/Easy`: Soal ini melibatkan konversi satuan dasar dan satu operasi pengurangan, yang merupakan prosedur standar untuk kelas 3.. Bukti: 8.000 gram; 4 kg; Berapa sisa mangga yang belum terjual?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konversi 1 kg = 1.000 gram dan operasi pengurangan bilangan ribuan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konversi satuan berat adalah materi standar kelas 3. Soal ini bersifat rutin tanpa jebakan kompleks. |

Run 3 — solusi: Konversi 4 kg ke gram: 4 kg = 4.000 gram. Sisa mangga = 8.000 gram - 4.000 gram = 4.000 gram atau 4 kg.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur konversi satuan berat (kg ke gram) dan melakukan operasi pengurangan dasar dalam konteks rutin.. Bukti: 8.000 gram; menjual mangga tersebut sebanyak 4 kg; Berapa sisa mangga yang belum terjual?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma konversi satuan berat (1 kg = 1.000 gram) dan teknik pengurangan.. Bukti: 8.000 gram; 4 kg
- Intended difficulty `classify/Easy`: Soal ini melibatkan prosedur rutin konversi satuan dan pengurangan sederhana yang sesuai dengan kurikulum kelas 3.. Bukti: 8.000 gram; 4 kg; Berapa sisa mangga yang belum terjual?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konversi satuan berat (kg ke gram) dan operasi pengurangan bilangan ribuan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah mempelajari hubungan antarsatuan berat dan operasi hitung dasar, sehingga soal ini termasuk kategori mudah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 107/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000004 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.058422; conceptual=0.931595; procedural=0.009983; metacognitive=0.000000 | conceptual | 0.931595 | 0.200479 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.876315; Medium=0.120015; Hard=0.003670 | Easy | 0.876315 | 0.355657 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000005; H = 0.000005/ln(3) = 0.000004; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.931595; −Σp ln(p) = 0.277922; H = 0.277922/ln(4) = 0.200479; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.876315; −Σp ln(p) = 0.390729; H = 0.390729/ln(3) = 0.355657; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Hubungan Antarsatuan Baku Berat
Tipe soal: multiple_choice
Stimulus: -
Soal: Meutia memiliki satu pohon mangga. Dari hasil panennya, Meutia mendapatkan 8.000 gram mangga. Kemudian Meutia menjual mangga tersebut sebanyak 4 kg. Berapa sisa mangga yang belum terjual?
Pilihan: A. 8.000 gram
B. 4.000 gram (4 kg)
C. 4.400 gram
D. 12.000 gram
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 29. Soal `dd3cb9360df4fe034e2f2480`

Urutkan gambar sesuai dengan waktu kegiatan.<br><br>Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).

| Opsi | Isi |
|---|---|
| A | bangun tidur, menyikat gigi, makan siang, bermain bola |
| B | menyikat gigi, bangun tidur, makan siang, bermain bola |
| C | bangun tidur, makan siang, menyikat gigi, bermain bola |
| D | bermain bola, makan siang, menyikat gigi, bangun tidur |

![Gambar sumber soal 29](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0198-04.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Mengurutkan kegiatan berdasarkan waktu pada jam: bangun tidur (06.00) -> menyikat gigi (08.00) -> makan siang (12.00) -> bermain bola (16.00). Urutan yang benar adalah C, D, B, A.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0198-04.png. Transkripsi visual: Gambar C: Anak bangun tidur, jam menunjukkan pukul 06.00. Gambar D: Anak menyikat gigi, jam menunjukkan pukul 08.00. Gambar B: Anak makan siang, jam menunjukkan pukul 12.00. Gambar A: Anak bermain bola, jam menunjukkan pukul 16.00.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ea663360cd956481e1ed8e54eeaddf416f5b4bae515217861e93250e7056019b`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2604 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2585 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2571 |

Run 1 — solusi: Mengurutkan kegiatan berdasarkan waktu pada jam: bangun tidur (06.00) -> menyikat gigi (08.00) -> makan siang (12.00) -> bermain bola (16.00). Urutan yang benar adalah C, D, B, A.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi waktu pada jam analog dan mengaitkannya dengan urutan kronologis kegiatan sehari-hari yang rutin. Ini adalah proses menerapkan pemahaman konsep waktu ke dalam situasi rutin.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan pengetahuan konseptual tentang urutan waktu (pagi, siang, sore) dan bagaimana waktu tersebut direpresentasikan pada jam analog.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan
- Intended difficulty `classify/Easy`: Soal ini meminta siswa mengurutkan empat kejadian berdasarkan jam yang tertera. Ini adalah tugas rutin yang melibatkan pembacaan jam sederhana dan pengurutan kronologis, sesuai untuk kelas 3.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca jam analog (pukul tepat) dan pemahaman urutan waktu sehari-hari. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 diharapkan sudah mampu membaca jam analog dan memahami urutan kegiatan harian. Tugas ini bersifat rutin dan tidak memerlukan strategi kompleks. |

Run 2 — solusi: Urutan waktu berdasarkan jam analog: 06:00 (bangun tidur) -> 08:00 (menyikat gigi) -> 12:00 (makan siang) -> 16:00 (bermain bola).
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi waktu pada jam analog dan mengurutkan kejadian berdasarkan kronologi waktu sehari-hari. Ini adalah proses menerapkan pemahaman konsep waktu ke dalam situasi rutin.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang urutan waktu dalam satu hari yang dikaitkan dengan pembacaan jam analog.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan
- Intended difficulty `classify/Easy`: Soal ini termasuk mudah karena menggunakan konteks kegiatan sehari-hari yang sangat familiar bagi siswa kelas 3 dan prosedur pengurutannya bersifat langsung.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca jam analog sederhana (jam tepat) dan pemahaman urutan waktu harian (pagi, siang, sore). |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah terbiasa dengan jadwal harian dan pembacaan jam analog dasar, sehingga tugas ini sesuai dengan tingkat perkembangan mereka. |

Run 3 — solusi: Urutan kronologis berdasarkan waktu pada jam: 06:00 (bangun tidur) -> 08:00 (menyikat gigi) -> 12:00 (makan siang) -> 16:00 (bermain bola).
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi waktu pada jam analog dan mengaitkannya dengan urutan kegiatan sehari-hari yang rutin, yang merupakan proses applying.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang urutan waktu dalam sehari dan pembacaan jam sederhana.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 3, melibatkan pembacaan jam sederhana dan pengurutan kejadian sehari-hari yang familiar.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mampu membaca jam analog (jam tepat) dan memahami urutan kegiatan harian. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 3 karena mengintegrasikan literasi waktu dasar dengan konteks kehidupan sehari-hari. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 167/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000885; applying=0.999115; reasoning=0.000000 | applying | 0.999115 | 0.006468 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.112005; conceptual=0.884968; procedural=0.003026; metacognitive=0.000000 | conceptual | 0.884968 | 0.267550 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.752109; Medium=0.241300; Hard=0.006591 | Easy | 0.752109 | 0.537420 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999115; −Σp ln(p) = 0.007106; H = 0.007106/ln(3) = 0.006468; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.884968; −Σp ln(p) = 0.370903; H = 0.370903/ln(4) = 0.267550; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.752109; −Σp ln(p) = 0.590416; H = 0.590416/ln(3) = 0.537420; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Waktu
Tipe soal: multiple_choice
Stimulus: -
Soal: Urutkan gambar sesuai dengan waktu kegiatan.

Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).
Pilihan: A. bangun tidur, menyikat gigi, makan siang, bermain bola
B. menyikat gigi, bangun tidur, makan siang, bermain bola
C. bangun tidur, makan siang, menyikat gigi, bermain bola
D. bermain bola, makan siang, menyikat gigi, bangun tidur
Transkripsi visual: Gambar C: Anak bangun tidur, jam menunjukkan pukul 06.00. Gambar D: Anak menyikat gigi, jam menunjukkan pukul 08.00. Gambar B: Anak makan siang, jam menunjukkan pukul 12.00. Gambar A: Anak bermain bola, jam menunjukkan pukul 16.00.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 30. Soal `75434d44f2b377da3027e153`

Temukan panjang pensil berikut. A B C. Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.<br><br>Urutan pensil dari paling pendek: ...., ...., ....

| Opsi | Isi |
|---|---|
| A | A, B, C |
| B | A, C, B |
| C | C, A, B |
| D | B, C, A |

![Gambar sumber soal 30](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0225-04.png>)


Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0225-04.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ce385a8708bc19c0b941f589e16babab13989544bb60c079510346f0031d7c35`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 113/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |

<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Mengukur Panjang Benda
Tipe soal: multiple_choice
Stimulus: -
Soal: Temukan panjang pensil berikut. A B C. Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.

Urutan pensil dari paling pendek: ...., ...., ....
Pilihan: A. A, B, C
B. A, C, B
C. C, A, B
D. B, C, A
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 31. Soal `e5989dcabcf5ead62a6aec0b`

KL adalah ....

| Opsi | Isi |
|---|---|
| A | Ruas garis |
| B | Garis |
| C | Sinar garis |
| D | Kurva/garis lengkung |

![Gambar sumber soal 31](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0162-00.png>)


Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas3_panduan_siswa_kelas3.pdf-0162-00.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9c7a39f956a4aea52ab41407097eadc26c6702ff45037b5aecbf1944292f35c1`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 59/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |

<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Sisi Pada Bangun Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: KL adalah ....
Pilihan: A. Ruas garis
B. Garis
C. Sinar garis
D. Kurva/garis lengkung
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 32. Soal `d0868911a2fc9547f4f8231b`

PQ adalah ....

| Opsi | Isi |
|---|---|
| A | Kurva/garis lengkung |
| B | Garis |
| C | Ruas garis |
| D | Sinar garis |

![Gambar sumber soal 32](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0162-01.png>)


Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas3_panduan_siswa_kelas3.pdf-0162-01.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6ac00d369bca6b3d4ec0048acc6ddd6343768d1554fe9e7b3ed48d749c093ae5`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 60/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |

<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Sisi Pada Bangun Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: PQ adalah ....
Pilihan: A. Kurva/garis lengkung
B. Garis
C. Ruas garis
D. Sinar garis
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 33. Soal `2c9c0a53b57350101ebd57b0`

Sebutkan nama sudut-sudut berikut. Tuliskan ukuran dan jenisnya.

| Opsi | Isi |
|---|---|
| A | ∠MON, ukurannya 120°, jenisnya sudut lancip |
| B | ∠MON, ukurannya 120°, jenisnya sudut tumpul |
| C | ∠MON, ukurannya 60°, jenisnya sudut lancip |
| D | ∠MON, ukurannya 90°, jenisnya sudut siku-siku |

![Gambar sumber soal 33](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0182-01.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Sudut MON pada gambar c memiliki bukaan lebih besar dari 90 derajat dan kurang dari 180 derajat, sehingga dikategorikan sebagai sudut tumpul. Nilai 120 derajat konsisten dengan visualisasi sudut tumpul tersebut.
Gambar sumber: images/kelas3_panduan_siswa_kelas3.pdf-0182-01.png. Transkripsi visual: Gambar c menunjukkan sudut MON dengan titik sudut O. Garis OM dan ON membentuk bukaan yang lebih lebar dari sudut siku-siku (90 derajat) tetapi kurang dari garis lurus (180 derajat).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menyebutkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `12f1e624918f3170214ec793f6bcb7077429fe16a99ef9c17dde34464ebb0843`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2617 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2715 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2742 |

Run 1 — solusi: Sudut MON pada gambar c memiliki bukaan lebih besar dari 90 derajat dan kurang dari 180 derajat, sehingga dikategorikan sebagai sudut tumpul. Nilai 120 derajat konsisten dengan visualisasi sudut tumpul tersebut.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi jenis sudut berdasarkan visualisasi (tumpul) dan mengaitkannya dengan estimasi ukuran yang logis (120 derajat). Ini adalah proses menerapkan pemahaman konsep sudut ke dalam situasi rutin.. Bukti: Sebutkan nama sudut-sudut berikut. Tuliskan ukuran dan jenisnya.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang klasifikasi sudut (lancip, siku-siku, tumpul) berdasarkan besarannya.. Bukti: jenisnya sudut tumpul; ukurannya 120°
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin untuk kelas 3 yang sedang mempelajari jenis-jenis sudut. Siswa hanya perlu membandingkan bukaan sudut dengan sudut siku-siku (benchmark).. Bukti: Sebutkan nama sudut-sudut berikut. Tuliskan ukuran dan jenisnya.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang sudut siku-siku sebagai acuan (90 derajat). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pada kelas 3, pengenalan sudut tumpul dan lancip adalah materi standar. Soal ini langsung menanyakan identifikasi tanpa langkah kompleks. |

Run 2 — solusi: Sudut MON pada gambar c memiliki bukaan lebih besar dari 90° dan kurang dari 180°, sehingga dikategorikan sebagai sudut tumpul. Nilai 120° adalah estimasi yang valid untuk sudut tumpul tersebut.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi jenis sudut berdasarkan visualisasi (tumpul) dan menerapkan pengetahuan tentang klasifikasi sudut (tumpul > 90°). Ini adalah proses penerapan konsep pada situasi rutin.. Bukti: Sebutkan nama sudut-sudut berikut. Tuliskan ukuran dan jenisnya.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang definisi dan kategori sudut (konseptual) serta kemampuan mengklasifikasikan sudut berdasarkan karakteristik visualnya.. Bukti: jenisnya sudut tumpul; ukurannya 120°
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya meminta identifikasi visual dasar dari jenis sudut yang sudah umum dipelajari di kelas 3.. Bukti: Sebutkan nama sudut-sudut berikut. Tuliskan ukuran dan jenisnya.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang sudut siku-siku, lancip, dan tumpul. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah diajarkan membedakan jenis sudut secara visual. Tugas ini adalah tugas rutin yang sesuai dengan tingkat perkembangan kognitif mereka. |

Run 3 — solusi: Sudut MON pada gambar c memiliki bukaan lebih besar dari 90° dan kurang dari 180°, sehingga dikategorikan sebagai sudut tumpul. Nilai 120° konsisten dengan estimasi visual sudut tumpul tersebut.
- Domain kognitif `classify/applying`: Siswa perlu mengenali karakteristik visual sudut (tumpul) dan mengaitkannya dengan estimasi ukuran derajat yang logis, yang merupakan proses applying konsep dasar geometri.. Bukti: Sebutkan nama sudut-sudut berikut. Tuliskan ukuran dan jenisnya.; jenisnya sudut tumpul
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami definisi dan kategori sudut (lancip, siku-siku, tumpul) serta hubungan antara bukaan sudut dengan estimasi besaran derajatnya.. Bukti: jenisnya sudut tumpul; ukurannya 120°
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah untuk kelas 3 karena hanya memerlukan identifikasi visual dasar terhadap jenis sudut yang familiar (tumpul) tanpa perhitungan rumit.. Bukti: Sebutkan nama sudut-sudut berikut. Tuliskan ukuran dan jenisnya.; ∠MON, ukurannya 120°, jenisnya sudut tumpul

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang jenis-jenis sudut (lancip, siku-siku, tumpul). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pada kelas 3, pengenalan jenis sudut berdasarkan bukaan (lebih besar/kecil dari siku-siku) adalah materi standar yang rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 129/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.277619; applying=0.722381; reasoning=0.000000 | applying | 0.722381 | 0.537670 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.021876; conceptual=0.970069; procedural=0.008055; metacognitive=0.000000 | conceptual | 0.970069 | 0.109596 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.759002; Medium=0.237641; Hard=0.003357 | Easy | 0.759002 | 0.518752 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.722381; −Σp ln(p) = 0.590691; H = 0.590691/ln(3) = 0.537670; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.970069; −Σp ln(p) = 0.151933; H = 0.151933/ln(4) = 0.109596; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.759002; −Σp ln(p) = 0.569907; H = 0.569907/ln(3) = 0.518752; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Sudut Pada Bidang Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebutkan nama sudut-sudut berikut. Tuliskan ukuran dan jenisnya.
Pilihan: A. ∠MON, ukurannya 120°, jenisnya sudut lancip
B. ∠MON, ukurannya 120°, jenisnya sudut tumpul
C. ∠MON, ukurannya 60°, jenisnya sudut lancip
D. ∠MON, ukurannya 90°, jenisnya sudut siku-siku
Transkripsi visual: Gambar c menunjukkan sudut MON dengan titik sudut O. Garis OM dan ON membentuk bukaan yang lebih lebar dari sudut siku-siku (90 derajat) tetapi kurang dari garis lurus (180 derajat).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: Soal meminta siswa menyebutkan nama, ukuran, dan jenis sudut, namun pilihan ganda hanya menyediakan satu sudut (∠MON) tanpa konteks gambar yang jelas untuk membedakan dari sudut lain (a-f).; Terdapat ketidaksesuaian antara instruksi soal (terbuka) dengan format pilihan ganda yang diberikan.; Soal meminta siswa menyebutkan nama, ukuran, dan jenis sudut, namun pilihan jawaban hanya berfokus pada satu sudut (∠MON) tanpa memberikan konteks bahwa ini adalah bagian dari serangkaian gambar (a-f).; Terdapat ketidaksesuaian antara instruksi soal yang bersifat terbuka (tuliskan) dengan format pilihan ganda yang disediakan..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 34. Soal `e856f8b6ea486b876939d3ba`

Sebutkan nama sudut-sudut berikut. Tuliskan ukuran dan jenisnya.

| Opsi | Isi |
|---|---|
| A | ∠RST, ukurannya 45°, jenisnya sudut lancip |
| B | ∠RST, ukurannya 180°, jenisnya sudut lurus |
| C | ∠RST, ukurannya 90°, jenisnya sudut siku-siku |
| D | ∠RST, ukurannya 90°, jenisnya sudut tumpul |

![Gambar sumber soal 34](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0182-01.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Simbol kotak kecil pada titik sudut S di gambar b menunjukkan sudut tersebut adalah sudut siku-siku, yang besarnya tepat 90°.
Gambar sumber: images/kelas3_panduan_siswa_kelas3.pdf-0182-01.png. Transkripsi visual: Gambar b menunjukkan sudut RST dengan simbol kotak kecil di titik sudut S, yang secara konvensional dalam geometri melambangkan sudut siku-siku (90 derajat).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menyebutkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `373b38ee342ab316f609b5e408a2dde7f777f9b79ac55924d50e6159f44e76cc`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2603 |
| 2 | success | valid / verified | knowing | factual | Easy | 2617 |
| 3 | success | valid / verified | knowing | factual | Easy | 2603 |

Run 1 — solusi: Simbol kotak kecil pada titik sudut S di gambar b menunjukkan sudut tersebut adalah sudut siku-siku, yang besarnya tepat 90°.
- Domain kognitif `classify/knowing`: Siswa diminta mengenali simbol geometris standar (kotak kecil) untuk mengidentifikasi jenis sudut dan ukurannya. Ini adalah proses pengenalan langsung terhadap fakta geometris.. Bukti: Sebutkan nama sudut-sudut berikut. Tuliskan ukuran dan jenisnya.; Pada gambar b, sudut RST digambar dengan tanda kotak kecil di titik sudut S
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman siswa terhadap simbol atau notasi geometris (fakta) bahwa tanda kotak kecil merepresentasikan sudut siku-siku.. Bukti: tanda kotak kecil di titik sudut S yang menunjukkan sudut tepat 90°
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar bagi siswa kelas 3, hanya memerlukan pengenalan simbol visual standar untuk sudut siku-siku tanpa perhitungan atau langkah kompleks.. Bukti: Sebutkan nama sudut-sudut berikut. Tuliskan ukuran dan jenisnya.; tanda kotak kecil di titik sudut S

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal konsep dasar sudut dan simbol sudut siku-siku. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 3 karena fokus pada pengenalan visual dasar sudut siku-siku yang merupakan materi awal geometri. |

Run 2 — solusi: Simbol kotak kecil pada titik sudut S dalam geometri secara universal merepresentasikan sudut siku-siku yang besarnya tepat 90 derajat.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali simbol konvensional (kotak kecil) untuk mengidentifikasi jenis sudut sebagai sudut siku-siku. Ini adalah proses pengenalan fakta geometris dasar.. Bukti: tanda kotak kecil di titik sudut S
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman siswa terhadap simbol atau notasi standar dalam geometri (fakta bahwa kotak kecil = 90 derajat).. Bukti: tanda kotak kecil di titik sudut S
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar karena hanya memerlukan pengenalan simbol visual yang sudah diajarkan sebagai standar untuk sudut siku-siku.. Bukti: tanda kotak kecil di titik sudut S

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang simbol sudut siku-siku. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, mengenali simbol sudut siku-siku adalah materi standar yang bersifat langsung dan rutin. |

Run 3 — solusi: Simbol kotak kecil pada titik sudut S di gambar b secara definisi geometri menunjukkan sudut siku-siku, yang besarnya adalah 90°.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengenali simbol geometris (kotak kecil) dan mengaitkannya dengan konsep sudut siku-siku yang sudah dipelajari. Ini adalah proses pengenalan langsung.. Bukti: Sebutkan nama sudut-sudut berikut. Tuliskan ukuran dan jenisnya.; tanda kotak kecil di titik sudut S yang menunjukkan sudut tepat 90°
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman siswa terhadap simbol atau notasi standar dalam geometri (kotak kecil untuk sudut siku-siku), yang merupakan pengetahuan faktual.. Bukti: tanda kotak kecil di titik sudut S yang menunjukkan sudut tepat 90°
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mengidentifikasi simbol visual yang sudah umum diajarkan di kelas 3 untuk sudut siku-siku.. Bukti: tanda kotak kecil di titik sudut S yang menunjukkan sudut tepat 90°

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal simbol sudut siku-siku (kotak kecil). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah diajarkan untuk mengidentifikasi sudut siku-siku melalui simbol visual atau alat bantu (seperti pojok kertas). |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 120/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.364257; applying=0.635743; reasoning=0.000000 | applying | 0.635743 | 0.596961 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.399815; conceptual=0.534506; procedural=0.065679; metacognitive=0.000000 | conceptual | 0.534506 | 0.634927 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.868342; Medium=0.128840; Hard=0.002818 | Easy | 0.868342 | 0.366962 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.635743; −Σp ln(p) = 0.655828; H = 0.655828/ln(3) = 0.596961; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.534506; −Σp ln(p) = 0.880195; H = 0.880195/ln(4) = 0.634927; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.868342; −Σp ln(p) = 0.403149; H = 0.403149/ln(3) = 0.366962; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Sudut Pada Bidang Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebutkan nama sudut-sudut berikut. Tuliskan ukuran dan jenisnya.
Pilihan: A. ∠RST, ukurannya 45°, jenisnya sudut lancip
B. ∠RST, ukurannya 180°, jenisnya sudut lurus
C. ∠RST, ukurannya 90°, jenisnya sudut siku-siku
D. ∠RST, ukurannya 90°, jenisnya sudut tumpul
Transkripsi visual: Gambar b menunjukkan sudut RST dengan simbol kotak kecil di titik sudut S, yang secara konvensional dalam geometri melambangkan sudut siku-siku (90 derajat).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: Soal meminta siswa menyebutkan nama, ukuran, dan jenis untuk semua sudut (a-f), namun pilihan jawaban hanya menyediakan analisis untuk satu sudut (∠RST) yang merujuk pada gambar b. Ini menunjukkan ketidaksesuaian antara instruksi soal dengan format pilihan ganda yang diberikan..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 35. Soal `f311bf91df38724a90b35b69`

Perhatikan huruf-huruf berikut ini.<br><br>Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?

| Opsi | Isi |
|---|---|
| A | Huruf M |
| B | Tidak ada |
| C | Huruf T |
| D | Huruf E |

![Gambar sumber soal 35](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0198-01.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Analisis huruf: M memiliki sepasang garis sejajar tetapi tidak ada garis tegak lurus. T memiliki garis tegak lurus tetapi tidak ada garis sejajar. E memiliki tiga pasang garis sejajar dan dua pasang garis tegak lurus. Tidak ada huruf yang memenuhi kriteria tepat satu pasang garis sejajar dan dua pasang garis tegak lurus.
Gambar sumber: images/kelas3_panduan_siswa_kelas3.pdf-0198-01.png. Transkripsi visual: Gambar menampilkan kata 'MATEMATIKA' yang ditulis dengan huruf kapital di atas kertas berpetak. Huruf-huruf tersebut adalah M, A, T, E, M, A, T, I, K, A.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e6eec90358a126ffb1835d6d90ecdc60b9d58bb616f711c2b11906176f354bb1`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2695 |
| 2 | success | valid / verified | applying | conceptual | Hard | 2688 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2708 |

Run 1 — solusi: Analyzing the letters provided in the image: M has parallel lines but no perpendicular lines. T has one perpendicular intersection but no parallel lines. E has three horizontal lines (parallel) and one vertical line, creating multiple perpendicular intersections and multiple pairs of parallel lines. None of the letters satisfy the condition of exactly one pair of parallel lines and two pairs of perpendicular lines.
- Domain kognitif `classify/applying`: Siswa perlu menganalisis properti geometris dari setiap huruf (sejajar dan tegak lurus) dan membandingkannya dengan kriteria yang diberikan, yang merupakan proses applying konsep pada situasi visual.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang definisi dan hubungan antar garis (sejajar dan tegak lurus) dalam bentuk huruf, yang merupakan pengetahuan konseptual.. Bukti: Garis-Garis Tegak Lurus dan Garis-Garis Sejajar
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk memeriksa setiap opsi secara sistematis terhadap dua kriteria geometris yang berbeda. Ini melibatkan lebih dari satu langkah rutin dan integrasi informasi visual.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang garis sejajar dan tegak lurus. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Untuk kelas 3, menganalisis properti geometris pada huruf memerlukan ketelitian visual yang cukup tinggi, sehingga dikategorikan Medium. |

Run 2 — solusi: Analisis huruf: M tidak memiliki garis tegak lurus. T hanya memiliki garis tegak lurus (tanpa sejajar). E memiliki 3 pasang garis sejajar dan 2 pasang garis tegak lurus. Tidak ada huruf yang memenuhi kriteria tepat satu pasang sejajar dan dua pasang tegak lurus.
- Domain kognitif `classify/applying`: Siswa harus menganalisis sifat geometris setiap huruf (sejajar/tegak lurus) dan membandingkannya dengan kriteria yang diberikan, yang memerlukan penerapan konsep pada situasi baru.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang hubungan geometris (sejajar dan tegak lurus) yang merupakan konsep dasar dalam geometri.. Bukti: Garis-Garis Tegak Lurus dan Garis-Garis Sejajar
- Intended difficulty `classify/Hard`: Soal ini menuntut siswa untuk melakukan analisis visual pada setiap opsi dan memverifikasi kondisi ganda (sejajar dan tegak lurus) secara simultan, yang cukup menantang untuk kelas 3.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang garis sejajar dan garis tegak lurus. |
| dependentSteps | 4 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 3 biasanya baru mengenal definisi garis. Menganalisis sifat geometris huruf secara mendetail dan mengeliminasi opsi berdasarkan kriteria ganda adalah tugas yang kompleks untuk level ini. |

Run 3 — solusi: Analisis huruf: M (tidak ada tegak lurus), T (satu tegak lurus, tidak ada sejajar), E (tiga pasang sejajar, dua tegak lurus). Tidak ada huruf yang memenuhi syarat tepat satu pasang sejajar dan dua pasang tegak lurus.
- Domain kognitif `classify/applying`: Siswa harus menganalisis properti geometris setiap huruf (sejajar dan tegak lurus) dan membandingkannya dengan kriteria yang diberikan, yang merupakan proses applying konsep pada situasi visual.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan geometris (sejajar dan tegak lurus) yang merupakan konsep dasar dalam geometri.. Bukti: Garis-Garis Tegak Lurus dan Garis-Garis Sejajar
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk memeriksa setiap opsi secara sistematis terhadap dua kriteria sekaligus. Ini melibatkan beberapa langkah rutin dan analisis visual yang cermat, yang sesuai untuk tingkat kesulitan menengah bagi kelas 3.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang garis sejajar dan tegak lurus. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 3 diharapkan mampu mengidentifikasi garis sejajar dan tegak lurus, namun melakukan verifikasi pada setiap huruf (M, T, E) dan menyimpulkan 'tidak ada' memerlukan ketelitian lebih tinggi daripada sekadar mengenali satu bentuk. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 2, "Hard": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4242`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa harus menerapkan pemahaman konsep garis sejajar dan tegak lurus untuk menganalisis properti geometris dari setiap huruf yang diberikan, kemudian membandingkannya dengan kriteria yang diminta.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang definisi dan hubungan antar garis (sejajar dan tegak lurus) dalam konteks visual.
- Intended difficulty `Medium`: Soal ini menuntut siswa untuk melakukan analisis visual sistematis pada beberapa objek (huruf) dan memverifikasi kondisi ganda secara simultan, yang merupakan tugas yang cukup menantang untuk tingkat kelas 3.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang garis sejajar dan garis tegak lurus. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 3 diharapkan mampu mengidentifikasi garis sejajar dan tegak lurus, namun melakukan verifikasi pada setiap huruf (M, T, E) dan menyimpulkan 'tidak ada' memerlukan ketelitian visual dan penalaran yang lebih tinggi daripada sekadar mengenali satu bentuk. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 122/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.007503; applying=0.992497; reasoning=0.000000 | applying | 0.992497 | 0.040218 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.048578; conceptual=0.933127; procedural=0.018296; metacognitive=0.000000 | conceptual | 0.933127 | 0.205379 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.818846; Medium=0.177538; Hard=0.003616 | Easy | 0.818846 | 0.446809 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.992497; −Σp ln(p) = 0.044184; H = 0.044184/ln(3) = 0.040218; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.933127; −Σp ln(p) = 0.284716; H = 0.284716/ln(4) = 0.205379; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.818846; −Σp ln(p) = 0.490870; H = 0.490870/ln(3) = 0.446809; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Garis-Garis Tegak Lurus dan Garis-Garis Sejajar
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan huruf-huruf berikut ini.

Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?
Pilihan: A. Huruf M
B. Tidak ada
C. Huruf T
D. Huruf E
Transkripsi visual: Gambar menampilkan kata 'MATEMATIKA' yang ditulis dengan huruf kapital di atas kertas berpetak. Huruf-huruf tersebut adalah M, A, T, E, M, A, T, I, K, A.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 36. Soal `548ed93702987b740b35d2b4`

Manakah dari pasangan garis berikut yang sejajar?

| Opsi | Isi |
|---|---|
| A | a dan b |
| B | a, b, c, dan e |
| C | c, d, dan e |
| D | a, b, c, d, dan e |

![Gambar sumber soal 36](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0196-03.png>)


![Gambar sumber soal 36](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0196-04.png>)


![Gambar sumber soal 36](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0196-05.png>)


![Gambar sumber soal 36](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0196-06.png>)


![Gambar sumber soal 36](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0196-07.png>)


![Gambar sumber soal 36](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0196-08.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Garis sejajar adalah garis yang memiliki jarak tetap dan tidak akan pernah berpotongan. Berdasarkan pengamatan pada kertas berpetak: a (horizontal), b (vertikal), c (diagonal), dan e (diagonal) memiliki kemiringan yang sama dan jarak yang konsisten, sehingga semuanya sejajar.
Gambar sumber: images/kelas3_panduan_siswa_kelas3.pdf-0196-03.png, images/kelas3_panduan_siswa_kelas3.pdf-0196-04.png, images/kelas3_panduan_siswa_kelas3.pdf-0196-05.png, images/kelas3_panduan_siswa_kelas3.pdf-0196-06.png, images/kelas3_panduan_siswa_kelas3.pdf-0196-07.png, images/kelas3_panduan_siswa_kelas3.pdf-0196-08.png. Transkripsi visual: Terdapat 6 gambar (a sampai f) yang menunjukkan pasangan garis pada kertas berpetak. Gambar a: dua garis horizontal sejajar. Gambar b: dua garis vertikal sejajar. Gambar c: dua garis diagonal sejajar (kemiringan sama). Gambar d: dua garis diagonal yang tidak sejajar (jarak menyempit). Gambar e: dua garis diagonal sejajar (kemiringan sama). Gambar f: dua garis membentuk sudut (tidak sejajar).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `adfa8b15ec048f4e9ba9d97ce2e6d09e664718219ae8672fe0857647e0d7821a`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 8099 |
| 2 | success | valid / verified | applying | conceptual | Medium | 8096 |
| 3 | success | valid / verified | applying | conceptual | Medium | 8107 |

Run 1 — solusi: Garis sejajar adalah garis yang memiliki jarak tetap dan tidak akan pernah berpotongan. Berdasarkan pengamatan pada kertas berpetak: a (horizontal), b (vertikal), c (diagonal), dan e (diagonal) memiliki kemiringan yang sama dan jarak yang konsisten, sehingga semuanya sejajar.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi pasangan garis yang sejajar dari beberapa pilihan visual. Ini memerlukan penerapan konsep garis sejajar pada berbagai orientasi (horizontal, vertikal, diagonal), yang merupakan tugas penerapan konsep.. Bukti: Manakah dari pasangan garis berikut yang sejajar?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang definisi dan karakteristik garis sejajar (konsep) dan kemampuan menerapkannya untuk mengklasifikasikan pasangan garis yang diberikan.. Bukti: Garis-Garis Tegak Lurus dan Garis-Garis Sejajar
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk mengenali garis sejajar dalam berbagai orientasi, bukan hanya horizontal atau vertikal. Ini adalah tugas rutin bagi siswa kelas 3 yang sudah mempelajari geometri dasar.. Bukti: Manakah dari pasangan garis berikut yang sejajar?; a, b, c, dan e

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang garis sejajar dan kemampuan visualisasi pada kertas berpetak. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 5 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, mengidentifikasi garis sejajar dalam orientasi diagonal (c dan e) sedikit lebih menantang daripada sekadar horizontal/vertikal, namun masih dalam cakupan kurikulum geometri dasar. |

Run 2 — solusi: Garis sejajar adalah garis yang tidak akan pernah berpotongan meskipun diperpanjang. Pada gambar, pasangan a (horizontal), b (vertikal), c (miring), dan e (miring) memiliki jarak yang konstan dan tidak akan bertemu, sehingga semuanya sejajar.
- Domain kognitif `classify/applying`: Siswa perlu mengenali dan mengidentifikasi properti garis sejajar pada berbagai orientasi (horizontal, vertikal, miring) untuk menentukan pasangan mana yang memenuhi definisi tersebut.. Bukti: Manakah dari pasangan garis berikut yang sejajar?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi garis sejajar dan kemampuan untuk mengkategorikan pasangan garis berdasarkan properti geometris tersebut.. Bukti: Garis-Garis Tegak Lurus dan Garis-Garis Sejajar
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk memeriksa beberapa kasus (a, b, c, d, e, f) dan menerapkan konsep garis sejajar pada orientasi yang berbeda, bukan sekadar garis horizontal/vertikal standar.. Bukti: Manakah dari pasangan garis berikut yang sejajar?; a, b, c, dan e

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang garis dan konsep jarak antar garis. |
| dependentSteps | 5 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, mengidentifikasi garis sejajar pada orientasi miring (c dan e) di samping horizontal/vertikal (a dan b) meningkatkan kompleksitas kognitif dari sekadar pengenalan visual sederhana. |

Run 3 — solusi: Garis sejajar adalah garis yang memiliki jarak tetap dan tidak akan pernah berpotongan. Pasangan a (horizontal), b (vertikal), c (miring), dan e (miring) memenuhi kriteria ini karena memiliki kemiringan yang sama dan jarak yang konstan pada grid.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi pasangan garis yang sejajar berdasarkan representasi visual pada grid. Ini melibatkan pengenalan konsep garis sejajar dalam berbagai orientasi (horizontal, vertikal, miring), yang merupakan penerapan konsep dasar.. Bukti: Manakah dari pasangan garis berikut yang sejajar?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang definisi dan karakteristik garis sejajar (konsep) dan kemampuan menerapkannya pada contoh visual.. Bukti: Garis-Garis Tegak Lurus dan Garis-Garis Sejajar
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak hanya harus mengenali garis sejajar yang mudah (horizontal/vertikal), tetapi juga harus membedakan garis sejajar miring dari garis yang tidak sejajar (seperti d dan f) pada grid, yang memerlukan ketelitian visual.. Bukti: Manakah dari pasangan garis berikut yang sejajar?; a, b, c, dan e

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang garis sejajar dan kemampuan membaca grid. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, mengidentifikasi garis sejajar dalam berbagai orientasi (terutama miring) adalah tantangan yang sesuai untuk tingkat menengah, karena sering kali siswa hanya terbiasa dengan garis horizontal/vertikal. |

Histori retry: run 1 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 2 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 169/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.022176; applying=0.977824; reasoning=0.000000 | applying | 0.977824 | 0.096843 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.005567; conceptual=0.991712; procedural=0.002721; metacognitive=0.000000 | conceptual | 0.991712 | 0.038393 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.581845; Medium=0.412238; Hard=0.005918 | Easy | 0.581845 | 0.646964 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.977824; −Σp ln(p) = 0.106393; H = 0.106393/ln(3) = 0.096843; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.991712; −Σp ln(p) = 0.053224; H = 0.053224/ln(4) = 0.038393; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.581845; −Σp ln(p) = 0.710763; H = 0.710763/ln(3) = 0.646964; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Garis-Garis Tegak Lurus dan Garis-Garis Sejajar
Tipe soal: multiple_choice
Stimulus: -
Soal: Manakah dari pasangan garis berikut yang sejajar?
Pilihan: A. a dan b
B. a, b, c, dan e
C. c, d, dan e
D. a, b, c, d, dan e
Transkripsi visual: Terdapat 6 gambar (a sampai f) yang menunjukkan pasangan garis pada kertas berpetak. Gambar a: dua garis horizontal sejajar. Gambar b: dua garis vertikal sejajar. Gambar c: dua garis diagonal sejajar (kemiringan sama). Gambar d: dua garis diagonal yang tidak sejajar (jarak menyempit). Gambar e: dua garis diagonal sejajar (kemiringan sama). Gambar f: dua garis membentuk sudut (tidak sejajar).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 37. Soal `087423442be49795c5b1bf93`

Toni sedang menyusun mainan balok.<br><br>Ada berapa banyak balok satuan pada mainan yang Toni susun?

| Opsi | Isi |
|---|---|
| A | 7 |
| B | 14 |
| C | 6 |
| D | 8 |

![Gambar sumber soal 37](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0110-06.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Struktur terdiri dari baris depan (3 balok) dan baris belakang (3 balok di bawah + 2 balok di atas). Total = 3 + 3 + 2 = 8 balok.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0110-06.png. Transkripsi visual: Gambar menunjukkan susunan balok satuan (kubus) berwarna hijau. Struktur terdiri dari dua baris. Baris depan (paling dekat dengan pengamat) memiliki 3 balok di lantai dasar. Baris belakang memiliki 3 balok di lantai dasar (terlihat sebagian) dan 2 balok di atasnya. Total balok yang terlihat dan tersirat adalah 3 (depan) + 3 (belakang bawah) + 2 (belakang atas) = 8 balok.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `197f54ccdfd11b40789d2a13b908b47e26463d139452cfab21bf0be5f30e858c`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2566 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 2611 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2616 |

Run 1 — solusi: Susunan terdiri dari 6 balok pada lapisan dasar (2x3) dan 2 balok pada lapisan kedua di tengah, total 8 balok.
- Domain kognitif `classify/applying`: Siswa perlu melakukan visualisasi spasial untuk menghitung balok yang tidak terlihat secara langsung (tersembunyi di belakang), yang melampaui sekadar mengingat fakta.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang volume sebagai jumlah unit kubus yang menyusun suatu bangun ruang.. Bukti: balok satuan
- Intended difficulty `classify/Medium`: Soal ini memerlukan penalaran spasial untuk membayangkan bagian yang tersembunyi, namun prosedurnya tetap rutin bagi siswa kelas 3 yang sudah belajar volume.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang volume sebagai kumpulan kubus satuan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 diharapkan mampu menghitung volume bangun ruang sederhana dengan kubus satuan. Kesulitan terletak pada visualisasi objek 3D. |

Run 2 — solusi: Susunan terdiri dari 4 balok di baris depan, 2 balok di baris belakang bawah, dan 2 balok di atas baris belakang. Total = 4 + 2 + 2 = 8 balok.
- Domain kognitif `classify/reasoning`: Siswa perlu mengintegrasikan informasi visual tentang balok yang terlihat dan menyimpulkan keberadaan balok yang tersembunyi (penalaran spasial) untuk menentukan jumlah total.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang struktur bangun ruang dan bagaimana objek 3D disusun dari unit-unit dasar.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?
- Intended difficulty `classify/Medium`: Soal ini memerlukan penalaran spasial untuk membayangkan bagian yang tidak terlihat, yang merupakan tantangan di atas prosedur rutin bagi siswa kelas 3.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang volume sebagai jumlah unit kubus dan kemampuan visualisasi spasial sederhana. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, menghitung objek 3D yang memiliki bagian tersembunyi memerlukan kemampuan visualisasi yang lebih dari sekadar menghitung objek 2D, sehingga dikategorikan Medium. |

Run 3 — solusi: Susunan terdiri dari dua baris. Baris depan memiliki 3 balok. Baris belakang memiliki 3 balok di bawah dan 2 balok di atasnya. Total = 3 + 3 + 2 = 8 balok.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi struktur 3D dari representasi 2D dan melakukan perhitungan spasial sederhana untuk menentukan jumlah total balok, termasuk yang tidak terlihat langsung.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang volume sebagai jumlah unit kubus yang menyusun suatu bangun ruang.. Bukti: Toni sedang menyusun mainan balok.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa kelas 3 harus melakukan penalaran spasial untuk membayangkan balok yang tersembunyi di balik struktur yang terlihat, bukan sekadar menghitung objek yang tampak.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang volume sebagai jumlah kubus satuan dan kemampuan visualisasi spasial. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, membayangkan objek 3D dari gambar 2D dan menghitung bagian yang tersembunyi merupakan tantangan kognitif yang sesuai untuk tingkat menengah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "reasoning": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3937`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu melakukan penalaran spasial untuk mengidentifikasi dan menghitung balok yang tidak terlihat secara langsung (tersembunyi di bagian belakang bawah), yang melampaui sekadar mengingat fakta.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang volume sebagai jumlah unit kubus yang menyusun suatu bangun ruang.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena siswa kelas 3 harus melakukan penalaran spasial untuk membayangkan balok yang tersembunyi di balik struktur yang terlihat, bukan sekadar menghitung objek yang tampak.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang volume sebagai jumlah kubus satuan dan kemampuan visualisasi spasial. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, membayangkan objek 3D dari gambar 2D dan menghitung bagian yang tersembunyi merupakan tantangan kognitif yang sesuai untuk tingkat menengah. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 139/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000003 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.017958; conceptual=0.977474; procedural=0.004568; metacognitive=0.000000 | conceptual | 0.977474 | 0.085892 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.705422; Medium=0.290608; Hard=0.003970 | Easy | 0.705422 | 0.570939 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000003; H = 0.000003/ln(3) = 0.000003; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.977474; −Σp ln(p) = 0.119071; H = 0.119071/ln(4) = 0.085892; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.705422; −Σp ln(p) = 0.627241; H = 0.627241/ln(3) = 0.570939; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Bangun Ruang
Tipe soal: multiple_choice
Stimulus: -
Soal: Toni sedang menyusun mainan balok.

Ada berapa banyak balok satuan pada mainan yang Toni susun?
Pilihan: A. 7
B. 14
C. 6
D. 8
Transkripsi visual: Gambar menunjukkan susunan balok satuan (kubus) berwarna hijau. Struktur terdiri dari dua baris. Baris depan (paling dekat dengan pengamat) memiliki 3 balok di lantai dasar. Baris belakang memiliki 3 balok di lantai dasar (terlihat sebagian) dan 2 balok di atasnya. Total balok yang terlihat dan tersirat adalah 3 (depan) + 3 (belakang bawah) + 2 (belakang atas) = 8 balok.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 38. Soal `7c1d7c661ba64bbf365e8625`

Hasil penilaian harian Matematika diperoleh: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10<br><br>Berapakah jangkauan data hasil penilaian harian Matematika?

| Opsi | Isi |
|---|---|
| A | 6 |
| B | 5 (10 - 5) |
| C | 15 |
| D | 10 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Data terbesar adalah 10 dan data terkecil adalah 5. Jangkauan = 10 - 5 = 5.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `510a5b9b3bb849bfc17aa6a458303129f802755f586c78458fdae54b2b6ae78f`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1440 |
| 2 | success | valid / verified | applying | procedural | Easy | 1441 |
| 3 | success | valid / verified | applying | procedural | Easy | 1420 |

Run 1 — solusi: Data terbesar adalah 10 dan data terkecil adalah 5. Jangkauan = 10 - 5 = 5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan definisi jangkauan (selisih nilai terbesar dan terkecil) pada sekumpulan data yang diberikan.. Bukti: Berapakah jangkauan data hasil penilaian harian Matematika?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep statistik dasar (jangkauan) dan prosedur untuk menghitungnya.. Bukti: Berapakah jangkauan data hasil penilaian harian Matematika?
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan identifikasi nilai ekstrem (min/max) dari data yang sudah tersedia dan melakukan satu operasi pengurangan sederhana.. Bukti: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10; Berapakah jangkauan data

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengurutkan bilangan dan melakukan operasi pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, mengidentifikasi nilai terbesar dan terkecil dari sekumpulan data adalah tugas rutin yang sesuai dengan tingkat perkembangan kognitif mereka. |

Run 2 — solusi: Data terbesar adalah 10, data terkecil adalah 5. Jangkauan = 10 - 5 = 5.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur rutin untuk menentukan jangkauan (selisih nilai terbesar dan terkecil) dari sekumpulan data yang diberikan.. Bukti: Berapakah jangkauan data hasil penilaian harian Matematika?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang prosedur statistik dasar (jangkauan) yang merupakan teknik standar dalam pengolahan data.. Bukti: Berapakah jangkauan data hasil penilaian harian Matematika?
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan identifikasi nilai ekstrem dan operasi pengurangan dasar, yang merupakan prosedur familiar bagi siswa kelas 3.. Bukti: Hasil penilaian harian Matematika diperoleh: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan bilangan cacah dan melakukan pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari jangkauan adalah konsep dasar pengolahan data yang sesuai untuk kurikulum kelas 3, dengan beban kognitif yang rendah. |

Run 3 — solusi: Data terbesar adalah 10, data terkecil adalah 5. Jangkauan = 10 - 5 = 5.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur rutin untuk menentukan jangkauan (selisih nilai terbesar dan terkecil) dari sekumpulan data yang diberikan.. Bukti: Berapakah jangkauan data hasil penilaian harian Matematika?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau teknik menghitung jangkauan data.. Bukti: Berapakah jangkauan data hasil penilaian harian Matematika?
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan identifikasi nilai ekstrem dan operasi pengurangan dasar, yang merupakan prosedur standar untuk kelas 3.. Bukti: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10; Berapakah jangkauan data

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengurutkan bilangan dan melakukan operasi pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menghitung jangkauan data adalah materi dasar statistik yang sesuai untuk tingkat kelas 3 SD. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2780`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan prosedur rutin untuk menghitung jangkauan (selisih nilai terbesar dan terkecil) dari sekumpulan data yang diberikan.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang prosedur atau algoritma standar untuk menghitung jangkauan data.
- Intended difficulty `Easy`: Soal ini tergolong mudah karena hanya memerlukan identifikasi nilai ekstrem dan operasi pengurangan dasar, yang merupakan prosedur familiar bagi siswa kelas 3.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan bilangan cacah dan melakukan pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari jangkauan adalah konsep dasar pengolahan data yang sesuai untuk kurikulum kelas 3, dengan beban kognitif yang rendah. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 88/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.001123; applying=0.998877; reasoning=0.000000 | applying | 0.998877 | 0.007963 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.382692; conceptual=0.578524; procedural=0.038784; metacognitive=0.000000 | conceptual | 0.578524 | 0.584461 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.916176; Medium=0.081825; Hard=0.001999 | Easy | 0.916176 | 0.270754 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.998877; −Σp ln(p) = 0.008748; H = 0.008748/ln(3) = 0.007963; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.578524; −Σp ln(p) = 0.810235; H = 0.810235/ln(4) = 0.584461; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.916176; −Σp ln(p) = 0.297454; H = 0.297454/ln(3) = 0.270754; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Mengurutkan dan Membandingkan Data
Tipe soal: multiple_choice
Stimulus: -
Soal: Hasil penilaian harian Matematika diperoleh: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10

Berapakah jangkauan data hasil penilaian harian Matematika?
Pilihan: A. 6
B. 5 (10 - 5)
C. 15
D. 10
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 39. Soal `50d5212989ff58e40d99d14c`

Perhatikan gambar berikut!<br><br>Berapa banyak bola dalam gambar tersebut?

| Opsi | Isi |
|---|---|
| A | 5 |
| B | 2 |
| C | 3 |
| D | 4 |

![Gambar sumber soal 39](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0220-01.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Dengan mengamati gambar secara teliti, terdapat tepat 3 objek berbentuk bola basket yang tersebar di antara alat tulis.
Gambar sumber: images/kelas3_panduan_siswa_kelas3.pdf-0220-01.png. Transkripsi visual: Gambar menampilkan berbagai alat tulis (buku, pensil, penghapus, rautan) dan tiga bola basket yang tersebar di antara objek-objek tersebut.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `20f88ba118b5079f9ad3cec9cdc546783c4b0bdf7323a3ab0a8e28beb68d798d`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2447 |
| 2 | success | valid / verified | knowing | factual | Easy | 2443 |
| 3 | success | valid / verified | knowing | factual | Easy | 2453 |

Run 1 — solusi: Dengan mengamati gambar secara teliti, terdapat tepat 3 objek berbentuk bola basket yang tersebar di antara alat tulis.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan proses identifikasi visual dan penghitungan objek yang sangat langsung (counting).. Bukti: Berapa banyak bola dalam gambar tersebut?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengenalan fakta dasar tentang objek (bola) dalam kumpulan benda yang lebih besar.. Bukti: Berapa banyak bola dalam gambar tersebut?
- Intended difficulty `classify/Easy`: Tugas ini sangat sederhana, hanya memerlukan pengamatan visual langsung tanpa manipulasi data atau prosedur kompleks.. Bukti: Berapa banyak bola dalam gambar tersebut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung objek secara akurat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah sangat mahir dalam menghitung objek visual sederhana. Soal ini tidak menuntut kemampuan matematika tingkat lanjut. |

Run 2 — solusi: Dengan mengamati gambar secara teliti, terdapat tiga objek berbentuk bola basket yang tersebar di area gambar.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan proses menghitung objek (bola) secara langsung dari gambar yang diberikan.. Bukti: Berapa banyak bola dalam gambar tersebut?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji kemampuan dasar dalam mengenali dan menghitung objek (fakta) dalam sebuah kumpulan data visual.. Bukti: Berapa banyak bola dalam gambar tersebut?
- Intended difficulty `classify/Easy`: Tugas ini sangat sederhana, hanya melibatkan identifikasi visual objek yang jelas dan penghitungan dasar.. Bukti: Berapa banyak bola dalam gambar tersebut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan dasar menghitung objek (1-10). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 3, tugas menghitung objek dalam gambar adalah tugas yang sangat mendasar dan rutin. |

Run 3 — solusi: Mengidentifikasi dan menghitung objek berbentuk bola basket dalam gambar. Terdapat satu bola di kiri atas, satu bola di kiri bawah, dan satu bola di kanan tengah. Total ada 3 bola.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali objek (bola) dan melakukan penghitungan langsung (counting) tanpa perlu strategi kompleks.. Bukti: Berapa banyak bola dalam gambar tersebut?
- Dimensi pengetahuan `classify/factual`: Tugas ini melibatkan pengenalan objek visual sederhana (fakta) dan penghitungan dasar.. Bukti: Berapa banyak bola dalam gambar tersebut?
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana, hanya memerlukan pengamatan visual langsung dan membilang objek yang jelas perbedaannya dengan objek lain (buku, pensil).. Bukti: Berapa banyak bola dalam gambar tersebut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang objek 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah sangat mahir dalam melakukan penghitungan objek visual sederhana. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 87/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.052254; applying=0.947746; reasoning=0.000000 | applying | 0.947746 | 0.186690 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.365306; conceptual=0.626854; procedural=0.007840; metacognitive=0.000000 | conceptual | 0.626854 | 0.503969 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.907540; Medium=0.089865; Hard=0.002594 | Easy | 0.907540 | 0.291295 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.947746; −Σp ln(p) = 0.205100; H = 0.205100/ln(3) = 0.186690; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.626854; −Σp ln(p) = 0.698649; H = 0.698649/ln(4) = 0.503969; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.907540; −Σp ln(p) = 0.320020; H = 0.320020/ln(3) = 0.291295; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Mengurutkan dan Membandingkan Data
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan gambar berikut!

Berapa banyak bola dalam gambar tersebut?
Pilihan: A. 5
B. 2
C. 3
D. 4
Transkripsi visual: Gambar menampilkan berbagai alat tulis (buku, pensil, penghapus, rautan) dan tiga bola basket yang tersebar di antara objek-objek tersebut.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 40. Soal `631ea2e9a2d5222d502bdf5c`

Hasil penilaian harian Matematika diperoleh: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10<br><br>Berapa banyak siswa yang mendapatkan nilai lebih dari 7?

| Opsi | Isi |
|---|---|
| A | 15 siswa |
| B | 8 siswa |
| C | 10 siswa |
| D | 12 siswa |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Data: 9, 8, 8, 5, 9, 6, 10, 9, 8, 6, 7, 8, 9, 9, 5, 6, 7, 7, 9, 10. Nilai > 7 adalah 8, 9, dan 10. Frekuensi nilai 8 ada 4, nilai 9 ada 6, nilai 10 ada 2. Total = 4 + 6 + 2 = 12.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f133fb514df3bd91db6f887bd495038ac219c3ca6551bfbfe0ca59730beaf69b`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 1499 |
| 2 | success | valid / verified | applying | procedural | Medium | 1537 |
| 3 | success | valid / verified | applying | procedural | Medium | 1532 |

Run 1 — solusi: Data: 9, 8, 8, 5, 9, 6, 10, 9, 8, 6, 7, 8, 9, 9, 5, 6, 7, 7, 9, 10. Nilai > 7 adalah 8, 9, dan 10. Frekuensi nilai 8 ada 4, nilai 9 ada 6, nilai 10 ada 2. Total = 4 + 6 + 2 = 12.
- Domain kognitif `classify/applying`: Siswa perlu mengklasifikasikan data ke dalam kategori (nilai > 7) dan melakukan perhitungan frekuensi sederhana.. Bukti: Berapa banyak siswa yang mendapatkan nilai lebih dari 7?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur pengorganisasian data mentah ke dalam kategori yang ditentukan.. Bukti: Hasil penilaian harian Matematika diperoleh: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10
- Intended difficulty `classify/Medium`: Soal memerlukan ketelitian dalam menyortir data mentah dan menjumlahkan frekuensi. Ini adalah tugas rutin untuk kelas 3.. Bukti: Berapa banyak siswa yang mendapatkan nilai lebih dari 7?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung frekuensi dan membandingkan bilangan (lebih dari 7). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 20 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengolah data mentah menjadi informasi adalah standar kelas 3, namun jumlah data yang cukup banyak (20 item) meningkatkan beban kognitif. |

Run 2 — solusi: Data: 9, 8, 8, 5, 9, 6, 10, 9, 8, 6, 7, 8, 9, 9, 5, 6, 7, 7, 9, 10. Nilai > 7 adalah 8, 9, 10. Frekuensi nilai 8 ada 4, nilai 9 ada 6, nilai 10 ada 2. Total = 4 + 6 + 2 = 12.
- Domain kognitif `classify/applying`: Siswa perlu mengklasifikasikan data mentah ke dalam kategori (nilai > 7) dan menghitung frekuensinya, yang merupakan penerapan prosedur rutin dalam pengolahan data.. Bukti: Berapa banyak siswa yang mendapatkan nilai lebih dari 7?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang bagaimana mengorganisasi dan menghitung data mentah menjadi informasi yang bermakna.. Bukti: Hasil penilaian harian Matematika diperoleh: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10
- Intended difficulty `classify/Medium`: Soal ini melibatkan pengolahan data mentah yang cukup panjang (20 data) untuk siswa kelas 3, menuntut ketelitian dalam mengelompokkan dan menghitung, namun prosedurnya bersifat rutin.. Bukti: Berapa banyak siswa yang mendapatkan nilai lebih dari 7?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung frekuensi data dan membandingkan bilangan (lebih dari 7). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 20 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, mengolah 20 data mentah tanpa tabel frekuensi yang disediakan menuntut ketelitian yang cukup tinggi, sehingga dikategorikan Medium. |

Run 3 — solusi: Data: 9, 8, 8, 5, 9, 6, 10, 9, 8, 6, 7, 8, 9, 9, 5, 6, 7, 7, 9, 10. Nilai > 7 adalah 8, 9, dan 10. Frekuensi nilai 8 ada 4, nilai 9 ada 6, nilai 10 ada 2. Total = 4 + 6 + 2 = 12.
- Domain kognitif `classify/applying`: Siswa perlu mengklasifikasikan data mentah ke dalam kategori (nilai > 7) dan melakukan perhitungan frekuensi sederhana, yang merupakan penerapan prosedur rutin.. Bukti: Berapa banyak siswa yang mendapatkan nilai lebih dari 7?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan teknik pengurutan atau penghitungan frekuensi (prosedur) untuk mengolah data mentah.. Bukti: Hasil penilaian harian Matematika diperoleh: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10
- Intended difficulty `classify/Medium`: Soal ini melibatkan pengolahan data mentah yang cukup panjang (20 data) namun prosedurnya sangat rutin dan familiar bagi kelas 3.. Bukti: Berapa banyak siswa yang mendapatkan nilai lebih dari 7?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung frekuensi dan membandingkan bilangan (lebih dari 7). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 20 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, mengolah 20 data mentah menuntut ketelitian (beban kognitif moderat) meskipun prosedurnya rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 89/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.003469; applying=0.996531; reasoning=0.000000 | applying | 0.996531 | 0.021036 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.325887; conceptual=0.660661; procedural=0.013452; metacognitive=0.000000 | conceptual | 0.660661 | 0.502924 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.902638; Medium=0.095299; Hard=0.002063 | Easy | 0.902638 | 0.299685 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.996531; −Σp ln(p) = 0.023110; H = 0.023110/ln(3) = 0.021036; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.660661; −Σp ln(p) = 0.697200; H = 0.697200/ln(4) = 0.502924; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.902638; −Σp ln(p) = 0.329238; H = 0.329238/ln(3) = 0.299685; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Menyajikan Data dalam Bentuk Tabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Hasil penilaian harian Matematika diperoleh: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10

Berapa banyak siswa yang mendapatkan nilai lebih dari 7?
Pilihan: A. 15 siswa
B. 8 siswa
C. 10 siswa
D. 12 siswa
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 41. Soal `af80792faa77f2a7be932750`

a, b, c, x, y, z, b, c, x, y, a, b, c, a, b, c, x, y, y, b, c, x, y, x, b, c, x, b, c, x, a, y, b, c, x, c, c, b, c,<br><br>Berapa banyak c yang ada pada data tersebut?

| Opsi | Isi |
|---|---|
| A | 11 |
| B | 9 |
| C | 6 |
| D | 8 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `13239fd6bc9d776bdbaa09fd2d92e3c4f76c1a8901ab7570b810bfc764466dbc`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 136/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |

<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Menyajikan Data dalam Bentuk Tabel
Tipe soal: multiple_choice
Stimulus: -
Soal: a, b, c, x, y, z, b, c, x, y, a, b, c, a, b, c, x, y, y, b, c, x, y, x, b, c, x, b, c, x, a, y, b, c, x, c, c, b, c,

Berapa banyak c yang ada pada data tersebut?
Pilihan: A. 11
B. 9
C. 6
D. 8
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 42. Soal `655cea6ab3fa2ff165080502`

Kira sedang mendata kue kesukaan teman-teman sekelasnya. Berikut adalah data yang Kira dapatkan. Diagram Gambar Kue Kesukaan. Setiap gambar mewakili 1 anak. Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.<br><br>Ada 5 anak yang suka onde-onde.<br>Ada 3 anak yang suka lemper.<br>Ada 7 anak yang suka kue talam.<br><br>Ada .... anak yang suka kue cucur.

| Opsi | Isi |
|---|---|
| A | 3 |
| B | 5 |
| C | 7 |
| D | 6 |

![Gambar sumber soal 42](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0254-04.png>)


Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0254-04.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b8b3a89232b02ca8f1efe08e5f362d0544c197c768bf40acf9ebb60449eed6c7`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 126/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified;essential_visual_transcript_missing |

<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Diagram Gambar
Tipe soal: multiple_choice
Stimulus: -
Soal: Kira sedang mendata kue kesukaan teman-teman sekelasnya. Berikut adalah data yang Kira dapatkan. Diagram Gambar Kue Kesukaan. Setiap gambar mewakili 1 anak. Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.

Ada 5 anak yang suka onde-onde.
Ada 3 anak yang suka lemper.
Ada 7 anak yang suka kue talam.

Ada .... anak yang suka kue cucur.
Pilihan: A. 3
B. 5
C. 7
D. 6
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
