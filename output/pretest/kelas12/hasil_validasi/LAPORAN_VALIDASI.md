# Validasi ulang soal kelas 12 — Gemini blind N=3 dan diagnostik IndoBERT

**Batch belum selesai:** 0/96 run awal sukses; 0 item tercatat membutuhkan adjudikasi setelah run lengkap. Distribusi berikut masih sementara; item tanpa keputusan ditampilkan sebagai undecided. Provider berhenti karena kuota harian; checkpoint kerja dapat dilanjutkan saat kuota tersedia.

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v8-blind-sma12-key-verified`. Rubrik: `math-rubric-3x4x3-v6-sma12-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 12 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan bukan keputusan ahli manusia.

Checkpoint dikunci dengan SHA-256 sebelum pemeriksaan scope IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Model SD berada di luar cakupan kelas 12, sehingga seluruh head abstain dan tidak menghasilkan ukuran agreement dengan label blind.

Jumlah soal: 32; distribusi label advisory: `{"mathCognitiveDomain": {"undecided": 32, "knowing": 0, "applying": 0, "reasoning": 0}, "knowledgeDimension": {"undecided": 32, "factual": 0, "conceptual": 0, "procedural": 0, "metacognitive": 0}, "intendedDifficulty": {"undecided": 32, "Easy": 0, "Medium": 0, "Hard": 0}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"knowing": 0, "applying": 0, "reasoning": 0}, "knowledgeDimension": {"factual": 0, "conceptual": 0, "procedural": 0, "metacognitive": 0}, "intendedDifficulty": {"Easy": 0, "Medium": 0, "Hard": 0}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"llm_retry_or_manual_review": 32}`.
Run awal sukses: 0/96; adjudikasi: 0; token sukses tercatat: 0.

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

Untuk kelas 12, encoder dan head IndoBERT tidak dijalankan karena scope model hanya kelas 1–6. Probabilitas kosong, label/confidence/entropy null, dan action abstain berasal dari pemeriksaan scope runtime. Suara Gemini adalah bukti penilaian advisory, bukan probabilitas IndoBERT.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

Model IndoBERT lama hanya mendukung SD kelas 1–6. Untuk kelas 12, diagnostik mengembalikan `out_of_scope` dan `abstain`: label, confidence, dan entropy null serta probabilitas kosong. Label advisory mengikuti Gemini blind dengan rubrik SMA kelas 12. Tidak ada inferensi SD yang dipaksakan sebagai prediksi SMA.

## 1. Soal `ddce171a6063467f30bcf924`

Tentukan dua suku berikutnya dari barisan bilangan berikut ini: 1, 1, 2, 6, …, …

| Opsi | Isi |
|---|---|
| A | 24, 120 |
| B | 1, 3 |
| C | $\frac{1}{4}$, $\frac{1}{16}$ |
| D | 4, 4 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d51b8feef95a16b60e767947dfe27aa252d340f06ed52ad8602ee6cfa1e42adb`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Barisan
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan dua suku berikutnya dari barisan bilangan berikut ini: 1, 1, 2, 6, …, …
Pilihan: A. 24, 120
B. 1, 3
C. $\frac{1}{4}$, $\frac{1}{16}$
D. 4, 4
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `577daf905630d2b50cdcacfa`

Tentukan dua suku berikutnya dari barisan bilangan berikut ini: 4, 4, 4, 4, …, …

| Opsi | Isi |
|---|---|
| A | 24, 120 |
| B | $\frac{1}{4}$, $\frac{1}{16}$ |
| C | 4, 4 |
| D | 1, 3 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `06a7556edc1c8b767ad9cee5a5e779539ed27e3786b51dd3c3f38ae1027f7d0c`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Barisan
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan dua suku berikutnya dari barisan bilangan berikut ini: 4, 4, 4, 4, …, …
Pilihan: A. 24, 120
B. $\frac{1}{4}$, $\frac{1}{16}$
C. 4, 4
D. 1, 3
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `cde1c3bcaf6c566fa0d0dfde`

Jika Un menyatakan suku ke-n suatu barisan aritmetika dan diketahui U 6 - U 8 + U 10 - U 12 + U 14 = 20, berapa jumlah 19 suku pertama barisan tersebut?

| Opsi | Isi |
|---|---|
| A | 380 |
| B | 20 |
| C | 360 |
| D | 190 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `01955ec269139de2b13770aada8145d2ac3a4c43c9d46a1b34002d1f53f47a19`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Deret
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika Un menyatakan suku ke-n suatu barisan aritmetika dan diketahui U 6 - U 8 + U 10 - U 12 + U 14 = 20, berapa jumlah 19 suku pertama barisan tersebut?
Pilihan: A. 380
B. 20
C. 360
D. 190
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `6e5ddb2020e2a12b1ecf2b03`

Suatu deret geometri memiliki suku pertama a = 5 dan rasio r = 2. Hitunglah jumlah 6 suku pertama deret tersebut.

| Opsi | Isi |
|---|---|
| A | 635 |
| B | 315 |
| C | 310 |
| D | 320 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2d3c4ddfa58405319a3af3c7a915df547be3cc74f951f5d437f6faaf58d338b1`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Deret
Tipe soal: multiple_choice
Stimulus: -
Soal: Suatu deret geometri memiliki suku pertama a = 5 dan rasio r = 2. Hitunglah jumlah 6 suku pertama deret tersebut.
Pilihan: A. 635
B. 315
C. 310
D. 320
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `50f81b2d500c6fab49401822`

Raka mengikuti program Youth Creative Entrepreneur di sekolahnya. Untuk membeli peralatan produksi awal, ia memperoleh dana talangan usaha sebesar Rp2.500.000,00 dari koperasi pemuda. Koperasi tersebut menerapkan bunga sederhana sebesar 4% per tahun dan memberikan keringanan berupa angsuran bulanan tetap selama 2 tahun agar para peserta tidak terbebani. Sebagai bentuk tanggung jawab finansial, Raka perlu menghitung besar cicilan bulanan yang harus ia bayarkan agar pinjaman tersebut lunas sesuai perjanjian. Berapakah cicilan yang harus dibayarkan Raka setiap bulan?

