# Validasi ulang soal kelas 10 — Gemini blind N=3 dan diagnostik IndoBERT

**Batch belum selesai:** 0/138 run awal sukses; 0 item tercatat membutuhkan adjudikasi setelah run lengkap. Distribusi berikut masih sementara; item tanpa keputusan ditampilkan sebagai undecided. Provider berhenti karena kuota harian; checkpoint kerja dapat dilanjutkan saat kuota tersedia.

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v8-blind-sma10-key-verified`. Rubrik: `math-rubric-3x4x3-v6-sma10-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 10 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan bukan keputusan ahli manusia.

Checkpoint dikunci dengan SHA-256 sebelum pemeriksaan scope IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Model SD berada di luar cakupan kelas 10, sehingga seluruh head abstain dan tidak menghasilkan ukuran agreement dengan label blind.

Jumlah soal: 46; distribusi label advisory: `{"mathCognitiveDomain": {"undecided": 46, "knowing": 0, "applying": 0, "reasoning": 0}, "knowledgeDimension": {"undecided": 46, "factual": 0, "conceptual": 0, "procedural": 0, "metacognitive": 0}, "intendedDifficulty": {"undecided": 46, "Easy": 0, "Medium": 0, "Hard": 0}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"knowing": 0, "applying": 0, "reasoning": 0}, "knowledgeDimension": {"factual": 0, "conceptual": 0, "procedural": 0, "metacognitive": 0}, "intendedDifficulty": {"Easy": 0, "Medium": 0, "Hard": 0}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"llm_retry_or_manual_review": 46}`.
Run awal sukses: 0/138; adjudikasi: 0; token sukses tercatat: 0.

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

Untuk kelas 10, encoder dan head IndoBERT tidak dijalankan karena scope model hanya kelas 1–6. Probabilitas kosong, label/confidence/entropy null, dan action abstain berasal dari pemeriksaan scope runtime. Suara Gemini adalah bukti penilaian advisory, bukan probabilitas IndoBERT.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

Model IndoBERT lama hanya mendukung SD kelas 1–6. Untuk kelas 10, diagnostik mengembalikan `out_of_scope` dan `abstain`: label, confidence, dan entropy null serta probabilitas kosong. Label advisory mengikuti Gemini blind dengan rubrik SMA kelas 10. Tidak ada inferensi SD yang dipaksakan sebagai prediksi SMA.

## 1. Soal `20c03a0ebabbdc13efb66801`

Seseorang membagikan pesan berisi informasi yang salah (hoaks) kepada 2 orang temannya. Setelah membaca pesan ini, kedua orang tersebut mengikuti arahan dan membagikan pesan yang sama kepada 2 orang lainnya. Lengkapilah tabel di bawah ini yang akan memberimu gambaran penyebaran di setiap fase hingga fase ke-8.<br><br>\|Fase penyebaran\|1\|2\|3\|4\|5\|6\|7\|8\|<br>\|---\|---\|---\|---\|---\|---\|---\|---\|---\|<br>\|Banyak orang yang menerima hoaks\|2\|4\|…\|….\|….\|….\|….\|….\|<br><br>Jika banyak fase adalah n, tentukan rumus sederhana untuk menghitung banyak orang yang menerima hoaks pada fase ke-n tersebut?

| Opsi | Isi |
|---|---|
| A | $2^{n-1}$ |
| B | $2n$ |
| C | $n^2$ |
| D | $2^n$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b7c416ae66299aecef164f2c42dadd67b6b2936101e46bbde6700c37310913ac`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

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
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Definisi Eksponen
Tipe soal: multiple_choice
Stimulus: -
Soal: Seseorang membagikan pesan berisi informasi yang salah (hoaks) kepada 2 orang temannya. Setelah membaca pesan ini, kedua orang tersebut mengikuti arahan dan membagikan pesan yang sama kepada 2 orang lainnya. Lengkapilah tabel di bawah ini yang akan memberimu gambaran penyebaran di setiap fase hingga fase ke-8.

|Fase penyebaran|1|2|3|4|5|6|7|8|
|---|---|---|---|---|---|---|---|---|
|Banyak orang yang menerima hoaks|2|4|…|….|….|….|….|….|

Jika banyak fase adalah n, tentukan rumus sederhana untuk menghitung banyak orang yang menerima hoaks pada fase ke-n tersebut?
Pilihan: A. $2^{n-1}$
B. $2n$
C. $n^2$
D. $2^n$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `1a4524c9fb9888217a46bdf7`

Seseorang membagikan pesan berisi informasi yang salah (hoaks) kepada 2 orang temannya. Setelah membaca pesan ini, kedua orang tersebut mengikuti arahan dan membagikan pesan yang sama kepada 2 orang lainnya. Dengan asumsi setiap orang yang menerima pesan ini tidak mengetahui bahwa ini adalah hoaks, bayangkan betapa cepat hoaks ini akan tersebar. Lengkapilah tabel di bawah ini yang akan memberimu gambaran penyebaran di setiap fase hingga fase ke-8.<br><br>\|Fase penyebaran\|1\|2\|3\|4\|5\|6\|7\|8\|<br>\|---\|---\|---\|---\|---\|---\|---\|---\|---\|<br>\|Banyak orang yang menerima hoaks\|2\|4\|…\|….\|….\|….\|….\|….\|<br><br>Dengan memanfaatkan pola bilangan tersebut, hitung jumlah orang yang menerima hoaks tersebut pada fase ke-6?

| Opsi | Isi |
|---|---|
| A | 128 orang |
| B | 64 orang |
| C | 12 orang |
| D | 32 orang |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `84ba3449a5a25a605511b7fe1a05c360e04d7bfd34650609e9bdab01f3a133b2`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Definisi Eksponen
Tipe soal: multiple_choice
Stimulus: -
Soal: Seseorang membagikan pesan berisi informasi yang salah (hoaks) kepada 2 orang temannya. Setelah membaca pesan ini, kedua orang tersebut mengikuti arahan dan membagikan pesan yang sama kepada 2 orang lainnya. Dengan asumsi setiap orang yang menerima pesan ini tidak mengetahui bahwa ini adalah hoaks, bayangkan betapa cepat hoaks ini akan tersebar. Lengkapilah tabel di bawah ini yang akan memberimu gambaran penyebaran di setiap fase hingga fase ke-8.

|Fase penyebaran|1|2|3|4|5|6|7|8|
|---|---|---|---|---|---|---|---|---|
|Banyak orang yang menerima hoaks|2|4|…|….|….|….|….|….|

Dengan memanfaatkan pola bilangan tersebut, hitung jumlah orang yang menerima hoaks tersebut pada fase ke-6?
Pilihan: A. 128 orang
B. 64 orang
C. 12 orang
D. 32 orang
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `d16acca83decc68e658d11d5`

Tentukan nilai p sedemikian sehingga persamaan berikut ini tepat.<br><br>$(3\pi)^p = 27\pi^3$

| Opsi | Isi |
|---|---|
| A | $p = 27$ |
| B | $p = 3$ |
| C | $p = 1$ |
| D | $p = 9$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7fa500f5bd43ffc92ff7076c23f5492e849d4b4de104744af61b8bdd610c84af`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Sifat-Sifat Eksponen
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan nilai p sedemikian sehingga persamaan berikut ini tepat.

$(3\pi)^p = 27\pi^3$
Pilihan: A. $p = 27$
B. $p = 3$
C. $p = 1$
D. $p = 9$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `972c064ee62227036f9b40cd`

Tentukan nilai p sedemikian sehingga persamaan berikut ini tepat.<br><br>$(3^4)^2 = 3^p$

