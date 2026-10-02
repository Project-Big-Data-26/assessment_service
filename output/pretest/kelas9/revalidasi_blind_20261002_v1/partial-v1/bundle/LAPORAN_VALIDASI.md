# Validasi ulang soal kelas 9 — Gemini blind N=3 dan diagnostik IndoBERT

**Batch belum selesai:** 0/126 run awal sukses; 0 item tercatat membutuhkan adjudikasi setelah run lengkap. Distribusi berikut masih sementara; item tanpa keputusan ditampilkan sebagai undecided. Provider berhenti karena kuota harian; checkpoint kerja dapat dilanjutkan saat kuota tersedia.

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v7-blind-smp9-key-verified`. Rubrik: `math-rubric-3x4x3-v5-smp9-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 9 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan bukan keputusan ahli manusia.

Checkpoint dikunci dengan SHA-256 sebelum pemeriksaan scope IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Model SD berada di luar cakupan kelas 9, sehingga seluruh head abstain dan tidak menghasilkan ukuran agreement dengan label blind.

Jumlah soal: 42; distribusi label advisory: `{"mathCognitiveDomain": {"undecided": 42, "knowing": 0, "applying": 0, "reasoning": 0}, "knowledgeDimension": {"undecided": 42, "factual": 0, "conceptual": 0, "procedural": 0, "metacognitive": 0}, "intendedDifficulty": {"undecided": 42, "Easy": 0, "Medium": 0, "Hard": 0}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"knowing": 0, "applying": 0, "reasoning": 0}, "knowledgeDimension": {"factual": 0, "conceptual": 0, "procedural": 0, "metacognitive": 0}, "intendedDifficulty": {"Easy": 0, "Medium": 0, "Hard": 0}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"llm_retry_or_manual_review": 42}`.
Run awal sukses: 0/126; adjudikasi: 0; token sukses tercatat: 0.

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

Untuk kelas 9, encoder dan head IndoBERT tidak dijalankan karena scope model hanya kelas 1–6. Probabilitas kosong, label/confidence/entropy null, dan action abstain berasal dari pemeriksaan scope runtime. Suara Gemini adalah bukti penilaian advisory, bukan probabilitas IndoBERT.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

Model IndoBERT lama hanya mendukung SD kelas 1–6. Untuk kelas 9, diagnostik mengembalikan `out_of_scope` dan `abstain`: label, confidence, dan entropy null serta probabilitas kosong. Label advisory mengikuti Gemini blind dengan rubrik SMP kelas 9. Tidak ada inferensi SD yang dipaksakan sebagai prediksi SMP.

## 1. Soal `8af0a2ca82017a432c92902d`

Diketahui keliling sebuah segitiga sama kaki adalah 48 cm. Tentukan model matematika yang menghubungkan antara keliling dan panjang sisi segitiga tersebut.

| Opsi | Isi |
|---|---|
| A | $x + y = 48$ |
| B | $2x + y = 48$ |
| C | $x + 2y = 48$ |
| D | $2x + 2y = 48$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8dcd4892e97e22b81f55c5bd58747ff78c0b139fb72bff17e415d6df26ed31a6`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | failed | — / — | — | — | — | 0 |

Run 1 gagal: `ClientError:429`; tidak dihitung sebagai suara.

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

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
Soal: Diketahui keliling sebuah segitiga sama kaki adalah 48 cm. Tentukan model matematika yang menghubungkan antara keliling dan panjang sisi segitiga tersebut.
Pilihan: A. $x + y = 48$
B. $2x + y = 48$
C. $x + 2y = 48$
D. $2x + 2y = 48$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `e7003333bef697d763016f2e`

Nyatakan pernyataan berikut ke dalam bentuk persamaan linear dua variabel.<br><br>Diketahui harga tiket film di suatu bioskop Rp35.000,00. y menyatakan pendapatan dari hasil penjualan tiket dan x menyatakan banyak tiket terjual.

| Opsi | Isi |
|---|---|
| A | $y = \frac{x}{35.000}$ |
| B | $y = 35.000x$ |
| C | $x = 35.000y$ |
| D | $y = 35.000 + x$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ac5c8b5a8a8f810654e96a77be3cdb2d8f37b8ff433956519fa8ae67e365aefc`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

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
Soal: Nyatakan pernyataan berikut ke dalam bentuk persamaan linear dua variabel.

Diketahui harga tiket film di suatu bioskop Rp35.000,00. y menyatakan pendapatan dari hasil penjualan tiket dan x menyatakan banyak tiket terjual.
Pilihan: A. $y = \frac{x}{35.000}$
B. $y = 35.000x$
C. $x = 35.000y$
D. $y = 35.000 + x$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `0b4b98faa7f553833f0db971`

Suatu toko alat lukis menjual 40 kuas lukis. Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.<br><br>Jika uang yang didapat oleh toko tersebut Rp1.103.000,00, maka berapa banyak masing-masing jenis kuas lukis yang terjual?

| Opsi | Isi |
|---|---|
| A | 27 kuas lukis jenis I dan 13 kuas lukis jenis II |
| B | 20 kuas lukis jenis I dan 20 kuas lukis jenis II |
| C | 13 kuas lukis jenis I dan 27 kuas lukis jenis II |
| D | 15 kuas lukis jenis I dan 25 kuas lukis jenis II |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `28d46a185734f7cafe26bcf65adeb6a16ee3748d0d3b37766e75118228d25ead`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

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
Soal: Suatu toko alat lukis menjual 40 kuas lukis. Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.

Jika uang yang didapat oleh toko tersebut Rp1.103.000,00, maka berapa banyak masing-masing jenis kuas lukis yang terjual?
Pilihan: A. 27 kuas lukis jenis I dan 13 kuas lukis jenis II
B. 20 kuas lukis jenis I dan 20 kuas lukis jenis II
C. 13 kuas lukis jenis I dan 27 kuas lukis jenis II
D. 15 kuas lukis jenis I dan 25 kuas lukis jenis II
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `a4219a3c217e0979ca28b57e`

Wayan pergi ke toko kue tradisional untuk membeli kue basung (kue yang berasal dari Sumatera Barat) dan kue mendut (kue yang berasal dari Jawa Tengah). Dia membeli satu kue basung dan tiga kue mendut dengan harga seluruhnya Rp13.500,00. Di toko yang sama, Aisyah membeli dua kue basung dan lima kue mendut dengan harga seluruhnya Rp24.000,00.<br><br>Berapa harga tiga kue mendut dan tujuh kue basung?