| Opsi | Isi |
|---|---|
| A | Rp104.166,67 |
| B | Rp112.500,00 |
| C | Rp108.333,33 |
| D | Rp225.000,00 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6cc983bc2b559e75882a50753ac7feed3dc807a10cd40c40ac1e4b0082205962`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Bunga Tunggal
Tipe soal: multiple_choice
Stimulus: -
Soal: Raka mengikuti program Youth Creative Entrepreneur di sekolahnya. Untuk membeli peralatan produksi awal, ia memperoleh dana talangan usaha sebesar Rp2.500.000,00 dari koperasi pemuda. Koperasi tersebut menerapkan bunga sederhana sebesar 4% per tahun dan memberikan keringanan berupa angsuran bulanan tetap selama 2 tahun agar para peserta tidak terbebani. Sebagai bentuk tanggung jawab finansial, Raka perlu menghitung besar cicilan bulanan yang harus ia bayarkan agar pinjaman tersebut lunas sesuai perjanjian. Berapakah cicilan yang harus dibayarkan Raka setiap bulan?
Pilihan: A. Rp104.166,67
B. Rp112.500,00
C. Rp108.333,33
D. Rp225.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `ada21d81536b4020ff184696`

Angga adalah seorang siswa SMA yang rajin dan memiliki semangat menabung. Setelah menerima hadiah ulang tahun berupa uang tunai sebesar Rp1.000.000,00 dari orang tuanya, ia memutuskan untuk tidak menghabiskannya begitu saja. Ia pergi ke bank dan membuka rekening tabungan khusus pelajar. Petugas bank menjelaskan bahwa tabungannya akan mendapatkan bunga tetap sebesar 5% setiap tahun dari saldo awal. Bunga tersebut akan langsung ditambahkan ke saldo tabungannya setiap akhir tahun. Tabel 1.5 Perhitungan Nilai Tabungan Angga: Tahun 1, Bunga 5% × 1.000.000 = 50.000, Nilai Uang 1.000.000 + 50.000 = 1.050.000. Tahun 2, Bunga 5% × 1.000.000 = ...., Nilai Uang 1.050.000 + 50.000 = ...<br><br>Berapa nilai total tabungan Angga pada akhir tahun kedua?

| Opsi | Isi |
|---|---|
| A | Rp1.150.000,00 |
| B | Rp1.050.000,00 |
| C | Rp1.100.000,00 |
| D | Rp1.102.500,00 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d8da7760bfffbb9c5f3e456bf6b86199ac630c4723ba264a9c6238ab7f0abda9`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Bunga Tunggal
Tipe soal: multiple_choice
Stimulus: -
Soal: Angga adalah seorang siswa SMA yang rajin dan memiliki semangat menabung. Setelah menerima hadiah ulang tahun berupa uang tunai sebesar Rp1.000.000,00 dari orang tuanya, ia memutuskan untuk tidak menghabiskannya begitu saja. Ia pergi ke bank dan membuka rekening tabungan khusus pelajar. Petugas bank menjelaskan bahwa tabungannya akan mendapatkan bunga tetap sebesar 5% setiap tahun dari saldo awal. Bunga tersebut akan langsung ditambahkan ke saldo tabungannya setiap akhir tahun. Tabel 1.5 Perhitungan Nilai Tabungan Angga: Tahun 1, Bunga 5% × 1.000.000 = 50.000, Nilai Uang 1.000.000 + 50.000 = 1.050.000. Tahun 2, Bunga 5% × 1.000.000 = ...., Nilai Uang 1.050.000 + 50.000 = ...

Berapa nilai total tabungan Angga pada akhir tahun kedua?
Pilihan: A. Rp1.150.000,00
B. Rp1.050.000,00
C. Rp1.100.000,00
D. Rp1.102.500,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `d215f8aa8bc3bed140f75b0b`

Firman menyimpan uang sejumlah Rp10.000.000,00 di bank dalam bentuk deposito dengan bunga 3% per tahun. Setiap tahun bank mengirim bunga ke rekening tabungan Firman. Gigih juga memiliki deposito sejumlah Rp10.000.000,00 di bank dengan bunga 3% per tahun. Setiap tahun, saat perpanjangan deposito, Gigih meminta bank untuk menambahkan bunganya ke dalam nilai depositonya.<br><br>d. Setelah lima tahun, lebih banyak uang Firman atau Gigih? Berapa selisihnya?

| Opsi | Isi |
|---|---|
| A | Uang Gigih lebih banyak, selisihnya Rp9.000,00 |
| B | Uang Gigih lebih banyak, selisihnya Rp92.741,00 |
| C | Uang Firman lebih banyak, selisihnya Rp92.741,00 |
| D | Sama banyak, selisihnya Rp0,00 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung', 'membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4f2e3cd095db034255fd6b8e0ee5f3caff49c1022c52773450b905a92c76edbe`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Bunga
Tipe soal: multiple_choice
Stimulus: -
Soal: Firman menyimpan uang sejumlah Rp10.000.000,00 di bank dalam bentuk deposito dengan bunga 3% per tahun. Setiap tahun bank mengirim bunga ke rekening tabungan Firman. Gigih juga memiliki deposito sejumlah Rp10.000.000,00 di bank dengan bunga 3% per tahun. Setiap tahun, saat perpanjangan deposito, Gigih meminta bank untuk menambahkan bunganya ke dalam nilai depositonya.

d. Setelah lima tahun, lebih banyak uang Firman atau Gigih? Berapa selisihnya?
Pilihan: A. Uang Gigih lebih banyak, selisihnya Rp9.000,00
B. Uang Gigih lebih banyak, selisihnya Rp92.741,00
C. Uang Firman lebih banyak, selisihnya Rp92.741,00
D. Sama banyak, selisihnya Rp0,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `b599e139114197a77a84c95d`

Pak Roni merupakan anggota koperasi simpan pinjam. Pak Roni menyimpan sejumlah uang di koperasi sebesar Rp15.000.000,00 dengan bunga koperasi 1% per tahun.<br><br>Berapa jumlah simpanan Pak Roni setelah 5 tahun?

| Opsi | Isi |
|---|---|
| A | Rp15.750.000,00 |
| B | Rp15.075.000,00 |
| C | Rp16.500.000,00 |
| D | Rp750.000,00 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8e3fe428dba512808e90191936ab7c42164c919bbecf8dd33469575df35b9135`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Suku Bunga Tunggal
Tipe soal: multiple_choice
Stimulus: -
Soal: Pak Roni merupakan anggota koperasi simpan pinjam. Pak Roni menyimpan sejumlah uang di koperasi sebesar Rp15.000.000,00 dengan bunga koperasi 1% per tahun.

Berapa jumlah simpanan Pak Roni setelah 5 tahun?
Pilihan: A. Rp15.750.000,00
B. Rp15.075.000,00
C. Rp16.500.000,00
D. Rp750.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 9. Soal `5a320ce9d400ac199d8082a9`