| Opsi | Isi |
|---|---|
| A | $p = 2$ |
| B | $p = 6$ |
| C | $p = 8$ |
| D | $p = 16$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3bcb982879f528364c66593c954ddbd44ebebd62ca4702f8d5f0e0500d1ed67b`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Sifat-Sifat Eksponen
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan nilai p sedemikian sehingga persamaan berikut ini tepat.

$(3^4)^2 = 3^p$
Pilihan: A. $p = 2$
B. $p = 6$
C. $p = 8$
D. $p = 16$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `d84e49739900804aa0aa6417`

Pada tahun 2015 kasus positif HIV-AIDS berjumlah sekitar 36 juta jiwa. Jumlah ini meningkat rata-rata 2% setiap tahun dari tahun 2010 hingga 2015. Jika peningkatan kasus positif HIV di tahun-tahun berikutnya diprediksi bertambah secara eksponen pada peningkatan 2% setiap tahun, berapa banyak kasus yang terjadi pada tahun 2020?

| Opsi | Isi |
|---|---|
| A | ≈39.746.909 jiwa |
| B | 38.203.488 jiwa |
| C | 39.600.000 jiwa |
| D | 40.541.832 jiwa |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `cad1579905c36291e926c9d1473e00e3703bfe7b4728aced77e0657adbd5f438`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Fungsi Eksponensial
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada tahun 2015 kasus positif HIV-AIDS berjumlah sekitar 36 juta jiwa. Jumlah ini meningkat rata-rata 2% setiap tahun dari tahun 2010 hingga 2015. Jika peningkatan kasus positif HIV di tahun-tahun berikutnya diprediksi bertambah secara eksponen pada peningkatan 2% setiap tahun, berapa banyak kasus yang terjadi pada tahun 2020?
Pilihan: A. ≈39.746.909 jiwa
B. 38.203.488 jiwa
C. 39.600.000 jiwa
D. 40.541.832 jiwa
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `6bd03dd3f29670f8050110d7`

Massa suatu zat radioaktif adalah 0,3 kg pada pukul 10 pagi. Tingkat peluruhan zat radioaktif tersebut adalah 15 % setiap jam. Berapakah jumlah zat radioaktif tersebut 8 jam kemudian?

| Opsi | Isi |
|---|---|
| A | 0,21828 kg (218,28 gram) |
| B | 0,2724 kg (272,4 gram) |
| C | 0,255 kg (255 gram) |
| D | ≈0,08172 kg (81,72 gram) |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fa530a3201e13d6d286ceb74197b4e44b98651936fe8f57751f8e48b1cb831d2`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Fungsi Eksponensial
Tipe soal: multiple_choice
Stimulus: -
Soal: Massa suatu zat radioaktif adalah 0,3 kg pada pukul 10 pagi. Tingkat peluruhan zat radioaktif tersebut adalah 15 % setiap jam. Berapakah jumlah zat radioaktif tersebut 8 jam kemudian?
Pilihan: A. 0,21828 kg (218,28 gram)
B. 0,2724 kg (272,4 gram)
C. 0,255 kg (255 gram)
D. ≈0,08172 kg (81,72 gram)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `842ca4bb6c6ebd4208641b61`

Sederhanakan bentuk akar berikut ini.<br><br>$(5\sqrt{x^5})(3\sqrt[3]{x})$

| Opsi | Isi |
|---|---|
| A | $8x^{\frac{17}{6}}$ |
| B | $15x^{\frac{17}{6}}$ |
| C | $15x^{\frac{13}{6}}$ |
| D | $15x^{\frac{6}{17}}$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `424ca71ba3d2d2f6c4ba0f473491505d7a354a191a9dbc4e83c3ef41cf97e9cf`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Bentuk Akar
Tipe soal: multiple_choice
Stimulus: -
Soal: Sederhanakan bentuk akar berikut ini.

$(5\sqrt{x^5})(3\sqrt[3]{x})$
Pilihan: A. $8x^{\frac{17}{6}}$
B. $15x^{\frac{17}{6}}$
C. $15x^{\frac{13}{6}}$
D. $15x^{\frac{6}{17}}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `7f717b29ae76a834f5c1363a`

Rasionalkan bentuk berikut ini.<br><br>$\dfrac{2}{\sqrt3+\sqrt5}$

| Opsi | Isi |
|---|---|
| A | $-1$ |
| B | $\sqrt5-\sqrt3$ |
| C | $\sqrt3-\sqrt5$ |
| D | $2(\sqrt3-\sqrt5)$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `709022a1bb35e8f1e78c657c5c53c27bcc18672a44a995de534665fc0f3f0fbc`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Bentuk Akar
Tipe soal: multiple_choice
Stimulus: -
Soal: Rasionalkan bentuk berikut ini.

$\dfrac{2}{\sqrt3+\sqrt5}$
Pilihan: A. $-1$
B. $\sqrt5-\sqrt3$
C. $\sqrt3-\sqrt5$
D. $2(\sqrt3-\sqrt5)$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 9. Soal `e97f2eaa7ee74e27d6bb517c`

Buat bilangan berikut dalam bentuk baku. 34.000.000.000

| Opsi | Isi |
|---|---|
| A | 3,4 × 10<sup>10</sup> |
| B | 3,4 × 10<sup>11</sup> |
| C | 3,4 × 10<sup>-10</sup> |
| D | 3,4 × 10<sup>9</sup> |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e91b7341d15b6fe2335f0773aa67389f36f00c1ec54ce6d2fffffdfab4dfea13`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Penulisan Bentuk Baku
Tipe soal: multiple_choice
Stimulus: -
Soal: Buat bilangan berikut dalam bentuk baku. 34.000.000.000
Pilihan: A. 3,4 × 10<sup>10</sup>
B. 3,4 × 10<sup>11</sup>
C. 3,4 × 10<sup>-10</sup>
D. 3,4 × 10<sup>9</sup>
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `1704f944a606f647f17a0cc0`

Ivan membagikan permen kepada teman-temannya dengan cara tertentu. Teman pertama mendapat tiga permen. Teman kedua mendapat lima permen. Teman ketiga mendapat tujuh permen. Dia melanjutkan pola ini hingga sepuluh temannya mendapat permen. Berapa permen yang didapat oleh teman kesepuluh?

| Opsi | Isi |
|---|---|
| A | 120 |
| B | 21 |
| C | 19 |
| D | 23 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ad454ab2f2f87379640474c244425f13c4fbe8852678a70ee0fbaecb85283c2a`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Barisan
Tipe soal: multiple_choice
Stimulus: -
Soal: Ivan membagikan permen kepada teman-temannya dengan cara tertentu. Teman pertama mendapat tiga permen. Teman kedua mendapat lima permen. Teman ketiga mendapat tujuh permen. Dia melanjutkan pola ini hingga sepuluh temannya mendapat permen. Berapa permen yang didapat oleh teman kesepuluh?
Pilihan: A. 120
B. 21
C. 19
D. 23
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `b9a85ae0df70ee2053be254e`

Tentukan suku ke-50 dari barisan berikut: 5, –2, –9, –16, …

| Opsi | Isi |
|---|---|
| A | -338 |
| B | 348 |
| C | -345 |
| D | -331 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `09f0c26e9a7180ff36e493cb764272751828019fbeef968c633e6aeb1774c886`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Barisan
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan suku ke-50 dari barisan berikut: 5, –2, –9, –16, …
Pilihan: A. -338
B. 348
C. -345
D. -331
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 12. Soal `c2fbd0a67c610e96b504751e`

Tentukanlah jumlah bilangan kelipatan 4 di antara bilangan 10 dan 99.

| Opsi | Isi |
|---|---|
| A | 1.288 |
| B | 1.196 |
| C | 1.134 |
| D | 1.188 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d10a356e0e427e3c8daed3f93bfcd596ec64641550f5dd1c1d165135304d4dfc`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Deret
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukanlah jumlah bilangan kelipatan 4 di antara bilangan 10 dan 99.
Pilihan: A. 1.288
B. 1.196
C. 1.134
D. 1.188
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 13. Soal `24793dda0631231d4688920b`

Vina membagikan permen kepada tujuh temannya dengan cara tertentu. Teman pertama mendapat dua permen. Teman kedua mendapat lima permen. Teman ketiga mendapat delapan permen. Dia melanjutkan pola ini, setiap teman mendapat tiga permen lebih banyak daripada teman sebelumnya, sampai semua temannya mendapat permen. Berapa permen yang harus Vina siapkan?

| Opsi | Isi |
|---|---|
| A | 57 |
| B | 100 |
| C | 20 |
| D | 77 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung', 'membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3816dfa9cf31fc27cf3c6043ee44b456157f68d83845c103fdbadf22c86ccbb8`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Deret
Tipe soal: multiple_choice
Stimulus: -
Soal: Vina membagikan permen kepada tujuh temannya dengan cara tertentu. Teman pertama mendapat dua permen. Teman kedua mendapat lima permen. Teman ketiga mendapat delapan permen. Dia melanjutkan pola ini, setiap teman mendapat tiga permen lebih banyak daripada teman sebelumnya, sampai semua temannya mendapat permen. Berapa permen yang harus Vina siapkan?
Pilihan: A. 57
B. 100
C. 20
D. 77
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `d215f8aa8bc3bed140f75b0b`

