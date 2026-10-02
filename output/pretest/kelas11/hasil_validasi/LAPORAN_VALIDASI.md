# Validasi ulang soal kelas 11 — Gemini blind N=3 dan diagnostik IndoBERT

**Batch belum selesai:** 0/66 run awal sukses; 0 item tercatat membutuhkan adjudikasi setelah run lengkap. Distribusi berikut masih sementara; item tanpa keputusan ditampilkan sebagai undecided. Provider berhenti karena kuota harian; checkpoint kerja dapat dilanjutkan saat kuota tersedia.

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v8-blind-sma11-key-verified`. Rubrik: `math-rubric-3x4x3-v6-sma11-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 11 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan bukan keputusan ahli manusia.

Checkpoint dikunci dengan SHA-256 sebelum pemeriksaan scope IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Model SD berada di luar cakupan kelas 11, sehingga seluruh head abstain dan tidak menghasilkan ukuran agreement dengan label blind.

Jumlah soal: 22; distribusi label advisory: `{"mathCognitiveDomain": {"undecided": 22, "knowing": 0, "applying": 0, "reasoning": 0}, "knowledgeDimension": {"undecided": 22, "factual": 0, "conceptual": 0, "procedural": 0, "metacognitive": 0}, "intendedDifficulty": {"undecided": 22, "Easy": 0, "Medium": 0, "Hard": 0}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"knowing": 0, "applying": 0, "reasoning": 0}, "knowledgeDimension": {"factual": 0, "conceptual": 0, "procedural": 0, "metacognitive": 0}, "intendedDifficulty": {"Easy": 0, "Medium": 0, "Hard": 0}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"llm_retry_or_manual_review": 22}`.
Run awal sukses: 0/66; adjudikasi: 0; token sukses tercatat: 0.

Seluruh label masih silver/advisory, gold manusia tetap null, dan publishing otomatis tidak diaktifkan. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

IndoBERT aktif: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Artifact belum disetujui; tidak ada training ulang dalam batch ini. Difficulty model lama dapat mengalami class collapse. Confidence dari kalibrasi kelas 1 yang kecil belum membuktikan ketepatan label.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten tetap memerlukan pemeriksaan ahli.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 0 | 0 | [Easy.json](difficulty/Easy.json) |
| Medium | 0 | 0 | [Medium.json](difficulty/Medium.json) |
| Hard | 0 | 0 | [Hard.json](difficulty/Hard.json) |

## Perhitungan yang dipakai

Untuk kelas 11, encoder dan head IndoBERT tidak dijalankan karena scope model hanya kelas 1–6. Probabilitas kosong, label/confidence/entropy null, dan action abstain berasal dari pemeriksaan scope runtime. Suara Gemini adalah bukti penilaian advisory, bukan probabilitas IndoBERT.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

Model IndoBERT lama hanya mendukung SD kelas 1–6. Untuk kelas 11, diagnostik mengembalikan `out_of_scope` dan `abstain`: label, confidence, dan entropy null serta probabilitas kosong. Label advisory mengikuti Gemini blind dengan rubrik SMA kelas 11. Tidak ada inferensi SD yang dipaksakan sebagai prediksi SMA.

## 1. Soal `6e23a873d17dbf71c29d8901`

Berdasarkan data, pada tahun 2001 perusahaan A mampu menjual 9 laptop. Pada tahun 2002 dan 2003 perusahaan A mampu menjual masing-masing 27 dan 81 laptop. Apabila relasi antara tahun dan jumlah penjualan laptop membentuk fungsi eksponensial, berapa penjualan laptop pada tahun 2007?