Pak Bayu merupakan anggota koperasi "Maju Bersama". Beliau menyimpan modal awal sebesar Rp1.000.000,00 di koperasi tersebut. Koperasi memberikan bunga tunggal sebesar 18% per tahun untuk simpanan anggota. Pak Bayu menyimpan modalnya selama 8 bulan.<br><br>Hitunglah berapa besar bunga yang akan diterima dan berapa total simpanan Pak Bayu setelah 8 bulan?

| Opsi | Isi |
|---|---|
| A | Bunga Rp1.440.000,00, total simpanan Rp2.440.000,00 |
| B | Bunga Rp120.000,00, total simpanan Rp1.120.000,00 |
| C | Bunga Rp126.492,00, total simpanan Rp1.126.492,00 |
| D | Bunga Rp120.000,00, total simpanan Rp120.000,00 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `059f1c1a79f6dcfa9f82fe685909d0827cce4d51a13ee3cea274db6bac829ad2`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Suku Bunga Tunggal
Tipe soal: multiple_choice
Stimulus: -
Soal: Pak Bayu merupakan anggota koperasi "Maju Bersama". Beliau menyimpan modal awal sebesar Rp1.000.000,00 di koperasi tersebut. Koperasi memberikan bunga tunggal sebesar 18% per tahun untuk simpanan anggota. Pak Bayu menyimpan modalnya selama 8 bulan.

Hitunglah berapa besar bunga yang akan diterima dan berapa total simpanan Pak Bayu setelah 8 bulan?
Pilihan: A. Bunga Rp1.440.000,00, total simpanan Rp2.440.000,00
B. Bunga Rp120.000,00, total simpanan Rp1.120.000,00
C. Bunga Rp126.492,00, total simpanan Rp1.126.492,00
D. Bunga Rp120.000,00, total simpanan Rp120.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `affcbcedba377489f39a2309`

Seluruh bank di suatu wilayah menawarkan deposito dengan bunga 5%–7% per tahun. Bank XYZ termasuk salah satu bank di wilayah tersebut dengan Ahmad dan Maya sebagai nasabahnya. Ahmad telah menjadi nasabah selama 5 tahun dan Maya telah menjadi nasabah selama 10 tahun.<br><br>Jika saldo deposito Ahmad menjadi Rp26.764.500,00, uang yang disetorkan oleh Ahmad mula-mula adalah ....

| Opsi | Isi |
|---|---|
| A | Rp24.000.000,00 |
| B | Rp22.000.000,00 |
| C | Rp18.000.000,00 |
| D | Rp20.000.000,00 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `72c6fde134336517c1baec94210055004e6da177f85df57528bbc068072a5dbe`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Investasi Bunga Majemuk
Tipe soal: multiple_choice
Stimulus: -
Soal: Seluruh bank di suatu wilayah menawarkan deposito dengan bunga 5%–7% per tahun. Bank XYZ termasuk salah satu bank di wilayah tersebut dengan Ahmad dan Maya sebagai nasabahnya. Ahmad telah menjadi nasabah selama 5 tahun dan Maya telah menjadi nasabah selama 10 tahun.

Jika saldo deposito Ahmad menjadi Rp26.764.500,00, uang yang disetorkan oleh Ahmad mula-mula adalah ....
Pilihan: A. Rp24.000.000,00
B. Rp22.000.000,00
C. Rp18.000.000,00
D. Rp20.000.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `36b2b05ba07a1b3dfb573f9e`

Seseorang berinvestasi saham di suatu aplikasi online. Modal usaha yang diberikan sebesar Rp5.000.000,00. Keuntungan yang didapat menggunakan suku bunga majemuk 15% per tahun. Hitunglah nilai akhir modal tersebut setelah 3 tahun.

| Opsi | Isi |
|---|---|
| A | Rp6.612.500,00 |
| B | Rp7.604.375,00 |
| C | Rp8.573.750,00 |
| D | Rp7.250.000,00 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0b56f47ab60c13a5225ccff7542cba28a4ea15976feae2e46c80574cca02710d`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Investasi Bunga Majemuk
Tipe soal: multiple_choice
Stimulus: -
Soal: Seseorang berinvestasi saham di suatu aplikasi online. Modal usaha yang diberikan sebesar Rp5.000.000,00. Keuntungan yang didapat menggunakan suku bunga majemuk 15% per tahun. Hitunglah nilai akhir modal tersebut setelah 3 tahun.
Pilihan: A. Rp6.612.500,00
B. Rp7.604.375,00
C. Rp8.573.750,00
D. Rp7.250.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 12. Soal `1bc4c0c055bdae30032aa047`

Dani adalah seorang mahasiswa tingkat dua akhir yang ingin menabung untuk melanjutkan studi magister di suatu universitas Kota S. Biaya kuliah dan hidup di Kota S diperkirakan sebesar Rp100.000.000,00. Dani berencana untuk mulai menabung setelah pergantian semester sebesar Rp2.000.000,00 setiap bulan ke dalam rekening deposito yang memberikan bunga 9% per tahun.<br><br>Lama waktu Dani harus menabung agar dapat mencapai targetnya adalah … bulan.

| Opsi | Isi |
|---|---|
| A | 41 |
| B | 44 |
| C | 42 |
| D | 43 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `722856df30f23f8b076aa89c4064ab528674eec38501bddc9ea16d231f7de482`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Investasi Anuitas
Tipe soal: multiple_choice
Stimulus: -
Soal: Dani adalah seorang mahasiswa tingkat dua akhir yang ingin menabung untuk melanjutkan studi magister di suatu universitas Kota S. Biaya kuliah dan hidup di Kota S diperkirakan sebesar Rp100.000.000,00. Dani berencana untuk mulai menabung setelah pergantian semester sebesar Rp2.000.000,00 setiap bulan ke dalam rekening deposito yang memberikan bunga 9% per tahun.

Lama waktu Dani harus menabung agar dapat mencapai targetnya adalah … bulan.
Pilihan: A. 41
B. 44
C. 42
D. 43
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 13. Soal `6e3411514cf1a09e78e56ecd`

Dani adalah seorang mahasiswa tingkat dua akhir yang ingin menabung untuk melanjutkan studi magister di suatu universitas Kota S. Biaya kuliah dan hidup di Kota S diperkirakan sebesar Rp100.000.000,00. Dani berencana untuk mulai menabung setelah pergantian semester sebesar Rp2.000.000,00 setiap bulan ke dalam rekening deposito yang memberikan bunga 9% per tahun.<br><br>Nilai masa depan dari tabungannya setelah empat tahun adalah ....

| Opsi | Isi |
|---|---|
| A | Rp115.000.000,00 |
| B | Rp113.000.000,00 |
| C | Rp114.000.000,00 |
| D | Rp112.000.000,00 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8299fadce580acb88063bd5b28843c6d8a256c0176804738ef7dc19ecb67ff7f`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Investasi Anuitas
Tipe soal: multiple_choice
Stimulus: -
Soal: Dani adalah seorang mahasiswa tingkat dua akhir yang ingin menabung untuk melanjutkan studi magister di suatu universitas Kota S. Biaya kuliah dan hidup di Kota S diperkirakan sebesar Rp100.000.000,00. Dani berencana untuk mulai menabung setelah pergantian semester sebesar Rp2.000.000,00 setiap bulan ke dalam rekening deposito yang memberikan bunga 9% per tahun.