| Opsi | Isi |
|---|---|
| A | Rp42.000,00 |
| B | Rp34.500,00 |
| C | Rp37.500,00 |
| D | Rp40.500,00 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2d7b3e17b4ad6777bc1f2b7f3fbfbc488fc57f69dce7c524fb08373840b4ddab`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

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
Soal: Wayan pergi ke toko kue tradisional untuk membeli kue basung (kue yang berasal dari Sumatera Barat) dan kue mendut (kue yang berasal dari Jawa Tengah). Dia membeli satu kue basung dan tiga kue mendut dengan harga seluruhnya Rp13.500,00. Di toko yang sama, Aisyah membeli dua kue basung dan lima kue mendut dengan harga seluruhnya Rp24.000,00.

Berapa harga tiga kue mendut dan tujuh kue basung?
Pilihan: A. Rp42.000,00
B. Rp34.500,00
C. Rp37.500,00
D. Rp40.500,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `4b2524b8440c37d72e127b02`

Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg. Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.<br><br>Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?

| Opsi | Isi |
|---|---|
| A | 9,45 kali pengangkutan |
| B | 10 kali pengangkutan |
| C | 9 kali pengangkutan |
| D | 11 kali pengangkutan |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `eef8fab116137ab5c99fd256d96b63b7e5693223a5887bc6636776164b1cd0dd`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Menyelesaikan Masalah terkait Pertidaksamaan Linier Satu Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg. Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.

Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?
Pilihan: A. 9,45 kali pengangkutan
B. 10 kali pengangkutan
C. 9 kali pengangkutan
D. 11 kali pengangkutan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `6d6cb72cedbdc46857aa2701`

Titik P(2,-1) dan R(6,2) merupakan titik sudut yang berhadapan pada sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat, maka persamaan garis yang melalui titik Q dan S adalah ....

| Opsi | Isi |
|---|---|
| A | 4x + 3y - 14 = 0 |
| B | 3x + 4y - 14 = 0 |
| C | 4x - 3y + 14 = 0 |
| D | 3x - 4y + 33 = 0 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0649161cd843360a799331c908701ac43a0c5a716f588e2c910d050b0bba9e61`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pengertian Kemiringan
Tipe soal: multiple_choice
Stimulus: -
Soal: Titik P(2,-1) dan R(6,2) merupakan titik sudut yang berhadapan pada sisi persegi panjang PQRS yang sejajar dengan sumbu-sumbu koordinat, maka persamaan garis yang melalui titik Q dan S adalah ....
Pilihan: A. 4x + 3y - 14 = 0
B. 3x + 4y - 14 = 0
C. 4x - 3y + 14 = 0
D. 3x - 4y + 33 = 0
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `d0b943d7f97005ee05dfe7b2`

Dapatkah kita membuat jaring-jaring bangun ruang bola?

| Opsi | Isi |
|---|---|
| A | Hanya kerucut dan tabung yang bisa dibuat jaring-jaringnya, bola tidak |
| B | Tidak, sama sekali tidak mungkin dibuat |
| C | Ya, tetapi hasilnya selalu berbentuk persegi panjang |
| D | Ya, jaring-jaring bangun ruang bola dapat dibuat |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e321e5c4060dc48e7b1d25aea59c13da8dc31333e4563871b066b46bbbea8949`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Klasifikasi Bangun Ruang dan Jaring-Jaring
Tipe soal: multiple_choice
Stimulus: -
Soal: Dapatkah kita membuat jaring-jaring bangun ruang bola?
Pilihan: A. Hanya kerucut dan tabung yang bisa dibuat jaring-jaringnya, bola tidak
B. Tidak, sama sekali tidak mungkin dibuat
C. Ya, tetapi hasilnya selalu berbentuk persegi panjang
D. Ya, jaring-jaring bangun ruang bola dapat dibuat
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `394ec3b5c5b98c434a4cedde`

Apa yang dimaksud dengan jaring-jaring bangun ruang?

| Opsi | Isi |
|---|---|
| A | Kumpulan rusuk yang membentuk kerangka luar suatu bangun ruang |
| B | Bagian permukaan bangun ruang yang terlihat dari luar saja |
| C | Bentuk tiga dimensi yang menunjukkan besar ruang yang ditempati suatu bangun ruang |
| D | Bentuk dua dimensi yang dapat digambar, dipotong, dan dirangkai sedemikian rupa sehingga menjadi sebuah bangun tiga dimensi |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b4cfab5f8d06a65f376ac625b4a7bc6d19bd0ae909af2e14bd6f37322b4fb0ed`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Klasifikasi Bangun Ruang dan Jaring-Jaring
Tipe soal: multiple_choice
Stimulus: -
Soal: Apa yang dimaksud dengan jaring-jaring bangun ruang?
Pilihan: A. Kumpulan rusuk yang membentuk kerangka luar suatu bangun ruang
B. Bagian permukaan bangun ruang yang terlihat dari luar saja
C. Bentuk tiga dimensi yang menunjukkan besar ruang yang ditempati suatu bangun ruang
D. Bentuk dua dimensi yang dapat digambar, dipotong, dan dirangkai sedemikian rupa sehingga menjadi sebuah bangun tiga dimensi
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 9. Soal `ee45c96e4346ffea193e7a99`

Sebuah kotak pensil terbuat dari logam dengan dimensi 20 cm × 10 cm × 3 cm. Hitunglah berapa luas logam yang dibutuhkan untuk membuat kotak pensil tersebut.

