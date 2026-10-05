# Validasi ulang soal kelas 9 — Gemini blind N=3 dan diagnostik IndoBERT

**Batch belum selesai:** 9/810 run awal sukses; 0 item tercatat membutuhkan adjudikasi setelah run lengkap. Distribusi berikut masih sementara; item tanpa keputusan ditampilkan sebagai undecided.

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v10-blind-smp9-key-verified`. Rubrik: `math-rubric-3x4x3-v8-smp9-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 9 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan menjadi keputusan silver operasional.

Checkpoint dikunci dengan SHA-256 sebelum pemeriksaan scope IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Artifact berada di luar cakupan kelas 9, sehingga seluruh head abstain dan tidak menghasilkan ukuran agreement dengan label blind.

Jumlah soal: 270; distribusi label advisory: `{"mathCognitiveDomain": {"undecided": 267, "knowing": 1, "applying": 2, "reasoning": 0}, "knowledgeDimension": {"undecided": 267, "conceptual": 2, "procedural": 1, "factual": 0, "metacognitive": 0}, "intendedDifficulty": {"undecided": 267, "Easy": 2, "Medium": 1, "Hard": 0}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"knowing": 1, "applying": 2, "reasoning": 0}, "knowledgeDimension": {"conceptual": 2, "procedural": 1, "factual": 0, "metacognitive": 0}, "intendedDifficulty": {"Easy": 2, "Medium": 1, "Hard": 0}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"needs_ai_review": 267, "silver_ready": 3}`.
Run awal sukses: 9/810; adjudikasi: 2; token sukses tercatat: 33,760.

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

Untuk kelas 9, encoder dan head IndoBERT tidak dijalankan karena cakupan artifact adalah kelas [1, 2, 3, 4, 5, 6], jalur ['regular']. Probabilitas kosong, label/confidence/entropy null, dan action abstain berasal dari pemeriksaan scope runtime. Suara Gemini adalah bukti penilaian advisory, bukan probabilitas IndoBERT.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

Cakupan artifact: kelas [1, 2, 3, 4, 5, 6], jalur ['regular']. Untuk kelas 9, diagnostik mengembalikan `out_of_scope` dan `abstain`: label, confidence, dan entropy null serta probabilitas kosong. Label advisory mengikuti Gemini blind dengan rubrik SMP kelas 9.

## 1. Soal `7775cb1339c155533c46ee6f`

Keliling sebuah segitiga sama kaki adalah 54 cm. Jika $x$ adalah panjang kaki dan $y$ adalah panjang alas, model matematika yang menghubungkan keliling dan panjang sisinya adalah ....

| Opsi | Isi |
|---|---|
| A | $x + y = 54$ |
| B | $2x + y = 54$ |
| C | $x + 2y = 54$ |
| D | $2x + 2y = 54$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `953138b382ad34bfe47d528f12025584cfd5ab71a07e2f74ffcaf71c0f0edd6a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Keliling sebuah segitiga sama kaki adalah 54 cm. Jika $x$ adalah panjang kaki dan $y$ adalah panjang alas, model matematika yang menghubungkan keliling dan panjang sisinya adalah ....
Pilihan: A. $x + y = 54$
B. $2x + y = 54$
C. $x + 2y = 54$
D. $2x + 2y = 54$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `4369b350a304114f453e7b7c`

Manakah di antara persamaan berikut yang merupakan persamaan linear dua variabel?

| Opsi | Isi |
|---|---|
| A | $x + 5 = 9$ |
| B | $x^2 + y = 4$ |
| C | $xy = 6$ |
| D | $2x + 3y = 7$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e322d16b7760d94bff25f301a89d5fbb76cfdead1250bc4659e9d9e97c0e3d88`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Manakah di antara persamaan berikut yang merupakan persamaan linear dua variabel?
Pilihan: A. $x + 5 = 9$
B. $x^2 + y = 4$
C. $xy = 6$
D. $2x + 3y = 7$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `55abb206468b5af76f3a7fe3`

Harga tiket masuk sebuah konser Rp50.000,00. Jika $y$ menyatakan pendapatan dari penjualan tiket dan $x$ menyatakan banyak tiket terjual, persamaan yang sesuai adalah ....

| Opsi | Isi |
|---|---|
| A | $y = 50.000x$ |
| B | $y = 50.000 + x$ |
| C | $y = \frac{x}{50.000}$ |
| D | $x = 50.000y$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `21bebf36d86020a26fff3d848925ad6721e4a7ee3cf16f95abf25b4a29049ad6`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Harga tiket masuk sebuah konser Rp50.000,00. Jika $y$ menyatakan pendapatan dari penjualan tiket dan $x$ menyatakan banyak tiket terjual, persamaan yang sesuai adalah ....
Pilihan: A. $y = 50.000x$
B. $y = 50.000 + x$
C. $y = \frac{x}{50.000}$
D. $x = 50.000y$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `bdc51197b2514ba2e0bd05c2`

Sebuah kebun berbentuk persegi panjang memiliki keliling 36 m. Jika panjang kebun $p$ dan lebarnya $l$, maka persamaan yang menyatakan hubungan $p$ dan $l$ adalah ....

| Opsi | Isi |
|---|---|
| A | $2p + 2l = 36$ |
| B | $p + l = 36$ |
| C | $p \times l = 36$ |
| D | $2p + l = 36$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menganalisis']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c3d2b0d8381037648c306048d1e6d9e7afa74cd8926cf10f0d2585d9ca77b836`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kebun berbentuk persegi panjang memiliki keliling 36 m. Jika panjang kebun $p$ dan lebarnya $l$, maka persamaan yang menyatakan hubungan $p$ dan $l$ adalah ....
Pilihan: A. $2p + 2l = 36$
B. $p + l = 36$
C. $p \times l = 36$
D. $2p + l = 36$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `a11bf73b8e60d039bcd0ec8b`

Pada persamaan linear dua variabel $4x - 7y = 12$, koefisien dari $y$ adalah ....

| Opsi | Isi |
|---|---|
| A | $-7$ |
| B | $4$ |
| C | $7$ |
| D | $12$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f5ed150e80c0b01a2826611670c5a3af0bfd7afd618611e408bbe6f07d1021db`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada persamaan linear dua variabel $4x - 7y = 12$, koefisien dari $y$ adalah ....
Pilihan: A. $-7$
B. $4$
C. $7$
D. $12$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `8900a9266742debdf88a718c`

Tissa pergi ke toko alat tulis. Ia membeli 4 buku tulis dan 2 bolpoin dengan membayar Rp16.000,00. Jika $m$ adalah harga 1 buku tulis dan $n$ adalah harga 1 bolpoin, model matematikanya adalah ....

| Opsi | Isi |
|---|---|
| A | $2m + 4n = 16.000$ |
| B | $m + n = 16.000$ |
| C | $4m + 2n = 16.000$ |
| D | $4m + 2n = 16$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a681e6a3a692766d0d58226378d9b27ed1357d07b5a9d23de618f6b6958ea571`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Tissa pergi ke toko alat tulis. Ia membeli 4 buku tulis dan 2 bolpoin dengan membayar Rp16.000,00. Jika $m$ adalah harga 1 buku tulis dan $n$ adalah harga 1 bolpoin, model matematikanya adalah ....
Pilihan: A. $2m + 4n = 16.000$
B. $m + n = 16.000$
C. $4m + 2n = 16.000$
D. $4m + 2n = 16$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `045922814a60fb192d2e1fb0`

Seorang pembeli memesan nasi goreng yang harganya Rp15.000,00 per porsi. Jika $b$ adalah total pembayaran dan $n$ adalah banyak porsi, hubungan $b$ dan $n$ dinyatakan dengan ....

| Opsi | Isi |
|---|---|
| A | $n = 15.000b$ |
| B | $b = 15.000n$ |
| C | $b = 15.000 + n$ |
| D | $b = \frac{n}{15.000}$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menganalisis']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `af5a01441b82f8634a20a2fe9ca47e19fa00035d99be88d84d5b251e3820af04`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Seorang pembeli memesan nasi goreng yang harganya Rp15.000,00 per porsi. Jika $b$ adalah total pembayaran dan $n$ adalah banyak porsi, hubungan $b$ dan $n$ dinyatakan dengan ....
Pilihan: A. $n = 15.000b$
B. $b = 15.000n$
C. $b = 15.000 + n$
D. $b = \frac{n}{15.000}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `f0ddaa09ac9ce79597db18bb`

Pasangan berurutan yang merupakan penyelesaian dari persamaan $3x + y = 10$ adalah ....

| Opsi | Isi |
|---|---|
| A | $(5, 5)$ |
| B | $(4, 2)$ |
| C | $(2, 4)$ |
| D | $(3, 2)$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0b8d246026012c8d154b5205f9dfbb2cbf0a829b9a34c83bdc5c95f8d7840fe0`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Pasangan berurutan yang merupakan penyelesaian dari persamaan $3x + y = 10$ adalah ....
Pilihan: A. $(5, 5)$
B. $(4, 2)$
C. $(2, 4)$
D. $(3, 2)$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 9. Soal `2f86274b791b9607888c59ae`

Di kantin sekolah, Dika membeli 2 gelas teh dan 3 potong roti dan membayar Rp17.000,00. Jika $t$ adalah harga segelas teh dan $r$ adalah harga sepotong roti, persamaan yang sesuai adalah ....

| Opsi | Isi |
|---|---|
| A | $5tr = 17.000$ |
| B | $3t + 2r = 17.000$ |
| C | $t + r = 17.000$ |
| D | $2t + 3r = 17.000$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `45f4153abf432f9d111c792003e6a872a83cc2955e7a22575cb730eee846ac0d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Di kantin sekolah, Dika membeli 2 gelas teh dan 3 potong roti dan membayar Rp17.000,00. Jika $t$ adalah harga segelas teh dan $r$ adalah harga sepotong roti, persamaan yang sesuai adalah ....
Pilihan: A. $5tr = 17.000$
B. $3t + 2r = 17.000$
C. $t + r = 17.000$
D. $2t + 3r = 17.000$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `ac129a72ae5a3dd3bf8d3fc8`

Jika tidak dituliskan secara spesifik, nilai variabel pada persamaan linear dua variabel mewakili himpunan bilangan ....

| Opsi | Isi |
|---|---|
| A | bulat |
| B | asli |
| C | cacah |
| D | real |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `19079dc2e3c03a1e824a01beac04355d420c8b2c295ac393e38b7b451329d2ad`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika tidak dituliskan secara spesifik, nilai variabel pada persamaan linear dua variabel mewakili himpunan bilangan ....
Pilihan: A. bulat
B. asli
C. cacah
D. real
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `5263011920abb5f3c19b2bb7`

Harga 3 ekor sapi dan 4 ekor kambing Rp70.000.000,00. Jika $s$ adalah harga seekor sapi dan $k$ adalah harga seekor kambing, persamaan yang diperoleh adalah ....

| Opsi | Isi |
|---|---|
| A | $s + k = 70.000.000$ |
| B | $7sk = 70.000.000$ |
| C | $3s + 4k = 70.000.000$ |
| D | $4s + 3k = 70.000.000$ |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Harga 3 ekor sapi adalah 3s dan harga 4 ekor kambing adalah 4k. Total harga adalah 3s + 4k = 70.000.000.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ad8a88595d48912aad0675db8dae65f4852f0abf4928d30525ee1b6d59c11b3d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2702 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2715 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2741 |

Run 1 — solusi: Harga 3 ekor sapi adalah 3 dikali harga seekor sapi (3s) dan harga 4 ekor kambing adalah 4 dikali harga seekor kambing (4k). Total harga adalah 3s + 4k = 70.000.000.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk menerjemahkan situasi verbal ke dalam model matematika (persamaan linear dua variabel) secara langsung tanpa perlu melakukan perhitungan atau manipulasi aljabar lebih lanjut.. Bukti: Harga 3 ekor sapi dan 4 ekor kambing Rp70.000.000,00; Jika s adalah harga seekor sapi dan k adalah harga seekor kambing, persamaan yang diperoleh adalah
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep variabel dan koefisien dalam konteks persamaan linear dua variabel untuk merepresentasikan hubungan harga.. Bukti: persamaan yang diperoleh adalah
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (straightforward) karena hanya meminta pembentukan model matematika dari pernyataan yang diberikan. Tidak ada langkah penyelesaian sistem atau manipulasi yang diperlukan.. Bukti: Harga 3 ekor sapi dan 4 ekor kambing Rp70.000.000,00; persamaan yang diperoleh adalah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel dan koefisien dalam aljabar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 sudah sangat familiar dengan pemodelan SPLDV sederhana seperti ini. Soal tidak menuntut integrasi langkah atau strategi kompleks. |

Run 2 — solusi: Harga 3 ekor sapi adalah 3 dikali harga seekor sapi (3s) dan harga 4 ekor kambing adalah 4 dikali harga seekor kambing (4k). Total harga adalah 3s + 4k = 70.000.000.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk menerjemahkan situasi kontekstual ke dalam bentuk model matematika (persamaan linear dua variabel) secara langsung tanpa perlu melakukan perhitungan atau manipulasi aljabar lebih lanjut.. Bukti: Harga 3 ekor sapi dan 4 ekor kambing Rp70.000.000,00; s adalah harga seekor sapi dan k adalah harga seekor kambing, persamaan yang diperoleh adalah
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep variabel dan koefisien dalam konteks persamaan linear dua variabel untuk merepresentasikan hubungan harga.. Bukti: persamaan yang diperoleh adalah
- Intended difficulty `classify/Easy`: Soal ini bersifat sangat langsung (direct translation). Siswa hanya perlu mengidentifikasi koefisien (jumlah hewan) dan variabel (harga per hewan) untuk membentuk persamaan. Tidak ada langkah perencanaan atau integrasi yang kompleks.. Bukti: Harga 3 ekor sapi dan 4 ekor kambing Rp70.000.000,00; persamaan yang diperoleh adalah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel dan koefisien dalam aljabar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal dasar untuk materi SPLDV kelas 9 yang menguji kemampuan pemodelan sederhana. Tidak ada tuntutan kognitif tinggi. |

Run 3 — solusi: Harga 3 ekor sapi adalah 3 dikali harga seekor sapi (3s). Harga 4 ekor kambing adalah 4 dikali harga seekor kambing (4k). Total harga adalah 3s + 4k = 70.000.000.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk menerjemahkan situasi verbal ke dalam bentuk persamaan linear dua variabel. Ini adalah tugas mengenali dan menerapkan konsep dasar pemodelan matematika.. Bukti: Harga 3 ekor sapi dan 4 ekor kambing Rp70.000.000,00; s adalah harga seekor sapi dan k adalah harga seekor kambing, persamaan yang diperoleh adalah
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara kuantitas (banyak ekor) dan variabel (harga per ekor) untuk membentuk model matematika yang tepat.. Bukti: persamaan yang diperoleh adalah
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (straightforward) dalam menerjemahkan kalimat ke dalam model matematika tanpa perlu manipulasi aljabar atau penyelesaian sistem persamaan. Siswa hanya perlu mengidentifikasi koefisien dan variabel yang sesuai.. Bukti: Harga 3 ekor sapi dan 4 ekor kambing Rp70.000.000,00; persamaan yang diperoleh adalah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel dan koefisien dalam konteks harga. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal dasar pemodelan SPLDV yang sesuai untuk kelas 9, di mana siswa diharapkan mampu mengubah masalah kontekstual sederhana menjadi bentuk persamaan linear. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4252`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal meminta siswa untuk menerjemahkan pernyataan verbal ke dalam model matematika (persamaan linear dua variabel) secara langsung. Ini adalah tugas mengenali hubungan antara kuantitas dan variabel.
- Dimensi pengetahuan `conceptual`: Siswa perlu memahami konsep variabel dan koefisien dalam konteks persamaan linear dua variabel untuk merepresentasikan hubungan harga.
- Intended difficulty `Easy`: Soal ini bersifat sangat langsung (direct translation). Siswa hanya perlu mengidentifikasi koefisien (jumlah hewan) dan variabel (harga per hewan) untuk membentuk persamaan. Tidak ada langkah perencanaan atau integrasi yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel dan koefisien dalam aljabar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal dasar untuk materi SPLDV kelas 9 yang menguji kemampuan pemodelan sederhana. Tidak ada tuntutan kognitif tinggi. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Harga 3 ekor sapi dan 4 ekor kambing Rp70.000.000,00. Jika $s$ adalah harga seekor sapi dan $k$ adalah harga seekor kambing, persamaan yang diperoleh adalah ....
Pilihan: A. $s + k = 70.000.000$
B. $7sk = 70.000.000$
C. $3s + 4k = 70.000.000$
D. $4s + 3k = 70.000.000$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 12. Soal `4a1d8481803f8c9f2794c996`

Seorang pedagang membeli 6 kg apel dan 2 kg jeruk dengan harga Rp240.000,00. Jika $a$ adalah harga 1 kg apel dan $j$ adalah harga 1 kg jeruk, persamaan yang diperoleh adalah ....

| Opsi | Isi |
|---|---|
| A | $8aj = 240.000$ |
| B | $2a + 6j = 240.000$ |
| C | $6a + 2j = 240.000$ |
| D | $a + j = 240.000$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3bcebc9184362657804d68b6b46840e908b7c8275bfb9f2eb7e503b9917539d0`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Seorang pedagang membeli 6 kg apel dan 2 kg jeruk dengan harga Rp240.000,00. Jika $a$ adalah harga 1 kg apel dan $j$ adalah harga 1 kg jeruk, persamaan yang diperoleh adalah ....
Pilihan: A. $8aj = 240.000$
B. $2a + 6j = 240.000$
C. $6a + 2j = 240.000$
D. $a + j = 240.000$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 13. Soal `88af158369cc112ebd739c9d`

Diketahui persamaan $2x + 3y = 18$. Jika $x = 6$, maka nilai $y$ adalah ....

| Opsi | Isi |
|---|---|
| A | $6$ |
| B | $2$ |
| C | $4$ |
| D | $10$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `20b8ff130b7aed0bd98a1fab626962aa8bdd587a0a1b1013027fa132a1586b04`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui persamaan $2x + 3y = 18$. Jika $x = 6$, maka nilai $y$ adalah ....
Pilihan: A. $6$
B. $2$
C. $4$
D. $10$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `ccdd6ca8c3002241585b0ccf`

Sebuah warnet menetapkan tarif Rp5.000,00 per jam dan biaya pendaftaran Rp10.000,00 satu kali. Jika $b$ adalah total biaya dan $j$ adalah lama pemakaian dalam jam, persamaan yang sesuai adalah ....

| Opsi | Isi |
|---|---|
| A | $b = 5.000j + 10.000$ |
| B | $b = 5.000j - 10.000$ |
| C | $b = 15.000j$ |
| D | $b = 10.000j + 5.000$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e7c0d489614cd335c99b87948e56120ee2ffdff67b2acc6e706bfc8720b68f9b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah warnet menetapkan tarif Rp5.000,00 per jam dan biaya pendaftaran Rp10.000,00 satu kali. Jika $b$ adalah total biaya dan $j$ adalah lama pemakaian dalam jam, persamaan yang sesuai adalah ....
Pilihan: A. $b = 5.000j + 10.000$
B. $b = 5.000j - 10.000$
C. $b = 15.000j$
D. $b = 10.000j + 5.000$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 15. Soal `44432153f4fe1141d805590f`

Jika $x$ dan $y$ adalah bilangan real, banyak penyelesaian dari persamaan $x + y = 5$ adalah ....

| Opsi | Isi |
|---|---|
| A | 6 pasangan |
| B | 5 pasangan |
| C | tepat 1 pasangan |
| D | tak hingga banyaknya |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `15b00f45e7502162be59e9f19844cb6c8b9f1789d1d5afa2d8031e610dd1eb00`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika $x$ dan $y$ adalah bilangan real, banyak penyelesaian dari persamaan $x + y = 5$ adalah ....
Pilihan: A. 6 pasangan
B. 5 pasangan
C. tepat 1 pasangan
D. tak hingga banyaknya
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `f3e712b41cf5cfb4630510e4`

Diketahui persamaan linear dua variabel $4x + y = 20$ dengan $x$ dan $y$ bilangan bulat positif. Dari semua pasangan $(x, y)$ yang memenuhi, nilai $x + y$ yang terbesar adalah ....

| Opsi | Isi |
|---|---|
| A | $8$ |
| B | $20$ |
| C | $17$ |
| D | $16$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `611cc552cc3eab9838cb73e7844d46f21a6a78268d06c04d6ab8e3762a01ad1f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui persamaan linear dua variabel $4x + y = 20$ dengan $x$ dan $y$ bilangan bulat positif. Dari semua pasangan $(x, y)$ yang memenuhi, nilai $x + y$ yang terbesar adalah ....
Pilihan: A. $8$
B. $20$
C. $17$
D. $16$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 17. Soal `a73d94fb5c38278b7e3f9bad`

Di sebuah kandang terdapat $x$ ekor ayam (2 kaki) dan $y$ ekor kambing (4 kaki) dengan jumlah kaki seluruhnya 28. Banyak ayam dan banyak kambing adalah bilangan cacah, dan kandang berisi sekurang-kurangnya satu ayam dan satu kambing. Jumlah hewan terbanyak yang mungkin ada di kandang tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | 7 ekor |
| B | 14 ekor |
| C | 8 ekor |
| D | 13 ekor |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9e9681cbe8045d2ab6611132c30d272df9e5955e99eb25f1e4b279bec57e965c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Di sebuah kandang terdapat $x$ ekor ayam (2 kaki) dan $y$ ekor kambing (4 kaki) dengan jumlah kaki seluruhnya 28. Banyak ayam dan banyak kambing adalah bilangan cacah, dan kandang berisi sekurang-kurangnya satu ayam dan satu kambing. Jumlah hewan terbanyak yang mungkin ada di kandang tersebut adalah ....
Pilihan: A. 7 ekor
B. 14 ekor
C. 8 ekor
D. 13 ekor
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `9031f917d70f7b9db2fcc074`

Harga tiket sebuah pertunjukan Rp40.000,00 dan biaya operasional Rp1.800.000,00 per hari. Jika $y$ menyatakan laba (pendapatan dikurangi biaya operasional) dan $x$ menyatakan banyak tiket terjual, pada suatu hari laba Rp2.600.000,00. Pada hari lain terjual 20 tiket lebih sedikit. Laba pada hari lain tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | Rp3.600.000,00 |
| B | Rp1.800.000,00 |
| C | Rp3.400.000,00 |
| D | Rp800.000,00 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fac4e04af4561c05d09d6dc9f2db8e20034162eb9bf6e6bc6f77b2528f2d7534`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Harga tiket sebuah pertunjukan Rp40.000,00 dan biaya operasional Rp1.800.000,00 per hari. Jika $y$ menyatakan laba (pendapatan dikurangi biaya operasional) dan $x$ menyatakan banyak tiket terjual, pada suatu hari laba Rp2.600.000,00. Pada hari lain terjual 20 tiket lebih sedikit. Laba pada hari lain tersebut adalah ....
Pilihan: A. Rp3.600.000,00
B. Rp1.800.000,00
C. Rp3.400.000,00
D. Rp800.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 19. Soal `425f527c4d2d981b100e9d58`

Rani pergi ke toko alat tulis. Ia membeli 4 buku tulis dan 3 bolpoin dengan membayar Rp50.000,00. Harga satu buku tulis dan harga satu bolpoin masing-masing dinyatakan dalam ribuan rupiah berupa bilangan bulat positif, dan harga buku tulis lebih mahal daripada harga bolpoin. Banyak pasangan harga (buku tulis, bolpoin) yang mungkin adalah ....

| Opsi | Isi |
|---|---|
| A | 2 pasangan |
| B | 3 pasangan |
| C | 4 pasangan |
| D | 1 pasangan |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e02135463563d75f0217a1768d13b7cc63680925655c56535474f5b383cc1313`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Rani pergi ke toko alat tulis. Ia membeli 4 buku tulis dan 3 bolpoin dengan membayar Rp50.000,00. Harga satu buku tulis dan harga satu bolpoin masing-masing dinyatakan dalam ribuan rupiah berupa bilangan bulat positif, dan harga buku tulis lebih mahal daripada harga bolpoin. Banyak pasangan harga (buku tulis, bolpoin) yang mungkin adalah ....
Pilihan: A. 2 pasangan
B. 3 pasangan
C. 4 pasangan
D. 1 pasangan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `41ef8424e0d74b2e08dab0ca`

Perhatikan persamaan $2x + 3y = 18$. Pernyataan yang benar adalah ....

| Opsi | Isi |
|---|---|
| A | Jika $x$ dan $y$ bilangan bulat, semua penyelesaiannya berupa pasangan dengan $x \ge 0$ dan $y \ge 0$ |
| B | Jika $x$ dan $y$ bilangan real, himpunan penyelesaiannya tercacah |
| C | Jika $x$ dan $y$ bilangan cacah, persamaan tersebut memiliki tepat 4 penyelesaian |
| D | Pasangan $(2, \frac{14}{3})$ bukan penyelesaian jika $x$ dan $y$ bilangan real |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d0e9743886a6d77fe015efccea5060eda5ea9e47e0dbff452b80611730744592`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan persamaan $2x + 3y = 18$. Pernyataan yang benar adalah ....
Pilihan: A. Jika $x$ dan $y$ bilangan bulat, semua penyelesaiannya berupa pasangan dengan $x \ge 0$ dan $y \ge 0$
B. Jika $x$ dan $y$ bilangan real, himpunan penyelesaiannya tercacah
C. Jika $x$ dan $y$ bilangan cacah, persamaan tersebut memiliki tepat 4 penyelesaian
D. Pasangan $(2, \frac{14}{3})$ bukan penyelesaian jika $x$ dan $y$ bilangan real
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 21. Soal `8f6edb84b973d12115784ac4`

Dika diminta menentukan $a$ jika pasangan $(a, -1)$ merupakan penyelesaian dari $3x - 4y = 10$. Penyelesaiannya: Langkah 1: $3a - 4(-1) = 10$. Langkah 2: $3a - 4 = 10$. Langkah 3: $3a = 14$. Langkah 4: $a = \frac{14}{3}$. Kesalahan pertama terjadi pada langkah ... dan nilai $a$ yang benar adalah ....

| Opsi | Isi |
|---|---|
| A | langkah 2; $a = \frac{14}{3}$ |
| B | langkah 4; $a = \frac{14}{3}$ |
| C | langkah 2; $a = 2$ |
| D | langkah 3; $a = 2$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `434247da02471440000cb8858c2c2dd910ec4ba0436300cfbde28872670009d5`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Dika diminta menentukan $a$ jika pasangan $(a, -1)$ merupakan penyelesaian dari $3x - 4y = 10$. Penyelesaiannya: Langkah 1: $3a - 4(-1) = 10$. Langkah 2: $3a - 4 = 10$. Langkah 3: $3a = 14$. Langkah 4: $a = \frac{14}{3}$. Kesalahan pertama terjadi pada langkah ... dan nilai $a$ yang benar adalah ....
Pilihan: A. langkah 2; $a = \frac{14}{3}$
B. langkah 4; $a = \frac{14}{3}$
C. langkah 2; $a = 2$
D. langkah 3; $a = 2$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 22. Soal `b00ede801f2fa976756e262f`

Bu Sari membeli $x$ kg beras seharga Rp12.000,00 per kg dan $y$ kg gula seharga Rp15.000,00 per kg. Ia mendapat potongan harga Rp6.000,00 untuk seluruh belanjaannya, lalu membayar dengan uang Rp200.000,00 dan menerima kembalian Rp38.000,00. Model matematika yang tepat adalah ....

| Opsi | Isi |
|---|---|
| A | $12.000x + 15.000y = 238.000$ |
| B | $12.000x + 15.000y = 168.000$ |
| C | $12.000x + 15.000y = 156.000$ |
| D | $12.000x + 15.000y = 162.000$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1a9a587a88302e89647a22a84a41e431be84105e703e68ab03506d02503d5d81`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Bu Sari membeli $x$ kg beras seharga Rp12.000,00 per kg dan $y$ kg gula seharga Rp15.000,00 per kg. Ia mendapat potongan harga Rp6.000,00 untuk seluruh belanjaannya, lalu membayar dengan uang Rp200.000,00 dan menerima kembalian Rp38.000,00. Model matematika yang tepat adalah ....
Pilihan: A. $12.000x + 15.000y = 238.000$
B. $12.000x + 15.000y = 168.000$
C. $12.000x + 15.000y = 156.000$
D. $12.000x + 15.000y = 162.000$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 23. Soal `bfd6929467992471e0a53ec9`

Biaya sewa di rental A dinyatakan dengan $y = 12.000x + 30.000$ dan di rental B dengan $y = 15.000x + 12.000$, dengan $y$ biaya (rupiah) dan $x$ lama sewa (jam). Pernyataan yang benar adalah ....

| Opsi | Isi |
|---|---|
| A | untuk 4 jam, rental A lebih murah daripada rental B |
| B | untuk 8 jam, rental A lebih murah Rp6.000,00 daripada rental B |
| C | untuk 5 jam, rental A lebih murah Rp3.000,00 daripada rental B |
| D | untuk 6 jam, rental B lebih murah Rp18.000,00 daripada rental A |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3e5723e889aedbaa9badd777258e41220968ecc9493940a39a934bf31cddc9c3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Biaya sewa di rental A dinyatakan dengan $y = 12.000x + 30.000$ dan di rental B dengan $y = 15.000x + 12.000$, dengan $y$ biaya (rupiah) dan $x$ lama sewa (jam). Pernyataan yang benar adalah ....
Pilihan: A. untuk 4 jam, rental A lebih murah daripada rental B
B. untuk 8 jam, rental A lebih murah Rp6.000,00 daripada rental B
C. untuk 5 jam, rental A lebih murah Rp3.000,00 daripada rental B
D. untuk 6 jam, rental B lebih murah Rp18.000,00 daripada rental A
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 24. Soal `6a7c5cbe91f9d4637f8ba3af`

Pasangan berurutan $(a + 1, 2a - 3)$ merupakan penyelesaian dari persamaan $5x - 3y = 4$. Nilai $x + y$ pada pasangan tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $-26$ |
| B | $28$ |
| C | $10$ |
| D | $17$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `95a420c90f50d26d6025698c6ea23968f1c05d2bdba41d62ade4ca2298476367`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Pasangan berurutan $(a + 1, 2a - 3)$ merupakan penyelesaian dari persamaan $5x - 3y = 4$. Nilai $x + y$ pada pasangan tersebut adalah ....
Pilihan: A. $-26$
B. $28$
C. $10$
D. $17$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 25. Soal `be4e8dcfc06532ffdb860609`

Sebuah pegas meregang 2,5 cm ketika diberi beban 100 g dan 5 cm ketika diberi beban 200 g. Berat beban $y$ (gram) proporsional dengan regangan $x$ (cm). Sebuah benda ditimbang dan pegas meregang 7,5 cm lebih panjang daripada ketika dibebani 180 g. Berat benda tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | 480 g |
| B | 300 g |
| C | 660 g |
| D | 1.350 g |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e46525024ff33740433f4108feeddce21995edd72c278d1a9a284eeca807ed25`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah pegas meregang 2,5 cm ketika diberi beban 100 g dan 5 cm ketika diberi beban 200 g. Berat beban $y$ (gram) proporsional dengan regangan $x$ (cm). Sebuah benda ditimbang dan pegas meregang 7,5 cm lebih panjang daripada ketika dibebani 180 g. Berat benda tersebut adalah ....
Pilihan: A. 480 g
B. 300 g
C. 660 g
D. 1.350 g
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 26. Soal `faf4b054e1b67f13496e6912`

Soal: Tentukan himpunan penyelesaian $x + 2y = 7$ dengan $x$ dan $y$ bilangan bulat. Penyelesaian Andi: Langkah 1: $x = 7 - 2y$. Langkah 2: untuk $y = 0, 1, 2, 3$ diperoleh $x = 7, 5, 3, 1$. Langkah 3: untuk $y = 4$ diperoleh $x = -1$ sehingga tidak diambil. Langkah 4: himpunan penyelesaiannya $\{(7,0), (5,1), (3,2), (1,3)\}$. Kesalahan Andi adalah ....

| Opsi | Isi |
|---|---|
| A | hanya memakai nilai tidak negatif, padahal bilangan bulat boleh negatif |
| B | langkah 1 salah, seharusnya $x = 7 + 2y$ |
| C | langkah 2 salah, untuk $y = 1$ seharusnya $x = 6$ |
| D | pasangan seharusnya ditulis sebagai $(y, x)$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3a39151751480fba54ec71dca707f76641b0796f476cb58e5d19af5807087f2b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Soal: Tentukan himpunan penyelesaian $x + 2y = 7$ dengan $x$ dan $y$ bilangan bulat. Penyelesaian Andi: Langkah 1: $x = 7 - 2y$. Langkah 2: untuk $y = 0, 1, 2, 3$ diperoleh $x = 7, 5, 3, 1$. Langkah 3: untuk $y = 4$ diperoleh $x = -1$ sehingga tidak diambil. Langkah 4: himpunan penyelesaiannya $\{(7,0), (5,1), (3,2), (1,3)\}$. Kesalahan Andi adalah ....
Pilihan: A. hanya memakai nilai tidak negatif, padahal bilangan bulat boleh negatif
B. langkah 1 salah, seharusnya $x = 7 + 2y$
C. langkah 2 salah, untuk $y = 1$ seharusnya $x = 6$
D. pasangan seharusnya ditulis sebagai $(y, x)$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 27. Soal `9b7202a7a07a47764fb3e6d5`

Persamaan $P$: $3x + 2y = 24$ dan persamaan $Q$: $4x + 3y = 24$. Jika $x$ dan $y$ bilangan cacah, banyak penyelesaian $P$ dan $Q$ berturut-turut adalah ....

| Opsi | Isi |
|---|---|
| A | 5 dan 9 |
| B | 3 dan 1 |
| C | 5 dan 3 |
| D | 9 dan 7 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f97252bc72e6311910b0c8f98e4928f21f774c871d4dba6aa5ee7fd7f1199422`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Persamaan $P$: $3x + 2y = 24$ dan persamaan $Q$: $4x + 3y = 24$. Jika $x$ dan $y$ bilangan cacah, banyak penyelesaian $P$ dan $Q$ berturut-turut adalah ....
Pilihan: A. 5 dan 9
B. 3 dan 1
C. 5 dan 3
D. 9 dan 7
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 28. Soal `6d3ebfd8fc44c580e2f95c95`

Pasangan $(2, 3)$ merupakan penyelesaian dari persamaan $px + qy = 24$ dengan $p$ dan $q$ bilangan bulat positif serta $p > q$. Jika dipilih persamaan dengan $p + q$ sekecil mungkin, persamaan tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $3x + 6y = 24$ |
| B | $9x + 2y = 24$ |
| C | $6x + 3y = 24$ |
| D | $6x + 4y = 24$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c26366e8f638ba32e157f366bb885cde8f06faf44cbd0a8062a9cb2dc887a22f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Pasangan $(2, 3)$ merupakan penyelesaian dari persamaan $px + qy = 24$ dengan $p$ dan $q$ bilangan bulat positif serta $p > q$. Jika dipilih persamaan dengan $p + q$ sekecil mungkin, persamaan tersebut adalah ....
Pilihan: A. $3x + 6y = 24$
B. $9x + 2y = 24$
C. $6x + 3y = 24$
D. $6x + 4y = 24$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 29. Soal `78e3b6a0d86e1445c081d67e`

Persamaan $(m^2 - 16)x^2 + (m + 4)xy + 5x - 2y = 9$ dengan $m$ bilangan real dapat dinyatakan dalam bentuk $ax + by = c$ (persamaan linear dua variabel). Nilai $m$ yang memenuhi adalah ....

| Opsi | Isi |
|---|---|
| A | $4$ |
| B | $4$ atau $-4$ |
| C | $16$ |
| D | $-4$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `bf6d40e9b0093caf68729adb8de22c927dd9cae0c9e7d0ccb4533143a1ae272e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Persamaan $(m^2 - 16)x^2 + (m + 4)xy + 5x - 2y = 9$ dengan $m$ bilangan real dapat dinyatakan dalam bentuk $ax + by = c$ (persamaan linear dua variabel). Nilai $m$ yang memenuhi adalah ....
Pilihan: A. $4$
B. $4$ atau $-4$
C. $16$
D. $-4$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 30. Soal `c75b70d8877eaadf0e1f88e3`

Persamaan $\frac{2x - 1}{3} - \frac{y + 2}{4} = 1$ dinyatakan dalam bentuk $ax + by = c$ dengan $a$, $b$, $c$ bilangan bulat tanpa faktor persekutuan selain 1 dan $a$ positif. Nilai $a + b + c$ adalah ....

| Opsi | Isi |
|---|---|
| A | $27$ |
| B | $33$ |
| C | $16$ |
| D | $15$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `35cf14df57eae537efd55434db7adde295118c453df66c4f7a65cbbd3180eb46`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Persamaan $\frac{2x - 1}{3} - \frac{y + 2}{4} = 1$ dinyatakan dalam bentuk $ax + by = c$ dengan $a$, $b$, $c$ bilangan bulat tanpa faktor persekutuan selain 1 dan $a$ positif. Nilai $a + b + c$ adalah ....
Pilihan: A. $27$
B. $33$
C. $16$
D. $15$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 31. Soal `444c2b78db198274d5f3ad9e`

Himpunan penyelesaian dari persamaan $4x + y = 12$ dengan $x$ dan $y$ bilangan cacah adalah ....

| Opsi | Isi |
|---|---|
| A | $\{(0, 12), (1, 8), (2, 4), (3, 0)\}$ |
| B | $\{(12, 0), (8, 1), (4, 2), (0, 3)\}$ |
| C | $\{(0, 12), (1, 8), (2, 4), (3, 0), (4, -4)\}$ |
| D | $\{(1, 8), (2, 4)\}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `573fc763ad8478c3353e7c6e01d7d0d2c7857310f391945a9cb62460dc9d9cca`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Himpunan penyelesaian dari persamaan $4x + y = 12$ dengan $x$ dan $y$ bilangan cacah adalah ....
Pilihan: A. $\{(0, 12), (1, 8), (2, 4), (3, 0)\}$
B. $\{(12, 0), (8, 1), (4, 2), (0, 3)\}$
C. $\{(0, 12), (1, 8), (2, 4), (3, 0), (4, -4)\}$
D. $\{(1, 8), (2, 4)\}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 32. Soal `c9dae4735d07d8ffd74eae15`

Tissa pergi ke toko alat tulis. Ia membeli 5 buku tulis dan 2 bolpoin dengan membayar Rp26.000,00. Jika harga 1 buku tulis Rp4.000,00, harga 1 bolpoin adalah ....

| Opsi | Isi |
|---|---|
| A | Rp6.000,00 |
| B | Rp11.000,00 |
| C | Rp13.000,00 |
| D | Rp3.000,00 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3f57d30bb4ae7a3ab3305b55494133a4c9fc83f2af612d315b59167981fd82a0`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Tissa pergi ke toko alat tulis. Ia membeli 5 buku tulis dan 2 bolpoin dengan membayar Rp26.000,00. Jika harga 1 buku tulis Rp4.000,00, harga 1 bolpoin adalah ....
Pilihan: A. Rp6.000,00
B. Rp11.000,00
C. Rp13.000,00
D. Rp3.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 33. Soal `c6bacf866132e812f3c58321`

Harga 4 ekor sapi dan 3 ekor kambing Rp94.000.000,00. Jika harga seekor kambing Rp6.000.000,00, harga seekor sapi adalah ....

| Opsi | Isi |
|---|---|
| A | Rp19.000.000,00 |
| B | Rp23.500.000,00 |
| C | Rp22.000.000,00 |
| D | Rp76.000.000,00 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `474305aaa2336ca3a817dece1919c05246c9aa45f86f7f66f1932cc637c7b179`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Harga 4 ekor sapi dan 3 ekor kambing Rp94.000.000,00. Jika harga seekor kambing Rp6.000.000,00, harga seekor sapi adalah ....
Pilihan: A. Rp19.000.000,00
B. Rp23.500.000,00
C. Rp22.000.000,00
D. Rp76.000.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 34. Soal `c319a07be1cd3b6e42226854`

Sebuah taksi menetapkan tarif Rp8.000,00 per km ditambah biaya buka pintu Rp7.000,00. Jika $y$ adalah total biaya dan $x$ adalah jarak tempuh dalam km, biaya perjalanan sejauh 12 km adalah ....

| Opsi | Isi |
|---|---|
| A | Rp180.000,00 |
| B | Rp96.000,00 |
| C | Rp103.000,00 |
| D | Rp89.000,00 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `424d3409b55a6c74de752081a65b9fc0cc6ab172bd32c037b75509d04c064d17`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah taksi menetapkan tarif Rp8.000,00 per km ditambah biaya buka pintu Rp7.000,00. Jika $y$ adalah total biaya dan $x$ adalah jarak tempuh dalam km, biaya perjalanan sejauh 12 km adalah ....
Pilihan: A. Rp180.000,00
B. Rp96.000,00
C. Rp103.000,00
D. Rp89.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 35. Soal `a884207209e1cd4a71c7cfe4`

Harga tiket masuk sebuah wahana Rp25.000,00. Jika $y$ menyatakan pendapatan dari hasil penjualan tiket dan $x$ menyatakan banyak tiket terjual, banyak tiket yang terjual saat pendapatan Rp1.350.000,00 adalah ....

| Opsi | Isi |
|---|---|
| A | 1.325 tiket |
| B | 33.750.000 tiket |
| C | 54 tiket |
| D | 540 tiket |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `72c81bb671ae8272b5acc4050491d76fd937ae81d2cd7c25b94aeb1448be0643`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Harga tiket masuk sebuah wahana Rp25.000,00. Jika $y$ menyatakan pendapatan dari hasil penjualan tiket dan $x$ menyatakan banyak tiket terjual, banyak tiket yang terjual saat pendapatan Rp1.350.000,00 adalah ....
Pilihan: A. 1.325 tiket
B. 33.750.000 tiket
C. 54 tiket
D. 540 tiket
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 36. Soal `9ef9b19736e01721f50af1a0`

Keliling sebuah segitiga sama kaki adalah 44 cm. Jika panjang kaki 4 cm lebih panjang daripada panjang alas, panjang alas segitiga tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | 20 cm |
| B | 16 cm |
| C | 36 cm |
| D | 12 cm |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d5d715cdc8df024265ef18a9f97ccc48a92bcce99eb899f3373dda1f2081845b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Keliling sebuah segitiga sama kaki adalah 44 cm. Jika panjang kaki 4 cm lebih panjang daripada panjang alas, panjang alas segitiga tersebut adalah ....
Pilihan: A. 20 cm
B. 16 cm
C. 36 cm
D. 12 cm
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 37. Soal `40a6068697c829ae25830d09`

Pak Rudi memiliki uang Rp20.000,00 yang terdiri dari lembaran Rp2.000,00 sebanyak $a$ lembar dan lembaran Rp5.000,00 sebanyak $b$ lembar, dengan $a$ dan $b$ bilangan cacah (salah satu jenis lembaran boleh tidak ada). Banyak kombinasi $(a, b)$ yang mungkin adalah ....

| Opsi | Isi |
|---|---|
| A | 2 kombinasi |
| B | 1 kombinasi |
| C | 3 kombinasi |
| D | 5 kombinasi |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `48c35aeb8a3646b3e2f59563c6b411a19f18e7cc249b3b72b5a06c34f24163ec`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Pak Rudi memiliki uang Rp20.000,00 yang terdiri dari lembaran Rp2.000,00 sebanyak $a$ lembar dan lembaran Rp5.000,00 sebanyak $b$ lembar, dengan $a$ dan $b$ bilangan cacah (salah satu jenis lembaran boleh tidak ada). Banyak kombinasi $(a, b)$ yang mungkin adalah ....
Pilihan: A. 2 kombinasi
B. 1 kombinasi
C. 3 kombinasi
D. 5 kombinasi
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 38. Soal `06dbf4de70429eb310eabc2c`

Manakah persamaan berikut yang setelah disederhanakan merupakan persamaan linear dua variabel?

| Opsi | Isi |
|---|---|
| A | $2(x + y) = 3x - 5$ |
| B | $3x - 7 = 2x + 1$ |
| C | $x(y + 1) = 6$ |
| D | $x^2 + y = 5$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d37fb29c4791abecdbadf7721cded8dd751cf95df855eac38000c7f3c5b107c0`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Manakah persamaan berikut yang setelah disederhanakan merupakan persamaan linear dua variabel?
Pilihan: A. $2(x + y) = 3x - 5$
B. $3x - 7 = 2x + 1$
C. $x(y + 1) = 6$
D. $x^2 + y = 5$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 39. Soal `7401fc315e0c1b11031b4b58`

Persamaan $3x = 8 - 2y$ dinyatakan dalam bentuk $ax + by = c$. Nilai $a + b + c$ adalah ....

| Opsi | Isi |
|---|---|
| A | $5$ |
| B | $-3$ |
| C | $13$ |
| D | $9$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `eef699b4c4254c721a67278507f8326a3c59c5ce8699a6bd5a55f37ecf688a7b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Persamaan $3x = 8 - 2y$ dinyatakan dalam bentuk $ax + by = c$. Nilai $a + b + c$ adalah ....
Pilihan: A. $5$
B. $-3$
C. $13$
D. $9$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 40. Soal `117e222bb56a23599976ca49`

Banyak pasangan bilangan cacah $(x, y)$ yang memenuhi persamaan $x + 2y = 9$ dengan syarat $x > y$ adalah ....

| Opsi | Isi |
|---|---|
| A | 3 pasangan |
| B | 2 pasangan |
| C | 4 pasangan |
| D | 5 pasangan |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `92538f6a7e1c511961bc80ea447825c09e7b3c9ff13f1f0e5ff65b16c22c71bd`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Banyak pasangan bilangan cacah $(x, y)$ yang memenuhi persamaan $x + 2y = 9$ dengan syarat $x > y$ adalah ....
Pilihan: A. 3 pasangan
B. 2 pasangan
C. 4 pasangan
D. 5 pasangan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 41. Soal `7ac39a7dd2a698ce5063c9ba`

Dina membeli $x$ pensil seharga Rp3.000,00 per buah dan $y$ buku seharga Rp5.000,00 per buah. Ia membayar dengan uang Rp50.000,00 dan menerima kembalian Rp7.000,00. Model matematika dari permasalahan tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $3.000x + 5.000y = 50.000$ |
| B | $3.000x + 5.000y = 57.000$ |
| C | $5.000x + 3.000y = 43.000$ |
| D | $3.000x + 5.000y = 43.000$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `25acc6174a6efd18479ec7e022469664d4887eb79692499d2803cb408f50ac7d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Dina membeli $x$ pensil seharga Rp3.000,00 per buah dan $y$ buku seharga Rp5.000,00 per buah. Ia membayar dengan uang Rp50.000,00 dan menerima kembalian Rp7.000,00. Model matematika dari permasalahan tersebut adalah ....
Pilihan: A. $3.000x + 5.000y = 50.000$
B. $3.000x + 5.000y = 57.000$
C. $5.000x + 3.000y = 43.000$
D. $3.000x + 5.000y = 43.000$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 42. Soal `9b534669f20e152254856228`

Pasangan berurutan $(a, 3)$ dan $(4, b)$ merupakan penyelesaian dari persamaan $2x + 3y = 17$. Nilai $a + b$ adalah ....

| Opsi | Isi |
|---|---|
| A | $10$ |
| B | $7$ |
| C | $11$ |
| D | $13$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `67a97a2fb06de33f73e4b1dc0184958345e073e4e4174ba9b4359f50a36ed018`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Pasangan berurutan $(a, 3)$ dan $(4, b)$ merupakan penyelesaian dari persamaan $2x + 3y = 17$. Nilai $a + b$ adalah ....
Pilihan: A. $10$
B. $7$
C. $11$
D. $13$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 43. Soal `afad2e9074857a263ba77a37`

Himpunan penyelesaian dari persamaan $3x + 2y = 12$ dengan $x$ dan $y$ bilangan bulat. Pasangan berikut yang BUKAN anggota himpunan tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $(6, -3)$ |
| B | $(1, \frac{9}{2})$ |
| C | $(-2, 9)$ |
| D | $(2, 3)$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `99e5ed82d1e54c1ba4c3fc4c05bfa4cd3d2a236427c6ca99a01318077bbcd2fd`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Himpunan penyelesaian dari persamaan $3x + 2y = 12$ dengan $x$ dan $y$ bilangan bulat. Pasangan berikut yang BUKAN anggota himpunan tersebut adalah ....
Pilihan: A. $(6, -3)$
B. $(1, \frac{9}{2})$
C. $(-2, 9)$
D. $(2, 3)$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 44. Soal `b63ebd4b748b1d6abd098272`

Keliling sebuah persegi panjang adalah 40 cm. Jika panjangnya 14 cm, luas persegi panjang tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | 364 cm$^2$ |
| B | 84 cm$^2$ |
| C | 196 cm$^2$ |
| D | 168 cm$^2$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a2d3f4dd66a3d6dd267993febcce006dde870184628e964fd9e0e590ad7699ec`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Keliling sebuah persegi panjang adalah 40 cm. Jika panjangnya 14 cm, luas persegi panjang tersebut adalah ....
Pilihan: A. 364 cm$^2$
B. 84 cm$^2$
C. 196 cm$^2$
D. 168 cm$^2$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 45. Soal `dbe6f7d7b6edb2f2d50cdc6e`

Biaya sewa lapangan futsal dinyatakan dengan $y = 2.500x + 5.000$, dengan $y$ biaya (rupiah) dan $x$ lama sewa (jam). Pernyataan yang benar adalah ....

| Opsi | Isi |
|---|---|
| A | setiap tambahan 1 jam sewa, biaya bertambah Rp7.500,00 |
| B | setiap tambahan 1 jam sewa, biaya bertambah Rp2.500,00 |
| C | biaya sewa untuk 2 jam adalah Rp7.500,00 |
| D | biaya sebelum disewa ($x = 0$) adalah Rp0,00 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e964dbaf1d48e568b00e5b624a02a105cf129061383a9dd1e89d9f40fb9e2a17`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Biaya sewa lapangan futsal dinyatakan dengan $y = 2.500x + 5.000$, dengan $y$ biaya (rupiah) dan $x$ lama sewa (jam). Pernyataan yang benar adalah ....
Pilihan: A. setiap tambahan 1 jam sewa, biaya bertambah Rp7.500,00
B. setiap tambahan 1 jam sewa, biaya bertambah Rp2.500,00
C. biaya sewa untuk 2 jam adalah Rp7.500,00
D. biaya sebelum disewa ($x = 0$) adalah Rp0,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 46. Soal `e2bc608a35f5591816dbc749`

Dino membeli satu mangkuk bakso dan tiga gelas es teh dengan harga seluruhnya Rp19.500,00. Di warung yang sama, Sari membeli dua mangkuk bakso dan lima gelas es teh dengan harga seluruhnya Rp35.000,00.<br><br>Jika harga satu mangkuk bakso adalah $b$ dan harga satu gelas es teh adalah $t$, sistem persamaan linear dua variabel yang sesuai adalah ....

| Opsi | Isi |
|---|---|
| A | $b + 3t = 19.500$ dan $5b + 2t = 35.000$ |
| B | $b + 3t = 35.000$ dan $2b + 5t = 19.500$ |
| C | $b + 3t = 19.500$ dan $2b + 5t = 35.000$ |
| D | $3b + t = 19.500$ dan $5b + 2t = 35.000$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `586623adc72d8a46ec09a37c8fe2f57f7918384fa1cc377a93e56c7a6306f3a4`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Dino membeli satu mangkuk bakso dan tiga gelas es teh dengan harga seluruhnya Rp19.500,00. Di warung yang sama, Sari membeli dua mangkuk bakso dan lima gelas es teh dengan harga seluruhnya Rp35.000,00.

Jika harga satu mangkuk bakso adalah $b$ dan harga satu gelas es teh adalah $t$, sistem persamaan linear dua variabel yang sesuai adalah ....
Pilihan: A. $b + 3t = 19.500$ dan $5b + 2t = 35.000$
B. $b + 3t = 35.000$ dan $2b + 5t = 19.500$
C. $b + 3t = 19.500$ dan $2b + 5t = 35.000$
D. $3b + t = 19.500$ dan $5b + 2t = 35.000$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 47. Soal `bb18908569d7e1ff8519ce77`

Wayan membeli satu kue basung dan dua kue mendut dengan harga seluruhnya Rp10.000,00. Di toko yang sama, Aisyah membeli satu kue basung dan empat kue mendut dengan harga seluruhnya Rp16.000,00.<br><br>Berapa harga satu kue mendut?

| Opsi | Isi |
|---|---|
| A | Rp3.000,00 |
| B | Rp5.000,00 |
| C | Rp4.000,00 |
| D | Rp6.000,00 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3e363a41d995970361f993d654d14f0e02cf0f1e5f8bd9110f2638c2684ddcce`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Wayan membeli satu kue basung dan dua kue mendut dengan harga seluruhnya Rp10.000,00. Di toko yang sama, Aisyah membeli satu kue basung dan empat kue mendut dengan harga seluruhnya Rp16.000,00.

Berapa harga satu kue mendut?
Pilihan: A. Rp3.000,00
B. Rp5.000,00
C. Rp4.000,00
D. Rp6.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 48. Soal `e4f2c3646f7940f41bee0c4f`

Sebuah toko mainan menjual 25 boneka. Harga boneka kecil Rp20.000,00 dan harga boneka besar Rp45.000,00. Uang yang diperoleh toko dari penjualan tersebut Rp700.000,00.<br><br>Jika banyak boneka kecil adalah $x$ dan banyak boneka besar adalah $y$, sistem persamaan linear dua variabel yang sesuai adalah ....

| Opsi | Isi |
|---|---|
| A | $x + y = 700.000$ dan $20.000x + 45.000y = 25$ |
| B | $x + y = 25$ dan $45.000x + 20.000y = 700.000$ |
| C | $x + y = 25$ dan $20.000x + 45.000y = 700.000$ |
| D | $x + y = 25$ dan $65.000x = 700.000$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9b3f1fdb5645e9f53bb444d6ada38a70443cb32e839596f590c37b0bbfdabfb5`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah toko mainan menjual 25 boneka. Harga boneka kecil Rp20.000,00 dan harga boneka besar Rp45.000,00. Uang yang diperoleh toko dari penjualan tersebut Rp700.000,00.

Jika banyak boneka kecil adalah $x$ dan banyak boneka besar adalah $y$, sistem persamaan linear dua variabel yang sesuai adalah ....
Pilihan: A. $x + y = 700.000$ dan $20.000x + 45.000y = 25$
B. $x + y = 25$ dan $45.000x + 20.000y = 700.000$
C. $x + y = 25$ dan $20.000x + 45.000y = 700.000$
D. $x + y = 25$ dan $65.000x = 700.000$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 49. Soal `412b9fb52d326b97991b4d80`

Seorang petani membuat kolam ikan berbentuk persegi panjang. Lebar kolam 3 meter lebih pendek dari panjangnya. Keliling kolam tersebut adalah 34 meter. Dengan $p$ panjang dan $l$ lebar, diperoleh sistem $l = p - 3$ dan $2p + 2l = 34$.<br><br>Jika $l = p - 3$ disubstitusikan ke persamaan $2p + 2l = 34$, bentuk yang diperoleh adalah ....

| Opsi | Isi |
|---|---|
| A | $2p + 2(p + 3) = 34$ |
| B | $2p + (p - 3) = 34$ |
| C | $2p + 2p - 3 = 34$ |
| D | $2p + 2(p - 3) = 34$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f0061a285cc116b339794e4b810f6dd205c19c547086c1a739ddfe8b151f5cd4`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Seorang petani membuat kolam ikan berbentuk persegi panjang. Lebar kolam 3 meter lebih pendek dari panjangnya. Keliling kolam tersebut adalah 34 meter. Dengan $p$ panjang dan $l$ lebar, diperoleh sistem $l = p - 3$ dan $2p + 2l = 34$.

Jika $l = p - 3$ disubstitusikan ke persamaan $2p + 2l = 34$, bentuk yang diperoleh adalah ....
Pilihan: A. $2p + 2(p + 3) = 34$
B. $2p + (p - 3) = 34$
C. $2p + 2p - 3 = 34$
D. $2p + 2(p - 3) = 34$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 50. Soal `8120fe13631a4c636e5f9a26`

Sebuah lapangan berbentuk persegi panjang. Lebar lapangan tersebut 6 meter lebih pendek dari panjangnya. Keliling lapangan itu adalah 76 meter.<br><br>Panjang lapangan tersebut adalah ... meter.

| Opsi | Isi |
|---|---|
| A | 19 |
| B | 32 |
| C | 16 |
| D | 22 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `691e9617b16f71eb5d22797784f9a0bcec5b8406e509ed3aa20a6a05eb6cdecb`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah lapangan berbentuk persegi panjang. Lebar lapangan tersebut 6 meter lebih pendek dari panjangnya. Keliling lapangan itu adalah 76 meter.

Panjang lapangan tersebut adalah ... meter.
Pilihan: A. 19
B. 32
C. 16
D. 22
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 51. Soal `a1d5f1d2e9c9548735927491`

Rina membeli 2 topi dan 1 tas dengan total harga Rp70.000,00. Doni membeli 3 topi dan 4 tas dengan total harga Rp205.000,00.<br><br>Jika harga 1 topi dinyatakan dengan $t$ dan harga 1 tas dinyatakan dengan $s$, sistem persamaan linear dua variabel yang sesuai adalah ....

| Opsi | Isi |
|---|---|
| A | $t + 2s = 70.000$ dan $4t + 3s = 205.000$ |
| B | $2t + s = 70.000$ dan $3t + 4s = 205.000$ |
| C | $2t + s = 205.000$ dan $3t + 4s = 70.000$ |
| D | $2t + s = 70.000$ dan $5t + 5s = 275.000$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2adfd26bf15319c66a10f41c5bdbf60bee44b2aa9a1998e836377ace7b96ebd3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Rina membeli 2 topi dan 1 tas dengan total harga Rp70.000,00. Doni membeli 3 topi dan 4 tas dengan total harga Rp205.000,00.

Jika harga 1 topi dinyatakan dengan $t$ dan harga 1 tas dinyatakan dengan $s$, sistem persamaan linear dua variabel yang sesuai adalah ....
Pilihan: A. $t + 2s = 70.000$ dan $4t + 3s = 205.000$
B. $2t + s = 70.000$ dan $3t + 4s = 205.000$
C. $2t + s = 205.000$ dan $3t + 4s = 70.000$
D. $2t + s = 70.000$ dan $5t + 5s = 275.000$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 52. Soal `ecf31862552cb15b9f1a53d2`

Diberikan sistem persamaan linear $x + y = 14$ dan $2x + 3y = 38$, dengan $x$ dan $y$ bilangan real.<br><br>Nilai $y$ yang memenuhi sistem tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $4$ |
| B | $10$ |
| C | $24$ |
| D | $12$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2106f7429fd0d0d6de2297b73a42b114c847ff979aed7eab8ff7028ad4363a1b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Diberikan sistem persamaan linear $x + y = 14$ dan $2x + 3y = 38$, dengan $x$ dan $y$ bilangan real.

Nilai $y$ yang memenuhi sistem tersebut adalah ....
Pilihan: A. $4$
B. $10$
C. $24$
D. $12$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 53. Soal `1d49b4b1fb49e45267f25ec2`

Pasangan $(x, y)$ disebut penyelesaian suatu sistem persamaan linear dua variabel jika ....

| Opsi | Isi |
|---|---|
| A | nilai $x$ dan $y$ hanya memenuhi salah satu persamaan |
| B | nilai $x$ dan $y$ memenuhi kedua persamaan dalam sistem itu |
| C | nilai $x$ dan $y$ sama besar |
| D | nilai $x$ dan $y$ keduanya bilangan bulat positif |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5f93d236255e22da79262dcd8dbbaccf0e3b896d5df870a99aa66be5ab1e81e3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Pasangan $(x, y)$ disebut penyelesaian suatu sistem persamaan linear dua variabel jika ....
Pilihan: A. nilai $x$ dan $y$ hanya memenuhi salah satu persamaan
B. nilai $x$ dan $y$ memenuhi kedua persamaan dalam sistem itu
C. nilai $x$ dan $y$ sama besar
D. nilai $x$ dan $y$ keduanya bilangan bulat positif
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 54. Soal `2c6b8ef079371f570caaff3b`

Diberikan sistem persamaan linear $5x + y = 9$ dan $2x - 3y = 7$.<br><br>Pasangan berikut yang merupakan penyelesaian sistem tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $(2, -1)$ |
| B | $(-1, 2)$ |
| C | $(0, 9)$ |
| D | $(5, 1)$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `499178a96fe2dce4bb15968036b938b51430b24ac6584bf387d9524f7b8e4543`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Diberikan sistem persamaan linear $5x + y = 9$ dan $2x - 3y = 7$.

Pasangan berikut yang merupakan penyelesaian sistem tersebut adalah ....
Pilihan: A. $(2, -1)$
B. $(-1, 2)$
C. $(0, 9)$
D. $(5, 1)$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 55. Soal `70bafed668328e4a069cbd4e`

Diberikan sistem persamaan linear $x + y = 5$ dan $x + y = 8$.<br><br>Banyak penyelesaian sistem tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | tidak memiliki penyelesaian |
| B | tepat satu penyelesaian |
| C | tepat dua penyelesaian |
| D | tak hingga penyelesaian |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `84f0bec05864a18b3cc79ca33f06d4a3fbc76d08f615ab09a7ea1eaeadfd1947`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Diberikan sistem persamaan linear $x + y = 5$ dan $x + y = 8$.

Banyak penyelesaian sistem tersebut adalah ....
Pilihan: A. tidak memiliki penyelesaian
B. tepat satu penyelesaian
C. tepat dua penyelesaian
D. tak hingga penyelesaian
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 56. Soal `2be5cfca2e06fd766a9d24fe`

Diberikan sistem persamaan linear $2x + y = 6$ dan $4x + 2y = 12$.<br><br>Banyak penyelesaian sistem tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | tepat satu penyelesaian |
| B | tidak memiliki penyelesaian |
| C | tak hingga penyelesaian |
| D | tepat dua penyelesaian |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `61a0bc50174ab673ca90886c402b441e0eb445c9affe51ccf5e95889fc2b7e9d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Diberikan sistem persamaan linear $2x + y = 6$ dan $4x + 2y = 12$.

Banyak penyelesaian sistem tersebut adalah ....
Pilihan: A. tepat satu penyelesaian
B. tidak memiliki penyelesaian
C. tak hingga penyelesaian
D. tepat dua penyelesaian
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 57. Soal `26372f291ba9e6d93304999a`

Manakah yang merupakan sistem persamaan linear dua variabel?

| Opsi | Isi |
|---|---|
| A | $x^2 + y = 4$ dan $x - y = 1$ |
| B | $xy + y = 4$ dan $x - y = 1$ |
| C | $\frac{1}{x} + y = 4$ dan $x - y = 1$ |
| D | $2x + 3y = 7$ dan $x - y = 1$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2c84940b3fa554a7854f61c2d189d3c5a37b77678030f4602bcf5cc3967cd205`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Manakah yang merupakan sistem persamaan linear dua variabel?
Pilihan: A. $x^2 + y = 4$ dan $x - y = 1$
B. $xy + y = 4$ dan $x - y = 1$
C. $\frac{1}{x} + y = 4$ dan $x - y = 1$
D. $2x + 3y = 7$ dan $x - y = 1$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 58. Soal `e1fb7911356dbe4c39422f1b`

Ide utama metode eliminasi dalam menyelesaikan sistem persamaan linear dua variabel adalah ....

| Opsi | Isi |
|---|---|
| A | menebak pasangan nilai sampai memenuhi kedua persamaan |
| B | menghilangkan salah satu variabel agar variabel lainnya dapat ditentukan |
| C | mengganti satu variabel dengan bentuk variabel lain pada persamaan lainnya |
| D | menggambar kedua garis dan mencari titik potongnya |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1a1585561ead0e262c667ec5c15978f97afae832efbb9b02659fe237e68cb86c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Ide utama metode eliminasi dalam menyelesaikan sistem persamaan linear dua variabel adalah ....
Pilihan: A. menebak pasangan nilai sampai memenuhi kedua persamaan
B. menghilangkan salah satu variabel agar variabel lainnya dapat ditentukan
C. mengganti satu variabel dengan bentuk variabel lain pada persamaan lainnya
D. menggambar kedua garis dan mencari titik potongnya
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 59. Soal `38394e82179dea8100d2a65e`

Diberikan sistem persamaan linear $2x + y = 11$ dan $x + y = 7$.<br><br>Dengan metode eliminasi, nilai $x$ adalah ....

| Opsi | Isi |
|---|---|
| A | $18$ |
| B | $-4$ |
| C | $3$ |
| D | $4$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5ca199a7a2d818f24314c17c17f20dc88e198101dc6b6aacf125d67cc19909aa`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Diberikan sistem persamaan linear $2x + y = 11$ dan $x + y = 7$.

Dengan metode eliminasi, nilai $x$ adalah ....
Pilihan: A. $18$
B. $-4$
C. $3$
D. $4$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 60. Soal `23338b798950330091b01ea0`

Diberikan sistem persamaan linear $x = y + 3$ dan $x + 2y = 12$.<br><br>Dengan metode substitusi, nilai $y$ adalah ....

| Opsi | Isi |
|---|---|
| A | $3$ |
| B | $4$ |
| C | $5$ |
| D | $6$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e1ae66181cd2eb7cf8a00e32d88d0fca94988f534b475c708c2f43786401b852`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Diberikan sistem persamaan linear $x = y + 3$ dan $x + 2y = 12$.

Dengan metode substitusi, nilai $y$ adalah ....
Pilihan: A. $3$
B. $4$
C. $5$
D. $6$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 61. Soal `8e07af8eab26fcabf885f274`

Suatu toko alat lukis menjual 45 kuas lukis. Harga kuas lukis jenis I Rp30.000,00 dan harga kuas lukis jenis II Rp18.000,00. Semua kuas terjual dan toko mencatat uang yang didapat Rp1.000.000,00.<br><br>Penilaian yang tepat terhadap catatan penjualan toko tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | jenis I terjual 15 kuas dan jenis II terjual 30 kuas, hasil pembulatan |
| B | jenis I terjual 21 kuas dan jenis II terjual 24 kuas, dari pembagian |
| C | tidak ada banyak kuas cacah yang sesuai, sehingga catatan itu pasti keliru |
| D | jenis I terjual 16 kuas dan jenis II terjual 29 kuas, hasil pembulatan |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6ca05b1dda2cc88fee4d12b030edd1e3be2ca603c658ebc2f5b90db1d81258d4`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Suatu toko alat lukis menjual 45 kuas lukis. Harga kuas lukis jenis I Rp30.000,00 dan harga kuas lukis jenis II Rp18.000,00. Semua kuas terjual dan toko mencatat uang yang didapat Rp1.000.000,00.

Penilaian yang tepat terhadap catatan penjualan toko tersebut adalah ....
Pilihan: A. jenis I terjual 15 kuas dan jenis II terjual 30 kuas, hasil pembulatan
B. jenis I terjual 21 kuas dan jenis II terjual 24 kuas, dari pembagian
C. tidak ada banyak kuas cacah yang sesuai, sehingga catatan itu pasti keliru
D. jenis I terjual 16 kuas dan jenis II terjual 29 kuas, hasil pembulatan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 62. Soal `13d5afe505d2f9040c6a1a6c`

Bimo datang ke toko alat tulis untuk membeli pulpen dan buku. Ia membeli dua pulpen dan tiga buku dengan harga seluruhnya Rp23.500,00. Di toko yang sama, Cika membeli tiga pulpen dan dua buku dengan harga seluruhnya Rp21.500,00. Toko menawarkan Paket X berisi 4 pulpen dan 1 buku, serta Paket Y berisi 1 pulpen dan 4 buku.<br><br>Pernyataan yang benar tentang harga kedua paket tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | Paket Y lebih murah Rp6.000,00 daripada Paket X |
| B | Paket X lebih murah Rp2.000,00 daripada Paket Y |
| C | kedua paket sama harganya karena sama-sama berisi 5 barang |
| D | Paket X lebih murah Rp6.000,00 daripada Paket Y |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8881d9cade5ec024598a969b1ac4face785daaa6f2f0e6e1468b4b3522cc4a4d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Bimo datang ke toko alat tulis untuk membeli pulpen dan buku. Ia membeli dua pulpen dan tiga buku dengan harga seluruhnya Rp23.500,00. Di toko yang sama, Cika membeli tiga pulpen dan dua buku dengan harga seluruhnya Rp21.500,00. Toko menawarkan Paket X berisi 4 pulpen dan 1 buku, serta Paket Y berisi 1 pulpen dan 4 buku.

Pernyataan yang benar tentang harga kedua paket tersebut adalah ....
Pilihan: A. Paket Y lebih murah Rp6.000,00 daripada Paket X
B. Paket X lebih murah Rp2.000,00 daripada Paket Y
C. kedua paket sama harganya karena sama-sama berisi 5 barang
D. Paket X lebih murah Rp6.000,00 daripada Paket Y
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 63. Soal `d076908879b9d1dfc1b4776e`

Diberikan sistem persamaan linear $2x + 3y = 6$ dan $4x + 6y = c$ dengan $c$ bilangan real.<br><br>Pernyataan yang benar tentang banyak penyelesaian sistem tersebut untuk berbagai nilai $c$ adalah ....

| Opsi | Isi |
|---|---|
| A | tepat satu jika $c \neq 12$ dan tak hingga jika $c = 12$ |
| B | tepat satu untuk setiap nilai $c$ real |
| C | tak hingga jika $c = 12$ dan tidak ada jika $c \neq 12$ |
| D | tidak ada jika $c = 12$ dan tak hingga jika $c \neq 12$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3b83ca35dd42b72f85c53c20426a0cee34d2a2f2512826591a101328ecdcd350`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Diberikan sistem persamaan linear $2x + 3y = 6$ dan $4x + 6y = c$ dengan $c$ bilangan real.

Pernyataan yang benar tentang banyak penyelesaian sistem tersebut untuk berbagai nilai $c$ adalah ....
Pilihan: A. tepat satu jika $c \neq 12$ dan tak hingga jika $c = 12$
B. tepat satu untuk setiap nilai $c$ real
C. tak hingga jika $c = 12$ dan tidak ada jika $c \neq 12$
D. tidak ada jika $c = 12$ dan tak hingga jika $c \neq 12$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 64. Soal `a38791526ce2118065483a79`

Diberikan sistem persamaan linear $mx + 4y = 6$ dan $x + my = 3$ dengan $m$ bilangan real.<br><br>Agar sistem tersebut tidak memiliki penyelesaian, nilai $m$ adalah ....

| Opsi | Isi |
|---|---|
| A | $2$ |
| B | $-2$ |
| C | $0$ |
| D | $4$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f41596ebd38d7ad853ad876a4858f8b14790e1b09a985aeb8bf68aaf5c350bdd`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Diberikan sistem persamaan linear $mx + 4y = 6$ dan $x + my = 3$ dengan $m$ bilangan real.

Agar sistem tersebut tidak memiliki penyelesaian, nilai $m$ adalah ....
Pilihan: A. $2$
B. $-2$
C. $0$
D. $4$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 65. Soal `ade2f02ee1a0b3811ed4e9c8`

Dito menyelesaikan sistem $3x + 2y = 12$ dan $2x - 5y = -11$ dengan eliminasi. Persamaan I dikalikan 5 menjadi $15x + 10y = 60$. Persamaan II dikalikan 2 menjadi $4x - 10y = -11$. Keduanya dijumlahkan sehingga $19x = 49$ dan $x = \frac{49}{19}$.<br><br>Pernyataan yang benar tentang pekerjaan Dito adalah ....

| Opsi | Isi |
|---|---|
| A | ruas kanan persamaan II belum ikut dikalikan 2; penyelesaian yang benar $(3, 2)$ |
| B | persamaan I seharusnya dikalikan 2, bukan 5; penyelesaian yang benar $(2, 3)$ |
| C | ruas kanan persamaan II belum ikut dikalikan 2; penyelesaian yang benar $(2, 3)$ |
| D | kedua persamaan seharusnya dikurangkan, bukan dijumlahkan; penyelesaian yang benar $(2, 3)$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7b41c41d5e495bd2dc8290f25df26a01230927d281204cdf4a46f996543fe77f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Dito menyelesaikan sistem $3x + 2y = 12$ dan $2x - 5y = -11$ dengan eliminasi. Persamaan I dikalikan 5 menjadi $15x + 10y = 60$. Persamaan II dikalikan 2 menjadi $4x - 10y = -11$. Keduanya dijumlahkan sehingga $19x = 49$ dan $x = \frac{49}{19}$.

Pernyataan yang benar tentang pekerjaan Dito adalah ....
Pilihan: A. ruas kanan persamaan II belum ikut dikalikan 2; penyelesaian yang benar $(3, 2)$
B. persamaan I seharusnya dikalikan 2, bukan 5; penyelesaian yang benar $(2, 3)$
C. ruas kanan persamaan II belum ikut dikalikan 2; penyelesaian yang benar $(2, 3)$
D. kedua persamaan seharusnya dikurangkan, bukan dijumlahkan; penyelesaian yang benar $(2, 3)$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 66. Soal `0bdf2f2af5b5091c36651b92`

Jumlah umur Pak Anton dan putranya sekarang 50 tahun. Lima tahun yang lalu, umur Pak Anton 7 kali umur putranya.<br><br>Umur Pak Anton tepat dua kali umur putranya ... lagi.

| Opsi | Isi |
|---|---|
| A | 40 tahun |
| B | 30 tahun |
| C | 10 tahun |
| D | 20 tahun |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `aab006e041b08cd19f248c9546e5a52d4a1c999ff6a9fe327f8dfb32e5dd1439`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Jumlah umur Pak Anton dan putranya sekarang 50 tahun. Lima tahun yang lalu, umur Pak Anton 7 kali umur putranya.

Umur Pak Anton tepat dua kali umur putranya ... lagi.
Pilihan: A. 40 tahun
B. 30 tahun
C. 10 tahun
D. 20 tahun
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 67. Soal `fd28da9f801d64e0ed87e09b`

Persamaan pertama sebuah sistem adalah $2x + y = 5$. Dina ingin menambahkan persamaan kedua agar sistem itu memiliki tepat satu penyelesaian, yaitu $(3, -1)$.<br><br>Persamaan kedua yang dapat dipilih Dina adalah ....

| Opsi | Isi |
|---|---|
| A | $3x - y = 8$ |
| B | $4x + 2y = 10$ |
| C | $x + y = 4$ |
| D | $x - y = 4$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `aa10d2eec46da7d1e3b194509af59bdf793224e6ef34b3e6e31d844356a07370`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Persamaan pertama sebuah sistem adalah $2x + y = 5$. Dina ingin menambahkan persamaan kedua agar sistem itu memiliki tepat satu penyelesaian, yaitu $(3, -1)$.

Persamaan kedua yang dapat dipilih Dina adalah ....
Pilihan: A. $3x - y = 8$
B. $4x + 2y = 10$
C. $x + y = 4$
D. $x - y = 4$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 68. Soal `a770e8b70f4405cecd58e68b`

Dua garis pada bidang koordinat memiliki persamaan $2x + y = 8$ dan $x - y = 1$. Kedua garis berpotongan di satu titik dan masing-masing memotong sumbu $x$. Ketiga titik itu membentuk sebuah segitiga.<br><br>Luas segitiga tersebut adalah ... satuan luas.

| Opsi | Isi |
|---|---|
| A | $3$ |
| B | $4$ |
| C | $5$ |
| D | $6$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2471bcad5c49f34bc32b3d73e8c2eebd41030c11f19362296a83e99007d4afb5`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Dua garis pada bidang koordinat memiliki persamaan $2x + y = 8$ dan $x - y = 1$. Kedua garis berpotongan di satu titik dan masing-masing memotong sumbu $x$. Ketiga titik itu membentuk sebuah segitiga.

Luas segitiga tersebut adalah ... satuan luas.
Pilihan: A. $3$
B. $4$
C. $5$
D. $6$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 69. Soal `7628dd9086d5cc309904270b`

Rina menyelesaikan sistem $3x + 2y = 19$ dan $2x + 3y = 16$. Untuk mengetahui nilai $x + y$ saja, ia menjumlahkan kedua persamaan sehingga diperoleh $5x + 5y = 35$, lalu membaginya dengan 5 tanpa mencari $x$ dan $y$ lebih dulu.<br><br>Penilaian yang tepat terhadap cara Rina adalah ....

| Opsi | Isi |
|---|---|
| A | cara Rina benar dan nilai $x + y = 7$ |
| B | cara Rina benar, tetapi nilai $x + y = 35$ |
| C | cara Rina benar, tetapi nilai $x + y = 3$ |
| D | cara Rina salah karena $x$ dan $y$ harus dicari lebih dulu, $x + y = 7$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a684a24888723751d86f4c79b4c24174da16416e8b52c12e32ce9fb83cb6dd98`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Rina menyelesaikan sistem $3x + 2y = 19$ dan $2x + 3y = 16$. Untuk mengetahui nilai $x + y$ saja, ia menjumlahkan kedua persamaan sehingga diperoleh $5x + 5y = 35$, lalu membaginya dengan 5 tanpa mencari $x$ dan $y$ lebih dulu.

Penilaian yang tepat terhadap cara Rina adalah ....
Pilihan: A. cara Rina benar dan nilai $x + y = 7$
B. cara Rina benar, tetapi nilai $x + y = 35$
C. cara Rina benar, tetapi nilai $x + y = 3$
D. cara Rina salah karena $x$ dan $y$ harus dicari lebih dulu, $x + y = 7$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 70. Soal `da1ea540a6a146340aa4e954`

Taksi A menetapkan tarif awal Rp8.000,00 ditambah Rp4.000,00 untuk setiap kilometer. Taksi B menetapkan tarif awal Rp5.000,00 ditambah Rp5.000,00 untuk setiap kilometer. Jarak tempuh dinyatakan dengan $x$ km dan biaya dengan $y$ rupiah.<br><br>Taksi A lebih murah daripada taksi B jika jarak tempuh lebih dari ....

| Opsi | Isi |
|---|---|
| A | 20 km |
| B | 3 km |
| C | $\frac{1}{3}$ km |
| D | 13 km |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5ca56a2f23623e1acacd86d3ddab130309fc0c2e697dff0ddad67db381d8e145`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Taksi A menetapkan tarif awal Rp8.000,00 ditambah Rp4.000,00 untuk setiap kilometer. Taksi B menetapkan tarif awal Rp5.000,00 ditambah Rp5.000,00 untuk setiap kilometer. Jarak tempuh dinyatakan dengan $x$ km dan biaya dengan $y$ rupiah.

Taksi A lebih murah daripada taksi B jika jarak tempuh lebih dari ....
Pilihan: A. 20 km
B. 3 km
C. $\frac{1}{3}$ km
D. 13 km
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 71. Soal `c9e78fad01e1d5000c1f796b`

Perhatikan empat sistem persamaan linear berikut.<br><br>I. $y = 2x - 1$ dan $6x - 2y = 5$<br><br>II. $y = 3x + 1$ dan $6x - 2y = -2$<br><br>III. $y = -2x + 4$ dan $4x + 2y = 7$<br><br>IV. $x - 3y = 6$ dan $2x - 6y = 5$<br><br>Pernyataan yang benar tentang keempat sistem tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | tidak ada penyelesaian: 3 sistem; tak hingga: 1 sistem; tepat satu: 0 sistem |
| B | tidak ada penyelesaian: 2 sistem; tak hingga: 1 sistem; tepat satu: 1 sistem |
| C | tidak ada penyelesaian: 1 sistem; tak hingga: 1 sistem; tepat satu: 2 sistem |
| D | tidak ada penyelesaian: 1 sistem; tak hingga: 2 sistem; tepat satu: 1 sistem |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `380f994242c51ae41976e2c156141d8b9de6f946d06923d78891add31ea106d3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan empat sistem persamaan linear berikut.

I. $y = 2x - 1$ dan $6x - 2y = 5$

II. $y = 3x + 1$ dan $6x - 2y = -2$

III. $y = -2x + 4$ dan $4x + 2y = 7$

IV. $x - 3y = 6$ dan $2x - 6y = 5$

Pernyataan yang benar tentang keempat sistem tersebut adalah ....
Pilihan: A. tidak ada penyelesaian: 3 sistem; tak hingga: 1 sistem; tepat satu: 0 sistem
B. tidak ada penyelesaian: 2 sistem; tak hingga: 1 sistem; tepat satu: 1 sistem
C. tidak ada penyelesaian: 1 sistem; tak hingga: 1 sistem; tepat satu: 2 sistem
D. tidak ada penyelesaian: 1 sistem; tak hingga: 2 sistem; tepat satu: 1 sistem
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 72. Soal `26da3e3762d0db6e54d2bf41`

Di sebuah toko, 2 bolpoin dan 3 pensil seharga Rp12.000,00, sedangkan 3 bolpoin dan 2 pensil seharga Rp13.000,00. Harga tiap barang sama pada semua pembelian.<br><br>Pembelian berikut yang harganya sesuai dengan harga barang di toko itu adalah ....

| Opsi | Isi |
|---|---|
| A | 4 bolpoin dan 3 pensil seharga Rp25.000,00 |
| B | 1 bolpoin dan 4 pensil seharga Rp11.000,00 |
| C | 2 bolpoin dan 2 pensil seharga Rp12.500,00 |
| D | 4 bolpoin dan 1 pensil seharga Rp11.000,00 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `53c515fe486297ee58977dd0d4cc520a0b58749c4acafdfa29027d28d446d2c1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Di sebuah toko, 2 bolpoin dan 3 pensil seharga Rp12.000,00, sedangkan 3 bolpoin dan 2 pensil seharga Rp13.000,00. Harga tiap barang sama pada semua pembelian.

Pembelian berikut yang harganya sesuai dengan harga barang di toko itu adalah ....
Pilihan: A. 4 bolpoin dan 3 pensil seharga Rp25.000,00
B. 1 bolpoin dan 4 pensil seharga Rp11.000,00
C. 2 bolpoin dan 2 pensil seharga Rp12.500,00
D. 4 bolpoin dan 1 pensil seharga Rp11.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 73. Soal `8d3ddc8f2a7eab1b416646cd`

Sebuah perahu menempuh 24 km searah arus sungai dalam 2 jam, lalu kembali melawan arus sejauh 24 km dalam 3 jam. Kecepatan perahu di air tenang dan kecepatan arus dianggap tetap.<br><br>Kecepatan arus sungai tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | 4 km/jam |
| B | 20 km/jam |
| C | 2 km/jam |
| D | 10 km/jam |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `061d5427d8927ded32bf0a2b476d1bb0948658e00ae1f5d2c3f59908e6a76688`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah perahu menempuh 24 km searah arus sungai dalam 2 jam, lalu kembali melawan arus sejauh 24 km dalam 3 jam. Kecepatan perahu di air tenang dan kecepatan arus dianggap tetap.

Kecepatan arus sungai tersebut adalah ....
Pilihan: A. 4 km/jam
B. 20 km/jam
C. 2 km/jam
D. 10 km/jam
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 74. Soal `08bea6f3b0a531ab4ebbfb8c`

Pasangan $(x, y)$ adalah penyelesaian sistem persamaan linear $3x + 2y = 24$ dan $x - y = 3$, dengan $x$ dan $y$ bilangan real. Diberikan tiga pernyataan.<br><br>(i) $x = 2y$<br><br>(ii) $xy = 18$<br><br>(iii) $x + y = 10$<br><br>Pernyataan yang benar adalah ....

| Opsi | Isi |
|---|---|
| A | (i) dan (ii) saja |
| B | (i), (ii), dan (iii) |
| C | (ii) dan (iii) saja |
| D | (i) dan (iii) saja |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `45c1fa5f80eaba9b516b08adda352c9806fb306dea9dd62491735f9f3f97c486`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Pasangan $(x, y)$ adalah penyelesaian sistem persamaan linear $3x + 2y = 24$ dan $x - y = 3$, dengan $x$ dan $y$ bilangan real. Diberikan tiga pernyataan.

(i) $x = 2y$

(ii) $xy = 18$

(iii) $x + y = 10$

Pernyataan yang benar adalah ....
Pilihan: A. (i) dan (ii) saja
B. (i), (ii), dan (iii)
C. (ii) dan (iii) saja
D. (i) dan (iii) saja
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 75. Soal `3aab1637e5cf084bbd80a78f`

Garis $ax + 2y = 6$ dan garis $3x - y = 2$ berpotongan di sebuah titik yang terletak pada sumbu $x$.<br><br>Nilai $a$ adalah ....

| Opsi | Isi |
|---|---|
| A | $9$ |
| B | $4$ |
| C | $3$ |
| D | $6$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `afad8da4821dff33f83f195c98c7dc2e1722d3e8f4116f8cbf3340b8f90ccbe7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Garis $ax + 2y = 6$ dan garis $3x - y = 2$ berpotongan di sebuah titik yang terletak pada sumbu $x$.

Nilai $a$ adalah ....
Pilihan: A. $9$
B. $4$
C. $3$
D. $6$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 76. Soal `de3e836b7c8ed3eedcb6cead`

Ratih membeli 4 penggaris dan 3 pensil dengan harga seluruhnya Rp18.000,00. Di toko yang sama, Tomo membeli 5 penggaris dan 4 pensil dengan harga seluruhnya Rp23.000,00.<br><br>Berapa harga 6 penggaris dan 1 pensil?

| Opsi | Isi |
|---|---|
| A | Rp41.000,00 |
| B | Rp23.000,00 |
| C | Rp20.000,00 |
| D | Rp15.000,00 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5f7f53f65fd25cd32a04aa95041c88bfc26abcfa5c9c3c60640ae084b3b9a6a6`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Ratih membeli 4 penggaris dan 3 pensil dengan harga seluruhnya Rp18.000,00. Di toko yang sama, Tomo membeli 5 penggaris dan 4 pensil dengan harga seluruhnya Rp23.000,00.

Berapa harga 6 penggaris dan 1 pensil?
Pilihan: A. Rp41.000,00
B. Rp23.000,00
C. Rp20.000,00
D. Rp15.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 77. Soal `e1443b1e4c4a24afd4fc56b4`

Di sebuah wahana, Bimo membeli 4 tiket dewasa dan 3 tiket anak dengan harga seluruhnya Rp200.000,00. Pada loket yang sama, Citra membeli 3 tiket dewasa dan 2 tiket anak dengan harga seluruhnya Rp145.000,00.<br><br>Selisih harga satu tiket dewasa dan satu tiket anak adalah ....

| Opsi | Isi |
|---|---|
| A | Rp20.000,00 |
| B | Rp15.000,00 |
| C | Rp55.000,00 |
| D | Rp35.000,00 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3596ab6cc9de5536053e5023b6c307e59f3d27751f6de542ebf6685869d2f6eb`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Di sebuah wahana, Bimo membeli 4 tiket dewasa dan 3 tiket anak dengan harga seluruhnya Rp200.000,00. Pada loket yang sama, Citra membeli 3 tiket dewasa dan 2 tiket anak dengan harga seluruhnya Rp145.000,00.

Selisih harga satu tiket dewasa dan satu tiket anak adalah ....
Pilihan: A. Rp20.000,00
B. Rp15.000,00
C. Rp55.000,00
D. Rp35.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 78. Soal `b1c456d46e83317d9089d835`

Sebuah koperasi sekolah menjual 30 buku tulis. Harga buku tulis jenis I Rp4.000,00 dan harga buku tulis jenis II Rp6.500,00. Uang yang diperoleh koperasi dari penjualan tersebut Rp150.000,00.<br><br>Banyak buku tulis jenis II yang terjual adalah ....

| Opsi | Isi |
|---|---|
| A | 15 |
| B | 12 |
| C | 20 |
| D | 18 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d5b9ea0c14a8e3d29f553cb27279ab04d9903e76743982095019d903418bc4f9`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah koperasi sekolah menjual 30 buku tulis. Harga buku tulis jenis I Rp4.000,00 dan harga buku tulis jenis II Rp6.500,00. Uang yang diperoleh koperasi dari penjualan tersebut Rp150.000,00.

Banyak buku tulis jenis II yang terjual adalah ....
Pilihan: A. 15
B. 12
C. 20
D. 18
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 79. Soal `a76ae18cafd0f404352020ee`

Seorang kasir menyimpan 28 lembar uang pecahan Rp5.000,00 dan Rp10.000,00. Jumlah seluruh uang tersebut Rp190.000,00.<br><br>Banyak lembar uang pecahan Rp10.000,00 adalah ....

| Opsi | Isi |
|---|---|
| A | 10 |
| B | 8 |
| C | 14 |
| D | 18 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8ee5144cb43d51824b055e28919f46ce376699b1391e678c646daf394828d6b3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Seorang kasir menyimpan 28 lembar uang pecahan Rp5.000,00 dan Rp10.000,00. Jumlah seluruh uang tersebut Rp190.000,00.

Banyak lembar uang pecahan Rp10.000,00 adalah ....
Pilihan: A. 10
B. 8
C. 14
D. 18
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 80. Soal `ea319da075141bd128fc28aa`

Sebuah lahan parkir berbentuk persegi panjang. Lebar lahan tersebut 7 meter lebih pendek dari panjangnya. Keliling lahan itu adalah 62 meter.<br><br>Luas lahan parkir tersebut adalah ... $m^2$.

| Opsi | Isi |
|---|---|
| A | 228 |
| B | 372 |
| C | 133 |
| D | 361 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `758f07b8a6c40c771d7998b4761c0e6e2dedcc816efa7775eb66b9fe0cc66117`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah lahan parkir berbentuk persegi panjang. Lebar lahan tersebut 7 meter lebih pendek dari panjangnya. Keliling lahan itu adalah 62 meter.

Luas lahan parkir tersebut adalah ... $m^2$.
Pilihan: A. 228
B. 372
C. 133
D. 361
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 81. Soal `fc73337d3288b54ffb35ef81`

Sebuah kolam renang anak berbentuk persegi panjang. Panjang kolam tersebut 3 meter lebih dari dua kali lebarnya. Keliling kolam itu adalah 36 meter.<br><br>Panjang kolam renang tersebut adalah ... meter.

| Opsi | Isi |
|---|---|
| A | 5 |
| B | 13 |
| C | 11 |
| D | 18 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `21f7b64eb79956144e5fc3669646202e97bc8cd173e191541e7f3e4e5c2fc21c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kolam renang anak berbentuk persegi panjang. Panjang kolam tersebut 3 meter lebih dari dua kali lebarnya. Keliling kolam itu adalah 36 meter.

Panjang kolam renang tersebut adalah ... meter.
Pilihan: A. 5
B. 13
C. 11
D. 18
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 82. Soal `99bc449fa4e99ee186600926`

Dina menyelesaikan sistem $2x + y = 8$ dan $x - y = 1$. Dari $2x + y = 8$ diperoleh $y = 8 - 2x$. Lalu $y = 8 - 2x$ disubstitusikan ke $2x + y = 8$ sehingga $2x + 8 - 2x = 8$, yaitu $8 = 8$. Dina menyimpulkan sistem itu memiliki banyak penyelesaian.<br><br>Pernyataan yang benar tentang pekerjaan Dina adalah ....

| Opsi | Isi |
|---|---|
| A | Tidak tepat, sistem itu tidak memiliki penyelesaian |
| B | Tidak tepat, tetapi penyelesaian yang benar adalah $(2, 3)$ |
| C | Tidak tepat, seharusnya disubstitusikan ke persamaan lain dan penyelesaiannya $(3, 2)$ |
| D | Sudah tepat, sistem itu memiliki banyak penyelesaian |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2764a5e85d089e2f60b2b6f50b11d23735c5ce81c4d577f7ffb3dae5641c5f5c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Dina menyelesaikan sistem $2x + y = 8$ dan $x - y = 1$. Dari $2x + y = 8$ diperoleh $y = 8 - 2x$. Lalu $y = 8 - 2x$ disubstitusikan ke $2x + y = 8$ sehingga $2x + 8 - 2x = 8$, yaitu $8 = 8$. Dina menyimpulkan sistem itu memiliki banyak penyelesaian.

Pernyataan yang benar tentang pekerjaan Dina adalah ....
Pilihan: A. Tidak tepat, sistem itu tidak memiliki penyelesaian
B. Tidak tepat, tetapi penyelesaian yang benar adalah $(2, 3)$
C. Tidak tepat, seharusnya disubstitusikan ke persamaan lain dan penyelesaiannya $(3, 2)$
D. Sudah tepat, sistem itu memiliki banyak penyelesaian
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 83. Soal `011366152fa7bf1ba6a1051c`

Diberikan sistem persamaan linear $4x + 3y = 8$ dan $7x - 2y = -15$, dengan $x$ dan $y$ bilangan real.<br><br>Nilai $x - y$ adalah ....

| Opsi | Isi |
|---|---|
| A | $3$ |
| B | $5$ |
| C | $-4$ |
| D | $-5$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `05db43a3db2b62010dd26a7ec920784294881c24e9bf30b9b6c5a8a5fa5c3e90`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Diberikan sistem persamaan linear $4x + 3y = 8$ dan $7x - 2y = -15$, dengan $x$ dan $y$ bilangan real.

Nilai $x - y$ adalah ....
Pilihan: A. $3$
B. $5$
C. $-4$
D. $-5$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 84. Soal `b529bc4f44a96722a96c2989`

Sebuah toko menjual 12 kipas angin. Harga kipas jenis A Rp150.000,00 dan harga kipas jenis B Rp250.000,00. Uang yang diperoleh toko dari penjualan tersebut Rp2.200.000,00. Dengan $x$ banyak kipas jenis A dan $y$ banyak kipas jenis B, diperoleh $x + y = 12$ dan $150.000x + 250.000y = 2.200.000$.<br><br>Banyak kipas jenis B yang terjual adalah ....

| Opsi | Isi |
|---|---|
| A | 8 |
| B | 6 |
| C | 2 |
| D | 4 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `07c44c915ed1d62c1474f4254712223831cb221a06ab054d7430fe9308b8bfce`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah toko menjual 12 kipas angin. Harga kipas jenis A Rp150.000,00 dan harga kipas jenis B Rp250.000,00. Uang yang diperoleh toko dari penjualan tersebut Rp2.200.000,00. Dengan $x$ banyak kipas jenis A dan $y$ banyak kipas jenis B, diperoleh $x + y = 12$ dan $150.000x + 250.000y = 2.200.000$.

Banyak kipas jenis B yang terjual adalah ....
Pilihan: A. 8
B. 6
C. 2
D. 4
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 85. Soal `a2efa19a3a7a3257d403f6c5`

Diberikan sistem persamaan linear $3x + 2y = 7$ (persamaan I) dan $5x - 3y = -1$ (persamaan II).<br><br>Agar variabel $x$ dapat dieliminasi, langkah yang tepat adalah ....

| Opsi | Isi |
|---|---|
| A | persamaan I dikalikan 2, persamaan II dikalikan 3, lalu dijumlahkan |
| B | persamaan I dikalikan 5, persamaan II dikalikan 3, lalu dijumlahkan |
| C | persamaan I dikalikan 5, persamaan II dikalikan 3, lalu dikurangkan |
| D | persamaan I dikalikan 3, persamaan II dikalikan 5, lalu dikurangkan |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4b8c02a67785199257f5b78cab5f6591118bb1710eea6dfac779bd03bbd21420`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Diberikan sistem persamaan linear $3x + 2y = 7$ (persamaan I) dan $5x - 3y = -1$ (persamaan II).

Agar variabel $x$ dapat dieliminasi, langkah yang tepat adalah ....
Pilihan: A. persamaan I dikalikan 2, persamaan II dikalikan 3, lalu dijumlahkan
B. persamaan I dikalikan 5, persamaan II dikalikan 3, lalu dijumlahkan
C. persamaan I dikalikan 5, persamaan II dikalikan 3, lalu dikurangkan
D. persamaan I dikalikan 3, persamaan II dikalikan 5, lalu dikurangkan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 86. Soal `ea34ba1b73e0c1a384fd7268`

Diberikan sistem persamaan linear $2x + 3y = 13$ dan $3x - 2y = 0$, dengan $x$ dan $y$ bilangan real.<br><br>Nilai $x + y$ adalah ....

| Opsi | Isi |
|---|---|
| A | $1$ |
| B | $6$ |
| C | $4$ |
| D | $5$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `78b20236825f09905613114b21add4357a17c577e67ad2afba00cbfc30bff30c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Diberikan sistem persamaan linear $2x + 3y = 13$ dan $3x - 2y = 0$, dengan $x$ dan $y$ bilangan real.

Nilai $x + y$ adalah ....
Pilihan: A. $1$
B. $6$
C. $4$
D. $5$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 87. Soal `193c57ca8b7bd7a3a718a6e9`

Diberikan sistem persamaan linear $2x + 3y = 5$ dan $4x + ky = 10$.<br><br>Agar sistem tersebut memiliki tak hingga penyelesaian, nilai $k$ adalah ....

| Opsi | Isi |
|---|---|
| A | $6$ |
| B | $5$ |
| C | $12$ |
| D | $3$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3d4d8dee8949e459f19b9b0ef0c4e4b1d8452cbdeead7fce3d41a5966fe078f7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Diberikan sistem persamaan linear $2x + 3y = 5$ dan $4x + ky = 10$.

Agar sistem tersebut memiliki tak hingga penyelesaian, nilai $k$ adalah ....
Pilihan: A. $6$
B. $5$
C. $12$
D. $3$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 88. Soal `c9e6d648b92e4bd360bcad87`

Jumlah dua bilangan adalah 47. Bilangan pertama 13 lebihnya dari bilangan kedua. Dengan $a$ bilangan pertama dan $b$ bilangan kedua, diperoleh $a + b = 47$ dan $a = b + 13$.<br><br>Hasil kali kedua bilangan tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $390$ |
| B | $340$ |
| C | $611$ |
| D | $510$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d8c44144a6bc39f2883f35a68f6698189dfe3eb0a3b831d14758a615e90692e1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Jumlah dua bilangan adalah 47. Bilangan pertama 13 lebihnya dari bilangan kedua. Dengan $a$ bilangan pertama dan $b$ bilangan kedua, diperoleh $a + b = 47$ dan $a = b + 13$.

Hasil kali kedua bilangan tersebut adalah ....
Pilihan: A. $390$
B. $340$
C. $611$
D. $510$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 89. Soal `bf2da4d2878f1047594987a4`

Di sebuah tempat parkir terdapat 30 kendaraan berupa sepeda motor dan mobil. Jumlah seluruh roda kendaraan tersebut 84. Sepeda motor beroda 2 dan mobil beroda 4. Dengan $x$ banyak sepeda motor dan $y$ banyak mobil, diperoleh $x + y = 30$ dan $2x + 4y = 84$.<br><br>Banyak mobil di tempat parkir tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | 12 |
| B | 21 |
| C | 18 |
| D | 15 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `28e206b5ae548cb830ecb32711969f367a2703e3c78e05234375695f11c86bd8`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Di sebuah tempat parkir terdapat 30 kendaraan berupa sepeda motor dan mobil. Jumlah seluruh roda kendaraan tersebut 84. Sepeda motor beroda 2 dan mobil beroda 4. Dengan $x$ banyak sepeda motor dan $y$ banyak mobil, diperoleh $x + y = 30$ dan $2x + 4y = 84$.

Banyak mobil di tempat parkir tersebut adalah ....
Pilihan: A. 12
B. 21
C. 18
D. 15
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 90. Soal `5c19edb5e127031e47af5fdb`

Pasangan $(3, -2)$ merupakan penyelesaian sistem persamaan linear $ax + 2y = 5$ dan $3x + by = 13$.<br><br>Nilai $a + b$ adalah ....

| Opsi | Isi |
|---|---|
| A | $3$ |
| B | $5$ |
| C | $1$ |
| D | $-6$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9407c889a844803bdd147b2f91928399b9dbafd69e4daadf91ce9d3dc7503288`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Pasangan $(3, -2)$ merupakan penyelesaian sistem persamaan linear $ax + 2y = 5$ dan $3x + by = 13$.

Nilai $a + b$ adalah ....
Pilihan: A. $3$
B. $5$
C. $1$
D. $-6$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 91. Soal `f6f0c085063bcfbced859df5`

Seorang guru menunjuk satu siswa secara acak dari kelas yang terdiri dari 15 siswa laki-laki dan 21 siswa perempuan. Banyaknya anggota ruang sampel percobaan tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $36$ |
| B | $15$ |
| C | $21$ |
| D | $6$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ca5329b8338aa71f00d1c297efa308f295d19bf6962c0186ee23537096c14407`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Seorang guru menunjuk satu siswa secara acak dari kelas yang terdiri dari 15 siswa laki-laki dan 21 siswa perempuan. Banyaknya anggota ruang sampel percobaan tersebut adalah ....
Pilihan: A. $36$
B. $15$
C. $21$
D. $6$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 92. Soal `25dbf7a662657b97e02ba95c`

Sebuah kantong berisi tujuh kelereng biru, tiga kelereng putih, dan lima kelereng kuning. Satu kelereng diambil secara acak dari kantong tersebut. Peluang terambilnya kelereng yang bukan biru adalah ....

| Opsi | Isi |
|---|---|
| A | $\frac{7}{15}$ |
| B | $\frac{8}{15}$ |
| C | $\frac{8}{7}$ |
| D | $\frac{1}{3}$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `737eb33d7f6baddd28fcf3f378cac1cdbd647e2256f8157526d83749ad96ea6f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kantong berisi tujuh kelereng biru, tiga kelereng putih, dan lima kelereng kuning. Satu kelereng diambil secara acak dari kantong tersebut. Peluang terambilnya kelereng yang bukan biru adalah ....
Pilihan: A. $\frac{7}{15}$
B. $\frac{8}{15}$
C. $\frac{8}{7}$
D. $\frac{1}{3}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 93. Soal `8fec18e98ab28d4c837030c7`

Sebuah toples berisi empat permen cokelat dan enam permen stroberi. Jika kalian akan mengambil satu permen dari toples tersebut secara acak, berapakah peluang terambilnya permen stroberi?

| Opsi | Isi |
|---|---|
| A | $\frac{3}{5}$ |
| B | $\frac{3}{2}$ |
| C | $\frac{2}{5}$ |
| D | $\frac{1}{6}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5286ee284c5ea674c125eb8b279131841aa85c370bf35f6bc724cbcb7f7c7aa5`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah toples berisi empat permen cokelat dan enam permen stroberi. Jika kalian akan mengambil satu permen dari toples tersebut secara acak, berapakah peluang terambilnya permen stroberi?
Pilihan: A. $\frac{3}{5}$
B. $\frac{3}{2}$
C. $\frac{2}{5}$
D. $\frac{1}{6}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 94. Soal `ecdf5ec3e4645225210e9add`

Satu pak kartu terdiri dari kartu-kartu yang diberi nomor berurutan, mulai dari 3 sampai 11. Jika kalian mengambil satu kartu secara acak, peluang mendapatkan kartu bernomor ganjil adalah ....

| Opsi | Isi |
|---|---|
| A | $\frac{4}{9}$ |
| B | $\frac{5}{8}$ |
| C | $\frac{5}{11}$ |
| D | $\frac{5}{9}$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `20d0eab7d3f17495972da06ca73366b1abdfec99872169f28ec0c3b05d004456`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Satu pak kartu terdiri dari kartu-kartu yang diberi nomor berurutan, mulai dari 3 sampai 11. Jika kalian mengambil satu kartu secara acak, peluang mendapatkan kartu bernomor ganjil adalah ....
Pilihan: A. $\frac{4}{9}$
B. $\frac{5}{8}$
C. $\frac{5}{11}$
D. $\frac{5}{9}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 95. Soal `838d1f430e9c059d5d78d916`

Pernyataan berikut yang benar mengenai hubungan kejadian dan ruang sampel dalam suatu percobaan adalah ....

| Opsi | Isi |
|---|---|
| A | kejadian dapat memuat hasil yang bukan anggota ruang sampel |
| B | ruang sampel selalu merupakan himpunan bagian dari kejadian |
| C | setiap kejadian merupakan himpunan bagian dari ruang sampel |
| D | banyak anggota kejadian selalu lebih besar daripada banyak anggota ruang sampel |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menganalisis']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `26e8524562c0a51ca4591993c0f44979599727821244c19c84e3a4d70c43b619`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Pernyataan berikut yang benar mengenai hubungan kejadian dan ruang sampel dalam suatu percobaan adalah ....
Pilihan: A. kejadian dapat memuat hasil yang bukan anggota ruang sampel
B. ruang sampel selalu merupakan himpunan bagian dari kejadian
C. setiap kejadian merupakan himpunan bagian dari ruang sampel
D. banyak anggota kejadian selalu lebih besar daripada banyak anggota ruang sampel
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 96. Soal `f756c49fb806d150ec25280a`

Pada suatu percobaan yang semua hasilnya mempunyai kemungkinan sama, rumus peluang kejadian $A$ yang benar adalah ....

| Opsi | Isi |
|---|---|
| A | $P(A) = \frac{n(S)}{n(A)}$ |
| B | $P(A) = \frac{n(A)}{n(S)}$ |
| C | $P(A) = n(S) - n(A)$ |
| D | $P(A) = n(A) \times n(S)$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d9e547df689acea354455ed8f434118ad8267c0020c49c610f2aef0eb7b0ce49`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada suatu percobaan yang semua hasilnya mempunyai kemungkinan sama, rumus peluang kejadian $A$ yang benar adalah ....
Pilihan: A. $P(A) = \frac{n(S)}{n(A)}$
B. $P(A) = \frac{n(A)}{n(S)}$
C. $P(A) = n(S) - n(A)$
D. $P(A) = n(A) \times n(S)$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 97. Soal `2911a8b2d8d2808a5c3bddae`

Manakah nilai berikut yang tidak mungkin menjadi nilai peluang suatu kejadian?

| Opsi | Isi |
|---|---|
| A | $0$ |
| B | $\frac{7}{8}$ |
| C | $1,2$ |
| D | $1$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `db43c3dc83bb3fc193eafc42e2690a12fa993cb52b8b549de1677b27e06ee4cf`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Manakah nilai berikut yang tidak mungkin menjadi nilai peluang suatu kejadian?
Pilihan: A. $0$
B. $\frac{7}{8}$
C. $1,2$
D. $1$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 98. Soal `a2c7bb449a1e0b89a562fcef`

Dalam pengambilan satu kartu secara acak dari satu pak kartu yang berisi kartu-kartu bernomor 1–20, diperoleh kartu bernomor kurang dari 25. Kejadian tersebut merupakan ....

| Opsi | Isi |
|---|---|
| A | bukan kejadian mustahil maupun pasti, peluangnya $rac{1}{2}$ |
| B | kejadian pasti |
| C | kejadian mustahil |
| D | bukan kejadian mustahil maupun pasti, peluangnya $rac{3}{4}$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0cb699ae056ba3e9cc562c176e6420e2d6e9f7c66a58e3cec2acebf3aa8c0780`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Dalam pengambilan satu kartu secara acak dari satu pak kartu yang berisi kartu-kartu bernomor 1–20, diperoleh kartu bernomor kurang dari 25. Kejadian tersebut merupakan ....
Pilihan: A. bukan kejadian mustahil maupun pasti, peluangnya $rac{1}{2}$
B. kejadian pasti
C. kejadian mustahil
D. bukan kejadian mustahil maupun pasti, peluangnya $rac{3}{4}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 99. Soal `19ee18700b1ee639b372c53b`

Dalam pengambilan satu bola secara acak dari sebuah kotak yang berisi 12 bola biru, peluang diperoleh bola biru adalah ....

| Opsi | Isi |
|---|---|
| A | $12$ |
| B | $\frac{1}{12}$ |
| C | $0$ |
| D | $1$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a4f991c7bdeac0d1c07fb84c331e8799d6005a6d3eb606e8ceec2a1f5b794a65`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Dalam pengambilan satu bola secara acak dari sebuah kotak yang berisi 12 bola biru, peluang diperoleh bola biru adalah ....
Pilihan: A. $12$
B. $\frac{1}{12}$
C. $0$
D. $1$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 100. Soal `462cb569f9ce6e8932f20c93`

Sebuah koin dilempar tiga kali. Banyaknya anggota ruang sampel percobaan tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $9$ |
| B | $6$ |
| C | $3$ |
| D | $8$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `96ec2ce5b591cde1377bdd547a3ed92ab7d362bd4f1814e1681e6aed3910dfe3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah koin dilempar tiga kali. Banyaknya anggota ruang sampel percobaan tersebut adalah ....
Pilihan: A. $9$
B. $6$
C. $3$
D. $8$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 101. Soal `53fdbdd81ce2cb408ce6c20f`

Sebuah dadu setimbang bersisi enam dilempar satu kali. Peluang diperoleh mata dadu bilangan prima adalah ....

| Opsi | Isi |
|---|---|
| A | $\frac{1}{3}$ |
| B | $\frac{2}{3}$ |
| C | $\frac{1}{2}$ |
| D | $\frac{3}{5}$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d73f66f9f8e253d287f99917b8fcf2d4943116d178030c4d2add086c88bb5601`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah dadu setimbang bersisi enam dilempar satu kali. Peluang diperoleh mata dadu bilangan prima adalah ....
Pilihan: A. $\frac{1}{3}$
B. $\frac{2}{3}$
C. $\frac{1}{2}$
D. $\frac{3}{5}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 102. Soal `37561aeb4c363fcae87bb4f8`

Peluang suatu kejadian adalah $\frac{3}{20}$. Jika dinyatakan dalam persentase, peluang tersebut sama dengan ....

| Opsi | Isi |
|---|---|
| A | $3\%$ |
| B | $30\%$ |
| C | $15\%$ |
| D | $0,15\%$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6e2ecbd41d05fa8181b3dd3f23f59583236feb3b195f8430154cfd376d01f11c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Peluang suatu kejadian adalah $\frac{3}{20}$. Jika dinyatakan dalam persentase, peluang tersebut sama dengan ....
Pilihan: A. $3\%$
B. $30\%$
C. $15\%$
D. $0,15\%$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 103. Soal `5d2bdccefbfeef43d65119c9`

Pada lempar undi sebuah dadu, kejadian $A$ adalah diperoleh mata dadu genap. Komplemen kejadian $A$ adalah ....

| Opsi | Isi |
|---|---|
| A | mata dadu 1, 3, atau 5 |
| B | mata dadu 2, 3, atau 5 |
| C | mata dadu 2, 4, atau 6 |
| D | mata dadu 1, 2, atau 3 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a0c573306320c1d8fdc57494966d62cff81d537f0811a19d03c8f91f0edd39e9`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada lempar undi sebuah dadu, kejadian $A$ adalah diperoleh mata dadu genap. Komplemen kejadian $A$ adalah ....
Pilihan: A. mata dadu 1, 3, atau 5
B. mata dadu 2, 3, atau 5
C. mata dadu 2, 4, atau 6
D. mata dadu 1, 2, atau 3
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 104. Soal `72bad53adcd459298dac3ff7`

Dua buah dadu setimbang dilempar bersama. Peluang jumlah kedua mata dadu yang muncul adalah 7 sama dengan ....

| Opsi | Isi |
|---|---|
| A | $\frac{1}{2}$ |
| B | $\frac{1}{36}$ |
| C | $\frac{7}{36}$ |
| D | $\frac{1}{6}$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f42c5858800f19404aaec9c36512fd4aa6ee359ea973ae90a000f42f8ba8b8bd`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Dua buah dadu setimbang dilempar bersama. Peluang jumlah kedua mata dadu yang muncul adalah 7 sama dengan ....
Pilihan: A. $\frac{1}{2}$
B. $\frac{1}{36}$
C. $\frac{7}{36}$
D. $\frac{1}{6}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 105. Soal `7ac55e843b8e87c029811274`

Percobaannya adalah pemilihan satu bilangan prima yang kurang dari 12 secara acak. Ruang sampel percobaan tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $S = \{2, 3, 5, 7, 11\}$ |
| B | $S = \{3, 5, 7, 11\}$ |
| C | $S = \{1, 2, 3, 5, 7, 11\}$ |
| D | $S = \{2, 3, 5, 7, 9, 11\}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e327c060cfdc3067a453db61ea7eb0f07be8d2930059859e8848f6421b26f3a3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Percobaannya adalah pemilihan satu bilangan prima yang kurang dari 12 secara acak. Ruang sampel percobaan tersebut adalah ....
Pilihan: A. $S = \{2, 3, 5, 7, 11\}$
B. $S = \{3, 5, 7, 11\}$
C. $S = \{1, 2, 3, 5, 7, 11\}$
D. $S = \{2, 3, 5, 7, 9, 11\}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 106. Soal `7b53a781bca4918e30c88bf7`

Sebuah kantong berisi 6 bola merah dan 4 bola putih. Agar peluang terambilnya bola putih pada pengambilan satu bola secara acak menjadi $\frac{1}{2}$, banyak bola putih yang harus ditambahkan ke dalam kantong adalah ....

| Opsi | Isi |
|---|---|
| A | $4$ |
| B | $1$ |
| C | $2$ |
| D | $5$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1d1605c905263b8f02b5649370a88684ea7271dbee4ad6e7dabc79155f3c96c1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kantong berisi 6 bola merah dan 4 bola putih. Agar peluang terambilnya bola putih pada pengambilan satu bola secara acak menjadi $\frac{1}{2}$, banyak bola putih yang harus ditambahkan ke dalam kantong adalah ....
Pilihan: A. $4$
B. $1$
C. $2$
D. $5$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 107. Soal `4ef1e66ac130826804c985ae`

Sebuah kotak berisi 20 bola, sebagian merah dan sisanya putih. Satu bola diambil secara acak. Peluang terambilnya bola merah lebih dari $0,3$ tetapi kurang dari $0,45$. Banyak kemungkinan banyaknya bola merah dalam kotak adalah ....

| Opsi | Isi |
|---|---|
| A | $2$ |
| B | $3$ |
| C | $15$ |
| D | $4$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `bf76573f32f96c90100ed0a3ed398597336ba734c79674c6c586b07b9ea272a4`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kotak berisi 20 bola, sebagian merah dan sisanya putih. Satu bola diambil secara acak. Peluang terambilnya bola merah lebih dari $0,3$ tetapi kurang dari $0,45$. Banyak kemungkinan banyaknya bola merah dalam kotak adalah ....
Pilihan: A. $2$
B. $3$
C. $15$
D. $4$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 108. Soal `227ae28a15be96f1483a9242`

Sebuah kotak berisi 40 kartu yang diberi nomor 1 sampai 40. Satu kartu diambil secara acak. Peluang terambilnya kartu bernomor lebih dari $k$ adalah $0,6$. Nilai $k$ adalah ....

| Opsi | Isi |
|---|---|
| A | $15$ |
| B | $16$ |
| C | $17$ |
| D | $24$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `12f2e1e16eec9f2d1533a1b381028df3a9aa065234e724c41e8d8cb2cb08cd78`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kotak berisi 40 kartu yang diberi nomor 1 sampai 40. Satu kartu diambil secara acak. Peluang terambilnya kartu bernomor lebih dari $k$ adalah $0,6$. Nilai $k$ adalah ....
Pilihan: A. $15$
B. $16$
C. $17$
D. $24$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 109. Soal `6c300776f3d075f1ab6f4f6c`

Sebuah kotak berisi 48 kupon undian. Peluang terambilnya kupon tidak berhadiah pada pengambilan satu kupon secara acak adalah $\frac{5}{8}$. Agar peluang terambilnya kupon berhadiah menjadi $\frac{1}{2}$, banyak kupon berhadiah yang harus ditambahkan ke dalam kotak adalah ....

| Opsi | Isi |
|---|---|
| A | $6$ |
| B | $30$ |
| C | $12$ |
| D | $18$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `70d8ba63f03125152918d88dd0cce3dfda37d3176933a87274039a4d43f9c0f1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kotak berisi 48 kupon undian. Peluang terambilnya kupon tidak berhadiah pada pengambilan satu kupon secara acak adalah $\frac{5}{8}$. Agar peluang terambilnya kupon berhadiah menjadi $\frac{1}{2}$, banyak kupon berhadiah yang harus ditambahkan ke dalam kotak adalah ....
Pilihan: A. $6$
B. $30$
C. $12$
D. $18$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 110. Soal `fc85c27f4d92aa3c48cf2d23`

Dua dadu setimbang dilempar bersamaan. Bilangan bulat $s$ terkecil sehingga peluang jumlah kedua mata dadu paling banyak $s$ lebih dari $\frac{1}{2}$ adalah ....

| Opsi | Isi |
|---|---|
| A | $8$ |
| B | $6$ |
| C | $18$ |
| D | $7$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7c8fde57ce4b325e4941b676217ce65ebe21fb1bfe37c0644749df9b85763651`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Dua dadu setimbang dilempar bersamaan. Bilangan bulat $s$ terkecil sehingga peluang jumlah kedua mata dadu paling banyak $s$ lebih dari $\frac{1}{2}$ adalah ....
Pilihan: A. $8$
B. $6$
C. $18$
D. $7$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 111. Soal `f116e94116ab9effec22d8c6`

Panitia ingin merancang undian dengan peluang terambilnya kupon berhadiah sebesar $24\%$ pada pengambilan satu kupon secara acak. Rancangan isi kotak yang memenuhi adalah ....

| Opsi | Isi |
|---|---|
| A | 24 kupon berhadiah dan 100 kupon tidak berhadiah |
| B | 6 kupon berhadiah dan 19 kupon tidak berhadiah |
| C | 6 kupon berhadiah dan 18 kupon tidak berhadiah |
| D | 6 kupon berhadiah dan 25 kupon tidak berhadiah |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f1ce24ce07fbe37e929a81c5591b1a9a94193b4ff33711db32c387fdbc25bc0b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Panitia ingin merancang undian dengan peluang terambilnya kupon berhadiah sebesar $24\%$ pada pengambilan satu kupon secara acak. Rancangan isi kotak yang memenuhi adalah ....
Pilihan: A. 24 kupon berhadiah dan 100 kupon tidak berhadiah
B. 6 kupon berhadiah dan 19 kupon tidak berhadiah
C. 6 kupon berhadiah dan 18 kupon tidak berhadiah
D. 6 kupon berhadiah dan 25 kupon tidak berhadiah
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 112. Soal `a3b4d800f392d5965214c2ba`

Dua pemain, Ana dan Budi, bermain dengan sebuah dadu setimbang bersisi enam yang dilempar satu kali. Ana menang jika muncul mata dadu bilangan prima. Agar permainan adil, setiap mata dadu hanya boleh memberi kemenangan kepada satu pemain dan kedua pemain harus berpeluang menang sama besar. Aturan kemenangan Budi yang memenuhi adalah ....

| Opsi | Isi |
|---|---|
| A | muncul mata dadu lebih dari 3 |
| B | muncul mata dadu 1 atau 4 |
| C | muncul mata dadu ganjil |
| D | muncul mata dadu 1, 4, atau 6 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1ffe2e42cc24da5415e8f733921d9d27e25fbed8199aa1e50f63182d14b1012e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Dua pemain, Ana dan Budi, bermain dengan sebuah dadu setimbang bersisi enam yang dilempar satu kali. Ana menang jika muncul mata dadu bilangan prima. Agar permainan adil, setiap mata dadu hanya boleh memberi kemenangan kepada satu pemain dan kedua pemain harus berpeluang menang sama besar. Aturan kemenangan Budi yang memenuhi adalah ....
Pilihan: A. muncul mata dadu lebih dari 3
B. muncul mata dadu 1 atau 4
C. muncul mata dadu ganjil
D. muncul mata dadu 1, 4, atau 6
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 113. Soal `615c8f377623d47510db938b`

Rafi ingin merancang percobaan yang semua hasilnya mempunyai kemungkinan sama dan salah satu kejadiannya berpeluang tepat $\frac{3}{8}$. Percobaan beserta kejadian yang memenuhi adalah ....

| Opsi | Isi |
|---|---|
| A | melempar tiga koin setimbang, kejadiannya semua koin menunjukkan sisi yang sama |
| B | melempar tiga koin setimbang, kejadiannya tepat dua koin menunjukkan gambar |
| C | melempar empat koin setimbang, kejadiannya tepat satu koin menunjukkan gambar |
| D | melempar tiga koin setimbang, kejadiannya paling sedikit dua koin menunjukkan gambar |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e3ee7f919f8738bcbe265b56a4b6344a025f99a1ef427f9993551f6ceaeccc0e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Rafi ingin merancang percobaan yang semua hasilnya mempunyai kemungkinan sama dan salah satu kejadiannya berpeluang tepat $\frac{3}{8}$. Percobaan beserta kejadian yang memenuhi adalah ....
Pilihan: A. melempar tiga koin setimbang, kejadiannya semua koin menunjukkan sisi yang sama
B. melempar tiga koin setimbang, kejadiannya tepat dua koin menunjukkan gambar
C. melempar empat koin setimbang, kejadiannya tepat satu koin menunjukkan gambar
D. melempar tiga koin setimbang, kejadiannya paling sedikit dua koin menunjukkan gambar
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 114. Soal `84b2737347f9ead2d5dfd18c`

Seorang perancang gim mengisi sebuah kantong dengan 36 bola berwarna merah, kuning, dan biru. Peluang terambilnya bola biru adalah $\frac{1}{3}$ dan banyak bola kuning dua kali banyak bola merah. Banyak bola kuning dalam kantong adalah ....

| Opsi | Isi |
|---|---|
| A | $16$ |
| B | $8$ |
| C | $24$ |
| D | $12$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b82ad9875e73c7267ddc133e1f3843c3daa3c9ce8e8c40abf8d4e496277ade1a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Seorang perancang gim mengisi sebuah kantong dengan 36 bola berwarna merah, kuning, dan biru. Peluang terambilnya bola biru adalah $\frac{1}{3}$ dan banyak bola kuning dua kali banyak bola merah. Banyak bola kuning dalam kantong adalah ....
Pilihan: A. $16$
B. $8$
C. $24$
D. $12$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 115. Soal `7af72fcdb9a63892ce669b2e`

Dua koin setimbang dilempar bersamaan. Andi menang jika kedua koin menunjukkan sisi yang sama, sedangkan Beni menang jika kedua koin menunjukkan sisi yang berbeda. Kesimpulan yang tepat tentang permainan tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | tidak adil, karena Andi menang pada 2 dari 3 hasil sehingga peluangnya $\frac{2}{3}$ |
| B | tidak adil, karena Beni hanya menang pada 1 dari 3 hasil sehingga peluangnya $\frac{1}{3}$ |
| C | adil, karena masing-masing berpeluang menang $\frac{1}{2}$ |
| D | tidak adil, karena Andi menang pada 2 hasil sedangkan Beni hanya pada 1 hasil dari 4 hasil |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menyimpulkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2f35518ca7470e6ebadec7a0dfd0214cdf3200405d37ca10fa03eadebb27a62e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Dua koin setimbang dilempar bersamaan. Andi menang jika kedua koin menunjukkan sisi yang sama, sedangkan Beni menang jika kedua koin menunjukkan sisi yang berbeda. Kesimpulan yang tepat tentang permainan tersebut adalah ....
Pilihan: A. tidak adil, karena Andi menang pada 2 dari 3 hasil sehingga peluangnya $\frac{2}{3}$
B. tidak adil, karena Beni hanya menang pada 1 dari 3 hasil sehingga peluangnya $\frac{1}{3}$
C. adil, karena masing-masing berpeluang menang $\frac{1}{2}$
D. tidak adil, karena Andi menang pada 2 hasil sedangkan Beni hanya pada 1 hasil dari 4 hasil
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 116. Soal `6375827c1adfea5a061459b0`

Dua dadu setimbang dilempar bersamaan. Ayu menang jika jumlah kedua mata dadu 7, sedangkan Budi menang jika jumlahnya 2, 3, atau 4. Budi berpendapat bahwa dia punya tiga jumlah untuk menang sedangkan Ayu hanya satu, sehingga dia lebih diuntungkan. Pernyataan yang tepat tentang permainan tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | adil, karena masing-masing berpeluang menang $\frac{1}{6}$ |
| B | tidak adil, karena peluang Ayu $\frac{1}{6}$ dan peluang Budi $\frac{1}{12}$ |
| C | tidak adil, karena jumlah 7 paling sering muncul sehingga Ayu lebih diuntungkan |
| D | tidak adil, karena Budi mempunyai tiga jumlah sedangkan Ayu satu sehingga Budi lebih diuntungkan |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0d3d7f9f0af0c8f68603fe9266416d0db584aec89e26ebbddb42e7252bee8012`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Dua dadu setimbang dilempar bersamaan. Ayu menang jika jumlah kedua mata dadu 7, sedangkan Budi menang jika jumlahnya 2, 3, atau 4. Budi berpendapat bahwa dia punya tiga jumlah untuk menang sedangkan Ayu hanya satu, sehingga dia lebih diuntungkan. Pernyataan yang tepat tentang permainan tersebut adalah ....
Pilihan: A. adil, karena masing-masing berpeluang menang $\frac{1}{6}$
B. tidak adil, karena peluang Ayu $\frac{1}{6}$ dan peluang Budi $\frac{1}{12}$
C. tidak adil, karena jumlah 7 paling sering muncul sehingga Ayu lebih diuntungkan
D. tidak adil, karena Budi mempunyai tiga jumlah sedangkan Ayu satu sehingga Budi lebih diuntungkan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 117. Soal `5466b85f1c514941f1aaad41`

Suatu percobaan memiliki 36 hasil yang mempunyai kemungkinan sama. Nilai berikut yang mungkin menjadi peluang suatu kejadian pada percobaan tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $\frac{4}{15}$ |
| B | $\frac{3}{8}$ |
| C | $\frac{5}{12}$ |
| D | $\frac{7}{24}$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a5ad5c374beac9f8de2afca45c50bdd9a58b38e6d2657d3e8f9c9111acf6a9c4`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Suatu percobaan memiliki 36 hasil yang mempunyai kemungkinan sama. Nilai berikut yang mungkin menjadi peluang suatu kejadian pada percobaan tersebut adalah ....
Pilihan: A. $\frac{4}{15}$
B. $\frac{3}{8}$
C. $\frac{5}{12}$
D. $\frac{7}{24}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 118. Soal `f712f464873ed09c4714cfea`

Pada pengambilan satu bola secara acak dari sebuah kantong yang berisi bola merah dan bola putih, peluang terambilnya bola merah adalah $\frac{3}{7}$. Pernyataan yang pasti benar tentang isi kantong adalah ....

| Opsi | Isi |
|---|---|
| A | banyak seluruh bola tepat 7 |
| B | banyak bola merah tepat 3 |
| C | banyak bola putih tepat 4 |
| D | banyak seluruh bola merupakan kelipatan 7 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6905d55b03ee23b4961893695d1d5cab0571f90eca586a6b835751c1f6c59405`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada pengambilan satu bola secara acak dari sebuah kantong yang berisi bola merah dan bola putih, peluang terambilnya bola merah adalah $\frac{3}{7}$. Pernyataan yang pasti benar tentang isi kantong adalah ....
Pilihan: A. banyak seluruh bola tepat 7
B. banyak bola merah tepat 3
C. banyak bola putih tepat 4
D. banyak seluruh bola merupakan kelipatan 7
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 119. Soal `b8d190cdeef8b75786c222b5`

Suatu percobaan memiliki 24 hasil yang mempunyai kemungkinan sama. Peluang kejadian $A$ sama dengan tiga kali peluang komplemen kejadian $A$. Banyak anggota kejadian $A$ adalah ....

| Opsi | Isi |
|---|---|
| A | $18$ |
| B | $6$ |
| C | $72$ |
| D | $8$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9650dc42cc8e046d0c71f1da92b0b2b64e963f69c3913e770d29d02e322a7b84`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Suatu percobaan memiliki 24 hasil yang mempunyai kemungkinan sama. Peluang kejadian $A$ sama dengan tiga kali peluang komplemen kejadian $A$. Banyak anggota kejadian $A$ adalah ....
Pilihan: A. $18$
B. $6$
C. $72$
D. $8$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 120. Soal `afd564041acc4e437d2c2098`

Sebuah koin setimbang dilempar sebanyak $n$ kali berturut-turut. Agar peluang semua lemparan menghasilkan sisi gambar kurang dari $\frac{1}{100}$, nilai $n$ bilangan asli terkecil adalah ....

| Opsi | Isi |
|---|---|
| A | $51$ |
| B | $7$ |
| C | $8$ |
| D | $6$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5c081029d482cd1b99426401407ab87ea8640ebf6a81c31411d78db0685b9555`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah koin setimbang dilempar sebanyak $n$ kali berturut-turut. Agar peluang semua lemparan menghasilkan sisi gambar kurang dari $\frac{1}{100}$, nilai $n$ bilangan asli terkecil adalah ....
Pilihan: A. $51$
B. $7$
C. $8$
D. $6$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 121. Soal `ea5779c957159c1b8ad7c37d`

Sebuah keranjang buah berisi sembilan jeruk, lima mangga, dan enam apel. Jika seorang anak mengambil satu buah tanpa memilih, peluang buah yang terambil bukan jeruk, dinyatakan dalam persentase, adalah ....

| Opsi | Isi |
|---|---|
| A | $45\%$ |
| B | $55\%$ |
| C | $11\%$ |
| D | $5,5\%$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c8f1b0538b787966907216f038c91dcdd9d4b9368fc23efae966b616fdc31995`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah keranjang buah berisi sembilan jeruk, lima mangga, dan enam apel. Jika seorang anak mengambil satu buah tanpa memilih, peluang buah yang terambil bukan jeruk, dinyatakan dalam persentase, adalah ....
Pilihan: A. $45\%$
B. $55\%$
C. $11\%$
D. $5,5\%$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 122. Soal `d26366961c3638680f7a5102`

Sebuah uang logam setimbang dilempar 4 kali berturut-turut. Peluang munculnya sisi gambar paling sedikit 3 kali adalah ....

| Opsi | Isi |
|---|---|
| A | $\frac{5}{8}$ |
| B | $\frac{1}{4}$ |
| C | $\frac{11}{16}$ |
| D | $\frac{5}{16}$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `139d067db5d9e9276a9e983c455c36abd59eb2e6943b58933824cec54e203686`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah uang logam setimbang dilempar 4 kali berturut-turut. Peluang munculnya sisi gambar paling sedikit 3 kali adalah ....
Pilihan: A. $\frac{5}{8}$
B. $\frac{1}{4}$
C. $\frac{11}{16}$
D. $\frac{5}{16}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 123. Soal `bd3e0f70004f660f91974f74`

Satu pak kartu terdiri dari kartu-kartu yang diberi nomor berurutan, mulai dari 15 sampai 44. Jika kalian mengambil satu kartu secara acak, peluang mendapatkan kartu bernomor kelipatan 6 adalah ....

| Opsi | Isi |
|---|---|
| A | $\frac{1}{6}$ |
| B | $\frac{5}{29}$ |
| C | $\frac{1}{5}$ |
| D | $\frac{5}{44}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `22276fcf24e27445d9738fb6b76db8bc00fc1eaa4007da397db892a9f2f8296d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Satu pak kartu terdiri dari kartu-kartu yang diberi nomor berurutan, mulai dari 15 sampai 44. Jika kalian mengambil satu kartu secara acak, peluang mendapatkan kartu bernomor kelipatan 6 adalah ....
Pilihan: A. $\frac{1}{6}$
B. $\frac{5}{29}$
C. $\frac{1}{5}$
D. $\frac{5}{44}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 124. Soal `e7782de8a742b2e8720341a0`

Rina diberi dua pilihan permainan. Permainan pertama: mengambil satu bola secara acak dari kantong berisi 3 bola hijau dan 9 bola kuning, menang jika terambil bola hijau. Permainan kedua: mengambil satu kartu secara acak dari kotak berisi 2 kartu bintang dan 4 kartu polos, menang jika terambil kartu bintang. Rina memilih permainan pertama karena ada 3 cara menang, lebih banyak daripada 2 cara menang pada permainan kedua. Pernyataan yang tepat tentang pilihan Rina adalah ....

| Opsi | Isi |
|---|---|
| A | pilihan Rina tepat karena banyak cara menang permainan pertama lebih banyak, sehingga peluangnya lebih besar |
| B | pilihan Rina kurang tepat karena peluang menang permainan pertama $\frac{1}{4}$ lebih kecil daripada permainan kedua $\frac{1}{3}$ |
| C | pilihan Rina kurang tepat karena peluang menang permainan pertama $\frac{1}{3}$ lebih kecil daripada permainan kedua $\frac{1}{4}$ |
| D | kedua permainan sama menguntungkan karena menang ditentukan oleh satu kali pengambilan |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8af637204d2bb37c4b8803d9dda3b5d372b44b64edfae85bcba742eca9bd5cbc`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Rina diberi dua pilihan permainan. Permainan pertama: mengambil satu bola secara acak dari kantong berisi 3 bola hijau dan 9 bola kuning, menang jika terambil bola hijau. Permainan kedua: mengambil satu kartu secara acak dari kotak berisi 2 kartu bintang dan 4 kartu polos, menang jika terambil kartu bintang. Rina memilih permainan pertama karena ada 3 cara menang, lebih banyak daripada 2 cara menang pada permainan kedua. Pernyataan yang tepat tentang pilihan Rina adalah ....
Pilihan: A. pilihan Rina tepat karena banyak cara menang permainan pertama lebih banyak, sehingga peluangnya lebih besar
B. pilihan Rina kurang tepat karena peluang menang permainan pertama $\frac{1}{4}$ lebih kecil daripada permainan kedua $\frac{1}{3}$
C. pilihan Rina kurang tepat karena peluang menang permainan pertama $\frac{1}{3}$ lebih kecil daripada permainan kedua $\frac{1}{4}$
D. kedua permainan sama menguntungkan karena menang ditentukan oleh satu kali pengambilan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 125. Soal `094678fc6b4c7f48c207730e`

Sebuah kantong berisi 2 bola biru dan 8 bola merah. Satu bola diambil secara acak. Karena warna bola hanya biru atau merah, Tono menyimpulkan peluang terambilnya bola biru adalah $50\%$. Pernyataan yang tepat tentang kesimpulan Tono adalah ....

| Opsi | Isi |
|---|---|
| A | kesimpulan Tono salah karena peluang terambilnya bola biru adalah $80\%$ |
| B | kesimpulan Tono benar karena hanya ada dua warna sehingga masing-masing berpeluang $50\%$ |
| C | kesimpulan Tono salah karena peluang terambilnya bola biru adalah $25\%$ |
| D | kesimpulan Tono salah karena peluang terambilnya bola biru adalah $20\%$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menyimpulkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8790074e5084c9c9135a7fc650eb2a6a831b94ecc11ed2833516daf6902bf535`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kantong berisi 2 bola biru dan 8 bola merah. Satu bola diambil secara acak. Karena warna bola hanya biru atau merah, Tono menyimpulkan peluang terambilnya bola biru adalah $50\%$. Pernyataan yang tepat tentang kesimpulan Tono adalah ....
Pilihan: A. kesimpulan Tono salah karena peluang terambilnya bola biru adalah $80\%$
B. kesimpulan Tono benar karena hanya ada dua warna sehingga masing-masing berpeluang $50\%$
C. kesimpulan Tono salah karena peluang terambilnya bola biru adalah $25\%$
D. kesimpulan Tono salah karena peluang terambilnya bola biru adalah $20\%$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 126. Soal `760b0b16283d20fbdc0cb811`

Dua dadu setimbang dilempar bersamaan. Seorang pemain boleh memilih satu aturan agar menang: jumlah mata dadu 4, jumlah 9, atau jumlah 12. Aturan yang paling menguntungkan dan peluang menangnya adalah ....

| Opsi | Isi |
|---|---|
| A | jumlah 4, peluangnya $\frac{1}{12}$ |
| B | ketiganya sama, peluangnya $\frac{1}{3}$ |
| C | jumlah 12, peluangnya $\frac{1}{36}$ |
| D | jumlah 9, peluangnya $\frac{1}{9}$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5b157dcb84fb2175a64a20250c78341e5c2f883d6688dc1e3e551a02c3a1a555`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Dua dadu setimbang dilempar bersamaan. Seorang pemain boleh memilih satu aturan agar menang: jumlah mata dadu 4, jumlah 9, atau jumlah 12. Aturan yang paling menguntungkan dan peluang menangnya adalah ....
Pilihan: A. jumlah 4, peluangnya $\frac{1}{12}$
B. ketiganya sama, peluangnya $\frac{1}{3}$
C. jumlah 12, peluangnya $\frac{1}{36}$
D. jumlah 9, peluangnya $\frac{1}{9}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 127. Soal `60d88acb49321dd41084d9aa`

Sebuah koin setimbang dilempar sebanyak 3 kali berturut-turut. Kejadian $B$ adalah muncul gambar pada ketiga lemparan. Peluang bahwa kejadian $B$ tidak terjadi adalah ....

| Opsi | Isi |
|---|---|
| A | $\frac{3}{4}$ |
| B | $\frac{5}{6}$ |
| C | $\frac{1}{8}$ |
| D | $\frac{7}{8}$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `60dd809c93e979fe5af64b16e4e30efeb30cbd39a8d1189e5ee0056f170e0b19`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah koin setimbang dilempar sebanyak 3 kali berturut-turut. Kejadian $B$ adalah muncul gambar pada ketiga lemparan. Peluang bahwa kejadian $B$ tidak terjadi adalah ....
Pilihan: A. $\frac{3}{4}$
B. $\frac{5}{6}$
C. $\frac{1}{8}$
D. $\frac{7}{8}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 128. Soal `81c73b378616a22668a10e98`

Sebuah dadu setimbang bersisi enam dilempar satu kali. Peluang diperoleh mata dadu genap atau mata dadu lebih dari 4 adalah ....

| Opsi | Isi |
|---|---|
| A | $\frac{5}{6}$ |
| B | $\frac{2}{3}$ |
| C | $\frac{1}{6}$ |
| D | $\frac{1}{2}$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `25940b5fb861aa4e1de07c47bb8296d4cf5a12b4a8504f2c2fefc75ff218f90d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah dadu setimbang bersisi enam dilempar satu kali. Peluang diperoleh mata dadu genap atau mata dadu lebih dari 4 adalah ....
Pilihan: A. $\frac{5}{6}$
B. $\frac{2}{3}$
C. $\frac{1}{6}$
D. $\frac{1}{2}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 129. Soal `4a4684165bc278be6e9d913e`

Dua dadu setimbang dilempar bersamaan. Peluang jumlah kedua mata dadu yang muncul lebih dari 8 adalah ....

| Opsi | Isi |
|---|---|
| A | $\frac{1}{9}$ |
| B | $\frac{5}{12}$ |
| C | $\frac{5}{18}$ |
| D | $\frac{5}{6}$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d7a6826edab696d1c927e17a3948a68fa58897da3e329d793126e51b12314caf`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Dua dadu setimbang dilempar bersamaan. Peluang jumlah kedua mata dadu yang muncul lebih dari 8 adalah ....
Pilihan: A. $\frac{1}{9}$
B. $\frac{5}{12}$
C. $\frac{5}{18}$
D. $\frac{5}{6}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 130. Soal `c2c646442468369f565431a6`

Sebuah kotak berisi 20 bola, 8 di antaranya merah. Ke dalam kotak ditambahkan 5 bola merah lagi, kemudian satu bola diambil secara acak. Peluang terambilnya bola merah sekarang adalah ....

| Opsi | Isi |
|---|---|
| A | $\frac{2}{5}$ |
| B | $\frac{13}{25}$ |
| C | $\frac{13}{20}$ |
| D | $\frac{8}{25}$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `14363a58759f4ce6334e5d109c2d9bd76112f21401348cc84187901a7a163b11`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kotak berisi 20 bola, 8 di antaranya merah. Ke dalam kotak ditambahkan 5 bola merah lagi, kemudian satu bola diambil secara acak. Peluang terambilnya bola merah sekarang adalah ....
Pilihan: A. $\frac{2}{5}$
B. $\frac{13}{25}$
C. $\frac{13}{20}$
D. $\frac{8}{25}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 131. Soal `4a5ff5508ba54e401bb0ba7f`

Kotak I berisi 4 bola biru dan 6 bola putih. Kotak II berisi 6 bola biru dan 10 bola putih. Dari tiap kotak diambil satu bola secara acak. Pernyataan yang benar tentang peluang terambilnya bola biru adalah ....

| Opsi | Isi |
|---|---|
| A | lebih besar pada Kotak II karena memuat lebih banyak bola biru, yaitu 6 bola |
| B | sama besar pada kedua kotak karena hanya ada dua warna bola |
| C | lebih besar pada Kotak I, yaitu $\frac{2}{5}$ dibanding $\frac{3}{8}$ pada Kotak II |
| D | lebih besar pada Kotak II, yaitu $\frac{3}{5}$ dibanding $\frac{2}{5}$ pada Kotak I |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `501745f3334d5495372af1b8a0eb0aee21791edd8e8b9d1b03efaf4522000c08`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Kotak I berisi 4 bola biru dan 6 bola putih. Kotak II berisi 6 bola biru dan 10 bola putih. Dari tiap kotak diambil satu bola secara acak. Pernyataan yang benar tentang peluang terambilnya bola biru adalah ....
Pilihan: A. lebih besar pada Kotak II karena memuat lebih banyak bola biru, yaitu 6 bola
B. sama besar pada kedua kotak karena hanya ada dua warna bola
C. lebih besar pada Kotak I, yaitu $\frac{2}{5}$ dibanding $\frac{3}{8}$ pada Kotak II
D. lebih besar pada Kotak II, yaitu $\frac{3}{5}$ dibanding $\frac{2}{5}$ pada Kotak I
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 132. Soal `9109ffcda5a1da2c53b1a752`

Sebuah kotak berisi 40 kupon undian. Peluang terambilnya kupon berhadiah pada pengambilan satu kupon secara acak adalah $\frac{3}{10}$. Banyaknya kupon yang tidak berhadiah adalah ....

| Opsi | Isi |
|---|---|
| A | $37$ |
| B | $7$ |
| C | $28$ |
| D | $12$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4944af31fee2fbe2a3fe1ba61267c45d294a85a5926bdcf48dc7479073e0969f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kotak berisi 40 kupon undian. Peluang terambilnya kupon berhadiah pada pengambilan satu kupon secara acak adalah $\frac{3}{10}$. Banyaknya kupon yang tidak berhadiah adalah ....
Pilihan: A. $37$
B. $7$
C. $28$
D. $12$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 133. Soal `1b6b4cb1ad0ca1bfd0225fc7`

Rani melempar dua koin setimbang. Dia menulis hasil yang mungkin: (A, A), (A, G), (G, G), lalu menyimpulkan peluang mendapat satu angka dan satu gambar adalah $\frac{1}{3}$. Pernyataan yang tepat tentang perhitungan Rani adalah ....

| Opsi | Isi |
|---|---|
| A | peluang yang benar $\frac{1}{4}$ karena hanya (A, G) yang memenuhi dari 4 hasil |
| B | ruang sampel sudah tepat tetapi banyak anggota kejadian seharusnya 2 sehingga peluangnya $\frac{2}{3}$ |
| C | hasil (G, A) tidak ikut didaftar sehingga ruang sampel seharusnya 4 anggota dan peluang yang benar $\frac{1}{2}$ |
| D | perhitungan Rani sudah tepat karena (A, G) dan (G, A) merupakan hasil yang sama |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `64f3fe86ac440c59b41f92de534e4fe97bf053315aa5054918002ed6582feb73`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Rani melempar dua koin setimbang. Dia menulis hasil yang mungkin: (A, A), (A, G), (G, G), lalu menyimpulkan peluang mendapat satu angka dan satu gambar adalah $\frac{1}{3}$. Pernyataan yang tepat tentang perhitungan Rani adalah ....
Pilihan: A. peluang yang benar $\frac{1}{4}$ karena hanya (A, G) yang memenuhi dari 4 hasil
B. ruang sampel sudah tepat tetapi banyak anggota kejadian seharusnya 2 sehingga peluangnya $\frac{2}{3}$
C. hasil (G, A) tidak ikut didaftar sehingga ruang sampel seharusnya 4 anggota dan peluang yang benar $\frac{1}{2}$
D. perhitungan Rani sudah tepat karena (A, G) dan (G, A) merupakan hasil yang sama
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 134. Soal `feb261277293b4d149ee5c2f`

Sebuah dadu setimbang dan sebuah koin setimbang dilempar bersamaan. Peluang munculnya sisi angka pada koin dan mata dadu bilangan prima pada dadu adalah ....

| Opsi | Isi |
|---|---|
| A | $\frac{1}{4}$ |
| B | $\frac{1}{12}$ |
| C | $\frac{3}{8}$ |
| D | $\frac{1}{2}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5706c5131983cbbe12a18913e3c75192a21966f27f22748164a7be3e51368e40`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah dadu setimbang dan sebuah koin setimbang dilempar bersamaan. Peluang munculnya sisi angka pada koin dan mata dadu bilangan prima pada dadu adalah ....
Pilihan: A. $\frac{1}{4}$
B. $\frac{1}{12}$
C. $\frac{3}{8}$
D. $\frac{1}{2}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 135. Soal `afe46653198f4b6cb9f9c0d5`

Setiap huruf pada kata MATEMATIKA ditulis pada sebuah kartu yang bentuknya sama, sehingga ada 10 kartu. Kartu dikocok dan satu kartu diambil secara acak. Peluang terambilnya kartu yang hurufnya muncul lebih dari satu kali dalam kata tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $\frac{7}{10}$ |
| B | $\frac{1}{2}$ |
| C | $\frac{7}{9}$ |
| D | $\frac{3}{10}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `97a65ea3692dc950487b2681966e3b08f4ae65d011b112d43379b5686419b4b6`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Setiap huruf pada kata MATEMATIKA ditulis pada sebuah kartu yang bentuknya sama, sehingga ada 10 kartu. Kartu dikocok dan satu kartu diambil secara acak. Peluang terambilnya kartu yang hurufnya muncul lebih dari satu kali dalam kata tersebut adalah ....
Pilihan: A. $\frac{7}{10}$
B. $\frac{1}{2}$
C. $\frac{7}{9}$
D. $\frac{3}{10}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 136. Soal `be4ad645a95eb2fa371d44fc`

Sebuah program komputer menampilkan 15 bilangan 5–8 secara acak. Hasilnya sebagai berikut.<br><br>6, 8, 5, 6, 6, 7, 8, 6, 5, 6, 8, 6, 7, 6, 6<br><br>Frekuensi relatif munculnya bilangan 7 adalah ....

| Opsi | Isi |
|---|---|
| A | $\frac{2}{15}$ |
| B | $\frac{2}{4}$ |
| C | $\frac{2}{13}$ |
| D | $\frac{3}{15}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5c88dc7028c83226ffe03ecfd7e6b37625d288975ab4a5b9f2853516793a2225`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah program komputer menampilkan 15 bilangan 5–8 secara acak. Hasilnya sebagai berikut.

6, 8, 5, 6, 6, 7, 8, 6, 5, 6, 8, 6, 7, 6, 6

Frekuensi relatif munculnya bilangan 7 adalah ....
Pilihan: A. $\frac{2}{15}$
B. $\frac{2}{4}$
C. $\frac{2}{13}$
D. $\frac{3}{15}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 137. Soal `715c3c2d7746688297aba6b5`

Rina mencatat cuaca selama 10 hari berturut-turut, C untuk cerah dan H untuk hujan.<br><br>C, H, C, C, H, C, C, C, H, C<br><br>Frekuensi relatif hari hujan dari catatan Rina adalah ....

| Opsi | Isi |
|---|---|
| A | $\frac{3}{10}$ |
| B | $\frac{3}{7}$ |
| C | $\frac{7}{10}$ |
| D | $\frac{1}{2}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `579a17dde06916e3d746f81d9fcd591b3b75160a30cca9d4d9511a6fcec2535d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Rina mencatat cuaca selama 10 hari berturut-turut, C untuk cerah dan H untuk hujan.

C, H, C, C, H, C, C, C, H, C

Frekuensi relatif hari hujan dari catatan Rina adalah ....
Pilihan: A. $\frac{3}{10}$
B. $\frac{3}{7}$
C. $\frac{7}{10}$
D. $\frac{1}{2}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 138. Soal `e69ca9d9da6e14994e293b9a`

Sebuah roda bernomor 1–5 diputar sebanyak 40 kali. Banyaknya jarum menunjuk tiap nomor tercatat pada tabel berikut.<br><br>\| Nomor \| 1 \| 2 \| 3 \| 4 \| 5 \|<br>\|---\|---\|---\|---\|---\|---\|<br>\| Frekuensi \| 8 \| 12 \| 6 \| 9 \| 5 \|<br><br>Frekuensi relatif jarum menunjuk nomor 2, jika dinyatakan dalam persen, adalah ....

| Opsi | Isi |
|---|---|
| A | $70\%$ |
| B | $12\%$ |
| C | $30\%$ |
| D | $3\%$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2b0af046f7eeebe731cd4b28c5ce62dae3dbeccc067450ecc493b13d1fae7519`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah roda bernomor 1–5 diputar sebanyak 40 kali. Banyaknya jarum menunjuk tiap nomor tercatat pada tabel berikut.

| Nomor | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Frekuensi | 8 | 12 | 6 | 9 | 5 |

Frekuensi relatif jarum menunjuk nomor 2, jika dinyatakan dalam persen, adalah ....
Pilihan: A. $70\%$
B. $12\%$
C. $30\%$
D. $3\%$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 139. Soal `bc2c93e91b4102a4a9453008`

Dalam sebuah eksperimen, seorang siswa mengambil satu bola dari kantong secara acak sebanyak $k$ kali dengan pengembalian. Bola biru terambil sebanyak $b$ kali. Frekuensi relatif terambilnya bola biru adalah ....

| Opsi | Isi |
|---|---|
| A | $\frac{k}{b}$ |
| B | $\frac{b}{k}$ |
| C | $\frac{k-b}{k}$ |
| D | $\frac{b}{k-b}$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ab0a80dbc91281ddfa3c2a0f527c7f578af1e91d091ec310a64998de45379dac`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Dalam sebuah eksperimen, seorang siswa mengambil satu bola dari kantong secara acak sebanyak $k$ kali dengan pengembalian. Bola biru terambil sebanyak $b$ kali. Frekuensi relatif terambilnya bola biru adalah ....
Pilihan: A. $\frac{k}{b}$
B. $\frac{b}{k}$
C. $\frac{k-b}{k}$
D. $\frac{b}{k-b}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 140. Soal `a24109469d957c5f28f85a3c`

Frekuensi relatif suatu kejadian juga disebut ....

| Opsi | Isi |
|---|---|
| A | ruang sampel |
| B | frekuensi harapan |
| C | peluang teoretis |
| D | peluang empiris |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1cfe58f31e6d4ca7ae2ed6153ebc0f7b934f2bcc095077d060833689659a4f62`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Frekuensi relatif suatu kejadian juga disebut ....
Pilihan: A. ruang sampel
B. frekuensi harapan
C. peluang teoretis
D. peluang empiris
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 141. Soal `0837595f5c04dca939236059`

Sebuah koin dilempar undi berulang kali dan banyak lemparannya semakin besar. Frekuensi relatif munculnya sisi angka akan ....

| Opsi | Isi |
|---|---|
| A | semakin menjauhi peluang teoretisnya, yaitu $\frac{1}{2}$ |
| B | mendekati peluang teoretisnya, yaitu $\frac{1}{2}$ |
| C | mendekati 1 karena sisi angka makin sering muncul |
| D | selalu tepat $\frac{1}{2}$ pada setiap banyak lemparan |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c89d15c662ce04217a35f442e378df13180c6ed2dfa4b75954bf08029e865625`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah koin dilempar undi berulang kali dan banyak lemparannya semakin besar. Frekuensi relatif munculnya sisi angka akan ....
Pilihan: A. semakin menjauhi peluang teoretisnya, yaitu $\frac{1}{2}$
B. mendekati peluang teoretisnya, yaitu $\frac{1}{2}$
C. mendekati 1 karena sisi angka makin sering muncul
D. selalu tepat $\frac{1}{2}$ pada setiap banyak lemparan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 142. Soal `4df50834581422917197222e`

Sebuah dadu dilempar undi 5 kali dan mata dadu 6 tidak pernah muncul, sehingga frekuensi relatif muncul mata dadu 6 adalah 0. Pernyataan yang paling tepat adalah ....

| Opsi | Isi |
|---|---|
| A | peluang teoretis muncul mata dadu 6 sama dengan 0 |
| B | mata dadu 6 tidak akan muncul pada lemparan berikutnya |
| C | mata dadu 6 tetap mungkin muncul karena percobaannya masih sedikit |
| D | muncul mata dadu 6 adalah kejadian yang mustahil |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6ba45bfcb4bc7e0e8eb0882b1caaf1f4ea0b32f8c1867618fe8891d4956d04ee`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah dadu dilempar undi 5 kali dan mata dadu 6 tidak pernah muncul, sehingga frekuensi relatif muncul mata dadu 6 adalah 0. Pernyataan yang paling tepat adalah ....
Pilihan: A. peluang teoretis muncul mata dadu 6 sama dengan 0
B. mata dadu 6 tidak akan muncul pada lemparan berikutnya
C. mata dadu 6 tetap mungkin muncul karena percobaannya masih sedikit
D. muncul mata dadu 6 adalah kejadian yang mustahil
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 143. Soal `b43e04491ec8f296f2504b5d`

Frekuensi relatif suatu kejadian ditentukan dengan membandingkan ....

| Opsi | Isi |
|---|---|
| A | banyaknya hasil yang memenuhi kejadian dengan total banyaknya percobaan |
| B | banyaknya hasil yang tidak memenuhi kejadian dengan total banyaknya percobaan |
| C | total banyaknya percobaan dengan banyaknya hasil yang memenuhi kejadian |
| D | banyaknya hasil yang memenuhi kejadian dengan banyaknya jenis hasil yang mungkin |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `eedbb84a85f2b4faf613f2c958533b03e99054130df3890d5e155e1c6607c52d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Frekuensi relatif suatu kejadian ditentukan dengan membandingkan ....
Pilihan: A. banyaknya hasil yang memenuhi kejadian dengan total banyaknya percobaan
B. banyaknya hasil yang tidak memenuhi kejadian dengan total banyaknya percobaan
C. total banyaknya percobaan dengan banyaknya hasil yang memenuhi kejadian
D. banyaknya hasil yang memenuhi kejadian dengan banyaknya jenis hasil yang mungkin
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 144. Soal `13e6d1c388b48d8be007f241`

Suatu eksperimen diulang-ulang dan frekuensi relatif suatu kejadian semakin lama semakin mendekati 0,5. Kejadian yang paling tepat adalah ....

| Opsi | Isi |
|---|---|
| A | dalam pemilihan bilangan 1–4 secara acak, diperoleh bilangan lebih dari 1 |
| B | dalam lempar undi sebuah dadu, diperoleh mata dadu lebih dari 4 |
| C | dalam pelemparan dua koin, diperoleh dua sisi gambar |
| D | dalam lempar undi sebuah dadu, diperoleh mata dadu bilangan genap |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b02f4d6c720dc8700790af11d0d2954a85a2073dc91828111dfd76ff12f5633e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Suatu eksperimen diulang-ulang dan frekuensi relatif suatu kejadian semakin lama semakin mendekati 0,5. Kejadian yang paling tepat adalah ....
Pilihan: A. dalam pemilihan bilangan 1–4 secara acak, diperoleh bilangan lebih dari 1
B. dalam lempar undi sebuah dadu, diperoleh mata dadu lebih dari 4
C. dalam pelemparan dua koin, diperoleh dua sisi gambar
D. dalam lempar undi sebuah dadu, diperoleh mata dadu bilangan genap
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 145. Soal `6396e7ec7a35c6794251745b`

Sebuah tas berisi 6 kelereng merah dan 14 kelereng biru. Satu kelereng diambil secara acak dengan pengembalian, dilakukan berulang kali dalam jumlah sangat banyak. Frekuensi relatif terambilnya kelereng biru akan mendekati ....

| Opsi | Isi |
|---|---|
| A | $\frac{14}{6}$ |
| B | $\frac{1}{2}$ |
| C | $\frac{6}{20}=\frac{3}{10}$ |
| D | $\frac{14}{20}=\frac{7}{10}$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c67353a2851329ea854a9f5f0d61777bce7fee12bd2708d85d2643ea7f4315b1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah tas berisi 6 kelereng merah dan 14 kelereng biru. Satu kelereng diambil secara acak dengan pengembalian, dilakukan berulang kali dalam jumlah sangat banyak. Frekuensi relatif terambilnya kelereng biru akan mendekati ....
Pilihan: A. $\frac{14}{6}$
B. $\frac{1}{2}$
C. $\frac{6}{20}=\frac{3}{10}$
D. $\frac{14}{20}=\frac{7}{10}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 146. Soal `3878105f54c9a2f4c96feb28`

Dalam sebuah kotak terdapat 40 kartu bergambar bulan, bintang, atau matahari. Sebanyak 80 anak bergiliran mengambil satu kartu secara acak dengan mata tertutup, lalu mengembalikannya. Hasilnya:<br><br>\| Gambar \| Bulan \| Bintang \| Matahari \|<br>\|---\|---\|---\|---\|<br>\| Frekuensi \| 10 \| 24 \| 46 \|<br><br>Perkiraan banyaknya kartu bergambar bulan di dalam kotak adalah ....

| Opsi | Isi |
|---|---|
| A | 12 kartu |
| B | 5 kartu |
| C | 10 kartu |
| D | 20 kartu |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `21066b01dfa9a7364c58b4bbbf2c68f0b5bcf9aa019bdec88a7c64b2a7cd9059`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Dalam sebuah kotak terdapat 40 kartu bergambar bulan, bintang, atau matahari. Sebanyak 80 anak bergiliran mengambil satu kartu secara acak dengan mata tertutup, lalu mengembalikannya. Hasilnya:

| Gambar | Bulan | Bintang | Matahari |
|---|---|---|---|
| Frekuensi | 10 | 24 | 46 |

Perkiraan banyaknya kartu bergambar bulan di dalam kotak adalah ....
Pilihan: A. 12 kartu
B. 5 kartu
C. 10 kartu
D. 20 kartu
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 147. Soal `2368aa1c50b9a426b00df719`

Seperangkat kartu berisi 10 kartu yang masing-masing bergambar persegi atau segitiga. Setelah dilakukan 200 kali pengambilan satu kartu secara acak dengan pengembalian, kartu persegi terambil 122 kali dan kartu segitiga terambil 78 kali.<br><br>Perkiraan banyaknya kartu bergambar persegi dan segitiga dalam seperangkat kartu tersebut berturut-turut adalah ....

| Opsi | Isi |
|---|---|
| A | 5 kartu persegi dan 5 kartu segitiga |
| B | 7 kartu persegi dan 3 kartu segitiga |
| C | 6 kartu persegi dan 4 kartu segitiga |
| D | 4 kartu persegi dan 6 kartu segitiga |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `097cae66cab7cb6a7fd6ef09ebf987a522787b1b32d9d7eddab27c701af1983d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Seperangkat kartu berisi 10 kartu yang masing-masing bergambar persegi atau segitiga. Setelah dilakukan 200 kali pengambilan satu kartu secara acak dengan pengembalian, kartu persegi terambil 122 kali dan kartu segitiga terambil 78 kali.

Perkiraan banyaknya kartu bergambar persegi dan segitiga dalam seperangkat kartu tersebut berturut-turut adalah ....
Pilihan: A. 5 kartu persegi dan 5 kartu segitiga
B. 7 kartu persegi dan 3 kartu segitiga
C. 6 kartu persegi dan 4 kartu segitiga
D. 4 kartu persegi dan 6 kartu segitiga
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 148. Soal `aa27d8311f21292a1e8e517d`

Sebuah roda putar mukanya terbagi menjadi 8 juring sama besar, tiap juring berwarna biru (B) atau kuning (K). Roda diputar 20 kali dan jarum menunjuk warna berikut.<br><br>K, B, K, K, K, B, K, K, K, K, B, K, K, K, B, K, K, K, B, K<br><br>Dugaan banyaknya juring berwarna biru pada roda tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | 2 juring |
| B | 5 juring |
| C | 6 juring |
| D | 4 juring |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `dcbdbc95166e779678493cdf61df369c61c62bdb369dcde0acb9bed0a8a86150`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah roda putar mukanya terbagi menjadi 8 juring sama besar, tiap juring berwarna biru (B) atau kuning (K). Roda diputar 20 kali dan jarum menunjuk warna berikut.

K, B, K, K, K, B, K, K, K, K, B, K, K, K, B, K, K, K, B, K

Dugaan banyaknya juring berwarna biru pada roda tersebut adalah ....
Pilihan: A. 2 juring
B. 5 juring
C. 6 juring
D. 4 juring
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 149. Soal `96c4ac6f809d3a1c7cd61ce4`

Sebuah roda putar diputar berulang kali. Frekuensi relatif jarum menunjuk juring ungu tercatat pada tabel berikut.<br><br>\| Banyak putaran \| 10 \| 50 \| 200 \| 1000 \| 5000 \|<br>\|---\|---\|---\|---\|---\|---\|<br>\| Frekuensi relatif \| 0,80 \| 0,68 \| 0,62 \| 0,60 \| 0,60 \|<br><br>Dugaan terbaik untuk peluang jarum menunjuk juring ungu adalah ....

| Opsi | Isi |
|---|---|
| A | $0{,}66$ |
| B | $0{,}6$ |
| C | $0{,}8$ |
| D | $0{,}4$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2e45ee17cb94230010db3325ecc4713352bf4f2cec20b154df7f2df375238adb`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah roda putar diputar berulang kali. Frekuensi relatif jarum menunjuk juring ungu tercatat pada tabel berikut.

| Banyak putaran | 10 | 50 | 200 | 1000 | 5000 |
|---|---|---|---|---|---|
| Frekuensi relatif | 0,80 | 0,68 | 0,62 | 0,60 | 0,60 |

Dugaan terbaik untuk peluang jarum menunjuk juring ungu adalah ....
Pilihan: A. $0{,}66$
B. $0{,}6$
C. $0{,}8$
D. $0{,}4$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 150. Soal `9f52b05e9544090136803121`

Sebuah papan memuat 25 stiker berwarna merah, hijau, atau ungu yang tidak terlihat warnanya. Seorang siswa mengambil satu stiker secara acak sebanyak 100 kali dengan pengembalian dan mencatat hasilnya.<br><br>\| Warna \| Merah \| Hijau \| Ungu \|<br>\|---\|---\|---\|---\|<br>\| Frekuensi \| 28 \| 40 \| 32 \|<br><br>Perkiraan banyaknya stiker hijau pada papan tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | 15 stiker |
| B | 8 stiker |
| C | 10 stiker |
| D | 40 stiker |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `534467ec5b9aa17e4b9dd0e49ba899f2eee62f797d58f08a9372a32b23cd0ce7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah papan memuat 25 stiker berwarna merah, hijau, atau ungu yang tidak terlihat warnanya. Seorang siswa mengambil satu stiker secara acak sebanyak 100 kali dengan pengembalian dan mencatat hasilnya.

| Warna | Merah | Hijau | Ungu |
|---|---|---|---|
| Frekuensi | 28 | 40 | 32 |

Perkiraan banyaknya stiker hijau pada papan tersebut adalah ....
Pilihan: A. 15 stiker
B. 8 stiker
C. 10 stiker
D. 40 stiker
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 151. Soal `2e16b6e75406ef7de7ce300d`

Tiara dan Bagas mengundi sebuah koin 6 kali. Setelah tiap lemparan, keduanya mencatat frekuensi relatif munculnya angka (A). G menyatakan gambar.<br><br>\| Lemparan ke- \| 1 \| 2 \| 3 \| 4 \| 5 \| 6 \|<br>\|---\|---\|---\|---\|---\|---\|---\|<br>\| Hasil \| A \| G \| G \| A \| A \| G \|<br>\| Catatan Tiara \| $1$ \| $\frac{1}{2}$ \| $\frac{1}{3}$ \| $\frac{1}{2}$ \| $\frac{3}{5}$ \| $\frac{1}{2}$ \|<br>\| Catatan Bagas \| $1$ \| $\frac{1}{2}$ \| $\frac{1}{3}$ \| $\frac{1}{4}$ \| $\frac{3}{5}$ \| $\frac{1}{2}$ \|<br><br>Hanya satu catatan yang mengandung kekeliruan, yaitu pada satu lemparan saja. Pernyataan yang benar adalah ....

| Opsi | Isi |
|---|---|
| A | Catatan Tiara keliru pada lemparan ke-4; seharusnya $\frac{1}{4}$ |
| B | Catatan Bagas keliru pada lemparan ke-5; seharusnya $\frac{2}{5}$ |
| C | Catatan Bagas keliru pada lemparan ke-4; seharusnya $\frac{1}{2}$ |
| D | Catatan Tiara keliru pada lemparan ke-6; seharusnya $\frac{1}{3}$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8719353c1c694eca893f62650ec1338e45af87cccfaba0faa21a75c47099e7dd`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Tiara dan Bagas mengundi sebuah koin 6 kali. Setelah tiap lemparan, keduanya mencatat frekuensi relatif munculnya angka (A). G menyatakan gambar.

| Lemparan ke- | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Hasil | A | G | G | A | A | G |
| Catatan Tiara | $1$ | $\frac{1}{2}$ | $\frac{1}{3}$ | $\frac{1}{2}$ | $\frac{3}{5}$ | $\frac{1}{2}$ |
| Catatan Bagas | $1$ | $\frac{1}{2}$ | $\frac{1}{3}$ | $\frac{1}{4}$ | $\frac{3}{5}$ | $\frac{1}{2}$ |

Hanya satu catatan yang mengandung kekeliruan, yaitu pada satu lemparan saja. Pernyataan yang benar adalah ....
Pilihan: A. Catatan Tiara keliru pada lemparan ke-4; seharusnya $\frac{1}{4}$
B. Catatan Bagas keliru pada lemparan ke-5; seharusnya $\frac{2}{5}$
C. Catatan Bagas keliru pada lemparan ke-4; seharusnya $\frac{1}{2}$
D. Catatan Tiara keliru pada lemparan ke-6; seharusnya $\frac{1}{3}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 152. Soal `3124735492739094aae66b70`

Dina melempar sebuah dadu seimbang 12 kali dan mata 6 muncul 3 kali. Ia menyimpulkan, "Frekuensi relatif mata 6 adalah $\frac{3}{12}=\frac{1}{4}$. Karena frekuensi relatif sama dengan peluang teoretis, peluang teoretis mata 6 adalah $\frac{1}{4}$."<br><br>Penilaian yang paling tepat terhadap kesimpulan Dina adalah ....

| Opsi | Isi |
|---|---|
| A | Benar, karena frekuensi relatif dihitung dari lemparan yang benar-benar terjadi |
| B | Salah, karena peluang teoretis mata 6 pada dadu seimbang adalah $\frac{1}{6}$, sedangkan $\frac{1}{4}$ hanya hasil dari 12 lemparan |
| C | Salah, karena peluang teoretis mata 6 pada dadu seimbang adalah $\frac{3}{6}=\frac{1}{2}$ |
| D | Benar, karena 12 lemparan sudah cukup untuk membuat keduanya sama persis |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menyimpulkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e59349ac56354e5d35c4252ee7fba90707d405fd5d5152214c7d9033d31a198e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Dina melempar sebuah dadu seimbang 12 kali dan mata 6 muncul 3 kali. Ia menyimpulkan, "Frekuensi relatif mata 6 adalah $\frac{3}{12}=\frac{1}{4}$. Karena frekuensi relatif sama dengan peluang teoretis, peluang teoretis mata 6 adalah $\frac{1}{4}$."

Penilaian yang paling tepat terhadap kesimpulan Dina adalah ....
Pilihan: A. Benar, karena frekuensi relatif dihitung dari lemparan yang benar-benar terjadi
B. Salah, karena peluang teoretis mata 6 pada dadu seimbang adalah $\frac{1}{6}$, sedangkan $\frac{1}{4}$ hanya hasil dari 12 lemparan
C. Salah, karena peluang teoretis mata 6 pada dadu seimbang adalah $\frac{3}{6}=\frac{1}{2}$
D. Benar, karena 12 lemparan sudah cukup untuk membuat keduanya sama persis
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 153. Soal `04a181ca4a960d926cf24b19`

Dua dadu bernomor 1–6 diuji untuk melihat apakah mata 6 muncul secara seimbang. Dadu P dilempar 1.200 kali dan mata 6 muncul 202 kali. Dadu Q dilempar 10 kali dan mata 6 muncul 4 kali.<br><br>Kesimpulan yang paling tepat adalah ....

| Opsi | Isi |
|---|---|
| A | dadu P tidak seimbang karena 202 tidak sama dengan 200 kali yang diharapkan |
| B | dadu Q pasti tidak seimbang karena frekuensi relatifnya $0{,}4$ jauh dari $\frac{1}{6}$ |
| C | kedua dadu seimbang karena setiap lemparan dadu bersifat acak |
| D | data dadu P sesuai dengan dadu seimbang, sedangkan data dadu Q belum cukup untuk menyimpulkan apa pun karena lemparannya terlalu sedikit |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menyimpulkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2142c87e73202f704d6ea0581e3bf74ac6c1e30ee9d659d7f5489f9f8c3d9447`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Dua dadu bernomor 1–6 diuji untuk melihat apakah mata 6 muncul secara seimbang. Dadu P dilempar 1.200 kali dan mata 6 muncul 202 kali. Dadu Q dilempar 10 kali dan mata 6 muncul 4 kali.

Kesimpulan yang paling tepat adalah ....
Pilihan: A. dadu P tidak seimbang karena 202 tidak sama dengan 200 kali yang diharapkan
B. dadu Q pasti tidak seimbang karena frekuensi relatifnya $0{,}4$ jauh dari $\frac{1}{6}$
C. kedua dadu seimbang karena setiap lemparan dadu bersifat acak
D. data dadu P sesuai dengan dadu seimbang, sedangkan data dadu Q belum cukup untuk menyimpulkan apa pun karena lemparannya terlalu sedikit
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 154. Soal `e0153a850c371575a35e8c33`

Sebuah pabrik menguji dadu dengan melemparnya 1.200 kali.<br><br>\| Mata dadu \| 1 \| 2 \| 3 \| 4 \| 5 \| 6 \|<br>\|---\|---\|---\|---\|---\|---\|---\|<br>\| Frekuensi \| 190 \| 215 \| 196 \| 178 \| 230 \| 191 \|<br><br>Dadu dinyatakan lolos uji jika untuk setiap mata dadu, selisih frekuensi relatifnya dengan peluang teoretis $\frac{1}{6}$ tidak lebih dari $0{,}02$.<br><br>Kesimpulan yang tepat berdasarkan kriteria tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | dadu lolos, karena semua mata memiliki selisih tidak lebih dari $0{,}02$ |
| B | dadu tidak lolos, karena mata 4 dan mata 5 selisihnya melebihi $0{,}02$ |
| C | dadu tidak lolos, karena hanya mata 5 yang selisihnya melebihi $0{,}02$ |
| D | dadu tidak lolos, karena mata 2 dan mata 5 selisihnya melebihi $0{,}02$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menyimpulkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b3dbab8b16ceada84209cf2e13068bc36fc2cb9a0b0bc223a0107734898a8d19`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah pabrik menguji dadu dengan melemparnya 1.200 kali.

| Mata dadu | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Frekuensi | 190 | 215 | 196 | 178 | 230 | 191 |

Dadu dinyatakan lolos uji jika untuk setiap mata dadu, selisih frekuensi relatifnya dengan peluang teoretis $\frac{1}{6}$ tidak lebih dari $0{,}02$.

Kesimpulan yang tepat berdasarkan kriteria tersebut adalah ....
Pilihan: A. dadu lolos, karena semua mata memiliki selisih tidak lebih dari $0{,}02$
B. dadu tidak lolos, karena mata 4 dan mata 5 selisihnya melebihi $0{,}02$
C. dadu tidak lolos, karena hanya mata 5 yang selisihnya melebihi $0{,}02$
D. dadu tidak lolos, karena mata 2 dan mata 5 selisihnya melebihi $0{,}02$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 155. Soal `634e203301b2d218180598fa`

Sebuah kantong tertutup berisi 40 kelereng merah dan putih. Banyak kelereng merah tidak diketahui. Ani ingin menduga banyak kelereng merah tanpa membuka kantong.<br><br>Rancangan percobaan yang paling dapat dipercaya untuk menduga banyak kelereng merah adalah ....

| Opsi | Isi |
|---|---|
| A | mengambil 10 kelereng sekaligus satu kali tanpa pengembalian, lalu menganggap perbandingan merah dan putih sama dengan isi kantong |
| B | mengambil satu kelereng secara acak sebanyak 300 kali dengan pengembalian, mencatat hanya saat merah terambil, lalu mengalikan banyak catatan dengan 40 |
| C | mengambil satu kelereng secara acak, mencatat warnanya, mengembalikannya, mengocok kantong, mengulang sampai ratusan kali, lalu mengalikan frekuensi relatif merah dengan 40 |
| D | mengambil satu kelereng yang paling mudah terjangkau, mencatat warnanya, mengembalikannya, mengulang sampai ratusan kali, lalu mengalikan frekuensi relatif merah dengan 40 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `06afe65ce44949fe06fc60fcba3e750c060eb0096ac921dab8dc777e09c637f0`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kantong tertutup berisi 40 kelereng merah dan putih. Banyak kelereng merah tidak diketahui. Ani ingin menduga banyak kelereng merah tanpa membuka kantong.

Rancangan percobaan yang paling dapat dipercaya untuk menduga banyak kelereng merah adalah ....
Pilihan: A. mengambil 10 kelereng sekaligus satu kali tanpa pengembalian, lalu menganggap perbandingan merah dan putih sama dengan isi kantong
B. mengambil satu kelereng secara acak sebanyak 300 kali dengan pengembalian, mencatat hanya saat merah terambil, lalu mengalikan banyak catatan dengan 40
C. mengambil satu kelereng secara acak, mencatat warnanya, mengembalikannya, mengocok kantong, mengulang sampai ratusan kali, lalu mengalikan frekuensi relatif merah dengan 40
D. mengambil satu kelereng yang paling mudah terjangkau, mencatat warnanya, mengembalikannya, mengulang sampai ratusan kali, lalu mengalikan frekuensi relatif merah dengan 40
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 156. Soal `9897392c04a035c4abc27100`

Sebuah roda bernomor 1–6 diputar 100 kali dengan hasil berikut.<br><br>\| Nomor \| 1 \| 2 \| 3 \| 4 \| 5 \| 6 \|<br>\|---\|---\|---\|---\|---\|---\|---\|<br>\| Frekuensi \| 23 \| 14 \| 31 \| 9 \| 12 \| 11 \|<br><br>Rani menentukan frekuensi relatif jarum menunjuk bilangan genap atau bilangan lebih dari 4.<br><br>Langkah 1: bilangan genap (2, 4, 6) muncul $14+9+11=34$ kali.<br><br>Langkah 2: bilangan lebih dari 4 (5, 6) muncul $12+11=23$ kali.<br><br>Langkah 3: kejadian genap atau lebih dari 4 muncul $34+23=57$ kali.<br><br>Langkah 4: frekuensi relatifnya $\frac{57}{100}$.<br><br>Pernyataan yang benar tentang penyelesaian Rani adalah ....

| Opsi | Isi |
|---|---|
| A | langkah 3 keliru karena nomor 6 terhitung dua kali; frekuensi relatif yang benar $\frac{34}{100}$ |
| B | langkah 2 keliru karena nomor 5 tidak termasuk lebih dari 4; frekuensi relatif yang benar $\frac{45}{100}$ |
| C | langkah 3 keliru karena nomor 6 terhitung dua kali; frekuensi relatif yang benar $\frac{46}{100}$ |
| D | tidak ada langkah yang keliru; frekuensi relatif yang benar $\frac{57}{100}$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `072438871ad51a2f8f4d431d9ac6c9541edb26309cafba0b69dd0a3ad7bbff73`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah roda bernomor 1–6 diputar 100 kali dengan hasil berikut.

| Nomor | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Frekuensi | 23 | 14 | 31 | 9 | 12 | 11 |

Rani menentukan frekuensi relatif jarum menunjuk bilangan genap atau bilangan lebih dari 4.

Langkah 1: bilangan genap (2, 4, 6) muncul $14+9+11=34$ kali.

Langkah 2: bilangan lebih dari 4 (5, 6) muncul $12+11=23$ kali.

Langkah 3: kejadian genap atau lebih dari 4 muncul $34+23=57$ kali.

Langkah 4: frekuensi relatifnya $\frac{57}{100}$.

Pernyataan yang benar tentang penyelesaian Rani adalah ....
Pilihan: A. langkah 3 keliru karena nomor 6 terhitung dua kali; frekuensi relatif yang benar $\frac{34}{100}$
B. langkah 2 keliru karena nomor 5 tidak termasuk lebih dari 4; frekuensi relatif yang benar $\frac{45}{100}$
C. langkah 3 keliru karena nomor 6 terhitung dua kali; frekuensi relatif yang benar $\frac{46}{100}$
D. tidak ada langkah yang keliru; frekuensi relatif yang benar $\frac{57}{100}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 157. Soal `11502084a148fc03a018bc20`

Setelah 25 lemparan sebuah koin, angka muncul 10 kali. Misalkan pada lemparan-lemparan berikutnya koin selalu menunjukkan angka.<br><br>Banyak lemparan tambahan paling sedikit agar frekuensi relatif munculnya angka mencapai paling sedikit $0{,}6$ adalah ....

| Opsi | Isi |
|---|---|
| A | 13 lemparan |
| B | 15 lemparan |
| C | 12 lemparan |
| D | 5 lemparan |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `815c719feed441b8f80313b228d71adb999d19b17cd811872f4b7bc6c9126e53`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Setelah 25 lemparan sebuah koin, angka muncul 10 kali. Misalkan pada lemparan-lemparan berikutnya koin selalu menunjukkan angka.

Banyak lemparan tambahan paling sedikit agar frekuensi relatif munculnya angka mencapai paling sedikit $0{,}6$ adalah ....
Pilihan: A. 13 lemparan
B. 15 lemparan
C. 12 lemparan
D. 5 lemparan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 158. Soal `7b2e3005f307e105c0eebde2`

Dalam suatu eksperimen, kejadian $P$ memiliki frekuensi relatif tepat $0{,}35$ dan kejadian $Q$ memiliki frekuensi relatif tepat $0{,}24$. Kedua frekuensi relatif itu dihitung dari total percobaan yang sama.<br><br>Banyak percobaan paling sedikit yang memungkinkan hal tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | 50 percobaan |
| B | 100 percobaan |
| C | 20 percobaan |
| D | 25 percobaan |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0a216b355b6929ce43dd691c1c50f448e36de5662712352f648a5820f293efee`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Dalam suatu eksperimen, kejadian $P$ memiliki frekuensi relatif tepat $0{,}35$ dan kejadian $Q$ memiliki frekuensi relatif tepat $0{,}24$. Kedua frekuensi relatif itu dihitung dari total percobaan yang sama.

Banyak percobaan paling sedikit yang memungkinkan hal tersebut adalah ....
Pilihan: A. 50 percobaan
B. 100 percobaan
C. 20 percobaan
D. 25 percobaan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 159. Soal `def9ad85b5e2ebb2154cd3e2`

Tiga kotak masing-masing berisi 20 bola merah atau putih. Kotak I berisi 4 bola merah, kotak II berisi 9 bola merah, dan kotak III berisi 15 bola merah. Salah satu kotak dipilih tanpa diketahui siapa pun. Dari kotak itu diambil satu bola secara acak dengan pengembalian sebanyak 600 kali, dan bola merah terambil 273 kali.<br><br>Kesimpulan yang paling tepat adalah ....

| Opsi | Isi |
|---|---|
| A | kotak yang dipilih kemungkinan besar kotak II, karena frekuensi relatif $0{,}455$ paling dekat dengan peluang teoretis $\frac{9}{20}=0{,}45$ |
| B | kotak yang dipilih kemungkinan besar kotak I, karena paling sedikit bola merahnya |
| C | kotak yang dipilih tidak dapat ditentukan, karena 273 tidak sama persis dengan $\frac{9}{20}\cdot600=270$ |
| D | kotak yang dipilih kemungkinan besar kotak III, karena bola merahnya paling banyak sehingga paling sering terambil |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menyimpulkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `470e22ff3a559278386cda2f1f5661e6f502c17a1c1f74244b272a734bd74d79`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Tiga kotak masing-masing berisi 20 bola merah atau putih. Kotak I berisi 4 bola merah, kotak II berisi 9 bola merah, dan kotak III berisi 15 bola merah. Salah satu kotak dipilih tanpa diketahui siapa pun. Dari kotak itu diambil satu bola secara acak dengan pengembalian sebanyak 600 kali, dan bola merah terambil 273 kali.

Kesimpulan yang paling tepat adalah ....
Pilihan: A. kotak yang dipilih kemungkinan besar kotak II, karena frekuensi relatif $0{,}455$ paling dekat dengan peluang teoretis $\frac{9}{20}=0{,}45$
B. kotak yang dipilih kemungkinan besar kotak I, karena paling sedikit bola merahnya
C. kotak yang dipilih tidak dapat ditentukan, karena 273 tidak sama persis dengan $\frac{9}{20}\cdot600=270$
D. kotak yang dipilih kemungkinan besar kotak III, karena bola merahnya paling banyak sehingga paling sering terambil
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 160. Soal `87b1e2536860ad519d07ffa9`

Peluang teoretis suatu kejadian adalah $\frac{1}{4}$. Frekuensi relatif kejadian itu dicatat pada beberapa banyak percobaan.<br><br>\| Banyak percobaan \| 50 \| 100 \| 200 \| 400 \| 800 \| 1600 \|<br>\|---\|---\|---\|---\|---\|---\|---\|<br>\| Frekuensi relatif \| 0,3 \| 0,27 \| 0,255 \| 0,2525 \| 0,2505 \| 0,2502 \|<br><br>Eksperimen dihentikan pada pencatatan pertama yang selisih frekuensi relatifnya dengan peluang teoretis kurang dari $0{,}003$.<br><br>Eksperimen tersebut dihentikan pada banyak percobaan ....

| Opsi | Isi |
|---|---|
| A | 1600 |
| B | 800 |
| C | 200 |
| D | 400 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `46ad7070a6a4c569f2bed3c3d2c51e0e2da112f6b8a9f690685b6f0b13798455`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Peluang teoretis suatu kejadian adalah $\frac{1}{4}$. Frekuensi relatif kejadian itu dicatat pada beberapa banyak percobaan.

| Banyak percobaan | 50 | 100 | 200 | 400 | 800 | 1600 |
|---|---|---|---|---|---|---|
| Frekuensi relatif | 0,3 | 0,27 | 0,255 | 0,2525 | 0,2505 | 0,2502 |

Eksperimen dihentikan pada pencatatan pertama yang selisih frekuensi relatifnya dengan peluang teoretis kurang dari $0{,}003$.

Eksperimen tersebut dihentikan pada banyak percobaan ....
Pilihan: A. 1600
B. 800
C. 200
D. 400
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 161. Soal `c5697abf461c0e764a010390`

Seorang pemain basket melakukan tembakan bebas. Setelah 12 tembakan, frekuensi relatif tembakan yang masuk adalah $0{,}75$. Setelah 20 tembakan, frekuensi relatif tembakan yang masuk adalah $0{,}6$.<br><br>Frekuensi relatif tembakan yang masuk pada tembakan ke-13 sampai ke-20, dinyatakan dalam persen, adalah ....

| Opsi | Isi |
|---|---|
| A | $37{,}5\%$ |
| B | $15\%$ |
| C | $25\%$ |
| D | $67{,}5\%$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6c7b397912a40b5ea8a32e97699a0794591dfa05f217dc61ad8e3b25881d7d28`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Seorang pemain basket melakukan tembakan bebas. Setelah 12 tembakan, frekuensi relatif tembakan yang masuk adalah $0{,}75$. Setelah 20 tembakan, frekuensi relatif tembakan yang masuk adalah $0{,}6$.

Frekuensi relatif tembakan yang masuk pada tembakan ke-13 sampai ke-20, dinyatakan dalam persen, adalah ....
Pilihan: A. $37{,}5\%$
B. $15\%$
C. $25\%$
D. $67{,}5\%$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 162. Soal `2b16c57f6efbdd85738ecd2e`

Sebuah roda putar terbagi menjadi 4 juring sama besar berwarna merah, biru, hijau, dan kuning. Roda diputar 200 kali dengan hasil berikut.<br><br>\| Warna \| Merah \| Biru \| Hijau \| Kuning \|<br>\|---\|---\|---\|---\|---\|<br>\| Frekuensi \| 44 \| 58 \| 52 \| 46 \|<br><br>Pernyataan yang benar adalah ....

| Opsi | Isi |
|---|---|
| A | frekuensi relatif biru melebihi peluang teoretisnya sebesar $0{,}04$ |
| B | jumlah frekuensi relatif merah dan hijau sama dengan $0{,}50$ |
| C | warna merah dan kuning memiliki frekuensi relatif yang sama |
| D | warna hijau memiliki frekuensi relatif yang paling jauh dari peluang teoretisnya |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6c02b7045495338bf0d2479e8627710093fa656db2507a2d2f4cfab4f7d332c9`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah roda putar terbagi menjadi 4 juring sama besar berwarna merah, biru, hijau, dan kuning. Roda diputar 200 kali dengan hasil berikut.

| Warna | Merah | Biru | Hijau | Kuning |
|---|---|---|---|---|
| Frekuensi | 44 | 58 | 52 | 46 |

Pernyataan yang benar adalah ....
Pilihan: A. frekuensi relatif biru melebihi peluang teoretisnya sebesar $0{,}04$
B. jumlah frekuensi relatif merah dan hijau sama dengan $0{,}50$
C. warna merah dan kuning memiliki frekuensi relatif yang sama
D. warna hijau memiliki frekuensi relatif yang paling jauh dari peluang teoretisnya
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 163. Soal `dc99f06bf016bfab9e548d0b`

Sebuah dadu seimbang dilempar 120 kali.<br><br>\| Mata dadu \| 1 \| 2 \| 3 \| 4 \| 5 \| 6 \|<br>\|---\|---\|---\|---\|---\|---\|---\|<br>\| Frekuensi \| 15 \| 25 \| 18 \| 22 \| 12 \| 28 \|<br><br>Kejadian yang frekuensi relatifnya paling jauh dari peluang teoretisnya adalah ....

| Opsi | Isi |
|---|---|
| A | diperoleh mata dadu prima |
| B | diperoleh mata dadu ganjil |
| C | diperoleh mata dadu kelipatan 3 |
| D | diperoleh mata dadu kurang dari 3 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fbbd75296b62a2f2ed99c24fd5fdae72b424b0e66b5bc89be870111a9eba45ae`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah dadu seimbang dilempar 120 kali.

| Mata dadu | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Frekuensi | 15 | 25 | 18 | 22 | 12 | 28 |

Kejadian yang frekuensi relatifnya paling jauh dari peluang teoretisnya adalah ....
Pilihan: A. diperoleh mata dadu prima
B. diperoleh mata dadu ganjil
C. diperoleh mata dadu kelipatan 3
D. diperoleh mata dadu kurang dari 3
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 164. Soal `0335fb3087fc0be476679a99`

Sebuah roda bernomor 1–4 diputar 200 kali. Jarum menunjuk nomor 4 dengan frekuensi relatif $0{,}25$ dan menunjuk nomor 3 sebanyak 30 kali. Jarum menunjuk nomor 1 dan nomor 2 sama banyak.<br><br>Frekuensi relatif jarum menunjuk nomor 1 atau nomor 3, dinyatakan dalam persen, adalah ....

| Opsi | Isi |
|---|---|
| A | $15\%$ |
| B | $60\%$ |
| C | $30\%$ |
| D | $45\%$ |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Total putaran = 200. Frekuensi nomor 4 = 0,25 * 200 = 50. Frekuensi nomor 3 = 30. Sisa putaran untuk nomor 1 dan 2 = 200 - 50 - 30 = 120. Karena frekuensi 1 = 2, maka frekuensi 1 = 120 / 2 = 60. Frekuensi (1 atau 3) = 60 + 30 = 90. Frekuensi relatif = 90 / 200 = 0,45 atau 45%.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `75a612c7ca0f7b767e41cc1451a1c235f7b5518b43a874e0af67bcb30b287727`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2930 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2963 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2929 |

Run 1 — solusi: Total putaran = 200. Frekuensi nomor 4 = 0,25 * 200 = 50. Frekuensi nomor 3 = 30. Sisa putaran untuk nomor 1 dan 2 = 200 - 50 - 30 = 120. Karena frekuensi 1 = 2, maka frekuensi 1 = 120 / 2 = 60. Frekuensi (1 atau 3) = 60 + 30 = 90. Frekuensi relatif = 90 / 200 = 0,45 atau 45%.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan informasi frekuensi relatif dan frekuensi absolut untuk menentukan frekuensi kejadian yang tidak diketahui, lalu menggabungkan dua kejadian (1 atau 3) untuk mendapatkan frekuensi relatif gabungan.. Bukti: Jarum menunjuk nomor 4 dengan frekuensi relatif 0,25; menunjuk nomor 3 sebanyak 30 kali; Jarum menunjuk nomor 1 dan nomor 2 sama banyak; Frekuensi relatif jarum menunjuk nomor 1 atau nomor 3
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang frekuensi relatif dan prosedur perhitungan frekuensi kejadian majemuk.. Bukti: frekuensi relatif 0,25; Frekuensi relatif jarum menunjuk nomor 1 atau nomor 3
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah saling terkait (menghitung frekuensi nomor 4, mencari sisa putaran, membagi sisa untuk nomor 1 dan 2, lalu menjumlahkan frekuensi 1 dan 3). Siswa harus merencanakan langkah-langkah ini secara berurutan.. Bukti: Jarum menunjuk nomor 4 dengan frekuensi relatif 0,25; menunjuk nomor 3 sebanyak 30 kali; Jarum menunjuk nomor 1 dan nomor 2 sama banyak

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar frekuensi relatif dan operasi aritmetika dasar. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 9 diharapkan mampu mengelola beberapa langkah perhitungan frekuensi relatif yang saling bergantung dalam konteks data empiris. |

Run 2 — solusi: Total putaran = 200. Frekuensi nomor 4 = 0,25 * 200 = 50. Frekuensi nomor 3 = 30. Sisa putaran untuk nomor 1 dan 2 = 200 - 50 - 30 = 120. Karena frekuensi 1 = 2, maka frekuensi nomor 1 = 120 / 2 = 60. Frekuensi relatif (1 atau 3) = (60 + 30) / 200 = 90 / 200 = 0,45 atau 45%.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep frekuensi relatif dan peluang empiris untuk memecahkan masalah yang melibatkan beberapa langkah logis (menghitung frekuensi masing-masing angka berdasarkan informasi parsial yang diberikan). Ini adalah penerapan konsep pada konteks rutin.. Bukti: Jarum menunjuk nomor 4 dengan frekuensi relatif 0,25 dan menunjuk nomor 3 sebanyak 30 kali.; Jarum menunjuk nomor 1 dan nomor 2 sama banyak.; Frekuensi relatif jarum menunjuk nomor 1 atau nomor 3, dinyatakan dalam persen, adalah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara frekuensi relatif, jumlah kejadian, dan prinsip penjumlahan peluang untuk kejadian yang saling lepas.. Bukti: frekuensi relatif; nomor 1 atau nomor 3
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah (menghitung frekuensi 4, mencari sisa, membagi sisa untuk 1 dan 2, lalu menjumlahkan frekuensi 1 dan 3). Meskipun prosedurnya familiar, siswa harus mengintegrasikan beberapa informasi yang saling bergantung. Tingkat kesulitan ini sesuai untuk kelas 9.. Bukti: Jarum menunjuk nomor 4 dengan frekuensi relatif 0,25; Jarum menunjuk nomor 1 dan nomor 2 sama banyak; Frekuensi relatif jarum menunjuk nomor 1 atau nomor 3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar frekuensi relatif dan operasi aritmetika dasar. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Tingkat kesulitan Medium karena siswa harus mengelola beberapa langkah perhitungan yang saling terkait (menentukan frekuensi 4, lalu sisa, lalu membagi sisa, lalu menjumlahkan) tanpa bantuan langkah per langkah. |

Run 3 — solusi: Frekuensi nomor 4 = 0,25 * 200 = 50. Frekuensi nomor 3 = 30. Sisa putaran untuk nomor 1 dan 2 = 200 - 50 - 30 = 120. Karena frekuensi 1 = 2, maka frekuensi 1 = 120 / 2 = 60. Frekuensi (1 atau 3) = 60 + 30 = 90. Frekuensi relatif = 90 / 200 = 0,45 atau 45%.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan informasi frekuensi relatif dan frekuensi absolut, serta menggunakan hubungan logis (sisa putaran dibagi dua) untuk menentukan frekuensi kejadian yang tidak diketahui sebelum menghitung peluang gabungan.. Bukti: Jarum menunjuk nomor 4 dengan frekuensi relatif 0,25; menunjuk nomor 3 sebanyak 30 kali; Jarum menunjuk nomor 1 dan nomor 2 sama banyak; Frekuensi relatif jarum menunjuk nomor 1 atau nomor 3
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman konseptual tentang frekuensi relatif dan bagaimana menggunakannya dalam konteks data empiris untuk menyelesaikan masalah yang melibatkan beberapa langkah.. Bukti: frekuensi relatif 0,25; nomor 1 atau nomor 3
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah logis yang saling bergantung: menghitung frekuensi nomor 4, menentukan sisa putaran, membagi sisa tersebut untuk nomor 1 dan 2, lalu menjumlahkan frekuensi 1 dan 3. Meskipun prosedurnya familiar, integrasi informasi ini menuntut ketelitian.. Bukti: Jarum menunjuk nomor 4 dengan frekuensi relatif 0,25; menunjuk nomor 3 sebanyak 30 kali; Jarum menunjuk nomor 1 dan nomor 2 sama banyak

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar frekuensi relatif, operasi aritmetika dasar, dan pemecahan masalah sederhana dengan variabel yang tidak diketahui. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Soal ini sesuai untuk kelas 9 karena menuntut kemampuan mengolah data empiris secara bertahap, yang merupakan standar kompetensi statistik dasar. |

Histori retry: run 2 sebelumnya `failed` / `ValidationError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

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
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah roda bernomor 1–4 diputar 200 kali. Jarum menunjuk nomor 4 dengan frekuensi relatif $0{,}25$ dan menunjuk nomor 3 sebanyak 30 kali. Jarum menunjuk nomor 1 dan nomor 2 sama banyak.

Frekuensi relatif jarum menunjuk nomor 1 atau nomor 3, dinyatakan dalam persen, adalah ....
Pilihan: A. $15\%$
B. $60\%$
C. $30\%$
D. $45\%$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 165. Soal `6adb374f0dd2bd212e7503cb`

Empat kelompok masing-masing melempar sebuah koin seimbang berulang kali. Frekuensi relatif munculnya angka pada beberapa banyak lemparan tercatat sebagai berikut.<br><br>\| Kelompok \| 10 lemparan \| 100 lemparan \| 1000 lemparan \|<br>\|---\|---\|---\|---\|<br>\| P \| 0,70 \| 0,56 \| 0,512 \|<br>\| Q \| 0,30 \| 0,45 \| 0,489 \|<br>\| R \| 0,60 \| 0,53 \| 0,507 \|<br>\| S \| 0,40 \| 0,47 \| 0,496 \|<br><br>Kesimpulan yang paling tepat dari tabel tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | frekuensi relatif pada 10 lemparan lebih mendekati $\frac{1}{2}$ daripada pada 1000 lemparan |
| B | selisih terbesar antar-kelompok mengecil dari $0{,}40$ menjadi $0{,}023$ dan semua nilai mendekati peluang teoretis $\frac{1}{2}$ saat lemparan makin banyak |
| C | kelompok P paling mendekati peluang teoretis $\frac{1}{2}$ pada 1000 lemparan karena paling tinggi pada 10 lemparan |
| D | selisih terbesar antar-kelompok tetap sekitar $0{,}40$ pada setiap banyak lemparan, sehingga hasil tiap kelompok tidak berhubungan dengan $\frac{1}{2}$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menyimpulkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0f42c483eaf775159af3b0dc255f71a32550c862547d1b5172f5b70ab93f1e5e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Empat kelompok masing-masing melempar sebuah koin seimbang berulang kali. Frekuensi relatif munculnya angka pada beberapa banyak lemparan tercatat sebagai berikut.

| Kelompok | 10 lemparan | 100 lemparan | 1000 lemparan |
|---|---|---|---|
| P | 0,70 | 0,56 | 0,512 |
| Q | 0,30 | 0,45 | 0,489 |
| R | 0,60 | 0,53 | 0,507 |
| S | 0,40 | 0,47 | 0,496 |

Kesimpulan yang paling tepat dari tabel tersebut adalah ....
Pilihan: A. frekuensi relatif pada 10 lemparan lebih mendekati $\frac{1}{2}$ daripada pada 1000 lemparan
B. selisih terbesar antar-kelompok mengecil dari $0{,}40$ menjadi $0{,}023$ dan semua nilai mendekati peluang teoretis $\frac{1}{2}$ saat lemparan makin banyak
C. kelompok P paling mendekati peluang teoretis $\frac{1}{2}$ pada 1000 lemparan karena paling tinggi pada 10 lemparan
D. selisih terbesar antar-kelompok tetap sekitar $0{,}40$ pada setiap banyak lemparan, sehingga hasil tiap kelompok tidak berhubungan dengan $\frac{1}{2}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 166. Soal `93d3bc6b431849510d20dd0c`

Dalam sebuah kotak terdapat 30 kartu yang masing-masing bergambar kubus, limas, atau prisma. Sebanyak 120 anak bergiliran mengambil satu kartu secara acak dengan mata tertutup, lalu mengembalikannya. Hasilnya:<br><br>\| Gambar \| Kubus \| Limas \| Prisma \|<br>\|---\|---\|---\|---\|<br>\| Frekuensi \| 24 \| 36 \| 60 \|<br><br>Selisih perkiraan banyaknya kartu bergambar yang paling banyak dan yang paling sedikit di dalam kotak adalah ....

| Opsi | Isi |
|---|---|
| A | 36 kartu |
| B | 15 kartu |
| C | 21 kartu |
| D | 9 kartu |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `42a5e79d0c1acbebd41c84b0efbb63a14b0328a3639660b955ddf0b0c4f11329`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Dalam sebuah kotak terdapat 30 kartu yang masing-masing bergambar kubus, limas, atau prisma. Sebanyak 120 anak bergiliran mengambil satu kartu secara acak dengan mata tertutup, lalu mengembalikannya. Hasilnya:

| Gambar | Kubus | Limas | Prisma |
|---|---|---|---|
| Frekuensi | 24 | 36 | 60 |

Selisih perkiraan banyaknya kartu bergambar yang paling banyak dan yang paling sedikit di dalam kotak adalah ....
Pilihan: A. 36 kartu
B. 15 kartu
C. 21 kartu
D. 9 kartu
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 167. Soal `7d7fd799a51e24d42c40da0a`

Dua kelompok melempar koin yang sama. Kelompok I melempar 40 kali dan angka muncul 18 kali. Kelompok II melempar 60 kali dan angka muncul 33 kali.<br><br>Frekuensi relatif muncul angka dari gabungan kedua percobaan, dinyatakan dalam persen, adalah ....

| Opsi | Isi |
|---|---|
| A | $50\%$ |
| B | $51\%$ |
| C | $45\%$ |
| D | $55\%$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7dc8c0a83e66c4545b5c624227e6a16898b969acde71aab15cbe5e02fd45f609`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Dua kelompok melempar koin yang sama. Kelompok I melempar 40 kali dan angka muncul 18 kali. Kelompok II melempar 60 kali dan angka muncul 33 kali.

Frekuensi relatif muncul angka dari gabungan kedua percobaan, dinyatakan dalam persen, adalah ....
Pilihan: A. $50\%$
B. $51\%$
C. $45\%$
D. $55\%$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 168. Soal `6f79c8f19dc536c35e1cdf13`

Sebuah eksperimen acak diulang-ulang. Frekuensi relatif suatu kejadian pada beberapa banyak percobaan tercatat sebagai berikut.<br><br>\| Banyak percobaan \| 50 \| 100 \| 200 \| 400 \| 800 \|<br>\|---\|---\|---\|---\|---\|---\|<br>\| Frekuensi relatif \| 0,40 \| 0,36 \| 0,34 \| 0,335 \| 0,333 \|<br><br>Kejadian yang paling tepat memiliki frekuensi relatif seperti pada tabel jika percobaannya diulang terus-menerus adalah ....

| Opsi | Isi |
|---|---|
| A | dalam lempar undi sebuah dadu, diperoleh mata dadu bilangan prima |
| B | dalam pemilihan bilangan 1–4 secara acak, diperoleh bilangan lebih dari 1 |
| C | dalam lempar undi sebuah dadu, diperoleh mata dadu kelipatan 3 |
| D | dalam pelemparan dua koin, diperoleh dua sisi gambar |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f961cd8a8a43bf7aeda38185eaf91e53099e46464fbf6e11bc159ce3547885ef`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah eksperimen acak diulang-ulang. Frekuensi relatif suatu kejadian pada beberapa banyak percobaan tercatat sebagai berikut.

| Banyak percobaan | 50 | 100 | 200 | 400 | 800 |
|---|---|---|---|---|---|
| Frekuensi relatif | 0,40 | 0,36 | 0,34 | 0,335 | 0,333 |

Kejadian yang paling tepat memiliki frekuensi relatif seperti pada tabel jika percobaannya diulang terus-menerus adalah ....
Pilihan: A. dalam lempar undi sebuah dadu, diperoleh mata dadu bilangan prima
B. dalam pemilihan bilangan 1–4 secara acak, diperoleh bilangan lebih dari 1
C. dalam lempar undi sebuah dadu, diperoleh mata dadu kelipatan 3
D. dalam pelemparan dua koin, diperoleh dua sisi gambar
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 169. Soal `de1b6822bee8588fb9716362`

Sebuah program komputer menampilkan 20 bilangan 6–9 secara acak. Hasilnya sebagai berikut.<br><br>7, 9, 6, 9, 8, 9, 7, 9, 9, 6, 8, 9, 7, 9, 8, 9, 6, 9, 9, 7<br><br>Frekuensi relatif munculnya bilangan yang lebih dari 7, dinyatakan dalam persen, adalah ....

| Opsi | Isi |
|---|---|
| A | $35\%$ |
| B | $50\%$ |
| C | $85\%$ |
| D | $65\%$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `166b3f3e43b5b1450de868ad31a2373c08cab89e3d235a7ea15e5214ca452aed`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah program komputer menampilkan 20 bilangan 6–9 secara acak. Hasilnya sebagai berikut.

7, 9, 6, 9, 8, 9, 7, 9, 9, 6, 8, 9, 7, 9, 8, 9, 6, 9, 9, 7

Frekuensi relatif munculnya bilangan yang lebih dari 7, dinyatakan dalam persen, adalah ....
Pilihan: A. $35\%$
B. $50\%$
C. $85\%$
D. $65\%$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 170. Soal `7ae8a34686ae0965804998e0`

Sebuah kantong berisi bola merah dan bola biru. Diketahui terdapat 12 bola merah, tetapi banyak bola biru tidak diketahui. Dari 200 kali pengambilan satu bola secara acak dengan pengembalian, bola merah terambil 60 kali.<br><br>Perkiraan banyaknya seluruh bola di dalam kantong adalah ....

| Opsi | Isi |
|---|---|
| A | 4 bola |
| B | 72 bola |
| C | 40 bola |
| D | 28 bola |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c7e0af0db0fd94cee4e217b024a4fab25e08941ea4fe2145f6797d0fdea8b72a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kantong berisi bola merah dan bola biru. Diketahui terdapat 12 bola merah, tetapi banyak bola biru tidak diketahui. Dari 200 kali pengambilan satu bola secara acak dengan pengembalian, bola merah terambil 60 kali.

Perkiraan banyaknya seluruh bola di dalam kantong adalah ....
Pilihan: A. 4 bola
B. 72 bola
C. 40 bola
D. 28 bola
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 171. Soal `54e8f2863c9462e726e2ec28`

Dimas mengundi sebuah koin delapan kali dan mencatat sisi yang muncul secara berurutan (A = angka, G = gambar).<br><br>G, A, A, G, A, G, G, A<br><br>Frekuensi relatif muncul angka setelah lemparan ke-7 dan setelah lemparan ke-8 berturut-turut adalah ....

| Opsi | Isi |
|---|---|
| A | $\frac{3}{8}$ dan $\frac{1}{2}$ |
| B | $\frac{4}{7}$ dan $\frac{1}{2}$ |
| C | $\frac{3}{7}$ dan $\frac{3}{8}$ |
| D | $\frac{3}{7}$ dan $\frac{1}{2}$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `70eae86f2192c74fe23d2e9c3ae5c47f57b6beee2ace95423defe786db4e3af3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Dimas mengundi sebuah koin delapan kali dan mencatat sisi yang muncul secara berurutan (A = angka, G = gambar).

G, A, A, G, A, G, G, A

Frekuensi relatif muncul angka setelah lemparan ke-7 dan setelah lemparan ke-8 berturut-turut adalah ....
Pilihan: A. $\frac{3}{8}$ dan $\frac{1}{2}$
B. $\frac{4}{7}$ dan $\frac{1}{2}$
C. $\frac{3}{7}$ dan $\frac{3}{8}$
D. $\frac{3}{7}$ dan $\frac{1}{2}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 172. Soal `be7ee605a0f4ec0f7a7de318`

Sebuah roda putar berwarna merah, biru, hijau, dan kuning diputar 80 kali. Hasilnya:<br><br>\| Warna \| Merah \| Biru \| Hijau \| Kuning \|<br>\|---\|---\|---\|---\|---\|<br>\| Frekuensi \| 8 \| 30 \| 24 \| 18 \|<br><br>Selisih frekuensi relatif warna yang paling sering dan yang paling jarang ditunjuk jarum, dinyatakan dalam persen, adalah ....

| Opsi | Isi |
|---|---|
| A | $7{,}5\%$ |
| B | $22\%$ |
| C | $37{,}5\%$ |
| D | $27{,}5\%$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `348f9fd9099f4196995b9b1d3efd62074e86d698f3e8d29c6eaa61ed02c83cbb`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah roda putar berwarna merah, biru, hijau, dan kuning diputar 80 kali. Hasilnya:

| Warna | Merah | Biru | Hijau | Kuning |
|---|---|---|---|---|
| Frekuensi | 8 | 30 | 24 | 18 |

Selisih frekuensi relatif warna yang paling sering dan yang paling jarang ditunjuk jarum, dinyatakan dalam persen, adalah ....
Pilihan: A. $7{,}5\%$
B. $22\%$
C. $37{,}5\%$
D. $27{,}5\%$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 173. Soal `1741d26f57c3acf7c29377df`

Sebuah mesin undian mengeluarkan satu bola bernomor 1–6 secara acak, lalu bola dikembalikan. Setelah 60 kali pengundian, hasilnya:<br><br>\| Nomor \| 1 \| 2 \| 3 \| 4 \| 5 \| 6 \|<br>\|---\|---\|---\|---\|---\|---\|---\|<br>\| Frekuensi \| 8 \| 14 \| 6 \| 12 \| 9 \| 11 \|<br><br>Frekuensi relatif terambilnya bola bernomor bilangan prima adalah ....

| Opsi | Isi |
|---|---|
| A | $\frac{37}{60}$ |
| B | $\frac{29}{60}$ |
| C | $\frac{1}{2}$ |
| D | $\frac{1}{4}$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `25183613eddca0cbb95ab3bd036ea34020b2c97f61c96ae52e0e47a4cee517ff`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah mesin undian mengeluarkan satu bola bernomor 1–6 secara acak, lalu bola dikembalikan. Setelah 60 kali pengundian, hasilnya:

| Nomor | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Frekuensi | 8 | 14 | 6 | 12 | 9 | 11 |

Frekuensi relatif terambilnya bola bernomor bilangan prima adalah ....
Pilihan: A. $\frac{37}{60}$
B. $\frac{29}{60}$
C. $\frac{1}{2}$
D. $\frac{1}{4}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 174. Soal `0329e27f073c9fec704d5f36`

Empat siswa masing-masing melempar sebuah dadu 50 kali, lalu melaporkan banyaknya mata dadu genap yang muncul beserta frekuensi relatifnya. Hanya satu laporan yang tidak sesuai.<br><br>Laporan yang keliru adalah ....

| Opsi | Isi |
|---|---|
| A | muncul 24 kali dengan frekuensi relatif $0{,}44$ |
| B | muncul 15 kali dengan frekuensi relatif $0{,}30$ |
| C | muncul 25 kali dengan frekuensi relatif $0{,}50$ |
| D | muncul 31 kali dengan frekuensi relatif $0{,}62$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `97b82ae3223df6999860faa55112d19cee5f9dd747c09648805db245d7ef8181`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Empat siswa masing-masing melempar sebuah dadu 50 kali, lalu melaporkan banyaknya mata dadu genap yang muncul beserta frekuensi relatifnya. Hanya satu laporan yang tidak sesuai.

Laporan yang keliru adalah ....
Pilihan: A. muncul 24 kali dengan frekuensi relatif $0{,}44$
B. muncul 15 kali dengan frekuensi relatif $0{,}30$
C. muncul 25 kali dengan frekuensi relatif $0{,}50$
D. muncul 31 kali dengan frekuensi relatif $0{,}62$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 175. Soal `14e6dc6c5649ac8f9588fb57`

Sebuah tas berisi 20 bola berwarna merah, biru, putih, atau hijau. Dari 400 kali pengambilan satu bola secara acak dengan pengembalian, hasilnya:<br><br>\| Warna \| Merah \| Biru \| Putih \| Hijau \|<br>\|---\|---\|---\|---\|---\|<br>\| Frekuensi \| 80 \| 120 \| 140 \| 60 \|<br><br>Perkiraan banyaknya bola di dalam tas yang bukan berwarna putih adalah ....

| Opsi | Isi |
|---|---|
| A | 260 bola |
| B | 9 bola |
| C | 13 bola |
| D | 7 bola |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2a9d457354a4e7847247e275fbab02cf150bc2af8ab2daf3e4fd9d7bc2d57353`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah tas berisi 20 bola berwarna merah, biru, putih, atau hijau. Dari 400 kali pengambilan satu bola secara acak dengan pengembalian, hasilnya:

| Warna | Merah | Biru | Putih | Hijau |
|---|---|---|---|---|
| Frekuensi | 80 | 120 | 140 | 60 |

Perkiraan banyaknya bola di dalam tas yang bukan berwarna putih adalah ....
Pilihan: A. 260 bola
B. 9 bola
C. 13 bola
D. 7 bola
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 176. Soal `74de2beb6c90d73d11e197b8`

Sebuah roda putar terbagi menjadi 12 juring sama besar, masing-masing berwarna merah atau putih. Dua kali percobaan memutar roda dilakukan.<br><br>\| Percobaan \| Banyak putaran \| Menunjuk merah \|<br>\|---\|---\|---\|<br>\| I \| 10 \| 6 \|<br>\| II \| 200 \| 66 \|<br><br>Dugaan banyaknya juring merah yang paling dapat dipercaya adalah ....

| Opsi | Isi |
|---|---|
| A | 4 juring |
| B | 3 juring |
| C | 6 juring |
| D | 7 juring |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b94a2a1e3532a608e3c48ca4a886acdf9cd197c5c32b47395739cc5e8681a78d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah roda putar terbagi menjadi 12 juring sama besar, masing-masing berwarna merah atau putih. Dua kali percobaan memutar roda dilakukan.

| Percobaan | Banyak putaran | Menunjuk merah |
|---|---|---|
| I | 10 | 6 |
| II | 200 | 66 |

Dugaan banyaknya juring merah yang paling dapat dipercaya adalah ....
Pilihan: A. 4 juring
B. 3 juring
C. 6 juring
D. 7 juring
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 177. Soal `0bde0e2f4a363331df7f9987`

Dalam 200 kali pengambilan satu kartu dari seperangkat kartu, kartu bergambar bintang muncul dengan frekuensi relatif $0{,}35$.<br><br>Banyaknya pengambilan yang tidak menghasilkan kartu bergambar bintang adalah ....

| Opsi | Isi |
|---|---|
| A | 130 kali |
| B | 70 kali |
| C | 35 kali |
| D | 65 kali |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c07cef12e8e0b6cbc20d77166e82a16d1e5acd01182f6c52ee6120eea0b43775`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Dalam 200 kali pengambilan satu kartu dari seperangkat kartu, kartu bergambar bintang muncul dengan frekuensi relatif $0{,}35$.

Banyaknya pengambilan yang tidak menghasilkan kartu bergambar bintang adalah ....
Pilihan: A. 130 kali
B. 70 kali
C. 35 kali
D. 65 kali
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 178. Soal `849ae81a9aadfaabc1361409`

Tiga siswa mengambil satu kartu dari seperangkat kartu remi (52 kartu) secara acak dengan pengembalian. Banyaknya kartu hati yang terambil:<br><br>\| Siswa \| Banyak pengambilan \| Kartu hati \|<br>\|---\|---\|---\|<br>\| Ana \| 20 \| 8 \|<br>\| Budi \| 100 \| 29 \|<br>\| Cici \| 400 \| 98 \|<br><br>Siswa yang hasilnya paling baik dipakai untuk menduga peluang terambilnya kartu hati adalah ....

| Opsi | Isi |
|---|---|
| A | ketiganya sama baik, karena kartu diambil secara acak |
| B | Cici, karena pengambilannya paling banyak dan frekuensi relatifnya $0{,}245$ paling dekat dengan $\frac{13}{52}=\frac{1}{4}$ |
| C | Ana, karena frekuensi relatifnya $0{,}40$ paling tinggi sehingga paling meyakinkan |
| D | Budi, karena banyak pengambilannya berada di tengah antara Ana dan Cici |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5a384c7a904b0a7090779aee3ffac1b1590b964178125ff3d1d16d48374573fe`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Tiga siswa mengambil satu kartu dari seperangkat kartu remi (52 kartu) secara acak dengan pengembalian. Banyaknya kartu hati yang terambil:

| Siswa | Banyak pengambilan | Kartu hati |
|---|---|---|
| Ana | 20 | 8 |
| Budi | 100 | 29 |
| Cici | 400 | 98 |

Siswa yang hasilnya paling baik dipakai untuk menduga peluang terambilnya kartu hati adalah ....
Pilihan: A. ketiganya sama baik, karena kartu diambil secara acak
B. Cici, karena pengambilannya paling banyak dan frekuensi relatifnya $0{,}245$ paling dekat dengan $\frac{13}{52}=\frac{1}{4}$
C. Ana, karena frekuensi relatifnya $0{,}40$ paling tinggi sehingga paling meyakinkan
D. Budi, karena banyak pengambilannya berada di tengah antara Ana dan Cici
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 179. Soal `7a1d3032ffc056c72a23a626`

Dalam suatu eksperimen pengambilan kartu berwarna hijau, kuning, dan merah, kartu hijau terambil 18 kali dengan frekuensi relatif $0{,}36$. Kartu kuning terambil 14 kali.<br><br>Frekuensi relatif terambilnya kartu kuning, dinyatakan dalam persen, adalah ....

| Opsi | Isi |
|---|---|
| A | $43{,}75\%$ |
| B | $28\%$ |
| C | $14\%$ |
| D | $38{,}9\%$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `59c9ab281339e19b59d6a200926a78853c1f4b343b24151dfc2e4089de60280a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Dalam suatu eksperimen pengambilan kartu berwarna hijau, kuning, dan merah, kartu hijau terambil 18 kali dengan frekuensi relatif $0{,}36$. Kartu kuning terambil 14 kali.

Frekuensi relatif terambilnya kartu kuning, dinyatakan dalam persen, adalah ....
Pilihan: A. $43{,}75\%$
B. $28\%$
C. $14\%$
D. $38{,}9\%$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 180. Soal `dab788699961fa0279c0517c`

Sebuah dadu seimbang dilempar 600 kali dan mata dadu 6 muncul 96 kali.<br><br>Pernyataan yang paling tepat tentang hasil tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | mata dadu 6 harus muncul tepat 100 kali pada 600 lemparan |
| B | peluang teoretis mata dadu 6 adalah $0{,}16$ karena itu hasil percobaan |
| C | hasilnya wajar karena frekuensi relatif $0{,}16$ mendekati peluang teoretis $\frac{1}{6}$ |
| D | dadu pasti tidak seimbang karena $0{,}16$ tidak sama persis dengan $\frac{1}{6}$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ff69c47766ddf56ef365a33ffc32e1f79feda7f7263e27bf26ff292d55ba17fc`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Peluang Empiris
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah dadu seimbang dilempar 600 kali dan mata dadu 6 muncul 96 kali.

Pernyataan yang paling tepat tentang hasil tersebut adalah ....
Pilihan: A. mata dadu 6 harus muncul tepat 100 kali pada 600 lemparan
B. peluang teoretis mata dadu 6 adalah $0{,}16$ karena itu hasil percobaan
C. hasilnya wajar karena frekuensi relatif $0{,}16$ mendekati peluang teoretis $\frac{1}{6}$
D. dadu pasti tidak seimbang karena $0{,}16$ tidak sama persis dengan $\frac{1}{6}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 181. Soal `469de112640034c9f608ead9`

Dalam pengambilan satu kartu secara acak dari seperangkat kartu remi (kartu dikembalikan dan dikocok lagi setiap kali), dilakukan 80 kali pengambilan. Frekuensi harapan tidak didapatkan kartu wajik adalah ....

| Opsi | Isi |
|---|---|
| A | 60 |
| B | 67 |
| C | 39 |
| D | 20 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c05be6cb6aa56d064cdac9e304917e7daa60d9e6ead34fcdd4d875d851933446`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Dalam pengambilan satu kartu secara acak dari seperangkat kartu remi (kartu dikembalikan dan dikocok lagi setiap kali), dilakukan 80 kali pengambilan. Frekuensi harapan tidak didapatkan kartu wajik adalah ....
Pilihan: A. 60
B. 67
C. 39
D. 20
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 182. Soal `0bfef8fe246e7cca6754aca8`

Sebuah dadu dilempar undi sebanyak 180 kali. Frekuensi harapan tidak muncul mata dadu 6 adalah ....

| Opsi | Isi |
|---|---|
| A | 175 |
| B | 30 |
| C | 36 |
| D | 150 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1275657b6e77c415e9540130ec440fcc82c08bebd63c066eeb8f68141d275946`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah dadu dilempar undi sebanyak 180 kali. Frekuensi harapan tidak muncul mata dadu 6 adalah ....
Pilihan: A. 175
B. 30
C. 36
D. 150
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 183. Soal `18853c3ce8432b790c8236a5`

Di sebuah kota, persentase penduduknya yang menggunakan sepeda ke tempat kerja adalah 40%. Jika dipilih 60 penduduk kota itu secara acak, frekuensi harapan mendapatkan penduduk yang bersepeda adalah ....

| Opsi | Isi |
|---|---|
| A | 60 |
| B | 36 |
| C | 24 |
| D | 40 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7a5bcf3ee11281e1f0b8b0dfc6fcd766427dda5f3b341bb04b3fb53323355cc3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Di sebuah kota, persentase penduduknya yang menggunakan sepeda ke tempat kerja adalah 40%. Jika dipilih 60 penduduk kota itu secara acak, frekuensi harapan mendapatkan penduduk yang bersepeda adalah ....
Pilihan: A. 60
B. 36
C. 24
D. 40
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 184. Soal `b7d30afd3f453d8404db5c8b`

Di sebuah sekolah, 35% siswanya mengikuti ekstrakurikuler pramuka. Seorang guru memilih 80 siswa sekolah itu secara acak. Frekuensi harapan guru tersebut mendapatkan siswa anggota pramuka adalah ....

| Opsi | Isi |
|---|---|
| A | 28 |
| B | 52 |
| C | 35 |
| D | 80 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4de803688883564643e156d09f9644cdbf919154a7e8c44176dd2898c1dac2f1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Di sebuah sekolah, 35% siswanya mengikuti ekstrakurikuler pramuka. Seorang guru memilih 80 siswa sekolah itu secara acak. Frekuensi harapan guru tersebut mendapatkan siswa anggota pramuka adalah ....
Pilihan: A. 28
B. 52
C. 35
D. 80
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 185. Soal `8fcb5b07fdce7b633a1880bb`

Tentukan frekuensi harapan kejadian berikut jika dilakukan 160 kali percobaan. Dalam lempar undi tiga koin, diperoleh tiga sisi angka. Frekuensi harapannya adalah ....

| Opsi | Isi |
|---|---|
| A | 40 |
| B | 20 |
| C | 80 |
| D | 60 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1bd20860aaf755c0ceb7d3770dd8bbc8f21d88818bdf18ef015d2839a47a5d12`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan frekuensi harapan kejadian berikut jika dilakukan 160 kali percobaan. Dalam lempar undi tiga koin, diperoleh tiga sisi angka. Frekuensi harapannya adalah ....
Pilihan: A. 40
B. 20
C. 80
D. 60
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 186. Soal `c159e2d3744189a83e45cfe2`

Dua koin dilempar undi bersamaan sebanyak 200 kali. Frekuensi harapan kedua koin menunjukkan sisi gambar adalah ....

| Opsi | Isi |
|---|---|
| A | 25 |
| B | 100 |
| C | 50 |
| D | 150 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `82376b38ddbc88a0605c7592dd2bbdda3c53ed635ca86117dc05ff43e60a06a8`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Dua koin dilempar undi bersamaan sebanyak 200 kali. Frekuensi harapan kedua koin menunjukkan sisi gambar adalah ....
Pilihan: A. 25
B. 100
C. 50
D. 150
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 187. Soal `573ce1442a6c52096d194cab`

Sebuah dadu dilempar undi sebanyak 240 kali. Frekuensi harapan diperoleh mata dadu bilangan-bilangan yang kurang dari lima adalah ....

| Opsi | Isi |
|---|---|
| A | 80 |
| B | 160 |
| C | 120 |
| D | 200 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ee72b352f803a8f8acc07987091c15a4e554afff89ebcf3ef564b34c5473fe9a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah dadu dilempar undi sebanyak 240 kali. Frekuensi harapan diperoleh mata dadu bilangan-bilangan yang kurang dari lima adalah ....
Pilihan: A. 80
B. 160
C. 120
D. 200
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 188. Soal `71c04644c1ef83002d530a0a`

Sepuluh kartu diberi nomor 1 sampai 10, dikocok, lalu diambil satu kartu secara acak dan dikembalikan. Pengambilan dilakukan 200 kali. Frekuensi harapan terambil kartu bernomor lebih dari 7 adalah ....

| Opsi | Isi |
|---|---|
| A | 140 |
| B | 20 |
| C | 60 |
| D | 100 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8b944dc9817f4401b99002f404a726743727af8477c3a1ace35410a54875c77a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Sepuluh kartu diberi nomor 1 sampai 10, dikocok, lalu diambil satu kartu secara acak dan dikembalikan. Pengambilan dilakukan 200 kali. Frekuensi harapan terambil kartu bernomor lebih dari 7 adalah ....
Pilihan: A. 140
B. 20
C. 60
D. 100
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 189. Soal `da59cfc384d1637fc763e483`

Sebuah roda putar dibagi menjadi 8 juring yang ukurannya sama. Tiga juring berwarna biru dan sisanya berwarna lain.<br><br>Jika roda tersebut diputar sebanyak 200 kali, frekuensi harapan jarum menunjuk juring berwarna biru adalah ....

| Opsi | Isi |
|---|---|
| A | 25 |
| B | 120 |
| C | 75 |
| D | 600 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ac99406161692393ce552e0e1f91f395b44a2db30b1d214ddd8313fc1db5f3c6`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah roda putar dibagi menjadi 8 juring yang ukurannya sama. Tiga juring berwarna biru dan sisanya berwarna lain.

Jika roda tersebut diputar sebanyak 200 kali, frekuensi harapan jarum menunjuk juring berwarna biru adalah ....
Pilihan: A. 25
B. 120
C. 75
D. 600
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 190. Soal `55c5cedcb7e26c7f7733a4d5`

Pernyataan yang tepat mengenai frekuensi harapan suatu kejadian adalah ....

| Opsi | Isi |
|---|---|
| A | perbandingan banyak kejadian muncul dengan banyak percobaan yang sudah dilakukan |
| B | banyak kejadian itu yang benar-benar muncul pada percobaan yang sudah dilakukan |
| C | banyaknya semua hasil yang mungkin dalam satu percobaan |
| D | harapan berapa kali kejadian itu terjadi dalam beberapa kali percobaan |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fe897a84d32847ba15330a4488a8d3edd1eb6738c7294579d14472bbcc1a10b1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Pernyataan yang tepat mengenai frekuensi harapan suatu kejadian adalah ....
Pilihan: A. perbandingan banyak kejadian muncul dengan banyak percobaan yang sudah dilakukan
B. banyak kejadian itu yang benar-benar muncul pada percobaan yang sudah dilakukan
C. banyaknya semua hasil yang mungkin dalam satu percobaan
D. harapan berapa kali kejadian itu terjadi dalam beberapa kali percobaan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 191. Soal `d7995d5b28b86bb167c20799`

Peluang suatu kejadian adalah 0,3. Jika percobaan dilakukan 60 kali, frekuensi harapan kejadian tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | 60,3 |
| B | 59,7 |
| C | 200 |
| D | 18 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7bfbb374bfb7133521376aadf77f266c3f4190be6c784d0b3aa0639ba8f22600`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Peluang suatu kejadian adalah 0,3. Jika percobaan dilakukan 60 kali, frekuensi harapan kejadian tersebut adalah ....
Pilihan: A. 60,3
B. 59,7
C. 200
D. 18
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 192. Soal `874b1a709b0d0270eaafd77c`

Peluang munculnya sisi angka pada sebuah koin adalah $\frac{1}{2}$. Agar frekuensi harapan munculnya sisi angka 45 kali, koin harus dilempar sebanyak ....

| Opsi | Isi |
|---|---|
| A | 45 kali |
| B | 90 kali |
| C | 44,5 kali |
| D | 22,5 kali |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ef583e1f6eb5f05d3aebe9008a4774f643df017ba36bd8a469b6d607b14f0159`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Peluang munculnya sisi angka pada sebuah koin adalah $\frac{1}{2}$. Agar frekuensi harapan munculnya sisi angka 45 kali, koin harus dilempar sebanyak ....
Pilihan: A. 45 kali
B. 90 kali
C. 44,5 kali
D. 22,5 kali
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 193. Soal `b01432c79643817602ce61f3`

Frekuensi harapan suatu kejadian sama dengan banyaknya percobaan yang dilakukan jika kejadian tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | kejadian dengan peluang $\frac{1}{2}$ |
| B | kejadian yang pasti terjadi |
| C | kejadian yang mustahil terjadi |
| D | kejadian dengan peluang 0,9 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ee4cc3d70f7e43816d02b58fe2977ad43853fe7fb3426dc25bdfff19080e0bce`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Frekuensi harapan suatu kejadian sama dengan banyaknya percobaan yang dilakukan jika kejadian tersebut adalah ....
Pilihan: A. kejadian dengan peluang $\frac{1}{2}$
B. kejadian yang pasti terjadi
C. kejadian yang mustahil terjadi
D. kejadian dengan peluang 0,9
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 194. Soal `e14985446a8910cb2ec48457`

Peluang hujan pada suatu hari di sebuah kota adalah 0,2. Dalam 40 hari, frekuensi harapan terjadinya hujan adalah 8. Makna dari hasil tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | diharapkan hujan terjadi sekitar 8 hari dalam 40 hari |
| B | hujan terjadi setiap 8 hari sekali |
| C | hujan pasti terjadi pada 8 hari pertama dari 40 hari |
| D | hujan terjadi pada 32 hari dari 40 hari |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f7e6fc212dcfae5e63cd4c0ac6e347bb8cbae15c50403f0e8299dc686fc57b21`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Peluang hujan pada suatu hari di sebuah kota adalah 0,2. Dalam 40 hari, frekuensi harapan terjadinya hujan adalah 8. Makna dari hasil tersebut adalah ....
Pilihan: A. diharapkan hujan terjadi sekitar 8 hari dalam 40 hari
B. hujan terjadi setiap 8 hari sekali
C. hujan pasti terjadi pada 8 hari pertama dari 40 hari
D. hujan terjadi pada 32 hari dari 40 hari
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 195. Soal `7b8d67d1129d384bbc0a4d00`

Sebuah kotak berisi 4 bola merah dan 6 bola putih. Satu bola diambil secara acak, dicatat warnanya, lalu dikembalikan. Pengambilan dilakukan 50 kali. Frekuensi harapan terambil bola merah adalah ....

| Opsi | Isi |
|---|---|
| A | 30 |
| B | 33 |
| C | 12 |
| D | 20 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a8206e51f9446c7250d816c77a384cab611b6ab8668de7676d71f27a557d7536`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kotak berisi 4 bola merah dan 6 bola putih. Satu bola diambil secara acak, dicatat warnanya, lalu dikembalikan. Pengambilan dilakukan 50 kali. Frekuensi harapan terambil bola merah adalah ....
Pilihan: A. 30
B. 33
C. 12
D. 20
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 196. Soal `e0a7a2d02c26f93fcb96aad6`

Kiki menyatakan, "Frekuensi harapan suatu kejadian pasti kurang dari banyak percobaan." Untuk mengujinya, ia melempar sebuah dadu 90 kali dan memeriksa kejadian muncul mata dadu yang kurang dari 7. Penilaian yang tepat terhadap pernyataan Kiki adalah ....

| Opsi | Isi |
|---|---|
| A | pernyataan Kiki benar, karena frekuensi harapannya 15, kurang dari 90 |
| B | pernyataan Kiki salah, karena frekuensi harapannya 540, lebih dari 90 |
| C | pernyataan Kiki salah, karena frekuensi harapannya 90, sama dengan banyak lemparan |
| D | pernyataan Kiki benar, karena peluang kejadian itu kurang dari 1 sehingga frekuensi harapannya kurang dari 90 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3e4fec08a68733409b69ac967cbe5661861972d0cd1ab4b7f521496ab3d48352`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Kiki menyatakan, "Frekuensi harapan suatu kejadian pasti kurang dari banyak percobaan." Untuk mengujinya, ia melempar sebuah dadu 90 kali dan memeriksa kejadian muncul mata dadu yang kurang dari 7. Penilaian yang tepat terhadap pernyataan Kiki adalah ....
Pilihan: A. pernyataan Kiki benar, karena frekuensi harapannya 15, kurang dari 90
B. pernyataan Kiki salah, karena frekuensi harapannya 540, lebih dari 90
C. pernyataan Kiki salah, karena frekuensi harapannya 90, sama dengan banyak lemparan
D. pernyataan Kiki benar, karena peluang kejadian itu kurang dari 1 sehingga frekuensi harapannya kurang dari 90
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 197. Soal `895a963cebb0d4cc795d3066`

Sebuah bola diambil secara acak dari kotak berisi bola bernomor 1 sampai 40, dicatat nomornya, lalu dikembalikan. Pengambilan dilakukan 200 kali. Doni menghitung frekuensi harapan terambil bola yang nomornya bukan kelipatan 2 maupun bukan kelipatan 3 (tidak habis dibagi 2 dan tidak habis dibagi 3) dengan cara $40 - 20 - 13 = 7$ bola, lalu memakai peluang $\frac{7}{40}$. Selisih antara hitungan Doni dan frekuensi harapan yang benar adalah ....

| Opsi | Isi |
|---|---|
| A | 65 |
| B | 30 |
| C | 35 |
| D | 100 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `21d5d6c098c81237746e3e5afa14a136973bdc7955da9db38c608b5fd5992615`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah bola diambil secara acak dari kotak berisi bola bernomor 1 sampai 40, dicatat nomornya, lalu dikembalikan. Pengambilan dilakukan 200 kali. Doni menghitung frekuensi harapan terambil bola yang nomornya bukan kelipatan 2 maupun bukan kelipatan 3 (tidak habis dibagi 2 dan tidak habis dibagi 3) dengan cara $40 - 20 - 13 = 7$ bola, lalu memakai peluang $\frac{7}{40}$. Selisih antara hitungan Doni dan frekuensi harapan yang benar adalah ....
Pilihan: A. 65
B. 30
C. 35
D. 100
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 198. Soal `22972f2af6f7f36c47cfc5fc`

Sebuah gim serupa Gim Koin memakai lima kali lemparan koin untuk setiap pion. Pion berakhir di salah satu persegi A, B, C, D, E, atau F dengan banyak cara berikut. Semua cara memiliki peluang yang sama.<br><br>\| Persegi \| A \| B \| C \| D \| E \| F \|<br>\|---\|---\|---\|---\|---\|---\|---\|<br>\| Banyak cara \| 1 \| 5 \| 10 \| 10 \| 5 \| 1 \|<br><br>Dalam menjalankan 64 pionnya, selisih frekuensi harapan pion yang sampai ke persegi C atau D dengan frekuensi harapan pion yang sampai ke persegi A atau F adalah ....

| Opsi | Isi |
|---|---|
| A | 16 |
| B | 36 |
| C | 44 |
| D | 40 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `bbc61e265948cebfc03172ffe38905646808cfd57e8fc221aaa3b2ec481bfb6f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah gim serupa Gim Koin memakai lima kali lemparan koin untuk setiap pion. Pion berakhir di salah satu persegi A, B, C, D, E, atau F dengan banyak cara berikut. Semua cara memiliki peluang yang sama.

| Persegi | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| Banyak cara | 1 | 5 | 10 | 10 | 5 | 1 |

Dalam menjalankan 64 pionnya, selisih frekuensi harapan pion yang sampai ke persegi C atau D dengan frekuensi harapan pion yang sampai ke persegi A atau F adalah ....
Pilihan: A. 16
B. 36
C. 44
D. 40
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 199. Soal `64faa1c0076b9a133837b59a`

Sebuah pasar malam memiliki dua stan permainan. Stan 1: pemain menang jika dua koin yang dilempar bersamaan keduanya menunjukkan sisi angka, hadiah Rp8.000 untuk setiap kemenangan. Stan 2: pemain menang jika sebuah dadu yang dilempar menunjukkan mata kelipatan 3, hadiah Rp5.000 untuk setiap kemenangan. Setiap stan dimainkan 300 kali.<br><br>Pemilik pasar malam ingin memilih stan yang total hadiah yang diharapkan harus dibayar lebih sedikit. Keputusan yang tepat adalah ....

| Opsi | Isi |
|---|---|
| A | Stan 2, karena frekuensi harapan kemenangannya 100 kali sehingga total hadiahnya paling sedikit |
| B | Stan 2, karena total hadiah yang diharapkan Rp500.000 lebih sedikit daripada Rp600.000 di Stan 1 |
| C | Stan 1, karena total hadiah yang diharapkan Rp500.000 lebih sedikit daripada Rp600.000 di Stan 2 |
| D | Stan 1, karena frekuensi harapan kemenangannya 75 kali, lebih sedikit daripada 100 kali di Stan 2 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3b2d95ea2ebfb727928eb359c43352e677d7e4ff1fcfbfddb1ef045813db0878`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah pasar malam memiliki dua stan permainan. Stan 1: pemain menang jika dua koin yang dilempar bersamaan keduanya menunjukkan sisi angka, hadiah Rp8.000 untuk setiap kemenangan. Stan 2: pemain menang jika sebuah dadu yang dilempar menunjukkan mata kelipatan 3, hadiah Rp5.000 untuk setiap kemenangan. Setiap stan dimainkan 300 kali.

Pemilik pasar malam ingin memilih stan yang total hadiah yang diharapkan harus dibayar lebih sedikit. Keputusan yang tepat adalah ....
Pilihan: A. Stan 2, karena frekuensi harapan kemenangannya 100 kali sehingga total hadiahnya paling sedikit
B. Stan 2, karena total hadiah yang diharapkan Rp500.000 lebih sedikit daripada Rp600.000 di Stan 1
C. Stan 1, karena total hadiah yang diharapkan Rp500.000 lebih sedikit daripada Rp600.000 di Stan 2
D. Stan 1, karena frekuensi harapan kemenangannya 75 kali, lebih sedikit daripada 100 kali di Stan 2
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 200. Soal `3c82959c96aa099701a86838`

Panitia merancang sebuah kantong berisi 24 bola yang hanya berwarna merah, kuning, dan hijau. Satu bola diambil secara acak, dicatat warnanya, lalu dikembalikan. Rancangan itu harus memenuhi syarat: dari 360 kali pengambilan, frekuensi harapan terambil bola merah adalah 135, dan frekuensi harapan terambil bola kuning dua kali frekuensi harapan terambil bola hijau. Banyak bola hijau dalam kantong adalah ....

| Opsi | Isi |
|---|---|
| A | 9 bola |
| B | 15 bola |
| C | 10 bola |
| D | 5 bola |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1a9bd8cb04fe82c52704915b77d4735c9c12dbee3e9dd393e1faf3395e0bc38e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Panitia merancang sebuah kantong berisi 24 bola yang hanya berwarna merah, kuning, dan hijau. Satu bola diambil secara acak, dicatat warnanya, lalu dikembalikan. Rancangan itu harus memenuhi syarat: dari 360 kali pengambilan, frekuensi harapan terambil bola merah adalah 135, dan frekuensi harapan terambil bola kuning dua kali frekuensi harapan terambil bola hijau. Banyak bola hijau dalam kantong adalah ....
Pilihan: A. 9 bola
B. 15 bola
C. 10 bola
D. 5 bola
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 201. Soal `39cbc8981cb7a034c1346e70`

Tiga koin dilempar bersamaan sebanyak 240 kali. Agar frekuensi harapan jumlah kedua mata dua dadu sama dengan 3 atau 9 persis sama dengan frekuensi harapan munculnya paling sedikit dua sisi angka pada tiga koin tersebut, dua dadu harus dilempar bersamaan sebanyak ....

| Opsi | Isi |
|---|---|
| A | 720 kali |
| B | 480 kali |
| C | 1.080 kali |
| D | 240 kali |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2d83b118196a9df36db4920c90740a988d1b5270ee0b49f23ce79a229f4d2991`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Tiga koin dilempar bersamaan sebanyak 240 kali. Agar frekuensi harapan jumlah kedua mata dua dadu sama dengan 3 atau 9 persis sama dengan frekuensi harapan munculnya paling sedikit dua sisi angka pada tiga koin tersebut, dua dadu harus dilempar bersamaan sebanyak ....
Pilihan: A. 720 kali
B. 480 kali
C. 1.080 kali
D. 240 kali
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 202. Soal `f8d6daa97c92698d02df8022`

Sebuah dadu dilempar 120 kali. Banyak kemunculan tiap mata dadu:<br><br>\| Mata dadu \| 1 \| 2 \| 3 \| 4 \| 5 \| 6 \|<br>\|---\|---\|---\|---\|---\|---\|---\|<br>\| Banyak muncul \| 12 \| 22 \| 19 \| 25 \| 20 \| 22 \|<br><br>Jika dadu dianggap setimbang, mata dadu yang hasil percobaannya paling jauh dari frekuensi harapannya dan arah penyimpangannya adalah ....

| Opsi | Isi |
|---|---|
| A | mata 1, kurang 8 dari frekuensi harapannya |
| B | mata 2, lebih 2 dari frekuensi harapannya |
| C | mata 1, lebih 8 dari frekuensi harapannya |
| D | mata 4, lebih 5 dari frekuensi harapannya |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `44c5a97906067ea41988ccb46677d9e84eb885b0854deadfb52d2bc442ad8273`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah dadu dilempar 120 kali. Banyak kemunculan tiap mata dadu:

| Mata dadu | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Banyak muncul | 12 | 22 | 19 | 25 | 20 | 22 |

Jika dadu dianggap setimbang, mata dadu yang hasil percobaannya paling jauh dari frekuensi harapannya dan arah penyimpangannya adalah ....
Pilihan: A. mata 1, kurang 8 dari frekuensi harapannya
B. mata 2, lebih 2 dari frekuensi harapannya
C. mata 1, lebih 8 dari frekuensi harapannya
D. mata 4, lebih 5 dari frekuensi harapannya
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 203. Soal `c0675ba0a1447a25e484d6f4`

Dewi melempar sebuah dadu setimbang 50 kali dan menghitung frekuensi harapan muncul mata 4 dengan hasil $\frac{1}{6} \times 50 = 8\frac{1}{3}$. Ia menyimpulkan, "Hasil ini pasti salah, karena banyak kemunculan selalu bilangan bulat." Penilaian yang tepat terhadap kesimpulan Dewi adalah ....

| Opsi | Isi |
|---|---|
| A | Dewi benar; frekuensi harapan harus dibulatkan menjadi 8 dan mata 4 pasti muncul 8 kali |
| B | Dewi benar; hitungan yang tepat adalah $6 \times 50 = 300$ kali karena ada enam mata dadu |
| C | Dewi benar; frekuensi harapan harus sama dengan banyak lemparan, yaitu 50 kali |
| D | hitungannya benar; frekuensi harapan adalah nilai harapan yang boleh bukan bilangan bulat dan tidak menjamin tepat 8 kali |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menyimpulkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e8cf4e63ee3039f8c52e8909b56504c39d6a2164c7de5a4875dfd8d4194dc110`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Dewi melempar sebuah dadu setimbang 50 kali dan menghitung frekuensi harapan muncul mata 4 dengan hasil $\frac{1}{6} \times 50 = 8\frac{1}{3}$. Ia menyimpulkan, "Hasil ini pasti salah, karena banyak kemunculan selalu bilangan bulat." Penilaian yang tepat terhadap kesimpulan Dewi adalah ....
Pilihan: A. Dewi benar; frekuensi harapan harus dibulatkan menjadi 8 dan mata 4 pasti muncul 8 kali
B. Dewi benar; hitungan yang tepat adalah $6 \times 50 = 300$ kali karena ada enam mata dadu
C. Dewi benar; frekuensi harapan harus sama dengan banyak lemparan, yaitu 50 kali
D. hitungannya benar; frekuensi harapan adalah nilai harapan yang boleh bukan bilangan bulat dan tidak menjamin tepat 8 kali
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 204. Soal `a4d649564515b4c9946f036b`

Kantin sekolah mencatat bahwa dari siswa yang membeli makan siang, persentase pemilihan menu adalah sebagai berikut. Hari ini diperkirakan ada 500 siswa yang membeli dan kantin telah menyiapkan sejumlah porsi.<br><br>\| Menu \| Persentase peminat \| Porsi disiapkan \|<br>\|---\|---\|---\|<br>\| Nasi goreng \| 36% \| 170 \|<br>\| Mie ayam \| 28% \| 150 \|<br>\| Soto \| 20% \| 90 \|<br>\| Bakso \| 16% \| 70 \|<br><br>Agar setiap menu tersedia minimal sebanyak frekuensi harapan peminatnya, banyak porsi tambahan seluruhnya yang harus disiapkan adalah ....

| Opsi | Isi |
|---|---|
| A | 20 porsi |
| B | 40 porsi |
| C | 30 porsi |
| D | 10 porsi |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6a6a1ddb9233a7c7fc81803acbf1f71956bcac1f71d45c183a160feadc155b99`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Kantin sekolah mencatat bahwa dari siswa yang membeli makan siang, persentase pemilihan menu adalah sebagai berikut. Hari ini diperkirakan ada 500 siswa yang membeli dan kantin telah menyiapkan sejumlah porsi.

| Menu | Persentase peminat | Porsi disiapkan |
|---|---|---|
| Nasi goreng | 36% | 170 |
| Mie ayam | 28% | 150 |
| Soto | 20% | 90 |
| Bakso | 16% | 70 |

Agar setiap menu tersedia minimal sebanyak frekuensi harapan peminatnya, banyak porsi tambahan seluruhnya yang harus disiapkan adalah ....
Pilihan: A. 20 porsi
B. 40 porsi
C. 30 porsi
D. 10 porsi
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 205. Soal `04ad45a5cc8f50241bf92d90`

Sebuah kotak harus memenuhi dua syarat: dari 120 kali pengambilan satu bola secara acak dengan pengembalian, (1) frekuensi harapan terambil bola merah tepat 40, dan (2) frekuensi harapan terambil bola biru paling sedikit tiga kali frekuensi harapan terambil bola hijau. Empat rancangan isi kotak:<br><br>\| Rancangan \| Merah \| Biru \| Hijau \|<br>\|---\|---\|---\|---\|<br>\| K1 \| 4 \| 5 \| 3 \|<br>\| K2 \| 6 \| 9 \| 3 \|<br>\| K3 \| 5 \| 6 \| 4 \|<br>\| K4 \| 8 \| 10 \| 6 \|<br><br>Rancangan yang memenuhi kedua syarat adalah ....

| Opsi | Isi |
|---|---|
| A | K2 |
| B | K1 |
| C | K3 |
| D | K4 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `607c26c871249ba78bbc0bf0b84ede6c97281c8e56a7e8e5fe519b32d681b842`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kotak harus memenuhi dua syarat: dari 120 kali pengambilan satu bola secara acak dengan pengembalian, (1) frekuensi harapan terambil bola merah tepat 40, dan (2) frekuensi harapan terambil bola biru paling sedikit tiga kali frekuensi harapan terambil bola hijau. Empat rancangan isi kotak:

| Rancangan | Merah | Biru | Hijau |
|---|---|---|---|
| K1 | 4 | 5 | 3 |
| K2 | 6 | 9 | 3 |
| K3 | 5 | 6 | 4 |
| K4 | 8 | 10 | 6 |

Rancangan yang memenuhi kedua syarat adalah ....
Pilihan: A. K2
B. K1
C. K3
D. K4
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 206. Soal `2f2e931a0ab3fd8746b219b5`

Dari pemeriksaan 80 lampu pada sebuah pabrik, ditemukan 6 lampu rusak. Pabrik akan mengirim 1.200 lampu dengan persediaan 80 lampu pengganti gratis. Berdasarkan hasil pemeriksaan tersebut, kesimpulan yang tepat adalah ....

| Opsi | Isi |
|---|---|
| A | persediaan cukup, karena frekuensi harapan lampu rusak 72, kurang dari 80 |
| B | persediaan kurang, karena frekuensi harapan lampu rusak 90 sehingga perlu tambahan 90 lampu |
| C | persediaan kurang, karena frekuensi harapan lampu rusak 90 sehingga perlu tambahan 10 lampu |
| D | persediaan cukup, karena frekuensi harapan lampu rusak sama dengan 80, yaitu banyak lampu diperiksa |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menyimpulkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `90cfe9fa069d4fe9b8351c6411ba9fae54c68b67028e5d18db93d56e7d508dde`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Dari pemeriksaan 80 lampu pada sebuah pabrik, ditemukan 6 lampu rusak. Pabrik akan mengirim 1.200 lampu dengan persediaan 80 lampu pengganti gratis. Berdasarkan hasil pemeriksaan tersebut, kesimpulan yang tepat adalah ....
Pilihan: A. persediaan cukup, karena frekuensi harapan lampu rusak 72, kurang dari 80
B. persediaan kurang, karena frekuensi harapan lampu rusak 90 sehingga perlu tambahan 90 lampu
C. persediaan kurang, karena frekuensi harapan lampu rusak 90 sehingga perlu tambahan 10 lampu
D. persediaan cukup, karena frekuensi harapan lampu rusak sama dengan 80, yaitu banyak lampu diperiksa
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 207. Soal `d58f7732ec34110444a730bd`

Sebuah koin setimbang dilempar 10 kali dan semuanya menunjukkan sisi gambar. Rudi berkata, "Dalam 20 lemparan berikutnya, frekuensi harapan sisi angka pasti lebih dari 10 supaya hasilnya seimbang." Penilaian yang tepat terhadap Rudi adalah ....

| Opsi | Isi |
|---|---|
| A | Rudi keliru, karena frekuensi harapan angka dalam 20 lemparan berikutnya adalah 20 |
| B | Rudi benar, karena sisi angka harus mengejar sehingga frekuensi harapannya lebih dari 10 |
| C | Rudi keliru, karena koin pasti hanya menghasilkan gambar sehingga frekuensi harapan angka 0 |
| D | Rudi keliru, karena peluang angka tiap lemparan tetap $\frac{1}{2}$ sehingga frekuensi harapannya 10 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `44badc5024219c887fefe9418399b288f9c1dc18d659a91b3947796155b3f819`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah koin setimbang dilempar 10 kali dan semuanya menunjukkan sisi gambar. Rudi berkata, "Dalam 20 lemparan berikutnya, frekuensi harapan sisi angka pasti lebih dari 10 supaya hasilnya seimbang." Penilaian yang tepat terhadap Rudi adalah ....
Pilihan: A. Rudi keliru, karena frekuensi harapan angka dalam 20 lemparan berikutnya adalah 20
B. Rudi benar, karena sisi angka harus mengejar sehingga frekuensi harapannya lebih dari 10
C. Rudi keliru, karena koin pasti hanya menghasilkan gambar sehingga frekuensi harapan angka 0
D. Rudi keliru, karena peluang angka tiap lemparan tetap $\frac{1}{2}$ sehingga frekuensi harapannya 10
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 208. Soal `8d45dccf8e285d75f29d7dd4`

Di sebuah kota, 28% penduduknya masuk Generasi Z dan 35% penduduknya masuk generasi milenial. Panitia memilih penduduk kota secara acak dan menginginkan frekuensi harapan terpilihnya penduduk Generasi Z atau milenial paling sedikit 100 orang. Banyak penduduk minimum yang harus dipilih adalah ....

| Opsi | Isi |
|---|---|
| A | 100 orang |
| B | 158 orang |
| C | 159 orang |
| D | 357 orang |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `77be6ff58b56f369ef1c48534d8c8ae54c3273921b5c109b19742bd469705dbf`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Di sebuah kota, 28% penduduknya masuk Generasi Z dan 35% penduduknya masuk generasi milenial. Panitia memilih penduduk kota secara acak dan menginginkan frekuensi harapan terpilihnya penduduk Generasi Z atau milenial paling sedikit 100 orang. Banyak penduduk minimum yang harus dipilih adalah ....
Pilihan: A. 100 orang
B. 158 orang
C. 159 orang
D. 357 orang
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 209. Soal `ee7b0725bdeed9ca69607f31`

Dalam sebuah permainan, pemain melempar sebuah koin. Jika muncul gambar, pemain kalah. Jika muncul angka, pemain melempar sebuah dadu dan menang bila mata dadu memenuhi aturan. Permainan dimainkan 240 kali. Empat aturan yang dipertimbangkan: Aturan I mata dadu prima, Aturan II mata dadu lebih dari 2, Aturan III mata dadu kelipatan 3, Aturan IV mata dadu bukan 6.<br><br>Pemilik ingin frekuensi harapan kemenangan sebesar mungkin tetapi tidak lebih dari 70 kali. Aturan yang dipilih adalah ....

| Opsi | Isi |
|---|---|
| A | Aturan III |
| B | Aturan I |
| C | Aturan II |
| D | Aturan IV |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `24c360c7fca929cd31384788aef8a713f603bc3f8cde0884968728900ad20a7d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Dalam sebuah permainan, pemain melempar sebuah koin. Jika muncul gambar, pemain kalah. Jika muncul angka, pemain melempar sebuah dadu dan menang bila mata dadu memenuhi aturan. Permainan dimainkan 240 kali. Empat aturan yang dipertimbangkan: Aturan I mata dadu prima, Aturan II mata dadu lebih dari 2, Aturan III mata dadu kelipatan 3, Aturan IV mata dadu bukan 6.

Pemilik ingin frekuensi harapan kemenangan sebesar mungkin tetapi tidak lebih dari 70 kali. Aturan yang dipilih adalah ....
Pilihan: A. Aturan III
B. Aturan I
C. Aturan II
D. Aturan IV
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 210. Soal `294524517cd93d6fff72d728`

Lima kelompok masing-masing melempar sebuah dadu setimbang 60 kali. Banyak kemunculan mata 6:<br><br>\| Kelompok \| 1 \| 2 \| 3 \| 4 \| 5 \|<br>\|---\|---\|---\|---\|---\|---\|<br>\| Mata 6 muncul \| 7 \| 12 \| 9 \| 13 \| 9 \|<br><br>Pernyataan yang tepat mengenai data tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | frekuensi harapan tiap kelompok 10; tidak ada kelompok yang tepat 10, tetapi jumlah semuanya 50 sama dengan frekuensi harapan gabungan |
| B | frekuensi harapan tiap kelompok 10, dan jumlah semuanya 50 berbeda dari frekuensi harapan gabungan 60 |
| C | frekuensi harapan tiap kelompok 13, yaitu kemunculan terbanyak yang diperoleh |
| D | frekuensi harapan tiap kelompok 10, tetapi karena tidak ada kelompok yang tepat 10, dadu itu pasti tidak setimbang |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `53c42e3c7c678b96b3f3918695db14b1de23950f9f049a90f2d7767c9eb4ce3a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Lima kelompok masing-masing melempar sebuah dadu setimbang 60 kali. Banyak kemunculan mata 6:

| Kelompok | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Mata 6 muncul | 7 | 12 | 9 | 13 | 9 |

Pernyataan yang tepat mengenai data tersebut adalah ....
Pilihan: A. frekuensi harapan tiap kelompok 10; tidak ada kelompok yang tepat 10, tetapi jumlah semuanya 50 sama dengan frekuensi harapan gabungan
B. frekuensi harapan tiap kelompok 10, dan jumlah semuanya 50 berbeda dari frekuensi harapan gabungan 60
C. frekuensi harapan tiap kelompok 13, yaitu kemunculan terbanyak yang diperoleh
D. frekuensi harapan tiap kelompok 10, tetapi karena tidak ada kelompok yang tepat 10, dadu itu pasti tidak setimbang
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 211. Soal `62b2cb62ef14f3b5c34e3ebf`

Satu kartu diambil secara acak dari seperangkat kartu remi (52 kartu), dicatat, lalu dikembalikan dan dikocok lagi. Pengambilan dilakukan 156 kali. Frekuensi harapan terambil kartu hati atau kartu As adalah ....

| Opsi | Isi |
|---|---|
| A | 39 |
| B | 51 |
| C | 12 |
| D | 48 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f65fde2b7cb0ad818fc7d6a78089538a2cac3683427c15441caff88263aa71c1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Satu kartu diambil secara acak dari seperangkat kartu remi (52 kartu), dicatat, lalu dikembalikan dan dikocok lagi. Pengambilan dilakukan 156 kali. Frekuensi harapan terambil kartu hati atau kartu As adalah ....
Pilihan: A. 39
B. 51
C. 12
D. 48
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 212. Soal `74fd0c51c35a0cdcf27a3068`

Sebuah kantong berisi 20 bola yang diberi nomor 1 sampai 20. Satu bola diambil secara acak, dicatat nomornya, lalu dikembalikan. Pengambilan dilakukan 180 kali. Frekuensi harapan terambil bola yang nomornya bukan bilangan prima adalah ....

| Opsi | Isi |
|---|---|
| A | 99 |
| B | 108 |
| C | 172 |
| D | 72 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ed44fae866ccd5f5c0bbbec893ad5cdffba39e6418665621954a3c4237c66c06`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kantong berisi 20 bola yang diberi nomor 1 sampai 20. Satu bola diambil secara acak, dicatat nomornya, lalu dikembalikan. Pengambilan dilakukan 180 kali. Frekuensi harapan terambil bola yang nomornya bukan bilangan prima adalah ....
Pilihan: A. 99
B. 108
C. 172
D. 72
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 213. Soal `42a74a866c139fb9a09bddc2`

Di sebuah kota, persentase penduduknya yang berlangganan internet rumah adalah 64%. Jika dipilih 250 penduduk kota itu secara acak, selisih frekuensi harapan penduduk yang berlangganan dan yang tidak berlangganan adalah ....

| Opsi | Isi |
|---|---|
| A | 70 |
| B | 90 |
| C | 186 |
| D | 160 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b2ca87c6f9ec489e0b43db88b5721364efd14f6ed5fa4397a705c02a2f851c39`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Di sebuah kota, persentase penduduknya yang berlangganan internet rumah adalah 64%. Jika dipilih 250 penduduk kota itu secara acak, selisih frekuensi harapan penduduk yang berlangganan dan yang tidak berlangganan adalah ....
Pilihan: A. 70
B. 90
C. 186
D. 160
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 214. Soal `cb06f45520b7f5cbd540bed4`

Tentukan frekuensi harapan kejadian berikut jika dilakukan 240 kali percobaan. Dalam lempar undi tiga koin, diperoleh paling sedikit dua sisi angka. Frekuensi harapannya adalah ....

| Opsi | Isi |
|---|---|
| A | 90 |
| B | 30 |
| C | 120 |
| D | 210 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `123791cf9cc6e0573ac6d6ea09228525f4a7f2bdbc938504c7ab6186319a262e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan frekuensi harapan kejadian berikut jika dilakukan 240 kali percobaan. Dalam lempar undi tiga koin, diperoleh paling sedikit dua sisi angka. Frekuensi harapannya adalah ....
Pilihan: A. 90
B. 30
C. 120
D. 210
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 215. Soal `19e9cbff9e47b5c8da6adc55`

Sebuah koin dan sebuah dadu dilempar undi bersamaan sebanyak 168 kali. Frekuensi harapan muncul sisi angka pada koin dan mata dadu bilangan prima adalah ....

| Opsi | Isi |
|---|---|
| A | 21 |
| B | 84 |
| C | 14 |
| D | 42 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `00ab9119dc9b08eda1e45b0f58736fcbf2938078389e359c2ee6b624ec8684ef`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah koin dan sebuah dadu dilempar undi bersamaan sebanyak 168 kali. Frekuensi harapan muncul sisi angka pada koin dan mata dadu bilangan prima adalah ....
Pilihan: A. 21
B. 84
C. 14
D. 42
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 216. Soal `7718701bac8386c62087a123`

Sebuah roda putar dibagi menjadi 10 juring yang ukurannya sama. Empat juring berwarna merah, tiga juring kuning, dua juring hijau, dan satu juring biru.<br><br>Jika roda tersebut diputar sebanyak 120 kali, frekuensi harapan jarum menunjuk juring berwarna merah atau hijau adalah ....

| Opsi | Isi |
|---|---|
| A | 48 |
| B | 36 |
| C | 72 |
| D | 84 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a30d9aff84a7e6aa25f9caf64124810da07d143080050316ce00d459e310eb77`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah roda putar dibagi menjadi 10 juring yang ukurannya sama. Empat juring berwarna merah, tiga juring kuning, dua juring hijau, dan satu juring biru.

Jika roda tersebut diputar sebanyak 120 kali, frekuensi harapan jarum menunjuk juring berwarna merah atau hijau adalah ....
Pilihan: A. 48
B. 36
C. 72
D. 84
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 217. Soal `6a8105c25982fff18e0f2b52`

Sebuah dadu dilempar undi sebanyak 420 kali. Frekuensi harapan diperoleh mata dadu bilangan prima atau kelipatan tiga adalah ....

| Opsi | Isi |
|---|---|
| A | 280 |
| B | 140 |
| C | 350 |
| D | 210 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `df1c0ea432767887a410c762673808238713cb1b5aad8ee3909b95b4f627b0e6`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah dadu dilempar undi sebanyak 420 kali. Frekuensi harapan diperoleh mata dadu bilangan prima atau kelipatan tiga adalah ....
Pilihan: A. 280
B. 140
C. 350
D. 210
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 218. Soal `5c1885247af503a912897636`

Dua dadu dilempar undi bersamaan sebanyak 360 kali. Frekuensi harapan jumlah kedua mata dadu sama dengan 8 adalah ....

| Opsi | Isi |
|---|---|
| A | 60 |
| B | 40 |
| C | 72 |
| D | 50 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1d31c17b0047984b91b268dbc32aaa3453b586169f6d01c4aa588f2e5ef89a79`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Dua dadu dilempar undi bersamaan sebanyak 360 kali. Frekuensi harapan jumlah kedua mata dadu sama dengan 8 adalah ....
Pilihan: A. 60
B. 40
C. 72
D. 50
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 219. Soal `e71bcc721234ee7bfebc6f9c`

Sebuah kotak berisi 2 bola putih dan beberapa bola merah. Satu bola diambil secara acak, dicatat warnanya, lalu dikembalikan. Dari 150 kali pengambilan, frekuensi harapan terambil bola merah adalah 90. Banyak bola merah dalam kotak adalah ....

| Opsi | Isi |
|---|---|
| A | 5 bola |
| B | 6 bola |
| C | 3 bola |
| D | 4 bola |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e3b5d24cb9c3b3909f910f5aa49007725e90c944cd7f7cf087522f3a9f4b0f99`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kotak berisi 2 bola putih dan beberapa bola merah. Satu bola diambil secara acak, dicatat warnanya, lalu dikembalikan. Dari 150 kali pengambilan, frekuensi harapan terambil bola merah adalah 90. Banyak bola merah dalam kotak adalah ....
Pilihan: A. 5 bola
B. 6 bola
C. 3 bola
D. 4 bola
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 220. Soal `bf417c0bf9458ba4df7420dd`

Ani melempar sebuah dadu sebanyak 270 kali dan mencatat banyak kemunculan mata dadu faktor dari 6. Budi melempar tiga koin bersamaan sebanyak 400 kali dan mencatat banyak kemunculan tepat dua sisi angka. Selisih frekuensi harapan kejadian Ani dan Budi adalah ....

| Opsi | Isi |
|---|---|
| A | 15 |
| B | 30 |
| C | 330 |
| D | 80 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1ff0f7b34b3718b6ae0272f21b95e0e3a9bc7fdc2a5449f1583956488aab1d23`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Ani melempar sebuah dadu sebanyak 270 kali dan mencatat banyak kemunculan mata dadu faktor dari 6. Budi melempar tiga koin bersamaan sebanyak 400 kali dan mencatat banyak kemunculan tepat dua sisi angka. Selisih frekuensi harapan kejadian Ani dan Budi adalah ....
Pilihan: A. 15
B. 30
C. 330
D. 80
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 221. Soal `37d1445d999f212a284efc59`

Tiga siswa masing-masing melempar undi sebuah koin sebanyak 80 kali. Banyak sisi angka yang diperoleh: Dian 44 kali, Eko 33 kali, dan Fitri 38 kali.<br><br>Hasil yang tidak biasa adalah hasil yang paling jauh dari frekuensi harapan sisi angka. Hasil siswa yang tidak biasa adalah ....

| Opsi | Isi |
|---|---|
| A | Eko, karena selisihnya dari frekuensi harapan paling besar |
| B | Tidak ada, karena hasil seharusnya selalu tepat 40 kali |
| C | Fitri, karena hasilnya paling mendekati frekuensi harapan |
| D | Dian, karena banyak sisi angkanya paling banyak |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `bc9a614f8b2dedf3b74099fcbabfa6872285eb8885c6bbdcac034c4a5a7a8ee1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Tiga siswa masing-masing melempar undi sebuah koin sebanyak 80 kali. Banyak sisi angka yang diperoleh: Dian 44 kali, Eko 33 kali, dan Fitri 38 kali.

Hasil yang tidak biasa adalah hasil yang paling jauh dari frekuensi harapan sisi angka. Hasil siswa yang tidak biasa adalah ....
Pilihan: A. Eko, karena selisihnya dari frekuensi harapan paling besar
B. Tidak ada, karena hasil seharusnya selalu tepat 40 kali
C. Fitri, karena hasilnya paling mendekati frekuensi harapan
D. Dian, karena banyak sisi angkanya paling banyak
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 222. Soal `4ff87549d34a99b362ae4d5b`

\| Kejadian \| Peluang \| Banyak percobaan \|<br>\|---\|---\|---\|<br>\| A \| $\frac{3}{8}$ \| 72 \|<br>\| B \| 40% \| 70 \|<br>\| C \| $\frac{5}{12}$ \| 60 \|<br>\| D \| 0,3 \| 90 \|<br><br>Berdasarkan data pada tabel, kejadian yang frekuensi harapannya paling besar adalah ....

| Opsi | Isi |
|---|---|
| A | kejadian C |
| B | kejadian D |
| C | kejadian B |
| D | kejadian A |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e2534e6661055cda02194f2e5c284ffe7d8e4b34c4332697c0c37e3a2f7aac96`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: | Kejadian | Peluang | Banyak percobaan |
|---|---|---|
| A | $\frac{3}{8}$ | 72 |
| B | 40% | 70 |
| C | $\frac{5}{12}$ | 60 |
| D | 0,3 | 90 |

Berdasarkan data pada tabel, kejadian yang frekuensi harapannya paling besar adalah ....
Pilihan: A. kejadian C
B. kejadian D
C. kejadian B
D. kejadian A
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 223. Soal `d3a4fd25c28ba697222779c7`

Di sebuah sekolah, 45% siswanya duduk di kelas IX, dan 20% siswa kelas IX adalah pengurus OSIS. Jika dipilih 400 siswa sekolah itu secara acak, frekuensi harapan terpilih siswa kelas IX yang menjadi pengurus OSIS adalah ....

| Opsi | Isi |
|---|---|
| A | 36 |
| B | 80 |
| C | 180 |
| D | 144 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8c3ab0714d95b0697b592024173d31184c04df8dd5e15b38671d17b07d9fafcb`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Di sebuah sekolah, 45% siswanya duduk di kelas IX, dan 20% siswa kelas IX adalah pengurus OSIS. Jika dipilih 400 siswa sekolah itu secara acak, frekuensi harapan terpilih siswa kelas IX yang menjadi pengurus OSIS adalah ....
Pilihan: A. 36
B. 80
C. 180
D. 144
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 224. Soal `c186958bf47f232bb95ad04c`

Sebuah kantong berisi 3 bola merah, 2 bola biru, dan 2 bola kuning. Satu bola diambil secara acak, dicatat warnanya, lalu dikembalikan. Agar frekuensi harapan terambil bola yang bukan merah sama dengan 96, bola harus diambil sebanyak ....

| Opsi | Isi |
|---|---|
| A | 72 kali |
| B | 168 kali |
| C | 224 kali |
| D | 384 kali |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a06666d206a40cd5b1a5607f2948827d3bbc111d6f8fb17c248a1d75b27d4729`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kantong berisi 3 bola merah, 2 bola biru, dan 2 bola kuning. Satu bola diambil secara acak, dicatat warnanya, lalu dikembalikan. Agar frekuensi harapan terambil bola yang bukan merah sama dengan 96, bola harus diambil sebanyak ....
Pilihan: A. 72 kali
B. 168 kali
C. 224 kali
D. 384 kali
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 225. Soal `8a82ccc8727c70ceb2a2cc51`

Dalam sebuah gim, setiap pion pemain 1 berakhir di salah satu persegi A, B, C, D, atau E dengan banyak cara: A = 1, B = 4, C = 6, D = 4, E = 1. Semua cara memiliki peluang yang sama.<br><br>Jika pemain 1 menjalankan 48 pion, frekuensi harapan pion yang tidak sampai ke persegi C maupun persegi E adalah ....

| Opsi | Isi |
|---|---|
| A | 30 |
| B | 21 |
| C | 18 |
| D | 27 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2aabaf3ec31d1e4897873fb1668b97ca158061608de8bcb9fe79b17b493e0cd5`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Frekuensi Harapan
Tipe soal: multiple_choice
Stimulus: -
Soal: Dalam sebuah gim, setiap pion pemain 1 berakhir di salah satu persegi A, B, C, D, atau E dengan banyak cara: A = 1, B = 4, C = 6, D = 4, E = 1. Semua cara memiliki peluang yang sama.

Jika pemain 1 menjalankan 48 pion, frekuensi harapan pion yang tidak sampai ke persegi C maupun persegi E adalah ....
Pilihan: A. 30
B. 21
C. 18
D. 27
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 226. Soal `d1ec8c3965b2718779e841e6`

Kumpulan semua orang atau objek yang akan diteliti disebut dengan ....

| Opsi | Isi |
|---|---|
| A | kejadian |
| B | ruang sampel |
| C | populasi |
| D | sampel |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8acd4ae5ebe4975b580b6de6044c568f3c5ceeb8097c05438afe7e43d7e990b7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Kumpulan semua orang atau objek yang akan diteliti disebut dengan ....
Pilihan: A. kejadian
B. ruang sampel
C. populasi
D. sampel
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 227. Soal `b0b3fbcb6147347f587d2024`

Sampel yang bentuk, pusat, dan sebarannya berbeda jauh dari populasinya disebut sampel yang ....

| Opsi | Isi |
|---|---|
| A | tidak representatif |
| B | acak |
| C | representatif |
| D | berukuran besar |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `99f77240f0ce8b6452771a4ae782217b6072bcc7586130af8defc42ed2628305`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Sampel yang bentuk, pusat, dan sebarannya berbeda jauh dari populasinya disebut sampel yang ....
Pilihan: A. tidak representatif
B. acak
C. representatif
D. berukuran besar
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 228. Soal `9dd5dbf85b3148ee16baf15b`

Benar atau Salah. Jika 30 siswa dipilih secara acak dari sebuah sekolah, pasti rata-rata tinggi badan sampel itu sama dengan rata-rata tinggi badan seluruh siswa. Jawaban yang tepat adalah ....

| Opsi | Isi |
|---|---|
| A | Salah, karena sampel acak hanya boleh diambil dari satu kelas |
| B | Benar, karena 30 siswa sudah cukup untuk menjamin hasilnya sama |
| C | Salah, karena sampel acak tetap mungkin tidak representatif |
| D | Benar, karena pemilihan acak menjamin rata-rata sampel sama dengan populasi |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7ee2e980bbbeba2a0df6955b075e5065adc34ffd46089790d8084b5e9da2c9b2`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Benar atau Salah. Jika 30 siswa dipilih secara acak dari sebuah sekolah, pasti rata-rata tinggi badan sampel itu sama dengan rata-rata tinggi badan seluruh siswa. Jawaban yang tepat adalah ....
Pilihan: A. Salah, karena sampel acak hanya boleh diambil dari satu kelas
B. Benar, karena 30 siswa sudah cukup untuk menjamin hasilnya sama
C. Salah, karena sampel acak tetap mungkin tidak representatif
D. Benar, karena pemilihan acak menjamin rata-rata sampel sama dengan populasi
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 229. Soal `31e9771813db006b1238616d`

Seorang peneliti ingin mengetahui persentase siswa SMP di Provinsi Jawa Barat yang memiliki telepon genggam. Populasi penelitian tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | siswa SMP di satu kelas di Provinsi Jawa Barat |
| B | semua siswa SMP di seluruh Indonesia |
| C | siswa SMP di Jawa Barat yang memiliki telepon genggam |
| D | semua siswa SMP di Provinsi Jawa Barat |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8ce446ec3f99e9b5100510cd6d9e051033c7e247f7ccd201e9d48f6da3a6cdf5`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Seorang peneliti ingin mengetahui persentase siswa SMP di Provinsi Jawa Barat yang memiliki telepon genggam. Populasi penelitian tersebut adalah ....
Pilihan: A. siswa SMP di satu kelas di Provinsi Jawa Barat
B. semua siswa SMP di seluruh Indonesia
C. siswa SMP di Jawa Barat yang memiliki telepon genggam
D. semua siswa SMP di Provinsi Jawa Barat
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 230. Soal `2cf4b569abcf65ccaa4bcae9`

Dinas kesehatan sebuah kota ingin mengetahui lama tidur rata-rata warga kota itu setiap malam. Pasangan populasi dan sampel yang mungkin untuk penelitian tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | Populasi: semua warga di satu RW di kota itu; sampel: semua warga di kota itu |
| B | Populasi: semua warga di kota itu; sampel: semua warga di kota tetangga |
| C | Populasi: semua tempat tidur di kota itu; sampel: semua warga di satu RW |
| D | Populasi: semua warga di kota itu; sampel: semua warga di satu RW di kota itu |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2c62c9f929016955107171cb984f636bedee51d7691342815811591a041ff4ae`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Dinas kesehatan sebuah kota ingin mengetahui lama tidur rata-rata warga kota itu setiap malam. Pasangan populasi dan sampel yang mungkin untuk penelitian tersebut adalah ....
Pilihan: A. Populasi: semua warga di satu RW di kota itu; sampel: semua warga di kota itu
B. Populasi: semua warga di kota itu; sampel: semua warga di kota tetangga
C. Populasi: semua tempat tidur di kota itu; sampel: semua warga di satu RW
D. Populasi: semua warga di kota itu; sampel: semua warga di satu RW di kota itu
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 231. Soal `1abf863be99a36a6974cdc24`

Rani calon ketua kelas dalam pemilihan tingkat sekolah. Ia ingin mengetahui persentase siswa sekolahnya yang akan memilihnya.<br><br>Cara pemilihan sampel manakah yang seharusnya dipilih Rani? Cara (1): ia bertanya kepada teman sebangkunya saja. Cara (2): ia mengundi nomor induk dari daftar seluruh siswa sekolah, lalu menyurvei siswa yang nomornya terundi. Cara (3): ia membuat survei lewat grup percakapan angkatannya.

| Opsi | Isi |
|---|---|
| A | Cara (2), mengundi nomor induk dari daftar seluruh siswa |
| B | Cara (3), survei lewat grup percakapan angkatannya |
| C | Cara (1), bertanya kepada teman sebangkunya saja |
| D | Cara (1) dan cara (3) sama baiknya |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `39bd3e18832d2f51b558f3796390d170457e8f690e9fd39e2a86d23b4d364be5`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Rani calon ketua kelas dalam pemilihan tingkat sekolah. Ia ingin mengetahui persentase siswa sekolahnya yang akan memilihnya.

Cara pemilihan sampel manakah yang seharusnya dipilih Rani? Cara (1): ia bertanya kepada teman sebangkunya saja. Cara (2): ia mengundi nomor induk dari daftar seluruh siswa sekolah, lalu menyurvei siswa yang nomornya terundi. Cara (3): ia membuat survei lewat grup percakapan angkatannya.
Pilihan: A. Cara (2), mengundi nomor induk dari daftar seluruh siswa
B. Cara (3), survei lewat grup percakapan angkatannya
C. Cara (1), bertanya kepada teman sebangkunya saja
D. Cara (1) dan cara (3) sama baiknya
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 232. Soal `267d5fd254d3755d48de02d7`

Dua survei mengenai ekstrakurikuler favorit siswa. Survei P: 200 siswa yang kebetulan mengisi polling di akun media sosial sekolah, 140 memilih basket. Survei Q: 50 siswa yang dipilih secara acak oleh komputer dari daftar seluruh siswa, 20 memilih basket.<br><br>Dari dua survei tersebut, manakah yang lebih dapat dipercaya?

| Opsi | Isi |
|---|---|
| A | Keduanya sama dapat dipercaya |
| B | Survei P, karena yang mengisi polling pasti mewakili seluruh siswa |
| C | Survei Q, karena sampelnya dipilih secara acak |
| D | Survei P, karena sampelnya lebih banyak |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8db5a7cc6cf01d68f53d222b19541ca7b9a739168448994f6be00fbc2aab6dcc`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Dua survei mengenai ekstrakurikuler favorit siswa. Survei P: 200 siswa yang kebetulan mengisi polling di akun media sosial sekolah, 140 memilih basket. Survei Q: 50 siswa yang dipilih secara acak oleh komputer dari daftar seluruh siswa, 20 memilih basket.

Dari dua survei tersebut, manakah yang lebih dapat dipercaya?
Pilihan: A. Keduanya sama dapat dipercaya
B. Survei P, karena yang mengisi polling pasti mewakili seluruh siswa
C. Survei Q, karena sampelnya dipilih secara acak
D. Survei P, karena sampelnya lebih banyak
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 233. Soal `9cc2064943141948bab5b2a1`

Nilai ulangan 40 siswa (populasi) terkumpul di sekitar 70 dengan sebaran 50 sampai 90 dan rata-rata sekitar 70. Sampel A terdiri atas 10 siswa dengan nilai tersebar dari 50 sampai 90, terkumpul di sekitar 70, rata-rata 70. Sampel B terdiri atas 10 siswa yang semuanya bernilai 85 atau 90.<br><br>Manakah sampel yang representatif? Mengapa?

| Opsi | Isi |
|---|---|
| A | Sampel A, karena bentuk, pusat, dan sebarannya menyerupai populasi |
| B | Sampel A dan B, karena sama-sama terdiri atas 10 siswa |
| C | Tidak ada, karena sampel kurang dari 40 siswa |
| D | Sampel B, karena seluruh nilainya tinggi |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `be9a0457829f1fd306bdca4c9e7b890d551cbc75729f212f5e9843feea2bcf9c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Nilai ulangan 40 siswa (populasi) terkumpul di sekitar 70 dengan sebaran 50 sampai 90 dan rata-rata sekitar 70. Sampel A terdiri atas 10 siswa dengan nilai tersebar dari 50 sampai 90, terkumpul di sekitar 70, rata-rata 70. Sampel B terdiri atas 10 siswa yang semuanya bernilai 85 atau 90.

Manakah sampel yang representatif? Mengapa?
Pilihan: A. Sampel A, karena bentuk, pusat, dan sebarannya menyerupai populasi
B. Sampel A dan B, karena sama-sama terdiri atas 10 siswa
C. Tidak ada, karena sampel kurang dari 40 siswa
D. Sampel B, karena seluruh nilainya tinggi
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 234. Soal `a9fc6012acd41a901d26b92c`

Dinas pertanian ingin mengetahui rata-rata berat semua buah semangka hasil panen di Kabupaten Jember. Himpunan berikut yang BUKAN kemungkinan sampel penelitian tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | semua buah semangka hasil panen di satu kebun di Jember |
| B | semua buah melon hasil panen di satu kebun di Jember |
| C | semua buah semangka hasil panen di tiga desa di Jember |
| D | semua buah semangka hasil panen di Kecamatan Ajung |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `bbe95017944eac8a5fb759f005cb57e50131bbece017730689be219fe31069c5`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Dinas pertanian ingin mengetahui rata-rata berat semua buah semangka hasil panen di Kabupaten Jember. Himpunan berikut yang BUKAN kemungkinan sampel penelitian tersebut adalah ....
Pilihan: A. semua buah semangka hasil panen di satu kebun di Jember
B. semua buah melon hasil panen di satu kebun di Jember
C. semua buah semangka hasil panen di tiga desa di Jember
D. semua buah semangka hasil panen di Kecamatan Ajung
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 235. Soal `1de9b2016a90d7fa4c31020d`

Sebuah sekolah memiliki 450 siswa. Untuk sebuah survei, dipilih 45 siswa dari sekolah tersebut.<br><br>Ukuran sampel pada survei tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | 10 |
| B | 45 |
| C | 450 |
| D | 405 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3565482d9ef9913dea0ecb9b8ea907800c67a2dee5959ab3b62709f05b087f09`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah sekolah memiliki 450 siswa. Untuk sebuah survei, dipilih 45 siswa dari sekolah tersebut.

Ukuran sampel pada survei tersebut adalah ....
Pilihan: A. 10
B. 45
C. 450
D. 405
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 236. Soal `7d205ba416faceff5002988e`

Sebuah sampel dipilih secara acak jika ....

| Opsi | Isi |
|---|---|
| A | setiap kemungkinan sampel berukuran sama memiliki peluang terpilih yang sama |
| B | anggotanya dipilih sesuai kemauan peneliti |
| C | hasilnya pasti sama dengan populasi |
| D | anggotanya hanya diambil dari siswa yang paling dekat |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e12fc0332d0935500e47527d3e03629cf4136ecf83a90469c2dad67dfb738f80`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah sampel dipilih secara acak jika ....
Pilihan: A. setiap kemungkinan sampel berukuran sama memiliki peluang terpilih yang sama
B. anggotanya dipilih sesuai kemauan peneliti
C. hasilnya pasti sama dengan populasi
D. anggotanya hanya diambil dari siswa yang paling dekat
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 237. Soal `bec7547364ad897864a8de42`

Ibu guru mengambil satu kartu bernomor dari kotak berisi kartu nomor absen. Nomor dicatat, kartu dikembalikan ke kotak, lalu kotak dikocok dan diambil kartu berikutnya.<br><br>Cara pemilihan sampel tersebut dilakukan ....

| Opsi | Isi |
|---|---|
| A | dengan memilih nomor terurut |
| B | tanpa pengocokan |
| C | tanpa pengembalian |
| D | dengan pengembalian |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b8ab727bce2a0537ce15c638213a33d80edef30218f42dcd7f99750a5d4ce528`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Ibu guru mengambil satu kartu bernomor dari kotak berisi kartu nomor absen. Nomor dicatat, kartu dikembalikan ke kotak, lalu kotak dikocok dan diambil kartu berikutnya.

Cara pemilihan sampel tersebut dilakukan ....
Pilihan: A. dengan memilih nomor terurut
B. tanpa pengocokan
C. tanpa pengembalian
D. dengan pengembalian
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 238. Soal `5a96900bc855d19e34cbbf43`

Populasi suatu penelitian adalah $P = \{\text{Ani, Budi, Cici, Dedi, Eka, Fani}\}$.<br><br>Himpunan berikut yang dapat menjadi sampel dari populasi tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $\{\text{Ani, Cici, Hadi}\}$ |
| B | $\{\text{Budi, Dedi, Gita}\}$ |
| C | $\{\text{Budi, Dedi, Eka}\}$ |
| D | $\{\text{Eka, Fani, Joko}\}$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `976bcb1abd88b4ae02080ebd451a2f88a527585d4116cc918b7de4668c9b13b8`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Populasi suatu penelitian adalah $P = \{\text{Ani, Budi, Cici, Dedi, Eka, Fani}\}$.

Himpunan berikut yang dapat menjadi sampel dari populasi tersebut adalah ....
Pilihan: A. $\{\text{Ani, Cici, Hadi}\}$
B. $\{\text{Budi, Dedi, Gita}\}$
C. $\{\text{Budi, Dedi, Eka}\}$
D. $\{\text{Eka, Fani, Joko}\}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 239. Soal `f288d13234608b81aea1bba5`

Sampel disebut representatif terhadap populasinya jika distribusinya menyerupai populasi dalam hal ....

| Opsi | Isi |
|---|---|
| A | tinggi, berat, dan lebar |
| B | bentuk, pusat, dan sebaran |
| C | warna, ukuran, dan bentuk |
| D | nama, urutan, dan banyak anggota |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0ae629aa871750041e65b3ab55909ef022cc96253a94a435addf8352e1de5035`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Sampel disebut representatif terhadap populasinya jika distribusinya menyerupai populasi dalam hal ....
Pilihan: A. tinggi, berat, dan lebar
B. bentuk, pusat, dan sebaran
C. warna, ukuran, dan bentuk
D. nama, urutan, dan banyak anggota
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 240. Soal `3c347e149134998b5c20bd59`

Pada sebuah diagram titik berat buah jeruk, kategori 0,3 kg memiliki empat titik.<br><br>Arti dari empat titik pada kategori 0,3 kg tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | ada 0,3 buah jeruk yang beratnya 4 kg |
| B | jumlah berat semua jeruk adalah 4 kg |
| C | ada satu buah jeruk yang beratnya 1,2 kg |
| D | ada empat buah jeruk yang beratnya 0,3 kg |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1c6da0ca02323613432afd20d00c2c28adf49dfe37efd5577fb6d1b51034482e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada sebuah diagram titik berat buah jeruk, kategori 0,3 kg memiliki empat titik.

Arti dari empat titik pada kategori 0,3 kg tersebut adalah ....
Pilihan: A. ada 0,3 buah jeruk yang beratnya 4 kg
B. jumlah berat semua jeruk adalah 4 kg
C. ada satu buah jeruk yang beratnya 1,2 kg
D. ada empat buah jeruk yang beratnya 0,3 kg
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 241. Soal `b688e517d2d27270936cda73`

Kepala desa ingin mengetahui apakah warga desa setuju dengan rencana pembangunan balai warga. Ia membagikan 500 formulir kepada warga yang dipilih secara acak dari daftar seluruh warga desa. Hanya 60 formulir yang dikembalikan, dan 54 di antaranya menyatakan setuju. Kepala desa menyimpulkan bahwa 90% warga desa setuju.<br><br>Penilaian yang tepat terhadap kesimpulan kepala desa adalah ....

| Opsi | Isi |
|---|---|
| A | belum dapat dipercaya, karena 60 warga yang mengembalikan formulir memilih sendiri untuk menjawab sehingga bukan sampel acak |
| B | belum dapat dipercaya, karena sampel harus berukuran separuh dari populasi |
| C | dapat dipercaya, karena 90% adalah persentase yang sangat tinggi |
| D | dapat dipercaya, karena 500 warga dipilih secara acak sehingga 60 jawaban pasti representatif |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menyimpulkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `406b9521185e5d6531fd2572d36138e9adc73153fff0a66b54abae06a28b9b29`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Kepala desa ingin mengetahui apakah warga desa setuju dengan rencana pembangunan balai warga. Ia membagikan 500 formulir kepada warga yang dipilih secara acak dari daftar seluruh warga desa. Hanya 60 formulir yang dikembalikan, dan 54 di antaranya menyatakan setuju. Kepala desa menyimpulkan bahwa 90% warga desa setuju.

Penilaian yang tepat terhadap kesimpulan kepala desa adalah ....
Pilihan: A. belum dapat dipercaya, karena 60 warga yang mengembalikan formulir memilih sendiri untuk menjawab sehingga bukan sampel acak
B. belum dapat dipercaya, karena sampel harus berukuran separuh dari populasi
C. dapat dipercaya, karena 90% adalah persentase yang sangat tinggi
D. dapat dipercaya, karena 500 warga dipilih secara acak sehingga 60 jawaban pasti representatif
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 242. Soal `2945624340ecf10ecb258546`

Sebuah sekolah memiliki 600 siswa: 300 siswa kelas VII, 200 siswa kelas VIII, dan 100 siswa kelas IX. Rani mengundi 30 siswa dari daftar seluruh siswa dengan cara yang memberi peluang sama kepada setiap kemungkinan sampel 30 siswa. Ternyata 22 siswa yang terpilih berasal dari kelas VII. Rani menyimpulkan bahwa cara pengundiannya salah.<br><br>Penilaian yang tepat terhadap kesimpulan Rani adalah ....

| Opsi | Isi |
|---|---|
| A | tidak tepat, karena cara mengundinya tetap acak dan hasil yang didominasi kelas VII hanya kebetulan sebab sampel acak hanya berpeluang besar representatif |
| B | tepat, karena sampel acak pasti representatif sehingga sampel yang timpang menunjukkan cara mengundinya salah |
| C | tidak tepat, karena sampel yang didominasi kelas VII tetap representatif terhadap seluruh siswa |
| D | tepat, karena sampel acak harus memuat siswa yang sama banyak dari setiap kelas |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menyimpulkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `99b7b9eba381a8d91aa95069c9ea4abdac556ccd76789aa0b61ef3173aa65dad`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah sekolah memiliki 600 siswa: 300 siswa kelas VII, 200 siswa kelas VIII, dan 100 siswa kelas IX. Rani mengundi 30 siswa dari daftar seluruh siswa dengan cara yang memberi peluang sama kepada setiap kemungkinan sampel 30 siswa. Ternyata 22 siswa yang terpilih berasal dari kelas VII. Rani menyimpulkan bahwa cara pengundiannya salah.

Penilaian yang tepat terhadap kesimpulan Rani adalah ....
Pilihan: A. tidak tepat, karena cara mengundinya tetap acak dan hasil yang didominasi kelas VII hanya kebetulan sebab sampel acak hanya berpeluang besar representatif
B. tepat, karena sampel acak pasti representatif sehingga sampel yang timpang menunjukkan cara mengundinya salah
C. tidak tepat, karena sampel yang didominasi kelas VII tetap representatif terhadap seluruh siswa
D. tepat, karena sampel acak harus memuat siswa yang sama banyak dari setiap kelas
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 243. Soal `52fb4b39449dbb1c65bca808`

Sebuah sekolah memiliki 240 siswa bernomor 1 sampai 240. Panitia akan memilih sampel 24 siswa.<br><br>Cara pemilihan yang menghasilkan sampel acak menurut Definisi 4.7 (semua kemungkinan sampel 24 siswa berpeluang sama) adalah ....

| Opsi | Isi |
|---|---|
| A | memilih siswa bernomor 1 sampai 24 |
| B | memasukkan 240 kartu bernomor ke kotak, mengocoknya, lalu mengambil 24 kartu sekaligus |
| C | mengambil satu kartu dari kotak berisi kartu nomor 1 sampai 10, lalu memilih nomor itu dan setiap kelipatan 10 berikutnya |
| D | memilih 24 siswa yang pertama kali tiba di sekolah pada hari survei |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5f90b5520d6b652fc0e7d3e7c99fb351a47f657b0cfe3d1120af50f7c4ab8609`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah sekolah memiliki 240 siswa bernomor 1 sampai 240. Panitia akan memilih sampel 24 siswa.

Cara pemilihan yang menghasilkan sampel acak menurut Definisi 4.7 (semua kemungkinan sampel 24 siswa berpeluang sama) adalah ....
Pilihan: A. memilih siswa bernomor 1 sampai 24
B. memasukkan 240 kartu bernomor ke kotak, mengocoknya, lalu mengambil 24 kartu sekaligus
C. mengambil satu kartu dari kotak berisi kartu nomor 1 sampai 10, lalu memilih nomor itu dan setiap kelipatan 10 berikutnya
D. memilih 24 siswa yang pertama kali tiba di sekolah pada hari survei
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 244. Soal `0dbf1acb824a7bdf7230b8c7`

Sebuah laporan menyatakan: "Kami menyurvei 400 pengunjung sebuah pusat perbelanjaan pada hari Sabtu siang, dan 320 orang menyatakan sering berbelanja secara daring. Karena sampel kami besar, dapat disimpulkan bahwa 80% seluruh warga kota sering berbelanja secara daring."<br><br>Kesalahan penalaran utama dalam laporan tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | memakai sampel yang terlalu besar, karena sampel tidak boleh lebih dari 100 orang |
| B | mengira sampel yang besar pasti mewakili warga kota, padahal pengunjung pusat perbelanjaan itu bukan sampel acak dari seluruh warga |
| C | menghitung persentase dengan salah, karena $\frac{320}{400}$ bukan 80% |
| D | memakai sampel yang terlalu kecil, karena sampel harus sama banyak dengan seluruh warga kota |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `495cc8d6eb34e0c0c8938f875e0d63a54d3c90ba05ba71ccdf5365617d99f7de`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah laporan menyatakan: "Kami menyurvei 400 pengunjung sebuah pusat perbelanjaan pada hari Sabtu siang, dan 320 orang menyatakan sering berbelanja secara daring. Karena sampel kami besar, dapat disimpulkan bahwa 80% seluruh warga kota sering berbelanja secara daring."

Kesalahan penalaran utama dalam laporan tersebut adalah ....
Pilihan: A. memakai sampel yang terlalu besar, karena sampel tidak boleh lebih dari 100 orang
B. mengira sampel yang besar pasti mewakili warga kota, padahal pengunjung pusat perbelanjaan itu bukan sampel acak dari seluruh warga
C. menghitung persentase dengan salah, karena $\frac{320}{400}$ bukan 80%
D. memakai sampel yang terlalu kecil, karena sampel harus sama banyak dengan seluruh warga kota
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 245. Soal `f693a6857f9d2950cd81bf6c`

Nilai ulangan 10 siswa (populasi): 50, 60, 60, 70, 70, 70, 70, 80, 80, 90. Dari populasi itu diambil sampel 4 siswa dengan nilai 70, 70, 70, 70. Dewi menyimpulkan bahwa sampel tersebut representatif karena rata-ratanya sama dengan rata-rata populasi.<br><br>Penilaian yang tepat terhadap kesimpulan Dewi adalah ....

| Opsi | Isi |
|---|---|
| A | kurang tepat, karena sampel 4 siswa harus sama banyak dengan 10 siswa populasi |
| B | tepat, karena kesamaan pusat data saja sudah cukup untuk sampel representatif |
| C | kurang tepat, karena sebaran sampel (semua bernilai 70) jauh lebih sempit daripada sebaran populasi (50 sampai 90) |
| D | kurang tepat, karena rata-rata sampel harus lebih besar daripada rata-rata populasi |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menyimpulkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7a1d21534513b4a3c509cac8c2225338dcac10c4b77c901887d951bdc9a1777f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Nilai ulangan 10 siswa (populasi): 50, 60, 60, 70, 70, 70, 70, 80, 80, 90. Dari populasi itu diambil sampel 4 siswa dengan nilai 70, 70, 70, 70. Dewi menyimpulkan bahwa sampel tersebut representatif karena rata-ratanya sama dengan rata-rata populasi.

Penilaian yang tepat terhadap kesimpulan Dewi adalah ....
Pilihan: A. kurang tepat, karena sampel 4 siswa harus sama banyak dengan 10 siswa populasi
B. tepat, karena kesamaan pusat data saja sudah cukup untuk sampel representatif
C. kurang tepat, karena sebaran sampel (semua bernilai 70) jauh lebih sempit daripada sebaran populasi (50 sampai 90)
D. kurang tepat, karena rata-rata sampel harus lebih besar daripada rata-rata populasi
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 246. Soal `3bf4621434cd5d992ec504a7`

Sebuah kotak berisi 5 kartu bernomor 1, 2, 3, 4, dan 5. Guru mengambil dua kartu satu per satu secara acak dan mencatat hasilnya berurutan. Guru ingin tahu apakah peluang jumlah kedua nomor sama dengan 8 berbeda untuk pengambilan dengan pengembalian dan tanpa pengembalian.<br><br>Pernyataan yang benar mengenai kedua peluang tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $\frac{1}{10}$ pada kedua cara, sehingga kedua peluang sama besar |
| B | dengan pengembalian $\frac{2}{25}$ dan tanpa pengembalian $\frac{1}{10}$, sehingga lebih besar tanpa pengembalian |
| C | dengan pengembalian $\frac{3}{25}$ dan tanpa pengembalian $\frac{3}{20}$, sehingga lebih besar tanpa pengembalian |
| D | dengan pengembalian $\frac{3}{25}$ dan tanpa pengembalian $\frac{1}{10}$, sehingga lebih besar dengan pengembalian |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0cbbe3602f8f34f1d3026807168db2dc14422acdaec70c64cee21b6916e933c7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kotak berisi 5 kartu bernomor 1, 2, 3, 4, dan 5. Guru mengambil dua kartu satu per satu secara acak dan mencatat hasilnya berurutan. Guru ingin tahu apakah peluang jumlah kedua nomor sama dengan 8 berbeda untuk pengambilan dengan pengembalian dan tanpa pengembalian.

Pernyataan yang benar mengenai kedua peluang tersebut adalah ....
Pilihan: A. $\frac{1}{10}$ pada kedua cara, sehingga kedua peluang sama besar
B. dengan pengembalian $\frac{2}{25}$ dan tanpa pengembalian $\frac{1}{10}$, sehingga lebih besar tanpa pengembalian
C. dengan pengembalian $\frac{3}{25}$ dan tanpa pengembalian $\frac{3}{20}$, sehingga lebih besar tanpa pengembalian
D. dengan pengembalian $\frac{3}{25}$ dan tanpa pengembalian $\frac{1}{10}$, sehingga lebih besar dengan pengembalian
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 247. Soal `a453a8f4171a5243882cfc9d`

Dina memiliki roda putar yang terbagi menjadi enam juring yang sama besar, masing-masing ditulis angka 2, 4, 6, 8, 10, dan 12. Ia memilih sampel dengan memutar roda itu tiga kali. Dina mengklaim bahwa peluang ia mendapatkan sampel yang rata-ratanya lebih dari 10 adalah $\frac{1}{20}$.<br><br>Penilaian yang tepat terhadap klaim Dina adalah ....

| Opsi | Isi |
|---|---|
| A | klaim salah, peluang sebenarnya $\frac{5}{108}$ dan lebih kecil daripada $\frac{1}{20}$ |
| B | klaim benar, karena ada 10 hasil yang memenuhi dari 200 hasil seluruhnya |
| C | klaim salah, peluang sebenarnya $\frac{1}{54}$ dan lebih kecil daripada $\frac{1}{20}$ |
| D | klaim salah, peluang sebenarnya $\frac{5}{54}$ dan lebih besar daripada $\frac{1}{20}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c93d1de1b4a44f36ee7264c40dad7cde7f9b4677602638e239a03be28193ff1f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Dina memiliki roda putar yang terbagi menjadi enam juring yang sama besar, masing-masing ditulis angka 2, 4, 6, 8, 10, dan 12. Ia memilih sampel dengan memutar roda itu tiga kali. Dina mengklaim bahwa peluang ia mendapatkan sampel yang rata-ratanya lebih dari 10 adalah $\frac{1}{20}$.

Penilaian yang tepat terhadap klaim Dina adalah ....
Pilihan: A. klaim salah, peluang sebenarnya $\frac{5}{108}$ dan lebih kecil daripada $\frac{1}{20}$
B. klaim benar, karena ada 10 hasil yang memenuhi dari 200 hasil seluruhnya
C. klaim salah, peluang sebenarnya $\frac{1}{54}$ dan lebih kecil daripada $\frac{1}{20}$
D. klaim salah, peluang sebenarnya $\frac{5}{54}$ dan lebih besar daripada $\frac{1}{20}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 248. Soal `e4b2f79c0302d6cc50e2e5e7`

Pak Dedi ingin mengetahui rata-rata jarak rumah ke sekolah seluruh 900 siswa. Setiap pagi ia berdiri di gerbang, lalu mencatat jarak rumah 60 siswa pertama yang datang dengan berjalan kaki.<br><br>Dibandingkan rata-rata jarak sebenarnya seluruh siswa, rata-rata jarak dari sampel Pak Dedi kemungkinan besar ....

| Opsi | Isi |
|---|---|
| A | sama, karena jarak rumah adalah data pasti yang tidak dipengaruhi cara memilih siswa |
| B | lebih kecil, karena siswa yang berjalan kaki umumnya tinggal lebih dekat sehingga pusat data sampel bergeser ke nilai rendah |
| C | lebih besar, karena siswa yang berjalan kaki umumnya berangkat lebih pagi dari rumah yang jauh |
| D | sama, karena 60 siswa sudah cukup banyak untuk mewakili 900 siswa |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1ce1d8667f28ce13a57de546fbc3776a6fc92dc2851bc641e1b7f8d9ccb45a2c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Pak Dedi ingin mengetahui rata-rata jarak rumah ke sekolah seluruh 900 siswa. Setiap pagi ia berdiri di gerbang, lalu mencatat jarak rumah 60 siswa pertama yang datang dengan berjalan kaki.

Dibandingkan rata-rata jarak sebenarnya seluruh siswa, rata-rata jarak dari sampel Pak Dedi kemungkinan besar ....
Pilihan: A. sama, karena jarak rumah adalah data pasti yang tidak dipengaruhi cara memilih siswa
B. lebih kecil, karena siswa yang berjalan kaki umumnya tinggal lebih dekat sehingga pusat data sampel bergeser ke nilai rendah
C. lebih besar, karena siswa yang berjalan kaki umumnya berangkat lebih pagi dari rumah yang jauh
D. sama, karena 60 siswa sudah cukup banyak untuk mewakili 900 siswa
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 249. Soal `ce3a5799cc87ef4d834772de`

Seorang guru memilih secara acak 100 siswa dari 1.200 siswa SMP Negeri 3 Kota Malang, dan 70 siswa di antaranya rutin sarapan. Ia menulis kesimpulan: "Sebanyak 70% siswa SMP di seluruh Indonesia rutin sarapan."<br><br>Kesalahan dalam kesimpulan guru tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | satu-satunya kesalahan adalah ukuran sampel 100 siswa yang harus menjadi 1.000 siswa |
| B | sampel acak tidak boleh dipakai untuk menyimpulkan keadaan populasi |
| C | kesimpulannya melampaui populasi, karena sampel acak itu hanya dapat mewakili siswa SMP Negeri 3 Kota Malang |
| D | sampel harus berisi semua 1.200 siswa sekolah itu agar kesimpulannya sah |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menyimpulkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `687ba5cfc3977794197148f5224bde088c38524a1d5a79d930cf0c71ff8a88bc`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Seorang guru memilih secara acak 100 siswa dari 1.200 siswa SMP Negeri 3 Kota Malang, dan 70 siswa di antaranya rutin sarapan. Ia menulis kesimpulan: "Sebanyak 70% siswa SMP di seluruh Indonesia rutin sarapan."

Kesalahan dalam kesimpulan guru tersebut adalah ....
Pilihan: A. satu-satunya kesalahan adalah ukuran sampel 100 siswa yang harus menjadi 1.000 siswa
B. sampel acak tidak boleh dipakai untuk menyimpulkan keadaan populasi
C. kesimpulannya melampaui populasi, karena sampel acak itu hanya dapat mewakili siswa SMP Negeri 3 Kota Malang
D. sampel harus berisi semua 1.200 siswa sekolah itu agar kesimpulannya sah
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 250. Soal `7b14db9176bc678447287840`

Lima siswa, yaitu Ani, Budi, Cici, Dedi, dan Eka, menjadi populasi. Guru memilih 3 kali secara acak. Cara I: dengan pengembalian (satu siswa boleh terpilih lebih dari sekali). Cara II: tanpa pengembalian (tiga siswa berbeda terpilih).<br><br>Peluang Ani termasuk dalam sampel pada kedua cara tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | Cara I $\frac{3}{5}$ dan Cara II $\frac{3}{5}$, sehingga kedua peluang sama |
| B | Cara I $\frac{61}{125}$ dan Cara II $\frac{2}{5}$, sehingga lebih besar pada Cara I |
| C | Cara I $\frac{61}{125}$ dan Cara II $\frac{3}{5}$, sehingga lebih besar pada Cara II |
| D | Cara I $\frac{64}{125}$ dan Cara II $\frac{3}{5}$, sehingga lebih besar pada Cara II |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `bb4472e900578ca91aef02cbb34e061dbff77123a6f2164b9dfaf640651b5e5b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Lima siswa, yaitu Ani, Budi, Cici, Dedi, dan Eka, menjadi populasi. Guru memilih 3 kali secara acak. Cara I: dengan pengembalian (satu siswa boleh terpilih lebih dari sekali). Cara II: tanpa pengembalian (tiga siswa berbeda terpilih).

Peluang Ani termasuk dalam sampel pada kedua cara tersebut adalah ....
Pilihan: A. Cara I $\frac{3}{5}$ dan Cara II $\frac{3}{5}$, sehingga kedua peluang sama
B. Cara I $\frac{61}{125}$ dan Cara II $\frac{2}{5}$, sehingga lebih besar pada Cara I
C. Cara I $\frac{61}{125}$ dan Cara II $\frac{3}{5}$, sehingga lebih besar pada Cara II
D. Cara I $\frac{64}{125}$ dan Cara II $\frac{3}{5}$, sehingga lebih besar pada Cara II
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 251. Soal `143054c49f16013c2661ff82`

Lima siswa memiliki nilai 1, 2, 3, 4, dan 5 (populasi). Dua siswa dipilih secara acak tanpa pengembalian (urutan tidak diperhatikan). Dina mengklaim bahwa rata-rata nilai sampel pasti sama dengan rata-rata nilai populasi.<br><br>Peluang sebenarnya rata-rata sampel tepat sama dengan rata-rata populasi adalah ....

| Opsi | Isi |
|---|---|
| A | $\frac{3}{10}$ |
| B | $\frac{1}{5}$ |
| C | $\frac{2}{5}$ |
| D | $\frac{1}{10}$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c2ea1f484b5d7eddb2769dbbd67840bd537dbef638b676241e90f5c3e8695991`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Lima siswa memiliki nilai 1, 2, 3, 4, dan 5 (populasi). Dua siswa dipilih secara acak tanpa pengembalian (urutan tidak diperhatikan). Dina mengklaim bahwa rata-rata nilai sampel pasti sama dengan rata-rata nilai populasi.

Peluang sebenarnya rata-rata sampel tepat sama dengan rata-rata populasi adalah ....
Pilihan: A. $\frac{3}{10}$
B. $\frac{1}{5}$
C. $\frac{2}{5}$
D. $\frac{1}{10}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 252. Soal `c35416223bcfceec9bae1fe7`

Sebuah sekolah memiliki 300 siswa. Guru memilih sampel 30 siswa dengan cara mengambil 30 kartu sekaligus dari 300 kartu nama yang sudah dikocok. Rafi menghitung bahwa peluang dirinya termasuk dalam sampel adalah $\frac{1}{300}$ karena ada 300 siswa dan ia hanya satu orang.<br><br>Pernyataan yang tepat tentang perhitungan Rafi adalah ....

| Opsi | Isi |
|---|---|
| A | salah, peluangnya $\frac{1}{270}$ karena ada 270 siswa yang tidak terpilih |
| B | benar, peluangnya $\frac{1}{300}$ karena ada 300 siswa dan Rafi hanya satu orang |
| C | salah, peluangnya $\frac{1}{30}$ karena sampelnya berisi 30 siswa |
| D | salah, peluangnya $\frac{1}{10}$ karena semua siswa berpeluang sama dan 30 dari 300 siswa terpilih |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0973bbeb6a723bd61a3203dcc83abeacf117d47b8f142fc786848fec7d687519`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah sekolah memiliki 300 siswa. Guru memilih sampel 30 siswa dengan cara mengambil 30 kartu sekaligus dari 300 kartu nama yang sudah dikocok. Rafi menghitung bahwa peluang dirinya termasuk dalam sampel adalah $\frac{1}{300}$ karena ada 300 siswa dan ia hanya satu orang.

Pernyataan yang tepat tentang perhitungan Rafi adalah ....
Pilihan: A. salah, peluangnya $\frac{1}{270}$ karena ada 270 siswa yang tidak terpilih
B. benar, peluangnya $\frac{1}{300}$ karena ada 300 siswa dan Rafi hanya satu orang
C. salah, peluangnya $\frac{1}{30}$ karena sampelnya berisi 30 siswa
D. salah, peluangnya $\frac{1}{10}$ karena semua siswa berpeluang sama dan 30 dari 300 siswa terpilih
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 253. Soal `9b0b1902cbab016ba39d4773`

Guru memiliki roda putar dengan 10 juring yang sama besar, masing-masing bertuliskan satu nomor siswa dari 1 sampai 10. Untuk memilih sampel, roda diputar 3 kali (pemilihan dengan pengembalian, jadi nomor yang sama dapat muncul lebih dari sekali). Guru berharap mendapat 3 siswa yang berbeda.<br><br>Peluang ketiga nomor yang terpilih berbeda semua adalah ....

| Opsi | Isi |
|---|---|
| A | $\frac{7}{25}$ |
| B | $\frac{4}{5}$ |
| C | $\frac{9}{10}$ |
| D | $\frac{18}{25}$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `26341cb2b3d11557e89fea0298f8826d971a56802c8c41e43c54e54021b4c485`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Guru memiliki roda putar dengan 10 juring yang sama besar, masing-masing bertuliskan satu nomor siswa dari 1 sampai 10. Untuk memilih sampel, roda diputar 3 kali (pemilihan dengan pengembalian, jadi nomor yang sama dapat muncul lebih dari sekali). Guru berharap mendapat 3 siswa yang berbeda.

Peluang ketiga nomor yang terpilih berbeda semua adalah ....
Pilihan: A. $\frac{7}{25}$
B. $\frac{4}{5}$
C. $\frac{9}{10}$
D. $\frac{18}{25}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 254. Soal `36f3f86f316f10b6a3997489`

Sebuah kelompok (populasi) terdiri atas 4 siswa putra dan 2 siswa putri. Guru memilih 3 siswa secara acak tanpa pengembalian sebagai sampel. Sampel dianggap menyerupai populasi dalam hal komposisi jika berisi 2 siswa putra dan 1 siswa putri, yaitu perbandingan putra : putri sama dengan populasi (2 : 1).<br><br>Peluang sampel yang dipilih memiliki komposisi menyerupai populasi tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | $\frac{3}{5}$ |
| B | $\frac{4}{5}$ |
| C | $\frac{2}{5}$ |
| D | $\frac{1}{5}$ |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9c25f8faaf7e7cde8d0c100fee22985a586bb5ed9b92d645704569f01d11ac8e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kelompok (populasi) terdiri atas 4 siswa putra dan 2 siswa putri. Guru memilih 3 siswa secara acak tanpa pengembalian sebagai sampel. Sampel dianggap menyerupai populasi dalam hal komposisi jika berisi 2 siswa putra dan 1 siswa putri, yaitu perbandingan putra : putri sama dengan populasi (2 : 1).

Peluang sampel yang dipilih memiliki komposisi menyerupai populasi tersebut adalah ....
Pilihan: A. $\frac{3}{5}$
B. $\frac{4}{5}$
C. $\frac{2}{5}$
D. $\frac{1}{5}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 255. Soal `e038792325cc54d97ac9b07c`

Sinta ingin mengetahui persentase seluruh siswa di sekolahnya yang setuju jam masuk sekolah dimajukan 30 menit. Sekolah itu memiliki 600 siswa yang tercatat dalam satu daftar nomor induk.<br><br>Dari empat rancangan pemilihan sampel berikut, rancangan yang paling berpeluang menghasilkan sampel representatif beserta alasannya adalah ....

| Opsi | Isi |
|---|---|
| A | menyurvei 60 anggota ekskul olahraga, karena semua anggotanya siswa sekolah itu sehingga sampel tidak berkecenderungan |
| B | menyurvei 60 siswa yang pertama kali tiba di gerbang, karena mereka berasal dari berbagai kelas sehingga sampel tidak berkecenderungan |
| C | mengundi 60 nomor induk dari daftar seluruh siswa, karena setiap siswa berpeluang sama terpilih sehingga sampel tidak berkecenderungan |
| D | membuat survei di akun media sosial sekolah dan memakai 60 jawaban pertama, karena semua siswa boleh mengisinya sehingga sampel tidak berkecenderungan |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b63e6ea228e476734fecfbb314bd64d93faafe46afbdd6cb4a91d6c53aa8240c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Sinta ingin mengetahui persentase seluruh siswa di sekolahnya yang setuju jam masuk sekolah dimajukan 30 menit. Sekolah itu memiliki 600 siswa yang tercatat dalam satu daftar nomor induk.

Dari empat rancangan pemilihan sampel berikut, rancangan yang paling berpeluang menghasilkan sampel representatif beserta alasannya adalah ....
Pilihan: A. menyurvei 60 anggota ekskul olahraga, karena semua anggotanya siswa sekolah itu sehingga sampel tidak berkecenderungan
B. menyurvei 60 siswa yang pertama kali tiba di gerbang, karena mereka berasal dari berbagai kelas sehingga sampel tidak berkecenderungan
C. mengundi 60 nomor induk dari daftar seluruh siswa, karena setiap siswa berpeluang sama terpilih sehingga sampel tidak berkecenderungan
D. membuat survei di akun media sosial sekolah dan memakai 60 jawaban pertama, karena semua siswa boleh mengisinya sehingga sampel tidak berkecenderungan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 256. Soal `902abd9a0b5f8353f05fe238`

Seorang peneliti ingin mengetahui rata-rata uang saku mingguan seluruh siswa SMP Harapan (kelas VII, VIII, dan IX). Tiga cara pemilihan sampel yang direncanakan: (1) bertanya kepada 10 siswa yang paling sering terlihat membeli jajan di kantin; (2) bertanya kepada 30 siswa yang dipilih secara acak dari daftar seluruh siswa sekolah; (3) bertanya kepada 30 siswa kelas IX yang dipilih secara acak.<br><br>Urutan cara pemilihan dari yang paling berpeluang representatif ke yang paling kurang representatif adalah ....

| Opsi | Isi |
|---|---|
| A | (2), (1), (3) |
| B | (2), (3), (1) |
| C | (3), (2), (1) |
| D | (1), (3), (2) |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `72986db5c8825891e88bc798e61a8bc397dcb8068dc3ccc7a5b913aca5aa0309`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Seorang peneliti ingin mengetahui rata-rata uang saku mingguan seluruh siswa SMP Harapan (kelas VII, VIII, dan IX). Tiga cara pemilihan sampel yang direncanakan: (1) bertanya kepada 10 siswa yang paling sering terlihat membeli jajan di kantin; (2) bertanya kepada 30 siswa yang dipilih secara acak dari daftar seluruh siswa sekolah; (3) bertanya kepada 30 siswa kelas IX yang dipilih secara acak.

Urutan cara pemilihan dari yang paling berpeluang representatif ke yang paling kurang representatif adalah ....
Pilihan: A. (2), (1), (3)
B. (2), (3), (1)
C. (3), (2), (1)
D. (1), (3), (2)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 257. Soal `5a9f923ecaf4c2f5c7c6c2d6`

Rina memiliki roda putar yang terbagi menjadi empat juring yang sama besar, masing-masing ditulis angka 10, 20, 30, dan 40. Ia memilih sampel dengan memutar roda itu sebanyak tiga kali. Peluang ia mendapatkan sampel yang rata-ratanya paling besar 20 adalah ....

| Opsi | Isi |
|---|---|
| A | $\frac{7}{64}$ |
| B | $\frac{19}{64}$ |
| C | $\frac{5}{16}$ |
| D | $\frac{5}{32}$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b114918cf8a137407ac06d30e5ccbd7ff194517aa2abc8c3fb66cb77b3411181`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Rina memiliki roda putar yang terbagi menjadi empat juring yang sama besar, masing-masing ditulis angka 10, 20, 30, dan 40. Ia memilih sampel dengan memutar roda itu sebanyak tiga kali. Peluang ia mendapatkan sampel yang rata-ratanya paling besar 20 adalah ....
Pilihan: A. $\frac{7}{64}$
B. $\frac{19}{64}$
C. $\frac{5}{16}$
D. $\frac{5}{32}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 258. Soal `472ec84003fc6c7de6a805e9`

Dinas perpustakaan sebuah kota ingin mengetahui persentase warga kota yang memiliki kartu anggota perpustakaan.<br><br>Cara pemilihan sampel yang paling berpeluang menghasilkan sampel representatif adalah ....

| Opsi | Isi |
|---|---|
| A | menyurvei warga pada rumah nomor urut ke-4, 8, dan 12 di setiap RW seluruh kota |
| B | menyurvei warga yang mengisi formulir di situs web perpustakaan |
| C | menyurvei warga yang tinggal di sekitar gedung perpustakaan |
| D | menyurvei warga yang sedang antre meminjam buku di perpustakaan |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9611afe1c484a6c24b124818de7fc77ceecc876180cc18969bcbb346af4b78af`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Dinas perpustakaan sebuah kota ingin mengetahui persentase warga kota yang memiliki kartu anggota perpustakaan.

Cara pemilihan sampel yang paling berpeluang menghasilkan sampel representatif adalah ....
Pilihan: A. menyurvei warga pada rumah nomor urut ke-4, 8, dan 12 di setiap RW seluruh kota
B. menyurvei warga yang mengisi formulir di situs web perpustakaan
C. menyurvei warga yang tinggal di sekitar gedung perpustakaan
D. menyurvei warga yang sedang antre meminjam buku di perpustakaan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 259. Soal `47fbd770fda3989166ab20ab`

Sebuah toko daring memuat dua laporan kepuasan pelanggan. Laporan P: 80 pelanggan yang mengisi kuesioner di akun media sosial toko, 60 menyatakan puas. Laporan Q: 40 pelanggan yang dipilih secara acak oleh komputer dari daftar seluruh pelanggan, 22 menyatakan puas.<br><br>Persentase pelanggan puas yang paling dapat dipercaya sebagai gambaran seluruh pelanggan toko adalah ....

| Opsi | Isi |
|---|---|
| A | 65% |
| B | 45% |
| C | 75% |
| D | 55% |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `bceaa643f0ef4dd79cdbc78ee071728d1963cf30e6133c28f7c98bd423766cd3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah toko daring memuat dua laporan kepuasan pelanggan. Laporan P: 80 pelanggan yang mengisi kuesioner di akun media sosial toko, 60 menyatakan puas. Laporan Q: 40 pelanggan yang dipilih secara acak oleh komputer dari daftar seluruh pelanggan, 22 menyatakan puas.

Persentase pelanggan puas yang paling dapat dipercaya sebagai gambaran seluruh pelanggan toko adalah ....
Pilihan: A. 65%
B. 45%
C. 75%
D. 55%
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 260. Soal `33a1bcc44022946a7d81f769`

Pabrik lampu menghasilkan 5.000 lampu pada bulan Maret. Untuk mengetahui rata-rata lama menyala lampu produksi bulan Maret itu, seorang petugas menguji 100 lampu yang dipilih secara acak dari seluruh produksi tersebut.<br><br>Pernyataan yang tepat tentang populasi dan ukuran sampel penelitian tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | populasinya semua lampu produksi pabrik sepanjang tahun dan ukuran sampelnya 100 lampu |
| B | populasinya 5.000 lampu produksi bulan Maret dan ukuran sampelnya 100 lampu |
| C | populasinya 5.000 lampu produksi bulan Maret dan ukuran sampelnya 4.900 lampu |
| D | populasinya 100 lampu yang diuji dan ukuran sampelnya 5.000 lampu |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ea077846feedb924d9c7dfd90ea154955b430e4db3d7312a13ec55b625a95162`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Pabrik lampu menghasilkan 5.000 lampu pada bulan Maret. Untuk mengetahui rata-rata lama menyala lampu produksi bulan Maret itu, seorang petugas menguji 100 lampu yang dipilih secara acak dari seluruh produksi tersebut.

Pernyataan yang tepat tentang populasi dan ukuran sampel penelitian tersebut adalah ....
Pilihan: A. populasinya semua lampu produksi pabrik sepanjang tahun dan ukuran sampelnya 100 lampu
B. populasinya 5.000 lampu produksi bulan Maret dan ukuran sampelnya 100 lampu
C. populasinya 5.000 lampu produksi bulan Maret dan ukuran sampelnya 4.900 lampu
D. populasinya 100 lampu yang diuji dan ukuran sampelnya 5.000 lampu
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 261. Soal `079f4902a408ddb1e04c3134`

Seorang peneliti ingin mengetahui persentase pelajar SMP di Kota Medan yang rutin sarapan sebelum berangkat sekolah. Ia memilih secara acak 250 pelajar SMP di kota itu, dan 175 di antaranya rutin sarapan.<br><br>Pernyataan yang benar mengenai penelitian tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | populasinya semua pelajar SMP di Kota Medan, ukuran sampelnya 175, dan 70% sampel rutin sarapan |
| B | populasinya 250 pelajar yang dipilih, ukuran sampelnya 250, dan 70% sampel rutin sarapan |
| C | populasinya semua pelajar SMP di Kota Medan, ukuran sampelnya 250, dan 70% sampel rutin sarapan |
| D | populasinya semua pelajar SMP di Kota Medan, ukuran sampelnya 250, dan 30% sampel rutin sarapan |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `27446eba89b371e08154989419e9452727ba7bec57b1831a489fe1e959ec7b50`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Seorang peneliti ingin mengetahui persentase pelajar SMP di Kota Medan yang rutin sarapan sebelum berangkat sekolah. Ia memilih secara acak 250 pelajar SMP di kota itu, dan 175 di antaranya rutin sarapan.

Pernyataan yang benar mengenai penelitian tersebut adalah ....
Pilihan: A. populasinya semua pelajar SMP di Kota Medan, ukuran sampelnya 175, dan 70% sampel rutin sarapan
B. populasinya 250 pelajar yang dipilih, ukuran sampelnya 250, dan 70% sampel rutin sarapan
C. populasinya semua pelajar SMP di Kota Medan, ukuran sampelnya 250, dan 70% sampel rutin sarapan
D. populasinya semua pelajar SMP di Kota Medan, ukuran sampelnya 250, dan 30% sampel rutin sarapan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 262. Soal `7e22ee867c2ebcb6a0a49761`

Seorang guru membariskan 60 siswa menurut berat badannya, dari yang teringan sampai terberat, lalu memberi nomor 1 sampai 60. Untuk mengetahui rata-rata berat badan 60 siswa itu, ia mempertimbangkan tiga cara. Cara (1): memilih siswa bernomor 1 sampai 6. Cara (2): semua nomor dimasukkan ke kotak tertutup, dikocok, lalu 6 nomor diambil sekaligus. Cara (3): satu nomor diambil dari kotak, lalu 5 nomor berikutnya yang berurutan setelah nomor itu ikut dipilih.<br><br>Cara yang berpeluang besar menghasilkan sampel yang representatif dan alasannya adalah ....

| Opsi | Isi |
|---|---|
| A | cara (3), karena hanya satu nomor yang diundi sehingga lebih acak |
| B | cara (3), karena nomor yang berurutan menjamin data tersebar merata |
| C | cara (1), karena hanya memuat siswa dengan berat badan paling rendah |
| D | cara (2), karena setiap kelompok 6 siswa memiliki peluang terpilih yang sama |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `78e51ef7f07ab90f5d9f0e1f4b821e8937de29b2c30f79ea60180b8194359c59`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Seorang guru membariskan 60 siswa menurut berat badannya, dari yang teringan sampai terberat, lalu memberi nomor 1 sampai 60. Untuk mengetahui rata-rata berat badan 60 siswa itu, ia mempertimbangkan tiga cara. Cara (1): memilih siswa bernomor 1 sampai 6. Cara (2): semua nomor dimasukkan ke kotak tertutup, dikocok, lalu 6 nomor diambil sekaligus. Cara (3): satu nomor diambil dari kotak, lalu 5 nomor berikutnya yang berurutan setelah nomor itu ikut dipilih.

Cara yang berpeluang besar menghasilkan sampel yang representatif dan alasannya adalah ....
Pilihan: A. cara (3), karena hanya satu nomor yang diundi sehingga lebih acak
B. cara (3), karena nomor yang berurutan menjamin data tersebar merata
C. cara (1), karena hanya memuat siswa dengan berat badan paling rendah
D. cara (2), karena setiap kelompok 6 siswa memiliki peluang terpilih yang sama
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 263. Soal `b4f4e8d430c4acc1bd93d15c`

Nilai ulangan 10 siswa (populasi): 60, 65, 70, 70, 75, 75, 80, 80, 85, 90. Sampel P: 65, 75, 75, 85. Sampel Q: 80, 80, 85, 90.<br><br>Sampel yang lebih representatif terhadap populasi dan alasannya adalah ....

| Opsi | Isi |
|---|---|
| A | sampel P, karena rata-ratanya 75 sama dengan populasi dan sebarannya menyerupai populasi |
| B | sampel P dan Q sama baik, karena keduanya terdiri atas 4 data |
| C | sampel Q, karena rata-ratanya 83,75 lebih tinggi daripada populasi |
| D | sampel Q, karena memuat nilai tertinggi 90 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `bbad9d185316d08b35690779de0ea37614a0adafaf3dcf63ea8a01350d86fceb`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Nilai ulangan 10 siswa (populasi): 60, 65, 70, 70, 75, 75, 80, 80, 85, 90. Sampel P: 65, 75, 75, 85. Sampel Q: 80, 80, 85, 90.

Sampel yang lebih representatif terhadap populasi dan alasannya adalah ....
Pilihan: A. sampel P, karena rata-ratanya 75 sama dengan populasi dan sebarannya menyerupai populasi
B. sampel P dan Q sama baik, karena keduanya terdiri atas 4 data
C. sampel Q, karena rata-ratanya 83,75 lebih tinggi daripada populasi
D. sampel Q, karena memuat nilai tertinggi 90
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 264. Soal `08eb5bb68c050c1dd02627ee`

Sebuah sekolah memiliki 1.200 siswa. Untuk mengetahui banyak siswa yang bersepeda ke sekolah, dipilih secara acak sampel 90 siswa, dan 36 di antaranya bersepeda. Anggap sampel itu representatif.<br><br>Perkiraan banyak siswa di sekolah itu yang bersepeda adalah ....

| Opsi | Isi |
|---|---|
| A | 480 siswa |
| B | 720 siswa |
| C | 40 siswa |
| D | 36 siswa |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0ca3da09ad4174a2f803435ed720d0eababa1f2eb004a301655591b817b2961a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah sekolah memiliki 1.200 siswa. Untuk mengetahui banyak siswa yang bersepeda ke sekolah, dipilih secara acak sampel 90 siswa, dan 36 di antaranya bersepeda. Anggap sampel itu representatif.

Perkiraan banyak siswa di sekolah itu yang bersepeda adalah ....
Pilihan: A. 480 siswa
B. 720 siswa
C. 40 siswa
D. 36 siswa
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 265. Soal `bbe74e36b777f6ff576f7a13`

Sebuah kotak berisi 6 kartu bernomor 1, 2, 3, 4, 5, dan 6. Dua kartu diambil satu per satu secara acak dengan pengembalian, dan hasilnya dicatat berurutan.<br><br>Peluang kedua kartu yang terambil bernomor genap adalah ....

| Opsi | Isi |
|---|---|
| A | $\frac{1}{2}$ |
| B | $\frac{1}{4}$ |
| C | $\frac{1}{6}$ |
| D | $\frac{1}{5}$ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Terdapat 6 kartu, 3 di antaranya genap {2, 4, 6}. Peluang terambil kartu genap pada satu pengambilan adalah 3/6 = 1/2. Karena pengambilan dilakukan dengan pengembalian, kedua kejadian bersifat independen. Peluang kedua kartu genap adalah (1/2) * (1/2) = 1/4.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `da190b143ce6d2701c5c543a55ecf2c00d8a61709546f77ece23be8a5163d710`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2749 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2728 |
| 3 | success | valid / verified | applying | procedural | Easy | 2711 |

Run 1 — solusi: Total ruang sampel untuk dua pengambilan dengan pengembalian adalah 6 x 6 = 36. Kartu genap adalah {2, 4, 6} (ada 3 kartu). Peluang kartu pertama genap adalah 3/6 = 1/2. Peluang kartu kedua genap adalah 3/6 = 1/2. Karena kejadian independen, peluang keduanya genap adalah 1/2 x 1/2 = 1/4.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep peluang kejadian majemuk yang saling bebas (independen) dengan pengembalian dan menerapkannya untuk menghitung peluang gabungan.. Bukti: Dua kartu diambil satu per satu secara acak dengan pengembalian; Peluang kedua kartu yang terambil bernomor genap
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang aturan perkalian peluang untuk kejadian independen.. Bukti: Dua kartu diambil satu per satu secara acak dengan pengembalian
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena prosedurnya sangat langsung dan familiar bagi siswa kelas 9. Siswa hanya perlu mengidentifikasi jumlah kejadian yang diinginkan (genap-genap) dan total ruang sampel (6x6) atau menggunakan aturan perkalian peluang (1/2 x 1/2). Tidak ada kendala yang berinteraksi atau kebutuhan strategi non-rutin.. Bukti: Dua kartu diambil satu per satu secara acak dengan pengembalian; Peluang kedua kartu yang terambil bernomor genap

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang kejadian tunggal dan aturan perkalian peluang kejadian independen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang dengan pengembalian adalah standar kurikulum kelas 9. Prosedur penyelesaiannya bersifat rutin dan langsung. |

Run 2 — solusi: Total ruang sampel dengan pengembalian adalah 6 x 6 = 36. Kartu genap adalah {2, 4, 6} (ada 3). Peluang kartu pertama genap = 3/6 = 1/2. Peluang kartu kedua genap = 3/6 = 1/2. Karena independen, peluang keduanya genap = 1/2 x 1/2 = 1/4.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep peluang kejadian majemuk yang saling bebas (independen) dengan pengembalian. Ini adalah penerapan prosedur standar pada konteks rutin.. Bukti: Dua kartu diambil satu per satu secara acak dengan pengembalian; Peluang kedua kartu yang terambil bernomor genap
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip dasar peluang dan aturan perkalian untuk kejadian independen.. Bukti: Dua kartu diambil satu per satu secara acak dengan pengembalian
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 9. Prosedur penyelesaiannya jelas (menentukan ruang sampel atau mengalikan peluang masing-masing kejadian). Tidak ada kendala yang berinteraksi atau kebutuhan strategi nonrutin.. Bukti: Dua kartu diambil satu per satu secara acak dengan pengembalian; Peluang kedua kartu yang terambil bernomor genap

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang kejadian tunggal dan aturan perkalian peluang kejadian saling bebas. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang dengan pengembalian adalah standar kurikulum kelas 9. Soal ini tidak memerlukan integrasi kompleks atau penalaran mendalam, cukup pemahaman prosedur dasar. |

Run 3 — solusi: Total ruang sampel untuk dua pengambilan dengan pengembalian adalah 6 x 6 = 36. Kartu genap adalah {2, 4, 6} (ada 3). Peluang kartu pertama genap adalah 3/6 = 1/2. Peluang kartu kedua genap adalah 3/6 = 1/2. Karena independen, peluang keduanya genap adalah (1/2) x (1/2) = 1/4.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep peluang kejadian majemuk yang saling bebas (dengan pengembalian) untuk menentukan ruang sampel dan kejadian yang diinginkan.. Bukti: Dua kartu diambil satu per satu secara acak dengan pengembalian; Peluang kedua kartu yang terambil bernomor genap
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang aturan perkalian peluang untuk kejadian independen.. Bukti: Dua kartu diambil satu per satu secara acak dengan pengembalian
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 9. Prosedur penentuan ruang sampel (6x6) dan kejadian genap (3x3) sangat standar. Tidak ada kendala kompleks atau integrasi strategi yang menuntut.. Bukti: Dua kartu diambil satu per satu secara acak dengan pengembalian; Peluang kedua kartu yang terambil bernomor genap

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang kejadian tunggal dan aturan perkalian peluang. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang dengan pengembalian adalah standar kurikulum kelas 9. Soal ini tidak memerlukan penalaran non-rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4340`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan konsep peluang kejadian majemuk yang saling bebas (independen) dengan pengembalian untuk menghitung peluang gabungan dari dua kejadian sederhana.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang aturan perkalian peluang untuk kejadian independen.
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengidentifikasi peluang kejadian tunggal dan menerapkan aturan perkalian untuk kejadian independen. Tidak ada kendala yang berinteraksi atau kebutuhan strategi non-rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar peluang kejadian tunggal dan aturan perkalian peluang kejadian independen. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi peluang dengan pengembalian adalah standar kurikulum kelas 9. Prosedur penyelesaiannya bersifat rutin dan langsung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kotak berisi 6 kartu bernomor 1, 2, 3, 4, 5, dan 6. Dua kartu diambil satu per satu secara acak dengan pengembalian, dan hasilnya dicatat berurutan.

Peluang kedua kartu yang terambil bernomor genap adalah ....
Pilihan: A. $\frac{1}{2}$
B. $\frac{1}{4}$
C. $\frac{1}{6}$
D. $\frac{1}{5}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 266. Soal `427a57c88a533b8f1fe11f91`

Dita ingin mengetahui rata-rata lama waktu membaca buku per hari seluruh siswa di sekolahnya. Ia membagikan angket hanya kepada siswa yang sedang berada di perpustakaan pada jam istirahat.<br><br>Alasan sampel Dita kemungkinan besar tidak representatif adalah ....

| Opsi | Isi |
|---|---|
| A | jumlah siswa di perpustakaan pasti melebihi seluruh siswa sekolah |
| B | sampel adalah himpunan bagian populasi sehingga tidak boleh dipakai |
| C | angket tidak dapat dipakai untuk mengetahui waktu membaca |
| D | siswa di perpustakaan cenderung lebih gemar membaca sehingga pusat data sampel lebih tinggi daripada populasi |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a77feb5d238caf596084d28fc060032cc3f934b7aed48f310f474f30eda9df12`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Dita ingin mengetahui rata-rata lama waktu membaca buku per hari seluruh siswa di sekolahnya. Ia membagikan angket hanya kepada siswa yang sedang berada di perpustakaan pada jam istirahat.

Alasan sampel Dita kemungkinan besar tidak representatif adalah ....
Pilihan: A. jumlah siswa di perpustakaan pasti melebihi seluruh siswa sekolah
B. sampel adalah himpunan bagian populasi sehingga tidak boleh dipakai
C. angket tidak dapat dipakai untuk mengetahui waktu membaca
D. siswa di perpustakaan cenderung lebih gemar membaca sehingga pusat data sampel lebih tinggi daripada populasi
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 267. Soal `d2a614a6c77a05eeb09867d7`

Dari empat siswa, yaitu Ali, Beni, Citra, dan Dini, dipilih dua siswa secara acak tanpa pengembalian untuk menjadi sampel (urutan tidak diperhatikan).<br><br>Menurut definisi sampel acak, peluang sampel {Ali, Citra} terpilih adalah ....

| Opsi | Isi |
|---|---|
| A | $\frac{1}{4}$ |
| B | $\frac{1}{12}$ |
| C | $\frac{1}{6}$ |
| D | $\frac{1}{2}$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0a829615767f2c790a37d6dca44112fed33f176ea185011b2d096e36e98353dd`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Dari empat siswa, yaitu Ali, Beni, Citra, dan Dini, dipilih dua siswa secara acak tanpa pengembalian untuk menjadi sampel (urutan tidak diperhatikan).

Menurut definisi sampel acak, peluang sampel {Ali, Citra} terpilih adalah ....
Pilihan: A. $\frac{1}{4}$
B. $\frac{1}{12}$
C. $\frac{1}{6}$
D. $\frac{1}{2}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 268. Soal `fb325575c2be75fe33fcea74`

Berat sampel buah jeruk disajikan dalam diagram titik. Banyak titik pada kategori 0,2 kg adalah 3, pada 0,3 kg adalah 4, pada 0,4 kg adalah 2, dan pada 0,5 kg adalah 1.<br><br>Ukuran sampel dan rata-rata berat jeruk pada sampel tersebut adalah ....

| Opsi | Isi |
|---|---|
| A | 4 buah dan 0,31 kg |
| B | 10 buah dan 0,31 kg |
| C | 4 buah dan 0,35 kg |
| D | 10 buah dan 0,35 kg |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8adfdef216b7e5a689cc20a663323cb895e98dcc58d68513f194ebacec826219`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Berat sampel buah jeruk disajikan dalam diagram titik. Banyak titik pada kategori 0,2 kg adalah 3, pada 0,3 kg adalah 4, pada 0,4 kg adalah 2, dan pada 0,5 kg adalah 1.

Ukuran sampel dan rata-rata berat jeruk pada sampel tersebut adalah ....
Pilihan: A. 4 buah dan 0,31 kg
B. 10 buah dan 0,31 kg
C. 4 buah dan 0,35 kg
D. 10 buah dan 0,35 kg
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 269. Soal `6b5cb48019aa2b07a65c830a`

Dari 800 siswa sebuah sekolah dipilih secara acak 40 siswa, dan rata-rata tinggi mereka 158 cm.<br><br>Kesimpulan yang paling tepat tentang rata-rata tinggi seluruh siswa sekolah itu adalah ....

| Opsi | Isi |
|---|---|
| A | tidak dapat diperkirakan sama sekali dari sampel itu |
| B | pasti lebih dari 158 cm, karena populasi lebih banyak daripada sampel |
| C | kemungkinan besar mendekati 158 cm, tetapi belum tentu tepat 158 cm |
| D | pasti tepat 158 cm, karena sampelnya acak |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menyimpulkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `789f0fb37f415ad37193a4422343cb386a7f0eb51d0693a591022b0fec6ce47a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Dari 800 siswa sebuah sekolah dipilih secara acak 40 siswa, dan rata-rata tinggi mereka 158 cm.

Kesimpulan yang paling tepat tentang rata-rata tinggi seluruh siswa sekolah itu adalah ....
Pilihan: A. tidak dapat diperkirakan sama sekali dari sampel itu
B. pasti lebih dari 158 cm, karena populasi lebih banyak daripada sampel
C. kemungkinan besar mendekati 158 cm, tetapi belum tentu tepat 158 cm
D. pasti tepat 158 cm, karena sampelnya acak
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 270. Soal `bc16af0f732c8f90b41e9a1d`

Pada upacara bendera, siswa berbaris dalam 12 barisan dan setiap barisan terdiri atas 30 siswa. Seorang peneliti menyurvei siswa yang menempati urutan ke-3, 6, dan 9 di setiap barisan.<br><br>Persentase ukuran sampel terhadap ukuran populasi adalah ....

| Opsi | Isi |
|---|---|
| A | 1% |
| B | 36% |
| C | 12% |
| D | 10% |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `39ae18c7a666bd4baf9deed7680030d09de9588195257f826bb6436ae8533fa1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada upacara bendera, siswa berbaris dalam 12 barisan dan setiap barisan terdiri atas 30 siswa. Seorang peneliti menyurvei siswa yang menempati urutan ke-3, 6, dan 9 di setiap barisan.

Persentase ukuran sampel terhadap ukuran populasi adalah ....
Pilihan: A. 1%
B. 36%
C. 12%
D. 10%
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `needs_ai_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