Nilai masa depan dari tabungannya setelah empat tahun adalah ....
Pilihan: A. Rp115.000.000,00
B. Rp113.000.000,00
C. Rp114.000.000,00
D. Rp112.000.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `e10756708fd7c9e1c3bf5ae2`

Ibu Hasti meminjam dana sebesar Rp12.000.000,00 yang diangsur selama 6 bulan (pokok tetap) dengan bunga 8% per tahun.<br><br>Hitung total bunga keseluruhan.

| Opsi | Isi |
|---|---|
| A | Rp960.000,00 |
| B | Rp320.016,00 |
| C | Rp280.014,00 |
| D | Rp480.000,00 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0d36afb72f601c2307c61b854af347def23c530a4f91af277af130acd3500288`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Pinjaman Bunga Majemuk
Tipe soal: multiple_choice
Stimulus: -
Soal: Ibu Hasti meminjam dana sebesar Rp12.000.000,00 yang diangsur selama 6 bulan (pokok tetap) dengan bunga 8% per tahun.

Hitung total bunga keseluruhan.
Pilihan: A. Rp960.000,00
B. Rp320.016,00
C. Rp280.014,00
D. Rp480.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 15. Soal `7f246f52d9fc331e3e277809`

Ibu Hasti meminjam dana sebesar Rp12.000.000,00 yang diangsur selama 6 bulan (pokok tetap) dengan bunga 8% per tahun.<br><br>Hitung angsuran pokok per bulan.

| Opsi | Isi |
|---|---|
| A | Rp2.960.000,00 |
| B | Rp1.500.000,00 |
| C | Rp1.000.000,00 |
| D | Rp2.000.000,00 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `03486477857b44ba6ce78cc601df3eccf4969f60bbe0f6b826f1f577eb3d3e25`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Pinjaman Bunga Majemuk
Tipe soal: multiple_choice
Stimulus: -
Soal: Ibu Hasti meminjam dana sebesar Rp12.000.000,00 yang diangsur selama 6 bulan (pokok tetap) dengan bunga 8% per tahun.

Hitung angsuran pokok per bulan.
Pilihan: A. Rp2.960.000,00
B. Rp1.500.000,00
C. Rp1.000.000,00
D. Rp2.000.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `a4ded83d90999b1517dcec47`

Bu Tania adalah pemilik usaha toko elektronik yang telah berkembang pesat di kotanya. Usahanya menghasilkan omzet rata-rata sebesar Rp120.000.000,00 per bulan. Ia memiliki 10 orang karyawan dengan gaji rata-rata Rp4.000.000,00, serta pengeluaran rutin lainnya sebesar Rp25.000.000,00 per bulan.<br><br>Kini Bu Tania ingin memperluas usahanya ke kota lain dan membutuhkan tambahan modal. Ia mengajukan kredit ke Bank Sentosa, dan mendapat brosur simulasi angsuran kredit seperti tabel berikut.<br><br>\| Pinjaman \| 12 bulan \| 24 bulan \| 36 bulan \| 48 bulan \| 60 bulan \|<br>\|---\|---\|---\|---\|---\|---\|<br>\| Rp10.000.000,00 \| Rp874.515,00 \| Rp456.847,00 \| - \| - \| - \|<br>\| Rp25.000.000,00 \| Rp2.186.287,00 \| Rp1.142.119,00 \| - \| - \| - \|<br>\| Rp30.000.000,00 \| Rp2.623.545,00 \| Rp1.370.542,00 \| - \| - \| - \|<br>\| Rp40.000.000,00 \| Rp3.498.059,00 \| Rp1.827.390,00 \| - \| - \| - \|<br>\| Rp50.000.000,00 \| Rp4.372.574,00 \| Rp2.284.237,00 \| - \| - \| - \|<br>\| Rp60.000.000,00 \| Rp5.247.089,00 \| Rp2.741.085,00 \| Rp1.907.984,00 \| - \| - \|<br>\| Rp70.000.000,00 \| Rp6.121.603,00 \| Rp3.197.932,00 \| Rp2.225.981,00 \| - \| - \|<br>\| Rp80.000.000,00 \| Rp6.996.118,00 \| Rp3.654.780,00 \| Rp2.543.978,00 \| - \| - \|<br>\| Rp100.000.000,00 \| Rp8.745.148,00 \| Rp4.568.474,00 \| Rp3.179.973,00 \| Rp2.488.504,00 \| - \|<br>\| Rp130.000.000,00 \| Rp11.368.693,00 \| Rp5.939.017,00 \| Rp4.133.965,00 \| Rp3.235.055,00 \| Rp2.698.586,00 \|<br>\| Rp150.000.000,00 \| Rp13.117.722,00 \| Rp6.852.711,00 \| Rp4.769.959,00 \| Rp3.732.756,00 \| Rp3.113.753,00 \|<br><br>Bu Tania memutuskan bahwa angsuran maksimal yang dapat ia bayarkan per bulan tidak lebih dari 20% dari total pendapatan bersih per bulan jika mengangsur selama 12 bulan. Namun, jika mengambil angsuran lebih dari 12 bulan (24, 36, 48, atau 60 bulan) tidak lebih dari 10% dari total pendapatan bersih per bulan.<br><br>Andaikan Bu Tania mengambil pinjaman sebesar Rp100.000.000,00 dengan tenor paling singkat, yaitu 12 bulan, Setelah membuka cabang baru, Bu Tania merekrut 5 orang karyawan tambahan dengan besaran gaji yang sama seperti karyawan sebelumnya (Rp4.000.000,00 per orang). Berapa omzet minimal yang harus diperoleh dari cabang baru agar pendapatan bersih total Bu Tania menjadi dua kali lipat dari sebelumnya?

| Opsi | Isi |
|---|---|
| A | Rp138.745.148,00 |
| B | Rp75.000.000,00 |
| C | Rp83.745.148,00 |
| D | Rp55.000.000,00 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `54cbf139c3132f74ad4b69987368613a4d2b2ee230d763e9e6884ad0a00a95c9`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Pinjaman dengan Anuitas
Tipe soal: multiple_choice
Stimulus: -
Soal: Bu Tania adalah pemilik usaha toko elektronik yang telah berkembang pesat di kotanya. Usahanya menghasilkan omzet rata-rata sebesar Rp120.000.000,00 per bulan. Ia memiliki 10 orang karyawan dengan gaji rata-rata Rp4.000.000,00, serta pengeluaran rutin lainnya sebesar Rp25.000.000,00 per bulan.

Kini Bu Tania ingin memperluas usahanya ke kota lain dan membutuhkan tambahan modal. Ia mengajukan kredit ke Bank Sentosa, dan mendapat brosur simulasi angsuran kredit seperti tabel berikut.

| Pinjaman | 12 bulan | 24 bulan | 36 bulan | 48 bulan | 60 bulan |
|---|---|---|---|---|---|
| Rp10.000.000,00 | Rp874.515,00 | Rp456.847,00 | - | - | - |
| Rp25.000.000,00 | Rp2.186.287,00 | Rp1.142.119,00 | - | - | - |
| Rp30.000.000,00 | Rp2.623.545,00 | Rp1.370.542,00 | - | - | - |
| Rp40.000.000,00 | Rp3.498.059,00 | Rp1.827.390,00 | - | - | - |
| Rp50.000.000,00 | Rp4.372.574,00 | Rp2.284.237,00 | - | - | - |
| Rp60.000.000,00 | Rp5.247.089,00 | Rp2.741.085,00 | Rp1.907.984,00 | - | - |
| Rp70.000.000,00 | Rp6.121.603,00 | Rp3.197.932,00 | Rp2.225.981,00 | - | - |
| Rp80.000.000,00 | Rp6.996.118,00 | Rp3.654.780,00 | Rp2.543.978,00 | - | - |
| Rp100.000.000,00 | Rp8.745.148,00 | Rp4.568.474,00 | Rp3.179.973,00 | Rp2.488.504,00 | - |
| Rp130.000.000,00 | Rp11.368.693,00 | Rp5.939.017,00 | Rp4.133.965,00 | Rp3.235.055,00 | Rp2.698.586,00 |
| Rp150.000.000,00 | Rp13.117.722,00 | Rp6.852.711,00 | Rp4.769.959,00 | Rp3.732.756,00 | Rp3.113.753,00 |

Bu Tania memutuskan bahwa angsuran maksimal yang dapat ia bayarkan per bulan tidak lebih dari 20% dari total pendapatan bersih per bulan jika mengangsur selama 12 bulan. Namun, jika mengambil angsuran lebih dari 12 bulan (24, 36, 48, atau 60 bulan) tidak lebih dari 10% dari total pendapatan bersih per bulan.

Andaikan Bu Tania mengambil pinjaman sebesar Rp100.000.000,00 dengan tenor paling singkat, yaitu 12 bulan, Setelah membuka cabang baru, Bu Tania merekrut 5 orang karyawan tambahan dengan besaran gaji yang sama seperti karyawan sebelumnya (Rp4.000.000,00 per orang). Berapa omzet minimal yang harus diperoleh dari cabang baru agar pendapatan bersih total Bu Tania menjadi dua kali lipat dari sebelumnya?
Pilihan: A. Rp138.745.148,00
B. Rp75.000.000,00
C. Rp83.745.148,00
D. Rp55.000.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 17. Soal `b5d6c979c2045301a3560ae7`

Seseorang meminjam uang sebesar Rp10.000.000,00 selama setengah tahun dengan suku bunga 8% per bulan. Berikut dalam tabel rencana angsuran pinjaman tersebut hingga anuitas ke-3 (dalam satuan Rp100.000,00).<br><br>\| Bulan \| Jumlah Pinjaman Awal Bulan \| Bunga Pinjaman \| Angsuran Pinjaman \| Jumlah Pinjaman Akhir Bulan \|<br>\|---\|---\|---\|---\|---\|<br>\| 1 \| 100 \| 8 \| 14 \| 86 \|<br>\| 2 \| 86 \| 6,88 \| 15,12 \| 70,88 \|<br>\| 3 \| 70,88 \| 5,7604 \| 16,32 \| 54,5504 \|<br><br>Besar anuitas pada sistem angsuran tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | Rp2.300.000,00 |
| B | Rp2.000.000,00 |
| C | Rp2.100.000,00 |
| D | Rp2.200.000,00 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e302286064bc4414a0213329aacc44aae92dd359da8027aafafd683fbce96c8d`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Pinjaman dengan Anuitas
Tipe soal: multiple_choice
Stimulus: -
Soal: Seseorang meminjam uang sebesar Rp10.000.000,00 selama setengah tahun dengan suku bunga 8% per bulan. Berikut dalam tabel rencana angsuran pinjaman tersebut hingga anuitas ke-3 (dalam satuan Rp100.000,00).