| Opsi | Isi |
|---|---|
| A | 6.561 laptop (3^8) |
| B | 2.187 (3^7) |
| C | 486 (9, 27, 81, ... ditambah 81 tiap tahun sampai 2007) |
| D | 19.683 (3^9) |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f283f034c03f64b4396906d4a3d8f6c0672e9ab9185a8e57d9287263a0cc22ff`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Fungsi
Tipe soal: multiple_choice
Stimulus: -
Soal: Berdasarkan data, pada tahun 2001 perusahaan A mampu menjual 9 laptop. Pada tahun 2002 dan 2003 perusahaan A mampu menjual masing-masing 27 dan 81 laptop. Apabila relasi antara tahun dan jumlah penjualan laptop membentuk fungsi eksponensial, berapa penjualan laptop pada tahun 2007?
Pilihan: A. 6.561 laptop (3^8)
B. 2.187 (3^7)
C. 486 (9, 27, 81, ... ditambah 81 tiap tahun sampai 2007)
D. 19.683 (3^9)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `84e4a0b4e7fdc64998b248b3`

Satuan energi adalah Joule dan kalori dengan 1 J = 2,4 kal. Apakah hubungan antara Joule dan kalori merupakan suatu fungsi? Jelaskan.

| Opsi | Isi |
|---|---|
| A | Ya, merupakan fungsi karena setiap nilai Joule berkorespondensi dengan tepat satu nilai kalori |
| B | Tidak, karena rumus 1 J = 2,4 kal hanya berlaku untuk bilangan bulat |
| C | Tidak, karena satu nilai Joule dapat menghasilkan lebih dari satu nilai kalori |
| D | Ya, tetapi hanya berlaku jika satuannya diubah ke kalori terlebih dahulu |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['menganalisis', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9ee8387e2c87579d93608cbf1519f066d116046e246a2bef4db20c96423e08eb`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Fungsi
Tipe soal: multiple_choice
Stimulus: -
Soal: Satuan energi adalah Joule dan kalori dengan 1 J = 2,4 kal. Apakah hubungan antara Joule dan kalori merupakan suatu fungsi? Jelaskan.
Pilihan: A. Ya, merupakan fungsi karena setiap nilai Joule berkorespondensi dengan tepat satu nilai kalori
B. Tidak, karena rumus 1 J = 2,4 kal hanya berlaku untuk bilangan bulat
C. Tidak, karena satu nilai Joule dapat menghasilkan lebih dari satu nilai kalori
D. Ya, tetapi hanya berlaku jika satuannya diubah ke kalori terlebih dahulu
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `f772da841c280f238b1bbb15`

Jika f (3) = 7, g (3) = 6, f (6) = 13, g (6) = 12, tentukan (f o g) (3).

| Opsi | Isi |
|---|---|
| A | 13 |
| B | 7 |
| C | 6 |
| D | 42 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ec13258fe684c3db23172e1177526382e985ac07d6739dcb4841accd01a2af31`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Komposisi Fungsi
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika f (3) = 7, g (3) = 6, f (6) = 13, g (6) = 12, tentukan (f o g) (3).
Pilihan: A. 13
B. 7
C. 6
D. 42
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `f69622cd0a44a030d0eca055`

Jika f (3) = 7, g (3) = 6, f (6) = 13, g (6) = 12, tentukan<br><br>f (3) × g(3)

| Opsi | Isi |
|---|---|
| A | 13 |
| B | 42 |
| C | 1 |
| D | 78 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b1c3baa5ccaefe5b0981d2eb6d85a35d8fc5581a59b804f676f7399bd76c4d83`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Komposisi Fungsi
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika f (3) = 7, g (3) = 6, f (6) = 13, g (6) = 12, tentukan

f (3) × g(3)
Pilihan: A. 13
B. 42
C. 1
D. 78
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `f2de3a4198c1c8c13c51a92a`

Diketahui f (x) = 2x + b dan f (f (x)) = 4x + 6. Tentukan nilai b dan f-1 (x).

