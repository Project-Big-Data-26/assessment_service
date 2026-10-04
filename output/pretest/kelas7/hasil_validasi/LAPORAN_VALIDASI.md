# Validasi ulang soal kelas 7 — Gemini blind N=3 dan diagnostik IndoBERT

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v10-blind-smp7-key-verified`. Rubrik: `math-rubric-3x4x3-v8-smp7-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 7 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan menjadi keputusan silver operasional.

Checkpoint dikunci dengan SHA-256 sebelum pemeriksaan scope IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Artifact berada di luar cakupan kelas 7, sehingga seluruh head abstain dan tidak menghasilkan ukuran agreement dengan label blind.

Jumlah soal: 49; distribusi label advisory: `{"mathCognitiveDomain": {"knowing": 18, "applying": 26, "reasoning": 5}, "knowledgeDimension": {"conceptual": 25, "procedural": 19, "factual": 5, "metacognitive": 0}, "intendedDifficulty": {"Easy": 32, "Medium": 16, "Hard": 1}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"knowing": 18, "applying": 25, "reasoning": 5}, "knowledgeDimension": {"conceptual": 25, "procedural": 18, "factual": 5, "metacognitive": 0}, "intendedDifficulty": {"Easy": 32, "Medium": 15, "Hard": 1}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"silver_ready": 48, "revision_required": 1}`.
Run awal sukses: 147/147; adjudikasi: 21; token sukses tercatat: 526,271.

Seluruh label memakai provenance ai_silver. Delivery memakai snapshot silver yang lolos qualification. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

Artifact diagnostik IndoBERT: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Dataset training: `kelas1-gemini-silver-n3-v1`. Approval provisional: `False`; research-only: `False`; gate data: `False`; anti-collapse: `False`; gate promosi: `False`. Packaging ini tidak melakukan training atau promosi model.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten dapat masuk snapshot silver operasional.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 32 | 32 | [Easy.json](difficulty/Easy.json) |
| Medium | 16 | 15 | [Medium.json](difficulty/Medium.json) |
| Hard | 1 | 1 | [Hard.json](difficulty/Hard.json) |

## Perhitungan yang dipakai

Untuk kelas 7, encoder dan head IndoBERT tidak dijalankan karena cakupan artifact adalah kelas [1, 2, 3, 4, 5, 6], jalur ['regular']. Probabilitas kosong, label/confidence/entropy null, dan action abstain berasal dari pemeriksaan scope runtime. Suara Gemini adalah bukti penilaian advisory, bukan probabilitas IndoBERT.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

Cakupan artifact: kelas [1, 2, 3, 4, 5, 6], jalur ['regular']. Untuk kelas 7, diagnostik mengembalikan `out_of_scope` dan `abstain`: label, confidence, dan entropy null serta probabilitas kosong. Label advisory mengikuti Gemini blind dengan rubrik SMP kelas 7.

## 1. Soal `96d7ccf391bfd43c525dac4f`

Urutkan bilangan bulat di bawah ini dari yang terkecil ke terbesar.<br><br>$ -8, 4, -2, 12 $

| Opsi | Isi |
|---|---|
| A | $ 12, 4, -2, -8 $ |
| B | $ -8, -2, 4, 12 $ |
| C | $ -2, -8, 4, 12 $ |
| D | $ -2, 4, -8, 12 $ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Membandingkan nilai bilangan bulat pada garis bilangan: -8 < -2 < 4 < 12. Urutan dari terkecil ke terbesar adalah -8, -2, 4, 12.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `db7b5d1ad4fcba3fa7ac53bb2447a47f8726f23da73cdde0c02e53f13a64cb2f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2362 |
| 2 | success | valid / verified | knowing | factual | Easy | 2348 |
| 3 | success | valid / verified | knowing | factual | Easy | 2796 |

Run 1 — solusi: Membandingkan nilai bilangan bulat pada garis bilangan: -8 < -2 < 4 < 12. Urutan dari terkecil ke terbesar adalah -8, -2, 4, 12.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengenali urutan nilai bilangan bulat pada garis bilangan, yang merupakan prosedur dasar dalam topik bilangan bulat.. Bukti: Urutkan bilangan bulat di bawah ini dari yang terkecil ke terbesar.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep dasar urutan bilangan bulat (fakta bahwa bilangan negatif lebih kecil dari positif, dan semakin besar angka negatif semakin kecil nilainya).. Bukti: Urutkan bilangan bulat di bawah ini dari yang terkecil ke terbesar.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin bagi siswa kelas 7. Tidak ada langkah yang saling bergantung atau kendala yang kompleks. Siswa hanya perlu menerapkan aturan urutan bilangan bulat.. Bukti: Urutkan bilangan bulat di bawah ini dari yang terkecil ke terbesar.; -8, 4, -2, 12

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
| gradeRelativeRationale | Mengurutkan bilangan bulat adalah materi dasar kelas 7. Soal ini tidak memiliki jebakan atau kompleksitas tambahan, sehingga termasuk kategori mudah. |

Run 2 — solusi: Membandingkan nilai bilangan bulat: -8 < -2 < 4 < 12. Urutan dari terkecil ke terbesar adalah -8, -2, 4, 12.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengenali urutan bilangan bulat pada garis bilangan, yang merupakan prosedur dasar dalam memahami konsep bilangan bulat.. Bukti: Urutkan bilangan bulat di bawah ini dari yang terkecil ke terbesar.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang urutan bilangan bulat dan posisi bilangan negatif relatif terhadap nol dan bilangan positif.. Bukti: Urutkan bilangan bulat di bawah ini dari yang terkecil ke terbesar.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin. Siswa hanya perlu menerapkan aturan dasar perbandingan bilangan bulat tanpa langkah tambahan atau integrasi konsep yang kompleks.. Bukti: Urutkan bilangan bulat di bawah ini dari yang terkecil ke terbesar.; -8, 4, -2, 12

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang garis bilangan dan perbandingan nilai bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan bilangan bulat adalah materi dasar kelas 7 yang sangat familiar dan tidak memerlukan langkah perencanaan yang rumit. |

Run 3 — solusi: -8 < -2 < 4 < 12
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengurutkan bilangan bulat berdasarkan nilai pada garis bilangan, yang merupakan prosedur langsung dan mendasar.. Bukti: Urutkan bilangan bulat di bawah ini dari yang terkecil ke terbesar.; -8, 4, -2, 12
- Dimensi pengetahuan `classify/factual`: Siswa perlu memahami fakta dasar tentang urutan bilangan bulat pada garis bilangan, di mana bilangan negatif yang lebih besar (nilai mutlaknya) justru lebih kecil nilainya.. Bukti: Urutkan bilangan bulat di bawah ini dari yang terkecil ke terbesar.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu membandingkan empat bilangan bulat yang diberikan tanpa memerlukan langkah perencanaan atau integrasi konsep yang kompleks.. Bukti: Urutkan bilangan bulat di bawah ini dari yang terkecil ke terbesar.; -8, 4, -2, 12

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep garis bilangan dan urutan bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan bilangan bulat adalah materi dasar kelas 7. Soal ini tidak memiliki kendala yang berinteraksi atau tuntutan kognitif tinggi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 1, "factual": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3674`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu mengenali dan menerapkan aturan urutan bilangan bulat pada garis bilangan, yang merupakan prosedur dasar dan langsung.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang urutan bilangan bulat, khususnya posisi bilangan negatif relatif terhadap bilangan positif pada garis bilangan.
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung. Tidak ada langkah perencanaan, integrasi kendala, atau strategi non-rutin yang diperlukan. Siswa hanya perlu menerapkan pemahaman dasar tentang urutan bilangan bulat.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang garis bilangan dan perbandingan nilai bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan bilangan bulat adalah materi dasar kelas 7 yang sangat familiar. Soal ini tidak memiliki kompleksitas tambahan atau jebakan yang menuntut penalaran tinggi. |

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
Solusi minimum hasil AI: Kerugian dalam konteks bilangan bulat direpresentasikan dengan tanda negatif (-). Maka, kerugian Rp250.000,00 ditulis sebagai -250.000.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7cd18e07faa748bfdccc47af987743f9d49f3311d6c94d17d7199c7b0693fe00`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2970 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2691 |
| 3 | success | valid / verified | knowing | factual | Easy | 2211 |

Run 1 — solusi: Dalam konteks bilangan bulat, kerugian direpresentasikan dengan tanda negatif (-). Maka, kerugian Rp250.000,00 ditulis sebagai -250.000.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali konvensi bahwa kerugian dalam bilangan bulat direpresentasikan dengan tanda negatif. Tidak ada prosedur kompleks atau strategi yang perlu dipilih.. Bukti: Nyatakan bilangan berikut ini dengan tanda positif atau negatif.; Penjualan di toko hari ini mengalami kerugian sebesar Rp250.000,00.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana bilangan bulat digunakan untuk merepresentasikan situasi dunia nyata, yaitu kerugian sebagai nilai negatif.. Bukti: Nyatakan bilangan berikut ini dengan tanda positif atau negatif.; Penjualan di toko hari ini mengalami kerugian sebesar Rp250.000,00.
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya memerlukan pemahaman dasar tentang representasi bilangan bulat untuk situasi kerugian. Tidak ada langkah tambahan atau integrasi yang diperlukan.. Bukti: Nyatakan bilangan berikut ini dengan tanda positif atau negatif.; Penjualan di toko hari ini mengalami kerugian sebesar Rp250.000,00.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bilangan bulat dan penggunaan tanda negatif untuk menyatakan kerugian. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Soal ini merupakan penerapan langsung dari konsep bilangan bulat dalam kehidupan sehari-hari yang sangat mendasar bagi siswa kelas 7. |

Run 2 — solusi: Dalam konteks bilangan bulat, kerugian direpresentasikan dengan tanda negatif. Maka, kerugian sebesar Rp250.000,00 ditulis sebagai -250.000.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengenali dan menerapkan konvensi dasar bilangan bulat (negatif untuk kerugian) secara langsung tanpa proses penalaran yang kompleks.. Bukti: Nyatakan bilangan berikut ini dengan tanda positif atau negatif.; Penjualan di toko hari ini mengalami kerugian sebesar Rp250.000,00.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep hubungan antara situasi dunia nyata (kerugian) dengan representasi simbolis (bilangan negatif).. Bukti: Nyatakan bilangan berikut ini dengan tanda positif atau negatif.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan merupakan pengenalan dasar bilangan bulat di kelas 7. Tidak ada langkah yang saling bergantung atau kendala yang berinteraksi.. Bukti: Nyatakan bilangan berikut ini dengan tanda positif atau negatif.; Penjualan di toko hari ini mengalami kerugian sebesar Rp250.000,00.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bilangan bulat dan penggunaan tanda positif/negatif dalam konteks situasi nyata. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Ini adalah materi dasar kelas 7 yang menuntut pengenalan langsung terhadap konvensi tanda bilangan bulat tanpa kompleksitas tambahan. |

Run 3 — solusi: Kerugian dalam konteks bilangan bulat direpresentasikan dengan tanda negatif (-). Maka, kerugian Rp250.000,00 ditulis sebagai -250.000.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengenali dan menerapkan konvensi tanda (positif/negatif) pada situasi nyata yang sederhana. Ini adalah pengenalan fakta dasar bilangan bulat.. Bukti: Nyatakan bilangan berikut ini dengan tanda positif atau negatif.; Penjualan di toko hari ini mengalami kerugian sebesar Rp250.000,00.
- Dimensi pengetahuan `classify/factual`: Siswa perlu memahami konvensi simbolik bahwa kerugian diasosiasikan dengan tanda negatif dalam konteks bilangan bulat.. Bukti: Nyatakan bilangan berikut ini dengan tanda positif atau negatif.
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya memerlukan pemahaman dasar tentang representasi bilangan bulat dalam konteks kerugian. Tidak ada langkah kompleks atau integrasi konsep yang diperlukan.. Bukti: Nyatakan bilangan berikut ini dengan tanda positif atau negatif.; Penjualan di toko hari ini mengalami kerugian sebesar Rp250.000,00.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep bilangan bulat dan penggunaan tanda negatif untuk menyatakan kerugian. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Ini adalah soal tingkat dasar untuk kelas 7 yang menguji pemahaman awal tentang bilangan bulat dalam kehidupan sehari-hari tanpa beban kognitif tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 2, "factual": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4499`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu mengenali konvensi bahwa kerugian dalam bilangan bulat direpresentasikan dengan tanda negatif. Tidak ada prosedur kompleks atau strategi yang perlu dipilih.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana bilangan bulat digunakan untuk merepresentasikan situasi dunia nyata, yaitu kerugian sebagai nilai negatif.
- Intended difficulty `Easy`: Soal ini sangat langsung, hanya memerlukan pemahaman dasar tentang representasi bilangan bulat untuk situasi kerugian. Tidak ada langkah tambahan atau integrasi yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bilangan bulat dan penggunaan tanda negatif untuk menyatakan kerugian. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Soal ini merupakan penerapan langsung dari konsep bilangan bulat dalam kehidupan sehari-hari yang sangat mendasar bagi siswa kelas 7. |

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
Solusi minimum hasil AI: Menerjemahkan aturan transfer ke operasi hitung: (5 x +1) + (2 x -1) - (3 x +1) - (4 x -1) = 5 - 2 - 3 + 4 = 4. Hasil positif 4 menunjukkan performa naik.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d3a35d09fa80da8d4865484477fb299129631222c6023b68837570d1c1683da4`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 4031 |
| 2 | success | valid / verified | applying | procedural | Medium | 2655 |
| 3 | success | valid / verified | applying | procedural | Medium | 2694 |

Run 1 — solusi: Menerjemahkan aturan transfer ke operasi hitung: (5 x +1) + (2 x -1) - (3 x +1) - (4 x -1) = 5 - 2 - 3 + 4 = 4. Hasil positif 4 menunjukkan performa naik.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan aturan operasi bilangan bulat yang diberikan dalam tabel ke dalam situasi konkret transfer pemain. Ini melibatkan pemilihan operasi yang tepat untuk setiap jenis transfer dan melakukan perhitungan aritmatika dasar.. Bukti: Mendapatkan satu pemain bagus \| +(+1); Mendapatkan satu pemain buruk \| +(−1); Melepaskan satu pemain bagus \| −(+1); Melepaskan satu pemain buruk \| −(−1)
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma operasi bilangan bulat (penjumlahan dan pengurangan bilangan bertanda) berdasarkan aturan yang didefinisikan.. Bukti: Klub D: mendapatkan 5 pemain bagus, mendapatkan 2 pemain buruk, melepaskan 3 pemain bagus, melepaskan 4 pemain buruk.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus mengintegrasikan empat operasi terpisah berdasarkan aturan yang diberikan. Meskipun prosedurnya familiar, terdapat potensi kesalahan pada tanda negatif (terutama -(-1) menjadi +1) yang memerlukan ketelitian dalam perencanaan langkah.. Bukti: Klub D: mendapatkan 5 pemain bagus, mendapatkan 2 pemain buruk, melepaskan 3 pemain bagus, melepaskan 4 pemain buruk.; Pilihan dan catatan ekstraksi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi hitung bilangan bulat (penjumlahan, pengurangan, perkalian dengan tanda). |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 7 sudah mempelajari operasi bilangan bulat. Soal ini menguji ketelitian dalam menerapkan aturan tanda, yang merupakan kompetensi inti di kelas 7. |

Run 2 — solusi: Menerjemahkan transfer ke operasi bilangan bulat: mendapatkan 5 pemain bagus (+5), mendapatkan 2 pemain buruk (+(-2)), melepaskan 3 pemain bagus (-(+3)), melepaskan 4 pemain buruk (-(-4)). Operasi: 5 - 2 - 3 + 4 = 4. Karena hasilnya positif, performa naik.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan deskripsi situasi transfer ke dalam model matematika menggunakan operasi bilangan bulat yang telah didefinisikan dalam tabel, kemudian melakukan perhitungan aritmatika dasar.. Bukti: Mendapatkan satu pemain bagus \| +(+1); Mendapatkan satu pemain buruk \| +(−1); Melepaskan satu pemain bagus \| −(+1); Melepaskan satu pemain buruk \| −(−1)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang aturan operasi bilangan bulat (terutama pengurangan bilangan negatif) dalam konteks yang diberikan.. Bukti: Tabel 1.1 Detail Perhitungan Nilai dan Efek Performa Bagi Klub dari Berbagai Proses Transfer
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan pemetaan (mapping) dari narasi ke operasi matematika secara akurat untuk empat kondisi berbeda, termasuk menangani operasi pengurangan bilangan negatif (-(-4)). Meskipun prosedurnya familiar, integrasi dari empat komponen transfer yang berbeda memerlukan ketelitian dalam perencanaan langkah agar tidak terjadi kesalahan tanda.. Bukti: Klub D: mendapatkan 5 pemain bagus, mendapatkan 2 pemain buruk, melepaskan 3 pemain bagus, melepaskan 4 pemain buruk.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi penjumlahan dan pengurangan bilangan bulat, termasuk pemahaman bahwa pengurangan bilangan negatif sama dengan penjumlahan. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu mengoperasikan bilangan bulat. Tantangan utama adalah ketelitian dalam menerjemahkan setiap jenis transfer ke dalam simbol matematika yang tepat, terutama pada bagian 'melepaskan pemain buruk' yang melibatkan pengurangan bilangan negatif. |

Run 3 — solusi: Klub D melakukan: mendapatkan 5 pemain bagus (+5), mendapatkan 2 pemain buruk (-2), melepaskan 3 pemain bagus (-3), dan melepaskan 4 pemain buruk (+4). Total nilai: (+5) + (-2) - (+3) - (-4) = 5 - 2 - 3 + 4 = 4. Karena hasilnya positif, performa naik.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan deskripsi naratif ke dalam model matematika menggunakan aturan tanda yang diberikan dalam tabel. Ini melibatkan penerapan prosedur operasi bilangan bulat pada konteks yang diberikan.. Bukti: Klub D: mendapatkan 5 pemain bagus, mendapatkan 2 pemain buruk, melepaskan 3 pemain bagus, melepaskan 4 pemain buruk.; Tabel 1.1 Detail Perhitungan Nilai dan Efek Performa Bagi Klub dari Berbagai Proses Transfer
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang aturan operasi bilangan bulat (terutama pengurangan bilangan negatif) dan penerapannya dalam konteks yang terstruktur.. Bukti: Tabel 1.1 Detail Perhitungan Nilai dan Efek Performa Bagi Klub dari Berbagai Proses Transfer
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus mengonversi empat kondisi berbeda menjadi ekspresi matematika yang tepat. Meskipun operasinya rutin, terdapat potensi kesalahan pada tanda (terutama -(-4)) yang memerlukan ketelitian dalam perencanaan langkah. Siswa harus mengintegrasikan aturan tabel ke dalam satu kalimat matematika yang utuh.. Bukti: Klub D: mendapatkan 5 pemain bagus, mendapatkan 2 pemain buruk, melepaskan 3 pemain bagus, melepaskan 4 pemain buruk.; Tabel 1.1 Detail Perhitungan Nilai dan Efek Performa Bagi Klub dari Berbagai Proses Transfer

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi penjumlahan dan pengurangan bilangan bulat, termasuk pemahaman bahwa pengurangan bilangan negatif adalah penjumlahan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu melakukan operasi bilangan bulat. Tantangan utama terletak pada konsistensi penerapan aturan tanda yang diberikan dalam tabel terhadap empat variabel yang berbeda. |

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
Solusi minimum hasil AI: Kedalaman 180 meter di bawah permukaan laut dinyatakan sebagai -180. Untuk mencari kedalaman dalam 1 jam, bagi total kedalaman dengan waktu: -180 / 3 = -60.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `50baf0569987107ae1f6c4374c48158f599c4fa8028884e05d9bc74a2c44515f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2386 |
| 2 | success | valid / verified | applying | procedural | Easy | 2375 |
| 3 | success | valid / verified | applying | procedural | Easy | 2365 |

Run 1 — solusi: Kedalaman 180 meter di bawah permukaan laut dinyatakan sebagai -180. Untuk mencari kedalaman dalam 1 jam, bagi total kedalaman dengan waktu: -180 / 3 = -60.
- Domain kognitif `classify/applying`: Siswa perlu memahami representasi bilangan negatif untuk kedalaman di bawah permukaan laut dan menerapkan operasi pembagian bilangan bulat untuk menentukan laju perubahan posisi.. Bukti: Kapal selam dapat bergerak hingga kedalaman 180 meter di bawah permukaan laut dalam waktu 3 jam.; Pada kedalaman berapa meter di bawah permukaan laut yang dicapai kapal selam dalam 1 jam? Nyatakan dalam bilangan bulat positif atau negatif.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman konseptual tentang penggunaan bilangan bulat (negatif) untuk merepresentasikan posisi di bawah permukaan laut.. Bukti: Nyatakan dalam bilangan bulat positif atau negatif.
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena alur penyelesaiannya sangat jelas (pembagian langsung), melibatkan konsep yang sudah familiar di kelas 7 (bilangan bulat dan laju), serta tidak memiliki kendala yang saling berinteraksi atau tuntutan perencanaan yang kompleks.. Bukti: Kapal selam dapat bergerak hingga kedalaman 180 meter di bawah permukaan laut dalam waktu 3 jam.; Pada kedalaman berapa meter di bawah permukaan laut yang dicapai kapal selam dalam 1 jam?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar bilangan bulat dan operasi pembagian. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah mempelajari operasi bilangan bulat dan penggunaan tanda negatif untuk konteks nyata seperti kedalaman laut. Soal ini merupakan penerapan langsung dari konsep tersebut. |

Run 2 — solusi: Kedalaman 180 meter di bawah permukaan laut dinyatakan sebagai -180. Kecepatan menyelam per jam adalah -180 / 3 = -60. Jadi, dalam 1 jam kapal berada pada kedalaman -60 meter.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep pembagian bilangan bulat dan representasi bilangan negatif untuk situasi kontekstual sederhana. Prosedur pembagian sudah jelas dan langsung.. Bukti: Pada kedalaman berapa meter di bawah permukaan laut yang dicapai kapal selam dalam 1 jam? Nyatakan dalam bilangan bulat positif atau negatif.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi pembagian bilangan bulat dan penggunaan tanda negatif untuk merepresentasikan posisi di bawah permukaan laut.. Bukti: Nyatakan dalam bilangan bulat positif atau negatif.
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena jalur penyelesaiannya sangat jelas (pembagian sederhana) dan konteksnya familiar bagi siswa kelas 7. Tidak ada kendala yang saling berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: Kapal selam dapat bergerak hingga kedalaman 180 meter di bawah permukaan laut dalam waktu 3 jam.; Pada kedalaman berapa meter di bawah permukaan laut yang dicapai kapal selam dalam 1 jam?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bilangan bulat negatif dan operasi pembagian. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah mempelajari bilangan bulat dan operasi hitungnya. Soal ini merupakan penerapan langsung dari konsep tersebut tanpa kerumitan tambahan. |