| Bulan | Jumlah Pinjaman Awal Bulan | Bunga Pinjaman | Angsuran Pinjaman | Jumlah Pinjaman Akhir Bulan |
|---|---|---|---|---|
| 1 | 100 | 8 | 14 | 86 |
| 2 | 86 | 6,88 | 15,12 | 70,88 |
| 3 | 70,88 | 5,7604 | 16,32 | 54,5504 |

Besar anuitas pada sistem angsuran tersebut adalah ....
Pilihan: A. Rp2.300.000,00
B. Rp2.000.000,00
C. Rp2.100.000,00
D. Rp2.200.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `c51d2c28576452736fad772a`

Untuk menggalakkan program koperasi berdaya guna, beberapa koperasi akan memberikan pinjaman masing-masing sebesar Rp50.000.000,00 kepada pengurus desa untuk modal pembangunan. Koperasi A memberikan suku bunga sebesar 3% per tahun selama 6 tahun, sedangkan Koperasi B memberikan suku bunga sebesar 2% per tahun selama 4 tahun.<br><br>Bandingkan nilai akhir yang akan didapat oleh masing-masing koperasi. Manakah yang lebih menguntungkan?

| Opsi | Isi |
|---|---|
| A | Koperasi A (nilai akhir Rp59.702.615,00) lebih menguntungkan dibanding Koperasi B (Rp56.308.121,00) |
| B | Koperasi A dan Koperasi B menghasilkan nilai akhir yang sama besar |
| C | Koperasi B (nilai akhir Rp56.308.121,00) lebih menguntungkan dibanding Koperasi A (Rp59.702.615,00) |
| D | Koperasi B lebih menguntungkan karena periode pinjamannya lebih singkat |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c1fa32af9099f0af37d7f6441cc3668275df22b3b390c9ffac372d01c42e274c`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Parameter Investasi dan Pinjaman
Tipe soal: multiple_choice
Stimulus: -
Soal: Untuk menggalakkan program koperasi berdaya guna, beberapa koperasi akan memberikan pinjaman masing-masing sebesar Rp50.000.000,00 kepada pengurus desa untuk modal pembangunan. Koperasi A memberikan suku bunga sebesar 3% per tahun selama 6 tahun, sedangkan Koperasi B memberikan suku bunga sebesar 2% per tahun selama 4 tahun.

Bandingkan nilai akhir yang akan didapat oleh masing-masing koperasi. Manakah yang lebih menguntungkan?
Pilihan: A. Koperasi A (nilai akhir Rp59.702.615,00) lebih menguntungkan dibanding Koperasi B (Rp56.308.121,00)
B. Koperasi A dan Koperasi B menghasilkan nilai akhir yang sama besar
C. Koperasi B (nilai akhir Rp56.308.121,00) lebih menguntungkan dibanding Koperasi A (Rp59.702.615,00)
D. Koperasi B lebih menguntungkan karena periode pinjamannya lebih singkat
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 19. Soal `7672dd47336c772dbd3a318a`

Suatu aplikasi pinjaman online memberikan pinjaman sebesar Rp10.000.000,00 dengan suku bunga 2% per tahun. Periode pinjaman selama 24 bulan. Berapakah nilai akhir pengembalian pinjaman tersebut?

| Opsi | Isi |
|---|---|
| A | Rp10.200.000,00 |
| B | Rp10.404.000,00 |
| C | Rp10.612.000,00 |
| D | Rp10.000.000,00 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f3936acb37c91c3e82122779d5ddaf43ef317b4a99211cd0b95e01ab85f42d70`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Parameter Investasi dan Pinjaman
Tipe soal: multiple_choice
Stimulus: -
Soal: Suatu aplikasi pinjaman online memberikan pinjaman sebesar Rp10.000.000,00 dengan suku bunga 2% per tahun. Periode pinjaman selama 24 bulan. Berapakah nilai akhir pengembalian pinjaman tersebut?
Pilihan: A. Rp10.200.000,00
B. Rp10.404.000,00
C. Rp10.612.000,00
D. Rp10.000.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `052c617a1f0c63d479f466ab`