Firman menyimpan uang sejumlah Rp10.000.000,00 di bank dalam bentuk deposito dengan bunga 3% per tahun. Setiap tahun bank mengirim bunga ke rekening tabungan Firman. Gigih juga memiliki deposito sejumlah Rp10.000.000,00 di bank dengan bunga 3% per tahun. Setiap tahun, saat perpanjangan deposito, Gigih meminta bank untuk menambahkan bunganya ke dalam nilai depositonya.<br><br>d. Setelah lima tahun, lebih banyak uang Firman atau Gigih? Berapa selisihnya?

| Opsi | Isi |
|---|---|
| A | Uang Gigih lebih banyak, selisihnya Rp92.741,00 |
| B | Uang Gigih lebih banyak, selisihnya Rp9.000,00 |
| C | Sama banyak, selisihnya Rp0,00 |
| D | Uang Firman lebih banyak, selisihnya Rp92.741,00 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung', 'membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `070b8ab829fb3705c9da79f0ca4904f0dc570fac01bedbe4d1c2a0acfae9a019`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Bunga
Tipe soal: multiple_choice
Stimulus: -
Soal: Firman menyimpan uang sejumlah Rp10.000.000,00 di bank dalam bentuk deposito dengan bunga 3% per tahun. Setiap tahun bank mengirim bunga ke rekening tabungan Firman. Gigih juga memiliki deposito sejumlah Rp10.000.000,00 di bank dengan bunga 3% per tahun. Setiap tahun, saat perpanjangan deposito, Gigih meminta bank untuk menambahkan bunganya ke dalam nilai depositonya.

d. Setelah lima tahun, lebih banyak uang Firman atau Gigih? Berapa selisihnya?
Pilihan: A. Uang Gigih lebih banyak, selisihnya Rp92.741,00
B. Uang Gigih lebih banyak, selisihnya Rp9.000,00
C. Sama banyak, selisihnya Rp0,00
D. Uang Firman lebih banyak, selisihnya Rp92.741,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 15. Soal `2fbae8e5300a92a89c82f97e`

Gigih juga memiliki deposito sejumlah Rp10.000.000,00 di bank dengan bunga 3% per tahun. Setiap tahun, saat perpanjangan deposito, Gigih meminta bank untuk menambahkan bunganya ke dalam nilai depositonya.<br><br>Berapa uang Gigih setelah satu tahun?

| Opsi | Isi |
|---|---|
| A | Rp300.000,00 |
| B | Rp10.300.000,00 |
| C | Rp10.030.000,00 |
| D | Rp10.609.000,00 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `019814a5df99dc24098ff2dc0f24928455f9db302aeece0be1e74d35866720a1`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Bunga
Tipe soal: multiple_choice
Stimulus: -
Soal: Gigih juga memiliki deposito sejumlah Rp10.000.000,00 di bank dengan bunga 3% per tahun. Setiap tahun, saat perpanjangan deposito, Gigih meminta bank untuk menambahkan bunganya ke dalam nilai depositonya.

Berapa uang Gigih setelah satu tahun?
Pilihan: A. Rp300.000,00
B. Rp10.300.000,00
C. Rp10.030.000,00
D. Rp10.609.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `a1eac21e1913dacf28f160b7`

Perhatikan tiga komposisi sirup merah.<br>- Untuk satu liter air campurkan $\frac{2}{3}$ liter sirup merah<br>- Campurkan air dan sirup merah dengan perbandingan 2 : 3<br>- $\frac{2}{3}$ dari campuran sirup merah adalah air<br><br>Campuran mana yang paling manis?.

| Opsi | Isi |
|---|---|
| A | Campuran pertama, karena untuk 1 liter air ada $\frac{2}{3}$ liter sirup merah |
| B | Campuran kedua (air dan sirup merah 2 : 3), karena untuk 1 liter air ada $\frac{3}{2}$ liter sirup merah |
| C | Campuran ketiga, karena $\frac{2}{3}$ bagian campuran sudah ditentukan |
| D | Ketiga campuran sama manisnya, karena semuanya memuat angka 2 dan 3 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `de70b0deafba4c257e5fa431d0417f8d904743c752ea23e3f44d0e760b718b19`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Laju Perubahan Satuan
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan tiga komposisi sirup merah.
- Untuk satu liter air campurkan $\frac{2}{3}$ liter sirup merah
- Campurkan air dan sirup merah dengan perbandingan 2 : 3
- $\frac{2}{3}$ dari campuran sirup merah adalah air

Campuran mana yang paling manis?.
Pilihan: A. Campuran pertama, karena untuk 1 liter air ada $\frac{2}{3}$ liter sirup merah
B. Campuran kedua (air dan sirup merah 2 : 3), karena untuk 1 liter air ada $\frac{3}{2}$ liter sirup merah
C. Campuran ketiga, karena $\frac{2}{3}$ bagian campuran sudah ditentukan
D. Ketiga campuran sama manisnya, karena semuanya memuat angka 2 dan 3
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 17. Soal `b7ee1480516d0d8e8f27caeb`

Anak Kecil Remaja Orang Dewasa 114 cm 148 cm 200 cm 305 cm seperti Gambar Segitiga-Segitiga Sebangun dari Bayangan Tiga Orang. Diketahui bahwa tan 30 o = 0,57. Gunakan contoh yang baru disampaikan untuk mencari tinggi orang dewasa.<br><br>Cari tinggi orang dewasa dengan menggunakan perbandingan segitiga sebangun.

| Opsi | Isi |
|---|---|
| A | 173,85 cm |
| B | 219 cm |
| C | 148 cm |
| D | 535,09 cm |

![Gambar sumber soal 17](<../../../images/kelas10_panduan_siswa_kelas10.pdf-0239-01.png>)


Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0239-01.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menerapkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `243e2ed9d9a7fcdf89332cd1c8284031948f7c1821b740845822334d29d1a9a2`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Perbandingan Trigonometri
Tipe soal: multiple_choice
Stimulus: -
Soal: Anak Kecil Remaja Orang Dewasa 114 cm 148 cm 200 cm 305 cm seperti Gambar Segitiga-Segitiga Sebangun dari Bayangan Tiga Orang. Diketahui bahwa tan 30 o = 0,57. Gunakan contoh yang baru disampaikan untuk mencari tinggi orang dewasa.

Cari tinggi orang dewasa dengan menggunakan perbandingan segitiga sebangun.
Pilihan: A. 173,85 cm
B. 219 cm
C. 148 cm
D. 535,09 cm
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `c6e8b0f4419e6dcbc2ddc05d`

Anak Kecil Remaja Orang Dewasa 114 cm 148 cm 200 cm 305 cm seperti Gambar Segitiga-Segitiga Sebangun dari Bayangan Tiga Orang. Diketahui bahwa tan 30 o = 0,57. Gunakan contoh yang baru disampaikan untuk mencari tinggi orang dewasa.<br><br>Cari tinggi orang dewasa dengan memanfaatkan perbandingan trigonometri.

| Opsi | Isi |
|---|---|
| A | 173,85 cm |
| B | 114 cm |
| C | 152,50 cm |
| D | 535,09 cm |