| Opsi | Isi |
|---|---|
| A | b = 3, f^-1(x) = (x - 3)/2 |
| B | b = 6, f^-1(x) = (x - 6)/2 |
| C | b = 2, f^-1(x) = (x + 2)/2 |
| D | b = 2, f^-1(x) = (x - 2)/2 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b5ca3120d698a310b9e2ac0abf813a276621684676bdeba0f34e357c80409684`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Fungsi Invers
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui f (x) = 2x + b dan f (f (x)) = 4x + 6. Tentukan nilai b dan f-1 (x).
Pilihan: A. b = 3, f^-1(x) = (x - 3)/2
B. b = 6, f^-1(x) = (x - 6)/2
C. b = 2, f^-1(x) = (x + 2)/2
D. b = 2, f^-1(x) = (x - 2)/2
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `7b396c45f8b99915cc10dc7b`

Tentukan fungsi invers (jika ada) dari f (x) = akar(x - 3), juga domain dan range-nya.

| Opsi | Isi |
|---|---|
| A | f^-1(x) = x^2 - 3, domain: semua bilangan riil >= 0, range: semua bilangan riil >= 3 |
| B | f^-1(x) = x^2 + 3, domain: semua bilangan riil, range: semua bilangan riil |
| C | f^-1(x) = x^2 + 3, domain: semua bilangan riil >= 0, range: semua bilangan riil >= 3 |
| D | f^-1(x) = akar(x) - 3, domain: semua bilangan riil >= 0, range: semua bilangan riil >= 3 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7c9c2b9ce39ede79212db5c8087fa50f9ba5d5f32dacb377d114fa865c679f41`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Fungsi Invers
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan fungsi invers (jika ada) dari f (x) = akar(x - 3), juga domain dan range-nya.
Pilihan: A. f^-1(x) = x^2 - 3, domain: semua bilangan riil >= 0, range: semua bilangan riil >= 3
B. f^-1(x) = x^2 + 3, domain: semua bilangan riil, range: semua bilangan riil
C. f^-1(x) = x^2 + 3, domain: semua bilangan riil >= 0, range: semua bilangan riil >= 3
D. f^-1(x) = akar(x) - 3, domain: semua bilangan riil >= 0, range: semua bilangan riil >= 3
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `d590344d18abe3ebd38fb8ed`

Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.<br><br>\|Waktu (Detik)\|0\|1\|2\|3\|4\|5\|6\|<br>\|---\|---\|---\|---\|---\|---\|---\|---\|<br>\|Jarak (m)\|0\|5\|8\|9\|8\|5\|0\|<br><br>Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah. Jelaskan alasanmu.

| Opsi | Isi |
|---|---|
| A | Terbuka ke bawah, karena nilai fungsi (jarak) naik kemudian turun lagi. |
| B | Terbuka ke atas, karena nilai fungsi naik kemudian turun lagi. |
| C | Terbuka ke bawah, karena nilai fungsi turun kemudian naik lagi. |
| D | Tidak dapat ditentukan tanpa menggambar grafiknya. |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2663e4aa5086572662f61adfb1398f67c0703dda06b341e6b27e49352bee58ff`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Fungsi Kuadrat
Tipe soal: multiple_choice
Stimulus: -
Soal: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.

|Waktu (Detik)|0|1|2|3|4|5|6|
|---|---|---|---|---|---|---|---|
|Jarak (m)|0|5|8|9|8|5|0|

Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah. Jelaskan alasanmu.
Pilihan: A. Terbuka ke bawah, karena nilai fungsi (jarak) naik kemudian turun lagi.
B. Terbuka ke atas, karena nilai fungsi naik kemudian turun lagi.
C. Terbuka ke bawah, karena nilai fungsi turun kemudian naik lagi.
D. Tidak dapat ditentukan tanpa menggambar grafiknya.
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `72d9df20cc708f4143b713d0`

Apabila diketahui banyak anggota dua himpunan seperti berikut ini, maka ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? a. n(A) = n(B) = 12<br><br>Ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12?

| Opsi | Isi |
|---|---|
| A | 12 x 12 = 144 |
| B | 12 + 11 + 10 + ... + 2 + 1 = 78 |
| C | 12 |
| D | 12! = 479.001.600 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `22753e6a5a815739037aae5bb0f8f9eb7e401c418fab617d36428846fe0ab1a0`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Korespondensi Satu-satu (Pengayaan)
Tipe soal: multiple_choice
Stimulus: -
Soal: Apabila diketahui banyak anggota dua himpunan seperti berikut ini, maka ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? a. n(A) = n(B) = 12

Ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12?
Pilihan: A. 12 x 12 = 144
B. 12 + 11 + 10 + ... + 2 + 1 = 78
C. 12
D. 12! = 479.001.600
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 9. Soal `280f78ecf94b2c1b0d7d8f4a`

AB adalah diameter pada lingkaran berikut. Jari-jari lingkaran 8,5 cm dan panjang AC = 8 cm. Tentukan:<br><br>panjang BC

| Opsi | Isi |
|---|---|
| A | 9 cm |
| B | 18,8 cm |
| C | 17 cm |
| D | 15 cm |

![Gambar sumber soal 9](<../images/kelas11_panduan_siswa_kelas11.pdf-0074-05.png>)


Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas11_panduan_siswa_kelas11.pdf-0074-05.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c84e593e9bc5d6c0c789eff46fbfbf8721ff8c905abbd4f1c1e856b53de4303a`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Lingkaran dan Busur Lingkaran
Tipe soal: multiple_choice
Stimulus: -
Soal: AB adalah diameter pada lingkaran berikut. Jari-jari lingkaran 8,5 cm dan panjang AC = 8 cm. Tentukan:

panjang BC
Pilihan: A. 9 cm
B. 18,8 cm
C. 17 cm
D. 15 cm
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `f6239979bb0b323db2b28a03`

Jika `∠` BOC = 90`◦` , berapakah besar `∠` BEC ?

| Opsi | Isi |
|---|---|
| A | 22,5° |
| B | 45° |
| C | 90° |
| D | 180° |

![Gambar sumber soal 10](<../images/kelas11_panduan_siswa_kelas11.pdf-0074-01.png>)


Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas11_panduan_siswa_kelas11.pdf-0074-01.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7b93f1cbfe5d3a011e2cb6cfebbdc51320729fed0ee810fbc575f03560b66038`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Lingkaran dan Busur Lingkaran
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika `∠` BOC = 90`◦` , berapakah besar `∠` BEC ?
Pilihan: A. 22,5°
B. 45°
C. 90°
D. 180°
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `838b526b72b79e514bd4fe62`

Pada gambar berikut, BD dan CD adalah garis singgung lingkaran A. Jika `∠` BAC = 147`◦` , tentukan besar `∠` BDC.

| Opsi | Isi |
|---|---|
| A | 33° |
| B | 57° |
| C | 147° |
| D | 90° |

![Gambar sumber soal 11](<../images/kelas11_panduan_siswa_kelas11.pdf-0081-05.png>)


Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas11_panduan_siswa_kelas11.pdf-0081-05.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f7efbda2f82b8a096023f0e8587e876669de06bed242804d37b0612c9a87d8e3`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Lingkaran dan Garis Singgung
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada gambar berikut, BD dan CD adalah garis singgung lingkaran A. Jika `∠` BAC = 147`◦` , tentukan besar `∠` BDC.
Pilihan: A. 33°
B. 57°
C. 147°
D. 90°
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 12. Soal `a0be320297e2f3ecca60fa01`

Jika jari-jari lingkaran A adalah 7 cm dan titik P berjarak 25 cm dari titik A, berapakah panjang garis singgung PB ?

| Opsi | Isi |
|---|---|
| A | 18 cm |
| B | 25 cm |
| C | 24 cm |
| D | 26 cm |

![Gambar sumber soal 12](<../images/kelas11_panduan_siswa_kelas11.pdf-0081-03.png>)


Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas11_panduan_siswa_kelas11.pdf-0081-03.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4a79debde6a1c9aa0ea83c449a85099553fe2c279e81b5e56c7f8d8ae3f87d3f`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Lingkaran dan Garis Singgung
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika jari-jari lingkaran A adalah 7 cm dan titik P berjarak 25 cm dari titik A, berapakah panjang garis singgung PB ?
Pilihan: A. 18 cm
B. 25 cm
C. 24 cm
D. 26 cm
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 13. Soal `9d3b005f20ecd5dabca2aa9e`

Jika AD = 3 cm dan BE = AD, tentukan:<br><br>besar `∠` BAE

| Opsi | Isi |
|---|---|
| A | 90° |
| B | 60° |
| C | 45° |
| D | 120° |

![Gambar sumber soal 13](<../images/kelas11_panduan_siswa_kelas11.pdf-0089-05.png>)


Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas11_panduan_siswa_kelas11.pdf-0089-05.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `03f691a4939d470ee4e71c1c640bb8c6b786d3fc66fc4d391f6b14e8053f3cf4`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Lingkaran dan Tali Busur
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika AD = 3 cm dan BE = AD, tentukan:

besar `∠` BAE
Pilihan: A. 90°
B. 60°
C. 45°
D. 120°
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `b9acc681a7567cd1039ff751`

Lingkaran yang berpusat di titik O dan jari-jarinya 5 cm. Berapa panjang tali busurnya yang paling panjang?

| Opsi | Isi |
|---|---|
| A | 10 cm |
| B | 15 cm |
| C | 20 cm |
| D | 5 cm |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d3b47862859c4e97c7de18acdeb87a7508a5fc3fd25c64287ade29556b5cfb4a`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Lingkaran dan Tali Busur
Tipe soal: multiple_choice
Stimulus: -
Soal: Lingkaran yang berpusat di titik O dan jari-jarinya 5 cm. Berapa panjang tali busurnya yang paling panjang?
Pilihan: A. 10 cm
B. 15 cm
C. 20 cm
D. 5 cm
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 15. Soal `1ef6efc5863938a14b737897`