| Opsi | Isi |
|---|---|
| A | 580 cm² |
| B | 600 cm² |
| C | 520 cm² |
| D | 290 cm² |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4b3e7b6fe10d4c943429d00f8e0e315e5a7be70a5786e6921e860a0226253418`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Luas Permukaan Bangun Ruang Sisi Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kotak pensil terbuat dari logam dengan dimensi 20 cm × 10 cm × 3 cm. Hitunglah berapa luas logam yang dibutuhkan untuk membuat kotak pensil tersebut.
Pilihan: A. 580 cm²
B. 600 cm²
C. 520 cm²
D. 290 cm²
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `27c5fab7664c58cab4d858b0`

Temukan luas permukaan kubus yang memiliki panjang sisi sebagai berikut. ⓐ 0,23 m

| Opsi | Isi |
|---|---|
| A | 0,0529 m² |
| B | 1,38 m² |
| C | 0,3174 m² |
| D | 0,012167 m² |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `095d4cbea76c75bf351eb837c1421dda2279d728956ffb96d170c2e69b24c1c7`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Luas Permukaan Bangun Ruang Sisi Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Temukan luas permukaan kubus yang memiliki panjang sisi sebagai berikut. ⓐ 0,23 m
Pilihan: A. 0,0529 m²
B. 1,38 m²
C. 0,3174 m²
D. 0,012167 m²
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `aee8fd25cf246c58a370058e`

Sebuah balok memiliki ukuran panjang 5, lebar 3, dan tinggi 7. Jika balok tersebut diubah ukurannya dengan skala 4, maka tentukan volume balok setelah diubah.

| Opsi | Isi |
|---|---|
| A | 420 satuan kubik |
| B | 1.680 satuan kubik |
| C | 105 satuan kubik |
| D | 6.720 satuan kubik |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `98f03295dad0ed8dcde8b257a8f0c38097f10f229a3bd41f7319ae2922717246`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Volume Bangun Ruang Sisi Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah balok memiliki ukuran panjang 5, lebar 3, dan tinggi 7. Jika balok tersebut diubah ukurannya dengan skala 4, maka tentukan volume balok setelah diubah.
Pilihan: A. 420 satuan kubik
B. 1.680 satuan kubik
C. 105 satuan kubik
D. 6.720 satuan kubik
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 12. Soal `bc9eda46aa2fecb0da3798d8`

Bagaimana kaitan antara volume limas dan prisma yang keduanya memiliki alas dan tinggi yang sama?

| Opsi | Isi |
|---|---|
| A | Volume limas adalah setengah dari volume prisma |
| B | Volume limas adalah tiga kali volume prisma |
| C | Volume limas tersebut adalah sepertiga dari volume prisma |
| D | Volume limas sama dengan volume prisma |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0c181b96d32afd91ccb4debebe64a1267f9c1aac0eec8a414d291a32b94b57bf`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Volume Bangun Ruang Sisi Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Bagaimana kaitan antara volume limas dan prisma yang keduanya memiliki alas dan tinggi yang sama?
Pilihan: A. Volume limas adalah setengah dari volume prisma
B. Volume limas adalah tiga kali volume prisma
C. Volume limas tersebut adalah sepertiga dari volume prisma
D. Volume limas sama dengan volume prisma
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 13. Soal `b0484eaccca405ba34c3f428`

Untuk tiap-tiap lingkaran yang diketahui r (panjang jari-jari) atau d (panjang diameter) berikut, tentukan keliling dan luasnya! ⓐ r = 12 cm

| Opsi | Isi |
|---|---|
| A | Keliling 75,36 cm dan luas 75,36 cm² |
| B | Keliling 452,16 cm dan luas 75,36 cm² |
| C | Keliling 75,36 cm dan luas 452,16 cm² |
| D | Keliling 37,68 cm dan luas 452,16 cm² |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `badb9952eedf5db2c534a65a39b865e5a4b85c5bd17e97e62ab727636d1f2e10`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Lingkaran
Tipe soal: multiple_choice
Stimulus: -
Soal: Untuk tiap-tiap lingkaran yang diketahui r (panjang jari-jari) atau d (panjang diameter) berikut, tentukan keliling dan luasnya! ⓐ r = 12 cm
Pilihan: A. Keliling 75,36 cm dan luas 75,36 cm²
B. Keliling 452,16 cm dan luas 75,36 cm²
C. Keliling 75,36 cm dan luas 452,16 cm²
D. Keliling 37,68 cm dan luas 452,16 cm²
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `ce529c7a884ca9ebbfb36e54`

Perbandingan antara keliling dan diameter suatu lingkaran adalah sekitar ____.

| Opsi | Isi |
|---|---|
| A | 22 |
| B | 3,14 (atau 22/7) |
| C | 3,41 |
| D | 2 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `33723f89d1d0e03419e781556162f9965cfd7783df87a2904fe750e7eed35cc3`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Lingkaran
Tipe soal: multiple_choice
Stimulus: -
Soal: Perbandingan antara keliling dan diameter suatu lingkaran adalah sekitar ____.
Pilihan: A. 22
B. 3,14 (atau 22/7)
C. 3,41
D. 2
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 15. Soal `487ffef7f793443d4d651476`

Untuk memperingati ulang tahun Gilang, ibunya membuat nasi tumpeng yang disusun sedemikian rupa sehingga nasinya berbentuk kerucut dengan diameter 20 cm. Tinggi nasi dengan bentuk kerucut ini sekitar 35 cm. Jika nasi kerucut ini ingin ditutupi dengan daun pisang, berapa luas daun pisang yang akan dibutuhkan?

| Opsi | Isi |
|---|---|
| A | ≈1.456,96 cm² |
| B | ≈2.285,92 cm² |
| C | ≈1.142,96 cm² |
| D | ≈1.099 cm² |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5d037f427573c6e035be42bb0e907e6bbf8d516423d5612c524d5eeac4f58186`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Luas Permukaan Bangun Ruang Sisi Lengkung
Tipe soal: multiple_choice
Stimulus: -
Soal: Untuk memperingati ulang tahun Gilang, ibunya membuat nasi tumpeng yang disusun sedemikian rupa sehingga nasinya berbentuk kerucut dengan diameter 20 cm. Tinggi nasi dengan bentuk kerucut ini sekitar 35 cm. Jika nasi kerucut ini ingin ditutupi dengan daun pisang, berapa luas daun pisang yang akan dibutuhkan?
Pilihan: A. ≈1.456,96 cm²
B. ≈2.285,92 cm²
C. ≈1.142,96 cm²
D. ≈1.099 cm²
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `efbc889b95676e6e2d913479`

Apa keterkaitan antara luas permukaan bola dan luas lingkaran yang memiliki jari-jari yang sama.

| Opsi | Isi |
|---|---|
| A | Luas permukaan bola sama dengan luas lingkaran yang memiliki jari-jari yang sama |
| B | Luas permukaan bola sama dengan dua kali luas lingkaran yang memiliki jari-jari yang sama |
| C | Luas permukaan bola sama dengan setengah luas lingkaran yang memiliki jari-jari yang sama |
| D | Luas permukaan bola sama dengan empat kali luas lingkaran yang memiliki jari-jari yang sama |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ac2a42dfed68f2a9e31dfac8966e1e2471dd9e52f325e190e0edcafddf0b2ab5`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Luas Permukaan Bangun Ruang Sisi Lengkung
Tipe soal: multiple_choice
Stimulus: -
Soal: Apa keterkaitan antara luas permukaan bola dan luas lingkaran yang memiliki jari-jari yang sama.
Pilihan: A. Luas permukaan bola sama dengan luas lingkaran yang memiliki jari-jari yang sama
B. Luas permukaan bola sama dengan dua kali luas lingkaran yang memiliki jari-jari yang sama
C. Luas permukaan bola sama dengan setengah luas lingkaran yang memiliki jari-jari yang sama
D. Luas permukaan bola sama dengan empat kali luas lingkaran yang memiliki jari-jari yang sama
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 17. Soal `1ef6efc5863938a14b737897`