![Gambar sumber soal 18](<../../../images/kelas10_panduan_siswa_kelas10.pdf-0239-01.png>)


Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0239-01.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menerapkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e2be9c55f5ceda54b17cc04acfcb23dfa89ba0491a092788e6289e7cb4694812`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Perbandingan Trigonometri
Tipe soal: multiple_choice
Stimulus: -
Soal: Anak Kecil Remaja Orang Dewasa 114 cm 148 cm 200 cm 305 cm seperti Gambar Segitiga-Segitiga Sebangun dari Bayangan Tiga Orang. Diketahui bahwa tan 30 o = 0,57. Gunakan contoh yang baru disampaikan untuk mencari tinggi orang dewasa.

Cari tinggi orang dewasa dengan memanfaatkan perbandingan trigonometri.
Pilihan: A. 173,85 cm
B. 114 cm
C. 152,50 cm
D. 535,09 cm
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 19. Soal `899fad8c8260df6013a595be`

Sebuah segitiga siku-siku PQR, mempunyai besaran ∠P = 53,2o dan besaran ∠Q = 36,8o. Q 36,8º 5 4 53,2º P 3 R<br><br>Nilai perbandingan panjang sisi QR dan QP sama dengan nilai ________.

| Opsi | Isi |
|---|---|
| A | tan 53,2° |
| B | cos 53,2° |
| C | cos 36,8° |
| D | tan 36,8° |

![Gambar sumber soal 19](<../../../images/kelas10_panduan_siswa_kelas10.pdf-0110-05.png>)


Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0110-05.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8f081a3d258b062f8d11da577e2cc1e4f14458086f67b1d982238c4676d2c7ba`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Pemanfaatan Perbandingan Trigonometri
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah segitiga siku-siku PQR, mempunyai besaran ∠P = 53,2o dan besaran ∠Q = 36,8o. Q 36,8º 5 4 53,2º P 3 R

Nilai perbandingan panjang sisi QR dan QP sama dengan nilai ________.
Pilihan: A. tan 53,2°
B. cos 53,2°
C. cos 36,8°
D. tan 36,8°
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `6392b9d64aaf026fd4ae54b2`

z 9,2 30º x<br><br>Cari panjang sisi x dan z.

| Opsi | Isi |
|---|---|
| A | x = 18,4 dan z = 15,94 |
| B | x = 5,31 dan z = 10,62 |
| C | x = 15,94 dan z = 18,4 |
| D | x = 9,2 dan z = 13,01 |

![Gambar sumber soal 20](<../../../images/kelas10_panduan_siswa_kelas10.pdf-0115-11.png>)


Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0115-11.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6124016732954dbdb2fade600081952ba62aecd7203cd01455792b5910e984d3`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Pemanfaatan Perbandingan Trigonometri
Tipe soal: multiple_choice
Stimulus: -
Soal: z 9,2 30º x

Cari panjang sisi x dan z.
Pilihan: A. x = 18,4 dan z = 15,94
B. x = 5,31 dan z = 10,62
C. x = 15,94 dan z = 18,4
D. x = 9,2 dan z = 13,01
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 21. Soal `e8e1147bfed27b5d98b29d8f`

Diketahui $\triangle ABC$ dengan titik-titik $A(-1, 3)$, $B(4, -2)$, dan $C(1, -5)$.<br><br>Apakah segitiga $ABC$ merupakan segitiga siku-siku? Jelaskan.

| Opsi | Isi |
|---|---|
| A | Ya, segitiga ABC siku-siku di B |
| B | Ya, segitiga ABC siku-siku di C |
| C | Tidak, karena sisi-sisinya tidak berupa bilangan bulat sehingga tidak membentuk tripel Pythagoras |
| D | Tidak, karena AB² + BC² tidak sama dengan CA² |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6036bd6bab55947314cc890072266d82ee54afc9797c425ebcbca17cdf404aa5`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Rumus Jarak (Pengayaan)
Tipe soal: multiple_choice
Stimulus: -
Soal: Diketahui $\triangle ABC$ dengan titik-titik $A(-1, 3)$, $B(4, -2)$, dan $C(1, -5)$.

Apakah segitiga $ABC$ merupakan segitiga siku-siku? Jelaskan.
Pilihan: A. Ya, segitiga ABC siku-siku di B
B. Ya, segitiga ABC siku-siku di C
C. Tidak, karena sisi-sisinya tidak berupa bilangan bulat sehingga tidak membentuk tripel Pythagoras
D. Tidak, karena AB² + BC² tidak sama dengan CA²
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 22. Soal `afeeb033a6caf863bee7e15a`

Asep memiliki beberapa jenis tongkat untuk olahraga: tongkat kasti, tongkat hoki, dan tongkat bisbol. Asep menjajarkan 3 tongkat kasti, 2 tongkat hoki, dan 1 tongkat bisbol dan panjangnya 455 cm. Asep menjajarkan sebuah tongkat kasti, 3 tongkat ukuran hoki, dan 2 tongkat bisbol dan panjangnya 545 cm. Asep juga mengamati bahwa 2 tongkat kasti sama panjang dengan tongkat bisbol.<br><br>Berapakah panjang tiap jenis tongkat?

| Opsi | Isi |
|---|---|
| A | Tongkat kasti 55 cm, tongkat hoki 90 cm, dan tongkat bisbol 110 cm. |
| B | Tongkat kasti 90 cm, tongkat hoki 55 cm, dan tongkat bisbol 110 cm. |
| C | Tongkat kasti 110 cm, tongkat hoki 90 cm, dan tongkat bisbol 55 cm. |
| D | Tongkat kasti 55 cm, tongkat hoki 110 cm, dan tongkat bisbol 90 cm. |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5eceaec48122cd2c8b50f1e25f459b65eae574246d5944cca74edf6b6343facc`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Sistem Persamaan Linear
Tipe soal: multiple_choice
Stimulus: -
Soal: Asep memiliki beberapa jenis tongkat untuk olahraga: tongkat kasti, tongkat hoki, dan tongkat bisbol. Asep menjajarkan 3 tongkat kasti, 2 tongkat hoki, dan 1 tongkat bisbol dan panjangnya 455 cm. Asep menjajarkan sebuah tongkat kasti, 3 tongkat ukuran hoki, dan 2 tongkat bisbol dan panjangnya 545 cm. Asep juga mengamati bahwa 2 tongkat kasti sama panjang dengan tongkat bisbol.

Berapakah panjang tiap jenis tongkat?
Pilihan: A. Tongkat kasti 55 cm, tongkat hoki 90 cm, dan tongkat bisbol 110 cm.
B. Tongkat kasti 90 cm, tongkat hoki 55 cm, dan tongkat bisbol 110 cm.
C. Tongkat kasti 110 cm, tongkat hoki 90 cm, dan tongkat bisbol 55 cm.
D. Tongkat kasti 55 cm, tongkat hoki 110 cm, dan tongkat bisbol 90 cm.
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 23. Soal `873ea535dcce2925196e80f4`

Sebuah minuman dijual dalam tiga kemasan berbeda: kecil, sedang, dan besar. Jika Bonar membeli 3 kemasan kecil, 2 kemasan sedang, dan 3 kemasan besar, dia mendapat minuman sebanyak 4.700 ml. Jika Bonar membeli 3 kemasan kecil, 1 kemasan sedang, dan 2 kemasan besar, dia mendapat 3.300 ml. Jika Bonar membeli 2 kemasan sedang dan 2 kemasan besar, dia mendapat 2.800 ml minuman. Berapakah volume tiap jenis kemasan?<br><br>Ada berapa solusi yang ada? Jelaskan.

| Opsi | Isi |
|---|---|
| A | Banyak solusi (tak terhingga), karena eliminasi persamaan (1) dan (2) identik dengan persamaan (3). |
| B | Tidak dapat ditentukan tanpa menggambar grafik tiga dimensi. |
| C | Tidak ada solusi, karena hasil eliminasi menghasilkan pernyataan yang tidak mungkin benar. |
| D | Hanya satu solusi, karena ada tiga persamaan untuk tiga variabel. |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8fd8179718e4a7fe35c15651eb3f44769963d6ebf5533a2b5167df426a69b6ec`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Sistem Persamaan Linear
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah minuman dijual dalam tiga kemasan berbeda: kecil, sedang, dan besar. Jika Bonar membeli 3 kemasan kecil, 2 kemasan sedang, dan 3 kemasan besar, dia mendapat minuman sebanyak 4.700 ml. Jika Bonar membeli 3 kemasan kecil, 1 kemasan sedang, dan 2 kemasan besar, dia mendapat 3.300 ml. Jika Bonar membeli 2 kemasan sedang dan 2 kemasan besar, dia mendapat 2.800 ml minuman. Berapakah volume tiap jenis kemasan?

