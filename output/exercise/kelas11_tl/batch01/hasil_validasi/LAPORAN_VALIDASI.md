# Validasi ulang soal kelas 11 TL — Gemini blind N=3 dan diagnostik IndoBERT

**Batch belum selesai:** 9/792 run awal sukses; 0 item tercatat membutuhkan adjudikasi setelah run lengkap. Distribusi berikut masih sementara; item tanpa keputusan ditampilkan sebagai undecided.

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v10-blind-sma11-tl-key-verified`. Rubrik: `math-rubric-3x4x3-v8-sma11-tl-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 11 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan menjadi keputusan silver operasional.

Checkpoint dikunci dengan SHA-256 sebelum pemeriksaan scope IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Artifact berada di luar cakupan kelas 11 TL, sehingga seluruh head abstain dan tidak menghasilkan ukuran agreement dengan label blind.

Jumlah soal: 264; distribusi label advisory: `{"mathCognitiveDomain": {"undecided": 261, "applying": 3, "knowing": 0, "reasoning": 0}, "knowledgeDimension": {"undecided": 261, "conceptual": 1, "procedural": 2, "factual": 0, "metacognitive": 0}, "intendedDifficulty": {"undecided": 261, "Medium": 1, "Easy": 2, "Hard": 0}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"applying": 3, "knowing": 0, "reasoning": 0}, "knowledgeDimension": {"conceptual": 1, "procedural": 2, "factual": 0, "metacognitive": 0}, "intendedDifficulty": {"Medium": 1, "Easy": 2, "Hard": 0}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"needs_ai_review": 261, "silver_ready": 3}`.
Run awal sukses: 9/792; adjudikasi: 1; token sukses tercatat: 29,929.

Seluruh label memakai provenance ai_silver. Delivery memakai snapshot silver yang lolos qualification. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

Artifact diagnostik IndoBERT: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Dataset training: `kelas1-gemini-silver-n3-v1`. Approval provisional: `False`; research-only: `False`; gate data: `False`; anti-collapse: `False`; gate promosi: `False`. Packaging ini tidak melakukan training atau promosi model.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten dapat masuk snapshot silver operasional.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 2 | 2 | [Easy.json](difficulty/Easy.json) |
| Medium | 1 | 1 | [Medium.json](difficulty/Medium.json) |
| Hard | 0 | 0 | [Hard.json](difficulty/Hard.json) |

## Perhitungan yang dipakai

Untuk kelas 11 TL, encoder dan head IndoBERT tidak dijalankan karena cakupan artifact adalah kelas [1, 2, 3, 4, 5, 6], jalur ['regular']. Probabilitas kosong, label/confidence/entropy null, dan action abstain berasal dari pemeriksaan scope runtime. Suara Gemini adalah bukti penilaian advisory, bukan probabilitas IndoBERT.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

Cakupan artifact: kelas [1, 2, 3, 4, 5, 6], jalur ['regular']. Untuk kelas 11 TL, diagnostik mengembalikan `out_of_scope` dan `abstain`: label, confidence, dan entropy null serta probabilitas kosong. Label advisory mengikuti Gemini blind dengan rubrik SMA kelas 11.

## 1. Soal `0103921d7bc075fde728b871`

$A = \begin{pmatrix} 6 & -4 \\ 5 & 8 \\ -7 & 9 \\ 4 & 12 \end{pmatrix}$<br><br>Tentukan jenis matriks $A$ tersebut.

| Opsi | Isi |
|---|---|
| A | Matriks tegak |
| B | Matriks persegi |
| C | Matriks kolom |
| D | Matriks datar |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `25bd1ba75d9b18fae484d70bb97c54c838de4124470cc928e971261a9cb4b4fe`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: $A = \begin{pmatrix} 6 & -4 \\ 5 & 8 \\ -7 & 9 \\ 4 & 12 \end{pmatrix}$

Tentukan jenis matriks $A$ tersebut.
Pilihan: A. Matriks tegak
B. Matriks persegi
C. Matriks kolom
D. Matriks datar
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `d485997ab5faa297fe259e66`

$B = \begin{pmatrix} 8 & -6 & 9 \\ 4 & 7 & -5 \\ 12 & 6 & 10 \end{pmatrix}$<br><br>Jenis matriks $B$ tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | Matriks segitiga atas |
| B | Matriks persegi |
| C | Matriks datar |
| D | Matriks diagonal |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `476c514b44508ef82393c0f6e706e01e13bfadf3bc75dfc264043d33e1f39bda`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: $B = \begin{pmatrix} 8 & -6 & 9 \\ 4 & 7 & -5 \\ 12 & 6 & 10 \end{pmatrix}$

Jenis matriks $B$ tersebut adalah ....
Pilihan: A. Matriks segitiga atas
B. Matriks persegi
C. Matriks datar
D. Matriks diagonal
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `39c563dea9da7ad2a9b2cae0`

$C = \begin{pmatrix} 4 & 0 & 0 \\ 7 & -5 & 0 \\ 8 & 6 & 9 \end{pmatrix}$<br><br>Tentukan jenis matriks $C$ tersebut.

| Opsi | Isi |
|---|---|
| A | Matriks segitiga atas |
| B | Matriks simetris |
| C | Matriks segitiga bawah |
| D | Matriks diagonal |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `dd89263864a13c9c092068fb81b403b26c8e99560198f8f8a83662ea6d7d6e9b`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: $C = \begin{pmatrix} 4 & 0 & 0 \\ 7 & -5 & 0 \\ 8 & 6 & 9 \end{pmatrix}$

Tentukan jenis matriks $C$ tersebut.
Pilihan: A. Matriks segitiga atas
B. Matriks simetris
C. Matriks segitiga bawah
D. Matriks diagonal
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `b2ba770ef02b83e78cffa45e`

$P = \begin{pmatrix} 5 & -2 & 8 \\ -2 & 6 & 4 \\ 8 & 4 & 9 \end{pmatrix}$<br><br>Jenis matriks $P$ tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | Matriks simetris |
| B | Matriks diagonal |
| C | Matriks segitiga bawah |
| D | Matriks segitiga atas |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `276f7e5d3d24d3a16214aafc90095984979efb8bde28bb1a3e048dad8fa689b4`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: $P = \begin{pmatrix} 5 & -2 & 8 \\ -2 & 6 & 4 \\ 8 & 4 & 9 \end{pmatrix}$

Jenis matriks $P$ tersebut adalah ....
Pilihan: A. Matriks simetris
B. Matriks diagonal
C. Matriks segitiga bawah
D. Matriks segitiga atas
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `e0af16757d46f9066f868760`

Matriks datar termasuk ke dalam kelompok matriks ....

| Opsi | Isi |
|---|---|
| A | segitiga |
| B | diagonal |
| C | persegi panjang |
| D | persegi |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `76d2cb09e09a7758d641745d154fd5429dd7563f5cc22f524a4c755f866eda89`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks datar termasuk ke dalam kelompok matriks ....
Pilihan: A. segitiga
B. diagonal
C. persegi panjang
D. persegi
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `4a87d237ea5e909a1d14d583`

Pernyataan yang benar tentang matriks diagonal adalah ....

| Opsi | Isi |
|---|---|
| A | Semua elemen pada diagonal utamanya bernilai satu |
| B | Elemen di atas diagonal utamanya boleh tidak nol |
| C | Semua elemen di luar diagonal utamanya bernilai nol |
| D | Banyak baris tidak sama dengan banyak kolom |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `89f40aa76badbd70a60db729b94f590c5b75f4f417243f5fe6da0f0c685538c2`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Pernyataan yang benar tentang matriks diagonal adalah ....
Pilihan: A. Semua elemen pada diagonal utamanya bernilai satu
B. Elemen di atas diagonal utamanya boleh tidak nol
C. Semua elemen di luar diagonal utamanya bernilai nol
D. Banyak baris tidak sama dengan banyak kolom
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `2629044e6458280325d272a3`

Jika matriks $P$ adalah matriks nol berordo $4 \times 4$, maka matriks $P$ adalah matriks ....

| Opsi | Isi |
|---|---|
| A | diagonal |
| B | kolom |
| C | datar |
| D | identitas |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `59b0529fd14188da2a890c130daeda3f5633cc6c01030ca79283b564d4e3b9ba`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika matriks $P$ adalah matriks nol berordo $4 \times 4$, maka matriks $P$ adalah matriks ....
Pilihan: A. diagonal
B. kolom
C. datar
D. identitas
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `c9d786cd4d15d409bd6c5258`

Sebuah matriks identitas $I_n$ selalu tergolong juga sebagai jenis matriks ....

| Opsi | Isi |
|---|---|
| A | baris |
| B | simetris |
| C | nol |
| D | datar |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9a708cc8c9fea66af5b5b7a79ac5619f2f3a3c9133b32e5893ea766e65f9aece`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah matriks identitas $I_n$ selalu tergolong juga sebagai jenis matriks ....
Pilihan: A. baris
B. simetris
C. nol
D. datar
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 9. Soal `8e859d5970fb95b368d73944`

Jika matriks $M$ adalah matriks diagonal dengan semua elemen diagonal utamanya bernilai satu, maka matriks $M$ disebut matriks ....

| Opsi | Isi |
|---|---|
| A | nol |
| B | tegak |
| C | baris |
| D | identitas |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d7eb9e6b7e2140fbbd73954496f8905c9455be802104eaa851069ae259f383e8`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika matriks $M$ adalah matriks diagonal dengan semua elemen diagonal utamanya bernilai satu, maka matriks $M$ disebut matriks ....
Pilihan: A. nol
B. tegak
C. baris
D. identitas
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `9bab1111a804392509c87111`

Jika $A$ adalah matriks kolom berordo $4 \times 1$ dan $A^t$ transposnya, maka ordo $A^t$ adalah ....

| Opsi | Isi |
|---|---|
| A | $4 \times 4$ |
| B | $1 \times 1$ |
| C | $1 \times 4$ |
| D | $4 \times 1$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2ab37bda9a828023fb2e40de0d477fc4515a334f7ad0cb938af9b8f01c03b497`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika $A$ adalah matriks kolom berordo $4 \times 1$ dan $A^t$ transposnya, maka ordo $A^t$ adalah ....
Pilihan: A. $4 \times 4$
B. $1 \times 1$
C. $1 \times 4$
D. $4 \times 1$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `e5d82ad9f058b9033a17d5d0`

Transpos dari matriks datar berordo $2 \times 5$ merupakan matriks ....

| Opsi | Isi |
|---|---|
| A | baris |
| B | datar |
| C | persegi |
| D | tegak |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `37425a680fca0563401b44c15ababe569f883de40bd416f78565c843e5324b3e`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Transpos dari matriks datar berordo $2 \times 5$ merupakan matriks ....
Pilihan: A. baris
B. datar
C. persegi
D. tegak
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 12. Soal `838e02654b7303347c39b3f8`

Banyak elemen pada sebuah matriks berordo $5 \times 6$ adalah ....

| Opsi | Isi |
|---|---|
| A | $25$ |
| B | $11$ |
| C | $56$ |
| D | $30$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b749694f4caa9a6529638df9017612b930471426a61e60d3cb257330e4b570b3`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Banyak elemen pada sebuah matriks berordo $5 \times 6$ adalah ....
Pilihan: A. $25$
B. $11$
C. $56$
D. $30$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 13. Soal `a5d571e208490af532f2d8b3`

$A = \begin{pmatrix} 12 & -3 & 8 \\ 5 & 9 & -6 \\ 7 & 4 & 10 \\ 2 & 11 & 1 \end{pmatrix}$<br><br>Nilai elemen $a_{32}$ pada matriks $A$ adalah ....

| Opsi | Isi |
|---|---|
| A | $-6$ |
| B | $4$ |
| C | $9$ |
| D | $11$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `dd0e3ddab29a259902882e119b3d0f7f8b110351c5b89d194d76c196b00b9799`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: $A = \begin{pmatrix} 12 & -3 & 8 \\ 5 & 9 & -6 \\ 7 & 4 & 10 \\ 2 & 11 & 1 \end{pmatrix}$

Nilai elemen $a_{32}$ pada matriks $A$ adalah ....
Pilihan: A. $-6$
B. $4$
C. $9$
D. $11$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `fb99506426b946e10816545c`

Nilai ulangan 7 siswa pada 3 mata pelajaran disajikan dalam sebuah matriks. Setiap baris memuat data satu siswa dan setiap kolom memuat data satu mata pelajaran. Ordo matriks tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $7 \times 7$ |
| B | $7 \times 3$ |
| C | $21 \times 1$ |
| D | $3 \times 7$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0c0e15333a8ca2ee5df56abd6c447022cb8b9ef182ab00c0100d6a1d6ca35d2b`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Nilai ulangan 7 siswa pada 3 mata pelajaran disajikan dalam sebuah matriks. Setiap baris memuat data satu siswa dan setiap kolom memuat data satu mata pelajaran. Ordo matriks tersebut adalah ....
Pilihan: A. $7 \times 7$
B. $7 \times 3$
C. $21 \times 1$
D. $3 \times 7$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 15. Soal `49029a2606b708d420f05f6c`

Di antara matriks berikut, yang merupakan matriks kolom adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix} 9 & -4 & 6 \end{pmatrix}$ |
| B | $\begin{pmatrix} 9 & -4 & 6 \\ 1 & 2 & 3 \\ 5 & 7 & 8 \end{pmatrix}$ |
| C | $\begin{pmatrix} 9 & -4 \\ 6 & 2 \\ 5 & 7 \end{pmatrix}$ |
| D | $\begin{pmatrix} 9 \\ -4 \\ 6 \end{pmatrix}$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f26282044180779cfc074f185d4aaf0ab1f344b4dd9268b61cd953cc4cc62c61`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Di antara matriks berikut, yang merupakan matriks kolom adalah ....
Pilihan: A. $\begin{pmatrix} 9 & -4 & 6 \end{pmatrix}$
B. $\begin{pmatrix} 9 & -4 & 6 \\ 1 & 2 & 3 \\ 5 & 7 & 8 \end{pmatrix}$
C. $\begin{pmatrix} 9 & -4 \\ 6 & 2 \\ 5 & 7 \end{pmatrix}$
D. $\begin{pmatrix} 9 \\ -4 \\ 6 \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `efc1ddaf69870b66cfd4eb73`

$A = \begin{pmatrix} 4 & -1 & 7 \\ 3 & 0 & 5 \end{pmatrix}$<br><br>Transpos dari matriks $A$, yaitu $A^t$, adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix} 7 & 5 \\ -1 & 0 \\ 4 & 3 \end{pmatrix}$ |
| B | $\begin{pmatrix} 4 & -1 \\ 7 & 3 \\ 0 & 5 \end{pmatrix}$ |
| C | $\begin{pmatrix} 4 & 3 \\ -1 & 0 \\ 7 & 5 \end{pmatrix}$ |
| D | $\begin{pmatrix} -4 & -3 \\ 1 & 0 \\ -7 & -5 \end{pmatrix}$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `485177254d2d948f25943acfc6f09c038a5e91e0560bfb13e9845b3db5b4c06f`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: $A = \begin{pmatrix} 4 & -1 & 7 \\ 3 & 0 & 5 \end{pmatrix}$

Transpos dari matriks $A$, yaitu $A^t$, adalah ....
Pilihan: A. $\begin{pmatrix} 7 & 5 \\ -1 & 0 \\ 4 & 3 \end{pmatrix}$
B. $\begin{pmatrix} 4 & -1 \\ 7 & 3 \\ 0 & 5 \end{pmatrix}$
C. $\begin{pmatrix} 4 & 3 \\ -1 & 0 \\ 7 & 5 \end{pmatrix}$
D. $\begin{pmatrix} -4 & -3 \\ 1 & 0 \\ -7 & -5 \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 17. Soal `e439d125d8cdf06783174929`

Matriks $S$ berordo $3 \times 3$ adalah matriks simetris dengan $a_{12} = 9$ dan $a_{23} = -4$. Nilai $a_{21} + a_{32}$ adalah ....

| Opsi | Isi |
|---|---|
| A | $5$ |
| B | $0$ |
| C | $13$ |
| D | $-5$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `01793ac4d156c667b0220d9c41b208f789708d28a5c7472ba1fcef7de98fcf33`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $S$ berordo $3 \times 3$ adalah matriks simetris dengan $a_{12} = 9$ dan $a_{23} = -4$. Nilai $a_{21} + a_{32}$ adalah ....
Pilihan: A. $5$
B. $0$
C. $13$
D. $-5$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `540642b03ca9901d5fdc13bf`

$K = \begin{pmatrix} 3 & 2 & 5 \\ -2 & 6 & 1 \\ 9 & 4 & 7 \end{pmatrix}$<br><br>Jumlah elemen-elemen pada diagonal utama matriks $K$ adalah ....

| Opsi | Isi |
|---|---|
| A | $10$ |
| B | $20$ |
| C | $35$ |
| D | $16$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a0c92baf894d7c800b06e5c252d2f4d9dffce413859f4f83952e6ceec38fa066`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: $K = \begin{pmatrix} 3 & 2 & 5 \\ -2 & 6 & 1 \\ 9 & 4 & 7 \end{pmatrix}$

Jumlah elemen-elemen pada diagonal utama matriks $K$ adalah ....
Pilihan: A. $10$
B. $20$
C. $35$
D. $16$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 19. Soal `34f0e546387d35ee3998f4ab`

Jumlah semua elemen pada matriks identitas berordo $5 \times 5$ adalah ....

| Opsi | Isi |
|---|---|
| A | $1$ |
| B | $5$ |
| C | $10$ |
| D | $25$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `169679be9eb811b997df16f101522229529d7eab7232fc7fcf3461769bb4beff`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Jumlah semua elemen pada matriks identitas berordo $5 \times 5$ adalah ....
Pilihan: A. $1$
B. $5$
C. $10$
D. $25$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `1cdc51d3d1afaf591dbe4a43`

Pada matriks segitiga atas berordo $4 \times 4$, banyak elemen yang di bawah diagonal utama (semuanya bernilai nol) adalah ....

| Opsi | Isi |
|---|---|
| A | $6$ |
| B | $4$ |
| C | $12$ |
| D | $10$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `147b043898a23e3c9565ca6f90b52591fdac7ad7274cfb4255e071d0efc188d3`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada matriks segitiga atas berordo $4 \times 4$, banyak elemen yang di bawah diagonal utama (semuanya bernilai nol) adalah ....
Pilihan: A. $6$
B. $4$
C. $12$
D. $10$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 21. Soal `c0f18a02ace3b32bf1d5095c`

Di antara pernyataan berikut, yang benar adalah ....

| Opsi | Isi |
|---|---|
| A | Setiap matriks segitiga atas adalah matriks simetris. |
| B | Setiap matriks simetris adalah matriks diagonal. |
| C | Transpos dari setiap matriks segitiga atas adalah matriks segitiga atas. |
| D | Setiap matriks diagonal adalah matriks simetris. |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `cfbaf720fb0e6ddc50da4eabfa4beccaae5aefbd686e1f68b555f99fc8e50f51`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Di antara pernyataan berikut, yang benar adalah ....
Pilihan: A. Setiap matriks segitiga atas adalah matriks simetris.
B. Setiap matriks simetris adalah matriks diagonal.
C. Transpos dari setiap matriks segitiga atas adalah matriks segitiga atas.
D. Setiap matriks diagonal adalah matriks simetris.
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 22. Soal `34d2027d5af150e8935039d9`

Sebuah matriks $M$ memenuhi $M^t = M$. Pernyataan yang pasti benar tentang $M$ adalah ....

| Opsi | Isi |
|---|---|
| A | $M$ merupakan matriks identitas |
| B | $M$ merupakan matriks persegi |
| C | $M$ merupakan matriks diagonal |
| D | $M$ memuat paling sedikit satu elemen bernilai nol |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `818eb0cc751f0e0164a572e28c042169b0289e445d2a2d299e0b6a0ccf970cd4`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah matriks $M$ memenuhi $M^t = M$. Pernyataan yang pasti benar tentang $M$ adalah ....
Pilihan: A. $M$ merupakan matriks identitas
B. $M$ merupakan matriks persegi
C. $M$ merupakan matriks diagonal
D. $M$ memuat paling sedikit satu elemen bernilai nol
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 23. Soal `ef46da6370f1fc91955096e0`

$K = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 5 \end{pmatrix}$<br><br>Seorang siswa menyatakan bahwa matriks $K$ bukan matriks diagonal karena ada elemen diagonal utama yang bernilai nol. Pernyataan yang tepat tentang penalaran siswa tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | Siswa benar: pada matriks diagonal semua elemen diagonal utama harus bukan nol, sehingga $K$ bukan matriks diagonal |
| B | Siswa keliru: $K$ adalah matriks identitas karena semua elemen di luar diagonal utama bernilai nol |
| C | Siswa keliru: $K$ adalah matriks segitiga atas tetapi bukan matriks diagonal |
| D | Siswa keliru: matriks diagonal hanya mensyaratkan elemen di luar diagonal utama bernilai nol, sehingga $K$ adalah matriks diagonal |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `aef6ef2d885df971ec29526a19c528615b0b94212a74356a1e5b105039ba933a`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: $K = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 5 \end{pmatrix}$

Seorang siswa menyatakan bahwa matriks $K$ bukan matriks diagonal karena ada elemen diagonal utama yang bernilai nol. Pernyataan yang tepat tentang penalaran siswa tersebut adalah ....
Pilihan: A. Siswa benar: pada matriks diagonal semua elemen diagonal utama harus bukan nol, sehingga $K$ bukan matriks diagonal
B. Siswa keliru: $K$ adalah matriks identitas karena semua elemen di luar diagonal utama bernilai nol
C. Siswa keliru: $K$ adalah matriks segitiga atas tetapi bukan matriks diagonal
D. Siswa keliru: matriks diagonal hanya mensyaratkan elemen di luar diagonal utama bernilai nol, sehingga $K$ adalah matriks diagonal
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 24. Soal `49a7280615d4861cac874c5b`

Setiap elemen matriks simetris berordo $3 \times 3$ dipilih dari himpunan $\{0, 1\}$. Banyak matriks yang dapat dibentuk adalah ....

| Opsi | Isi |
|---|---|
| A | $8$ |
| B | $64$ |
| C | $512$ |
| D | $32$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9e3ef25585f00d2abef3414ffe8f36ec72730d6d05ecbabe8186dccecf55a2d8`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Setiap elemen matriks simetris berordo $3 \times 3$ dipilih dari himpunan $\{0, 1\}$. Banyak matriks yang dapat dibentuk adalah ....
Pilihan: A. $8$
B. $64$
C. $512$
D. $32$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 25. Soal `34e45eca80337f97f10d5017`

Setiap elemen matriks persegi berordo $3 \times 3$ dipilih dari himpunan $\{0, 1, 2\}$. Banyak matriks yang sekaligus merupakan matriks segitiga bawah dan matriks simetris adalah ....

| Opsi | Isi |
|---|---|
| A | $27$ |
| B | $729$ |
| C | $9$ |
| D | $81$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d768387d5e24d1db26b6a69e84e0a90b0c2454811423b701f89df000c1768ff6`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Setiap elemen matriks persegi berordo $3 \times 3$ dipilih dari himpunan $\{0, 1, 2\}$. Banyak matriks yang sekaligus merupakan matriks segitiga bawah dan matriks simetris adalah ....
Pilihan: A. $27$
B. $729$
C. $9$
D. $81$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 26. Soal `e6b69eca4b040d37a29b5d3f`

Matriks $M = \begin{pmatrix} 3 & p + 4 & 0 \\ 3q - 6 & 6 & 2r + 2 \\ 0 & r + 1 & 8 \end{pmatrix}$ merupakan matriks segitiga atas sekaligus matriks simetris. Nilai $p + q + r$ adalah ....

| Opsi | Isi |
|---|---|
| A | $5$ |
| B | $-7$ |
| C | $-3$ |
| D | $-1$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `262358976862e781441238d6cf78118d507e2623c438297a249dc52bc8055a18`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $M = \begin{pmatrix} 3 & p + 4 & 0 \\ 3q - 6 & 6 & 2r + 2 \\ 0 & r + 1 & 8 \end{pmatrix}$ merupakan matriks segitiga atas sekaligus matriks simetris. Nilai $p + q + r$ adalah ....
Pilihan: A. $5$
B. $-7$
C. $-3$
D. $-1$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 27. Soal `deff0cee42ca22f2a07b53cd`

Matriks $A$ berordo $(k + 2) \times (10 - k)$ dengan $k$ bilangan asli. Jumlah semua kemungkinan banyak elemen $A$ jika $A$ merupakan matriks tegak tetapi bukan matriks kolom adalah ....

| Opsi | Isi |
|---|---|
| A | $125$ |
| B | $150$ |
| C | $114$ |
| D | $79$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `53f9c4805fc11a32f1434a396698d5534d76437c62dd1e0d105c45bad1a0437b`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$ berordo $(k + 2) \times (10 - k)$ dengan $k$ bilangan asli. Jumlah semua kemungkinan banyak elemen $A$ jika $A$ merupakan matriks tegak tetapi bukan matriks kolom adalah ....
Pilihan: A. $125$
B. $150$
C. $114$
D. $79$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 28. Soal `2aa711c2b030f8f84b05a098`

Diberikan klaim: "Jika $A$ dan $A^t$ sama-sama matriks segitiga atas, maka $A$ adalah matriks identitas." Matriks berordo $3 \times 3$ berikut yang merupakan contoh penyangkal klaim tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 5 \end{pmatrix}$ |
| B | $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ |
| C | $\begin{pmatrix} 1 & 0 & 0 \\ 3 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ |
| D | $\begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1bcad3dd9f301da2c80a3921e7863f5ddca6258cabe7b077e356dc7f83e92677`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diberikan klaim: "Jika $A$ dan $A^t$ sama-sama matriks segitiga atas, maka $A$ adalah matriks identitas." Matriks berordo $3 \times 3$ berikut yang merupakan contoh penyangkal klaim tersebut adalah ....
Pilihan: A. $\begin{pmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 5 \end{pmatrix}$
B. $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$
C. $\begin{pmatrix} 1 & 0 & 0 \\ 3 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$
D. $\begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 29. Soal `42137069df53b29832c7a5dd`

Matriks $A = (a_{ij})$ berordo $3 \times 3$ dengan $i$ nomor baris dan $j$ nomor kolom. Aturan elemen yang menghasilkan matriks simetris yang bukan matriks diagonal adalah ....

| Opsi | Isi |
|---|---|
| A | $a_{ij} = 2i - j$ |
| B | $a_{ij} = i - j$ |
| C | $a_{ij} = i + j$ |
| D | $a_{ij} = i^2 j$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `158a5e856be2f27ca75447387735016933952a4c1f2fdd1c8c84f62db397f1e4`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A = (a_{ij})$ berordo $3 \times 3$ dengan $i$ nomor baris dan $j$ nomor kolom. Aturan elemen yang menghasilkan matriks simetris yang bukan matriks diagonal adalah ....
Pilihan: A. $a_{ij} = 2i - j$
B. $a_{ij} = i - j$
C. $a_{ij} = i + j$
D. $a_{ij} = i^2 j$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 30. Soal `e18ad74984f74a8d128a4970`

Sebuah matriks segitiga atas berordo $n \times n$ memiliki tepat $45$ elemen yang pasti bernilai nol. Banyak elemen yang boleh bernilai tak nol pada matriks tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $10$ |
| B | $55$ |
| C | $45$ |
| D | $100$ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `55`.
Solusi minimum hasil AI: Matriks segitiga atas n x n memiliki elemen nol di bawah diagonal utama sebanyak n(n-1)/2. Diketahui n(n-1)/2 = 45, maka n^2 - n - 90 = 0, sehingga (n-10)(n+9) = 0. Karena n > 0, maka n = 10. Banyak elemen yang boleh tak nol adalah elemen pada diagonal utama dan di atasnya, yaitu n(n+1)/2 = 10(11)/2 = 55.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fe71f7fe8c9c6102bf2174ea48e755cf259fa952b40ce625919c80e8d9f480f2`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2811 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2800 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2828 |

Run 1 — solusi: Matriks segitiga atas n x n memiliki elemen nol di bawah diagonal utama sebanyak n(n-1)/2. Diketahui n(n-1)/2 = 45, maka n^2 - n - 90 = 0, sehingga (n-10)(n+9) = 0. Karena n > 0, maka n = 10. Banyak elemen yang boleh tak nol adalah elemen pada diagonal utama dan di atasnya, yaitu n(n+1)/2 = 10(11)/2 = 55.
- Domain kognitif `classify/applying`: Siswa perlu memahami definisi matriks segitiga atas, merumuskan jumlah elemen nol sebagai deret aritmatika, menyelesaikan persamaan kuadrat untuk mencari n, dan menghitung jumlah elemen tak nol. Ini melibatkan penerapan konsep pada konteks rutin.. Bukti: Sebuah matriks segitiga atas berordo n x n memiliki tepat 45 elemen yang pasti bernilai nol.; Banyak elemen yang boleh bernilai tak nol pada matriks tersebut adalah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman konseptual tentang struktur matriks segitiga atas dan prosedur aljabar untuk menentukan dimensi matriks berdasarkan properti elemennya.. Bukti: matriks segitiga atas berordo n x n; tepat 45 elemen yang pasti bernilai nol
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua tahap perencanaan: menentukan ukuran matriks (n) dari informasi elemen nol, kemudian menghitung elemen tak nol. Siswa harus mengaitkan properti matriks dengan rumus deret/kombinatorial. Tidak ada bantuan langsung, namun prosedurnya standar bagi siswa kelas 11.. Bukti: Sebuah matriks segitiga atas berordo n x n memiliki tepat 45 elemen yang pasti bernilai nol.; Banyak elemen yang boleh bernilai tak nol

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman definisi matriks segitiga atas dan rumus jumlah n bilangan asli pertama. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 diharapkan mampu memodelkan masalah matriks ke dalam persamaan aljabar sederhana. Tingkat kesulitan menengah karena memerlukan integrasi antara definisi matriks dan penyelesaian persamaan kuadrat. |

Run 2 — solusi: Matriks segitiga atas berordo n x n memiliki elemen nol di bawah diagonal utama sebanyak n(n-1)/2. Diketahui n(n-1)/2 = 45, maka n^2 - n - 90 = 0, sehingga (n-10)(n+9) = 0. Karena n > 0, maka n = 10. Banyak elemen yang boleh tak nol adalah elemen pada diagonal utama dan di atasnya, yaitu n(n+1)/2 = 10(11)/2 = 55.
- Domain kognitif `classify/applying`: Siswa perlu memahami definisi matriks segitiga atas, mengaitkan jumlah elemen nol dengan rumus deret aritmatika n(n-1)/2, menyelesaikan persamaan kuadrat untuk mencari n, dan menerapkan rumus n(n+1)/2 untuk mencari elemen tak nol. Ini melibatkan penerapan konsep pada konteks rutin.. Bukti: matriks segitiga atas berordo n x n memiliki tepat 45 elemen yang pasti bernilai nol; Banyak elemen yang boleh tak nol pada matriks tersebut adalah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang struktur matriks segitiga atas dan hubungan antara ordo matriks dengan jumlah elemen nol/tak nol.. Bukti: matriks segitiga atas berordo n x n; tepat 45 elemen yang pasti bernilai nol
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemahaman konsep matriks segitiga atas dan kemampuan aljabar untuk menyelesaikan persamaan kuadrat. Langkah-langkahnya jelas dan prosedural bagi siswa kelas 11, tidak memerlukan strategi non-rutin yang kompleks.. Bukti: matriks segitiga atas berordo n x n; tepat 45 elemen yang pasti bernilai nol

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi matriks segitiga atas, rumus jumlah elemen di bawah diagonal, dan penyelesaian persamaan kuadrat. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun melibatkan aljabar, konsep matriks segitiga atas adalah materi standar kelas 11. Tingkat kesulitan Medium karena siswa harus menghubungkan properti matriks dengan persamaan aljabar. |

Run 3 — solusi: Matriks segitiga atas berordo n x n memiliki elemen nol di bawah diagonal utama sebanyak n(n-1)/2. Diketahui n(n-1)/2 = 45, maka n^2 - n - 90 = 0, sehingga (n-10)(n+9) = 0. Karena n > 0, maka n = 10. Banyak elemen yang boleh tak nol adalah elemen pada diagonal utama dan di atasnya, yaitu n(n+1)/2 = 10(11)/2 = 55.
- Domain kognitif `classify/applying`: Siswa perlu memahami definisi matriks segitiga atas, mengaitkan jumlah elemen nol dengan rumus deret aritmatika n(n-1)/2, menyelesaikan persamaan kuadrat untuk mencari n, dan menghitung jumlah elemen tak nol menggunakan rumus n(n+1)/2. Ini adalah penerapan konsep pada konteks rutin.. Bukti: Sebuah matriks segitiga atas berordo n x n memiliki tepat 45 elemen yang pasti bernilai nol.; Banyak elemen yang boleh tak nol pada matriks tersebut adalah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang struktur matriks segitiga atas dan prosedur untuk menghitung jumlah elemen berdasarkan indeks baris dan kolom.. Bukti: matriks segitiga atas berordo n x n; tepat 45 elemen yang pasti bernilai nol
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua tahap perhitungan yang saling terkait: menentukan ordo matriks n dari informasi elemen nol, kemudian menghitung elemen tak nol. Siswa harus menghubungkan konsep matriks dengan deret aritmatika, namun prosedurnya standar dan familiar bagi siswa kelas 11.. Bukti: matriks segitiga atas berordo n x n; tepat 45 elemen yang pasti bernilai nol

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi matriks segitiga atas, rumus jumlah elemen di bawah diagonal utama, dan penyelesaian persamaan kuadrat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan mampu memodelkan struktur matriks ke dalam persamaan aljabar. Soal ini menuntut pemahaman struktur matriks, bukan sekadar operasi hitung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah matriks segitiga atas berordo $n \times n$ memiliki tepat $45$ elemen yang pasti bernilai nol. Banyak elemen yang boleh bernilai tak nol pada matriks tersebut adalah ....
Pilihan: A. $10$
B. $55$
C. $45$
D. $100$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 31. Soal `c173afa2ea6e0ab1b470a57d`

Sebuah matriks identitas berordo $4 \times 4$ tergolong ke dalam semua jenis matriks berikut, kecuali matriks ....

| Opsi | Isi |
|---|---|
| A | simetris |
| B | tegak |
| C | diagonal |
| D | segitiga bawah |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e48bc64ac29f457beba19ff1e7d4ea6ea0dc8055eb153a048324eb6b0660371b`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah matriks identitas berordo $4 \times 4$ tergolong ke dalam semua jenis matriks berikut, kecuali matriks ....
Pilihan: A. simetris
B. tegak
C. diagonal
D. segitiga bawah
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 32. Soal `021686301ce6aa70ea7f8b45`

Kebutuhan energi minimal atlet lari putri (dalam kalori) adalah sebagai berikut.<br><br>- Usia 14—15 tahun: normal 1.800; ditambah 3 jam latihan 2.400; ditambah 4 jam latihan 2.700; ditambah 5 jam latihan 3.000.<br>- Usia 16—17 tahun: normal 2.100; ditambah 3 jam latihan 2.600; ditambah 4 jam latihan 2.900; ditambah 5 jam latihan 3.300.<br>- Usia 18—20 tahun: normal 2.300; ditambah 3 jam latihan 2.800; ditambah 4 jam latihan 3.100; ditambah 5 jam latihan 3.500.<br><br>Data disusun menjadi matriks dengan baris menyatakan kelompok usia (urut dari yang termuda) dan kolom menyatakan kondisi (normal, tambah 3 jam, tambah 4 jam, tambah 5 jam). Pernyataan yang benar tentang matriks tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | Matriks tegak berordo $4 \times 3$ dengan elemen baris ke-2 kolom ke-3 bernilai $2.900$ |
| B | Matriks datar berordo $3 \times 4$ dengan elemen baris ke-2 kolom ke-3 bernilai $2.600$ |
| C | Matriks datar berordo $3 \times 4$ dengan elemen baris ke-2 kolom ke-3 bernilai $2.900$ |
| D | Matriks datar berordo $3 \times 4$ dengan elemen baris ke-2 kolom ke-3 bernilai $3.100$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6d726c04fbb9952c9f5c7e12df208fd434597b2b7684a7ec03314b7ec8cbd6ac`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Kebutuhan energi minimal atlet lari putri (dalam kalori) adalah sebagai berikut.

- Usia 14—15 tahun: normal 1.800; ditambah 3 jam latihan 2.400; ditambah 4 jam latihan 2.700; ditambah 5 jam latihan 3.000.
- Usia 16—17 tahun: normal 2.100; ditambah 3 jam latihan 2.600; ditambah 4 jam latihan 2.900; ditambah 5 jam latihan 3.300.
- Usia 18—20 tahun: normal 2.300; ditambah 3 jam latihan 2.800; ditambah 4 jam latihan 3.100; ditambah 5 jam latihan 3.500.

Data disusun menjadi matriks dengan baris menyatakan kelompok usia (urut dari yang termuda) dan kolom menyatakan kondisi (normal, tambah 3 jam, tambah 4 jam, tambah 5 jam). Pernyataan yang benar tentang matriks tersebut adalah ....
Pilihan: A. Matriks tegak berordo $4 \times 3$ dengan elemen baris ke-2 kolom ke-3 bernilai $2.900$
B. Matriks datar berordo $3 \times 4$ dengan elemen baris ke-2 kolom ke-3 bernilai $2.600$
C. Matriks datar berordo $3 \times 4$ dengan elemen baris ke-2 kolom ke-3 bernilai $2.900$
D. Matriks datar berordo $3 \times 4$ dengan elemen baris ke-2 kolom ke-3 bernilai $3.100$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 33. Soal `986fa0b1c23c4c63583a9107`

Kebutuhan energi lima atlet (dalam kalori) dicatat saat istirahat dan saat latihan.<br><br>\| Atlet \| Istirahat \| Latihan \|<br>\|---\|---\|---\|<br>\| Andi \| 1.700 \| 2.300 \|<br>\| Budi \| 1.900 \| 2.600 \|<br>\| Candra \| 2.200 \| 2.900 \|<br>\| Dimas \| 1.800 \| 2.400 \|<br>\| Eko \| 2.100 \| 2.800 \|<br><br>Data pada tabel disusun menjadi matriks $K$ dengan setiap baris memuat data satu kondisi (istirahat dan latihan) dan setiap kolom memuat data satu atlet. Matriks $K$ merupakan ....

| Opsi | Isi |
|---|---|
| A | matriks datar berordo $2 \times 5$ |
| B | matriks tegak berordo $5 \times 2$ |
| C | matriks kolom berordo $10 \times 1$ |
| D | matriks baris berordo $1 \times 10$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `84d5037799a6537c56ef31b6abb4a43144ddeb6cc012a0da8c5bea0dd6f525ec`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Kebutuhan energi lima atlet (dalam kalori) dicatat saat istirahat dan saat latihan.

| Atlet | Istirahat | Latihan |
|---|---|---|
| Andi | 1.700 | 2.300 |
| Budi | 1.900 | 2.600 |
| Candra | 2.200 | 2.900 |
| Dimas | 1.800 | 2.400 |
| Eko | 2.100 | 2.800 |

Data pada tabel disusun menjadi matriks $K$ dengan setiap baris memuat data satu kondisi (istirahat dan latihan) dan setiap kolom memuat data satu atlet. Matriks $K$ merupakan ....
Pilihan: A. matriks datar berordo $2 \times 5$
B. matriks tegak berordo $5 \times 2$
C. matriks kolom berordo $10 \times 1$
D. matriks baris berordo $1 \times 10$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 34. Soal `04f00a7a1504f1359426c352`

Sebuah matriks tegak memuat $60$ elemen dan memiliki paling sedikit dua kolom. Banyak kemungkinan ordo matriks tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $6$ |
| B | $10$ |
| C | $5$ |
| D | $12$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `973e6abd3ce5aedf31d26a251a421ba302ea47c91c737d8b397907498cb0b147`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah matriks tegak memuat $60$ elemen dan memiliki paling sedikit dua kolom. Banyak kemungkinan ordo matriks tersebut adalah ....
Pilihan: A. $6$
B. $10$
C. $5$
D. $12$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 35. Soal `975b39930ae217460cb10da6`

Matriks $K = \begin{pmatrix} 3 & p + 3 & 0 \\ 0 & 5 & 3q - 12 \\ 0 & 0 & 2 \end{pmatrix}$ merupakan matriks diagonal. Nilai $p \cdot q$ adalah ....

| Opsi | Isi |
|---|---|
| A | $-7$ |
| B | $12$ |
| C | $-12$ |
| D | $1$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `72f98872e6248cd398aeb22f917108c486f899df6ad32e152bc17b34ae9f71cb`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $K = \begin{pmatrix} 3 & p + 3 & 0 \\ 0 & 5 & 3q - 12 \\ 0 & 0 & 2 \end{pmatrix}$ merupakan matriks diagonal. Nilai $p \cdot q$ adalah ....
Pilihan: A. $-7$
B. $12$
C. $-12$
D. $1$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 36. Soal `b3493a9d9726248b26838eda`

Di antara matriks berordo $3 \times 3$ berikut, yang merupakan matriks simetris tetapi bukan matriks diagonal adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix} 6 & -2 & 0 \\ 2 & 4 & 5 \\ 0 & -5 & 3 \end{pmatrix}$ |
| B | $\begin{pmatrix} 6 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 3 \end{pmatrix}$ |
| C | $\begin{pmatrix} 6 & -2 & 0 \\ 0 & 4 & 5 \\ 0 & 0 & 3 \end{pmatrix}$ |
| D | $\begin{pmatrix} 6 & -2 & 0 \\ -2 & 4 & 5 \\ 0 & 5 & 3 \end{pmatrix}$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `db500ef720b2b2f5a93439346e1e48eee3f13f7fb65219f3cd2f78d7e0b36445`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Di antara matriks berordo $3 \times 3$ berikut, yang merupakan matriks simetris tetapi bukan matriks diagonal adalah ....
Pilihan: A. $\begin{pmatrix} 6 & -2 & 0 \\ 2 & 4 & 5 \\ 0 & -5 & 3 \end{pmatrix}$
B. $\begin{pmatrix} 6 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 3 \end{pmatrix}$
C. $\begin{pmatrix} 6 & -2 & 0 \\ 0 & 4 & 5 \\ 0 & 0 & 3 \end{pmatrix}$
D. $\begin{pmatrix} 6 & -2 & 0 \\ -2 & 4 & 5 \\ 0 & 5 & 3 \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 37. Soal `02efae58d2abc1412855c5eb`

Transpos matriks $P$ adalah matriks $Q$ berordo $3 \times 7$. Pernyataan yang benar tentang matriks $P$ adalah ....

| Opsi | Isi |
|---|---|
| A | $P$ merupakan matriks tegak yang memuat $21$ elemen |
| B | $P$ merupakan matriks persegi yang memuat $49$ elemen |
| C | $P$ merupakan matriks datar yang memuat $21$ elemen |
| D | $P$ merupakan matriks tegak yang memuat $10$ elemen |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2c1b556cdb05bf496cf719f9e27149dca6dd5196fc1323103ea62b24b569e0fb`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Transpos matriks $P$ adalah matriks $Q$ berordo $3 \times 7$. Pernyataan yang benar tentang matriks $P$ adalah ....
Pilihan: A. $P$ merupakan matriks tegak yang memuat $21$ elemen
B. $P$ merupakan matriks persegi yang memuat $49$ elemen
C. $P$ merupakan matriks datar yang memuat $21$ elemen
D. $P$ merupakan matriks tegak yang memuat $10$ elemen
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 38. Soal `e0dd0450f7bda42d1475d560`

$U = \begin{pmatrix} 6 & -4 & 7 \\ 0 & 8 & -3 \\ 0 & 0 & 5 \end{pmatrix}$<br><br>Matriks $U$ berjenis segitiga atas. Pernyataan yang benar tentang transpos $U$, yaitu $U^t$, adalah ....

| Opsi | Isi |
|---|---|
| A | $U^t$ matriks segitiga atas dan elemen baris ke-3 kolom ke-1 bernilai $7$ |
| B | $U^t$ matriks segitiga bawah dan elemen baris ke-3 kolom ke-1 bernilai $0$ |
| C | $U^t$ matriks segitiga bawah dan elemen baris ke-3 kolom ke-1 bernilai $-4$ |
| D | $U^t$ matriks segitiga bawah dan elemen baris ke-3 kolom ke-1 bernilai $7$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `55382406d20d14d095e3197b646b3b255067d65e566c440f3fe54812bbb9d8b3`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: $U = \begin{pmatrix} 6 & -4 & 7 \\ 0 & 8 & -3 \\ 0 & 0 & 5 \end{pmatrix}$

Matriks $U$ berjenis segitiga atas. Pernyataan yang benar tentang transpos $U$, yaitu $U^t$, adalah ....
Pilihan: A. $U^t$ matriks segitiga atas dan elemen baris ke-3 kolom ke-1 bernilai $7$
B. $U^t$ matriks segitiga bawah dan elemen baris ke-3 kolom ke-1 bernilai $0$
C. $U^t$ matriks segitiga bawah dan elemen baris ke-3 kolom ke-1 bernilai $-4$
D. $U^t$ matriks segitiga bawah dan elemen baris ke-3 kolom ke-1 bernilai $7$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 39. Soal `ed6d1f588c6e6de54beeb7bd`

$C = \begin{pmatrix} 7 & -8 & 9 & 4 & 6 \\ -10 & 11 & 12 & 14 & -6 \end{pmatrix}$<br><br>Tentukan jenis matriks $C^t$.

| Opsi | Isi |
|---|---|
| A | Matriks tegak |
| B | Matriks persegi |
| C | Matriks kolom |
| D | Matriks datar |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b03864cda7c16c7cf955cec0a6b20d61b90c164ea86bce10c2c84f6206171927`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: $C = \begin{pmatrix} 7 & -8 & 9 & 4 & 6 \\ -10 & 11 & 12 & 14 & -6 \end{pmatrix}$

Tentukan jenis matriks $C^t$.
Pilihan: A. Matriks tegak
B. Matriks persegi
C. Matriks kolom
D. Matriks datar
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 40. Soal `3efcbb154ab41a3fa6ddd740`

Sebuah matriks persegi panjang memuat $35$ elemen dan banyak barisnya $2$ lebih banyak daripada banyak kolomnya. Ordo matriks tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $6 \times 4$ |
| B | $7 \times 5$ |
| C | $5 \times 7$ |
| D | $35 \times 1$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `276ee40c2ab04f5c118e160e6f51cdf14c5b35d2a6eb3bb430ad7668abdd739a`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah matriks persegi panjang memuat $35$ elemen dan banyak barisnya $2$ lebih banyak daripada banyak kolomnya. Ordo matriks tersebut adalah ....
Pilihan: A. $6 \times 4$
B. $7 \times 5$
C. $5 \times 7$
D. $35 \times 1$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 41. Soal `eafbe60efd8c26e57d736253`

Matriks $A = (a_{ij})$ berordo $3 \times 3$ dengan $a_{ij} = i \cdot j - i$, dengan $i$ nomor baris dan $j$ nomor kolom. Jumlah elemen pada diagonal utama matriks $A$ adalah ....

| Opsi | Isi |
|---|---|
| A | $8$ |
| B | $20$ |
| C | $14$ |
| D | $4$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5fd9809c5475c1c50a2245206d30e6a877cb6aa32df0206b40c09103ebfa7c74`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A = (a_{ij})$ berordo $3 \times 3$ dengan $a_{ij} = i \cdot j - i$, dengan $i$ nomor baris dan $j$ nomor kolom. Jumlah elemen pada diagonal utama matriks $A$ adalah ....
Pilihan: A. $8$
B. $20$
C. $14$
D. $4$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 42. Soal `bcdf1875d85ced1040d8839d`

$A = \begin{pmatrix} 3 & -1 & 6 & 2 \\ 5 & 0 & -4 & -7 \\ 7 & 9 & 1 & -2 \end{pmatrix}$<br><br>Elemen pada baris ke-4 dan kolom ke-2 matriks $A^t$ bernilai ....

| Opsi | Isi |
|---|---|
| A | $9$ |
| B | $-4$ |
| C | $-2$ |
| D | $-7$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e14992e5074f6cd192fe5edd041e132a9aff656abebe011f42fbabc8c1a2debe`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: $A = \begin{pmatrix} 3 & -1 & 6 & 2 \\ 5 & 0 & -4 & -7 \\ 7 & 9 & 1 & -2 \end{pmatrix}$

Elemen pada baris ke-4 dan kolom ke-2 matriks $A^t$ bernilai ....
Pilihan: A. $9$
B. $-4$
C. $-2$
D. $-7$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 43. Soal `7fd4be0aa2258ebb04d0dde7`

Matriks $S = \begin{pmatrix} 3 & 2x & 5 \\ 10 & 1 & y + 2 \\ 5 & 6 & 4 \end{pmatrix}$ merupakan matriks simetris. Nilai $x + y$ adalah ....

| Opsi | Isi |
|---|---|
| A | $9$ |
| B | $11$ |
| C | $13$ |
| D | $14$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1031ff031a5e5945952778549ddae1a4922a71f4868a5a3a66470a054055c75c`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $S = \begin{pmatrix} 3 & 2x & 5 \\ 10 & 1 & y + 2 \\ 5 & 6 & 4 \end{pmatrix}$ merupakan matriks simetris. Nilai $x + y$ adalah ....
Pilihan: A. $9$
B. $11$
C. $13$
D. $14$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 44. Soal `f6fe0e4f5622378138702ecd`

Matriks segitiga atas berordo $6 \times 6$ dan matriks diagonal berordo $6 \times 6$ masing-masing dibuat dengan elemen tak nol sebanyak mungkin. Selisih banyak elemen tak nol kedua matriks tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $21$ |
| B | $27$ |
| C | $30$ |
| D | $15$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `69f549a0495460909471c4e3f8a73d578c0e4713d6b796691fc37be6648c3cae`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks segitiga atas berordo $6 \times 6$ dan matriks diagonal berordo $6 \times 6$ masing-masing dibuat dengan elemen tak nol sebanyak mungkin. Selisih banyak elemen tak nol kedua matriks tersebut adalah ....
Pilihan: A. $21$
B. $27$
C. $30$
D. $15$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 45. Soal `a5a86877ae7cf70501add9d8`

Di antara matriks berordo $3 \times 3$ berikut, yang merupakan matriks segitiga atas tetapi bukan matriks diagonal adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix} 2 & 0 & 0 \\ 5 & 3 & 0 \\ 1 & 4 & 6 \end{pmatrix}$ |
| B | $\begin{pmatrix} 2 & 5 & 1 \\ 0 & 3 & 4 \\ 7 & 0 & 6 \end{pmatrix}$ |
| C | $\begin{pmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 6 \end{pmatrix}$ |
| D | $\begin{pmatrix} 2 & 5 & 1 \\ 0 & 3 & 4 \\ 0 & 0 & 6 \end{pmatrix}$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `332a67e1721c168d53d1dd37a3a2c1ffc35d5f14a1fdcfd82b29bcd0eaf4197f`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Di antara matriks berordo $3 \times 3$ berikut, yang merupakan matriks segitiga atas tetapi bukan matriks diagonal adalah ....
Pilihan: A. $\begin{pmatrix} 2 & 0 & 0 \\ 5 & 3 & 0 \\ 1 & 4 & 6 \end{pmatrix}$
B. $\begin{pmatrix} 2 & 5 & 1 \\ 0 & 3 & 4 \\ 7 & 0 & 6 \end{pmatrix}$
C. $\begin{pmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 6 \end{pmatrix}$
D. $\begin{pmatrix} 2 & 5 & 1 \\ 0 & 3 & 4 \\ 0 & 0 & 6 \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 46. Soal `1facb098aa341522dcf30f8f`

Matriks persegi yang sekaligus merupakan matriks segitiga atas dan matriks simetris pasti merupakan matriks ....

| Opsi | Isi |
|---|---|
| A | identitas |
| B | datar |
| C | diagonal |
| D | nol |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0fff3c282433db0aad58d51873b1ea0ad3df549df017c084a1a546a6eb2bd308`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks persegi yang sekaligus merupakan matriks segitiga atas dan matriks simetris pasti merupakan matriks ....
Pilihan: A. identitas
B. datar
C. diagonal
D. nol
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 47. Soal `2421411df5e5a05821133ccf`

Rekapan absensi peserta didik kelas XII di SMA Makmur dalam satu semester.<br><br>\| Keterangan \| XII 1 \| XII 2 \| XII 3 \|<br>\|---\|---\|---\|---\|<br>\| Izin \| 1 \| 1 \| 3 \|<br>\| Sakit \| 2 \| 1 \| 3 \|<br>\| Tanpa keterangan \| 5 \| 1 \| 2 \|<br><br>Data pada tabel disajikan sebagai matriks dengan setiap baris menyatakan satu jenis keterangan dan setiap kolom menyatakan satu kelas. Pernyataan yang benar tentang matriks tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | Matriks segitiga atas dengan jumlah elemen diagonal utama $4$ |
| B | Matriks persegi dengan jumlah elemen diagonal utama $4$ |
| C | Matriks persegi dengan jumlah elemen diagonal utama $9$ |
| D | Matriks datar dengan jumlah elemen diagonal utama $4$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `dc72e4c3c6be97b13aec4ca972453c0bf0b45c3e57cdefb69498175d47fc8556`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Rekapan absensi peserta didik kelas XII di SMA Makmur dalam satu semester.

| Keterangan | XII 1 | XII 2 | XII 3 |
|---|---|---|---|
| Izin | 1 | 1 | 3 |
| Sakit | 2 | 1 | 3 |
| Tanpa keterangan | 5 | 1 | 2 |

Data pada tabel disajikan sebagai matriks dengan setiap baris menyatakan satu jenis keterangan dan setiap kolom menyatakan satu kelas. Pernyataan yang benar tentang matriks tersebut adalah ....
Pilihan: A. Matriks segitiga atas dengan jumlah elemen diagonal utama $4$
B. Matriks persegi dengan jumlah elemen diagonal utama $4$
C. Matriks persegi dengan jumlah elemen diagonal utama $9$
D. Matriks datar dengan jumlah elemen diagonal utama $4$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 48. Soal `77a017bcb918baf914effef4`

Matriks simetris berordo $4 \times 4$ paling banyak memiliki elemen dengan nilai yang berbeda sebanyak ....

| Opsi | Isi |
|---|---|
| A | $6$ |
| B | $16$ |
| C | $10$ |
| D | $12$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6cf87b2e3d5806d02af4611f94d076e49c0158a44c70ce79eebbd5781ef13509`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks simetris berordo $4 \times 4$ paling banyak memiliki elemen dengan nilai yang berbeda sebanyak ....
Pilihan: A. $6$
B. $16$
C. $10$
D. $12$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 49. Soal `b38d769153c003f829c45b65`

Matriks $E = \begin{pmatrix} 3p - 8 & 0 & 0 \\ 0 & q + 6 & 0 \\ 0 & 0 & 2r - 7 \end{pmatrix}$ merupakan matriks identitas. Nilai $p + q + r$ adalah ....

| Opsi | Isi |
|---|---|
| A | $12$ |
| B | $2$ |
| C | $6$ |
| D | $8$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `745662d5425c3d9c3dfbcab375f07c0d41f787ba4b584e42910a3756f2afd7a0`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $E = \begin{pmatrix} 3p - 8 & 0 & 0 \\ 0 & q + 6 & 0 \\ 0 & 0 & 2r - 7 \end{pmatrix}$ merupakan matriks identitas. Nilai $p + q + r$ adalah ....
Pilihan: A. $12$
B. $2$
C. $6$
D. $8$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 50. Soal `63f5342790d8774c8fd9af69`

Matriks $D = (d_{ij})$ berordo $3 \times 3$ dengan $d_{ij} = i + 2j$. Baris pertama matriks $D^t$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix} 3 & 5 & 7 \end{pmatrix}$ |
| B | $\begin{pmatrix} 3 & 4 & 5 \end{pmatrix}$ |
| C | $\begin{pmatrix} 5 & 7 & 9 \end{pmatrix}$ |
| D | $\begin{pmatrix} 2 & 3 & 4 \end{pmatrix}$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d8c1e6b4d89096feb656df0f058d0a228fa72b6cfed1987812421b5bf6fbbcd6`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $D = (d_{ij})$ berordo $3 \times 3$ dengan $d_{ij} = i + 2j$. Baris pertama matriks $D^t$ adalah ....
Pilihan: A. $\begin{pmatrix} 3 & 5 & 7 \end{pmatrix}$
B. $\begin{pmatrix} 3 & 4 & 5 \end{pmatrix}$
C. $\begin{pmatrix} 5 & 7 & 9 \end{pmatrix}$
D. $\begin{pmatrix} 2 & 3 & 4 \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 51. Soal `7020f0074123a861fe812baf`

Diketahui matriks $P = \begin{pmatrix} 2 & 5 \\ 7 & 3 \end{pmatrix}$. Matriks berikut yang sama dengan $P$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix} 2 & 7 \\ 5 & 3 \end{pmatrix}$ |
| B | $\begin{pmatrix} 2 & 5 & 0 \\ 7 & 3 & 0 \end{pmatrix}$ |
| C | $\begin{pmatrix} \frac{4}{2} & 5 \\ 7 & \frac{6}{2} \end{pmatrix}$ |
| D | $\begin{pmatrix} 2 & 5 \\ 3 & 7 \end{pmatrix}$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3a548dd7e095d975f098754f78c9cfd599daf79c3ef0a8206c353f34f82ce3f1`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui matriks $P = \begin{pmatrix} 2 & 5 \\ 7 & 3 \end{pmatrix}$. Matriks berikut yang sama dengan $P$ adalah ....
Pilihan: A. $\begin{pmatrix} 2 & 7 \\ 5 & 3 \end{pmatrix}$
B. $\begin{pmatrix} 2 & 5 & 0 \\ 7 & 3 & 0 \end{pmatrix}$
C. $\begin{pmatrix} \frac{4}{2} & 5 \\ 7 & \frac{6}{2} \end{pmatrix}$
D. $\begin{pmatrix} 2 & 5 \\ 3 & 7 \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 52. Soal `25a00100b2a704c17da563e9`

Matriks $A = (a_{ij})$ dan $B = (b_{ij})$ keduanya berordo $3 \times 3$ dan $A = B$. Jika $a_{23} = 9$, maka ....

| Opsi | Isi |
|---|---|
| A | $b_{32} = 9$ |
| B | $b_{13} = 9$ |
| C | $b_{22} = 9$ |
| D | $b_{23} = 9$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e68f671239cae4dd0d2bf42992cd203c76e274c1f8ab327e9eca77cccdfb024a`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A = (a_{ij})$ dan $B = (b_{ij})$ keduanya berordo $3 \times 3$ dan $A = B$. Jika $a_{23} = 9$, maka ....
Pilihan: A. $b_{32} = 9$
B. $b_{13} = 9$
C. $b_{22} = 9$
D. $b_{23} = 9$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 53. Soal `0e88aef69611afbca0d59171`

Diketahui $\begin{pmatrix} 2x & 5 \\ 1 & 7 \end{pmatrix} = \begin{pmatrix} 18 & 5 \\ 1 & 7 \end{pmatrix}$. Nilai $x$ adalah ....

| Opsi | Isi |
|---|---|
| A | 9 |
| B | 36 |
| C | -9 |
| D | 16 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `34f475f24ed0a0e55130331b820c9554e6c0bcc5eb6e9ad16c04e92251a455e7`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $\begin{pmatrix} 2x & 5 \\ 1 & 7 \end{pmatrix} = \begin{pmatrix} 18 & 5 \\ 1 & 7 \end{pmatrix}$. Nilai $x$ adalah ....
Pilihan: A. 9
B. 36
C. -9
D. 16
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 54. Soal `a0a68599e6b31c6e691e774f`

Diketahui $\begin{pmatrix} 3a - 2 & 0 \\ 4 & b + 6 \end{pmatrix} = \begin{pmatrix} 10 & 0 \\ 4 & 1 \end{pmatrix}$. Nilai $a + b$ adalah ....

| Opsi | Isi |
|---|---|
| A | 4 |
| B | -1 |
| C | 11 |
| D | -5 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `74fd6d86177e9c021d86a9170d6f6f107bf4c0baabd4e4a33cd540996bb3d043`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $\begin{pmatrix} 3a - 2 & 0 \\ 4 & b + 6 \end{pmatrix} = \begin{pmatrix} 10 & 0 \\ 4 & 1 \end{pmatrix}$. Nilai $a + b$ adalah ....
Pilihan: A. 4
B. -1
C. 11
D. -5
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 55. Soal `09c97736acaddc80f095bee7`

Diketahui $P = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$ dan $Q = \begin{pmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{pmatrix}$. Pernyataan yang benar adalah ....

| Opsi | Isi |
|---|---|
| A | $P = Q$ karena kedua matriks mempunyai 6 elemen |
| B | $P = Q$ karena kedua matriks memuat elemen 1, 2, 3, 4, 5, 6 |
| C | $P \neq Q$ karena ordo kedua matriks berbeda |
| D | $P \neq Q$ karena elemen pada baris ke-1 kolom ke-1 berbeda |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `190c41580ed4fdfa18a3795b45cf1eed64cbb50f020b6859ef9fdd1461ee6323`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $P = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$ dan $Q = \begin{pmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{pmatrix}$. Pernyataan yang benar adalah ....
Pilihan: A. $P = Q$ karena kedua matriks mempunyai 6 elemen
B. $P = Q$ karena kedua matriks memuat elemen 1, 2, 3, 4, 5, 6
C. $P \neq Q$ karena ordo kedua matriks berbeda
D. $P \neq Q$ karena elemen pada baris ke-1 kolom ke-1 berbeda
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 56. Soal `39d640fba381e3bfd9aa10ca`

Diketahui $\begin{pmatrix} m^2 & 1 \\ 0 & 5 \end{pmatrix} = \begin{pmatrix} 16 & 1 \\ 0 & 5 \end{pmatrix}$ dengan $m > 0$. Nilai $m$ adalah ....

| Opsi | Isi |
|---|---|
| A | 256 |
| B | 8 |
| C | -4 |
| D | 4 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `71fbff8e11a3d9895e11b8d6240964503a6899d0f89b7f297f2d160e75355c1b`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $\begin{pmatrix} m^2 & 1 \\ 0 & 5 \end{pmatrix} = \begin{pmatrix} 16 & 1 \\ 0 & 5 \end{pmatrix}$ dengan $m > 0$. Nilai $m$ adalah ....
Pilihan: A. 256
B. 8
C. -4
D. 4
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 57. Soal `10217db979eec78126d66dfb`

Matriks $\begin{pmatrix} a - 3 & 2b \\ c + 5 & d \end{pmatrix}$ sama dengan matriks nol berordo $2 \times 2$. Nilai $a + b + c + d$ adalah ....

| Opsi | Isi |
|---|---|
| A | -2 |
| B | 8 |
| C | 3 |
| D | -5 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `647a96a986d3f18a620c3a51b5c9b019cf9557d6ce5785fc37ba28df793a8117`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $\begin{pmatrix} a - 3 & 2b \\ c + 5 & d \end{pmatrix}$ sama dengan matriks nol berordo $2 \times 2$. Nilai $a + b + c + d$ adalah ....
Pilihan: A. -2
B. 8
C. 3
D. -5
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 58. Soal `fa79b7a7dce172280923bcea`

Diketahui $A = \begin{pmatrix} 1 & x \\ y & 4 \end{pmatrix}$ dan $B = \begin{pmatrix} 1 & 8 \\ 3 & 4 \end{pmatrix}$. Jika $A = B$, nilai $x - y$ adalah ....

| Opsi | Isi |
|---|---|
| A | 24 |
| B | -5 |
| C | 11 |
| D | 5 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `97e4c079884c1f49d71ded43d5fe835a402514d25886b63c05094b28504e4d97`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix} 1 & x \\ y & 4 \end{pmatrix}$ dan $B = \begin{pmatrix} 1 & 8 \\ 3 & 4 \end{pmatrix}$. Jika $A = B$, nilai $x - y$ adalah ....
Pilihan: A. 24
B. -5
C. 11
D. 5
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 59. Soal `5e715abd353c1681ff06d9eb`

Matriks $A = (a_{ij})$ dan $B = (b_{ij})$ berordo sama. Syarat kedua agar $A = B$ adalah ....

| Opsi | Isi |
|---|---|
| A | $a_{11} = b_{11}$ saja |
| B | $a_{ij} = b_{ij}$ untuk semua $i$ dan $j$ |
| C | jumlah semua $a_{ij}$ sama dengan jumlah semua $b_{ij}$ |
| D | $a_{ij} = b_{ji}$ untuk semua $i$ dan $j$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2973893787d4081ddd0f85f4ad3bad763501117d1227aa49ee79f915ba6bfa33`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A = (a_{ij})$ dan $B = (b_{ij})$ berordo sama. Syarat kedua agar $A = B$ adalah ....
Pilihan: A. $a_{11} = b_{11}$ saja
B. $a_{ij} = b_{ij}$ untuk semua $i$ dan $j$
C. jumlah semua $a_{ij}$ sama dengan jumlah semua $b_{ij}$
D. $a_{ij} = b_{ji}$ untuk semua $i$ dan $j$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 60. Soal `e038c81d3fc94ed9199942b6`

Agar matriks $P$ dan matriks $Q$ dapat dikatakan sama, syarat pertama yang harus dipenuhi adalah ....

| Opsi | Isi |
|---|---|
| A | keduanya berordo sama |
| B | keduanya mempunyai determinan yang sama |
| C | keduanya matriks persegi |
| D | hanya baris pertama keduanya yang sama |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d0a6486aca0b616f8afb20103f4a660c4344d596f8f75618fbe77b96512cfaeb`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Agar matriks $P$ dan matriks $Q$ dapat dikatakan sama, syarat pertama yang harus dipenuhi adalah ....
Pilihan: A. keduanya berordo sama
B. keduanya mempunyai determinan yang sama
C. keduanya matriks persegi
D. hanya baris pertama keduanya yang sama
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 61. Soal `e4d5925780a44ba16bdeba95`

Matriks $A$ berordo $2 \times 4$. Jika $A = B$, maka ordo matriks $B$ adalah ....

| Opsi | Isi |
|---|---|
| A | $2 \times 4$ |
| B | $8 \times 1$ |
| C | $4 \times 2$ |
| D | $2 \times 2$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `12c05ac095a2a2957920113d62afc5cb9104c31a2adb35e40080388ee5da9dda`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$ berordo $2 \times 4$. Jika $A = B$, maka ordo matriks $B$ adalah ....
Pilihan: A. $2 \times 4$
B. $8 \times 1$
C. $4 \times 2$
D. $2 \times 2$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 62. Soal `17ca69c0a7bff461c194c489`

Diketahui matriks $K = \begin{pmatrix} 3p & 7 \\ -q & 5 \end{pmatrix}$ dan $L = \begin{pmatrix} 12 & 7 \\ 6 & 5 \end{pmatrix}$. Jika matriks $K$ sama dengan matriks $L$, nilai $p$ dan $q$ berturut-turut adalah ....

| Opsi | Isi |
|---|---|
| A | $p = 9$ dan $q = -6$ |
| B | $p = 4$ dan $q = 6$ |
| C | $p = 36$ dan $q = -6$ |
| D | $p = 4$ dan $q = -6$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a196ffe8ed7cb6eb33b34c3257e8504b5df8a1511282cafe2ea1f2a3b9fa544e`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui matriks $K = \begin{pmatrix} 3p & 7 \\ -q & 5 \end{pmatrix}$ dan $L = \begin{pmatrix} 12 & 7 \\ 6 & 5 \end{pmatrix}$. Jika matriks $K$ sama dengan matriks $L$, nilai $p$ dan $q$ berturut-turut adalah ....
Pilihan: A. $p = 9$ dan $q = -6$
B. $p = 4$ dan $q = 6$
C. $p = 36$ dan $q = -6$
D. $p = 4$ dan $q = -6$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 63. Soal `a63e7fa49d1f86d99b455e2f`

Diketahui matriks $K = \begin{pmatrix} -r & 4 \\ 2s & t^2 \end{pmatrix}$ dan $L = \begin{pmatrix} -8 & 4 \\ 10 & 49 \end{pmatrix}$. Jika matriks $K$ sama dengan matriks $L$ dan $t > 0$, nilai $r$, $s$, dan $t$ berturut-turut adalah ....

| Opsi | Isi |
|---|---|
| A | $r = 8$, $s = 5$, $t = \frac{49}{2}$ |
| B | $r = 8$, $s = 20$, $t = 7$ |
| C | $r = -8$, $s = 5$, $t = 7$ |
| D | $r = 8$, $s = 5$, $t = 7$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a8228affc01ebf8a55b38cc9eb26a5517d7882f4a9d5a7388c38a8959beff98f`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui matriks $K = \begin{pmatrix} -r & 4 \\ 2s & t^2 \end{pmatrix}$ dan $L = \begin{pmatrix} -8 & 4 \\ 10 & 49 \end{pmatrix}$. Jika matriks $K$ sama dengan matriks $L$ dan $t > 0$, nilai $r$, $s$, dan $t$ berturut-turut adalah ....
Pilihan: A. $r = 8$, $s = 5$, $t = \frac{49}{2}$
B. $r = 8$, $s = 20$, $t = 7$
C. $r = -8$, $s = 5$, $t = 7$
D. $r = 8$, $s = 5$, $t = 7$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 64. Soal `b830f84a5b8f0c45fefd07c8`

Diketahui matriks $A = \begin{pmatrix} c & 2a \\ b + 4 & 9 \end{pmatrix}$ dan $B = \begin{pmatrix} 5 & 10 \\ 1 & d \end{pmatrix}$. Jika matriks $A$ sama dengan matriks $B$, nilai $a + b + c + d$ adalah ....

| Opsi | Isi |
|---|---|
| A | 22 |
| B | 16 |
| C | 24 |
| D | 21 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `add61907448b2abcc4ef4d090f6de43420b54ab02941eb750e2e5d1279a04bf1`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui matriks $A = \begin{pmatrix} c & 2a \\ b + 4 & 9 \end{pmatrix}$ dan $B = \begin{pmatrix} 5 & 10 \\ 1 & d \end{pmatrix}$. Jika matriks $A$ sama dengan matriks $B$, nilai $a + b + c + d$ adalah ....
Pilihan: A. 22
B. 16
C. 24
D. 21
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 65. Soal `32a89f524008bc9ab53b8de0`

Hitunglah nilai $a + b + c + d$ yang memenuhi kesamaan matriks berikut. $\begin{pmatrix} 4a & b + 8 \\ c - 6 & 3d \end{pmatrix} = \begin{pmatrix} 20 & 15 \\ 2 & 21 \end{pmatrix}$

| Opsi | Isi |
|---|---|
| A | 83 |
| B | 27 |
| C | 15 |
| D | 43 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6a61615bec41b39c91a1f9e7acff6aa717e27f8c0a97d0f64ea057b6bfb79054`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Hitunglah nilai $a + b + c + d$ yang memenuhi kesamaan matriks berikut. $\begin{pmatrix} 4a & b + 8 \\ c - 6 & 3d \end{pmatrix} = \begin{pmatrix} 20 & 15 \\ 2 & 21 \end{pmatrix}$
Pilihan: A. 83
B. 27
C. 15
D. 43
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 66. Soal `b911164ca435722f40bbcf64`

Jika $A = \begin{pmatrix} 4x - 3 & y + 5 \\ z - 9 & 6w - 5 \end{pmatrix}$ dan $I$ adalah matriks identitas berordo $2 \times 2$ dengan $A = I$, tentukan nilai $x + y + z + w$.

| Opsi | Isi |
|---|---|
| A | 16 |
| B | -12 |
| C | 6 |
| D | 8 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `cfcc94696e14f09d299729736f0bddd7344f87b31e363d583f0837eddc76a37a`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika $A = \begin{pmatrix} 4x - 3 & y + 5 \\ z - 9 & 6w - 5 \end{pmatrix}$ dan $I$ adalah matriks identitas berordo $2 \times 2$ dengan $A = I$, tentukan nilai $x + y + z + w$.
Pilihan: A. 16
B. -12
C. 6
D. 8
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 67. Soal `2c74a1d15652c99da26bdb68`

Hitunglah nilai $p + q + r$ yang memenuhi kesamaan matriks berikut. $\begin{pmatrix} 3p & q - 5 & r + 2 \end{pmatrix} = \begin{pmatrix} 18 & 4 & 9 \end{pmatrix}$

| Opsi | Isi |
|---|---|
| A | 22 |
| B | 70 |
| C | 12 |
| D | 26 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d9c2a2a62ba3f2245590cc7fa39ba2d31015eda8e64d07a9a56d4567b3e0ad29`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Hitunglah nilai $p + q + r$ yang memenuhi kesamaan matriks berikut. $\begin{pmatrix} 3p & q - 5 & r + 2 \end{pmatrix} = \begin{pmatrix} 18 & 4 & 9 \end{pmatrix}$
Pilihan: A. 22
B. 70
C. 12
D. 26
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 68. Soal `96d284295734e859afa8e490`

Diketahui matriks $A = \begin{pmatrix} 2p \\ q + 1 \\ r - 3 \end{pmatrix}$ dan $B = \begin{pmatrix} 8 \\ 0 \\ 5 \end{pmatrix}$. Jika matriks $A$ sama dengan matriks $B$, nilai $p + q + r$ adalah ....

| Opsi | Isi |
|---|---|
| A | 13 |
| B | 11 |
| C | 5 |
| D | 23 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `79029c701b7fe6348fed186680b4064d54630ec2e860265b6dc0aa326f1bff37`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui matriks $A = \begin{pmatrix} 2p \\ q + 1 \\ r - 3 \end{pmatrix}$ dan $B = \begin{pmatrix} 8 \\ 0 \\ 5 \end{pmatrix}$. Jika matriks $A$ sama dengan matriks $B$, nilai $p + q + r$ adalah ....
Pilihan: A. 13
B. 11
C. 5
D. 23
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 69. Soal `17bfb7edae810c2928de0d0a`

Matriks $G$ dan matriks $H$ keduanya berordo $3 \times 5$ dan $G = H$. Banyak persamaan yang terbentuk dari kesamaan elemen-elemen seletak $G$ dan $H$ adalah ....

| Opsi | Isi |
|---|---|
| A | 5 |
| B | 8 |
| C | 15 |
| D | 3 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `93e8579f16ec9a320958f1b70b8100731a024f54c6366caa5038b877105d7874`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $G$ dan matriks $H$ keduanya berordo $3 \times 5$ dan $G = H$. Banyak persamaan yang terbentuk dari kesamaan elemen-elemen seletak $G$ dan $H$ adalah ....
Pilihan: A. 5
B. 8
C. 15
D. 3
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 70. Soal `973227fe268b6fb932cd2779`

Diketahui $\begin{pmatrix} x + 1 & 2y \end{pmatrix} = \begin{pmatrix} 6 & -8 \end{pmatrix}$. Nilai $xy$ adalah ....

| Opsi | Isi |
|---|---|
| A | -80 |
| B | 20 |
| C | -20 |
| D | -28 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7f335f305b406f228ac5f57381ee3aa27d40dc2b8ac5e39bce4ef481304223b2`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $\begin{pmatrix} x + 1 & 2y \end{pmatrix} = \begin{pmatrix} 6 & -8 \end{pmatrix}$. Nilai $xy$ adalah ....
Pilihan: A. -80
B. 20
C. -20
D. -28
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 71. Soal `24bda618cd190d8a40b10dbe`

Diketahui $A = \begin{pmatrix} 1 & 4 \\ 3 & 2 \end{pmatrix}$ dan $B = \begin{pmatrix} 1 & 3 \\ 4 & 2 \end{pmatrix}$. Seorang siswa berpendapat bahwa $A = B$ karena kedua matriks berordo sama dan jumlah semua elemennya sama. Pernyataan yang benar mengenai pendapat tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $A \neq B$, sebab $a_{12} = 4$ berbeda dengan $b_{12} = 3$ walaupun ordo dan jumlah semua elemennya sama |
| B | $A = B$, sebab kedua matriks memuat elemen-elemen yang sama dan hanya urutannya berbeda |
| C | $A = B$, sebab ordo sama dan jumlah semua elemen sama ($10$) |
| D | $A \neq B$, sebab ordo $A$ berbeda dengan ordo $B$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `621d6e156b1f42d4ccf75e38fe2d292dd11cca54b7bef21657e0e277cfadd09a`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix} 1 & 4 \\ 3 & 2 \end{pmatrix}$ dan $B = \begin{pmatrix} 1 & 3 \\ 4 & 2 \end{pmatrix}$. Seorang siswa berpendapat bahwa $A = B$ karena kedua matriks berordo sama dan jumlah semua elemennya sama. Pernyataan yang benar mengenai pendapat tersebut adalah ....
Pilihan: A. $A \neq B$, sebab $a_{12} = 4$ berbeda dengan $b_{12} = 3$ walaupun ordo dan jumlah semua elemennya sama
B. $A = B$, sebab kedua matriks memuat elemen-elemen yang sama dan hanya urutannya berbeda
C. $A = B$, sebab ordo sama dan jumlah semua elemen sama ($10$)
D. $A \neq B$, sebab ordo $A$ berbeda dengan ordo $B$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 72. Soal `d556f2f0db5b137047827c0b`

Klaim: "Jika dua matriks berordo sama dan jumlah semua elemennya sama, maka kedua matriks itu sama." Pasangan matriks yang merupakan contoh penyangkal klaim tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix} 5 & 2 \\ 7 & 6 \end{pmatrix}$ dan $\begin{pmatrix} 5 & 2 & 7 & 6 \end{pmatrix}$ |
| B | $\begin{pmatrix} 5 & 2 \\ 7 & 6 \end{pmatrix}$ dan $\begin{pmatrix} 6 & 7 \\ 2 & 5 \end{pmatrix}$ |
| C | $\begin{pmatrix} 5 & 2 \\ 7 & 6 \end{pmatrix}$ dan $\begin{pmatrix} 5 & 2 \\ 7 & 6 \end{pmatrix}$ |
| D | $\begin{pmatrix} 5 & 2 \\ 7 & 6 \end{pmatrix}$ dan $\begin{pmatrix} 5 & 2 \\ 7 & 7 \end{pmatrix}$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0b8d6ef93b26637c2838dafc46ee786b4c95547e8037dbcde0cdd01aff3b31f7`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Klaim: "Jika dua matriks berordo sama dan jumlah semua elemennya sama, maka kedua matriks itu sama." Pasangan matriks yang merupakan contoh penyangkal klaim tersebut adalah ....
Pilihan: A. $\begin{pmatrix} 5 & 2 \\ 7 & 6 \end{pmatrix}$ dan $\begin{pmatrix} 5 & 2 & 7 & 6 \end{pmatrix}$
B. $\begin{pmatrix} 5 & 2 \\ 7 & 6 \end{pmatrix}$ dan $\begin{pmatrix} 6 & 7 \\ 2 & 5 \end{pmatrix}$
C. $\begin{pmatrix} 5 & 2 \\ 7 & 6 \end{pmatrix}$ dan $\begin{pmatrix} 5 & 2 \\ 7 & 6 \end{pmatrix}$
D. $\begin{pmatrix} 5 & 2 \\ 7 & 6 \end{pmatrix}$ dan $\begin{pmatrix} 5 & 2 \\ 7 & 7 \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 73. Soal `d55d0c75a31c075f9d2e6aed`

Seorang siswa menyimpulkan $A = B$ untuk $A = \begin{pmatrix} 3 & 1 & 4 \\ 2 & 5 & 6 \end{pmatrix}$ dan $B = \begin{pmatrix} 3 & 2 \\ 1 & 5 \\ 4 & 6 \end{pmatrix}$ dengan alasan keenam elemennya sama. Pernyataan yang benar mengenai kesimpulan siswa itu adalah ....

| Opsi | Isi |
|---|---|
| A | salah, sebab $A$ berordo $2 \times 3$ sedangkan $B$ berordo $3 \times 2$ sehingga syarat ordo yang sama tidak terpenuhi |
| B | salah, sebab elemen $1$ dan $2$ seharusnya diurutkan menaik pada $B$ |
| C | benar, sebab banyak elemen kedua matriks sama yaitu $6$ |
| D | benar, sebab kedua matriks memuat elemen yang sama persis |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['menyimpulkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f3fdff872219d87578ca80560241237f1dc0f735046f9c834f6a25c732eb7754`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Seorang siswa menyimpulkan $A = B$ untuk $A = \begin{pmatrix} 3 & 1 & 4 \\ 2 & 5 & 6 \end{pmatrix}$ dan $B = \begin{pmatrix} 3 & 2 \\ 1 & 5 \\ 4 & 6 \end{pmatrix}$ dengan alasan keenam elemennya sama. Pernyataan yang benar mengenai kesimpulan siswa itu adalah ....
Pilihan: A. salah, sebab $A$ berordo $2 \times 3$ sedangkan $B$ berordo $3 \times 2$ sehingga syarat ordo yang sama tidak terpenuhi
B. salah, sebab elemen $1$ dan $2$ seharusnya diurutkan menaik pada $B$
C. benar, sebab banyak elemen kedua matriks sama yaitu $6$
D. benar, sebab kedua matriks memuat elemen yang sama persis
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 74. Soal `6b6e8f617881ec459f4adac3`

Matriks $A$ berordo $(p + 1) \times (2p - 1)$ dan $B = \begin{pmatrix} 4 & 1 & 7 \\ 2 & 9 & 5 \end{pmatrix}$. Pernyataan yang benar mengenai nilai $p$ agar $A = B$ adalah ....

| Opsi | Isi |
|---|---|
| A | $p = 2$, sebab banyak kolom sudah sama |
| B | $p = 1$, sebab banyak baris sudah sama |
| C | $p = 3$, sebab $p + 1 = 4$ dan $2p - 1 = 5$ jika dijumlahkan menghasilkan ordo yang cocok |
| D | tidak ada $p$ yang memenuhi, sebab banyak baris menuntut $p = 1$ sedangkan banyak kolom menuntut $p = 2$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f1fc1716faea302919356586fa8fe002f60cc2edb06b022cdb5f075d27a54c59`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$ berordo $(p + 1) \times (2p - 1)$ dan $B = \begin{pmatrix} 4 & 1 & 7 \\ 2 & 9 & 5 \end{pmatrix}$. Pernyataan yang benar mengenai nilai $p$ agar $A = B$ adalah ....
Pilihan: A. $p = 2$, sebab banyak kolom sudah sama
B. $p = 1$, sebab banyak baris sudah sama
C. $p = 3$, sebab $p + 1 = 4$ dan $2p - 1 = 5$ jika dijumlahkan menghasilkan ordo yang cocok
D. tidak ada $p$ yang memenuhi, sebab banyak baris menuntut $p = 1$ sedangkan banyak kolom menuntut $p = 2$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 75. Soal `a4041cf4558f736f8c9f35e3`

Diketahui $A = \begin{pmatrix} x & 2 \\ 3 & y \end{pmatrix}$ dan $B = \begin{pmatrix} y & 2 \\ 3 & x \end{pmatrix}$ dengan $x$ dan $y$ bilangan real. Pernyataan yang benar adalah ....

| Opsi | Isi |
|---|---|
| A | $A = B$ tepat ketika $x = y$ |
| B | $A \neq B$ untuk semua bilangan real $x$ dan $y$ |
| C | $A = B$ untuk semua bilangan real $x$ dan $y$ |
| D | $A = B$ hanya jika $x = y = 2$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0ab0bea9dd08f1e67af550a4259bc323ecf6aefc4c184bc55f4d7fd4d564aae8`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix} x & 2 \\ 3 & y \end{pmatrix}$ dan $B = \begin{pmatrix} y & 2 \\ 3 & x \end{pmatrix}$ dengan $x$ dan $y$ bilangan real. Pernyataan yang benar adalah ....
Pilihan: A. $A = B$ tepat ketika $x = y$
B. $A \neq B$ untuk semua bilangan real $x$ dan $y$
C. $A = B$ untuk semua bilangan real $x$ dan $y$
D. $A = B$ hanya jika $x = y = 2$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 76. Soal `716478021c5bca651c4aab9f`

Diketahui $A = \begin{pmatrix} k^2 & 7 \\ 3 & 4k \end{pmatrix}$ dan $B = \begin{pmatrix} 5k & 7 \\ 3 & 4k \end{pmatrix}$. Banyak nilai real $k$ yang membuat $A = B$ adalah ....

| Opsi | Isi |
|---|---|
| A | $3$ |
| B | $1$ |
| C | $4$ |
| D | $2$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `02e92daebcbe742b6a288020de476fe9a57c3711e81450845ff806265cce97d3`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix} k^2 & 7 \\ 3 & 4k \end{pmatrix}$ dan $B = \begin{pmatrix} 5k & 7 \\ 3 & 4k \end{pmatrix}$. Banyak nilai real $k$ yang membuat $A = B$ adalah ....
Pilihan: A. $3$
B. $1$
C. $4$
D. $2$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 77. Soal `28779783aa142ae04efb5b4f`

Diketahui $A = \begin{pmatrix} x^2 - 4 & y \\ 0 & 5 \end{pmatrix}$ dan $B = \begin{pmatrix} 0 & y^3 \\ 0 & 5 \end{pmatrix}$. Banyak pasangan terurut $(x, y)$ bilangan real yang membuat $A = B$ adalah ....

| Opsi | Isi |
|---|---|
| A | $2$ |
| B | $5$ |
| C | $6$ |
| D | $3$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a224aa6030f609b6b9aee3a03603b9bc3e2806b09414548aac72badc19026858`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix} x^2 - 4 & y \\ 0 & 5 \end{pmatrix}$ dan $B = \begin{pmatrix} 0 & y^3 \\ 0 & 5 \end{pmatrix}$. Banyak pasangan terurut $(x, y)$ bilangan real yang membuat $A = B$ adalah ....
Pilihan: A. $2$
B. $5$
C. $6$
D. $3$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 78. Soal `3267d05fe51063e08dd14395`

Matriks $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ dengan $a, b, c, d \in \{1, 2, 3\}$ dan $N = \begin{pmatrix} b & a \\ d & c \end{pmatrix}$. Banyak matriks $M$ yang memenuhi $M = N$ adalah ....

| Opsi | Isi |
|---|---|
| A | $6$ |
| B | $9$ |
| C | $27$ |
| D | $3$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `46dadfd326811d59b644bc2b4f93fcddbe374a252f43968f3026a31365483967`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ dengan $a, b, c, d \in \{1, 2, 3\}$ dan $N = \begin{pmatrix} b & a \\ d & c \end{pmatrix}$. Banyak matriks $M$ yang memenuhi $M = N$ adalah ....
Pilihan: A. $6$
B. $9$
C. $27$
D. $3$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 79. Soal `d9b78a43a58c6d8f75d2fb4d`

Diketahui $A = \begin{pmatrix} 2a & b \\ 4 & c + 1 \end{pmatrix}$, $B = \begin{pmatrix} p & 5 \\ d & 9 \end{pmatrix}$, dan $C = \begin{pmatrix} 6 & q - 1 \\ 4 & r \end{pmatrix}$. Jika $A = B$ dan $B = C$, nilai $a + b + c + q + r$ adalah ....

| Opsi | Isi |
|---|---|
| A | $22$ |
| B | $34$ |
| C | $31$ |
| D | $30$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7e1baceefb99fe311bbe53d8d5b7e178021624ca53f92ce98204af09b8f2c340`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix} 2a & b \\ 4 & c + 1 \end{pmatrix}$, $B = \begin{pmatrix} p & 5 \\ d & 9 \end{pmatrix}$, dan $C = \begin{pmatrix} 6 & q - 1 \\ 4 & r \end{pmatrix}$. Jika $A = B$ dan $B = C$, nilai $a + b + c + q + r$ adalah ....
Pilihan: A. $22$
B. $34$
C. $31$
D. $30$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 80. Soal `1d939cc68f5db2045612bcd9`

Matriks $\begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} b + 1 & c + 1 \\ d + 1 & 2 \end{pmatrix}$ dengan $a, b, c, d$ bilangan real. Nilai $a + b + c + d$ adalah ....

| Opsi | Isi |
|---|---|
| A | $11$ |
| B | $14$ |
| C | $10$ |
| D | $120$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c81524150b6ecc98a414aae1ae13a5dd0b3be385cfc3c8fa43e333fd7545d288`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $\begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} b + 1 & c + 1 \\ d + 1 & 2 \end{pmatrix}$ dengan $a, b, c, d$ bilangan real. Nilai $a + b + c + d$ adalah ....
Pilihan: A. $11$
B. $14$
C. $10$
D. $120$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 81. Soal `f7e557ac354726bf988d53ee`

Hitunglah nilai $a + b + c + d$ yang memenuhi kesamaan matriks berikut. $\begin{pmatrix} a + 4b & 3a + b \\ c + 3d & 2c + d \end{pmatrix} = \begin{pmatrix} -4 & 10 \\ 15 & 0 \end{pmatrix}$

| Opsi | Isi |
|---|---|
| A | -7 |
| B | 11 |
| C | 9 |
| D | 5 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `bbb4b91506b2b0badad316afd02e0d4b3dfe993d9255961d629f54482a76df72`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Hitunglah nilai $a + b + c + d$ yang memenuhi kesamaan matriks berikut. $\begin{pmatrix} a + 4b & 3a + b \\ c + 3d & 2c + d \end{pmatrix} = \begin{pmatrix} -4 & 10 \\ 15 & 0 \end{pmatrix}$
Pilihan: A. -7
B. 11
C. 9
D. 5
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 82. Soal `b2a3ff4e2fca977be49a4b9a`

Tentukan nilai $ab + cd$ yang memenuhi kesamaan matriks berikut. $\begin{pmatrix} 2a - b & a + b \\ 3c + d & c - d \end{pmatrix} = \begin{pmatrix} 6 & 9 \\ -13 & 5 \end{pmatrix}$

| Opsi | Isi |
|---|---|
| A | 34 |
| B | 0 |
| C | 20 |
| D | 6 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9a61141115f02acc2e835438589d3adf7d08eb84d001284d00269f339cba6c43`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan nilai $ab + cd$ yang memenuhi kesamaan matriks berikut. $\begin{pmatrix} 2a - b & a + b \\ 3c + d & c - d \end{pmatrix} = \begin{pmatrix} 6 & 9 \\ -13 & 5 \end{pmatrix}$
Pilihan: A. 34
B. 0
C. 20
D. 6
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 83. Soal `fe1f95d21fc92c95b8997ec7`

Jika $A = \begin{pmatrix} 9x - y & 0 \\ (4x - y)^2 & 1 \end{pmatrix}$ dan $I$ adalah matriks identitas yang seordo dengan $A$. Jika $A = I$, tentukan nilai $x + 5y$.

| Opsi | Isi |
|---|---|
| A | $4$ |
| B | $\frac{9}{35}$ |
| C | $\frac{21}{13}$ |
| D | $\frac{21}{5}$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2b0e16e58e01f5856eda6c7848ef83ee2e3fca921f9692debc7f5f65630b8aed`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika $A = \begin{pmatrix} 9x - y & 0 \\ (4x - y)^2 & 1 \end{pmatrix}$ dan $I$ adalah matriks identitas yang seordo dengan $A$. Jika $A = I$, tentukan nilai $x + 5y$.
Pilihan: A. $4$
B. $\frac{9}{35}$
C. $\frac{21}{13}$
D. $\frac{21}{5}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 84. Soal `b58c8bfed062075a8c719c74`

Jika $A = \begin{pmatrix} 2x + y & (x - 4y)^2 \\ 0 & x + 5y \end{pmatrix}$ dan $I$ adalah matriks identitas berordo $2 \times 2$ dengan $A = I$, tentukan nilai $5x - y$.

| Opsi | Isi |
|---|---|
| A | $\frac{19}{9}$ |
| B | $\frac{19}{7}$ |
| C | $\frac{1}{6}$ |
| D | $\frac{20}{9}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `03847e745b76f8cbbec649a1a458a5db96726137182e3c3660eabdd9ee81e528`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika $A = \begin{pmatrix} 2x + y & (x - 4y)^2 \\ 0 & x + 5y \end{pmatrix}$ dan $I$ adalah matriks identitas berordo $2 \times 2$ dengan $A = I$, tentukan nilai $5x - y$.
Pilihan: A. $\frac{19}{9}$
B. $\frac{19}{7}$
C. $\frac{1}{6}$
D. $\frac{20}{9}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 85. Soal `1574a3f4ff257f54c670c63f`

Matriks $K = \begin{pmatrix} 3x - 1 & 4 \\ -y & z^2 \end{pmatrix}$ dan $L = \begin{pmatrix} 8 & 4 \\ 5 & 36 \end{pmatrix}$ memenuhi $K = L$. Nilai terkecil yang mungkin bagi $x + y + z$ adalah ....

| Opsi | Isi |
|---|---|
| A | 4 |
| B | -8 |
| C | 14 |
| D | 2 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b62f5ad3739236f0368b3f5f86883ed60cea6fc23759104824bdf9d34d32830a`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $K = \begin{pmatrix} 3x - 1 & 4 \\ -y & z^2 \end{pmatrix}$ dan $L = \begin{pmatrix} 8 & 4 \\ 5 & 36 \end{pmatrix}$ memenuhi $K = L$. Nilai terkecil yang mungkin bagi $x + y + z$ adalah ....
Pilihan: A. 4
B. -8
C. 14
D. 2
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 86. Soal `c982cc24bbc1c48f949e7fcd`

Diketahui $P = \begin{pmatrix} (m - 2)^2 & 5 \\ 2n & 1 \end{pmatrix}$ dan $Q = \begin{pmatrix} 49 & 5 \\ -6 & 1 \end{pmatrix}$. Jika $P = Q$, nilai terbesar yang mungkin bagi $m + n$ adalah ....

| Opsi | Isi |
|---|---|
| A | 6 |
| B | 12 |
| C | 4 |
| D | -8 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d65fedbf34547ea360ae14f26f38d6656dc39aaccf90cec8362a27fce48201ea`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $P = \begin{pmatrix} (m - 2)^2 & 5 \\ 2n & 1 \end{pmatrix}$ dan $Q = \begin{pmatrix} 49 & 5 \\ -6 & 1 \end{pmatrix}$. Jika $P = Q$, nilai terbesar yang mungkin bagi $m + n$ adalah ....
Pilihan: A. 6
B. 12
C. 4
D. -8
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 87. Soal `d9723536e84906d75781ac41`

Diketahui $A = \begin{pmatrix} 2a - 3 & b + 1 \\ c & 2d \end{pmatrix}$ dan $B = \begin{pmatrix} a + 4 & 2b - 3 \\ 3 & d + 6 \end{pmatrix}$. Jika $A = B$, nilai $a + b + c + d$ adalah ....

| Opsi | Isi |
|---|---|
| A | 18 |
| B | 20 |
| C | 17 |
| D | 14 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `534e14f2bd4770e843e551ae05f878e60be38bbc8d882168c0299ddec7412537`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix} 2a - 3 & b + 1 \\ c & 2d \end{pmatrix}$ dan $B = \begin{pmatrix} a + 4 & 2b - 3 \\ 3 & d + 6 \end{pmatrix}$. Jika $A = B$, nilai $a + b + c + d$ adalah ....
Pilihan: A. 18
B. 20
C. 17
D. 14
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 88. Soal `6bae76f6cfd6d110262ba823`

Diketahui $A = \begin{pmatrix} p + q \\ p - q \\ 2r - 1 \end{pmatrix}$ dan $B = \begin{pmatrix} 10 \\ 4 \\ -7 \end{pmatrix}$. Jika $A = B$, nilai $pq + r$ adalah ....

| Opsi | Isi |
|---|---|
| A | 24 |
| B | 21 |
| C | 18 |
| D | 7 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2f850fa7708b4dfcf538580b927120f0fb85228777c44342532b779e0877bc11`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix} p + q \\ p - q \\ 2r - 1 \end{pmatrix}$ dan $B = \begin{pmatrix} 10 \\ 4 \\ -7 \end{pmatrix}$. Jika $A = B$, nilai $pq + r$ adalah ....
Pilihan: A. 24
B. 21
C. 18
D. 7
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 89. Soal `b8e826349fd93a429a7c8fde`

Diketahui $\begin{pmatrix} 2x + y & 3 \\ 5 & x - y \end{pmatrix} = \begin{pmatrix} 11 & 3 \\ 5 & 1 \end{pmatrix}$. Nilai $x^2 + y^2$ adalah ....

| Opsi | Isi |
|---|---|
| A | 49 |
| B | 12 |
| C | 25 |
| D | 7 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5e012cc726bb31f4427993e8cb47a0ad19f3a45fdfeb508857a1835f22840f48`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $\begin{pmatrix} 2x + y & 3 \\ 5 & x - y \end{pmatrix} = \begin{pmatrix} 11 & 3 \\ 5 & 1 \end{pmatrix}$. Nilai $x^2 + y^2$ adalah ....
Pilihan: A. 49
B. 12
C. 25
D. 7
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 90. Soal `b7101ef62d352e1883d3f07b`

Transpos matriks $B$, ditulis $B^T$, adalah matriks yang diperoleh dengan menukar baris menjadi kolom. Diketahui $A = \begin{pmatrix} 2a & 5 \\ b - 1 & 7 \end{pmatrix}$ dan $B = \begin{pmatrix} 6 & 9 \\ 5 & 7 \end{pmatrix}$. Jika $A = B^T$, nilai $a + b$ adalah ....

| Opsi | Isi |
|---|---|
| A | 12 |
| B | 13 |
| C | 9 |
| D | 11 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9d91c6071ea78477e06630fea52a38de69a1a71928d16f6922df01d91fa06382`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Transpos matriks $B$, ditulis $B^T$, adalah matriks yang diperoleh dengan menukar baris menjadi kolom. Diketahui $A = \begin{pmatrix} 2a & 5 \\ b - 1 & 7 \end{pmatrix}$ dan $B = \begin{pmatrix} 6 & 9 \\ 5 & 7 \end{pmatrix}$. Jika $A = B^T$, nilai $a + b$ adalah ....
Pilihan: A. 12
B. 13
C. 9
D. 11
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 91. Soal `2b731c8bb8954652aeca56fb`

Nilai $k$ agar $\begin{pmatrix} 2k - 1 & 7 \\ 0 & k^2 \end{pmatrix} = \begin{pmatrix} 9 & 7 \\ 0 & 25 \end{pmatrix}$ adalah ....

| Opsi | Isi |
|---|---|
| A | -5 |
| B | 5 |
| C | 4 |
| D | 10 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e9c4ca45c141ce5bb0c2a3c0ec4607c6be58b5b495e590392adc3c43d1f9dc7e`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Nilai $k$ agar $\begin{pmatrix} 2k - 1 & 7 \\ 0 & k^2 \end{pmatrix} = \begin{pmatrix} 9 & 7 \\ 0 & 25 \end{pmatrix}$ adalah ....
Pilihan: A. -5
B. 5
C. 4
D. 10
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 92. Soal `fe10b8133938d0716454d0cd`

Diketahui $\begin{pmatrix} k^2 - 5k & 3 \\ 0 & k \end{pmatrix} = \begin{pmatrix} -6 & 3 \\ 0 & 2 \end{pmatrix}$. Nilai $k$ yang memenuhi kesamaan tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | 3 |
| B | 2 |
| C | -2 |
| D | 6 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b65f38b00017fead4f38a5bc50f558f38e76c218811809accf4a5ce6fabf9cb6`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $\begin{pmatrix} k^2 - 5k & 3 \\ 0 & k \end{pmatrix} = \begin{pmatrix} -6 & 3 \\ 0 & 2 \end{pmatrix}$. Nilai $k$ yang memenuhi kesamaan tersebut adalah ....
Pilihan: A. 3
B. 2
C. -2
D. 6
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 93. Soal `c151e4860f06944e90e64332`

Matriks $A$ berordo $(2m - 1) \times (3n + 2)$ dan matriks $B$ berordo $9 \times 11$. Jika $A = B$, nilai $mn$ adalah ....

| Opsi | Isi |
|---|---|
| A | 8 |
| B | 45 |
| C | 15 |
| D | 12 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `62ab3071f813fb9a61e62aad2a9f4a10086ebf41a1d351d98ceb23fe8faf7f72`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$ berordo $(2m - 1) \times (3n + 2)$ dan matriks $B$ berordo $9 \times 11$. Jika $A = B$, nilai $mn$ adalah ....
Pilihan: A. 8
B. 45
C. 15
D. 12
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 94. Soal `3a816ce0796ef5b9e1fd23a7`

Toko A dan Toko B menjual dua jenis barang dengan harga (dalam ribuan rupiah) yang sama. Daftar harga Toko A disajikan dalam matriks $A = \begin{pmatrix} 25 & 2x + 5 \\ 30 & 3y - 1 \end{pmatrix}$ dan Toko B dalam matriks $B = \begin{pmatrix} 25 & 45 \\ 30 & 38 \end{pmatrix}$. Nilai $x + y$ adalah ....

| Opsi | Isi |
|---|---|
| A | 59 |
| B | 53 |
| C | 33 |
| D | 38 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fe0fb3e7d0dd9580c33b0a28c525b893bc03142489fe53b259d186d5777bb6a3`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Toko A dan Toko B menjual dua jenis barang dengan harga (dalam ribuan rupiah) yang sama. Daftar harga Toko A disajikan dalam matriks $A = \begin{pmatrix} 25 & 2x + 5 \\ 30 & 3y - 1 \end{pmatrix}$ dan Toko B dalam matriks $B = \begin{pmatrix} 25 & 45 \\ 30 & 38 \end{pmatrix}$. Nilai $x + y$ adalah ....
Pilihan: A. 59
B. 53
C. 33
D. 38
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 95. Soal `bc5a222b3c288649071a31f7`

Diketahui $A = \begin{pmatrix} x + 2 & 3y \\ 7 & 1 \end{pmatrix}$ dan $B = \begin{pmatrix} y + 5 & 12 \\ 7 & 1 \end{pmatrix}$. Jika $A = B$, nilai $xy$ adalah ....

| Opsi | Isi |
|---|---|
| A | 44 |
| B | 11 |
| C | 36 |
| D | 28 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `61447a9c451731ee511a0d906d76108fcb73be86e41965731780d48acf389a51`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix} x + 2 & 3y \\ 7 & 1 \end{pmatrix}$ dan $B = \begin{pmatrix} y + 5 & 12 \\ 7 & 1 \end{pmatrix}$. Jika $A = B$, nilai $xy$ adalah ....
Pilihan: A. 44
B. 11
C. 36
D. 28
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 96. Soal `66a4783f803ec806d30abe21`

Diketahui $A = \begin{pmatrix} x + y & 0 & z + 1 \\ 0 & 3x + 4y & 0 \\ 0 & 0 & z^2 \end{pmatrix}$ dan $I$ adalah matriks identitas berordo $3 \times 3$. Jika $A = I$ dan $z < 0$, nilai $xyz$ adalah ....

| Opsi | Isi |
|---|---|
| A | 3 |
| B | -1 |
| C | -6 |
| D | 6 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6ab2ccd01a8940b41d37d0db5b375810fb43e01964796e9d7dd4b6a5a63adb94`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix} x + y & 0 & z + 1 \\ 0 & 3x + 4y & 0 \\ 0 & 0 & z^2 \end{pmatrix}$ dan $I$ adalah matriks identitas berordo $3 \times 3$. Jika $A = I$ dan $z < 0$, nilai $xyz$ adalah ....
Pilihan: A. 3
B. -1
C. -6
D. 6
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 97. Soal `2990ea2220237fbe4add62b4`

Matriks $A = (a_{ij})$ berordo $2 \times 2$ dengan $a_{ij} = (i + j)^2$. Jika $A = \begin{pmatrix} p^2 & 3q \\ r + 2 & 4s \end{pmatrix}$ dan $p > 0$, nilai $p + q + r + s$ adalah ....

| Opsi | Isi |
|---|---|
| A | 16 |
| B | 18 |
| C | 28 |
| D | 12 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `51b0c42c0b24a9e1271fc601850daac8d5e3fcd916aa41b68a7c80897f075788`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A = (a_{ij})$ berordo $2 \times 2$ dengan $a_{ij} = (i + j)^2$. Jika $A = \begin{pmatrix} p^2 & 3q \\ r + 2 & 4s \end{pmatrix}$ dan $p > 0$, nilai $p + q + r + s$ adalah ....
Pilihan: A. 16
B. 18
C. 28
D. 12
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 98. Soal `7b1233039522c9dd3a35d9e6`

Catatan penjualan buah (dalam kg) pada hari Senin dan Selasa ternyata sama. Penjualan hari Senin ditulis $P = \begin{pmatrix} 3x + 2 & 20 \\ 15 & 2y - 4 \end{pmatrix}$ dan hari Selasa ditulis $Q = \begin{pmatrix} 17 & 20 \\ 15 & 26 \end{pmatrix}$. Nilai $y - x$ adalah ....

| Opsi | Isi |
|---|---|
| A | 10 |
| B | 6 |
| C | 20 |
| D | -10 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `36adc4aee290aa8f69167653fd2f35cf4eef1fbabdedca692bc11ef95545a9ff`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Catatan penjualan buah (dalam kg) pada hari Senin dan Selasa ternyata sama. Penjualan hari Senin ditulis $P = \begin{pmatrix} 3x + 2 & 20 \\ 15 & 2y - 4 \end{pmatrix}$ dan hari Selasa ditulis $Q = \begin{pmatrix} 17 & 20 \\ 15 & 26 \end{pmatrix}$. Nilai $y - x$ adalah ....
Pilihan: A. 10
B. 6
C. 20
D. -10
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 99. Soal `49dfa9fbce31663fa795c366`

Diketahui $P = \begin{pmatrix} 2x & k + 1 \\ y & 4 \end{pmatrix}$ dan $Q = \begin{pmatrix} x + 3 & 9 \\ 5 & y - 1 \end{pmatrix}$. Jika $P = Q$, nilai $xy + k$ adalah ....

| Opsi | Isi |
|---|---|
| A | 24 |
| B | 7 |
| C | 15 |
| D | 23 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `96f1ce3a056fb07763ca2e84f0cb03702ac3e67b34db42c133b435926f96d9a9`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $P = \begin{pmatrix} 2x & k + 1 \\ y & 4 \end{pmatrix}$ dan $Q = \begin{pmatrix} x + 3 & 9 \\ 5 & y - 1 \end{pmatrix}$. Jika $P = Q$, nilai $xy + k$ adalah ....
Pilihan: A. 24
B. 7
C. 15
D. 23
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 100. Soal `9ba329c3814396df63b83392`

Diketahui $A = \begin{pmatrix} 3 & x \\ y & 5 \end{pmatrix}$ dan $B = \begin{pmatrix} 3 & 2y - 1 \\ x - 6 & 5 \end{pmatrix}$. Jika $A = B$, nilai $2x - y$ adalah ....

| Opsi | Isi |
|---|---|
| A | -17 |
| B | 13 |
| C | 19 |
| D | 20 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d70a441d004954aa619aee05a249c074cf25b4e3a5a4ea4097e19f94381fcded`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix} 3 & x \\ y & 5 \end{pmatrix}$ dan $B = \begin{pmatrix} 3 & 2y - 1 \\ x - 6 & 5 \end{pmatrix}$. Jika $A = B$, nilai $2x - y$ adalah ....
Pilihan: A. -17
B. 13
C. 19
D. 20
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 101. Soal `6e96b0be21e17bf1fdaf867f`

Matriks $A$ dan $B$ berordo sama. Pernyataan yang benar mengenai cara memperoleh matriks $A + B$ adalah ....

| Opsi | Isi |
|---|---|
| A | Semua elemen $A$ dijumlahkan lebih dulu, kemudian ditambahkan dengan jumlah semua elemen $B$ |
| B | Elemen-elemen $A$ dan $B$ yang seletak dijumlahkan, dan hasilnya berordo sama dengan $A$ dan $B$ |
| C | Baris-baris $A$ dikalikan dengan kolom-kolom $B$, lalu hasilnya dijumlahkan |
| D | Ordo hasil adalah jumlah ordo $A$ dan ordo $B$ sehingga matriks hasil lebih besar |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `202c5bd0b9565af11d3432955a940735d1cb047492316d8942fced9533c01591`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$ dan $B$ berordo sama. Pernyataan yang benar mengenai cara memperoleh matriks $A + B$ adalah ....
Pilihan: A. Semua elemen $A$ dijumlahkan lebih dulu, kemudian ditambahkan dengan jumlah semua elemen $B$
B. Elemen-elemen $A$ dan $B$ yang seletak dijumlahkan, dan hasilnya berordo sama dengan $A$ dan $B$
C. Baris-baris $A$ dikalikan dengan kolom-kolom $B$, lalu hasilnya dijumlahkan
D. Ordo hasil adalah jumlah ordo $A$ dan ordo $B$ sehingga matriks hasil lebih besar
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 102. Soal `faf9dc80b80fcb605881aefd`

Pada penjumlahan dua matriks $A$ dan $B$ yang berordo sama, elemen baris ke-2 kolom ke-3 matriks $A + B$ diperoleh dengan cara ....

| Opsi | Isi |
|---|---|
| A | menjumlahkan elemen baris ke-2 kolom ke-3 matriks $A$ dengan elemen baris ke-3 kolom ke-2 matriks $B$ |
| B | mengalikan elemen baris ke-2 kolom ke-3 matriks $A$ dengan elemen yang seletak pada matriks $B$ |
| C | menjumlahkan semua elemen baris ke-2 matriks $A$ dengan semua elemen baris ke-2 matriks $B$ |
| D | menjumlahkan elemen baris ke-2 kolom ke-3 matriks $A$ dengan elemen baris ke-2 kolom ke-3 matriks $B$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4e0612fdf2b33bf8524ab2f563e4e57e501327fb08dd4a468285e13b9a6fbfa3`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada penjumlahan dua matriks $A$ dan $B$ yang berordo sama, elemen baris ke-2 kolom ke-3 matriks $A + B$ diperoleh dengan cara ....
Pilihan: A. menjumlahkan elemen baris ke-2 kolom ke-3 matriks $A$ dengan elemen baris ke-3 kolom ke-2 matriks $B$
B. mengalikan elemen baris ke-2 kolom ke-3 matriks $A$ dengan elemen yang seletak pada matriks $B$
C. menjumlahkan semua elemen baris ke-2 matriks $A$ dengan semua elemen baris ke-2 matriks $B$
D. menjumlahkan elemen baris ke-2 kolom ke-3 matriks $A$ dengan elemen baris ke-2 kolom ke-3 matriks $B$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 103. Soal `395345c02552ac3bd6549e5d`

Matriks $M$ berordo $4 \times 3$. Matriks $N$ dapat dikurangkan dari $M$ (selisih $M - N$ terdefinisi) hanya jika $N$ berordo ....

| Opsi | Isi |
|---|---|
| A | $3 \times 3$ |
| B | $4 \times 4$ |
| C | $3 \times 4$ |
| D | $4 \times 3$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6fb2149961cd3e7ba9a3ba62b1a5948c8c211ff38835a99ecebdcd6e7338e66d`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $M$ berordo $4 \times 3$. Matriks $N$ dapat dikurangkan dari $M$ (selisih $M - N$ terdefinisi) hanya jika $N$ berordo ....
Pilihan: A. $3 \times 3$
B. $4 \times 4$
C. $3 \times 4$
D. $4 \times 3$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 104. Soal `bc4fdd9bff5e26984452f4c4`

Matriks $P$ dan $Q$ sama-sama berordo $3 \times 5$. Ordo matriks $P - Q$ adalah ....

| Opsi | Isi |
|---|---|
| A | $6 \times 10$ |
| B | $5 \times 3$ |
| C | $3 \times 3$ |
| D | $3 \times 5$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `59c1d4e09272f7fb760bc25ff11207e09013404c4d2d066d1ea4fa76e38bb5a7`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $P$ dan $Q$ sama-sama berordo $3 \times 5$. Ordo matriks $P - Q$ adalah ....
Pilihan: A. $6 \times 10$
B. $5 \times 3$
C. $3 \times 3$
D. $3 \times 5$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 105. Soal `4c0e532e4dc616302a31a4e1`

Diketahui $A$ = $\begin{bmatrix} 8 & -4 \\ 7 & 5 \end{bmatrix}$ dan $B$ = $\begin{bmatrix} 6 & 2 \\ -3 & 9 \\ 4 & 1 \end{bmatrix}$. Pernyataan yang benar mengenai $A + B$ adalah ....

| Opsi | Isi |
|---|---|
| A | $A + B$ = $\begin{bmatrix} 14 & -2 \\ 4 & 14 \\ 4 & 1 \end{bmatrix}$ karena baris ketiga $B$ disalin |
| B | $A + B$ tidak terdefinisi karena ordo $A$ dan $B$ berbeda |
| C | $A + B$ = $\begin{bmatrix} 14 & -2 \\ 4 & 14 \end{bmatrix}$ karena baris ketiga $B$ diabaikan |
| D | $A + B$ terdefinisi dan berordo $5 \times 2$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ca0420e12b914cdd5edeb63c07bc6853532ad288eb8105339870d88d2dd2b2b2`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A$ = $\begin{bmatrix} 8 & -4 \\ 7 & 5 \end{bmatrix}$ dan $B$ = $\begin{bmatrix} 6 & 2 \\ -3 & 9 \\ 4 & 1 \end{bmatrix}$. Pernyataan yang benar mengenai $A + B$ adalah ....
Pilihan: A. $A + B$ = $\begin{bmatrix} 14 & -2 \\ 4 & 14 \\ 4 & 1 \end{bmatrix}$ karena baris ketiga $B$ disalin
B. $A + B$ tidak terdefinisi karena ordo $A$ dan $B$ berbeda
C. $A + B$ = $\begin{bmatrix} 14 & -2 \\ 4 & 14 \end{bmatrix}$ karena baris ketiga $B$ diabaikan
D. $A + B$ terdefinisi dan berordo $5 \times 2$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 106. Soal `39e1b5bcebcb8cde6c9ba364`

Dua pabrik roti mencatat pengeluaran bulan ini (dalam juta rupiah) untuk tepung dan gula, dengan baris menyatakan Pabrik I dan Pabrik II serta kolom menyatakan roti tawar dan roti manis. Pengeluaran tepung $\begin{bmatrix} 14 & 22 \\ 9 & 17 \end{bmatrix}$ dan pengeluaran gula $\begin{bmatrix} 5 & 8 \\ 6 & 3 \end{bmatrix}$. Matriks total pengeluaran kedua bahan tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{bmatrix} 19 & 30 \\ 15 & 20 \end{bmatrix}$ |
| B | $\begin{bmatrix} 9 & 14 \\ 3 & 14 \end{bmatrix}$ |
| C | $\begin{bmatrix} 19 & 15 \\ 30 & 20 \end{bmatrix}$ |
| D | $\begin{bmatrix} 19 & 30 \\ 15 & 23 \end{bmatrix}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9d23290af702fadc89d4bcc50ebd8b63385d6f49ac1296e5a54caf9adf64eefc`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Dua pabrik roti mencatat pengeluaran bulan ini (dalam juta rupiah) untuk tepung dan gula, dengan baris menyatakan Pabrik I dan Pabrik II serta kolom menyatakan roti tawar dan roti manis. Pengeluaran tepung $\begin{bmatrix} 14 & 22 \\ 9 & 17 \end{bmatrix}$ dan pengeluaran gula $\begin{bmatrix} 5 & 8 \\ 6 & 3 \end{bmatrix}$. Matriks total pengeluaran kedua bahan tersebut adalah ....
Pilihan: A. $\begin{bmatrix} 19 & 30 \\ 15 & 20 \end{bmatrix}$
B. $\begin{bmatrix} 9 & 14 \\ 3 & 14 \end{bmatrix}$
C. $\begin{bmatrix} 19 & 15 \\ 30 & 20 \end{bmatrix}$
D. $\begin{bmatrix} 19 & 30 \\ 15 & 23 \end{bmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 107. Soal `d96926a66eb3d26b5279a659`

Banyak pesanan (unit) yang diterima sebuah toko daring.<br><br>\| Minggu I \| Kaos \| Topi \|<br>\|---\|---\|---\|<br>\| Cabang Timur \| 12 \| 7 \|<br>\| Cabang Barat \| 9 \| 15 \|<br>\| Cabang Utara \| 4 \| 10 \|<br><br>\| Minggu II \| Kaos \| Topi \|<br>\|---\|---\|---\|<br>\| Cabang Timur \| 6 \| 5 \|<br>\| Cabang Barat \| 11 \| 4 \|<br>\| Cabang Utara \| 8 \| 2 \|<br><br>Matriks banyak pesanan selama dua minggu, dengan baris menyatakan cabang (Timur, Barat, Utara) dan kolom menyatakan barang (kaos, topi), adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{bmatrix} 18 & 20 & 12 \\ 12 & 19 & 12 \end{bmatrix}$ |
| B | $\begin{bmatrix} 6 & 2 \\ -2 & 11 \\ -4 & 8 \end{bmatrix}$ |
| C | $\begin{bmatrix} 18 & 12 \\ 20 & 19 \\ 12 & 12 \end{bmatrix}$ |
| D | $\begin{bmatrix} -6 & -2 \\ 2 & -11 \\ 4 & -8 \end{bmatrix}$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a1febdbe7c6bc25f14b29fdb3227758246a7c9e89c61004f6a3902c414e5271c`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Banyak pesanan (unit) yang diterima sebuah toko daring.

| Minggu I | Kaos | Topi |
|---|---|---|
| Cabang Timur | 12 | 7 |
| Cabang Barat | 9 | 15 |
| Cabang Utara | 4 | 10 |

| Minggu II | Kaos | Topi |
|---|---|---|
| Cabang Timur | 6 | 5 |
| Cabang Barat | 11 | 4 |
| Cabang Utara | 8 | 2 |

Matriks banyak pesanan selama dua minggu, dengan baris menyatakan cabang (Timur, Barat, Utara) dan kolom menyatakan barang (kaos, topi), adalah ....
Pilihan: A. $\begin{bmatrix} 18 & 20 & 12 \\ 12 & 19 & 12 \end{bmatrix}$
B. $\begin{bmatrix} 6 & 2 \\ -2 & 11 \\ -4 & 8 \end{bmatrix}$
C. $\begin{bmatrix} 18 & 12 \\ 20 & 19 \\ 12 & 12 \end{bmatrix}$
D. $\begin{bmatrix} -6 & -2 \\ 2 & -11 \\ 4 & -8 \end{bmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 108. Soal `e6be96af302c72dd66edefab`

Sebuah toko buku memiliki stok awal (eksemplar) pada cabang X dan cabang Y untuk novel, komik, dan kamus: $\begin{bmatrix} 40 & 25 \\ 30 & 18 \\ 22 & 35 \end{bmatrix}$, dengan kolom pertama cabang X dan kolom kedua cabang Y. Buku yang terjual dalam sebulan: $\begin{bmatrix} 12 & 9 \\ 10 & 17 \\ 5 & 14 \end{bmatrix}$. Matriks sisa stok setiap jenis buku di kedua cabang adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{bmatrix} 28 & 20 & 17 \\ 16 & 1 & 21 \end{bmatrix}$ |
| B | $\begin{bmatrix} 52 & 34 \\ 40 & 35 \\ 27 & 49 \end{bmatrix}$ |
| C | $\begin{bmatrix} -28 & -16 \\ -20 & -1 \\ -17 & -21 \end{bmatrix}$ |
| D | $\begin{bmatrix} 28 & 16 \\ 20 & 1 \\ 17 & 21 \end{bmatrix}$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d7e184a088c53d6442814b417dfd952ef3971d3632ffa81564987dd9e8b17a1a`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah toko buku memiliki stok awal (eksemplar) pada cabang X dan cabang Y untuk novel, komik, dan kamus: $\begin{bmatrix} 40 & 25 \\ 30 & 18 \\ 22 & 35 \end{bmatrix}$, dengan kolom pertama cabang X dan kolom kedua cabang Y. Buku yang terjual dalam sebulan: $\begin{bmatrix} 12 & 9 \\ 10 & 17 \\ 5 & 14 \end{bmatrix}$. Matriks sisa stok setiap jenis buku di kedua cabang adalah ....
Pilihan: A. $\begin{bmatrix} 28 & 20 & 17 \\ 16 & 1 & 21 \end{bmatrix}$
B. $\begin{bmatrix} 52 & 34 \\ 40 & 35 \\ 27 & 49 \end{bmatrix}$
C. $\begin{bmatrix} -28 & -16 \\ -20 & -1 \\ -17 & -21 \end{bmatrix}$
D. $\begin{bmatrix} 28 & 16 \\ 20 & 1 \\ 17 & 21 \end{bmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 109. Soal `17f2aa2ed6aea4af40f5c603`

Kapasitas kursi dua studio bioskop pada sesi siang dan malam adalah $\begin{bmatrix} 80 & 60 \\ 120 & 90 \end{bmatrix}$ (baris: studio 1 dan 2; kolom: siang dan malam). Kursi yang terisi adalah $\begin{bmatrix} 57 & 41 \\ 85 & 63 \end{bmatrix}$. Matriks banyak kursi yang masih kosong adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{bmatrix} 23 & 19 \\ 35 & 27 \end{bmatrix}$ |
| B | $\begin{bmatrix} 137 & 101 \\ 205 & 153 \end{bmatrix}$ |
| C | $\begin{bmatrix} 23 & 19 \\ 120 & 90 \end{bmatrix}$ |
| D | $\begin{bmatrix} 23 & 35 \\ 19 & 27 \end{bmatrix}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8bd64560478d00c0f94e7aa148e884ad1e1e0e5574e39e14632298fae01ad5c9`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Kapasitas kursi dua studio bioskop pada sesi siang dan malam adalah $\begin{bmatrix} 80 & 60 \\ 120 & 90 \end{bmatrix}$ (baris: studio 1 dan 2; kolom: siang dan malam). Kursi yang terisi adalah $\begin{bmatrix} 57 & 41 \\ 85 & 63 \end{bmatrix}$. Matriks banyak kursi yang masih kosong adalah ....
Pilihan: A. $\begin{bmatrix} 23 & 19 \\ 35 & 27 \end{bmatrix}$
B. $\begin{bmatrix} 137 & 101 \\ 205 & 153 \end{bmatrix}$
C. $\begin{bmatrix} 23 & 19 \\ 120 & 90 \end{bmatrix}$
D. $\begin{bmatrix} 23 & 35 \\ 19 & 27 \end{bmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 110. Soal `cf96f7860acfda38bcb19174`

Diketahui $A$ = $\begin{bmatrix} 5 & 2 \\ 1 & 4 \end{bmatrix}$ dan $B$ = $\begin{bmatrix} 3 & 6 \\ 0 & 1 \end{bmatrix}$. Pernyataan yang benar mengenai $A - B$ dan $B - A$ adalah ....

| Opsi | Isi |
|---|---|
| A | $A - B$ dan $B - A$ berbeda ordo sehingga tidak dapat dibandingkan |
| B | $A - B$ dan $B - A$ saling berlawanan sehingga tidak sama; sifat komutatif tidak berlaku pada pengurangan |
| C | $A - B$ terdefinisi, tetapi $B - A$ tidak terdefinisi |
| D | $A - B$ dan $B - A$ sama karena kedua matriks berordo sama; sifat komutatif berlaku pada pengurangan |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2b23e39eedcc75010cbdb2879304b3475b68b0e3b267911b65955852e541edf5`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A$ = $\begin{bmatrix} 5 & 2 \\ 1 & 4 \end{bmatrix}$ dan $B$ = $\begin{bmatrix} 3 & 6 \\ 0 & 1 \end{bmatrix}$. Pernyataan yang benar mengenai $A - B$ dan $B - A$ adalah ....
Pilihan: A. $A - B$ dan $B - A$ berbeda ordo sehingga tidak dapat dibandingkan
B. $A - B$ dan $B - A$ saling berlawanan sehingga tidak sama; sifat komutatif tidak berlaku pada pengurangan
C. $A - B$ terdefinisi, tetapi $B - A$ tidak terdefinisi
D. $A - B$ dan $B - A$ sama karena kedua matriks berordo sama; sifat komutatif berlaku pada pengurangan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 111. Soal `c8b2528cd0243d7afdb1670b`

Diketahui $A$ = $\begin{bmatrix} 5 & -2 \\ 8 & 6 \end{bmatrix}$ dan $B$ = $\begin{bmatrix} -4 & 7 \\ 3 & -9 \end{bmatrix}$. Hasil $A + B$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{bmatrix} 9 & -9 \\ 5 & 15 \end{bmatrix}$ |
| B | $\begin{bmatrix} 1 & 5 \\ 11 & -3 \end{bmatrix}$ |
| C | $\begin{bmatrix} 1 & 5 \\ 11 & 15 \end{bmatrix}$ |
| D | $\begin{bmatrix} -20 & -14 \\ 24 & -54 \end{bmatrix}$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `044cd98c36a27a8a8f9e0d4bd407f6ad3a99ff582e284e5734615690db88b23e`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A$ = $\begin{bmatrix} 5 & -2 \\ 8 & 6 \end{bmatrix}$ dan $B$ = $\begin{bmatrix} -4 & 7 \\ 3 & -9 \end{bmatrix}$. Hasil $A + B$ adalah ....
Pilihan: A. $\begin{bmatrix} 9 & -9 \\ 5 & 15 \end{bmatrix}$
B. $\begin{bmatrix} 1 & 5 \\ 11 & -3 \end{bmatrix}$
C. $\begin{bmatrix} 1 & 5 \\ 11 & 15 \end{bmatrix}$
D. $\begin{bmatrix} -20 & -14 \\ 24 & -54 \end{bmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 112. Soal `e34c2febcae454b21c031720`

Diketahui $A$ = $\begin{bmatrix} 3 & -1 & 6 \\ 2 & 8 & -5 \end{bmatrix}$ dan $B$ = $\begin{bmatrix} 4 & 2 & -7 \\ -6 & 1 & 9 \end{bmatrix}$. Nilai elemen baris ke-2 kolom ke-3 dari $A + B$ adalah ....

| Opsi | Isi |
|---|---|
| A | $4$ |
| B | $9$ |
| C | $-14$ |
| D | $14$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e2e6882b1e17559a0d35c368e1c51e1e1a3d03bba8249f608570c20e6bb132b0`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A$ = $\begin{bmatrix} 3 & -1 & 6 \\ 2 & 8 & -5 \end{bmatrix}$ dan $B$ = $\begin{bmatrix} 4 & 2 & -7 \\ -6 & 1 & 9 \end{bmatrix}$. Nilai elemen baris ke-2 kolom ke-3 dari $A + B$ adalah ....
Pilihan: A. $4$
B. $9$
C. $-14$
D. $14$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 113. Soal `f8b2ee292c12abba3882779d`

Diketahui $P$ = $\begin{bmatrix} 6 & -3 \\ -2 & 5 \end{bmatrix}$ dan $Q$ = $\begin{bmatrix} -4 & 1 \\ 7 & -8 \end{bmatrix}$. Hasil $P - Q$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{bmatrix} -10 & 4 \\ 9 & -13 \end{bmatrix}$ |
| B | $\begin{bmatrix} 2 & -2 \\ 5 & -3 \end{bmatrix}$ |
| C | $\begin{bmatrix} 10 & -2 \\ 5 & 13 \end{bmatrix}$ |
| D | $\begin{bmatrix} 10 & -4 \\ -9 & 13 \end{bmatrix}$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4121dfeb4d22f143ccb50c46f19a8f0398ef57d66c3141ba7704577b9fc8ce3e`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $P$ = $\begin{bmatrix} 6 & -3 \\ -2 & 5 \end{bmatrix}$ dan $Q$ = $\begin{bmatrix} -4 & 1 \\ 7 & -8 \end{bmatrix}$. Hasil $P - Q$ adalah ....
Pilihan: A. $\begin{bmatrix} -10 & 4 \\ 9 & -13 \end{bmatrix}$
B. $\begin{bmatrix} 2 & -2 \\ 5 & -3 \end{bmatrix}$
C. $\begin{bmatrix} 10 & -2 \\ 5 & 13 \end{bmatrix}$
D. $\begin{bmatrix} 10 & -4 \\ -9 & 13 \end{bmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 114. Soal `61b7fdbf63adc8ccc0e954e6`

Diketahui $M$ = $\begin{bmatrix} 8 & -1 & 5 \end{bmatrix}$ dan $N$ = $\begin{bmatrix} 3 & 6 & -4 \end{bmatrix}$. Hasil $M - N$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{bmatrix} 11 & 5 & 1 \end{bmatrix}$ |
| B | $\begin{bmatrix} -5 & 7 & -9 \end{bmatrix}$ |
| C | $\begin{bmatrix} 5 & -7 & 9 \end{bmatrix}$ |
| D | $\begin{bmatrix} 5 & -7 & 1 \end{bmatrix}$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `412230c32f1fbdbd18932f08bfc8f255d2910ff47f6f883f73d258e71e664026`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $M$ = $\begin{bmatrix} 8 & -1 & 5 \end{bmatrix}$ dan $N$ = $\begin{bmatrix} 3 & 6 & -4 \end{bmatrix}$. Hasil $M - N$ adalah ....
Pilihan: A. $\begin{bmatrix} 11 & 5 & 1 \end{bmatrix}$
B. $\begin{bmatrix} -5 & 7 & -9 \end{bmatrix}$
C. $\begin{bmatrix} 5 & -7 & 9 \end{bmatrix}$
D. $\begin{bmatrix} 5 & -7 & 1 \end{bmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 115. Soal `a40c7f62ccfd9ddf50b600d6`

Lawan dari matriks $A$ = $\begin{bmatrix} 3 & -5 \\ -1 & 0 \\ 6 & 2 \end{bmatrix}$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{bmatrix} 0 & 0 \\ 0 & 0 \\ 0 & 0 \end{bmatrix}$ |
| B | $\begin{bmatrix} -3 & 5 \\ 1 & 0 \\ -6 & -2 \end{bmatrix}$ |
| C | $\begin{bmatrix} -3 & -5 \\ 1 & 0 \\ -6 & -2 \end{bmatrix}$ |
| D | $\begin{bmatrix} -3 & 5 \\ 1 & 0 \\ -6 & 2 \end{bmatrix}$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2fceca02daaf91a7af56efaf6bbe6c75f1fd75812aaf42151ecb3f82fc028896`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Lawan dari matriks $A$ = $\begin{bmatrix} 3 & -5 \\ -1 & 0 \\ 6 & 2 \end{bmatrix}$ adalah ....
Pilihan: A. $\begin{bmatrix} 0 & 0 \\ 0 & 0 \\ 0 & 0 \end{bmatrix}$
B. $\begin{bmatrix} -3 & 5 \\ 1 & 0 \\ -6 & -2 \end{bmatrix}$
C. $\begin{bmatrix} -3 & -5 \\ 1 & 0 \\ -6 & -2 \end{bmatrix}$
D. $\begin{bmatrix} -3 & 5 \\ 1 & 0 \\ -6 & 2 \end{bmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 116. Soal `82d7978593d6a45c7b98d3d5`

Diketahui $A$ = $\begin{bmatrix} 3 & -2 \\ 5 & 1 \end{bmatrix}$, $B$ = $\begin{bmatrix} 4 & 6 \\ -1 & 2 \end{bmatrix}$, dan $C$ = $\begin{bmatrix} 2 & -5 \\ 3 & 7 \end{bmatrix}$. Hasil $A + B - C$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{bmatrix} 5 & 9 \\ 1 & -4 \end{bmatrix}$ |
| B | $\begin{bmatrix} -3 & -3 \\ 3 & -8 \end{bmatrix}$ |
| C | $\begin{bmatrix} 5 & -1 \\ 1 & -4 \end{bmatrix}$ |
| D | $\begin{bmatrix} 9 & -1 \\ 7 & 10 \end{bmatrix}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `183b44c9d34f2bca345841c4ae1af4875f78a4c0bd219ddfba53acdba3abdd5c`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A$ = $\begin{bmatrix} 3 & -2 \\ 5 & 1 \end{bmatrix}$, $B$ = $\begin{bmatrix} 4 & 6 \\ -1 & 2 \end{bmatrix}$, dan $C$ = $\begin{bmatrix} 2 & -5 \\ 3 & 7 \end{bmatrix}$. Hasil $A + B - C$ adalah ....
Pilihan: A. $\begin{bmatrix} 5 & 9 \\ 1 & -4 \end{bmatrix}$
B. $\begin{bmatrix} -3 & -3 \\ 3 & -8 \end{bmatrix}$
C. $\begin{bmatrix} 5 & -1 \\ 1 & -4 \end{bmatrix}$
D. $\begin{bmatrix} 9 & -1 \\ 7 & 10 \end{bmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 117. Soal `2c5e722442e394f60422a762`

Matriks $A$ dan $B$ berordo sama dengan $A + B$ = $\begin{bmatrix} 3 & -1 \\ 8 & 2 \end{bmatrix}$. Hasil $B + A$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{bmatrix} 3 & 8 \\ -1 & 2 \end{bmatrix}$ |
| B | $\begin{bmatrix} 2 & 8 \\ -1 & 3 \end{bmatrix}$ |
| C | $\begin{bmatrix} 3 & -1 \\ 8 & 2 \end{bmatrix}$ |
| D | $\begin{bmatrix} -3 & 1 \\ -8 & -2 \end{bmatrix}$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e88923d3510229f81628906f5f1f02ec1a302b42b9a10314afb74399f4219921`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$ dan $B$ berordo sama dengan $A + B$ = $\begin{bmatrix} 3 & -1 \\ 8 & 2 \end{bmatrix}$. Hasil $B + A$ adalah ....
Pilihan: A. $\begin{bmatrix} 3 & 8 \\ -1 & 2 \end{bmatrix}$
B. $\begin{bmatrix} 2 & 8 \\ -1 & 3 \end{bmatrix}$
C. $\begin{bmatrix} 3 & -1 \\ 8 & 2 \end{bmatrix}$
D. $\begin{bmatrix} -3 & 1 \\ -8 & -2 \end{bmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 118. Soal `50e69e744f7525da778dc1f3`

Untuk matriks $A$ dan $B$ yang berordo sama, pengurangan $A - B$ didefinisikan sebagai ....

| Opsi | Isi |
|---|---|
| A | $-(A + B)$ |
| B | $(-A) + B$ |
| C | $A + (-B)$ |
| D | $A + B$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8014dfcbfabce9dc12a0afd1c76034c2c5d3475ed5959872dc89044af02bf787`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Untuk matriks $A$ dan $B$ yang berordo sama, pengurangan $A - B$ didefinisikan sebagai ....
Pilihan: A. $-(A + B)$
B. $(-A) + B$
C. $A + (-B)$
D. $A + B$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 119. Soal `e76fe15798ef599b67d863db`

Diketahui $\begin{bmatrix} x & 3 \\ 2 & y \end{bmatrix}$ + $\begin{bmatrix} 4 & -1 \\ 5 & 6 \end{bmatrix}$ = $\begin{bmatrix} 9 & 2 \\ 7 & 10 \end{bmatrix}$. Nilai $x + y$ adalah ....

| Opsi | Isi |
|---|---|
| A | $9$ |
| B | $1$ |
| C | $20$ |
| D | $29$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `51b74a18f768a539968ed912ff8eba2520e1a2a3170bd7896d19db77e5e6f20e`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $\begin{bmatrix} x & 3 \\ 2 & y \end{bmatrix}$ + $\begin{bmatrix} 4 & -1 \\ 5 & 6 \end{bmatrix}$ = $\begin{bmatrix} 9 & 2 \\ 7 & 10 \end{bmatrix}$. Nilai $x + y$ adalah ....
Pilihan: A. $9$
B. $1$
C. $20$
D. $29$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 120. Soal `03671da30d6dd47afe87240e`

Diketahui $P$ = $\begin{bmatrix} 2 & -5 \\ 6 & 1 \end{bmatrix}$ dan $Q$ = $\begin{bmatrix} 9 & -3 \\ -4 & 9 \end{bmatrix}$. Jika $X$ matriks berordo $2 \times 2$ dan $X + P = Q$, maka $X$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{bmatrix} 7 & -8 \\ -10 & 8 \end{bmatrix}$ |
| B | $\begin{bmatrix} 11 & -8 \\ 2 & 10 \end{bmatrix}$ |
| C | $\begin{bmatrix} 7 & 2 \\ -10 & 8 \end{bmatrix}$ |
| D | $\begin{bmatrix} -7 & -2 \\ 10 & -8 \end{bmatrix}$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ca96ab5b2098c9d2043570962903be786a04bc6c9f4f4aa5bee5c58d3b564cf1`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $P$ = $\begin{bmatrix} 2 & -5 \\ 6 & 1 \end{bmatrix}$ dan $Q$ = $\begin{bmatrix} 9 & -3 \\ -4 & 9 \end{bmatrix}$. Jika $X$ matriks berordo $2 \times 2$ dan $X + P = Q$, maka $X$ adalah ....
Pilihan: A. $\begin{bmatrix} 7 & -8 \\ -10 & 8 \end{bmatrix}$
B. $\begin{bmatrix} 11 & -8 \\ 2 & 10 \end{bmatrix}$
C. $\begin{bmatrix} 7 & 2 \\ -10 & 8 \end{bmatrix}$
D. $\begin{bmatrix} -7 & -2 \\ 10 & -8 \end{bmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 121. Soal `11dd951bbe1f7f7664255cb1`

Seorang siswa berpendapat bahwa $A - B = B - A$ untuk setiap dua matriks $A$ dan $B$ yang berordo sama, karena penjumlahan matriks bersifat komutatif. Penilaian yang tepat terhadap pendapat tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | Pendapat itu salah untuk semua pasangan $A$ dan $B$ tanpa kecuali |
| B | Pendapat itu benar bila $A$ dan $B$ sama-sama matriks persegi |
| C | Pendapat itu salah secara umum; $A - B = B - A$ hanya terjadi bila $A = B$ |
| D | Pendapat itu benar, sebab pengurangan didefinisikan sebagai penjumlahan dengan lawan matriks |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `98b887ae6281bc8a3b7c9acfb839292e40d60fb91ef409521fd421d311395cde`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Seorang siswa berpendapat bahwa $A - B = B - A$ untuk setiap dua matriks $A$ dan $B$ yang berordo sama, karena penjumlahan matriks bersifat komutatif. Penilaian yang tepat terhadap pendapat tersebut adalah ....
Pilihan: A. Pendapat itu salah untuk semua pasangan $A$ dan $B$ tanpa kecuali
B. Pendapat itu benar bila $A$ dan $B$ sama-sama matriks persegi
C. Pendapat itu salah secara umum; $A - B = B - A$ hanya terjadi bila $A = B$
D. Pendapat itu benar, sebab pengurangan didefinisikan sebagai penjumlahan dengan lawan matriks
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 122. Soal `d7138f9b6afcf14dd45fd448`

Seorang siswa menulis $A - (B - C) = A - B - C$ untuk matriks-matriks $A$, $B$, dan $C$ yang berordo sama. Kesalahan siswa tersebut dan bentuk yang benar adalah ....

| Opsi | Isi |
|---|---|
| A | Lawan dari $(B - C)$ adalah $-B + C$, sehingga bentuk yang benar adalah $A - B + C$ |
| B | Tanda $B$ yang keliru, sehingga bentuk yang benar adalah $A + B - C$ |
| C | Tidak ada kesalahan, karena pengurangan matriks bersifat asosiatif |
| D | Dua tanda negatif harus menjadi positif, sehingga bentuk yang benar adalah $A + B + C$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6a944a76c79faa1ef7834c680fe58bec0eb6e51f800fae3e143d6eb266b065e9`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Seorang siswa menulis $A - (B - C) = A - B - C$ untuk matriks-matriks $A$, $B$, dan $C$ yang berordo sama. Kesalahan siswa tersebut dan bentuk yang benar adalah ....
Pilihan: A. Lawan dari $(B - C)$ adalah $-B + C$, sehingga bentuk yang benar adalah $A - B + C$
B. Tanda $B$ yang keliru, sehingga bentuk yang benar adalah $A + B - C$
C. Tidak ada kesalahan, karena pengurangan matriks bersifat asosiatif
D. Dua tanda negatif harus menjadi positif, sehingga bentuk yang benar adalah $A + B + C$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 123. Soal `11c536c9606a48568144c975`

Diketahui $A$ = $\begin{pmatrix} 3 & -1 & 4 \\ 2 & 5 & 0 \end{pmatrix}$ dan $B$ = $\begin{pmatrix} 6 & 2 \\ -3 & 7 \end{pmatrix}$. Seorang siswa menjumlahkannya dengan menambahkan kolom nol pada $B$ hingga berordo $2 \times 3$, lalu memperoleh $A + B$ = $\begin{pmatrix} 9 & 1 & 4 \\ -1 & 12 & 0 \end{pmatrix}$. Penilaian yang tepat terhadap penyelesaian siswa tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | Benar, sebab elemen yang tidak memiliki pasangan dapat dianggap bernilai nol |
| B | Salah, sebab $A + B$ tidak terdefinisi: ordo $A$ ($2 \times 3$) dan $B$ ($2 \times 2$) berbeda, dan menambah kolom nol mengganti $B$ dengan matriks lain |
| C | Salah, sebab kolom nol seharusnya ditambahkan pada $A$ agar $A + B$ berordo $2 \times 2$ |
| D | Salah, sebab hasil penjumlahan seharusnya berordo $2 \times 2$ mengikuti ordo $B$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `67144ebb2a4b48982bea7b8b59ff1d0f0fea231a21cdef4f69899b923052e580`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A$ = $\begin{pmatrix} 3 & -1 & 4 \\ 2 & 5 & 0 \end{pmatrix}$ dan $B$ = $\begin{pmatrix} 6 & 2 \\ -3 & 7 \end{pmatrix}$. Seorang siswa menjumlahkannya dengan menambahkan kolom nol pada $B$ hingga berordo $2 \times 3$, lalu memperoleh $A + B$ = $\begin{pmatrix} 9 & 1 & 4 \\ -1 & 12 & 0 \end{pmatrix}$. Penilaian yang tepat terhadap penyelesaian siswa tersebut adalah ....
Pilihan: A. Benar, sebab elemen yang tidak memiliki pasangan dapat dianggap bernilai nol
B. Salah, sebab $A + B$ tidak terdefinisi: ordo $A$ ($2 \times 3$) dan $B$ ($2 \times 2$) berbeda, dan menambah kolom nol mengganti $B$ dengan matriks lain
C. Salah, sebab kolom nol seharusnya ditambahkan pada $A$ agar $A + B$ berordo $2 \times 2$
D. Salah, sebab hasil penjumlahan seharusnya berordo $2 \times 2$ mengikuti ordo $B$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 124. Soal `2573392da1a698ba9dd8f5d6`

Diketahui $A$ = $\begin{pmatrix} 5 & 2p - 1 \\ q + 3 & 7 \end{pmatrix}$ dan $B$ = $\begin{pmatrix} 1 & p - 8 \\ q - 11 & 2 \end{pmatrix}$. Jika $A + B$ merupakan matriks diagonal, nilai $p + q$ adalah ....

| Opsi | Isi |
|---|---|
| A | $-1$ |
| B | $7$ |
| C | $-3$ |
| D | $12$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `afd7716ad3b5270584153e99683b44b59d0381f036297a0a492192c860855920`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A$ = $\begin{pmatrix} 5 & 2p - 1 \\ q + 3 & 7 \end{pmatrix}$ dan $B$ = $\begin{pmatrix} 1 & p - 8 \\ q - 11 & 2 \end{pmatrix}$. Jika $A + B$ merupakan matriks diagonal, nilai $p + q$ adalah ....
Pilihan: A. $-1$
B. $7$
C. $-3$
D. $12$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 125. Soal `c951a9cde4a9e6544efe478a`

Klaim: "Jika selisih $A - B$ merupakan matriks simetris, maka $A$ dan $B$ keduanya simetris." Pasangan $(A, B)$ berikut yang merupakan contoh penyangkal klaim tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $A$ = $\begin{pmatrix} 3 & 5 \\ 1 & 4 \end{pmatrix}$ dan $B$ = $\begin{pmatrix} 1 & 2 \\ -2 & 0 \end{pmatrix}$ |
| B | $A$ = $\begin{pmatrix} 2 & 6 \\ 3 & 1 \end{pmatrix}$ dan $B$ = $\begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$ |
| C | $A$ = $\begin{pmatrix} 3 & 5 \\ 1 & 4 \end{pmatrix}$ dan $B$ = $\begin{pmatrix} 1 & 2 \\ 2 & 0 \end{pmatrix}$ |
| D | $A$ = $\begin{pmatrix} 2 & 1 \\ 1 & 5 \end{pmatrix}$ dan $B$ = $\begin{pmatrix} 1 & 4 \\ 4 & 2 \end{pmatrix}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `08b8c9338075ae430c7f90cb49a010278a802f57a602c6fc80fefe05777fd1b5`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Klaim: "Jika selisih $A - B$ merupakan matriks simetris, maka $A$ dan $B$ keduanya simetris." Pasangan $(A, B)$ berikut yang merupakan contoh penyangkal klaim tersebut adalah ....
Pilihan: A. $A$ = $\begin{pmatrix} 3 & 5 \\ 1 & 4 \end{pmatrix}$ dan $B$ = $\begin{pmatrix} 1 & 2 \\ -2 & 0 \end{pmatrix}$
B. $A$ = $\begin{pmatrix} 2 & 6 \\ 3 & 1 \end{pmatrix}$ dan $B$ = $\begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$
C. $A$ = $\begin{pmatrix} 3 & 5 \\ 1 & 4 \end{pmatrix}$ dan $B$ = $\begin{pmatrix} 1 & 2 \\ 2 & 0 \end{pmatrix}$
D. $A$ = $\begin{pmatrix} 2 & 1 \\ 1 & 5 \end{pmatrix}$ dan $B$ = $\begin{pmatrix} 1 & 4 \\ 4 & 2 \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 126. Soal `1f0129b1658816a7b4a78f11`

Diketahui $A$ = $\begin{pmatrix} 2 & t \\ 5 & 1 \end{pmatrix}$, $B$ = $\begin{pmatrix} 9 & 7 \\ 4 & 6 \end{pmatrix}$, $C$ = $\begin{pmatrix} 3 & t \\ 0 & 2 \end{pmatrix}$, dan $D$ = $\begin{pmatrix} 4 & 1 \\ -1 & 3 \end{pmatrix}$. Matriks $X$ berordo $2 \times 2$ harus memenuhi $X + A = B$ sekaligus $X - C = D$. Nilai $t$ yang memungkinkan adanya matriks $X$ tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $4$ |
| B | $6$ |
| C | $3$ |
| D | $-3$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `eb4b5c3a4141b8ca1f2c2c5a4f9d6f72805f0edd2972a822a15f948327510a7d`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A$ = $\begin{pmatrix} 2 & t \\ 5 & 1 \end{pmatrix}$, $B$ = $\begin{pmatrix} 9 & 7 \\ 4 & 6 \end{pmatrix}$, $C$ = $\begin{pmatrix} 3 & t \\ 0 & 2 \end{pmatrix}$, dan $D$ = $\begin{pmatrix} 4 & 1 \\ -1 & 3 \end{pmatrix}$. Matriks $X$ berordo $2 \times 2$ harus memenuhi $X + A = B$ sekaligus $X - C = D$. Nilai $t$ yang memungkinkan adanya matriks $X$ tersebut adalah ....
Pilihan: A. $4$
B. $6$
C. $3$
D. $-3$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 127. Soal `658ba6bfd4a895db9cc90ddb`

Diketahui $A$ = $\begin{pmatrix} 8 & -3 \\ 5 & 6 \end{pmatrix}$, $B$ = $\begin{pmatrix} 2 & 4 \\ -1 & 7 \end{pmatrix}$, dan $C$ = $\begin{pmatrix} 5 & -6 \\ 3 & -2 \end{pmatrix}$. Untuk menghitung $A - B - C$, siswa P menghitung $(A - B) + C$ dan siswa Q menghitung $A - (B - C)$. Pernyataan yang benar adalah ....

| Opsi | Isi |
|---|---|
| A | Hanya siswa Q yang benar, sebab kurung memisahkan $B$ dan $C$, hasilnya $\begin{pmatrix} 11 & -13 \\ 9 & -3 \end{pmatrix}$ |
| B | Keduanya benar karena hasilnya sama, yaitu $\begin{pmatrix} 11 & -13 \\ 9 & -3 \end{pmatrix}$ |
| C | Hanya siswa P yang benar, sebab mengerjakan dari kiri ke kanan, hasilnya $\begin{pmatrix} 11 & -13 \\ 9 & -3 \end{pmatrix}$ |
| D | Keduanya salah karena sama-sama menambahkan $C$; hasil yang benar adalah $\begin{pmatrix} 1 & -1 \\ 3 & 1 \end{pmatrix}$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c53ba938bdfefccae7e77f4ad12bbb7b78db1a8c4d69113fb8ccc74deb4987bc`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A$ = $\begin{pmatrix} 8 & -3 \\ 5 & 6 \end{pmatrix}$, $B$ = $\begin{pmatrix} 2 & 4 \\ -1 & 7 \end{pmatrix}$, dan $C$ = $\begin{pmatrix} 5 & -6 \\ 3 & -2 \end{pmatrix}$. Untuk menghitung $A - B - C$, siswa P menghitung $(A - B) + C$ dan siswa Q menghitung $A - (B - C)$. Pernyataan yang benar adalah ....
Pilihan: A. Hanya siswa Q yang benar, sebab kurung memisahkan $B$ dan $C$, hasilnya $\begin{pmatrix} 11 & -13 \\ 9 & -3 \end{pmatrix}$
B. Keduanya benar karena hasilnya sama, yaitu $\begin{pmatrix} 11 & -13 \\ 9 & -3 \end{pmatrix}$
C. Hanya siswa P yang benar, sebab mengerjakan dari kiri ke kanan, hasilnya $\begin{pmatrix} 11 & -13 \\ 9 & -3 \end{pmatrix}$
D. Keduanya salah karena sama-sama menambahkan $C$; hasil yang benar adalah $\begin{pmatrix} 1 & -1 \\ 3 & 1 \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 128. Soal `648894408e5dad6af59f3a41`

Siswa menghitung $\begin{pmatrix} 4 & -2 \\ -3 & 5 \end{pmatrix}$ - $\begin{pmatrix} 1 & -6 \\ -2 & 3 \end{pmatrix}$ dan menulis hasilnya $\begin{pmatrix} 3 & -8 \\ -5 & 2 \end{pmatrix}$. Pernyataan yang tepat mengenai hasil tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | Satu elemen salah, yaitu baris 1 kolom 2, karena $-2 - (-6)$ ditulis $-8$ |
| B | Seluruh elemen salah karena pengurangan matriks harus dikerjakan sebagai $B - A$ |
| C | Dua elemen salah, yaitu baris 1 kolom 1 dan baris 2 kolom 2, karena seharusnya dijumlahkan |
| D | Dua elemen salah, yaitu baris 1 kolom 2 dan baris 2 kolom 1, karena pengurang yang negatif diperlakukan sebagai bilangan positif |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c5126598dfc0df2ec3c2103638daa1c3dfa964c31bb81bc1adacf5d63a8b3729`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Siswa menghitung $\begin{pmatrix} 4 & -2 \\ -3 & 5 \end{pmatrix}$ - $\begin{pmatrix} 1 & -6 \\ -2 & 3 \end{pmatrix}$ dan menulis hasilnya $\begin{pmatrix} 3 & -8 \\ -5 & 2 \end{pmatrix}$. Pernyataan yang tepat mengenai hasil tersebut adalah ....
Pilihan: A. Satu elemen salah, yaitu baris 1 kolom 2, karena $-2 - (-6)$ ditulis $-8$
B. Seluruh elemen salah karena pengurangan matriks harus dikerjakan sebagai $B - A$
C. Dua elemen salah, yaitu baris 1 kolom 1 dan baris 2 kolom 2, karena seharusnya dijumlahkan
D. Dua elemen salah, yaitu baris 1 kolom 2 dan baris 2 kolom 1, karena pengurang yang negatif diperlakukan sebagai bilangan positif
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 129. Soal `0b5ce78b41d9ef238edae3c7`

Klaim: "Jika $A + B = O$ (matriks nol), maka $A = O$ dan $B = O$." Pernyataan yang benar mengenai klaim tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | Klaim salah; contohnya $A$ = $\begin{pmatrix} 2 & -1 \\ 3 & 4 \end{pmatrix}$ dan $B$ = $\begin{pmatrix} -2 & 1 \\ -3 & -4 \end{pmatrix}$ |
| B | Klaim benar bila $A$ dan $B$ berordo $2 \times 2$ |
| C | Klaim salah; contoh penyangkalnya $A$ = $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ dan $B$ = $\begin{pmatrix} -1 & 2 \\ -3 & 4 \end{pmatrix}$ |
| D | Klaim benar, sebab jumlah dua matriks hanya nol bila keduanya matriks nol |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `81ef636aaae8d951508fddb05f52b81f836e6d6aac7bfe8501aebdf8156b5511`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Klaim: "Jika $A + B = O$ (matriks nol), maka $A = O$ dan $B = O$." Pernyataan yang benar mengenai klaim tersebut adalah ....
Pilihan: A. Klaim salah; contohnya $A$ = $\begin{pmatrix} 2 & -1 \\ 3 & 4 \end{pmatrix}$ dan $B$ = $\begin{pmatrix} -2 & 1 \\ -3 & -4 \end{pmatrix}$
B. Klaim benar bila $A$ dan $B$ berordo $2 \times 2$
C. Klaim salah; contoh penyangkalnya $A$ = $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ dan $B$ = $\begin{pmatrix} -1 & 2 \\ -3 & 4 \end{pmatrix}$
D. Klaim benar, sebab jumlah dua matriks hanya nol bila keduanya matriks nol
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 130. Soal `1cda7c4fa18838da987ec244`

Matriks $A$ dan $B$ berordo $2 \times 2$ dengan elemen bilangan real, dan $B$ = $\begin{pmatrix} 2k - 6 & m + k \\ 3k - 9 & 2m + 6 \end{pmatrix}$. Jika $A + B = A - B$, nilai $k - m$ adalah ....

| Opsi | Isi |
|---|---|
| A | $-6$ |
| B | $6$ |
| C | $0$ |
| D | $3$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7834e18a813eef625014d242ce29a936e6e044ee99ff7878fe92183c3c23b841`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$ dan $B$ berordo $2 \times 2$ dengan elemen bilangan real, dan $B$ = $\begin{pmatrix} 2k - 6 & m + k \\ 3k - 9 & 2m + 6 \end{pmatrix}$. Jika $A + B = A - B$, nilai $k - m$ adalah ....
Pilihan: A. $-6$
B. $6$
C. $0$
D. $3$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 131. Soal `241c2b54fd8e8022cebdcabc`

Matriks $A$, $B$, dan $C$ berordo sama. Pernyataan yang benar untuk semua matriks $A$, $B$, $C$ tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $(A + B) - C = A - (B + C)$ |
| B | $(A - B) - C = (A - C) + B$ |
| C | $(A - B) + (B - C) + (C - A) = O$ |
| D | $A - O = O - A$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9c74dbfb7a077c78c3cca2f5b650eadc830549cae9a3b7b97a22af8e26822dcd`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$, $B$, dan $C$ berordo sama. Pernyataan yang benar untuk semua matriks $A$, $B$, $C$ tersebut adalah ....
Pilihan: A. $(A + B) - C = A - (B + C)$
B. $(A - B) - C = (A - C) + B$
C. $(A - B) + (B - C) + (C - A) = O$
D. $A - O = O - A$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 132. Soal `ce2822cb05c4bb83aaad7640`

Matriks $A$ dan $B$ berordo $1 \times 2$ dengan semua elemen bilangan cacah ($0, 1, 2, \ldots$) dan $A + B$ = $\begin{pmatrix} 4 & 3 \end{pmatrix}$. Banyak pasangan terurut $(A, B)$ yang mungkin adalah ....

| Opsi | Isi |
|---|---|
| A | $12$ |
| B | $7$ |
| C | $9$ |
| D | $20$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d1bb07c58e6845fed91711518ce3c4fa1bd0002eeb95c5ca25a19434a2314714`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$ dan $B$ berordo $1 \times 2$ dengan semua elemen bilangan cacah ($0, 1, 2, \ldots$) dan $A + B$ = $\begin{pmatrix} 4 & 3 \end{pmatrix}$. Banyak pasangan terurut $(A, B)$ yang mungkin adalah ....
Pilihan: A. $12$
B. $7$
C. $9$
D. $20$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 133. Soal `26df8400c8d2ba32d982768a`

Diketahui $\begin{pmatrix} 3x & y \\ 5z & 7z \end{pmatrix}$ - $\begin{pmatrix} 19 & -x \\ -4y & 17 \end{pmatrix}$ + $\begin{pmatrix} 4 & -3 \\ -7 & -4 \end{pmatrix}$ = $\begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$. Nilai $x$, $y$, dan $z$ berturut-turut adalah ....

| Opsi | Isi |
|---|---|
| A | $x = 5$, $y = -2$, $z = -3$ |
| B | $x = 5$, $y = -2$, $z = 3$ |
| C | $x = 5$, $y = -8$, $z = 3$ |
| D | $x = -5$, $y = -2$, $z = 3$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `81e254c6843ce7f1c33c6f7cd52f4861a14e655555003e66ac92fcda9c6b6a89`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $\begin{pmatrix} 3x & y \\ 5z & 7z \end{pmatrix}$ - $\begin{pmatrix} 19 & -x \\ -4y & 17 \end{pmatrix}$ + $\begin{pmatrix} 4 & -3 \\ -7 & -4 \end{pmatrix}$ = $\begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$. Nilai $x$, $y$, dan $z$ berturut-turut adalah ....
Pilihan: A. $x = 5$, $y = -2$, $z = -3$
B. $x = 5$, $y = -2$, $z = 3$
C. $x = 5$, $y = -8$, $z = 3$
D. $x = -5$, $y = -2$, $z = 3$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 134. Soal `f00968f88d1b621c562d1350`

Diketahui $\begin{pmatrix} 3x & 2y \\ z & 4z \end{pmatrix}$ - $\begin{pmatrix} 5 & -3x \\ 2y & -9 \end{pmatrix}$ + $\begin{pmatrix} 11 & -4 \\ 13 & 3 \end{pmatrix}$ = $\begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$. Nilai $x$, $y$, dan $z$ yang memenuhi adalah ....

| Opsi | Isi |
|---|---|
| A | $x = -2$, $y = 5$, $z = 3$ |
| B | $x = -2$, $y = 5$, $z = -3$ |
| C | $x = -2$, $y = -1$, $z = -3$ |
| D | $x = 2$, $y = -1$, $z = -3$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8eb70f6b6de1ac994d95c51b021ad8da79a725da1e8a9ca1bd8e12b4cf10cc72`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $\begin{pmatrix} 3x & 2y \\ z & 4z \end{pmatrix}$ - $\begin{pmatrix} 5 & -3x \\ 2y & -9 \end{pmatrix}$ + $\begin{pmatrix} 11 & -4 \\ 13 & 3 \end{pmatrix}$ = $\begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$. Nilai $x$, $y$, dan $z$ yang memenuhi adalah ....
Pilihan: A. $x = -2$, $y = 5$, $z = 3$
B. $x = -2$, $y = 5$, $z = -3$
C. $x = -2$, $y = -1$, $z = -3$
D. $x = 2$, $y = -1$, $z = -3$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 135. Soal `55c90f4ac5b683942d54e5b2`

Diketahui $\begin{pmatrix} 7a \\ 7b \end{pmatrix}$ + $\begin{pmatrix} 3b \\ 3a \end{pmatrix}$ = $\begin{pmatrix} 5 \\ -15 \end{pmatrix}$. Nilai $a$ dan $b$ adalah ....

| Opsi | Isi |
|---|---|
| A | $a = 2$, $b = -3$ |
| B | $a = -2$, $b = 3$ |
| C | $a = 2$, $b = 3$ |
| D | $a = -3$, $b = 2$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9e9d9f788734c5503c6382dfc35284cfa4f44bb6a4543a338de239351777bb0c`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $\begin{pmatrix} 7a \\ 7b \end{pmatrix}$ + $\begin{pmatrix} 3b \\ 3a \end{pmatrix}$ = $\begin{pmatrix} 5 \\ -15 \end{pmatrix}$. Nilai $a$ dan $b$ adalah ....
Pilihan: A. $a = 2$, $b = -3$
B. $a = -2$, $b = 3$
C. $a = 2$, $b = 3$
D. $a = -3$, $b = 2$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 136. Soal `71f11a0598a6e0edf723fb71`

Diketahui $\begin{pmatrix} 9a \\ 2b \end{pmatrix}$ + $\begin{pmatrix} 5b \\ 6a \end{pmatrix}$ = $\begin{pmatrix} 11 \\ 14 \end{pmatrix}$. Nilai $a + b$ adalah ....

| Opsi | Isi |
|---|---|
| A | $-20$ |
| B | $9$ |
| C | $-1$ |
| D | $1$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2daba6498f60525846b010d0e514092acd6c58922b7f4552b0373229a5b01b25`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $\begin{pmatrix} 9a \\ 2b \end{pmatrix}$ + $\begin{pmatrix} 5b \\ 6a \end{pmatrix}$ = $\begin{pmatrix} 11 \\ 14 \end{pmatrix}$. Nilai $a + b$ adalah ....
Pilihan: A. $-20$
B. $9$
C. $-1$
D. $1$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 137. Soal `f54dd9be2c437eae32c8fc4f`

Diketahui $\begin{pmatrix} a+b & 2c \\ c-d & 3a \end{pmatrix}$ + $\begin{pmatrix} 2a & -c \\ 4 & -b \end{pmatrix}$ = $\begin{pmatrix} 11 & 4 \\ 9 & 7 \end{pmatrix}$. Nilai $a + b + c + d$ adalah ....

| Opsi | Isi |
|---|---|
| A | $4$ |
| B | $8$ |
| C | $9$ |
| D | $10$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `16d1ab49120ea88c0f25ef49c273f2580f451c7a8a75f7d881ceaf1b56e5499e`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $\begin{pmatrix} a+b & 2c \\ c-d & 3a \end{pmatrix}$ + $\begin{pmatrix} 2a & -c \\ 4 & -b \end{pmatrix}$ = $\begin{pmatrix} 11 & 4 \\ 9 & 7 \end{pmatrix}$. Nilai $a + b + c + d$ adalah ....
Pilihan: A. $4$
B. $8$
C. $9$
D. $10$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 138. Soal `3657067d581f904849ffa0f5`

Diketahui $A$ = $\begin{pmatrix} 7 & -2 \\ 4 & 9 \\ -5 & 3 \end{pmatrix}$, $B$ = $\begin{pmatrix} 12 & 6 \\ -3 & 8 \\ 10 & -4 \end{pmatrix}$, dan $C$ = $\begin{pmatrix} 5 & -9 \\ 2 & -6 \\ 8 & 1 \end{pmatrix}$. Jika $X$ matriks berordo $3 \times 2$ dan $X + A = B - C$, maka $X$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix} 14 & 13 \\ -1 & 23 \\ -3 & -2 \end{pmatrix}$ |
| B | $\begin{pmatrix} 0 & -17 \\ 9 & -5 \\ -7 & 8 \end{pmatrix}$ |
| C | $\begin{pmatrix} 0 & 17 \\ -9 & 5 \\ 7 & -8 \end{pmatrix}$ |
| D | $\begin{pmatrix} 10 & -1 \\ -5 & -7 \\ 23 & -6 \end{pmatrix}$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `29babf35b63a2a399b8fdcc74f104fdea59a6cde5cc12bb76a71e5974f02092c`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A$ = $\begin{pmatrix} 7 & -2 \\ 4 & 9 \\ -5 & 3 \end{pmatrix}$, $B$ = $\begin{pmatrix} 12 & 6 \\ -3 & 8 \\ 10 & -4 \end{pmatrix}$, dan $C$ = $\begin{pmatrix} 5 & -9 \\ 2 & -6 \\ 8 & 1 \end{pmatrix}$. Jika $X$ matriks berordo $3 \times 2$ dan $X + A = B - C$, maka $X$ adalah ....
Pilihan: A. $\begin{pmatrix} 14 & 13 \\ -1 & 23 \\ -3 & -2 \end{pmatrix}$
B. $\begin{pmatrix} 0 & -17 \\ 9 & -5 \\ -7 & 8 \end{pmatrix}$
C. $\begin{pmatrix} 0 & 17 \\ -9 & 5 \\ 7 & -8 \end{pmatrix}$
D. $\begin{pmatrix} 10 & -1 \\ -5 & -7 \\ 23 & -6 \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 139. Soal `9d21d1a13e75a731f163596a`

Diketahui $A$ = $\begin{pmatrix} 9 & -4 & 6 \\ 2 & 8 & -5 \end{pmatrix}$, $B$ = $\begin{pmatrix} 3 & 7 & -2 \\ -6 & 1 & 4 \end{pmatrix}$, dan $C$ = $\begin{pmatrix} 5 & -3 & 8 \\ 2 & 9 & -1 \end{pmatrix}$. Jika $A - X = B + C$, maka $X$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix} 1 & -8 & 0 \\ 6 & -2 & -8 \end{pmatrix}$ |
| B | $\begin{pmatrix} -1 & 8 & 0 \\ -6 & 2 & 8 \end{pmatrix}$ |
| C | $\begin{pmatrix} 11 & -14 & 16 \\ 10 & 16 & -10 \end{pmatrix}$ |
| D | $\begin{pmatrix} 17 & 0 & 12 \\ -2 & 18 & -2 \end{pmatrix}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3a8d0d62f084901d25d7e4491ace9dbb103bfd1fb8f1bb94ae3f55a5f58d4c06`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A$ = $\begin{pmatrix} 9 & -4 & 6 \\ 2 & 8 & -5 \end{pmatrix}$, $B$ = $\begin{pmatrix} 3 & 7 & -2 \\ -6 & 1 & 4 \end{pmatrix}$, dan $C$ = $\begin{pmatrix} 5 & -3 & 8 \\ 2 & 9 & -1 \end{pmatrix}$. Jika $A - X = B + C$, maka $X$ adalah ....
Pilihan: A. $\begin{pmatrix} 1 & -8 & 0 \\ 6 & -2 & -8 \end{pmatrix}$
B. $\begin{pmatrix} -1 & 8 & 0 \\ -6 & 2 & 8 \end{pmatrix}$
C. $\begin{pmatrix} 11 & -14 & 16 \\ 10 & 16 & -10 \end{pmatrix}$
D. $\begin{pmatrix} 17 & 0 & 12 \\ -2 & 18 & -2 \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 140. Soal `3fbb56bd7f0750d3b2bc74ea`

Diketahui $P$ = $\begin{pmatrix} 6 & -3 \\ -8 & 5 \\ 2 & 9 \end{pmatrix}$, $Q$ = $\begin{pmatrix} 4 & 7 \\ -1 & -6 \\ 3 & 2 \end{pmatrix}$, dan $R$ = $\begin{pmatrix} -5 & 2 \\ 9 & 1 \\ -4 & 8 \end{pmatrix}$. Jika $X$ memenuhi $(X - P) + (Q - R) = O$ dengan $O$ matriks nol berordo $3 \times 2$, maka $X$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix} 15 & 2 \\ -18 & -2 \\ 9 & 3 \end{pmatrix}$ |
| B | $\begin{pmatrix} 7 & -12 \\ -16 & 10 \\ 3 & -1 \end{pmatrix}$ |
| C | $\begin{pmatrix} 3 & 8 \\ -2 & -12 \\ 5 & -15 \end{pmatrix}$ |
| D | $\begin{pmatrix} -3 & -8 \\ 2 & 12 \\ -5 & 15 \end{pmatrix}$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a189302aba3d7f4e7204e53c2e395c2d16a87b8eafd41acbe790899142ca77a4`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $P$ = $\begin{pmatrix} 6 & -3 \\ -8 & 5 \\ 2 & 9 \end{pmatrix}$, $Q$ = $\begin{pmatrix} 4 & 7 \\ -1 & -6 \\ 3 & 2 \end{pmatrix}$, dan $R$ = $\begin{pmatrix} -5 & 2 \\ 9 & 1 \\ -4 & 8 \end{pmatrix}$. Jika $X$ memenuhi $(X - P) + (Q - R) = O$ dengan $O$ matriks nol berordo $3 \times 2$, maka $X$ adalah ....
Pilihan: A. $\begin{pmatrix} 15 & 2 \\ -18 & -2 \\ 9 & 3 \end{pmatrix}$
B. $\begin{pmatrix} 7 & -12 \\ -16 & 10 \\ 3 & -1 \end{pmatrix}$
C. $\begin{pmatrix} 3 & 8 \\ -2 & -12 \\ 5 & -15 \end{pmatrix}$
D. $\begin{pmatrix} -3 & -8 \\ 2 & 12 \\ -5 & 15 \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 141. Soal `482e561005c7424fd8faf9d3`

Matriks $A$ berordo $(2m - 1) \times (n + 2)$ dan matriks $B$ berordo $5 \times 6$. Jika $A - B$ terdefinisi dengan $m$ dan $n$ bilangan asli, nilai $m + n$ adalah ....

| Opsi | Isi |
|---|---|
| A | $9$ |
| B | $7$ |
| C | $11$ |
| D | $6$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8578069b5fdb5b0d269d573d580eb7a6f9b3a0bef778343031780d897af4f629`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$ berordo $(2m - 1) \times (n + 2)$ dan matriks $B$ berordo $5 \times 6$. Jika $A - B$ terdefinisi dengan $m$ dan $n$ bilangan asli, nilai $m + n$ adalah ....
Pilihan: A. $9$
B. $7$
C. $11$
D. $6$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 142. Soal `e520f1d965ae0b9c7610b06d`

Biaya pembelian kain pada bulan Januari disusun dalam matriks $P$ berordo $3 \times 4$ (baris: jenis kain, kolom: pemasok ke-1 sampai ke-4). Pada bulan Februari pemasok ke-4 tidak dipakai lagi sehingga matriks $Q$ hanya berordo $3 \times 3$. Agar $P + Q$ dapat dihitung tanpa menambah data baru pada $Q$, pernyataan yang benar adalah ....

| Opsi | Isi |
|---|---|
| A | Kolom pemasok ke-4 pada $P$ dihapus sehingga $P$ berordo $3 \times 3$ dan $P + Q$ berordo $3 \times 3$ |
| B | Baris ketiga pada $P$ dihapus sehingga $P$ berordo $2 \times 4$ dan $P + Q$ berordo $2 \times 4$ |
| C | Kolom pemasok ke-1 pada $Q$ digandakan sehingga $Q$ berordo $3 \times 4$ dan $P + Q$ berordo $3 \times 4$ |
| D | Kolom pemasok ke-4 pada $P$ dihapus sehingga $P + Q$ dapat dihitung dan berordo $3 \times 4$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `086db8e42f547fc457c2daa339a20291d7fcc6399bbc0de23d58ef0677450c67`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Biaya pembelian kain pada bulan Januari disusun dalam matriks $P$ berordo $3 \times 4$ (baris: jenis kain, kolom: pemasok ke-1 sampai ke-4). Pada bulan Februari pemasok ke-4 tidak dipakai lagi sehingga matriks $Q$ hanya berordo $3 \times 3$. Agar $P + Q$ dapat dihitung tanpa menambah data baru pada $Q$, pernyataan yang benar adalah ....
Pilihan: A. Kolom pemasok ke-4 pada $P$ dihapus sehingga $P$ berordo $3 \times 3$ dan $P + Q$ berordo $3 \times 3$
B. Baris ketiga pada $P$ dihapus sehingga $P$ berordo $2 \times 4$ dan $P + Q$ berordo $2 \times 4$
C. Kolom pemasok ke-1 pada $Q$ digandakan sehingga $Q$ berordo $3 \times 4$ dan $P + Q$ berordo $3 \times 4$
D. Kolom pemasok ke-4 pada $P$ dihapus sehingga $P + Q$ dapat dihitung dan berordo $3 \times 4$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 143. Soal `79a63bbbaa406feee5ada15a`

Penjualan roti (buah) sebuah toko pada pagi hari dicatat dalam matriks $M$ = $\begin{pmatrix} 38 & 52 & 23 \\ 45 & 17 & 60 \end{pmatrix}$ dan pada sore hari dalam matriks $N$ = $\begin{pmatrix} 27 & 33 & 14 \\ 19 & 41 & 25 \end{pmatrix}$, dengan baris menyatakan cabang (Utara, Selatan) dan kolom menyatakan jenis roti (tawar, manis, keju). Pernyataan yang benar mengenai elemen baris ke-2 kolom ke-3 matriks $M + N$ adalah ....

| Opsi | Isi |
|---|---|
| A | total roti manis yang terjual di cabang Selatan sepanjang hari, yaitu 58 buah |
| B | selisih penjualan roti keju pagi dan sore di cabang Selatan, yaitu 35 buah |
| C | total roti keju yang terjual di cabang Utara sepanjang hari, yaitu 37 buah |
| D | total roti keju yang terjual di cabang Selatan sepanjang hari, yaitu 85 buah |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b2b3f64e8542240a010bb5a9a406c89ab799d89c0db6baa099884889e16d9208`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Penjualan roti (buah) sebuah toko pada pagi hari dicatat dalam matriks $M$ = $\begin{pmatrix} 38 & 52 & 23 \\ 45 & 17 & 60 \end{pmatrix}$ dan pada sore hari dalam matriks $N$ = $\begin{pmatrix} 27 & 33 & 14 \\ 19 & 41 & 25 \end{pmatrix}$, dengan baris menyatakan cabang (Utara, Selatan) dan kolom menyatakan jenis roti (tawar, manis, keju). Pernyataan yang benar mengenai elemen baris ke-2 kolom ke-3 matriks $M + N$ adalah ....
Pilihan: A. total roti manis yang terjual di cabang Selatan sepanjang hari, yaitu 58 buah
B. selisih penjualan roti keju pagi dan sore di cabang Selatan, yaitu 35 buah
C. total roti keju yang terjual di cabang Utara sepanjang hari, yaitu 37 buah
D. total roti keju yang terjual di cabang Selatan sepanjang hari, yaitu 85 buah
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 144. Soal `04b4e13a04e957b402c73674`

Diketahui $A$ = $\begin{pmatrix} 6 & -1 \\ 3 & 8 \end{pmatrix}$, $B$ = $\begin{pmatrix} 2 & 5 \\ -4 & 1 \end{pmatrix}$, dan $C$ = $\begin{pmatrix} 3 & -2 \\ 7 & 4 \end{pmatrix}$. Pernyataan yang benar tentang $(A - B) - C$ dan $A - (B - C)$ adalah ....

| Opsi | Isi |
|---|---|
| A | kedua bentuk sama dengan $\begin{pmatrix} 1 & -4 \\ 0 & 3 \end{pmatrix}$ sehingga sifat asosiatif berlaku pada pengurangan |
| B | $(A - B) - C$ = $\begin{pmatrix} 7 & -8 \\ 14 & 11 \end{pmatrix}$ dan $A - (B - C)$ = $\begin{pmatrix} 1 & -4 \\ 0 & 3 \end{pmatrix}$ sehingga sifat asosiatif tidak berlaku pada pengurangan |
| C | $(A - B) - C$ = $\begin{pmatrix} 1 & -4 \\ 0 & 3 \end{pmatrix}$ dan $A - (B - C)$ = $\begin{pmatrix} 7 & -8 \\ 14 & 11 \end{pmatrix}$ sehingga sifat asosiatif tidak berlaku pada pengurangan |
| D | kedua bentuk sama dengan $\begin{pmatrix} 7 & -8 \\ 14 & 11 \end{pmatrix}$ sehingga sifat asosiatif berlaku pada pengurangan |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6c8b87980464dc64247ef27302b83c46a7c362e9f49de7c4148603e72d3d5110`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A$ = $\begin{pmatrix} 6 & -1 \\ 3 & 8 \end{pmatrix}$, $B$ = $\begin{pmatrix} 2 & 5 \\ -4 & 1 \end{pmatrix}$, dan $C$ = $\begin{pmatrix} 3 & -2 \\ 7 & 4 \end{pmatrix}$. Pernyataan yang benar tentang $(A - B) - C$ dan $A - (B - C)$ adalah ....
Pilihan: A. kedua bentuk sama dengan $\begin{pmatrix} 1 & -4 \\ 0 & 3 \end{pmatrix}$ sehingga sifat asosiatif berlaku pada pengurangan
B. $(A - B) - C$ = $\begin{pmatrix} 7 & -8 \\ 14 & 11 \end{pmatrix}$ dan $A - (B - C)$ = $\begin{pmatrix} 1 & -4 \\ 0 & 3 \end{pmatrix}$ sehingga sifat asosiatif tidak berlaku pada pengurangan
C. $(A - B) - C$ = $\begin{pmatrix} 1 & -4 \\ 0 & 3 \end{pmatrix}$ dan $A - (B - C)$ = $\begin{pmatrix} 7 & -8 \\ 14 & 11 \end{pmatrix}$ sehingga sifat asosiatif tidak berlaku pada pengurangan
D. kedua bentuk sama dengan $\begin{pmatrix} 7 & -8 \\ 14 & 11 \end{pmatrix}$ sehingga sifat asosiatif berlaku pada pengurangan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 145. Soal `b7b05c718f899c07c3a92d6e`

Matriks $A$, $B$, dan $C$ berordo sama. Bentuk paling sederhana dari $(A + B) - (B - C) - C$ adalah ....

| Opsi | Isi |
|---|---|
| A | $A$ |
| B | $A - 2C$ |
| C | $A + 2C$ |
| D | $O$ (matriks nol) |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `35ab42c5ca2a4eae0d938b3a66ade8eab3d867bf8eea5d2c4df596a0e968608a`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$, $B$, dan $C$ berordo sama. Bentuk paling sederhana dari $(A + B) - (B - C) - C$ adalah ....
Pilihan: A. $A$
B. $A - 2C$
C. $A + 2C$
D. $O$ (matriks nol)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 146. Soal `be3a1df7c6d74083b0f61881`

Matriks $A$, $B$, dan $C$ berordo $2 \times 2$ dengan $A + B$ = $\begin{pmatrix} 8 & -3 \\ 5 & 11 \end{pmatrix}$ dan $B - C$ = $\begin{pmatrix} 2 & 6 \\ -4 & 3 \end{pmatrix}$. Hasil $A + C$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix} 10 & 3 \\ 1 & 14 \end{pmatrix}$ |
| B | $\begin{pmatrix} -10 & -3 \\ -1 & -14 \end{pmatrix}$ |
| C | $\begin{pmatrix} -6 & 9 \\ -9 & -8 \end{pmatrix}$ |
| D | $\begin{pmatrix} 6 & -9 \\ 9 & 8 \end{pmatrix}$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8b98afca2e95e48bcf48008766cab71f480469b2a369138056ca52142085c447`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$, $B$, dan $C$ berordo $2 \times 2$ dengan $A + B$ = $\begin{pmatrix} 8 & -3 \\ 5 & 11 \end{pmatrix}$ dan $B - C$ = $\begin{pmatrix} 2 & 6 \\ -4 & 3 \end{pmatrix}$. Hasil $A + C$ adalah ....
Pilihan: A. $\begin{pmatrix} 10 & 3 \\ 1 & 14 \end{pmatrix}$
B. $\begin{pmatrix} -10 & -3 \\ -1 & -14 \end{pmatrix}$
C. $\begin{pmatrix} -6 & 9 \\ -9 & -8 \end{pmatrix}$
D. $\begin{pmatrix} 6 & -9 \\ 9 & 8 \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 147. Soal `618629d4e618298d91f6ea00`

Sebuah usaha konveksi mencatat biaya (dalam juta rupiah) di dua cabang untuk dua jenis pakaian (baris: cabang I dan II; kolom: kemeja dan jaket). Biaya kain adalah $\begin{pmatrix} 24 & 35 \\ 18 & 42 \end{pmatrix}$, biaya upah penjahit adalah $\begin{pmatrix} 9 & 12 \\ 7 & 15 \end{pmatrix}$, dan biaya pengiriman adalah $\begin{pmatrix} 4 & 6 \\ 3 & 5 \end{pmatrix}$. Matriks total biaya produksi ketiga komponen tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix} 37 & 53 \\ 28 & 62 \end{pmatrix}$ |
| B | $\begin{pmatrix} 11 & 17 \\ 8 & 22 \end{pmatrix}$ |
| C | $\begin{pmatrix} 29 & 41 \\ 22 & 52 \end{pmatrix}$ |
| D | $\begin{pmatrix} 33 & 47 \\ 25 & 57 \end{pmatrix}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2375a1bc4d114ec43206f1942da5951ee1a848a1507ac746c52831e4f214f5bc`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah usaha konveksi mencatat biaya (dalam juta rupiah) di dua cabang untuk dua jenis pakaian (baris: cabang I dan II; kolom: kemeja dan jaket). Biaya kain adalah $\begin{pmatrix} 24 & 35 \\ 18 & 42 \end{pmatrix}$, biaya upah penjahit adalah $\begin{pmatrix} 9 & 12 \\ 7 & 15 \end{pmatrix}$, dan biaya pengiriman adalah $\begin{pmatrix} 4 & 6 \\ 3 & 5 \end{pmatrix}$. Matriks total biaya produksi ketiga komponen tersebut adalah ....
Pilihan: A. $\begin{pmatrix} 37 & 53 \\ 28 & 62 \end{pmatrix}$
B. $\begin{pmatrix} 11 & 17 \\ 8 & 22 \end{pmatrix}$
C. $\begin{pmatrix} 29 & 41 \\ 22 & 52 \end{pmatrix}$
D. $\begin{pmatrix} 33 & 47 \\ 25 & 57 \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 148. Soal `f3c4fe5c4417269f15177e77`

Dua koperasi (A dan B) menerima kiriman tiga jenis beras (kg): $\begin{pmatrix} 58 & 41 \\ 36 & 75 \\ 64 & 29 \end{pmatrix}$, dengan baris menyatakan jenis beras dan kolom menyatakan koperasi (kolom pertama koperasi A, kolom kedua koperasi B). Setelah diperiksa, beras yang rusak dan tidak layak jual adalah $\begin{pmatrix} 7 & 3 \\ 0 & 9 \\ 5 & 2 \end{pmatrix}$. Total beras layak jual di koperasi B adalah .... kg.

| Opsi | Isi |
|---|---|
| A | $159$ |
| B | $146$ |
| C | $131$ |
| D | $145$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `04bd30544df129135ee918f7577032bfe3194da062b168953806de35ee57ea55`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Dua koperasi (A dan B) menerima kiriman tiga jenis beras (kg): $\begin{pmatrix} 58 & 41 \\ 36 & 75 \\ 64 & 29 \end{pmatrix}$, dengan baris menyatakan jenis beras dan kolom menyatakan koperasi (kolom pertama koperasi A, kolom kedua koperasi B). Setelah diperiksa, beras yang rusak dan tidak layak jual adalah $\begin{pmatrix} 7 & 3 \\ 0 & 9 \\ 5 & 2 \end{pmatrix}$. Total beras layak jual di koperasi B adalah .... kg.
Pilihan: A. $159$
B. $146$
C. $131$
D. $145$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 149. Soal `1b604a62df676b0641544208`

Penjualan tiga jenis sepatu (pasang) di dua toko dicatat tiap bulan, dengan baris menyatakan toko dan kolom menyatakan jenis sepatu. Penjualan Januari adalah $\begin{pmatrix} 34 & 28 & 19 \\ 41 & 25 & 36 \end{pmatrix}$ dan Februari adalah $\begin{pmatrix} 29 & 31 & 22 \\ 38 & 27 & 40 \end{pmatrix}$. Total penjualan selama Januari-Maret adalah $\begin{pmatrix} 95 & 89 & 64 \\ 120 & 81 & 115 \end{pmatrix}$. Matriks penjualan bulan Maret adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix} 158 & 148 & 105 \\ 199 & 133 & 191 \end{pmatrix}$ |
| B | $\begin{pmatrix} 32 & 30 & 23 \\ 41 & 29 & 39 \end{pmatrix}$ |
| C | $\begin{pmatrix} 61 & 61 & 45 \\ 79 & 56 & 79 \end{pmatrix}$ |
| D | $\begin{pmatrix} 90 & 92 & 67 \\ 117 & 83 & 119 \end{pmatrix}$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `994e26aec0a627fbd92da31b8824ff6ea6f6eb393fdd35a8b510b13df780e2ab`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Penjualan tiga jenis sepatu (pasang) di dua toko dicatat tiap bulan, dengan baris menyatakan toko dan kolom menyatakan jenis sepatu. Penjualan Januari adalah $\begin{pmatrix} 34 & 28 & 19 \\ 41 & 25 & 36 \end{pmatrix}$ dan Februari adalah $\begin{pmatrix} 29 & 31 & 22 \\ 38 & 27 & 40 \end{pmatrix}$. Total penjualan selama Januari-Maret adalah $\begin{pmatrix} 95 & 89 & 64 \\ 120 & 81 & 115 \end{pmatrix}$. Matriks penjualan bulan Maret adalah ....
Pilihan: A. $\begin{pmatrix} 158 & 148 & 105 \\ 199 & 133 & 191 \end{pmatrix}$
B. $\begin{pmatrix} 32 & 30 & 23 \\ 41 & 29 & 39 \end{pmatrix}$
C. $\begin{pmatrix} 61 & 61 & 45 \\ 79 & 56 & 79 \end{pmatrix}$
D. $\begin{pmatrix} 90 & 92 & 67 \\ 117 & 83 & 119 \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 150. Soal `6214b3e1fd56b2d6a3584cdf`

Diketahui $\begin{pmatrix} 2a & 5 \\ b+1 & 4 \end{pmatrix}$ - $\begin{pmatrix} 3 & c \\ 2b & -1 \end{pmatrix}$ = $\begin{pmatrix} 9 & -2 \\ -3 & 5 \end{pmatrix}$. Nilai $a + b + c$ adalah ....

| Opsi | Isi |
|---|---|
| A | $3$ |
| B | $14$ |
| C | $15$ |
| D | $17$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ff8ec8c4a01fcd8bdb79d22f0f266df6092b943ac2d2b0222e3eba843a558b7a`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $\begin{pmatrix} 2a & 5 \\ b+1 & 4 \end{pmatrix}$ - $\begin{pmatrix} 3 & c \\ 2b & -1 \end{pmatrix}$ = $\begin{pmatrix} 9 & -2 \\ -3 & 5 \end{pmatrix}$. Nilai $a + b + c$ adalah ....
Pilihan: A. $3$
B. $14$
C. $15$
D. $17$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 151. Soal `d81ed05681f1e5f57c85dc7b`

Matriks $A$ dan $B$ berordo $2 \times 2$ dengan $A + B$ = $\begin{pmatrix} 7 & 3 \\ 10 & -2 \end{pmatrix}$ dan $A - B$ = $\begin{pmatrix} 1 & 9 \\ 4 & 6 \end{pmatrix}$. Matriks $B$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix} 4 & 6 \\ 7 & 2 \end{pmatrix}$ |
| B | $\begin{pmatrix} -3 & 3 \\ -3 & 4 \end{pmatrix}$ |
| C | $\begin{pmatrix} 3 & -3 \\ 3 & -4 \end{pmatrix}$ |
| D | $\begin{pmatrix} 6 & -6 \\ 6 & -8 \end{pmatrix}$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8ccf7fc57b6bb9ebeca14f6e863182d43fb87aa90ea350a2ff3388e3d15e62bd`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$ dan $B$ berordo $2 \times 2$ dengan $A + B$ = $\begin{pmatrix} 7 & 3 \\ 10 & -2 \end{pmatrix}$ dan $A - B$ = $\begin{pmatrix} 1 & 9 \\ 4 & 6 \end{pmatrix}$. Matriks $B$ adalah ....
Pilihan: A. $\begin{pmatrix} 4 & 6 \\ 7 & 2 \end{pmatrix}$
B. $\begin{pmatrix} -3 & 3 \\ -3 & 4 \end{pmatrix}$
C. $\begin{pmatrix} 3 & -3 \\ 3 & -4 \end{pmatrix}$
D. $\begin{pmatrix} 6 & -6 \\ 6 & -8 \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 152. Soal `0a8601ea4433443d10b7aa84`

Diketahui $A$ = $\begin{pmatrix} 4 & -2 & 7 \\ 3 & 5 & -1 \\ 6 & 0 & 2 \end{pmatrix}$ dan $B$ = $\begin{pmatrix} 9 & 1 & -3 \\ -4 & 8 & 2 \\ 5 & -6 & 14 \end{pmatrix}$. Jika $X + A = B$, jumlah elemen pada diagonal utama matriks $X$ adalah ....

| Opsi | Isi |
|---|---|
| A | $-8$ |
| B | $42$ |
| C | $-20$ |
| D | $20$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c959d87c342e3f16f7caa13d0137e66f7038ebc6bdf18bc5e487e4fd04ee9825`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A$ = $\begin{pmatrix} 4 & -2 & 7 \\ 3 & 5 & -1 \\ 6 & 0 & 2 \end{pmatrix}$ dan $B$ = $\begin{pmatrix} 9 & 1 & -3 \\ -4 & 8 & 2 \\ 5 & -6 & 14 \end{pmatrix}$. Jika $X + A = B$, jumlah elemen pada diagonal utama matriks $X$ adalah ....
Pilihan: A. $-8$
B. $42$
C. $-20$
D. $20$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 153. Soal `af420cdf1df65e2a17fa52fb`

Matriks $P$ berordo $p \times q$ dan $h$ adalah suatu skalar. Pernyataan yang benar mengenai matriks $hP$ adalah ....

| Opsi | Isi |
|---|---|
| A | $hP$ berordo $1 \times 1$ |
| B | $hP$ berordo $p \times p$ |
| C | $hP$ berordo $p \times q$ |
| D | $hP$ berordo $q \times p$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5900c47e1ef1f6c4a42f54f2e74e29f64b6990b54a90e49973bd10191888d9e1`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $P$ berordo $p \times q$ dan $h$ adalah suatu skalar. Pernyataan yang benar mengenai matriks $hP$ adalah ....
Pilihan: A. $hP$ berordo $1 \times 1$
B. $hP$ berordo $p \times p$
C. $hP$ berordo $p \times q$
D. $hP$ berordo $q \times p$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 154. Soal `784560674e904e2e29c35b53`

Matriks $M$ berordo $4 \times 3$ dikalikan dengan skalar $5$ sehingga diperoleh matriks $5M$. Banyak elemen pada matriks $5M$ adalah ....

| Opsi | Isi |
|---|---|
| A | 7 |
| B | 12 |
| C | 20 |
| D | 60 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `78b2909800267033388e72d56f51e1452a107496b75dc8375c48a5c0bea1f607`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $M$ berordo $4 \times 3$ dikalikan dengan skalar $5$ sehingga diperoleh matriks $5M$. Banyak elemen pada matriks $5M$ adalah ....
Pilihan: A. 7
B. 12
C. 20
D. 60
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 155. Soal `092945fd68df6d3d5dedf5d3`

Diketahui $A$ matriks nol berordo $2 \times 2$ dan $B = \begin{pmatrix}7 & -4 \\ 5 & 9\end{pmatrix}$. Hasil perkalian $AB$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix}0 & 0 \\ 0 & 0\end{pmatrix}$ |
| B | $\begin{pmatrix}7 & 0 \\ 0 & 9\end{pmatrix}$ |
| C | $\begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix}$ |
| D | $\begin{pmatrix}7 & -4 \\ 5 & 9\end{pmatrix}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2b5e6dfbd85f6a46a0b5fd77a79a986bbc64c8a5830a83fb1c03db80a5ab84fd`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A$ matriks nol berordo $2 \times 2$ dan $B = \begin{pmatrix}7 & -4 \\ 5 & 9\end{pmatrix}$. Hasil perkalian $AB$ adalah ....
Pilihan: A. $\begin{pmatrix}0 & 0 \\ 0 & 0\end{pmatrix}$
B. $\begin{pmatrix}7 & 0 \\ 0 & 9\end{pmatrix}$
C. $\begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix}$
D. $\begin{pmatrix}7 & -4 \\ 5 & 9\end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 156. Soal `c2b717e4b926ea082bbffc03`

Misalkan $O$ matriks nol berordo $3 \times 3$ dan $C$ sembarang matriks berordo $3 \times 3$. Pernyataan yang benar adalah ....

| Opsi | Isi |
|---|---|
| A | $CO = C$ |
| B | $CO = I$ |
| C | $CO$ tidak terdefinisi |
| D | $CO = O$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `835901416163e4e1b3f622ba0809c6ec55d51582e8dd157ea83ef345462a405d`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Misalkan $O$ matriks nol berordo $3 \times 3$ dan $C$ sembarang matriks berordo $3 \times 3$. Pernyataan yang benar adalah ....
Pilihan: A. $CO = C$
B. $CO = I$
C. $CO$ tidak terdefinisi
D. $CO = O$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 157. Soal `a7908637c795c913bdc24e61`

Matriks bukan nol berordo $2 \times 2$ berikut yang memenuhi $AA = A$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix}2 & 0 \\ 0 & 2\end{pmatrix}$ |
| B | $\begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix}$ |
| C | $\begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix}$ |
| D | $\begin{pmatrix}-1 & 0 \\ 0 & -1\end{pmatrix}$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `57dfae6d78718e97f753e6df344a1cdda1732ed35203ef2abcc51038145a1e07`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks bukan nol berordo $2 \times 2$ berikut yang memenuhi $AA = A$ adalah ....
Pilihan: A. $\begin{pmatrix}2 & 0 \\ 0 & 2\end{pmatrix}$
B. $\begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix}$
C. $\begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix}$
D. $\begin{pmatrix}-1 & 0 \\ 0 & -1\end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 158. Soal `7a09d2ea220f172612b4db01`

Diketahui $A = \begin{pmatrix}1 & 0 \\ 0 & 0\end{pmatrix}$. Pernyataan yang benar adalah ....

| Opsi | Isi |
|---|---|
| A | $AA = O$ |
| B | $AA = 2A$ |
| C | $A$ bukan matriks nol dan $AA = A$ |
| D | $AA = I$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1e6d674ff36db5b8f0a53193fbb0b4118b934b070b3e8a0328b2ea6a1534ee25`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix}1 & 0 \\ 0 & 0\end{pmatrix}$. Pernyataan yang benar adalah ....
Pilihan: A. $AA = O$
B. $AA = 2A$
C. $A$ bukan matriks nol dan $AA = A$
D. $AA = I$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 159. Soal `ff7f85b23aa8e4518bd878dd`

Pernyataan yang benar tentang perkalian dua matriks $A$ dan $B$ yang berordo $2 \times 2$ adalah ....

| Opsi | Isi |
|---|---|
| A | $AB = BA$ selalu berlaku jika semua elemen $A$ dan $B$ bukan nol |
| B | Ada pasangan $A$ dan $B$ sehingga $AB \neq BA$ |
| C | $AB$ terdefinisi tetapi $BA$ tidak terdefinisi |
| D | $AB = BA$ berlaku untuk setiap pasangan $A$ dan $B$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a47f80640245aab182e653ef9c53ac889e48da83269e7917c3d546bc0ea14c5f`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Pernyataan yang benar tentang perkalian dua matriks $A$ dan $B$ yang berordo $2 \times 2$ adalah ....
Pilihan: A. $AB = BA$ selalu berlaku jika semua elemen $A$ dan $B$ bukan nol
B. Ada pasangan $A$ dan $B$ sehingga $AB \neq BA$
C. $AB$ terdefinisi tetapi $BA$ tidak terdefinisi
D. $AB = BA$ berlaku untuk setiap pasangan $A$ dan $B$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 160. Soal `39515aba73eab3e428217d94`

Sebuah bengkel memiliki $6$ montir tetap dan $4$ montir paruh waktu. Gaji per hari montir tetap Rp150.000,00 dan montir paruh waktu Rp90.000,00. Gaji dalam ribu rupiah dinyatakan oleh matriks $\begin{pmatrix}6 & 4\end{pmatrix}\begin{pmatrix}150 \\ 90\end{pmatrix}$. Total gaji yang harus dibayar bengkel per hari adalah ....

| Opsi | Isi |
|---|---|
| A | Rp1.140.000,00 |
| B | Rp126.000,00 |
| C | Rp240.000,00 |
| D | Rp1.260.000,00 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `41fa551549810d6a123b4b2937b8c32cdaaf200f7d5494aae1669d7f38b52f8b`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah bengkel memiliki $6$ montir tetap dan $4$ montir paruh waktu. Gaji per hari montir tetap Rp150.000,00 dan montir paruh waktu Rp90.000,00. Gaji dalam ribu rupiah dinyatakan oleh matriks $\begin{pmatrix}6 & 4\end{pmatrix}\begin{pmatrix}150 \\ 90\end{pmatrix}$. Total gaji yang harus dibayar bengkel per hari adalah ....
Pilihan: A. Rp1.140.000,00
B. Rp126.000,00
C. Rp240.000,00
D. Rp1.260.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 161. Soal `c570816d38711fed4c4f3b24`

Dua cabang usaha memiliki karyawan tetap dan karyawan paruh waktu yang dinyatakan oleh matriks $A = \begin{pmatrix}300 & 90 \\ 260 & 110\end{pmatrix}$ (baris: cabang I dan II; kolom: tetap dan paruh waktu). Gaji per hari (ribu rupiah) dinyatakan oleh $B = \begin{pmatrix}175 \\ 60\end{pmatrix}$. Dana gaji per hari untuk cabang II adalah ....

| Opsi | Isi |
|---|---|
| A | Rp57.900.000,00 |
| B | Rp5.210.000,00 |
| C | Rp34.850.000,00 |
| D | Rp52.100.000,00 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `92495bff5fcbfbfa4d86ce5be2dd5addb7f99e5de40108a3b03b8e4a27ea53b1`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Dua cabang usaha memiliki karyawan tetap dan karyawan paruh waktu yang dinyatakan oleh matriks $A = \begin{pmatrix}300 & 90 \\ 260 & 110\end{pmatrix}$ (baris: cabang I dan II; kolom: tetap dan paruh waktu). Gaji per hari (ribu rupiah) dinyatakan oleh $B = \begin{pmatrix}175 \\ 60\end{pmatrix}$. Dana gaji per hari untuk cabang II adalah ....
Pilihan: A. Rp57.900.000,00
B. Rp5.210.000,00
C. Rp34.850.000,00
D. Rp52.100.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 162. Soal `eab14272b1eb1388ea8e0de1`

Sebuah toko roti menjual roti tawar, roti manis, dan roti keju. Banyak roti yang terjual dinyatakan oleh $\begin{pmatrix}14 & 9 & 11\end{pmatrix}$ dan harga per buah (ribu rupiah) oleh $\begin{pmatrix}25 \\ 35 \\ 18\end{pmatrix}$. Pendapatan toko jika semua roti terjual adalah ....

| Opsi | Isi |
|---|---|
| A | Rp86.300,00 |
| B | Rp913.000,00 |
| C | Rp863.000,00 |
| D | Rp2.652.000,00 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `bb78c6652dd119e8d1ae2b923dcb1fae3cf1bd70ed5e2aedb37d56d0df32b382`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah toko roti menjual roti tawar, roti manis, dan roti keju. Banyak roti yang terjual dinyatakan oleh $\begin{pmatrix}14 & 9 & 11\end{pmatrix}$ dan harga per buah (ribu rupiah) oleh $\begin{pmatrix}25 \\ 35 \\ 18\end{pmatrix}$. Pendapatan toko jika semua roti terjual adalah ....
Pilihan: A. Rp86.300,00
B. Rp913.000,00
C. Rp863.000,00
D. Rp2.652.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 163. Soal `edf3835a47c48a07494c606f`

Matriks tabungan tiga anggota koperasi (dalam rupiah) adalah $\begin{pmatrix}1500000 \\ 2800000 \\ 5000000\end{pmatrix}$. Jika suku bunga tunggal $8\%$ per tahun, matriks besarnya bunga setelah satu tahun (dalam rupiah) adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix}1580000 \\ 2880000 \\ 5080000\end{pmatrix}$ |
| B | $\begin{pmatrix}12000 \\ 22400 \\ 40000\end{pmatrix}$ |
| C | $\begin{pmatrix}120000 \\ 224000 \\ 400000\end{pmatrix}$ |
| D | $\begin{pmatrix}1200000 \\ 2240000 \\ 4000000\end{pmatrix}$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `02496b0fff037d6f2c81633dba6786b35ccb0b4636d6867fe3395eb5f18d514a`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks tabungan tiga anggota koperasi (dalam rupiah) adalah $\begin{pmatrix}1500000 \\ 2800000 \\ 5000000\end{pmatrix}$. Jika suku bunga tunggal $8\%$ per tahun, matriks besarnya bunga setelah satu tahun (dalam rupiah) adalah ....
Pilihan: A. $\begin{pmatrix}1580000 \\ 2880000 \\ 5080000\end{pmatrix}$
B. $\begin{pmatrix}12000 \\ 22400 \\ 40000\end{pmatrix}$
C. $\begin{pmatrix}120000 \\ 224000 \\ 400000\end{pmatrix}$
D. $\begin{pmatrix}1200000 \\ 2240000 \\ 4000000\end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 164. Soal `ffd60ee202aa37088a639aaa`

Matriks $A$ berordo $3 \times 2$ dan matriks $B$ berordo $2 \times 5$. Ordo matriks $AB$ adalah ....

| Opsi | Isi |
|---|---|
| A | $3 \times 5$ |
| B | $2 \times 2$ |
| C | $3 \times 2$ |
| D | $5 \times 3$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7a12442e14579511ec24bbe7ef6bef0f842a0e6566ee0bf0b74518648b357c38`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$ berordo $3 \times 2$ dan matriks $B$ berordo $2 \times 5$. Ordo matriks $AB$ adalah ....
Pilihan: A. $3 \times 5$
B. $2 \times 2$
C. $3 \times 2$
D. $5 \times 3$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 165. Soal `23ed83ac30f273d592b6c84d`

Matriks $P$ berordo $2 \times 3$. Agar hasil kali $PQ$ terdefinisi, ordo matriks $Q$ yang mungkin adalah ....

| Opsi | Isi |
|---|---|
| A | $2 \times 2$ |
| B | $4 \times 3$ |
| C | $3 \times 4$ |
| D | $2 \times 3$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `65cba1f7fb86765475c0ec3fd03d4f7499cabfde343521751871e6fab2332146`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $P$ berordo $2 \times 3$. Agar hasil kali $PQ$ terdefinisi, ordo matriks $Q$ yang mungkin adalah ....
Pilihan: A. $2 \times 2$
B. $4 \times 3$
C. $3 \times 4$
D. $2 \times 3$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 166. Soal `1606ddba4b92692fd7204a12`

Matriks $A$ berordo $4 \times 2$ dan matriks $B$ berordo $3 \times 4$. Pernyataan yang benar adalah ....

| Opsi | Isi |
|---|---|
| A | $BA$ terdefinisi dan berordo $3 \times 2$ |
| B | $BA$ terdefinisi dan berordo $4 \times 3$ |
| C | $AB$ terdefinisi dan berordo $4 \times 3$ |
| D | $BA$ tidak terdefinisi |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5305dc19de6b6afbd48a58914dbe556d2ce7079022167968208820cf6503e526`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$ berordo $4 \times 2$ dan matriks $B$ berordo $3 \times 4$. Pernyataan yang benar adalah ....
Pilihan: A. $BA$ terdefinisi dan berordo $3 \times 2$
B. $BA$ terdefinisi dan berordo $4 \times 3$
C. $AB$ terdefinisi dan berordo $4 \times 3$
D. $BA$ tidak terdefinisi
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 167. Soal `f7f33df16bb1903fa8fee189`

Diketahui $A = \begin{pmatrix}2 & -1 \\ 3 & 4\end{pmatrix}$ dan $B = \begin{pmatrix}5 & 0 \\ -2 & 6\end{pmatrix}$. Elemen baris ke-2 kolom ke-1 pada $AB$ adalah ....

| Opsi | Isi |
|---|---|
| A | 24 |
| B | 23 |
| C | 12 |
| D | 7 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f7c2c69ec78ed4190e1806590555963e991f75cbcbdec320f0c73531b0ed502e`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix}2 & -1 \\ 3 & 4\end{pmatrix}$ dan $B = \begin{pmatrix}5 & 0 \\ -2 & 6\end{pmatrix}$. Elemen baris ke-2 kolom ke-1 pada $AB$ adalah ....
Pilihan: A. 24
B. 23
C. 12
D. 7
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 168. Soal `9206bbb9ecd9cee1b53109c1`

Diketahui $A = \begin{pmatrix}4 & -2 \\ 1 & 6\end{pmatrix}$. Matriks $-3A$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix}-12 & 6 \\ -3 & -18\end{pmatrix}$ |
| B | $\begin{pmatrix}1 & -5 \\ -2 & 3\end{pmatrix}$ |
| C | $\begin{pmatrix}12 & -6 \\ 3 & 18\end{pmatrix}$ |
| D | $\begin{pmatrix}-12 & -2 \\ -3 & -18\end{pmatrix}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ec2c45a7acda0ba6a62799288e055cf27ab22d375e013dc1fd7812944f8eaf09`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix}4 & -2 \\ 1 & 6\end{pmatrix}$. Matriks $-3A$ adalah ....
Pilihan: A. $\begin{pmatrix}-12 & 6 \\ -3 & -18\end{pmatrix}$
B. $\begin{pmatrix}1 & -5 \\ -2 & 3\end{pmatrix}$
C. $\begin{pmatrix}12 & -6 \\ 3 & 18\end{pmatrix}$
D. $\begin{pmatrix}-12 & -2 \\ -3 & -18\end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 169. Soal `b68699876fbeac3efdf3ef16`

Diketahui $A = \begin{pmatrix}1 & -2 \\ 4 & 3\end{pmatrix}$. Matriks $2(3A)$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix}8 & -16 \\ 32 & 24\end{pmatrix}$ |
| B | $\begin{pmatrix}6 & -12 \\ 24 & 18\end{pmatrix}$ |
| C | $\begin{pmatrix}5 & -10 \\ 20 & 15\end{pmatrix}$ |
| D | $\begin{pmatrix}6 & -2 \\ 4 & 3\end{pmatrix}$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6c729d309b49caab60af8aa65e2139a3ff0909536a66ced97e926cabdcff601a`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix}1 & -2 \\ 4 & 3\end{pmatrix}$. Matriks $2(3A)$ adalah ....
Pilihan: A. $\begin{pmatrix}8 & -16 \\ 32 & 24\end{pmatrix}$
B. $\begin{pmatrix}6 & -12 \\ 24 & 18\end{pmatrix}$
C. $\begin{pmatrix}5 & -10 \\ 20 & 15\end{pmatrix}$
D. $\begin{pmatrix}6 & -2 \\ 4 & 3\end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 170. Soal `159c6bb388f1eee5b36b245e`

Diketahui $A = \begin{pmatrix}2 & 1 \\ -1 & 3\end{pmatrix}$ dan $B = \begin{pmatrix}4 & -2 \\ 0 & 5\end{pmatrix}$. Matriks $AB$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix}8 & 1 \\ -4 & 17\end{pmatrix}$ |
| B | $\begin{pmatrix}10 & -2 \\ -5 & 15\end{pmatrix}$ |
| C | $\begin{pmatrix}8 & -2 \\ 0 & 15\end{pmatrix}$ |
| D | $\begin{pmatrix}8 & 9 \\ -4 & 13\end{pmatrix}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `37884932657368fed29648d075a1cbbaed12863d250c32bd81953f2ebf137bcf`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix}2 & 1 \\ -1 & 3\end{pmatrix}$ dan $B = \begin{pmatrix}4 & -2 \\ 0 & 5\end{pmatrix}$. Matriks $AB$ adalah ....
Pilihan: A. $\begin{pmatrix}8 & 1 \\ -4 & 17\end{pmatrix}$
B. $\begin{pmatrix}10 & -2 \\ -5 & 15\end{pmatrix}$
C. $\begin{pmatrix}8 & -2 \\ 0 & 15\end{pmatrix}$
D. $\begin{pmatrix}8 & 9 \\ -4 & 13\end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 171. Soal `3a6127a737598e3a077157da`

Diketahui $A = \begin{pmatrix}2 & -3 \\ 5 & 7\end{pmatrix}$ dan $I$ matriks identitas berordo $2 \times 2$. Matriks $AI$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix}2 & 0 \\ 0 & 7\end{pmatrix}$ |
| B | $\begin{pmatrix}2 & -3 \\ 5 & 7\end{pmatrix}$ |
| C | $\begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix}$ |
| D | $\begin{pmatrix}0 & 0 \\ 0 & 0\end{pmatrix}$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7f51d62a41310b4e3aabc930cade318b8f5e45f0e7ad047231bba8d7a4e957c9`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix}2 & -3 \\ 5 & 7\end{pmatrix}$ dan $I$ matriks identitas berordo $2 \times 2$. Matriks $AI$ adalah ....
Pilihan: A. $\begin{pmatrix}2 & 0 \\ 0 & 7\end{pmatrix}$
B. $\begin{pmatrix}2 & -3 \\ 5 & 7\end{pmatrix}$
C. $\begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix}$
D. $\begin{pmatrix}0 & 0 \\ 0 & 0\end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 172. Soal `e7bd3c0911b7c0fe31655d13`

Matriks $A$ berordo $3 \times 2$. Hasil $0 \cdot A$ adalah ....

| Opsi | Isi |
|---|---|
| A | Matriks $A$ sendiri |
| B | Bilangan $0$ |
| C | Matriks nol berordo $2 \times 3$ |
| D | Matriks nol berordo $3 \times 2$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `435be3d4d91c94d2786b96fa93375a4b1afa17246bfb6875c60992d42b911966`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$ berordo $3 \times 2$. Hasil $0 \cdot A$ adalah ....
Pilihan: A. Matriks $A$ sendiri
B. Bilangan $0$
C. Matriks nol berordo $2 \times 3$
D. Matriks nol berordo $3 \times 2$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 173. Soal `20c5f524f1b12c70324839c7`

Seorang siswa menyatakan bahwa jika $AB = O$ maka $A = O$ atau $B = O$. Diketahui $A = \begin{pmatrix}2 & 4 \\ 1 & 2\end{pmatrix}$ dan $B = \begin{pmatrix}6 & -2 \\ -3 & 1\end{pmatrix}$. Pernyataan yang benar tentang $A$ dan $B$ adalah ....

| Opsi | Isi |
|---|---|
| A | $B = O$ karena semua elemen $AB$ bernilai nol |
| B | $AB = O$, $A \neq O$, $B \neq O$, dan $BA = O$ |
| C | $AB = O$ padahal $A \neq O$ dan $B \neq O$, tetapi $BA \neq O$ |
| D | $AB \neq O$ karena $A \neq O$ dan $B \neq O$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4f6cb391d931d185943ba212571ee9042352447af87f96c29f47f0e596a3a8f6`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Seorang siswa menyatakan bahwa jika $AB = O$ maka $A = O$ atau $B = O$. Diketahui $A = \begin{pmatrix}2 & 4 \\ 1 & 2\end{pmatrix}$ dan $B = \begin{pmatrix}6 & -2 \\ -3 & 1\end{pmatrix}$. Pernyataan yang benar tentang $A$ dan $B$ adalah ....
Pilihan: A. $B = O$ karena semua elemen $AB$ bernilai nol
B. $AB = O$, $A \neq O$, $B \neq O$, dan $BA = O$
C. $AB = O$ padahal $A \neq O$ dan $B \neq O$, tetapi $BA \neq O$
D. $AB \neq O$ karena $A \neq O$ dan $B \neq O$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 174. Soal `315ed1a21d696e94e4e91ba7`

Seorang siswa menyimpulkan bahwa $AB = AC$ berarti $B = C$ karena $A$ boleh dicoret. Diketahui $A = \begin{pmatrix}1 & 2 \\ 2 & 4\end{pmatrix}$, $B = \begin{pmatrix}3 & 6 \\ 3 & -1\end{pmatrix}$, dan $C = \begin{pmatrix}1 & 0 \\ 4 & 2\end{pmatrix}$. Pernyataan yang benar adalah ....

| Opsi | Isi |
|---|---|
| A | $AB \neq AC$, sehingga $B \neq C$ |
| B | $BA = CA$, sehingga $B = C$ |
| C | $AB = AC$ dan $B = C$ |
| D | $AB = AC$ walaupun $B \neq C$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `36449176cd3048f9131132363f3cffecdade9c6dd74795ce688cd5aa43ac1471`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Seorang siswa menyimpulkan bahwa $AB = AC$ berarti $B = C$ karena $A$ boleh dicoret. Diketahui $A = \begin{pmatrix}1 & 2 \\ 2 & 4\end{pmatrix}$, $B = \begin{pmatrix}3 & 6 \\ 3 & -1\end{pmatrix}$, dan $C = \begin{pmatrix}1 & 0 \\ 4 & 2\end{pmatrix}$. Pernyataan yang benar adalah ....
Pilihan: A. $AB \neq AC$, sehingga $B \neq C$
B. $BA = CA$, sehingga $B = C$
C. $AB = AC$ dan $B = C$
D. $AB = AC$ walaupun $B \neq C$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 175. Soal `874b7a2f1ff665f6ff8d70be`

Diketahui $A = \begin{pmatrix}2 & 1 \\ 3 & 4\end{pmatrix}$ dan $B = \begin{pmatrix}1 & 5 \\ 2 & 3\end{pmatrix}$. Seorang siswa menyatakan $(A-B)^2 = A^2 - 2AB + B^2$. Matriks $(A-B)^2 - (A^2 - 2AB + B^2)$ sebenarnya sama dengan ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix}21 & 34 \\ 24 & 41\end{pmatrix}$ |
| B | $O$ |
| C | $\begin{pmatrix}-13 & -8 \\ -2 & 13\end{pmatrix}$ |
| D | $\begin{pmatrix}13 & 8 \\ 2 & -13\end{pmatrix}$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d698e0afa1e49c559d92b4957db405883c2006bc95af7975353942dbb714aca1`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix}2 & 1 \\ 3 & 4\end{pmatrix}$ dan $B = \begin{pmatrix}1 & 5 \\ 2 & 3\end{pmatrix}$. Seorang siswa menyatakan $(A-B)^2 = A^2 - 2AB + B^2$. Matriks $(A-B)^2 - (A^2 - 2AB + B^2)$ sebenarnya sama dengan ....
Pilihan: A. $\begin{pmatrix}21 & 34 \\ 24 & 41\end{pmatrix}$
B. $O$
C. $\begin{pmatrix}-13 & -8 \\ -2 & 13\end{pmatrix}$
D. $\begin{pmatrix}13 & 8 \\ 2 & -13\end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 176. Soal `d920eb3d3291a299d9e14723`

Diketahui $A = \begin{pmatrix}2 & 5 \\ 3 & x\end{pmatrix}$ dan $B = \begin{pmatrix}7 & 10 \\ 6 & 9\end{pmatrix}$. Nilai $x$ yang membuat $AB = BA$ adalah ....

| Opsi | Isi |
|---|---|
| A | $3$ |
| B | $6$ |
| C | $5$ |
| D | $4$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `794715151713a64ca704b15be98c517e6ead72c96dccc04a677fcac17610f718`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix}2 & 5 \\ 3 & x\end{pmatrix}$ dan $B = \begin{pmatrix}7 & 10 \\ 6 & 9\end{pmatrix}$. Nilai $x$ yang membuat $AB = BA$ adalah ....
Pilihan: A. $3$
B. $6$
C. $5$
D. $4$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 177. Soal `ef79f3762293bb71c4ca90cf`

Diketahui $A = \begin{pmatrix}1 & 7 \\ 0 & 1\end{pmatrix}$. Elemen baris 1 kolom 2 dari $A^{12}$ adalah ....

| Opsi | Isi |
|---|---|
| A | $77$ |
| B | $84$ |
| C | $12$ |
| D | $19$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6b108346af7bd10a377864b56bb699bf91edeaf6e1ce134abe241fac84ffc295`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix}1 & 7 \\ 0 & 1\end{pmatrix}$. Elemen baris 1 kolom 2 dari $A^{12}$ adalah ....
Pilihan: A. $77$
B. $84$
C. $12$
D. $19$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 178. Soal `0737547ae3e3acfbdfd22019`

Diketahui $A = \begin{pmatrix}0 & 1 \\ -1 & 0\end{pmatrix}$. Jumlah semua elemen matriks $A^{2026}$ adalah ....

| Opsi | Isi |
|---|---|
| A | $0$ |
| B | $2$ |
| C | $-1$ |
| D | $-2$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e52deff36a9aa1e27f45937bba39d7a8c964d836f90c066aa3fcbbf2c606b4be`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix}0 & 1 \\ -1 & 0\end{pmatrix}$. Jumlah semua elemen matriks $A^{2026}$ adalah ....
Pilihan: A. $0$
B. $2$
C. $-1$
D. $-2$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 179. Soal `161e52bccf0c00f8222eeb77`

Matriks $A = \begin{pmatrix}3 & -6 \\ 1 & x\end{pmatrix}$ memenuhi $AA = A$. Nilai $x$ adalah ....

| Opsi | Isi |
|---|---|
| A | $3$ |
| B | $-2$ |
| C | $-3$ |
| D | $2$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1d730a1b2ff7b71aa32d3b013838fdecc8aa24c2423fb83d0c7f5f7d8f3bdee1`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A = \begin{pmatrix}3 & -6 \\ 1 & x\end{pmatrix}$ memenuhi $AA = A$. Nilai $x$ adalah ....
Pilihan: A. $3$
B. $-2$
C. $-3$
D. $2$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 180. Soal `98024154a6211080df8020d6`

Matriks $A = \begin{pmatrix}3 & -9 \\ 1 & x\end{pmatrix}$ memenuhi $AA = O$. Nilai $x$ adalah ....

| Opsi | Isi |
|---|---|
| A | $9$ |
| B | $-1$ |
| C | $-3$ |
| D | $3$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `344fd4352ed1b1082a9b9479051a2642a3059cf03446552ba3741f1e7baf371f`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A = \begin{pmatrix}3 & -9 \\ 1 & x\end{pmatrix}$ memenuhi $AA = O$. Nilai $x$ adalah ....
Pilihan: A. $9$
B. $-1$
C. $-3$
D. $3$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 181. Soal `1980dd55042d466faf047a73`

Diketahui $A = \begin{pmatrix}2 & 6 \\ 1 & 3\end{pmatrix}$. Matriks $B$ yang bukan matriks nol dan memenuhi $AB = O$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix}-1 & 2 \\ 3 & -6\end{pmatrix}$ |
| B | $\begin{pmatrix}1 & 3 \\ -2 & -6\end{pmatrix}$ |
| C | $\begin{pmatrix}3 & -6 \\ -1 & 2\end{pmatrix}$ |
| D | $\begin{pmatrix}3 & -6 \\ 1 & -2\end{pmatrix}$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `335c01dcca9d7192589f81a89219815d6e5d07d9bf1522ab1f316b600e4aa164`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix}2 & 6 \\ 1 & 3\end{pmatrix}$. Matriks $B$ yang bukan matriks nol dan memenuhi $AB = O$ adalah ....
Pilihan: A. $\begin{pmatrix}-1 & 2 \\ 3 & -6\end{pmatrix}$
B. $\begin{pmatrix}1 & 3 \\ -2 & -6\end{pmatrix}$
C. $\begin{pmatrix}3 & -6 \\ -1 & 2\end{pmatrix}$
D. $\begin{pmatrix}3 & -6 \\ 1 & -2\end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 182. Soal `53f83b74fb0a1cd1776b0f6b`

Diketahui $A = \begin{pmatrix}2 & -1 \\ 3 & 4\end{pmatrix}$ dan $B = \begin{pmatrix}5 & 1 \\ -2 & 6\end{pmatrix}$. Seorang siswa menuliskan $AB = \begin{pmatrix}12 & 8 \\ 7 & 27\end{pmatrix}$ dan hanya satu elemen yang salah. Elemen yang salah beserta nilai yang benar adalah ....

| Opsi | Isi |
|---|---|
| A | baris 2 kolom 2, seharusnya $8$ |
| B | baris 1 kolom 2, seharusnya $-4$ |
| C | baris 1 kolom 2, seharusnya $4$ |
| D | baris 2 kolom 1, seharusnya $-4$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b5cc45de0c2d2bd6991e74b2ed808241198ed0080bdf9750eaef2137e580142b`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix}2 & -1 \\ 3 & 4\end{pmatrix}$ dan $B = \begin{pmatrix}5 & 1 \\ -2 & 6\end{pmatrix}$. Seorang siswa menuliskan $AB = \begin{pmatrix}12 & 8 \\ 7 & 27\end{pmatrix}$ dan hanya satu elemen yang salah. Elemen yang salah beserta nilai yang benar adalah ....
Pilihan: A. baris 2 kolom 2, seharusnya $8$
B. baris 1 kolom 2, seharusnya $-4$
C. baris 1 kolom 2, seharusnya $4$
D. baris 2 kolom 1, seharusnya $-4$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 183. Soal `753235bba60f693a75e0f193`

Diketahui $A = \begin{pmatrix}3 & 1 \\ 2 & 4\end{pmatrix}$ dan $B = \begin{pmatrix}1 & -2 \\ 5 & 0\end{pmatrix}$. Seorang siswa menuliskan $AB = \begin{pmatrix}-1 & -7 \\ 15 & 5\end{pmatrix}$. Kesalahan siswa dan jumlah semua elemen $AB$ yang benar adalah ....

| Opsi | Isi |
|---|---|
| A | siswa menghitung $BA$ (urutan tertukar); jumlahnya $12$ |
| B | siswa menghitung $BA$ (urutan tertukar); jumlahnya $20$ |
| C | siswa salah tanda pada satu elemen; jumlahnya $12$ |
| D | siswa menjumlahkan, bukan mengalikan; jumlahnya $20$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `28e3a0e1ced964464657a289c425cab656060acee02878a501805a2a1e73407f`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix}3 & 1 \\ 2 & 4\end{pmatrix}$ dan $B = \begin{pmatrix}1 & -2 \\ 5 & 0\end{pmatrix}$. Seorang siswa menuliskan $AB = \begin{pmatrix}-1 & -7 \\ 15 & 5\end{pmatrix}$. Kesalahan siswa dan jumlah semua elemen $AB$ yang benar adalah ....
Pilihan: A. siswa menghitung $BA$ (urutan tertukar); jumlahnya $12$
B. siswa menghitung $BA$ (urutan tertukar); jumlahnya $20$
C. siswa salah tanda pada satu elemen; jumlahnya $12$
D. siswa menjumlahkan, bukan mengalikan; jumlahnya $20$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 184. Soal `4cd076a00320f587ac33dd03`

Banyak perkalian bilangan untuk mengalikan matriks berordo $m \times n$ dengan $n \times p$ adalah $m \cdot n \cdot p$. Matriks $A$ berordo $10 \times 2$, $B$ berordo $2 \times 10$, dan $C$ berordo $10 \times 1$. Hasil $ABC$ sama saja, tetapi selisih banyak perkalian bilangan antara cara $(AB)C$ dan cara $A(BC)$ adalah ....

| Opsi | Isi |
|---|---|
| A | $340$ |
| B | $40$ |
| C | $300$ |
| D | $260$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2ff4124057e783cb776c0be8a9033fe92a5809a636d6947f4bb1b34eddb3a143`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Banyak perkalian bilangan untuk mengalikan matriks berordo $m \times n$ dengan $n \times p$ adalah $m \cdot n \cdot p$. Matriks $A$ berordo $10 \times 2$, $B$ berordo $2 \times 10$, dan $C$ berordo $10 \times 1$. Hasil $ABC$ sama saja, tetapi selisih banyak perkalian bilangan antara cara $(AB)C$ dan cara $A(BC)$ adalah ....
Pilihan: A. $340$
B. $40$
C. $300$
D. $260$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 185. Soal `6ab1934b5b30416ccf89775d`

Banyak perkalian bilangan untuk mengalikan matriks berordo $m \times n$ dengan $n \times p$ adalah $m \cdot n \cdot p$. Matriks $A$ berordo $3 \times 40$, $B$ berordo $40 \times 2$, dan $C$ berordo $2 \times 50$. Banyak perkalian bilangan paling sedikit untuk memperoleh $ABC$ dengan memilih salah satu pengelompokan adalah ....

| Opsi | Isi |
|---|---|
| A | $540$ |
| B | $4.240$ |
| C | $10.540$ |
| D | $10.000$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `921ba02ac1d38a832214465ca84a868dfa760fec26d43ebe1fb2758bf9ddaf24`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Banyak perkalian bilangan untuk mengalikan matriks berordo $m \times n$ dengan $n \times p$ adalah $m \cdot n \cdot p$. Matriks $A$ berordo $3 \times 40$, $B$ berordo $40 \times 2$, dan $C$ berordo $2 \times 50$. Banyak perkalian bilangan paling sedikit untuk memperoleh $ABC$ dengan memilih salah satu pengelompokan adalah ....
Pilihan: A. $540$
B. $4.240$
C. $10.540$
D. $10.000$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 186. Soal `123e4528c06c909e1a39b611`

Matriks $A$ bukan matriks nol dan memenuhi $AA = A$, sedangkan $I$ matriks identitas seordo dengan $A$. Untuk $B = 2A - I$, hasil $B^2$ sama dengan ....

| Opsi | Isi |
|---|---|
| A | $O$ |
| B | $A$ |
| C | $4A - I$ |
| D | $I$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0457dcfd944479daf968c868d54b3054527c8f246c02e9a07ae8fe727fbd3b16`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$ bukan matriks nol dan memenuhi $AA = A$, sedangkan $I$ matriks identitas seordo dengan $A$. Untuk $B = 2A - I$, hasil $B^2$ sama dengan ....
Pilihan: A. $O$
B. $A$
C. $4A - I$
D. $I$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 187. Soal `d0e7211ecbf661798f877918`

Matriks $A$ bukan matriks nol, memenuhi $AA = O$, dan $I$ matriks identitas seordo dengan $A$. Hasil $(I + A)^4$ sama dengan ....

| Opsi | Isi |
|---|---|
| A | $I + 6A$ |
| B | $I + 4A$ |
| C | $I$ |
| D | $I + A$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `edc174b64f89837ae8e8ee928524af03ca63e10a644639436b800b726f6bf33a`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$ bukan matriks nol, memenuhi $AA = O$, dan $I$ matriks identitas seordo dengan $A$. Hasil $(I + A)^4$ sama dengan ....
Pilihan: A. $I + 6A$
B. $I + 4A$
C. $I$
D. $I + A$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 188. Soal `26fcce227cbeb739dba99eaa`

Diketahui $A = \begin{pmatrix}2 & 3 \\ 4 & 1\end{pmatrix}$ dan $I$ matriks identitas ordo $2 \times 2$. Jika $A^2 = pA + qI$, nilai $q - p$ adalah ....

| Opsi | Isi |
|---|---|
| A | $7$ |
| B | $10$ |
| C | $13$ |
| D | $-7$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2aa425ef618b6ad2d3599a7487927a439fc6119cbe97ce45528fdbcff2a803db`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix}2 & 3 \\ 4 & 1\end{pmatrix}$ dan $I$ matriks identitas ordo $2 \times 2$. Jika $A^2 = pA + qI$, nilai $q - p$ adalah ....
Pilihan: A. $7$
B. $10$
C. $13$
D. $-7$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 189. Soal `fc9cddbc320f636aa295a91f`

Matriks $A$, $B$, $C$ semuanya persegi seordo. Pernyataan yang selalu benar adalah ....

| Opsi | Isi |
|---|---|
| A | $(A + B)C = AC + BC$ |
| B | $(AB)^2 = A^2 B^2$ |
| C | $(A + B)^2 = A^2 + 2AB + B^2$ |
| D | jika $AB = AC$ maka $B = C$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5b670f1c158e4eb8fc9572343161c4c315b26e8f972dc1552a8b2bacd69a2fc1`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$, $B$, $C$ semuanya persegi seordo. Pernyataan yang selalu benar adalah ....
Pilihan: A. $(A + B)C = AC + BC$
B. $(AB)^2 = A^2 B^2$
C. $(A + B)^2 = A^2 + 2AB + B^2$
D. jika $AB = AC$ maka $B = C$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 190. Soal `4695c27392142a5db7f2c4b6`

Matriks $A$ dan $B$ persegi seordo, dan $I$ matriks identitas seordo. Pernyataan yang selalu benar adalah ....

| Opsi | Isi |
|---|---|
| A | jika $AB = O$ maka $BA = O$ |
| B | $(A + B)(A - B) = A^2 - B^2$ |
| C | $(A + I)(A - I) = A^2 - I$ |
| D | jika $A^2 = I$ maka $A = I$ atau $A = -I$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d108f53c76dbdb424a1f24e057d059f89b1ef7e8deeb7acef5b6b511264aeafb`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$ dan $B$ persegi seordo, dan $I$ matriks identitas seordo. Pernyataan yang selalu benar adalah ....
Pilihan: A. jika $AB = O$ maka $BA = O$
B. $(A + B)(A - B) = A^2 - B^2$
C. $(A + I)(A - I) = A^2 - I$
D. jika $A^2 = I$ maka $A = I$ atau $A = -I$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 191. Soal `ac1fab4f9af53aea4c941f62`

Diketahui $P = \begin{pmatrix}50 & 21 \\ 12 & 63\end{pmatrix}$ dan $Q = \begin{pmatrix}6 & 9 \\ -4 & 7\end{pmatrix}$. Matriks $X$ berordo $2 \times 2$ yang memenuhi $P - 4X = 5Q$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix}11 & 3 \\ 4 & 14\end{pmatrix}$ |
| B | $\begin{pmatrix}-20 & 24 \\ -32 & -28\end{pmatrix}$ |
| C | $\begin{pmatrix}20 & -24 \\ 32 & 28\end{pmatrix}$ |
| D | $\begin{pmatrix}5 & -6 \\ 8 & 7\end{pmatrix}$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `29b566d26dee889b149304966c26cc711da846782329db0e0a4e12a192b717ee`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $P = \begin{pmatrix}50 & 21 \\ 12 & 63\end{pmatrix}$ dan $Q = \begin{pmatrix}6 & 9 \\ -4 & 7\end{pmatrix}$. Matriks $X$ berordo $2 \times 2$ yang memenuhi $P - 4X = 5Q$ adalah ....
Pilihan: A. $\begin{pmatrix}11 & 3 \\ 4 & 14\end{pmatrix}$
B. $\begin{pmatrix}-20 & 24 \\ -32 & -28\end{pmatrix}$
C. $\begin{pmatrix}20 & -24 \\ 32 & 28\end{pmatrix}$
D. $\begin{pmatrix}5 & -6 \\ 8 & 7\end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 192. Soal `d7221e98976f376077153be8`

Diketahui $A = \begin{pmatrix}17 & -11 & -9 \\ 25 & 18 & -35\end{pmatrix}$ dan $B = \begin{pmatrix}6 & -3 & 8 \\ -5 & 4 & 5\end{pmatrix}$. Jika $X$ memenuhi $5X - A = 3B$, jumlah semua elemen matriks $X$ adalah ....

| Opsi | Isi |
|---|---|
| A | 4 |
| B | -8 |
| C | 50 |
| D | 10 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `25b0dd1bd9feab6b0f72ee7e5197b6e2433119f024008e91d28b19d6b52ee797`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix}17 & -11 & -9 \\ 25 & 18 & -35\end{pmatrix}$ dan $B = \begin{pmatrix}6 & -3 & 8 \\ -5 & 4 & 5\end{pmatrix}$. Jika $X$ memenuhi $5X - A = 3B$, jumlah semua elemen matriks $X$ adalah ....
Pilihan: A. 4
B. -8
C. 50
D. 10
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 193. Soal `6091556224652f1805d058a3`

Diketahui $egin{pmatrix}x+5 & 7 \ 6 & -8\end{pmatrix}egin{pmatrix}8 & 0 \ 5 & y-6\end{pmatrix} = egin{pmatrix}35 & 14 \ 8 & -16\end{pmatrix}$. Nilai $x - 2y$ adalah ....

| Opsi | Isi |
|---|---|
| A | -21 |
| B | -11 |
| C | -56 |
| D | 3 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Perform matrix multiplication for the first row: (x+5)(8) + (7)(5) = 35 => 8x + 40 + 35 = 35 => 8x = -40 => x = -5. For the (1,2) element: (x+5)(0) + (7)(y-6) = 14 => 7(y-6) = 14 => y-6 = 2 => y = 8. Thus, x - 2y = -5 - 2(8) = -5 - 16 = -21.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `71a425f5786f422ce1e34f801beb2709097c5abb34fb8e3ef769129a2bd3e8f2`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2867 |
| 2 | success | valid / verified | applying | procedural | Easy | 2967 |
| 3 | success | valid / verified | applying | procedural | Easy | 2931 |

Run 1 — solusi: Perform matrix multiplication for the first row: (x+5)(8) + (7)(5) = 35 => 8x + 40 + 35 = 35 => 8x = -40 => x = -5. For the (1,2) element: (x+5)(0) + (7)(y-6) = 14 => 7(y-6) = 14 => y-6 = 2 => y = 8. Thus, x - 2y = -5 - 2(8) = -5 - 16 = -21.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur perkalian matriks untuk membentuk sistem persamaan linear sederhana guna mencari nilai variabel x dan y, kemudian melakukan operasi aritmatika dasar untuk mendapatkan hasil akhir.. Bukti: Diketahui \begin{pmatrix}x+5 & 7 \ 6 & -8\end{pmatrix} \begin{pmatrix}8 & 0 \ 5 & y-6\end{pmatrix} =  \begin{pmatrix}35 & 14 \ 8 & -16\end{pmatrix}
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang algoritma perkalian matriks dan penyelesaian persamaan linear sederhana.. Bukti: Perkalian Matriks
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu melakukan perkalian matriks pada elemen-elemen yang relevan untuk mendapatkan nilai x dan y. Tidak ada kendala yang berinteraksi secara kompleks atau kebutuhan untuk strategi non-rutin.. Bukti: Nilai x - 2y adalah ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian matriks 2x2 dan penyelesaian persamaan linear satu variabel. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi matriks adalah standar kelas 11. Soal ini menguji prosedur dasar perkalian matriks tanpa variasi atau jebakan konseptual yang signifikan, sehingga tergolong mudah bagi siswa kelas 11. |

Run 2 — solusi: Perkalian matriks: elemen (1,1) adalah (x+5)(8) + (7)(5) = 8x + 40 + 35 = 8x + 75. Diketahui elemen (1,1) = 35, maka 8x + 75 = 35 => 8x = -40 => x = -5. Elemen (1,2) adalah (x+5)(0) + (7)(y-6) = 7y - 42. Diketahui elemen (1,2) = 14, maka 7y - 42 = 14 => 7y = 56 => y = 8. Nilai x - 2y = -5 - 2(8) = -5 - 16 = -21.
- Domain kognitif `classify/applying`: Siswa diminta melakukan operasi perkalian matriks standar dan menyelesaikan sistem persamaan linear sederhana untuk menemukan nilai variabel x dan y, kemudian menghitung nilai akhir. Ini adalah penerapan prosedur rutin.. Bukti: Diketahui (x+5 & 7 \ 6 & -8) (8 & 0 \ 5 & y-6) = (35 & 14 \ 8 & -16). Nilai x - 2y adalah ....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma perkalian matriks dan penyelesaian persamaan linear, yang merupakan pengetahuan prosedural.. Bukti: Diketahui (x+5 & 7 \ 6 & -8) (8 & 0 \ 5 & y-6) = (35 & 14 \ 8 & -16).
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu melakukan perkalian matriks 2x2 dan menyelesaikan persamaan linear satu variabel. Tidak ada kendala yang berinteraksi atau kebutuhan strategi non-rutin.. Bukti: Diketahui (x+5 & 7 \ 6 & -8) (8 & 0 \ 5 & y-6) = (35 & 14 \ 8 & -16). Nilai x - 2y adalah ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi matriks dasar dan aljabar linear dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi perkalian matriks adalah standar kelas 11. Soal ini tidak memerlukan manipulasi kompleks atau konsep lanjutan, sehingga dikategorikan mudah bagi siswa kelas 11. |

Run 3 — solusi: Perkalian matriks: elemen (1,1) adalah (x+5)(8) + (7)(5) = 8x + 40 + 35 = 8x + 75. Diketahui elemen (1,1) = 35, maka 8x + 75 = 35 => 8x = -40 => x = -5. Elemen (1,2) adalah (x+5)(0) + 7(y-6) = 7y - 42. Diketahui elemen (1,2) = 14, maka 7y - 42 = 14 => 7y = 56 => y = 8. Nilai x - 2y = -5 - 2(8) = -5 - 16 = -21.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur perkalian matriks untuk membentuk persamaan linear dari elemen matriks yang bersesuaian, kemudian menyelesaikan sistem persamaan linear sederhana untuk mendapatkan nilai variabel.. Bukti: Diketahui (x+5 & 7 \\ 6 & -8)(8 & 0 \\ 5 & y-6) = (35 & 14 \\ 8 & -16); Nilai x - 2y adalah
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang algoritma perkalian matriks dan penyelesaian persamaan linear.. Bukti: Perkalian matriks; Nilai x - 2y adalah
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu melakukan perkalian matriks pada elemen yang relevan (baris 1) untuk mendapatkan nilai x dan y. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Diketahui (x+5 & 7 \\ 6 & -8)(8 & 0 \\ 5 & y-6) = (35 & 14 \\ 8 & -16)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi perkalian matriks dan penyelesaian SPLDV sederhana. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi matriks adalah standar kelas 11. Soal ini adalah aplikasi langsung dari definisi perkalian matriks tanpa variasi kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $egin{pmatrix}x+5 & 7 \ 6 & -8\end{pmatrix}egin{pmatrix}8 & 0 \ 5 & y-6\end{pmatrix} = egin{pmatrix}35 & 14 \ 8 & -16\end{pmatrix}$. Nilai $x - 2y$ adalah ....
Pilihan: A. -21
B. -11
C. -56
D. 3
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 194. Soal `76f091541b2de74d77d1e769`

Diketahui $egin{pmatrix}7 & x \ 6 & 5\end{pmatrix}egin{pmatrix}y & 8 \ -5 & 11\end{pmatrix} = egin{pmatrix}79 & -10 \ 17 & 103\end{pmatrix}$. Nilai $2x - y$ adalah ....

| Opsi | Isi |
|---|---|
| A | -19 |
| B | -15 |
| C | -5 |
| D | 5 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4a9a48a7a9c075f1c98c008b423433a82a822a28a56a913818cb27728bf66ab4`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $egin{pmatrix}7 & x \ 6 & 5\end{pmatrix}egin{pmatrix}y & 8 \ -5 & 11\end{pmatrix} = egin{pmatrix}79 & -10 \ 17 & 103\end{pmatrix}$. Nilai $2x - y$ adalah ....
Pilihan: A. -19
B. -15
C. -5
D. 5
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 195. Soal `80efcaa0186da1dfbbff0ad9`

Sebuah usaha rumahan membuat sabun, lilin, dan dupa yang dikirim ke Toko X, Toko Y, dan Toko Z. Banyak barang (lusin) dinyatakan oleh matriks $P = \begin{pmatrix}17 & 13 & 21 \\ 24 & 19 & 11 \\ 14 & 26 & 18\end{pmatrix}$, dengan baris berturut-turut sabun, lilin, dan dupa, serta kolom berturut-turut Toko X, Toko Y, dan Toko Z. Harga per lusin (ribu rupiah) untuk sabun, lilin, dan dupa berturut-turut adalah 9, 14, dan 7. Pendapatan usaha tersebut dari Toko Y jika semua barang terjual adalah ....

| Opsi | Isi |
|---|---|
| A | Rp56.500,00 |
| B | Rp565.000,00 |
| C | Rp559.000,00 |
| D | Rp1.740.000,00 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c02a78d1087e10f7e504168f49f1ce34ace646c1238b51fafaecad2eebea9ffd`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah usaha rumahan membuat sabun, lilin, dan dupa yang dikirim ke Toko X, Toko Y, dan Toko Z. Banyak barang (lusin) dinyatakan oleh matriks $P = \begin{pmatrix}17 & 13 & 21 \\ 24 & 19 & 11 \\ 14 & 26 & 18\end{pmatrix}$, dengan baris berturut-turut sabun, lilin, dan dupa, serta kolom berturut-turut Toko X, Toko Y, dan Toko Z. Harga per lusin (ribu rupiah) untuk sabun, lilin, dan dupa berturut-turut adalah 9, 14, dan 7. Pendapatan usaha tersebut dari Toko Y jika semua barang terjual adalah ....
Pilihan: A. Rp56.500,00
B. Rp565.000,00
C. Rp559.000,00
D. Rp1.740.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 196. Soal `b2768a1dbfc37b42d7ed4e22`

Sebuah peternakan memasok telur, susu, dan madu ke Toko I dan Toko II. Banyak barang (kemasan) dinyatakan oleh matriks $P = \begin{pmatrix}30 & 25 \\ 18 & 40 \\ 12 & 16\end{pmatrix}$ dengan baris berturut-turut telur, susu, dan madu, serta kolom berturut-turut Toko I dan Toko II. Harga per kemasan (ribu rupiah) untuk telur, susu, dan madu berturut-turut adalah 22, 15, dan 60. Matriks baris pendapatan (dalam ribu rupiah) untuk Toko I dan Toko II berturut-turut adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix}1650 & 2110\end{pmatrix}$ |
| B | $\begin{pmatrix}2110 & 1650\end{pmatrix}$ |
| C | $\begin{pmatrix}1566 & 2215\end{pmatrix}$ |
| D | $\begin{pmatrix}2334 & 2452\end{pmatrix}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `eeaddd8d95ed7ddf653cf57df76e245b0ee324266f32dc6370dc4f9891a4c2a4`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah peternakan memasok telur, susu, dan madu ke Toko I dan Toko II. Banyak barang (kemasan) dinyatakan oleh matriks $P = \begin{pmatrix}30 & 25 \\ 18 & 40 \\ 12 & 16\end{pmatrix}$ dengan baris berturut-turut telur, susu, dan madu, serta kolom berturut-turut Toko I dan Toko II. Harga per kemasan (ribu rupiah) untuk telur, susu, dan madu berturut-turut adalah 22, 15, dan 60. Matriks baris pendapatan (dalam ribu rupiah) untuk Toko I dan Toko II berturut-turut adalah ....
Pilihan: A. $\begin{pmatrix}1650 & 2110\end{pmatrix}$
B. $\begin{pmatrix}2110 & 1650\end{pmatrix}$
C. $\begin{pmatrix}1566 & 2215\end{pmatrix}$
D. $\begin{pmatrix}2334 & 2452\end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 197. Soal `6cf85eae1b6bf56841607dfa`

Toko oleh-oleh memiliki dua cabang, yaitu Bandung dan Malang. Banyak stoples bakpia, keripik, dan dodol yang tersedia dinyatakan oleh $A = \begin{pmatrix}24 & 31 & 18 \\ 29 & 22 & 35\end{pmatrix}$ (baris: Bandung dan Malang; kolom: bakpia, keripik, dodol). Harga normal per stoples (ribu rupiah) berturut-turut adalah 45, 38, dan 52. Jika semua harga diberi potongan 20% dan semua stoples terjual, pendapatan cabang Malang adalah ....

| Opsi | Isi |
|---|---|
| A | Rp3.961.000,00 |
| B | Rp2.555.200,00 |
| C | Rp792.200,00 |
| D | Rp3.168.800,00 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `402cb0693f9cb729a5956d2fbc6bf9c74fa84deabe61ae6ee0a05405a5626a3d`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Toko oleh-oleh memiliki dua cabang, yaitu Bandung dan Malang. Banyak stoples bakpia, keripik, dan dodol yang tersedia dinyatakan oleh $A = \begin{pmatrix}24 & 31 & 18 \\ 29 & 22 & 35\end{pmatrix}$ (baris: Bandung dan Malang; kolom: bakpia, keripik, dodol). Harga normal per stoples (ribu rupiah) berturut-turut adalah 45, 38, dan 52. Jika semua harga diberi potongan 20% dan semua stoples terjual, pendapatan cabang Malang adalah ....
Pilihan: A. Rp3.961.000,00
B. Rp2.555.200,00
C. Rp792.200,00
D. Rp3.168.800,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 198. Soal `0b5ccd879d5ef1d27893db1d`

Diketahui $A = \begin{pmatrix}3 & 1 \\ -2 & 4\end{pmatrix}$ dan $B = \begin{pmatrix}2 & 5 \\ 1 & -3\end{pmatrix}$. Pernyataan yang benar mengenai $AB$ dan $BA$ adalah ....

| Opsi | Isi |
|---|---|
| A | $AB \neq BA$, sebab elemen baris 1 kolom 1 pada $AB$ adalah $7$ sedangkan pada $BA$ adalah $-4$ |
| B | $AB = BA$, sebab elemen baris 1 kolom 1 keduanya bernilai $7$ |
| C | $AB \neq BA$, sebab elemen baris 1 kolom 1 pada $AB$ adalah $-4$ sedangkan pada $BA$ adalah $7$ |
| D | $AB \neq BA$, sebab elemen baris 1 kolom 1 pada $AB$ adalah $6$ sedangkan pada $BA$ adalah $-4$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9f8c573fee5dbc5c2f435b4025d9a1683863575ffe81a8f40a04e18412225d86`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix}3 & 1 \\ -2 & 4\end{pmatrix}$ dan $B = \begin{pmatrix}2 & 5 \\ 1 & -3\end{pmatrix}$. Pernyataan yang benar mengenai $AB$ dan $BA$ adalah ....
Pilihan: A. $AB \neq BA$, sebab elemen baris 1 kolom 1 pada $AB$ adalah $7$ sedangkan pada $BA$ adalah $-4$
B. $AB = BA$, sebab elemen baris 1 kolom 1 keduanya bernilai $7$
C. $AB \neq BA$, sebab elemen baris 1 kolom 1 pada $AB$ adalah $-4$ sedangkan pada $BA$ adalah $7$
D. $AB \neq BA$, sebab elemen baris 1 kolom 1 pada $AB$ adalah $6$ sedangkan pada $BA$ adalah $-4$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 199. Soal `180607bd8d06c578f61ddbae`

Sebuah perusahaan memiliki tiga lokasi. Banyak karyawan tetap dan paruh waktu dinyatakan oleh $A = \begin{pmatrix}40 & 25 \\ 55 & 30 \\ 35 & 45\end{pmatrix}$ (baris: lokasi 1, 2, 3; kolom: tetap dan paruh waktu). Gaji per hari (ribu rupiah) dinyatakan oleh $B = \begin{pmatrix}210 \\ 95\end{pmatrix}$ (baris: tetap dan paruh waktu). Selisih dana gaji per hari antara lokasi 2 dan lokasi 3 adalah ....

| Opsi | Isi |
|---|---|
| A | Rp3.625.000,00 |
| B | Rp2.775.000,00 |
| C | Rp1.250.000,00 |
| D | Rp277.500,00 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9487f8d12de68ee7a37e64176e4b91fe56aa4b374bae95c746226350579c4887`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah perusahaan memiliki tiga lokasi. Banyak karyawan tetap dan paruh waktu dinyatakan oleh $A = \begin{pmatrix}40 & 25 \\ 55 & 30 \\ 35 & 45\end{pmatrix}$ (baris: lokasi 1, 2, 3; kolom: tetap dan paruh waktu). Gaji per hari (ribu rupiah) dinyatakan oleh $B = \begin{pmatrix}210 \\ 95\end{pmatrix}$ (baris: tetap dan paruh waktu). Selisih dana gaji per hari antara lokasi 2 dan lokasi 3 adalah ....
Pilihan: A. Rp3.625.000,00
B. Rp2.775.000,00
C. Rp1.250.000,00
D. Rp277.500,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 200. Soal `53ccd9ad6f6cc5bb43e68427`

Diketahui $A = \begin{pmatrix}3 & -1 & 2 \\ 0 & 4 & -2\end{pmatrix}$ dan $B = \begin{pmatrix}1 & 5 \\ -3 & 2 \\ 4 & -1\end{pmatrix}$. Matriks $AB$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix}8 & 11 \\ -20 & 10\end{pmatrix}$ |
| B | $\begin{pmatrix}14 & -20 \\ 11 & 10\end{pmatrix}$ |
| C | $\begin{pmatrix}14 & 11 \\ -20 & 10\end{pmatrix}$ |
| D | $\begin{pmatrix}3 & 19 & -8 \\ -9 & 11 & -10 \\ 12 & -8 & 10\end{pmatrix}$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `846e30c66ac018d35bb39d4f0fb9cc2c986594f58be8daf6c198a8b3c9a77c52`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix}3 & -1 & 2 \\ 0 & 4 & -2\end{pmatrix}$ dan $B = \begin{pmatrix}1 & 5 \\ -3 & 2 \\ 4 & -1\end{pmatrix}$. Matriks $AB$ adalah ....
Pilihan: A. $\begin{pmatrix}8 & 11 \\ -20 & 10\end{pmatrix}$
B. $\begin{pmatrix}14 & -20 \\ 11 & 10\end{pmatrix}$
C. $\begin{pmatrix}14 & 11 \\ -20 & 10\end{pmatrix}$
D. $\begin{pmatrix}3 & 19 & -8 \\ -9 & 11 & -10 \\ 12 & -8 & 10\end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 201. Soal `64a634e78ab216a01d599fa7`

Diketahui $A = \begin{pmatrix}2 & -1 \\ 3 & 4 \\ -2 & 5\end{pmatrix}$ dan $B = \begin{pmatrix}2 & 3 & -2 \\ 4 & -1 & 2\end{pmatrix}$. Jumlah elemen pada diagonal utama matriks $AB$ adalah ....

| Opsi | Isi |
|---|---|
| A | 15 |
| B | -1 |
| C | 19 |
| D | 49 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0baad040cb6dbeeb7f754a1773a08ea9dd5432d4bb892e546bf5b545298d97ea`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix}2 & -1 \\ 3 & 4 \\ -2 & 5\end{pmatrix}$ dan $B = \begin{pmatrix}2 & 3 & -2 \\ 4 & -1 & 2\end{pmatrix}$. Jumlah elemen pada diagonal utama matriks $AB$ adalah ....
Pilihan: A. 15
B. -1
C. 19
D. 49
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 202. Soal `18d131898d3bd0c9e27a59f4`

Diketahui $A = \begin{pmatrix}3 & -2 \\ 1 & 4\end{pmatrix}$. Matriks $A^2$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix}6 & -4 \\ 2 & 8\end{pmatrix}$ |
| B | $\begin{pmatrix}9 & 4 \\ 1 & 16\end{pmatrix}$ |
| C | $\begin{pmatrix}7 & 2 \\ 7 & 14\end{pmatrix}$ |
| D | $\begin{pmatrix}7 & -14 \\ 7 & 14\end{pmatrix}$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0f9808cf3a8c8ae3a60fc666214ea89022188927c70ae7662dd7294a2a54bb15`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix}3 & -2 \\ 1 & 4\end{pmatrix}$. Matriks $A^2$ adalah ....
Pilihan: A. $\begin{pmatrix}6 & -4 \\ 2 & 8\end{pmatrix}$
B. $\begin{pmatrix}9 & 4 \\ 1 & 16\end{pmatrix}$
C. $\begin{pmatrix}7 & 2 \\ 7 & 14\end{pmatrix}$
D. $\begin{pmatrix}7 & -14 \\ 7 & 14\end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 203. Soal `dd05449eb5438a533aef7ada`

Diketahui $A = \begin{pmatrix}2 & 1 \\ -3 & 4\end{pmatrix}$ dan $I$ matriks identitas berordo $2 \times 2$. Matriks $A^2 - 2A + 3I$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix}-3 & 4 \\ -12 & 5\end{pmatrix}$ |
| B | $\begin{pmatrix}0 & 4 \\ -12 & 8\end{pmatrix}$ |
| C | $\begin{pmatrix}0 & 7 \\ -9 & 8\end{pmatrix}$ |
| D | $\begin{pmatrix}3 & -1 \\ 15 & 11\end{pmatrix}$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `32a8312d977117fea668ad71bcb6fefa1b5a04e771e2df8de99f4d34e4f2e828`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix}2 & 1 \\ -3 & 4\end{pmatrix}$ dan $I$ matriks identitas berordo $2 \times 2$. Matriks $A^2 - 2A + 3I$ adalah ....
Pilihan: A. $\begin{pmatrix}-3 & 4 \\ -12 & 5\end{pmatrix}$
B. $\begin{pmatrix}0 & 4 \\ -12 & 8\end{pmatrix}$
C. $\begin{pmatrix}0 & 7 \\ -9 & 8\end{pmatrix}$
D. $\begin{pmatrix}3 & -1 \\ 15 & 11\end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 204. Soal `21de4fe752b9850cb809e86c`

Diketahui $A = \begin{pmatrix}1 & 2 \\ 3 & -1\end{pmatrix}$, $B = \begin{pmatrix}2 & 0 \\ -1 & 3\end{pmatrix}$, dan $C = \begin{pmatrix}4 \\ -2\end{pmatrix}$. Matriks $ABC$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix}-12 \\ 34\end{pmatrix}$ |
| B | $\begin{pmatrix}12 \\ 22\end{pmatrix}$ |
| C | $\begin{pmatrix}0 \\ 42\end{pmatrix}$ |
| D | $\begin{pmatrix}8 \\ -10\end{pmatrix}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6fb6066546eb4e5c9b0be76b4a6559214b4dc794939ddf1683180fd7f6180375`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix}1 & 2 \\ 3 & -1\end{pmatrix}$, $B = \begin{pmatrix}2 & 0 \\ -1 & 3\end{pmatrix}$, dan $C = \begin{pmatrix}4 \\ -2\end{pmatrix}$. Matriks $ABC$ adalah ....
Pilihan: A. $\begin{pmatrix}-12 \\ 34\end{pmatrix}$
B. $\begin{pmatrix}12 \\ 22\end{pmatrix}$
C. $\begin{pmatrix}0 \\ 42\end{pmatrix}$
D. $\begin{pmatrix}8 \\ -10\end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 205. Soal `41399e24e2bb29f8124f19d2`

Diketahui $\begin{pmatrix}2 & 3 \\ 1 & -4\end{pmatrix}\begin{pmatrix}p \\ q\end{pmatrix} = \begin{pmatrix}1 \\ 17\end{pmatrix}$. Nilai $3p - q$ adalah ....

| Opsi | Isi |
|---|---|
| A | -14 |
| B | 12 |
| C | 18 |
| D | -18 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `89e022048a79f8b604663ad502222160e2f0fcba660c7bda6d3b00bb30b1b986`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $\begin{pmatrix}2 & 3 \\ 1 & -4\end{pmatrix}\begin{pmatrix}p \\ q\end{pmatrix} = \begin{pmatrix}1 \\ 17\end{pmatrix}$. Nilai $3p - q$ adalah ....
Pilihan: A. -14
B. 12
C. 18
D. -18
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 206. Soal `a2cc74c54d62697cd0fd6129`

Matriks $A$ berordo $2 \times 3$ dan matriks $B$ berordo $(x+1) \times (y-2)$. Jika $AB$ dan $BA$ sama-sama terdefinisi, nilai $2x + y$ adalah ....

| Opsi | Isi |
|---|---|
| A | 7 |
| B | 8 |
| C | 9 |
| D | 6 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ec25f024f3fe879e7ec7904b9f14d5895cc919f21b65e7bb76668ad1b6019b52`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$ berordo $2 \times 3$ dan matriks $B$ berordo $(x+1) \times (y-2)$. Jika $AB$ dan $BA$ sama-sama terdefinisi, nilai $2x + y$ adalah ....
Pilihan: A. 7
B. 8
C. 9
D. 6
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 207. Soal `2a4744f80c7185fe46a61ab3`

Matriks $A$, $B$, dan $C$ berordo $2 \times 2$ dengan $AB = \begin{pmatrix}4 & -3 \\ 7 & 2\end{pmatrix}$ dan $AC = \begin{pmatrix}1 & 5 \\ -2 & 6\end{pmatrix}$. Matriks $A(B - C)$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix}-3 & 8 \\ -9 & 4\end{pmatrix}$ |
| B | $\begin{pmatrix}3 & -8 \\ 9 & -4\end{pmatrix}$ |
| C | $\begin{pmatrix}3 & -8 \\ 9 & 4\end{pmatrix}$ |
| D | $\begin{pmatrix}5 & 2 \\ 5 & 8\end{pmatrix}$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d25ba62bf60e01d8870ee103ba4aaef321c6f815f2c60272d5a8eee3faff38c0`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$, $B$, dan $C$ berordo $2 \times 2$ dengan $AB = \begin{pmatrix}4 & -3 \\ 7 & 2\end{pmatrix}$ dan $AC = \begin{pmatrix}1 & 5 \\ -2 & 6\end{pmatrix}$. Matriks $A(B - C)$ adalah ....
Pilihan: A. $\begin{pmatrix}-3 & 8 \\ -9 & 4\end{pmatrix}$
B. $\begin{pmatrix}3 & -8 \\ 9 & -4\end{pmatrix}$
C. $\begin{pmatrix}3 & -8 \\ 9 & 4\end{pmatrix}$
D. $\begin{pmatrix}5 & 2 \\ 5 & 8\end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 208. Soal `ff2ae7b4210f6b1d6da93cf0`

Diketahui $A = \begin{pmatrix}2 & x \\ 1 & 3\end{pmatrix}$ dan $B = \begin{pmatrix}4 & -1 \\ -2 & 3\end{pmatrix}$. Jika jumlah elemen pada baris pertama matriks $AB$ sama dengan $1$, nilai $x$ adalah ....

| Opsi | Isi |
|---|---|
| A | -3 |
| B | -7 |
| C | -5 |
| D | 5 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `cc0a9f57b956f89903ac9d37cc0735a51af1a879f9d2f5a4d2a13b1d5b327435`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix}2 & x \\ 1 & 3\end{pmatrix}$ dan $B = \begin{pmatrix}4 & -1 \\ -2 & 3\end{pmatrix}$. Jika jumlah elemen pada baris pertama matriks $AB$ sama dengan $1$, nilai $x$ adalah ....
Pilihan: A. -3
B. -7
C. -5
D. 5
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 209. Soal `dc47e45cdb029e1422e829cf`

Sebuah toko roti membuat kue A dan kue B. Banyak kue yang dipesan pada hari pertama dan kedua dinyatakan oleh $P = \begin{pmatrix}12 & 8 \\ 15 & 10\end{pmatrix}$ (baris: hari pertama dan kedua; kolom: kue A dan B). Bahan per kue dinyatakan oleh $N = \begin{pmatrix}3 & 2 & 1 \\ 2 & 4 & 2\end{pmatrix}$ (baris: kue A dan B; kolom: tepung (kg), gula (kg), telur (butir)). Harga bahan (ribu rupiah) per kg tepung, per kg gula, dan per butir telur berturut-turut adalah 12, 20, dan 2. Biaya bahan yang diperlukan pada hari kedua adalah ....

| Opsi | Isi |
|---|---|
| A | Rp2.400.000,00 |
| B | Rp225.000,00 |
| C | Rp2.250.000,00 |
| D | Rp1.800.000,00 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5f3a58af9220dda86e53a7bcfd430f67fd45ee731cdbf5a395b3f6a21fcc695d`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah toko roti membuat kue A dan kue B. Banyak kue yang dipesan pada hari pertama dan kedua dinyatakan oleh $P = \begin{pmatrix}12 & 8 \\ 15 & 10\end{pmatrix}$ (baris: hari pertama dan kedua; kolom: kue A dan B). Bahan per kue dinyatakan oleh $N = \begin{pmatrix}3 & 2 & 1 \\ 2 & 4 & 2\end{pmatrix}$ (baris: kue A dan B; kolom: tepung (kg), gula (kg), telur (butir)). Harga bahan (ribu rupiah) per kg tepung, per kg gula, dan per butir telur berturut-turut adalah 12, 20, dan 2. Biaya bahan yang diperlukan pada hari kedua adalah ....
Pilihan: A. Rp2.400.000,00
B. Rp225.000,00
C. Rp2.250.000,00
D. Rp1.800.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 210. Soal `a75edd0d95a4f106f2d6ab0c`

Matriks $A$ dan $B$ berordo $2 \times 2$. Bentuk $(A + B)(A + B)$ yang pasti benar untuk sembarang $A$ dan $B$ tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $A^2 + 2AB + B^2$ |
| B | $A^2 + 2BA + B^2$ |
| C | $A^2 + B^2$ |
| D | $A^2 + AB + BA + B^2$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c97ce91def0d025bbf759f8b4602b330ce4c84e44e41d278dbab2e0dba91231a`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Perkalian Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$ dan $B$ berordo $2 \times 2$. Bentuk $(A + B)(A + B)$ yang pasti benar untuk sembarang $A$ dan $B$ tersebut adalah ....
Pilihan: A. $A^2 + 2AB + B^2$
B. $A^2 + 2BA + B^2$
C. $A^2 + B^2$
D. $A^2 + AB + BA + B^2$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 211. Soal `bb15e9b99625e0c3eed2c039`

Misalkan $A$ dan $B$ dua matriks persegi dengan ordo yang sama. Pernyataan yang berlaku untuk setiap pasangan $A$ dan $B$ tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $\|AB\| = \|A\|\,\|B\|$ |
| B | $\|A+B\| = \|A\| + \|B\|$ |
| C | $\|AB\| = \|A\| + \|B\|$ |
| D | $\|A+B\| = \|A\|\,\|B\|$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4b3f4c902a79d76af9f127f95aca111481635400353e5c326bdf734ef345dd93`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Misalkan $A$ dan $B$ dua matriks persegi dengan ordo yang sama. Pernyataan yang berlaku untuk setiap pasangan $A$ dan $B$ tersebut adalah ....
Pilihan: A. $|AB| = |A|\,|B|$
B. $|A+B| = |A| + |B|$
C. $|AB| = |A| + |B|$
D. $|A+B| = |A|\,|B|$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 212. Soal `8016658a228f98a1d2c9cffd`

Dua matriks persegi $A$ dan $B$ yang berordo sama memiliki $\|A\| = 3$ dan $\|B\| = -4$. Nilai $\|AB\|$ adalah ....

| Opsi | Isi |
|---|---|
| A | $7$ |
| B | $12$ |
| C | $-1$ |
| D | $-12$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a7eb35617a669b0ad8a67c3a2bcd5fe7fc3d968b0d293465c0aa897d6e343cd1`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Dua matriks persegi $A$ dan $B$ yang berordo sama memiliki $|A| = 3$ dan $|B| = -4$. Nilai $|AB|$ adalah ....
Pilihan: A. $7$
B. $12$
C. $-1$
D. $-12$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 213. Soal `9209b1f4ce11279a76275164`

Matriks $A$ berordo $2 \times 2$ dan $\|A\| = 5$. Nilai $\|3A\|$ adalah ....

| Opsi | Isi |
|---|---|
| A | $135$ |
| B | $30$ |
| C | $15$ |
| D | $45$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ba148366d3a342db8a820605ae1bf907238e9533c8de512b642f1061407f7cde`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$ berordo $2 \times 2$ dan $|A| = 5$. Nilai $|3A|$ adalah ....
Pilihan: A. $135$
B. $30$
C. $15$
D. $45$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 214. Soal `d9a94e3056a49f9f04e8197d`

Matriks $C$ berordo $3 \times 3$ dan $\|C\| = 2$. Nilai $\|2C\|$ adalah ....

| Opsi | Isi |
|---|---|
| A | $64$ |
| B | $8$ |
| C | $16$ |
| D | $4$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9040445355445c884f615ee69fb21322e974dc7d693b29282f39fb1393360e95`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $C$ berordo $3 \times 3$ dan $|C| = 2$. Nilai $|2C|$ adalah ....
Pilihan: A. $64$
B. $8$
C. $16$
D. $4$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 215. Soal `7d8131eb5c6fd230ac533449`

Matriks persegi $A$, $B$, dan $C$ berordo sama dengan $\|A\| = 2$, $\|B\| = -3$, dan $\|C\| = 4$. Nilai $\|ABC\|$ adalah ....

| Opsi | Isi |
|---|---|
| A | $24$ |
| B | $-6$ |
| C | $-24$ |
| D | $3$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4f211d0a82f7e81627dc3e98125c8a0a06dbf7e46c3a76bef892bb1f648c4af8`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks persegi $A$, $B$, dan $C$ berordo sama dengan $|A| = 2$, $|B| = -3$, dan $|C| = 4$. Nilai $|ABC|$ adalah ....
Pilihan: A. $24$
B. $-6$
C. $-24$
D. $3$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 216. Soal `1decaa8eed730838deed2c51`

Jika $A$ dan $B$ matriks persegi berordo sama yang masing-masing mempunyai invers, maka $(AB)^{-1}$ sama dengan ....

| Opsi | Isi |
|---|---|
| A | $A^{-1}B^{-1}$ |
| B | $(A+B)^{-1}$ |
| C | $B^{-1}A^{-1}$ |
| D | $A^{-1} + B^{-1}$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8574c5941c0bf48f7cdf29cd50a650a5071147eb6b1c2897bbe4b762d3cc071e`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika $A$ dan $B$ matriks persegi berordo sama yang masing-masing mempunyai invers, maka $(AB)^{-1}$ sama dengan ....
Pilihan: A. $A^{-1}B^{-1}$
B. $(A+B)^{-1}$
C. $B^{-1}A^{-1}$
D. $A^{-1} + B^{-1}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 217. Soal `1394c3008b5d4f041ab03cd7`

Matriks persegi $A$ mempunyai invers $A^{-1}$ dan $I$ adalah matriks identitas yang berordo sama. Hasil kali $A \cdot A^{-1}$ adalah ....

| Opsi | Isi |
|---|---|
| A | matriks nol $O$ |
| B | $A$ |
| C | $A^{2}$ |
| D | $I$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `519a32ebc70dd95d60be814da89728173b542f9dde70132ab70172f1fd78c8aa`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks persegi $A$ mempunyai invers $A^{-1}$ dan $I$ adalah matriks identitas yang berordo sama. Hasil kali $A \cdot A^{-1}$ adalah ....
Pilihan: A. matriks nol $O$
B. $A$
C. $A^{2}$
D. $I$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 218. Soal `115d1a55a8d26cd6d245bd18`

Diketahui $X = \begin{pmatrix} 9 & 5 \\ 7 & 4 \end{pmatrix}$. Invers matriks $X$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix} 4 & -7 \\ -5 & 9 \end{pmatrix}$ |
| B | $\begin{pmatrix} 4 & -5 \\ -7 & 9 \end{pmatrix}$ |
| C | $\begin{pmatrix} 4 & 5 \\ 7 & 9 \end{pmatrix}$ |
| D | $\begin{pmatrix} 9 & -5 \\ -7 & 4 \end{pmatrix}$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a1cb638ed79c4e4d6f4f94d4d6010264c987ab877020c2d93ab2853037636b66`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $X = \begin{pmatrix} 9 & 5 \\ 7 & 4 \end{pmatrix}$. Invers matriks $X$ adalah ....
Pilihan: A. $\begin{pmatrix} 4 & -7 \\ -5 & 9 \end{pmatrix}$
B. $\begin{pmatrix} 4 & -5 \\ -7 & 9 \end{pmatrix}$
C. $\begin{pmatrix} 4 & 5 \\ 7 & 9 \end{pmatrix}$
D. $\begin{pmatrix} 9 & -5 \\ -7 & 4 \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 219. Soal `d7b917fdda790bc0acd06f9c`

Diketahui $Y = \begin{pmatrix} 6 & 4 \\ 7 & 5 \end{pmatrix}$. Invers matriks $Y$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\frac{1}{2}\begin{pmatrix} 5 & -4 \\ -7 & 6 \end{pmatrix}$ |
| B | $\frac{1}{2}\begin{pmatrix} 6 & -4 \\ -7 & 5 \end{pmatrix}$ |
| C | $\frac{1}{2}\begin{pmatrix} 5 & 4 \\ 7 & 6 \end{pmatrix}$ |
| D | $\begin{pmatrix} 5 & -4 \\ -7 & 6 \end{pmatrix}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `24e0aaa42842f037d63597ae4a8de96ad8a3ccbb1f34231540ab2ad8b410df4e`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $Y = \begin{pmatrix} 6 & 4 \\ 7 & 5 \end{pmatrix}$. Invers matriks $Y$ adalah ....
Pilihan: A. $\frac{1}{2}\begin{pmatrix} 5 & -4 \\ -7 & 6 \end{pmatrix}$
B. $\frac{1}{2}\begin{pmatrix} 6 & -4 \\ -7 & 5 \end{pmatrix}$
C. $\frac{1}{2}\begin{pmatrix} 5 & 4 \\ 7 & 6 \end{pmatrix}$
D. $\begin{pmatrix} 5 & -4 \\ -7 & 6 \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 220. Soal `2716c2587dc4e8bd8e489fa1`

Tentukan $(AB^{-1})^{-1}$ jika diketahui $A^{-1} = \begin{pmatrix} 6 & 7 \\ 0 & 8 \end{pmatrix}$ dan $B = \begin{pmatrix} 9 & 0 \\ 6 & 7 \end{pmatrix}$.

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix} 96 & 48 \\ 49 & 56 \end{pmatrix}$ |
| B | $\begin{pmatrix} 54 & 36 \\ 63 & 98 \end{pmatrix}$ |
| C | $\begin{pmatrix} 54 & 63 \\ 36 & 98 \end{pmatrix}$ |
| D | $\begin{pmatrix} 96 & 49 \\ 48 & 56 \end{pmatrix}$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ce29eb3db4d2ea27d892551e127aebddb3a1bf08258653e14d5e9e0cdf6a7fe0`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan $(AB^{-1})^{-1}$ jika diketahui $A^{-1} = \begin{pmatrix} 6 & 7 \\ 0 & 8 \end{pmatrix}$ dan $B = \begin{pmatrix} 9 & 0 \\ 6 & 7 \end{pmatrix}$.
Pilihan: A. $\begin{pmatrix} 96 & 48 \\ 49 & 56 \end{pmatrix}$
B. $\begin{pmatrix} 54 & 36 \\ 63 & 98 \end{pmatrix}$
C. $\begin{pmatrix} 54 & 63 \\ 36 & 98 \end{pmatrix}$
D. $\begin{pmatrix} 96 & 49 \\ 48 & 56 \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 221. Soal `708c86b73a2a8c961239acb1`

Nilai determinan matriks $A = \begin{pmatrix} 6 & 4 \\ 3 & 5 \end{pmatrix}$ adalah ....

| Opsi | Isi |
|---|---|
| A | $-18$ |
| B | $30$ |
| C | $18$ |
| D | $42$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7c1de7f7189138c3cb69ae5be524a083960aa5d7b0327418ccfe6d969eaefc3e`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Nilai determinan matriks $A = \begin{pmatrix} 6 & 4 \\ 3 & 5 \end{pmatrix}$ adalah ....
Pilihan: A. $-18$
B. $30$
C. $18$
D. $42$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 222. Soal `3ebb3883a595056d22d26e1c`

Nilai $\det B$ untuk $B = \begin{pmatrix} -3 & 5 \\ 2 & -4 \end{pmatrix}$ adalah ....

| Opsi | Isi |
|---|---|
| A | $2$ |
| B | $-2$ |
| C | $22$ |
| D | $-22$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `08650ec8fdd255d5c6f680629807d98832e3728614cc50f908426f78f9e7ad2b`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Nilai $\det B$ untuk $B = \begin{pmatrix} -3 & 5 \\ 2 & -4 \end{pmatrix}$ adalah ....
Pilihan: A. $2$
B. $-2$
C. $22$
D. $-22$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 223. Soal `9b9f97df38959b6dc4b90e53`

Matriks $A = \begin{pmatrix} x & 10 \\ 3 & 5 \end{pmatrix}$ merupakan matriks singular. Nilai $x$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\frac{3}{2}$ |
| B | $30$ |
| C | $-6$ |
| D | $6$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `67c486a8bf25de6285f9adf28de88d41b3e08e1caf95c6c816496015e45101d9`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A = \begin{pmatrix} x & 10 \\ 3 & 5 \end{pmatrix}$ merupakan matriks singular. Nilai $x$ adalah ....
Pilihan: A. $\frac{3}{2}$
B. $30$
C. $-6$
D. $6$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 224. Soal `1ae7e7aa897cff27235ec2e2`

Di antara matriks berikut, matriks yang mempunyai invers adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix} 5 & 2 \\ 3 & 1 \end{pmatrix}$ |
| B | $\begin{pmatrix} 2 & 4 \\ 3 & 6 \end{pmatrix}$ |
| C | $\begin{pmatrix} 1 & -2 \\ -3 & 6 \end{pmatrix}$ |
| D | $\begin{pmatrix} 3 & 9 \\ 1 & 3 \end{pmatrix}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2510b49bb77adc9a63ebff1b155c33f22c4ace6efedaf9a7c9216342046c4379`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Di antara matriks berikut, matriks yang mempunyai invers adalah ....
Pilihan: A. $\begin{pmatrix} 5 & 2 \\ 3 & 1 \end{pmatrix}$
B. $\begin{pmatrix} 2 & 4 \\ 3 & 6 \end{pmatrix}$
C. $\begin{pmatrix} 1 & -2 \\ -3 & 6 \end{pmatrix}$
D. $\begin{pmatrix} 3 & 9 \\ 1 & 3 \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 225. Soal `422e690c20eca2cf718c3c90`

Matriks persegi $A$ dengan $\|A\| = 0$ disebut ....

| Opsi | Isi |
|---|---|
| A | matriks adjoin |
| B | matriks singular |
| C | matriks identitas |
| D | matriks nonsingular |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a8a4ee7f9cd2885da9b644be2959bf633437778cde61352ca01c53447c19e6ec`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks persegi $A$ dengan $|A| = 0$ disebut ....
Pilihan: A. matriks adjoin
B. matriks singular
C. matriks identitas
D. matriks nonsingular
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 226. Soal `7fc5c057fb230a325f8d603a`

Diketahui $A = \begin{pmatrix} 4 & 3 \\ 1 & 2 \end{pmatrix}$. Elemen pada baris pertama kolom kedua dari $A^{-1}$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\frac{3}{5}$ |
| B | $-\frac{3}{5}$ |
| C | $-\frac{1}{5}$ |
| D | $-3$ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Determinan A = (4)(2) - (3)(1) = 5. Invers A = (1/5) * adj(A). Adjoin A diperoleh dengan menukar elemen diagonal utama (4, 2 menjadi 2, 4) dan mengubah tanda elemen diagonal samping (3, 1 menjadi -3, -1). Maka A^-1 = (1/5) * [[2, -3], [-1, 4]]. Elemen baris pertama kolom kedua adalah (1/5) * (-3) = -3/5.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f5fcdf504b7c88cfe9c1f56b52ca5a63a94d16e013540c198a0e1e5ff310bbd9`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2761 |
| 2 | success | valid / verified | applying | procedural | Easy | 2762 |
| 3 | success | valid / verified | applying | procedural | Easy | 2745 |

Run 1 — solusi: Determinan A = (4)(2) - (3)(1) = 5. Invers A = (1/5) * adj(A). Adjoin A diperoleh dengan menukar elemen diagonal utama (4, 2 menjadi 2, 4) dan mengubah tanda elemen diagonal samping (3, 1 menjadi -3, -1). Maka A^-1 = (1/5) * [[2, -3], [-1, 4]]. Elemen baris pertama kolom kedua adalah (1/5) * (-3) = -3/5.
- Domain kognitif `classify/knowing`: Soal meminta penerapan langsung prosedur standar untuk mencari invers matriks 2x2 dan mengidentifikasi elemen spesifiknya. Siswa hanya perlu mengingat rumus invers dan determinan, lalu melakukan perhitungan rutin.. Bukti: Elemen pada baris pertama kolom kedua dari A^-1 adalah
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang algoritma invers matriks 2x2 (determinan dan adjoin).. Bukti: Diketahui A = (4 3 / 1 2). Elemen pada baris pertama kolom kedua dari A^-1
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Tidak ada langkah yang saling bergantung secara kompleks atau kendala yang harus diintegrasikan. Siswa hanya perlu menerapkan rumus invers matriks 2x2 yang merupakan materi dasar kelas 11.. Bukti: Diketahui A = (4 3 / 1 2). Elemen pada baris pertama kolom kedua dari A^-1

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep determinan dan invers matriks 2x2. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi invers matriks 2x2 adalah standar dasar kelas 11. Soal tidak memerlukan manipulasi aljabar lanjut atau penalaran non-rutin. |

Run 2 — solusi: Determinan A = (4)(2) - (3)(1) = 5. Invers A = (1/5) * adj(A). Adjoin A diperoleh dengan menukar elemen diagonal utama (4, 2 menjadi 2, 4) dan mengubah tanda elemen diagonal samping (3, 1 menjadi -3, -1). Maka A^-1 = (1/5) * [[2, -3], [-1, 4]]. Elemen baris 1 kolom 2 adalah (1/5) * (-3) = -3/5.
- Domain kognitif `classify/applying`: Soal meminta penerapan langsung prosedur standar untuk mencari invers matriks 2x2 dan mengidentifikasi elemen spesifiknya. Siswa hanya perlu menghitung determinan dan adjoin, lalu mengalikan dengan skalar.. Bukti: Elemen pada baris pertama kolom kedua dari A^-1 adalah
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang algoritma invers matriks 2x2 (determinan dan adjoin).. Bukti: Diketahui A = (4 3; 1 2). Elemen pada baris pertama kolom kedua dari A^-1
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa kelas 11 TL sudah familiar dengan prosedur invers matriks 2x2. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi non-rutin.. Bukti: Diketahui A = (4 3; 1 2). Elemen pada baris pertama kolom kedua dari A^-1

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi matriks dasar dan determinan matriks 2x2. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi invers matriks 2x2 adalah standar dasar kelas 11 TL. Prosedur penyelesaian sangat langsung dan familiar bagi siswa. |

Run 3 — solusi: Determinan A = (4)(2) - (3)(1) = 5. Invers A = (1/5) * adj(A). Adjoin A diperoleh dengan menukar elemen diagonal utama (4 dan 2) dan mengubah tanda elemen diagonal samping (3 dan 1 menjadi -3 dan -1). Maka A^-1 = (1/5) * [[2, -3], [-1, 4]]. Elemen baris pertama kolom kedua adalah (1/5) * (-3) = -3/5.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan prosedur standar untuk mencari invers matriks 2x2 dan mengidentifikasi elemen spesifik. Ini adalah penerapan langsung dari algoritma invers matriks.. Bukti: Elemen pada baris pertama kolom kedua dari A^-1 adalah
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami algoritma invers matriks 2x2 (determinan dan adjoin) untuk menyelesaikan masalah ini.. Bukti: Diketahui A = (4 3 / 1 2). Elemen pada baris pertama kolom kedua dari A^-1
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu menghitung determinan dan menerapkan rumus invers matriks 2x2 secara langsung. Tidak ada langkah kompleks atau integrasi konsep yang menantang.. Bukti: Diketahui A = (4 3 / 1 2). Elemen pada baris pertama kolom kedua dari A^-1

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang determinan dan invers matriks 2x2. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi invers matriks 2x2 adalah standar dasar kelas 11 TL. Soal ini menguji prosedur dasar tanpa modifikasi atau tuntutan penalaran tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 1, "applying": 2} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4457`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Soal meminta penerapan langsung prosedur standar untuk mencari invers matriks 2x2 dan mengidentifikasi elemen spesifiknya. Siswa hanya perlu mengingat rumus invers dan determinan, lalu melakukan perhitungan rutin.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman prosedural tentang algoritma invers matriks 2x2 (determinan dan adjoin).
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung. Tidak ada langkah yang saling bergantung secara kompleks atau kendala yang harus diintegrasikan. Siswa hanya perlu menerapkan rumus invers matriks 2x2 yang merupakan materi dasar kelas 11.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep determinan dan invers matriks 2x2. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi invers matriks 2x2 adalah standar dasar kelas 11. Soal tidak memerlukan manipulasi aljabar lanjut atau penalaran non-rutin. |

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix} 4 & 3 \\ 1 & 2 \end{pmatrix}$. Elemen pada baris pertama kolom kedua dari $A^{-1}$ adalah ....
Pilihan: A. $\frac{3}{5}$
B. $-\frac{3}{5}$
C. $-\frac{1}{5}$
D. $-3$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 227. Soal `fd8e3caace6e0609ef7257a9`

Untuk $A = \begin{pmatrix} 6 & -2 \\ 5 & 3 \end{pmatrix}$, matriks $Adjoin(A)$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix} 3 & 2 \\ -5 & 6 \end{pmatrix}$ |
| B | $\begin{pmatrix} 3 & -5 \\ 2 & 6 \end{pmatrix}$ |
| C | $\begin{pmatrix} 3 & -2 \\ 5 & 6 \end{pmatrix}$ |
| D | $\begin{pmatrix} 6 & 2 \\ -5 & 3 \end{pmatrix}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `26122e734f3f1e30c8949e8f88ead1a146f1265a196b7da90c94bcb2c3fc13ee`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Untuk $A = \begin{pmatrix} 6 & -2 \\ 5 & 3 \end{pmatrix}$, matriks $Adjoin(A)$ adalah ....
Pilihan: A. $\begin{pmatrix} 3 & 2 \\ -5 & 6 \end{pmatrix}$
B. $\begin{pmatrix} 3 & -5 \\ 2 & 6 \end{pmatrix}$
C. $\begin{pmatrix} 3 & -2 \\ 5 & 6 \end{pmatrix}$
D. $\begin{pmatrix} 6 & 2 \\ -5 & 3 \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 228. Soal `fea7777bffa38a9f53d8cb76`

Diketahui $A^{-1} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$ dan $AX = B$ dengan $B = \begin{pmatrix} 4 \\ 9 \end{pmatrix}$. Matriks $X$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix} -33 \\ 14 \end{pmatrix}$ |
| B | $\begin{pmatrix} 21 \\ -38 \end{pmatrix}$ |
| C | $\begin{pmatrix} -3 \\ 2 \end{pmatrix}$ |
| D | $\begin{pmatrix} 3 \\ -2 \end{pmatrix}$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `520e15fbc034e49cf7eb9800808dca6ad5d655219c8d257ea91df58ba1447c54`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A^{-1} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$ dan $AX = B$ dengan $B = \begin{pmatrix} 4 \\ 9 \end{pmatrix}$. Matriks $X$ adalah ....
Pilihan: A. $\begin{pmatrix} -33 \\ 14 \end{pmatrix}$
B. $\begin{pmatrix} 21 \\ -38 \end{pmatrix}$
C. $\begin{pmatrix} -3 \\ 2 \end{pmatrix}$
D. $\begin{pmatrix} 3 \\ -2 \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 229. Soal `3f6bb2b24e54c9cc7c602c98`

Diketahui $A = \begin{pmatrix} 2 & 1 & 3 \\ 4 & 0 & 5 \\ 1 & 6 & 2 \end{pmatrix}$. Kofaktor $k_{12}$ dari matriks $A$ adalah ....

| Opsi | Isi |
|---|---|
| A | $-16$ |
| B | $-3$ |
| C | $13$ |
| D | $3$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `66d7f244f10dfd13bcf07bf51dabc948894c336c4038cde40aa991178c56186b`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix} 2 & 1 & 3 \\ 4 & 0 & 5 \\ 1 & 6 & 2 \end{pmatrix}$. Kofaktor $k_{12}$ dari matriks $A$ adalah ....
Pilihan: A. $-16$
B. $-3$
C. $13$
D. $3$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 230. Soal `2272187ceb18b0b3ed4ff184`

Dengan Metode Sarrus, nilai determinan $\begin{vmatrix} 2 & 1 & 0 \\ 1 & 3 & 2 \\ 4 & 0 & 1 \end{vmatrix}$ adalah ....

| Opsi | Isi |
|---|---|
| A | $14$ |
| B | $13$ |
| C | $-13$ |
| D | $15$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `db66e792d3ad8996f9025a9f7a4427d700fad8037882dbec74c7a283feb2a2a1`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Dengan Metode Sarrus, nilai determinan $\begin{vmatrix} 2 & 1 & 0 \\ 1 & 3 & 2 \\ 4 & 0 & 1 \end{vmatrix}$ adalah ....
Pilihan: A. $14$
B. $13$
C. $-13$
D. $15$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 231. Soal `609d9e40c8ddd8e321b93881`

Misalkan $A$ dan $B$ matriks persegi berordo sama yang keduanya mempunyai invers. Pernyataan yang berlaku untuk setiap pasangan $A$ dan $B$ tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $\|A + B\| = \|A\| + \|B\|$ |
| B | $(AB)^{-1} = A^{-1}B^{-1}$ |
| C | $\|AB\| = \|BA\|$ |
| D | $AB = BA$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f32516f9a919da8823971badd33c09da4a2df7548acba9125f6a2bd1fde0267f`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Misalkan $A$ dan $B$ matriks persegi berordo sama yang keduanya mempunyai invers. Pernyataan yang berlaku untuk setiap pasangan $A$ dan $B$ tersebut adalah ....
Pilihan: A. $|A + B| = |A| + |B|$
B. $(AB)^{-1} = A^{-1}B^{-1}$
C. $|AB| = |BA|$
D. $AB = BA$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 232. Soal `bdfc0672276c2641b1e22c07`

Matriks $A$ berordo $3 \times 3$ dengan $\|A\| = 4$. Nilai $\|2A^{-1}\|$ adalah ....

| Opsi | Isi |
|---|---|
| A | $8$ |
| B | $\frac{1}{2}$ |
| C | $32$ |
| D | $2$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c4f93c78c7aa74ebcdb1ef39775f96848b8e54d6a96fbcfcbfab192169660a0d`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$ berordo $3 \times 3$ dengan $|A| = 4$. Nilai $|2A^{-1}|$ adalah ....
Pilihan: A. $8$
B. $\frac{1}{2}$
C. $32$
D. $2$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 233. Soal `8df7971559fe6b502b0fee8c`

Seorang siswa menghitung invers dari $A = \begin{pmatrix} 5 & 2 \\ 7 & 3 \end{pmatrix}$ dan menulis $A^{-1} = \begin{pmatrix} 3 & 2 \\ 7 & 5 \end{pmatrix}$. Kesalahan siswa tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | elemen diagonal utama tidak ditukar |
| B | elemen diagonal samping tidak diubah tandanya |
| C | determinan $A$ dihitung salah sehingga pengali $\frac{1}{\|A\|}$ keliru |
| D | elemen diagonal utama ikut diubah tandanya seharusnya |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8d9280dbb25a505fef307f261dba087030a25623bd92b7af039deaf5a176727f`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Seorang siswa menghitung invers dari $A = \begin{pmatrix} 5 & 2 \\ 7 & 3 \end{pmatrix}$ dan menulis $A^{-1} = \begin{pmatrix} 3 & 2 \\ 7 & 5 \end{pmatrix}$. Kesalahan siswa tersebut adalah ....
Pilihan: A. elemen diagonal utama tidak ditukar
B. elemen diagonal samping tidak diubah tandanya
C. determinan $A$ dihitung salah sehingga pengali $\frac{1}{|A|}$ keliru
D. elemen diagonal utama ikut diubah tandanya seharusnya
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 234. Soal `d4edd7c9db0dcc7c31cf42cd`

Untuk $M = \begin{pmatrix} 2 & 1 & 3 \\ 0 & 4 & 5 \\ 6 & 7 & 1 \end{pmatrix}$, seorang siswa menghitung determinan dengan ekspansi baris pertama memakai minor langsung tanpa pola tanda, yaitu $2M_{11} + 1M_{12} + 3M_{13}$. Determinan sebenarnya lebih besar daripada hasil siswa tersebut sebesar ....

| Opsi | Isi |
|---|---|
| A | 30 |
| B | 60 |
| C | -104 |
| D | -60 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8e694702d27402865e98f4bb990306f77a15fb1cc4dc1671551fa90334ec770d`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Untuk $M = \begin{pmatrix} 2 & 1 & 3 \\ 0 & 4 & 5 \\ 6 & 7 & 1 \end{pmatrix}$, seorang siswa menghitung determinan dengan ekspansi baris pertama memakai minor langsung tanpa pola tanda, yaitu $2M_{11} + 1M_{12} + 3M_{13}$. Determinan sebenarnya lebih besar daripada hasil siswa tersebut sebesar ....
Pilihan: A. 30
B. 60
C. -104
D. -60
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 235. Soal `0fa4e68ab2488edfaf1ed823`

Diketahui $A = \begin{pmatrix} x+1 & 3 \\ 2 & x \end{pmatrix}$ dan $B = \begin{pmatrix} x & 4 \\ 1 & 2 \end{pmatrix}$. Jika $A$ singular tetapi $B$ mempunyai invers, nilai $x$ yang memenuhi adalah ....

| Opsi | Isi |
|---|---|
| A | $-3$ |
| B | $-1$ |
| C | $6$ |
| D | $2$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `806a2c622f7af8b54f1df86fa00537d199ca09406e56ca70177284b277bc0317`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix} x+1 & 3 \\ 2 & x \end{pmatrix}$ dan $B = \begin{pmatrix} x & 4 \\ 1 & 2 \end{pmatrix}$. Jika $A$ singular tetapi $B$ mempunyai invers, nilai $x$ yang memenuhi adalah ....
Pilihan: A. $-3$
B. $-1$
C. $6$
D. $2$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 236. Soal `b78c33a0f4d415b8652538db`

Matriks $A = \begin{pmatrix} 2 & p \\ q & -2 \end{pmatrix}$ memenuhi $A = A^{-1}$. Nilai $pq$ adalah ....

| Opsi | Isi |
|---|---|
| A | $-5$ |
| B | $-1$ |
| C | $-3$ |
| D | $3$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `21cc0eca40cad5b61e2829ce4b497142b1e37fb6beee253bb52fc5a249515dee`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A = \begin{pmatrix} 2 & p \\ q & -2 \end{pmatrix}$ memenuhi $A = A^{-1}$. Nilai $pq$ adalah ....
Pilihan: A. $-5$
B. $-1$
C. $-3$
D. $3$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 237. Soal `7c6eaa0ca98d72c2c5525e71`

Matriks $A$ berordo $3 \times 3$ dengan $\|A\| = -3$. Karena $A^{-1} = \frac{1}{\|A\|}\,Adjoin(A)$, nilai $\|Adjoin(A)\|$ adalah ....

| Opsi | Isi |
|---|---|
| A | $-9$ |
| B | $-3$ |
| C | $-27$ |
| D | $9$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f30e1ea73cf17965c7ffe8e6d49e6eccfa7cd251a616b6e93d4b9efce75f97ee`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$ berordo $3 \times 3$ dengan $|A| = -3$. Karena $A^{-1} = \frac{1}{|A|}\,Adjoin(A)$, nilai $|Adjoin(A)|$ adalah ....
Pilihan: A. $-9$
B. $-3$
C. $-27$
D. $9$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 238. Soal `38d85a96002430efd56f8578`

Semua elemen suatu matriks berordo $2 \times 2$ adalah bilangan bulat. Di antara matriks berikut, yang semua elemen inversnya juga bilangan bulat adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix} 5 & 2 \\ 4 & 1 \end{pmatrix}$ |
| B | $\begin{pmatrix} 4 & 1 \\ 3 & 2 \end{pmatrix}$ |
| C | $\begin{pmatrix} 2 & 3 \\ 3 & 4 \end{pmatrix}$ |
| D | $\begin{pmatrix} 3 & 4 \\ 1 & 2 \end{pmatrix}$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `60cc8b3b124600926963bd190c9e9bda6986c173940c194351685882ab74628a`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Semua elemen suatu matriks berordo $2 \times 2$ adalah bilangan bulat. Di antara matriks berikut, yang semua elemen inversnya juga bilangan bulat adalah ....
Pilihan: A. $\begin{pmatrix} 5 & 2 \\ 4 & 1 \end{pmatrix}$
B. $\begin{pmatrix} 4 & 1 \\ 3 & 2 \end{pmatrix}$
C. $\begin{pmatrix} 2 & 3 \\ 3 & 4 \end{pmatrix}$
D. $\begin{pmatrix} 3 & 4 \\ 1 & 2 \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 239. Soal `28633a618a9a3a94a50e5054`

Diketahui $A = \begin{pmatrix} x & x+1 \\ 1 & x \end{pmatrix}$. Banyak nilai real $x$ yang membuat $A$ mempunyai invers dengan $\|A\| = \|A^{-1}\|$ adalah ....

| Opsi | Isi |
|---|---|
| A | $4$ |
| B | $3$ |
| C | $6$ |
| D | $2$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4534c3ca2b670ad854ecdcaed7525ef59d4ced112462be4935e19249933a83a1`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix} x & x+1 \\ 1 & x \end{pmatrix}$. Banyak nilai real $x$ yang membuat $A$ mempunyai invers dengan $|A| = |A^{-1}|$ adalah ....
Pilihan: A. $4$
B. $3$
C. $6$
D. $2$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 240. Soal `2e3b5fc304d954884bfc6276`

Pernyataan: \"Jika $AB = AC$, maka $B = C$.\" Pernyataan ini salah. Pasangan $A$, $B$, $C$ berordo $2 \times 2$ yang merupakan contoh penyangkal pernyataan tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $A = \begin{pmatrix} 2 & 4 \\ 1 & 2 \end{pmatrix}$, $B = \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}$, $C = \begin{pmatrix} 1 & -3 \\ 2 & 5 \end{pmatrix}$ |
| B | $A = \begin{pmatrix} 2 & 4 \\ 1 & 3 \end{pmatrix}$, $B = \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}$, $C = \begin{pmatrix} 1 & -3 \\ 2 & 4 \end{pmatrix}$ |
| C | $A = \begin{pmatrix} 2 & 4 \\ 1 & 2 \end{pmatrix}$, $B = \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}$, $C = \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}$ |
| D | $A = \begin{pmatrix} 2 & 4 \\ 1 & 2 \end{pmatrix}$, $B = \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}$, $C = \begin{pmatrix} 1 & -3 \\ 2 & 4 \end{pmatrix}$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `74c4b8b4ecef96194de590e8ec3d5e3c03d0125466fab83d73acb8b7c217bd82`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Pernyataan: \"Jika $AB = AC$, maka $B = C$.\" Pernyataan ini salah. Pasangan $A$, $B$, $C$ berordo $2 \times 2$ yang merupakan contoh penyangkal pernyataan tersebut adalah ....
Pilihan: A. $A = \begin{pmatrix} 2 & 4 \\ 1 & 2 \end{pmatrix}$, $B = \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}$, $C = \begin{pmatrix} 1 & -3 \\ 2 & 5 \end{pmatrix}$
B. $A = \begin{pmatrix} 2 & 4 \\ 1 & 3 \end{pmatrix}$, $B = \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}$, $C = \begin{pmatrix} 1 & -3 \\ 2 & 4 \end{pmatrix}$
C. $A = \begin{pmatrix} 2 & 4 \\ 1 & 2 \end{pmatrix}$, $B = \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}$, $C = \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}$
D. $A = \begin{pmatrix} 2 & 4 \\ 1 & 2 \end{pmatrix}$, $B = \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}$, $C = \begin{pmatrix} 1 & -3 \\ 2 & 4 \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 241. Soal `080d12453284bbeeec512df2`

Matriks persegi $A$ mempunyai invers dan memenuhi $A^2 = A$. Kesimpulan yang pasti benar adalah ....

| Opsi | Isi |
|---|---|
| A | $\|A\| = 0$ |
| B | $\|A\| = 2$ |
| C | $A = O$ |
| D | $A = I$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['menyimpulkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7fcdc5d7905ba2787113b1a31fa429c1706fda202d54bbfbeec2e7ef2a65f39c`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks persegi $A$ mempunyai invers dan memenuhi $A^2 = A$. Kesimpulan yang pasti benar adalah ....
Pilihan: A. $|A| = 0$
B. $|A| = 2$
C. $A = O$
D. $A = I$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 242. Soal `313b6d1eb5a5b3d8ba964d38`

Sebuah sistem persamaan linear tiga variabel mempunyai $D = D_x = D_y = D_z = 0$. Pernyataan yang pasti benar tentang sistem tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | sistem tidak mungkin mempunyai tepat satu penyelesaian |
| B | sistem pasti mempunyai tak hingga banyak penyelesaian |
| C | penyelesaiannya adalah $x = y = z = 0$ |
| D | sistem pasti tidak mempunyai penyelesaian |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2ed39299f10cc7337aafef8ad74a7ef1abb7f7e6dc575438cbda7035170706f8`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah sistem persamaan linear tiga variabel mempunyai $D = D_x = D_y = D_z = 0$. Pernyataan yang pasti benar tentang sistem tersebut adalah ....
Pilihan: A. sistem tidak mungkin mempunyai tepat satu penyelesaian
B. sistem pasti mempunyai tak hingga banyak penyelesaian
C. penyelesaiannya adalah $x = y = z = 0$
D. sistem pasti tidak mempunyai penyelesaian
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 243. Soal `79bfaba1aa0b987ddb9f80b3`

Untuk $B = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 5 & 6 & 0 \end{pmatrix}$, seorang siswa menentukan $B^{-1}$ sebagai $\frac{1}{\|B\|}K$ dengan $K$ matriks kofaktor (tanpa transpos). Elemen baris kedua kolom pertama hasil yang benar dikurangi hasil siswa adalah ....

| Opsi | Isi |
|---|---|
| A | 20 |
| B | 2 |
| C | 18 |
| D | -2 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `53b2d96ad6ccc7d06dfa4abe0f662a97ee87c44a8d9aec0a6b4ce931bf909716`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Untuk $B = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 5 & 6 & 0 \end{pmatrix}$, seorang siswa menentukan $B^{-1}$ sebagai $\frac{1}{|B|}K$ dengan $K$ matriks kofaktor (tanpa transpos). Elemen baris kedua kolom pertama hasil yang benar dikurangi hasil siswa adalah ....
Pilihan: A. 20
B. 2
C. 18
D. -2
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 244. Soal `91668276fd25bd75d5b68e3b`

Matriks $A$ dan $P$ berordo sama dengan $\|A\| = 5$ dan $\|P\| = -2$, dan $P$ mempunyai invers. Nilai $\|P^{-1}AP\|$ adalah ....

| Opsi | Isi |
|---|---|
| A | $5$ |
| B | $-10$ |
| C | $-\frac{5}{2}$ |
| D | $20$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b5b54d8ced871e66137f74d15647e8b4b7857b7a64a25fa820dcc4cf0b06854a`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$ dan $P$ berordo sama dengan $|A| = 5$ dan $|P| = -2$, dan $P$ mempunyai invers. Nilai $|P^{-1}AP|$ adalah ....
Pilihan: A. $5$
B. $-10$
C. $-\frac{5}{2}$
D. $20$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 245. Soal `5d2975efa6814c63a43e99c9`

Diketahui $A = \begin{pmatrix} 7 & 3 \\ 4 & 2 \end{pmatrix}$, $B = \begin{pmatrix} 9 & -4 \\ 5 & 6 \end{pmatrix}$, dan matriks $C$ memenuhi $AC = B$. Nilai determinan $C$ adalah ....

| Opsi | Isi |
|---|---|
| A | $37$ |
| B | $72$ |
| C | $76$ |
| D | $148$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `cda25bad2f3c61a337b267b246ffadf8c2e28cff774538140fe39a16b6d26b92`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix} 7 & 3 \\ 4 & 2 \end{pmatrix}$, $B = \begin{pmatrix} 9 & -4 \\ 5 & 6 \end{pmatrix}$, dan matriks $C$ memenuhi $AC = B$. Nilai determinan $C$ adalah ....
Pilihan: A. $37$
B. $72$
C. $76$
D. $148$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 246. Soal `b1a62e976fec3750bad0cf73`

Matriks $P = \begin{pmatrix} 2 & 7 \\ 3 & 6 \end{pmatrix}$ dan $Q = \begin{pmatrix} 4 & -5 \\ 6 & 6 \end{pmatrix}$. Jika matriks $R$ memenuhi $PR = Q$, nilai $\|R\|$ adalah ....

| Opsi | Isi |
|---|---|
| A | $-6$ |
| B | $6$ |
| C | $-486$ |
| D | $63$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `537e40ed6605e04d28eca6cc2bba59b77fb85f76ee4c0354f52c6ec29ebf8cac`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $P = \begin{pmatrix} 2 & 7 \\ 3 & 6 \end{pmatrix}$ dan $Q = \begin{pmatrix} 4 & -5 \\ 6 & 6 \end{pmatrix}$. Jika matriks $R$ memenuhi $PR = Q$, nilai $|R|$ adalah ....
Pilihan: A. $-6$
B. $6$
C. $-486$
D. $63$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 247. Soal `8d1df9957e62c0b5cbe73b82`

Tabel berikut menunjukkan banyak satuan makanan yang dikonsumsi setiap bakteri per hari.<br><br>\| Makanan \| Strain I \| Strain II \| Strain III \|<br>\|---\|---\|---\|---\|<br>\| A \| 2 \| 1 \| 3 \|<br>\| B \| 1 \| 2 \| 2 \|<br>\| C \| 3 \| 1 \| 1 \|<br><br>Seorang peneliti menempatkan tiga jenis bakteri dalam satu tabung. Setiap hari tersedia 630 satuan makanan A, 580 satuan makanan B, dan 590 satuan makanan C, dan semuanya habis dikonsumsi. Berdasarkan tabel, banyak bakteri Strain II adalah ....

| Opsi | Isi |
|---|---|
| A | 120 |
| B | -1500 |
| C | 150 |
| D | 80 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9d1ab4b6d81eebc205eec3327f930267b4e29cac0717326e012efffce759bde3`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Tabel berikut menunjukkan banyak satuan makanan yang dikonsumsi setiap bakteri per hari.

| Makanan | Strain I | Strain II | Strain III |
|---|---|---|---|
| A | 2 | 1 | 3 |
| B | 1 | 2 | 2 |
| C | 3 | 1 | 1 |

Seorang peneliti menempatkan tiga jenis bakteri dalam satu tabung. Setiap hari tersedia 630 satuan makanan A, 580 satuan makanan B, dan 590 satuan makanan C, dan semuanya habis dikonsumsi. Berdasarkan tabel, banyak bakteri Strain II adalah ....
Pilihan: A. 120
B. -1500
C. 150
D. 80
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 248. Soal `451bcb9a8f79d3889f1c7345`

Banyak kilogram pakan yang dihabiskan seekor ternak per bulan.<br><br>\| Pakan \| Ayam \| Bebek \| Puyuh \|<br>\|---\|---\|---\|---\|<br>\| Dedak \| 1 \| 2 \| 1 \|<br>\| Jagung \| 2 \| 1 \| 3 \|<br>\| Konsentrat \| 1 \| 1 \| 2 \|<br><br>Sebuah peternakan memelihara ayam, bebek, dan puyuh. Selama sebulan, tersedia 120 kg dedak, 195 kg jagung, dan 125 kg konsentrat yang habis terpakai sesuai tabel. Banyak puyuh yang dipelihara adalah ....

| Opsi | Isi |
|---|---|
| A | 30 |
| B | 40 |
| C | 25 |
| D | -60 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5f5d454689d6bdda0143751d99af9cbf253ba06a16be5fcbd6b987a6ed653f5a`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Banyak kilogram pakan yang dihabiskan seekor ternak per bulan.

| Pakan | Ayam | Bebek | Puyuh |
|---|---|---|---|
| Dedak | 1 | 2 | 1 |
| Jagung | 2 | 1 | 3 |
| Konsentrat | 1 | 1 | 2 |

Sebuah peternakan memelihara ayam, bebek, dan puyuh. Selama sebulan, tersedia 120 kg dedak, 195 kg jagung, dan 125 kg konsentrat yang habis terpakai sesuai tabel. Banyak puyuh yang dipelihara adalah ....
Pilihan: A. 30
B. 40
C. 25
D. -60
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 249. Soal `c01636ed4525912ab19b5938`

Diketahui $X = \begin{pmatrix} 3 & 1 \\ 5 & 2 \end{pmatrix}$ dan $Y = \begin{pmatrix} 2 & 4 \\ 1 & 3 \end{pmatrix}$. Matriks $X^{-1} + Y^{-1}$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix} \frac{7}{2} & -\frac{3}{2} \\ -7 & 4 \end{pmatrix}$ |
| B | $\begin{pmatrix} -1 & 1 \\ \frac{6}{5} & -1 \end{pmatrix}$ |
| C | $\begin{pmatrix} 5 & -5 \\ -6 & 5 \end{pmatrix}$ |
| D | $\begin{pmatrix} \frac{7}{2} & -3 \\ -\frac{11}{2} & 4 \end{pmatrix}$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9ec1c8c02881ccf38189a729b0703daeb7492a6c434cb71b1f7d6d66e7eec763`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $X = \begin{pmatrix} 3 & 1 \\ 5 & 2 \end{pmatrix}$ dan $Y = \begin{pmatrix} 2 & 4 \\ 1 & 3 \end{pmatrix}$. Matriks $X^{-1} + Y^{-1}$ adalah ....
Pilihan: A. $\begin{pmatrix} \frac{7}{2} & -\frac{3}{2} \\ -7 & 4 \end{pmatrix}$
B. $\begin{pmatrix} -1 & 1 \\ \frac{6}{5} & -1 \end{pmatrix}$
C. $\begin{pmatrix} 5 & -5 \\ -6 & 5 \end{pmatrix}$
D. $\begin{pmatrix} \frac{7}{2} & -3 \\ -\frac{11}{2} & 4 \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 250. Soal `d4fb4eac67645248cba31998`

Diketahui $X = \begin{pmatrix} 4 & 3 \\ 1 & 1 \end{pmatrix}$ dan $Y = \begin{pmatrix} 5 & 2 \\ 3 & 2 \end{pmatrix}$. Elemen baris pertama kolom kedua dari matriks $(X + Y)^{-1}$ adalah ....

| Opsi | Isi |
|---|---|
| A | $-\frac{5}{7}$ |
| B | $-5$ |
| C | $-\frac{7}{2}$ |
| D | $\frac{5}{7}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c26d413d20e3f0c6cbe374dee9219880f38df250ac1539dd0ddb4da7bafb4082`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $X = \begin{pmatrix} 4 & 3 \\ 1 & 1 \end{pmatrix}$ dan $Y = \begin{pmatrix} 5 & 2 \\ 3 & 2 \end{pmatrix}$. Elemen baris pertama kolom kedua dari matriks $(X + Y)^{-1}$ adalah ....
Pilihan: A. $-\frac{5}{7}$
B. $-5$
C. $-\frac{7}{2}$
D. $\frac{5}{7}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 251. Soal `52f42db228d908c8e414216c`

Diketahui $M = \begin{pmatrix} 2 & -1 & 4 \\ 0 & 3 & 1 \\ 5 & 2 & -2 \end{pmatrix}$. Nilai $\|2M\|$ adalah ....

| Opsi | Isi |
|---|---|
| A | $-324$ |
| B | $-162$ |
| C | $-648$ |
| D | $648$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5f50c9a0d361b87735b895b1045e56e2339e1ef1ab67ddb206917e2734d01b08`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $M = \begin{pmatrix} 2 & -1 & 4 \\ 0 & 3 & 1 \\ 5 & 2 & -2 \end{pmatrix}$. Nilai $|2M|$ adalah ....
Pilihan: A. $-324$
B. $-162$
C. $-648$
D. $648$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 252. Soal `b23d66751de2c1860961e38e`

Diketahui $A = \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix}$ dan $B = \begin{pmatrix} 1 & -2 \\ 3 & 5 \end{pmatrix}$. Jika $C$ matriks berordo $2 \times 2$ dengan $\|C\| = -2$, nilai $\|ABC\|$ adalah ....

| Opsi | Isi |
|---|---|
| A | $220$ |
| B | $-220$ |
| C | $-20$ |
| D | $19$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ee9d1aeae43b29598fee4787b310f3d25b7a2ed129e638fe8cf246fbe68813db`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix}$ dan $B = \begin{pmatrix} 1 & -2 \\ 3 & 5 \end{pmatrix}$. Jika $C$ matriks berordo $2 \times 2$ dengan $|C| = -2$, nilai $|ABC|$ adalah ....
Pilihan: A. $220$
B. $-220$
C. $-20$
D. $19$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 253. Soal `d5b2598dcc9878be03b8f3c1`

Dengan Metode Sarrus, nilai $\begin{vmatrix} 2 & -1 & 3 \\ 4 & 0 & -2 \\ 1 & 5 & 3 \end{vmatrix}$ adalah ....

| Opsi | Isi |
|---|---|
| A | $94$ |
| B | $30$ |
| C | $-94$ |
| D | $62$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `edf4b20d5333c401a3075fe903313f3f6c3ede26e3054e86f69f447b53acaaf3`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Dengan Metode Sarrus, nilai $\begin{vmatrix} 2 & -1 & 3 \\ 4 & 0 & -2 \\ 1 & 5 & 3 \end{vmatrix}$ adalah ....
Pilihan: A. $94$
B. $30$
C. $-94$
D. $62$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 254. Soal `1e3b92870a7752e70155dc4c`

Determinan $\begin{vmatrix} 0 & 3 & 2 \\ 5 & 1 & -1 \\ 0 & 4 & 6 \end{vmatrix}$ jika dihitung dengan ekspansi kofaktor sepanjang kolom pertama adalah ....

| Opsi | Isi |
|---|---|
| A | $50$ |
| B | $-50$ |
| C | $-130$ |
| D | $-10$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `152394b32b30a600cd9fe80e1cbe557cc842725a43e8318ef958e75dc67b15ba`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Determinan $\begin{vmatrix} 0 & 3 & 2 \\ 5 & 1 & -1 \\ 0 & 4 & 6 \end{vmatrix}$ jika dihitung dengan ekspansi kofaktor sepanjang kolom pertama adalah ....
Pilihan: A. $50$
B. $-50$
C. $-130$
D. $-10$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 255. Soal `eaeec0cfc299c320e5842faf`

Matriks $A = \begin{pmatrix} 2 & 3 & 1 \\ 1 & x & 2 \\ 4 & 1 & 3 \end{pmatrix}$ merupakan matriks singular. Nilai $x$ adalah ....

| Opsi | Isi |
|---|---|
| A | $-24$ |
| B | $-12$ |
| C | $-6$ |
| D | $6$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6affec4a576c540724a0b8bb87b2f1aa9760f9e2bdf8d583d347d337eaaff931`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A = \begin{pmatrix} 2 & 3 & 1 \\ 1 & x & 2 \\ 4 & 1 & 3 \end{pmatrix}$ merupakan matriks singular. Nilai $x$ adalah ....
Pilihan: A. $-24$
B. $-12$
C. $-6$
D. $6$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 256. Soal `7344b219c13561a2563c0407`

Matriks $A = \begin{pmatrix} x & 6 \\ 1 & x - 5 \end{pmatrix}$ tidak mempunyai invers. Nilai $x$ terbesar yang mungkin adalah ....

| Opsi | Isi |
|---|---|
| A | $-1$ |
| B | $5$ |
| C | $6$ |
| D | $1$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `399d679b4c2b074c3743c43212971a71f90a57456a198011a8b8200c822d8cb3`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A = \begin{pmatrix} x & 6 \\ 1 & x - 5 \end{pmatrix}$ tidak mempunyai invers. Nilai $x$ terbesar yang mungkin adalah ....
Pilihan: A. $-1$
B. $5$
C. $6$
D. $1$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 257. Soal `3635ec6c4c4444f55dcf79b1`

Diketahui $A = \begin{pmatrix} 3 & x \\ 2 & 5 \end{pmatrix}$. Jika elemen baris pertama kolom kedua dari $A^{-1}$ bernilai $2$, nilai $x$ adalah ....

| Opsi | Isi |
|---|---|
| A | $8$ |
| B | $10$ |
| C | $30$ |
| D | $6$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `996329c8955c98b25af4f81220be91db965c24bccf171514c703a3e30ca6ba2f`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix} 3 & x \\ 2 & 5 \end{pmatrix}$. Jika elemen baris pertama kolom kedua dari $A^{-1}$ bernilai $2$, nilai $x$ adalah ....
Pilihan: A. $8$
B. $10$
C. $30$
D. $6$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 258. Soal `a57ec2d2ab0442c6b421679f`

Diketahui $A = \begin{pmatrix} 2 & 1 \\ 5 & 4 \end{pmatrix}$ dan $B = \begin{pmatrix} 5 & 3 \\ 17 & 6 \end{pmatrix}$. Matriks $X$ yang memenuhi $AX = B$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix} 3 & 6 \\ 9 & -3 \end{pmatrix}$ |
| B | $\begin{pmatrix} \frac{37}{3} & 6 \\ \frac{59}{3} & 9 \end{pmatrix}$ |
| C | $\begin{pmatrix} 1 & 2 \\ 3 & -1 \end{pmatrix}$ |
| D | $\begin{pmatrix} \frac{5}{3} & \frac{1}{3} \\ \frac{38}{3} & -\frac{5}{3} \end{pmatrix}$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `cbaf76052d6a6ea3113603ab8247ef0567ac4310b478e15d9ecb23c531fd0166`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix} 2 & 1 \\ 5 & 4 \end{pmatrix}$ dan $B = \begin{pmatrix} 5 & 3 \\ 17 & 6 \end{pmatrix}$. Matriks $X$ yang memenuhi $AX = B$ adalah ....
Pilihan: A. $\begin{pmatrix} 3 & 6 \\ 9 & -3 \end{pmatrix}$
B. $\begin{pmatrix} \frac{37}{3} & 6 \\ \frac{59}{3} & 9 \end{pmatrix}$
C. $\begin{pmatrix} 1 & 2 \\ 3 & -1 \end{pmatrix}$
D. $\begin{pmatrix} \frac{5}{3} & \frac{1}{3} \\ \frac{38}{3} & -\frac{5}{3} \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 259. Soal `ffa57b503656a7da211faaaf`

Diketahui $A = \begin{pmatrix} 4 & 3 \\ 3 & 3 \end{pmatrix}$ dan $B = \begin{pmatrix} 5 & 3 \\ 13 & 12 \end{pmatrix}$. Matriks $X$ yang memenuhi $XA = B$ adalah ....

| Opsi | Isi |
|---|---|
| A | $\begin{pmatrix} -8 & -9 \\ \frac{37}{3} & 13 \end{pmatrix}$ |
| B | $\begin{pmatrix} 2 & -1 \\ 1 & 3 \end{pmatrix}$ |
| C | $\begin{pmatrix} 2 & 1 \\ -1 & 3 \end{pmatrix}$ |
| D | $\begin{pmatrix} 6 & -3 \\ 3 & 9 \end{pmatrix}$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `48e9b4bbd2dec78b26724a2e9def1e2afa9563492ef1175c907e05a19de7a82c`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix} 4 & 3 \\ 3 & 3 \end{pmatrix}$ dan $B = \begin{pmatrix} 5 & 3 \\ 13 & 12 \end{pmatrix}$. Matriks $X$ yang memenuhi $XA = B$ adalah ....
Pilihan: A. $\begin{pmatrix} -8 & -9 \\ \frac{37}{3} & 13 \end{pmatrix}$
B. $\begin{pmatrix} 2 & -1 \\ 1 & 3 \end{pmatrix}$
C. $\begin{pmatrix} 2 & 1 \\ -1 & 3 \end{pmatrix}$
D. $\begin{pmatrix} 6 & -3 \\ 3 & 9 \end{pmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 260. Soal `39aa24d976287d60e74968ab`

Anto membeli 3 buku dan 2 pensil dengan membayar Rp21.000,00. Budi membeli 5 buku dan 4 pensil dengan membayar Rp37.000,00. Jika sistem persamaannya diselesaikan dengan invers matriks, harga 4 buku dan 3 pensil adalah ....

| Opsi | Isi |
|---|---|
| A | Rp58.000,00 |
| B | Rp29.000,00 |
| C | Rp8.000,00 |
| D | Rp27.000,00 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7fbec453b23fd561116a1e6b082c75f8760458ada6c598df4fbe2840956c056d`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Anto membeli 3 buku dan 2 pensil dengan membayar Rp21.000,00. Budi membeli 5 buku dan 4 pensil dengan membayar Rp37.000,00. Jika sistem persamaannya diselesaikan dengan invers matriks, harga 4 buku dan 3 pensil adalah ....
Pilihan: A. Rp58.000,00
B. Rp29.000,00
C. Rp8.000,00
D. Rp27.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 261. Soal `7968db6a7f655f76118bf817`

Diketahui $A = \begin{pmatrix} 1 & 2 & 1 \\ 0 & 3 & 1 \\ 2 & 1 & 4 \end{pmatrix}$. Elemen baris pertama kolom ketiga dari $A^{-1}$ adalah ....

| Opsi | Isi |
|---|---|
| A | $-1$ |
| B | $\frac{1}{9}$ |
| C | $-\frac{2}{3}$ |
| D | $-\frac{1}{9}$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9d0eb36f439bfdde73de98800c57edfc10f64b28f690a20fd3352e0623561602`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $A = \begin{pmatrix} 1 & 2 & 1 \\ 0 & 3 & 1 \\ 2 & 1 & 4 \end{pmatrix}$. Elemen baris pertama kolom ketiga dari $A^{-1}$ adalah ....
Pilihan: A. $-1$
B. $\frac{1}{9}$
C. $-\frac{2}{3}$
D. $-\frac{1}{9}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 262. Soal `d225094dfdad3d9ea90de30b`

Dengan determinan, nilai $z$ dari sistem $\begin{cases} 2x + y + z = 6 \\ x - y + 3z = 12 \\ 3x + 2y - z = 1 \end{cases}$ adalah ....

| Opsi | Isi |
|---|---|
| A | $15$ |
| B | $-1$ |
| C | $2$ |
| D | $3$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `87b1d887446a89c4b8dc5f31b3c879534763fc24524e9dad2b8b0a747621870c`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Dengan determinan, nilai $z$ dari sistem $\begin{cases} 2x + y + z = 6 \\ x - y + 3z = 12 \\ 3x + 2y - z = 1 \end{cases}$ adalah ....
Pilihan: A. $15$
B. $-1$
C. $2$
D. $3$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 263. Soal `b421dfa869cb59d9419a2c64`

Pada matriks $A = \begin{pmatrix} 2 & x & 1 \\ 4 & 3 & x \\ 1 & 5 & 2 \end{pmatrix}$, kofaktor $k_{23} = -4$. Nilai $x$ adalah ....

| Opsi | Isi |
|---|---|
| A | $-6$ |
| B | $4$ |
| C | $14$ |
| D | $6$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fc95000cc0ebeb2b03b6c6b29251be3a85be9c8b97db2aba8969d6e2b0bda69f`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada matriks $A = \begin{pmatrix} 2 & x & 1 \\ 4 & 3 & x \\ 1 & 5 & 2 \end{pmatrix}$, kofaktor $k_{23} = -4$. Nilai $x$ adalah ....
Pilihan: A. $-6$
B. $4$
C. $14$
D. $6$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 264. Soal `c5f377cefa62f8e05e256d99`

Matriks $A$ dan $B$ berordo $3 \times 3$ dengan $\|A\| = 2$ dan $\|B\| = -3$. Nilai $\|2AB\|$ adalah ....

| Opsi | Isi |
|---|---|
| A | $-12$ |
| B | $-24$ |
| C | $48$ |
| D | $-48$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3ca829eef71ae98a6d94593807230a2c9d4bc6e04469aa61c4861823399ed663`. Bukti verifikasi AI tetap tercatat sebagai silver.

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
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Matriks $A$ dan $B$ berordo $3 \times 3$ dengan $|A| = 2$ dan $|B| = -3$. Nilai $|2AB|$ adalah ....
Pilihan: A. $-12$
B. $-24$
C. $48$
D. $-48$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