Berapa liter gas bumi yang dapat ditampung dengan truk yang memiliki tabung penyimpanan besar seperti Gambar dengan diameter 2 meter dan panjang 12 meter?

| Opsi | Isi |
|---|---|
| A | 36.000 liter |
| B | 150.720 liter |
| C | 37.680 liter |
| D | 37,68 liter |

![Gambar sumber soal 17](<../../../images/kelas9_crop-s0011-truk-gas.png>)


Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas9_crop-s0011-truk-gas.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `81d50e566a057b01efe572c6bed5fb1af51195f12a5bb08ffb57283346305ac9`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Volume Bangun Ruang Sisi Lengkung
Tipe soal: multiple_choice
Stimulus: -
Soal: Berapa liter gas bumi yang dapat ditampung dengan truk yang memiliki tabung penyimpanan besar seperti Gambar dengan diameter 2 meter dan panjang 12 meter?
Pilihan: A. 36.000 liter
B. 150.720 liter
C. 37.680 liter
D. 37,68 liter
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `a0c228d869728c3140dece74`

Apa hubungan antara volume kerucut dan tabung yang memiliki jari-jari dan tinggi yang sama?

| Opsi | Isi |
|---|---|
| A | Volume kerucut sama dengan sepertiga volume tabung |
| B | Volume kerucut adalah tiga kali volume tabung |
| C | Volume kerucut sama dengan volume tabung |
| D | Volume kerucut adalah setengah volume tabung |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menganalisis']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d39f57959b694d633a92295896db4ac1a30dc59ff658f0cb45d39c454b465980`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Volume Bangun Ruang Sisi Lengkung
Tipe soal: multiple_choice
Stimulus: -
Soal: Apa hubungan antara volume kerucut dan tabung yang memiliki jari-jari dan tinggi yang sama?
Pilihan: A. Volume kerucut sama dengan sepertiga volume tabung
B. Volume kerucut adalah tiga kali volume tabung
C. Volume kerucut sama dengan volume tabung
D. Volume kerucut adalah setengah volume tabung
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 19. Soal `4088b8d020de84282c07a2b3`

Sebuah tangki air berisi 2.225 liter air. Pada siang hari 975 liter 325 ml air dipompa keluar dari tangki. Berapa banyak air yang tersisa di tangki?

| Opsi | Isi |
|---|---|
| A | 1.250 liter 325 ml |
| B | 1.249 liter 675 ml |
| C | 1.249 liter 325 ml |
| D | 1.250 liter 675 ml |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d667150af038b2b0b31aeaad5b6405567fcca77c4407ee098ad9848a664b9f21`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Pengukuran Volume
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah tangki air berisi 2.225 liter air. Pada siang hari 975 liter 325 ml air dipompa keluar dari tangki. Berapa banyak air yang tersisa di tangki?
Pilihan: A. 1.250 liter 325 ml
B. 1.249 liter 675 ml
C. 1.249 liter 325 ml
D. 1.250 liter 675 ml
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `0d61de45054218c7d9af6710`

Bapak memiliki kawat sepanjang 60 cm. Dengan menggunakan kawat tersebut, Bapak ingin membuat kerangka berbentuk persegi panjang. Bantulah beliau membuat gambar kerangka tersebut.<br><br>Manakah yang menghasilkan kerangka yang terluas?

| Opsi | Isi |
|---|---|
| A | Panjang 15 cm dan lebar 15 cm (luas 225 cm²) |
| B | Panjang 25 cm dan lebar 5 cm (luas 125 cm²) |
| C | Panjang 20 cm dan lebar 10 cm (luas 200 cm²) |
| D | Panjang 18 cm dan lebar 12 cm (luas 216 cm²) |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9c5f1f859a86aefa349f91c6bbe063d6989e6d7260389972ababaf3548bddae5`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Hubungan Keliling dan Luas Daerah Bangun Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Bapak memiliki kawat sepanjang 60 cm. Dengan menggunakan kawat tersebut, Bapak ingin membuat kerangka berbentuk persegi panjang. Bantulah beliau membuat gambar kerangka tersebut.

Manakah yang menghasilkan kerangka yang terluas?
Pilihan: A. Panjang 15 cm dan lebar 15 cm (luas 225 cm²)
B. Panjang 25 cm dan lebar 5 cm (luas 125 cm²)
C. Panjang 20 cm dan lebar 10 cm (luas 200 cm²)
D. Panjang 18 cm dan lebar 12 cm (luas 216 cm²)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 21. Soal `e81a665e38e1781b745677fd`

Sebuah kubus terletak pada (F,1) dan akan dipindahkan ke (D,2). Kubus ini tidak boleh diangkat, tetapi direbahkan ke salah satu sisi tegaknya. Panjangnya rusuk kubus sama dengan jarak antara garis-garis horizontal dan garis-garis vertikal pada sistem berpetak yang digunakan.<br><br>Berapa kali kubus tersebut direbahkan untuk mencapai tujuannya?

| Opsi | Isi |
|---|---|
| A | 2 kali |
| B | 4 kali |
| C | 5 kali |
| D | 3 kali |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `eb7854bb1d8f58f1a834cfe4bc65d9e0836f2bb55ea49f932f17a3b202089e7f`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Lokasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah kubus terletak pada (F,1) dan akan dipindahkan ke (D,2). Kubus ini tidak boleh diangkat, tetapi direbahkan ke salah satu sisi tegaknya. Panjangnya rusuk kubus sama dengan jarak antara garis-garis horizontal dan garis-garis vertikal pada sistem berpetak yang digunakan.

Berapa kali kubus tersebut direbahkan untuk mencapai tujuannya?
Pilihan: A. 2 kali
B. 4 kali
C. 5 kali
D. 3 kali
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 22. Soal `bba0d92faac1dbb90cd622ef`

Diketahui segitiga ABC dengan A(0,-3), B(2,2) dan C(4,5) ditranslasikan sehingga bayangannya adalah A'(-2,1). Tentukan translasinya serta koordinat titik B' dan C'.