Ada berapa solusi yang ada? Jelaskan.
Pilihan: A. Banyak solusi (tak terhingga), karena eliminasi persamaan (1) dan (2) identik dengan persamaan (3).
B. Tidak dapat ditentukan tanpa menggambar grafik tiga dimensi.
C. Tidak ada solusi, karena hasil eliminasi menghasilkan pernyataan yang tidak mungkin benar.
D. Hanya satu solusi, karena ada tiga persamaan untuk tiga variabel.
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 24. Soal `55f4593490fe0eca29b58712`

Pak Eko menimbang buah menggunakan timbangan bebek. Dua buah apel dan lima buah jeruk beratnya kurang dari 1 kg. Enam buah apel dan dua buah jeruk beratnya lebih dari 1 kg. Berat 1 apel (misal disebut x) dan berat 1 jeruk (misal disebut y), dalam satuan ons (1 kg = 10 ons).<br><br>Apakah titik (0,0) merupakan daerah hasil pertidaksamaan 2 x + 5 y < 10? Petunjuk: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan dan periksalah apakah pertidaksamaan bernilai benar.

| Opsi | Isi |
|---|---|
| A | Tidak, karena 2(0) + 5(0) tidak sama dengan 10. |
| B | Ya, karena titik (0,0) pasti termasuk daerah hasil pertidaksamaan apa pun. |
| C | Ya, karena 2(0) + 5(0) = 0 dan 0 < 10 (pertidaksamaan bernilai benar). |
| D | Tidak dapat ditentukan tanpa menggambar grafiknya terlebih dahulu. |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6b6b6a1a0b5175eb6dbeaea00d985c35ba96c3951b4038bdaf8e03e9987f7337`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Sistem Pertidaksamaan Linear
Tipe soal: multiple_choice
Stimulus: -
Soal: Pak Eko menimbang buah menggunakan timbangan bebek. Dua buah apel dan lima buah jeruk beratnya kurang dari 1 kg. Enam buah apel dan dua buah jeruk beratnya lebih dari 1 kg. Berat 1 apel (misal disebut x) dan berat 1 jeruk (misal disebut y), dalam satuan ons (1 kg = 10 ons).

Apakah titik (0,0) merupakan daerah hasil pertidaksamaan 2 x + 5 y < 10? Petunjuk: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan dan periksalah apakah pertidaksamaan bernilai benar.
Pilihan: A. Tidak, karena 2(0) + 5(0) tidak sama dengan 10.
B. Ya, karena titik (0,0) pasti termasuk daerah hasil pertidaksamaan apa pun.
C. Ya, karena 2(0) + 5(0) = 0 dan 0 < 10 (pertidaksamaan bernilai benar).
D. Tidak dapat ditentukan tanpa menggambar grafiknya terlebih dahulu.
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 25. Soal `17d32fe57e7f77cdae983dc8`

Pak Eko menimbang buah menggunakan timbangan bebek. Dua buah apel dan lima buah jeruk beratnya kurang dari 1 kg. Enam buah apel dan dua buah jeruk beratnya lebih dari 1 kg. Berat 1 apel (misal disebut x) dan berat 1 jeruk (misal disebut y), dalam satuan ons (1 kg = 10 ons).<br><br>Apakah titik (0,0) merupakan daerah hasil pertidaksamaan 6 x + 2 y > 10? Petunjuk: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan dan periksalah apakah pertidaksamaan bernilai benar.

| Opsi | Isi |
|---|---|
| A | Ya, karena titik (0,0) pasti termasuk daerah hasil pertidaksamaan apa pun. |
| B | Tidak dapat ditentukan tanpa menggambar grafiknya terlebih dahulu. |
| C | Ya, karena 6(0) + 2(0) = 0 sudah memenuhi pertidaksamaan tersebut. |
| D | Tidak, karena 6(0) + 2(0) = 0 dan 0 > 10 salah (pertidaksamaan tidak bernilai benar). |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `87f6ca4d457bcd94a77f37caab792d6ae0fe2894f6cb579cb01c3377748689de`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Sistem Pertidaksamaan Linear
Tipe soal: multiple_choice
Stimulus: -
Soal: Pak Eko menimbang buah menggunakan timbangan bebek. Dua buah apel dan lima buah jeruk beratnya kurang dari 1 kg. Enam buah apel dan dua buah jeruk beratnya lebih dari 1 kg. Berat 1 apel (misal disebut x) dan berat 1 jeruk (misal disebut y), dalam satuan ons (1 kg = 10 ons).

Apakah titik (0,0) merupakan daerah hasil pertidaksamaan 6 x + 2 y > 10? Petunjuk: substitusi nilai x = 0 dan y = 0 ke dalam pertidaksamaan dan periksalah apakah pertidaksamaan bernilai benar.
Pilihan: A. Ya, karena titik (0,0) pasti termasuk daerah hasil pertidaksamaan apa pun.
B. Tidak dapat ditentukan tanpa menggambar grafiknya terlebih dahulu.
C. Ya, karena 6(0) + 2(0) = 0 sudah memenuhi pertidaksamaan tersebut.
D. Tidak, karena 6(0) + 2(0) = 0 dan 0 > 10 salah (pertidaksamaan tidak bernilai benar).
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 26. Soal `0b4b98faa7f553833f0db971`

Suatu toko alat lukis menjual 40 kuas lukis. Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.<br><br>Jika uang yang didapat oleh toko tersebut Rp1.103.000,00, maka berapa banyak masing-masing jenis kuas lukis yang terjual?

| Opsi | Isi |
|---|---|
| A | 20 kuas lukis jenis I dan 20 kuas lukis jenis II |
| B | 15 kuas lukis jenis I dan 25 kuas lukis jenis II |
| C | 27 kuas lukis jenis I dan 13 kuas lukis jenis II |
| D | 13 kuas lukis jenis I dan 27 kuas lukis jenis II |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8c1a9811e05201190584d90a718904cddc91456b1c0eca555f73384e14c94539`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Sistem Persamaan Linear Dua Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Suatu toko alat lukis menjual 40 kuas lukis. Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.

Jika uang yang didapat oleh toko tersebut Rp1.103.000,00, maka berapa banyak masing-masing jenis kuas lukis yang terjual?
Pilihan: A. 20 kuas lukis jenis I dan 20 kuas lukis jenis II
B. 15 kuas lukis jenis I dan 25 kuas lukis jenis II
C. 27 kuas lukis jenis I dan 13 kuas lukis jenis II
D. 13 kuas lukis jenis I dan 27 kuas lukis jenis II
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 27. Soal `8fa35d360450878f96feeb48`

Tentukan solusi atau akar-akar dari persamaan kuadrat $2x^2 - 8x + 6 = 0$.

| Opsi | Isi |
|---|---|
| A | x = -1 atau x = 3 |
| B | x = -1 atau x = -3 |
| C | x = 2 atau x = 6 |
| D | x = 1 atau x = 3 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3f3f58398fd050d03b43ea179b37efb8c6dd3ad5da78ad3a1c44a23b24d86dd6`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Persamaan Kuadrat
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan solusi atau akar-akar dari persamaan kuadrat $2x^2 - 8x + 6 = 0$.
Pilihan: A. x = -1 atau x = 3
B. x = -1 atau x = -3
C. x = 2 atau x = 6
D. x = 1 atau x = 3
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 28. Soal `6d67a36d7ac3cfb4348b802b`

Tentukan akar-akar dari persamaan kuadrat $2x^2 - 18 = 0$.

| Opsi | Isi |
|---|---|
| A | x = 9 atau x = -9 |
| B | x = -3 (akar kembar) |
| C | x = 3 (hanya satu akar) |
| D | x = 3 atau x = -3 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `905de4b503082ad252cbfa8ab98db4a3e121a75ceb1f5bbee4feaad75b76183f`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Persamaan Kuadrat
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan akar-akar dari persamaan kuadrat $2x^2 - 18 = 0$.
Pilihan: A. x = 9 atau x = -9
B. x = -3 (akar kembar)
C. x = 3 (hanya satu akar)
D. x = 3 atau x = -3
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 29. Soal `d590344d18abe3ebd38fb8ed`

Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.<br><br>\|Waktu (Detik)\|0\|1\|2\|3\|4\|5\|6\|<br>\|---\|---\|---\|---\|---\|---\|---\|---\|<br>\|Jarak (m)\|0\|5\|8\|9\|8\|5\|0\|<br><br>Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah. Jelaskan alasanmu.

| Opsi | Isi |
|---|---|
| A | Tidak dapat ditentukan tanpa menggambar grafiknya. |
| B | Terbuka ke bawah, karena nilai fungsi (jarak) naik kemudian turun lagi. |
| C | Terbuka ke atas, karena nilai fungsi naik kemudian turun lagi. |
| D | Terbuka ke bawah, karena nilai fungsi turun kemudian naik lagi. |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6dd1ddc6f64fe513667c2a64cdd2ae8d03aab8ca3672f01da8075e3a85965e6a`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Fungsi Kuadrat
Tipe soal: multiple_choice
Stimulus: -
Soal: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.