Run 3 — solusi: Kedalaman 180 meter di bawah permukaan laut dinyatakan sebagai -180. Kecepatan menyelam per jam adalah -180 / 3 = -60.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pembagian bilangan bulat sederhana dalam konteks yang sudah ditentukan (kedalaman sebagai bilangan negatif). Ini adalah penerapan langsung dari konsep operasi bilangan bulat.. Bukti: Pada kedalaman berapa meter di bawah permukaan laut yang dicapai kapal selam dalam 1 jam? Nyatakan dalam bilangan bulat positif atau negatif.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana merepresentasikan posisi di bawah permukaan laut sebagai bilangan negatif dan melakukan operasi pembagian bilangan bulat.. Bukti: Nyatakan dalam bilangan bulat positif atau negatif.
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena jalur penyelesaiannya sangat jelas (pembagian langsung). Siswa hanya perlu memahami konvensi tanda negatif untuk kedalaman dan melakukan satu operasi pembagian sederhana. Tidak ada kendala yang saling berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Kapal selam dapat bergerak hingga kedalaman 180 meter di bawah permukaan laut dalam waktu 3 jam.; Pada kedalaman berapa meter di bawah permukaan laut yang dicapai kapal selam dalam 1 jam?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar bilangan bulat negatif dan operasi pembagian. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan aplikasi langsung dari operasi bilangan bulat yang merupakan materi dasar kelas 7. Tidak ada tuntutan kognitif tinggi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3936`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan konsep bilangan bulat negatif untuk merepresentasikan kedalaman di bawah permukaan laut dan melakukan operasi pembagian bilangan bulat sederhana untuk menentukan posisi per jam. Ini adalah penerapan prosedur yang sudah dipelajari dalam konteks yang diberikan.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana merepresentasikan posisi di bawah permukaan laut sebagai bilangan negatif dan melakukan operasi pembagian bilangan bulat.
- Intended difficulty `Easy`: Soal ini tergolong Easy karena alur penyelesaiannya sangat jelas (pembagian langsung), melibatkan konsep yang sudah familiar di kelas 7 (bilangan bulat dan laju), serta tidak memiliki kendala yang saling berinteraksi atau tuntutan perencanaan yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar bilangan bulat negatif dan operasi pembagian. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah mempelajari operasi bilangan bulat dan penggunaan tanda negatif untuk konteks nyata seperti kedalaman laut. Soal ini merupakan penerapan langsung dari konsep tersebut. |

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
Solusi minimum hasil AI: Menentukan KPK dari 4, 6, dan 8. Faktorisasi prima: 4 = 2^2, 6 = 2 x 3, 8 = 2^3. KPK = 2^3 x 3 = 24. Mereka bertemu kembali 24 hari setelah 8 Agustus. Agustus memiliki 31 hari. Sisa hari di Agustus setelah tanggal 8 adalah 31 - 8 = 23 hari. Maka 24 - 23 = 1 hari di bulan berikutnya, yaitu 1 September 2022.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4c4f09ce4035aaef76a9daadd5f2a70ac0d71715b03ccf7f37a72334d242273b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2674 |
| 2 | success | valid / verified | applying | procedural | Medium | 2614 |
| 3 | success | valid / verified | applying | procedural | Medium | 2673 |

Run 1 — solusi: Menentukan KPK dari 4, 6, dan 8. Kelipatan 4: 4, 8, 12, 16, 20, 24. Kelipatan 6: 6, 12, 18, 24. Kelipatan 8: 8, 16, 24. KPK adalah 24. Menambahkan 24 hari ke tanggal 8 Agustus 2022. Agustus memiliki 31 hari. 8 + 24 = 32. 32 - 31 = 1. Jadi, tanggal 1 September 2022.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan konsep KPK untuk menyelesaikan masalah kontekstual yang rutin. Siswa perlu mengidentifikasi bahwa ini adalah masalah kelipatan persekutuan terkecil dan melakukan perhitungan kalender sederhana.. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari. Karena Aldi baru mencoba untuk ikut berbagi makanan, maka ia akan melakukannya setiap 8 hari.; Jika pada hari ini, Senin tanggal 8 Agustus 2022 mereka bertiga membagikan makanan secara bersama-sama, maka tanggal berapa mereka melakukannya bersama kembali?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara jadwal rutin dan konsep kelipatan persekutuan terkecil (KPK) untuk menentukan waktu pertemuan berikutnya.. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari. Karena Aldi baru mencoba untuk ikut berbagi makanan, maka ia akan melakukannya setiap 8 hari.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua tahap utama: menentukan KPK dari tiga bilangan (4, 6, 8) dan melakukan konversi tanggal dengan memperhatikan jumlah hari dalam bulan Agustus. Meskipun prosedurnya familiar, siswa harus mengintegrasikan pengetahuan kalender (Agustus memiliki 31 hari) dengan hasil perhitungan KPK.. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari. Karena Aldi baru mencoba untuk ikut berbagi makanan, maka ia akan melakukannya setiap 8 hari.; Jika pada hari ini, Senin tanggal 8 Agustus 2022 mereka bertiga membagikan makanan secara bersama-sama, maka tanggal berapa mereka melakukannya bersama kembali?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep KPK, operasi penjumlahan bilangan bulat, pengetahuan dasar kalender (jumlah hari dalam bulan). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah KPK tiga bilangan dan penambahan tanggal adalah materi standar kelas 7. Tingkat kesulitan Medium diberikan karena adanya kebutuhan untuk memperhatikan jumlah hari dalam bulan (Agustus 31 hari) yang sering menjadi jebakan bagi siswa. |

Run 2 — solusi: Menentukan KPK dari 4, 6, dan 8. Faktorisasi prima: 4=2^2, 6=2x3, 8=2^3. KPK = 2^3 x 3 = 24. Mereka bertemu kembali 24 hari setelah 8 Agustus. Agustus memiliki 31 hari. 31 - 8 = 23 hari tersisa di bulan Agustus. Maka 24 - 23 = 1 hari di bulan berikutnya, yaitu 1 September 2022.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa masalah ini menuntut pencarian kelipatan persekutuan terkecil (KPK) dari tiga bilangan untuk menentukan waktu pertemuan berikutnya, yang merupakan penerapan konsep dasar KPK dalam konteks rutin.. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari. Karena Aldi baru mencoba untuk ikut berbagi makanan, maka ia akan melakukannya setiap 8 hari.; mereka bertiga membagikan makanan secara bersama-sama, maka tanggal berapa mereka melakukannya bersama kembali?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara mencari KPK dan menerapkannya pada situasi nyata (penjadwalan).. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari. Karena Aldi baru mencoba untuk ikut berbagi makanan, maka ia akan melakukannya setiap 8 hari.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua tahap utama: menghitung KPK dari tiga bilangan (4, 6, 8) dan melakukan perhitungan kalender yang melibatkan transisi bulan (Agustus ke September). Meskipun prosedurnya familiar, siswa harus teliti dalam menghitung jumlah hari dalam bulan Agustus untuk menentukan tanggal yang tepat.. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari. Karena Aldi baru mencoba untuk ikut berbagi makanan, maka ia akan melakukannya setiap 8 hari.; Jika pada hari ini, Senin tanggal 8 Agustus 2022 mereka bertiga membagikan makanan secara bersama-sama, maka tanggal berapa mereka melakukannya bersama kembali?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep KPK, faktorisasi prima, dan pengetahuan jumlah hari dalam bulan kalender. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah mempelajari KPK dan operasi bilangan. Tantangan utama terletak pada ketelitian menghitung durasi hari melintasi batas bulan, yang merupakan keterampilan dasar yang sesuai untuk tingkat ini. |

Run 3 — solusi: Menentukan KPK dari 4, 6, dan 8. Kelipatan 4: 4, 8, 12, 16, 20, 24. Kelipatan 6: 6, 12, 18, 24. Kelipatan 8: 8, 16, 24. KPK adalah 24. Menambahkan 24 hari ke tanggal 8 Agustus 2022. Agustus memiliki 31 hari. 31 - 8 = 23 hari tersisa di bulan Agustus. Maka 24 - 23 = 1 hari di bulan September. Tanggal 1 September 2022.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa masalah ini memerlukan pencarian KPK dari tiga bilangan (4, 6, 8) untuk menentukan interval waktu bersama, kemudian menerapkan hasil tersebut pada kalender (penjumlahan tanggal). Ini adalah penerapan konsep KPK dalam konteks rutin.. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari. Karena Aldi baru mencoba untuk ikut berbagi makanan, maka ia akan melakukannya setiap 8 hari.; Jika pada hari ini, Senin tanggal 8 Agustus 2022 mereka bertiga membagikan makanan secara bersama-sama, maka tanggal berapa mereka melakukannya bersama kembali?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara mencari KPK dan menerapkannya pada situasi nyata (penjadwalan).. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari. Karena Aldi baru mencoba untuk ikut berbagi makanan, maka ia akan melakukannya setiap 8 hari.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua tahap utama: mencari KPK dari tiga bilangan dan melakukan konversi tanggal dengan memperhatikan jumlah hari dalam bulan (Agustus 31 hari). Meskipun prosedurnya familiar, siswa harus mengintegrasikan pengetahuan kalender dengan hasil perhitungan KPK.. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari. Karena Aldi baru mencoba untuk ikut berbagi makanan, maka ia akan melakukannya setiap 8 hari.; Jika pada hari ini, Senin tanggal 8 Agustus 2022 mereka bertiga membagikan makanan secara bersama-sama, maka tanggal berapa mereka melakukannya bersama kembali?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep KPK, operasi penjumlahan dasar, dan pengetahuan jumlah hari dalam bulan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 7 sudah mempelajari KPK dan penggunaan kalender. Tantangan utama adalah ketelitian dalam menghitung sisa hari di bulan Agustus (31 hari) untuk menentukan tanggal di bulan berikutnya. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4847`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Soal ini meminta siswa menerapkan prosedur KPK yang sudah dipelajari untuk menyelesaikan masalah kontekstual rutin. Siswa perlu mengidentifikasi bahwa ini adalah masalah kelipatan persekutuan terkecil dan melakukan perhitungan kalender sederhana.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang cara mencari KPK dan menerapkannya pada situasi nyata (penjadwalan).
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena memerlukan dua tahap utama: mencari KPK dari tiga bilangan dan melakukan konversi tanggal dengan memperhatikan jumlah hari dalam bulan (Agustus 31 hari). Meskipun prosedurnya familiar, siswa harus mengintegrasikan pengetahuan kalender dengan hasil perhitungan KPK.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep KPK, operasi penjumlahan dasar, dan pengetahuan jumlah hari dalam bulan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah mempelajari KPK dan penggunaan kalender. Tantangan utama adalah ketelitian dalam menghitung sisa hari di bulan Agustus (31 hari) untuk menentukan tanggal di bulan berikutnya. |

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
Solusi minimum hasil AI: Menentukan KPK dari 4 dan 6. Kelipatan 4 adalah 4, 8, 12, 16... Kelipatan 6 adalah 6, 12, 18... KPK(4, 6) = 12. Jadi, mereka akan membagikan makanan bersama-sama kembali setiap 12 hari.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['mengidentifikasi', 'menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `dabba6e375d5431a3e352dd44bd45f6bf3fea5e9251e78563f4d41e548f57d5c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2431 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2425 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2427 |

Run 1 — solusi: Menentukan KPK dari 4 dan 6. Kelipatan 4 adalah 4, 8, 12, 16... Kelipatan 6 adalah 6, 12, 18... KPK(4, 6) = 12. Jadi, mereka akan membagikan makanan bersama-sama kembali setiap 12 hari.
- Domain kognitif `classify/applying`: Soal ini meminta siswa untuk menerapkan konsep KPK dalam konteks masalah sehari-hari yang rutin. Siswa perlu mengenali bahwa situasi 'bersama-sama kembali' memerlukan penentuan kelipatan persekutuan terkecil.. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari.; tentukan setiap berapa hari mereka membagikan makanan secara bersama-sama kembali?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep kelipatan dan hubungan antara siklus waktu yang berbeda untuk menentukan titik temu berikutnya, yang merupakan pemahaman konseptual tentang KPK.. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari.; tentukan setiap berapa hari mereka membagikan makanan secara bersama-sama kembali?
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena merupakan masalah rutin yang sangat umum di kelas 7. Jalur penyelesaiannya jelas (mencari KPK), tidak ada kendala yang berinteraksi, dan beban kognitifnya rendah.. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari.; tentukan setiap berapa hari mereka membagikan makanan secara bersama-sama kembali?

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
| gradeRelativeRationale | Masalah KPK dua bilangan adalah standar kurikulum kelas 7 dan sering diajarkan sebagai prosedur rutin. |

Run 2 — solusi: Menentukan KPK dari 4 dan 6. Kelipatan 4 adalah 4, 8, 12, 16, ... Kelipatan 6 adalah 6, 12, 18, ... KPK(4, 6) = 12. Jadi, mereka akan membagikan makanan bersama-sama kembali setiap 12 hari.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa masalah ini menuntut pencarian kelipatan persekutuan terkecil (KPK) dari dua bilangan yang diberikan untuk menentukan waktu pertemuan berikutnya. Ini adalah penerapan prosedur standar pada konteks rutin.. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari.; tentukan setiap berapa hari mereka membagikan makanan secara bersama-sama kembali?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang kelipatan dan prosedur untuk mencari KPK dalam konteks masalah cerita.. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari.; tentukan setiap berapa hari mereka membagikan makanan secara bersama-sama kembali?
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin yang sangat umum di kelas 7. Siswa hanya perlu mengenali pola masalah 'pertemuan kembali' sebagai masalah KPK dan menerapkan prosedur KPK yang sudah familiar. Tidak ada kendala yang berinteraksi atau perencanaan kompleks yang diperlukan.. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari.; tentukan setiap berapa hari mereka membagikan makanan secara bersama-sama kembali?

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
| gradeRelativeRationale | Masalah KPK dua bilangan adalah materi dasar kelas 7 yang sering dilatih dengan prosedur rutin. |

Run 3 — solusi: Menentukan KPK dari 4 dan 6. Kelipatan 4 adalah 4, 8, 12, 16, ... Kelipatan 6 adalah 6, 12, 18, ... KPK(4, 6) = 12. Jadi, mereka akan membagikan makanan bersama-sama kembali setiap 12 hari.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan konsep KPK untuk menyelesaikan masalah kontekstual rutin. Siswa perlu mengenali bahwa situasi 'kejadian berulang bersama' memerlukan pencarian kelipatan persekutuan terkecil.. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari.; tentukan setiap berapa hari mereka membagikan makanan secara bersama-sama kembali?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara siklus kejadian dan konsep kelipatan persekutuan (KPK) untuk memecahkan masalah.. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari.; tentukan setiap berapa hari mereka membagikan makanan secara bersama-sama kembali?
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin yang sangat umum di kelas 7. Jalur penyelesaiannya jelas (mencari KPK), tidak ada kendala yang berinteraksi, dan beban kognitifnya rendah karena hanya melibatkan satu konsep dasar.. Bukti: Anita membagikan makanan setiap 4 hari, sedangkan Rossa membagikan makanan setiap 6 hari.; tentukan setiap berapa hari mereka membagikan makanan secara bersama-sama kembali?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang kelipatan bilangan dan konsep KPK. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah KPK dua bilangan adalah standar kurikulum kelas 7 dan merupakan prosedur rutin yang diajarkan secara eksplisit. |

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
Solusi minimum hasil AI: Faktorisasi prima: 7 = 7, 18 = 2 x 3^2, 33 = 3 x 11. FPB adalah faktor prima persekutuan terbesar yang membagi ketiganya. Karena tidak ada faktor prima yang sama untuk ketiganya, FPB = 1. KPK adalah hasil kali semua faktor prima dengan pangkat tertinggi: 2 x 3^2 x 7 x 11 = 2 x 9 x 7 x 11 = 1.386.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8f8978e72d353e331d0451edfe84538638844a47696fd3dc84489465953d3589`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2434 |
| 2 | success | valid / verified | applying | procedural | Easy | 2482 |
| 3 | success | valid / verified | applying | procedural | Medium | 2513 |

Run 1 — solusi: Faktorisasi prima: 7 = 7; 18 = 2 x 3^2; 33 = 3 x 11. KPK = 2 x 3^2 x 7 x 11 = 1.386. FPB = 1 (karena tidak ada faktor prima yang sama untuk ketiga bilangan tersebut).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur faktorisasi prima untuk menentukan KPK dan FPB dari tiga bilangan. Ini adalah penerapan langsung dari algoritma yang sudah dipelajari.. Bukti: Tentukan KPK dan FPB dari bilangan-bilangan berikut dengan menggunakan cara faktorisasi prima
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma atau metode faktorisasi prima yang spesifik untuk menyelesaikan masalah.. Bukti: menggunakan cara faktorisasi prima dan cara pembagian berulang
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena melibatkan tiga bilangan dengan faktorisasi yang sedikit lebih kompleks (terdapat faktor 3^2 pada 18) dibandingkan hanya dua bilangan, namun prosedurnya sangat rutin dan familiar bagi siswa kelas 7.. Bukti: 7, 18, 33

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep bilangan prima, faktorisasi prima, dan definisi KPK/FPB. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun prosedurnya rutin, melakukan faktorisasi dan menentukan KPK/FPB untuk tiga bilangan sekaligus meningkatkan beban kognitif dibandingkan dua bilangan, namun tetap berada dalam cakupan standar kelas 7. |

Run 2 — solusi: Faktorisasi prima: 7 = 7, 18 = 2 x 3^2, 33 = 3 x 11. FPB adalah faktor prima persekutuan terkecil, karena tidak ada faktor prima yang sama untuk ketiganya, maka FPB = 1. KPK adalah hasil kali semua faktor prima dengan pangkat terbesar: 2 x 3^2 x 7 x 11 = 2 x 9 x 7 x 11 = 1.386.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan prosedur faktorisasi prima yang sudah dipelajari untuk menentukan KPK dan FPB dari tiga bilangan. Ini adalah penerapan langsung dari algoritma yang familiar.. Bukti: Tentukan KPK dan FPB dari bilangan-bilangan berikut dengan menggunakan cara faktorisasi prima
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami dan menerapkan algoritma faktorisasi prima untuk mencari KPK dan FPB.. Bukti: menggunakan cara faktorisasi prima dan cara pembagian berulang
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena melibatkan prosedur standar (faktorisasi prima) untuk tiga bilangan yang relatif kecil. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin; siswa hanya perlu melakukan faktorisasi dan menerapkan aturan KPK/FPB secara langsung.. Bukti: 7, 18, 33

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman faktorisasi prima dan definisi KPK/FPB. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari KPK/FPB dari tiga bilangan adalah materi standar kelas 7. Prosedur faktorisasi prima adalah metode rutin yang diajarkan untuk menyelesaikan masalah ini. |

Run 3 — solusi: Faktorisasi prima: 7 = 7, 18 = 2 x 3^2, 33 = 3 x 11. FPB adalah faktor persekutuan terbesar yang membagi ketiganya, karena tidak ada faktor prima yang sama untuk ketiganya, FPB = 1. KPK adalah hasil kali semua faktor prima dengan pangkat tertinggi: 2 x 3^2 x 7 x 11 = 2 x 9 x 7 x 11 = 1.26 x 11 = 1.386.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan prosedur faktorisasi prima yang sudah dipelajari untuk menentukan KPK dan FPB dari tiga bilangan. Ini adalah penerapan langsung dari algoritma yang familiar.. Bukti: Tentukan KPK dan FPB dari bilangan-bilangan berikut dengan menggunakan cara faktorisasi prima
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman dan penerapan prosedur faktorisasi prima untuk mencari KPK dan FPB.. Bukti: menggunakan cara faktorisasi prima
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena melibatkan tiga bilangan yang harus difaktorkan dan diintegrasikan untuk mencari KPK dan FPB. Meskipun prosedurnya rutin, siswa harus berhati-hati dalam menentukan faktor prima (terutama 18 = 2 x 3^2) dan mengalikan faktor-faktor tersebut untuk KPK, yang memerlukan ketelitian lebih tinggi daripada dua bilangan.. Bukti: 7, 18, 33

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep bilangan prima, faktorisasi prima, dan definisi KPK/FPB. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 7, mencari KPK/FPB dari tiga bilangan adalah standar. Tingkat kesulitan Medium diberikan karena adanya tiga bilangan yang memerlukan ketelitian dalam faktorisasi dan penggabungan faktor (terutama pangkat pada 18), bukan karena kompleksitas konsep. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4137`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan prosedur faktorisasi prima yang sudah dipelajari untuk menentukan KPK dan FPB dari tiga bilangan. Ini adalah penerapan langsung dari algoritma yang familiar.
- Dimensi pengetahuan `procedural`: Soal menuntut penggunaan algoritma atau metode faktorisasi prima yang spesifik untuk menyelesaikan masalah.
- Intended difficulty `Medium`: Soal ini tergolong Medium karena melibatkan tiga bilangan yang harus difaktorkan dan diintegrasikan untuk mencari KPK dan FPB. Meskipun prosedurnya rutin, siswa harus berhati-hati dalam menentukan faktor prima (terutama 18 = 2 x 3^2) dan mengalikan faktor-faktor tersebut untuk KPK, yang memerlukan ketelitian lebih tinggi daripada dua bilangan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep bilangan prima, faktorisasi prima, dan definisi KPK/FPB. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari KPK/FPB dari tiga bilangan adalah materi standar kelas 7. Tingkat kesulitan Medium diberikan karena adanya tiga bilangan yang memerlukan ketelitian dalam faktorisasi dan penggabungan faktor (terutama pangkat pada 18), bukan karena kompleksitas konsep. |

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
| 1 | success | valid / verified | applying | conceptual | Easy | 2636 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2623 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2558 |

Run 1 — solusi: Total uang Ibu = (4 x 100.000) + (4 x 10.000) + (3 x 1.000) = 400.000 + 40.000 + 3.000 = 443.000. Kekurangan uang = 450.000 - 443.000 = 7.000.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi nilai nominal uang (dekomposisi bilangan) dan menerapkan operasi aritmetika dasar untuk menentukan selisih. Ini adalah penerapan prosedur yang familiar dalam konteks rutin.. Bukti: Ibu akan membeli seragam sekolah seharga Rp450.000,00.; Ibu hanya mempunyai uang 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang nilai tempat dan komposisi bilangan (konsep dasar nilai mata uang) yang kemudian dioperasikan secara prosedural.. Bukti: 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan alur penyelesaian yang jelas (menghitung total uang lalu mencari selisih). Tidak ada kendala yang berinteraksi atau kebutuhan strategi non-rutin.. Bukti: Ibu akan membeli seragam sekolah seharga Rp450.000,00.; 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi penjumlahan dan pengurangan bilangan cacah sampai 1.000.000. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sesuai untuk kelas 7 sebagai penguatan konsep bilangan dan operasi dasar yang sudah dipelajari di jenjang sebelumnya. |

Run 2 — solusi: Total uang Ibu = (4 x 100.000) + (4 x 10.000) + (3 x 1.000) = 400.000 + 40.000 + 3.000 = 443.000. Kekurangan uang = 450.000 - 443.000 = 7.000.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi nilai nominal uang (dekomposisi bilangan) dan melakukan operasi pengurangan untuk menemukan selisih. Ini adalah penerapan prosedur aritmetika dasar pada konteks rutin.. Bukti: Ibu akan membeli seragam sekolah seharga Rp450.000,00.; Ibu hanya mempunyai uang 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang nilai tempat dan komposisi bilangan (konsep dasar nilai mata uang) yang kemudian dioperasikan secara prosedural.. Bukti: 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena jalur penyelesaian sangat jelas dan langsung. Siswa hanya perlu menghitung total uang yang dimiliki lalu menguranginya dari harga barang. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Ibu akan membeli seragam sekolah seharga Rp450.000,00.; 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi penjumlahan dan pengurangan bilangan cacah sampai 1.000.000. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini sangat mendasar untuk kelas 7, melibatkan operasi aritmetika yang sudah dipelajari di jenjang sebelumnya dengan konteks sehari-hari yang sederhana. |

Run 3 — solusi: Total uang Ibu = (4 * 100.000) + (4 * 10.000) + (3 * 1.000) = 400.000 + 40.000 + 3.000 = 443.000. Kekurangan uang = 450.000 - 443.000 = 7.000.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi nilai dari komposisi uang yang diberikan, menjumlahkannya, lalu melakukan operasi pengurangan untuk mencari selisih. Ini adalah penerapan prosedur aritmetika dasar pada konteks rutin.. Bukti: Ibu hanya mempunyai uang 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan; Berapakah kurangnya uang ibu?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang nilai tempat dan komposisi bilangan (dekomposisi nilai uang) yang merupakan pengetahuan konseptual dasar.. Bukti: 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang sangat jelas. Siswa hanya perlu melakukan perkalian sederhana dan penjumlahan untuk menentukan total uang, kemudian pengurangan untuk mencari selisih. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi nonrutin.. Bukti: Ibu akan membeli seragam sekolah seharga Rp450.000,00; 4 lembar seratus ribuan, 4 lembar sepuluh ribuan, 3 lembar seribuan

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
| gradeRelativeRationale | Soal ini sangat sesuai untuk kelas 7 sebagai latihan dasar aritmetika dan pemahaman nilai bilangan, dengan beban kognitif yang rendah. |

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
Solusi minimum hasil AI: Bilangan rasional didefinisikan sebagai bilangan yang dapat dinyatakan sebagai a/b (a, b bilangan bulat, b tidak nol). Bilangan desimal tak terbatas yang tidak berulang (seperti akar 2, pi, dan e) tidak dapat dinyatakan dalam bentuk tersebut, sehingga ketiganya adalah bilangan irasional.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `77f839f763c5111a416cd01b486291fc39678647a7803b83b5c9090c3a630572`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Easy | 2495 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 2560 |
| 3 | success | valid / verified | reasoning | conceptual | Medium | 2558 |

Run 1 — solusi: Bilangan rasional adalah bilangan yang dapat dinyatakan sebagai a/b (a, b bilangan bulat, b tidak nol). Bilangan desimal tak terbatas yang tidak berulang (seperti akar 2, pi, dan e) tidak dapat dinyatakan dalam bentuk tersebut, sehingga ketiganya adalah bilangan irasional.
- Domain kognitif `classify/reasoning`: Soal ini menuntut siswa untuk memahami definisi bilangan rasional dan membedakannya dari bilangan irasional berdasarkan sifat desimalnya, bukan sekadar menghitung.. Bukti: Apakah semua bilangan desimal merupakan bilangan rasional?; Apakah kalian dapat menyatakan ketiga bilangan di atas dalam pembagian bilangan bulat a/b dengan b tidak 0?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep dasar bilangan rasional dan irasional serta hubungan antara representasi desimal dan bentuk pecahan.. Bukti: Apakah semua bilangan desimal merupakan bilangan rasional?; ketiganya memiliki angka desimal yang tak terbatas
- Intended difficulty `classify/Easy`: Soal ini menguji pemahaman konseptual yang mendasar namun krusial. Meskipun konsepnya abstrak, jalur penyelesaiannya langsung bagi siswa yang memahami definisi bilangan rasional, tanpa memerlukan perhitungan kompleks atau perencanaan langkah yang panjang.. Bukti: Apakah semua bilangan desimal merupakan bilangan rasional?; ketiganya memiliki angka desimal yang tak terbatas

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi bilangan rasional sebagai hasil bagi dua bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Memahami perbedaan bilangan rasional dan irasional adalah bagian dari kurikulum bilangan kelas 7. Soal ini bersifat konseptual dan tidak menuntut langkah prosedural yang rumit. |

Run 2 — solusi: Bilangan rasional adalah bilangan yang dapat dinyatakan sebagai a/b (a, b bilangan bulat, b tidak nol). Bilangan desimal tak terbatas yang tidak berulang (seperti akar 2, pi, dan e) tidak dapat dinyatakan sebagai pecahan a/b, sehingga ketiganya adalah bilangan irasional.
- Domain kognitif `classify/reasoning`: Soal ini menuntut siswa untuk memahami definisi bilangan rasional dan membedakannya dari bilangan irasional berdasarkan sifat desimalnya, bukan sekadar menghitung.. Bukti: Apakah semua bilangan desimal merupakan bilangan rasional?; Apakah kalian dapat menyatakan ketiga bilangan di atas dalam pembagian bilangan bulat a/b
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang klasifikasi bilangan (rasional vs irasional) dan sifat representasi desimalnya.. Bukti: Apakah semua bilangan desimal merupakan bilangan rasional?; ketiganya memiliki angka desimal yang tak terbatas
- Intended difficulty `classify/Medium`: Soal ini menuntut pemahaman konseptual yang mendalam tentang definisi bilangan rasional. Meskipun terlihat sederhana, siswa sering memiliki miskonsepsi bahwa semua desimal tak terbatas adalah rasional. Ini memerlukan evaluasi terhadap sifat bilangan irasional, yang merupakan konsep abstrak bagi siswa kelas 7.. Bukti: Apakah semua bilangan desimal merupakan bilangan rasional?; ketiganya memiliki angka desimal yang tak terbatas

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
| distractorQuality | plausible |
| gradeRelativeRationale | Membedakan bilangan rasional dan irasional berdasarkan sifat desimalnya adalah konsep yang menantang di kelas 7, karena siswa cenderung menggeneralisasi bahwa semua desimal tak terbatas adalah rasional (seperti 1/3 = 0,333...). Soal ini menguji pemahaman konseptual, bukan prosedur hitung. |

Run 3 — solusi: Bilangan rasional adalah bilangan yang dapat dinyatakan sebagai pembagian dua bilangan bulat (a/b). Bilangan desimal tak terbatas yang tidak berulang (seperti akar 2, pi, dan e) tidak dapat dinyatakan sebagai pembagian dua bilangan bulat, sehingga ketiganya adalah bilangan irasional.
- Domain kognitif `classify/reasoning`: Soal ini menuntut siswa untuk memahami definisi bilangan rasional dan mengklasifikasikan bilangan berdasarkan sifat desimalnya (berulang vs tidak berulang). Ini memerlukan pemahaman konseptual tentang klasifikasi bilangan, bukan sekadar prosedur hitung.. Bukti: Apakah semua bilangan desimal merupakan bilangan rasional?; Apakah kalian dapat menyatakan ketiga bilangan di atas dalam pembagian bilangan bulat a/b
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang definisi dan kategori bilangan (rasional vs irasional), yang merupakan pengetahuan konseptual.. Bukti: Apakah semua bilangan desimal merupakan bilangan rasional?; ketiganya memiliki angka desimal yang tak terbatas
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena menuntut pemahaman konseptual yang mendalam tentang sifat bilangan irasional. Siswa tidak bisa hanya mengandalkan prosedur rutin; mereka harus mengenali bahwa desimal tak terbatas tidak otomatis berarti rasional (perlu berulang). Ini memerlukan integrasi konsep yang lebih tinggi daripada sekadar operasi dasar.. Bukti: Apakah semua bilangan desimal merupakan bilangan rasional?; ketiganya memiliki angka desimal yang tak terbatas

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi bilangan rasional sebagai a/b dan pemahaman dasar tentang desimal berulang vs tidak berulang. |
| dependentSteps | 2 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 7, membedakan bilangan rasional dan irasional berdasarkan sifat desimalnya adalah konsep yang menantang dan memerlukan penalaran konseptual, bukan sekadar hafalan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 3} | unanimous_3_0 / adjudicated | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 1, "Medium": 2} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4236`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `reasoning`: Soal ini menuntut siswa untuk menerapkan definisi konseptual bilangan rasional untuk mengevaluasi sifat bilangan irasional. Siswa harus membedakan antara desimal tak terbatas yang berulang (rasional) dan tidak berulang (irasional), yang merupakan proses penalaran konseptual.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman tentang kategori bilangan (rasional vs irasional) dan prinsip dasar representasi desimalnya, yang merupakan pengetahuan konseptual.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena menuntut pemahaman konseptual yang mendalam. Meskipun tidak ada perhitungan rumit, siswa sering terjebak pada miskonsepsi bahwa semua desimal tak terbatas adalah rasional. Membedakan sifat irasional memerlukan integrasi konsep yang lebih tinggi daripada sekadar prosedur rutin bagi siswa kelas 7.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi bilangan rasional sebagai hasil bagi dua bilangan bulat (a/b) dan pemahaman dasar tentang desimal berulang vs tidak berulang. |
| dependentSteps | 1 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membedakan bilangan rasional dan irasional berdasarkan sifat desimalnya adalah konsep yang menantang di kelas 7, karena siswa cenderung menggeneralisasi bahwa semua desimal tak terbatas adalah rasional. Soal ini menguji pemahaman konseptual, bukan prosedur hitung. |

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
Solusi minimum hasil AI: Definisi bilangan rasional a/b mensyaratkan b tidak sama dengan 0 karena operasi pembagian dengan nol tidak terdefinisi dalam sistem bilangan real.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `857d226ff010322873a3bc400b727739a59dd6a14a4575b1d42af5700d3f1fb4`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2311 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2362 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2339 |

Run 1 — solusi: Definisi bilangan rasional a/b mensyaratkan b tidak sama dengan 0 karena operasi pembagian dengan nol tidak terdefinisi dalam sistem bilangan real.
- Domain kognitif `classify/knowing`: Soal ini menuntut pemahaman konseptual tentang definisi bilangan rasional dan sifat dasar operasi pembagian, bukan sekadar prosedur menghitung.. Bukti: Mengapa pada bilangan rasional yang dinyatakan dalam a/b, nilai b tidak boleh nol?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman terhadap prinsip atau aturan dasar (definisi) dalam sistem bilangan rasional.. Bukti: Mengapa pada bilangan rasional yang dinyatakan dalam a/b, nilai b tidak boleh nol?
- Intended difficulty `classify/Easy`: Soal ini bersifat teoretis dan langsung menguji pemahaman definisi. Tidak ada langkah perhitungan atau integrasi yang diperlukan, hanya pengenalan konsep dasar.. Bukti: Mengapa pada bilangan rasional yang dinyatakan dalam a/b, nilai b tidak boleh nol?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang definisi bilangan rasional dan operasi pembagian. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pertanyaan ini merupakan konsep fundamental yang diajarkan di awal materi bilangan rasional kelas 7. Tidak ada kompleksitas prosedural. |

Run 2 — solusi: Dalam sistem bilangan, pembagian dengan nol tidak terdefinisi karena tidak ada bilangan yang jika dikalikan dengan nol menghasilkan pembilang yang bukan nol.
- Domain kognitif `classify/knowing`: Soal ini menuntut pemahaman konseptual tentang definisi bilangan rasional dan sifat dasar operasi pembagian. Siswa perlu mengenali prinsip fundamental bahwa pembagian dengan nol tidak terdefinisi, yang merupakan konsep dasar dalam aritmatika.. Bukti: Mengapa pada bilangan rasional yang dinyatakan dalam a/b, nilai b tidak boleh nol?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep dasar bilangan rasional dan aturan operasi pembagian, yang termasuk dalam kategori pengetahuan konseptual.. Bukti: Mengapa pada bilangan rasional yang dinyatakan dalam a/b, nilai b tidak boleh nol?
- Intended difficulty `classify/Easy`: Soal ini bersifat konseptual dan langsung. Siswa yang memahami definisi bilangan rasional akan langsung mengetahui alasan pembatasan penyebut. Tidak ada langkah perhitungan atau integrasi strategi yang diperlukan.. Bukti: Mengapa pada bilangan rasional yang dinyatakan dalam a/b, nilai b tidak boleh nol?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang definisi bilangan rasional dan operasi pembagian. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pertanyaan ini menguji pemahaman teoretis dasar yang diajarkan saat memperkenalkan bilangan rasional di kelas 7. Tingkat kesulitannya rendah karena hanya memerlukan ingatan atau pemahaman konsep dasar tanpa proses pemecahan masalah yang kompleks. |

Run 3 — solusi: Dalam sistem bilangan, pembagian dengan nol tidak terdefinisi karena tidak ada bilangan yang jika dikalikan dengan nol menghasilkan pembilang (a) yang bukan nol.
- Domain kognitif `classify/knowing`: Soal ini menguji pemahaman konseptual tentang definisi bilangan rasional dan sifat dasar pembagian dalam sistem bilangan. Siswa perlu memahami konsep pembagian sebagai invers perkalian.. Bukti: Mengapa pada bilangan rasional yang dinyatakan dalam a/b, nilai b tidak boleh nol?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menanyakan tentang prinsip dasar atau definisi dalam sistem bilangan, yang merupakan pengetahuan konseptual.. Bukti: Mengapa pada bilangan rasional yang dinyatakan dalam a/b, nilai b tidak boleh nol?
- Intended difficulty `classify/Easy`: Soal ini bersifat teoretis dan langsung menguji pemahaman definisi. Tidak ada perhitungan yang diperlukan, hanya pengenalan terhadap aturan dasar sistem bilangan yang diajarkan di kelas 7.. Bukti: Mengapa pada bilangan rasional yang dinyatakan dalam a/b, nilai b tidak boleh nol?

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
| gradeRelativeRationale | Pertanyaan ini adalah pertanyaan konseptual dasar yang sering dibahas saat memperkenalkan bilangan rasional di kelas 7. Tidak memerlukan langkah prosedural yang kompleks. |

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
Solusi minimum hasil AI: Hitung selisih berat Minggu 1 dengan berat saat menetas untuk setiap pakan: Pakan A = 152,6 - 42,9 = 109,7; Pakan B = 120,8 - 41,5 = 79,3; Pakan C = 155,4 - 48,3 = 107,1. Membandingkan 109,7, 79,3, dan 107,1, nilai tertinggi adalah 109,7 (Pakan A).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `95610264c521bebb1803d0ac97c5c7678fbb390378d08370eecdf09a1267d4b8`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2680 |
| 2 | success | valid / verified | applying | procedural | Easy | 2644 |
| 3 | success | valid / verified | applying | procedural | Easy | 2667 |

Run 1 — solusi: Hitung selisih berat Minggu 1 dengan berat saat menetas untuk setiap pakan: Pakan A = 152,6 - 42,9 = 109,7; Pakan B = 120,8 - 41,5 = 79,3; Pakan C = 155,4 - 48,3 = 107,1. Membandingkan 109,7, 79,3, dan 107,1, nilai tertinggi adalah 109,7 (Pakan A).
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan prosedur pengurangan bilangan desimal untuk menentukan selisih, kemudian membandingkan hasilnya untuk memilih jawaban yang tepat. Ini adalah penerapan konsep dasar dalam konteks rutin.. Bukti: Ayam yang diberi pakan apa yang memiliki penambahan berat tertinggi pada minggu pertama?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi pengurangan bilangan desimal dan perbandingan nilai untuk menyelesaikan masalah yang disajikan dalam bentuk tabel.. Bukti: Tabel di bawah ini menunjukkan hasil penimbangan berat ayam.
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena jalur penyelesaiannya sangat jelas (menghitung selisih dua data untuk setiap baris) dan tidak memerlukan perencanaan strategi yang kompleks atau integrasi kendala yang sulit bagi siswa kelas 7.. Bukti: Ayam yang diberi pakan apa yang memiliki penambahan berat tertinggi pada minggu pertama?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pengurangan bilangan desimal dan perbandingan bilangan desimal. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah familiar dengan operasi bilangan desimal dan interpretasi tabel sederhana. Tugas ini hanya memerlukan perhitungan rutin tanpa jebakan konseptual yang berat. |

Run 2 — solusi: Hitung selisih berat minggu ke-1 dengan saat menetas untuk setiap pakan: Pakan A = 152,6 - 42,9 = 109,7; Pakan B = 120,8 - 41,5 = 79,3; Pakan C = 155,4 - 48,3 = 107,1. Membandingkan ketiga hasil, 109,7 adalah yang tertinggi.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan prosedur pengurangan bilangan desimal untuk membandingkan selisih berat, yang merupakan penerapan konsep dasar bilangan rasional dalam konteks rutin.. Bukti: Ayam yang diberi pakan apa yang memiliki penambahan berat tertinggi pada minggu pertama?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma pengurangan bilangan desimal (prosedural) untuk menyelesaikan masalah perbandingan.. Bukti: Tabel di bawah ini menunjukkan hasil penimbangan berat ayam.
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena jalur penyelesaiannya sangat jelas (menghitung selisih), melibatkan operasi dasar yang familiar bagi kelas 7, dan tidak memerlukan integrasi konsep yang kompleks.. Bukti: Ayam yang diberi pakan apa yang memiliki penambahan berat tertinggi pada minggu pertama?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pengurangan bilangan desimal. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah terbiasa dengan operasi bilangan desimal dan interpretasi tabel sederhana. Soal tidak memiliki jebakan konseptual yang rumit. |

Run 3 — solusi: Hitung selisih berat minggu ke-1 dengan saat menetas untuk setiap pakan: Pakan A = 152,6 - 42,9 = 109,7; Pakan B = 120,8 - 41,5 = 79,3; Pakan C = 155,4 - 48,3 = 107,1. Nilai tertinggi adalah 109,7 (Pakan A).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pengurangan bilangan desimal untuk membandingkan selisih berat (penambahan) antar pakan. Ini adalah penerapan konsep operasi bilangan rasional pada konteks data tabel.. Bukti: Ayam yang diberi pakan apa yang memiliki penambahan berat tertinggi pada minggu pertama?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritme pengurangan bilangan desimal (prosedural) untuk mengolah data yang disajikan dalam tabel.. Bukti: Tabel di bawah ini menunjukkan hasil penimbangan berat ayam.
- Intended difficulty `classify/Easy`: Soal memerlukan perhitungan selisih untuk tiga kategori data. Jalur penyelesaian sangat jelas (pengurangan), tidak ada kendala yang berinteraksi, dan prosedur pengurangan desimal adalah materi dasar kelas 7.. Bukti: Ayam yang diberi pakan apa yang memiliki penambahan berat tertinggi pada minggu pertama?

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
| gradeRelativeRationale | Tugas ini adalah latihan rutin membandingkan nilai selisih dari data tabel. Beban kognitif utama hanya pada ketelitian operasi pengurangan desimal, yang sesuai untuk tingkat kelas 7. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: Lihat kolom 'Minggu 1' pada tabel: Pakan A = 152,6; Pakan B = 120,8; Pakan C = 155,4. Membandingkan ketiga bilangan desimal tersebut, 155,4 adalah yang terbesar.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `02a8bc73b4e3ba6566d884a972a476e1a511100176685abc59f2ca2debd375fa`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2512 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2555 |
| 3 | success | valid / verified | knowing | factual | Easy | 2571 |

Run 1 — solusi: Lihat kolom 'Minggu 1' pada tabel: Pakan A = 152,6; Pakan B = 120,8; Pakan C = 155,4. Membandingkan ketiga bilangan desimal tersebut, 155,4 adalah yang terbesar.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data dari tabel dan melakukan perbandingan langsung antara tiga bilangan desimal untuk menentukan nilai terbesar.. Bukti: Ayam yang diberi pakan apa yang memiliki berat tertinggi pada minggu pertama?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang cara membaca tabel dan membandingkan nilai bilangan desimal.. Bukti: Tabel 2.10 Berat Ayam
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena hanya menuntut pembacaan data langsung dari tabel tanpa perlu melakukan perhitungan tambahan atau analisis kompleks. Jalur penyelesaian sangat jelas.. Bukti: Ayam yang diberi pakan apa yang memiliki berat tertinggi pada minggu pertama?

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
| distractorQuality | weak |
| gradeRelativeRationale | Tugas membandingkan bilangan desimal sederhana adalah materi dasar kelas 7 yang rutin dilakukan. |

Run 2 — solusi: Lihat kolom 'Minggu 1' pada tabel. Bandingkan nilai desimal untuk setiap pakan: Pakan A = 152,6; Pakan B = 120,8; Pakan C = 155,4. Nilai tertinggi adalah 155,4 yang merupakan milik Pakan C.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk membaca data dari tabel dan membandingkan nilai desimal secara langsung. Ini adalah aktivitas mengenali dan membandingkan fakta numerik tanpa perlu manipulasi atau strategi kompleks.. Bukti: Ayam yang diberi pakan apa yang memiliki berat tertinggi pada minggu pertama?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami cara membaca tabel dan membandingkan nilai desimal (bilangan rasional), yang merupakan pengetahuan konseptual dasar tentang sistem bilangan.. Bukti: Tabel 2.10 Berat Ayam
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mencari kolom 'Minggu 1' dan membandingkan tiga angka desimal yang tersedia. Tidak ada langkah perantara, tidak ada perhitungan, dan tidak ada kendala yang berinteraksi.. Bukti: Ayam yang diberi pakan apa yang memiliki berat tertinggi pada minggu pertama?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca tabel sederhana dan membandingkan nilai desimal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Tugas membandingkan tiga angka desimal dalam tabel adalah keterampilan dasar yang diharapkan sudah dikuasai siswa kelas 7. |

Run 3 — solusi: Lihat kolom 'Minggu 1' pada tabel. Berat ayam untuk pakan A adalah 152,6 gram, pakan B adalah 120,8 gram, dan pakan C adalah 155,4 gram. Membandingkan ketiga bilangan desimal tersebut (155,4 > 152,6 > 120,8), berat tertinggi adalah 155,4 gram yang berasal dari pakan C.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk membaca data dari tabel dan melakukan perbandingan langsung antara tiga bilangan desimal. Ini adalah tugas mengenali dan membandingkan nilai, yang termasuk dalam domain knowing.. Bukti: Ayam yang diberi pakan apa yang memiliki berat tertinggi pada minggu pertama?
- Dimensi pengetahuan `classify/factual`: Siswa perlu memahami cara membaca tabel dan membandingkan nilai bilangan desimal, yang merupakan pengetahuan faktual tentang data yang disajikan.. Bukti: Tabel 2.10 Berat Ayam
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mencari kolom 'Minggu 1' dan membandingkan tiga angka desimal yang tersedia. Tidak ada langkah perantara, perhitungan kompleks, atau integrasi konsep yang diperlukan.. Bukti: Ayam yang diberi pakan apa yang memiliki berat tertinggi pada minggu pertama?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca tabel sederhana dan membandingkan bilangan desimal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas membaca tabel dan membandingkan bilangan desimal adalah keterampilan dasar yang diharapkan sudah dikuasai siswa kelas 7. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3952`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu membaca data dari tabel dan melakukan perbandingan langsung antara tiga bilangan desimal untuk menentukan nilai terbesar. Tidak ada manipulasi atau strategi kompleks yang diperlukan.
- Dimensi pengetahuan `factual`: Soal ini menguji pemahaman dasar tentang cara membaca tabel dan membandingkan nilai bilangan desimal (bilangan rasional).
- Intended difficulty `Easy`: Soal ini sangat langsung. Siswa hanya perlu mencari kolom 'Minggu 1' dan membandingkan tiga angka desimal yang tersedia. Tidak ada langkah perantara, tidak ada perhitungan, dan tidak ada kendala yang berinteraksi.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca tabel sederhana dan membandingkan nilai desimal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Tugas membandingkan tiga angka desimal dalam tabel adalah keterampilan dasar yang diharapkan sudah dikuasai siswa kelas 7. |

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
Solusi minimum hasil AI: 1. Hitung IMT setiap orang: Pak Bintoro = 50 / (1,7^2) = 50 / 2,89 ≈ 17,30 (masuk kategori 17,0-18,4). 2. Hitung berat badan target untuk IMT 18,5: BB_target = 18,5 * (1,7^2) = 18,5 * 2,89 = 53,465 kg. 3. Selisih berat badan: 53,465 - 50 = 3,465 kg.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `406d1dab271f4e6892ce5ebdfca159668f306eadd37040f30c885a4bbae5d172`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2936 |
| 2 | success | valid / verified | applying | procedural | Medium | 2953 |
| 3 | success | valid / verified | applying | procedural | Medium | 2953 |

Run 1 — solusi: 1. Hitung IMT setiap orang: Pak Bintoro = 50 / (1,7^2) = 50 / 2,89 ≈ 17,30 (masuk kategori 17,0-18,4). 2. Hitung berat badan target untuk IMT 18,5: BB_target = 18,5 * (1,7^2) = 18,5 * 2,89 = 53,465 kg. 3. Selisih berat badan: 53,465 - 50 = 3,465 kg.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus yang diberikan ke dalam data yang tersedia (applying) untuk mengidentifikasi individu yang memenuhi kriteria, kemudian memanipulasi rumus tersebut untuk mencari nilai berat badan yang diperlukan.. Bukti: Siapa yang memiliki IMT dengan kategori kekurangan berat badan tingkat ringan?; Berapa berat badan yang harus ditambah agar tercapai IMT sebesar 18,5?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma perhitungan (prosedural) berdasarkan rumus yang diberikan dan klasifikasi data berdasarkan kriteria yang sudah ditentukan (konseptual).. Bukti: Indeks Massa Tubuh = BB/TB^2; Tabel 2.12 Kategori Indeks Massa Tubuh; Tabel 2.13 Data Berat dan Tinggi Badan
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah yang saling terkait: menghitung IMT, membandingkan dengan tabel kategori, memanipulasi rumus untuk mencari variabel yang tidak diketahui (BB target), dan menghitung selisih. Meskipun prosedurnya familiar, integrasi langkah-langkah ini menuntut ketelitian.. Bukti: Siapa yang memiliki IMT dengan kategori kekurangan berat badan tingkat ringan?; Berapa berat badan yang harus ditambah agar tercapai IMT sebesar 18,5?

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
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu melakukan operasi hitung desimal dan mengikuti instruksi rumus, namun mengintegrasikan beberapa langkah perhitungan untuk memecahkan masalah dua bagian ini cukup menantang. |