| Opsi | Isi |
|---|---|
| A | Translasi $\binom{2}{-4}$, B'(4,-2), C'(6,1) |
| B | Translasi $\binom{-2}{4}$, B'(0,6), C'(2,9) |
| C | Translasi $\binom{4}{-2}$, B'(6,0), C'(8,3) |
| D | Translasi $\binom{-2}{4}$, B'(4,-2), C'(6,1) |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1b28c487fa6da1ba7a081c501115c024b0a0ed2a651fb971d0889bab179da38d`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Translasi (Pergeseran)
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui segitiga ABC dengan A(0,-3), B(2,2) dan C(4,5) ditranslasikan sehingga bayangannya adalah A'(-2,1). Tentukan translasinya serta koordinat titik B' dan C'.
Pilihan: A. Translasi $\binom{2}{-4}$, B'(4,-2), C'(6,1)
B. Translasi $\binom{-2}{4}$, B'(0,6), C'(2,9)
C. Translasi $\binom{4}{-2}$, B'(6,0), C'(8,3)
D. Translasi $\binom{-2}{4}$, B'(4,-2), C'(6,1)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 23. Soal `944be36e182518ad72be95aa`

Bayangan titik A(-2,5) oleh $\binom{-4}{3}$ adalah …

| Opsi | Isi |
|---|---|
| A | A'(-6,8) |
| B | A'(-6,-8) |
| C | A'(2,2) |
| D | A'(-2,8) |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `aae23ec4afb2a57f3e1ebf8bb7b2d59c827f331e580a80e7c75ac6fb6aabe9dc`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Translasi (Pergeseran)
Tipe soal: multiple_choice
Stimulus: -
Soal: Bayangan titik A(-2,5) oleh $\binom{-4}{3}$ adalah …
Pilihan: A. A'(-6,8)
B. A'(-6,-8)
C. A'(2,2)
D. A'(-2,8)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 24. Soal `34e4b41c04e7c9417acca5ce`

Titik (2,-3) direfleksikan terhadap garis y=x. Tentukan bayangannya.

| Opsi | Isi |
|---|---|
| A | (2,3) |
| B | (-3,2) |
| C | (3,-2) |
| D | (2,1) |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `24152f993c7d9856ddbfc3ff25d1a54bb281c9b3cbcbf4684e3ec3cda83d420a`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Refleksi (Pencerminan)
Tipe soal: multiple_choice
Stimulus: -
Soal: Titik (2,-3) direfleksikan terhadap garis y=x. Tentukan bayangannya.
Pilihan: A. (2,3)
B. (-3,2)
C. (3,-2)
D. (2,1)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 25. Soal `e23d76dc5ff2cda98f0f4ccc`

Titik (2,-3) direfleksikan terhadap sumbu x. Tentukan bayangannya.

| Opsi | Isi |
|---|---|
| A | (2,3) |
| B | (-2,3) |
| C | (-2,-3) |
| D | (4,-3) |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `61aa35a6508b9e456843796171e0a57565a4f01789388be687885a06d9968669`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Refleksi (Pencerminan)
Tipe soal: multiple_choice
Stimulus: -
Soal: Titik (2,-3) direfleksikan terhadap sumbu x. Tentukan bayangannya.
Pilihan: A. (2,3)
B. (-2,3)
C. (-2,-3)
D. (4,-3)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 26. Soal `078d6a87b40b143dc0e0683c`

Diketahui segi empat KLMN dengan titik sudutnya di K(1,2), L(6,4), M(8,-3) dan N(3,-1). Tentukan bayangan hasil rotasi 180º terhadap titik pusat O(0,0). Gambarkan segi empat KLMN beserta bayangannya pada bidang koordinat.

| Opsi | Isi |
|---|---|
| A | K'(-1,-2), L'(-6,-4), M'(-8,3), N'(-3,1) |
| B | K'(-2,1), L'(-4,6), M'(3,8), N'(1,3) |
| C | K'(1,-2), L'(6,-4), M'(8,3), N'(3,1) |
| D | K'(-1,2), L'(-6,4), M'(-8,-3), N'(-3,-1) |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3ea6717225cfeab735d99a168159be1de9dd7a3e9c2075f1f372f85d2f16d071`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Rotasi (Perputaran)
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui segi empat KLMN dengan titik sudutnya di K(1,2), L(6,4), M(8,-3) dan N(3,-1). Tentukan bayangan hasil rotasi 180º terhadap titik pusat O(0,0). Gambarkan segi empat KLMN beserta bayangannya pada bidang koordinat.
Pilihan: A. K'(-1,-2), L'(-6,-4), M'(-8,3), N'(-3,1)
B. K'(-2,1), L'(-4,6), M'(3,8), N'(1,3)
C. K'(1,-2), L'(6,-4), M'(8,3), N'(3,1)
D. K'(-1,2), L'(-6,4), M'(-8,-3), N'(-3,-1)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 27. Soal `5cdb075f3e6376933323750c`

A(5,2), B(8,5), dan C(2,1) adalah titik-titik sudut pada ΔABC. Tentukan bayangan ΔABC dari hasil rotasi sebesar 90º berlawanan arah jarum jam terhadap titik pusat O(0,0).

| Opsi | Isi |
|---|---|
| A | A'(-2,5), B'(-5,8), C'(-1,2) |
| B | A'(2,-5), B'(5,-8), C'(1,-2) |
| C | A'(-5,2), B'(-8,5), C'(-2,1) |
| D | A'(-5,-2), B'(-8,-5), C'(-2,-1) |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a5fe1af2f8985f276a93adc43cdf846388908011ff84becacf0a9c17cb2d8cd0`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Rotasi (Perputaran)
Tipe soal: multiple_choice
Stimulus: -
Soal: A(5,2), B(8,5), dan C(2,1) adalah titik-titik sudut pada ΔABC. Tentukan bayangan ΔABC dari hasil rotasi sebesar 90º berlawanan arah jarum jam terhadap titik pusat O(0,0).
Pilihan: A. A'(-2,5), B'(-5,8), C'(-1,2)
B. A'(2,-5), B'(5,-8), C'(1,-2)
C. A'(-5,2), B'(-8,5), C'(-2,1)
D. A'(-5,-2), B'(-8,-5), C'(-2,-1)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 28. Soal `f6516e65a41da50ae0f6a8b9`

Jika ΔMDN ≅ ΔKPG, maka MN = _____.

| Opsi | Isi |
|---|---|
| A | KP |
| B | KG |
| C | PG |
| D | DN |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `69076807f95c4c7e0210fe1e226e4297e5c3491499a58b81492b8d649220e769`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Kekongruenan
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika ΔMDN ≅ ΔKPG, maka MN = _____.
Pilihan: A. KP
B. KG
C. PG
D. DN
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 29. Soal `5494cb036f9f5ecded212fcf`