|Waktu (Detik)|0|1|2|3|4|5|6|
|---|---|---|---|---|---|---|---|
|Jarak (m)|0|5|8|9|8|5|0|

Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah. Jelaskan alasanmu.
Pilihan: A. Tidak dapat ditentukan tanpa menggambar grafiknya.
B. Terbuka ke bawah, karena nilai fungsi (jarak) naik kemudian turun lagi.
C. Terbuka ke atas, karena nilai fungsi naik kemudian turun lagi.
D. Terbuka ke bawah, karena nilai fungsi turun kemudian naik lagi.
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 30. Soal `3fab45a2a8a53e25de52d0f6`

Sebuah bola dilemparkan dari ketinggian awal 4 m dan mencapai ketinggian maksimum 8 m setelah dua detik sejak dilempar.<br><br>Nyatakan fungsi kuadrat tinggi bola tersebut dalam bentuk umum $y = ax^2+bx+c$.

| Opsi | Isi |
|---|---|
| A | $y = -x^2 - 4x + 4$ |
| B | $y = x^2 - 4x + 4$ |
| C | $y = -x^2 + 4x + 4$ |
| D | $y = -x^2 + 4x + 8$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d116f1eb4f99dd264dbaf3d5b8fe16fdbb2f365543f2bbf232b1d6e8284741fb`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Fungsi Kuadrat
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah bola dilemparkan dari ketinggian awal 4 m dan mencapai ketinggian maksimum 8 m setelah dua detik sejak dilempar.

Nyatakan fungsi kuadrat tinggi bola tersebut dalam bentuk umum $y = ax^2+bx+c$.
Pilihan: A. $y = -x^2 - 4x + 4$
B. $y = x^2 - 4x + 4$
C. $y = -x^2 + 4x + 4$
D. $y = -x^2 + 4x + 8$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 31. Soal `4b2524b8440c37d72e127b02`

Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg. Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.<br><br>Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?

| Opsi | Isi |
|---|---|
| A | 10 kali pengangkutan |
| B | 11 kali pengangkutan |
| C | 9,45 kali pengangkutan |
| D | 9 kali pengangkutan |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `49a7eca21d03a71a66fe4e6dadda728ec0f2cbf1a136f2ada875790e9f3c2989`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Menyelesaikan Masalah terkait Pertidaksamaan Linier Satu Variabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Mobil pick up hanya dapat membawa muatan seberat 2.000 kg. Pengemudi dan kernek memiliki berat total 150 kg. Mobil pick up tersebut akan mengangkut kotak yang berisi 50 kg.

Jika mobil pick up harus membawa 350 kotak, berapa kali pengangkutan kotak yang harus dilakukan sampai semua kotak terangkut?
Pilihan: A. 10 kali pengangkutan
B. 11 kali pengangkutan
C. 9,45 kali pengangkutan
D. 9 kali pengangkutan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 32. Soal `72d9df20cc708f4143b713d0`

Apabila diketahui banyak anggota dua himpunan seperti berikut ini, maka ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? a. n(A) = n(B) = 12<br><br>Ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12?

| Opsi | Isi |
|---|---|
| A | 12 + 11 + 10 + ... + 2 + 1 = 78 |
| B | 12! = 479.001.600 |
| C | 12 |
| D | 12 x 12 = 144 |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e6c25efc3054bf7c47393ec0ac8d109138ab922be1ccf41986661f18251930be`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Korespondensi Satu-satu (Pengayaan)
Tipe soal: multiple_choice
Stimulus: -
Soal: Apabila diketahui banyak anggota dua himpunan seperti berikut ini, maka ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? a. n(A) = n(B) = 12

Ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12?
Pilihan: A. 12 + 11 + 10 + ... + 2 + 1 = 78
B. 12! = 479.001.600
C. 12
D. 12 x 12 = 144
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 33. Soal `3b808934c13bf0822544d6d6`

1. Perhatikan diagram batang berikut. Diagram berikut menunjukkan waktu yang ditempuh oleh para atlet di Olimpiade 1998 cabang Lintas Alam 10 km. Gambar 6.4 Diagram Batang Waktu yang Ditempuh Peserta Lintas Alam Olimpiade 1998. Untuk dapat memahami diagram dengan lebih baik, kamu perlu memahami situasi dan konteks dari diagram.<br><br>Berapakah atlet yang menyelesaikan lomba ini dengan interval catatan waktu antara 31 menit dan 32 menit 59 detik?

| Opsi | Isi |
|---|---|
| A | 6 pelari |
| B | 10 pelari |
| C | 4 pelari |
| D | 8 pelari |

![Gambar sumber soal 33](<../../../images/kelas10_panduan_siswa_kelas10.pdf-0200-09.png>)


Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0200-09.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `43667eb2552c244a022ee3f0a9d06438172be0a89a4ccbe695411a83e958b19a`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Representasi Data
Tipe soal: multiple_choice
Stimulus: -
Soal: 1. Perhatikan diagram batang berikut. Diagram berikut menunjukkan waktu yang ditempuh oleh para atlet di Olimpiade 1998 cabang Lintas Alam 10 km. Gambar 6.4 Diagram Batang Waktu yang Ditempuh Peserta Lintas Alam Olimpiade 1998. Untuk dapat memahami diagram dengan lebih baik, kamu perlu memahami situasi dan konteks dari diagram.

Berapakah atlet yang menyelesaikan lomba ini dengan interval catatan waktu antara 31 menit dan 32 menit 59 detik?
Pilihan: A. 6 pelari
B. 10 pelari
C. 4 pelari
D. 8 pelari
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 34. Soal `e9d27eefa537bb209c6d3b40`

Perhatikan diagram batang berikut. Diagram berikut menunjukkan waktu yang ditempuh oleh para atlet di Olimpiade 1998 cabang Lintas Alam 10 km. Gambar 6.4 Diagram Batang Waktu yang Ditempuh Peserta Lintas Alam Olimpiade 1998<br><br>Dari Gambar 6.4, ada berapa atlet yang berpartisipasi dalam cabang lintas alam? Ada berapa negara yang berpartisipasi dalam cabang ini?

| Opsi | Isi |
|---|---|
| A | 20 atlet; 25 negara |
| B | 25 atlet; 20 negara |
| C | 25 atlet; 25 negara |
| D | 24 atlet; 20 negara |