Sepuluh orang siswa memiliki tinggi yang berbeda. Guru olahraga menginginkan mereka berbaris menyamping dengan syarat tidak ada siswa diapit oleh dua siswa lain yang lebih tinggi dari dirinya. Berapa banyaknya cara membuat barisan sesuai ketentuan itu?

| Opsi | Isi |
|---|---|
| A | 1.024 cara |
| B | 256 cara |
| C | 512 cara |
| D | 3.628.800 cara |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7252de6261667cf696bbdc004acb53debaca47688b324915a5b71395a1ab0dfe`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Aturan Pengisian Tempat
Tipe soal: multiple_choice
Stimulus: -
Soal: Sepuluh orang siswa memiliki tinggi yang berbeda. Guru olahraga menginginkan mereka berbaris menyamping dengan syarat tidak ada siswa diapit oleh dua siswa lain yang lebih tinggi dari dirinya. Berapa banyaknya cara membuat barisan sesuai ketentuan itu?
Pilihan: A. 1.024 cara
B. 256 cara
C. 512 cara
D. 3.628.800 cara
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 21. Soal `439575e9c1a8bdff1255c8d5`

Arkan memiliki 5 potong kemeja, 4 celana panjang, dan 3 pasang sepatu berbeda yang digunakan sehari-hari sebagai pakaian bekerja. Jika Arkan membuat setelan yang berbeda saat mengenakannya dalam bekerja, tentukan banyak setelan berbeda yang dibuat.

| Opsi | Isi |
|---|---|
| A | 15 setelan |
| B | 12 setelan |
| C | 20 setelan |
| D | 60 setelan |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `807e1c75cee4e179009f0a4a76a503b5705c09f74417d74cba3a1d898e3cb900`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Aturan Pengisian Tempat
Tipe soal: multiple_choice
Stimulus: -
Soal: Arkan memiliki 5 potong kemeja, 4 celana panjang, dan 3 pasang sepatu berbeda yang digunakan sehari-hari sebagai pakaian bekerja. Jika Arkan membuat setelan yang berbeda saat mengenakannya dalam bekerja, tentukan banyak setelan berbeda yang dibuat.
Pilihan: A. 15 setelan
B. 12 setelan
C. 20 setelan
D. 60 setelan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 22. Soal `cd21884f9b39f41443039e69`

Swalayan AAmart mengeluarkan kupon hadiah dengan kode berbentuk bilangan yang disusun dari angka 1, 2, 2, 6, dan 8. Jika kupon-kupon tersebut disusun berdasarkan kodenya mulai dari yang terkecil sampai dengan yang terbesar, maka kupon dengan kode lebih besar daripada 62000 sebanyak ....

| Opsi | Isi |
|---|---|
| A | 19 kupon |
| B | 21 kupon |
| C | 24 kupon |
| D | 20 kupon |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5ef9f2a75d20e6717a9c17abfe220d3f133f02e45c4e1e410bc4b48d1a968191`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Permutasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Swalayan AAmart mengeluarkan kupon hadiah dengan kode berbentuk bilangan yang disusun dari angka 1, 2, 2, 6, dan 8. Jika kupon-kupon tersebut disusun berdasarkan kodenya mulai dari yang terkecil sampai dengan yang terbesar, maka kupon dengan kode lebih besar daripada 62000 sebanyak ....
Pilihan: A. 19 kupon
B. 21 kupon
C. 24 kupon
D. 20 kupon
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 23. Soal `4c33984e92f3e85b5396ba7f`

Ada tujuh orang siswa akan membentuk barisan. Tentukan banyaknya susunan barisan yang mungkin terjadi.