Jika dua segitiga memiliki dua pasang sisi yang sama panjang dan sudut yang diapit sisi-sisi tersebut sama besar, maka kedua segitiga tersebut kongruen. Pernyataan tersebut merupakan bunyi kriteria _____.

| Opsi | Isi |
|---|---|
| A | S-S-Sd |
| B | Sd-S-Sd |
| C | S-Sd-S |
| D | S-S-S |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c6d4c5c6b98df601d7de5d480940ea4059d4fd4ccded2ebdb12efbc6a96c4b99`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Kekongruenan
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika dua segitiga memiliki dua pasang sisi yang sama panjang dan sudut yang diapit sisi-sisi tersebut sama besar, maka kedua segitiga tersebut kongruen. Pernyataan tersebut merupakan bunyi kriteria _____.
Pilihan: A. S-S-Sd
B. Sd-S-Sd
C. S-Sd-S
D. S-S-S
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 30. Soal `907f9e4697523a633ea0ac02`

Suatu segitiga ABC siku-siku di titik B memiliki panjang AB=8 cm, BC=15 cm, dan AC=17 cm. Jika ΔA'B'C' merupakan hasil dilatasi dari ΔABC dengan faktor skala 3, maka luas ΔA'B'C' adalah…

| Opsi | Isi |
|---|---|
| A | 180 cm² |
| B | 1.620 cm² |
| C | 540 cm² |
| D | 60 cm² |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b3e3511e29025c3e95a72fd3dda273cf3da67c489f6433e61fc9c58bd22383f3`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Dilatasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Suatu segitiga ABC siku-siku di titik B memiliki panjang AB=8 cm, BC=15 cm, dan AC=17 cm. Jika ΔA'B'C' merupakan hasil dilatasi dari ΔABC dengan faktor skala 3, maka luas ΔA'B'C' adalah…
Pilihan: A. 180 cm²
B. 1.620 cm²
C. 540 cm²
D. 60 cm²
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 31. Soal `61e70f2732214f09d97c2039`

Diketahui ΔABC dengan A(-3,-2), B(6,4) dan C(1,-2). Tentukan bayangan ΔABC yang didilatasikan terhadap $[O, \frac{1}{2}]$! Gambarkan segitiga tersebut beserta bayangannya pada bidang koordinat!

| Opsi | Isi |
|---|---|
| A | $A'(-\frac{3}{2},-2)$, $B'(3,4)$, $C'(\frac{1}{2},-2)$ |
| B | A'(-2.5,-1.5), B'(6.5,4.5), C'(1.5,-1.5) |
| C | A'(-6,-4), B'(12,8), C'(2,-4) |
| D | $A'(-\frac{3}{2},-1)$, $B'(3,2)$, $C'(\frac{1}{2},-1)$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `72711152f55c6e3e75a126a8ee5662c976bae3bb281fbe8c0591615a1f26e3e2`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Dilatasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui ΔABC dengan A(-3,-2), B(6,4) dan C(1,-2). Tentukan bayangan ΔABC yang didilatasikan terhadap $[O, \frac{1}{2}]$! Gambarkan segitiga tersebut beserta bayangannya pada bidang koordinat!
Pilihan: A. $A'(-\frac{3}{2},-2)$, $B'(3,4)$, $C'(\frac{1}{2},-2)$
B. A'(-2.5,-1.5), B'(6.5,4.5), C'(1.5,-1.5)
C. A'(-6,-4), B'(12,8), C'(2,-4)
D. $A'(-\frac{3}{2},-1)$, $B'(3,2)$, $C'(\frac{1}{2},-1)$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 32. Soal `78652b4108bd747c96b2f4a8`

Pada $\triangle ABC$, $AD$ membagi $\angle A$ menjadi dua bagian yang sama besar. $AD$ disebut garis bagi. Titik $D$ terletak pada sisi $BC$. Petunjuk: Gambarkan garis yang sejajar dengan $AD$ dan melalui titik $C$. Garis ini berpotongan dengan perpanjangan $AB$ di titik $E$.<br><br>Beri alasan bahwa $\triangle ACE$ sama kaki. Tuliskan sisi-sisi yang sama panjang.

| Opsi | Isi |
|---|---|
| A | AC = AE, karena ∠ACE = ∠AEC |
| B | AC = CE, karena ∠CAE = ∠AEC |
| C | AE = CE, karena ∠ACE = ∠CAE |
| D | AB = AC, karena AD garis bagi |

![Gambar sumber soal 32](<../../../images/kelas7_crop-p0205-garis-bagi.png>)


Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas7_crop-p0205-garis-bagi.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menyebutkan', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `688148e53a0c2792f2c51fd978fd926eb005b76b5839e07d12a2f8689e8ca87f`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Kesebangunan pada Segitiga
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada $\triangle ABC$, $AD$ membagi $\angle A$ menjadi dua bagian yang sama besar. $AD$ disebut garis bagi. Titik $D$ terletak pada sisi $BC$. Petunjuk: Gambarkan garis yang sejajar dengan $AD$ dan melalui titik $C$. Garis ini berpotongan dengan perpanjangan $AB$ di titik $E$.

Beri alasan bahwa $\triangle ACE$ sama kaki. Tuliskan sisi-sisi yang sama panjang.
Pilihan: A. AC = AE, karena ∠ACE = ∠AEC
B. AC = CE, karena ∠CAE = ∠AEC
C. AE = CE, karena ∠ACE = ∠CAE
D. AB = AC, karena AD garis bagi
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 33. Soal `49861bd79ef9562f45188055`

Tentukan banyaknya anggota ruang sampel percobaan-percobaan berikut. ⓒ Jenis kelamin dari seorang siswa yang pertama kali ditunjuk oleh seorang guru dalam kelas yang terdiri dari 12 siswa laki-laki dan 18 siswa perempuan.