![Gambar sumber soal 34](<../../../images/kelas10_panduan_siswa_kelas10.pdf-0200-09.png>)


Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0200-09.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fc4a62786dc9ca2311dcbc18e521dade5343176a7f1c07f8e30a6bfafab8c592`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Representasi Data
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan diagram batang berikut. Diagram berikut menunjukkan waktu yang ditempuh oleh para atlet di Olimpiade 1998 cabang Lintas Alam 10 km. Gambar 6.4 Diagram Batang Waktu yang Ditempuh Peserta Lintas Alam Olimpiade 1998

Dari Gambar 6.4, ada berapa atlet yang berpartisipasi dalam cabang lintas alam? Ada berapa negara yang berpartisipasi dalam cabang ini?
Pilihan: A. 20 atlet; 25 negara
B. 25 atlet; 20 negara
C. 25 atlet; 25 negara
D. 24 atlet; 20 negara
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 35. Soal `ff85b5a87bfa58eb3957ceb3`

Jika data penjualan sepatu di toko A pada Tabel kita ubah menjadi tabel Frekuensi data tunggal sebagai berikut. Tabel Frekuensi Data Tunggal Penjualan Sepatu di Toko A \| Ukuran: 38, 39, 40, 41, 42, 43, 44, 45, 46 \| Frekuensi: 1, 1, 2, 4, 5, 7, 7, 2, 1<br><br>Tentukanlah modus, median, dan mean dari kumpulan data di atas.

| Opsi | Isi |
|---|---|
| A | Modus = 43 dan 44, median = 42, mean = 42,5 |
| B | Modus = 43 dan 44, median = 43, mean = 42 |
| C | Modus = 7, median = 43, mean = 42,5 |
| D | Modus = 43 dan 44, median = 43, mean = 42,5 |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `405c701bed04053a8fd499bb56ab9f9fbf68fbcfc728f33e1e029c03b90ec5b9`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Statistik Deskriptif
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika data penjualan sepatu di toko A pada Tabel kita ubah menjadi tabel Frekuensi data tunggal sebagai berikut. Tabel Frekuensi Data Tunggal Penjualan Sepatu di Toko A | Ukuran: 38, 39, 40, 41, 42, 43, 44, 45, 46 | Frekuensi: 1, 1, 2, 4, 5, 7, 7, 2, 1

Tentukanlah modus, median, dan mean dari kumpulan data di atas.
Pilihan: A. Modus = 43 dan 44, median = 42, mean = 42,5
B. Modus = 43 dan 44, median = 43, mean = 42
C. Modus = 7, median = 43, mean = 42,5
D. Modus = 43 dan 44, median = 43, mean = 42,5
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 36. Soal `2de15d728d070fae8af5319c`

Data berikut menunjukkan jumlah kue yang dijual melalui situs online setiap harinya: 0 3 2 7 4 2 3 0 4 0 6 5 5 2 4 0<br><br>Tentukanlah modus dan median dari data di atas.

| Opsi | Isi |
|---|---|
| A | Modus = 4, median = 3 |
| B | Modus = 0, median = 3,5 |
| C | Modus = 0, median = 3 |
| D | Modus = 0, median = 2 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a92692465be52f267f6029bb8bf6652c78110b38768bf873ee1b1ca2764b8f78`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Statistik Deskriptif
Tipe soal: multiple_choice
Stimulus: -
Soal: Data berikut menunjukkan jumlah kue yang dijual melalui situs online setiap harinya: 0 3 2 7 4 2 3 0 4 0 6 5 5 2 4 0

Tentukanlah modus dan median dari data di atas.
Pilihan: A. Modus = 4, median = 3
B. Modus = 0, median = 3,5
C. Modus = 0, median = 3
D. Modus = 0, median = 2
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 37. Soal `d6d3b4c5f9819d69d4c859d0`

Dalam upaya untuk mempromosikan penggunaan energi yang efisien, sebuah kota melakukan survei terhadap konsumsi listrik bulanan (dalam kWh) dari 10 rumah tangga diperoleh data sebagai berikut. 300, 320, 310, 305, 315, 320, 750, 310, 325, 315<br><br>Mengapa angka 750 kWh dapat dianggap sebagai pencilan?

| Opsi | Isi |
|---|---|
| A | Karena 750 kWh lebih dari 1,5 kali median data (315 kWh) |
| B | Karena 750 kWh lebih besar dari nilai data lainnya yang tertinggi (325 kWh) |
| C | Karena 750 kWh lebih besar dari batas atas IQR (335 kWh), sehingga berada di luar rentang wajar data |
| D | Karena 750 kWh adalah satu-satunya data yang jumlah angkanya lebih dari tiga digit |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `596cb713fe0bef3ba8e51ce1d60fff001d416aa358ef9460a7b9f8da9fd80444`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Representasi Data Lanjutan
Tipe soal: multiple_choice
Stimulus: -
Soal: Dalam upaya untuk mempromosikan penggunaan energi yang efisien, sebuah kota melakukan survei terhadap konsumsi listrik bulanan (dalam kWh) dari 10 rumah tangga diperoleh data sebagai berikut. 300, 320, 310, 305, 315, 320, 750, 310, 325, 315

Mengapa angka 750 kWh dapat dianggap sebagai pencilan?
Pilihan: A. Karena 750 kWh lebih dari 1,5 kali median data (315 kWh)
B. Karena 750 kWh lebih besar dari nilai data lainnya yang tertinggi (325 kWh)
C. Karena 750 kWh lebih besar dari batas atas IQR (335 kWh), sehingga berada di luar rentang wajar data
D. Karena 750 kWh adalah satu-satunya data yang jumlah angkanya lebih dari tiga digit
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 38. Soal `8d43b2c9894a7ba29b09e984`

Perhatikan Box Plot dari data waktu yang diperlukan (dalam menit) untuk pengisian HP dari 0% sampai 100%. Gambar 6.17 Diagram Box-and-Whisker Kecepatan Pengisian HP dari 0 sampai 100%<br><br>Tentukanlah nilai dari data minimum, Q1, Q2, Q3 dan data maksimum dari data tersebut.

| Opsi | Isi |
|---|---|
| A | Data minimum = 68, Q1 = 71, Q2 = 72, Q3 = 76, data maksimum = 77 |
| B | Data minimum = 68, Q1 = 72, Q2 = 76, Q3 = 77, data maksimum = 80 |
| C | Data minimum = 68, Q1 = 72, Q2 = 74, Q3 = 76, data maksimum = 80 |
| D | Data minimum = 70, Q1 = 71, Q2 = 72, Q3 = 76, data maksimum = 80 |

![Gambar sumber soal 38](<../../../images/kelas10_panduan_siswa_kelas10.pdf-0228-02.png>)


![Gambar sumber soal 38](<../../../images/kelas10_panduan_siswa_kelas10.pdf-0228-03.png>)


Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0228-02.png, images/kelas10_panduan_siswa_kelas10.pdf-0228-03.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `eec133ea650d44cb87e6bab3cf9d954490e25e20f7b10c7023c3a6fc3c864c6b`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Representasi Data Lanjutan
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan Box Plot dari data waktu yang diperlukan (dalam menit) untuk pengisian HP dari 0% sampai 100%. Gambar 6.17 Diagram Box-and-Whisker Kecepatan Pengisian HP dari 0 sampai 100%

Tentukanlah nilai dari data minimum, Q1, Q2, Q3 dan data maksimum dari data tersebut.
Pilihan: A. Data minimum = 68, Q1 = 71, Q2 = 72, Q3 = 76, data maksimum = 77
B. Data minimum = 68, Q1 = 72, Q2 = 76, Q3 = 77, data maksimum = 80
C. Data minimum = 68, Q1 = 72, Q2 = 74, Q3 = 76, data maksimum = 80
D. Data minimum = 70, Q1 = 71, Q2 = 72, Q3 = 76, data maksimum = 80
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 39. Soal `49d68d1b46c35ead12cca547`

Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.<br><br>50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65

| Opsi | Isi |
|---|---|
| A | Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5 |
| B | Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 15 |
| C | Q1 = 80; Q2 = 67,5; Q3 = 65; jangkauan kuartil = 15; simpangan kuartil = 7,5 |
| D | Q1 = 65; Q2 = 70,4; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5 |