Run 2 — solusi: 1. Hitung IMT Pak Bintoro: 50 / (1,70^2) = 50 / 2,89 ≈ 17,30 (masuk kategori 17,0-18,4). 2. Hitung target berat badan untuk IMT 18,5: 18,5 * (1,70^2) = 18,5 * 2,89 = 53,465 kg. 3. Hitung selisih berat: 53,465 - 50 = 3,465 kg.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus IMT yang diberikan untuk mengidentifikasi subjek yang memenuhi kriteria kategori tertentu, kemudian melakukan manipulasi aljabar sederhana (mengalikan IMT target dengan kuadrat tinggi badan) untuk menentukan selisih berat badan. Ini adalah penerapan prosedur pada konteks yang diberikan.. Bukti: Siapa yang memiliki IMT dengan kategori kekurangan berat badan tingkat ringan?; Berapa berat badan yang harus ditambah agar tercapai IMT sebesar 18,5?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan rumus (prosedural) dan pemahaman tentang bagaimana data tersebut dikategorikan berdasarkan rentang nilai (konseptual).. Bukti: Indeks Massa Tubuh = BB / TB^2; Tabel 2.12 Kategori Indeks Massa Tubuh; Tabel 2.13 Data Berat dan Tinggi Badan
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah yang saling terkait: menghitung IMT, membandingkan dengan tabel kategori, membalikkan rumus untuk mencari target berat badan, dan melakukan pengurangan. Meskipun prosedurnya familiar, siswa harus mengintegrasikan beberapa langkah tersebut secara mandiri.. Bukti: Siapa yang memiliki IMT dengan kategori kekurangan berat badan tingkat ringan?; Berapa berat badan yang harus ditambah agar tercapai IMT sebesar 18,5?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi hitung bilangan desimal, kuadrat, dan pemahaman rumus dasar. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah mempelajari operasi bilangan rasional dan pemodelan sederhana. Soal ini menuntut ketelitian dalam urutan operasi (kuadrat terlebih dahulu) dan pemahaman hubungan antar variabel dalam rumus, yang sesuai dengan tingkat kesulitan menengah untuk jenjang tersebut. |

Run 3 — solusi: 1. Hitung IMT Pak Bintoro: 50 / (1,70^2) = 50 / 2,89 ≈ 17,30 (masuk kategori 17,0-18,4). 2. Hitung target berat badan untuk IMT 18,5: 18,5 * 1,70^2 = 18,5 * 2,89 = 53,465 kg. 3. Hitung selisih berat: 53,465 - 50 = 3,465 kg.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus yang diberikan untuk mengidentifikasi kategori (applying) dan melakukan manipulasi aljabar sederhana (mengisolasi variabel BB) untuk menentukan selisih berat badan yang diperlukan.. Bukti: siapa yang memiliki IMT dengan kategori kekurangan berat badan tingkat ringan?; Berapa berat badan yang harus ditambah agar tercapai IMT sebesar 18,5?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan rumus (prosedural) yang diterapkan pada data yang diberikan untuk mengkategorikan dan menghitung nilai baru.. Bukti: Indeks Massa Tubuh = BB/TB^2; Tabel 2.12 Kategori Indeks Massa Tubuh; Tabel 2.13 Data Berat dan Tinggi Badan
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena menuntut dua langkah yang saling bergantung: pertama mengidentifikasi subjek yang memenuhi kriteria, kedua melakukan perhitungan terbalik (reverse calculation) menggunakan rumus yang diberikan. Meskipun prosedurnya familiar, siswa harus merencanakan langkah perhitungan target berat badan dengan benar.. Bukti: siapa yang memiliki IMT dengan kategori kekurangan berat badan tingkat ringan?; Berapa berat badan yang harus ditambah agar tercapai IMT sebesar 18,5?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi hitung bilangan desimal dan kuadrat. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu mengoperasikan bilangan desimal dan memahami penggunaan rumus sederhana. Tantangan terletak pada ketelitian perhitungan dan pemahaman bahwa target berat badan harus dihitung ulang berdasarkan IMT 18,5. |

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
Solusi minimum hasil AI: 20 / 1,25 = 16
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5c71394580fa88aa97ed1a47ad6d51fe9886cf6ea1634034d95595d4269e525b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2697 |
| 2 | success | valid / verified | applying | procedural | Easy | 2934 |
| 3 | success | valid / verified | applying | procedural | Easy | 2882 |

Run 1 — solusi: 20 / 1,25 = 16
- Domain kognitif `classify/applying`: Siswa diminta menerapkan operasi pembagian bilangan desimal dalam konteks kehidupan sehari-hari yang rutin.. Bukti: Ibu memiliki kain sepanjang 20 meter. Ibu ingin memotong-motong kain tersebut dengan panjang tiap potongan 1,25 m.
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penggunaan algoritme pembagian bilangan desimal yang merupakan prosedur standar.. Bukti: Berapa banyak potongan kain yang ibu dapat?
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung konsep pembagian dengan satu langkah penyelesaian. Tidak ada kendala yang berinteraksi atau kebutuhan perencanaan strategi yang kompleks.. Bukti: Ibu memiliki kain sepanjang 20 meter. Ibu ingin memotong-motong kain tersebut dengan panjang tiap potongan 1,25 m.

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
| gradeRelativeRationale | Pembagian bilangan bulat dengan desimal adalah kompetensi dasar kelas 7 yang rutin dan tidak memerlukan integrasi konsep yang rumit. |

Run 2 — solusi: 20 dibagi 1,25 sama dengan 16.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan operasi pembagian bilangan desimal pada konteks kehidupan sehari-hari yang rutin.. Bukti: Ibu memiliki kain sepanjang 20 meter; panjang tiap potongan 1,25 m; Berapa banyak potongan kain yang ibu dapat?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma pembagian bilangan desimal untuk menyelesaikan masalah.. Bukti: 20 meter; 1,25 m; Berapa banyak potongan
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari operasi pembagian bilangan desimal. Jalur penyelesaian sangat jelas, tidak ada kendala yang berinteraksi, dan konteksnya sangat familiar bagi siswa kelas 7.. Bukti: Ibu memiliki kain sepanjang 20 meter; panjang tiap potongan 1,25 m

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pembagian bilangan desimal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pembagian bilangan desimal adalah materi dasar kelas 7. Soal ini tidak memiliki kerumitan tambahan, hanya satu langkah operasi langsung. |

Run 3 — solusi: 20 dibagi 1,25 sama dengan 16.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dan menerapkan operasi pembagian bilangan desimal untuk menyelesaikan masalah kontekstual yang rutin.. Bukti: Ibu memiliki kain sepanjang 20 meter. Ibu ingin memotong-motong kain tersebut dengan panjang tiap potongan 1,25 m.
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritme pembagian bilangan desimal untuk mendapatkan hasil.. Bukti: 20 : 1,25 = 16
- Intended difficulty `classify/Easy`: Masalah ini adalah penerapan langsung operasi pembagian bilangan desimal dalam konteks sehari-hari. Jalur penyelesaian sangat jelas, tidak ada kendala yang berinteraksi, dan tidak memerlukan strategi nonrutin.. Bukti: Ibu memiliki kain sepanjang 20 meter. Ibu ingin memotong-motong kain tersebut dengan panjang tiap potongan 1,25 m.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pembagian bilangan desimal. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan soal rutin yang sesuai untuk kelas 7, tidak memerlukan perencanaan kompleks atau integrasi konsep yang sulit. |

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