| Opsi | Isi |
|---|---|
| A | 30 (12 siswa laki-laki + 18 siswa perempuan) |
| B | 18 (hanya menghitung banyaknya siswa perempuan) |
| C | 12 (hanya menghitung banyaknya siswa laki-laki) |
| D | 2 (hanya menghitung banyaknya kategori jenis kelamin: laki-laki dan perempuan) |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `aeaa8c24e301942846f1ecbb5f8b24b509cebd3bdb7b1de6a00c5242125f5acf`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

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
Soal: Tentukan banyaknya anggota ruang sampel percobaan-percobaan berikut. ⓒ Jenis kelamin dari seorang siswa yang pertama kali ditunjuk oleh seorang guru dalam kelas yang terdiri dari 12 siswa laki-laki dan 18 siswa perempuan.
Pilihan: A. 30 (12 siswa laki-laki + 18 siswa perempuan)
B. 18 (hanya menghitung banyaknya siswa perempuan)
C. 12 (hanya menghitung banyaknya siswa laki-laki)
D. 2 (hanya menghitung banyaknya kategori jenis kelamin: laki-laki dan perempuan)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 34. Soal `47721424de374937d3a86de8`

Tentukan peluang tiap-tiap kejadian berikut ini dan nyatakan nilainya ke dalam pecahan biasa, pecahan desimal, dan persentase. ⓒ Sebuah kotak berisi enam bola merah, dua bola kuning, dan empat bola hijau. Dalam pengambilan satu bola dari kotak tersebut secara acak, kalian mendapatkan bola yang bukan merah.

| Opsi | Isi |
|---|---|
| A | 1 (membandingkan bola bukan merah dengan sesamanya, bukan dengan total bola di kotak) |
| B | 1/6 (hanya menghitung peluang terambilnya bola kuning saja, lupa bola hijau) |
| C | 1/3 (hanya menghitung peluang terambilnya bola hijau saja, lupa bola kuning) |
| D | 1/2 (atau 0,5 atau 50%) |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e7d45040ae7814a7cfd6748d5182f8b171df8a97867891c773f2fe86282f2260`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

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
Soal: Tentukan peluang tiap-tiap kejadian berikut ini dan nyatakan nilainya ke dalam pecahan biasa, pecahan desimal, dan persentase. ⓒ Sebuah kotak berisi enam bola merah, dua bola kuning, dan empat bola hijau. Dalam pengambilan satu bola dari kotak tersebut secara acak, kalian mendapatkan bola yang bukan merah.
Pilihan: A. 1 (membandingkan bola bukan merah dengan sesamanya, bukan dengan total bola di kotak)
B. 1/6 (hanya menghitung peluang terambilnya bola kuning saja, lupa bola hijau)
C. 1/3 (hanya menghitung peluang terambilnya bola hijau saja, lupa bola kuning)
D. 1/2 (atau 0,5 atau 50%)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 35. Soal `2fa02b235094086c5cc7be86`

Sebuah program komputer digunakan untuk menampilkan 12 bilangan 0–3 secara acak. Hasilnya adalah sebagai berikut. 1, 3, 3, 0, 1, 3, 3, 0, 3, 2, 1, 3<br><br>Tentukan frekuensi relatif munculnya bilangan 0.

| Opsi | Isi |
|---|---|
| A | 2/4 (= 1/2) |
| B | 2/12 (= 1/6) |
| C | 3/12 (= 1/4) |
| D | 1/12 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `31499aaffa3951b942524580051a5ac3328f9d8c4f88d4f1d106fac1f31cec64`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

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
Soal: Sebuah program komputer digunakan untuk menampilkan 12 bilangan 0–3 secara acak. Hasilnya adalah sebagai berikut. 1, 3, 3, 0, 1, 3, 3, 0, 3, 2, 1, 3

Tentukan frekuensi relatif munculnya bilangan 0.
Pilihan: A. 2/4 (= 1/2)
B. 2/12 (= 1/6)
C. 3/12 (= 1/4)
D. 1/12
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 36. Soal `b09a24b57d973871a9f482c8`

Seperangkat kartu berisi 5 kartu yang masing-masing bergambar lingkaran atau bintang. Setelah dilakukan 500 percobaan pengambilan satu kartu secara acak, diperoleh hasil pada Gambar 4.20. 450 407 400 350 300 250 200 150 93 100 50 0 Lingkaran Bintang Gambar yang Muncul Frekuensi Gambar Frekuensi Munculnya Kartu Bergambar Lingkaran dan Bintang<br><br>Tentukan banyaknya kartu bergambar lingkaran dan bintang dalam seperangkat kartu tersebut.

| Opsi | Isi |
|---|---|
| A | 4 kartu lingkaran dan 1 kartu bintang |
| B | 5 kartu lingkaran dan 0 kartu bintang |
| C | 1 kartu lingkaran dan 4 kartu bintang |
| D | 3 kartu lingkaran dan 2 kartu bintang |

![Gambar sumber soal 36](<../../../images/kelas9_crop-s0012-gambar-muncul.png>)


Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas9_crop-s0012-gambar-muncul.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a64390c594a663350fb4e2318c3ed1904aadff98b4f5f1041de8ddc0b84f7e09`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

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
Soal: Seperangkat kartu berisi 5 kartu yang masing-masing bergambar lingkaran atau bintang. Setelah dilakukan 500 percobaan pengambilan satu kartu secara acak, diperoleh hasil pada Gambar 4.20. 450 407 400 350 300 250 200 150 93 100 50 0 Lingkaran Bintang Gambar yang Muncul Frekuensi Gambar Frekuensi Munculnya Kartu Bergambar Lingkaran dan Bintang

Tentukan banyaknya kartu bergambar lingkaran dan bintang dalam seperangkat kartu tersebut.
Pilihan: A. 4 kartu lingkaran dan 1 kartu bintang
B. 5 kartu lingkaran dan 0 kartu bintang
C. 1 kartu lingkaran dan 4 kartu bintang
D. 3 kartu lingkaran dan 2 kartu bintang
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 37. Soal `0292b36d9d04627c0f3ae4e8`

Tentukan frekuensi harapan setiap kejadian berikut jika dilakukan 100 kali percobaan. b. Dalam pengambilan satu kartu secara acak dari seperangkat kartu remi, tidak didapatkan kartu hati.

| Opsi | Isi |
|---|---|
| A | 48 |
| B | 25 |
| C | 13 |
| D | 75 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1560757bb939c864b1e7cbad15ce8d2e045c85dc4537017ddef0e088230cf814`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

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
Soal: Tentukan frekuensi harapan setiap kejadian berikut jika dilakukan 100 kali percobaan. b. Dalam pengambilan satu kartu secara acak dari seperangkat kartu remi, tidak didapatkan kartu hati.
Pilihan: A. 48
B. 25
C. 13
D. 75
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 38. Soal `dfd8cbd993b44696494b45c1`

Di sebuah kota, persentase penduduknya yang masuk Generasi Z adalah 28%. Jika kalian memilih 75 penduduk kota itu secara acak, tentukan frekuensi harapan kalian mendapatkan penduduk Generasi Z.

| Opsi | Isi |
|---|---|
| A | 28 |
| B | 47 |
| C | 75 |
| D | 21 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3574145b98066c947e09c7795b97dc292460675b0af5ce01b2201e1ffb623450`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

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
Soal: Di sebuah kota, persentase penduduknya yang masuk Generasi Z adalah 28%. Jika kalian memilih 75 penduduk kota itu secara acak, tentukan frekuensi harapan kalian mendapatkan penduduk Generasi Z.
Pilihan: A. 28
B. 47
C. 75
D. 21
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 39. Soal `4e77f956826bf22b33dbf58b`