Berapa liter gas bumi yang dapat ditampung dengan truk yang memiliki tabung penyimpanan besar seperti Gambar 2.77 dengan diameter 2 meter dan panjang 12 meter?

| Opsi | Isi |
|---|---|
| A | 37,68 liter |
| B | 150.720 liter |
| C | 37.680 liter |
| D | 36.000 liter |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2dc682d6fdacc200fbd012d28bf61005a3728910231d2cac3d7fcac4b33af10f`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Volume Bangun Ruang Sisi Lengkung
Tipe soal: multiple_choice
Stimulus: -
Soal: Berapa liter gas bumi yang dapat ditampung dengan truk yang memiliki tabung penyimpanan besar seperti Gambar 2.77 dengan diameter 2 meter dan panjang 12 meter?
Pilihan: A. 37,68 liter
B. 150.720 liter
C. 37.680 liter
D. 36.000 liter
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `9bee88ce31163c95d6276272`

Perhatikan pasangan-pasangan variabel di bawah ini. Tentukan bagaimana hubungan mereka dan berikan alasan kalian.<br><br>Bagaimana hubungan antara banyak kendaraan bermotor dan tingkat polusi udara? Berikan alasan kalian.

| Opsi | Isi |
|---|---|
| A | Semakin banyak kendaraan bermotor, semakin menurun tingkat polusi udara (korelasi negatif) |
| B | Semakin banyak kendaraan bermotor, semakin meningkat tingkat polusi udara (korelasi positif) |
| C | Tidak ada hubungan antara banyak kendaraan bermotor dan tingkat polusi udara |
| D | Hubungan keduanya tidak dapat ditentukan tanpa data numerik |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi', 'menganalisis', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `954ac77164f15396df49be9638c12294c98d0111a9828ea1736928753c7ae520`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Diagram Pencar atau Diagram Scatter
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan pasangan-pasangan variabel di bawah ini. Tentukan bagaimana hubungan mereka dan berikan alasan kalian.

Bagaimana hubungan antara banyak kendaraan bermotor dan tingkat polusi udara? Berikan alasan kalian.
Pilihan: A. Semakin banyak kendaraan bermotor, semakin menurun tingkat polusi udara (korelasi negatif)
B. Semakin banyak kendaraan bermotor, semakin meningkat tingkat polusi udara (korelasi positif)
C. Tidak ada hubungan antara banyak kendaraan bermotor dan tingkat polusi udara
D. Hubungan keduanya tidak dapat ditentukan tanpa data numerik
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 17. Soal `954fcaa8282f462df30d7e71`

Perhatikan pasangan-pasangan variabel di bawah ini. Tentukan bagaimana hubungan mereka dan berikan alasan kalian.<br><br>Bagaimana hubungan antara jarak yang ditempuh oleh sebuah motor dan volume bensin dalam tangki bensin? Berikan alasan kalian.

| Opsi | Isi |
|---|---|
| A | Tidak ada hubungan antara jarak tempuh dan volume bensin |
| B | Hubungan keduanya tidak dapat ditentukan tanpa data numerik |
| C | Semakin jauh jarak yang ditempuh oleh sebuah motor, semakin berkurang volume bensin dalam tangki bensin (korelasi negatif) |
| D | Semakin jauh jarak yang ditempuh oleh sebuah motor, semakin bertambah volume bensin dalam tangki bensin (korelasi positif) |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['mengidentifikasi', 'menganalisis', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b28c10c4471499fb6531aa0aecf7b88f9fcf96dc562984ec03c4241e57d4110e`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Diagram Pencar atau Diagram Scatter
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan pasangan-pasangan variabel di bawah ini. Tentukan bagaimana hubungan mereka dan berikan alasan kalian.

