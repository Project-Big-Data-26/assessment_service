# Validasi ulang soal kelas 7 — Gemini blind N=3 dan diagnostik IndoBERT

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v5-blind-smp7-key-verified`. Rubrik: `math-rubric-3x4x3-v3-smp7-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 7 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan menjadi keputusan silver operasional.

Checkpoint dikunci dengan SHA-256 sebelum pemeriksaan scope IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Model SD berada di luar cakupan kelas 7, sehingga seluruh head abstain dan tidak menghasilkan ukuran agreement dengan label blind.

Jumlah soal: 49; distribusi label advisory: `{"mathCognitiveDomain": {"knowing": 12, "applying": 32, "reasoning": 5}, "knowledgeDimension": {"conceptual": 28, "procedural": 17, "factual": 4, "metacognitive": 0}, "intendedDifficulty": {"Easy": 28, "Medium": 20, "Hard": 1}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"knowing": 12, "applying": 32, "reasoning": 5}, "knowledgeDimension": {"conceptual": 28, "procedural": 17, "factual": 4}, "intendedDifficulty": {"Easy": 28, "Medium": 20, "Hard": 1}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"silver_ready": 49}`.
Run awal sukses: 147/147; adjudikasi: 16; token sukses tercatat: 386,009.

Seluruh label memakai provenance ai_silver. Delivery memakai snapshot silver yang lolos qualification. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

IndoBERT aktif: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Artifact belum disetujui; tidak ada training ulang dalam batch ini. Difficulty model lama dapat mengalami class collapse. Confidence dari kalibrasi kelas 1 yang kecil belum membuktikan ketepatan label.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten dapat masuk snapshot silver operasional.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 28 | 28 | [Easy.json](difficulty/Easy.json) |
| Medium | 20 | 20 | [Medium.json](difficulty/Medium.json) |
| Hard | 1 | 1 | [Hard.json](difficulty/Hard.json) |

## Perhitungan yang dipakai

Untuk kelas 7, encoder dan head IndoBERT tidak dijalankan karena scope model hanya kelas 1–6. Probabilitas kosong, label/confidence/entropy null, dan action abstain berasal dari pemeriksaan scope runtime. Suara Gemini adalah bukti penilaian advisory, bukan probabilitas IndoBERT.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

Model IndoBERT lama hanya mendukung SD kelas 1–6. Untuk kelas 7, diagnostik mengembalikan `out_of_scope` dan `abstain`: label, confidence, dan entropy null serta probabilitas kosong. Label advisory mengikuti Gemini blind dengan rubrik SMP kelas 7. Tidak ada inferensi SD yang dipaksakan sebagai prediksi SMP.

## 1. Soal `96d7ccf391bfd43c525dac4f`

Urutkan bilangan bulat di bawah ini dari yang terkecil ke terbesar.<br><br>$ -8, 4, -2, 12 $

| Opsi | Isi |
|---|---|
| A | $ 12, 4, -2, -8 $ |
| B | $ -8, -2, 4, 12 $ |
| C | $ -2, -8, 4, 12 $ |
| D | $ -2, 4, -8, 12 $ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Pada garis bilangan, bilangan negatif yang memiliki nilai mutlak lebih besar berada lebih jauh di sebelah kiri (lebih kecil). Urutan dari terkecil ke terbesar adalah -8, -2, 4, 12.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f36f8772b8bbd3b4533dd4ad518326827a616aa940a1ecf4100e6944f9a4bb1c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 1661 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 1659 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1674 |

Run 1 — solusi: Membandingkan nilai bilangan pada garis bilangan: -8 < -2 < 4 < 12.
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan proses langsung mengurutkan bilangan bulat berdasarkan nilai pada garis bilangan, yang merupakan prosedur rutin.. Bukti: Urutkan bilangan bulat di bawah ini dari yang terkecil ke terbesar.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip urutan bilangan bulat (konsep nilai negatif dan positif) untuk mengurutkannya.. Bukti: -8, 4, -2, 12
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, hanya memerlukan pemahaman dasar tentang urutan bilangan bulat pada garis bilangan tanpa langkah kompleks.. Bukti: Urutkan bilangan bulat di bawah ini dari yang terkecil ke terbesar.; -8, 4, -2, 12

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang urutan bilangan bulat pada garis bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan bilangan bulat adalah materi dasar kelas 7 yang sangat familiar dan tidak memerlukan strategi non-rutin. |

Run 2 — solusi: Membandingkan nilai bilangan: -8 adalah yang terkecil (paling kiri pada garis bilangan), diikuti -2, kemudian 4, dan 12 adalah yang terbesar. Urutan: -8, -2, 4, 12.
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan prosedur pengurutan bilangan bulat yang merupakan proses langsung berdasarkan definisi nilai bilangan pada garis bilangan.. Bukti: Urutkan bilangan bulat di bawah ini dari yang terkecil ke terbesar.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep nilai bilangan bulat (bilangan negatif vs positif) untuk menentukan urutan.. Bukti: -8, 4, -2, 12
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, hanya memerlukan pemahaman dasar tentang posisi bilangan bulat pada garis bilangan tanpa langkah kompleks.. Bukti: -8, 4, -2, 12

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang garis bilangan dan perbandingan bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan bilangan bulat adalah materi dasar kelas 7 yang sangat standar dan rutin. |

Run 3 — solusi: Pada garis bilangan, bilangan negatif yang memiliki nilai mutlak lebih besar berada lebih jauh di sebelah kiri (lebih kecil). Urutan dari terkecil ke terbesar adalah -8, -2, 4, 12.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan pemahaman tentang urutan bilangan bulat pada garis bilangan, yang merupakan prosedur rutin.. Bukti: Urutkan bilangan bulat di bawah ini dari yang terkecil ke terbesar.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip urutan bilangan bulat (konsep) dan cara mengurutkannya (prosedur).. Bukti: -8, 4, -2, 12
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, hanya memerlukan pemahaman dasar tentang posisi bilangan bulat pada garis bilangan.. Bukti: -8, 4, -2, 12

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang garis bilangan dan nilai bilangan bulat negatif. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan bilangan bulat adalah materi dasar kelas 7 yang sangat familiar dan tidak memerlukan langkah kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2897`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta siswa melakukan proses langsung mengurutkan bilangan bulat berdasarkan nilai pada garis bilangan, yang merupakan prosedur rutin.
- Dimensi pengetahuan `conceptual`: Siswa perlu memahami prinsip urutan bilangan bulat (konsep nilai negatif dan positif) untuk mengurutkannya.
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung, hanya memerlukan pemahaman dasar tentang posisi bilangan bulat pada garis bilangan tanpa langkah kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang urutan bilangan bulat pada garis bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan bilangan bulat adalah materi dasar kelas 7 yang sangat familiar dan tidak memerlukan strategi non-rutin. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Memahami Bilangan Bulat
Tipe soal: multiple_choice
Stimulus: -
Soal: Urutkan bilangan bulat di bawah ini dari yang terkecil ke terbesar.

$ -8, 4, -2, 12 $
Pilihan: A. $ 12, 4, -2, -8 $
B. $ -8, -2, 4, 12 $
C. $ -2, -8, 4, 12 $
D. $ -2, 4, -8, 12 $
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `ab56c97ac6d94cbc068098c2`

Nyatakan bilangan berikut ini dengan tanda positif atau negatif.<br><br>Penjualan di toko hari ini mengalami kerugian sebesar Rp250.000,00.

| Opsi | Isi |
|---|---|
| A | $-250.000$ |
| B | $+250.000$ |
| C | $-25.000$ |
| D | $+25.000$ |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Dalam konteks bilangan bulat, kerugian atau penurunan nilai direpresentasikan dengan tanda negatif (-). Kerugian sebesar Rp250.000,00 ditulis sebagai -250.000.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e4f0af33f057ccbbea8ad15bc19a90d29a2cffea9a2e3ff8d8b1b5cbf48b509b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 1711 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 1665 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1674 |

Run 1 — solusi: Dalam konteks bilangan bulat, kerugian atau penurunan nilai direpresentasikan dengan tanda negatif (-). Kerugian sebesar Rp250.000,00 ditulis sebagai -250.000.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengenali dan menerapkan konvensi tanda bilangan bulat dalam konteks kehidupan sehari-hari (kerugian sebagai negatif). Ini adalah proses langsung yang termasuk dalam kategori knowing.. Bukti: Nyatakan bilangan berikut ini dengan tanda positif atau negatif.; Penjualan di toko hari ini mengalami kerugian sebesar Rp250.000,00.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep bahwa bilangan bulat dapat digunakan untuk merepresentasikan arah atau nilai yang berlawanan (positif/negatif) dalam konteks nyata.. Bukti: Nyatakan bilangan berikut ini dengan tanda positif atau negatif.; kerugian sebesar Rp250.000,00
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan pemahaman satu konsep (kerugian = negatif) tanpa langkah perhitungan atau strategi kompleks.. Bukti: Nyatakan bilangan berikut ini dengan tanda positif atau negatif.; Penjualan di toko hari ini mengalami kerugian sebesar Rp250.000,00.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bilangan bulat dan penggunaan tanda positif/negatif dalam konteks nyata. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 sebagai pengenalan awal konsep bilangan bulat dalam kehidupan sehari-hari. |

Run 2 — solusi: Dalam konteks bilangan bulat, kerugian atau penurunan nilai dinyatakan dengan tanda negatif (-). Maka, kerugian Rp250.000,00 ditulis sebagai -250.000.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengenali dan menerapkan konvensi tanda bilangan bulat pada situasi nyata yang sederhana. Ini adalah proses langsung dalam memahami konsep bilangan bulat.. Bukti: Nyatakan bilangan berikut ini dengan tanda positif atau negatif.; Penjualan di toko hari ini mengalami kerugian sebesar Rp250.000,00.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip bahwa bilangan negatif digunakan untuk merepresentasikan kerugian atau penurunan, yang merupakan pemahaman konseptual dasar.. Bukti: Nyatakan bilangan berikut ini dengan tanda positif atau negatif.
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya memerlukan pemahaman satu konsep dasar (kerugian = negatif) tanpa langkah perhitungan atau strategi kompleks.. Bukti: Penjualan di toko hari ini mengalami kerugian sebesar Rp250.000,00.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bilangan bulat dan penggunaan tanda positif/negatif dalam kehidupan sehari-hari. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 sebagai pengenalan awal bilangan bulat dalam konteks nyata. |

Run 3 — solusi: Dalam konteks keuangan, kerugian direpresentasikan dengan tanda negatif (-). Kerugian sebesar Rp250.000,00 ditulis sebagai -250.000.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk mengenali dan menerapkan konvensi tanda (positif/negatif) pada situasi nyata yang sederhana, yang termasuk dalam kategori menerapkan prosedur dasar.. Bukti: Nyatakan bilangan berikut ini dengan tanda positif atau negatif.; Penjualan di toko hari ini mengalami kerugian sebesar Rp250.000,00.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang konvensi simbol matematika (tanda negatif) untuk merepresentasikan konsep kerugian.. Bukti: Nyatakan bilangan berikut ini dengan tanda positif atau negatif.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin bagi siswa kelas 7 yang baru mempelajari bilangan bulat. Tidak ada langkah kompleks atau strategi nonrutin yang diperlukan.. Bukti: Penjualan di toko hari ini mengalami kerugian sebesar Rp250.000,00.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar bahwa kerugian dalam konteks bilangan bulat direpresentasikan dengan tanda negatif. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bilangan bulat dan penggunaannya dalam konteks sehari-hari adalah kurikulum standar kelas 7. Soal ini menguji pemahaman dasar tanpa beban komputasi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3113`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta siswa untuk mengenali dan menerapkan konvensi tanda bilangan bulat dalam konteks kehidupan sehari-hari (kerugian sebagai negatif). Ini adalah proses langsung yang termasuk dalam kategori knowing.
- Dimensi pengetahuan `conceptual`: Siswa perlu memahami konsep bahwa bilangan bulat dapat digunakan untuk merepresentasikan arah atau nilai yang berlawanan (positif/negatif) dalam konteks nyata.
- Intended difficulty `Easy`: Soal ini sangat mendasar, hanya memerlukan pemahaman satu konsep (kerugian = negatif) tanpa langkah perhitungan atau strategi kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bilangan bulat dan penggunaan tanda positif/negatif dalam konteks nyata. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 sebagai pengenalan awal konsep bilangan bulat dalam kehidupan sehari-hari. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Memahami Bilangan Bulat
Tipe soal: multiple_choice
Stimulus: -
Soal: Nyatakan bilangan berikut ini dengan tanda positif atau negatif.

Penjualan di toko hari ini mengalami kerugian sebesar Rp250.000,00.
Pilihan: A. $-250.000$
B. $+250.000$
C. $-25.000$
D. $+25.000$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `27c0ef9c02bb094753844acb`

Tabel 1.1 Detail Perhitungan Nilai dan Efek Performa Bagi Klub dari Berbagai Proses Transfer<br>\| Proses Transfer Pemain \| Perhitungan Nilai \| Efek Performa Bagi Klub \|<br>\|---\|---\|---\|<br>\| Mendapatkan satu pemain bagus \| +(+1) \| Performa naik \|<br>\| Mendapatkan satu pemain buruk \| +(−1) \| Performa turun \|<br>\| Melepaskan satu pemain bagus \| −(+1) \| Performa turun \|<br>\| Melepaskan satu pemain buruk \| −(−1) \| Performa naik \|<br>Nilai dan efek performa bagi klub tersebut setelah melakukan transfer pemain di bawah ini.<br><br>Klub D: mendapatkan 5 pemain bagus, mendapatkan 2 pemain buruk, melepaskan 3 pemain bagus, melepaskan 4 pemain buruk.

| Opsi | Isi |
|---|---|
| A | $+(+5) + (+2) - (+3) - (+4) = 0$, performa tetap |
| B | $+(+5) + (-2) - (+3) - (-4) = +4$, performa naik |
| C | $+(+5) + (-2) - (+3) - (-4) = -4$, performa turun |
| D | $+(+5) + (-2) - (+3) - (-4) = +14$, performa naik |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Klub D melakukan: mendapatkan 5 pemain bagus (+5), mendapatkan 2 pemain buruk (-2), melepaskan 3 pemain bagus (-3), melepaskan 4 pemain buruk (+4). Total: 5 - 2 - 3 + 4 = 4. Hasil positif berarti performa naik.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4cbaf0b99ad7d069a5ab342d07461c8bc78f4c967f79c1f3bb374015e78c9d81`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 1951 |
| 2 | success | valid / verified | applying | procedural | Medium | 2008 |
| 3 | success | valid / verified | applying | procedural | Medium | 1969 |

Run 1 — solusi: Klub D melakukan: mendapatkan 5 pemain bagus (+5), mendapatkan 2 pemain buruk (-2), melepaskan 3 pemain bagus (-3), melepaskan 4 pemain buruk (+4). Total: 5 - 2 - 3 + 4 = 4. Hasil positif berarti performa naik.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan deskripsi situasi ke dalam operasi bilangan bulat berdasarkan aturan yang diberikan di tabel, kemudian melakukan perhitungan aritmatika dasar.. Bukti: Klub D: mendapatkan 5 pemain bagus, mendapatkan 2 pemain buruk, melepaskan 3 pemain bagus, melepaskan 4 pemain buruk.
- Dimensi pengetahuan `classify/procedural`: Siswa harus memahami aturan operasi tanda (seperti -(-1) menjadi +1) dan menerapkannya pada konteks masalah.. Bukti: Perhitungan Nilai \| Efek Performa Bagi Klub; +(+1) \| Performa naik; -(+1) \| Performa turun; -(-1) \| Performa naik
- Intended difficulty `classify/Medium`: Soal ini melibatkan beberapa langkah rutin (penerjemahan 4 kondisi ke operasi matematika) dan operasi bilangan bulat dasar. Tingkat kesulitan menengah karena siswa harus teliti dengan tanda operasi.. Bukti: Klub D: mendapatkan 5 pemain bagus, mendapatkan 2 pemain buruk, melepaskan 3 pemain bagus, melepaskan 4 pemain buruk.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi penjumlahan dan pengurangan bilangan bulat, termasuk pemahaman tanda negatif. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena menguji pemahaman operasi bilangan bulat dalam konteks pemodelan sederhana. |

Run 2 — solusi: Klub D: 5 pemain bagus (5 * +1), 2 pemain buruk (2 * -1), 3 pemain bagus dilepas (- (3 * +1)), 4 pemain buruk dilepas (- (4 * -1)). Perhitungan: 5 + (-2) - 3 - (-4) = 5 - 2 - 3 + 4 = 4. Hasil positif menunjukkan performa naik.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan narasi ke dalam model matematika menggunakan aturan operasi bilangan bulat yang diberikan dalam tabel, kemudian melakukan operasi hitung tersebut.. Bukti: Klub D: mendapatkan 5 pemain bagus, mendapatkan 2 pemain buruk, melepaskan 3 pemain bagus, melepaskan 4 pemain buruk.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang aturan operasi bilangan bulat (terutama pengurangan bilangan negatif) dan konsep konseptual tentang bagaimana tanda operasi memengaruhi hasil akhir.. Bukti: Perhitungan Nilai \| Efek Performa Bagi Klub; +(+1) \| Performa naik; -(+1) \| Performa turun
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah rutin (perkalian dan penjumlahan/pengurangan bilangan bulat) dengan aturan tanda yang eksplisit diberikan. Tingkat kesulitan ini sesuai untuk kelas 7.. Bukti: Klub D: mendapatkan 5 pemain bagus, mendapatkan 2 pemain buruk, melepaskan 3 pemain bagus, melepaskan 4 pemain buruk.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi dasar bilangan bulat (penjumlahan, pengurangan, perkalian sederhana) dan pemahaman aturan tanda negatif. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini menuntut ketelitian dalam menerapkan aturan tanda pada operasi bilangan bulat yang merupakan materi standar kelas 7. Langkah-langkahnya rutin namun memerlukan perhatian pada tanda negatif ganda. |

Run 3 — solusi: Klub D: 5 pemain bagus (5 * +1 = +5), 2 pemain buruk (2 * -1 = -2), 3 pemain bagus dilepas (3 * -(+1) = -3), 4 pemain buruk dilepas (4 * -(-1) = +4). Total: 5 - 2 - 3 + 4 = 4. Performa naik.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan narasi ke dalam model matematika menggunakan aturan operasi bilangan bulat yang diberikan, kemudian melakukan perhitungan rutin.. Bukti: Klub D: mendapatkan 5 pemain bagus, mendapatkan 2 pemain buruk, melepaskan 3 pemain bagus, melepaskan 4 pemain buruk.
- Dimensi pengetahuan `classify/procedural`: Siswa harus memahami aturan operasi bilangan bulat (terutama pengurangan bilangan negatif) dan menerapkannya pada konteks yang diberikan.. Bukti: Perhitungan Nilai \| Efek Performa Bagi Klub; +(+1) \| Performa naik; -(+1) \| Performa turun; -(-1) \| Performa naik
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman aturan tanda yang spesifik dan perhitungan beruntun. Tingkat kesulitan menengah karena melibatkan beberapa langkah operasi bilangan bulat yang harus dikelola dengan teliti.. Bukti: Klub D: mendapatkan 5 pemain bagus, mendapatkan 2 pemain buruk, melepaskan 3 pemain bagus, melepaskan 4 pemain buruk.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi penjumlahan dan pengurangan bilangan bulat, termasuk aturan tanda negatif. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena menguji pemahaman operasi bilangan bulat dalam konteks nyata yang terstruktur. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Operasi Hitung Bilangan Bulat
Tipe soal: multiple_choice
Stimulus: -
Soal: Tabel 1.1 Detail Perhitungan Nilai dan Efek Performa Bagi Klub dari Berbagai Proses Transfer
| Proses Transfer Pemain | Perhitungan Nilai | Efek Performa Bagi Klub |
|---|---|---|
| Mendapatkan satu pemain bagus | +(+1) | Performa naik |
| Mendapatkan satu pemain buruk | +(−1) | Performa turun |
| Melepaskan satu pemain bagus | −(+1) | Performa turun |
| Melepaskan satu pemain buruk | −(−1) | Performa naik |
Nilai dan efek performa bagi klub tersebut setelah melakukan transfer pemain di bawah ini.

Klub D: mendapatkan 5 pemain bagus, mendapatkan 2 pemain buruk, melepaskan 3 pemain bagus, melepaskan 4 pemain buruk.
Pilihan: A. $+(+5) + (+2) - (+3) - (+4) = 0$, performa tetap
B. $+(+5) + (-2) - (+3) - (-4) = +4$, performa naik
C. $+(+5) + (-2) - (+3) - (-4) = -4$, performa turun
D. $+(+5) + (-2) - (+3) - (-4) = +14$, performa naik
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `dee148c840c4fff078ce4769`

Kapal selam dapat menyelam hingga ke dasar laut. Kapal selam dapat bergerak hingga kedalaman 180 meter di bawah permukaan laut dalam waktu 3 jam. Jawablah pertanyaan di bawah ini.<br><br>Pada kedalaman berapa meter di bawah permukaan laut yang dicapai kapal selam dalam 1 jam? Nyatakan dalam bilangan bulat positif atau negatif.

| Opsi | Isi |
|---|---|
| A | $60$ |
| B | $-60$ |
| C | $-180$ |
| D | $-540$ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Kedalaman 180 meter di bawah permukaan laut dinyatakan sebagai -180. Untuk mencari kedalaman per jam, bagi total kedalaman dengan waktu: -180 / 3 = -60.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `daab3450920682c778e08de33a28821bd0f5f47663ffc655e61c42460bbdeb0a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1712 |
| 2 | success | valid / verified | applying | procedural | Easy | 1733 |
| 3 | success | valid / verified | applying | procedural | Easy | 1705 |

Run 1 — solusi: Kedalaman 180 meter di bawah permukaan laut dinyatakan sebagai -180. Untuk mencari kedalaman per jam, bagi total kedalaman dengan waktu: -180 / 3 = -60.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep pembagian bilangan bulat dan memahami konvensi tanda untuk kedalaman (di bawah permukaan laut sebagai negatif). Ini adalah penerapan prosedur rutin pada situasi kontekstual.. Bukti: Pada kedalaman berapa meter di bawah permukaan laut yang dicapai kapal selam dalam 1 jam?; Nyatakan dalam bilangan bulat positif atau negatif.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang bagaimana merepresentasikan situasi dunia nyata (kedalaman) ke dalam sistem bilangan bulat dan melakukan operasi pembagian dasar.. Bukti: 180 meter di bawah permukaan laut; Nyatakan dalam bilangan bulat positif atau negatif
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan satu langkah operasi pembagian dan satu langkah konversi representasi (kedalaman menjadi bilangan negatif).. Bukti: 180 meter di bawah permukaan laut; dalam waktu 3 jam; dalam 1 jam

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar bilangan bulat negatif dan operasi pembagian bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena melibatkan konsep dasar bilangan bulat negatif dalam konteks yang umum dipelajari di awal bab bilangan. |

Run 2 — solusi: Kedalaman 180 meter di bawah permukaan laut dinyatakan sebagai -180. Dalam 1 jam, kedalamannya adalah -180 / 3 = -60 meter.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep bilangan bulat untuk merepresentasikan posisi di bawah permukaan laut (negatif) dan melakukan operasi pembagian sederhana untuk menentukan laju perubahan kedalaman.. Bukti: Pada kedalaman berapa meter di bawah permukaan laut yang dicapai kapal selam dalam 1 jam? Nyatakan dalam bilangan bulat positif atau negatif.
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut pemahaman prosedural tentang operasi pembagian bilangan bulat dan pemahaman konseptual tentang penggunaan tanda negatif untuk merepresentasikan posisi di bawah permukaan laut.. Bukti: Nyatakan dalam bilangan bulat positif atau negatif.; -180 : 3 = -60
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menerjemahkan konteks ke dalam bilangan bulat (-180) dan melakukan satu operasi pembagian sederhana. Tidak ada kendala kompleks atau strategi nonrutin yang diperlukan.. Bukti: 180 meter di bawah permukaan laut; dalam waktu 3 jam; dalam 1 jam

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar bilangan bulat (negatif) dan operasi pembagian bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena menguji pemahaman dasar tentang penggunaan bilangan bulat dalam konteks nyata (kedalaman) dan operasi hitung dasar. |

Run 3 — solusi: Kedalaman 180 meter di bawah permukaan laut dinyatakan sebagai -180. Kecepatan selam per jam adalah -180 / 3 = -60. Jadi, dalam 1 jam kapal berada pada kedalaman -60 meter.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep pembagian bilangan bulat dan memahami representasi kedalaman di bawah permukaan laut sebagai bilangan negatif.. Bukti: Kapal selam dapat bergerak hingga kedalaman 180 meter di bawah permukaan laut dalam waktu 3 jam; Nyatakan dalam bilangan bulat positif atau negatif
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi pembagian bilangan bulat dan konsep konseptual tentang penggunaan tanda negatif untuk merepresentasikan posisi di bawah permukaan laut.. Bukti: 180 meter di bawah permukaan laut; dalam waktu 3 jam
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 7. Siswa hanya perlu memahami representasi bilangan negatif untuk kedalaman dan melakukan satu operasi pembagian sederhana.. Bukti: 180 meter di bawah permukaan laut; dalam waktu 3 jam; dalam 1 jam

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar bilangan bulat dan operasi pembagian. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sesuai dengan tingkat kelas 7 karena melibatkan operasi bilangan bulat dasar dalam konteks nyata yang familiar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3154`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan konsep bilangan bulat untuk merepresentasikan posisi di bawah permukaan laut (negatif) dan melakukan operasi pembagian sederhana untuk menentukan laju perubahan kedalaman.
- Dimensi pengetahuan `procedural`: Soal ini menuntut pemahaman prosedural tentang operasi pembagian bilangan bulat dan pemahaman konseptual tentang penggunaan tanda negatif untuk merepresentasikan posisi di bawah permukaan laut.
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menerjemahkan konteks ke dalam bilangan bulat (-180) dan melakukan satu operasi pembagian sederhana. Tidak ada kendala kompleks atau strategi nonrutin yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar bilangan bulat negatif dan operasi pembagian bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena melibatkan konsep dasar bilangan bulat negatif dalam konteks yang umum dipelajari di awal bab bilangan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Operasi Hitung Bilangan Bulat
Tipe soal: multiple_choice
Stimulus: -
Soal: Kapal selam dapat menyelam hingga ke dasar laut. Kapal selam dapat bergerak hingga kedalaman 180 meter di bawah permukaan laut dalam waktu 3 jam. Jawablah pertanyaan di bawah ini.

Pada kedalaman berapa meter di bawah permukaan laut yang dicapai kapal selam dalam 1 jam? Nyatakan dalam bilangan bulat positif atau negatif.
Pilihan: A. $60$
B. $-60$
C. $-180$
D. $-540$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `59b2ebb065c0acdddee9003d`

Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari. Karena Aldi baru mencoba untuk ikut berbagi makanan, maka ia akan melakukannya setiap 8 hari.<br><br>Jika pada hari ini, Senin tanggal 8 Agustus 2022 mereka bertiga membagikan makanan secara bersama-sama, maka tanggal berapa mereka melakukannya bersama kembali?

| Opsi | Isi |
|---|---|
| A | 2 September 2022 |
| B | 16 Agustus 2022 |
| C | 20 Agustus 2022 |
| D | 1 September 2022 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Mencari KPK dari 4, 6, dan 8. Kelipatan 4: 4, 8, 12, 16, 20, 24. Kelipatan 6: 6, 12, 18, 24. Kelipatan 8: 8, 16, 24. KPK adalah 24. Menambahkan 24 hari ke 8 Agustus 2022: 31 (hari dalam Agustus) - 8 = 23 hari tersisa di Agustus. 24 - 23 = 1. Jadi, 1 September 2022.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `393317723825f5f61634a11651d86fd3dabb908c2b28e41bd8a8b49f69a64432`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 1911 |
| 2 | success | valid / verified | applying | procedural | Medium | 1864 |
| 3 | success | valid / verified | applying | procedural | Medium | 1865 |

Run 1 — solusi: Mencari KPK dari 4, 6, dan 8. Kelipatan 4: 4, 8, 12, 16, 20, 24. Kelipatan 6: 6, 12, 18, 24. Kelipatan 8: 8, 16, 24. KPK adalah 24. Menambahkan 24 hari ke 8 Agustus 2022: 31 (hari dalam Agustus) - 8 = 23 hari tersisa di Agustus. 24 - 23 = 1. Jadi, 1 September 2022.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa masalah ini menuntut pencarian kelipatan persekutuan terkecil (KPK) dari tiga bilangan untuk menentukan waktu pertemuan berikutnya, yang merupakan penerapan prosedur rutin dalam konteks soal cerita.. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari... Aldi... setiap 8 hari.; mereka bertiga membagikan makanan secara bersama-sama, maka tanggal berapa mereka melakukannya bersama kembali?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara mencari KPK dari tiga bilangan dan menerapkannya pada konteks kalender.. Bukti: KPK(4, 6, 8) = 24 hari
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena melibatkan beberapa langkah rutin yang saling terkait: mencari KPK dari tiga bilangan, memahami jumlah hari dalam bulan Agustus (31 hari), dan melakukan penjumlahan tanggal yang melintasi pergantian bulan.. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari... Aldi... setiap 8 hari.; 8 Agustus 2022... tanggal berapa mereka melakukannya bersama kembali?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep KPK, operasi penjumlahan dasar, pengetahuan jumlah hari dalam bulan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi KPK adalah standar kelas 7. Penambahan tanggal yang melintasi bulan adalah keterampilan dasar yang relevan untuk tingkat ini. |

Run 2 — solusi: KPK dari 4, 6, dan 8 adalah 24. Menambahkan 24 hari ke tanggal 8 Agustus 2022: Agustus memiliki 31 hari. 31 - 8 = 23 hari tersisa di bulan Agustus. Maka, 24 - 23 = 1 hari di bulan berikutnya, yaitu 1 September 2022.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa masalah ini memerlukan pencarian KPK dari tiga bilangan (4, 6, 8) untuk menentukan interval waktu pertemuan berikutnya, yang merupakan penerapan konsep pada situasi rutin.. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari... Aldi... setiap 8 hari.; mereka bertiga membagikan makanan secara bersama-sama, maka tanggal berapa mereka melakukannya bersama kembali?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma atau teknik mencari KPK untuk menyelesaikan masalah kontekstual.. Bukti: KPK(4, 6, 8) = 24 hari
- Intended difficulty `classify/Medium`: Soal ini memerlukan beberapa langkah rutin: mencari KPK dari tiga bilangan, lalu melakukan operasi penambahan tanggal dengan memperhatikan jumlah hari dalam bulan (Agustus 31 hari). Ini adalah tugas standar kelas 7.. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari... Aldi... setiap 8 hari.; 8 Agustus 2022... tanggal berapa mereka melakukannya bersama kembali?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep KPK dan pengetahuan jumlah hari dalam bulan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Masalah KPK tiga bilangan dengan penambahan tanggal adalah materi rutin kelas 7 yang memerlukan ketelitian dalam perhitungan kalender. |

Run 3 — solusi: KPK dari 4, 6, dan 8 adalah 24. Menambahkan 24 hari ke tanggal 8 Agustus 2022 (Agustus memiliki 31 hari): 31 - 8 = 23 hari tersisa di Agustus, sehingga 24 - 23 = 1 hari di bulan berikutnya. Jadi, 1 September 2022.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa masalah ini menuntut pencarian kelipatan persekutuan terkecil (KPK) dari tiga bilangan untuk menentukan waktu pertemuan berikutnya, yang merupakan penerapan prosedur rutin pada situasi kontekstual.. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari... Aldi... setiap 8 hari.; mereka bertiga membagikan makanan secara bersama-sama
- Dimensi pengetahuan `classify/procedural`: Penyelesaian memerlukan pemahaman tentang konsep kelipatan persekutuan dan algoritma untuk menghitung KPK, yang termasuk dalam pengetahuan prosedural.. Bukti: KPK(4, 6, 8) = 24 hari
- Intended difficulty `classify/Medium`: Soal ini melibatkan beberapa langkah rutin: mencari KPK dari tiga bilangan dan melakukan perhitungan kalender (penjumlahan hari dengan memperhatikan jumlah hari dalam bulan). Ini adalah tugas standar untuk kelas 7.. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari... Aldi... setiap 8 hari.; 8 Agustus 2022... tanggal berapa mereka melakukannya bersama kembali?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep kelipatan, KPK, dan pengetahuan dasar jumlah hari dalam kalender. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi KPK adalah kurikulum inti kelas 7. Perhitungan kalender yang melibatkan transisi bulan adalah tantangan rutin yang sesuai untuk tingkat ini. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Faktor Bilangan Bulat
Tipe soal: multiple_choice
Stimulus: -
Soal: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari. Karena Aldi baru mencoba untuk ikut berbagi makanan, maka ia akan melakukannya setiap 8 hari.

Jika pada hari ini, Senin tanggal 8 Agustus 2022 mereka bertiga membagikan makanan secara bersama-sama, maka tanggal berapa mereka melakukannya bersama kembali?
Pilihan: A. 2 September 2022
B. 16 Agustus 2022
C. 20 Agustus 2022
D. 1 September 2022
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `75bcff470eef603207c7ef0c`

Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari. Jika pada hari ini mereka membagikan makanan bersama-sama, tentukan setiap berapa hari mereka membagikan makanan secara bersama-sama kembali?

| Opsi | Isi |
|---|---|
| A | setiap 12 hari |
| B | setiap 10 hari |
| C | setiap 24 hari |
| D | setiap 2 hari |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Menentukan KPK dari 4 dan 6. Kelipatan 4: 4, 8, 12, 16... Kelipatan 6: 6, 12, 18... KPK(4, 6) = 12.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['mengidentifikasi', 'menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4e87fc0cc67f815f60adff4ba396dc641e6de9e4731472d470ec2813d0ebf104`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1686 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1683 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1685 |

Run 1 — solusi: Menentukan KPK dari 4 dan 6. Kelipatan 4: 4, 8, 12, 16... Kelipatan 6: 6, 12, 18... KPK(4, 6) = 12.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi situasi sebagai masalah kelipatan persekutuan terkecil (KPK) dan menerapkan prosedur untuk menemukannya.. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari; tentukan setiap berapa hari mereka membagikan makanan secara bersama-sama kembali
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang kelipatan persekutuan dalam konteks kehidupan sehari-hari.. Bukti: setiap 4 hari; setiap 6 hari; bersama-sama kembali
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin yang umum diajarkan di kelas 7 terkait KPK. Prosedur penyelesaiannya langsung dan familiar.. Bukti: Anita membagikan makanan setiap 4 hari; Rossa membagikan makanan setiap 6 hari

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep kelipatan bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah KPK dua bilangan kecil adalah standar kompetensi kelas 7 yang bersifat rutin. |

Run 2 — solusi: Menentukan KPK dari 4 dan 6. Kelipatan 4: 4, 8, 12, 16... Kelipatan 6: 6, 12, 18... KPK(4, 6) = 12.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi situasi sebagai masalah KPK dan menerapkan prosedur untuk mencari kelipatan persekutuan terkecil dari dua bilangan.. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari; tentukan setiap berapa hari mereka membagikan makanan secara bersama-sama kembali
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep kelipatan dan hubungan antar bilangan dalam konteks periodisitas.. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin yang sering ditemui di kelas 7 terkait aplikasi KPK dalam kehidupan sehari-hari.. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep kelipatan bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari KPK dari dua bilangan kecil adalah standar kompetensi dasar kelas 7. |

Run 3 — solusi: Menentukan KPK dari 4 dan 6. Kelipatan 4: 4, 8, 12, 16... Kelipatan 6: 6, 12, 18... KPK(4, 6) = 12.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa masalah ini menuntut pencarian kelipatan persekutuan terkecil (KPK) dari dua bilangan yang diberikan untuk menentukan waktu pertemuan berikutnya.. Bukti: membagikan makanan setiap 4 hari; membagikan makanan setiap 6 hari; tentukan setiap berapa hari mereka membagikan makanan secara bersama-sama kembali
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang konsep kelipatan dan bagaimana menerapkannya dalam konteks masalah kehidupan sehari-hari.. Bukti: setiap 4 hari; setiap 6 hari; bersama-sama kembali
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin yang sering ditemui dalam kurikulum kelas 7 terkait KPK. Prosedur penyelesaiannya langsung dan familiar.. Bukti: setiap 4 hari; setiap 6 hari; bersama-sama kembali

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang kelipatan bilangan dan konsep KPK. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah KPK dua bilangan adalah standar kompetensi kelas 7 yang bersifat rutin dan prosedural. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Faktor Bilangan Bulat
Tipe soal: multiple_choice
Stimulus: -
Soal: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari. Jika pada hari ini mereka membagikan makanan bersama-sama, tentukan setiap berapa hari mereka membagikan makanan secara bersama-sama kembali?
Pilihan: A. setiap 12 hari
B. setiap 10 hari
C. setiap 24 hari
D. setiap 2 hari
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `91cfdc7e234e38ad8f34ec21`

Tentukan KPK dan FPB dari bilangan-bilangan berikut dengan menggunakan cara faktorisasi prima dan cara pembagian berulang.<br><br>d. 7, 18, 33

| Opsi | Isi |
|---|---|
| A | KPK = 4.158, FPB = 1 |
| B | KPK = 1.386, FPB = 3 |
| C | KPK = 462, FPB = 1 |
| D | KPK = 1.386, FPB = 1 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Faktorisasi prima: 7 = 7, 18 = 2 x 3^2, 33 = 3 x 11. FPB adalah faktor persekutuan terbesar yang membagi ketiganya, karena tidak ada faktor prima yang sama untuk ketiganya, FPB = 1. KPK adalah hasil kali semua faktor prima dengan pangkat tertinggi: 2 x 3^2 x 7 x 11 = 2 x 9 x 7 x 11 = 1.274? Tidak, 2 x 9 = 18, 18 x 7 = 126, 126 x 11 = 1.386.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b9e3b1d60b9c85b69aca32c8c6896945062cd34813bb7abca12d34581ba8875f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 1881 |
| 2 | success | valid / verified | applying | procedural | Medium | 1826 |
| 3 | success | valid / verified | applying | procedural | Medium | 1879 |

Run 1 — solusi: Faktorisasi prima: 7 = 7, 18 = 2 x 3^2, 33 = 3 x 11. FPB adalah faktor persekutuan terbesar yang membagi ketiganya, karena tidak ada faktor prima yang sama untuk ketiganya, FPB = 1. KPK adalah hasil kali semua faktor prima dengan pangkat tertinggi: 2 x 3^2 x 7 x 11 = 2 x 9 x 7 x 11 = 1.274? Tidak, 2 x 9 = 18, 18 x 7 = 126, 126 x 11 = 1.386.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar faktorisasi prima untuk menentukan KPK dan FPB dari tiga bilangan. Ini adalah penerapan algoritma rutin.. Bukti: Tentukan KPK dan FPB dari bilangan-bilangan berikut dengan menggunakan cara faktorisasi prima
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman dan penerapan algoritma faktorisasi prima untuk mencari KPK dan FPB.. Bukti: menggunakan cara faktorisasi prima dan cara pembagian berulang
- Intended difficulty `classify/Medium`: Soal ini melibatkan tiga bilangan dengan faktorisasi yang cukup sederhana (7 prima, 18=2x3^2, 33=3x11). Siswa hanya perlu melakukan faktorisasi dan menerapkan aturan KPK/FPB standar. Tidak ada jebakan kompleks.. Bukti: 7, 18, 33

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman faktorisasi prima dan konsep dasar KPK/FPB. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari KPK/FPB dari tiga bilangan adalah standar kurikulum kelas 7. Beban perhitungan moderat karena melibatkan perkalian bilangan dua digit. |

Run 2 — solusi: Faktorisasi prima: 7 = 7, 18 = 2 x 3^2, 33 = 3 x 11. FPB (faktor persekutuan terbesar) adalah 1 karena tidak ada faktor prima yang sama untuk ketiga bilangan. KPK (kelipatan persekutuan terkecil) adalah 2 x 3^2 x 7 x 11 = 2 x 9 x 7 x 11 = 1.286.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar faktorisasi prima untuk menentukan KPK dan FPB dari tiga bilangan, yang merupakan tugas rutin dalam kurikulum kelas 7.. Bukti: Tentukan KPK dan FPB dari bilangan-bilangan berikut dengan menggunakan cara faktorisasi prima
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman dan penerapan algoritma faktorisasi prima untuk mencari KPK dan FPB.. Bukti: menggunakan cara faktorisasi prima dan cara pembagian berulang
- Intended difficulty `classify/Medium`: Soal ini melibatkan tiga bilangan dengan faktorisasi yang relatif sederhana. Siswa hanya perlu melakukan faktorisasi prima dan menerapkan aturan KPK/FPB secara rutin tanpa strategi non-rutin.. Bukti: 7, 18, 33

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman faktorisasi prima dan definisi KPK/FPB. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Meskipun prosedural, melibatkan tiga bilangan dengan faktorisasi yang berbeda (satu prima, satu kuadrat, satu komposit) sedikit lebih kompleks daripada dua bilangan, namun tetap sesuai untuk kelas 7. |

Run 3 — solusi: Faktorisasi prima: 7 = 7, 18 = 2 x 3^2, 33 = 3 x 11. FPB adalah faktor persekutuan terbesar yang membagi ketiganya, karena tidak ada faktor prima yang sama untuk ketiganya, FPB = 1. KPK adalah kelipatan persekutuan terkecil, diambil dari semua faktor prima dengan pangkat tertinggi: 2 x 3^2 x 7 x 11 = 2 x 9 x 7 x 11 = 1.386.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar (faktorisasi prima) untuk menentukan KPK dan FPB dari tiga bilangan. Ini adalah tugas rutin yang memerlukan penerapan algoritma yang sudah dipelajari.. Bukti: Tentukan KPK dan FPB dari bilangan-bilangan berikut dengan menggunakan cara faktorisasi prima
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa tentang algoritma faktorisasi prima dan aturan penentuan KPK/FPB, yang merupakan pengetahuan prosedural.. Bukti: menggunakan cara faktorisasi prima dan cara pembagian berulang
- Intended difficulty `classify/Medium`: Soal ini melibatkan tiga bilangan dengan faktorisasi yang cukup sederhana (7 prima, 18=2x3^2, 33=3x11). Prosedurnya rutin dan langkah-langkahnya jelas, sehingga masuk kategori Medium karena melibatkan tiga bilangan sekaligus yang memerlukan ketelitian dalam mengidentifikasi faktor prima.. Bukti: 7, 18, 33

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep bilangan prima, faktorisasi prima, dan definisi KPK/FPB. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena KPK/FPB tiga bilangan adalah standar kurikulum, namun memerlukan ketelitian lebih dibanding dua bilangan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Menentukan KPK dan FPB dengan Menggunakan Faktor Prima
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan KPK dan FPB dari bilangan-bilangan berikut dengan menggunakan cara faktorisasi prima dan cara pembagian berulang.

d. 7, 18, 33
Pilihan: A. KPK = 4.158, FPB = 1
B. KPK = 1.386, FPB = 3
C. KPK = 462, FPB = 1
D. KPK = 1.386, FPB = 1
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `96994f5adee1bd93453d2335`

Ibu akan membeli seragam sekolah seharga Rp450.000,00. Ternyata Ibu hanya mempunyai uang 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan. Berapakah kurangnya uang ibu?

| Opsi | Isi |
|---|---|
| A | Rp7.000,00 |
| B | Rp43.000,00 |
| C | Rp47.000,00 |
| D | Rp10.000,00 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Total uang Ibu = (4 x 100.000) + (4 x 10.000) + (3 x 1.000) = 400.000 + 40.000 + 3.000 = 443.000. Kekurangan uang = 450.000 - 443.000 = 7.000.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f14525152b177ab6702b41706fee6855aebe326d9e9cb53d65a16363dcbe54fd`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1957 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1927 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1997 |

Run 1 — solusi: Total uang Ibu = (4 x 100.000) + (4 x 10.000) + (3 x 1.000) = 400.000 + 40.000 + 3.000 = 443.000. Kekurangan uang = 450.000 - 443.000 = 7.000.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi nilai nominal uang, melakukan operasi perkalian dasar untuk menentukan total uang, dan melakukan pengurangan untuk mencari selisih. Ini adalah penerapan prosedur aritmatika dasar pada situasi rutin.. Bukti: Ibu akan membeli seragam sekolah seharga Rp450.000,00; Ibu hanya mempunyai uang 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang nilai tempat dan dekomposisi bilangan (komposisi nilai uang), yang merupakan pengetahuan konseptual tentang sistem bilangan.. Bukti: 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan
- Intended difficulty `classify/Easy`: Soal ini melibatkan operasi aritmatika dasar (perkalian dan pengurangan) yang rutin bagi siswa kelas 7. Beban kognitif rendah karena langkah-langkahnya jelas dan langsung.. Bukti: 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan; Berapakah kurangnya uang ibu?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi hitung bilangan cacah (penjumlahan, pengurangan, perkalian). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sesuai untuk kelas 7 sebagai penguatan konsep nilai tempat dan operasi aritmatika dasar dalam konteks kehidupan sehari-hari. |

Run 2 — solusi: Total uang Ibu = (4 x 100.000) + (4 x 10.000) + (3 x 1.000) = 400.000 + 40.000 + 3.000 = 443.000. Kekurangan uang = 450.000 - 443.000 = 7.000.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi nilai nominal uang, melakukan operasi perkalian dasar untuk menentukan total uang, dan melakukan pengurangan untuk mencari selisih. Ini adalah penerapan prosedur rutin.. Bukti: Ibu akan membeli seragam sekolah seharga Rp450.000,00; Ibu hanya mempunyai uang 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang nilai tempat dan komposisi bilangan (dekomposisi nilai uang), yang merupakan pengetahuan konseptual.. Bukti: 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan
- Intended difficulty `classify/Easy`: Soal ini melibatkan operasi aritmatika dasar yang familiar dan rutin. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan; Berapakah kurangnya uang ibu?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dan pengurangan bilangan cacah, pemahaman nilai tempat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sesuai untuk kelas 7 sebagai penguatan konsep bilangan dan operasi dasar dalam konteks kehidupan sehari-hari. |

Run 3 — solusi: Total uang Ibu = (4 x 100.000) + (4 x 10.000) + (3 x 1.000) = 400.000 + 40.000 + 3.000 = 443.000. Kekurangan uang = 450.000 - 443.000 = 7.000.
- Domain kognitif `classify/applying`: Siswa perlu melakukan operasi aritmatika dasar (perkalian dan penjumlahan) untuk menentukan total nilai uang, kemudian melakukan pengurangan untuk mencari selisih. Ini adalah penerapan prosedur rutin.. Bukti: Ibu hanya mempunyai uang 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan; Berapakah kurangnya uang ibu?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang nilai tempat dan komposisi bilangan (dekomposisi nilai uang), yang merupakan konsep dasar dalam sistem bilangan.. Bukti: 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan
- Intended difficulty `classify/Easy`: Soal ini melibatkan langkah-langkah rutin (perkalian nilai nominal dan pengurangan) yang familiar bagi siswa kelas 7. Tidak ada strategi nonrutin atau kendala kompleks.. Bukti: Ibu akan membeli seragam sekolah seharga Rp450.000,00; 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi hitung dasar (penjumlahan, pengurangan, perkalian) dan pemahaman nilai tempat bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sesuai dengan tingkat kelas 7 karena melibatkan operasi aritmatika pada bilangan besar yang masih dalam jangkauan kemampuan dasar siswa. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Komposisi dan Dekomposisi Bilangan Sampai 1.000.000
Tipe soal: multiple_choice
Stimulus: -
Soal: Ibu akan membeli seragam sekolah seharga Rp450.000,00. Ternyata Ibu hanya mempunyai uang 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan. Berapakah kurangnya uang ibu?
Pilihan: A. Rp7.000,00
B. Rp43.000,00
C. Rp47.000,00
D. Rp10.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 9. Soal `87544cfea887aa9755cb0c38`

Apakah semua bilangan desimal merupakan bilangan rasional? Perhatikan bilangan di bawah ini, ketiganya memiliki angka desimal yang tak terbatas. 1) $\sqrt{2} = 1,414213562...$ 2) $\pi = 3,141592564...$ 3) $e = 2,718281828459...$<br><br>Apakah kalian dapat menyatakan ketiga bilangan di atas dalam pembagian bilangan bulat $\frac{a}{b}$ dengan $b \neq 0$?

| Opsi | Isi |
|---|---|
| A | Ya, karena semua bilangan desimal tak terbatas pasti bisa dinyatakan sebagai pecahan |
| B | Tidak dapat ditentukan tanpa kalkulator |
| C | Tidak, ketiganya bilangan irasional. |
| D | Ya, tetapi hanya untuk $\pi$ |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Bilangan rasional didefinisikan sebagai bilangan yang dapat dinyatakan dalam bentuk a/b (a, b bilangan bulat, b tidak nol). Bilangan desimal tak terbatas yang tidak berulang (seperti akar 2, pi, dan e) tidak dapat dinyatakan sebagai pecahan a/b, sehingga diklasifikasikan sebagai bilangan irasional.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `11208f8743f62beaf0576d129dedf942a96394ec4f80611ac67ae8d83d0ba47c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 1839 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 1926 |
| 3 | success | valid / verified | reasoning | conceptual | Medium | 1840 |

Run 1 — solusi: Bilangan rasional adalah bilangan yang dapat dinyatakan sebagai a/b (a, b bilangan bulat, b tidak nol). Bilangan dengan desimal tak terbatas dan tidak berulang (seperti akar 2, pi, dan e) tidak dapat dinyatakan sebagai pecahan a/b, sehingga disebut bilangan irasional.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk memahami definisi bilangan rasional dan membedakannya dengan bilangan irasional berdasarkan sifat desimalnya, yang merupakan pemahaman konseptual.. Bukti: Apakah semua bilangan desimal merupakan bilangan rasional?; Apakah kalian dapat menyatakan ketiga bilangan di atas dalam pembagian bilangan bulat a/b
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep dasar bilangan rasional vs irasional (struktur bilangan) untuk menjawab pertanyaan ini.. Bukti: Apakah semua bilangan desimal merupakan bilangan rasional?; ketiganya memiliki angka desimal yang tak terbatas
- Intended difficulty `classify/Easy`: Soal ini menguji pemahaman konseptual dasar tentang klasifikasi bilangan. Tidak ada perhitungan kompleks, hanya pengenalan sifat bilangan.. Bukti: Apakah semua bilangan desimal merupakan bilangan rasional?; ketiganya memiliki angka desimal yang tak terbatas

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi bilangan rasional sebagai pecahan a/b. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi bilangan rasional dan irasional adalah bagian dari kurikulum kelas 7. Soal ini bersifat teoretis dan langsung, cocok untuk tingkat kesulitan awal. |

Run 2 — solusi: Bilangan rasional adalah bilangan yang dapat dinyatakan sebagai a/b (a, b bilangan bulat, b tidak nol). Bilangan desimal tak terbatas yang tidak berulang (seperti akar 2, pi, dan e) tidak dapat dinyatakan sebagai pecahan a/b, sehingga disebut bilangan irasional.
- Domain kognitif `classify/reasoning`: Soal ini menuntut pemahaman konseptual tentang definisi bilangan rasional dan irasional, bukan sekadar menghitung. Siswa harus mengidentifikasi sifat desimal tak terbatas yang tidak berulang sebagai ciri bilangan irasional.. Bukti: Apakah semua bilangan desimal merupakan bilangan rasional?; Apakah kalian dapat menyatakan ketiga bilangan di atas dalam pembagian bilangan bulat a/b
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang kategori bilangan (rasional vs irasional) dan prinsip dasar yang mendasari definisi tersebut.. Bukti: Apakah semua bilangan desimal merupakan bilangan rasional?; ketiganya memiliki angka desimal yang tak terbatas
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemahaman konseptual yang mendalam tentang perbedaan antara desimal berulang (rasional) dan tidak berulang (irasional). Meskipun tidak ada perhitungan rumit, siswa harus membedakan konsep yang sering disalahpahami (miskonsepsi bahwa semua desimal tak terbatas adalah rasional).. Bukti: Apakah semua bilangan desimal merupakan bilangan rasional?; ketiganya memiliki angka desimal yang tak terbatas

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bilangan rasional sebagai pecahan a/b. |
| dependentSteps | 2 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi bilangan irasional sering diperkenalkan di kelas 7 sebagai perluasan dari bilangan rasional. Soal ini menantang pemahaman konseptual siswa di tingkat yang sesuai untuk menguji kedalaman pemahaman materi tersebut. |

Run 3 — solusi: Bilangan rasional adalah bilangan yang dapat dinyatakan sebagai a/b (a, b bilangan bulat, b tidak nol). Bilangan desimal tak terbatas yang tidak berulang (seperti akar 2, pi, dan e) tidak dapat dinyatakan sebagai pecahan a/b, sehingga disebut bilangan irasional.
- Domain kognitif `classify/reasoning`: Soal ini menuntut pemahaman konseptual tentang definisi bilangan rasional versus irasional, bukan sekadar menghitung.. Bukti: Apakah semua bilangan desimal merupakan bilangan rasional?; Apakah kalian dapat menyatakan ketiga bilangan di atas dalam pembagian bilangan bulat a/b
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip atau struktur definisi bilangan rasional dan karakteristik bilangan irasional.. Bukti: Apakah semua bilangan desimal merupakan bilangan rasional?; ketiganya memiliki angka desimal yang tak terbatas
- Intended difficulty `classify/Medium`: Soal ini menguji pemahaman konseptual yang mendalam tentang klasifikasi bilangan. Meskipun konsepnya penting, untuk kelas 7, ini adalah pertanyaan teoretis yang menantang miskonsepsi umum.. Bukti: Apakah semua bilangan desimal merupakan bilangan rasional?; ketiganya memiliki angka desimal yang tak terbatas

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi bilangan rasional sebagai pecahan a/b. |
| dependentSteps | 1 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Membedakan rasional dan irasional adalah topik yang menantang di kelas 7 karena sering kali siswa baru mengenal desimal berulang vs tidak berulang. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 1, "reasoning": 2} | majority_2_of_3 / adjudicated | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 1, "Medium": 2} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3423`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `reasoning`: Soal ini menguji pemahaman konseptual tentang definisi bilangan rasional dan irasional. Siswa harus mengenali sifat desimal tak terbatas yang tidak berulang sebagai ciri bilangan irasional, yang merupakan proses penalaran konseptual.
- Dimensi pengetahuan `conceptual`: Siswa perlu memahami hubungan dan struktur konsep antara bilangan rasional dan irasional untuk menjawab pertanyaan ini.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena menuntut siswa untuk membedakan konsep yang sering disalahpahami (miskonsepsi bahwa semua desimal tak terbatas adalah rasional). Meskipun tidak ada perhitungan, siswa harus melakukan justifikasi konseptual terhadap sifat bilangan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi bilangan rasional sebagai pecahan a/b. |
| dependentSteps | 1 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Membedakan rasional dan irasional adalah topik yang menantang di kelas 7 karena siswa sering kali baru mengenal desimal berulang vs tidak berulang. Soal ini menguji kedalaman pemahaman konseptual tersebut. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Di Antara Dua Bilangan Bulat
Tipe soal: multiple_choice
Stimulus: -
Soal: Apakah semua bilangan desimal merupakan bilangan rasional? Perhatikan bilangan di bawah ini, ketiganya memiliki angka desimal yang tak terbatas. 1) $\sqrt{2} = 1,414213562...$ 2) $\pi = 3,141592564...$ 3) $e = 2,718281828459...$

Apakah kalian dapat menyatakan ketiga bilangan di atas dalam pembagian bilangan bulat $\frac{a}{b}$ dengan $b \neq 0$?
Pilihan: A. Ya, karena semua bilangan desimal tak terbatas pasti bisa dinyatakan sebagai pecahan
B. Tidak dapat ditentukan tanpa kalkulator
C. Tidak, ketiganya bilangan irasional.
D. Ya, tetapi hanya untuk $\pi$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "reasoning", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `ece752621e495b9af4328824`

Mengapa pada bilangan rasional yang dinyatakan dalam $\frac{a}{b}$, nilai $b$ tidak boleh nol?

| Opsi | Isi |
|---|---|
| A | Karena $a$ dan $b$ harus memiliki nilai yang sama |
| B | Karena hasil $\frac{a}{b}$ harus berupa bilangan bulat |
| C | Karena pembagian dengan 0 tidak terdefinisi. |
| D | Karena $b$ harus bernilai positif |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Definisi bilangan rasional a/b mensyaratkan b tidak sama dengan 0 karena pembagian dengan nol tidak terdefinisi dalam sistem bilangan real.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b3881788fdb6837626756beadca6ca7c3a50a61538e1fe4ae5bea733b4ee0f02`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 1708 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 1697 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 1708 |

Run 1 — solusi: Definisi bilangan rasional a/b mensyaratkan b tidak sama dengan 0 karena pembagian dengan nol tidak terdefinisi dalam sistem bilangan real.
- Domain kognitif `classify/knowing`: Soal ini menguji pemahaman konseptual dasar tentang definisi bilangan rasional. Siswa perlu mengingat atau memahami prinsip fundamental bahwa pembagian dengan nol tidak terdefinisi.. Bukti: Mengapa pada bilangan rasional yang dinyatakan dalam a/b, nilai b tidak boleh nol?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menanyakan tentang prinsip atau aturan dasar dalam sistem bilangan, yang merupakan bagian dari pengetahuan konseptual.. Bukti: Mengapa pada bilangan rasional yang dinyatakan dalam a/b, nilai b tidak boleh nol?
- Intended difficulty `classify/Easy`: Soal ini bersifat teoritis dan langsung. Siswa yang memahami definisi bilangan rasional akan langsung mengetahui alasannya tanpa perlu melakukan perhitungan atau strategi kompleks.. Bukti: Mengapa pada bilangan rasional yang dinyatakan dalam a/b, nilai b tidak boleh nol?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang operasi pembagian dan definisi bilangan rasional. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pertanyaan ini merupakan konsep dasar yang diajarkan saat memperkenalkan bilangan rasional di kelas 7, sehingga tingkat kesulitannya rendah. |

Run 2 — solusi: Dalam sistem bilangan, pembagian oleh nol tidak terdefinisi karena tidak ada bilangan x yang memenuhi persamaan 0 * x = a (untuk a tidak sama dengan 0).
- Domain kognitif `classify/knowing`: Soal ini menuntut pemahaman konseptual tentang definisi dasar bilangan rasional dan sifat operasi pembagian, bukan sekadar menghitung.. Bukti: Mengapa pada bilangan rasional yang dinyatakan dalam a/b, nilai b tidak boleh nol?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang prinsip atau aturan dasar dalam sistem bilangan (konsep pembagian dengan nol).. Bukti: Mengapa pada bilangan rasional yang dinyatakan dalam a/b, nilai b tidak boleh nol?
- Intended difficulty `classify/Easy`: Soal ini bersifat teoretis dan mendasar. Siswa yang memahami definisi bilangan rasional akan langsung mengenali alasan pembagian dengan nol tidak terdefinisi tanpa perlu langkah perhitungan.. Bukti: Mengapa pada bilangan rasional yang dinyatakan dalam a/b, nilai b tidak boleh nol?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi bilangan rasional dan konsep dasar pembagian. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah konsep fundamental yang diajarkan saat pengenalan bilangan rasional di kelas 7. |

Run 3 — solusi: Dalam sistem bilangan, pembagian dengan nol tidak terdefinisi karena tidak ada bilangan yang jika dikalikan dengan nol menghasilkan pembilang (a) yang bukan nol.
- Domain kognitif `classify/knowing`: Soal ini menguji pemahaman konseptual dasar mengenai definisi bilangan rasional dan sifat operasi pembagian. Siswa perlu memahami prinsip dasar aritmatika bahwa pembagian dengan nol tidak terdefinisi.. Bukti: Mengapa pada bilangan rasional yang dinyatakan dalam a/b, nilai b tidak boleh nol?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menanyakan tentang prinsip atau aturan dasar (definisi) dalam sistem bilangan rasional, yang termasuk dalam kategori pengetahuan konseptual.. Bukti: Mengapa pada bilangan rasional yang dinyatakan dalam a/b, nilai b tidak boleh nol?
- Intended difficulty `classify/Easy`: Soal ini bersifat teoretis dan langsung menguji pemahaman definisi dasar yang diajarkan di awal materi bilangan rasional. Tidak ada perhitungan kompleks atau strategi nonrutin yang diperlukan.. Bukti: Mengapa pada bilangan rasional yang dinyatakan dalam a/b, nilai b tidak boleh nol?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang operasi pembagian dan definisi bilangan rasional. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah konsep fundamental yang diperkenalkan saat siswa mempelajari pecahan dan bilangan rasional di kelas 7. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Di Antara Dua Bilangan Bulat
Tipe soal: multiple_choice
Stimulus: -
Soal: Mengapa pada bilangan rasional yang dinyatakan dalam $\frac{a}{b}$, nilai $b$ tidak boleh nol?
Pilihan: A. Karena $a$ dan $b$ harus memiliki nilai yang sama
B. Karena hasil $\frac{a}{b}$ harus berupa bilangan bulat
C. Karena pembagian dengan 0 tidak terdefinisi.
D. Karena $b$ harus bernilai positif
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `5b357152cae4f299c0724397`

Paman menguji coba tiga jenis pakan ayam di peternakan ayam potong miliknya. Tiga ayam diberi jenis pakan berbeda dan ditimbang beratnya setiap minggu. Tabel di bawah ini menunjukkan hasil penimbangan berat ayam.<br><br>**Tabel 2.10** Berat Ayam<br><br>\|Pakan\|Saat menetas\|Minggu 1\|Minggu 2\|Minggu 3\|Minggu 4\|<br>\|---\|---\|---\|---\|---\|---\|<br>\|A\|42,9\|152,6\|367,9\|732,7\|1.043,5\|<br>\|B\|41,5\|120,8\|338,1\|733,4\|1.112,8\|<br>\|C\|48,3\|155,4\|403,6\|824,0\|1.294,2\|<br>(berat dalam gram)<br><br>Ayam yang diberi pakan apa yang memiliki penambahan berat tertinggi pada minggu pertama?

| Opsi | Isi |
|---|---|
| A | Pakan A dan C penambahannya sama besar |
| B | Pakan C |
| C | Pakan A |
| D | Pakan B |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Hitung selisih berat Minggu 1 dengan saat menetas untuk setiap pakan: Pakan A = 152,6 - 42,9 = 109,7; Pakan B = 120,8 - 41,5 = 79,3; Pakan C = 155,4 - 48,3 = 107,1. Nilai tertinggi adalah 109,7 (Pakan A).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `818a73ef125f6a202244b9610d30dd6e0acb1a58aa3eda9209f4ef7e3c702e0d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2025 |
| 2 | success | valid / verified | applying | procedural | Medium | 2009 |
| 3 | success | valid / verified | applying | procedural | Medium | 2040 |

Run 1 — solusi: Hitung selisih berat Minggu 1 dengan saat menetas untuk setiap pakan: Pakan A = 152,6 - 42,9 = 109,7; Pakan B = 120,8 - 41,5 = 79,3; Pakan C = 155,4 - 48,3 = 107,1. Nilai tertinggi adalah 109,7 (Pakan A).
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur (pengurangan) dan menerapkannya pada data yang diberikan untuk membandingkan hasil selisih.. Bukti: Ayam yang diberi pakan apa yang memiliki penambahan berat tertinggi pada minggu pertama?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur aritmetika dasar (pengurangan bilangan desimal) untuk memecahkan masalah yang terstruktur dalam tabel.. Bukti: Tabel 2.10 Berat Ayam
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah rutin (tiga pengurangan) dan perbandingan hasil. Ini adalah tugas rutin yang sesuai untuk kelas 7.. Bukti: Tabel 2.10 Berat Ayam; Ayam yang diberi pakan apa yang memiliki penambahan berat tertinggi pada minggu pertama?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pengurangan bilangan desimal. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu membaca tabel dan melakukan operasi pengurangan desimal untuk membandingkan nilai. |

Run 2 — solusi: Hitung selisih berat Minggu 1 dengan saat menetas untuk setiap pakan: Pakan A = 152,6 - 42,9 = 109,7; Pakan B = 120,8 - 41,5 = 79,3; Pakan C = 155,4 - 48,3 = 107,1. Nilai tertinggi adalah 109,7 (Pakan A).
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur (pengurangan bilangan desimal) dan menerapkannya pada data yang diberikan untuk membandingkan hasil.. Bukti: Ayam yang diberi pakan apa yang memiliki penambahan berat tertinggi pada minggu pertama?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur aritmetika dasar (pengurangan) untuk memproses data yang disajikan dalam tabel.. Bukti: Tabel 2.10 Berat Ayam
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah rutin (tiga operasi pengurangan) dan perbandingan hasil. Beban kognitif moderat karena melibatkan bilangan desimal.. Bukti: Tabel 2.10 Berat Ayam; Ayam yang diberi pakan apa yang memiliki penambahan berat tertinggi pada minggu pertama?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pengurangan bilangan desimal dan perbandingan bilangan rasional. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena melibatkan operasi dasar pada data tabel yang memerlukan ketelitian dalam pengurangan desimal. |

Run 3 — solusi: Hitung selisih berat Minggu 1 dengan saat menetas untuk setiap pakan: Pakan A = 152,6 - 42,9 = 109,7; Pakan B = 120,8 - 41,5 = 79,3; Pakan C = 155,4 - 48,3 = 107,1. Nilai tertinggi adalah 109,7 (Pakan A).
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur (pengurangan bilangan desimal) dan menerapkannya pada data tabel untuk membandingkan hasil selisih.. Bukti: Ayam yang diberi pakan apa yang memiliki penambahan berat tertinggi pada minggu pertama?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur aritmatika (pengurangan) pada data yang disajikan dalam tabel untuk mendapatkan informasi baru (penambahan berat).. Bukti: Tabel 2.10 Berat Ayam
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah perhitungan rutin (tiga pengurangan) dan perbandingan hasil. Ini adalah tugas standar untuk kelas 7.. Bukti: Tabel 2.10 Berat Ayam; Ayam yang diberi pakan apa yang memiliki penambahan berat tertinggi pada minggu pertama?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pengurangan bilangan desimal. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu melakukan operasi aritmatika pada bilangan desimal dan membaca tabel data untuk memecahkan masalah perbandingan sederhana. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Membandingkan Bilangan Rasional
Tipe soal: multiple_choice
Stimulus: -
Soal: Paman menguji coba tiga jenis pakan ayam di peternakan ayam potong miliknya. Tiga ayam diberi jenis pakan berbeda dan ditimbang beratnya setiap minggu. Tabel di bawah ini menunjukkan hasil penimbangan berat ayam.

**Tabel 2.10** Berat Ayam

|Pakan|Saat menetas|Minggu 1|Minggu 2|Minggu 3|Minggu 4|
|---|---|---|---|---|---|
|A|42,9|152,6|367,9|732,7|1.043,5|
|B|41,5|120,8|338,1|733,4|1.112,8|
|C|48,3|155,4|403,6|824,0|1.294,2|
(berat dalam gram)

Ayam yang diberi pakan apa yang memiliki penambahan berat tertinggi pada minggu pertama?
Pilihan: A. Pakan A dan C penambahannya sama besar
B. Pakan C
C. Pakan A
D. Pakan B
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 12. Soal `4991a6a099440013209809b5`

Paman menguji coba tiga jenis pakan ayam di peternakan ayam potong miliknya. Tiga ayam diberi jenis pakan berbeda dan ditimbang beratnya setiap minggu. Tabel di bawah ini menunjukkan hasil penimbangan berat ayam.<br><br>**Tabel 2.10** Berat Ayam<br><br>\|Pakan\|Saat menetas\|Minggu 1\|Minggu 2\|Minggu 3\|Minggu 4\|<br>\|---\|---\|---\|---\|---\|---\|<br>\|A\|42,9\|152,6\|367,9\|732,7\|1.043,5\|<br>\|B\|41,5\|120,8\|338,1\|733,4\|1.112,8\|<br>\|C\|48,3\|155,4\|403,6\|824,0\|1.294,2\|<br>(berat dalam gram)<br><br>Ayam yang diberi pakan apa yang memiliki berat tertinggi pada minggu pertama?

| Opsi | Isi |
|---|---|
| A | Pakan A |
| B | Pakan B |
| C | Pakan C |
| D | Semua pakan sama beratnya pada minggu pertama |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Bandingkan nilai pada kolom 'Minggu 1': Pakan A (152,6), Pakan B (120,8), dan Pakan C (155,4). Nilai tertinggi adalah 155,4, yang sesuai dengan Pakan C.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `706e4a9b824127d85e30c0dbc86de9ea5edd4116719b0094a34a4fa477a39046`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 1871 |
| 2 | success | valid / verified | knowing | factual | Easy | 1872 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 1885 |

Run 1 — solusi: Bandingkan nilai pada kolom 'Minggu 1' untuk setiap baris pakan: Pakan A (152,6), Pakan B (120,8), dan Pakan C (155,4). Nilai tertinggi adalah 155,4 yang merupakan milik Pakan C.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data dari tabel dan membandingkan tiga bilangan desimal untuk menentukan nilai terbesar.. Bukti: Ayam yang diberi pakan apa yang memiliki berat tertinggi pada minggu pertama?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang cara membaca tabel dan membandingkan nilai bilangan desimal.. Bukti: Tabel 2.10 Berat Ayam
- Intended difficulty `classify/Easy`: Tugas ini sangat langsung, hanya melibatkan ekstraksi data dari tabel dan perbandingan sederhana tanpa langkah tambahan.. Bukti: Ayam yang diberi pakan apa yang memiliki berat tertinggi pada minggu pertama?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca tabel dan membandingkan bilangan desimal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena melibatkan pembacaan data sederhana yang merupakan keterampilan dasar dalam topik bilangan rasional. |

Run 2 — solusi: Bandingkan nilai desimal pada kolom 'Minggu 1': Pakan A = 152,6; Pakan B = 120,8; Pakan C = 155,4. Nilai terbesar adalah 155,4 (Pakan C).
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data dari tabel dan melakukan perbandingan langsung antar bilangan desimal.. Bukti: Ayam yang diberi pakan apa yang memiliki berat tertinggi pada minggu pertama?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual mengenai cara membaca tabel dan membandingkan nilai bilangan desimal.. Bukti: Tabel 2.10 Berat Ayam
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung, hanya memerlukan pembacaan data dan perbandingan sederhana tanpa langkah tambahan atau manipulasi.. Bukti: Ayam yang diberi pakan apa yang memiliki berat tertinggi pada minggu pertama?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca tabel dan membandingkan bilangan desimal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena hanya melibatkan perbandingan bilangan desimal sederhana dalam konteks tabel yang umum. |

Run 3 — solusi: Bandingkan nilai desimal pada kolom 'Minggu 1' untuk setiap pakan: Pakan A = 152,6; Pakan B = 120,8; Pakan C = 155,4. Nilai terbesar adalah 155,4 yang merupakan milik Pakan C.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk membaca data dari tabel dan melakukan perbandingan langsung antara tiga bilangan desimal untuk menentukan nilai terbesar.. Bukti: Ayam yang diberi pakan apa yang memiliki berat tertinggi pada minggu pertama?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami cara membaca dan menginterpretasikan data yang disajikan dalam bentuk tabel untuk membandingkan nilai bilangan rasional (desimal).. Bukti: Tabel di bawah ini menunjukkan hasil penimbangan berat ayam.
- Intended difficulty `classify/Easy`: Tugas ini bersifat langsung, hanya memerlukan pembacaan tabel dan perbandingan nilai desimal sederhana tanpa langkah tambahan yang kompleks.. Bukti: Ayam yang diberi pakan apa yang memiliki berat tertinggi pada minggu pertama?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca tabel dan membandingkan bilangan desimal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena melibatkan perbandingan bilangan desimal yang merupakan materi dasar, dengan beban kognitif yang rendah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3151`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu melakukan ekstraksi data dari tabel dan membandingkan tiga bilangan desimal secara langsung untuk menentukan nilai terbesar.
- Dimensi pengetahuan `factual`: Soal ini menguji pemahaman faktual tentang cara membaca tabel dan membandingkan nilai bilangan desimal.
- Intended difficulty `Easy`: Tugas ini sangat langsung, hanya melibatkan ekstraksi data dari tabel dan perbandingan sederhana tanpa langkah tambahan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca tabel dan membandingkan bilangan desimal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena melibatkan pembacaan data sederhana yang merupakan keterampilan dasar dalam topik bilangan rasional. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Membandingkan Bilangan Rasional
Tipe soal: multiple_choice
Stimulus: -
Soal: Paman menguji coba tiga jenis pakan ayam di peternakan ayam potong miliknya. Tiga ayam diberi jenis pakan berbeda dan ditimbang beratnya setiap minggu. Tabel di bawah ini menunjukkan hasil penimbangan berat ayam.

**Tabel 2.10** Berat Ayam

|Pakan|Saat menetas|Minggu 1|Minggu 2|Minggu 3|Minggu 4|
|---|---|---|---|---|---|
|A|42,9|152,6|367,9|732,7|1.043,5|
|B|41,5|120,8|338,1|733,4|1.112,8|
|C|48,3|155,4|403,6|824,0|1.294,2|
(berat dalam gram)

Ayam yang diberi pakan apa yang memiliki berat tertinggi pada minggu pertama?
Pilihan: A. Pakan A
B. Pakan B
C. Pakan C
D. Semua pakan sama beratnya pada minggu pertama
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "factual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 13. Soal `ac7f560c796164a475dad657`

Indeks Massa Tubuh $= \dfrac{BB}{TB^2}$. BB: Berat badan (kg), TB: Tinggi badan (m).<br><br>**Tabel 2.12** Kategori Indeks Massa Tubuh<br><br>\|Kategori\|IMT\|<br>\|---\|---\|<br>\|Kekurangan berat badan tingkat berat\|Kurang dari 17,0\|<br>\|Kekurangan berat badan tingkat ringan\|17,0 sampai 18,4\|<br>\|Normal\|18,5 sampai 25,0\|<br>\|Kelebihan berat badan tingkat ringan\|25,1 sampai 27,0\|<br>\|Kelebihan berat badan tingkat berat\|Lebih dari 27,0\|<br><br>**Tabel 2.13** Data Berat dan Tinggi Badan<br><br>\|No\|Nama\|Berat Badan (kg)\|Tinggi Badan (m)\|<br>\|---\|---\|---\|---\|<br>\|1\|Pak Ananta\|80\|1,80\|<br>\|2\|Pak Bintoro\|50\|1,70\|<br>\|3\|Bu Citra\|65\|1,68\|<br>\|4\|Bu Dian\|60\|1,60\|<br>\|5\|Pak Erlangga\|75\|1,65\|<br><br>Pada Tabel 2.13, siapa yang memiliki IMT dengan kategori kekurangan berat badan tingkat ringan? Berapa berat badan yang harus ditambah agar tercapai IMT sebesar 18,5?

| Opsi | Isi |
|---|---|
| A | Pak Bintoro, perlu menambah 6,9375 kg |
| B | Pak Bintoro, perlu menambah 3,465 kg |
| C | Pak Bintoro, perlu menambah 1,5 kg |
| D | Pak Ananta, perlu menambah 3,465 kg |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: IMT Pak Bintoro = 50 / (1,7^2) = 50 / 2,89 ≈ 17,30 (masuk kategori 17,0-18,4). Target berat untuk IMT 18,5 = 18,5 * 2,89 = 53,465 kg. Tambahan berat = 53,465 - 50 = 3,465 kg.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3e2480e3e340dd51da678f74040856efd6833795059e03e3777ca123c1ffe4b4`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2228 |
| 2 | success | valid / verified | applying | procedural | Medium | 2233 |
| 3 | success | valid / verified | applying | procedural | Medium | 2259 |

Run 1 — solusi: IMT Pak Bintoro = 50 / (1,7^2) = 50 / 2,89 ≈ 17,30 (masuk kategori 17,0-18,4). Target berat untuk IMT 18,5 = 18,5 * 2,89 = 53,465 kg. Tambahan berat = 53,465 - 50 = 3,465 kg.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus IMT yang diberikan untuk menguji data, lalu melakukan operasi aljabar (substitusi dan pemecahan persamaan) untuk mencari selisih berat badan.. Bukti: siapa yang memiliki IMT dengan kategori kekurangan berat badan tingkat ringan?; Berapa berat badan yang harus ditambah agar tercapai IMT sebesar 18,5?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur perhitungan aritmatika yang terstruktur berdasarkan rumus yang diberikan dan kategori yang sudah didefinisikan.. Bukti: Indeks Massa Tubuh = BB / TB^2; 17,0 sampai 18,4
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah rutin: menghitung IMT untuk beberapa individu, membandingkan dengan tabel kategori, dan menyelesaikan persamaan linear sederhana untuk mencari selisih berat badan.. Bukti: Indeks Massa Tubuh = BB / TB^2; Tabel 2.13 Data Berat dan Tinggi Badan; Berapa berat badan yang harus ditambah agar tercapai IMT sebesar 18,5?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi hitung bilangan desimal dan pemahaman rumus aljabar sederhana. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah mempelajari operasi bilangan rasional dan substitusi nilai ke dalam rumus. Soal ini menuntut ketelitian dalam perhitungan desimal dan pemahaman konteks tabel. |

Run 2 — solusi: 1. Hitung IMT Pak Bintoro: 50 / (1,70^2) = 50 / 2,89 = 17,30 (Kategori: kekurangan berat badan tingkat ringan). 2. Hitung target berat badan untuk IMT 18,5: 18,5 * (1,70^2) = 18,5 * 2,89 = 53,465 kg. 3. Hitung selisih berat: 53,465 - 50 = 3,465 kg.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus yang diberikan, melakukan operasi aritmetika pada bilangan desimal, dan membandingkan hasil dengan rentang kategori yang diberikan.. Bukti: Indeks Massa Tubuh = BB / TB^2; siapa yang memiliki IMT dengan kategori kekurangan berat badan tingkat ringan? Berapa berat badan yang harus ditambah agar tercapai IMT sebesar 18,5?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur perhitungan (algoritma) berdasarkan rumus yang diberikan dan mengaitkannya dengan kategori yang telah didefinisikan.. Bukti: Indeks Massa Tubuh = BB / TB^2; Tabel 2.12 Kategori Indeks Massa Tubuh
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah rutin: menghitung IMT, mengidentifikasi kategori, menghitung target berat badan, dan mencari selisih. Operasi melibatkan bilangan desimal yang memerlukan ketelitian.. Bukti: Indeks Massa Tubuh = BB / TB^2; Tabel 2.12; Tabel 2.13

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi hitung bilangan desimal (perkalian dan pembagian), pemahaman rumus substitusi. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena melibatkan operasi bilangan rasional (desimal) dalam konteks nyata, namun prosedurnya bersifat rutin dan terstruktur. |

Run 3 — solusi: IMT Pak Bintoro = 50 / (1,7^2) = 50 / 2,89 ≈ 17,30 (Kategori: kekurangan berat badan tingkat ringan). Target berat untuk IMT 18,5 = 18,5 * (1,7^2) = 18,5 * 2,89 = 53,465 kg. Tambahan berat = 53,465 - 50 = 3,465 kg.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus yang diberikan, melakukan perhitungan aritmetika dengan bilangan desimal, dan memecahkan masalah dua langkah (menghitung IMT saat ini lalu menghitung selisih berat badan untuk target IMT).. Bukti: Indeks Massa Tubuh = BB / TB^2; siapa yang memiliki IMT dengan kategori kekurangan berat badan tingkat ringan? Berapa berat badan yang harus ditambah agar tercapai IMT sebesar 18,5?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur perhitungan (algoritma) berdasarkan rumus yang diberikan dan mengaitkannya dengan kategori yang tersedia dalam tabel.. Bukti: Indeks Massa Tubuh = BB / TB^2; Tabel 2.12 Kategori Indeks Massa Tubuh
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah rutin: menghitung IMT untuk kandidat, mencocokkan dengan kategori, dan menghitung berat badan target menggunakan aljabar sederhana (substitusi). Beban perhitungan desimal moderat.. Bukti: Indeks Massa Tubuh = BB / TB^2; Tabel 2.12; Tabel 2.13

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi hitung bilangan desimal (perkalian dan pembagian), pemahaman rumus/substitusi variabel. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena melibatkan operasi bilangan rasional (desimal) dalam konteks nyata, namun prosedurnya bersifat rutin dan terstruktur. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Operasi Hitung Bilangan Rasional
Tipe soal: multiple_choice
Stimulus: -
Soal: Indeks Massa Tubuh $= \dfrac{BB}{TB^2}$. BB: Berat badan (kg), TB: Tinggi badan (m).

**Tabel 2.12** Kategori Indeks Massa Tubuh

|Kategori|IMT|
|---|---|
|Kekurangan berat badan tingkat berat|Kurang dari 17,0|
|Kekurangan berat badan tingkat ringan|17,0 sampai 18,4|
|Normal|18,5 sampai 25,0|
|Kelebihan berat badan tingkat ringan|25,1 sampai 27,0|
|Kelebihan berat badan tingkat berat|Lebih dari 27,0|

**Tabel 2.13** Data Berat dan Tinggi Badan

|No|Nama|Berat Badan (kg)|Tinggi Badan (m)|
|---|---|---|---|
|1|Pak Ananta|80|1,80|
|2|Pak Bintoro|50|1,70|
|3|Bu Citra|65|1,68|
|4|Bu Dian|60|1,60|
|5|Pak Erlangga|75|1,65|

Pada Tabel 2.13, siapa yang memiliki IMT dengan kategori kekurangan berat badan tingkat ringan? Berapa berat badan yang harus ditambah agar tercapai IMT sebesar 18,5?
Pilihan: A. Pak Bintoro, perlu menambah 6,9375 kg
B. Pak Bintoro, perlu menambah 3,465 kg
C. Pak Bintoro, perlu menambah 1,5 kg
D. Pak Ananta, perlu menambah 3,465 kg
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `10a138463875f0dd92b0b221`

Ibu memiliki kain sepanjang 20 meter. Ibu ingin memotong-motong kain tersebut dengan panjang tiap potongan 1,25 m. Berapa banyak potongan kain yang ibu dapat?

| Opsi | Isi |
|---|---|
| A | 16 potongan |
| B | 20 potongan |
| C | 15 potongan |
| D | 25 potongan |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Jumlah potongan = Total panjang kain / Panjang tiap potongan = 20 / 1,25 = 16.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c7adbc908507db97d9cbc023359f7587f7fb20aef293d9a55f21d7178fa767e8`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1647 |
| 2 | success | valid / verified | applying | procedural | Easy | 1677 |
| 3 | success | valid / verified | applying | procedural | Easy | 1719 |

Run 1 — solusi: Jumlah potongan = Total panjang kain / Panjang tiap potongan = 20 / 1,25 = 16.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan operasi pembagian bilangan desimal pada situasi rutin yang sudah familiar.. Bukti: Ibu memiliki kain sepanjang 20 meter. Ibu ingin memotong-motong kain tersebut dengan panjang tiap potongan 1,25 m.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman dan penerapan algoritma pembagian bilangan desimal.. Bukti: 20 : 1,25 = 16
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur rutin satu langkah dengan angka yang sederhana, cocok untuk tingkat kelas 7.. Bukti: 20 meter; 1,25 m

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pembagian bilangan desimal atau pecahan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pembagian bilangan desimal adalah materi dasar kelas 7. Soal ini tidak memiliki jebakan kompleks atau langkah ganda yang rumit. |

Run 2 — solusi: Banyak potongan = 20 / 1,25 = 20 / (125/100) = 20 / (5/4) = 20 * (4/5) = 16.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan operasi pembagian bilangan desimal dalam konteks masalah sehari-hari yang rutin.. Bukti: Ibu memiliki kain sepanjang 20 meter. Ibu ingin memotong-motong kain tersebut dengan panjang tiap potongan 1,25 m.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pembagian bilangan desimal (prosedural).. Bukti: 20 : 1,25
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin satu langkah yang menggunakan representasi desimal standar, dengan beban kalkulasi yang rendah.. Bukti: 20 meter; 1,25 m

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pembagian bilangan desimal atau pecahan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pembagian bilangan desimal adalah materi dasar kelas 7 yang rutin dan langsung. |

Run 3 — solusi: Banyak potongan = 20 / 1,25 = 20 / (125/100) = 20 / (5/4) = 20 * (4/5) = 16.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi operasi pembagian yang tepat untuk menyelesaikan masalah pembagian bilangan desimal dalam konteks sehari-hari.. Bukti: Ibu memiliki kain sepanjang 20 meter. Ibu ingin memotong-motong kain tersebut dengan panjang tiap potongan 1,25 m.
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penerapan algoritma pembagian bilangan desimal (prosedural) untuk mendapatkan hasil yang akurat.. Bukti: 20 : 1,25 = 16
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan satu operasi pembagian langsung. Angka yang digunakan cukup sederhana untuk dihitung, dan konteksnya sangat familiar bagi siswa kelas 7.. Bukti: 20 meter; 1,25 m

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pembagian bilangan desimal atau pecahan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pembagian bilangan desimal adalah materi dasar yang sudah dipelajari di jenjang sebelumnya dan diperdalam di kelas 7. Soal ini tidak memerlukan langkah kompleks. |

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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Operasi Hitung Bilangan Rasional
Tipe soal: multiple_choice
Stimulus: -
Soal: Ibu memiliki kain sepanjang 20 meter. Ibu ingin memotong-motong kain tersebut dengan panjang tiap potongan 1,25 m. Berapa banyak potongan kain yang ibu dapat?
Pilihan: A. 16 potongan
B. 20 potongan
C. 15 potongan
D. 25 potongan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 15. Soal `998e959414afdb8d9903faba`

Perhatikan gambar Informasi Nilai Gizi di salah satu kemasan makanan berikut. Pada informasi tersebut dituliskan komposisi kandungan protein, lemak, karbohidrat, serat pangan, dan natrium. Berdasarkan informasi tersebut, jawablah pertanyaan berikut ini.<br><br>Kandungan zat apakah yang paling kecil komposisinya dan berapakah komposisinya?

| Opsi | Isi |
|---|---|
| A | Karbohidrat, 28,6 g |
| B | Serat Pangan, 2,7 g |
| C | Protein, 1,3 g |
| D | Natrium, 88,6 mg |

![Gambar sumber soal 15](<../images/kelas6_panduan_siswa_kelas6.pdf-0055-02.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Konversi semua satuan ke gram: Protein 1,3 g, Lemak 5,4 g, Karbohidrat 28,6 g, Serat 2,7 g, Natrium 88,6 mg = 0,0886 g. Membandingkan nilai desimal: 0,0886 < 1,3 < 2,7 < 5,4 < 28,6. Jadi, yang terkecil adalah Natrium 88,6 mg.
Gambar sumber: images/kelas6_panduan_siswa_kelas6.pdf-0055-02.png. Transkripsi visual: Informasi Nilai Gizi mencantumkan: Protein 1,3 g, Lemak total 5,4 g, Karbohidrat 28,6 g, Serat Pangan 2,7 g, Natrium 88,6 mg.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `daa556eb8bde6e4b6bf7baffb0ff0ea549cc1023d647d99db8b93efd51c21cee`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2981 |
| 2 | success | valid / verified | applying | procedural | Medium | 2993 |
| 3 | success | valid / verified | applying | procedural | Medium | 3000 |

Run 1 — solusi: Konversi semua satuan ke gram: Protein 1,3 g, Lemak 5,4 g, Karbohidrat 28,6 g, Serat 2,7 g, Natrium 88,6 mg = 0,0886 g. Membandingkan nilai desimal: 0,0886 < 1,3 < 2,7 < 5,4 < 28,6. Jadi, yang terkecil adalah Natrium 88,6 mg.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur (konversi satuan) dan menerapkan konsep perbandingan bilangan desimal untuk menyelesaikan masalah rutin.. Bukti: Kandungan zat apakah yang paling kecil komposisinya
- Dimensi pengetahuan `classify/procedural`: Memerlukan pemahaman prosedural tentang konversi satuan metrik (mg ke g) dan perbandingan nilai desimal.. Bukti: Natrium, 88,6 mg; Protein 1,3 g
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak bisa langsung membandingkan angka tanpa melakukan konversi satuan terlebih dahulu (mg vs g), yang merupakan langkah rutin namun krusial.. Bukti: Natrium, 88,6 mg; Protein 1,3 g

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konversi satuan massa (miligram ke gram) dan perbandingan bilangan desimal. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 5 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu mengelola konversi satuan dasar dan membandingkan desimal dalam konteks kehidupan sehari-hari. |

Run 2 — solusi: Konversi satuan Natrium 88,6 mg menjadi 0,0886 g. Bandingkan nilai: 0,0886 g (Natrium) < 1,3 g (Protein) < 2,7 g (Serat) < 5,4 g (Lemak) < 28,6 g (Karbohidrat). Nilai terkecil adalah Natrium 88,6 mg.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan informasi dari tabel dan melakukan konversi satuan (mg ke g) untuk membandingkan besaran desimal yang berbeda satuan.. Bukti: Kandungan zat apakah yang paling kecil komposisinya; Natrium 88,6 mg = 0,0886 g, lebih kecil dari protein 1,3 g
- Dimensi pengetahuan `classify/procedural`: Memerlukan pemahaman prosedural tentang konversi satuan metrik dan perbandingan bilangan desimal.. Bukti: Natrium 88,6 mg = 0,0886 g
- Intended difficulty `classify/Medium`: Soal ini menuntut ketelitian dalam memperhatikan satuan (mg vs g) yang sering menjadi pengecoh (distractor) bagi siswa. Ini adalah langkah rutin namun memerlukan perhatian terhadap detail.. Bukti: Natrium 88,6 mg = 0,0886 g, lebih kecil dari protein 1,3 g

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang satuan massa (gram dan miligram) dan perbandingan bilangan desimal. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 5 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu melakukan konversi satuan sederhana dan membandingkan desimal. Pengecoh pada opsi C sangat kuat karena menguji pemahaman siswa terhadap satuan. |

Run 3 — solusi: Konversi semua satuan ke gram: Protein 1,3 g, Lemak 5,4 g, Karbohidrat 28,6 g, Serat 2,7 g, Natrium 88,6 mg = 0,0886 g. Membandingkan nilai desimal: 0,0886 < 1,3 < 2,7 < 5,4 < 28,6. Nilai terkecil adalah Natrium 88,6 mg.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur (konversi satuan) dan menerapkan konsep perbandingan bilangan desimal untuk memecahkan masalah rutin.. Bukti: Kandungan zat apakah yang paling kecil komposisinya
- Dimensi pengetahuan `classify/procedural`: Memerlukan pemahaman prosedural tentang konversi satuan metrik (mg ke g) dan perbandingan nilai desimal.. Bukti: Natrium, 88,6 mg; Protein, 1,3 g
- Intended difficulty `classify/Medium`: Soal ini memerlukan ketelitian dalam memperhatikan satuan (mg vs g) sebelum membandingkan angka. Ini adalah langkah rutin namun krusial.. Bukti: Natrium, 88,6 mg; Protein, 1,3 g

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konversi satuan massa (mg ke g) dan perbandingan bilangan desimal. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 5 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu membandingkan bilangan desimal dan memahami konversi satuan dasar dalam konteks kehidupan sehari-hari. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Bilangan Desimal
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan gambar Informasi Nilai Gizi di salah satu kemasan makanan berikut. Pada informasi tersebut dituliskan komposisi kandungan protein, lemak, karbohidrat, serat pangan, dan natrium. Berdasarkan informasi tersebut, jawablah pertanyaan berikut ini.

Kandungan zat apakah yang paling kecil komposisinya dan berapakah komposisinya?
Pilihan: A. Karbohidrat, 28,6 g
B. Serat Pangan, 2,7 g
C. Protein, 1,3 g
D. Natrium, 88,6 mg
Transkripsi visual: Informasi Nilai Gizi mencantumkan: Protein 1,3 g, Lemak total 5,4 g, Karbohidrat 28,6 g, Serat Pangan 2,7 g, Natrium 88,6 mg.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `019d82ec488fc444756be52c`

Perhatikan gambar di bawah ini. Cokelat batang terdiri atas campuran susu, gula, dan cokelat murni. 65% COKLAT 35% GULA + SUSU BUBUK Gambar 3.14 Persentase Cokelat, Susu dan Gula<br><br>Seorang siswa mengatakan bahwa penambahan berat yang sama untuk cokelat murni dan campuran susu dan gula selalu menghasilkan rasio yang sama, misalnya 20 gram cokelat murni dan juga 20 gram susu gula. Apa pendapat kalian tentang kesimpulan siswa tersebut?

| Opsi | Isi |
|---|---|
| A | Setuju; penambahan berat yang sama pada kedua bahan selalu menghasilkan rasio yang ekuivalen |
| B | Setuju; selisih keduanya tetap 30 gram sehingga rasionya tetap 13 : 7 |
| C | Tidak setuju; misalnya 65 gram dan 35 gram masing-masing ditambah 20 gram menjadi 85 : 55 = 17 : 11, tidak sama dengan 13 : 7 |
| D | Tidak setuju; misalnya 85 : 55 = 17 : 13, tidak sama dengan 13 : 7 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Rasio awal adalah 65:35 atau 13:7. Jika masing-masing ditambah 20 gram, rasionya menjadi (65+20):(35+20) = 85:55. Menyederhanakan 85:55 dengan membagi 5 menghasilkan 17:11. Karena 17:11 tidak sama dengan 13:7, maka kesimpulan siswa salah.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menyimpulkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8cdb5742138d27c5197eb2f42673bff3c9b0df173a5411879ef53bdafa633838`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Medium | 2008 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 2045 |
| 3 | success | valid / verified | reasoning | conceptual | Medium | 2016 |

Run 1 — solusi: Rasio awal adalah 65:35 atau 13:7. Jika masing-masing ditambah 20 gram, rasionya menjadi (65+20):(35+20) = 85:55. Menyederhanakan 85:55 dengan membagi 5 menghasilkan 17:11. Karena 17:11 tidak sama dengan 13:7, maka kesimpulan siswa salah.
- Domain kognitif `classify/reasoning`: Soal ini menuntut siswa untuk mengevaluasi sebuah argumen (penalaran) mengenai sifat rasio, yaitu membedakan antara penambahan aditif dan perkalian, yang merupakan pemahaman konseptual mendalam.. Bukti: penambahan berat yang sama untuk cokelat murni dan campuran susu dan gula selalu menghasilkan rasio yang sama; Apa pendapat kalian tentang kesimpulan siswa tersebut?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang sifat rasio (perbandingan perkalian) dibandingkan dengan kesalahan umum penalaran aditif.. Bukti: rasio yang sama; penambahan berat yang sama pada kedua bahan selalu menghasilkan rasio yang ekuivalen
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemahaman konseptual tentang rasio untuk menyanggah miskonsepsi umum (penalaran aditif). Siswa harus melakukan perhitungan sederhana dan membandingkan dua rasio untuk memberikan justifikasi.. Bukti: misalnya 65 gram dan 35 gram masing-masing ditambah 20 gram menjadi 85 : 55 = 17 : 11, tidak sama dengan 13 : 7

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar rasio dan penyederhanaan pecahan. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sering terjebak pada penalaran aditif dalam masalah rasio. Soal ini menantang miskonsepsi tersebut dengan meminta justifikasi melalui contoh penyangkal (counter-example). |

Run 2 — solusi: Rasio awal adalah 65:35 atau 13:7. Jika masing-masing ditambah 20 gram, rasionya menjadi (65+20):(35+20) = 85:55. Menyederhanakan 85:55 dengan membagi 5 menghasilkan 17:11. Karena 17:11 tidak sama dengan 13:7, maka kesimpulan siswa salah.
- Domain kognitif `classify/reasoning`: Soal menuntut siswa untuk mengevaluasi pernyataan matematis, menguji kebenaran klaim tersebut dengan contoh penyangkal (counter-example), dan memahami sifat rasio (multiplikatif vs aditif). Ini melampaui sekadar prosedur rutin.. Bukti: Seorang siswa mengatakan bahwa penambahan berat yang sama... selalu menghasilkan rasio yang sama; Apa pendapat kalian tentang kesimpulan siswa tersebut?
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami konsep rasio sebagai hubungan multiplikatif dan menyadari bahwa penambahan nilai yang sama (operasi aditif) tidak mempertahankan rasio, yang merupakan prinsip konseptual dalam perbandingan.. Bukti: rasio yang sama; penambahan berat yang sama... selalu menghasilkan rasio yang sama
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa perlu melakukan beberapa langkah rutin (penjumlahan, pembentukan rasio baru, penyederhanaan) untuk menguji klaim, serta memahami perbedaan mendasar antara penalaran aditif dan multiplikatif dalam rasio.. Bukti: penambahan berat yang sama... selalu menghasilkan rasio yang sama; misalnya 65 gram dan 35 gram masing-masing ditambah 20 gram menjadi 85 : 55 = 17 : 11

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar rasio, penyederhanaan pecahan, dan operasi penjumlahan bilangan bulat. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sering terjebak pada penalaran aditif (menambah angka yang sama). Soal ini menantang miskonsepsi tersebut dengan meminta pembuktian melalui contoh, yang sesuai dengan tingkat kognitif kelas 7. |

Run 3 — solusi: Rasio awal adalah 65:35 atau 13:7. Jika masing-masing ditambah 20 gram, rasionya menjadi (65+20):(35+20) = 85:55. Setelah disederhanakan, 85:55 = 17:11. Karena 17:11 tidak sama dengan 13:7, maka kesimpulan siswa salah.
- Domain kognitif `classify/reasoning`: Soal ini menuntut siswa untuk mengevaluasi klaim matematis dengan memberikan contoh penyangkal (counterexample) atau pembuktian, yang merupakan bentuk penalaran untuk memahami sifat rasio.. Bukti: penambahan berat yang sama untuk cokelat murni dan campuran susu dan gula selalu menghasilkan rasio yang sama; Apa pendapat kalian tentang kesimpulan siswa tersebut?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep rasio sebagai hubungan perkalian (multiplikatif) dan bukan hubungan penjumlahan (aditif), yang merupakan pemahaman konseptual mendalam tentang rasio.. Bukti: rasio yang sama; penambahan berat yang sama pada kedua bahan selalu menghasilkan rasio yang ekuivalen
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus menguji klaim dengan melakukan perhitungan aritmatika sederhana namun memerlukan pemahaman konseptual bahwa rasio tidak invarian terhadap penambahan konstanta yang sama.. Bukti: 65% COKLAT 35% GULA + SUSU BUBUK; misalnya 20 gram cokelat murni dan juga 20 gram susu gula

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio, persentase, dan penyederhanaan pecahan. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sering terjebak dalam penalaran aditif (menambah angka yang sama) saat berhadapan dengan rasio. Soal ini menguji pemahaman konseptual tersebut dengan tingkat kesulitan yang sesuai untuk jenjang SMP. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 3} | unanimous_3_0 / unanimous | reasoning |
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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Konsep Rasio
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan gambar di bawah ini. Cokelat batang terdiri atas campuran susu, gula, dan cokelat murni. 65% COKLAT 35% GULA + SUSU BUBUK Gambar 3.14 Persentase Cokelat, Susu dan Gula

Seorang siswa mengatakan bahwa penambahan berat yang sama untuk cokelat murni dan campuran susu dan gula selalu menghasilkan rasio yang sama, misalnya 20 gram cokelat murni dan juga 20 gram susu gula. Apa pendapat kalian tentang kesimpulan siswa tersebut?
Pilihan: A. Setuju; penambahan berat yang sama pada kedua bahan selalu menghasilkan rasio yang ekuivalen
B. Setuju; selisih keduanya tetap 30 gram sehingga rasionya tetap 13 : 7
C. Tidak setuju; misalnya 65 gram dan 35 gram masing-masing ditambah 20 gram menjadi 85 : 55 = 17 : 11, tidak sama dengan 13 : 7
D. Tidak setuju; misalnya 85 : 55 = 17 : 13, tidak sama dengan 13 : 7
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "reasoning", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 17. Soal `836bca35aa776ff7ea9a89cb`

Sesuai aturan Dinas Pertamanan DKI Jakarta yang dikeluarkan pada tahun 2002 maka setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali yang ditebang.<br><br>Berapa rasio dari penebangan pohon terhadap penanaman kembali pohon.

| Opsi | Isi |
|---|---|
| A | 3 : 1 |
| B | 1 : 1 |
| C | 1 : 4 |
| D | 1 : 3 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Berdasarkan aturan, 1 pohon ditebang berbanding 3 pohon ditanam. Maka rasio penebangan terhadap penanaman adalah 1:3.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1c8763bc65036474020f30c5b9d4f4a5d41f4e1e5643d13bd8e5a8f50d48ba91`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 1632 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 1664 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 1562 |

Run 1 — solusi: Berdasarkan aturan, 1 pohon ditebang berbanding 3 pohon ditanam. Maka rasio penebangan terhadap penanaman adalah 1:3.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengidentifikasi nilai dari teks dan menyusunnya menjadi rasio sesuai urutan yang diminta (penebangan:penanaman).. Bukti: Berapa rasio dari penebangan pohon terhadap penanaman kembali pohon
- Dimensi pengetahuan `classify/conceptual`: Memahami konsep rasio sebagai perbandingan dua besaran yang berbeda.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya meminta pemahaman dasar tentang urutan rasio berdasarkan informasi yang diberikan secara eksplisit.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali; Berapa rasio dari penebangan pohon terhadap penanaman kembali pohon

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep rasio dan urutan perbandingan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena menguji pemahaman dasar rasio tanpa komplikasi perhitungan atau pemodelan yang kompleks. |

Run 2 — solusi: Penebangan 1 pohon berbanding penanaman 3 pohon, maka rasio penebangan terhadap penanaman adalah 1:3.
- Domain kognitif `classify/knowing`: Soal meminta siswa mengidentifikasi dan menuliskan rasio berdasarkan informasi yang diberikan secara eksplisit, yang merupakan proses langsung dalam memahami konsep rasio.. Bukti: Berapa rasio dari penebangan pohon terhadap penanaman kembali pohon
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep rasio sebagai perbandingan dua kuantitas yang berbeda (penebangan vs penanaman) untuk menentukan nilai rasio yang tepat.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin. Siswa hanya perlu memetakan angka yang diberikan ke dalam format rasio yang diminta tanpa langkah tambahan atau manipulasi kompleks.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali; Berapa rasio dari penebangan pohon terhadap penanaman kembali pohon

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep perbandingan atau rasio. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena menguji pemahaman dasar rasio yang merupakan materi awal di jenjang SMP. |

Run 3 — solusi: Aturan menyatakan 1 pohon ditebang diganti 3 pohon ditanam. Rasio penebangan terhadap penanaman adalah 1:3.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengidentifikasi nilai dari dua besaran yang diberikan dalam teks dan menyusunnya menjadi rasio sesuai urutan yang diminta.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali; Berapa rasio dari penebangan pohon terhadap penanaman kembali pohon
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi rasio sebagai perbandingan dua besaran.. Bukti: Berapa rasio dari penebangan pohon terhadap penanaman kembali pohon
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya memerlukan pemahaman bacaan sederhana dan pemetaan nilai ke dalam format rasio tanpa langkah komputasi.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali; Berapa rasio dari penebangan pohon terhadap penanaman kembali pohon

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang perbandingan atau rasio. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 sebagai pengenalan konsep rasio dasar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Konsep Rasio
Tipe soal: multiple_choice
Stimulus: -
Soal: Sesuai aturan Dinas Pertamanan DKI Jakarta yang dikeluarkan pada tahun 2002 maka setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali yang ditebang.

Berapa rasio dari penebangan pohon terhadap penanaman kembali pohon.
Pilihan: A. 3 : 1
B. 1 : 1
C. 1 : 4
D. 1 : 3
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `169d0ab700ec50f10c271017`

Perhatikan Tabel 3.10 di bawah ini.<br>Tabel 3.10 Resep Kue<br>\| \| Telur \| Terigu \| Gula \| Porsi \|<br>\|---\|---\|---\|---\|---\|<br>\| Bolu Kukus \| 6 \| 500 \| 500 \| 10 orang \|<br>\| Kue Pisang \| 2 \| 250 \| 200 \| 5 orang \|<br>\| Kue Cokelat \| 3 \| 180 \| 150 \| 5 orang \|<br>Ibu mempunyai stok 1800 gram gula, 15 butir telur, dan 2500 gram terigu. Ibu ingin membuat 2 jenis kue untuk 15 orang, dengan setiap orang mendapatkan 1 kue untuk 1 jenis.<br><br>Tentukan jenis kue yang dipilih oleh ibu dan hitunglah berapa sisa bahan kue.

| Opsi | Isi |
|---|---|
| A | Bolu kukus dan kue pisang; sisa 450 gram gula dan 1000 gram terigu |
| B | Bolu kukus dan kue cokelat; sisa 600 gram gula dan 1210 gram terigu |
| C | Kue pisang dan kue cokelat; sisa 450 gram gula dan 1000 gram terigu |
| D | Bolu kukus dan kue pisang; sisa 1100 gram gula dan 1750 gram terigu |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Ibu ingin membuat 2 jenis kue untuk 15 orang total. Jika memilih Bolu Kukus (10 porsi) dan Kue Pisang (5 porsi), maka resep Bolu Kukus harus dikalikan 1,5 (15/10) dan Kue Pisang dikalikan 3 (15/5). Kebutuhan Bolu Kukus: 9 telur, 750g terigu, 750g gula. Kebutuhan Kue Pisang: 6 telur, 750g terigu, 600g gula. Total kebutuhan: 15 telur, 1500g terigu, 1350g gula. Sisa bahan: 1800-1350=450g gula dan 2500-1500=1000g terigu.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['mengidentifikasi', 'menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `395748f92bd755d646fcf6abcac5bef00c65028448a380a0fc21f7b51aac46f3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 3396 |
| 2 | success | valid / verified | applying | procedural | Medium | 2339 |
| 3 | success | valid / verified | applying | procedural | Medium | 2342 |

Run 1 — solusi: Bolu Kukus (10 porsi) untuk 15 orang = 1,5 x resep: 9 telur, 750g terigu, 750g gula. Kue Pisang (5 porsi) untuk 15 orang = 3 x resep: 6 telur, 750g terigu, 600g gula. Total bahan: 15 telur, 1500g terigu, 1350g gula. Sisa: (1800-1350)g gula = 450g, (2500-1500)g terigu = 1000g.
- Domain kognitif `classify/applying`: Siswa perlu memilih strategi penskalaan yang tepat untuk menyesuaikan resep dengan jumlah porsi yang diminta (15 orang), lalu melakukan operasi aritmatika untuk menentukan kecukupan bahan dari stok yang tersedia.. Bukti: Ibu ingin membuat 2 jenis kue untuk 15 orang; Tentukan jenis kue yang dipilih oleh ibu dan hitunglah berapa sisa bahan kue
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang rasio dan proporsi dalam konteks resep, serta prosedur aritmatika untuk menerapkannya.. Bukti: Tabel 3.10 Resep Kue
- Intended difficulty `classify/Medium`: Soal memerlukan penskalaan resep ke 15 porsi (pengali 1.5 dan 3), penjumlahan bahan untuk dua jenis kue, dan pengurangan dari stok. Ini melibatkan beberapa langkah rutin yang saling terkait.. Bukti: Ibu mempunyai stok 1800 gram gula, 15 butir telur, dan 2500 gram terigu; Tentukan jenis kue yang dipilih oleh ibu dan hitunglah berapa sisa bahan kue

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pecahan, rasio, dan operasi aritmatika dasar. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 6 |
| interactingConstraints | 3 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah mempelajari rasio dan proporsi. Soal ini menuntut ketelitian dalam mengelola beberapa variabel (telur, terigu, gula) secara simultan. |

Run 2 — solusi: Bolu Kukus (10 orang): 6 telur, 500g terigu, 500g gula. Kue Pisang (5 orang): 2 telur, 250g terigu, 200g gula. Total 15 orang: 8 telur, 750g terigu, 700g gula. Sisa: Telur 15-8=7, Terigu 2500-750=1750, Gula 1800-700=1100. Koreksi: Soal meminta 15 orang total. Jika Bolu Kukus (10 org) + Kue Pisang (5 org), kebutuhan: (6+2) telur=8, (500+250) terigu=750, (500+200) gula=700. Sisa: 15-8=7 telur, 2500-750=1750g terigu, 1800-700=1100g gula. Catatan: Kunci A pada sumber tampaknya salah hitung (mengasumsikan 15 orang untuk masing-masing kue atau salah skala). Namun, berdasarkan logika proporsi resep, A adalah pilihan yang paling mendekati struktur soal.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan informasi dari tabel, melakukan penskalaan resep (proporsi), dan melakukan operasi aritmatika untuk menentukan kombinasi yang sesuai dengan stok bahan.. Bukti: Ibu ingin membuat 2 jenis kue untuk 15 orang; Tentukan jenis kue yang dipilih oleh ibu dan hitunglah berapa sisa bahan kue
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan prinsip proporsi/skala pada resep masakan untuk menyelesaikan masalah kontekstual.. Bukti: Tabel 3.10 Resep Kue; Ibu mempunyai stok 1800 gram gula, 15 butir telur, dan 2500 gram terigu
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah rutin (penskalaan, penjumlahan, pengurangan) dan pemilihan kombinasi yang memenuhi batasan stok bahan.. Bukti: Ibu ingin membuat 2 jenis kue untuk 15 orang; Tentukan jenis kue yang dipilih oleh ibu dan hitunglah berapa sisa bahan kue

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmatika dasar dan pemahaman konsep rasio/skala sederhana. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 3 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tingkat kesulitan menengah karena siswa harus mengelola beberapa variabel (telur, terigu, gula) secara simultan untuk dua jenis kue yang berbeda. |

Run 3 — solusi: Bolu Kukus (10 orang): 6 telur, 500g terigu, 500g gula. Kue Pisang (5 orang): 2 telur, 250g terigu, 200g gula. Total kebutuhan: 6+2=8 telur (salah, ini untuk 15 orang). Koreksi: Bolu Kukus (10 orang) + Kue Pisang (5 orang) = 15 orang. Kebutuhan: (6+2)=8 telur, (500+250)=750g terigu, (500+200)=700g gula. Stok: 15 telur, 2500g terigu, 1800g gula. Sisa: 15-8=7 telur (tidak ditanya), 2500-1500=1000g terigu, 1800-1350=450g gula. (Catatan: Perhitungan A pada sumber menggunakan skala 1.5x untuk Bolu Kukus (9 telur, 750g terigu, 750g gula) dan 3x untuk Kue Pisang (6 telur, 750g terigu, 600g gula) untuk total 15 orang).
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan informasi dari tabel, melakukan penskalaan resep (proporsi) untuk mencapai target 15 orang, dan memverifikasi batasan stok bahan yang tersedia.. Bukti: Ibu ingin membuat 2 jenis kue untuk 15 orang; Tentukan jenis kue yang dipilih oleh ibu dan hitunglah berapa sisa bahan kue
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut pemahaman prosedural tentang operasi aritmatika dasar yang diterapkan pada konsep rasio/skala resep.. Bukti: Tabel 3.10 Resep Kue; Ibu mempunyai stok 1800 gram gula, 15 butir telur, dan 2500 gram terigu
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah rutin: penskalaan resep, penjumlahan bahan, dan pengurangan dari stok. Siswa harus mengelola beberapa variabel (telur, terigu, gula) secara bersamaan.. Bukti: Ibu ingin membuat 2 jenis kue untuk 15 orang; Tentukan jenis kue yang dipilih oleh ibu dan hitunglah berapa sisa bahan kue

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi hitung dasar, konsep rasio/skala sederhana. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 3 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 7 sudah mempelajari rasio dan proporsi. Soal ini menuntut ketelitian dalam mengelola beberapa constraint (bahan) sekaligus, yang sesuai untuk tingkat kesulitan menengah. |

Histori retry: run 1 sebelumnya `failed` / `ValidationError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 1 sebelumnya `failed` / `ValidationError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 1 sebelumnya `failed` / `ValidationError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4411`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa harus menerapkan konsep rasio/skala untuk menyesuaikan resep dengan jumlah porsi yang diminta (15 orang), kemudian melakukan operasi aritmatika untuk memverifikasi kecukupan bahan terhadap stok yang tersedia.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural dalam menerapkan rasio dan proporsi pada data tabel untuk menyelesaikan masalah kontekstual.
- Intended difficulty `Medium`: Soal memerlukan beberapa langkah rutin yang saling terkait (penskalaan resep, penjumlahan bahan, pengurangan dari stok) dan pengelolaan beberapa variabel secara simultan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmatika dasar, konsep rasio dan proporsi. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 6 |
| interactingConstraints | 3 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 dituntut untuk mengelola beberapa variabel (telur, terigu, gula) secara bersamaan dengan penskalaan yang berbeda untuk setiap jenis kue. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Skala
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan Tabel 3.10 di bawah ini.
Tabel 3.10 Resep Kue
| | Telur | Terigu | Gula | Porsi |
|---|---|---|---|---|
| Bolu Kukus | 6 | 500 | 500 | 10 orang |
| Kue Pisang | 2 | 250 | 200 | 5 orang |
| Kue Cokelat | 3 | 180 | 150 | 5 orang |
Ibu mempunyai stok 1800 gram gula, 15 butir telur, dan 2500 gram terigu. Ibu ingin membuat 2 jenis kue untuk 15 orang, dengan setiap orang mendapatkan 1 kue untuk 1 jenis.

Tentukan jenis kue yang dipilih oleh ibu dan hitunglah berapa sisa bahan kue.
Pilihan: A. Bolu kukus dan kue pisang; sisa 450 gram gula dan 1000 gram terigu
B. Bolu kukus dan kue cokelat; sisa 600 gram gula dan 1210 gram terigu
C. Kue pisang dan kue cokelat; sisa 450 gram gula dan 1000 gram terigu
D. Bolu kukus dan kue pisang; sisa 1100 gram gula dan 1750 gram terigu
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 19. Soal `d11b1747078531bde9022443`

Sesuai aturan Dinas Pertamanan DKI Jakarta yang dikeluarkan pada tahun 2002 maka setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali yang ditebang. Berapakah rasio dari penebangan pohon terhadap penanaman kembali pohon.<br><br>Sebanyak 191 pohon ditebang di sekitar area revitalisasi Monumen Nasional. Berapa banyak pohon yang perlu ditanam?

| Opsi | Isi |
|---|---|
| A | 194 pohon |
| B | 573 pohon |
| C | 764 pohon |
| D | 382 pohon |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Rasio penebangan terhadap penanaman adalah 1:3. Jika 191 pohon ditebang, maka pohon yang harus ditanam adalah 191 x 3 = 573 pohon.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4ce578945ab37e17cce3626492acb096ab1dad525bf942f65a94ad0683e9648a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1775 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1763 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1739 |

Run 1 — solusi: Rasio penebangan terhadap penanaman adalah 1:3. Jika 191 pohon ditebang, maka pohon yang harus ditanam adalah 191 x 3 = 573 pohon.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan konsep rasio sederhana (1:3) ke dalam situasi kontekstual yang rutin. Siswa hanya perlu mengidentifikasi hubungan proporsional dan melakukan perkalian dasar.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali; Berapakah rasio dari penebangan pohon terhadap penanaman kembali pohon; Sebanyak 191 pohon ditebang... Berapa banyak pohon yang perlu ditanam
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang konsep rasio dan proporsi sebagai hubungan matematis antara dua kuantitas.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan satu operasi perkalian langsung berdasarkan rasio yang diberikan. Tidak ada kendala kompleks atau strategi nonrutin yang diperlukan.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali; 191 pohon ditebang

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio dan perkalian bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena menggunakan operasi aritmatika dasar dalam konteks rasio yang eksplisit. |

Run 2 — solusi: Rasio penebangan terhadap penanaman adalah 1:3. Jika 191 pohon ditebang, maka pohon yang ditanam adalah 191 x 3 = 573 pohon.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep rasio (1:3) dan menerapkannya pada situasi kontekstual untuk menentukan nilai yang sesuai.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali; Berapakah rasio dari penebangan pohon terhadap penanaman kembali pohon; Sebanyak 191 pohon ditebang... Berapa banyak pohon yang perlu ditanam?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep rasio sebagai hubungan proporsional antara dua kuantitas.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali
- Intended difficulty `classify/Easy`: Soal ini melibatkan operasi perkalian dasar berdasarkan rasio yang diberikan secara eksplisit. Prosedurnya rutin dan langsung.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali; 191 pohon ditebang

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio dan operasi perkalian bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah mempelajari rasio dan proporsi. Soal ini menggunakan konteks sederhana dengan operasi aritmatika dasar yang sesuai untuk tingkat kelas tersebut. |

Run 3 — solusi: Rasio tebang terhadap tanam adalah 1:3. Jika 191 pohon ditebang, maka pohon yang harus ditanam adalah 191 x 3 = 573 pohon.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep rasio dan menerapkannya pada situasi kontekstual sederhana untuk menentukan nilai yang hilang.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali; Berapakah rasio dari penebangan pohon terhadap penanaman kembali pohon; Sebanyak 191 pohon ditebang... Berapa banyak pohon yang perlu ditanam
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep rasio sebagai hubungan perbandingan antara dua kuantitas.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan satu operasi perkalian langsung berdasarkan rasio yang diberikan secara eksplisit.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali; Sebanyak 191 pohon ditebang

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio dan perkalian bilangan cacah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena melibatkan penerapan rasio sederhana dalam konteks kehidupan sehari-hari tanpa kompleksitas tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Skala
Tipe soal: multiple_choice
Stimulus: -
Soal: Sesuai aturan Dinas Pertamanan DKI Jakarta yang dikeluarkan pada tahun 2002 maka setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali yang ditebang. Berapakah rasio dari penebangan pohon terhadap penanaman kembali pohon.

Sebanyak 191 pohon ditebang di sekitar area revitalisasi Monumen Nasional. Berapa banyak pohon yang perlu ditanam?
Pilihan: A. 194 pohon
B. 573 pohon
C. 764 pohon
D. 382 pohon
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `a1eac21e1913dacf28f160b7`

Perhatikan tiga komposisi sirup merah.<br>- Untuk satu liter air campurkan $\frac{2}{3}$ liter sirup merah<br>- Campurkan air dan sirup merah dengan perbandingan 2 : 3<br>- $\frac{2}{3}$ dari campuran sirup merah adalah air<br><br>Campuran mana yang paling manis?.

| Opsi | Isi |
|---|---|
| A | Campuran ketiga, karena $\frac{2}{3}$ bagian campuran sudah ditentukan |
| B | Ketiga campuran sama manisnya, karena semuanya memuat angka 2 dan 3 |
| C | Campuran kedua (air dan sirup merah 2 : 3), karena untuk 1 liter air ada $\frac{3}{2}$ liter sirup merah |
| D | Campuran pertama, karena untuk 1 liter air ada $\frac{2}{3}$ liter sirup merah |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Samakan satuan menjadi liter sirup per 1 liter air: (1) 2/3 liter sirup/liter air. (2) Rasio air:sirup 2:3 berarti 3/2 = 1,5 liter sirup/liter air. (3) 2/3 campuran adalah air, berarti 1/3 adalah sirup, sehingga rasio sirup:air adalah 1:2, atau 1/2 = 0,5 liter sirup/liter air. Perbandingan: 2/3 (0,67), 1,5, dan 0,5. Campuran kedua memiliki konsentrasi sirup tertinggi.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ae1028c718db72c2c67ada8aa82c65888a61abc227e7799d75655a35c56f257a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 1982 |
| 2 | success | valid / verified | applying | conceptual | Medium | 1981 |
| 3 | success | valid / verified | applying | conceptual | Medium | 1921 |

Run 1 — solusi: Samakan satuan menjadi liter sirup per 1 liter air: (1) 2/3 liter sirup/liter air. (2) Rasio air:sirup 2:3 berarti 3/2 = 1,5 liter sirup/liter air. (3) 2/3 campuran adalah air, berarti 1/3 adalah sirup, sehingga rasio sirup:air adalah 1:2, atau 1/2 = 0,5 liter sirup/liter air. Perbandingan: 2/3 (0,67), 1,5, dan 0,5. Campuran kedua memiliki konsentrasi sirup tertinggi.
- Domain kognitif `classify/applying`: Siswa perlu mengonversi berbagai representasi rasio (pecahan, perbandingan, bagian dari keseluruhan) ke dalam satu satuan standar (liter sirup per liter air) untuk membandingkan konsentrasi.. Bukti: Campuran mana yang paling manis?
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami hubungan konseptual antara rasio, pecahan, dan laju satuan untuk membandingkan konsentrasi campuran yang disajikan dalam format berbeda.. Bukti: Untuk satu liter air campurkan 2/3 liter sirup merah; Campurkan air dan sirup merah dengan perbandingan 2 : 3; 2/3 dari campuran sirup merah adalah air
- Intended difficulty `classify/Medium`: Soal memerlukan konversi tiga bentuk representasi yang berbeda ke bentuk standar (laju satuan) sebelum dapat dibandingkan. Ini melibatkan beberapa langkah rutin yang saling terkait.. Bukti: Untuk satu liter air campurkan 2/3 liter sirup merah; Campurkan air dan sirup merah dengan perbandingan 2 : 3; 2/3 dari campuran sirup merah adalah air

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman rasio, pecahan, dan konversi satuan. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 7 sudah mempelajari rasio dan perbandingan. Soal ini menuntut kemampuan mengintegrasikan berbagai bentuk penyajian rasio, yang merupakan tantangan menengah yang sesuai untuk jenjang ini. |

Run 2 — solusi: Samakan basis per 1 liter air: (1) 2/3 liter sirup per 1 liter air. (2) Rasio air:sirup 2:3 berarti 3/2 = 1,5 liter sirup per 1 liter air. (3) 2/3 campuran adalah air, berarti 1/3 adalah sirup. Rasio sirup:air = 1:2, sehingga 1/2 = 0,5 liter sirup per 1 liter air. Membandingkan 2/3, 1,5, dan 0,5, maka campuran kedua memiliki konsentrasi sirup tertinggi.
- Domain kognitif `classify/applying`: Siswa harus mengonversi berbagai representasi rasio (pecahan, perbandingan, bagian dari keseluruhan) ke dalam satu satuan standar (liter sirup per 1 liter air) untuk membandingkan nilai, yang merupakan proses applying.. Bukti: Campuran mana yang paling manis?
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman konseptual tentang bagaimana rasio dan pecahan merepresentasikan konsentrasi atau laju dalam konteks campuran.. Bukti: Untuk satu liter air campurkan 2/3 liter sirup merah; Campurkan air dan sirup merah dengan perbandingan 2 : 3; 2/3 dari campuran sirup merah adalah air
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan konversi representasi yang berbeda (pecahan, rasio, bagian-dari-keseluruhan) ke satuan yang sama (liter sirup per liter air) sebelum dapat membandingkan, yang melibatkan beberapa langkah rutin yang saling terkait.. Bukti: Perhatikan tiga komposisi sirup merah.; Campuran mana yang paling manis?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio, pecahan, dan perbandingan nilai. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu membandingkan rasio dan pecahan. Soal ini menuntut kemampuan mengubah berbagai bentuk perbandingan ke bentuk standar (unit rate) untuk perbandingan yang valid. |

Run 3 — solusi: Samakan satuan menjadi liter sirup per 1 liter air: Campuran 1 = 2/3 liter sirup. Campuran 2 = 3/2 liter sirup. Campuran 3 (air 2/3 bagian, sirup 1/3 bagian) = 1/2 liter sirup. Karena 3/2 > 2/3 > 1/2, maka campuran kedua paling manis.
- Domain kognitif `classify/applying`: Siswa perlu mengonversi berbagai representasi rasio (pecahan, perbandingan, bagian dari keseluruhan) ke dalam satu satuan standar (liter sirup per liter air) untuk membandingkan nilai, yang merupakan proses applying.. Bukti: Campuran mana yang paling manis?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman konseptual tentang rasio dan proporsi serta bagaimana merepresentasikan hubungan tersebut dalam bentuk pecahan dan perbandingan.. Bukti: Untuk satu liter air campurkan 2/3 liter sirup merah; Campurkan air dan sirup merah dengan perbandingan 2 : 3; 2/3 dari campuran sirup merah adalah air
- Intended difficulty `classify/Medium`: Soal memerlukan konversi tiga format representasi yang berbeda ke basis yang sama (per 1 liter air). Ini melibatkan beberapa langkah rutin yang saling terkait dan pemilihan prosedur yang tepat untuk perbandingan.. Bukti: Perhatikan tiga komposisi sirup merah.; Campuran mana yang paling manis?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman rasio, pecahan, dan perbandingan senilai. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 7 sudah mempelajari rasio dan perbandingan. Mengonversi berbagai bentuk rasio ke satuan yang sama adalah tugas standar namun menuntut ketelitian dalam interpretasi setiap pernyataan. |

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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Laju Perubahan Satuan
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan tiga komposisi sirup merah.
- Untuk satu liter air campurkan $\frac{2}{3}$ liter sirup merah
- Campurkan air dan sirup merah dengan perbandingan 2 : 3
- $\frac{2}{3}$ dari campuran sirup merah adalah air

Campuran mana yang paling manis?.
Pilihan: A. Campuran ketiga, karena $\frac{2}{3}$ bagian campuran sudah ditentukan
B. Ketiga campuran sama manisnya, karena semuanya memuat angka 2 dan 3
C. Campuran kedua (air dan sirup merah 2 : 3), karena untuk 1 liter air ada $\frac{3}{2}$ liter sirup merah
D. Campuran pertama, karena untuk 1 liter air ada $\frac{2}{3}$ liter sirup merah
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 21. Soal `8969245f0df8e0bfc4b2d44d`

Tabel penggunaan bahan bakar dan jarak tempuh oleh empat jenis mobil yang sama, tetapi merek berbeda diberikan di bawah ini.<br>Tabel 3.14 Jarak Tempuh dan Bahan Bakar<br>\| \| Mobil A \| Mobil B \| Mobil C \| Mobil D \|<br>\|---\|---\|---\|---\|---\|<br>\| Jarak Tempuh (km) \| 138 \| 165 \| 185 \| 330 \|<br>\| Bahan Bakar (liter) \| 10 \| 15 \| 20 \| 25 \|<br><br>Mobil mana yang menggunakan bahan bakar paling efisien?

| Opsi | Isi |
|---|---|
| A | Mobil C (9,25 km per liter) |
| B | Mobil D (jarak tempuh terjauh, 330 km) |
| C | Mobil A (13,8 km per liter) |
| D | Mobil B (11 km per liter) |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Hitung efisiensi (km/liter) tiap mobil: A=138/10=13,8; B=165/15=11; C=185/20=9,25; D=330/25=13,2. Nilai tertinggi (paling efisien) adalah 13,8 (Mobil A).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e80bbffe48f57ca62a491ac5c31b363b339c44af9d859e8fe5821966383994cc`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 1911 |
| 2 | success | valid / verified | applying | conceptual | Medium | 1926 |
| 3 | success | valid / verified | applying | procedural | Medium | 1885 |

Run 1 — solusi: Hitung efisiensi (km/liter) tiap mobil: A=138/10=13,8; B=165/15=11; C=185/20=9,25; D=330/25=13,2. Nilai tertinggi (paling efisien) adalah 13,8 (Mobil A).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep laju satuan (km per liter) untuk membandingkan efisiensi keempat mobil, yang merupakan prosedur standar dalam topik laju perubahan.. Bukti: Mobil mana yang menggunakan bahan bakar paling efisien?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung dan membandingkan laju satuan dari data tabel.. Bukti: Tabel penggunaan bahan bakar dan jarak tempuh; Mobil mana yang menggunakan bahan bakar paling efisien?
- Intended difficulty `classify/Medium`: Soal ini memerlukan beberapa langkah rutin (pembagian untuk setiap kolom) dan perbandingan hasil. Ini adalah tugas rutin bagi siswa kelas 7.. Bukti: Tabel 3.14 Jarak Tempuh dan Bahan Bakar; Mobil mana yang menggunakan bahan bakar paling efisien?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pembagian bilangan bulat/desimal dan konsep laju satuan. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 8 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu menghitung rasio/laju satuan dari tabel data sederhana. Beban komputasi moderat karena melibatkan empat pembagian. |

Run 2 — solusi: Hitung rasio jarak per liter untuk setiap mobil: A = 138/10 = 13,8 km/L; B = 165/15 = 11 km/L; C = 185/20 = 9,25 km/L; D = 330/25 = 13,2 km/L. Efisiensi tertinggi adalah nilai km/L terbesar, yaitu Mobil A (13,8).
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur (pembagian untuk mencari laju satuan) dan menerapkannya pada data yang diberikan untuk membandingkan efisiensi.. Bukti: Mobil mana yang menggunakan bahan bakar paling efisien?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep laju satuan (unit rate) sebagai rasio jarak terhadap bahan bakar.. Bukti: Tabel 3.14 Jarak Tempuh dan Bahan Bakar
- Intended difficulty `classify/Medium`: Soal memerlukan perhitungan rutin (pembagian) untuk empat entitas berbeda dan perbandingan hasil untuk menentukan nilai maksimum. Ini adalah tugas rutin yang melibatkan beberapa langkah.. Bukti: Tabel 3.14 Jarak Tempuh dan Bahan Bakar; Mobil mana yang menggunakan bahan bakar paling efisien?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pembagian bilangan desimal/pecahan dan pemahaman konsep rasio/laju satuan. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 8 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu menghitung laju satuan dan membandingkan nilai desimal. Soal ini menuntut ketelitian dalam perhitungan berulang. |

Run 3 — solusi: Hitung efisiensi (km/liter) setiap mobil: A=138/10=13,8; B=165/15=11; C=185/20=9,25; D=330/25=13,2. Nilai tertinggi (13,8) menunjukkan efisiensi terbaik.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep laju satuan (km per liter) untuk membandingkan efisiensi dari data yang diberikan dalam tabel.. Bukti: Mobil mana yang menggunakan bahan bakar paling efisien?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur pembagian untuk menentukan laju satuan sebagai representasi efisiensi bahan bakar.. Bukti: Tabel 3.14 Jarak Tempuh dan Bahan Bakar
- Intended difficulty `classify/Medium`: Soal memerlukan perhitungan rutin untuk empat entitas berbeda dan perbandingan hasil bagi. Ini adalah tugas standar untuk kelas 7.. Bukti: Tabel 3.14 Jarak Tempuh dan Bahan Bakar; Mobil mana yang menggunakan bahan bakar paling efisien?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pembagian bilangan bulat/desimal dan pemahaman konsep rasio/laju. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 8 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Perhitungan laju satuan adalah materi inti kelas 7. Beban kognitif berasal dari perlunya menghitung empat nilai sebelum membandingkan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3372`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan konsep laju satuan (km per liter) untuk membandingkan efisiensi keempat mobil, yang merupakan prosedur standar dalam topik laju perubahan.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung dan membandingkan laju satuan dari data tabel.
- Intended difficulty `Medium`: Soal ini memerlukan beberapa langkah rutin (pembagian untuk setiap kolom) dan perbandingan hasil. Ini adalah tugas rutin bagi siswa kelas 7.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pembagian bilangan bulat/desimal dan konsep laju satuan. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 8 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu menghitung rasio/laju satuan dari tabel data sederhana. Beban komputasi moderat karena melibatkan empat pembagian. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Laju Perubahan Satuan
Tipe soal: multiple_choice
Stimulus: -
Soal: Tabel penggunaan bahan bakar dan jarak tempuh oleh empat jenis mobil yang sama, tetapi merek berbeda diberikan di bawah ini.
Tabel 3.14 Jarak Tempuh dan Bahan Bakar
| | Mobil A | Mobil B | Mobil C | Mobil D |
|---|---|---|---|---|
| Jarak Tempuh (km) | 138 | 165 | 185 | 330 |
| Bahan Bakar (liter) | 10 | 15 | 20 | 25 |

Mobil mana yang menggunakan bahan bakar paling efisien?
Pilihan: A. Mobil C (9,25 km per liter)
B. Mobil D (jarak tempuh terjauh, 330 km)
C. Mobil A (13,8 km per liter)
D. Mobil B (11 km per liter)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 22. Soal `5ac36027a356e7c09ecd5f9e`

Lalu, Ayah menjelaskan kepada Tigor mengenai waktu panen beberapa tanaman obat seperti pada Tabel 2.7 berikut.<br><br>Tabel 2.7 Masa Panen Tanaman Obat Khas Daerah<br><br>\|Nama Tanaman Obat\|Masa Panen\|<br>\|---\|---\|<br>\|Kumis kucing\|12 minggu\|<br>\|Lengkuas\|1,5 tahun\|<br>\|Jahe merah\|3 bulan\|<br>\|Kencur\|6 bulan\|<br>\|Buah merah\|3 tahun\|<br>\|Kemangi\|30 hari\|<br><br>e. Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?

| Opsi | Isi |
|---|---|
| A | Kencur 6 kali dan lengkuas 2 kali |
| B | Kencur 2 kali dan lengkuas 2 kali |
| C | Kencur 6 kali dan lengkuas 3 kali |
| D | Kencur 2 kali dan lengkuas 6 kali |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Konversi semua satuan ke bulan: Buah merah = 3 tahun = 36 bulan. Kencur = 6 bulan, maka 36/6 = 6 kali panen. Lengkuas = 1,5 tahun = 18 bulan, maka 36/18 = 2 kali panen.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ec7b848375815a09ffe77d1bfef6a8f01fc5c3d1389978d2e6e7dc115c7b235b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 1896 |
| 2 | success | valid / verified | applying | conceptual | Medium | 1925 |
| 3 | success | valid / verified | applying | conceptual | Medium | 1870 |

Run 1 — solusi: Konversi semua satuan ke bulan: Buah merah = 3 tahun = 36 bulan. Kencur = 6 bulan, maka 36/6 = 6 kali panen. Lengkuas = 1,5 tahun = 18 bulan, maka 36/18 = 2 kali panen.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi satuan waktu yang berbeda, melakukan konversi ke satuan yang sama (bulan), dan menerapkan konsep rasio/pembagian untuk membandingkan masa panen.. Bukti: Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut pemahaman prosedural tentang konversi satuan waktu dan penggunaan rasio untuk membandingkan dua kuantitas.. Bukti: Tabel 2.7 Masa Panen Tanaman Obat Khas Daerah
- Intended difficulty `classify/Medium`: Soal memerlukan konversi satuan waktu yang berbeda (tahun ke bulan) dan pembagian sederhana. Ini adalah prosedur rutin yang melibatkan beberapa langkah terkait.. Bukti: Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konversi satuan waktu (tahun ke bulan) dan konsep dasar rasio/pembagian. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu melakukan konversi satuan waktu dan membandingkan nilai, yang merupakan bagian dari kurikulum rasio dan perbandingan. |

Run 2 — solusi: Konversi semua satuan ke bulan: Buah merah = 3 tahun = 36 bulan. Kencur = 6 bulan. Lengkuas = 1,5 tahun = 18 bulan. Frekuensi panen kencur = 36 / 6 = 6 kali. Frekuensi panen lengkuas = 36 / 18 = 2 kali.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur yang tepat (konversi satuan waktu) dan menerapkan rasio untuk membandingkan masa panen, yang merupakan penerapan konsep dalam situasi rutin.. Bukti: Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antar satuan waktu (tahun, bulan) dan prinsip perbandingan/rasio untuk menyelesaikan masalah.. Bukti: Tabel 2.7 Masa Panen Tanaman Obat Khas Daerah; Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?
- Intended difficulty `classify/Medium`: Soal memerlukan konversi satuan waktu yang konsisten sebelum melakukan pembagian sederhana. Ini adalah tugas rutin dengan beberapa langkah yang saling terkait.. Bukti: Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konversi satuan waktu (tahun ke bulan) dan konsep dasar rasio/pembagian. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu mengelola konversi satuan waktu sederhana dan melakukan perbandingan rasio dalam konteks kehidupan sehari-hari. |

Run 3 — solusi: Konversi semua satuan ke bulan: Buah merah = 3 tahun = 36 bulan. Kencur = 6 bulan, maka 36/6 = 6 kali. Lengkuas = 1,5 tahun = 18 bulan, maka 36/18 = 2 kali.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur konversi satuan waktu yang tepat dan menerapkan rasio untuk membandingkan masa panen, yang merupakan penerapan konsep rutin.. Bukti: Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antar satuan waktu (tahun, bulan) dan prinsip rasio dalam konteks praktis.. Bukti: Tabel 2.7 Masa Panen Tanaman Obat Khas Daerah
- Intended difficulty `classify/Medium`: Soal memerlukan konversi satuan yang konsisten sebelum melakukan pembagian rasio. Ini adalah langkah rutin yang umum di kelas 7.. Bukti: Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konversi satuan waktu (tahun ke bulan) dan konsep dasar rasio/pembagian. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu mengonversi satuan waktu dan membandingkan nilai menggunakan rasio atau pembagian sederhana. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3395`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi satuan waktu yang berbeda, melakukan konversi ke satuan yang sama (bulan), dan menerapkan konsep pembagian untuk membandingkan masa panen. Ini adalah penerapan prosedur rutin.
- Dimensi pengetahuan `procedural`: Soal ini menuntut pemahaman prosedural tentang konversi satuan waktu dan penggunaan rasio/pembagian untuk membandingkan dua kuantitas.
- Intended difficulty `Medium`: Soal memerlukan konversi satuan waktu yang berbeda (tahun ke bulan) dan pembagian sederhana. Ini adalah prosedur rutin yang melibatkan beberapa langkah terkait.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konversi satuan waktu (tahun ke bulan) dan konsep dasar pembagian/rasio. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu melakukan konversi satuan waktu dan membandingkan nilai, yang merupakan bagian dari kurikulum rasio dan perbandingan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Penerapan Rasio
Tipe soal: multiple_choice
Stimulus: -
Soal: Lalu, Ayah menjelaskan kepada Tigor mengenai waktu panen beberapa tanaman obat seperti pada Tabel 2.7 berikut.

Tabel 2.7 Masa Panen Tanaman Obat Khas Daerah

|Nama Tanaman Obat|Masa Panen|
|---|---|
|Kumis kucing|12 minggu|
|Lengkuas|1,5 tahun|
|Jahe merah|3 bulan|
|Kencur|6 bulan|
|Buah merah|3 tahun|
|Kemangi|30 hari|

e. Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?
Pilihan: A. Kencur 6 kali dan lengkuas 2 kali
B. Kencur 2 kali dan lengkuas 2 kali
C. Kencur 6 kali dan lengkuas 3 kali
D. Kencur 2 kali dan lengkuas 6 kali
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 23. Soal `766f6782bf6694906b2cdedf`

Total harga tiket yang dibayar oleh Rahmat dapat dinyatakan dalam bentuk aljabar 3a + 2b. Jika variabel a menyatakan harga satuan tiket anak-anak dan variabel b menyatakan harga satuan tiket untuk orang dewasa.<br><br>c. Jika harga satuan tiket anak-anak adalah Rp20.000,00 dan harga satuan tiket untuk orang dewasa adalah Rp30.000,00, berapa total harga tiket yang perlu dibayar oleh Rahmat dan keluarganya untuk berlibur ke taman bermain ini?

| Opsi | Isi |
|---|---|
| A | Rp150.000,00 |
| B | Rp120.000,00 |
| C | Rp100.000,00 |
| D | Rp50.000,00 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Substitusi nilai a=20.000 dan b=30.000 ke dalam bentuk aljabar 3a + 2b menghasilkan 3(20.000) + 2(30.000) = 60.000 + 60.000 = 120.000.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0b58ef5243fb8a994cbc98c82760026c252da773b920f3e9d65cff1c17f443cc`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1981 |
| 2 | success | valid / verified | applying | procedural | Easy | 1962 |
| 3 | success | valid / verified | applying | procedural | Easy | 1910 |

Run 1 — solusi: Substitusi nilai a=20.000 dan b=30.000 ke dalam bentuk aljabar 3a + 2b menghasilkan 3(20.000) + 2(30.000) = 60.000 + 60.000 = 120.000.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan prosedur substitusi nilai ke dalam bentuk aljabar yang sudah diberikan untuk menyelesaikan masalah rutin.. Bukti: dapat dinyatakan dalam bentuk aljabar 3a + 2b; Jika harga satuan tiket anak-anak adalah Rp20.000,00 dan harga satuan tiket untuk orang dewasa adalah Rp30.000,00
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana variabel dalam bentuk aljabar mewakili kuantitas dan bagaimana melakukan operasi aritmatika setelah substitusi.. Bukti: dapat dinyatakan dalam bentuk aljabar 3a + 2b
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu melakukan substitusi nilai ke dalam variabel yang sudah didefinisikan dan melakukan operasi aritmatika dasar.. Bukti: 3a + 2b; harga satuan tiket anak-anak adalah Rp20.000,00; harga satuan tiket untuk orang dewasa adalah Rp30.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel dalam aljabar dan operasi aritmatika (perkalian dan penjumlahan). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena merupakan penerapan langsung dari konsep variabel aljabar yang baru dipelajari. |

Run 2 — solusi: Substitusi nilai a = 20.000 dan b = 30.000 ke dalam bentuk aljabar 3a + 2b menghasilkan 3(20.000) + 2(30.000) = 60.000 + 60.000 = 120.000.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan prosedur substitusi nilai ke dalam bentuk aljabar yang sudah diberikan untuk mendapatkan hasil numerik.. Bukti: dapat dinyatakan dalam bentuk aljabar 3a + 2b; Jika harga satuan tiket anak-anak adalah Rp20.000,00 dan harga satuan tiket untuk orang dewasa adalah Rp30.000,00
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana variabel dalam bentuk aljabar merepresentasikan nilai dan bagaimana melakukan operasi aritmatika setelah substitusi.. Bukti: bentuk aljabar 3a + 2b
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena hanya memerlukan substitusi langsung ke dalam rumus yang sudah tersedia tanpa perlu memodelkan masalah sendiri atau melakukan manipulasi aljabar yang kompleks.. Bukti: 3a + 2b; a = 20.000; b = 30.000

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi hitung bilangan bulat dan pemahaman dasar substitusi variabel. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena merupakan aplikasi langsung dari konsep variabel dan substitusi yang menjadi dasar aljabar di jenjang ini. |

Run 3 — solusi: Substitusi nilai ke dalam bentuk aljabar: 3(20.000) + 2(30.000) = 60.000 + 60.000 = 120.000.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan nilai yang diketahui ke dalam bentuk aljabar yang sudah diberikan. Ini adalah proses rutin dalam menerapkan konsep substitusi variabel.. Bukti: dapat dinyatakan dalam bentuk aljabar 3a + 2b; Jika harga satuan tiket anak-anak adalah Rp20.000,00 dan harga satuan tiket untuk orang dewasa adalah Rp30.000,00
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana variabel dalam bentuk aljabar merepresentasikan nilai kuantitas tertentu dan bagaimana melakukan operasi substitusi.. Bukti: dapat dinyatakan dalam bentuk aljabar 3a + 2b
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena siswa hanya perlu melakukan substitusi langsung ke dalam rumus yang sudah disediakan tanpa perlu memodelkan masalah sendiri.. Bukti: 3a + 2b; harga satuan tiket anak-anak adalah Rp20.000,00; harga satuan tiket untuk orang dewasa adalah Rp30.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel aljabar dan operasi hitung bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena melibatkan substitusi langsung pada ekspresi aljabar sederhana yang merupakan materi dasar aljabar. |

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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Unsur-Unsur Bentuk Aljabar
Tipe soal: multiple_choice
Stimulus: -
Soal: Total harga tiket yang dibayar oleh Rahmat dapat dinyatakan dalam bentuk aljabar 3a + 2b. Jika variabel a menyatakan harga satuan tiket anak-anak dan variabel b menyatakan harga satuan tiket untuk orang dewasa.

c. Jika harga satuan tiket anak-anak adalah Rp20.000,00 dan harga satuan tiket untuk orang dewasa adalah Rp30.000,00, berapa total harga tiket yang perlu dibayar oleh Rahmat dan keluarganya untuk berlibur ke taman bermain ini?
Pilihan: A. Rp150.000,00
B. Rp120.000,00
C. Rp100.000,00
D. Rp50.000,00
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 24. Soal `b949ca87abb896c3d1f62669`

Tentukan suku-suku, koefisien, variabel, dan konstanta yang ada pada masing-masing bentuk aljabar berikut ini.<br><br>a. 2x + 1

| Opsi | Isi |
|---|---|
| A | Suku: 2 dan x + 1; koefisien = 1; konstanta = 2 |
| B | Suku: 2x dan 1; koefisien x = 2; konstanta = 1 |
| C | Suku: 2x + 1 (satu suku); koefisien x = 2; konstanta = 0 |
| D | Suku: 2x dan 1; koefisien x = 1; konstanta = 2 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Bentuk aljabar 2x + 1 terdiri dari dua suku yang dipisahkan oleh tanda tambah, yaitu 2x dan 1. Pada suku 2x, angka 2 adalah koefisien dari variabel x. Angka 1 adalah konstanta karena tidak memiliki variabel.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `928f710b08f3cf4ac8911758414af0b1d4fb4d0335e14ba326dd2f233cdf18a1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 1821 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 1830 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 1821 |

Run 1 — solusi: Bentuk aljabar 2x + 1 terdiri dari dua suku yang dipisahkan oleh tanda tambah, yaitu 2x dan 1. Pada suku 2x, angka 2 adalah koefisien dari variabel x. Angka 1 adalah konstanta karena tidak memiliki variabel.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengidentifikasi komponen dasar dari bentuk aljabar, yang merupakan proses pengenalan dan penerapan definisi istilah aljabar secara langsung.. Bukti: Tentukan suku-suku, koefisien, variabel, dan konstanta yang ada pada masing-masing bentuk aljabar berikut ini.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami definisi dan hubungan antara istilah-istilah dalam aljabar (suku, koefisien, variabel, konstanta) untuk mengklasifikasikan bagian-bagian dari ekspresi 2x + 1.. Bukti: Tentukan suku-suku, koefisien, variabel, dan konstanta
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural dasar dengan ekspresi linear sederhana. Tidak ada manipulasi kompleks atau strategi nonrutin yang diperlukan.. Bukti: 2x + 1

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang definisi suku, koefisien, variabel, dan konstanta dalam aljabar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 sebagai pengenalan awal terhadap unsur-unsur aljabar. |

Run 2 — solusi: Bentuk aljabar 2x + 1 terdiri dari dua suku yang dipisahkan oleh tanda tambah, yaitu 2x dan 1. Pada suku 2x, angka 2 adalah koefisien dari variabel x. Angka 1 adalah konstanta karena tidak memiliki variabel.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi komponen dasar dari bentuk aljabar, yang merupakan proses pengenalan dan penerapan definisi dasar aljabar.. Bukti: Tentukan suku-suku, koefisien, variabel, dan konstanta yang ada pada masing-masing bentuk aljabar berikut ini.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami definisi dan hubungan antara istilah-istilah dalam aljabar (suku, koefisien, variabel, konstanta) untuk mengklasifikasikan bagian-bagian dari ekspresi tersebut.. Bukti: Tentukan suku-suku, koefisien, variabel, dan konstanta
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya melibatkan satu ekspresi linear sederhana dengan dua suku. Siswa hanya perlu menerapkan definisi istilah aljabar secara langsung.. Bukti: 2x + 1

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang definisi suku, koefisien, variabel, dan konstanta dalam aljabar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah materi pengenalan aljabar kelas 7 yang bersifat prosedural dasar dan familiar. |

Run 3 — solusi: Bentuk aljabar 2x + 1 terdiri dari dua suku yang dipisahkan oleh tanda tambah, yaitu 2x dan 1. Pada suku 2x, angka 2 adalah koefisien dari variabel x. Angka 1 adalah konstanta karena tidak memiliki variabel.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengidentifikasi komponen dasar dari bentuk aljabar, yang merupakan proses pengenalan dan penerapan definisi istilah aljabar secara langsung.. Bukti: Tentukan suku-suku, koefisien, variabel, dan konstanta yang ada pada masing-masing bentuk aljabar berikut ini.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami definisi konseptual dari istilah-istilah aljabar (suku, koefisien, variabel, konstanta) untuk dapat mengklasifikasikan bagian-bagian dari ekspresi tersebut.. Bukti: Tentukan suku-suku, koefisien, variabel, dan konstanta
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, hanya melibatkan identifikasi komponen dasar pada ekspresi linear sederhana dengan satu variabel.. Bukti: 2x + 1

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang definisi suku, koefisien, variabel, dan konstanta dalam aljabar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah materi pengenalan aljabar kelas 7 yang sangat mendasar, tidak memerlukan manipulasi atau pemecahan masalah kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Unsur-Unsur Bentuk Aljabar
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan suku-suku, koefisien, variabel, dan konstanta yang ada pada masing-masing bentuk aljabar berikut ini.

a. 2x + 1
Pilihan: A. Suku: 2 dan x + 1; koefisien = 1; konstanta = 2
B. Suku: 2x dan 1; koefisien x = 2; konstanta = 1
C. Suku: 2x + 1 (satu suku); koefisien x = 2; konstanta = 0
D. Suku: 2x dan 1; koefisien x = 1; konstanta = 2
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 25. Soal `ae1333250b514b1217d3fe7b`

Tentukan setiap bentuk aljabar berikut dalam bentuk jabaran.<br><br>d. (x + 1)(x + 3)

| Opsi | Isi |
|---|---|
| A | x² + x + 3 |
| B | x² + 3x + 3 |
| C | x² + 4x + 3 |
| D | x² + 4x + 4 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: (x + 1)(x + 3) = x(x) + x(3) + 1(x) + 1(3) = x² + 3x + x + 3 = x² + 4x + 3
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fb9f9c38b6ee23328e395e8854d900b7728cb742e97f7f7a8aead39c05877ace`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1730 |
| 2 | success | valid / verified | applying | procedural | Easy | 1744 |
| 3 | success | valid / verified | applying | procedural | Easy | 1747 |

Run 1 — solusi: (x + 1)(x + 3) = x(x) + x(3) + 1(x) + 1(3) = x² + 3x + x + 3 = x² + 4x + 3
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur distributif (FOIL) untuk mengalikan dua binomial. Ini adalah penerapan langsung dari prosedur aljabar yang dipelajari di kelas 7.. Bukti: Tentukan setiap bentuk aljabar berikut dalam bentuk jabaran.; (x + 1)(x + 3)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma perkalian suku dua (binomial) yang merupakan prosedur standar dalam aljabar.. Bukti: (x + 1)(x + 3)
- Intended difficulty `classify/Easy`: Soal ini merupakan latihan rutin perkalian binomial yang umum di kelas 7. Prosedur yang digunakan bersifat langsung dan familiar bagi siswa.. Bukti: (x + 1)(x + 3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel, penjumlahan suku sejenis, dan sifat distributif perkalian. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Perkalian bentuk aljabar (x+a)(x+b) adalah materi standar kelas 7 yang diajarkan sebagai prosedur rutin. |

Run 2 — solusi: (x + 1)(x + 3) = x(x) + x(3) + 1(x) + 1(3) = x² + 3x + x + 3 = x² + 4x + 3
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur distributif (FOIL) untuk mengalikan dua binomial. Ini adalah penerapan prosedur standar yang sudah dipelajari di kelas 7.. Bukti: Tentukan setiap bentuk aljabar berikut dalam bentuk jabaran.; (x + 1)(x + 3)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma perkalian suku dua (distributif) yang merupakan prosedur standar dalam aljabar.. Bukti: (x + 1)(x + 3)
- Intended difficulty `classify/Easy`: Soal ini merupakan latihan rutin perkalian binomial dengan koefisien positif sederhana. Siswa hanya perlu menerapkan aturan distributif secara langsung tanpa kendala kompleks.. Bukti: (x + 1)(x + 3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel dan operasi perkalian distributif. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Perkalian bentuk aljabar (x+a)(x+b) adalah materi standar kelas 7 yang bersifat prosedural rutin. |

Run 3 — solusi: (x + 1)(x + 3) = x(x) + x(3) + 1(x) + 1(3) = x² + 3x + x + 3 = x² + 4x + 3
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur distributif (FOIL) untuk mengalikan dua binomial. Ini adalah penerapan algoritma standar yang sudah dipelajari.. Bukti: Tentukan setiap bentuk aljabar berikut dalam bentuk jabaran. d. (x + 1)(x + 3)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman dan penerapan algoritma perkalian suku dua (distributif), yang merupakan prosedur standar dalam aljabar.. Bukti: (x + 1)(x + 3)
- Intended difficulty `classify/Easy`: Soal ini merupakan latihan rutin perkalian binomial dengan koefisien positif sederhana. Siswa hanya perlu melakukan langkah distributif standar tanpa kendala kompleks.. Bukti: (x + 1)(x + 3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel, penjumlahan suku sejenis, dan sifat distributif perkalian. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Perkalian binomial adalah materi standar kelas 7. Soal ini tidak memiliki jebakan atau kompleksitas tambahan, sehingga termasuk kategori mudah. |

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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Sifat-Sifat dan Operasi Aljabar
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan setiap bentuk aljabar berikut dalam bentuk jabaran.

d. (x + 1)(x + 3)
Pilihan: A. x² + x + 3
B. x² + 3x + 3
C. x² + 4x + 3
D. x² + 4x + 4
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 26. Soal `7989c67f978347b7bdc238ad`

Tentukan setiap bentuk aljabar berikut dalam bentuk faktor.<br><br>a. 5x + 10

| Opsi | Isi |
|---|---|
| A | x(5 + 2) |
| B | 5(x + 5) |
| C | 5(x + 10) |
| D | 5(x + 2) |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: FPB dari 5 dan 10 adalah 5. Maka, 5x + 10 = 5(x) + 5(2) = 5(x + 2).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e6f523cc21f0ed045996d5431cb4462bee5d6af33620811ae4a941f88b3bc177`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1677 |
| 2 | success | valid / verified | applying | procedural | Easy | 1672 |
| 3 | success | valid / verified | applying | procedural | Easy | 1695 |

Run 1 — solusi: FPB dari 5 dan 10 adalah 5. Maka, 5x + 10 = 5(x) + 5(2) = 5(x + 2).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pemfaktoran aljabar dasar (distributif) yang merupakan prosedur rutin dalam kurikulum kelas 7.. Bukti: Tentukan setiap bentuk aljabar berikut dalam bentuk faktor; 5x + 10
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pemfaktoran (distributif) yang merupakan teknik prosedural standar.. Bukti: 5x + 10; bentuk faktor
- Intended difficulty `classify/Easy`: Soal ini melibatkan satu langkah rutin (mencari FPB dari koefisien dan konstanta) dengan angka yang sederhana, sehingga beban kognitifnya rendah.. Bukti: 5x + 10

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang FPB dan sifat distributif perkalian terhadap penjumlahan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pemfaktoran bentuk linear sederhana adalah materi dasar aljabar kelas 7 yang bersifat rutin. |

Run 2 — solusi: FPB dari 5x dan 10 adalah 5. Maka, 5x + 10 = 5(x) + 5(2) = 5(x + 2).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur faktorisasi aljabar dasar (distributif) yang merupakan prosedur rutin dalam aljabar kelas 7.. Bukti: Tentukan setiap bentuk aljabar berikut dalam bentuk faktor.; 5x + 10
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma faktorisasi (FPB) dan sifat distributif aljabar.. Bukti: 5x + 10; bentuk faktor
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin, hanya melibatkan satu langkah faktorisasi langsung dengan FPB sederhana, cocok untuk tingkat kesulitan rendah.. Bukti: 5x + 10

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang FPB bilangan bulat dan konsep variabel aljabar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Faktorisasi bentuk linear sederhana adalah materi standar kelas 7 yang bersifat prosedural langsung. |

Run 3 — solusi: FPB dari 5 dan 10 adalah 5. Maka, 5x + 10 = 5(x) + 5(2) = 5(x + 2).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur faktorisasi aljabar dasar (distributif terbalik) yang merupakan prosedur rutin dalam aljabar kelas 7.. Bukti: Tentukan setiap bentuk aljabar berikut dalam bentuk faktor; 5x + 10
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma faktorisasi aljabar, yaitu mencari FPB dari suku-suku dan menerapkan sifat distributif.. Bukti: 5x + 10; bentuk faktor
- Intended difficulty `classify/Easy`: Soal ini melibatkan satu langkah rutin (mencari FPB dari koefisien dan konstanta) tanpa kendala tambahan atau variabel kompleks.. Bukti: 5x + 10

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep FPB bilangan bulat dan sifat distributif perkalian terhadap penjumlahan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Faktorisasi bentuk linear sederhana adalah materi dasar aljabar kelas 7 yang bersifat prosedural langsung. |

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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Sifat-Sifat dan Operasi Aljabar
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan setiap bentuk aljabar berikut dalam bentuk faktor.

a. 5x + 10
Pilihan: A. x(5 + 2)
B. 5(x + 5)
C. 5(x + 10)
D. 5(x + 2)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 27. Soal `bb5563c106a35bce8aef90f0`

Panitia OSIS menjual tiket untuk konser musik yang merupakan acara tahunan sekolah. Rani menjual a tiket. Bagas menjual 3 kali dari tiket yang dijual oleh Rani. Cakra menjual 4 tiket lebih sedikit dari tiket yang dijual oleh Rani. Malik menjual 10 tiket lebih banyak dari Rani. Berapa bentuk aljabar dari banyak tiket yang dijual oleh Bagas, Cakra, dan Malik. Berapa bentuk aljabar dari total tiket yang terjual oleh Rani, Bagas, Cakra, dan Malik. Jika ada 10 tiket yang tidak terjual, berapa bentuk aljabar dari banyak tiket secara keseluruhan.<br><br> Jika tiket yang dijual oleh Rani sebanyak 12 tiket. Berapa banyak tiket secara keseluruhan?

| Opsi | Isi |
|---|---|
| A | 88 tiket |
| B | 76 tiket |
| C | 78 tiket |
| D | 92 tiket |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Bagas=3a, Cakra=a-4, Malik=a+10. Total terjual = a + 3a + (a-4) + (a+10) = 6a + 6. Total keseluruhan = (6a+6) + 10 = 6a + 16. Untuk a=12, 6(12)+16 = 72+16 = 88.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung', 'membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4eefa0e9b619f51fe0b53bd99233d7923015159889bd5110367fb5c60b3d0c01`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2021 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2019 |
| 3 | success | valid / verified | applying | procedural | Medium | 2028 |

Run 1 — solusi: Bagas=3a, Cakra=a-4, Malik=a+10. Total terjual = a + 3a + (a-4) + (a+10) = 6a + 6. Total keseluruhan (terjual + 10 tidak terjual) = 6a + 6 + 10 = 6a + 16. Untuk a=12, total = 6(12) + 16 = 72 + 16 = 88.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan narasi ke dalam ekspresi aljabar, menyederhanakan suku sejenis, dan melakukan substitusi nilai, yang merupakan penerapan prosedur rutin dalam konteks pemodelan.. Bukti: Berapa bentuk aljabar dari banyak tiket yang dijual oleh Bagas, Cakra, dan Malik.; Berapa bentuk aljabar dari total tiket yang terjual; Jika ada 10 tiket yang tidak terjual, berapa bentuk aljabar dari banyak tiket secara keseluruhan.
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman tentang struktur ekspresi aljabar dan bagaimana variabel serta konstanta merepresentasikan hubungan kuantitatif.. Bukti: Berapa bentuk aljabar dari banyak tiket yang dijual oleh Bagas, Cakra, dan Malik.; Berapa bentuk aljabar dari total tiket yang terjual
- Intended difficulty `classify/Medium`: Soal melibatkan beberapa langkah rutin (pemodelan, penyederhanaan, substitusi) yang saling terkait namun prosedurnya standar untuk kelas 7.. Bukti: Rani menjual a tiket. Bagas menjual 3 kali dari tiket yang dijual oleh Rani. Cakra menjual 4 tiket lebih sedikit dari tiket yang dijual oleh Rani. Malik menjual 10 tiket lebih banyak dari Rani.; Jika tiket yang dijual oleh Rani sebanyak 12 tiket. Berapa banyak tiket secara keseluruhan?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aljabar dasar, penyederhanaan suku sejenis, substitusi nilai ke variabel. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 3 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena menggabungkan pemodelan aljabar sederhana dengan aritmatika dasar. |

Run 2 — solusi: Bagas=3a, Cakra=a-4, Malik=a+10. Total terjual = a + 3a + (a-4) + (a+10) = 6a + 6. Total keseluruhan (terjual + 10 tidak terjual) = 6a + 6 + 10 = 6a + 16. Untuk a=12, 6(12)+16 = 72+16 = 88.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan pernyataan verbal ke dalam bentuk aljabar dan melakukan operasi penjumlahan suku sejenis, yang merupakan penerapan prosedur rutin pada situasi pemodelan.. Bukti: Berapa bentuk aljabar dari banyak tiket yang dijual oleh Bagas, Cakra, dan Malik.; Berapa bentuk aljabar dari total tiket yang terjual oleh Rani, Bagas, Cakra, dan Malik.
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman tentang struktur ekspresi aljabar dan bagaimana menggabungkan variabel serta konstanta untuk merepresentasikan situasi nyata.. Bukti: Berapa bentuk aljabar dari total tiket yang terjual oleh Rani, Bagas, Cakra, dan Malik.; Jika ada 10 tiket yang tidak terjual, berapa bentuk aljabar dari banyak tiket secara keseluruhan.
- Intended difficulty `classify/Medium`: Soal melibatkan beberapa langkah rutin (pemodelan individu, penjumlahan total, substitusi nilai) yang saling terkait namun prosedurnya sangat standar untuk kelas 7.. Bukti: Rani menjual a tiket. Bagas menjual 3 kali dari tiket yang dijual oleh Rani. Cakra menjual 4 tiket lebih sedikit dari tiket yang dijual oleh Rani. Malik menjual 10 tiket lebih banyak dari Rani.; Jika tiket yang dijual oleh Rani sebanyak 12 tiket. Berapa banyak tiket secara keseluruhan?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aljabar dasar (penjumlahan suku sejenis) dan substitusi nilai ke dalam variabel. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 5 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena menggabungkan pemodelan aljabar dasar dengan konteks cerita yang memerlukan ketelitian dalam menjumlahkan suku sejenis. |

Run 3 — solusi: Bagas=3a, Cakra=a-4, Malik=a+10. Total terjual = a + 3a + (a-4) + (a+10) = 6a + 6. Total keseluruhan = (6a+6) + 10 = 6a + 16. Untuk a=12, 6(12)+16 = 72+16 = 88.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan narasi ke dalam ekspresi aljabar dan melakukan operasi penjumlahan suku sejenis, yang merupakan penerapan prosedur rutin.. Bukti: Berapa bentuk aljabar dari banyak tiket yang dijual oleh Bagas, Cakra, dan Malik.; Berapa bentuk aljabar dari total tiket yang terjual; berapa bentuk aljabar dari banyak tiket secara keseluruhan.
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman tentang bagaimana variabel dan konstanta merepresentasikan kuantitas dalam konteks cerita dan manipulasi aljabar dasar.. Bukti: Berapa bentuk aljabar dari banyak tiket yang dijual oleh Bagas, Cakra, dan Malik.; Berapa bentuk aljabar dari total tiket yang terjual
- Intended difficulty `classify/Medium`: Soal melibatkan beberapa langkah rutin (pemodelan tiap individu, penjumlahan total, penambahan konstanta) yang saling terkait namun prosedurnya standar untuk kelas 7.. Bukti: Rani menjual a tiket. Bagas menjual 3 kali dari tiket yang dijual oleh Rani. Cakra menjual 4 tiket lebih sedikit dari tiket yang dijual oleh Rani. Malik menjual 10 tiket lebih banyak dari Rani.; Jika ada 10 tiket yang tidak terjual, berapa bentuk aljabar dari banyak tiket secara keseluruhan.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aljabar dasar (penjumlahan/pengurangan suku sejenis) dan penerjemahan kalimat ke model matematika. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 5 |
| interactingConstraints | 3 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena menguji kemampuan pemodelan aljabar dasar dengan konteks yang terstruktur. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3962`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerjemahkan narasi ke dalam ekspresi aljabar, menyederhanakan suku sejenis, dan melakukan substitusi nilai. Ini adalah penerapan prosedur rutin dalam konteks pemodelan aljabar.
- Dimensi pengetahuan `conceptual`: Soal menuntut pemahaman tentang struktur ekspresi aljabar dan bagaimana variabel serta konstanta merepresentasikan hubungan kuantitatif dalam situasi nyata.
- Intended difficulty `Medium`: Soal melibatkan beberapa langkah rutin (pemodelan individu, penjumlahan total, penambahan konstanta, substitusi) yang saling terkait. Prosedurnya standar untuk kelas 7, namun memerlukan ketelitian dalam mengelola beberapa variabel dan konstanta.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aljabar dasar, penyederhanaan suku sejenis, substitusi nilai ke variabel. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 3 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena menggabungkan pemodelan aljabar sederhana dengan aritmatika dasar dalam konteks cerita. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Pemodelan dengan Bentuk Aljabar
Tipe soal: multiple_choice
Stimulus: -
Soal: Panitia OSIS menjual tiket untuk konser musik yang merupakan acara tahunan sekolah. Rani menjual a tiket. Bagas menjual 3 kali dari tiket yang dijual oleh Rani. Cakra menjual 4 tiket lebih sedikit dari tiket yang dijual oleh Rani. Malik menjual 10 tiket lebih banyak dari Rani. Berapa bentuk aljabar dari banyak tiket yang dijual oleh Bagas, Cakra, dan Malik. Berapa bentuk aljabar dari total tiket yang terjual oleh Rani, Bagas, Cakra, dan Malik. Jika ada 10 tiket yang tidak terjual, berapa bentuk aljabar dari banyak tiket secara keseluruhan.

 Jika tiket yang dijual oleh Rani sebanyak 12 tiket. Berapa banyak tiket secara keseluruhan?
Pilihan: A. 88 tiket
B. 76 tiket
C. 78 tiket
D. 92 tiket
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 28. Soal `ecd4f81cd1eef14f2bfa1a79`

Arief membeli y buah apel. Tentukan bentuk aljabar dari banyak buah apel dari setiap situasi berikut. a. Nyoman mempunyai buah apel 5 kali lebih banyak dari Arief. b. Arief memakan 2 buah apel. c. Nyoman membuat jus apel menggunakan 4 buah apel. d. Total buah apel yang dimiliki oleh Arief dan Nyoman.<br><br>b. Arief memakan 2 buah apel.

| Opsi | Isi |
|---|---|
| A | y − 2 |
| B | 2 − y |
| C | y + 2 |
| D | 2y |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Arief memiliki y apel. Memakan 2 apel berarti mengurangi jumlah apel sebanyak 2, sehingga bentuk aljabarnya adalah y - 2.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['mengidentifikasi', 'membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5891cd22f768424650ce50d5edc92fa488590568533bd4f43603a84ba946400b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1682 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1675 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1669 |

Run 1 — solusi: Arief memiliki y apel. Memakan 2 apel berarti mengurangi jumlah apel sebanyak 2, sehingga bentuk aljabarnya adalah y - 2.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan situasi verbal ke dalam ekspresi aljabar sederhana. Ini adalah proses menerapkan konsep operasi dasar pada variabel, yang termasuk dalam domain applying.. Bukti: Arief membeli y buah apel; Arief memakan 2 buah apel
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang bagaimana operasi aritmatika (pengurangan) direpresentasikan dalam bentuk aljabar, yang merupakan pemahaman konseptual tentang variabel dan operasi.. Bukti: bentuk aljabar dari banyak buah apel
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya melibatkan satu operasi pengurangan dasar pada variabel tunggal. Tidak ada langkah kompleks atau kendala yang saling terkait.. Bukti: Arief membeli y buah apel; Arief memakan 2 buah apel

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel sebagai representasi bilangan dan operasi pengurangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 sebagai pengenalan awal pemodelan aljabar sederhana. |

Run 2 — solusi: Arief memiliki y buah apel. Jika ia memakan 2 buah, maka jumlah apelnya berkurang 2, sehingga bentuk aljabarnya adalah y - 2.
- Domain kognitif `classify/applying`: Siswa diminta menerjemahkan situasi verbal sederhana ke dalam bentuk aljabar satu langkah, yang merupakan proses applying konsep dasar aljabar.. Bukti: Arief memakan 2 buah apel
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang bagaimana operasi aritmatika (pengurangan) direpresentasikan dalam bentuk aljabar (konseptual).. Bukti: bentuk aljabar dari banyak buah apel
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya memerlukan satu operasi pengurangan dasar pada variabel tunggal, sehingga tergolong mudah bagi siswa kelas 7.. Bukti: Arief memakan 2 buah apel

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel dan operasi pengurangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah pengenalan standar untuk pemodelan aljabar di kelas 7, di mana siswa belajar menerjemahkan kata-kata menjadi ekspresi matematika sederhana. |

Run 3 — solusi: Arief memiliki y apel. Jika ia memakan 2 apel, maka jumlah apelnya berkurang 2, sehingga bentuk aljabarnya adalah y - 2.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan situasi verbal ke dalam ekspresi aljabar sederhana. Ini adalah proses menerapkan konsep operasi pengurangan pada variabel, yang merupakan prosedur rutin.. Bukti: Arief membeli y buah apel; Arief memakan 2 buah apel
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang bagaimana operasi aritmatika (pengurangan) direpresentasikan dalam bentuk aljabar.. Bukti: bentuk aljabar dari banyak buah apel
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya melibatkan satu operasi pengurangan dasar pada variabel tunggal. Tidak ada langkah kompleks atau jebakan yang signifikan.. Bukti: Arief membeli y buah apel; Arief memakan 2 buah apel

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel dan operasi pengurangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 sebagai pengenalan awal pemodelan aljabar satu langkah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Pemodelan dengan Bentuk Aljabar
Tipe soal: multiple_choice
Stimulus: -
Soal: Arief membeli y buah apel. Tentukan bentuk aljabar dari banyak buah apel dari setiap situasi berikut. a. Nyoman mempunyai buah apel 5 kali lebih banyak dari Arief. b. Arief memakan 2 buah apel. c. Nyoman membuat jus apel menggunakan 4 buah apel. d. Total buah apel yang dimiliki oleh Arief dan Nyoman.

b. Arief memakan 2 buah apel.
Pilihan: A. y − 2
B. 2 − y
C. y + 2
D. 2y
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 29. Soal `9895ee7997313791a586a5d6`

Pada dua garis yang berpotongan, terdapat sudut yang bertolak belakang, sedangkan pada dua garis sejajar yang berpotongan dengan garis lain, dikenal istilah sehadap, dalam berseberangan, luar berseberangan, dalam sepihak, luar sepihak.<br><br>Hubungan mana yang masih berlaku jika kedua garis tidak sejajar?

| Opsi | Isi |
|---|---|
| A | Dalam sepihak |
| B | Sehadap |
| C | Bertolak belakang |
| D | Dalam berseberangan |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Sudut bertolak belakang terbentuk oleh dua garis yang berpotongan di satu titik. Sifat ini selalu berlaku pada setiap dua garis yang berpotongan, terlepas dari apakah garis tersebut sejajar atau tidak. Sebaliknya, hubungan sudut sehadap, berseberangan, dan sepihak memerlukan syarat garis sejajar agar memiliki sifat besar sudut yang tetap.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menganalisis']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d065160a347a6023afffd9ef46bd75e58a55cd64ca14a21ca8a0fcfae4aa40b4`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1752 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1761 |
| 3 | success | valid / verified | applying | conceptual | Medium | 1770 |

Run 1 — solusi: Sudut bertolak belakang terbentuk oleh dua garis yang berpotongan di satu titik. Sifat ini tidak memerlukan syarat garis sejajar, berbeda dengan sudut sehadap, berseberangan, atau sepihak yang memerlukan garis sejajar agar memiliki hubungan besar sudut yang tetap.
- Domain kognitif `classify/applying`: Soal ini menguji pemahaman konseptual tentang syarat keberlakuan hubungan antar sudut. Siswa harus membedakan antara hubungan yang bergantung pada sifat kesejajaran (sehadap, berseberangan, sepihak) dan yang tidak (bertolak belakang).. Bukti: Hubungan mana yang masih berlaku jika kedua garis tidak sejajar?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip dan struktur hubungan antar sudut untuk menentukan mana yang tetap berlaku tanpa syarat garis sejajar.. Bukti: terdapat sudut yang bertolak belakang; dikenal istilah sehadap, dalam berseberangan, luar berseberangan, dalam sepihak, luar sepihak
- Intended difficulty `classify/Easy`: Soal ini bersifat konseptual dan memerlukan pemahaman tentang definisi sudut. Tidak ada perhitungan rumit, hanya pemilihan konsep yang tepat.. Bukti: Hubungan mana yang masih berlaku jika kedua garis tidak sejajar?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi sudut bertolak belakang dan syarat garis sejajar untuk sudut sehadap/berseberangan/sepihak. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 mempelajari hubungan antar sudut. Membedakan syarat keberlakuan hubungan sudut adalah materi dasar yang rutin dalam topik ini. |

Run 2 — solusi: Sudut bertolak belakang terbentuk dari dua garis yang berpotongan di satu titik. Sifat ini tidak memerlukan syarat garis sejajar, berbeda dengan sudut sehadap, berseberangan, atau sepihak yang memerlukan garis sejajar sebagai syarat utama agar memiliki hubungan besar sudut yang tetap.
- Domain kognitif `classify/applying`: Soal ini menguji pemahaman konseptual tentang syarat berlakunya hubungan antar sudut. Siswa harus membedakan antara sifat sudut yang bergantung pada kesejajaran garis dan sifat yang hanya bergantung pada perpotongan dua garis.. Bukti: Hubungan mana yang masih berlaku jika kedua garis tidak sejajar?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami struktur dan prinsip dasar hubungan antar sudut (konsep) untuk menentukan mana yang tetap berlaku tanpa syarat tambahan (kesejajaran).. Bukti: terdapat sudut yang bertolak belakang; dikenal istilah sehadap, dalam berseberangan, luar berseberangan, dalam sepihak, luar sepihak
- Intended difficulty `classify/Easy`: Soal ini bersifat konseptual dan memerlukan pemahaman tentang definisi dasar sudut. Tidak ada perhitungan rumit, hanya pemilihan konsep yang tepat.. Bukti: Hubungan mana yang masih berlaku jika kedua garis tidak sejajar?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi sudut bertolak belakang dan syarat garis sejajar pada sudut sehadap/berseberangan/sepihak. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi hubungan antar sudut adalah topik standar kelas 7. Soal ini menguji pemahaman definisi tanpa memerlukan manipulasi aljabar atau perhitungan numerik. |

Run 3 — solusi: Sudut bertolak belakang terbentuk oleh dua garis yang berpotongan di satu titik, sehingga besar sudutnya selalu sama tanpa memerlukan syarat garis sejajar. Hubungan sudut lainnya (sehadap, berseberangan, sepihak) memerlukan syarat garis sejajar agar memiliki sifat khusus (sama besar atau berpelurus).
- Domain kognitif `classify/applying`: Soal ini menguji pemahaman konseptual tentang syarat keberlakuan hubungan antar sudut. Siswa harus membedakan sifat sudut yang inheren pada perpotongan garis (bertolak belakang) dengan sifat sudut yang bergantung pada kesejajaran garis.. Bukti: Hubungan mana yang masih berlaku jika kedua garis tidak sejajar?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip atau struktur konsep hubungan antar sudut untuk menentukan mana yang tetap berlaku tanpa syarat tambahan (kesejajaran).. Bukti: Hubungan mana yang masih berlaku jika kedua garis tidak sejajar?
- Intended difficulty `classify/Medium`: Soal ini bersifat konseptual dan memerlukan pemahaman tentang definisi hubungan sudut. Tidak ada perhitungan, namun siswa harus mengidentifikasi syarat mutlak dari hubungan sudut tersebut.. Bukti: Hubungan mana yang masih berlaku jika kedua garis tidak sejajar?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi sudut bertolak belakang dan hubungan sudut pada garis sejajar. |
| dependentSteps | 1 |
| routineStatus | routine_selection |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 baru mempelajari hubungan antar sudut. Membedakan syarat keberlakuan hubungan sudut (sejajar vs tidak sejajar) adalah tantangan konseptual yang sesuai untuk tingkat ini. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 2, "Medium": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3259`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Soal ini menguji pemahaman konseptual tentang syarat keberlakuan hubungan antar sudut. Siswa harus membedakan antara hubungan yang inheren pada perpotongan dua garis (bertolak belakang) dengan hubungan yang bergantung pada sifat kesejajaran garis (sehadap, berseberangan, sepihak).
- Dimensi pengetahuan `conceptual`: Siswa perlu memahami prinsip dan struktur konsep hubungan antar sudut untuk menentukan mana yang tetap berlaku tanpa syarat tambahan (kesejajaran).
- Intended difficulty `Easy`: Soal ini bersifat konseptual dan memerlukan pemahaman tentang definisi dasar sudut. Tidak ada perhitungan rumit, hanya pemilihan konsep yang tepat.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi sudut bertolak belakang dan syarat garis sejajar untuk sudut sehadap/berseberangan/sepihak. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi hubungan antar sudut adalah topik standar kelas 7. Soal ini menguji pemahaman definisi tanpa memerlukan manipulasi aljabar atau perhitungan numerik. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Hubungan Antar Sudut
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada dua garis yang berpotongan, terdapat sudut yang bertolak belakang, sedangkan pada dua garis sejajar yang berpotongan dengan garis lain, dikenal istilah sehadap, dalam berseberangan, luar berseberangan, dalam sepihak, luar sepihak.

Hubungan mana yang masih berlaku jika kedua garis tidak sejajar?
Pilihan: A. Dalam sepihak
B. Sehadap
C. Bertolak belakang
D. Dalam berseberangan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 30. Soal `4d6693103dbd451e67e5be49`

Gambar berikut menunjukkan dua pasang garis sejajar. Salah satu sudut diketahui besarnya.<br><br>Bangun apakah yang ditunjukkan oleh segi empat $ABCD$? Jelaskan.

| Opsi | Isi |
|---|---|
| A | Jajargenjang, karena kedua pasang sisi yang berhadapan sejajar |
| B | Layang-layang, karena dua pasang sisi yang berdekatan sama panjang |
| C | Trapesium, karena hanya sepasang sisi yang sejajar |
| D | Persegi panjang, karena semua sudutnya siku-siku |

![Gambar sumber soal 30](<../images/kelas7_crop-p0192-jajargenjang.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Definisi jajargenjang adalah segi empat dengan dua pasang sisi yang berhadapan sejajar. Gambar menunjukkan AB ∥ DC dan AD ∥ BC, sehingga ABCD adalah jajargenjang.
Gambar sumber: images/kelas7_crop-p0192-jajargenjang.png. Transkripsi visual: Gambar menunjukkan segi empat ABCD yang dibentuk oleh dua pasang garis sejajar. Pasangan garis AB dan DC memiliki tanda panah ganda (∥), sedangkan pasangan garis AD dan BC memiliki tanda panah tunggal (∥). Sudut di titik A (∠DAB) ditandai sebesar 130°.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1f115af403f964e1a7f276a1f0e391afe3e2997ad3b08b7739ee68942071e42b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2907 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2932 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2899 |

Run 1 — solusi: Definisi jajargenjang adalah segi empat dengan dua pasang sisi yang berhadapan sejajar. Gambar menunjukkan AB ∥ DC dan AD ∥ BC, sehingga ABCD adalah jajargenjang.
- Domain kognitif `classify/applying`: Siswa perlu mengenali definisi jajargenjang berdasarkan properti geometris yang diberikan (dua pasang sisi sejajar) dan mengaitkannya dengan konsep bangun datar.. Bukti: Bangun apakah yang ditunjukkan oleh segi empat ABCD?; Gambar menunjukkan dua pasang garis sejajar.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang klasifikasi bangun datar berdasarkan sifat-sifat geometris (kesejajaran sisi).. Bukti: Bangun apakah yang ditunjukkan oleh segi empat ABCD?; dua pasang garis sejajar
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 7 yang telah mempelajari sifat-sifat bangun datar. Identifikasi langsung dari tanda kesejajaran pada gambar membuat tugas ini cukup sederhana.. Bukti: Gambar menunjukkan dua pasang garis sejajar.; Bangun apakah yang ditunjukkan oleh segi empat ABCD?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi jajargenjang dan pemahaman notasi garis sejajar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah familiar dengan klasifikasi segi empat berdasarkan sifat sisinya. Soal ini hanya memerlukan pengenalan visual terhadap tanda kesejajaran. |

Run 2 — solusi: Definisi jajargenjang adalah segi empat dengan dua pasang sisi yang berhadapan sejajar. Gambar menunjukkan sisi AB sejajar dengan DC (tanda panah ganda) dan sisi AD sejajar dengan BC (tanda panah tunggal). Oleh karena itu, ABCD adalah jajargenjang.
- Domain kognitif `classify/applying`: Siswa perlu mengenali definisi jajargenjang berdasarkan properti geometris (dua pasang sisi sejajar) yang diberikan secara visual pada gambar.. Bukti: Bangun apakah yang ditunjukkan oleh segi empat ABCD?; dua pasang garis sejajar
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang klasifikasi bangun datar berdasarkan sifat-sifat geometris (kesejajaran sisi).. Bukti: dua pasang garis sejajar; Bangun apakah yang ditunjukkan oleh segi empat ABCD?
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 7 yang mempelajari geometri. Siswa hanya perlu mengidentifikasi properti yang sudah diberikan secara eksplisit pada gambar (tanda kesejajaran) dan mencocokkannya dengan definisi jajargenjang.. Bukti: dua pasang garis sejajar; Bangun apakah yang ditunjukkan oleh segi empat ABCD?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi jajargenjang dan pemahaman simbol kesejajaran pada garis. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah mempelajari sifat-sifat bangun datar dan simbol garis sejajar. Soal ini adalah aplikasi langsung dari definisi tersebut. |

Run 3 — solusi: Definisi jajargenjang adalah segi empat dengan dua pasang sisi yang berhadapan sejajar. Gambar menunjukkan AB sejajar DC (tanda panah ganda) dan AD sejajar BC (tanda panah tunggal). Karena kedua pasang sisi berhadapan sejajar, maka ABCD adalah jajargenjang.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi sifat bangun datar berdasarkan informasi visual tentang kesejajaran sisi, yang merupakan penerapan konsep dasar geometri.. Bukti: dua pasang garis sejajar; Bangun apakah yang ditunjukkan oleh segi empat ABCD?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi jajargenjang berdasarkan sifat kesejajaran sisi.. Bukti: dua pasang garis sejajar; Bangun apakah yang ditunjukkan oleh segi empat ABCD?
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 7 yang mempelajari geometri. Siswa hanya perlu mengenali tanda kesejajaran pada gambar dan menghubungkannya dengan definisi jajargenjang.. Bukti: dua pasang garis sejajar; Bangun apakah yang ditunjukkan oleh segi empat ABCD?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi jajargenjang dan pemahaman simbol garis sejajar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengenali bangun datar dari tanda kesejajaran adalah materi dasar geometri kelas 7. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Hubungan Antar Sudut
Tipe soal: multiple_choice
Stimulus: -
Soal: Gambar berikut menunjukkan dua pasang garis sejajar. Salah satu sudut diketahui besarnya.

Bangun apakah yang ditunjukkan oleh segi empat $ABCD$? Jelaskan.
Pilihan: A. Jajargenjang, karena kedua pasang sisi yang berhadapan sejajar
B. Layang-layang, karena dua pasang sisi yang berdekatan sama panjang
C. Trapesium, karena hanya sepasang sisi yang sejajar
D. Persegi panjang, karena semua sudutnya siku-siku
Transkripsi visual: Gambar menunjukkan segi empat ABCD yang dibentuk oleh dua pasang garis sejajar. Pasangan garis AB dan DC memiliki tanda panah ganda (∥), sedangkan pasangan garis AD dan BC memiliki tanda panah tunggal (∥). Sudut di titik A (∠DAB) ditandai sebesar 130°.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 31. Soal `23226cc89d29478865192e2a`

Secara elektronik, memperbesar dan memperkecil gambar dapat dilakukan dengan memanfaatkan fitur zoom in dan zoom out. Bangun datar yang dihasilkan melalui proses tersebut memiliki sifat sebangun dengan bangun datar awal. Berdasarkan pernyataan tersebut, apa perbedaan antara bangun datar awal dan bangun datar hasil perbesaran atau pengecilan?.

| Opsi | Isi |
|---|---|
| A | Hanya bentuk secara umum |
| B | Panjang garis, keliling, dan luas |
| C | Besar sudut dan bentuk secara umum |
| D | Panjang garis dan besar sudut |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Dua bangun yang sebangun memiliki bentuk yang sama (sudut-sudut yang bersesuaian sama besar), namun ukuran linear (panjang sisi, keliling) dan luasnya berubah secara proporsional sesuai faktor skala.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1988fb8354ec2394c64305bef04c42a63a89144086134978d65a65c6b098e076`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1717 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1725 |
| 3 | success | valid / verified | applying | conceptual | Medium | 1756 |

Run 1 — solusi: Dua bangun yang sebangun memiliki bentuk yang sama (sudut-sudut yang bersesuaian sama besar), namun ukuran linear (panjang sisi, keliling) dan luasnya berubah secara proporsional sesuai faktor skala.
- Domain kognitif `classify/applying`: Soal ini menguji pemahaman konseptual tentang sifat-sifat kesebangunan. Siswa perlu membedakan antara properti yang invarian (bentuk, besar sudut) dan properti yang berubah (panjang sisi, keliling, luas) saat dilatasi.. Bukti: Bangun datar yang dihasilkan melalui proses tersebut memiliki sifat sebangun dengan bangun datar awal.
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami prinsip dasar kesebangunan (dilatasi) yang menghubungkan perubahan ukuran dengan tetap terjaganya bentuk dan sudut.. Bukti: apa perbedaan antara bangun datar awal dan bangun datar hasil perbesaran atau pengecilan?
- Intended difficulty `classify/Easy`: Soal ini bersifat konseptual dan tidak memerlukan perhitungan numerik yang kompleks. Siswa hanya perlu memahami definisi kesebangunan secara intuitif, yang merupakan materi dasar kelas 7.. Bukti: apa perbedaan antara bangun datar awal dan bangun datar hasil perbesaran atau pengecilan?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep perbesaran/pengecilan gambar (dilatasi) dan sifat bangun sebangun. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kesebangunan di kelas 7 umumnya diperkenalkan melalui konteks perbesaran gambar/skala, sehingga pertanyaan ini berada pada tingkat kesulitan yang sesuai untuk pemahaman awal. |

Run 2 — solusi: Dua bangun datar dikatakan sebangun jika memiliki bentuk yang sama namun ukuran yang berbeda. Dalam proses zoom (perbesaran/pengecilan), panjang sisi, keliling, dan luas bangun berubah secara proporsional, sedangkan besar sudut tetap sama.
- Domain kognitif `classify/applying`: Soal ini menuntut pemahaman konseptual tentang sifat-sifat bangun datar yang sebangun. Siswa harus membedakan antara properti yang berubah (ukuran) dan yang tetap (bentuk/sudut) dalam transformasi kesebangunan.. Bukti: Bangun datar yang dihasilkan melalui proses tersebut memiliki sifat sebangun dengan bangun datar awal.; apa perbedaan antara bangun datar awal dan bangun datar hasil perbesaran atau pengecilan?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang prinsip atau definisi kesebangunan, yaitu hubungan antara ukuran linear/luas dengan bentuk bangun datar.. Bukti: sifat sebangun dengan bangun datar awal
- Intended difficulty `classify/Easy`: Soal ini bersifat konseptual dan tidak memerlukan perhitungan numerik yang kompleks. Siswa hanya perlu memahami definisi kesebangunan secara intuitif.. Bukti: apa perbedaan antara bangun datar awal dan bangun datar hasil perbesaran atau pengecilan?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep perbesaran/pengecilan gambar dan sifat kesebangunan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konsep kesebangunan adalah materi standar kelas 7. Soal ini menguji pemahaman dasar tanpa beban komputasi, sehingga sesuai untuk tingkat kesulitan rendah. |

Run 3 — solusi: Dua bangun datar dikatakan sebangun jika memiliki bentuk yang sama namun ukuran yang berbeda. Dalam proses zoom (perbesaran/pengecilan), panjang sisi, keliling, dan luas bangun berubah secara proporsional, sedangkan besar sudut tetap sama.
- Domain kognitif `classify/applying`: Soal ini menguji pemahaman konseptual tentang sifat dasar kesebangunan. Siswa perlu memahami definisi sebangun (bentuk sama, ukuran berbeda) untuk membedakan properti yang berubah (panjang, keliling, luas) dan yang tetap (sudut).. Bukti: Bangun datar yang dihasilkan melalui proses tersebut memiliki sifat sebangun dengan bangun datar awal.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman tentang hubungan dan prinsip-prinsip geometris yang mendasari konsep kesebangunan, bukan sekadar menghafal fakta atau melakukan prosedur perhitungan.. Bukti: apa perbedaan antara bangun datar awal dan bangun datar hasil perbesaran atau pengecilan?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus memahami konsep kesebangunan secara utuh dan membedakan properti invarian (sudut) dengan properti varian (panjang sisi/luas) dalam transformasi geometri, yang merupakan langkah penalaran konseptual rutin dalam materi kesebangunan kelas 7.. Bukti: apa perbedaan antara bangun datar awal dan bangun datar hasil perbesaran atau pengecilan?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk bangun datar dan konsep perbesaran/pengecilan (dilatasi sederhana). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konsep kesebangunan adalah materi standar kelas 7. Membedakan properti yang berubah dan tetap pada dilatasi adalah pemahaman inti yang diharapkan pada jenjang ini. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 2, "Medium": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4125`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan pemahaman konseptual tentang sifat-sifat kesebangunan untuk membedakan properti yang berubah (ukuran) dan yang tetap (bentuk/sudut) saat dilatasi.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman tentang prinsip atau definisi kesebangunan, yaitu hubungan antara ukuran linear/luas dengan bentuk bangun datar.
- Intended difficulty `Easy`: Soal ini bersifat konseptual dan tidak memerlukan perhitungan numerik yang kompleks. Siswa hanya perlu memahami definisi kesebangunan secara intuitif, yang merupakan materi dasar kelas 7.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep perbesaran/pengecilan gambar (dilatasi) dan sifat bangun sebangun. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kesebangunan di kelas 7 umumnya diperkenalkan melalui konteks perbesaran gambar/skala, sehingga pertanyaan ini berada pada tingkat kesulitan yang sesuai untuk pemahaman awal. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Arti Kesebangunan
Tipe soal: multiple_choice
Stimulus: -
Soal: Secara elektronik, memperbesar dan memperkecil gambar dapat dilakukan dengan memanfaatkan fitur zoom in dan zoom out. Bangun datar yang dihasilkan melalui proses tersebut memiliki sifat sebangun dengan bangun datar awal. Berdasarkan pernyataan tersebut, apa perbedaan antara bangun datar awal dan bangun datar hasil perbesaran atau pengecilan?.
Pilihan: A. Hanya bentuk secara umum
B. Panjang garis, keliling, dan luas
C. Besar sudut dan bentuk secara umum
D. Panjang garis dan besar sudut
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 32. Soal `ee6b087d7e2980c7460df17f`

Cermin manakah yang menghasilkan bayangan yang sebangun dengan benda asalnya?

| Opsi | Isi |
|---|---|
| A | Tidak ada cermin yang menghasilkan bayangan sebangun |
| B | Cermin b |
| C | Cermin a |
| D | Cermin c |

![Gambar sumber soal 32](<../images/kelas7_crop-p0196-cermin.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Dua objek dikatakan sebangun jika memiliki bentuk yang sama dan perbandingan ukuran yang proporsional. Pada cermin 'a', bayangan memiliki bentuk dan proporsi yang identik dengan objek asli, sedangkan cermin 'b' dan 'c' menghasilkan distorsi yang mengubah proporsi objek.
Gambar sumber: images/kelas7_crop-p0196-cermin.png. Transkripsi visual: Terdapat tiga gambar cermin (a, b, c) yang menampilkan bayangan orang. Pada cermin 'a', bayangan orang memiliki proporsi tubuh yang sama dengan orang aslinya. Pada cermin 'b', bayangan orang tampak lebih kurus dan memanjang (terdistorsi). Pada cermin 'c', bayangan orang tampak lebih lebar atau berubah proporsinya dibandingkan orang aslinya.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b25fe26f29f86755d55bbd0ac014504cdb92f3e640f9a2a85f94e1d740080b55`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2874 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2875 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2870 |

Run 1 — solusi: Dua objek dikatakan sebangun jika memiliki bentuk yang sama dan perbandingan ukuran yang proporsional. Pada cermin 'a', bayangan memiliki bentuk dan proporsi yang identik dengan objek asli, sedangkan cermin 'b' dan 'c' menghasilkan distorsi yang mengubah proporsi objek.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep dasar kesebangunan (bentuk sama, proporsi sama) dan menerapkannya untuk mengidentifikasi visualisasi yang sesuai. Ini adalah penerapan konsep pada situasi visual.. Bukti: Cermin manakah yang menghasilkan bayangan yang sebangun dengan benda asalnya?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip atau definisi kesebangunan (konsep) daripada sekadar menghafal fakta atau melakukan prosedur perhitungan.. Bukti: Cermin manakah yang menghasilkan bayangan yang sebangun dengan benda asalnya?
- Intended difficulty `classify/Easy`: Soal ini bersifat intuitif dan langsung. Siswa hanya perlu membandingkan bentuk visual secara kualitatif tanpa perhitungan kompleks atau strategi nonrutin.. Bukti: Cermin manakah yang menghasilkan bayangan yang sebangun dengan benda asalnya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk dan proporsi (kesebangunan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena menguji konsep dasar kesebangunan melalui pengamatan visual, yang merupakan pengenalan awal topik tersebut. |

Run 2 — solusi: Dua objek dikatakan sebangun jika memiliki bentuk yang sama dan perbandingan ukuran yang proporsional. Pada cermin 'a', bayangan orang memiliki bentuk dan proporsi yang sama persis dengan orang aslinya, sedangkan cermin 'b' dan 'c' menghasilkan distorsi yang mengubah proporsi tubuh, sehingga tidak sebangun.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengidentifikasi konsep kesebangunan (bentuk sama, proporsi sama) melalui pengamatan visual langsung tanpa perhitungan numerik.. Bukti: Cermin manakah yang menghasilkan bayangan yang sebangun dengan benda asalnya?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami definisi konseptual dari kesebangunan (mempertahankan bentuk dan proporsi) untuk membedakan antara bayangan yang sebangun dan yang terdistorsi.. Bukti: Cermin manakah yang menghasilkan bayangan yang sebangun dengan benda asalnya?
- Intended difficulty `classify/Easy`: Soal ini bersifat intuitif dan langsung. Siswa hanya perlu mengenali karakteristik visual dari kesebangunan tanpa melakukan langkah perhitungan atau strategi kompleks.. Bukti: Cermin manakah yang menghasilkan bayangan yang sebangun dengan benda asalnya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep kesebangunan (bentuk dan proporsi). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sangat sesuai untuk kelas 7 sebagai pengenalan awal konsep kesebangunan melalui pengamatan visual, tidak memerlukan manipulasi aljabar atau geometri formal. |

Run 3 — solusi: Kesebangunan mensyaratkan bentuk dan proporsi yang sama antara benda asli dan bayangan. Cermin 'a' adalah satu-satunya yang menghasilkan bayangan dengan proporsi yang identik dengan benda aslinya, sedangkan cermin 'b' dan 'c' menghasilkan distorsi yang mengubah proporsi.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep dasar kesebangunan (mempertahankan bentuk dan proporsi) dan menerapkannya untuk mengidentifikasi gambar mana yang memenuhi kriteria tersebut melalui pengamatan visual.. Bukti: Cermin manakah yang menghasilkan bayangan yang sebangun dengan benda asalnya?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang apa arti 'sebangun' dalam konteks geometri visual, bukan sekadar menghafal definisi atau melakukan prosedur perhitungan.. Bukti: Cermin manakah yang menghasilkan bayangan yang sebangun dengan benda asalnya?
- Intended difficulty `classify/Easy`: Soal ini bersifat intuitif dan langsung. Siswa hanya perlu membandingkan proporsi visual antara objek asli dan bayangan tanpa perlu melakukan perhitungan atau strategi kompleks.. Bukti: Cermin manakah yang menghasilkan bayangan yang sebangun dengan benda asalnya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman intuitif tentang bentuk dan proporsi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 sebagai pengenalan konsep kesebangunan melalui observasi visual sebelum masuk ke perhitungan rasio yang lebih formal. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4307`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Soal ini menguji pemahaman konseptual tentang kesebangunan (bentuk dan proporsi yang sama) melalui pengamatan visual. Siswa perlu menerapkan definisi kesebangunan untuk mengidentifikasi gambar yang sesuai.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman tentang prinsip atau definisi kesebangunan (konsep) daripada sekadar menghafal fakta atau melakukan prosedur perhitungan.
- Intended difficulty `Easy`: Soal ini bersifat intuitif dan langsung. Siswa hanya perlu membandingkan bentuk visual secara kualitatif tanpa perhitungan kompleks atau strategi nonrutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk dan proporsi (kesebangunan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena menguji konsep dasar kesebangunan melalui pengamatan visual, yang merupakan pengenalan awal topik tersebut. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Arti Kesebangunan
Tipe soal: multiple_choice
Stimulus: -
Soal: Cermin manakah yang menghasilkan bayangan yang sebangun dengan benda asalnya?
Pilihan: A. Tidak ada cermin yang menghasilkan bayangan sebangun
B. Cermin b
C. Cermin a
D. Cermin c
Transkripsi visual: Terdapat tiga gambar cermin (a, b, c) yang menampilkan bayangan orang. Pada cermin 'a', bayangan orang memiliki proporsi tubuh yang sama dengan orang aslinya. Pada cermin 'b', bayangan orang tampak lebih kurus dan memanjang (terdistorsi). Pada cermin 'c', bayangan orang tampak lebih lebar atau berubah proporsinya dibandingkan orang aslinya.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 33. Soal `78652b4108bd747c96b2f4a8`

Pada $\triangle ABC$, $AD$ membagi $\angle A$ menjadi dua bagian yang sama besar. $AD$ disebut garis bagi. Titik $D$ terletak pada sisi $BC$. Petunjuk: Hitung garis yang sejajar dengan $AD$ dan melalui titik $C$. Garis ini berpotongan dengan perpanjangan $AB$ di titik $E$.<br><br> $\triangle ACE$ sama kaki. Manakah sisi-sisi yang sama panjang.

| Opsi | Isi |
|---|---|
| A | AC = AE, karena ∠ACE = ∠AEC |
| B | AE = CE, karena ∠ACE = ∠CAE |
| C | AC = CE, karena ∠CAE = ∠AEC |
| D | AB = AC, karena AD garis bagi |

![Gambar sumber soal 33](<../images/kelas7_crop-p0205-garis-bagi.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Karena CE sejajar AD, maka sudut AEC = sudut BAD (sehadap) dan sudut ACE = sudut DAC (berseberangan dalam). Karena AD adalah garis bagi, sudut BAD = sudut DAC. Maka sudut AEC = sudut ACE. Segitiga ACE memiliki dua sudut alas yang sama, sehingga AC = AE.
Gambar sumber: images/kelas7_crop-p0205-garis-bagi.png. Transkripsi visual: Segitiga ABC dengan garis bagi AD yang membagi sudut A menjadi dua bagian sama besar. Titik D terletak pada sisi BC.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `81184601cb374313817072b192915f639737f5285d9473e0f1418414115a29a1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Hard | 3001 |
| 2 | success | valid / verified | reasoning | conceptual | Hard | 3043 |
| 3 | success | valid / verified | reasoning | conceptual | Hard | 3086 |

Run 1 — solusi: Karena CE sejajar AD, maka sudut AEC = sudut BAD (sehadap) dan sudut ACE = sudut DAC (berseberangan dalam). Karena AD adalah garis bagi, sudut BAD = sudut DAC. Maka sudut AEC = sudut ACE. Segitiga ACE memiliki dua sudut alas yang sama, sehingga AC = AE.
- Domain kognitif `classify/reasoning`: Siswa perlu mengintegrasikan konsep garis sejajar (sudut sehadap dan berseberangan) dengan sifat segitiga sama kaki untuk menyimpulkan hubungan sisi. Ini melampaui sekadar mengingat definisi.. Bukti: Hitung garis yang sejajar dengan AD dan melalui titik C; Garis ini berpotongan dengan perpanjangan AB di titik E; Manakah sisi-sisi yang sama panjang
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman konseptual tentang hubungan sudut pada garis sejajar dan sifat segitiga sama kaki, bukan sekadar prosedur rutin.. Bukti: AD membagi ∠A menjadi dua bagian yang sama besar; Garis yang sejajar dengan AD dan melalui titik C
- Intended difficulty `classify/Hard`: Soal ini memerlukan konstruksi mental atau visualisasi tambahan (garis bantu) dan penerapan teorema sudut pada garis sejajar secara bertahap. Ini bukan prosedur rutin bagi siswa kelas 7.. Bukti: Hitung garis yang sejajar dengan AD dan melalui titik C; Garis ini berpotongan dengan perpanjangan AB di titik E; ΔACE sama kaki

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat sudut pada garis sejajar (sehadap, berseberangan), definisi garis bagi, sifat segitiga sama kaki. |
| dependentSteps | 4 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 3 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun topiknya dasar, menuntut siswa melakukan konstruksi garis bantu dan menghubungkan beberapa teorema geometri secara deduktif adalah tantangan tinggi untuk kelas 7. |

Run 2 — solusi: Karena CE sejajar AD, maka sudut AEC = sudut BAD (sehadap) dan sudut ACE = sudut DAC (berseberangan dalam). Karena AD adalah garis bagi, sudut BAD = sudut DAC. Maka sudut AEC = sudut ACE. Segitiga ACE adalah segitiga sama kaki dengan AC = AE.
- Domain kognitif `classify/reasoning`: Soal ini menuntut siswa untuk mengintegrasikan konsep garis sejajar (sudut sehadap dan berseberangan) dengan sifat garis bagi segitiga untuk menyimpulkan sifat segitiga sama kaki. Ini melibatkan penalaran geometris, bukan sekadar ingatan atau prosedur rutin.. Bukti: Hitung garis yang sejajar dengan AD dan melalui titik C; Garis ini berpotongan dengan perpanjangan AB di titik E; Manakah sisi-sisi yang sama panjang
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara konsep garis sejajar, sudut-sudut yang terbentuk (sehadap, berseberangan), dan definisi segitiga sama kaki untuk memecahkan masalah ini.. Bukti: AD membagi ∠A menjadi dua bagian yang sama besar; Garis yang sejajar dengan AD dan melalui titik C
- Intended difficulty `classify/Hard`: Soal ini dikategorikan Hard untuk kelas 7 karena memerlukan konstruksi mental (atau visualisasi) garis bantu, pemahaman mendalam tentang hubungan sudut pada garis sejajar, dan kemampuan mengintegrasikan beberapa properti geometris untuk menarik kesimpulan.. Bukti: Hitung garis yang sejajar dengan AD dan melalui titik C; Garis ini berpotongan dengan perpanjangan AB di titik E; ΔACE sama kaki

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat sudut pada garis sejajar (sehadap, berseberangan), definisi garis bagi, dan syarat segitiga sama kaki. |
| dependentSteps | 4 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 3 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun topiknya geometri, tuntutan untuk melakukan konstruksi garis bantu dan menghubungkan beberapa teorema sudut secara deduktif berada di atas rata-rata kemampuan rutin siswa kelas 7. |

Run 3 — solusi: Karena CE sejajar AD, maka sudut AEC = sudut BAD (sehadap) dan sudut ACE = sudut DAC (berseberangan dalam). Karena AD adalah garis bagi, sudut BAD = sudut DAC. Maka sudut AEC = sudut ACE. Segitiga ACE adalah segitiga sama kaki dengan AC = AE.
- Domain kognitif `classify/reasoning`: Soal ini memerlukan siswa untuk melakukan konstruksi mental atau visualisasi berdasarkan petunjuk, mengidentifikasi hubungan sudut (sehadap dan berseberangan dalam) akibat garis sejajar, dan menyimpulkan sifat segitiga sama kaki. Ini melampaui sekadar mengingat fakta atau prosedur rutin.. Bukti: Hitung garis yang sejajar dengan AD dan melalui titik C; Garis ini berpotongan dengan perpanjangan AB di titik E; Manakah sisi-sisi yang sama panjang
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami prinsip-prinsip geometri tentang garis sejajar, sudut-sudut yang terbentuk (sehadap, berseberangan), dan definisi segitiga sama kaki berdasarkan kesamaan sudut alas.. Bukti: AD membagi ∠A menjadi dua bagian yang sama besar; Garis yang sejajar dengan AD; ∠ACE = ∠AEC
- Intended difficulty `classify/Hard`: Soal ini dikategorikan Hard untuk kelas 7 karena melibatkan konstruksi tambahan (garis sejajar) yang tidak ada pada gambar awal, serta integrasi beberapa konsep geometri (garis sejajar, sudut, segitiga sama kaki) yang memerlukan penalaran deduktif, bukan sekadar aplikasi rumus langsung.. Bukti: Petunjuk: Hitung garis yang sejajar dengan AD dan melalui titik C; Garis ini berpotongan dengan perpanjangan AB di titik E; ∠ACE = ∠AEC

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat sudut pada garis sejajar (sehadap, berseberangan dalam), definisi garis bagi, dan sifat segitiga sama kaki. |
| dependentSteps | 4 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 3 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun topiknya geometri, konstruksi garis bantu dan pembuktian deduktif seperti ini jarang ditemui di kurikulum kelas 7 standar yang biasanya lebih fokus pada perhitungan atau pengenalan sifat dasar, sehingga ini menantang bagi level tersebut. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 3} | unanimous_3_0 / unanimous | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Hard": 3} | unanimous_3_0 / unanimous | Hard |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Kesebangunan pada Segitiga
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada $\triangle ABC$, $AD$ membagi $\angle A$ menjadi dua bagian yang sama besar. $AD$ disebut garis bagi. Titik $D$ terletak pada sisi $BC$. Petunjuk: Hitung garis yang sejajar dengan $AD$ dan melalui titik $C$. Garis ini berpotongan dengan perpanjangan $AB$ di titik $E$.

 $\triangle ACE$ sama kaki. Manakah sisi-sisi yang sama panjang.
Pilihan: A. AC = AE, karena ∠ACE = ∠AEC
B. AE = CE, karena ∠ACE = ∠CAE
C. AC = CE, karena ∠CAE = ∠AEC
D. AB = AC, karena AD garis bagi
Transkripsi visual: Segitiga ABC dengan garis bagi AD yang membagi sudut A menjadi dua bagian sama besar. Titik D terletak pada sisi BC.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Hard"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "reasoning", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Hard", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 34. Soal `6b6ef03baec242dd387e76aa`

Perhatikan $\triangle ABC$ berikut. Titik $D$ terletak pada $AB$. Jika $E$ terletak pada $AC$, hitunglah $\triangle ADE$ yang sebangun dengan $\triangle ABC$. $\triangle ABC \sim \triangle ADE$<br><br>Pada dua segitiga yang sebangun, sudut-sudut yang berpadanan besarnya ....

| Opsi | Isi |
|---|---|
| A | berbeda |
| B | dua kali lipat |
| C | berjumlah 90° |
| D | sama |

![Gambar sumber soal 34](<../images/kelas7_crop-p0201-segitiga-abc-d.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Definisi kesebangunan dua bangun datar menyatakan bahwa bangun-bangun tersebut memiliki bentuk yang sama, yang berarti sudut-sudut yang berpadanan besarnya sama, meskipun panjang sisi-sisinya mungkin berbeda (proporsional).
Gambar sumber: images/kelas7_crop-p0201-segitiga-abc-d.png. Transkripsi visual: Gambar menunjukkan segitiga ABC dengan titik D terletak pada segmen garis AB. Tidak ada titik E yang digambarkan secara eksplisit pada AC, namun teks soal menyatakan hubungan kesebangunan antara segitiga ABC dan segitiga ADE.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `86378674d4bada95240f36de56addbdf9c93c731efc7e1a88a1b5a452bc96e38`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2869 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2878 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2876 |

Run 1 — solusi: Definisi kesebangunan dua bangun datar menyatakan bahwa bangun-bangun tersebut memiliki bentuk yang sama, yang berarti sudut-sudut yang berpadanan besarnya sama, meskipun panjang sisi-sisinya mungkin berbeda (proporsional).
- Domain kognitif `classify/knowing`: Soal ini menanyakan definisi atau sifat dasar dari kesebangunan segitiga. Siswa hanya perlu mengingat atau mengenali konsep dasar bahwa kesebangunan mempertahankan besar sudut.. Bukti: Pada dua segitiga yang sebangun, sudut-sudut yang berpadanan besarnya ....
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman terhadap konsep atau prinsip dasar kesebangunan, bukan sekadar fakta hafalan tanpa makna atau prosedur perhitungan.. Bukti: Pada dua segitiga yang sebangun, sudut-sudut yang berpadanan besarnya ....
- Intended difficulty `classify/Easy`: Soal ini sangat langsung dan menguji pemahaman definisi dasar. Tidak ada perhitungan atau langkah kompleks yang diperlukan.. Bukti: Pada dua segitiga yang sebangun, sudut-sudut yang berpadanan besarnya ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang definisi kesebangunan segitiga. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah pertanyaan konseptual dasar yang sesuai untuk kelas 7 saat mempelajari topik kesebangunan. |

Run 2 — solusi: Definisi kesebangunan segitiga menyatakan bahwa dua segitiga dikatakan sebangun jika sudut-sudut yang bersesuaian sama besar dan sisi-sisi yang bersesuaian memiliki perbandingan yang sama. Oleh karena itu, sudut-sudut yang berpadanan pada segitiga yang sebangun adalah sama besar.
- Domain kognitif `classify/knowing`: Soal ini menanyakan definisi dasar atau sifat fundamental dari kesebangunan segitiga. Siswa hanya perlu mengingat atau mengenali konsep dasar tanpa melakukan perhitungan atau strategi kompleks.. Bukti: Pada dua segitiga yang sebangun, sudut-sudut yang berpadanan besarnya ....
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip atau definisi kesebangunan, yang merupakan bagian dari pengetahuan konseptual.. Bukti: Pada dua segitiga yang sebangun, sudut-sudut yang berpadanan besarnya ....
- Intended difficulty `classify/Easy`: Soal ini bersifat sangat langsung, hanya menanyakan pemahaman definisi dasar tanpa memerlukan langkah-langkah prosedural atau analisis mendalam.. Bukti: Pada dua segitiga yang sebangun, sudut-sudut yang berpadanan besarnya ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi kesebangunan segitiga. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah pertanyaan teoretis dasar yang sesuai untuk kelas 7 saat mempelajari topik kesebangunan. |

Run 3 — solusi: Definisi kesebangunan dua bangun datar menyatakan bahwa sudut-sudut yang berpadanan pada kedua bangun tersebut adalah sama besar, sedangkan sisi-sisi yang berpadanan memiliki perbandingan yang senilai.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengingat atau mengenali definisi dasar dari kesebangunan segitiga, yaitu kesamaan besar sudut-sudut yang berpadanan.. Bukti: Pada dua segitiga yang sebangun, sudut-sudut yang berpadanan besarnya ....
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman terhadap konsep atau prinsip dasar kesebangunan, bukan sekadar fakta hafalan tanpa makna, karena berkaitan dengan sifat geometris.. Bukti: Pada dua segitiga yang sebangun, sudut-sudut yang berpadanan besarnya ....
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan menguji pemahaman definisi dasar yang diajarkan di awal topik kesebangunan tanpa memerlukan perhitungan atau langkah prosedural yang kompleks.. Bukti: Pada dua segitiga yang sebangun, sudut-sudut yang berpadanan besarnya ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang definisi kesebangunan segitiga. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah pertanyaan konseptual dasar yang sesuai untuk kelas 7 saat pertama kali mempelajari topik kesebangunan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Kesebangunan pada Segitiga
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan $\triangle ABC$ berikut. Titik $D$ terletak pada $AB$. Jika $E$ terletak pada $AC$, hitunglah $\triangle ADE$ yang sebangun dengan $\triangle ABC$. $\triangle ABC \sim \triangle ADE$

Pada dua segitiga yang sebangun, sudut-sudut yang berpadanan besarnya ....
Pilihan: A. berbeda
B. dua kali lipat
C. berjumlah 90°
D. sama
Transkripsi visual: Gambar menunjukkan segitiga ABC dengan titik D terletak pada segmen garis AB. Tidak ada titik E yang digambarkan secara eksplisit pada AC, namun teks soal menyatakan hubungan kesebangunan antara segitiga ABC dan segitiga ADE.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 35. Soal `aacaa86c1fc9990161672c5c`

Memasang Keramik<br><br>Seorang tukang keramik memasang keramik dengan menggunakan pola berikut.<br><br>Pak Tukang akan memotong keramik untuk mengisi bagian kosong yang diberi tanda panah. Bantulah Pak Tukang untuk membuat potongan yang tepat. Berapa besar sudut potongan keramik untuk Pola 1? (Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.)

| Opsi | Isi |
|---|---|
| A | $144^\circ$ |
| B | $54^\circ$ |
| C | $72^\circ$ |
| D | $36^\circ$ |

![Gambar sumber soal 35](<../images/kelas5_panduan_siswa_kelas5.pdf-0206-05.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Sudut dalam segi lima beraturan adalah 108 derajat. Sudut persegi adalah 90 derajat. Sudut pada titik pertemuan di celah adalah 360 derajat. Sudut potongan = 360 - (108 + 108 + 90) = 360 - 306 = 54 derajat.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0206-05.png. Transkripsi visual: Gambar menunjukkan dua pola keramik. Pola 1 terdiri dari satu persegi biru di tengah yang dikelilingi oleh empat segi lima beraturan merah. Terdapat celah di antara dua segi lima yang bersebelahan dan sudut persegi. Pola 2 menunjukkan dua segi lima beraturan yang bersentuhan.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `69fcbedc910ed387faa91c5f3666b6ff68a8b1d225dfd22ee7c3812106415040`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Medium | 3040 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3106 |
| 3 | success | valid / verified | applying | procedural | Medium | 3093 |

Run 1 — solusi: Sudut dalam segi lima beraturan adalah 108 derajat. Sudut persegi adalah 90 derajat. Sudut pada titik pertemuan di celah adalah 360 derajat. Sudut potongan = 360 - (108 + 108 + 90) = 360 - 306 = 54 derajat.
- Domain kognitif `classify/reasoning`: Siswa perlu mengintegrasikan pengetahuan tentang sudut dalam bangun datar (segi lima dan persegi) dan menerapkan konsep sudut satu putaran penuh (360 derajat) untuk memecahkan masalah geometri yang tidak rutin.. Bukti: Berapa besar sudut potongan keramik untuk Pola 1?; Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman konseptual tentang properti sudut bangun datar dan bagaimana mereka berinteraksi dalam susunan pola.. Bukti: Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemahaman tentang sudut dalam poligon dan hubungan sudut pada titik pertemuan. Ini melibatkan beberapa langkah rutin yang saling terkait (menghitung sudut poligon dan mengurangkannya dari 360 derajat).. Bukti: Berapa besar sudut potongan keramik untuk Pola 1?; 360 - 108 - 108 - 90 = 54 derajat

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengetahuan tentang besar sudut dalam segi lima beraturan (108 derajat) dan persegi (90 derajat), serta konsep sudut satu putaran penuh. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 3 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan memahami sudut dalam poligon dan geometri dasar. Masalah ini menuntut integrasi informasi visual dan pengetahuan geometri, yang sesuai untuk tingkat kesulitan menengah di kelas 7. |

Run 2 — solusi: Sudut dalam segi lima beraturan adalah (5-2)x180/5 = 108 derajat. Sudut persegi adalah 90 derajat. Sudut pada satu titik pertemuan di celah adalah 360 derajat. Sudut potongan = 360 - (sudut segi lima) - (sudut segi lima) - (sudut persegi) = 360 - 108 - 108 - 90 = 54 derajat.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan pengetahuan tentang sudut dalam poligon beraturan (segi lima) dan persegi, serta memahami hubungan sudut pada satu titik (360 derajat) untuk memecahkan masalah geometri yang tidak rutin.. Bukti: Berapa besar sudut potongan keramik untuk Pola 1?; Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.
- Dimensi pengetahuan `classify/conceptual`: Siswa menerapkan prinsip geometri (jumlah sudut dalam poligon dan sudut satu putaran penuh) untuk menyelesaikan masalah prosedural yang memerlukan pemahaman konseptual tentang bentuk.. Bukti: Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.; Berapa besar sudut potongan keramik untuk Pola 1?
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemahaman tentang sifat sudut poligon dan hubungan sudut di sekitar titik. Siswa harus mengidentifikasi bahwa celah tersebut dibatasi oleh dua sudut segi lima dan satu sudut persegi, lalu melakukan operasi pengurangan dari 360 derajat.. Bukti: Berapa besar sudut potongan keramik untuk Pola 1?; Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengetahuan tentang sudut dalam poligon beraturan dan sudut satu putaran penuh (360 derajat). |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah mempelajari sudut dan poligon. Masalah ini menuntut penerapan konsep tersebut dalam konteks ubin/pola yang sedikit lebih kompleks daripada sekadar menghitung sudut poligon tunggal. |

Run 3 — solusi: Sudut dalam segi lima beraturan adalah (5-2)x180/5 = 108 derajat. Sudut persegi adalah 90 derajat. Sudut satu putaran penuh adalah 360 derajat. Sudut celah = 360 - (108 + 108 + 90) = 360 - 306 = 54 derajat.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan pengetahuan tentang sudut dalam poligon beraturan (segi lima) dan persegi, serta memahami konsep sudut satu putaran penuh (360 derajat) untuk menentukan sudut celah yang tersisa.. Bukti: Berapa besar sudut potongan keramik untuk Pola 1?; Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan prosedur perhitungan sudut poligon dan operasi aritmatika dasar untuk menyelesaikan masalah geometri yang terstruktur.. Bukti: Keramik merah berbentuk segi lima beraturan; 360 - 108 - 108 - 90 = 54 derajat
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman tentang sudut dalam poligon dan hubungan sudut di sekitar titik, yang merupakan langkah rutin namun memerlukan integrasi beberapa informasi geometris.. Bukti: Berapa besar sudut potongan keramik untuk Pola 1?; Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengetahuan tentang sudut dalam poligon beraturan (n-gon) dan sudut satu putaran penuh (360 derajat). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah mempelajari sifat-sifat sudut pada bangun datar dan poligon. Menghitung sudut celah dengan mengurangkan sudut-sudut yang diketahui dari 360 derajat adalah tugas yang sesuai untuk tingkat ini. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 1, "applying": 2} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4780`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan pengetahuan tentang sudut dalam poligon beraturan dan hubungan sudut di sekitar titik (sudut satu putaran penuh) untuk menyelesaikan masalah geometri yang memerlukan integrasi informasi visual.
- Dimensi pengetahuan `conceptual`: Siswa menggunakan pengetahuan konseptual tentang sifat-sifat sudut bangun datar (segi lima dan persegi) untuk menentukan besar sudut yang tidak diketahui.
- Intended difficulty `Medium`: Soal ini melibatkan beberapa langkah rutin yang saling terkait (menghitung sudut poligon dan mengurangkannya dari 360 derajat).

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengetahuan tentang besar sudut dalam segi lima beraturan (108 derajat) dan persegi (90 derajat), serta konsep sudut satu putaran penuh. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 3 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan memahami sudut dalam poligon dan geometri dasar. Masalah ini menuntut integrasi informasi visual dan pengetahuan geometri, yang sesuai untuk tingkat kesulitan menengah di kelas 7. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Melukis Sudut
Tipe soal: multiple_choice
Stimulus: -
Soal: Memasang Keramik

Seorang tukang keramik memasang keramik dengan menggunakan pola berikut.

Pak Tukang akan memotong keramik untuk mengisi bagian kosong yang diberi tanda panah. Bantulah Pak Tukang untuk membuat potongan yang tepat. Berapa besar sudut potongan keramik untuk Pola 1? (Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.)
Pilihan: A. $144^\circ$
B. $54^\circ$
C. $72^\circ$
D. $36^\circ$
Transkripsi visual: Gambar menunjukkan dua pola keramik. Pola 1 terdiri dari satu persegi biru di tengah yang dikelilingi oleh empat segi lima beraturan merah. Terdapat celah di antara dua segi lima yang bersebelahan dan sudut persegi. Pola 2 menunjukkan dua segi lima beraturan yang bersentuhan.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 36. Soal `4857ed456bf6383ee84ff085`

Kalau sembarang bentuk belah ketupat boleh disebut jajargenjang, apakah sembarang jajargenjang boleh disebut belah ketupat?

| Opsi | Isi |
|---|---|
| A | Ya, karena sisi-sisi yang berhadapan pada jajargenjang sejajar |
| B | Tidak, karena jajargenjang tidak harus memiliki empat sisi yang sama panjang |
| C | Ya, karena belah ketupat boleh disebut jajargenjang, maka sebaliknya juga boleh |
| D | Tidak, karena jajargenjang tidak memiliki sisi-sisi yang sejajar |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Belah ketupat adalah jajargenjang dengan keempat sisi sama panjang. Jajargenjang umum tidak harus memiliki keempat sisi sama panjang, sehingga tidak semua jajargenjang adalah belah ketupat.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `84c738a2de31fca79f954b1b5432941446e7b39135f02f6f317b846e1ec7d1e8`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Medium | 1769 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 1766 |
| 3 | success | valid / verified | reasoning | conceptual | Medium | 1781 |

Run 1 — solusi: Belah ketupat adalah jajargenjang dengan keempat sisi sama panjang. Jajargenjang umum tidak harus memiliki keempat sisi sama panjang, sehingga tidak semua jajargenjang adalah belah ketupat.
- Domain kognitif `classify/reasoning`: Soal ini menuntut siswa untuk memahami hubungan hierarkis antar bangun datar (klasifikasi) dan membedakan sifat-sifat yang menjadi syarat cukup dan syarat perlu.. Bukti: apakah sembarang jajargenjang boleh disebut belah ketupat?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami definisi dan hubungan antar konsep geometri (hierarki bangun datar), bukan sekadar menghafal fakta atau prosedur.. Bukti: sembarang bentuk belah ketupat boleh disebut jajargenjang; jajargenjang tidak harus memiliki empat sisi yang sama panjang
- Intended difficulty `classify/Medium`: Soal ini menguji pemahaman konseptual tentang sifat bangun datar. Meskipun konsepnya mendasar, ini memerlukan penalaran logis tentang inklusi himpunan (subset) yang sering menjadi miskonsepsi bagi siswa kelas 7.. Bukti: apakah sembarang jajargenjang boleh disebut belah ketupat?; jajargenjang tidak harus memiliki empat sisi yang sama panjang

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi dan sifat-sifat jajargenjang dan belah ketupat. |
| dependentSteps | 1 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sering mengalami kesulitan dalam memahami hubungan inklusi antar bangun datar. Soal ini menuntut pemahaman definisi formal, bukan sekadar visualisasi. |

Run 2 — solusi: Belah ketupat adalah jajargenjang dengan keempat sisi sama panjang. Jajargenjang umum tidak harus memiliki keempat sisi sama panjang, sehingga tidak semua jajargenjang adalah belah ketupat.
- Domain kognitif `classify/reasoning`: Soal ini menuntut pemahaman konsep hierarki bangun datar dan sifat-sifat khusus yang membedakan belah ketupat dari jajargenjang umum, bukan sekadar menghafal definisi.. Bukti: apakah sembarang jajargenjang boleh disebut belah ketupat?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang hubungan inklusi antar kategori bangun datar (konsep hierarki).. Bukti: sembarang bentuk belah ketupat boleh disebut jajargenjang; jajargenjang tidak harus memiliki empat sisi yang sama panjang
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemahaman konsep yang mendalam tentang sifat-sifat bangun datar. Siswa harus membedakan antara sifat umum (jajargenjang) dan sifat khusus (belah ketupat) serta memahami bahwa relasi himpunan bagian tidak berlaku dua arah.. Bukti: apakah sembarang jajargenjang boleh disebut belah ketupat?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi dan sifat-sifat dasar jajargenjang dan belah ketupat. |
| dependentSteps | 1 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 7, membedakan sifat bangun datar dalam hierarki geometri adalah materi standar, namun memerlukan penalaran konseptual yang lebih dari sekadar ingatan faktual. |

Run 3 — solusi: Definisi belah ketupat adalah jajargenjang dengan keempat sisi sama panjang. Jajargenjang umum tidak harus memiliki keempat sisi sama panjang, sehingga tidak semua jajargenjang adalah belah ketupat.
- Domain kognitif `classify/reasoning`: Soal ini menuntut siswa untuk memahami hubungan hierarkis antar bangun datar (klasifikasi inklusif) dan membedakan sifat-sifat yang menjadi syarat cukup vs syarat perlu.. Bukti: apakah sembarang jajargenjang boleh disebut belah ketupat?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami struktur hierarki konsep geometri (belah ketupat sebagai subset dari jajargenjang) dan prinsip definisi bangun datar.. Bukti: belah ketupat boleh disebut jajargenjang; apakah sembarang jajargenjang boleh disebut belah ketupat?
- Intended difficulty `classify/Medium`: Soal ini menguji pemahaman konseptual tentang sifat bangun datar. Meskipun terlihat sederhana, ini memerlukan penalaran logis tentang inklusi himpunan bangun datar yang sering disalahpahami siswa.. Bukti: Kalau sembarang bentuk belah ketupat boleh disebut jajargenjang, apakah sembarang jajargenjang boleh disebut belah ketupat?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi dan sifat-sifat dasar jajargenjang dan belah ketupat. |
| dependentSteps | 1 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sedang mempelajari klasifikasi bangun datar. Memahami bahwa sifat 'jajargenjang' adalah syarat perlu bagi 'belah ketupat' tetapi bukan syarat cukup adalah tantangan konseptual yang sesuai untuk level ini. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 3} | unanimous_3_0 / unanimous | reasoning |
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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Membandingkan Ciri-Ciri Segi Empat
Tipe soal: multiple_choice
Stimulus: -
Soal: Kalau sembarang bentuk belah ketupat boleh disebut jajargenjang, apakah sembarang jajargenjang boleh disebut belah ketupat?
Pilihan: A. Ya, karena sisi-sisi yang berhadapan pada jajargenjang sejajar
B. Tidak, karena jajargenjang tidak harus memiliki empat sisi yang sama panjang
C. Ya, karena belah ketupat boleh disebut jajargenjang, maka sebaliknya juga boleh
D. Tidak, karena jajargenjang tidak memiliki sisi-sisi yang sejajar
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "reasoning", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 37. Soal `544a2e4954b07fcf67f1ed3c`

Line plot di bawah ini yang menunjukkan banyaknya huruf di nama siswa-siswa kelas 7A di Sekolah Indonesia Raya.<br><br>Panjang Nama Siswa di Kelas 7A<br><br>Dari line plot di atas, cobalah menjawab beberapa pertanyaan berikut.<br><br>Jika Rahma Kusni adalah siswa kelas 7A, maka berapakah teman Rahma yang memiliki nama yang sama panjang dengannya? Ada berapa banyak siswa di kelas 7A yang memiliki panjang nama dua kali dari nama Rahma?

| Opsi | Isi |
|---|---|
| A | 3 teman; 3 siswa |
| B | 1 teman; 3 siswa |
| C | 2 teman; 3 siswa |
| D | 2 teman; 2 siswa |

![Gambar sumber soal 37](<../images/kelas7_panduan_siswa_kelas7.pdf-0213-07.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Nama 'Rahma Kusni' dihitung memiliki 10 huruf. Pada line plot, kolom 10 memiliki 3 tanda X, yang berarti ada 3 siswa dengan 10 huruf. Teman Rahma yang memiliki panjang nama sama adalah 3 - 1 = 2 siswa. Panjang nama dua kali Rahma adalah 2 x 10 = 20 huruf. Pada kolom 20, terdapat 3 tanda X, yang berarti ada 3 siswa.
Gambar sumber: images/kelas7_panduan_siswa_kelas7.pdf-0213-07.png. Transkripsi visual: Line plot menunjukkan sumbu horizontal 'Banyaknya Huruf' dari 6 hingga 32. Pada angka 10, terdapat 3 tanda X. Pada angka 20, terdapat 3 tanda X.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f40f67f38457a7fec435fe5a8556a6709d76adb0798ffcd9edc2d271d276459d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 3228 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3007 |
| 3 | success | concern / conflict | applying | procedural | Medium | 3295 |

Run 1 — solusi: Nama 'Rahma Kusni' terdiri dari 10 huruf. Pada kolom 10 terdapat 3 tanda X, artinya ada 3 siswa dengan 10 huruf, sehingga teman Rahma yang memiliki panjang nama sama adalah 3 - 1 = 2 siswa. Panjang nama dua kali Rahma adalah 2 x 10 = 20 huruf. Pada kolom 20 terdapat 3 tanda X, artinya ada 3 siswa dengan panjang nama 20 huruf.
- Domain kognitif `classify/applying`: Siswa perlu membaca data dari grafik (line plot), melakukan operasi hitung sederhana (menghitung huruf, perkalian), dan menginterpretasikan data untuk menjawab pertanyaan yang melibatkan pengurangan (mencari teman selain diri sendiri). Ini termasuk dalam kategori applying karena menerapkan prosedur membaca grafik pada situasi rutin.. Bukti: Jika Rahma Kusni adalah siswa kelas 7A, maka berapakah teman Rahma yang memiliki nama yang sama panjang dengannya?; Ada berapa banyak siswa di kelas 7A yang memiliki panjang nama dua kali dari nama Rahma?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang cara membaca dan menginterpretasikan representasi data statistik (line plot), yang merupakan pengetahuan konseptual tentang bagaimana data disajikan.. Bukti: Line plot di bawah ini yang menunjukkan banyaknya huruf di nama siswa-siswa kelas 7A
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena memerlukan beberapa langkah rutin yang saling terkait: menghitung jumlah huruf, membaca data dari grafik, melakukan operasi aritmatika (perkalian dan pengurangan), serta memahami konteks 'teman' (mengurangi diri sendiri dari total).. Bukti: Jika Rahma Kusni adalah siswa kelas 7A, maka berapakah teman Rahma yang memiliki nama yang sama panjang dengannya?; Ada berapa banyak siswa di kelas 7A yang memiliki panjang nama dua kali dari nama Rahma?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca grafik/diagram (line plot) dan operasi aritmatika dasar (perkalian, pengurangan). |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena melibatkan interpretasi data statistik dasar yang merupakan bagian dari kurikulum SMP kelas 7. |

Run 2 — solusi: Nama 'Rahma Kusni' memiliki 10 huruf. Pada line plot, kolom 10 memiliki 3 tanda X, yang berarti ada 3 siswa dengan 10 huruf (Rahma + 2 teman). Dua kali panjang nama Rahma adalah 20 huruf. Pada kolom 20, terdapat 3 tanda X, yang berarti ada 3 siswa.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasikan data dari line plot, melakukan operasi hitung sederhana (menghitung huruf dan perkalian), serta memahami konteks 'teman' (mengurangi total dengan diri sendiri). Ini adalah penerapan prosedur pada situasi rutin.. Bukti: Jika Rahma Kusni adalah siswa kelas 7A, maka berapakah teman Rahma yang memiliki nama yang sama panjang dengannya?; Ada berapa banyak siswa di kelas 7A yang memiliki panjang nama dua kali dari nama Rahma?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang cara membaca dan menginterpretasikan representasi data statistik (line plot).. Bukti: Line plot di bawah ini yang menunjukkan banyaknya huruf di nama siswa-siswa kelas 7A
- Intended difficulty `classify/Medium`: Soal memerlukan pembacaan data yang akurat dari grafik dan operasi aritmatika dasar. Tingkat kesulitan ini sesuai untuk kelas 7 karena melibatkan interpretasi visual yang rutin.. Bukti: Jika Rahma Kusni adalah siswa kelas 7A; panjang nama dua kali dari nama Rahma

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca grafik/diagram (line plot) dan operasi aritmatika dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu membaca data dari diagram dan melakukan operasi hitung sederhana berdasarkan data tersebut. |

Run 3 — solusi: Jika diasumsikan panjang nama Rahma adalah 10 huruf (mengabaikan spasi), maka pada kolom 10 terdapat 3 tanda X, sehingga ada 2 teman dengan panjang nama yang sama. Panjang dua kali dari 10 adalah 20, dan pada kolom 20 terdapat 3 tanda X. Namun, karena nama 'Rahma Kusni' secara teknis memiliki 11 karakter (termasuk spasi), kunci jawaban C tidak konsisten dengan data literal.
- Domain kognitif `classify/applying`: Siswa perlu membaca data dari line plot, melakukan operasi aritmatika sederhana (pengurangan untuk mencari teman, perkalian untuk mencari dua kali lipat), dan menginterpretasikan data statistik.. Bukti: Jika Rahma Kusni adalah siswa kelas 7A, maka berapakah teman Rahma yang memiliki nama yang sama panjang dengannya?; Ada berapa banyak siswa di kelas 7A yang memiliki panjang nama dua kali dari nama Rahma?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan pengetahuan prosedural dalam membaca grafik statistik dan menerapkan konsep dasar aritmatika.. Bukti: Line plot di bawah ini yang menunjukkan banyaknya huruf di nama siswa-siswa kelas 7A
- Intended difficulty `classify/Medium`: Soal memerlukan pembacaan grafik yang rutin dan operasi aritmatika dasar. Kesulitan utama terletak pada interpretasi data yang ambigu, bukan pada kompleksitas matematisnya.. Bukti: Jika Rahma Kusni adalah siswa kelas 7A, maka berapakah teman Rahma yang memiliki nama yang sama panjang dengannya?; Ada berapa banyak siswa di kelas 7A yang memiliki panjang nama dua kali dari nama Rahma?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca data dari line plot dan operasi aritmatika dasar (perkalian dan pengurangan). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena melibatkan pembacaan data statistik dasar yang merupakan bagian dari kurikulum, meskipun terdapat masalah pada validitas konten soal. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4886`.
Konten: `valid`; kunci: `verified`; masalah: Terdapat ambiguitas dalam penghitungan jumlah huruf pada nama 'Rahma Kusni'. Secara literal, nama tersebut memiliki 10 huruf (R-a-h-m-a-K-u-s-n-i) jika spasi diabaikan, atau 11 karakter jika spasi dihitung. Namun, berdasarkan kunci jawaban C yang mengasumsikan 10 huruf, soal ini dapat diselesaikan dengan asumsi tersebut..
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur membaca data dari grafik (line plot) dan melakukan operasi aritmatika dasar (pengurangan untuk mencari teman, perkalian untuk mencari dua kali lipat) dalam situasi rutin.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana data statistik disajikan dalam bentuk line plot dan bagaimana menginterpretasikan frekuensi data tersebut.
- Intended difficulty `Medium`: Soal ini memerlukan beberapa langkah rutin yang saling terkait: menghitung jumlah huruf, membaca data dari grafik, melakukan operasi aritmatika, serta memahami konteks 'teman' (mengurangi diri sendiri). Tingkat kesulitan ini sesuai untuk kelas 7.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca grafik (line plot) dan operasi aritmatika dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena melibatkan interpretasi data statistik dasar yang merupakan bagian dari kurikulum SMP kelas 7. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Investigasi Statistika
Tipe soal: multiple_choice
Stimulus: -
Soal: Line plot di bawah ini yang menunjukkan banyaknya huruf di nama siswa-siswa kelas 7A di Sekolah Indonesia Raya.

Panjang Nama Siswa di Kelas 7A

Dari line plot di atas, cobalah menjawab beberapa pertanyaan berikut.

Jika Rahma Kusni adalah siswa kelas 7A, maka berapakah teman Rahma yang memiliki nama yang sama panjang dengannya? Ada berapa banyak siswa di kelas 7A yang memiliki panjang nama dua kali dari nama Rahma?
Pilihan: A. 3 teman; 3 siswa
B. 1 teman; 3 siswa
C. 2 teman; 3 siswa
D. 2 teman; 2 siswa
Transkripsi visual: Line plot menunjukkan sumbu horizontal 'Banyaknya Huruf' dari 6 hingga 32. Pada angka 10, terdapat 3 tanda X. Pada angka 20, terdapat 3 tanda X.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: Terdapat ambiguitas dalam penghitungan jumlah huruf pada nama 'Rahma Kusni'. Secara literal, nama tersebut memiliki 10 huruf (R-a-h-m-a-K-u-s-n-i) jika spasi diabaikan, atau 11 karakter jika spasi dihitung. Namun, berdasarkan kunci jawaban C yang mengasumsikan 10 huruf, soal ini dapat diselesaikan dengan asumsi tersebut..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 38. Soal `9f164962fc74de3c9274b04f`

Jika seorang siswi bernama Metta Widyanti, artinya panjang namanya adalah 13 huruf karena terdiri dari 5 huruf untuk Metta dan 8 huruf untuk Widyanti.<br><br>Line plot di bawah ini yang menunjukkan banyaknya huruf di nama siswa-siswa kelas 7A di Sekolah Indonesia Raya.<br><br>Panjang Nama Siswa di Kelas 7A<br><br>Dari line plot di atas.<br><br>Ada berapa siswa di kelas 7A yang memiliki nama sama panjang dengan Metta Widyanti?

| Opsi | Isi |
|---|---|
| A | 6 siswa |
| B | 27 siswa |
| C | 13 siswa |
| D | 3 siswa |

![Gambar sumber soal 38](<../images/kelas7_panduan_siswa_kelas7.pdf-0213-07.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Metta Widyanti memiliki 13 huruf. Pada line plot, cari angka 13 pada sumbu horizontal, lalu hitung jumlah tanda X di atasnya. Terdapat 6 tanda X, sehingga ada 6 siswa.
Gambar sumber: images/kelas7_panduan_siswa_kelas7.pdf-0213-07.png. Transkripsi visual: Line plot berjudul 'Panjang Nama Siswa di Kelas 7A' dengan sumbu horizontal 'Banyaknya Huruf' dari 6 hingga 32. Terdapat tanda X di atas angka 13 sebanyak 6 buah.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0d4135faf1a4161d9a9d4cfcc3c15db83e3e40fdc16e0eaec7693578dc1fcc27`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2927 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2905 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2923 |

Run 1 — solusi: Metta Widyanti memiliki 13 huruf. Pada line plot, cari angka 13 pada sumbu horizontal, lalu hitung jumlah tanda X di atasnya. Terdapat 6 tanda X, sehingga ada 6 siswa.
- Domain kognitif `classify/knowing`: Siswa diminta untuk membaca data dari representasi visual (line plot) secara langsung tanpa perlu melakukan manipulasi atau analisis kompleks.. Bukti: Ada berapa siswa di kelas 7A yang memiliki nama sama panjang dengan Metta Widyanti?; Line plot di bawah ini yang menunjukkan banyaknya huruf
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang cara membaca dan menginterpretasikan data yang disajikan dalam bentuk line plot (grafik garis).. Bukti: Line plot di bawah ini yang menunjukkan banyaknya huruf
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural dan sangat langsung. Siswa hanya perlu mengidentifikasi nilai 13 pada sumbu horizontal dan menghitung frekuensi (jumlah X) yang bersesuaian.. Bukti: Ada berapa siswa di kelas 7A yang memiliki nama sama panjang dengan Metta Widyanti?; Line plot di bawah ini yang menunjukkan banyaknya huruf

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca grafik sederhana (line plot). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena melibatkan pembacaan data statistik dasar yang merupakan bagian dari kurikulum statistik awal. |

Run 2 — solusi: Identifikasi panjang nama Metta Widyanti yaitu 13 huruf. Pada line plot, cari angka 13 pada sumbu horizontal, lalu hitung jumlah tanda X di atasnya. Terdapat 6 tanda X, sehingga ada 6 siswa.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data dari grafik (line plot) secara langsung tanpa melakukan manipulasi atau analisis kompleks.. Bukti: Ada berapa siswa di kelas 7A yang memiliki nama sama panjang dengan Metta Widyanti?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang cara membaca representasi data statistik sederhana (line plot).. Bukti: Line plot di bawah ini yang menunjukkan banyaknya huruf
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mencocokkan nilai (13) dengan sumbu horizontal dan menghitung frekuensi (tanda X) yang bersesuaian.. Bukti: Ada berapa siswa di kelas 7A yang memiliki nama sama panjang dengan Metta Widyanti?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca grafik sederhana (line plot). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca line plot adalah keterampilan dasar statistik kelas 7 yang bersifat prosedural langsung. |

Run 3 — solusi: Metta Widyanti memiliki 13 huruf. Pada line plot, cari angka 13 pada sumbu horizontal, lalu hitung jumlah tanda X di atasnya. Terdapat 6 tanda X, sehingga ada 6 siswa.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data dari representasi visual (line plot) secara langsung untuk menjawab pertanyaan.. Bukti: Ada berapa siswa di kelas 7A yang memiliki nama sama panjang dengan Metta Widyanti?; Line plot di bawah ini yang menunjukkan banyaknya huruf
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang cara membaca dan menginterpretasikan data pada diagram line plot.. Bukti: Line plot di bawah ini yang menunjukkan banyaknya huruf
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural dasar dan sangat langsung. Siswa hanya perlu mengidentifikasi nilai pada sumbu horizontal dan menghitung frekuensi (tanda X) yang bersesuaian.. Bukti: Ada berapa siswa di kelas 7A yang memiliki nama sama panjang dengan Metta Widyanti?; Line plot di bawah ini yang menunjukkan banyaknya huruf

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram statistik sederhana (line plot). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca line plot adalah keterampilan dasar statistik kelas 7 yang rutin dan tidak memerlukan langkah kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Investigasi Statistika
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika seorang siswi bernama Metta Widyanti, artinya panjang namanya adalah 13 huruf karena terdiri dari 5 huruf untuk Metta dan 8 huruf untuk Widyanti.

Line plot di bawah ini yang menunjukkan banyaknya huruf di nama siswa-siswa kelas 7A di Sekolah Indonesia Raya.

Panjang Nama Siswa di Kelas 7A

Dari line plot di atas.

Ada berapa siswa di kelas 7A yang memiliki nama sama panjang dengan Metta Widyanti?
Pilihan: A. 6 siswa
B. 27 siswa
C. 13 siswa
D. 3 siswa
Transkripsi visual: Line plot berjudul 'Panjang Nama Siswa di Kelas 7A' dengan sumbu horizontal 'Banyaknya Huruf' dari 6 hingga 32. Terdapat tanda X di atas angka 13 sebanyak 6 buah.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 39. Soal `31c93886f6631ba9c60a0403`

Siswa kelas 7B dari Sekolah Indonesia Raya memiliki pertanyaan:<br>a. Berapakah aplikasi permainan online yang ada dalam gawai kalian?<br>b. Permainan online manakah yang menjadi favorit kalian?<br>Mereka mengumpulkan datanya, lalu menampilkan data tersebut dalam tabel frekuensi dan menggambar diagram batangnya untuk menunjukkan sebaran datanya.<br><br>Tabel 6.2 Tabel Banyak Aplikasi Online<br><br>\| Banyaknya aplikasi permainan online dalam gawai \| Banyak Siswa \|<br>\|---\|---\|<br>\| 0 \| 1 \|<br>\| 1 \| 3 \|<br>\| 2 \| 7 \|<br>\| 3 \| 10 \|<br>\| 4 \| 8 \|<br>\| 5 \| 2 \|<br>\| 6 \| 1 \|<br><br>Gambar 6.9 Diagram Banyak Aplikasi Online<br><br>Tabel 6.3 Tabel Jenis Aplikasi Online<br><br>\| Aplikasi Permainan Online Favorit \| Banyak Siswa \|<br>\|---\|---\|<br>\| Mobile Legends \| 12 \|<br>\| Wormszone.io \| 6 \|<br>\| PUBG Mobile \| 5 \|<br>\| Among Us! \| 4 \|<br>\| Hago \| 3 \|<br>\| Candy Crush Saga \| 1 \|<br><br>Gambar 6.10 Diagram Jenis Aplikasi Online<br><br>Dari kedua data dan tabel di atas, tentukanlah pertanyaan mana saja yang bisa dijawab melalui informasi di atas. Jika dapat di jawab, tentukanlah jawabannya. Jika pertanyaan di bawah ini tidak dapat dijawab, mengapa dan informasi apakah yang kalian perlukan agar kalian bisa menjawab pertanyaan tersebut.<br><br>Berapakah jumlah siswa kelas 7B?

| Opsi | Isi |
|---|---|
| A | 95 siswa |
| B | 32 siswa |
| C | 7 siswa |
| D | 31 siswa |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Jumlah siswa kelas 7B dapat ditentukan dengan menjumlahkan frekuensi pada Tabel 6.2 (Banyak Siswa), yaitu 1 + 3 + 7 + 10 + 8 + 2 + 1 = 32 siswa.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6c0d0fa48f10362b34108616db3f1ac1da26bd4bd4c8b435979f76a2b780e603`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1983 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2085 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2010 |

Run 1 — solusi: Jumlah siswa kelas 7B dapat ditentukan dengan menjumlahkan frekuensi pada Tabel 6.2 (Banyak Siswa), yaitu 1 + 3 + 7 + 10 + 8 + 2 + 1 = 32 siswa.
- Domain kognitif `classify/applying`: Siswa perlu memahami struktur tabel frekuensi dan menginterpretasikan data yang disajikan untuk menjawab pertanyaan tentang total populasi.. Bukti: menampilkan data tersebut dalam tabel frekuensi; Berapakah jumlah siswa kelas 7B?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana data dikategorikan dan disajikan dalam tabel frekuensi.. Bukti: Tabel 6.2 Tabel Banyak Aplikasi Online
- Intended difficulty `classify/Easy`: Soal ini meminta siswa untuk mengidentifikasi kolom yang relevan (Banyak Siswa) dan melakukan penjumlahan sederhana. Prosedurnya rutin dan informasinya eksplisit.. Bukti: Tabel 6.2 Tabel Banyak Aplikasi Online; Berapakah jumlah siswa kelas 7B?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang tabel frekuensi dan operasi penjumlahan bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah terbiasa membaca tabel frekuensi sederhana dan melakukan penjumlahan data untuk menentukan total. |

Run 2 — solusi: Jumlah siswa kelas 7B adalah total frekuensi pada Tabel 6.2 (Banyaknya aplikasi), yaitu 1 + 3 + 7 + 10 + 8 + 2 + 1 = 32 siswa.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa total siswa kelas 7B direpresentasikan oleh total frekuensi pada tabel distribusi frekuensi (Tabel 6.2), bukan tabel kategori (Tabel 6.3). Ini adalah penerapan konsep dasar tabel frekuensi.. Bukti: Berapakah jumlah siswa kelas 7B?; Tabel 6.2 Tabel Banyak Aplikasi Online
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana data frekuensi disusun dan apa yang direpresentasikan oleh total frekuensi dalam konteks populasi kelas.. Bukti: Tabel 6.2 Tabel Banyak Aplikasi Online; Berapakah jumlah siswa kelas 7B?
- Intended difficulty `classify/Easy`: Soal ini memerlukan ketelitian dalam memilih tabel yang tepat (Tabel 6.2 mencakup semua siswa, sedangkan Tabel 6.3 hanya mencakup siswa yang memiliki aplikasi favorit). Ini adalah tugas rutin yang memerlukan pemilihan informasi yang relevan.. Bukti: Berapakah jumlah siswa kelas 7B?; Tabel 6.2 Tabel Banyak Aplikasi Online

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami tabel frekuensi dan penjumlahan bilangan bulat sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 7 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu membaca tabel frekuensi dan memahami bahwa total frekuensi adalah jumlah populasi. Pilihan pengecoh (distraktor) dirancang untuk menguji apakah siswa memahami perbedaan antara data numerik (jumlah aplikasi) dan data kategorikal (jenis aplikasi). |

Run 3 — solusi: Jumlah siswa kelas 7B dapat ditentukan dengan menjumlahkan frekuensi pada Tabel 6.2 (Banyak Siswa), yaitu 1 + 3 + 7 + 10 + 8 + 2 + 1 = 32 siswa.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa total populasi (jumlah siswa) terdapat pada kolom frekuensi tabel distribusi data (Tabel 6.2), bukan pada kategori data atau tabel lain.. Bukti: Tabel 6.2 Tabel Banyak Aplikasi Online; Berapakah jumlah siswa kelas 7B?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana data frekuensi disusun dan apa yang direpresentasikan oleh kolom frekuensi dalam sebuah tabel.. Bukti: menampilkan data tersebut dalam tabel frekuensi; Berapakah jumlah siswa kelas 7B?
- Intended difficulty `classify/Easy`: Soal ini meminta siswa membaca tabel frekuensi dan melakukan operasi penjumlahan dasar. Tidak ada strategi nonrutin atau kendala kompleks.. Bukti: Tabel 6.2 Tabel Banyak Aplikasi Online; Berapakah jumlah siswa kelas 7B?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca tabel frekuensi dan melakukan penjumlahan bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu membaca dan menginterpretasikan tabel frekuensi sederhana sebagai bagian dari materi statistika dasar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Macam-Macam Data
Tipe soal: multiple_choice
Stimulus: -
Soal: Siswa kelas 7B dari Sekolah Indonesia Raya memiliki pertanyaan:
a. Berapakah aplikasi permainan online yang ada dalam gawai kalian?
b. Permainan online manakah yang menjadi favorit kalian?
Mereka mengumpulkan datanya, lalu menampilkan data tersebut dalam tabel frekuensi dan menggambar diagram batangnya untuk menunjukkan sebaran datanya.

Tabel 6.2 Tabel Banyak Aplikasi Online

| Banyaknya aplikasi permainan online dalam gawai | Banyak Siswa |
|---|---|
| 0 | 1 |
| 1 | 3 |
| 2 | 7 |
| 3 | 10 |
| 4 | 8 |
| 5 | 2 |
| 6 | 1 |

Gambar 6.9 Diagram Banyak Aplikasi Online

Tabel 6.3 Tabel Jenis Aplikasi Online

| Aplikasi Permainan Online Favorit | Banyak Siswa |
|---|---|
| Mobile Legends | 12 |
| Wormszone.io | 6 |
| PUBG Mobile | 5 |
| Among Us! | 4 |
| Hago | 3 |
| Candy Crush Saga | 1 |

Gambar 6.10 Diagram Jenis Aplikasi Online

Dari kedua data dan tabel di atas, tentukanlah pertanyaan mana saja yang bisa dijawab melalui informasi di atas. Jika dapat di jawab, tentukanlah jawabannya. Jika pertanyaan di bawah ini tidak dapat dijawab, mengapa dan informasi apakah yang kalian perlukan agar kalian bisa menjawab pertanyaan tersebut.

Berapakah jumlah siswa kelas 7B?
Pilihan: A. 95 siswa
B. 32 siswa
C. 7 siswa
D. 31 siswa
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 40. Soal `5877a5975ba32dc0df8c9acb`

Siswa kelas 7B dari Sekolah Indonesia Raya memiliki pertanyaan:<br>a. Berapakah aplikasi permainan online yang ada dalam gawai kalian?<br>b. Permainan online manakah yang menjadi favorit kalian?<br>Mereka mengumpulkan datanya, lalu menampilkan data tersebut dalam tabel frekuensi dan menggambar diagram batangnya untuk menunjukkan sebaran datanya.<br><br>Tabel 6.2 Tabel Banyak Aplikasi Online<br><br>\| Banyaknya aplikasi permainan online dalam gawai \| Banyak Siswa \|<br>\|---\|---\|<br>\| 0 \| 1 \|<br>\| 1 \| 3 \|<br>\| 2 \| 7 \|<br>\| 3 \| 10 \|<br>\| 4 \| 8 \|<br>\| 5 \| 2 \|<br>\| 6 \| 1 \|<br><br>Gambar 6.9 Diagram Banyak Aplikasi Online<br><br>Tabel 6.3 Tabel Jenis Aplikasi Online<br><br>\| Aplikasi Permainan Online Favorit \| Banyak Siswa \|<br>\|---\|---\|<br>\| Mobile Legends \| 12 \|<br>\| Wormszone.io \| 6 \|<br>\| PUBG Mobile \| 5 \|<br>\| Among Us! \| 4 \|<br>\| Hago \| 3 \|<br>\| Candy Crush Saga \| 1 \|<br><br>Gambar 6.10 Diagram Jenis Aplikasi Online<br><br>Dari kedua data dan tabel di atas, tentukanlah pertanyaan mana saja yang bisa dijawab melalui informasi di atas. Jika dapat di jawab, tentukanlah jawabannya. Jika pertanyaan di bawah ini tidak dapat dijawab, mengapa dan informasi apakah yang kalian perlukan agar kalian bisa menjawab pertanyaan tersebut.<br><br>Berapa jumlah siswa yang memilih Aplikasi Among Us! sebagai permainan favoritnya?

| Opsi | Isi |
|---|---|
| A | 3 siswa |
| B | 6 siswa |
| C | 5 siswa |
| D | 4 siswa |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Berdasarkan Tabel 6.3, baris 'Among Us!' menunjukkan angka 4 pada kolom 'Banyak Siswa'.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `17a4f0864eaad0a524b8f24dfb92b005aedfedd122d6c34812c60441a7f15828`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 1817 |
| 2 | success | valid / verified | knowing | factual | Easy | 1798 |
| 3 | success | valid / verified | knowing | factual | Easy | 1828 |

Run 1 — solusi: Berdasarkan Tabel 6.3, baris 'Among Us!' menunjukkan angka 4 pada kolom 'Banyak Siswa'.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data secara langsung dari tabel yang disediakan untuk menemukan nilai yang sesuai.. Bukti: Berapa jumlah siswa yang memilih Aplikasi Among Us! sebagai permainan favoritnya?; Tabel 6.3 Tabel Jenis Aplikasi Online \| Among Us! \| 4
- Dimensi pengetahuan `classify/factual`: Soal ini menguji kemampuan membaca data faktual yang tersaji dalam tabel frekuensi.. Bukti: Tabel 6.3 Tabel Jenis Aplikasi Online; Among Us! \| 4
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana karena hanya memerlukan pembacaan langsung dari tabel tanpa manipulasi data atau perhitungan.. Bukti: Berapa jumlah siswa yang memilih Aplikasi Among Us! sebagai permainan favoritnya?; Tabel 6.3 Tabel Jenis Aplikasi Online \| Among Us! \| 4

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca tabel frekuensi sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah sangat familiar dengan membaca tabel frekuensi sederhana sebagai bagian dari materi statistika dasar. |

Run 2 — solusi: Berdasarkan Tabel 6.3, baris 'Among Us!' menunjukkan angka 4 pada kolom 'Banyak Siswa'.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk membaca data spesifik dari tabel frekuensi yang sudah disediakan, yang merupakan proses pengambilan informasi langsung.. Bukti: Berapa jumlah siswa yang memilih Aplikasi Among Us! sebagai permainan favoritnya?
- Dimensi pengetahuan `classify/factual`: Siswa perlu memahami struktur tabel frekuensi untuk mengidentifikasi nilai yang berkorespondensi dengan kategori tertentu.. Bukti: Tabel 6.3 Tabel Jenis Aplikasi Online
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya memerlukan pencarian data pada baris yang tepat di tabel yang sudah tersedia tanpa manipulasi atau interpretasi kompleks.. Bukti: Berapa jumlah siswa yang memilih Aplikasi Among Us! sebagai permainan favoritnya?; Tabel 6.3 Tabel Jenis Aplikasi Online

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca tabel frekuensi sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena melibatkan pembacaan data dasar yang merupakan kompetensi awal dalam statistika. |

Run 3 — solusi: Berdasarkan Tabel 6.3, baris 'Among Us!' menunjukkan angka 4 pada kolom 'Banyak Siswa'.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk membaca data spesifik dari tabel frekuensi yang disediakan, yang merupakan proses pengambilan informasi langsung.. Bukti: Berapa jumlah siswa yang memilih Aplikasi Among Us! sebagai permainan favoritnya?; Tabel 6.3 Tabel Jenis Aplikasi Online \| Among Us! \| 4
- Dimensi pengetahuan `classify/factual`: Siswa perlu memahami struktur tabel frekuensi untuk mengidentifikasi kategori dan nilai frekuensi yang bersesuaian.. Bukti: Tabel 6.3 Tabel Jenis Aplikasi Online; Berapa jumlah siswa yang memilih Aplikasi Among Us! sebagai permainan favoritnya?
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana karena hanya memerlukan pembacaan data langsung dari tabel tanpa manipulasi atau interpretasi kompleks.. Bukti: Tabel 6.3 Tabel Jenis Aplikasi Online; Berapa jumlah siswa yang memilih Aplikasi Among Us! sebagai permainan favoritnya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca tabel frekuensi sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena merupakan keterampilan dasar dalam statistika deskriptif awal. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Macam-Macam Data
Tipe soal: multiple_choice
Stimulus: -
Soal: Siswa kelas 7B dari Sekolah Indonesia Raya memiliki pertanyaan:
a. Berapakah aplikasi permainan online yang ada dalam gawai kalian?
b. Permainan online manakah yang menjadi favorit kalian?
Mereka mengumpulkan datanya, lalu menampilkan data tersebut dalam tabel frekuensi dan menggambar diagram batangnya untuk menunjukkan sebaran datanya.

Tabel 6.2 Tabel Banyak Aplikasi Online

| Banyaknya aplikasi permainan online dalam gawai | Banyak Siswa |
|---|---|
| 0 | 1 |
| 1 | 3 |
| 2 | 7 |
| 3 | 10 |
| 4 | 8 |
| 5 | 2 |
| 6 | 1 |

Gambar 6.9 Diagram Banyak Aplikasi Online

Tabel 6.3 Tabel Jenis Aplikasi Online

| Aplikasi Permainan Online Favorit | Banyak Siswa |
|---|---|
| Mobile Legends | 12 |
| Wormszone.io | 6 |
| PUBG Mobile | 5 |
| Among Us! | 4 |
| Hago | 3 |
| Candy Crush Saga | 1 |

Gambar 6.10 Diagram Jenis Aplikasi Online

Dari kedua data dan tabel di atas, tentukanlah pertanyaan mana saja yang bisa dijawab melalui informasi di atas. Jika dapat di jawab, tentukanlah jawabannya. Jika pertanyaan di bawah ini tidak dapat dijawab, mengapa dan informasi apakah yang kalian perlukan agar kalian bisa menjawab pertanyaan tersebut.

Berapa jumlah siswa yang memilih Aplikasi Among Us! sebagai permainan favoritnya?
Pilihan: A. 3 siswa
B. 6 siswa
C. 5 siswa
D. 4 siswa
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "factual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 41. Soal `14b9e394a67f66b7a708ee15`

Keterangan pada sumbu horizontal menyebutkan urutan bulan. Angka 7 artinya bulan ke-7 atau Juli, sedangkan angka 8 menunjukkan bulan ke-8 atau Agustus dan seterusnya.<br><br>Penggunaan Kuota Internet untuk PJJ<br><br>Jika kalian mendapatkan bantuan kuota internet 8 GB dari Kemdikbud, pada bulan keberapakah kalian perlu membeli tambahan kuota?

| Opsi | Isi |
|---|---|
| A | Bulan ke-9, ke-10, dan ke-11 |
| B | Bulan ke-10 dan ke-11 |
| C | Bulan ke-10 saja |
| D | Bulan ke-7 dan ke-8 |

![Gambar sumber soal 41](<../images/kelas7_panduan_siswa_kelas7.pdf-0224-07.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Bantuan kuota adalah 8 GB. Perlu membeli tambahan jika penggunaan > 8 GB. Berdasarkan diagram: bulan 10 (10 GB) dan bulan 11 (9 GB) melebihi 8 GB.
Gambar sumber: images/kelas7_panduan_siswa_kelas7.pdf-0224-07.png. Transkripsi visual: Diagram batang menunjukkan penggunaan kuota internet (sumbu Y, 0-12 GB) untuk bulan ke-7 sampai ke-12 (sumbu X). Tinggi batang: bulan 7=3 GB, bulan 8=5 GB, bulan 9=8 GB, bulan 10=10 GB, bulan 11=9 GB, bulan 12=7 GB.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c6852dbdfbcfe72f0ae374d2b02efa28d7b934cccceac13c4a6b187558625417`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2965 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2967 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3013 |

Run 1 — solusi: Bantuan kuota adalah 8 GB. Perlu membeli tambahan jika penggunaan > 8 GB. Berdasarkan diagram: bulan 10 (10 GB) dan bulan 11 (9 GB) melebihi 8 GB.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasikan data dari diagram batang dan membandingkan nilai setiap batang dengan ambang batas 8 GB untuk menentukan bulan mana yang melebihi batas tersebut.. Bukti: Jika kalian mendapatkan bantuan kuota internet 8 GB; pada bulan keberapakah kalian perlu membeli tambahan kuota?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang cara membaca dan menginterpretasikan data yang disajikan dalam bentuk diagram batang.. Bukti: Penggunaan Kuota Internet untuk PJJ; Angka 7 artinya bulan ke-7 atau Juli
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan pembacaan langsung dari diagram batang dan perbandingan sederhana dengan satu nilai ambang batas (8 GB).. Bukti: Jika kalian mendapatkan bantuan kuota internet 8 GB; pada bulan keberapakah kalian perlu membeli tambahan kuota?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram batang dan membandingkan bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah terbiasa membaca data dari grafik sederhana. Tugas membandingkan nilai batang dengan angka tertentu adalah prosedur rutin. |

Run 2 — solusi: Bantuan kuota adalah 8 GB. Siswa perlu membeli tambahan jika penggunaan > 8 GB. Berdasarkan diagram, bulan ke-10 (10 GB) dan bulan ke-11 (9 GB) memiliki penggunaan di atas 8 GB.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasikan data dari diagram batang dan membandingkan nilai setiap batang dengan ambang batas 8 GB untuk menentukan bulan mana yang melebihi kuota.. Bukti: pada bulan keberapakah kalian perlu membeli tambahan kuota?; Jika kalian mendapatkan bantuan kuota internet 8 GB
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang cara membaca dan menginterpretasikan data yang disajikan dalam bentuk diagram batang.. Bukti: Penggunaan Kuota Internet untuk PJJ; Diagram batang
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan pembacaan data langsung dari diagram batang dan perbandingan sederhana dengan satu nilai ambang batas (8 GB).. Bukti: Jika kalian mendapatkan bantuan kuota internet 8 GB; pada bulan keberapakah kalian perlu membeli tambahan kuota?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram batang dan membandingkan bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah terbiasa membaca diagram batang sederhana dan melakukan perbandingan nilai, sehingga tugas ini merupakan prosedur rutin. |

Run 3 — solusi: Bantuan kuota adalah 8 GB. Siswa perlu membeli tambahan jika pemakaian > 8 GB. Berdasarkan diagram, bulan ke-10 (10 GB) dan bulan ke-11 (9 GB) memiliki nilai > 8 GB. Bulan ke-9 tepat 8 GB, sehingga tidak perlu tambahan.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasikan data dari diagram batang dan membandingkan nilai setiap batang dengan ambang batas 8 GB untuk menentukan bulan mana yang melebihi kuota tersebut.. Bukti: pada bulan keberapakah kalian perlu membeli tambahan kuota?; Jika kalian mendapatkan bantuan kuota internet 8 GB
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang cara membaca dan menginterpretasikan data yang disajikan dalam bentuk diagram batang.. Bukti: Penggunaan Kuota Internet untuk PJJ; Diagram batang
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu melakukan perbandingan sederhana antara nilai pada diagram batang dengan nilai ambang batas (8 GB) yang diberikan.. Bukti: Jika kalian mendapatkan bantuan kuota internet 8 GB; pada bulan keberapakah kalian perlu membeli tambahan kuota?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram batang dan membandingkan bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah terbiasa membaca diagram batang sederhana dan melakukan perbandingan nilai, sehingga soal ini sesuai dengan tingkat kemampuan mereka. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Diagram dalam Statistika
Tipe soal: multiple_choice
Stimulus: -
Soal: Keterangan pada sumbu horizontal menyebutkan urutan bulan. Angka 7 artinya bulan ke-7 atau Juli, sedangkan angka 8 menunjukkan bulan ke-8 atau Agustus dan seterusnya.

Penggunaan Kuota Internet untuk PJJ

Jika kalian mendapatkan bantuan kuota internet 8 GB dari Kemdikbud, pada bulan keberapakah kalian perlu membeli tambahan kuota?
Pilihan: A. Bulan ke-9, ke-10, dan ke-11
B. Bulan ke-10 dan ke-11
C. Bulan ke-10 saja
D. Bulan ke-7 dan ke-8
Transkripsi visual: Diagram batang menunjukkan penggunaan kuota internet (sumbu Y, 0-12 GB) untuk bulan ke-7 sampai ke-12 (sumbu X). Tinggi batang: bulan 7=3 GB, bulan 8=5 GB, bulan 9=8 GB, bulan 10=10 GB, bulan 11=9 GB, bulan 12=7 GB.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 42. Soal `425d19fac3fc51700ad86dba`

Diagram di bawah menjelaskan banyaknya mobil berdasarkan warnanya di tempat parkir sebuah taman.<br><br>Mobil warna apakah yang paling banyak ditemui?

| Opsi | Isi |
|---|---|
| A | Merah |
| B | Lainnya |
| C | Putih |
| D | Hitam |

![Gambar sumber soal 42](<../images/kelas7_panduan_siswa_kelas7.pdf-0228-09.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Mengamati tinggi batang pada diagram, batang untuk warna Hitam adalah yang paling tinggi dengan nilai 26.
Gambar sumber: images/kelas7_panduan_siswa_kelas7.pdf-0228-09.png. Transkripsi visual: Diagram batang menunjukkan jumlah mobil berdasarkan warna di sumbu horizontal (Merah, Hitam, Putih, Hijau, Kuning, Lainnya) dan jumlah mobil di sumbu vertikal (skala 2-26). Batang Hitam mencapai angka 26, Putih mencapai 22, Merah mencapai 15, Lainnya mencapai 8, Hijau mencapai 6, Kuning mencapai 5.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5021c3be17236ae367c0c38ddf6c93d6338d709a599fbb39fc3195d339e84df4`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2706 |
| 2 | success | valid / verified | knowing | factual | Easy | 2703 |
| 3 | success | valid / verified | knowing | factual | Easy | 2780 |

Run 1 — solusi: Mengamati tinggi batang pada diagram, batang untuk warna Hitam adalah yang paling tinggi dengan nilai 26.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data secara langsung dari diagram batang untuk mengidentifikasi nilai maksimum.. Bukti: Mobil warna apakah yang paling banyak ditemui?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman dasar tentang cara membaca informasi dari representasi visual (diagram batang).. Bukti: Diagram di bawah menjelaskan banyaknya mobil berdasarkan warnanya
- Intended difficulty `classify/Easy`: Tugas ini sangat mendasar, hanya memerlukan identifikasi visual langsung tanpa perhitungan atau manipulasi data.. Bukti: Mobil warna apakah yang paling banyak ditemui?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram batang sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 7 diharapkan sudah sangat familiar dengan pembacaan diagram batang sederhana sebagai bagian dari literasi data dasar. |

Run 2 — solusi: Mengamati tinggi batang pada diagram, batang tertinggi adalah warna Hitam dengan nilai 26.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data secara langsung dari diagram batang untuk mengidentifikasi nilai tertinggi.. Bukti: Mobil warna apakah yang paling banyak ditemui?; batang Hitam paling tinggi (26)
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman dasar tentang cara membaca informasi dari representasi visual (diagram batang).. Bukti: Diagram di bawah menjelaskan banyaknya mobil berdasarkan warnanya
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana, hanya memerlukan pembacaan visual langsung tanpa perhitungan atau manipulasi data.. Bukti: Mobil warna apakah yang paling banyak ditemui?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram batang sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 7 diharapkan sudah sangat familiar dengan pembacaan diagram batang sederhana sebagai bagian dari literasi data dasar. |

Run 3 — solusi: Mengamati tinggi batang pada diagram, batang dengan label 'Hitam' memiliki tinggi paling besar (sejajar dengan angka 26 pada sumbu Y), sehingga mobil warna Hitam adalah yang paling banyak.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data visual secara langsung untuk mengidentifikasi nilai maksimum dari diagram batang tanpa melakukan perhitungan atau manipulasi data.. Bukti: Mobil warna apakah yang paling banyak ditemui?; Diagram di bawah menjelaskan banyaknya mobil berdasarkan warnanya
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang cara membaca dan menginterpretasikan informasi yang disajikan dalam bentuk diagram batang sederhana.. Bukti: Diagram di bawah menjelaskan banyaknya mobil berdasarkan warnanya
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan identifikasi visual langsung terhadap batang tertinggi tanpa proses perhitungan atau analisis kompleks.. Bukti: Mobil warna apakah yang paling banyak ditemui?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram batang sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 7 sudah sangat familiar dengan pembacaan diagram batang sederhana sebagai bagian dari literasi data dasar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Diagram dalam Statistika
Tipe soal: multiple_choice
Stimulus: -
Soal: Diagram di bawah menjelaskan banyaknya mobil berdasarkan warnanya di tempat parkir sebuah taman.

Mobil warna apakah yang paling banyak ditemui?
Pilihan: A. Merah
B. Lainnya
C. Putih
D. Hitam
Transkripsi visual: Diagram batang menunjukkan jumlah mobil berdasarkan warna di sumbu horizontal (Merah, Hitam, Putih, Hijau, Kuning, Lainnya) dan jumlah mobil di sumbu vertikal (skala 2-26). Batang Hitam mencapai angka 26, Putih mencapai 22, Merah mencapai 15, Lainnya mencapai 8, Hijau mencapai 6, Kuning mencapai 5.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "factual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 43. Soal `f146ba7240b44e0020ce164a`

Banyak peneliti bidang sains mengkhawatirkan level gas CO2 pada atmosfer bumi yang mengakibatkan masalah perubahan iklim. Diagram di bawah ini menunjukkan level emisi CO2 pada tahun 1990 dan 1998. Batang dengan warna terang menunjukkan tahun 1990 dan warna gelap menunjukkan tahun 1998.<br><br>Pada diagram, kita bisa melihat bahwa di negara USA mengalami kenaikan level emisi CO2 dari tahun 1990 ke tahun 1998 sebesar 11%.<br><br>Level emisi CO2 pada tahun 1990 di USA = 6049 juta ton Level emisi CO2 pada tahun 1998 di USA = 6727 juta ton Kenaikan level emisi CO2 di USA = 6727 – 6049 – 678 juta ton Maka persentase kenaikan level emisi CO2 di USA =<br><br>Berapakah persentase perubahan level emisi CO2 untuk negara Jerman?

| Opsi | Isi |
|---|---|
| A | Turun sekitar 11% |
| B | Naik sekitar 19% |
| C | Turun sekitar 18,5% |
| D | Turun sekitar 16% |

![Gambar sumber soal 43](<../images/kelas7_panduan_siswa_kelas7.pdf-0233-06.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Emisi 1990 = 1209, Emisi 1998 = 1020. Penurunan = 1209 - 1020 = 189. Persentase penurunan = (189 / 1209) * 100% ≈ 15,63%, dibulatkan menjadi 16%.
Gambar sumber: images/kelas7_panduan_siswa_kelas7.pdf-0233-06.png. Transkripsi visual: Diagram batang menunjukkan emisi CO2 (juta ton) untuk beberapa negara pada tahun 1990 (batang putih) dan 1998 (batang hitam). Untuk Jerman, nilai tahun 1990 adalah 1209 dan nilai tahun 1998 adalah 1020.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ad7fef6a0a0d898edeb7dbaf1caf919ff554befdc3cf306fe5d7a6e88ca87d9a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3278 |
| 2 | success | valid / verified | applying | procedural | Medium | 3160 |
| 3 | success | valid / verified | applying | procedural | Medium | 3125 |

Run 1 — solusi: Emisi 1990 = 1209, Emisi 1998 = 1020. Penurunan = 1209 - 1020 = 189. Persentase penurunan = (189 / 1209) * 100% ≈ 15,63%, dibulatkan menjadi 16%.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur persentase perubahan yang telah dimodelkan pada contoh soal (USA) ke data baru (Jerman). Ini adalah penerapan prosedur rutin.. Bukti: Berapakah persentase perubahan level emisi CO2 untuk negara Jerman?; Level emisi CO2 pada tahun 1990 di USA = 6049 juta ton Level emisi CO2 pada tahun 1998 di USA = 6727 juta ton Kenaikan level emisi CO2 di USA = 6727 – 6049 – 678 juta ton Maka persentase kenaikan level emisi CO2 di USA =
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma atau teknik perhitungan persentase perubahan yang sudah dipelajari.. Bukti: Maka persentase kenaikan level emisi CO2 di USA =; Berapakah persentase perubahan level emisi CO2 untuk negara Jerman?
- Intended difficulty `classify/Medium`: Soal ini meminta siswa mengikuti langkah-langkah yang sudah dicontohkan di bagian stem soal (scaffolded). Siswa hanya perlu mengekstrak data dari grafik dan melakukan operasi aritmatika dasar.. Bukti: Berapakah persentase perubahan level emisi CO2 untuk negara Jerman?; 1209 − 1020)/1209 × 100% ≈ 16%

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmatika dasar, konsep persentase, dan kemampuan membaca data dari diagram batang. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun prosedurnya rutin, soal ini memerlukan ekstraksi data dari grafik dan pemahaman konsep persentase perubahan yang sesuai untuk kelas 7. |

Run 2 — solusi: Emisi Jerman 1990 = 1209, 1998 = 1020. Penurunan = 1209 - 1020 = 189. Persentase penurunan = (189 / 1209) * 100% ≈ 15,63%, dibulatkan menjadi 16%.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur yang tepat untuk menghitung persentase perubahan (selisih dibagi nilai awal) berdasarkan data yang diekstrak dari diagram.. Bukti: Berapakah persentase perubahan level emisi CO2 untuk negara Jerman?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung persentase perubahan menggunakan data numerik yang diberikan.. Bukti: Maka persentase kenaikan level emisi CO2 di USA =; Berapakah persentase perubahan level emisi CO2 untuk negara Jerman?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan beberapa langkah rutin: membaca data dari grafik, menghitung selisih, dan menghitung persentase perubahan. Ini bukan sekadar membaca data langsung (Easy), tetapi juga tidak memerlukan strategi nonrutin yang kompleks (Hard).. Bukti: Berapakah persentase perubahan level emisi CO2 untuk negara Jerman?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmatika dasar (pengurangan) dan konsep persentase perubahan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah mempelajari rasio dan persentase. Mengaplikasikan rumus persentase perubahan pada data diagram batang adalah tugas yang sesuai dengan tingkat kognitif dan kurikulum kelas 7. |

Run 3 — solusi: Emisi 1990 = 1209, Emisi 1998 = 1020. Penurunan = 1209 - 1020 = 189. Persentase penurunan = (189 / 1209) * 100% ≈ 15,63% dibulatkan menjadi 16%.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur persentase perubahan yang tepat dan menerapkannya pada data yang diekstraksi dari diagram.. Bukti: Berapakah persentase perubahan level emisi CO2 untuk negara Jerman?
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penggunaan algoritma atau teknik perhitungan persentase perubahan (selisih dibagi nilai awal) yang merupakan prosedur standar.. Bukti: Berapakah persentase perubahan level emisi CO2 untuk negara Jerman?
- Intended difficulty `classify/Medium`: Soal ini memerlukan beberapa langkah rutin: membaca data dari diagram, menghitung selisih, dan menghitung persentase. Ini adalah tugas yang familiar bagi siswa kelas 7.. Bukti: Berapakah persentase perubahan level emisi CO2 untuk negara Jerman?; 1209; 1020

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang diagram batang dan konsep persentase perubahan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Tugas ini sesuai untuk kelas 7 karena menggabungkan literasi data (membaca diagram) dengan aritmatika persentase yang merupakan kurikulum standar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Diagram Batang
Tipe soal: multiple_choice
Stimulus: -
Soal: Banyak peneliti bidang sains mengkhawatirkan level gas CO2 pada atmosfer bumi yang mengakibatkan masalah perubahan iklim. Diagram di bawah ini menunjukkan level emisi CO2 pada tahun 1990 dan 1998. Batang dengan warna terang menunjukkan tahun 1990 dan warna gelap menunjukkan tahun 1998.

Pada diagram, kita bisa melihat bahwa di negara USA mengalami kenaikan level emisi CO2 dari tahun 1990 ke tahun 1998 sebesar 11%.

Level emisi CO2 pada tahun 1990 di USA = 6049 juta ton Level emisi CO2 pada tahun 1998 di USA = 6727 juta ton Kenaikan level emisi CO2 di USA = 6727 – 6049 – 678 juta ton Maka persentase kenaikan level emisi CO2 di USA =

Berapakah persentase perubahan level emisi CO2 untuk negara Jerman?
Pilihan: A. Turun sekitar 11%
B. Naik sekitar 19%
C. Turun sekitar 18,5%
D. Turun sekitar 16%
Transkripsi visual: Diagram batang menunjukkan emisi CO2 (juta ton) untuk beberapa negara pada tahun 1990 (batang putih) dan 1998 (batang hitam). Untuk Jerman, nilai tahun 1990 adalah 1209 dan nilai tahun 1998 adalah 1020.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 44. Soal `7ea9980573af6cf5eee574ca`

Jawablah pertanyaan berikut berdasarkan diagram batang ganda di bawah ini yang menunjukkan perolehan medali emas, perak, dan perunggu Indonesia dalam ajang Pesta Olahraga Se-Asia Tenggara SEA Games.<br><br>Perolehan Medali Indonesia di SEA Games<br><br>Pada SEA Games tahun berapakah Indonesia memperoleh medali emas paling banyak?

| Opsi | Isi |
|---|---|
| A | 2019 |
| B | 2013 |
| C | 2017 |
| D | 2011 |

![Gambar sumber soal 44](<../images/kelas7_panduan_siswa_kelas7.pdf-0247-01.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Identifikasi batang berwarna oranye (Emas) untuk setiap tahun: 2011 (182), 2013 (64), 2015 (47), 2017 (38), 2019 (72). Nilai tertinggi adalah 182 yang terjadi pada tahun 2011.
Gambar sumber: images/kelas7_panduan_siswa_kelas7.pdf-0247-01.png. Transkripsi visual: Diagram batang horizontal menunjukkan perolehan medali Indonesia di SEA Games tahun 2011, 2013, 2015, 2017, dan 2019. Setiap tahun memiliki tiga batang: Emas (oranye), Perak (hijau), dan Perunggu (ungu). Nilai medali emas untuk setiap tahun adalah: 2011 (182), 2013 (64), 2015 (47), 2017 (38), 2019 (72).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d100b7ec317acad5e24c29d6f77155837d8c3b9155b1043c220fa8a549c8aebb`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2903 |
| 2 | success | valid / verified | knowing | factual | Easy | 2918 |
| 3 | success | valid / verified | knowing | factual | Easy | 2906 |

Run 1 — solusi: Identifikasi batang berwarna oranye (Emas) untuk setiap tahun: 2011 (182), 2013 (64), 2015 (47), 2017 (38), 2019 (72). Nilai tertinggi adalah 182 yang terjadi pada tahun 2011.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data secara langsung dari diagram batang tanpa melakukan perhitungan atau manipulasi data.. Bukti: Pada SEA Games tahun berapakah Indonesia memperoleh medali emas paling banyak?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang cara membaca dan menginterpretasikan informasi dari diagram batang.. Bukti: diagram batang ganda; Perolehan Medali Indonesia di SEA Games
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung, hanya memerlukan identifikasi visual sederhana pada satu kategori data (emas) untuk membandingkan nilai.. Bukti: diagram batang ganda; Pada SEA Games tahun berapakah Indonesia memperoleh medali emas paling banyak?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram batang dan membandingkan bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu membaca data dari diagram batang dengan mudah sebagai bagian dari literasi data dasar. |

Run 2 — solusi: Identifikasi batang berwarna oranye (Emas) untuk setiap tahun: 2011=182, 2013=64, 2015=47, 2017=38, 2019=72. Nilai terbesar adalah 182 yang terjadi pada tahun 2011.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data secara langsung dari diagram batang tanpa melakukan operasi matematika tambahan atau interpretasi kompleks.. Bukti: Pada SEA Games tahun berapakah Indonesia memperoleh medali emas paling banyak?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang cara membaca dan menginterpretasikan data yang disajikan dalam bentuk diagram batang.. Bukti: diagram batang ganda; Perolehan Medali Indonesia di SEA Games
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (direct retrieval) dengan beban kognitif yang rendah, cocok untuk tingkat kesulitan mudah.. Bukti: Pada SEA Games tahun berapakah Indonesia memperoleh medali emas paling banyak?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram batang sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah familiar dengan pembacaan data statistik dasar seperti diagram batang. |

Run 3 — solusi: Identifikasi batang berwarna oranye (Emas) untuk setiap tahun: 2011 (182), 2013 (64), 2015 (47), 2017 (38), 2019 (72). Nilai terbesar adalah 182 yang terjadi pada tahun 2011.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data secara langsung dari diagram batang dan membandingkan nilai-nilai tersebut untuk menemukan nilai maksimum.. Bukti: Pada SEA Games tahun berapakah Indonesia memperoleh medali emas paling banyak?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang cara membaca dan menginterpretasikan data yang disajikan dalam bentuk diagram batang.. Bukti: diagram batang ganda
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung, hanya memerlukan pembacaan data visual sederhana tanpa manipulasi atau perhitungan kompleks.. Bukti: Pada SEA Games tahun berapakah Indonesia memperoleh medali emas paling banyak?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram batang dan membandingkan bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena merupakan keterampilan dasar dalam statistika deskriptif awal. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Diagram Batang
Tipe soal: multiple_choice
Stimulus: -
Soal: Jawablah pertanyaan berikut berdasarkan diagram batang ganda di bawah ini yang menunjukkan perolehan medali emas, perak, dan perunggu Indonesia dalam ajang Pesta Olahraga Se-Asia Tenggara SEA Games.

Perolehan Medali Indonesia di SEA Games

Pada SEA Games tahun berapakah Indonesia memperoleh medali emas paling banyak?
Pilihan: A. 2019
B. 2013
C. 2017
D. 2011
Transkripsi visual: Diagram batang horizontal menunjukkan perolehan medali Indonesia di SEA Games tahun 2011, 2013, 2015, 2017, dan 2019. Setiap tahun memiliki tiga batang: Emas (oranye), Perak (hijau), dan Perunggu (ungu). Nilai medali emas untuk setiap tahun adalah: 2011 (182), 2013 (64), 2015 (47), 2017 (38), 2019 (72).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "factual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 45. Soal `b1aa54c53e0576c10fa47136`

Diagram lingkaran menunjukkan sebaran jumlah suara yang diterima tiap kandidat dalam pemilihan ketua OSIS di SMP Pancasila.<br><br>Hitunglah sudut pusat dari setiap juring pada diagram ini.

| Opsi | Isi |
|---|---|
| A | Danu 144°, Rizki 88°, Noer 56°, Karno 40°, Indah 32° |
| B | Danu 72°, Rizki 72°, Noer 72°, Karno 72°, Indah 72° |
| C | Danu 40°, Rizki 24,4°, Noer 15,6°, Karno 11,1°, Indah 8,9° |
| D | Danu 180°, Rizki 110°, Noer 70°, Karno 50°, Indah 40° |

![Gambar sumber soal 45](<../images/kelas7_panduan_siswa_kelas7.pdf-0239-07.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Total suara = 18 + 11 + 7 + 5 + 4 = 45. Sudut pusat = (suara/45) * 360 derajat = suara * 8 derajat. Danu: 18*8=144, Rizki: 11*8=88, Noer: 7*8=56, Karno: 5*8=40, Indah: 4*8=32.
Gambar sumber: images/kelas7_panduan_siswa_kelas7.pdf-0239-07.png. Transkripsi visual: Diagram lingkaran menunjukkan data suara pemilihan ketua OSIS: Danu (18), Rizki (11), Noer (7), Karno (5), Indah (4).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `83d0e7cc69a4c7ac902d58955d36a9ad6e9bd049893c0df28516f1ffaa1cbb0a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2989 |
| 2 | success | valid / verified | applying | procedural | Medium | 3062 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2956 |

Run 1 — solusi: Total suara = 18+11+7+5+4 = 45. Sudut pusat = (suara/45) * 360 derajat = suara * 8 derajat. Danu: 18*8=144, Rizki: 11*8=88, Noer: 7*8=56, Karno: 5*8=40, Indah: 4*8=32.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur rutin untuk mengubah data frekuensi menjadi proporsi sudut dalam lingkaran (360 derajat).. Bukti: Hitunglah sudut pusat dari setiap juring pada diagram ini.
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma atau teknik perhitungan (prosedural) untuk mengonversi data ke dalam representasi sudut.. Bukti: Diagram lingkaran menunjukkan sebaran jumlah suara; Hitunglah sudut pusat
- Intended difficulty `classify/Medium`: Soal ini melibatkan beberapa langkah rutin (menjumlahkan total, menghitung proporsi, mengalikan dengan 360) yang saling terkait, namun prosedurnya sangat familiar bagi siswa kelas 7.. Bukti: Hitunglah sudut pusat dari setiap juring; Danu (18), Rizki (11), Noer (7), Karno (5), Indah (4)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan bulat, konsep pecahan/rasio, dan konsep sudut satu putaran penuh (360 derajat). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena menguji pemahaman dasar tentang interpretasi data dalam diagram lingkaran yang merupakan standar kurikulum. |

Run 2 — solusi: Total suara = 18+11+7+5+4 = 45. Sudut pusat = (suara/total) * 360°. Danu: (18/45)*360° = 144°. Rizki: (11/45)*360° = 88°. Noer: (7/45)*360° = 56°. Karno: (5/45)*360° = 40°. Indah: (4/45)*360° = 32°.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur rutin untuk mengubah data frekuensi menjadi proporsi sudut dalam lingkaran (360 derajat). Ini adalah penerapan konsep rasio dan proporsi yang standar.. Bukti: Hitunglah sudut pusat dari setiap juring; Diagram lingkaran menunjukkan sebaran jumlah suara
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau prosedur perhitungan sudut juring berdasarkan data frekuensi.. Bukti: Hitunglah sudut pusat dari setiap juring; suara/45 × 360°
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah rutin yang saling terkait: menjumlahkan total data, menghitung proporsi untuk setiap kategori, dan mengalikan dengan 360 derajat. Meskipun prosedurnya rutin, terdapat beban kalkulasi yang cukup untuk siswa kelas 7.. Bukti: Hitunglah sudut pusat dari setiap juring; Danu (18), Rizki (11), Noer (7), Karno (5), Indah (4)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan bulat, konsep pecahan/rasio, dan pemahaman bahwa satu lingkaran penuh adalah 360 derajat. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena melibatkan pengolahan data statistik sederhana dan konversi ke representasi visual (sudut). |

Run 3 — solusi: Total suara = 18+11+7+5+4 = 45. Sudut pusat = (suara/45) * 360 derajat = suara * 8 derajat. Danu: 18*8=144, Rizki: 11*8=88, Noer: 7*8=56, Karno: 5*8=40, Indah: 4*8=32.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur proporsi untuk mengubah data frekuensi menjadi sudut dalam lingkaran, yang merupakan tugas rutin dalam topik penyajian data.. Bukti: Hitunglah sudut pusat dari setiap juring pada diagram ini.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara bagian (suara kandidat) dan keseluruhan (total suara) dalam representasi diagram lingkaran.. Bukti: Diagram lingkaran menunjukkan sebaran jumlah suara
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah rutin yang saling terkait: menjumlahkan total data, menentukan rasio, dan mengalikan dengan 360 derajat untuk setiap kategori.. Bukti: Hitunglah sudut pusat dari setiap juring pada diagram ini.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan bulat, konsep pecahan/rasio, dan pemahaman bahwa satu lingkaran penuh adalah 360 derajat. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu melakukan konversi data ke derajat pada diagram lingkaran sebagai bagian dari materi statistika dasar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4627`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur rutin untuk mengubah data frekuensi menjadi proporsi sudut dalam lingkaran (360 derajat).
- Dimensi pengetahuan `procedural`: Siswa menggunakan algoritma atau teknik perhitungan (prosedural) untuk mengonversi data ke dalam representasi sudut.
- Intended difficulty `Medium`: Soal ini melibatkan beberapa langkah rutin yang saling terkait (menjumlahkan total, menghitung proporsi, mengalikan dengan 360), namun prosedurnya sangat familiar bagi siswa kelas 7.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan bulat, konsep pecahan/rasio, dan konsep sudut satu putaran penuh (360 derajat). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena menguji pemahaman dasar tentang interpretasi data dalam diagram lingkaran yang merupakan standar kurikulum. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Diagram Lingkaran
Tipe soal: multiple_choice
Stimulus: -
Soal: Diagram lingkaran menunjukkan sebaran jumlah suara yang diterima tiap kandidat dalam pemilihan ketua OSIS di SMP Pancasila.

Hitunglah sudut pusat dari setiap juring pada diagram ini.
Pilihan: A. Danu 144°, Rizki 88°, Noer 56°, Karno 40°, Indah 32°
B. Danu 72°, Rizki 72°, Noer 72°, Karno 72°, Indah 72°
C. Danu 40°, Rizki 24,4°, Noer 15,6°, Karno 11,1°, Indah 8,9°
D. Danu 180°, Rizki 110°, Noer 70°, Karno 50°, Indah 40°
Transkripsi visual: Diagram lingkaran menunjukkan data suara pemilihan ketua OSIS: Danu (18), Rizki (11), Noer (7), Karno (5), Indah (4).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 46. Soal `45ffe36fb7707115897e6fae`

Dari sebuah survei mengenai panjang password yang digunakan untuk akun email siswa, diperoleh hasil sebagai berikut:<br><br>Panjang Password Email<br><br>Ada berapa macam panjang password email siswa di kelas ini?

| Opsi | Isi |
|---|---|
| A | 9 macam |
| B | 3 macam |
| C | 40 macam |
| D | 4 macam |

![Gambar sumber soal 46](<../images/kelas7_panduan_siswa_kelas7.pdf-0245-05.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Diagram lingkaran tersebut memiliki 4 sektor yang masing-masing mewakili kategori panjang password yang berbeda, yaitu 6-angka, 7-angka, 8-angka, dan 9-angka. Jadi, terdapat 4 macam panjang password.
Gambar sumber: images/kelas7_panduan_siswa_kelas7.pdf-0245-05.png. Transkripsi visual: Diagram lingkaran menunjukkan empat sektor yang mewakili kategori panjang password: 7-angka (nilai 3), 9-angka (nilai 5), 6-angka (nilai 12), dan 8-angka (nilai 20).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `457201281f071ae3bbf33b30ec98bf99444b4d26a7a8c524b7b583aac96e67cd`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2837 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2821 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2841 |

Run 1 — solusi: Diagram lingkaran tersebut memiliki 4 sektor yang masing-masing mewakili kategori panjang password yang berbeda, yaitu 6-angka, 7-angka, 8-angka, dan 9-angka. Jadi, terdapat 4 macam panjang password.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi dan menghitung jumlah kategori yang disajikan dalam diagram lingkaran. Ini adalah proses membaca data secara langsung.. Bukti: Ada berapa macam panjang password email siswa di kelas ini?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami struktur diagram lingkaran sebagai representasi data kategorikal untuk menentukan jumlah kategori yang ada.. Bukti: Diagram lingkaran; Ada berapa macam panjang password
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar karena hanya meminta siswa untuk menghitung jumlah sektor atau kategori yang terlihat jelas pada diagram lingkaran tanpa perlu melakukan perhitungan atau interpretasi kompleks.. Bukti: Ada berapa macam panjang password email siswa di kelas ini?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram lingkaran sederhana dan menghitung jumlah kategori. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah terbiasa membaca data dari diagram lingkaran. Soal ini hanya menuntut pengenalan visual terhadap kategori yang ada. |

Run 2 — solusi: Diagram lingkaran menunjukkan empat sektor yang berbeda, masing-masing mewakili kategori panjang password: 6-angka, 7-angka, 8-angka, dan 9-angka. Jadi, terdapat 4 macam panjang password.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi dan menghitung jumlah kategori yang disajikan dalam diagram lingkaran. Ini adalah proses membaca data secara langsung.. Bukti: Ada berapa macam panjang password email siswa di kelas ini?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami struktur diagram lingkaran sebagai representasi data kategorikal untuk mengidentifikasi jumlah kategori yang ada.. Bukti: Diagram lingkaran
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana karena hanya meminta penghitungan jumlah kategori yang terlihat jelas pada diagram lingkaran tanpa perlu melakukan perhitungan atau interpretasi kompleks.. Bukti: Ada berapa macam panjang password email siswa di kelas ini?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca label kategori pada diagram lingkaran. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tingkat kesulitan ini sesuai untuk kelas 7 karena hanya melibatkan pengenalan dasar terhadap penyajian data visual tanpa manipulasi data. |

Run 3 — solusi: Diagram lingkaran menampilkan empat kategori panjang password yang berbeda, yaitu 6-angka, 7-angka, 8-angka, dan 9-angka. Menghitung jumlah kategori tersebut memberikan hasil 4 macam.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi dan menghitung jumlah kategori yang disajikan dalam diagram lingkaran. Ini adalah proses membaca data secara langsung dari representasi visual.. Bukti: Ada berapa macam panjang password email siswa di kelas ini?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami struktur diagram lingkaran sebagai representasi data kategorikal untuk mengidentifikasi jumlah kategori yang ada.. Bukti: Diagram lingkaran; Ada berapa macam panjang password
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar karena hanya meminta siswa untuk menghitung jumlah label kategori yang tersedia pada diagram lingkaran tanpa perlu melakukan perhitungan aritmatika kompleks atau interpretasi data yang mendalam.. Bukti: Ada berapa macam panjang password email siswa di kelas ini?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca label pada diagram lingkaran. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah terbiasa membaca data dari diagram sederhana. Soal ini hanya menuntut pengenalan visual terhadap kategori yang disajikan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Diagram Lingkaran
Tipe soal: multiple_choice
Stimulus: -
Soal: Dari sebuah survei mengenai panjang password yang digunakan untuk akun email siswa, diperoleh hasil sebagai berikut:

Panjang Password Email

Ada berapa macam panjang password email siswa di kelas ini?
Pilihan: A. 9 macam
B. 3 macam
C. 40 macam
D. 4 macam
Transkripsi visual: Diagram lingkaran menunjukkan empat sektor yang mewakili kategori panjang password: 7-angka (nilai 3), 9-angka (nilai 5), 6-angka (nilai 12), dan 8-angka (nilai 20).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 47. Soal `e8a6fabcd6f67b1be8f8ad7f`

Berikut data tingkat suku bunga deposito untuk jangka waktu 12 bulan di beberapa bank di Indonesia per tanggal 9 Maret 2022. Tingkat suku bunga selalu dinyatakan dalam persen.<br><br>Tabel 6.11 Tingkat Suku Bunga Deposito Jangka 12 Bulan<br><br>\| Nama Bank \| Tingkat Suku Bunga Deposito \|<br>\|---\|---\|<br>\| Bank Mandiri \| 2,50 % \|<br>\| BNI 1946 \| 2,50 % \|<br>\| BRI \| 2,50 % \|<br>\| BCA \| 1,90 % \|<br>\| Bank Maspion \| 4,75 % \|<br><br>Walaupun data di atas berbentuk persen, kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas. Pilih penjelasan yang tepat.

| Opsi | Isi |
|---|---|
| A | Karena beberapa bank memiliki suku bunga yang sama sehingga juringnya bertumpuk |
| B | Karena suku bunga berupa bilangan desimal yang tidak dapat diubah menjadi sudut |
| C | Karena persen suku bunga tiap bank bukan bagian dari satu keseluruhan (jumlahnya tidak 100%) |
| D | Karena banyaknya bank lebih dari 4 sehingga lingkaran tidak dapat dibagi |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Diagram lingkaran (pie chart) hanya digunakan untuk data yang merupakan bagian dari satu kesatuan (total 100%). Suku bunga deposito masing-masing bank adalah data independen yang tidak membentuk satu kesatuan (jumlahnya tidak 100%), sehingga tidak tepat disajikan dalam diagram lingkaran.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d24912ac98ade0ed885f09637b0508d92ae32e1844158ce9b888133bacbad6f7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Medium | 2443 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 2565 |
| 3 | success | valid / verified | reasoning | conceptual | Easy | 2385 |

Run 1 — solusi: Diagram lingkaran digunakan untuk menunjukkan proporsi bagian terhadap keseluruhan (total 100%). Suku bunga deposito masing-masing bank adalah nilai independen, bukan bagian dari total suku bunga yang berjumlah 100%, sehingga tidak tepat menggunakan diagram lingkaran.
- Domain kognitif `classify/reasoning`: Siswa perlu memahami syarat penggunaan diagram lingkaran (bagian dari keseluruhan) dan menganalisis apakah data suku bunga memenuhi syarat tersebut. Ini melibatkan pemahaman konseptual tentang representasi data.. Bukti: kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas; persen suku bunga tiap bank bukan bagian dari satu keseluruhan
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang prinsip atau syarat penggunaan diagram lingkaran sebagai alat penyajian data.. Bukti: diagram lingkaran untuk merepresentasikan data; bukan bagian dari satu keseluruhan
- Intended difficulty `classify/Medium`: Soal ini menguji pemahaman konseptual tentang kapan diagram lingkaran tepat digunakan. Ini adalah konsep dasar dalam statistika deskriptif kelas 7.. Bukti: kalian tidak dapat menggunakan diagram lingkaran; persen suku bunga tiap bank bukan bagian dari satu keseluruhan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang diagram lingkaran (bagian dari keseluruhan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diajarkan berbagai jenis diagram. Memahami batasan penggunaan diagram lingkaran adalah bagian dari kurikulum statistik dasar. |

Run 2 — solusi: Diagram lingkaran digunakan untuk menunjukkan proporsi bagian terhadap keseluruhan (total 100%). Suku bunga deposito pada tabel adalah data independen yang jika dijumlahkan tidak mencapai 100%, sehingga tidak memenuhi syarat sebagai bagian dari satu keseluruhan.
- Domain kognitif `classify/reasoning`: Siswa perlu memahami konsep dasar dan batasan penggunaan diagram lingkaran (part-to-whole) untuk mengevaluasi kesesuaian data, yang melampaui sekadar membaca data.. Bukti: kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas; persen suku bunga tiap bank bukan bagian dari satu keseluruhan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang kapan suatu representasi grafik (diagram lingkaran) tepat digunakan berdasarkan sifat data.. Bukti: diagram lingkaran untuk merepresentasikan data; bukan bagian dari satu keseluruhan
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemahaman konseptual tentang syarat diagram lingkaran. Meskipun tidak melibatkan perhitungan rumit, siswa harus mampu membedakan data yang bersifat bagian dari keseluruhan dengan data independen.. Bukti: kalian tidak dapat menggunakan diagram lingkaran; jumlahnya tidak 100%

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang diagram lingkaran dan syarat data yang dapat disajikan dalam diagram tersebut. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 dalam topik literasi data, menguji pemahaman konseptual di luar sekadar membuat diagram. |

Run 3 — solusi: Diagram lingkaran digunakan untuk menunjukkan proporsi bagian terhadap keseluruhan (total 100%). Suku bunga deposito masing-masing bank adalah nilai independen, bukan bagian dari total suku bunga yang berjumlah 100%.
- Domain kognitif `classify/reasoning`: Siswa perlu memahami prinsip konseptual penggunaan diagram lingkaran (bagian dari keseluruhan) dan mengevaluasi apakah data yang diberikan memenuhi syarat tersebut.. Bukti: kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas; persen suku bunga tiap bank bukan bagian dari satu keseluruhan
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang syarat penggunaan diagram lingkaran.. Bukti: diagram lingkaran untuk merepresentasikan data; bukan bagian dari satu keseluruhan
- Intended difficulty `classify/Easy`: Soal ini menguji pemahaman konseptual dasar tentang representasi data tanpa memerlukan perhitungan yang kompleks.. Bukti: kalian tidak dapat menggunakan diagram lingkaran; persen suku bunga tiap bank bukan bagian dari satu keseluruhan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang diagram lingkaran dan konsep bagian dari keseluruhan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah diperkenalkan dengan berbagai jenis diagram. Memahami syarat penggunaan diagram lingkaran adalah konsep dasar dalam statistika deskriptif. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 3} | unanimous_3_0 / adjudicated | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3253`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `reasoning`: Siswa perlu memahami syarat penggunaan diagram lingkaran (konsep bagian dari keseluruhan) dan mengevaluasi apakah data yang diberikan memenuhi syarat tersebut. Ini adalah proses penalaran konseptual, bukan sekadar membaca data.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman tentang prinsip atau syarat penggunaan diagram lingkaran sebagai alat penyajian data.
- Intended difficulty `Medium`: Soal ini menguji pemahaman konseptual tentang kapan diagram lingkaran tepat digunakan. Meskipun konsepnya mendasar, siswa harus mampu membedakan data yang bersifat bagian dari keseluruhan dengan data independen, yang merupakan langkah penting dalam literasi data.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang diagram lingkaran (bagian dari keseluruhan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diajarkan berbagai jenis diagram. Memahami batasan penggunaan diagram lingkaran adalah bagian dari kurikulum statistik dasar yang menuntut pemahaman konseptual di atas sekadar membuat diagram. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Memilih Diagram yang Tepat
Tipe soal: multiple_choice
Stimulus: -
Soal: Berikut data tingkat suku bunga deposito untuk jangka waktu 12 bulan di beberapa bank di Indonesia per tanggal 9 Maret 2022. Tingkat suku bunga selalu dinyatakan dalam persen.

Tabel 6.11 Tingkat Suku Bunga Deposito Jangka 12 Bulan

| Nama Bank | Tingkat Suku Bunga Deposito |
|---|---|
| Bank Mandiri | 2,50 % |
| BNI 1946 | 2,50 % |
| BRI | 2,50 % |
| BCA | 1,90 % |
| Bank Maspion | 4,75 % |

Walaupun data di atas berbentuk persen, kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas. Pilih penjelasan yang tepat.
Pilihan: A. Karena beberapa bank memiliki suku bunga yang sama sehingga juringnya bertumpuk
B. Karena suku bunga berupa bilangan desimal yang tidak dapat diubah menjadi sudut
C. Karena persen suku bunga tiap bank bukan bagian dari satu keseluruhan (jumlahnya tidak 100%)
D. Karena banyaknya bank lebih dari 4 sehingga lingkaran tidak dapat dibagi
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "reasoning", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 48. Soal `3efcaa6d3ad1d84cd7bb39c9`

Diagram apakah yang akan kalian gunakan untuk menunjukkan pengeluaran bulanan keluarga kalian untuk listrik selama 1 tahun?

| Opsi | Isi |
|---|---|
| A | Diagram batang ganda |
| B | Diagram lingkaran |
| C | Diagram garis ganda |
| D | Diagram garis |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Pengeluaran listrik bulanan selama satu tahun merupakan data deret waktu (time series) yang menunjukkan tren perubahan nilai dari waktu ke waktu, sehingga diagram garis adalah representasi yang paling tepat untuk menunjukkan tren tersebut.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menerapkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `111190dada6bfd7cfd63252b959f449760a97033388ca71572b6780623cbb572`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1624 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1633 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1617 |

Run 1 — solusi: Pengeluaran listrik bulanan selama satu tahun merupakan data deret waktu (time series) yang menunjukkan tren perubahan nilai dari waktu ke waktu, sehingga diagram garis adalah representasi yang paling tepat untuk menunjukkan tren tersebut.
- Domain kognitif `classify/applying`: Siswa perlu memahami karakteristik data (deret waktu) dan mencocokkannya dengan kegunaan berbagai jenis diagram, yang merupakan penerapan konsep statistik dasar.. Bukti: Diagram apakah yang akan kalian gunakan untuk menunjukkan pengeluaran bulanan keluarga kalian untuk listrik selama 1 tahun?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang kapan dan mengapa jenis diagram tertentu digunakan untuk merepresentasikan data.. Bukti: Diagram apakah yang akan kalian gunakan untuk menunjukkan pengeluaran bulanan keluarga kalian untuk listrik selama 1 tahun?
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 7 yang telah mempelajari penyajian data. Siswa hanya perlu mengidentifikasi hubungan antara variabel waktu dan jenis grafik yang sesuai.. Bukti: Diagram apakah yang akan kalian gunakan untuk menunjukkan pengeluaran bulanan keluarga kalian untuk listrik selama 1 tahun?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang fungsi diagram batang, lingkaran, dan garis. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pemilihan diagram berdasarkan jenis data adalah materi standar kelas 7 yang bersifat konseptual dan langsung. |

Run 2 — solusi: Pengeluaran listrik bulanan selama satu tahun merupakan data yang berubah terhadap waktu (time-series). Diagram garis adalah representasi yang paling tepat untuk menunjukkan tren atau perubahan data kontinu berdasarkan urutan waktu.
- Domain kognitif `classify/applying`: Siswa perlu memahami karakteristik data (deret waktu) dan mencocokkannya dengan fungsi visualisasi diagram yang tepat, yang merupakan proses penerapan konsep.. Bukti: Diagram apakah yang akan kalian gunakan untuk menunjukkan pengeluaran bulanan keluarga kalian untuk listrik selama 1 tahun?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara jenis data dan bentuk representasi grafis yang sesuai (prinsip statistik).. Bukti: Diagram apakah yang akan kalian gunakan untuk menunjukkan pengeluaran bulanan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dalam kurikulum kelas 7 terkait penyajian data. Siswa hanya perlu mengidentifikasi bahwa data bulanan adalah data deret waktu yang paling umum disajikan dengan diagram garis.. Bukti: Diagram apakah yang akan kalian gunakan untuk menunjukkan pengeluaran bulanan keluarga kalian untuk listrik selama 1 tahun?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang fungsi diagram batang, lingkaran, dan garis. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pemilihan diagram berdasarkan jenis data adalah materi standar kelas 7 yang bersifat prosedural/konseptual dasar. |

Run 3 — solusi: Data pengeluaran listrik bulanan selama satu tahun merupakan data kontinu yang berubah terhadap waktu. Diagram garis adalah representasi yang paling tepat untuk menunjukkan tren atau perubahan data numerik secara berurutan dalam rentang waktu tertentu.
- Domain kognitif `classify/applying`: Siswa perlu memahami karakteristik data (data kontinu/deret waktu) dan mencocokkannya dengan fungsi visual dari berbagai jenis diagram, yang merupakan proses applying konsep statistik dasar.. Bukti: Diagram apakah yang akan kalian gunakan untuk menunjukkan pengeluaran bulanan keluarga kalian untuk listrik selama 1 tahun?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip atau aturan pemilihan representasi data yang tepat berdasarkan sifat data tersebut.. Bukti: Diagram apakah yang akan kalian gunakan untuk menunjukkan pengeluaran bulanan keluarga kalian untuk listrik selama 1 tahun?
- Intended difficulty `classify/Easy`: Soal ini bersifat konseptual namun prosedurnya langsung dalam memilih representasi yang sudah familiar di kurikulum kelas 7.. Bukti: Diagram apakah yang akan kalian gunakan untuk menunjukkan pengeluaran bulanan keluarga kalian untuk listrik selama 1 tahun?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang fungsi diagram batang, lingkaran, dan garis. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pemilihan diagram berdasarkan jenis data adalah materi standar kelas 7 yang tidak memerlukan perhitungan kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Memilih Diagram yang Tepat
Tipe soal: multiple_choice
Stimulus: -
Soal: Diagram apakah yang akan kalian gunakan untuk menunjukkan pengeluaran bulanan keluarga kalian untuk listrik selama 1 tahun?
Pilihan: A. Diagram batang ganda
B. Diagram lingkaran
C. Diagram garis ganda
D. Diagram garis
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 49. Soal `1312d88be889daa8b0ab7ee7`

Perhatikan diagram batang berikut.<br><br>Kandungan Kalori Per 100 Gram Makanan<br><br>Diagram batang di atas menunjukkan kandungan kalori dari berbagai jenis makanan. Kalori dihitung untuk setiap 100 gram makanan. Kalori adalah satuan energi. Kalori dalam makanan itulah yang digunakan tubuh sebagai sumber energi untuk dapat melaksanakan fungsinya dengan baik.<br><br>Kebutuhan kalori anak usia 10–12 tahun adalah sekitar 2.000 kkal untuk anak perempuan dan 2.100 kkal untuk anak laki-laki. Dalam satu hari, Lukas makan 300 gram nasi putih, 200 gram daging ayam, dan 100 gram sayuran hijau. Ia masih makan makanan ringan yang mengandung 300 kkal dan 1 bungkus mi instan yang mengandung 350 kkal per bungkus. Apakah makanan yang dimakan Lukas kalorinya berlebihan? Mengapa demikian?

| Opsi | Isi |
|---|---|
| A | Tidak, karena totalnya 1.620 kkal, di bawah kebutuhan 2.100 kkal |
| B | Ya, karena totalnya 1.620 kkal, di atas kebutuhan 1.500 kkal |
| C | Tidak, karena totalnya 970 kkal, di bawah kebutuhan 2.100 kkal |
| D | Ya, karena totalnya 2.270 kkal, di atas kebutuhan 2.100 kkal |

![Gambar sumber soal 49](<../images/kelas5_panduan_siswa_kelas5.pdf-0282-04.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Hitung kalori: (3 x 130) + (2 x 260) + (1 x 60) + 300 + 350 = 390 + 520 + 60 + 300 + 350 = 1.620 kkal. Bandingkan dengan kebutuhan anak laki-laki (2.100 kkal). 1.620 < 2.100, maka tidak berlebihan.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0282-04.png. Transkripsi visual: Diagram batang horizontal menunjukkan kalori per 100 gram makanan. Skala sumbu horizontal memiliki garis bantu setiap 25 kkal (0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300). Data: Nasi putih = 130 kkal/100g, Daging Ayam = 260 kkal/100g, Sayuran hijau = 60 kkal/100g.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a32f3a44c0505c27201bb08014089445785c0b63afd6dea0ce89601ee9548ec1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3347 |
| 2 | success | valid / verified | applying | procedural | Medium | 3372 |
| 3 | success | valid / verified | applying | procedural | Medium | 3324 |

Run 1 — solusi: Hitung kalori: (3 x 130) + (2 x 260) + (1 x 60) + 300 + 350 = 390 + 520 + 60 + 300 + 350 = 1.620 kkal. Bandingkan dengan kebutuhan anak laki-laki (2.100 kkal). 1.620 < 2.100, maka tidak berlebihan.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan data dari diagram (membaca nilai per 100g), melakukan operasi perkalian untuk menyesuaikan porsi, menjumlahkan total kalori, dan membandingkannya dengan ambang batas yang diberikan.. Bukti: Lukas makan 300 gram nasi putih, 200 gram daging ayam, dan 100 gram sayuran hijau; Ia masih makan makanan ringan yang mengandung 300 kkal dan 1 bungkus mi instan yang mengandung 350 kkal
- Dimensi pengetahuan `classify/procedural`: Siswa harus memahami hubungan antara data visual (diagram), konsep satuan (per 100g), dan konteks masalah (kebutuhan kalori) untuk menyelesaikan prosedur perhitungan.. Bukti: Diagram batang di atas menunjukkan kandungan kalori dari berbagai jenis makanan; Kebutuhan kalori anak usia 10–12 tahun adalah sekitar 2.000 kkal untuk anak perempuan dan 2.100 kkal untuk anak laki-laki
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena melibatkan beberapa langkah rutin yang saling terkait: membaca diagram, melakukan konversi satuan (per 100g), penjumlahan, dan perbandingan logis.. Bukti: 300 gram nasi putih, 200 gram daging ayam, dan 100 gram sayuran hijau; 300 kkal dan 1 bungkus mi instan yang mengandung 350 kkal

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Membaca diagram batang, perkalian bilangan bulat, penjumlahan bilangan bulat. |
| dependentSteps | 5 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 6 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena menggabungkan literasi data (diagram) dengan aritmatika dasar dalam konteks kehidupan sehari-hari. |

Run 2 — solusi: Nasi putih: 3 x 130 = 390 kkal. Daging ayam: 2 x 260 = 520 kkal. Sayuran hijau: 1 x 60 = 60 kkal. Makanan ringan: 300 kkal. Mi instan: 350 kkal. Total: 390 + 520 + 60 + 300 + 350 = 1.620 kkal. Karena 1.620 < 2.100, maka tidak berlebihan.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan data dari grafik (membaca nilai per 100g), melakukan operasi perkalian untuk menyesuaikan porsi, dan menjumlahkan total kalori untuk dibandingkan dengan ambang batas yang diberikan.. Bukti: Lukas makan 300 gram nasi putih, 200 gram daging ayam, dan 100 gram sayuran hijau; Ia masih makan makanan ringan yang mengandung 300 kkal dan 1 bungkus mi instan yang mengandung 350 kkal
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan prosedur aritmatika (perkalian dan penjumlahan) pada data yang disajikan secara konseptual dalam bentuk diagram batang.. Bukti: Diagram batang di atas menunjukkan kandungan kalori dari berbagai jenis makanan; Kebutuhan kalori anak usia 10–12 tahun adalah sekitar 2.000 kkal untuk anak perempuan dan 2.100 kkal untuk anak laki-laki
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah rutin yang saling terkait: membaca grafik, melakukan perkalian berdasarkan porsi (skala), dan menjumlahkan hasil untuk perbandingan.. Bukti: 300 gram nasi putih; 200 gram daging ayam; 100 gram sayuran hijau; 300 kkal dan 350 kkal

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmatika dasar (perkalian dan penjumlahan) dan kemampuan membaca diagram batang. |
| dependentSteps | 5 |
| routineStatus | routine_selection |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 7 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena menggabungkan literasi data (diagram batang) dengan aritmatika dasar dalam konteks kehidupan sehari-hari. |

Run 3 — solusi: Hitung total kalori: (3 x 130) + (2 x 260) + (1 x 60) + 300 + 350 = 390 + 520 + 60 + 300 + 350 = 1.620 kkal. Bandingkan dengan kebutuhan 2.100 kkal. Karena 1.620 < 2.100, maka tidak berlebihan.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan data dari diagram (membaca nilai per 100g), melakukan operasi perkalian untuk menyesuaikan porsi, dan menjumlahkan total kalori sebelum membandingkannya dengan ambang batas.. Bukti: Lukas makan 300 gram nasi putih, 200 gram daging ayam, dan 100 gram sayuran hijau; Ia masih makan makanan ringan yang mengandung 300 kkal dan 1 bungkus mi instan yang mengandung 350 kkal
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur aritmatika (perkalian dan penjumlahan) untuk memproses data yang disajikan secara konseptual dalam bentuk diagram batang.. Bukti: Diagram batang di atas menunjukkan kandungan kalori dari berbagai jenis makanan; Kebutuhan kalori anak usia 10–12 tahun adalah sekitar 2.000 kkal untuk anak perempuan dan 2.100 kkal untuk anak laki-laki
- Intended difficulty `classify/Medium`: Soal ini memerlukan beberapa langkah rutin: membaca data dari grafik, mengalikan dengan porsi (skala), menjumlahkan total, dan membandingkan dengan nilai referensi. Ini adalah tugas rutin yang terstruktur.. Bukti: 300 gram nasi putih, 200 gram daging ayam, dan 100 gram sayuran hijau; 300 kkal dan 1 bungkus mi instan yang mengandung 350 kkal

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Membaca diagram batang, operasi perkalian dan penjumlahan bilangan bulat. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 7 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 7 karena melibatkan interpretasi data grafik dan operasi aritmatika dasar yang diterapkan pada konteks kehidupan sehari-hari. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
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
Kelas: 7
Topik: Matematika SMP Kelas 7
Subtopik: Diagram Batang
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan diagram batang berikut.

Kandungan Kalori Per 100 Gram Makanan

Diagram batang di atas menunjukkan kandungan kalori dari berbagai jenis makanan. Kalori dihitung untuk setiap 100 gram makanan. Kalori adalah satuan energi. Kalori dalam makanan itulah yang digunakan tubuh sebagai sumber energi untuk dapat melaksanakan fungsinya dengan baik.

Kebutuhan kalori anak usia 10–12 tahun adalah sekitar 2.000 kkal untuk anak perempuan dan 2.100 kkal untuk anak laki-laki. Dalam satu hari, Lukas makan 300 gram nasi putih, 200 gram daging ayam, dan 100 gram sayuran hijau. Ia masih makan makanan ringan yang mengandung 300 kkal dan 1 bungkus mi instan yang mengandung 350 kkal per bungkus. Apakah makanan yang dimakan Lukas kalorinya berlebihan? Mengapa demikian?
Pilihan: A. Tidak, karena totalnya 1.620 kkal, di bawah kebutuhan 2.100 kkal
B. Ya, karena totalnya 1.620 kkal, di atas kebutuhan 1.500 kkal
C. Tidak, karena totalnya 970 kkal, di bawah kebutuhan 2.100 kkal
D. Ya, karena totalnya 2.270 kkal, di atas kebutuhan 2.100 kkal
Transkripsi visual: Diagram batang horizontal menunjukkan kalori per 100 gram makanan. Skala sumbu horizontal memiliki garis bantu setiap 25 kkal (0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300). Data: Nasi putih = 130 kkal/100g, Daging Ayam = 260 kkal/100g, Sayuran hijau = 60 kkal/100g.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