| Opsi | Isi |
|---|---|
| A | 720 susunan |
| B | 40.320 susunan |
| C | 5.040 susunan |
| D | 49 susunan |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6ecc6d4c6377a07db51d2ad4e063d58baefd3f7209ad352a468722ef1bdc90a5`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Permutasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Ada tujuh orang siswa akan membentuk barisan. Tentukan banyaknya susunan barisan yang mungkin terjadi.
Pilihan: A. 720 susunan
B. 40.320 susunan
C. 5.040 susunan
D. 49 susunan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 24. Soal `e9e9f310f9de364e628b69a2`

Terdapat sepuluh orang pergi ketempat wisata dengan mengendarai 3 mobil berkapasitas 4 orang dan tiga orang diantarannya adalah pemilik mobil. Jika setiap mobil dikemudikan oleh pemiliknya dan di setiap mobil minimal ada satu penumpang selain pengemudi, banyaknya kemungkinan komposisi berbeda untuk menempatkan penumpang di ketiga mobil tersebut ada ....

| Opsi | Isi |
|---|---|
| A | 1.190 cara |
| B | 1.050 cara |
| C | 840 cara |
| D | 700 cara |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `47f7b3e788de89a8deb98a1f7a98873f978b924f0bee5f5e67cfec2fcd42946c`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Kombinasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Terdapat sepuluh orang pergi ketempat wisata dengan mengendarai 3 mobil berkapasitas 4 orang dan tiga orang diantarannya adalah pemilik mobil. Jika setiap mobil dikemudikan oleh pemiliknya dan di setiap mobil minimal ada satu penumpang selain pengemudi, banyaknya kemungkinan komposisi berbeda untuk menempatkan penumpang di ketiga mobil tersebut ada ....
Pilihan: A. 1.190 cara
B. 1.050 cara
C. 840 cara
D. 700 cara
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 25. Soal `42af439f72392b9d1118073a`

Pada suatu Olimpiade Matematika, peserta diwajibkan mengerjakan 5 soal dari 8 soal yang tersedia. Tentukan banyaknya jenis pilihan soal yang mungkin dikerjakan.

| Opsi | Isi |
|---|---|
| A | 6.720 |
| B | 40 |
| C | 70 |
| D | 56 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fc2f1d3898fed6dafe44842296de127813dc304b2438e0beaeafe4f445adc45f`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Kombinasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada suatu Olimpiade Matematika, peserta diwajibkan mengerjakan 5 soal dari 8 soal yang tersedia. Tentukan banyaknya jenis pilihan soal yang mungkin dikerjakan.
Pilihan: A. 6.720
B. 40
C. 70
D. 56
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 26. Soal `d4a29da533d9881db57e7c74`

Tim futsal SMA Abhipraya dijadwalkan mengikuti 3 pertandingan awal dalam turnamen dengan sistem poin. Peluang menang untuk setiap pertandingan diperkirakan sebesar 0,6 berdasarkan data latihan dan uji coba. Tentukan peluang tim futsal memenangkan tepat 2 dari 3 pertandingan pertama.

| Opsi | Isi |
|---|---|
| A | 0,216 |
| B | 0,6 |
| C | 0,432 |
| D | 0,36 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `895aecaa215a8c12fabf00c7ee8e330f5b6839f10820045b06d7bbc86f9d8759`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Penerapan Permutasi dan Kombinasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Tim futsal SMA Abhipraya dijadwalkan mengikuti 3 pertandingan awal dalam turnamen dengan sistem poin. Peluang menang untuk setiap pertandingan diperkirakan sebesar 0,6 berdasarkan data latihan dan uji coba. Tentukan peluang tim futsal memenangkan tepat 2 dari 3 pertandingan pertama.
Pilihan: A. 0,216
B. 0,6
C. 0,432
D. 0,36
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 27. Soal `eded99210de8f3efd55fe9df`

Guru IPA menjelaskan bahwa kenyamanan belajar dipengaruhi oleh kualitas udara, yang tergantung pada suhu (t) dan kelembaban (h). Dalam penelitian kecil di kelas, ditemukan bahwa pengaruh suhu dua kali lebih besar dibanding kelembaban, dan model total pengaruhnya adalah $(2t+h)^5$. Jika suatu waktu suhu memberi pengaruh 3 bagian dan kelembaban 2 bagian. Berapakah total kontribusi kombinasi tersebut?

| Opsi | Isi |
|---|---|
| A | 80 |
| B | 32 |
| C | 10 |
| D | 40 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `07f098b72dc678574eb80ff56f3bdd4045ef1badc7e97224fad51551160ac50a`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Penerapan Permutasi dan Kombinasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Guru IPA menjelaskan bahwa kenyamanan belajar dipengaruhi oleh kualitas udara, yang tergantung pada suhu (t) dan kelembaban (h). Dalam penelitian kecil di kelas, ditemukan bahwa pengaruh suhu dua kali lebih besar dibanding kelembaban, dan model total pengaruhnya adalah $(2t+h)^5$. Jika suatu waktu suhu memberi pengaruh 3 bagian dan kelembaban 2 bagian. Berapakah total kontribusi kombinasi tersebut?
Pilihan: A. 80
B. 32
C. 10
D. 40
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 28. Soal `6353e1b1ac73792bd65d8bcc`

Kirana sedang memainkan sebuah permainan yang menggunakan dadu. Dia harus melemparkan sepasang dadu dan mendapatkan angka dobel dan pada lemparan kedua mendapatkan jumlah enam. Dia ingin tahu berapa peluang ini dapat terjadi.<br><br>Jelaskan mengapa aturan perkalian dapat digunakan untuk menentukan peluang ini? Berapa peluangnya?