Putu memiliki roda putar yang terbagi menjadi lima juring yang sama besar, masing-masing ditulis angka 1, 2, 3, 4, dan 5. Dia akan memilih sampel dengan memutar roda tersebut sebanyak tiga kali. Tentukan peluang dia mendapatkan sampel yang rata-ratanya kurang dari 2.

| Opsi | Isi |
|---|---|
| A | 3/125 |
| B | 10/125 (atau 0,08) |
| C | 6/125 |
| D | 5/125 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `055ba4b015b1276b6086b514714670e2b938e800e56b7881142886fbf838d5ce`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

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
Soal: Putu memiliki roda putar yang terbagi menjadi lima juring yang sama besar, masing-masing ditulis angka 1, 2, 3, 4, dan 5. Dia akan memilih sampel dengan memutar roda tersebut sebanyak tiga kali. Tentukan peluang dia mendapatkan sampel yang rata-ratanya kurang dari 2.
Pilihan: A. 3/125
B. 10/125 (atau 0,08)
C. 6/125
D. 5/125
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 40. Soal `d57b84b818b2d3b772624d73`

Dhien adalah calon ketua OSIS. Dia ingin mengetahui persentase teman-teman di sekolahnya yang akan memilihnya.<br><br>Dari tiga kemungkinan cara pemilihan sampel berikut, mana yang seharusnya dipilih Dhien? Mengapa? ⓐ Dia bertanya kepada semua teman sekelasnya. ⓑ Dia menyurvei anak yang menempati urutan ke-3, 6, dan 9 di setiap barisan ketika upacara bendera. ⓒ Dia melakukan survei melalui media sosial terhadap teman-teman sekolahnya.

| Opsi | Isi |
|---|---|
| A | Dia menyurvei anak yang menempati urutan ke-3, 6, dan 9 di setiap barisan ketika upacara bendera |
| B | Dia menyurvei murid yang kebetulan lewat di depan kelasnya saat istirahat |
| C | Dia bertanya kepada semua teman sekelasnya |
| D | Dia melakukan survei melalui media sosial terhadap teman-teman sekolahnya |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `466104c8c6e5c53de5380e8cde0b09fc76f8887f9e13778a235df7dbe65f89b9`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

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
Soal: Dhien adalah calon ketua OSIS. Dia ingin mengetahui persentase teman-teman di sekolahnya yang akan memilihnya.

Dari tiga kemungkinan cara pemilihan sampel berikut, mana yang seharusnya dipilih Dhien? Mengapa? ⓐ Dia bertanya kepada semua teman sekelasnya. ⓑ Dia menyurvei anak yang menempati urutan ke-3, 6, dan 9 di setiap barisan ketika upacara bendera. ⓒ Dia melakukan survei melalui media sosial terhadap teman-teman sekolahnya.
Pilihan: A. Dia menyurvei anak yang menempati urutan ke-3, 6, dan 9 di setiap barisan ketika upacara bendera
B. Dia menyurvei murid yang kebetulan lewat di depan kelasnya saat istirahat
C. Dia bertanya kepada semua teman sekelasnya
D. Dia melakukan survei melalui media sosial terhadap teman-teman sekolahnya
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 41. Soal `b0bcef02731ce1c1ec1f8a92`

Pilihan dadu<br><br>\|Pilihan 1\|Pilihan 2\|<br>\|---\|---\|<br>\|Dadu kubus dengan sisi sebagai\|Dadu piramida dengan sisi\|<br>\|berikut:\|sebagai berikut:\|<br>\|1, 2, 3, 4, 5, 6\|1, 2, 3, 4\|<br><br>Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan. Syarat menangnya adalah mendapatkan angka 3. Jelaskan alasan atas pilihan kalian!

| Opsi | Isi |
|---|---|
| A | Keduanya sama besar karena sama-sama punya satu angka 3 |
| B | Pilihan 1 (dadu kubus) |
| C | Pilihan 2 (dadu piramida) |
| D | Tidak bisa ditentukan karena bentuk dadunya berbeda |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['menerapkan', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `48c641a5e2cf6cf9398abe5bd009403c7eaf314cd157af758c1f2175edf45ac1`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Membandingkan Peluang Kejadian
Tipe soal: multiple_choice
Stimulus: -
Soal: Pilihan dadu

|Pilihan 1|Pilihan 2|
|---|---|
|Dadu kubus dengan sisi sebagai|Dadu piramida dengan sisi|
|berikut:|sebagai berikut:|
|1, 2, 3, 4, 5, 6|1, 2, 3, 4|

Pilih dadu yang kalian akan gunakan apabila ingin mendapatkan peluang terbesar untuk menang dalam permainan. Syarat menangnya adalah mendapatkan angka 3. Jelaskan alasan atas pilihan kalian!
Pilihan: A. Keduanya sama besar karena sama-sama punya satu angka 3
B. Pilihan 1 (dadu kubus)
C. Pilihan 2 (dadu piramida)
D. Tidak bisa ditentukan karena bentuk dadunya berbeda
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 42. Soal `49d68d1b46c35ead12cca547`

Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.<br><br>50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65

| Opsi | Isi |
|---|---|
| A | Q1 = 65; Q2 = 70,4; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5 |
| B | Q1 = 80; Q2 = 67,5; Q3 = 65; jangkauan kuartil = 15; simpangan kuartil = 7,5 |
| C | Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5 |
| D | Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 15 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 9 / Matematika SMP Kelas 9. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `293a70f98bc81e897eb0fdb6ca6e06c782ad391e9016d6dc00751524332cf437`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 9
Topik: Matematika SMP Kelas 9
Subtopik: Penyebaran Data
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.

50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65
Pilihan: A. Q1 = 65; Q2 = 70,4; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5
B. Q1 = 80; Q2 = 67,5; Q3 = 65; jangkauan kuartil = 15; simpangan kuartil = 7,5
C. Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5
D. Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 15
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