![Gambar sumber soal 15](<../../../images/kelas6_panduan_siswa_kelas6.pdf-0055-02.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Samakan satuan ke gram (g). Natrium 88,6 mg = 0,0886 g. Membandingkan nilai: 0,0886 g (Natrium) < 1,3 g (Protein) < 2,7 g (Serat Pangan) < 5,4 g (Lemak) < 28,6 g (Karbohidrat). Jadi, yang terkecil adalah Natrium.
Gambar sumber: images/kelas6_panduan_siswa_kelas6.pdf-0055-02.png. Transkripsi visual: Informasi Nilai Gizi: Protein 1,3 g, Lemak total 5,4 g, Karbohidrat 28,6 g, Serat Pangan 2,7 g, Natrium 88,6 mg.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f88091eaa52e5cc6ed71dac5c92308f44d4bcc3efb361c09101094b01872f71e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3676 |
| 2 | success | valid / verified | applying | procedural | Medium | 3759 |
| 3 | success | valid / verified | applying | procedural | Easy | 3661 |

Run 1 — solusi: Untuk membandingkan nilai, samakan satuan ke gram (g). Natrium 88,6 mg = 0,0886 g. Membandingkan semua nilai: 0,0886 g (Natrium) < 1,3 g (Protein) < 2,7 g (Serat Pangan) < 5,4 g (Lemak) < 28,6 g (Karbohidrat). Jadi, yang terkecil adalah Natrium dengan 88,6 mg.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur konversi satuan (mg ke g) dan membandingkan nilai desimal untuk menentukan nilai terkecil. Ini adalah penerapan konsep dalam konteks rutin.. Bukti: Kandungan zat apakah yang paling kecil komposisinya dan berapakah komposisinya?; Natrium 88,6 mg
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritme konversi satuan (mg ke g) dan teknik perbandingan bilangan desimal.. Bukti: Natrium 88,6 mg; Protein 1,3 g
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak bisa langsung membandingkan angka (88,6 vs 1,3) tanpa melakukan konversi satuan terlebih dahulu. Terdapat dua langkah logis: konversi satuan dan perbandingan nilai. Meskipun prosedurnya familiar, siswa harus sadar akan perbedaan satuan (mg vs g) untuk menghindari kesalahan umum.. Bukti: Natrium 88,6 mg; Protein 1,3 g

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konversi satuan massa (mg ke g) dan perbandingan bilangan desimal. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 5 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu melakukan konversi satuan dasar dan membandingkan desimal. Tantangan utama adalah jebakan satuan (mg vs g) yang menguji ketelitian dalam membandingkan besaran. |

Run 2 — solusi: Konversi semua satuan ke gram: Protein 1,3 g, Lemak 5,4 g, Karbohidrat 28,6 g, Serat Pangan 2,7 g, Natrium 88,6 mg = 0,0886 g. Membandingkan nilai desimal: 0,0886 < 1,3 < 2,7 < 5,4 < 28,6. Jadi, yang terkecil adalah Natrium dengan 88,6 mg.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur konversi satuan (mg ke g) dan membandingkan bilangan desimal untuk menentukan nilai terkecil. Ini adalah penerapan konsep pada konteks rutin.. Bukti: Kandungan zat apakah yang paling kecil komposisinya; Protein 1,3 g, Lemak total 5,4 g, Karbohidrat 28,6 g, Serat Pangan 2,7 g, Natrium 88,6 mg
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman tentang hubungan antar satuan (konversi mg ke g) dan perbandingan nilai desimal, yang merupakan pengetahuan prosedural.. Bukti: Natrium 88,6 mg; 1,3 g, 5,4 g, 28,6 g, 2,7 g
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena menuntut siswa untuk menyadari perbedaan satuan (g vs mg) dan melakukan konversi sebelum membandingkan. Meskipun prosedurnya familiar, siswa harus berhati-hati dengan satuan yang berbeda untuk menghindari kesalahan perbandingan angka mentah.. Bukti: Natrium 88,6 mg; Protein 1,3 g, Lemak total 5,4 g, Karbohidrat 28,6 g, Serat Pangan 2,7 g

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konversi satuan massa (mg ke g) dan perbandingan bilangan desimal. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 5 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu membandingkan desimal, namun jebakan satuan (mg vs g) meningkatkan tuntutan kognitif dari sekadar membandingkan angka menjadi membandingkan nilai yang setara. |

Run 3 — solusi: Konversi semua satuan ke gram: Protein 1,3 g, Lemak 5,4 g, Karbohidrat 28,6 g, Serat 2,7 g, Natrium 88,6 mg = 0,0886 g. Membandingkan nilai desimal: 0,0886 < 1,3 < 2,7 < 5,4 < 28,6. Nilai terkecil adalah Natrium 88,6 mg.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman tentang konversi satuan (mg ke g) dan membandingkan bilangan desimal untuk menentukan nilai terkecil. Ini adalah penerapan konsep pada konteks rutin.. Bukti: Kandungan zat apakah yang paling kecil komposisinya; Protein 1,3 g, Lemak total 5,4 g, Karbohidrat 28,6 g, Serat Pangan 2,7 g, Natrium 88,6 mg
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman prosedural tentang konversi satuan metrik dan perbandingan nilai desimal.. Bukti: Natrium 88,6 mg = 0,0886 g
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu melakukan konversi satuan sederhana dan membandingkan bilangan desimal. Jalur penyelesaian sangat jelas dan tidak memerlukan perencanaan langkah yang kompleks.. Bukti: Natrium 88,6 mg; Protein 1,3 g

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang satuan massa (gram, miligram) dan perbandingan bilangan desimal. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 5 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu melakukan konversi satuan dasar dan membandingkan nilai desimal dalam konteks sehari-hari seperti label nutrisi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `5474`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur konversi satuan (mg ke g) dan membandingkan bilangan desimal untuk menentukan nilai terkecil. Ini adalah penerapan konsep pada konteks rutin.
- Dimensi pengetahuan `procedural`: Soal menuntut penggunaan algoritme konversi satuan (mg ke g) dan teknik perbandingan bilangan desimal.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena siswa tidak bisa langsung membandingkan angka (88,6 vs 1,3) tanpa melakukan konversi satuan terlebih dahulu. Terdapat dua langkah logis: konversi satuan dan perbandingan nilai. Meskipun prosedurnya familiar, siswa harus sadar akan perbedaan satuan (mg vs g) untuk menghindari kesalahan umum.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konversi satuan massa (mg ke g) dan perbandingan bilangan desimal. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 5 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu melakukan konversi satuan dasar dan membandingkan desimal. Tantangan utama adalah jebakan satuan (mg vs g) yang menguji ketelitian dalam membandingkan besaran. |

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
Transkripsi visual: Informasi Nilai Gizi: Protein 1,3 g, Lemak total 5,4 g, Karbohidrat 28,6 g, Serat Pangan 2,7 g, Natrium 88,6 mg.
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
Solusi minimum hasil AI: Rasio awal adalah 65:35 atau 13:7. Jika ditambahkan 20 gram ke masing-masing bagian, rasio baru menjadi (65+20):(35+20) = 85:55. Menyederhanakan 85:55 dengan membagi 5 menghasilkan 17:11. Karena 17:11 tidak sama dengan 13:7, maka kesimpulan siswa tersebut salah.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menyimpulkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2774cd703c3b5a2a8a289b7edfee482b194c05f456907651a6e090d4aeeb2137`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Medium | 2691 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 3430 |
| 3 | success | valid / verified | reasoning | conceptual | Medium | 2748 |

Run 1 — solusi: Rasio awal adalah 65:35 atau 13:7. Jika ditambahkan 20 gram ke masing-masing bagian, rasio baru menjadi (65+20):(35+20) = 85:55. Menyederhanakan 85:55 dengan membagi 5 menghasilkan 17:11. Karena 17:11 tidak sama dengan 13:7, maka kesimpulan siswa tersebut salah.
- Domain kognitif `classify/reasoning`: Soal menuntut siswa untuk mengevaluasi klaim matematis dengan memberikan kontra-contoh atau pembuktian logis, yang melampaui sekadar menerapkan prosedur rutin.. Bukti: Seorang siswa mengatakan bahwa penambahan berat yang sama untuk cokelat murni dan campuran susu dan gula selalu menghasilkan rasio yang sama; Apa pendapat kalian tentang kesimpulan siswa tersebut?
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami sifat dasar rasio (perbandingan perkalian) dan bagaimana operasi penjumlahan memengaruhi rasio tersebut, yang merupakan pemahaman konseptual.. Bukti: penambahan berat yang sama untuk cokelat murni dan campuran susu dan gula selalu menghasilkan rasio yang sama
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena menuntut siswa untuk menguji klaim dengan kontra-contoh. Meskipun prosedurnya sederhana (penjumlahan dan penyederhanaan pecahan), siswa harus memahami konsep rasio secara mendalam untuk menolak penalaran aditif yang keliru (seperti pada opsi B).. Bukti: penambahan berat yang sama untuk cokelat murni dan campuran susu dan gula selalu menghasilkan rasio yang sama; misalnya 65 gram dan 35 gram masing-masing ditambah 20 gram menjadi 85 : 55 = 17 : 11, tidak sama dengan 13 : 7

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio sebagai perbandingan perkalian dan penyederhanaan pecahan. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 7 sering terjebak pada penalaran aditif dalam masalah rasio. Soal ini menguji pemahaman konseptual tersebut dengan menuntut evaluasi terhadap klaim yang salah secara intuitif namun keliru secara matematis. |

Run 2 — solusi: Rasio awal cokelat terhadap campuran susu-gula adalah 65:35, yang disederhanakan menjadi 13:7. Jika ditambahkan 20 gram pada masing-masing, rasionya menjadi (65+20):(35+20) = 85:55. Setelah disederhanakan, 85:55 menjadi 17:11. Karena 17:11 tidak sama dengan 13:7, maka kesimpulan siswa tersebut salah.
- Domain kognitif `classify/reasoning`: Siswa diminta untuk mengevaluasi klaim tentang sifat rasio, yang mengharuskan pemahaman bahwa rasio bersifat multiplikatif, bukan aditif. Ini menuntut penalaran untuk menyanggah klaim tersebut.. Bukti: Seorang siswa mengatakan bahwa penambahan berat yang sama untuk cokelat murni dan campuran susu dan gula selalu menghasilkan rasio yang sama
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual mengenai perbedaan antara operasi aditif dan hubungan rasio (multiplikatif).. Bukti: penambahan berat yang sama untuk cokelat murni dan campuran susu dan gula selalu menghasilkan rasio yang sama
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena menuntut siswa untuk membedakan penalaran aditif dan multiplikatif dalam rasio. Meskipun ada bantuan berupa contoh penyanggah pada pilihan jawaban, siswa tetap harus memverifikasi kebenaran logika tersebut.. Bukti: Seorang siswa mengatakan bahwa penambahan berat yang sama untuk cokelat murni dan campuran susu dan gula selalu menghasilkan rasio yang sama; Tidak setuju; misalnya 65 gram dan 35 gram masing-masing ditambah 20 gram menjadi 85 : 55 = 17 : 11, tidak sama dengan 13 : 7

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep rasio dasar dan penyederhanaan pecahan/rasio. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sering terjebak pada penalaran aditif dalam rasio. Soal ini menguji pemahaman konseptual tersebut dengan meminta evaluasi klaim. |

Run 3 — solusi: Rasio awal adalah 65:35 atau 13:7. Jika masing-masing ditambah 20 gram, rasionya menjadi (65+20):(35+20) = 85:55. Menyederhanakan 85:55 dengan membagi 5 menghasilkan 17:11. Karena 17:11 tidak sama dengan 13:7, maka kesimpulan siswa tersebut salah.
- Domain kognitif `classify/reasoning`: Soal menuntut siswa untuk mengevaluasi klaim tentang sifat rasio (perkalian vs aditif) dengan memberikan contoh penyangkal (counterexample) atau melakukan perhitungan untuk memverifikasi kesetaraan rasio.. Bukti: Seorang siswa mengatakan bahwa penambahan berat yang sama untuk cokelat murni dan campuran susu dan gula selalu menghasilkan rasio yang sama; Apa pendapat kalian tentang kesimpulan siswa tersebut?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep rasio sebagai hubungan perkalian (multiplikatif) dan bukan hubungan penjumlahan (aditif), yang merupakan pemahaman konseptual mendasar dalam topik rasio.. Bukti: penambahan berat yang sama untuk cokelat murni dan campuran susu dan gula selalu menghasilkan rasio yang sama
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena menuntut siswa untuk menguji klaim konseptual yang sering disalahpahami (penalaran aditif vs multiplikatif). Meskipun perhitungannya sederhana, siswa harus mampu mengonstruksi argumen atau contoh penyangkal untuk memvalidasi atau menyanggah pernyataan, yang memerlukan pemahaman hubungan rasio yang lebih dalam daripada sekadar menghitung rasio.. Bukti: penambahan berat yang sama untuk cokelat murni dan campuran susu dan gula selalu menghasilkan rasio yang sama; misalnya 65 gram dan 35 gram masing-masing ditambah 20 gram menjadi 85 : 55 = 17 : 11, tidak sama dengan 13 : 7

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio, penyederhanaan pecahan, dan operasi penjumlahan bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sering terjebak pada penalaran aditif dalam masalah rasio. Soal ini menguji pemahaman konseptual tersebut dengan meminta evaluasi terhadap klaim yang salah, yang merupakan tantangan kognitif yang sesuai untuk tingkat menengah. |

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
Solusi minimum hasil AI: Soal meminta rasio penebangan terhadap penanaman. Diketahui 1 pohon ditebang diimbangi dengan 3 pohon ditanam. Maka rasio penebangan : penanaman = 1 : 3.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a32fd298e2aa3779fef844c6ab8be633652ce007925914719531bd5325e56079`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2324 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3059 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2330 |

Run 1 — solusi: Soal meminta rasio penebangan terhadap penanaman. Diketahui 1 pohon ditebang diimbangi dengan 3 pohon ditanam. Maka rasio penebangan : penanaman = 1 : 3.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengidentifikasi nilai dari dua besaran yang diberikan dalam teks dan menyusunnya menjadi rasio sesuai urutan yang diminta (penebangan terhadap penanaman). Ini adalah pengenalan langsung terhadap konsep rasio.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali; Berapa rasio dari penebangan pohon terhadap penanaman kembali pohon
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep dasar rasio sebagai perbandingan dua besaran.. Bukti: Berapa rasio dari penebangan pohon terhadap penanaman kembali pohon
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu membaca informasi dan menerjemahkannya ke dalam notasi rasio tanpa perlu melakukan perhitungan kompleks atau langkah perantara.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali; Berapa rasio dari penebangan pohon terhadap penanaman kembali pohon

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep rasio dan perbandingan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan langsung konsep rasio yang sangat mendasar dan sesuai untuk kelas 7. |

Run 2 — solusi: Berdasarkan teks, 1 pohon ditebang diimbangi dengan 3 pohon ditanam. Maka rasio penebangan terhadap penanaman adalah 1:3.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengidentifikasi nilai dari teks soal dan menyusunnya menjadi rasio sesuai urutan yang diminta. Tidak ada proses kompleks atau penalaran nonrutin.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali yang ditebang; Berapa rasio dari penebangan pohon terhadap penanaman kembali pohon
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang bagaimana rasio merepresentasikan hubungan antara dua kuantitas yang diberikan.. Bukti: Berapa rasio dari penebangan pohon terhadap penanaman kembali pohon
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu memetakan angka dari teks ke dalam format rasio. Tidak ada langkah perantara atau kendala yang perlu diintegrasikan.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali yang ditebang; Berapa rasio dari penebangan pohon terhadap penanaman kembali pohon

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep rasio sebagai perbandingan dua nilai. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan langsung konsep rasio yang sangat mendasar dan sesuai untuk kelas 7. |

Run 3 — solusi: Soal meminta rasio penebangan pohon terhadap penanaman kembali. Diketahui 1 pohon ditebang diimbangi dengan 3 pohon ditanam. Maka rasionya adalah 1 : 3.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengidentifikasi nilai dari dua besaran yang diberikan dalam teks dan menyusunnya menjadi rasio sesuai urutan yang diminta. Ini adalah proses pengenalan fakta dan prosedur dasar.. Bukti: Berapa rasio dari penebangan pohon terhadap penanaman kembali pohon.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang konsep rasio sebagai perbandingan dua besaran yang sudah didefinisikan secara eksplisit.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali yang ditebang
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu memetakan angka 1 (penebangan) dan 3 (penanaman) ke dalam bentuk rasio. Tidak ada langkah perantara atau integrasi yang kompleks.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali yang ditebang; Berapa rasio dari penebangan pohon terhadap penanaman kembali pohon.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep rasio dan perbandingan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan langsung dari definisi rasio yang sangat mendasar untuk kelas 7, tanpa memerlukan manipulasi atau penalaran lebih lanjut. |

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

Kunci sumber: `A`; status AI: `conflict`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: Berdasarkan interpretasi literal 'membuat 2 jenis kue untuk 15 orang' (total porsi 15): Memilih Bolu Kukus (10 porsi) dan Kue Pisang (5 porsi) membutuhkan 6+2=8 telur, 500+250=750g terigu, dan 500+200=700g gula. Sisa bahan: 15-8=7 telur, 2500-750=1750g terigu, 1800-700=1100g gula. Kunci jawaban A salah karena menggunakan asumsi penskalaan yang tidak konsisten dengan teks soal.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['mengidentifikasi', 'menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d4ba68f3bbd7517495b2fbfc2ba50166dc0fb96c5cc81767f005820629e0a56f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2971 |
| 2 | success | valid / verified | applying | procedural | Medium | 2966 |
| 3 | success | valid / verified | applying | procedural | Medium | 3012 |

Run 1 — solusi: Ibu ingin membuat kue untuk 15 orang. Opsi A (Bolu Kukus + Kue Pisang): Bolu Kukus (10 orang) butuh 6 telur, 500g terigu, 500g gula. Kue Pisang (5 orang) butuh 2 telur, 250g terigu, 200g gula. Total kebutuhan: 8 telur, 750g terigu, 700g gula. Stok: 15 telur, 2500g terigu, 1800g gula. Sisa: 7 telur, 1750g terigu, 1100g gula. Catatan: Terdapat ketidaksesuaian antara perhitungan logis dengan pilihan jawaban A yang tertulis di soal (sisa 450g gula dan 1000g terigu). Namun, berdasarkan analisis kebutuhan bahan, pasangan Bolu Kukus dan Kue Pisang adalah yang paling mungkin secara stok dibandingkan opsi lain yang melanggar batas stok atau salah hitung.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rasio/skala untuk menyesuaikan resep dengan jumlah orang (15 orang), lalu melakukan operasi aritmetika dasar untuk menghitung total kebutuhan bahan dan sisa stok. Ini adalah penerapan prosedur pada konteks rutin.. Bukti: Ibu ingin membuat 2 jenis kue untuk 15 orang; Tentukan jenis kue yang dipilih oleh ibu dan hitunglah berapa sisa bahan kue
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman tentang hubungan proporsional (skala resep) dan penggunaan algoritme aritmetika untuk menyelesaikan masalah.. Bukti: Tabel 3.10 Resep Kue; Ibu mempunyai stok 1800 gram gula, 15 butir telur, dan 2500 gram terigu
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan beberapa langkah yang saling terkait: menyesuaikan resep (skala), menjumlahkan kebutuhan bahan dari dua resep berbeda, membandingkan dengan stok, dan menghitung sisa. Meskipun prosedurnya rutin, terdapat beberapa kendala (stok bahan) yang harus diperiksa secara simultan.. Bukti: Ibu ingin membuat 2 jenis kue untuk 15 orang; Tentukan jenis kue yang dipilih oleh ibu dan hitunglah berapa sisa bahan kue

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmetika dasar, konsep rasio/skala sederhana. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 8 |
| interactingConstraints | 3 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu melakukan penyesuaian rasio sederhana dan operasi hitung dasar. Kompleksitas terletak pada manajemen beberapa variabel bahan secara bersamaan. |

Run 2 — solusi: Ibu ingin membuat kue untuk 15 orang. Opsi A (Bolu Kukus untuk 10 orang + Kue Pisang untuk 5 orang) membutuhkan: Telur (6+2=8 telur, namun tabel menunjukkan Bolu Kukus 10 orang butuh 6 telur, maka untuk 15 orang Bolu Kukus butuh 9 telur + Kue Pisang 6 telur = 15 telur). Terigu (Bolu Kukus 15 orang: 750g + Kue Pisang 15 orang: 750g = 1500g). Gula (Bolu Kukus 15 orang: 750g + Kue Pisang 15 orang: 600g = 1350g). Sisa: Telur (15-15=0), Terigu (2500-1500=1000g), Gula (1800-1350=450g).
- Domain kognitif `classify/applying`: Siswa harus menerapkan konsep rasio untuk menskalakan resep ke jumlah porsi yang diinginkan (15 orang), kemudian mengintegrasikan beberapa kendala (stok bahan) untuk menentukan kombinasi yang mungkin.. Bukti: Ibu ingin membuat 2 jenis kue untuk 15 orang; Tentukan jenis kue yang dipilih oleh ibu dan hitunglah berapa sisa bahan kue
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur aritmetika dasar (perkalian rasio dan pengurangan) dalam konteks pemecahan masalah yang terstruktur.. Bukti: Tabel 3.10 Resep Kue; Ibu mempunyai stok 1800 gram gula, 15 butir telur, dan 2500 gram terigu
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena menuntut siswa melakukan penskalaan resep (konsep rasio) untuk beberapa bahan secara simultan dan memeriksa kendala stok bahan yang terbatas. Siswa perlu merencanakan langkah-langkah (menghitung kebutuhan bahan per kue untuk 15 orang, menjumlahkan, lalu membandingkan dengan stok) yang saling bergantung.. Bukti: Ibu ingin membuat 2 jenis kue untuk 15 orang; Tentukan jenis kue yang dipilih oleh ibu dan hitunglah berapa sisa bahan kue

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep rasio dan proporsi sederhana, operasi aritmetika dasar. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 8 |
| interactingConstraints | 3 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu melakukan penskalaan sederhana dan mengelola beberapa variabel (telur, terigu, gula) secara bersamaan dalam konteks kehidupan sehari-hari. |

Run 3 — solusi: Bolu kukus (10 orang) perlu 6 telur, 500g terigu, 500g gula. Kue pisang (5 orang) perlu 2 telur, 250g terigu, 200g gula. Total untuk 15 orang: 8 telur, 750g terigu, 700g gula. Sisa: 1800-700=1100g gula, 15-8=7 telur, 2500-750=1750g terigu. Koreksi: Soal meminta 15 orang, namun tabel resep untuk 10 dan 5 orang. Jika memilih Bolu Kukus (10 org) + Kue Pisang (5 org), total bahan: (6+2) telur = 8 telur, (500+250) terigu = 750g, (500+200) gula = 700g. Sisa: 1800-700=1100g gula, 2500-750=1750g terigu. Kunci A salah hitung sisa, namun secara logika pemilihan kue A adalah yang paling mungkin memenuhi stok.
- Domain kognitif `classify/applying`: Siswa perlu memilih kombinasi kue yang sesuai dengan stok bahan yang tersedia dan jumlah porsi yang diminta (15 orang), yang melibatkan penerapan konsep rasio/skala sederhana dalam konteks kehidupan sehari-hari.. Bukti: Ibu ingin membuat 2 jenis kue untuk 15 orang; Tentukan jenis kue yang dipilih oleh ibu dan hitunglah berapa sisa bahan kue
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prinsip proporsi/skala untuk menyesuaikan resep dengan jumlah porsi yang diinginkan, yang merupakan pemahaman prosedural dalam mengelola data.. Bukti: Tabel 3.10 Resep Kue; Ibu mempunyai stok 1800 gram gula, 15 butir telur, dan 2500 gram terigu
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan beberapa langkah: memilih kombinasi kue yang tepat agar tidak melebihi stok bahan (kendala), melakukan penjumlahan bahan dari dua resep yang berbeda, dan menghitung sisa bahan. Meskipun prosedurnya familiar, terdapat beberapa langkah yang saling bergantung dan kendala stok yang harus diperiksa.. Bukti: Ibu ingin membuat 2 jenis kue untuk 15 orang; Tentukan jenis kue yang dipilih oleh ibu dan hitunglah berapa sisa bahan kue

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmetika dasar dan pemahaman rasio/skala sederhana. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 3 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu mengelola data dari tabel dan melakukan operasi hitung untuk memecahkan masalah kontekstual terkait rasio/skala. |

Histori retry: run 2 sebelumnya `failed` / `ValidationError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 2 sebelumnya `failed` / `ValidationError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `5501`.
Konten: `concern`; kunci: `conflict`; masalah: Terdapat ketidaksesuaian matematis yang signifikan antara data resep pada tabel dengan kunci jawaban A. Jika Ibu membuat Bolu Kukus (10 orang) dan Kue Pisang (5 orang), total kebutuhan bahan adalah 8 telur, 750g terigu, dan 700g gula. Sisa bahan seharusnya adalah 7 telur, 1750g terigu, dan 1100g gula. Kunci jawaban A mengklaim sisa 450g gula dan 1000g terigu, yang mengasumsikan resep telah diskalakan ke 15 orang untuk setiap jenis kue (misalnya, Bolu Kukus untuk 15 orang = 9 telur, 750g terigu, 750g gula), namun soal menyatakan 'Ibu ingin membuat 2 jenis kue untuk 15 orang' dengan total 15 orang, bukan 15 orang per jenis kue.; Soal ambigu dalam frasa 'Ibu ingin membuat 2 jenis kue untuk 15 orang'. Apakah ini berarti total porsi dari kedua kue tersebut harus 15 (misal 10+5), atau masing-masing kue harus untuk 15 orang? Interpretasi kunci jawaban A mengasumsikan masing-masing kue dibuat untuk 15 orang, yang bertentangan dengan logika 'membuat 2 jenis kue untuk 15 orang' secara kolektif..
- Domain kognitif `applying`: Siswa diminta untuk menerapkan konsep rasio/skala dan operasi aritmetika dasar untuk menyelesaikan masalah kontekstual. Meskipun ada ambiguitas konten, proses kognitif yang diminta adalah menerapkan prosedur pada konteks.
- Dimensi pengetahuan `procedural`: Siswa perlu memahami hubungan proporsional dalam resep dan menggunakan prosedur aritmetika untuk menghitung kebutuhan bahan.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena menuntut siswa mengintegrasikan beberapa variabel (telur, terigu, gula) dan melakukan penskalaan resep. Meskipun prosedurnya rutin, terdapat beberapa langkah yang saling bergantung (memilih kombinasi, menghitung total, menghitung sisa) yang memerlukan ketelitian.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmetika dasar, konsep rasio/skala sederhana. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 3 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu mengelola data dari tabel dan melakukan operasi hitung untuk memecahkan masalah kontekstual terkait rasio/skala. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `revision_required`.
Status konten: `concern`. Catatan konten: Terdapat ketidaksesuaian matematis yang signifikan antara data resep pada tabel dengan kunci jawaban A. Jika Ibu membuat Bolu Kukus (10 orang) dan Kue Pisang (5 orang), total kebutuhan bahan adalah 8 telur, 750g terigu, dan 700g gula. Sisa bahan seharusnya adalah 7 telur, 1750g terigu, dan 1100g gula. Kunci jawaban A mengklaim sisa 450g gula dan 1000g terigu, yang mengasumsikan resep telah diskalakan ke 15 orang untuk setiap jenis kue (misalnya, Bolu Kukus untuk 15 orang = 9 telur, 750g terigu, 750g gula), namun soal menyatakan 'Ibu ingin membuat 2 jenis kue untuk 15 orang' dengan total 15 orang, bukan 15 orang per jenis kue.; Soal ambigu dalam frasa 'Ibu ingin membuat 2 jenis kue untuk 15 orang'. Apakah ini berarti total porsi dari kedua kue tersebut harus 15 (misal 10+5), atau masing-masing kue harus untuk 15 orang? Interpretasi kunci jawaban A mengasumsikan masing-masing kue dibuat untuk 15 orang, yang bertentangan dengan logika 'membuat 2 jenis kue untuk 15 orang' secara kolektif..
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
Solusi minimum hasil AI: Rasio penebangan terhadap penanaman adalah 1:3. Jika 191 pohon ditebang, maka jumlah pohon yang harus ditanam adalah 191 x 3 = 573 pohon.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e8fef1329ab7fbdd8b64c314f4905ee020c983daba0c47f3c5cef2917c7e1ed0`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2438 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2436 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2467 |

Run 1 — solusi: Rasio penebangan terhadap penanaman adalah 1:3. Jika 191 pohon ditebang, maka jumlah pohon yang harus ditanam adalah 191 x 3 = 573 pohon.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi rasio dari informasi yang diberikan dan menerapkan rasio tersebut (1:3) untuk menghitung nilai baru berdasarkan jumlah yang diketahui. Ini adalah penerapan langsung dari konsep rasio.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali; Berapakah rasio dari penebangan pohon terhadap penanaman kembali pohon; Sebanyak 191 pohon ditebang... Berapa banyak pohon yang perlu ditanam?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang rasio sebagai hubungan perbandingan antara dua kuantitas.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena jalur penyelesaiannya sangat jelas (perkalian sederhana berdasarkan rasio yang diberikan secara eksplisit). Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali; Sebanyak 191 pohon ditebang

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
| gradeRelativeRationale | Soal ini merupakan penerapan langsung rasio yang sesuai dengan kurikulum kelas 7, dengan beban kognitif yang rendah karena hubungan antar variabel diberikan secara eksplisit. |

Run 2 — solusi: Rasio penebangan terhadap penanaman adalah 1:3. Jika 191 pohon ditebang, maka pohon yang harus ditanam adalah 191 x 3 = 573 pohon.
- Domain kognitif `classify/applying`: Soal meminta siswa mengidentifikasi rasio dari informasi yang diberikan dan menerapkan rasio tersebut (1:3) untuk menghitung nilai baru berdasarkan jumlah yang diketahui. Ini adalah penerapan langsung konsep rasio.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali; Berapakah rasio dari penebangan pohon terhadap penanaman kembali pohon; Sebanyak 191 pohon ditebang... Berapa banyak pohon yang perlu ditanam?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep rasio sebagai hubungan perbandingan antara dua kuantitas (pohon ditebang dan pohon ditanam) untuk menyelesaikan masalah.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena jalur penyelesaiannya sangat jelas (perkalian sederhana berdasarkan rasio yang diberikan secara eksplisit). Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali; Sebanyak 191 pohon ditebang

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
| gradeRelativeRationale | Soal ini merupakan penerapan langsung konsep rasio yang merupakan materi dasar kelas 7. Tidak ada kompleksitas tambahan dalam langkah penyelesaian. |

Run 3 — solusi: Rasio penebangan terhadap penanaman adalah 1:3. Jika 191 pohon ditebang, maka pohon yang harus ditanam adalah 191 x 3 = 573 pohon.
- Domain kognitif `classify/applying`: Soal meminta siswa mengidentifikasi rasio dari narasi dan menerapkan rasio tersebut (1:3) untuk menghitung nilai baru berdasarkan jumlah yang diberikan. Ini adalah penerapan langsung konsep rasio.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali; Berapakah rasio dari penebangan pohon terhadap penanaman kembali pohon; Sebanyak 191 pohon ditebang... Berapa banyak pohon yang perlu ditanam?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep rasio sebagai hubungan perbandingan antara dua kuantitas (pohon ditebang dan pohon ditanam) untuk menyelesaikan masalah.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali; rasio dari penebangan pohon terhadap penanaman kembali pohon
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu memahami rasio 1:3 dan melakukan satu operasi perkalian sederhana. Tidak ada kendala yang berinteraksi atau perencanaan langkah yang kompleks.. Bukti: setiap penebangan satu pohon harus diimbangi dengan penanaman pohon sebanyak tiga kali; Sebanyak 191 pohon ditebang; Berapa banyak pohon yang perlu ditanam?

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
| gradeRelativeRationale | Soal ini sangat mendasar untuk kelas 7, hanya memerlukan pemahaman rasio sederhana dan satu langkah operasi hitung tanpa jebakan atau kompleksitas tambahan. |

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
Solusi minimum hasil AI: Samakan satuan menjadi rasio sirup per 1 liter air: (1) 2/3 liter sirup/liter air. (2) Rasio air:sirup = 2:3, maka sirup/air = 3/2 = 1,5 liter sirup/liter air. (3) Air = 2/3 bagian campuran, maka sirup = 1/3 bagian campuran. Rasio sirup/air = (1/3) / (2/3) = 1/2 = 0,5 liter sirup/liter air. Membandingkan 2/3 (0,67), 3/2 (1,5), dan 1/2 (0,5), yang paling manis adalah campuran kedua.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fdc1457794da6ac56b8af7e3ce7677ad9db1c019f1b5500a00ef9260c5ad0d9c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2701 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2671 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2719 |

Run 1 — solusi: Samakan satuan menjadi rasio sirup per 1 liter air: (1) 2/3 liter sirup/liter air. (2) Rasio air:sirup = 2:3, maka sirup/air = 3/2 = 1,5 liter sirup/liter air. (3) Air = 2/3 bagian campuran, maka sirup = 1/3 bagian campuran. Rasio sirup/air = (1/3) / (2/3) = 1/2 = 0,5 liter sirup/liter air. Membandingkan 2/3 (0,67), 3/2 (1,5), dan 1/2 (0,5), yang paling manis adalah campuran kedua.
- Domain kognitif `classify/applying`: Siswa perlu mengonversi berbagai bentuk representasi rasio (pecahan, perbandingan, bagian dari keseluruhan) ke dalam satu satuan standar (sirup per 1 liter air) untuk membandingkan konsentrasi sirup. Ini melibatkan penerapan konsep rasio pada konteks yang berbeda-beda.. Bukti: Perhatikan tiga komposisi sirup merah.; Campuran mana yang paling manis?
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman konseptual tentang rasio dan bagaimana mengubah berbagai bentuk perbandingan menjadi satuan yang dapat dibandingkan (laju satuan).. Bukti: Perhatikan tiga komposisi sirup merah.; Campuran mana yang paling manis?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan konversi representasi yang berbeda (pecahan, rasio, bagian dari keseluruhan) ke bentuk yang seragam (laju satuan) sebelum dapat membandingkan. Meskipun prosedurnya familiar, siswa perlu berhati-hati dalam menginterpretasikan setiap pernyataan agar tidak salah membandingkan (misalnya, membandingkan air terhadap sirup atau sebaliknya).. Bukti: Untuk satu liter air campurkan 2/3 liter sirup merah; Campurkan air dan sirup merah dengan perbandingan 2 : 3; 2/3 dari campuran sirup merah adalah air

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman rasio, pecahan, dan laju satuan. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 7 sudah mempelajari rasio dan laju satuan. Tantangan utama adalah mengonversi ketiga pernyataan ke basis yang sama (sirup per 1 liter air) untuk membandingkan nilai secara akurat. |

Run 2 — solusi: Samakan satuan menjadi rasio sirup per 1 liter air: (1) 2/3 liter sirup per 1 liter air = 0,67 liter sirup. (2) Rasio air:sirup 2:3 berarti 3/2 liter sirup per 1 liter air = 1,5 liter sirup. (3) 2/3 bagian campuran adalah air, berarti 1/3 bagian adalah sirup. Rasio air:sirup 2:1, berarti 1/2 liter sirup per 1 liter air = 0,5 liter sirup. Campuran kedua memiliki konsentrasi sirup tertinggi (1,5 liter per liter air).
- Domain kognitif `classify/applying`: Siswa harus mengonversi tiga representasi rasio yang berbeda ke dalam bentuk standar (sirup per 1 liter air) untuk membandingkan konsentrasi. Ini memerlukan penerapan konsep rasio dan laju satuan pada konteks yang bervariasi.. Bukti: Campuran mana yang paling manis?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang rasio dan proporsi, serta bagaimana merepresentasikan hubungan bagian-ke-bagian dan bagian-ke-keseluruhan dalam bentuk laju satuan.. Bukti: Perhatikan tiga komposisi sirup merah.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan konversi representasi (dari rasio bagian-ke-bagian, bagian-ke-keseluruhan, dan laju satuan) ke bentuk yang seragam sebelum membandingkan. Meskipun prosedurnya familiar, siswa perlu merencanakan langkah konversi untuk setiap kasus secara mandiri.. Bukti: Perhatikan tiga komposisi sirup merah.; Untuk satu liter air campurkan 2/3 liter sirup merah; Campurkan air dan sirup merah dengan perbandingan 2 : 3; 2/3 dari campuran sirup merah adalah air

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman rasio, pecahan, dan laju satuan. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu membandingkan rasio, namun menuntut konversi tiga format berbeda ke basis yang sama (1 liter air) meningkatkan kompleksitas kognitif dibandingkan soal rasio satu langkah. |

Run 3 — solusi: Samakan satuan menjadi rasio sirup per 1 liter air: (1) 2/3 liter sirup per 1 liter air = 0,67 liter sirup. (2) Rasio air:sirup = 2:3, maka 1 liter air: 1,5 liter sirup. (3) Air 2/3 dari campuran, maka sirup 1/3 dari campuran. Jika air 2/3 liter, sirup 1/3 liter. Per 1 liter air, sirup = (1/3) / (2/3) = 0,5 liter. Campuran kedua memiliki sirup terbanyak per liter air (1,5 liter), sehingga paling manis.
- Domain kognitif `classify/applying`: Siswa harus mengonversi ketiga bentuk representasi (pecahan, rasio, bagian dari keseluruhan) ke dalam satu satuan standar (sirup per liter air) untuk membandingkan nilai. Ini memerlukan pemilihan prosedur yang tepat dan integrasi konsep rasio.. Bukti: Campuran mana yang paling manis?; Untuk satu liter air campurkan 2/3 liter sirup merah; Campurkan air dan sirup merah dengan perbandingan 2 : 3; 2/3 dari campuran sirup merah adalah air
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman konseptual tentang hubungan antara rasio, pecahan, dan laju satuan, serta bagaimana mengonversi antar representasi tersebut.. Bukti: Untuk satu liter air campurkan 2/3 liter sirup merah; Campurkan air dan sirup merah dengan perbandingan 2 : 3; 2/3 dari campuran sirup merah adalah air
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan konversi representasi yang berbeda-beda (pecahan, rasio, bagian dari total) ke dalam satu standar yang sama (laju satuan). Meskipun prosedurnya familiar, siswa perlu merencanakan langkah konversi untuk setiap opsi sebelum membandingkan, yang melibatkan beberapa langkah saling terkait.. Bukti: Perhatikan tiga komposisi sirup merah.; Campuran mana yang paling manis?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman rasio, pecahan, dan laju satuan (unit rate). |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu membandingkan rasio dan pecahan. Tantangan utama adalah menstandarisasi ketiga bentuk informasi yang berbeda ke dalam satu basis (sirup per liter air) untuk menentukan yang paling manis. |

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
Solusi minimum hasil AI: Menghitung laju tempuh (km/liter) untuk setiap mobil: A = 138/10 = 13,8 km/L; B = 165/15 = 11 km/L; C = 185/20 = 9,25 km/L; D = 330/25 = 13,2 km/L. Efisiensi tertinggi adalah nilai km/L terbesar, yaitu Mobil A (13,8 km/L).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7b99ac6dee7ec0d31d8827fbfc01d970d17587edbb36bf42a7c206937b4085e2`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2599 |
| 2 | success | valid / verified | applying | procedural | Medium | 2646 |
| 3 | success | valid / verified | applying | procedural | Medium | 2594 |

Run 1 — solusi: Menghitung laju tempuh (km/liter) untuk setiap mobil: A = 138/10 = 13,8 km/L; B = 165/15 = 11 km/L; C = 185/20 = 9,25 km/L; D = 330/25 = 13,2 km/L. Efisiensi tertinggi adalah nilai km/L terbesar, yaitu Mobil A (13,8 km/L).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep laju satuan (km per liter) untuk membandingkan efisiensi keempat mobil. Ini adalah penerapan prosedur yang dipelajari pada konteks rutin.. Bukti: Mobil mana yang menggunakan bahan bakar paling efisien?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan metode perhitungan laju satuan (pembagian jarak dengan bahan bakar) untuk memecahkan masalah perbandingan.. Bukti: Tabel 3.14 Jarak Tempuh dan Bahan Bakar
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah perhitungan (4 pembagian) dan perbandingan hasil untuk menentukan jawaban. Meskipun prosedurnya familiar, siswa harus melakukan serangkaian langkah yang saling terkait dan teliti dalam membandingkan nilai desimal untuk menghindari jebakan (distraktor).. Bukti: Tabel 3.14 Jarak Tempuh dan Bahan Bakar; Mobil mana yang menggunakan bahan bakar paling efisien?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pembagian bilangan bulat dan desimal, pemahaman konsep laju satuan. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 8 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu menghitung laju satuan. Beban kognitif berasal dari keharusan menghitung empat nilai berbeda dan membandingkannya, yang merupakan tugas rutin namun menuntut ketelitian. |

Run 2 — solusi: Hitung efisiensi (km/liter) untuk setiap mobil: Mobil A = 138/10 = 13,8 km/L; Mobil B = 165/15 = 11 km/L; Mobil C = 185/20 = 9,25 km/L; Mobil D = 330/25 = 13,2 km/L. Nilai tertinggi (paling efisien) adalah 13,8 km/L (Mobil A).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep laju satuan (km per liter) untuk membandingkan efisiensi bahan bakar dari data yang diberikan dalam tabel. Ini adalah penerapan prosedur rutin pada konteks yang diberikan.. Bukti: Mobil mana yang menggunakan bahan bakar paling efisien?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung dan membandingkan laju satuan (rasio) untuk menentukan nilai yang paling efisien.. Bukti: Tabel 3.14 Jarak Tempuh dan Bahan Bakar
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan beberapa langkah perhitungan (pembagian) untuk setiap opsi sebelum membandingkan hasilnya. Meskipun prosedurnya familiar, terdapat beberapa langkah yang saling terkait dan siswa harus memahami bahwa efisiensi bahan bakar diukur dari jarak per satuan bahan bakar, bukan sekadar melihat angka jarak atau bahan bakar secara terpisah.. Bukti: Mobil mana yang menggunakan bahan bakar paling efisien?; 138 : 10 = 13,8; B 165 : 15 = 11; C 185 : 20 = 9,25; D 330 : 25 = 13,2

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio, pembagian bilangan, dan konsep laju satuan. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 8 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu menghitung laju satuan. Soal ini memerlukan ketelitian dalam melakukan empat operasi pembagian dan membandingkan hasilnya, yang merupakan tuntutan standar untuk tingkat menengah. |

Run 3 — solusi: Hitung efisiensi setiap mobil (km/liter): Mobil A = 138/10 = 13,8 km/L; Mobil B = 165/15 = 11 km/L; Mobil C = 185/20 = 9,25 km/L; Mobil D = 330/25 = 13,2 km/L. Mobil paling efisien adalah yang memiliki jarak tempuh per liter tertinggi, yaitu Mobil A (13,8 km/L).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep laju satuan (km per liter) untuk membandingkan efisiensi empat objek yang berbeda. Ini adalah penerapan prosedur standar pada konteks rutin.. Bukti: Mobil mana yang menggunakan bahan bakar paling efisien?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung dan membandingkan laju satuan (rasio) dari data yang disajikan dalam tabel.. Bukti: Tabel penggunaan bahan bakar dan jarak tempuh
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan perhitungan pembagian untuk empat data yang berbeda dan membandingkan hasilnya untuk menentukan nilai maksimum. Meskipun prosedurnya familiar, terdapat beberapa langkah yang saling terkait (menghitung 4 rasio lalu membandingkan) yang menuntut ketelitian, namun jalurnya sangat jelas dan rutin.. Bukti: Tabel penggunaan bahan bakar dan jarak tempuh oleh empat jenis mobil; Mobil mana yang menggunakan bahan bakar paling efisien?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang rasio, pembagian bilangan, dan perbandingan nilai desimal. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 8 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu menghitung dan membandingkan rasio. Beban kognitif berasal dari keharusan melakukan empat perhitungan terpisah sebelum membuat keputusan, yang merupakan tugas rutin namun memerlukan ketelitian. |

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
Solusi minimum hasil AI: Samakan satuan ke bulan: Buah merah = 3 tahun = 36 bulan. Kencur = 6 bulan. Lengkuas = 1,5 tahun = 18 bulan. Frekuensi kencur = 36 / 6 = 6 kali. Frekuensi lengkuas = 36 / 18 = 2 kali.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `95b9072a5d995321f8356d23987857cc9a83805e7ad9f138d1f4f4130ffd3a65`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2579 |
| 2 | success | valid / verified | applying | procedural | Medium | 2596 |
| 3 | success | valid / verified | applying | procedural | Medium | 2577 |

Run 1 — solusi: Samakan satuan waktu ke bulan: Buah merah = 3 tahun = 36 bulan. Kencur = 6 bulan. Lengkuas = 1,5 tahun = 18 bulan. Frekuensi panen kencur = 36 / 6 = 6 kali. Frekuensi panen lengkuas = 36 / 18 = 2 kali.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur konversi satuan waktu yang tepat dan menerapkan operasi pembagian untuk menentukan rasio frekuensi panen dalam konteks rutin.. Bukti: Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman konseptual tentang hubungan antar satuan waktu (tahun ke bulan) dan prosedur pembagian untuk membandingkan frekuensi.. Bukti: Masa Panen; 1,5 tahun; 3 tahun
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena menuntut siswa melakukan konversi satuan waktu (tahun ke bulan) sebelum melakukan operasi pembagian. Meskipun prosedurnya familiar, terdapat beberapa langkah yang saling terkait (konversi, lalu pembagian) dan perlunya ketelitian dalam menyamakan satuan sebelum membandingkan.. Bukti: Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konversi satuan waktu (tahun ke bulan) dan operasi pembagian dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu mengonversi satuan waktu dan memahami konsep perbandingan/rasio sederhana. Soal ini menguji ketelitian dalam menyamakan satuan sebelum menghitung rasio frekuensi. |

Run 2 — solusi: Samakan satuan masa panen ke bulan: Buah merah = 3 tahun = 36 bulan. Kencur = 6 bulan. Lengkuas = 1,5 tahun = 18 bulan. Frekuensi panen kencur dalam satu masa panen buah merah = 36 / 6 = 6 kali. Frekuensi panen lengkuas dalam satu masa panen buah merah = 36 / 18 = 2 kali.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rasio dan konversi satuan waktu untuk membandingkan masa panen tanaman yang berbeda dalam satu kerangka waktu yang sama (masa panen buah merah).. Bukti: Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut pemahaman prosedural tentang konversi satuan waktu (tahun ke bulan) dan penerapan konsep rasio/pembagian untuk menentukan frekuensi kejadian.. Bukti: Tabel 2.7 Masa Panen Tanaman Obat Khas Daerah
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena menuntut siswa melakukan konversi satuan waktu yang berbeda (tahun ke bulan) sebelum melakukan operasi pembagian untuk menentukan rasio frekuensi. Terdapat beberapa langkah yang saling terkait (konversi, lalu pembagian) yang harus dilakukan secara sistematis.. Bukti: Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konversi satuan waktu (tahun ke bulan) dan konsep dasar pembagian/rasio. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu mengonversi satuan waktu dan memahami perbandingan sederhana. Soal ini memerlukan ketelitian dalam menyamakan satuan sebelum membandingkan, yang merupakan standar kompetensi kelas 7. |

Run 3 — solusi: Samakan satuan waktu ke bulan: Buah merah = 3 tahun = 36 bulan. Kencur = 6 bulan. Lengkuas = 1,5 tahun = 18 bulan. Frekuensi panen kencur dalam 36 bulan = 36 / 6 = 6 kali. Frekuensi panen lengkuas dalam 36 bulan = 36 / 18 = 2 kali.
- Domain kognitif `classify/applying`: Siswa perlu memilih prosedur konversi satuan waktu yang tepat dan menerapkan operasi pembagian untuk menentukan frekuensi panen dalam durasi tertentu.. Bukti: Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman prosedural tentang konversi satuan waktu (tahun ke bulan) dan penerapan konsep rasio/perbandingan untuk memecahkan masalah.. Bukti: Tabel 2.7 Masa Panen Tanaman Obat Khas Daerah
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena menuntut siswa melakukan konversi satuan waktu (tahun ke bulan) sebelum melakukan operasi pembagian. Terdapat beberapa langkah yang saling terkait (konversi, lalu pembagian) dan siswa harus berhati-hati dengan satuan yang berbeda agar tidak terjebak pada kesalahan umum (seperti membagi langsung tanpa konversi).. Bukti: Berapa kali kencur dan lengkuas dapat dipanen dalam satu kali masa panen buah merah?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konversi satuan waktu (tahun ke bulan) dan operasi pembagian dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu melakukan konversi satuan waktu dasar dan memahami konsep perbandingan/frekuensi dalam konteks kehidupan sehari-hari. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4237`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur konversi satuan waktu yang tepat dan melakukan operasi pembagian untuk menentukan rasio frekuensi dalam konteks rutin.
- Dimensi pengetahuan `procedural`: Soal menuntut pemahaman prosedural tentang konversi satuan waktu (tahun ke bulan) dan penerapan konsep pembagian untuk membandingkan frekuensi.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena menuntut siswa melakukan konversi satuan waktu (tahun ke bulan) sebelum melakukan operasi pembagian. Terdapat beberapa langkah yang saling terkait (konversi, lalu pembagian) dan perlunya ketelitian dalam menyamakan satuan sebelum membandingkan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konversi satuan waktu (tahun ke bulan) dan operasi pembagian dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu mengonversi satuan waktu dan memahami konsep perbandingan/rasio sederhana. Soal ini menguji ketelitian dalam menyamakan satuan sebelum menghitung rasio frekuensi. |

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
Solusi minimum hasil AI: Substitusi nilai a = 20.000 dan b = 30.000 ke dalam bentuk aljabar 3a + 2b: 3(20.000) + 2(30.000) = 60.000 + 60.000 = 120.000.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fe69b68930f58295fabb4e37f85bac3ba169e1a7d1b60fa066856b1a0ffca3db`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2586 |
| 2 | success | valid / verified | applying | procedural | Easy | 3442 |
| 3 | success | valid / verified | applying | procedural | Easy | 2566 |

Run 1 — solusi: Substitusi nilai a = 20.000 dan b = 30.000 ke dalam bentuk aljabar 3a + 2b: 3(20.000) + 2(30.000) = 60.000 + 60.000 = 120.000.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan prosedur substitusi nilai ke dalam bentuk aljabar yang sudah diberikan. Ini adalah penerapan langsung dari konsep variabel dan operasi aljabar dasar.. Bukti: dapat dinyatakan dalam bentuk aljabar 3a + 2b; Jika harga satuan tiket anak-anak adalah Rp20.000,00 dan harga satuan tiket untuk orang dewasa adalah Rp30.000,00
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana variabel dalam bentuk aljabar merepresentasikan nilai dan bagaimana melakukan operasi hitung setelah substitusi.. Bukti: dapat dinyatakan dalam bentuk aljabar 3a + 2b
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu melakukan substitusi nilai ke dalam ekspresi yang sudah tersedia dan melakukan operasi aritmatika dasar. Tidak ada perencanaan strategi yang kompleks atau integrasi kendala yang sulit.. Bukti: 3a + 2b; harga satuan tiket anak-anak adalah Rp20.000,00; harga satuan tiket untuk orang dewasa adalah Rp30.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel, koefisien, dan operasi aritmatika (perkalian dan penjumlahan). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 7, substitusi nilai ke dalam bentuk aljabar linear sederhana adalah materi dasar yang familiar dan tidak menuntut penalaran tingkat tinggi. |

Run 2 — solusi: 3(20.000) + 2(30.000) = 60.000 + 60.000 = 120.000
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur substitusi nilai ke dalam variabel pada bentuk aljabar yang sudah diberikan, kemudian melakukan operasi hitung aritmetika dasar.. Bukti: dapat dinyatakan dalam bentuk aljabar 3a + 2b; Jika harga satuan tiket anak-anak adalah Rp20.000,00 dan harga satuan tiket untuk orang dewasa adalah Rp30.000,00
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan metode substitusi nilai ke dalam variabel untuk menyelesaikan perhitungan, yang merupakan prosedur standar dalam aljabar.. Bukti: dapat dinyatakan dalam bentuk aljabar 3a + 2b; Jika harga satuan tiket anak-anak adalah Rp20.000,00
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung karena bentuk aljabar dan nilai variabel sudah diberikan secara eksplisit. Siswa hanya perlu melakukan substitusi dan operasi hitung dasar tanpa perlu melakukan pemodelan atau perumusan masalah.. Bukti: dapat dinyatakan dalam bentuk aljabar 3a + 2b; Jika harga satuan tiket anak-anak adalah Rp20.000,00 dan harga satuan tiket untuk orang dewasa adalah Rp30.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar substitusi variabel dan operasi hitung bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan latihan dasar substitusi aljabar yang umum untuk kelas 7, di mana siswa hanya perlu memasukkan nilai yang diketahui ke dalam rumus yang sudah tersedia tanpa perlu melakukan pemodelan matematika yang kompleks. |

Run 3 — solusi: Substitusi nilai a = 20.000 dan b = 30.000 ke dalam bentuk aljabar 3a + 2b: 3(20.000) + 2(30.000) = 60.000 + 60.000 = 120.000.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan prosedur substitusi nilai ke dalam bentuk aljabar yang sudah diberikan. Ini adalah penerapan langsung dari konsep variabel dan operasi aljabar dasar.. Bukti: dapat dinyatakan dalam bentuk aljabar 3a + 2b; Jika harga satuan tiket anak-anak adalah Rp20.000,00 dan harga satuan tiket untuk orang dewasa adalah Rp30.000,00
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana variabel dalam bentuk aljabar merepresentasikan nilai tertentu dan bagaimana melakukan operasi hitung setelah substitusi.. Bukti: dapat dinyatakan dalam bentuk aljabar 3a + 2b
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu melakukan substitusi nilai ke dalam ekspresi yang sudah tersedia dan melakukan operasi aritmatika dasar. Tidak ada perencanaan strategi yang kompleks atau kendala yang saling berinteraksi.. Bukti: 3a + 2b; a = 20.000; b = 30.000

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel, koefisien, dan operasi hitung bilangan bulat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 7, substitusi nilai ke dalam bentuk aljabar linear dua variabel adalah materi dasar yang rutin dan langsung. |

Histori retry: run 2 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

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
| 1 | success | valid / verified | knowing | factual | Easy | 2483 |
| 2 | success | valid / verified | knowing | factual | Easy | 2484 |
| 3 | success | valid / verified | knowing | factual | Easy | 2465 |

Run 1 — solusi: Bentuk aljabar 2x + 1 terdiri dari dua suku yang dipisahkan oleh tanda tambah, yaitu 2x dan 1. Pada suku 2x, angka 2 adalah koefisien dari variabel x. Angka 1 adalah konstanta karena tidak memiliki variabel.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengidentifikasi komponen dasar dari bentuk aljabar (suku, koefisien, konstanta). Ini adalah tugas pengenalan istilah dan struktur dasar aljabar yang bersifat langsung.. Bukti: Tentukan suku-suku, koefisien, variabel, dan konstanta yang ada pada masing-masing bentuk aljabar berikut ini. a. 2x + 1
- Dimensi pengetahuan `classify/factual`: Siswa perlu memahami definisi dan terminologi (fakta) mengenai unsur-unsur dalam bentuk aljabar.. Bukti: Tentukan suku-suku, koefisien, variabel, dan konstanta
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar bagi kelas 7. Siswa hanya perlu mengenali definisi suku, koefisien, dan konstanta pada ekspresi linear sederhana. Tidak ada langkah kompleks atau integrasi konsep yang diperlukan.. Bukti: a. 2x + 1

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
| gradeRelativeRationale | Ini adalah materi pengenalan aljabar kelas 7 yang bersifat prosedural langsung dan sangat familiar. |

Run 2 — solusi: Bentuk aljabar 2x + 1 terdiri dari dua suku yang dipisahkan oleh tanda tambah, yaitu 2x dan 1. Pada suku 2x, angka 2 adalah koefisien dari variabel x. Angka 1 adalah konstanta karena tidak memiliki variabel.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengidentifikasi komponen dasar dari bentuk aljabar (suku, koefisien, konstanta). Ini adalah tugas pengenalan istilah dan struktur dasar aljabar yang langsung, sehingga masuk dalam domain knowing.. Bukti: Tentukan suku-suku, koefisien, variabel, dan konstanta yang ada pada masing-masing bentuk aljabar berikut ini. a. 2x + 1
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman siswa terhadap definisi dan terminologi (fakta) dalam aljabar, yaitu apa yang dimaksud dengan suku, koefisien, dan konstanta.. Bukti: Tentukan suku-suku, koefisien, variabel, dan konstanta
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan merupakan pengenalan awal terhadap struktur aljabar di kelas 7. Siswa hanya perlu menerapkan definisi suku, koefisien, dan konstanta pada satu bentuk aljabar sederhana tanpa langkah-langkah kompleks.. Bukti: a. 2x + 1

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang operasi hitung dan pengenalan simbol aljabar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah materi pengenalan aljabar kelas 7 yang bersifat prosedural dasar. Tidak ada tuntutan integrasi atau penalaran yang kompleks. |

Run 3 — solusi: Bentuk aljabar 2x + 1 terdiri dari dua suku, yaitu 2x dan 1. Pada suku 2x, angka 2 adalah koefisien dari variabel x. Angka 1 adalah konstanta karena tidak memiliki variabel.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi komponen dasar dari bentuk aljabar (suku, koefisien, konstanta). Ini adalah pengenalan istilah dan struktur dasar aljabar yang bersifat prosedural langsung.. Bukti: Tentukan suku-suku, koefisien, variabel, dan konstanta yang ada pada masing-masing bentuk aljabar berikut ini. a. 2x + 1
- Dimensi pengetahuan `classify/factual`: Siswa perlu memahami definisi dan terminologi (fakta/istilah) dalam aljabar untuk mengklasifikasikan bagian-bagian dari ekspresi tersebut.. Bukti: Tentukan suku-suku, koefisien, variabel, dan konstanta
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan merupakan pengenalan awal aljabar. Tidak ada langkah kompleks atau integrasi konsep yang diperlukan, hanya pengenalan istilah.. Bukti: 2x + 1

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang operasi penjumlahan dan pengenalan simbol aljabar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah materi pengenalan aljabar kelas 7 yang sangat standar dan langsung. |

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "factual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: Menggunakan hukum distributif (FOIL): (x + 1)(x + 3) = x(x) + x(3) + 1(x) + 1(3) = x^2 + 3x + x + 3 = x^2 + 4x + 3.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `50d389b1a86bbdd26884b6b229f7d1ca9ef201ecca16f75b5fe8eb9780e0ffd4`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2396 |
| 2 | success | valid / verified | applying | procedural | Easy | 2384 |
| 3 | success | valid / verified | applying | procedural | Easy | 2397 |

Run 1 — solusi: Menggunakan hukum distributif (FOIL): (x + 1)(x + 3) = x(x) + x(3) + 1(x) + 1(3) = x^2 + 3x + x + 3 = x^2 + 4x + 3.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur distributif (perkalian suku dua) yang merupakan prosedur standar dalam aljabar kelas 7. Tidak ada strategi non-rutin yang diperlukan.. Bukti: Tentukan setiap bentuk aljabar berikut dalam bentuk jabaran.; (x + 1)(x + 3)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman dan penerapan algoritma perkalian bentuk aljabar (prosedural) yang didasarkan pada konsep distributif.. Bukti: (x + 1)(x + 3)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 7 yang sedang mempelajari aljabar. Langkah penyelesaiannya jelas (distributif), tidak melibatkan kendala yang berinteraksi, dan beban kalkulasinya rendah.. Bukti: (x + 1)(x + 3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel, suku aljabar, dan hukum distributif perkalian. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Perkalian binomial adalah materi inti kelas 7. Soal ini adalah latihan langsung tanpa variasi atau konteks yang kompleks. |

Run 2 — solusi: Gunakan sifat distributif: (x + 1)(x + 3) = x(x) + x(3) + 1(x) + 1(3) = x^2 + 3x + x + 3 = x^2 + 4x + 3.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan prosedur distributif (FOIL) untuk menjabarkan bentuk aljabar binomial. Ini adalah penerapan langsung dari prosedur yang dipelajari di kelas 7.. Bukti: Tentukan setiap bentuk aljabar berikut dalam bentuk jabaran.; (x + 1)(x + 3)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritme atau metode perkalian suku dua (distributif), yang merupakan pengetahuan prosedural.. Bukti: (x + 1)(x + 3)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menerapkan aturan distributif dasar tanpa kendala tambahan atau integrasi konsep yang kompleks. Jalur penyelesaian sangat jelas.. Bukti: (x + 1)(x + 3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel, penjumlahan suku sejenis, dan sifat distributif perkalian. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjabaran binomial adalah materi standar kelas 7. Soal ini tidak memiliki kerumitan tambahan, menjadikannya tugas rutin yang sesuai untuk tingkat kemudahan rendah. |

Run 3 — solusi: Menggunakan sifat distributif (FOIL): (x + 1)(x + 3) = x(x) + x(3) + 1(x) + 1(3) = x² + 3x + x + 3 = x² + 4x + 3.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan prosedur perkalian suku dua (distributif) yang merupakan prosedur standar dalam aljabar kelas 7. Ini adalah penerapan langsung dari algoritma perkalian aljabar.. Bukti: Tentukan setiap bentuk aljabar berikut dalam bentuk jabaran.; (x + 1)(x + 3)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang prosedur perkalian bentuk aljabar (distributif/FOIL), yang merupakan pengetahuan prosedural.. Bukti: (x + 1)(x + 3)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menerapkan aturan distributif dasar tanpa kendala tambahan atau integrasi konsep yang kompleks. Jalur penyelesaian sangat jelas.. Bukti: (x + 1)(x + 3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel, penjumlahan suku sejenis, dan sifat distributif perkalian. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Perkalian bentuk aljabar (x+a)(x+b) adalah materi standar kelas 7. Soal ini tidak memerlukan manipulasi lebih lanjut atau pemecahan masalah, sehingga dikategorikan mudah. |

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
Solusi minimum hasil AI: Untuk memfaktorkan 5x + 10, tentukan FPB dari koefisien 5 dan konstanta 10, yaitu 5. Bagi setiap suku dengan 5: 5x ÷ 5 = x dan 10 ÷ 5 = 2. Maka, 5x + 10 = 5(x + 2).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `cd9d4e24a29b75c4a56e4ca88e820ef474de69ac2746beea6a3a2381802307b2`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2375 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2396 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2405 |

Run 1 — solusi: Untuk memfaktorkan 5x + 10, cari FPB dari koefisien 5 dan konstanta 10, yaitu 5. Bagi setiap suku dengan 5: 5x/5 = x dan 10/5 = 2. Maka, 5x + 10 = 5(x + 2).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pemfaktoran aljabar sederhana dengan mengeluarkan faktor persekutuan terbesar (FPB). Ini adalah penerapan langsung dari prosedur yang sudah dipelajari.. Bukti: Tentukan setiap bentuk aljabar berikut dalam bentuk faktor.; 5x + 10
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritme pemfaktoran aljabar (distributif terbalik), yang merupakan pengetahuan prosedural.. Bukti: 5x + 10
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengidentifikasi FPB dari dua suku dan menerapkan sifat distributif. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: 5x + 10

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang FPB bilangan bulat dan sifat distributif perkalian terhadap penjumlahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pemfaktoran bentuk linear sederhana adalah materi dasar aljabar kelas 7 yang diajarkan secara eksplisit sebagai prosedur rutin. |

Run 2 — solusi: Untuk memfaktorkan 5x + 10, cari FPB dari koefisien 5 dan konstanta 10, yaitu 5. Bagi setiap suku dengan 5: 5x/5 = x dan 10/5 = 2. Maka, 5x + 10 = 5(x + 2).
- Domain kognitif `classify/knowing`: Siswa diminta untuk menerapkan prosedur pemfaktoran aljabar sederhana (distributif terbalik) yang merupakan prosedur standar dalam kurikulum kelas 7.. Bukti: Tentukan setiap bentuk aljabar berikut dalam bentuk faktor.; 5x + 10
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritme pemfaktoran aljabar dasar (prosedural) yang didasarkan pada konsep FPB (konseptual).. Bukti: 5x + 10
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengidentifikasi FPB dari dua suku dan menerapkan sifat distributif. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: 5x + 10

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang FPB bilangan bulat dan sifat distributif perkalian terhadap penjumlahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pemfaktoran bentuk aljabar linear dua suku adalah materi dasar kelas 7 yang diajarkan secara eksplisit sebagai prosedur rutin. |

Run 3 — solusi: Untuk memfaktorkan 5x + 10, cari FPB dari koefisien 5 dan konstanta 10, yaitu 5. Bagi setiap suku dengan 5: 5x/5 = x dan 10/5 = 2. Maka, 5x + 10 = 5(x + 2).
- Domain kognitif `classify/knowing`: Soal meminta siswa menerapkan prosedur pemfaktoran aljabar sederhana (distributif terbalik) yang merupakan prosedur standar dalam kurikulum kelas 7.. Bukti: Tentukan setiap bentuk aljabar berikut dalam bentuk faktor.; 5x + 10
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami konsep faktor persekutuan terbesar (FPB) dan menerapkan algoritma pemfaktoran aljabar.. Bukti: Tentukan setiap bentuk aljabar berikut dalam bentuk faktor.; 5x + 10
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengidentifikasi FPB dari dua suku dan menerapkan sifat distributif. Tidak ada kendala yang berinteraksi atau perencanaan langkah yang kompleks.. Bukti: 5x + 10

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang faktor persekutuan terbesar (FPB) dan sifat distributif perkalian terhadap penjumlahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pemfaktoran bentuk aljabar linear dua suku dengan koefisien sederhana adalah materi dasar kelas 7 yang diajarkan secara eksplisit sebagai prosedur rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 1, "knowing": 2} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3849`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta siswa untuk melakukan prosedur pemfaktoran aljabar sederhana menggunakan sifat distributif. Ini adalah tugas rutin yang langsung menguji penguasaan prosedur dasar.
- Dimensi pengetahuan `procedural`: Soal ini menguji penerapan algoritme pemfaktoran aljabar (distributif terbalik), yang merupakan pengetahuan prosedural standar dalam kurikulum kelas 7.
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengidentifikasi FPB dari dua suku dan menerapkan sifat distributif. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang FPB bilangan bulat dan sifat distributif perkalian terhadap penjumlahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pemfaktoran bentuk aljabar linear dua suku dengan koefisien sederhana adalah materi dasar kelas 7 yang diajarkan secara eksplisit sebagai prosedur rutin. |

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: Tiket terjual: Rani=a, Bagas=3a, Cakra=a-4, Malik=a+10. Total terjual = a + 3a + (a-4) + (a+10) = 6a + 6. Total tiket keseluruhan = (6a + 6) + 10 = 6a + 16. Jika a=12, maka 6(12) + 16 = 72 + 16 = 88.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung', 'membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e665b98d4f5a775ff3cffa2e007883429ce4be7154959911d7b8a51cf149f3c2`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2710 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2720 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2729 |

Run 1 — solusi: Tiket terjual: Rani=a, Bagas=3a, Cakra=a-4, Malik=a+10. Total terjual = a + 3a + (a-4) + (a+10) = 6a + 6. Total tiket keseluruhan = (6a + 6) + 10 = 6a + 16. Jika a=12, maka 6(12) + 16 = 72 + 16 = 88.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerjemahkan situasi verbal ke dalam bentuk aljabar (pemodelan) dan melakukan operasi penjumlahan suku sejenis, yang merupakan penerapan konsep aljabar dasar.. Bukti: Berapa bentuk aljabar dari banyak tiket yang dijual oleh Bagas, Cakra, dan Malik.; Berapa bentuk aljabar dari total tiket yang terjual oleh Rani, Bagas, Cakra, dan Malik.; Jika ada 10 tiket yang tidak terjual, berapa bentuk aljabar dari banyak tiket secara keseluruhan.
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman tentang bagaimana variabel dan konstanta merepresentasikan kuantitas dalam konteks cerita, yang merupakan pengetahuan konseptual tentang aljabar.. Bukti: Berapa bentuk aljabar dari banyak tiket yang dijual oleh Bagas, Cakra, dan Malik.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena melibatkan beberapa langkah yang saling bergantung: memodelkan masing-masing individu, menjumlahkan ekspresi aljabar, dan melakukan substitusi nilai. Siswa harus mengelola beberapa informasi (Rani, Bagas, Cakra, Malik, tiket tidak terjual) secara bersamaan untuk membentuk ekspresi total yang benar.. Bukti: Rani menjual a tiket. Bagas menjual 3 kali dari tiket yang dijual oleh Rani. Cakra menjual 4 tiket lebih sedikit dari tiket yang dijual oleh Rani. Malik menjual 10 tiket lebih banyak dari Rani.; Jika tiket yang dijual oleh Rani sebanyak 12 tiket. Berapa banyak tiket secara keseluruhan?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aljabar dasar (penjumlahan suku sejenis) dan substitusi nilai ke dalam variabel. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 5 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu memodelkan situasi sederhana ke bentuk aljabar. Soal ini menuntut ketelitian dalam menggabungkan variabel dan konstanta, namun prosedurnya standar. |

Run 2 — solusi: Tiket terjual: Rani=a, Bagas=3a, Cakra=a-4, Malik=a+10. Total terjual = a + 3a + (a-4) + (a+10) = 6a + 6. Total tiket keseluruhan = (6a + 6) + 10 = 6a + 16. Untuk a=12: 6(12) + 16 = 72 + 16 = 88.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk menerjemahkan situasi verbal ke dalam bentuk aljabar (pemodelan) dan melakukan operasi penjumlahan suku sejenis. Ini adalah penerapan konsep aljabar dasar yang rutin bagi siswa kelas 7.. Bukti: Berapa bentuk aljabar dari banyak tiket yang dijual oleh Bagas, Cakra, dan Malik.; Berapa bentuk aljabar dari total tiket yang terjual oleh Rani, Bagas, Cakra, dan Malik.; Jika ada 10 tiket yang tidak terjual, berapa bentuk aljabar dari banyak tiket secara keseluruhan.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antar variabel dan prinsip penjumlahan suku sejenis dalam aljabar.. Bukti: Berapa bentuk aljabar dari banyak tiket yang dijual oleh Bagas, Cakra, dan Malik.; Berapa bentuk aljabar dari total tiket yang terjual oleh Rani, Bagas, Cakra, dan Malik.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena melibatkan beberapa langkah yang saling terkait (pemodelan empat variabel berbeda, penjumlahan aljabar, dan penambahan konstanta untuk total keseluruhan) yang menuntut ketelitian dalam mengelola variabel dan konstanta.. Bukti: Rani menjual a tiket. Bagas menjual 3 kali dari tiket yang dijual oleh Rani. Cakra menjual 4 tiket lebih sedikit dari tiket yang dijual oleh Rani. Malik menjual 10 tiket lebih banyak dari Rani.; Jika ada 10 tiket yang tidak terjual, berapa bentuk aljabar dari banyak tiket secara keseluruhan.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aljabar dasar (penjumlahan/pengurangan suku sejenis) dan penerjemahan kalimat verbal ke bentuk aljabar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 5 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu memodelkan situasi sederhana ke bentuk aljabar. Soal ini memerlukan ketelitian dalam menjumlahkan suku sejenis dan konstanta, namun prosedurnya standar dan familiar. |

Run 3 — solusi: Tiket terjual: Rani=a, Bagas=3a, Cakra=a-4, Malik=a+10. Total terjual = a + 3a + (a-4) + (a+10) = 6a + 6. Total tiket keseluruhan = (6a + 6) + 10 = 6a + 16. Untuk a=12: 6(12) + 16 = 72 + 16 = 88.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerjemahkan situasi verbal ke dalam bentuk aljabar dan melakukan operasi penjumlahan suku sejenis, yang merupakan penerapan prosedur aljabar dasar pada konteks rutin.. Bukti: Berapa bentuk aljabar dari banyak tiket yang dijual oleh Bagas, Cakra, dan Malik.; Berapa bentuk aljabar dari total tiket yang terjual oleh Rani, Bagas, Cakra, dan Malik.; Jika ada 10 tiket yang tidak terjual, berapa bentuk aljabar dari banyak tiket secara keseluruhan.
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman tentang bagaimana variabel dan konstanta digunakan untuk merepresentasikan hubungan kuantitatif dalam situasi nyata.. Bukti: Berapa bentuk aljabar dari banyak tiket yang dijual oleh Bagas, Cakra, dan Malik.; Berapa bentuk aljabar dari total tiket yang terjual oleh Rani, Bagas, Cakra, dan Malik.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena melibatkan beberapa langkah yang saling bergantung (memodelkan masing-masing individu, menjumlahkan total, menambahkan konstanta tiket tidak terjual, lalu substitusi). Meskipun prosedurnya familiar, siswa harus mengintegrasikan beberapa informasi dan menjaga konsistensi variabel agar tidak terjadi kesalahan penjumlahan.. Bukti: Rani menjual a tiket. Bagas menjual 3 kali dari tiket yang dijual oleh Rani. Cakra menjual 4 tiket lebih sedikit dari tiket yang dijual oleh Rani. Malik menjual 10 tiket lebih banyak dari Rani.; Jika tiket yang dijual oleh Rani sebanyak 12 tiket. Berapa banyak tiket secara keseluruhan?

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
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu memodelkan situasi sederhana ke bentuk aljabar. Tingkat kesulitan Medium sesuai karena menuntut ketelitian dalam mengintegrasikan empat ekspresi aljabar yang berbeda dan menambahkan konstanta tambahan sebelum substitusi. |

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
Solusi minimum hasil AI: Arief memiliki y buah apel. Jika ia memakan 2 buah apel, maka jumlah apel berkurang 2, sehingga bentuk aljabarnya adalah y - 2.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['mengidentifikasi', 'membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f254e3a0da2adc24f159c3354cf795a53d4f8139562c48f59bdf30aa0052e164`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2337 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2320 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2341 |

Run 1 — solusi: Arief memiliki y apel. Jika ia memakan 2 apel, maka jumlah apel berkurang 2, sehingga bentuk aljabarnya adalah y - 2.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerjemahkan situasi verbal ke dalam bentuk aljabar sederhana. Ini adalah penerapan langsung dari konsep variabel dan operasi pengurangan dalam aljabar.. Bukti: Arief membeli y buah apel.; Arief memakan 2 buah apel.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang bagaimana variabel dan operasi aritmatika digunakan untuk merepresentasikan situasi nyata (konseptual).. Bukti: Tentukan bentuk aljabar dari banyak buah apel dari setiap situasi berikut.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar bagi siswa kelas 7. Siswa hanya perlu mengidentifikasi variabel (y) dan operasi yang sesuai (pengurangan) untuk situasi yang diberikan. Tidak ada langkah yang saling bergantung atau kendala yang kompleks.. Bukti: Arief membeli y buah apel.; Arief memakan 2 buah apel.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel dan operasi pengurangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal pengenalan aljabar yang sangat standar untuk kelas 7, di mana siswa belajar menerjemahkan kalimat menjadi ekspresi aljabar satu langkah. |

Run 2 — solusi: Arief memiliki y apel. Jika ia memakan 2 apel, maka jumlah apelnya berkurang 2, sehingga bentuk aljabarnya adalah y - 2.
- Domain kognitif `classify/knowing`: Siswa diminta menerjemahkan situasi verbal ke dalam bentuk aljabar sederhana. Ini adalah prosedur langsung yang mengenali operasi pengurangan dalam konteks variabel.. Bukti: Arief memakan 2 buah apel.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang bagaimana variabel dan operasi dasar (pengurangan) digunakan untuk merepresentasikan situasi nyata.. Bukti: Tentukan bentuk aljabar dari banyak buah apel dari setiap situasi berikut.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 7. Siswa hanya perlu memahami bahwa 'memakan' berarti pengurangan dan menerjemahkannya ke notasi aljabar. Tidak ada langkah yang saling bergantung atau kendala yang kompleks.. Bukti: Arief memakan 2 buah apel.; y - 2

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar operasi pengurangan dan notasi variabel. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah pengenalan standar aljabar kelas 7. Siswa diharapkan mampu memodelkan situasi pengurangan sederhana tanpa kesulitan berarti. |

Run 3 — solusi: Arief memiliki y buah apel. Jika ia memakan 2 buah apel, maka jumlah apel yang tersisa adalah y dikurangi 2, yaitu y - 2.
- Domain kognitif `classify/knowing`: Siswa diminta menerjemahkan situasi verbal sederhana ke dalam bentuk aljabar dasar. Ini melibatkan pengenalan operasi pengurangan dalam konteks variabel, yang merupakan prosedur langsung.. Bukti: Arief memakan 2 buah apel.; Tentukan bentuk aljabar dari banyak buah apel dari setiap situasi berikut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang simbol dan operasi dasar dalam aljabar (pengurangan), yang termasuk dalam pengetahuan prosedural untuk memodelkan situasi.. Bukti: Arief memakan 2 buah apel.; y - 2
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar bagi siswa kelas 7. Tidak ada langkah yang saling bergantung atau kendala yang berinteraksi. Siswa hanya perlu mengidentifikasi operasi pengurangan dari konteks 'memakan'.. Bukti: Arief memakan 2 buah apel.; y - 2

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel sebagai representasi jumlah dan operasi aritmatika dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah pengenalan awal aljabar di kelas 7. Soal ini bersifat langsung dan tidak memerlukan perencanaan kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 1, "knowing": 2} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3672`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa diminta menerjemahkan situasi verbal sederhana ke dalam bentuk aljabar dasar. Ini adalah prosedur langsung yang mengenali operasi pengurangan dalam konteks variabel.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang simbol dan operasi dasar dalam aljabar (pengurangan), yang merupakan pengetahuan prosedural untuk memodelkan situasi.
- Intended difficulty `Easy`: Soal ini sangat mendasar bagi siswa kelas 7. Tidak ada langkah yang saling bergantung atau kendala yang berinteraksi. Siswa hanya perlu mengidentifikasi operasi pengurangan dari konteks 'memakan'.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel sebagai representasi jumlah dan operasi aritmatika dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah pengenalan awal aljabar di kelas 7. Soal ini bersifat langsung dan tidak memerlukan perencanaan kompleks. |

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: Sudut bertolak belakang terbentuk dari dua garis yang berpotongan di satu titik. Hubungan ini hanya memerlukan dua garis yang berpotongan, sehingga tetap berlaku meskipun garis-garis tersebut tidak sejajar. Sebaliknya, hubungan sehadap, berseberangan, dan sepihak memerlukan syarat garis sejajar agar memiliki sifat sudut yang sama besar atau berpelurus.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menganalisis']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `20c7e73f3812e0f1ed3fc207168f096fba4e26ab61e7f9cb30f619984a769ea4`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2461 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2428 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2389 |

Run 1 — solusi: Sudut bertolak belakang terbentuk dari dua garis yang berpotongan di satu titik. Hubungan ini hanya memerlukan dua garis yang berpotongan, sehingga tetap berlaku meskipun garis-garis tersebut tidak sejajar. Sebaliknya, hubungan sehadap, berseberangan, dan sepihak memerlukan syarat garis sejajar agar memiliki sifat sudut yang sama besar atau berpelurus.
- Domain kognitif `classify/knowing`: Soal menuntut siswa untuk memahami definisi dan syarat keberlakuan hubungan antar sudut. Siswa harus membedakan antara hubungan yang bergantung pada sifat kesejajaran (sehadap, berseberangan, sepihak) dan hubungan yang hanya bergantung pada perpotongan dua garis (bertolak belakang). Ini melibatkan pemahaman konsep dasar geometri.. Bukti: Hubungan mana yang masih berlaku jika kedua garis tidak sejajar?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual mengenai syarat-syarat geometris yang mendasari berbagai jenis hubungan sudut, bukan sekadar menghitung atau menerapkan prosedur algoritmis.. Bukti: Pada dua garis yang berpotongan, terdapat sudut yang bertolak belakang, sedangkan pada dua garis sejajar yang berpotongan dengan garis lain, dikenal istilah sehadap, dalam berseberangan, luar berseberangan, dalam sepihak, luar sepihak.
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena menanyakan konsep dasar yang langsung. Siswa hanya perlu mengenali definisi sudut bertolak belakang yang sudah dipelajari di awal materi garis dan sudut. Tidak ada langkah perhitungan atau integrasi kompleks yang diperlukan.. Bukti: Hubungan mana yang masih berlaku jika kedua garis tidak sejajar?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang definisi sudut bertolak belakang dan syarat garis sejajar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi hubungan antar sudut adalah kurikulum standar kelas 7. Soal ini menguji pemahaman teoretis dasar yang seharusnya dikuasai siswa setelah mempelajari topik tersebut. |

Run 2 — solusi: Sudut bertolak belakang terbentuk oleh dua garis yang berpotongan di satu titik. Hubungan ini tidak memerlukan syarat garis sejajar, sehingga tetap berlaku meskipun garis tidak sejajar. Sebaliknya, hubungan sehadap, berseberangan, dan sepihak memerlukan syarat garis sejajar agar memiliki sifat sudut yang konsisten (sama besar atau berpelurus).
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk memahami definisi dan syarat keberlakuan hubungan antar sudut. Siswa harus membedakan antara hubungan yang bergantung pada sifat kesejajaran garis (sehadap, berseberangan, sepihak) dan hubungan yang hanya bergantung pada perpotongan dua garis (bertolak belakang). Ini melibatkan pemahaman konsep dasar geometri.. Bukti: Hubungan mana yang masih berlaku jika kedua garis tidak sejajar?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang definisi dan syarat-syarat yang mendasari hubungan antar sudut dalam geometri.. Bukti: Pada dua garis yang berpotongan, terdapat sudut yang bertolak belakang; dikenal istilah sehadap, dalam berseberangan, luar berseberangan, dalam sepihak, luar sepihak
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena menanyakan konsep dasar yang langsung. Siswa hanya perlu mengenali sifat dasar sudut bertolak belakang yang sudah dipelajari sebagai bagian dari materi dasar garis dan sudut. Tidak ada langkah perhitungan atau integrasi kompleks yang diperlukan.. Bukti: Hubungan mana yang masih berlaku jika kedua garis tidak sejajar?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi sudut bertolak belakang dan syarat garis sejajar dalam hubungan sudut. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi hubungan antar sudut adalah kurikulum standar kelas 7. Membedakan sifat sudut yang bergantung pada kesejajaran adalah pemahaman dasar yang diharapkan. |

Run 3 — solusi: Sudut bertolak belakang terbentuk oleh dua garis yang berpotongan di satu titik. Sifat ini tidak memerlukan syarat garis sejajar, sehingga tetap berlaku meskipun kedua garis tidak sejajar. Hubungan sudut lainnya (sehadap, berseberangan, sepihak) memerlukan syarat garis sejajar agar memiliki nilai yang sama atau berpelurus.
- Domain kognitif `classify/knowing`: Soal menuntut pemahaman konseptual tentang syarat keberlakuan hubungan antar sudut. Siswa harus membedakan sifat sudut yang bergantung pada kesejajaran garis dengan sifat yang hanya bergantung pada perpotongan dua garis.. Bukti: Hubungan mana yang masih berlaku jika kedua garis tidak sejajar?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual mengenai definisi dan syarat keberlakuan hubungan antar sudut (sudut bertolak belakang vs sudut-sudut pada garis sejajar).. Bukti: Pada dua garis yang berpotongan, terdapat sudut yang bertolak belakang; Hubungan mana yang masih berlaku jika kedua garis tidak sejajar?
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena menguji pemahaman konsep dasar tentang sifat sudut bertolak belakang yang merupakan materi fundamental dalam geometri kelas 7. Tidak ada perhitungan kompleks atau perencanaan langkah yang rumit; siswa hanya perlu mengenali definisi dasar.. Bukti: Hubungan mana yang masih berlaku jika kedua garis tidak sejajar?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang sudut bertolak belakang dan syarat garis sejajar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konsep sudut bertolak belakang adalah materi dasar kelas 7. Soal tidak menuntut analisis mendalam, hanya pengenalan sifat dasar. |

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 30. Soal `4d6693103dbd451e67e5be49`

Gambar berikut menunjukkan dua pasang garis sejajar. Salah satu sudut diketahui besarnya.<br><br>Bangun apakah yang ditunjukkan oleh segi empat $ABCD$? Jelaskan.

| Opsi | Isi |
|---|---|
| A | Jajargenjang, karena kedua pasang sisi yang berhadapan sejajar |
| B | Layang-layang, karena dua pasang sisi yang berdekatan sama panjang |
| C | Trapesium, karena hanya sepasang sisi yang sejajar |
| D | Persegi panjang, karena semua sudutnya siku-siku |

![Gambar sumber soal 30](<../../../images/kelas7_crop-p0192-jajargenjang.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Berdasarkan tanda panah pada gambar, sisi AB sejajar dengan DC (tanda panah ganda) dan sisi AD sejajar dengan BC (tanda panah tunggal). Definisi jajargenjang adalah segiempat dengan dua pasang sisi yang berhadapan sejajar. Karena ABCD memiliki dua pasang sisi sejajar, maka ABCD adalah jajargenjang.
Gambar sumber: images/kelas7_crop-p0192-jajargenjang.png. Transkripsi visual: Gambar menunjukkan segiempat ABCD. Sisi AB dan DC memiliki tanda panah ganda, menunjukkan keduanya sejajar. Sisi AD dan BC memiliki tanda panah tunggal, menunjukkan keduanya sejajar. Terdapat sudut 130 derajat di titik A.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `61721f942a50a8c5370a093cbd7d088aaab4d7017b3de14b8efbca411452a9bd`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3578 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3568 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3569 |

Run 1 — solusi: Berdasarkan tanda pada gambar, sisi AB sejajar dengan DC dan sisi AD sejajar dengan BC. Definisi jajargenjang adalah segiempat dengan dua pasang sisi yang berhadapan sejajar. Oleh karena itu, ABCD adalah jajargenjang.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi bangun datar berdasarkan properti geometris (garis sejajar) yang diberikan secara eksplisit pada gambar. Ini adalah penerapan langsung dari definisi jajargenjang.. Bukti: Gambar berikut menunjukkan dua pasang garis sejajar.; Bangun apakah yang ditunjukkan oleh segi empat ABCD?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami definisi konseptual dari jajargenjang (segiempat dengan dua pasang sisi sejajar) dan mengenali simbol garis sejajar pada gambar.. Bukti: dua pasang garis sejajar; Bangun apakah yang ditunjukkan oleh segi empat ABCD?
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengenali simbol garis sejajar pada gambar dan mencocokkannya dengan definisi jajargenjang. Tidak ada langkah perhitungan atau integrasi konsep yang kompleks.. Bukti: Gambar berikut menunjukkan dua pasang garis sejajar.; Bangun apakah yang ditunjukkan oleh segi empat ABCD?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang definisi jajargenjang dan pengenalan simbol garis sejajar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah mempelajari sifat-sifat bangun datar dan hubungan antar garis. Soal ini menguji pengenalan konsep dasar tanpa kerumitan tambahan. |

Run 2 — solusi: Definisi jajargenjang adalah segi empat dengan dua pasang sisi yang berhadapan sejajar. Gambar menunjukkan AB ∥ DC (tanda panah ganda) dan AD ∥ BC (tanda panah tunggal). Oleh karena itu, ABCD adalah jajargenjang.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi bangun datar berdasarkan properti geometris (garis sejajar) yang diberikan secara eksplisit pada gambar. Ini adalah penerapan langsung dari definisi jajargenjang.. Bukti: Bangun apakah yang ditunjukkan oleh segi empat ABCD?; Gambar menunjukkan dua pasang garis sejajar.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang definisi dan klasifikasi bangun datar (konsep) berdasarkan properti garis sejajar.. Bukti: Bangun apakah yang ditunjukkan oleh segi empat ABCD?; Gambar menunjukkan dua pasang garis sejajar.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengenali simbol garis sejajar pada gambar dan mencocokkannya dengan definisi jajargenjang. Tidak ada langkah kompleks atau integrasi konsep yang sulit.. Bukti: Gambar menunjukkan dua pasang garis sejajar.; Bangun apakah yang ditunjukkan oleh segi empat ABCD?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang definisi jajargenjang dan simbol garis sejajar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah mempelajari sifat-sifat bangun datar dan garis sejajar. Soal ini merupakan pengenalan langsung terhadap properti jajargenjang tanpa memerlukan manipulasi atau penalaran bertingkat. |

Run 3 — solusi: Definisi jajargenjang adalah segi empat dengan dua pasang sisi yang berhadapan sejajar. Gambar menunjukkan AB sejajar DC dan AD sejajar BC. Oleh karena itu, ABCD adalah jajargenjang.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi bangun datar berdasarkan sifat geometris (kesejajaran sisi) yang diberikan secara visual pada gambar. Ini adalah penerapan langsung dari definisi jajargenjang.. Bukti: Bangun apakah yang ditunjukkan oleh segi empat ABCD?; Gambar berikut menunjukkan dua pasang garis sejajar.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang definisi dan sifat-sifat bangun datar (jajargenjang) berdasarkan hubungan kesejajaran sisi.. Bukti: Bangun apakah yang ditunjukkan oleh segi empat ABCD?; Gambar berikut menunjukkan dua pasang garis sejajar.
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu mengenali definisi jajargenjang berdasarkan informasi visual yang sudah eksplisit (tanda panah kesejajaran). Tidak ada langkah kompleks atau integrasi konsep yang sulit.. Bukti: Gambar berikut menunjukkan dua pasang garis sejajar.; Bangun apakah yang ditunjukkan oleh segi empat ABCD?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang definisi jajargenjang dan notasi garis sejajar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah mempelajari sifat-sifat bangun datar dan notasi garis sejajar. Soal ini merupakan pengenalan langsung terhadap definisi jajargenjang tanpa memerlukan manipulasi atau penalaran bertingkat. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `5089`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta siswa untuk mengidentifikasi bangun datar berdasarkan properti geometris (garis sejajar) yang diberikan secara eksplisit pada gambar. Ini adalah penerapan langsung dari definisi jajargenjang.
- Dimensi pengetahuan `conceptual`: Siswa perlu memahami definisi konseptual dari jajargenjang (segiempat dengan dua pasang sisi sejajar) dan mengenali simbol garis sejajar pada gambar.
- Intended difficulty `Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengenali simbol garis sejajar pada gambar dan mencocokkannya dengan definisi jajargenjang. Tidak ada langkah perhitungan atau integrasi konsep yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang definisi jajargenjang dan pengenalan simbol garis sejajar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah mempelajari sifat-sifat bangun datar dan hubungan antar garis. Soal ini menguji pengenalan konsep dasar tanpa kerumitan tambahan. |

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
Transkripsi visual: Gambar menunjukkan segiempat ABCD. Sisi AB dan DC memiliki tanda panah ganda, menunjukkan keduanya sejajar. Sisi AD dan BC memiliki tanda panah tunggal, menunjukkan keduanya sejajar. Terdapat sudut 130 derajat di titik A.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: Dua bangun datar yang sebangun memiliki bentuk yang sama dan besar sudut yang bersesuaian sama, namun ukuran panjang sisi, keliling, dan luasnya berubah secara proporsional sesuai faktor skala.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3bf12194606524b27b7f6923c6cc9f528be30bf5f7ae3cd444fbd4ab932d6024`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2372 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2348 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2380 |

Run 1 — solusi: Dua bangun datar yang sebangun memiliki bentuk yang sama dan besar sudut yang bersesuaian sama, namun ukuran panjang sisi, keliling, dan luasnya berubah secara proporsional sesuai faktor skala.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengidentifikasi properti yang berubah pada bangun datar yang sebangun (panjang sisi, keliling, luas) dibandingkan dengan properti yang tetap (bentuk, besar sudut). Ini memerlukan pemahaman konseptual tentang definisi kesebangunan.. Bukti: Bangun datar yang dihasilkan melalui proses tersebut memiliki sifat sebangun dengan bangun datar awal.; apa perbedaan antara bangun datar awal dan bangun datar hasil perbesaran atau pengecilan?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep kesebangunan, yaitu hubungan antara bentuk yang tetap sama dan ukuran yang berubah secara proporsional.. Bukti: memiliki sifat sebangun dengan bangun datar awal; perbedaan antara bangun datar awal dan bangun datar hasil perbesaran atau pengecilan
- Intended difficulty `classify/Easy`: Soal ini bersifat teoretis dan langsung menanyakan pemahaman dasar tentang definisi kesebangunan. Tidak ada perhitungan atau langkah prosedural yang kompleks. Siswa hanya perlu mengenali karakteristik bangun sebangun.. Bukti: memiliki sifat sebangun dengan bangun datar awal; apa perbedaan antara bangun datar awal dan bangun datar hasil perbesaran atau pengecilan?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep kesebangunan (bentuk sama, ukuran berubah). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini menguji pemahaman konseptual dasar yang diajarkan di kelas 7 mengenai kesebangunan, tanpa menuntut analisis atau perhitungan yang rumit. |

Run 2 — solusi: Dua bangun datar yang sebangun memiliki bentuk yang sama (sudut-sudut yang bersesuaian sama besar), namun ukuran panjang sisi, keliling, dan luasnya berubah secara proporsional sesuai dengan faktor skala perbesaran atau pengecilan.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk memahami konsep dasar kesebangunan, yaitu membedakan properti yang invarian (bentuk dan sudut) dengan properti yang berubah (panjang sisi, keliling, luas) saat terjadi dilatasi/perbesaran.. Bukti: Bangun datar yang dihasilkan melalui proses tersebut memiliki sifat sebangun dengan bangun datar awal.; apa perbedaan antara bangun datar awal dan bangun datar hasil perbesaran atau pengecilan?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip atau konsep dasar kesebangunan (bahwa bentuk tetap sama namun ukuran berubah) untuk menjawab pertanyaan ini.. Bukti: Bangun datar yang dihasilkan melalui proses tersebut memiliki sifat sebangun dengan bangun datar awal.
- Intended difficulty `classify/Easy`: Soal ini bersifat konseptual dan langsung. Siswa hanya perlu mengidentifikasi sifat dasar kesebangunan tanpa melakukan perhitungan atau perencanaan langkah yang kompleks.. Bukti: apa perbedaan antara bangun datar awal dan bangun datar hasil perbesaran atau pengecilan?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep kesebangunan dan dilatasi (perbesaran/pengecilan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pertanyaan ini menguji pemahaman teoretis dasar yang sesuai dengan kurikulum kelas 7 mengenai kesebangunan, tanpa beban komputasi. |

Run 3 — solusi: Dua bangun datar yang sebangun memiliki bentuk yang sama dan besar sudut yang bersesuaian sama, namun ukuran panjang sisi, keliling, dan luasnya berubah secara proporsional sesuai faktor skala.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengidentifikasi properti yang berubah pada bangun datar yang sebangun (panjang sisi, keliling, luas) dibandingkan dengan properti yang tetap (bentuk, besar sudut). Ini memerlukan pemahaman konseptual tentang definisi kesebangunan.. Bukti: Bangun datar yang dihasilkan melalui proses tersebut memiliki sifat sebangun dengan bangun datar awal.; apa perbedaan antara bangun datar awal dan bangun datar hasil perbesaran atau pengecilan?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep kesebangunan, yaitu hubungan antara bentuk yang sama namun ukuran yang berbeda, yang merupakan pemahaman konseptual.. Bukti: memiliki sifat sebangun dengan bangun datar awal; perbedaan antara bangun datar awal dan bangun datar hasil perbesaran atau pengecilan
- Intended difficulty `classify/Easy`: Soal ini bersifat konseptual dasar mengenai definisi kesebangunan. Siswa hanya perlu mengenali properti yang berubah (ukuran) dan yang tetap (bentuk/sudut) tanpa melakukan perhitungan kompleks atau perencanaan langkah yang rumit.. Bukti: memiliki sifat sebangun dengan bangun datar awal; apa perbedaan antara bangun datar awal dan bangun datar hasil perbesaran atau pengecilan?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep kesebangunan dan perbesaran/pengecilan gambar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini menguji pemahaman definisi dasar kesebangunan yang merupakan materi awal kelas 7, tanpa menuntut analisis atau perhitungan yang mendalam. |

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 32. Soal `ee6b087d7e2980c7460df17f`

Cermin manakah yang menghasilkan bayangan yang sebangun dengan benda asalnya?

| Opsi | Isi |
|---|---|
| A | Tidak ada cermin yang menghasilkan bayangan sebangun |
| B | Cermin b |
| C | Cermin a |
| D | Cermin c |

![Gambar sumber soal 32](<../../../images/kelas7_crop-p0196-cermin.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Dua bangun dikatakan sebangun jika memiliki bentuk yang sama dan perbandingan sisi-sisi yang bersesuaian senilai. Pada cermin a, bayangan memiliki bentuk dan proporsi yang sama dengan benda aslinya, sehingga sebangun. Cermin b dan c menghasilkan bayangan yang terdistorsi (tidak proporsional), sehingga tidak sebangun.
Gambar sumber: images/kelas7_crop-p0196-cermin.png. Transkripsi visual: Terdapat tiga cermin yang diberi label a, b, dan c. Cermin a menampilkan bayangan orang yang proporsinya sama dengan orang aslinya. Cermin b menampilkan bayangan orang yang tampak lebih kurus atau memanjang (terdistorsi). Cermin c menampilkan bayangan orang yang tampak lebih lebar atau pendek (terdistorsi).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `213d9f39df734a1351f23dff8fc66d81a7ae854eb073c447b8d0d96d1663d718`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3532 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3503 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 3552 |

Run 1 — solusi: Dua bangun dikatakan sebangun jika memiliki bentuk yang sama dan perbandingan sisi-sisi yang bersesuaian senilai. Pada cermin a, bayangan memiliki bentuk dan proporsi yang sama dengan benda asli (orang), sehingga sebangun. Cermin b dan c menghasilkan bayangan yang terdistorsi (tidak proporsional), sehingga tidak sebangun.
- Domain kognitif `classify/applying`: Soal ini meminta siswa untuk mengidentifikasi contoh kesebangunan dalam konteks visual. Siswa perlu mengenali konsep kesebangunan (bentuk sama, proporsi terjaga) dan menerapkannya untuk mengevaluasi gambar yang diberikan.. Bukti: Cermin manakah yang menghasilkan bayangan yang sebangun dengan benda asalnya?
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami konsep kesebangunan (conceptual) untuk membedakan antara bayangan yang proporsional (sebangun) dan yang terdistorsi.. Bukti: Cermin manakah yang menghasilkan bayangan yang sebangun dengan benda asalnya?
- Intended difficulty `classify/Easy`: Soal ini bersifat intuitif dan langsung. Siswa hanya perlu membandingkan bentuk visual antara objek asli dan bayangan untuk menentukan mana yang mempertahankan proporsi. Tidak ada perhitungan atau langkah kompleks yang diperlukan.. Bukti: Cermin manakah yang menghasilkan bayangan yang sebangun dengan benda asalnya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk dan proporsi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini menguji pemahaman konseptual dasar tentang kesebangunan melalui pengamatan visual, yang sesuai dengan tingkat kognitif kelas 7. |

Run 2 — solusi: Dua bangun dikatakan sebangun jika memiliki bentuk yang sama dan perbandingan sisi-sisi yang bersesuaian senilai. Pada cermin 'a', bayangan memiliki bentuk dan proporsi yang sama dengan benda aslinya, sehingga sebangun. Cermin 'b' dan 'c' menghasilkan distorsi yang mengubah proporsi bayangan.
- Domain kognitif `classify/applying`: Soal ini meminta siswa untuk mengidentifikasi konsep kesebangunan (bentuk sama, proporsi sama) melalui pengamatan visual, yang merupakan penerapan langsung dari definisi kesebangunan.. Bukti: Cermin manakah yang menghasilkan bayangan yang sebangun dengan benda asalnya?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep konseptual tentang apa itu kesebangunan (proporsionalitas bentuk) untuk membedakan antara bayangan yang sebangun dan yang terdistorsi.. Bukti: Cermin manakah yang menghasilkan bayangan yang sebangun dengan benda asalnya?
- Intended difficulty `classify/Easy`: Soal ini bersifat intuitif dan langsung. Siswa hanya perlu mengenali visual yang mempertahankan proporsi tanpa perhitungan matematis yang kompleks atau langkah-langkah prosedural yang panjang.. Bukti: Cermin manakah yang menghasilkan bayangan yang sebangun dengan benda asalnya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep kesebangunan (bentuk sama, proporsi sama). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sangat mendasar untuk kelas 7, menguji pemahaman visual konsep kesebangunan tanpa beban hitungan. |

Run 3 — solusi: Dua bangun dikatakan sebangun jika memiliki bentuk yang sama dan perbandingan sisi-sisi yang bersesuaian senilai. Pada cermin 'a', bayangan orang memiliki bentuk dan proporsi yang sama dengan benda aslinya, sehingga bayangan tersebut sebangun. Cermin 'b' dan 'c' menghasilkan bayangan yang terdistorsi (berubah proporsinya), sehingga tidak sebangun.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengenali konsep kesebangunan melalui pengamatan visual. Siswa perlu memahami definisi dasar kesebangunan (bentuk sama, proporsi terjaga) dan menerapkannya untuk mengidentifikasi gambar mana yang memenuhi kriteria tersebut tanpa melakukan perhitungan matematis yang kompleks.. Bukti: Cermin manakah yang menghasilkan bayangan yang sebangun dengan benda asalnya?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang apa arti 'sebangun' dalam konteks geometri visual, bukan sekadar menghafal fakta atau melakukan prosedur perhitungan.. Bukti: Cermin manakah yang menghasilkan bayangan yang sebangun dengan benda asalnya?
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu melakukan pengamatan visual langsung untuk membandingkan proporsi antara objek asli dan bayangannya. Tidak ada perhitungan, perencanaan langkah, atau integrasi konsep yang rumit yang diperlukan.. Bukti: Cermin manakah yang menghasilkan bayangan yang sebangun dengan benda asalnya?

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
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu membedakan bentuk yang proporsional dan terdistorsi secara visual sebagai pengenalan awal terhadap konsep kesebangunan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `5064`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta siswa untuk mengenali konsep kesebangunan melalui pengamatan visual. Siswa perlu memahami definisi dasar kesebangunan (bentuk sama, proporsi terjaga) dan menerapkannya untuk mengidentifikasi gambar mana yang memenuhi kriteria tersebut tanpa melakukan perhitungan matematis yang kompleks.
- Dimensi pengetahuan `conceptual`: Siswa harus memahami konsep konseptual tentang apa itu kesebangunan (proporsionalitas bentuk) untuk membedakan antara bayangan yang sebangun dan yang terdistorsi.
- Intended difficulty `Easy`: Soal ini bersifat intuitif dan langsung. Siswa hanya perlu membandingkan bentuk visual antara objek asli dan bayangan untuk menentukan mana yang mempertahankan proporsi. Tidak ada perhitungan atau langkah kompleks yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk dan proporsi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini menguji pemahaman konseptual dasar tentang kesebangunan melalui pengamatan visual, yang sesuai dengan tingkat kognitif kelas 7. |

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
Transkripsi visual: Terdapat tiga cermin yang diberi label a, b, dan c. Cermin a menampilkan bayangan orang yang proporsinya sama dengan orang aslinya. Cermin b menampilkan bayangan orang yang tampak lebih kurus atau memanjang (terdistorsi). Cermin c menampilkan bayangan orang yang tampak lebih lebar atau pendek (terdistorsi).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 33. Soal `78652b4108bd747c96b2f4a8`

Pada $\triangle ABC$, $AD$ membagi $\angle A$ menjadi dua bagian yang sama besar. $AD$ disebut garis bagi. Titik $D$ terletak pada sisi $BC$. Petunjuk: Hitung garis yang sejajar dengan $AD$ dan melalui titik $C$. Garis ini berpotongan dengan perpanjangan $AB$ di titik $E$.<br><br> $\triangle ACE$ sama kaki. Manakah sisi-sisi yang sama panjang.

| Opsi | Isi |
|---|---|
| A | AC = AE, karena ∠ACE = ∠AEC |
| B | AE = CE, karena ∠ACE = ∠CAE |
| C | AC = CE, karena ∠CAE = ∠AEC |
| D | AB = AC, karena AD garis bagi |

![Gambar sumber soal 33](<../../../images/kelas7_crop-p0205-garis-bagi.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Misalkan garis CE sejajar AD. Karena AD \|\| CE, maka ∠BAD = ∠AEC (sudut sehadap) dan ∠DAC = ∠ACE (sudut dalam berseberangan). Karena AD adalah pembagi sudut, ∠BAD = ∠DAC. Maka ∠AEC = ∠ACE. Dalam segitiga ACE, karena dua sudut alasnya sama, maka sisi di hadapannya sama panjang, yaitu AC = AE.
Gambar sumber: images/kelas7_crop-p0205-garis-bagi.png. Transkripsi visual: Segitiga ABC dengan garis AD sebagai pembagi sudut A menjadi dua bagian sama besar (ditandai dengan busur hijau). Titik D terletak pada ruas garis BC.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e8e757055b2d8c67c705faf1e792a843e9cf79a2994495fc6fed85b2b60f9960`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Hard | 3729 |
| 2 | success | valid / verified | reasoning | conceptual | Hard | 3728 |
| 3 | success | valid / verified | reasoning | conceptual | Hard | 3687 |

Run 1 — solusi: Misalkan garis CE sejajar AD. Karena AD \|\| CE, maka ∠BAD = ∠AEC (sudut sehadap) dan ∠DAC = ∠ACE (sudut dalam berseberangan). Karena AD adalah pembagi sudut, ∠BAD = ∠DAC. Maka ∠AEC = ∠ACE. Dalam segitiga ACE, karena dua sudut alasnya sama, maka sisi di hadapannya sama panjang, yaitu AC = AE.
- Domain kognitif `classify/reasoning`: Soal ini meminta siswa untuk melakukan penalaran deduktif berdasarkan konstruksi geometri yang diberikan. Siswa harus menghubungkan sifat garis sejajar (sudut sehadap dan berseberangan) dengan sifat segitiga sama kaki untuk menyimpulkan hubungan panjang sisi. Ini melampaui sekadar menerapkan rumus.. Bukti: Petunjuk: Hitung garis yang sejajar dengan AD dan melalui titik C. Garis ini berpotongan dengan perpanjangan AB di titik E.; ΔACE sama kaki. Manakah sisi-sisi yang sama panjang.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep hubungan sudut pada garis sejajar (sudut sehadap, sudut dalam berseberangan) dan konsep segitiga sama kaki untuk membangun argumen logis.. Bukti: AD membagi ∠A menjadi dua bagian yang sama besar.; Garis yang sejajar dengan AD dan melalui titik C.; ΔACE sama kaki.
- Intended difficulty `classify/Hard`: Soal ini tergolong Hard untuk kelas 7 karena menuntut kemampuan melakukan konstruksi mental (atau visualisasi) berdasarkan petunjuk, serta mengintegrasikan beberapa konsep geometri (garis sejajar, sudut, segitiga sama kaki) untuk membuktikan hubungan sisi. Meskipun petunjuk diberikan, siswa harus mampu mengaitkan hubungan sudut-sudut tersebut secara mandiri untuk mencapai kesimpulan.. Bukti: Petunjuk: Hitung garis yang sejajar dengan AD dan melalui titik C. Garis ini berpotongan dengan perpanjangan AB di titik E.; ΔACE sama kaki.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang sudut sehadap, sudut dalam berseberangan, dan sifat segitiga sama kaki. |
| dependentSteps | 4 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 3 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun topiknya ada di kurikulum, pembuktian geometri melalui konstruksi garis bantu jarang menjadi rutinitas di kelas 7. Tuntutan untuk mengintegrasikan sifat garis sejajar dan segitiga sama kaki secara deduktif menjadikannya tantangan tinggi. |

Run 2 — solusi: Karena CE sejajar AD, maka sudut AEC = sudut BAD (sehadap) dan sudut ACE = sudut DAC (berseberangan dalam). Karena AD adalah garis bagi, maka sudut BAD = sudut DAC. Akibatnya, sudut AEC = sudut ACE. Dalam segitiga ACE, karena dua sudut alasnya sama, maka segitiga tersebut sama kaki dengan sisi AC = AE.
- Domain kognitif `classify/reasoning`: Soal ini menuntut siswa untuk melakukan penalaran geometris dengan mengintegrasikan hubungan sudut (sehadap dan berseberangan dalam) yang terbentuk dari garis sejajar dan transversal, serta menghubungkannya dengan sifat segitiga sama kaki. Ini melampaui sekadar penerapan prosedur rutin.. Bukti: AD membagi ∠A menjadi dua bagian yang sama besar; Hitung garis yang sejajar dengan AD dan melalui titik C; ΔACE sama kaki. Manakah sisi-sisi yang sama panjang
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip-prinsip geometri tentang garis sejajar, hubungan sudut, dan sifat segitiga sama kaki untuk membangun argumen logis.. Bukti: AD membagi ∠A menjadi dua bagian yang sama besar; Garis yang sejajar dengan AD dan melalui titik C; ΔACE sama kaki
- Intended difficulty `classify/Hard`: Soal ini dikategorikan Hard untuk kelas 7 karena menuntut perencanaan langkah-langkah pembuktian geometris yang tidak langsung. Siswa harus mengonstruksi pemahaman tentang hubungan sudut (sehadap, berseberangan) yang melibatkan garis bantu (ekstensi AB dan garis sejajar AD), serta mengintegrasikan konsep tersebut untuk menyimpulkan sifat segitiga sama kaki. Tingkat abstraksi dan integrasi konsep geometri ini cukup tinggi bagi siswa kelas 7.. Bukti: Hitung garis yang sejajar dengan AD dan melalui titik C; Garis ini berpotongan dengan perpanjangan AB di titik E; ΔACE sama kaki

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat sudut pada garis sejajar (sehadap, berseberangan dalam) dan sifat dasar segitiga sama kaki. |
| dependentSteps | 4 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 3 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materinya adalah geometri dasar, kemampuan untuk melakukan pembuktian atau derivasi langkah demi langkah dengan garis bantu (konstruksi) jarang diajarkan secara mendalam di kelas 7, sehingga menuntut kemampuan penalaran yang lebih tinggi dari rata-rata kurikulum. |

Run 3 — solusi: Misalkan garis CE sejajar AD dengan E pada perpanjangan AB. Sudut AEC = sudut BAD (sehadap) dan sudut ACE = sudut DAC (berseberangan dalam). Karena AD membagi sudut A sama besar (sudut BAD = sudut DAC), maka sudut AEC = sudut ACE. Segitiga ACE adalah segitiga sama kaki dengan AC = AE.
- Domain kognitif `classify/reasoning`: Soal ini menuntut siswa untuk melakukan penalaran geometris dengan menerapkan konsep garis sejajar dan sudut-sudut yang terbentuk (sehadap dan berseberangan dalam) untuk membuktikan sifat segitiga sama kaki. Ini melampaui sekadar mengingat fakta atau menerapkan prosedur rutin.. Bukti: Petunjuk: Hitung garis yang sejajar dengan AD dan melalui titik C. Garis ini berpotongan dengan perpanjangan AB di titik E.; ΔACE sama kaki. Manakah sisi-sisi yang sama panjang.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara garis sejajar, sudut yang terbentuk, dan sifat segitiga sama kaki. Ini melibatkan pemahaman prinsip-prinsip geometris (konseptual) untuk membangun argumen logis.. Bukti: AD membagi ∠A menjadi dua bagian yang sama besar.; Garis yang sejajar dengan AD dan melalui titik C.
- Intended difficulty `classify/Hard`: Soal ini dikategorikan Hard untuk kelas 7 karena menuntut kemampuan konstruksi geometris (membuat garis bantu) dan integrasi konsep garis sejajar dengan sifat segitiga sama kaki. Siswa harus merencanakan langkah-langkah pembuktian yang saling bergantung tanpa bantuan prosedur yang sudah familiar.. Bukti: Petunjuk: Hitung garis yang sejajar dengan AD dan melalui titik C. Garis ini berpotongan dengan perpanjangan AB di titik E.; ΔACE sama kaki.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat sudut pada garis sejajar (sehadap, berseberangan dalam) dan definisi segitiga sama kaki. |
| dependentSteps | 4 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 3 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun topiknya adalah kesebangunan/segitiga, menuntut siswa melakukan konstruksi garis bantu dan melakukan pembuktian deduktif sederhana adalah tantangan kognitif yang tinggi untuk level kelas 7. |

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
Transkripsi visual: Segitiga ABC dengan garis AD sebagai pembagi sudut A menjadi dua bagian sama besar (ditandai dengan busur hijau). Titik D terletak pada ruas garis BC.
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

![Gambar sumber soal 34](<../../../images/kelas7_crop-p0201-segitiga-abc-d.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Definisi kesebangunan dua bangun datar adalah bangun-bangun yang memiliki bentuk yang sama, di mana sudut-sudut yang berpadanan sama besar dan sisi-sisi yang berpadanan memiliki perbandingan yang senilai.
Gambar sumber: images/kelas7_crop-p0201-segitiga-abc-d.png. Transkripsi visual: Gambar menunjukkan segitiga ABC dengan titik D terletak pada ruas garis AB. Tidak ada titik E yang digambarkan pada sisi AC.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `02b0cc6e999c85c88e5e82af9b0bf2a1e244e12ceb81acf0ebe5a62d8f3b0bd1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3491 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3538 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 3590 |

Run 1 — solusi: Definisi kesebangunan dua bangun datar adalah bangun-bangun yang memiliki bentuk yang sama, di mana sudut-sudut yang berpadanan sama besar dan sisi-sisi yang berpadanan memiliki perbandingan yang senilai.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengingat dan menerapkan definisi dasar dari konsep kesebangunan, yaitu kesamaan besar sudut pada bangun yang sebangun.. Bukti: Pada dua segitiga yang sebangun, sudut-sudut yang berpadanan besarnya ....
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman terhadap prinsip atau definisi konseptual mengenai sifat kesebangunan segitiga.. Bukti: Pada dua segitiga yang sebangun, sudut-sudut yang berpadanan besarnya ....
- Intended difficulty `classify/Easy`: Soal ini bersifat recall atau pemahaman dasar mengenai definisi kesebangunan. Tidak ada langkah perhitungan atau integrasi konsep yang kompleks yang diperlukan.. Bukti: Pada dua segitiga yang sebangun, sudut-sudut yang berpadanan besarnya ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang definisi kesebangunan bangun datar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan pertanyaan teoretis dasar yang sesuai untuk level kelas 7 saat mempelajari topik kesebangunan. |

Run 2 — solusi: Definisi kesebangunan dua bangun datar menyatakan bahwa sudut-sudut yang berpadanan pada kedua bangun tersebut memiliki besar yang sama, sedangkan sisi-sisi yang berpadanan memiliki perbandingan yang senilai.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengingat dan menerapkan definisi dasar dari konsep kesebangunan segitiga. Tidak ada perhitungan atau analisis strategi yang kompleks yang diperlukan, hanya pemahaman konseptual dasar.. Bukti: Pada dua segitiga yang sebangun, sudut-sudut yang berpadanan besarnya ....
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa mengenai prinsip atau definisi dasar (konsep) dari kesebangunan, yaitu kesamaan sudut-sudut yang berpadanan.. Bukti: Pada dua segitiga yang sebangun, sudut-sudut yang berpadanan besarnya ....
- Intended difficulty `classify/Easy`: Soal ini bersifat sangat mendasar dan langsung menguji definisi kesebangunan. Tidak ada langkah-langkah yang harus direncanakan atau kendala yang perlu diintegrasikan. Siswa hanya perlu mengetahui sifat dasar segitiga sebangun.. Bukti: Pada dua segitiga yang sebangun, sudut-sudut yang berpadanan besarnya ....

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
| distractorQuality | weak |
| gradeRelativeRationale | Soal ini adalah pertanyaan teoretis langsung yang sesuai dengan tingkat kognitif kelas 7 untuk topik kesebangunan, di mana siswa diharapkan memahami sifat-sifat dasar bangun yang sebangun. |

Run 3 — solusi: Definisi kesebangunan segitiga menyatakan bahwa dua segitiga dikatakan sebangun jika sudut-sudut yang berpadanan sama besar dan sisi-sisi yang berpadanan memiliki perbandingan yang sama. Oleh karena itu, sudut-sudut yang berpadanan pada dua segitiga yang sebangun adalah sama besar.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengingat dan menerapkan definisi dasar atau sifat fundamental dari kesebangunan segitiga. Tidak ada proses analisis kompleks atau pemecahan masalah non-rutin yang diperlukan.. Bukti: Pada dua segitiga yang sebangun, sudut-sudut yang berpadanan besarnya ....
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual mengenai sifat dasar kesebangunan (sudut-sudut yang berpadanan sama besar), yang merupakan prinsip utama dalam topik kesebangunan.. Bukti: Pada dua segitiga yang sebangun, sudut-sudut yang berpadanan besarnya ....
- Intended difficulty `classify/Easy`: Soal ini bersifat sangat mendasar (recall) mengenai definisi kesebangunan. Tidak ada langkah perhitungan atau integrasi konsep yang diperlukan.. Bukti: Pada dua segitiga yang sebangun, sudut-sudut yang berpadanan besarnya ....

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
| gradeRelativeRationale | Soal ini hanya menanyakan definisi atau sifat dasar yang diajarkan di awal topik kesebangunan kelas 7, sehingga tingkat kesulitannya rendah. |

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
Transkripsi visual: Gambar menunjukkan segitiga ABC dengan titik D terletak pada ruas garis AB. Tidak ada titik E yang digambarkan pada sisi AC.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: Kalimat 'hitunglah ΔADE yang sebangun dengan ΔABC' dalam soal kurang tepat secara matematis karena konteksnya adalah pernyataan sifat kesebangunan, bukan perhitungan nilai numerik.; Kalimat 'hitunglah ΔADE yang sebangun dengan ΔABC' dalam soal kurang tepat secara matematis karena tidak ada nilai numerik yang diminta untuk dihitung; seharusnya kalimat tersebut berupa instruksi untuk mengidentifikasi atau menyatakan sifat kesebangunan..
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

![Gambar sumber soal 35](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0206-05.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Sudut dalam segi lima beraturan adalah (5-2)x180/5 = 108 derajat. Sudut persegi adalah 90 derajat. Pada titik pertemuan, sudut potongan = 360 - (108 + 108 + 90) = 360 - 306 = 54 derajat.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0206-05.png. Transkripsi visual: Pola 1 menunjukkan sebuah persegi biru di tengah yang dikelilingi oleh empat segi lima beraturan merah. Terdapat celah di antara dua segi lima beraturan yang bersebelahan dan sudut persegi biru. Sudut dalam segi lima beraturan adalah 108 derajat dan sudut persegi adalah 90 derajat. Titik pertemuan di celah tersebut membentuk sudut satu putaran penuh (360 derajat).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3825e60f3d7363bc7d7692f9544592aa35b3201f5216bb66dc1216d2317febd1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 3760 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3770 |
| 3 | success | valid / verified | applying | conceptual | Medium | 3777 |

Run 1 — solusi: Sudut dalam segi lima beraturan adalah (5-2)x180/5 = 108 derajat. Sudut persegi adalah 90 derajat. Pada titik pertemuan, sudut potongan = 360 - (108 + 108 + 90) = 360 - 306 = 54 derajat.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan pengetahuan tentang sudut dalam poligon beraturan (segi lima) dan persegi, serta memahami hubungan sudut pada satu titik (sudut satu putaran penuh) untuk menentukan sudut yang hilang. Ini melibatkan penerapan konsep geometri pada situasi baru (pola keramik).. Bukti: Berapa besar sudut potongan keramik untuk Pola 1?; Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman konseptual tentang sifat-sifat poligon (jumlah sudut dalam) dan hubungan antar sudut yang bertemu pada satu titik.. Bukti: Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.; Berapa besar sudut potongan keramik untuk Pola 1?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus mengidentifikasi dan mengintegrasikan beberapa informasi (sudut segi lima, sudut persegi, dan sudut satu putaran penuh) untuk menyelesaikan masalah. Meskipun prosedurnya familiar, siswa perlu merencanakan langkah-langkah secara mandiri tanpa bantuan eksplisit mengenai rumus sudut poligon.. Bukti: Berapa besar sudut potongan keramik untuk Pola 1?; Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengetahuan tentang jumlah sudut dalam poligon dan sudut satu putaran penuh (360 derajat). |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu menghitung sudut dalam poligon dan memahami hubungan sudut pada titik pertemuan. Soal ini menuntut integrasi konsep tersebut dalam konteks visual yang sedikit lebih kompleks daripada sekadar menghitung sudut poligon secara terpisah. |

Run 2 — solusi: Sudut dalam segi lima beraturan adalah (5-2)x180/5 = 108 derajat. Sudut persegi adalah 90 derajat. Pada titik pertemuan di Pola 1, terdapat satu sudut persegi (90 derajat) dan dua sudut segi lima (108 derajat dan 108 derajat). Sudut potongan yang diperlukan adalah 360 - (90 + 108 + 108) = 360 - 306 = 54 derajat.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan pengetahuan tentang sudut dalam poligon (segi lima dan persegi) dan memahami geometri sudut pada satu titik (sudut satu putaran penuh) untuk menentukan sudut yang hilang. Ini melibatkan penerapan konsep pada situasi geometris yang baru.. Bukti: Berapa besar sudut potongan keramik untuk Pola 1?; Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang sifat-sifat sudut dalam poligon beraturan dan bagaimana mereka berinteraksi dalam susunan geometris.. Bukti: Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus mengidentifikasi dan mengintegrasikan beberapa informasi (sudut segi lima, sudut persegi, dan sudut satu putaran penuh) untuk menyelesaikan masalah. Meskipun prosedurnya familiar, siswa perlu merencanakan langkah-langkah yang saling bergantung tanpa bantuan eksplisit tentang bagaimana sudut-sudut tersebut berinteraksi di titik pertemuan.. Bukti: Berapa besar sudut potongan keramik untuk Pola 1?; Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang sudut dalam poligon beraturan dan sudut satu putaran penuh (360 derajat). |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu menghitung sudut dalam poligon dan memahami hubungan sudut pada titik pertemuan. Soal ini menuntut integrasi konsep tersebut dalam konteks visual yang sedikit lebih kompleks daripada sekadar menghitung sudut poligon secara terisolasi. |

Run 3 — solusi: Sudut dalam segi lima beraturan = 108 derajat. Sudut persegi = 90 derajat. Sudut potongan = 360 - (108 + 108 + 90) = 360 - 306 = 54 derajat.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi hubungan geometris di sekitar titik pertemuan (sudut satu putaran penuh) dan menerapkan pengetahuan tentang besar sudut dalam poligon beraturan (segi lima dan persegi) untuk menyelesaikan masalah.. Bukti: Berapa besar sudut potongan keramik untuk Pola 1?; Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman konseptual tentang sifat-sifat sudut dalam poligon beraturan dan bagaimana mereka berinteraksi dalam susunan geometris (tessellation sederhana).. Bukti: Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.; Berapa besar sudut potongan keramik untuk Pola 1?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus mengintegrasikan pengetahuan tentang sudut dalam poligon (segi lima dan persegi) dan memahami hubungan sudut di sekitar titik pertemuan (360 derajat). Meskipun prosedurnya standar, siswa perlu merencanakan langkah-langkah untuk mengidentifikasi sudut-sudut yang mengelilingi celah tersebut tanpa bantuan eksplisit mengenai rumus sudut poligon.. Bukti: Berapa besar sudut potongan keramik untuk Pola 1?; Keramik merah berbentuk segi lima beraturan, keramik biru berbentuk persegi.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengetahuan tentang besar sudut dalam segi lima beraturan (108 derajat) dan persegi (90 derajat), serta konsep sudut satu putaran penuh (360 derajat). |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 3 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan memahami sudut poligon dan sudut pada titik pertemuan. Soal ini menuntut integrasi beberapa informasi geometris yang tidak diberikan secara langsung dalam satu langkah, sehingga berada di tingkat Medium. |

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
Transkripsi visual: Pola 1 menunjukkan sebuah persegi biru di tengah yang dikelilingi oleh empat segi lima beraturan merah. Terdapat celah di antara dua segi lima beraturan yang bersebelahan dan sudut persegi biru. Sudut dalam segi lima beraturan adalah 108 derajat dan sudut persegi adalah 90 derajat. Titik pertemuan di celah tersebut membentuk sudut satu putaran penuh (360 derajat).
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
Solusi minimum hasil AI: Definisi belah ketupat adalah segiempat dengan empat sisi sama panjang. Jajargenjang hanya mensyaratkan sisi berhadapan sejajar dan sama panjang, namun tidak mensyaratkan keempat sisinya sama panjang. Oleh karena itu, tidak semua jajargenjang adalah belah ketupat.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `124164280367131dceb39dd05795a6832fbe7027bf2f1050a452446a30674f61`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Medium | 2488 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 2495 |
| 3 | success | valid / verified | reasoning | conceptual | Medium | 2450 |

Run 1 — solusi: Definisi belah ketupat adalah segiempat dengan empat sisi sama panjang. Jajargenjang hanya mensyaratkan sisi berhadapan sejajar dan sama panjang, namun tidak mensyaratkan keempat sisinya sama panjang. Oleh karena itu, tidak semua jajargenjang adalah belah ketupat.
- Domain kognitif `classify/reasoning`: Soal ini menuntut siswa untuk memahami hubungan hierarkis antara bangun datar (klasifikasi inklusif) dan membedakan sifat-sifat yang menjadi syarat cukup bagi suatu bangun. Siswa harus menerapkan pemahaman konsep sifat bangun datar untuk mengevaluasi pernyataan logis.. Bukti: apakah sembarang jajargenjang boleh disebut belah ketupat?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang definisi dan hubungan antar kategori bangun datar (konseptual), bukan sekadar menghafal fakta atau melakukan prosedur hitung.. Bukti: sembarang bentuk belah ketupat boleh disebut jajargenjang; apakah sembarang jajargenjang boleh disebut belah ketupat?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena menuntut pemahaman konseptual yang mendalam tentang sifat-sifat bangun datar. Siswa tidak bisa hanya mengandalkan prosedur rutin, melainkan harus membandingkan syarat definisi (sisi sama panjang) antara dua bangun. Meskipun konsepnya mendasar, kemampuan untuk menolak generalisasi yang salah (bahwa hubungan inklusi berlaku dua arah) memerlukan penalaran yang lebih dari sekadar pengenalan fakta.. Bukti: apakah sembarang jajargenjang boleh disebut belah ketupat?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman definisi dan sifat-sifat jajargenjang dan belah ketupat. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 7, membedakan sifat bangun datar dalam hierarki inklusi adalah materi standar, namun sering menjadi miskonsepsi. Soal ini menuntut pemahaman konsep yang lebih dari sekadar identifikasi visual. |

Run 2 — solusi: Definisi belah ketupat adalah jajargenjang dengan empat sisi sama panjang. Jajargenjang secara umum hanya mensyaratkan sisi berhadapan sejajar dan sama panjang, tidak harus keempat sisinya sama panjang. Oleh karena itu, tidak semua jajargenjang adalah belah ketupat.
- Domain kognitif `classify/reasoning`: Soal ini menuntut siswa untuk memahami hubungan hierarkis antara konsep belah ketupat dan jajargenjang. Siswa harus membedakan syarat perlu dan syarat cukup dari definisi bangun datar tersebut, yang merupakan aktivitas penalaran konseptual.. Bukti: apakah sembarang jajargenjang boleh disebut belah ketupat?; jajargenjang tidak harus memiliki empat sisi yang sama panjang
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang definisi dan klasifikasi bangun datar (konsep), bukan sekadar menghafal fakta atau melakukan prosedur perhitungan.. Bukti: sembarang bentuk belah ketupat boleh disebut jajargenjang; jajargenjang tidak harus memiliki empat sisi yang sama panjang
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena menuntut pemahaman konsep klasifikasi bangun datar yang sering disalahpahami siswa. Meskipun langkah penyelesaiannya singkat, siswa harus mampu membedakan sifat-sifat yang membatasi (empat sisi sama panjang) antara dua bangun yang memiliki kemiripan sifat dasar (sisi sejajar).. Bukti: Kalau sembarang bentuk belah ketupat boleh disebut jajargenjang, apakah sembarang jajargenjang boleh disebut belah ketupat?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman definisi dan sifat-sifat jajargenjang dan belah ketupat. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sering mengalami miskonsepsi dalam klasifikasi bangun datar. Soal ini menguji pemahaman mendalam tentang definisi, bukan sekadar identifikasi visual, sehingga menuntut penalaran yang lebih dari sekadar pengenalan fakta dasar. |

Run 3 — solusi: Definisi belah ketupat adalah jajargenjang dengan empat sisi sama panjang. Jajargenjang umum tidak harus memiliki empat sisi sama panjang, sehingga tidak semua jajargenjang adalah belah ketupat.
- Domain kognitif `classify/reasoning`: Soal menuntut siswa untuk memahami hubungan hierarkis antara dua bangun datar (belah ketupat dan jajargenjang) dan menerapkan definisi sifat-sifat bangun tersebut untuk menarik kesimpulan logis.. Bukti: apakah sembarang jajargenjang boleh disebut belah ketupat?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep dan hubungan antar kategori bangun datar (hierarki klasifikasi geometri), bukan sekadar menghafal fakta atau prosedur hitung.. Bukti: sembarang bentuk belah ketupat boleh disebut jajargenjang; jajargenjang tidak harus memiliki empat sisi yang sama panjang
- Intended difficulty `classify/Medium`: Soal ini menguji pemahaman konseptual tentang klasifikasi bangun datar. Siswa harus membedakan sifat yang dimiliki oleh semua jajargenjang dengan sifat khusus yang hanya dimiliki belah ketupat. Meskipun konsepnya mendasar, ini memerlukan penalaran tentang inklusi himpunan yang sering disalahpahami siswa.. Bukti: Kalau sembarang bentuk belah ketupat boleh disebut jajargenjang, apakah sembarang jajargenjang boleh disebut belah ketupat?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman sifat-sifat dasar jajargenjang dan belah ketupat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 7, memahami hierarki bangun datar (bahwa belah ketupat adalah subset dari jajargenjang) adalah materi standar, namun kemampuan untuk membalikkan logika tersebut (apakah berlaku sebaliknya) merupakan tantangan konseptual yang umum di tingkat ini. |

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

![Gambar sumber soal 37](<../../../images/kelas7_panduan_siswa_kelas7.pdf-0213-07.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Nama 'Rahma Kusni' memiliki 10 huruf (R-a-h-m-a-K-u-s-n-i). Pada line plot, kolom 10 memiliki 3 tanda X. Karena Rahma adalah salah satunya, maka teman yang memiliki panjang nama sama adalah 3 - 1 = 2 orang. Panjang nama dua kali Rahma adalah 10 * 2 = 20 huruf. Pada kolom 20, terdapat 3 tanda X, sehingga ada 3 siswa.
Gambar sumber: images/kelas7_panduan_siswa_kelas7.pdf-0213-07.png. Transkripsi visual: Line plot menunjukkan frekuensi panjang nama siswa. Sumbu horizontal (6-32) adalah banyaknya huruf. Kolom 10 memiliki 3 tanda X. Kolom 20 memiliki 3 tanda X.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `782644db36c4bfeaa76f8a50921da3329f5a1f8a137eeb426b868d0ac5bbcb6d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3735 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3792 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3881 |

Run 1 — solusi: Nama 'Rahma Kusni' memiliki 10 huruf (R-a-h-m-a-K-u-s-n-i). Pada line plot, kolom 10 memiliki 3 tanda X. Karena Rahma adalah salah satunya, maka teman yang memiliki panjang nama sama adalah 3 - 1 = 2 orang. Panjang nama dua kali Rahma adalah 10 * 2 = 20 huruf. Pada kolom 20, terdapat 3 tanda X, sehingga ada 3 siswa.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk menginterpretasikan data dari line plot, melakukan operasi hitung sederhana (menghitung jumlah X dan perkalian), serta memahami konteks 'teman' (mengurangi diri sendiri dari total frekuensi). Ini adalah penerapan konsep statistik dasar pada konteks yang diberikan.. Bukti: Jika Rahma Kusni adalah siswa kelas 7A, maka berapakah teman Rahma yang memiliki nama yang sama panjang dengannya?; Ada berapa banyak siswa di kelas 7A yang memiliki panjang nama dua kali dari nama Rahma?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami cara membaca dan menginterpretasikan representasi data berupa line plot (konsep statistik dasar).. Bukti: Line plot di bawah ini yang menunjukkan banyaknya huruf di nama siswa-siswa kelas 7A
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena jalur penyelesaian sangat jelas: menghitung jumlah X pada kolom tertentu dan melakukan operasi perkalian dasar. Tidak ada kendala yang saling berinteraksi atau kebutuhan untuk merencanakan strategi kompleks. Siswa hanya perlu membaca data secara akurat.. Bukti: Jika Rahma Kusni adalah siswa kelas 7A, maka berapakah teman Rahma yang memiliki nama yang sama panjang dengannya?; Ada berapa banyak siswa di kelas 7A yang memiliki panjang nama dua kali dari nama Rahma?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca data pada line plot dan operasi hitung dasar (perkalian dan pengurangan). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan latihan standar dalam membaca grafik/diagram untuk kelas 7. Tidak ada tuntutan kognitif tinggi selain ketelitian membaca data. |

Run 2 — solusi: Rahma Kusni has 10 letters (R-a-h-m-a-K-u-s-n-i). On the line plot, column 10 has 3 X's. Since Rahma is one of them, the number of friends with the same length is 3 - 1 = 2. Twice the length of Rahma's name is 10 * 2 = 20. Column 20 has 3 X's. Therefore, 2 friends and 3 students.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi nilai (panjang nama Rahma), membaca data dari representasi visual (line plot), melakukan operasi aritmatika sederhana (pengurangan untuk mencari 'teman' dan perkalian untuk mencari 'dua kali'), serta menginterpretasikan konteks soal (Rahma tidak dihitung sebagai temannya sendiri). Ini adalah penerapan konsep statistik dasar pada konteks rutin.. Bukti: Jika Rahma Kusni adalah siswa kelas 7A, maka berapakah teman Rahma yang memiliki nama yang sama panjang dengannya?; Ada berapa banyak siswa di kelas 7A yang memiliki panjang nama dua kali dari nama Rahma?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang cara membaca dan menginterpretasikan data dari diagram (line plot), yang merupakan pengetahuan konseptual dalam statistika.. Bukti: Line plot di bawah ini yang menunjukkan banyaknya huruf di nama siswa-siswa kelas 7A
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena jalur penyelesaiannya sangat jelas dan langsung. Siswa hanya perlu menghitung jumlah huruf pada nama 'Rahma Kusni', membaca frekuensi pada kolom 10 dan 20 di line plot, serta melakukan operasi aritmatika dasar. Tidak ada kendala yang saling berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: Jika Rahma Kusni adalah siswa kelas 7A, maka berapakah teman Rahma yang memiliki nama yang sama panjang dengannya?; Ada berapa banyak siswa di kelas 7A yang memiliki panjang nama dua kali dari nama Rahma?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung jumlah huruf dalam kata dan membaca frekuensi data pada line plot. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas membaca line plot dan melakukan operasi aritmatika dasar adalah kompetensi standar untuk kelas 7. Soal tidak menuntut analisis data yang mendalam atau interpretasi statistik yang kompleks. |

Run 3 — solusi: Nama 'Rahma Kusni' memiliki 10 huruf (R-a-h-m-a-K-u-s-n-i). Pada line plot, kolom 10 memiliki 3 tanda X. Karena Rahma adalah salah satunya, maka jumlah temannya adalah 3 - 1 = 2 siswa. Panjang nama dua kali Rahma adalah 2 x 10 = 20 huruf. Pada kolom 20, terdapat 3 tanda X. Jadi, jawabannya adalah 2 teman dan 3 siswa.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi data dari representasi visual (line plot), melakukan operasi hitung sederhana (menghitung jumlah X dan perkalian), serta memahami konteks 'teman' (mengurangi total dengan diri sendiri). Ini adalah penerapan konsep statistik dasar pada konteks rutin.. Bukti: Jika Rahma Kusni adalah siswa kelas 7A, maka berapakah teman Rahma yang memiliki nama yang sama panjang dengannya?; Ada berapa banyak siswa di kelas 7A yang memiliki panjang nama dua kali dari nama Rahma?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang cara membaca dan menginterpretasikan data yang disajikan dalam bentuk line plot, yang merupakan pengetahuan konseptual dalam statistika.. Bukti: Line plot di bawah ini yang menunjukkan banyaknya huruf di nama siswa-siswa kelas 7A
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu melakukan pembacaan data langsung dari grafik dan operasi aritmatika dasar. Tidak ada integrasi konsep yang kompleks atau perencanaan strategi yang rumit.. Bukti: Jika Rahma Kusni adalah siswa kelas 7A, maka berapakah teman Rahma yang memiliki nama yang sama panjang dengannya?; Ada berapa banyak siswa di kelas 7A yang memiliki panjang nama dua kali dari nama Rahma?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca grafik sederhana (line plot) dan operasi hitung dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah familiar dengan penyajian data sederhana. Tugas ini hanya memerlukan ketelitian membaca grafik dan logika dasar pengurangan 'diri sendiri' dari total kelompok. |

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
Transkripsi visual: Line plot menunjukkan frekuensi panjang nama siswa. Sumbu horizontal (6-32) adalah banyaknya huruf. Kolom 10 memiliki 3 tanda X. Kolom 20 memiliki 3 tanda X.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: Soal meminta jumlah teman yang memiliki panjang nama sama dengan Rahma Kusni (10 huruf). Pada kolom 10, terdapat 3 tanda X. Jika Rahma adalah salah satu dari 3 siswa tersebut, maka jumlah temannya adalah 3 - 1 = 2. Kunci jawaban C menyatakan 2 teman, yang konsisten dengan logika ini.; Soal meminta jumlah siswa dengan panjang nama dua kali Rahma (2 x 10 = 20 huruf). Pada kolom 20, terdapat 3 tanda X. Kunci jawaban C menyatakan 3 siswa, yang konsisten dengan data visual..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 38. Soal `9f164962fc74de3c9274b04f`

Jika seorang siswi bernama Metta Widyanti, artinya panjang namanya adalah 13 huruf karena terdiri dari 5 huruf untuk Metta dan 8 huruf untuk Widyanti.<br><br>Line plot di bawah ini yang menunjukkan banyaknya huruf di nama siswa-siswa kelas 7A di Sekolah Indonesia Raya.<br><br>Panjang Nama Siswa di Kelas 7A<br><br>Dari line plot di atas.<br><br>Ada berapa siswa di kelas 7A yang memiliki nama sama panjang dengan Metta Widyanti?

| Opsi | Isi |
|---|---|
| A | 6 siswa |
| B | 27 siswa |
| C | 13 siswa |
| D | 3 siswa |

![Gambar sumber soal 38](<../../../images/kelas7_panduan_siswa_kelas7.pdf-0213-07.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Hitung jumlah tanda 'X' yang berada tepat di atas angka 13 pada sumbu horizontal line plot. Terdapat 6 tanda 'X', yang berarti ada 6 siswa dengan panjang nama 13 huruf.
Gambar sumber: images/kelas7_panduan_siswa_kelas7.pdf-0213-07.png. Transkripsi visual: A line plot titled 'Panjang Nama Siswa di Kelas 7A' shows the number of letters in names on the horizontal axis (ranging from 6 to 32). The vertical axis represents the frequency of each length, marked by 'X' symbols. Specifically, above the number 13 on the horizontal axis, there is a column of 6 'X' symbols.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `409b71501d0a98524ddbca80783ca9238b512026571b30b60e60454bae0ec2cf`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 3566 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3556 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 3550 |

Run 1 — solusi: Identifikasi angka 13 pada sumbu horizontal line plot, kemudian hitung jumlah tanda X yang berada tepat di atas angka tersebut. Terdapat 6 tanda X, sehingga ada 6 siswa dengan panjang nama 13 huruf.
- Domain kognitif `classify/knowing`: Siswa diminta untuk membaca data dari representasi visual (line plot) dan melakukan ekstraksi informasi langsung tanpa perlu melakukan manipulasi atau analisis data yang kompleks.. Bukti: Ada berapa siswa di kelas 7A yang memiliki nama sama panjang dengan Metta Widyanti?; Line plot di bawah ini yang menunjukkan banyaknya huruf
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman siswa terhadap istilah dan cara membaca representasi data statistik dasar (line plot).. Bukti: Line plot di bawah ini yang menunjukkan banyaknya huruf
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena hanya memerlukan kemampuan membaca grafik secara langsung. Tidak ada langkah perantara atau integrasi konsep yang diperlukan.. Bukti: Ada berapa siswa di kelas 7A yang memiliki nama sama panjang dengan Metta Widyanti?; Line plot di bawah ini yang menunjukkan banyaknya huruf

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca grafik sederhana (line plot) dan menghitung objek. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah familiar dengan penyajian data sederhana. Soal ini hanya menuntut pembacaan data langsung tanpa proses analisis lebih lanjut. |

Run 2 — solusi: Identifikasi angka 13 pada sumbu horizontal, lalu hitung jumlah tanda X yang berada tepat di atas angka tersebut. Terdapat 6 tanda X.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk membaca data dari representasi visual (line plot) dan melakukan penghitungan langsung. Ini adalah prosedur rutin dalam membaca grafik.. Bukti: Ada berapa siswa di kelas 7A yang memiliki nama sama panjang dengan Metta Widyanti?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami cara kerja line plot sebagai representasi data statistik sederhana.. Bukti: Line plot di bawah ini yang menunjukkan banyaknya huruf di nama siswa-siswa kelas 7A
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mencari nilai 13 pada sumbu horizontal dan menghitung jumlah tanda X di atasnya. Tidak ada langkah perantara atau integrasi yang kompleks.. Bukti: Ada berapa siswa di kelas 7A yang memiliki nama sama panjang dengan Metta Widyanti?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca grafik sederhana (line plot) dan menghitung objek. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca line plot adalah materi dasar statistika kelas 7. Soal ini tidak menuntut analisis data lebih lanjut, hanya pembacaan data eksplisit. |

Run 3 — solusi: Identifikasi panjang nama Metta Widyanti (13 huruf). Pada line plot, hitung jumlah tanda X di kolom angka 13. Terdapat 6 tanda X, sehingga ada 6 siswa.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data dari representasi visual (line plot) dan melakukan penghitungan sederhana (counting) tanpa perlu manipulasi data lebih lanjut.. Bukti: Ada berapa siswa di kelas 7A yang memiliki nama sama panjang dengan Metta Widyanti?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang cara membaca dan menginterpretasikan data yang disajikan dalam bentuk line plot, yang merupakan konsep dasar statistika.. Bukti: Line plot di bawah ini yang menunjukkan banyaknya huruf di nama siswa-siswa kelas 7A
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mencari nilai 13 pada sumbu horizontal dan menghitung jumlah tanda X di atasnya. Tidak ada langkah perantara atau integrasi konsep yang kompleks.. Bukti: Ada berapa siswa di kelas 7A yang memiliki nama sama panjang dengan Metta Widyanti?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca grafik sederhana (line plot) dan menghitung objek. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca line plot adalah materi dasar statistika kelas 7. Tugas ini hanya memerlukan observasi visual langsung tanpa analisis data lebih dalam. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4950`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu melakukan ekstraksi data langsung dari representasi visual (line plot) dengan menghitung frekuensi (jumlah tanda X) untuk nilai tertentu. Tidak ada analisis atau manipulasi data yang diperlukan.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman dasar tentang cara membaca dan menginterpretasikan representasi data statistik sederhana (line plot).
- Intended difficulty `Easy`: Soal ini sangat langsung dan rutin. Siswa hanya perlu mengidentifikasi nilai 13 pada sumbu horizontal dan menghitung jumlah tanda X di atasnya. Tidak ada langkah perantara, integrasi konsep, atau kendala yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca grafik sederhana (line plot) dan menghitung objek. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca line plot adalah materi dasar statistika kelas 7. Soal ini hanya menuntut observasi visual langsung tanpa analisis data lebih lanjut. |

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
Transkripsi visual: A line plot titled 'Panjang Nama Siswa di Kelas 7A' shows the number of letters in names on the horizontal axis (ranging from 6 to 32). The vertical axis represents the frequency of each length, marked by 'X' symbols. Specifically, above the number 13 on the horizontal axis, there is a column of 6 'X' symbols.
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
| 1 | success | valid / verified | applying | conceptual | Easy | 2659 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2684 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2715 |

Run 1 — solusi: Jumlah siswa kelas 7B dapat ditentukan dengan menjumlahkan frekuensi pada Tabel 6.2 (Banyak Siswa), yaitu 1 + 3 + 7 + 10 + 8 + 2 + 1 = 32 siswa.
- Domain kognitif `classify/applying`: Siswa perlu memahami bahwa total populasi dalam data frekuensi dapat diperoleh dengan menjumlahkan seluruh frekuensi (banyak siswa) yang ada pada tabel tersebut. Ini adalah penerapan konsep dasar penyajian data.. Bukti: Tabel 6.2 Tabel Banyak Aplikasi Online; Berapakah jumlah siswa kelas 7B?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana data frekuensi disusun dan bagaimana total populasi direpresentasikan dalam tabel frekuensi.. Bukti: Tabel 6.2 Tabel Banyak Aplikasi Online; Berapakah jumlah siswa kelas 7B?
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu melakukan operasi penjumlahan sederhana dari nilai frekuensi yang sudah tersedia secara eksplisit dalam tabel. Tidak ada langkah rumit atau integrasi konsep yang kompleks.. Bukti: Tabel 6.2 Tabel Banyak Aplikasi Online; Berapakah jumlah siswa kelas 7B?

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
| gradeRelativeRationale | Siswa kelas 7 sudah terbiasa membaca tabel frekuensi sederhana dan menjumlahkan data untuk mencari total populasi. |

Run 2 — solusi: Jumlah siswa kelas 7B dapat ditentukan dengan menjumlahkan frekuensi pada Tabel 6.2 (Banyaknya aplikasi permainan online dalam gawai). Total siswa = 1 + 3 + 7 + 10 + 8 + 2 + 1 = 32 siswa.
- Domain kognitif `classify/applying`: Siswa diminta untuk menginterpretasikan tabel frekuensi dan memahami bahwa total frekuensi pada tabel yang mencakup seluruh populasi (banyaknya aplikasi per siswa) merepresentasikan total siswa.. Bukti: Tabel 6.2 Tabel Banyak Aplikasi Online; Berapakah jumlah siswa kelas 7B?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep tabel frekuensi sebagai representasi data populasi dan menerapkan prosedur penjumlahan untuk mendapatkan total data.. Bukti: Tabel 6.2 Tabel Banyak Aplikasi Online; Berapakah jumlah siswa kelas 7B?
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu memahami bahwa total frekuensi pada tabel yang mencakup seluruh responden (Tabel 6.2) adalah jumlah total siswa. Tidak ada langkah kompleks atau integrasi antar-tabel yang sulit; siswa hanya perlu memilih tabel yang tepat dan menjumlahkan nilainya.. Bukti: Tabel 6.2 Tabel Banyak Aplikasi Online; Berapakah jumlah siswa kelas 7B?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang tabel frekuensi dan penjumlahan bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu membaca tabel frekuensi sederhana dan memahami bahwa total frekuensi adalah total populasi. Soal ini merupakan penerapan langsung dari konsep tersebut. |

Run 3 — solusi: Jumlah siswa kelas 7B dapat ditentukan dengan menjumlahkan frekuensi pada Tabel 6.2 (Banyaknya aplikasi permainan online dalam gawai). Total siswa = 1 + 3 + 7 + 10 + 8 + 2 + 1 = 32 siswa.
- Domain kognitif `classify/applying`: Siswa perlu memahami bahwa tabel frekuensi menyajikan data jumlah siswa berdasarkan kategori tertentu. Untuk menjawab pertanyaan, siswa harus mengidentifikasi tabel yang mencakup seluruh populasi kelas (Tabel 6.2) dan menjumlahkan seluruh frekuensinya.. Bukti: Tabel 6.2 Tabel Banyak Aplikasi Online; Berapakah jumlah siswa kelas 7B?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana data frekuensi disusun dan bagaimana total populasi dapat diperoleh dari tabel frekuensi.. Bukti: menampilkan data tersebut dalam tabel frekuensi; Tabel 6.2 Tabel Banyak Aplikasi Online
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu memahami cara membaca tabel frekuensi dan melakukan penjumlahan dasar. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks. Siswa hanya perlu mengenali bahwa Tabel 6.2 mencakup semua siswa (termasuk yang memiliki 0 aplikasi), sedangkan Tabel 6.3 hanya mencakup siswa yang memiliki aplikasi favorit.. Bukti: Tabel 6.2 Tabel Banyak Aplikasi Online; Berapakah jumlah siswa kelas 7B?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami cara membaca tabel frekuensi dan melakukan penjumlahan bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah terbiasa membaca tabel frekuensi sederhana. Menjumlahkan frekuensi untuk mendapatkan total populasi adalah prosedur rutin yang sesuai dengan tingkat kelas. |

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
Solusi minimum hasil AI: Berdasarkan Tabel 6.3 (Tabel Jenis Aplikasi Online), baris 'Among Us!' menunjukkan angka 4 pada kolom 'Banyak Siswa'. Jadi, jumlah siswa yang memilih Among Us! adalah 4 siswa.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6f8d1adfdf6b77bae7b6592ef65aa6520796bd41482782c2d3be7c85ac2b6acd`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2576 |
| 2 | success | valid / verified | knowing | factual | Easy | 2557 |
| 3 | success | valid / verified | knowing | factual | Easy | 2497 |

Run 1 — solusi: Berdasarkan Tabel 6.3 (Tabel Jenis Aplikasi Online), baris 'Among Us!' menunjukkan angka 4 pada kolom 'Banyak Siswa'. Jadi, jumlah siswa yang memilih Among Us! adalah 4 siswa.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk membaca data dari tabel frekuensi yang sudah disediakan secara langsung tanpa perlu melakukan kalkulasi atau interpretasi kompleks. Ini adalah aktivitas mengenali informasi faktual dari representasi data.. Bukti: Berapa jumlah siswa yang memilih Aplikasi Among Us! sebagai permainan favoritnya?
- Dimensi pengetahuan `classify/factual`: Soal menguji kemampuan siswa dalam membaca dan mengidentifikasi data dari tabel frekuensi, yang merupakan pengetahuan faktual mengenai cara membaca data.. Bukti: Tabel 6.3 Tabel Jenis Aplikasi Online; Berapa jumlah siswa yang memilih Aplikasi Among Us! sebagai permainan favoritnya?
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena hanya memerlukan pembacaan langsung dari tabel yang sudah tersedia. Tidak ada langkah tambahan, integrasi, atau analisis yang diperlukan.. Bukti: Berapa jumlah siswa yang memilih Aplikasi Among Us! sebagai permainan favoritnya?

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
| gradeRelativeRationale | Siswa kelas 7 sudah sangat familiar dengan membaca tabel data sederhana. Soal ini tidak menuntut analisis lebih lanjut selain ekstraksi data langsung. |

Run 2 — solusi: Berdasarkan Tabel 6.3 (Tabel Jenis Aplikasi Online), baris 'Among Us!' menunjukkan angka 4 pada kolom 'Banyak Siswa'. Jadi, jumlah siswa yang memilih Among Us! adalah 4 siswa.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan ekstraksi data langsung dari tabel frekuensi yang disediakan. Tidak ada proses pengolahan data atau interpretasi kompleks yang diperlukan.. Bukti: Berapa jumlah siswa yang memilih Aplikasi Among Us! sebagai permainan favoritnya?; Tabel 6.3 Tabel Jenis Aplikasi Online \| Among Us! \| 4
- Dimensi pengetahuan `classify/factual`: Soal ini menguji kemampuan membaca data dari tabel frekuensi, yang merupakan pengetahuan faktual mengenai cara menyajikan dan membaca data.. Bukti: Tabel 6.3 Tabel Jenis Aplikasi Online
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena hanya menuntut pembacaan data secara langsung dari tabel. Tidak ada langkah perantara, perhitungan, atau analisis yang diperlukan.. Bukti: Berapa jumlah siswa yang memilih Aplikasi Among Us! sebagai permainan favoritnya?

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
| gradeRelativeRationale | Siswa kelas 7 sudah sangat familiar dengan membaca tabel data sederhana. Soal ini tidak memiliki kompleksitas tambahan. |

Run 3 — solusi: Melihat Tabel 6.3 pada baris 'Among Us!', nilai frekuensi (Banyak Siswa) adalah 4.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data secara langsung dari tabel frekuensi yang disediakan tanpa melakukan operasi atau interpretasi tambahan.. Bukti: Berapa jumlah siswa yang memilih Aplikasi Among Us! sebagai permainan favoritnya?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji kemampuan membaca informasi faktual dari tabel frekuensi.. Bukti: Tabel 6.3 Tabel Jenis Aplikasi Online
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana karena hanya meminta pembacaan data langsung dari tabel. Tidak ada langkah tambahan, integrasi, atau analisis yang diperlukan.. Bukti: Berapa jumlah siswa yang memilih Aplikasi Among Us! sebagai permainan favoritnya?

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
| gradeRelativeRationale | Siswa kelas 7 sudah terbiasa membaca tabel data sederhana. Soal ini tidak menuntut penalaran lebih lanjut selain ekstraksi data. |

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

![Gambar sumber soal 41](<../../../images/kelas7_panduan_siswa_kelas7.pdf-0224-07.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Bantuan kuota adalah 8 GB. Siswa perlu membeli tambahan jika pemakaian > 8 GB. Berdasarkan grafik, bulan ke-10 (10 GB) dan bulan ke-11 (9 GB) memiliki pemakaian di atas 8 GB. Bulan ke-9 tepat 8 GB, sehingga tidak perlu tambahan.
Gambar sumber: images/kelas7_panduan_siswa_kelas7.pdf-0224-07.png. Transkripsi visual: Diagram batang berjudul 'Penggunaan Kuota Internet untuk PJJ Juli - Desember 2021'. Sumbu horizontal menunjukkan bulan ke-7 hingga ke-12. Sumbu vertikal menunjukkan 'Kuota Internet yang terpakai (GB)' dengan skala 2, 4, 6, 8, 10, 12. Tinggi batang: bulan 7=3 GB, bulan 8=5 GB, bulan 9=8 GB, bulan 10=10 GB, bulan 11=9 GB, bulan 12=7 GB.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `17aae221bfb714f30af3302fe39863d80bd533f1b7e08ecd607d9c4da0a48b8c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3716 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3742 |
| 3 | success | valid / verified | applying | procedural | Easy | 3653 |

Run 1 — solusi: Bantuan kuota adalah 8 GB. Perlu tambahan jika pemakaian > 8 GB. Berdasarkan grafik: bulan ke-10 (10 GB) dan bulan ke-11 (9 GB) memiliki pemakaian di atas 8 GB. Bulan ke-9 tepat 8 GB, sehingga tidak perlu tambahan.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasikan data dari diagram batang dan membandingkan nilai setiap batang dengan ambang batas (8 GB) untuk menentukan bulan mana yang melebihi nilai tersebut. Ini adalah penerapan konsep pembacaan data pada konteks rutin.. Bukti: Jika kalian mendapatkan bantuan kuota internet 8 GB dari Kemdikbud, pada bulan keberapakah kalian perlu membeli tambahan kuota?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang bagaimana membaca dan menginterpretasikan informasi yang disajikan dalam bentuk diagram batang (konsep statistik dasar).. Bukti: Keterangan pada sumbu horizontal menyebutkan urutan bulan. Angka 7 artinya bulan ke-7 atau Juli
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu melakukan perbandingan sederhana antara nilai pada batang dengan nilai ambang batas (8 GB). Jalur penyelesaian sangat jelas, tidak ada kendala yang berinteraksi, dan representasi data sudah sangat familiar bagi siswa kelas 7.. Bukti: Jika kalian mendapatkan bantuan kuota internet 8 GB dari Kemdikbud, pada bulan keberapakah kalian perlu membeli tambahan kuota?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram batang dan membandingkan bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah terbiasa membaca diagram batang sederhana. Tugas membandingkan nilai batang dengan garis acuan 8 GB adalah prosedur rutin yang tidak menuntut perencanaan kompleks. |

Run 2 — solusi: The student needs to identify months where usage exceeds 8 GB. Comparing bar heights to the 8 GB line on the vertical axis: Month 9 is exactly 8 GB (not exceeding), Month 10 is 10 GB (>8), and Month 11 is 9 GB (>8). Therefore, additional quota is needed for months 10 and 11.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep perbandingan nilai data (membaca grafik batang) terhadap ambang batas (8 GB) untuk menentukan bulan mana yang memenuhi kondisi 'lebih dari 8 GB'. Ini adalah penerapan prosedur membaca data pada konteks rutin.. Bukti: Jika kalian mendapatkan bantuan kuota internet 8 GB dari Kemdikbud, pada bulan keberapakah kalian perlu membeli tambahan kuota?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana data disajikan dalam grafik batang dan bagaimana menginterpretasikan hubungan antara sumbu horizontal (waktu) dan vertikal (kuantitas) untuk menjawab pertanyaan spesifik.. Bukti: Keterangan pada sumbu horizontal menyebutkan urutan bulan.; Penggunaan Kuota Internet untuk PJJ
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu melakukan pembacaan langsung pada grafik batang dan membandingkan tinggi batang dengan garis acuan 8 GB. Jalur penyelesaian sangat jelas, tidak ada kendala yang berinteraksi, dan tidak memerlukan perencanaan langkah yang kompleks.. Bukti: Jika kalian mendapatkan bantuan kuota internet 8 GB dari Kemdikbud, pada bulan keberapakah kalian perlu membeli tambahan kuota?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca grafik batang dan membandingkan nilai bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah familiar dengan pembacaan grafik batang sederhana. Tugas membandingkan nilai batang dengan garis ambang batas adalah tugas rutin yang sesuai dengan tingkat kognitif kelas 7. |

Run 3 — solusi: Bandingkan penggunaan kuota setiap bulan dengan batas 8 GB. Bulan yang memerlukan tambahan adalah bulan dengan penggunaan > 8 GB. Berdasarkan diagram: bulan 10 (10 GB) dan bulan 11 (9 GB). Bulan 9 tepat 8 GB, sehingga tidak memerlukan tambahan.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasikan data dari diagram batang dan membandingkan nilai setiap batang dengan ambang batas (8 GB) untuk menentukan bulan mana yang melebihi batas tersebut. Ini adalah penerapan konsep pembacaan data pada konteks rutin.. Bukti: Jika kalian mendapatkan bantuan kuota internet 8 GB dari Kemdikbud, pada bulan keberapakah kalian perlu membeli tambahan kuota?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dalam membaca diagram batang dan menerapkan kriteria perbandingan (lebih besar dari) untuk menyelesaikan masalah.. Bukti: Penggunaan Kuota Internet untuk PJJ
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu melakukan perbandingan nilai sederhana antara tinggi batang dengan garis acuan 8 GB. Tidak ada langkah kompleks atau integrasi antar-konsep yang diperlukan.. Bukti: Jika kalian mendapatkan bantuan kuota internet 8 GB dari Kemdikbud, pada bulan keberapakah kalian perlu membeli tambahan kuota?

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
| gradeRelativeRationale | Siswa kelas 7 sudah familiar dengan pembacaan diagram batang sederhana. Tugas ini hanya memerlukan perbandingan visual langsung dengan ambang batas yang diberikan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `5311`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur membaca data dari diagram batang dan membandingkan nilai setiap batang dengan ambang batas (8 GB) untuk menentukan bulan mana yang memenuhi kondisi 'lebih dari 8 GB'. Ini adalah penerapan konsep pembacaan data pada konteks rutin.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural dalam membaca diagram batang dan menerapkan kriteria perbandingan (lebih besar dari) untuk menyelesaikan masalah.
- Intended difficulty `Easy`: Soal ini tergolong mudah karena siswa hanya perlu melakukan perbandingan nilai sederhana antara tinggi batang dengan garis acuan 8 GB. Tidak ada langkah kompleks atau integrasi antar-konsep yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram batang dan membandingkan bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah familiar dengan pembacaan diagram batang sederhana. Tugas ini hanya memerlukan perbandingan visual langsung dengan ambang batas yang diberikan. |

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
Transkripsi visual: Diagram batang berjudul 'Penggunaan Kuota Internet untuk PJJ Juli - Desember 2021'. Sumbu horizontal menunjukkan bulan ke-7 hingga ke-12. Sumbu vertikal menunjukkan 'Kuota Internet yang terpakai (GB)' dengan skala 2, 4, 6, 8, 10, 12. Tinggi batang: bulan 7=3 GB, bulan 8=5 GB, bulan 9=8 GB, bulan 10=10 GB, bulan 11=9 GB, bulan 12=7 GB.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 42. Soal `425d19fac3fc51700ad86dba`

Diagram di bawah menjelaskan banyaknya mobil berdasarkan warnanya di tempat parkir sebuah taman.<br><br>Mobil warna apakah yang paling banyak ditemui?

| Opsi | Isi |
|---|---|
| A | Merah |
| B | Lainnya |
| C | Putih |
| D | Hitam |

![Gambar sumber soal 42](<../../../images/kelas7_panduan_siswa_kelas7.pdf-0228-09.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Mengamati tinggi batang pada diagram. Batang tertinggi adalah batang berwarna Hitam dengan nilai 26.
Gambar sumber: images/kelas7_panduan_siswa_kelas7.pdf-0228-09.png. Transkripsi visual: Diagram batang berjudul 'Jumlah Mobil Berdasarkan Warna di Tempat Parkir'. Sumbu X menunjukkan warna mobil: Merah, Hitam, Putih, Hijau, Kuning, Lainnya. Sumbu Y menunjukkan jumlah mobil dengan skala 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26. Batang Hitam adalah yang tertinggi, mencapai angka 26.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fe9619646b672d58d453406117141d4c505750137db5a7c5fab964990de1f1b7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 3401 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3395 |
| 3 | success | valid / verified | knowing | factual | Easy | 3436 |

Run 1 — solusi: Mengamati tinggi batang pada diagram batang. Batang tertinggi adalah batang berwarna Hitam dengan nilai 26.
- Domain kognitif `classify/knowing`: Soal hanya meminta siswa untuk membaca data secara langsung dari diagram batang dengan mengidentifikasi batang tertinggi. Tidak ada proses perhitungan atau analisis hubungan yang diperlukan.. Bukti: Mobil warna apakah yang paling banyak ditemui?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman dasar tentang cara membaca informasi dari representasi visual (diagram batang), yang merupakan pengetahuan faktual tentang cara kerja grafik.. Bukti: Diagram di bawah menjelaskan banyaknya mobil berdasarkan warnanya
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana karena hanya memerlukan observasi visual langsung terhadap tinggi batang. Tidak ada langkah-langkah yang saling bergantung atau strategi yang perlu dipilih.. Bukti: Mobil warna apakah yang paling banyak ditemui?

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
| gradeRelativeRationale | Tugas membaca diagram batang adalah kompetensi dasar yang sangat rutin untuk siswa kelas 7. |

Run 2 — solusi: Mengamati tinggi batang pada diagram batang. Batang tertinggi adalah batang untuk warna Hitam, yang mencapai nilai 26 pada sumbu Y.
- Domain kognitif `classify/knowing`: Soal hanya meminta siswa untuk mengidentifikasi batang tertinggi pada diagram batang, yang merupakan prosedur langsung untuk membaca data.. Bukti: Mobil warna apakah yang paling banyak ditemui?; Diagram di bawah menjelaskan banyaknya mobil berdasarkan warnanya
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami cara membaca diagram batang sebagai representasi data, yang merupakan pengetahuan konseptual dasar.. Bukti: Diagram di bawah menjelaskan banyaknya mobil berdasarkan warnanya
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana karena hanya memerlukan pembacaan visual langsung tanpa perhitungan atau interpretasi kompleks.. Bukti: Mobil warna apakah yang paling banyak ditemui?

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
| gradeRelativeRationale | Siswa kelas 7 sudah sangat familiar dengan membaca diagram batang sederhana. Tidak ada langkah kompleks yang diperlukan. |

Run 3 — solusi: Mengamati tinggi batang pada diagram. Batang tertinggi adalah Hitam dengan nilai 26.
- Domain kognitif `classify/knowing`: Soal hanya meminta siswa untuk membaca data secara langsung dari diagram batang tanpa perlu melakukan perhitungan atau interpretasi kompleks. Siswa cukup mengenali batang tertinggi.. Bukti: Mobil warna apakah yang paling banyak ditemui?; Diagram di bawah menjelaskan banyaknya mobil berdasarkan warnanya
- Dimensi pengetahuan `classify/factual`: Soal menguji pemahaman dasar tentang cara membaca diagram batang sebagai representasi data.. Bukti: Diagram di bawah menjelaskan banyaknya mobil berdasarkan warnanya
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena hanya memerlukan kemampuan visual dasar untuk membandingkan tinggi batang. Tidak ada langkah perhitungan atau analisis yang diperlukan.. Bukti: Mobil warna apakah yang paling banyak ditemui?

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
| gradeRelativeRationale | Siswa kelas 7 sudah sangat familiar dengan pembacaan diagram batang sederhana. Soal ini tidak menuntut analisis data, hanya observasi visual. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4531`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal hanya meminta siswa untuk membaca data secara langsung dari diagram batang dengan mengidentifikasi batang tertinggi. Tidak ada proses perhitungan atau analisis hubungan yang diperlukan.
- Dimensi pengetahuan `factual`: Soal ini menguji pemahaman dasar tentang cara membaca informasi dari representasi visual (diagram batang), yang merupakan pengetahuan faktual tentang cara kerja grafik.
- Intended difficulty `Easy`: Soal ini sangat sederhana karena hanya memerlukan observasi visual langsung terhadap tinggi batang. Tidak ada langkah-langkah yang saling bergantung atau strategi yang perlu dipilih.

Profil difficulty hasil adjudikasi:

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
| gradeRelativeRationale | Tugas membaca diagram batang adalah kompetensi dasar yang sangat rutin untuk siswa kelas 7. |

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
Transkripsi visual: Diagram batang berjudul 'Jumlah Mobil Berdasarkan Warna di Tempat Parkir'. Sumbu X menunjukkan warna mobil: Merah, Hitam, Putih, Hijau, Kuning, Lainnya. Sumbu Y menunjukkan jumlah mobil dengan skala 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26. Batang Hitam adalah yang tertinggi, mencapai angka 26.
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

![Gambar sumber soal 43](<../../../images/kelas7_panduan_siswa_kelas7.pdf-0233-06.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Emisi Jerman 1990 = 1209, 1998 = 1020. Penurunan = 1209 - 1020 = 189. Persentase penurunan = (189 / 1209) * 100% ≈ 15,63%, dibulatkan menjadi 16%.
Gambar sumber: images/kelas7_panduan_siswa_kelas7.pdf-0233-06.png. Transkripsi visual: Diagram batang menunjukkan emisi CO2 (juta ton) untuk berbagai negara pada tahun 1990 (batang putih) dan 1998 (batang hitam). Untuk Jerman, nilai tahun 1990 adalah 1209 dan nilai tahun 1998 adalah 1020.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f8bb5faf1444571466384c2db0fa58ce89717eef36882799ff0374848aae3964`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3902 |
| 2 | success | valid / verified | applying | procedural | Easy | 3850 |
| 3 | success | valid / verified | applying | procedural | Easy | 3885 |

Run 1 — solusi: Emisi Jerman 1990 = 1209, 1998 = 1020. Penurunan = 1209 - 1020 = 189. Persentase penurunan = (189 / 1209) * 100% ≈ 15,63%, dibulatkan menjadi 16%.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan prosedur persentase perubahan (selisih dibagi nilai awal) pada data yang diambil dari diagram. Ini adalah penerapan konsep persentase pada konteks data yang diberikan.. Bukti: Berapakah persentase perubahan level emisi CO2 untuk negara Jerman?; Diagram di bawah ini menunjukkan level emisi CO2 pada tahun 1990 dan 1998.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang prosedur perhitungan persentase perubahan (kenaikan/penurunan relatif) yang merupakan teknik prosedural standar.. Bukti: persentase perubahan level emisi CO2
- Intended difficulty `classify/Easy`: Soal ini memberikan contoh langkah-langkah perhitungan untuk negara lain (USA), yang berfungsi sebagai perancah (scaffold) kuat bagi siswa untuk mengikuti prosedur yang sama pada data Jerman. Siswa hanya perlu mengidentifikasi nilai yang relevan dari grafik dan menerapkan rumus yang telah dicontohkan.. Bukti: Berapakah persentase perubahan level emisi CO2 untuk negara Jerman?; Level emisi CO2 pada tahun 1990 di USA = 6049 juta ton Level emisi CO2 pada tahun 1998 di USA = 6727 juta ton Kenaikan level emisi CO2 di USA = 6727 – 6049 – 678 juta ton Maka persentase kenaikan level emisi CO2 di USA =

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi pengurangan bilangan bulat dan konsep dasar persentase (perubahan relatif). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun melibatkan angka besar, prosedur perhitungan persentase perubahan sudah dicontohkan secara eksplisit dalam teks soal, sehingga mengurangi beban kognitif perencanaan bagi siswa kelas 7. |

Run 2 — solusi: Emisi Jerman 1990 = 1209, 1998 = 1020. Penurunan = 1209 - 1020 = 189. Persentase penurunan = (189 / 1209) * 100% ≈ 15,63% ≈ 16%.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur persentase perubahan yang telah dicontohkan dalam soal (untuk USA) ke data negara lain (Jerman). Ini adalah penerapan konsep pada konteks rutin.. Bukti: Berapakah persentase perubahan level emisi CO2 untuk negara Jerman?; Diagram di bawah ini menunjukkan level emisi CO2 pada tahun 1990 dan 1998.
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritme atau metode perhitungan persentase perubahan yang sudah diberikan contoh prosedurnya di bagian awal soal.. Bukti: Kenaikan level emisi CO2 di USA = 6727 – 6049 – 678 juta ton Maka persentase kenaikan level emisi CO2 di USA =; Berapakah persentase perubahan level emisi CO2 untuk negara Jerman?
- Intended difficulty `classify/Easy`: Soal memberikan contoh langkah-langkah perhitungan (scaffolding) untuk negara USA, sehingga siswa hanya perlu meniru prosedur tersebut untuk negara Jerman. Jalur penyelesaian sangat jelas dan familiar.. Bukti: Pada diagram, kita bisa melihat bahwa di negara USA mengalami kenaikan level emisi CO2 dari tahun 1990 ke tahun 1998 sebesar 11%.; Berapakah persentase perubahan level emisi CO2 untuk negara Jerman?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmetika dasar dan konsep persentase perubahan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah mempelajari persentase dan interpretasi data. Adanya contoh pengerjaan yang eksplisit membuat soal ini menjadi latihan rutin yang mudah. |

Run 3 — solusi: Emisi 1990 = 1209, Emisi 1998 = 1020. Penurunan = 1209 - 1020 = 189. Persentase penurunan = (189 / 1209) * 100% ≈ 15,63% (dibulatkan menjadi 16%).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur persentase perubahan yang telah dicontohkan dalam soal (untuk USA) ke data negara lain (Jerman). Ini adalah penerapan prosedur pada konteks rutin.. Bukti: Berapakah persentase perubahan level emisi CO2 untuk negara Jerman?; Level emisi CO2 pada tahun 1990 di USA = 6049 juta ton Level emisi CO2 pada tahun 1998 di USA = 6727 juta ton
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritme persentase perubahan (selisih dibagi nilai awal dikali 100%) yang merupakan pengetahuan prosedural.. Bukti: Maka persentase kenaikan level emisi CO2 di USA =; Berapakah persentase perubahan level emisi CO2 untuk negara Jerman?
- Intended difficulty `classify/Easy`: Soal memberikan contoh langkah-langkah perhitungan yang eksplisit untuk negara lain (USA), sehingga siswa hanya perlu meniru prosedur tersebut untuk data Jerman. Jalur penyelesaian sangat jelas dan terbantu oleh contoh.. Bukti: Pada diagram, kita bisa melihat bahwa di negara USA mengalami kenaikan level emisi CO2 dari tahun 1990 ke tahun 1998 sebesar 11%.; Berapakah persentase perubahan level emisi CO2 untuk negara Jerman?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmetika dasar, konsep persentase, dan membaca data dari diagram batang. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | strong |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah mempelajari persentase dan diagram batang. Karena soal memberikan contoh langkah-langkah (scaffolding kuat) untuk kasus serupa, tingkat kesulitan menjadi rendah. |

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
Transkripsi visual: Diagram batang menunjukkan emisi CO2 (juta ton) untuk berbagai negara pada tahun 1990 (batang putih) dan 1998 (batang hitam). Untuk Jerman, nilai tahun 1990 adalah 1209 dan nilai tahun 1998 adalah 1020.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 44. Soal `7ea9980573af6cf5eee574ca`

Jawablah pertanyaan berikut berdasarkan diagram batang ganda di bawah ini yang menunjukkan perolehan medali emas, perak, dan perunggu Indonesia dalam ajang Pesta Olahraga Se-Asia Tenggara SEA Games.<br><br>Perolehan Medali Indonesia di SEA Games<br><br>Pada SEA Games tahun berapakah Indonesia memperoleh medali emas paling banyak?

| Opsi | Isi |
|---|---|
| A | 2019 |
| B | 2013 |
| C | 2017 |
| D | 2011 |

![Gambar sumber soal 44](<../../../images/kelas7_panduan_siswa_kelas7.pdf-0247-01.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Identifikasi batang berwarna oranye (Emas) untuk setiap tahun: 2011 (182), 2013 (64), 2015 (47), 2017 (38), 2019 (72). Nilai tertinggi adalah 182 pada tahun 2011.
Gambar sumber: images/kelas7_panduan_siswa_kelas7.pdf-0247-01.png. Transkripsi visual: Diagram batang horizontal menunjukkan perolehan medali Indonesia di SEA Games tahun 2011, 2013, 2015, 2017, dan 2019. Legenda: Oranye (Emas), Hijau (Perak), Ungu (Perunggu). Data Emas (Oranye): 2011=182, 2013=64, 2015=47, 2017=38, 2019=72.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3bb60a4672d264e525773211ac8dbfd6d995a6623cc58ce6aae927814509674a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3538 |
| 2 | success | valid / verified | knowing | factual | Easy | 3561 |
| 3 | success | valid / verified | knowing | factual | Easy | 3542 |

Run 1 — solusi: Identifikasi batang berwarna oranye (Emas) untuk setiap tahun: 2011 (182), 2013 (64), 2015 (47), 2017 (38), 2019 (72). Nilai tertinggi adalah 182 pada tahun 2011.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk membaca data dari diagram batang dan melakukan perbandingan nilai sederhana untuk menemukan nilai maksimum. Ini adalah prosedur langsung dalam membaca data.. Bukti: Pada SEA Games tahun berapakah Indonesia memperoleh medali emas paling banyak?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami cara membaca diagram batang dan mengaitkan legenda warna dengan kategori data (emas).. Bukti: diagram batang ganda
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena hanya memerlukan pembacaan langsung dari grafik tanpa ada manipulasi data atau langkah tambahan. Siswa hanya perlu membandingkan nilai pada batang oranye.. Bukti: Pada SEA Games tahun berapakah Indonesia memperoleh medali emas paling banyak?

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
| distractorQuality | weak |
| gradeRelativeRationale | Tugas membaca data dari diagram batang adalah kompetensi dasar kelas 7 yang bersifat rutin dan langsung. |

Run 2 — solusi: Mengidentifikasi batang berwarna oranye (Emas) untuk setiap tahun: 2011=182, 2013=64, 2015=47, 2017=38, 2019=72. Nilai terbesar adalah 182 yang terjadi pada tahun 2011.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data dari diagram batang dan melakukan perbandingan nilai sederhana untuk menentukan nilai maksimum.. Bukti: Pada SEA Games tahun berapakah Indonesia memperoleh medali emas paling banyak?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang cara membaca dan menginterpretasikan data yang disajikan dalam bentuk diagram batang.. Bukti: diagram batang ganda; medali emas paling banyak
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (direct retrieval) tanpa memerlukan kalkulasi atau integrasi antar variabel. Siswa hanya perlu mengidentifikasi kategori 'Emas' dan mencari nilai tertinggi.. Bukti: Pada SEA Games tahun berapakah Indonesia memperoleh medali emas paling banyak?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca data dari diagram batang. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Tugas membaca data sederhana dari grafik adalah kompetensi dasar yang diharapkan bagi siswa kelas 7. |

Run 3 — solusi: Identifikasi batang berwarna oranye (emas) untuk setiap tahun: 2011 (182), 2013 (64), 2015 (47), 2017 (38), 2019 (72). Nilai terbesar adalah 182 pada tahun 2011.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data dari diagram batang dan membandingkan nilai untuk menentukan nilai maksimum. Ini adalah prosedur langsung.. Bukti: Pada SEA Games tahun berapakah Indonesia memperoleh medali emas paling banyak?
- Dimensi pengetahuan `classify/factual`: Soal menguji kemampuan membaca data faktual yang disajikan dalam bentuk diagram batang.. Bukti: diagram batang ganda; medali emas paling banyak
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena hanya memerlukan pembacaan langsung dari diagram batang tanpa perlu melakukan perhitungan atau manipulasi data yang kompleks.. Bukti: Pada SEA Games tahun berapakah Indonesia memperoleh medali emas paling banyak?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram batang dan membandingkan bilangan cacah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 7 sudah sangat familiar dengan pembacaan grafik sederhana. Soal ini tidak memerlukan analisis mendalam, hanya identifikasi nilai maksimum. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 1, "factual": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4914`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta siswa untuk membaca data dari diagram batang dan melakukan perbandingan nilai sederhana untuk menemukan nilai maksimum. Ini adalah prosedur langsung dalam membaca data.
- Dimensi pengetahuan `conceptual`: Siswa perlu memahami cara membaca diagram batang dan mengaitkan legenda warna dengan kategori data (emas).
- Intended difficulty `Easy`: Soal ini sangat mudah karena hanya memerlukan pembacaan langsung dari grafik tanpa ada manipulasi data atau langkah tambahan. Siswa hanya perlu membandingkan nilai pada batang oranye.

Profil difficulty hasil adjudikasi:

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
| distractorQuality | weak |
| gradeRelativeRationale | Tugas membaca data dari diagram batang adalah kompetensi dasar kelas 7 yang bersifat rutin dan langsung. |

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
Transkripsi visual: Diagram batang horizontal menunjukkan perolehan medali Indonesia di SEA Games tahun 2011, 2013, 2015, 2017, dan 2019. Legenda: Oranye (Emas), Hijau (Perak), Ungu (Perunggu). Data Emas (Oranye): 2011=182, 2013=64, 2015=47, 2017=38, 2019=72.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 45. Soal `b1aa54c53e0576c10fa47136`

Diagram lingkaran menunjukkan sebaran jumlah suara yang diterima tiap kandidat dalam pemilihan ketua OSIS di SMP Pancasila.<br><br>Hitunglah sudut pusat dari setiap juring pada diagram ini.

| Opsi | Isi |
|---|---|
| A | Danu 144°, Rizki 88°, Noer 56°, Karno 40°, Indah 32° |
| B | Danu 72°, Rizki 72°, Noer 72°, Karno 72°, Indah 72° |
| C | Danu 40°, Rizki 24,4°, Noer 15,6°, Karno 11,1°, Indah 8,9° |
| D | Danu 180°, Rizki 110°, Noer 70°, Karno 50°, Indah 40° |

![Gambar sumber soal 45](<../../../images/kelas7_panduan_siswa_kelas7.pdf-0239-07.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Total suara = 18 + 11 + 7 + 5 + 4 = 45. Sudut pusat = (suara/45) * 360 derajat = suara * 8 derajat. Danu: 18 * 8 = 144 derajat; Rizki: 11 * 8 = 88 derajat; Noer: 7 * 8 = 56 derajat; Karno: 5 * 8 = 40 derajat; Indah: 4 * 8 = 32 derajat.
Gambar sumber: images/kelas7_panduan_siswa_kelas7.pdf-0239-07.png. Transkripsi visual: Diagram lingkaran menunjukkan data suara pemilihan ketua OSIS: Danu (18), Rizki (11), Noer (7), Karno (5), Indah (4).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f89c499732570512a661079b6fda9658ec1447db0f6d8e3bcbb61ebbde6218d5`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3715 |
| 2 | success | valid / verified | applying | procedural | Medium | 3714 |
| 3 | success | valid / verified | applying | procedural | Easy | 3708 |

Run 1 — solusi: Total suara = 18+11+7+5+4 = 45. Sudut pusat = (suara/total) * 360 derajat. Danu: (18/45)*360 = 144 derajat. Rizki: (11/45)*360 = 88 derajat. Noer: (7/45)*360 = 56 derajat. Karno: (5/45)*360 = 40 derajat. Indah: (4/45)*360 = 32 derajat.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur untuk mengubah data frekuensi menjadi proporsi sudut dalam lingkaran (360 derajat). Ini adalah penerapan langsung dari konsep rasio dan proporsi dalam konteks diagram lingkaran.. Bukti: Hitunglah sudut pusat dari setiap juring pada diagram ini.
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penggunaan algoritma atau metode standar untuk menghitung sudut juring berdasarkan total data yang diberikan.. Bukti: Hitunglah sudut pusat dari setiap juring pada diagram ini.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah yang saling terkait (menjumlahkan total, menghitung proporsi, mengalikan dengan 360 derajat) untuk setiap kategori. Meskipun prosedurnya rutin, siswa harus mengelola perhitungan untuk lima kategori berbeda tanpa kesalahan, yang meningkatkan beban kognitif dibandingkan soal satu langkah.. Bukti: Hitunglah sudut pusat dari setiap juring pada diagram ini.; Danu (18), Rizki (11), Noer (7), Karno (5), Indah (4)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan bulat, konsep pecahan/rasio, dan pemahaman bahwa satu lingkaran penuh adalah 360 derajat. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu melakukan perhitungan rasio dan proporsi. Soal ini menuntut ketelitian dalam melakukan perhitungan berulang untuk setiap data, yang sesuai dengan tingkat kesulitan menengah untuk jenjang ini. |

Run 2 — solusi: Total suara = 18 + 11 + 7 + 5 + 4 = 45. Sudut pusat = (jumlah suara / total suara) * 360°. Danu: (18/45)*360 = 144°. Rizki: (11/45)*360 = 88°. Noer: (7/45)*360 = 56°. Karno: (5/45)*360 = 40°. Indah: (4/45)*360 = 32°.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar untuk mengubah data frekuensi menjadi sudut dalam diagram lingkaran. Ini adalah penerapan konsep rasio dan proporsi dalam konteks rutin.. Bukti: Hitunglah sudut pusat dari setiap juring pada diagram ini.; Diagram lingkaran menunjukkan sebaran jumlah suara yang diterima tiap kandidat
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritme atau metode perhitungan (proporsi terhadap 360 derajat) untuk menyelesaikan masalah data.. Bukti: Hitunglah sudut pusat dari setiap juring pada diagram ini.
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena memerlukan beberapa langkah yang saling terkait: menjumlahkan total data, menentukan rasio setiap bagian terhadap total, dan mengalikan dengan 360 derajat. Meskipun prosedurnya rutin, siswa harus melakukan perhitungan berulang untuk lima kategori yang berbeda, yang meningkatkan beban kognitif dibandingkan soal satu langkah.. Bukti: Hitunglah sudut pusat dari setiap juring pada diagram ini.; Danu (18), Rizki (11), Noer (7), Karno (5), Indah (4)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan bulat, konsep pecahan/rasio, dan pemahaman sudut satu putaran penuh (360 derajat). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu mengolah data statistik sederhana. Perhitungan berulang untuk 5 data meningkatkan kompleksitas prosedural namun tetap dalam koridor rutin. |

Run 3 — solusi: Total suara = 18 + 11 + 7 + 5 + 4 = 45. Sudut pusat = (suara/45) * 360 derajat = suara * 8 derajat. Danu: 18 * 8 = 144 derajat; Rizki: 11 * 8 = 88 derajat; Noer: 7 * 8 = 56 derajat; Karno: 5 * 8 = 40 derajat; Indah: 4 * 8 = 32 derajat.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur standar untuk mengubah data frekuensi menjadi sudut pusat pada diagram lingkaran. Ini adalah penerapan konsep rasio dan proporsi dalam konteks data yang rutin.. Bukti: Hitunglah sudut pusat dari setiap juring pada diagram ini.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritme atau metode perhitungan sudut juring berdasarkan proporsi data terhadap total.. Bukti: Hitunglah sudut pusat dari setiap juring pada diagram ini.
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena prosedur penyelesaiannya sangat langsung dan familiar bagi siswa kelas 7. Siswa hanya perlu menjumlahkan total data, menentukan rasio, dan mengalikan dengan 360 derajat. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi non-rutin.. Bukti: Hitunglah sudut pusat dari setiap juring pada diagram ini.; Danu (18), Rizki (11), Noer (7), Karno (5), Indah (4)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan bulat, konsep pecahan/rasio, dan pemahaman dasar tentang sudut satu lingkaran penuh (360 derajat). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi diagram lingkaran dan konversi data ke derajat adalah standar kurikulum kelas 7. Prosedur yang digunakan adalah rutin dan langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `5494`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan prosedur standar untuk mengubah data frekuensi menjadi sudut pusat dalam lingkaran (360 derajat). Ini adalah penerapan konsep rasio dan proporsi dalam konteks data yang rutin.
- Dimensi pengetahuan `procedural`: Soal menuntut penggunaan algoritme atau metode perhitungan (proporsi terhadap 360 derajat) untuk menyelesaikan masalah data.
- Intended difficulty `Medium`: Soal ini tergolong Medium karena memerlukan beberapa langkah yang saling terkait: menjumlahkan total data, menentukan rasio setiap bagian terhadap total, dan mengalikan dengan 360 derajat. Meskipun prosedurnya rutin, siswa harus melakukan perhitungan berulang untuk lima kategori yang berbeda, yang meningkatkan beban kognitif dibandingkan soal satu langkah.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan bulat, konsep pecahan/rasio, dan pemahaman sudut satu putaran penuh (360 derajat). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu mengolah data statistik sederhana. Perhitungan berulang untuk 5 data meningkatkan kompleksitas prosedural namun tetap dalam koridor rutin. |

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

![Gambar sumber soal 46](<../../../images/kelas7_panduan_siswa_kelas7.pdf-0245-05.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Mengamati diagram lingkaran, terdapat empat label kategori yang berbeda untuk panjang password, yaitu 6-angka, 7-angka, 8-angka, dan 9-angka. Jadi, terdapat 4 macam panjang password.
Gambar sumber: images/kelas7_panduan_siswa_kelas7.pdf-0245-05.png. Transkripsi visual: Diagram lingkaran menunjukkan empat sektor yang masing-masing diberi label: 6-angka (dengan nilai 12), 7-angka (dengan nilai 3), 8-angka (dengan nilai 20), dan 9-angka (dengan nilai 5).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1480002ad97f865e78bb7481f965b7b38243cd4df22e7b46b588299f32e9805d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 4566 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3478 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 3443 |

Run 1 — solusi: Mengamati diagram lingkaran dan menghitung jumlah kategori yang ada, yaitu 6-angka, 7-angka, 8-angka, dan 9-angka, sehingga totalnya ada 4 macam.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengidentifikasi dan menghitung jumlah kategori yang disajikan secara eksplisit dalam diagram lingkaran tanpa melakukan operasi atau analisis data lebih lanjut.. Bukti: Ada berapa macam panjang password email siswa di kelas ini?; 6-angka; 7-angka; 8-angka
- Dimensi pengetahuan `classify/factual`: Soal menuntut pengenalan elemen dasar (kategori) yang disajikan secara visual dan eksplisit dalam diagram.. Bukti: 6-angka; 7-angka; 8-angka; 9-angka
- Intended difficulty `classify/Easy`: Soal bersifat sangat langsung. Siswa hanya perlu menghitung jumlah label kategori yang tersedia pada diagram lingkaran. Tidak ada perhitungan atau interpretasi data yang kompleks yang diperlukan.. Bukti: Ada berapa macam panjang password email siswa di kelas ini?; 6-angka; 7-angka; 8-angka

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca label pada diagram statistik sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sudah terbiasa membaca data dari diagram lingkaran sederhana. Soal ini tidak menuntut analisis data, hanya identifikasi kategori. |

Run 2 — solusi: Mengamati label kategori pada diagram lingkaran menunjukkan terdapat empat sektor yang mewakili panjang password: 6-angka, 7-angka, 8-angka, dan 9-angka. Jadi, ada 4 macam panjang password.
- Domain kognitif `classify/knowing`: Soal hanya meminta siswa untuk mengidentifikasi jumlah kategori yang disajikan dalam diagram lingkaran. Ini adalah tugas mengenali informasi yang sudah tersedia secara eksplisit dalam visual.. Bukti: Ada berapa macam panjang password email siswa di kelas ini?; Diagram lingkaran menunjukkan empat kategori panjang password: 6-angka, 7-angka, 8-angka, dan 9-angka.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami istilah 'macam' dalam konteks data statistik (kategori data) yang disajikan dalam diagram lingkaran.. Bukti: Ada berapa macam panjang password email siswa di kelas ini?
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana karena hanya memerlukan pembacaan langsung terhadap label kategori pada diagram. Tidak ada perhitungan atau interpretasi hubungan yang kompleks.. Bukti: Ada berapa macam panjang password email siswa di kelas ini?; Diagram lingkaran menunjukkan empat kategori panjang password

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca label pada diagram lingkaran. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas membaca data dari diagram lingkaran adalah materi dasar kelas 7. Soal ini tidak menuntut analisis lebih lanjut selain menghitung jumlah kategori yang terlihat jelas. |

Run 3 — solusi: Mengamati diagram lingkaran, terdapat empat juring yang berbeda, masing-masing mewakili kategori panjang password: 6-angka, 7-angka, 8-angka, dan 9-angka. Jadi, ada 4 macam panjang password.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi jumlah kategori yang ada dalam diagram lingkaran. Ini adalah tugas mengenali informasi yang disajikan secara eksplisit dalam visual.. Bukti: Ada berapa macam panjang password email siswa di kelas ini?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami representasi data dalam diagram lingkaran untuk mengidentifikasi kategori yang disajikan.. Bukti: Panjang Password Email; 6-angka, 7-angka, 8-angka, dan 9-angka
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu menghitung jumlah juring atau label kategori yang ada pada diagram lingkaran. Tidak ada perhitungan atau integrasi langkah yang diperlukan.. Bukti: Ada berapa macam panjang password email siswa di kelas ini?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram lingkaran sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas ini adalah tingkat dasar dalam literasi data untuk kelas 7, yaitu sekadar membaca informasi yang sudah tersedia secara visual. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4802`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal hanya meminta siswa untuk mengidentifikasi dan menghitung jumlah kategori yang disajikan secara eksplisit dalam diagram lingkaran. Tidak ada operasi matematika atau analisis data yang diperlukan.
- Dimensi pengetahuan `factual`: Siswa perlu mengenali elemen dasar (kategori) yang disajikan dalam diagram statistik.
- Intended difficulty `Easy`: Soal ini sangat langsung dan bersifat rutin. Siswa hanya perlu membaca label kategori yang tersedia pada diagram. Tidak ada tuntutan perencanaan, integrasi, atau perhitungan yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca label pada diagram lingkaran sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas membaca data dari diagram lingkaran adalah materi dasar kelas 7. Soal ini tidak menuntut analisis lebih lanjut selain menghitung jumlah kategori yang terlihat jelas. |

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
Transkripsi visual: Diagram lingkaran menunjukkan empat sektor yang masing-masing diberi label: 6-angka (dengan nilai 12), 7-angka (dengan nilai 3), 8-angka (dengan nilai 20), dan 9-angka (dengan nilai 5).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "factual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: Diagram lingkaran (pie chart) digunakan untuk merepresentasikan proporsi bagian terhadap keseluruhan (total 100%). Suku bunga deposito pada tabel adalah nilai persentase masing-masing bank yang berdiri sendiri dan tidak merepresentasikan bagian dari satu kesatuan (jumlahnya tidak 100%), sehingga tidak tepat disajikan dalam diagram lingkaran.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1a702e1f26ab35447594c88e820ddabe1ca5651b9da2bd9431b335e17fdd3a7f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Easy | 2537 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 2527 |
| 3 | success | valid / verified | reasoning | conceptual | Easy | 2486 |

Run 1 — solusi: Diagram lingkaran digunakan untuk merepresentasikan proporsi bagian terhadap keseluruhan (total 100%). Suku bunga deposito pada tabel adalah nilai persentase masing-masing bank yang berdiri sendiri dan tidak merepresentasikan bagian dari satu kesatuan (jumlahnya tidak 100%), sehingga tidak tepat disajikan dalam diagram lingkaran.
- Domain kognitif `classify/reasoning`: Soal menuntut siswa untuk memahami prinsip dasar representasi data, yaitu syarat penggunaan diagram lingkaran (bagian dari keseluruhan). Siswa harus menghubungkan konsep diagram lingkaran dengan karakteristik data yang diberikan, yang merupakan proses reasoning untuk mengevaluasi kesesuaian representasi.. Bukti: kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas; Pilih penjelasan yang tepat
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang syarat penggunaan diagram lingkaran, yaitu data harus merupakan bagian dari satu kesatuan (proporsional terhadap total 100%).. Bukti: diagram lingkaran untuk merepresentasikan data; persen suku bunga tiap bank bukan bagian dari satu keseluruhan
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena menanyakan pemahaman dasar tentang fungsi diagram lingkaran. Siswa hanya perlu mengenali bahwa diagram lingkaran memerlukan data yang membentuk satu kesatuan (total 100%), yang merupakan konsep dasar dalam penyajian data di kelas 7.. Bukti: kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas; Pilih penjelasan yang tepat

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang diagram lingkaran dan syarat penggunaannya (bagian dari keseluruhan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan memahami kapan diagram lingkaran tepat digunakan. Soal ini menguji pemahaman konseptual dasar tanpa memerlukan perhitungan rumit atau integrasi langkah yang kompleks. |

Run 2 — solusi: Diagram lingkaran digunakan untuk merepresentasikan proporsi bagian terhadap keseluruhan (total 100%). Suku bunga deposito adalah nilai persentase masing-masing bank yang berdiri sendiri dan tidak membentuk satu kesatuan (jumlahnya tidak 100%), sehingga tidak tepat disajikan dalam diagram lingkaran.
- Domain kognitif `classify/reasoning`: Soal menuntut pemahaman konseptual tentang syarat penggunaan diagram lingkaran (bagian dari keseluruhan) dibandingkan dengan sekadar menyajikan data numerik. Siswa harus memahami sifat data persentase dalam konteks ini.. Bukti: kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang prinsip dasar representasi data, yaitu kapan suatu diagram tepat digunakan berdasarkan sifat data tersebut.. Bukti: diagram lingkaran untuk merepresentasikan data di atas
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena menuntut pemahaman konseptual yang lebih dalam daripada sekadar membaca tabel. Siswa harus membedakan antara data persentase yang merupakan bagian dari total 100% (proporsional) dengan data persentase yang merupakan nilai atribut independen (seperti suku bunga). Ini memerlukan penalaran tentang struktur data, bukan sekadar prosedur menggambar.. Bukti: kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang fungsi diagram lingkaran dan konsep persentase sebagai bagian dari keseluruhan. |
| dependentSteps | 1 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 sering kali menganggap semua data persentase otomatis bisa dibuat diagram lingkaran. Soal ini menantang miskonsepsi tersebut dengan menuntut pemahaman konseptual tentang 'keseluruhan' (whole) dalam diagram lingkaran. |

Run 3 — solusi: Diagram lingkaran (pie chart) digunakan untuk merepresentasikan proporsi bagian terhadap keseluruhan (total 100%). Suku bunga deposito adalah nilai persentase masing-masing bank yang berdiri sendiri dan tidak membentuk satu kesatuan (jumlahnya tidak 100%), sehingga tidak tepat disajikan dalam diagram lingkaran.
- Domain kognitif `classify/reasoning`: Soal menuntut pemahaman konseptual tentang syarat penggunaan diagram lingkaran. Siswa harus memahami bahwa diagram lingkaran merepresentasikan bagian dari keseluruhan (proporsi), bukan sekadar data yang berbentuk persen.. Bukti: kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual mengenai fungsi dan batasan penggunaan diagram lingkaran dalam penyajian data.. Bukti: diagram lingkaran untuk merepresentasikan data di atas
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena menanyakan konsep dasar penyajian data yang seharusnya sudah dipelajari. Siswa hanya perlu mengidentifikasi syarat utama diagram lingkaran (bagian dari keseluruhan) tanpa perlu melakukan perhitungan kompleks atau langkah-langkah yang saling bergantung.. Bukti: kalian tidak dapat menggunakan diagram lingkaran untuk merepresentasikan data di atas

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang fungsi diagram lingkaran sebagai representasi proporsi bagian terhadap keseluruhan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan memahami karakteristik dasar diagram statistik. Membedakan data yang bersifat proporsional (bagian dari total) dengan data yang bersifat independen (seperti suku bunga) adalah materi standar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"reasoning": 3} | unanimous_3_0 / adjudicated | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 2, "Medium": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4129`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `reasoning`: Soal ini menuntut siswa untuk mengevaluasi kesesuaian representasi data berdasarkan pemahaman konseptual tentang syarat penggunaan diagram lingkaran. Siswa harus menghubungkan karakteristik data (persentase independen) dengan prinsip diagram lingkaran (bagian dari keseluruhan), yang merupakan bentuk penalaran konseptual.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman konseptual tentang prinsip dasar penyajian data, yaitu syarat penggunaan diagram lingkaran (data harus merupakan bagian dari satu kesatuan/total 100%).
- Intended difficulty `Easy`: Soal ini tergolong Easy karena menguji pemahaman konseptual dasar yang seharusnya sudah dikuasai siswa kelas 7 mengenai fungsi diagram lingkaran. Tidak ada perhitungan yang diperlukan, tidak ada langkah-langkah yang saling bergantung, dan konsep 'bagian dari keseluruhan' adalah materi standar dalam penyajian data.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang fungsi diagram lingkaran sebagai representasi proporsi bagian terhadap keseluruhan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan memahami karakteristik dasar diagram statistik. Membedakan data yang bersifat proporsional (bagian dari total) dengan data yang bersifat independen (seperti suku bunga) adalah materi standar yang tidak memerlukan integrasi langkah yang kompleks. |

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

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "reasoning", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: Data pengeluaran listrik bulanan selama satu tahun merupakan data kontinu yang menunjukkan perubahan nilai terhadap waktu (bulan). Diagram garis adalah representasi yang paling tepat untuk menunjukkan tren atau perubahan data numerik secara berurutan dalam rentang waktu tertentu.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `['menerapkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e5c10a4ae13ad582e96085853bc7e7bbd99f906a12db36c0a7a0c5e27f576581`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2293 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2293 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2293 |

Run 1 — solusi: Data pengeluaran listrik bulanan selama satu tahun merupakan data kontinu yang menunjukkan perubahan nilai terhadap waktu (bulan). Diagram garis adalah representasi yang paling tepat untuk menunjukkan tren atau perubahan data numerik secara berurutan dalam rentang waktu tertentu.
- Domain kognitif `classify/applying`: Siswa diminta untuk memilih representasi data yang tepat berdasarkan karakteristik data (data deret waktu/time series). Ini memerlukan pemahaman konseptual tentang fungsi berbagai jenis diagram, bukan sekadar menghitung.. Bukti: Diagram apakah yang akan kalian gunakan untuk menunjukkan pengeluaran bulanan keluarga kalian untuk listrik selama 1 tahun?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang kapan dan mengapa menggunakan jenis diagram tertentu untuk merepresentasikan data.. Bukti: Diagram apakah yang akan kalian gunakan untuk menunjukkan pengeluaran bulanan keluarga kalian untuk listrik selama 1 tahun?
- Intended difficulty `classify/Easy`: Soal ini bersifat konseptual dan langsung. Siswa hanya perlu mengidentifikasi hubungan antara data deret waktu dengan diagram garis. Tidak ada perhitungan kompleks atau integrasi kendala yang rumit.. Bukti: Diagram apakah yang akan kalian gunakan untuk menunjukkan pengeluaran bulanan keluarga kalian untuk listrik selama 1 tahun?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang fungsi diagram batang, diagram lingkaran, dan diagram garis. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Memilih diagram yang tepat untuk data deret waktu adalah materi dasar statistika kelas 7. Soal tidak menuntut analisis data yang mendalam, hanya pemilihan alat representasi yang sesuai. |

Run 2 — solusi: Data pengeluaran listrik bulanan selama satu tahun merupakan data kontinu yang berubah terhadap waktu. Diagram garis adalah representasi yang paling tepat untuk menunjukkan tren atau perubahan data numerik secara berurutan dalam rentang waktu tertentu.
- Domain kognitif `classify/applying`: Siswa diminta untuk memilih jenis representasi data yang paling tepat berdasarkan karakteristik data (data deret waktu). Ini memerlukan pemahaman konseptual tentang fungsi berbagai jenis diagram, bukan sekadar menghitung.. Bukti: Diagram apakah yang akan kalian gunakan untuk menunjukkan pengeluaran bulanan keluarga kalian untuk listrik selama 1 tahun?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang kapan harus menggunakan diagram garis dibandingkan diagram lainnya untuk merepresentasikan data.. Bukti: Diagram apakah yang akan kalian gunakan untuk menunjukkan pengeluaran bulanan keluarga kalian untuk listrik selama 1 tahun?
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan menguji pengetahuan dasar tentang representasi data yang umum diajarkan di kelas 7. Tidak ada langkah perhitungan atau integrasi kendala yang kompleks.. Bukti: Diagram apakah yang akan kalian gunakan untuk menunjukkan pengeluaran bulanan keluarga kalian untuk listrik selama 1 tahun?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang fungsi diagram batang, diagram lingkaran, dan diagram garis. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pemilihan diagram berdasarkan jenis data adalah materi standar kelas 7. Soal ini tidak menuntut analisis data yang kompleks, hanya pengenalan jenis grafik yang sesuai untuk data deret waktu. |

Run 3 — solusi: Data pengeluaran listrik bulanan selama satu tahun merupakan data kontinu yang berubah terhadap waktu (Januari-Desember). Diagram garis adalah representasi yang paling tepat untuk menunjukkan tren atau perubahan data numerik secara berurutan dalam rentang waktu tertentu.
- Domain kognitif `classify/applying`: Siswa diminta untuk memilih jenis representasi data yang tepat berdasarkan karakteristik data (data deret waktu/time series). Ini memerlukan pemahaman konseptual tentang fungsi berbagai jenis diagram, bukan sekadar prosedur menghitung.. Bukti: Diagram apakah yang akan kalian gunakan untuk menunjukkan pengeluaran bulanan keluarga kalian untuk listrik selama 1 tahun?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual mengenai kegunaan dan karakteristik berbagai jenis diagram statistik dalam merepresentasikan data.. Bukti: Diagram apakah yang akan kalian gunakan untuk menunjukkan pengeluaran bulanan keluarga kalian untuk listrik selama 1 tahun?
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan menguji pemahaman dasar tentang representasi data yang umum diajarkan di kelas 7. Tidak ada langkah perhitungan atau integrasi kendala yang kompleks.. Bukti: Diagram apakah yang akan kalian gunakan untuk menunjukkan pengeluaran bulanan keluarga kalian untuk listrik selama 1 tahun?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang jenis-jenis diagram (batang, garis, lingkaran) dan kegunaan umumnya. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Memilih diagram yang tepat untuk data deret waktu adalah materi standar kelas 7 yang bersifat konseptual dasar tanpa beban komputasi. |

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

![Gambar sumber soal 49](<../../../images/kelas5_panduan_siswa_kelas5.pdf-0282-04.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Hitung kalori: Nasi putih (300g) = 3 * 130 = 390 kkal. Daging ayam (200g) = 2 * 260 = 520 kkal. Sayuran hijau (100g) = 1 * 60 = 60 kkal. Tambahan: Makanan ringan = 300 kkal, Mi instan = 350 kkal. Total = 390 + 520 + 60 + 300 + 350 = 1.620 kkal. Karena 1.620 < 2.100, maka tidak berlebihan.
Gambar sumber: images/kelas5_panduan_siswa_kelas5.pdf-0282-04.png. Transkripsi visual: Diagram batang menunjukkan kandungan kalori per 100 gram makanan. Sumbu horizontal (Kalori kkal) memiliki garis kisi setiap 50 unit (0, 50, 100, 150, 200, 250, 300). Nilai per 100g: Nasi putih = 130 kkal, Daging ayam = 260 kkal, Sayuran hijau = 60 kkal.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 7 / Matematika SMP Kelas 7. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ecd49b33765922acba2e15bea23579438eb4d0dcfb57cb28ef138eea484d1c22`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 4067 |
| 2 | success | valid / verified | applying | procedural | Medium | 4036 |
| 3 | success | valid / verified | applying | procedural | Medium | 4076 |

Run 1 — solusi: Hitung kalori: Nasi putih (300g) = 3 * 130 = 390 kkal. Daging ayam (200g) = 2 * 260 = 520 kkal. Sayuran hijau (100g) = 1 * 60 = 60 kkal. Tambahan: Makanan ringan = 300 kkal, Mi instan = 350 kkal. Total = 390 + 520 + 60 + 300 + 350 = 1.620 kkal. Karena 1.620 < 2.100, maka tidak berlebihan.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep rasio/proporsi (skala per 100g) untuk menghitung total kalori dari berbagai jenis makanan, lalu membandingkannya dengan nilai ambang batas. Ini adalah penerapan prosedur matematika pada konteks kehidupan sehari-hari.. Bukti: Lukas makan 300 gram nasi putih, 200 gram daging ayam, dan 100 gram sayuran hijau; Kandungan Kalori Per 100 Gram Makanan; Apakah makanan yang dimakan Lukas kalorinya berlebihan?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur perhitungan aritmetika dasar yang diterapkan pada data yang disajikan secara visual (diagram batang) dan informasi tekstual.. Bukti: Diagram batang di atas menunjukkan kandungan kalori dari berbagai jenis makanan; Kebutuhan kalori anak usia 10–12 tahun adalah sekitar 2.000 kkal untuk anak perempuan dan 2.100 kkal untuk anak laki-laki
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah yang saling terkait: membaca data dari diagram, melakukan konversi satuan (per 100g), menjumlahkan berbagai sumber kalori, dan membandingkan hasil akhir dengan kriteria yang diberikan. Meskipun prosedurnya familiar, siswa harus mengelola beberapa informasi sekaligus tanpa urutan langkah yang eksplisit.. Bukti: Lukas makan 300 gram nasi putih, 200 gram daging ayam, dan 100 gram sayuran hijau; Ia masih makan makanan ringan yang mengandung 300 kkal dan 1 bungkus mi instan yang mengandung 350 kkal

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmetika dasar, membaca diagram batang, konsep rasio/proporsi sederhana. |
| dependentSteps | 5 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 7 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu membaca diagram dan melakukan perhitungan aritmetika bertahap. Soal ini menuntut ketelitian dalam mengintegrasikan data dari diagram dan teks. |

Run 2 — solusi: Hitung total kalori: (3 x 130 kkal nasi putih) + (2 x 260 kkal daging ayam) + (1 x 60 kkal sayuran) + 300 kkal makanan ringan + 350 kkal mi instan = 390 + 520 + 60 + 300 + 350 = 1.620 kkal. Bandingkan 1.620 kkal dengan kebutuhan 2.100 kkal. Karena 1.620 < 2.100, maka tidak berlebihan.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur membaca data dari diagram batang, melakukan operasi perkalian untuk menyesuaikan porsi (per 100g), dan menjumlahkan total kalori sebelum membandingkannya dengan nilai acuan. Ini adalah penerapan konsep dalam konteks rutin.. Bukti: Lukas makan 300 gram nasi putih, 200 gram daging ayam, dan 100 gram sayuran hijau; Diagram batang menunjukkan kandungan kalori dari berbagai jenis makanan. Kalori dihitung untuk setiap 100 gram makanan
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan prosedur aritmatika (perkalian dan penjumlahan) berdasarkan data yang disajikan dalam bentuk grafik.. Bukti: Diagram batang menunjukkan kandungan kalori dari berbagai jenis makanan; Kebutuhan kalori anak usia 10–12 tahun adalah sekitar 2.000 kkal untuk anak perempuan dan 2.100 kkal untuk anak laki-laki
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah yang saling terkait: membaca data dari grafik, melakukan konversi satuan (per 100g), dan menjumlahkan berbagai sumber kalori. Meskipun prosedurnya familiar, siswa harus mengintegrasikan beberapa informasi (data grafik, porsi makan, kalori tambahan) untuk mencapai kesimpulan.. Bukti: Lukas makan 300 gram nasi putih, 200 gram daging ayam, dan 100 gram sayuran hijau; Ia masih makan makanan ringan yang mengandung 300 kkal dan 1 bungkus mi instan yang mengandung 350 kkal per bungkus

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Membaca diagram batang, operasi perkalian dan penjumlahan bilangan bulat. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 7 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu membaca data dan melakukan operasi hitung dasar. Tantangan utama terletak pada ketelitian mengintegrasikan data dari grafik dengan informasi teks tambahan. |

Run 3 — solusi: Hitung kalori per makanan: Nasi putih (3 x 130 = 390), Daging ayam (2 x 260 = 520), Sayuran hijau (1 x 60 = 60). Tambahkan makanan lain: 300 (snack) + 350 (mi) = 650. Total = 390 + 520 + 60 + 650 = 1.620 kkal. Bandingkan dengan kebutuhan anak laki-laki (2.100 kkal). Karena 1.620 < 2.100, maka tidak berlebihan.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasikan data dari diagram batang, melakukan operasi perkalian berdasarkan porsi (skala per 100g), menjumlahkan total kalori, dan membandingkannya dengan nilai referensi. Ini adalah penerapan konsep data dan aritmatika dalam konteks rutin.. Bukti: Diagram batang di atas menunjukkan kandungan kalori dari berbagai jenis makanan.; Lukas makan 300 gram nasi putih, 200 gram daging ayam, dan 100 gram sayuran hijau.; Apakah makanan yang dimakan Lukas kalorinya berlebihan?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dalam membaca data diagram batang dan melakukan perhitungan aritmatika dasar untuk menyelesaikan masalah kontekstual.. Bukti: Diagram batang di atas menunjukkan kandungan kalori dari berbagai jenis makanan.; Kebutuhan kalori anak usia 10–12 tahun adalah sekitar 2.000 kkal untuk anak perempuan dan 2.100 kkal untuk anak laki-laki.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah yang saling terkait: membaca data dari grafik, melakukan perkalian untuk menyesuaikan porsi, menjumlahkan berbagai sumber kalori, dan membandingkan hasil akhir dengan ambang batas. Meskipun prosedurnya familiar, siswa harus mengelola beberapa informasi yang berbeda secara cermat.. Bukti: Lukas makan 300 gram nasi putih, 200 gram daging ayam, dan 100 gram sayuran hijau.; Ia masih makan makanan ringan yang mengandung 300 kkal dan 1 bungkus mi instan yang mengandung 350 kkal per bungkus.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Membaca diagram batang, operasi perkalian dan penjumlahan bilangan bulat. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 6 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 7 diharapkan mampu membaca diagram batang dan melakukan operasi aritmatika dasar. Kompleksitas muncul dari banyaknya data yang harus diintegrasikan (porsi makanan, kalori per 100g, tambahan kalori snack/mi) sebelum membuat kesimpulan. |

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
Transkripsi visual: Diagram batang menunjukkan kandungan kalori per 100 gram makanan. Sumbu horizontal (Kalori kkal) memiliki garis kisi setiap 50 unit (0, 50, 100, 150, 200, 250, 300). Nilai per 100g: Nasi putih = 130 kkal, Daging ayam = 260 kkal, Sayuran hijau = 60 kkal.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