Kunci sumber: `A`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d103b7d1c69ee28fb5d5929a8993bb7d7d672130d2aadc7812281c519c7930f2`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Penyebaran Data
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan kuartil bawah, kuartil atas, jangkauan dan simpangan antar kuartil dari data berikut.

50, 60, 85, 70, 65, 50, 80, 85, 90, 65, 65, 75, 80 65
Pilihan: A. Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5
B. Q1 = 65; Q2 = 67,5; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 15
C. Q1 = 80; Q2 = 67,5; Q3 = 65; jangkauan kuartil = 15; simpangan kuartil = 7,5
D. Q1 = 65; Q2 = 70,4; Q3 = 80; jangkauan kuartil = 15; simpangan kuartil = 7,5
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 40. Soal `581df18ab4eeb6c5cf613ab7`

Tentukan peluang untuk kejadian berikut. Misalnya, Tabel 7.2 distribusi peluang di bawah ini menunjukkan semua kemungkinan jumlah yang dapat diperoleh dari lemparan dua dadu.<br><br>tentukan jumlah yang lebih besar daripada 3

| Opsi | Isi |
|---|---|
| A | $\frac{3}{36}$ |
| B | $\frac{33}{36}$ |
| C | $\frac{35}{36}$ |
| D | $\frac{34}{36}$ |

![Gambar sumber soal 40](<../../../images/kelas10_panduan_siswa_kelas10.pdf-0240-02.png>)


Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0240-02.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi', 'membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `912f5e34c0fdda2d96e53bdfadfa99522e6052219b975fda267ec2192bed511b`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Distribusi Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan peluang untuk kejadian berikut. Misalnya, Tabel 7.2 distribusi peluang di bawah ini menunjukkan semua kemungkinan jumlah yang dapat diperoleh dari lemparan dua dadu.

tentukan jumlah yang lebih besar daripada 3
Pilihan: A. $\frac{3}{36}$
B. $\frac{33}{36}$
C. $\frac{35}{36}$
D. $\frac{34}{36}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 41. Soal `cc90109177ce7d63bb1a90a7`

Coba kamu tentukan peluang untuk kejadian berikut. Misalnya, Tabel 7.2 distribusi peluang di bawah ini menunjukkan semua kemungkinan jumlah yang dapat diperoleh dari lemparan dua dadu.<br><br>a. jumlah 2 atau 3

| Opsi | Isi |
|---|---|
| A | $\frac{1}{36}$ |
| B | $\frac{6}{36}$ |
| C | $\frac{3}{36}$ |
| D | $\frac{2}{36}$ |

![Gambar sumber soal 41](<../../../images/kelas10_panduan_siswa_kelas10.pdf-0240-02.png>)


Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0240-02.png. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5d7d7f4905cb80f7a8c59892a84590dd99525c18963f10deb1cde97944e97435`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Distribusi Peluang
Tipe soal: multiple_choice
Stimulus: -
Soal: Coba kamu tentukan peluang untuk kejadian berikut. Misalnya, Tabel 7.2 distribusi peluang di bawah ini menunjukkan semua kemungkinan jumlah yang dapat diperoleh dari lemparan dua dadu.

a. jumlah 2 atau 3
Pilihan: A. $\frac{1}{36}$
B. $\frac{6}{36}$
C. $\frac{3}{36}$
D. $\frac{2}{36}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 42. Soal `4dc162c092a693bfc3a3ad55`

Gunakan aturan penjumlahan untuk soal-soal berikut mengenai sepasang dadu yang dilempar.<br><br>Tentukan peluang mendapatkan dua angka sama atau berjumlah 2.

| Opsi | Isi |
|---|---|
| A | $\frac{7}{36}$ |
| B | $\frac{5}{36}$ |
| C | $\frac{6}{36}$ |
| D | $\frac{1}{36}$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi', 'menerapkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3a56cb6960c6b3dadfafc4cb1a45fe2a5102e746d9c5eaaf0b4260d5b99b2299`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Aturan Penjumlahan
Tipe soal: multiple_choice
Stimulus: -
Soal: Gunakan aturan penjumlahan untuk soal-soal berikut mengenai sepasang dadu yang dilempar.

Tentukan peluang mendapatkan dua angka sama atau berjumlah 2.
Pilihan: A. $\frac{7}{36}$
B. $\frac{5}{36}$
C. $\frac{6}{36}$
D. $\frac{1}{36}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 43. Soal `60d456804bca8ee0d55a4bb7`

Gunakan aturan penjumlahan untuk soal-soal berikut mengenai sepasang dadu yang dilempar.<br><br>Tentukan peluang mendapatkan dua angka sama atau berjumlah 5.

| Opsi | Isi |
|---|---|
| A | $\frac{6}{36}$ |
| B | $\frac{4}{36}$ |
| C | $\frac{9}{36}$ |
| D | $\frac{10}{36}$ |

Kunci sumber: `D`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi', 'menerapkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1dfda453f6c86910a6c1c63ad8f4295d75773b80b75f18d5115ef9464cd92aeb`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Aturan Penjumlahan
Tipe soal: multiple_choice
Stimulus: -
Soal: Gunakan aturan penjumlahan untuk soal-soal berikut mengenai sepasang dadu yang dilempar.

Tentukan peluang mendapatkan dua angka sama atau berjumlah 5.
Pilihan: A. $\frac{6}{36}$
B. $\frac{4}{36}$
C. $\frac{9}{36}$
D. $\frac{10}{36}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 44. Soal `6353e1b1ac73792bd65d8bcc`

Kirana sedang memainkan sebuah permainan yang menggunakan dadu. Dia harus melemparkan sepasang dadu dan mendapatkan angka dobel dan pada lemparan kedua mendapatkan jumlah enam. Dia ingin tahu berapa peluang ini dapat terjadi.<br><br>Mengapa aturan perkalian dapat digunakan untuk menentukan peluang ini? Berapa peluangnya?

| Opsi | Isi |
|---|---|
| A | Kedua lemparan saling bebas; peluangnya $\frac{11}{36}$ |
| B | Kedua lemparan saling bebas; peluangnya $\frac{5}{36}$ |
| C | Kedua lemparan saling bebas; peluangnya $\frac{5}{216}$ |
| D | Kedua lemparan saling bebas; peluangnya $\frac{1}{36}$ |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1d82bb7fdb208f9c31b41c2c1e42969fc32573aff3652924afe52a7b9958c2a2`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Aturan Perkalian
Tipe soal: multiple_choice
Stimulus: -
Soal: Kirana sedang memainkan sebuah permainan yang menggunakan dadu. Dia harus melemparkan sepasang dadu dan mendapatkan angka dobel dan pada lemparan kedua mendapatkan jumlah enam. Dia ingin tahu berapa peluang ini dapat terjadi.

Mengapa aturan perkalian dapat digunakan untuk menentukan peluang ini? Berapa peluangnya?
Pilihan: A. Kedua lemparan saling bebas; peluangnya $\frac{11}{36}$
B. Kedua lemparan saling bebas; peluangnya $\frac{5}{36}$
C. Kedua lemparan saling bebas; peluangnya $\frac{5}{216}$
D. Kedua lemparan saling bebas; peluangnya $\frac{1}{36}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 45. Soal `a870c7129a611f1645f3744f`

Sebuah dadu dilempar dua kali. Hitung peluang untuk mendapatkan<br><br>dua angka genap

| Opsi | Isi |
|---|---|
| A | $\frac{1}{2}$ |
| B | $\frac{1}{4}$ |
| C | $\frac{1}{36}$ |
| D | $\frac{1}{12}$ |

Kunci sumber: `B`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `796c679b6c6bf26873fca7a2167c0715e43acad660055b5f5ce433f6c564a419`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Aturan Perkalian
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah dadu dilempar dua kali. Hitung peluang untuk mendapatkan

dua angka genap
Pilihan: A. $\frac{1}{2}$
B. $\frac{1}{4}$
C. $\frac{1}{36}$
D. $\frac{1}{12}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 46. Soal `4e77f956826bf22b33dbf58b`

Putu memiliki roda putar yang terbagi menjadi lima juring yang sama besar, masing-masing ditulis angka 1, 2, 3, 4, dan 5. Dia akan memilih sampel dengan memutar roda tersebut sebanyak tiga kali. Tentukan peluang dia mendapatkan sampel yang rata-ratanya kurang dari 2.

| Opsi | Isi |
|---|---|
| A | 6/125 |
| B | 5/125 |
| C | 10/125 (atau 0,08) |
| D | 3/125 |

Kunci sumber: `C`; status AI: `None`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: —
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 10 / Matematika SMA Kelas 10. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f9a1f682c862737acfa64431212cf2d5360ba661d2ccc52dbea9d74153cbfdf7`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {} | no_consensus / incomplete | — |
| Dimensi pengetahuan | {} | no_consensus / incomplete | — |
| Intended difficulty | {} | no_consensus / incomplete | — |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 10
Topik: Matematika SMA Kelas 10
Subtopik: Pemilihan Sampel
Tipe soal: multiple_choice
Stimulus: -
Soal: Putu memiliki roda putar yang terbagi menjadi lima juring yang sama besar, masing-masing ditulis angka 1, 2, 3, 4, dan 5. Dia akan memilih sampel dengan memutar roda tersebut sebanyak tiga kali. Tentukan peluang dia mendapatkan sampel yang rata-ratanya kurang dari 2.
Pilihan: A. 6/125
B. 5/125
C. 10/125 (atau 0,08)
D. 3/125
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": null, "knowledgeDimension": null, "intendedDifficulty": null}`. Routing: `llm_retry_or_manual_review`.
Status konten: `None`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": null, "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": null, "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": null, "agreement": null}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