| Opsi | Isi |
|---|---|
| A | Kedua lemparan saling bebas; peluangnya $\frac{5}{216}$ |
| B | Kedua lemparan saling bebas; peluangnya $\frac{11}{36}$ |
| C | Kedua lemparan saling bebas; peluangnya $\frac{1}{36}$ |
| D | Kedua lemparan saling bebas; peluangnya $\frac{5}{36}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6ebb91147bc4c45f2dafe314a27b79be26f28279720a1a57f8029100f7f85080`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Aturan Perkalian
Tipe soal: multiple_choice
Stimulus: -
Soal: Kirana sedang memainkan sebuah permainan yang menggunakan dadu. Dia harus melemparkan sepasang dadu dan mendapatkan angka dobel dan pada lemparan kedua mendapatkan jumlah enam. Dia ingin tahu berapa peluang ini dapat terjadi.

Jelaskan mengapa aturan perkalian dapat digunakan untuk menentukan peluang ini? Berapa peluangnya?
Pilihan: A. Kedua lemparan saling bebas; peluangnya $\frac{5}{216}$
B. Kedua lemparan saling bebas; peluangnya $\frac{11}{36}$
C. Kedua lemparan saling bebas; peluangnya $\frac{1}{36}$
D. Kedua lemparan saling bebas; peluangnya $\frac{5}{36}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 29. Soal `802d8b32ff2e7869391e39e1`

Mahira mulai mengunduh jadwal pertandingan sepak bola Piala Dunia yang akan datang dimulai dari babak perempat final. Berikut bagan yang diperoleh Mahira. Selanjutnya, Mahira memberikan jajak pendapat kepada teman-temannya yang dahulu rutin menonton pertandingan sepak bola dan menikmati permainan tersebut. Berdasarkan jajak pendapat yang dilakukan Mahira, ia dapat menghitung peluang masing-masing tim tersebut untuk menang di babak perempat final, seperti yang ditunjukkan pada tabel berikut ini. Namun, semua tim memiliki peluang yang sama untuk menang, yakni 0,5, di babak selanjutnya, yang terdiri dari semifinal dan final.<br><br>\|**Prakiraan Perempat Final Piala Dunia**\|\|<br>\|---\|---\|<br>\|Asal Negara\|Peluang Menang\|<br>\|Uruguay\|0,5\|<br>\|Prancis\|0,5\|<br>\|Brazil\|0,8\|<br>\|Belgia\|0,2\|<br>\|Swedia\|0,3\|<br>\|Inggris\|0,7\|<br>\|Rusia\|0,4\|<br>\|Kroasia\|0,6\|<br><br>Berdasarkan bagan pertandingan Piala Dunia dan tabel peluang yang dikumpulkan data oleh Mahira menunjukkan bahwa peluang Inggris untuk memenangkan turnamen tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | 0,343 |
| B | 0,125 |
| C | 0,175 |
| D | 1 |

![Gambar sumber soal 29](<../../../images/kelas12_panduan_siswa_kelas12.pdf-0154-01.png>)


Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas12_panduan_siswa_kelas12.pdf-0154-01.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8cdf1fbc8547fc6f1d5836579dd738f7495745d28bdf20c695a8625c7ac9a415`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Peluang Suatu Kejadian
Tipe soal: multiple_choice
Stimulus: -
Soal: Mahira mulai mengunduh jadwal pertandingan sepak bola Piala Dunia yang akan datang dimulai dari babak perempat final. Berikut bagan yang diperoleh Mahira. Selanjutnya, Mahira memberikan jajak pendapat kepada teman-temannya yang dahulu rutin menonton pertandingan sepak bola dan menikmati permainan tersebut. Berdasarkan jajak pendapat yang dilakukan Mahira, ia dapat menghitung peluang masing-masing tim tersebut untuk menang di babak perempat final, seperti yang ditunjukkan pada tabel berikut ini. Namun, semua tim memiliki peluang yang sama untuk menang, yakni 0,5, di babak selanjutnya, yang terdiri dari semifinal dan final.

|**Prakiraan Perempat Final Piala Dunia**||
|---|---|
|Asal Negara|Peluang Menang|
|Uruguay|0,5|
|Prancis|0,5|
|Brazil|0,8|
|Belgia|0,2|
|Swedia|0,3|
|Inggris|0,7|
|Rusia|0,4|
|Kroasia|0,6|

Berdasarkan bagan pertandingan Piala Dunia dan tabel peluang yang dikumpulkan data oleh Mahira menunjukkan bahwa peluang Inggris untuk memenangkan turnamen tersebut adalah ....
Pilihan: A. 0,343
B. 0,125
C. 0,175
D. 1
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 30. Soal `e6f2f945c5e535887f5e64bc`

Jika tiga dadu standar bersisi enam dilempar bersama-sama, berapakah peluang jumlah total dadu pada ketiga pelemparan sama dengan 12?

| Opsi | Isi |
|---|---|
| A | $\frac{1}{36}$ |
| B | $\frac{1}{216}$ |
| C | $\frac{1}{18}$ |
| D | $\frac{25}{216}$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `98ff35fa049e21938ec83581bfdc38002f600a1e6c1bf8b668c275198ebe02e5`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Peluang Suatu Kejadian
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika tiga dadu standar bersisi enam dilempar bersama-sama, berapakah peluang jumlah total dadu pada ketiga pelemparan sama dengan 12?
Pilihan: A. $\frac{1}{36}$
B. $\frac{1}{216}$
C. $\frac{1}{18}$
D. $\frac{25}{216}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 31. Soal `3631e6eb715153077f0dac66`

Suatu dompet berisi 4 keping uang logam seribu rupiah dan 3 keping uang logam lima ratus rupiah. Dompet kedua berisi 3 keping uang logam seribu rupiah dan 5 keping uang lima ratus ripuah. Satu koin diambil dari dompet pertama dan dimasukkan ke dompet kedua.<br><br>Jika kemudian diambil sekeping uang logam dari dompet kedua, berapa peluang bahwa uang logam yang diambil dari dompet kedua tersebut adalah logam lima ratus rupiah?

| Opsi | Isi |
|---|---|
| A | $\frac{38}{63}$ |
| B | $\frac{5}{8}$ |
| C | $\frac{3}{7}$ |
| D | $\frac{20}{63}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2671d9a323badc0e2375aaeb53c068c86cb5feefecbab879b35281fed09e4c92`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Peluang Kejadian Majemuk
Tipe soal: multiple_choice
Stimulus: -
Soal: Suatu dompet berisi 4 keping uang logam seribu rupiah dan 3 keping uang logam lima ratus rupiah. Dompet kedua berisi 3 keping uang logam seribu rupiah dan 5 keping uang lima ratus ripuah. Satu koin diambil dari dompet pertama dan dimasukkan ke dompet kedua.

Jika kemudian diambil sekeping uang logam dari dompet kedua, berapa peluang bahwa uang logam yang diambil dari dompet kedua tersebut adalah logam lima ratus rupiah?
Pilihan: A. $\frac{38}{63}$
B. $\frac{5}{8}$
C. $\frac{3}{7}$
D. $\frac{20}{63}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 32. Soal `4f4ccc08a9a611e7c44d48a3`

Suatu kantong berisi enam bola merah dan empat bola biru. Dari kantong tersebut akan diambil dua bola berturut-turut.<br><br>Berapa peluang terambilnya dua bola biru, jika: a. dengan pengembalian, dan

| Opsi | Isi |
|---|---|
| A | $\frac{4}{5}$ |
| B | $\frac{2}{15}$ |
| C | $\frac{2}{5}$ |
| D | $\frac{4}{25}$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 12 / Matematika SMA Kelas 12. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `78ebcc1a4e21ac4daed2861c261d42cecfbe6638b3738087048e1a05ecabfe9e`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 12
Topik: Matematika SMA Kelas 12
Subtopik: Peluang Kejadian Majemuk
Tipe soal: multiple_choice
Stimulus: -
Soal: Suatu kantong berisi enam bola merah dan empat bola biru. Dari kantong tersebut akan diambil dua bola berturut-turut.

Berapa peluang terambilnya dua bola biru, jika: a. dengan pengembalian, dan
Pilihan: A. $\frac{4}{5}$
B. $\frac{2}{15}$
C. $\frac{2}{5}$
D. $\frac{4}{25}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