Bagaimana hubungan antara jarak yang ditempuh oleh sebuah motor dan volume bensin dalam tangki bensin? Berikan alasan kalian.
Pilihan: A. Tidak ada hubungan antara jarak tempuh dan volume bensin
B. Hubungan keduanya tidak dapat ditentukan tanpa data numerik
C. Semakin jauh jarak yang ditempuh oleh sebuah motor, semakin berkurang volume bensin dalam tangki bensin (korelasi negatif)
D. Semakin jauh jarak yang ditempuh oleh sebuah motor, semakin bertambah volume bensin dalam tangki bensin (korelasi positif)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `cc594209724affd13041e475`

Pada saat kondisi mendadak, para pengendara mobil memerlukan waktu yang berbeda-beda untuk dapat bereaksi untuk menginjak rem mobil. Jarak yang diperlukan hingga terjadi reaksi menginjak rem disebut sebagai jarak reaksi. Tabel berikut ini memberikan informasi mengenai jarak reaksi dari mobil yang melaju dengan kecepatan yang berbeda-beda. Kecepatan (km/jam): 20, 30, 40, 50, 60, 70. Jarak Reaksi (m): 4,1; 6,2; 8,3; 10,1; 12,4; 14,5.<br><br>Hitunglah prediksi jarak reaksi jika suatu mobil bergerak dengan kecepatan 35 km/jam.

| Opsi | Isi |
|---|---|
| A | 8,3 m |
| B | 7,2 m |
| C | 12,4 m |
| D | 11,34 m |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `96ed89b0b065cdb47de720ddbe3627eb7bff3643900dfe1d30ae31347f734366`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Regresi Linear
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada saat kondisi mendadak, para pengendara mobil memerlukan waktu yang berbeda-beda untuk dapat bereaksi untuk menginjak rem mobil. Jarak yang diperlukan hingga terjadi reaksi menginjak rem disebut sebagai jarak reaksi. Tabel berikut ini memberikan informasi mengenai jarak reaksi dari mobil yang melaju dengan kecepatan yang berbeda-beda. Kecepatan (km/jam): 20, 30, 40, 50, 60, 70. Jarak Reaksi (m): 4,1; 6,2; 8,3; 10,1; 12,4; 14,5.

Hitunglah prediksi jarak reaksi jika suatu mobil bergerak dengan kecepatan 35 km/jam.
Pilihan: A. 8,3 m
B. 7,2 m
C. 12,4 m
D. 11,34 m
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 19. Soal `cb666d7ac7a8bdfb36335e5a`

Tabel berikut menunjukkan banyak tempat duduk terhadap biaya per jam dari tiga model pesawat terbang yang digunakan oleh maskapai Garuda Indonesia.<br><br>\|Model Pesawat\|Banyak tempat duduk\|Biaya (rupiah/jam)\|<br>\|---\|---\|---\|<br>\|A\|50\|1.100.000,00\|<br>\|B\|100\|2.100.000,00\|<br>\|C\|150\|2.700.000,00\|<br><br>Persamaan garis regresi mana yang lebih tepat untuk memprediksi banyak tempat duduk terhadap biaya, yˆ = 367000 + 16000x atau yˆ = 300000 + 16000x?

| Opsi | Isi |
|---|---|
| A | yˆ = 300000 + 16000x |
| B | yˆ = 367000 + 16000x |
| C | Tidak dapat ditentukan tanpa menggambar diagram pencarnya |
| D | Keduanya sama tepat karena mempunyai gradien (b) yang sama |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3ef115343361bd354f1a50594374a7c14169c15bc3b675506f1ef27bec8e7de7`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Regresi Linear
Tipe soal: multiple_choice
Stimulus: -
Soal: Tabel berikut menunjukkan banyak tempat duduk terhadap biaya per jam dari tiga model pesawat terbang yang digunakan oleh maskapai Garuda Indonesia.

|Model Pesawat|Banyak tempat duduk|Biaya (rupiah/jam)|
|---|---|---|
|A|50|1.100.000,00|
|B|100|2.100.000,00|
|C|150|2.700.000,00|

Persamaan garis regresi mana yang lebih tepat untuk memprediksi banyak tempat duduk terhadap biaya, yˆ = 367000 + 16000x atau yˆ = 300000 + 16000x?
Pilihan: A. yˆ = 300000 + 16000x
B. yˆ = 367000 + 16000x
C. Tidak dapat ditentukan tanpa menggambar diagram pencarnya
D. Keduanya sama tepat karena mempunyai gradien (b) yang sama
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `5a713d72bd575400bbc8e916`

Diagram pencar berikut menunjukkan tingkat IQ seseorang terhadap lingkar kepalanya dalam cm dari sampel 20 orang. Rata-rata IQ adalah 101 dan rata-rata lingkar kepala adalah 56,125 cm. Nilai koefisien korelasinya adalah 0,138.<br><br>Berapa persentase IQ yang diterangkan oleh lingkar kepala?

| Opsi | Isi |
|---|---|
| A | 13,8% |
| B | 0,19% |
| C | 98,1% |
| D | 1,9% |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2e7c3b076694ab6bc78722dfed8b99b0a533d378af69e6ee2587109140e26a81`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Analisis Korelasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Diagram pencar berikut menunjukkan tingkat IQ seseorang terhadap lingkar kepalanya dalam cm dari sampel 20 orang. Rata-rata IQ adalah 101 dan rata-rata lingkar kepala adalah 56,125 cm. Nilai koefisien korelasinya adalah 0,138.

Berapa persentase IQ yang diterangkan oleh lingkar kepala?
Pilihan: A. 13,8%
B. 0,19%
C. 98,1%
D. 1,9%
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 21. Soal `2071d19215ee9fcf4926b805`

Diagram pencar berikut menunjukkan tingkat IQ seseorang terhadap lingkar kepalanya dalam cm dari sampel 20 orang. Rata-rata IQ adalah 101 dan rata-rata lingkar kepala adalah 56,125 cm. Nilai koefisien korelasinya adalah 0,138.<br><br>Berapa persentase IQ yang diterangkan oleh variabel-variabel lainnya?

| Opsi | Isi |
|---|---|
| A | 0,981% |
| B | 99,1% |
| C | 98,1% |
| D | 1,9% |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6881c85f0c9e63f82266d0f5366880c202ac7cc19cb73d35d4f59f42a106b831`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Analisis Korelasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Diagram pencar berikut menunjukkan tingkat IQ seseorang terhadap lingkar kepalanya dalam cm dari sampel 20 orang. Rata-rata IQ adalah 101 dan rata-rata lingkar kepala adalah 56,125 cm. Nilai koefisien korelasinya adalah 0,138.

Berapa persentase IQ yang diterangkan oleh variabel-variabel lainnya?
Pilihan: A. 0,981%
B. 99,1%
C. 98,1%
D. 1,9%
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 22. Soal `d6d3b4c5f9819d69d4c859d0`

Dalam upaya untuk mempromosikan penggunaan energi yang efisien, sebuah kota melakukan survei terhadap konsumsi listrik bulanan (dalam kWh) dari 10 rumah tangga diperoleh data sebagai berikut. 300, 320, 310, 305, 315, 320, 750, 310, 325, 315<br><br>Mengapa angka 750 kWh dapat dianggap sebagai pencilan?

| Opsi | Isi |
|---|---|
| A | Karena 750 kWh lebih dari 1,5 kali median data (315 kWh) |
| B | Karena 750 kWh adalah satu-satunya data yang jumlah angkanya lebih dari tiga digit |
| C | Karena 750 kWh lebih besar dari nilai data lainnya yang tertinggi (325 kWh) |
| D | Karena 750 kWh lebih besar dari batas atas IQR (335 kWh), sehingga berada di luar rentang wajar data |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `31c1b2c091a427804603e51b0a82d319bd38f9ea744aec3ede748b23d5c1814d`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Topik: Matematika SMA Kelas 11
Subtopik: Representasi Data Lanjutan
Tipe soal: multiple_choice
Stimulus: -
Soal: Dalam upaya untuk mempromosikan penggunaan energi yang efisien, sebuah kota melakukan survei terhadap konsumsi listrik bulanan (dalam kWh) dari 10 rumah tangga diperoleh data sebagai berikut. 300, 320, 310, 305, 315, 320, 750, 310, 325, 315

Mengapa angka 750 kWh dapat dianggap sebagai pencilan?
Pilihan: A. Karena 750 kWh lebih dari 1,5 kali median data (315 kWh)
B. Karena 750 kWh adalah satu-satunya data yang jumlah angkanya lebih dari tiga digit
C. Karena 750 kWh lebih besar dari nilai data lainnya yang tertinggi (325 kWh)
D. Karena 750 kWh lebih besar dari batas atas IQR (335 kWh), sehingga berada di luar rentang wajar data
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
