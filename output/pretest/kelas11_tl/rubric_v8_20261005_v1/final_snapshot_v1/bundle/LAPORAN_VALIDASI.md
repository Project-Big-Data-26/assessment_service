# Validasi ulang soal kelas 11 TL — Gemini blind N=3 dan diagnostik IndoBERT

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v10-blind-sma11-tl-key-verified`. Rubrik: `math-rubric-3x4x3-v8-sma11-tl-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 11 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan menjadi keputusan silver operasional.

Checkpoint dikunci dengan SHA-256 sebelum pemeriksaan scope IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Artifact berada di luar cakupan kelas 11 TL, sehingga seluruh head abstain dan tidak menghasilkan ukuran agreement dengan label blind.

Jumlah soal: 55; distribusi label advisory: `{"mathCognitiveDomain": {"knowing": 24, "applying": 29, "reasoning": 2}, "knowledgeDimension": {"factual": 5, "conceptual": 22, "procedural": 28, "metacognitive": 0}, "intendedDifficulty": {"Easy": 46, "Medium": 8, "Hard": 1}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"knowing": 24, "applying": 29, "reasoning": 2}, "knowledgeDimension": {"factual": 5, "conceptual": 22, "procedural": 28, "metacognitive": 0}, "intendedDifficulty": {"Easy": 46, "Medium": 8, "Hard": 1}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"silver_ready": 55}`.
Run awal sukses: 165/165; adjudikasi: 18; token sukses tercatat: 565,434.

Seluruh label memakai provenance ai_silver. Delivery memakai snapshot silver yang lolos qualification. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

Artifact diagnostik IndoBERT: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Dataset training: `kelas1-gemini-silver-n3-v1`. Approval provisional: `False`; research-only: `False`; gate data: `False`; anti-collapse: `False`; gate promosi: `False`. Packaging ini tidak melakukan training atau promosi model.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten dapat masuk snapshot silver operasional.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 46 | 46 | [Easy.json](difficulty/Easy.json) |
| Medium | 8 | 8 | [Medium.json](difficulty/Medium.json) |
| Hard | 1 | 1 | [Hard.json](difficulty/Hard.json) |

## Perhitungan yang dipakai

Untuk kelas 11 TL, encoder dan head IndoBERT tidak dijalankan karena cakupan artifact adalah kelas [1, 2, 3, 4, 5, 6], jalur ['regular']. Probabilitas kosong, label/confidence/entropy null, dan action abstain berasal dari pemeriksaan scope runtime. Suara Gemini adalah bukti penilaian advisory, bukan probabilitas IndoBERT.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

Cakupan artifact: kelas [1, 2, 3, 4, 5, 6], jalur ['regular']. Untuk kelas 11 TL, diagnostik mengembalikan `out_of_scope` dan `abstain`: label, confidence, dan entropy null serta probabilitas kosong. Label advisory mengikuti Gemini blind dengan rubrik SMA kelas 11.

## 1. Soal `6678eff0f2f3f2aa21d884b8`

$A = \begin{bmatrix} -3 & 2 & 0 \\ 1 & 3 & 5 \end{bmatrix}$<br><br>Tentukan jenis matriks-matriks berikut.

| Opsi | Isi |
|---|---|
| A | Matriks datar |
| B | Matriks persegi |
| C | Matriks segitiga atas |
| D | Matriks tegak |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Matriks A memiliki 2 baris dan 3 kolom. Karena jumlah baris (2) lebih kecil dari jumlah kolom (3), maka matriks A diklasifikasikan sebagai matriks datar.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `01f936dbea3f99decd96d56447c3ea39b5cd31421bf2c6de681da20be92ac78c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 3674 |
| 2 | success | valid / verified | knowing | factual | Easy | 4088 |
| 3 | success | valid / verified | knowing | factual | Easy | 2644 |

Run 1 — solusi: Matriks A memiliki 2 baris dan 3 kolom. Karena jumlah baris (2) lebih kecil dari jumlah kolom (3), maka matriks A diklasifikasikan sebagai matriks datar.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali definisi jenis matriks berdasarkan ordo (baris dan kolom) dan mencocokkannya dengan pilihan jawaban yang tersedia tanpa memerlukan langkah prosedural yang kompleks.. Bukti: Tentukan jenis matriks-matriks berikut.; A = \begin{bmatrix} -3 & 2 & 0 \\ 1 & 3 & 5 \end{bmatrix}
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman terhadap terminologi dasar dan definisi jenis-jenis matriks.. Bukti: Tentukan jenis matriks-matriks berikut.
- Intended difficulty `classify/Easy`: Soal bersifat langsung (direct recall) mengenai definisi matriks. Tidak ada langkah perencanaan, integrasi konsep, atau kendala yang berinteraksi.. Bukti: A = \begin{bmatrix} -3 & 2 & 0 \\ 1 & 3 & 5 \end{bmatrix}

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang baris dan kolom matriks. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini merupakan dasar pengenalan matriks yang sangat sederhana untuk kelas 11. |

Run 2 — solusi: Matriks A memiliki 2 baris dan 3 kolom (ordo 2x3). Karena jumlah baris (2) lebih kecil dari jumlah kolom (3), maka matriks A dikategorikan sebagai matriks datar.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali definisi jenis matriks berdasarkan ordo matriks yang diberikan tanpa memerlukan proses analisis atau penalaran kompleks.. Bukti: A = \begin{bmatrix} -3 & 2 & 0 \\ 1 & 3 & 5 \end{bmatrix}; Tentukan jenis matriks-matriks berikut.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman terhadap terminologi dasar (faktual) mengenai klasifikasi matriks.. Bukti: Tentukan jenis matriks-matriks berikut.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar. Siswa hanya perlu menghitung jumlah baris dan kolom lalu mencocokkannya dengan definisi yang sudah dipelajari. Tidak ada langkah perencanaan atau integrasi yang kompleks.. Bukti: A = \begin{bmatrix} -3 & 2 & 0 \\ 1 & 3 & 5 \end{bmatrix}; Tentukan jenis matriks-matriks berikut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi ordo matriks dan jenis-jenis matriks dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini merupakan pengenalan dasar matriks di kelas 11. Soal tidak menuntut analisis mendalam, hanya pengenalan istilah. |

Run 3 — solusi: Matriks A memiliki 2 baris dan 3 kolom (ordo 2x3). Karena jumlah baris (2) kurang dari jumlah kolom (3), maka matriks A diklasifikasikan sebagai matriks datar.
- Domain kognitif `classify/knowing`: Siswa diminta mengenali definisi jenis matriks berdasarkan ordo yang diberikan. Ini adalah tugas pengenalan fakta/definisi dasar.. Bukti: Tentukan jenis matriks-matriks berikut.; A = \begin{bmatrix} -3 & 2 & 0 \\ 1 & 3 & 5 \end{bmatrix}
- Dimensi pengetahuan `classify/factual`: Soal menguji pemahaman terhadap terminologi dan definisi dasar dalam materi matriks (matriks datar).. Bukti: Tentukan jenis matriks-matriks berikut.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar. Siswa hanya perlu menghitung jumlah baris dan kolom lalu mencocokkannya dengan definisi matriks datar. Tidak ada langkah kompleks atau integrasi konsep.. Bukti: A = \begin{bmatrix} -3 & 2 & 0 \\ 1 & 3 & 5 \end{bmatrix}; Tentukan jenis matriks-matriks berikut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang baris dan kolom pada matriks. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah materi pengenalan awal matriks di kelas 11, sehingga tingkat kesulitannya rendah. |

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
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: $A = \begin{bmatrix} -3 & 2 & 0 \\ 1 & 3 & 5 \end{bmatrix}$

Tentukan jenis matriks-matriks berikut.
Pilihan: A. Matriks datar
B. Matriks persegi
C. Matriks segitiga atas
D. Matriks tegak
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "factual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `e2ffe980242e563b18f54620`

$B = \begin{bmatrix} 2 & 9 & -1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{bmatrix}$<br><br>Tentukan jenis matriks-matriks berikut.

| Opsi | Isi |
|---|---|
| A | Matriks segitiga atas |
| B | Matriks segitiga bawah |
| C | Matriks diagonal |
| D | Matriks identitas |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Matriks B adalah matriks persegi 3x3. Elemen-elemen di bawah diagonal utama (a21, a31, a32) semuanya bernilai 0. Berdasarkan definisi, matriks persegi dengan semua elemen di bawah diagonal utama bernilai nol adalah matriks segitiga atas.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9115523f2c97208ab7063ef661dece417ed402681865ecfab0735c402f8801a3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2753 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2697 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2738 |

Run 1 — solusi: Matriks B adalah matriks persegi 3x3. Elemen-elemen di bawah diagonal utama (a21, a31, a32) semuanya bernilai 0. Berdasarkan definisi, matriks persegi dengan semua elemen di bawah diagonal utama bernilai nol adalah matriks segitiga atas.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi jenis matriks berdasarkan definisi formal. Siswa hanya perlu mengenali pola elemen nol di bawah diagonal utama, yang merupakan prosedur langsung dalam materi matriks kelas 11.. Bukti: Tentukan jenis matriks-matriks berikut.; B = \begin{bmatrix} 2 & 9 & -1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{bmatrix}
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap definisi atau terminologi dasar dalam matriks (matriks segitiga atas), yang termasuk dalam kategori pengetahuan konseptual.. Bukti: Tentukan jenis matriks-matriks berikut.; B = \begin{bmatrix} 2 & 9 & -1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{bmatrix}
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan tidak memerlukan langkah-langkah perhitungan atau perencanaan strategi yang kompleks. Siswa hanya perlu mencocokkan struktur matriks dengan definisi yang sudah dipelajari.. Bukti: Tentukan jenis matriks-matriks berikut.; B = \begin{bmatrix} 2 & 9 & -1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{bmatrix}

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi matriks segitiga atas dan pemahaman tentang diagonal utama. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal pengenalan konsep dasar matriks yang sangat standar untuk kelas 11, tidak memerlukan analisis mendalam atau manipulasi aljabar. |

Run 2 — solusi: Matriks B adalah matriks persegi 3x3. Elemen-elemen di bawah diagonal utama (b_21, b_31, b_32) semuanya bernilai 0. Berdasarkan definisi, matriks persegi yang semua elemen di bawah diagonal utamanya adalah nol disebut matriks segitiga atas.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi jenis matriks berdasarkan definisi formal. Siswa hanya perlu mengenali pola elemen nol di bawah diagonal utama, yang merupakan prosedur langsung dalam pengenalan jenis matriks.. Bukti: Tentukan jenis matriks-matriks berikut.; B = [2 9 -1; 0 1 2; 0 0 1]
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman terhadap definisi atau terminologi dasar dalam matriks (matriks segitiga atas), yang termasuk dalam kategori pengetahuan konseptual.. Bukti: Tentukan jenis matriks-matriks berikut.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin. Siswa hanya perlu memeriksa elemen di bawah diagonal utama. Tidak ada langkah perencanaan, integrasi konsep, atau kendala yang saling berinteraksi.. Bukti: B = [2 9 -1; 0 1 2; 0 0 1]; Tentukan jenis matriks-matriks berikut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi matriks segitiga atas dan pemahaman letak diagonal utama pada matriks 3x3. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi pengenalan jenis matriks adalah materi dasar di awal bab matriks kelas 11. Soal ini tidak memerlukan manipulasi aljabar, hanya pengamatan visual terhadap elemen matriks. |

Run 3 — solusi: Matriks B memiliki elemen-elemen di bawah diagonal utama yang semuanya bernilai nol (b_21=0, b_31=0, b_32=0). Berdasarkan definisi, matriks persegi yang semua elemen di bawah diagonal utamanya adalah nol disebut matriks segitiga atas.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi jenis matriks berdasarkan definisi formal matriks segitiga atas. Proses ini melibatkan pengenalan pola elemen matriks (elemen di bawah diagonal utama adalah nol) dan mencocokkannya dengan definisi yang sudah dipelajari.. Bukti: Tentukan jenis matriks-matriks berikut.; B = \begin{bmatrix} 2 & 9 & -1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{bmatrix}
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap definisi konseptual dari jenis-jenis matriks (segitiga atas, segitiga bawah, diagonal, identitas).. Bukti: Tentukan jenis matriks-matriks berikut.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin. Siswa hanya perlu memeriksa elemen di bawah diagonal utama untuk mengklasifikasikan matriks. Tidak ada langkah perencanaan yang kompleks atau integrasi konsep yang sulit.. Bukti: B = \begin{bmatrix} 2 & 9 & -1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{bmatrix}; Tentukan jenis matriks-matriks berikut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi matriks segitiga atas dan struktur matriks persegi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi matriks adalah dasar kelas 11. Mengidentifikasi jenis matriks segitiga atas adalah prosedur standar yang sangat dasar dan familiar bagi siswa kelas 11. |

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
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Jenis-Jenis Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: $B = \begin{bmatrix} 2 & 9 & -1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{bmatrix}$

Tentukan jenis matriks-matriks berikut.
Pilihan: A. Matriks segitiga atas
B. Matriks segitiga bawah
C. Matriks diagonal
D. Matriks identitas
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `27a811fca5ea09e854337780`

Jika $A = \begin{bmatrix} -x-3y & 0 \\ (x-2y)^2 & 1 \end{bmatrix}$ dan $I$ adalah matriks identitas berordo 2 × 2 dengan $A = I$.<br><br>Tentukan nilai x + y.

| Opsi | Isi |
|---|---|
| A | -3/5 |
| B | -2/5 |
| C | 3/5 |
| D | -1/5 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Dari A=I, diperoleh -x-3y=1 dan (x-2y)^2=0. Dari (x-2y)^2=0, didapat x=2y. Substitusi ke -x-3y=1 menjadi -(2y)-3y=1, sehingga -5y=1 atau y=-1/5. Maka x=2(-1/5)=-2/5. Nilai x+y = -2/5 + (-1/5) = -3/5.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `985ac196d8963bc159260ad644f4bf57709dcfdc265c39a79f63fcbe52f7f6ed`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3611 |
| 2 | success | valid / verified | applying | procedural | Easy | 3592 |
| 3 | success | valid / verified | applying | procedural | Easy | 3621 |

Run 1 — solusi: Dari A=I, diperoleh -x-3y=1 dan (x-2y)^2=0. Dari (x-2y)^2=0, didapat x=2y. Substitusi ke -x-3y=1 menjadi -(2y)-3y=1, sehingga -5y=1 atau y=-1/5. Maka x=2(-1/5)=-2/5. Nilai x+y = -2/5 + (-1/5) = -3/5.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep kesamaan dua matriks untuk membentuk sistem persamaan linear dan menyelesaikannya. Prosedur ini rutin bagi siswa kelas 11.. Bukti: A = I; -x-3y = 1; (x-2y)^2 = 0
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma penyelesaian sistem persamaan linear yang diturunkan dari definisi kesamaan matriks.. Bukti: A = I; kesamaan dua matriks
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang jelas. Siswa hanya perlu menyamakan elemen-elemen matriks yang bersesuaian, membentuk sistem persamaan, dan menyelesaikannya. Tidak ada kendala yang berinteraksi secara kompleks atau kebutuhan untuk strategi non-rutin.. Bukti: A = I; Tentukan nilai x + y

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sistem Persamaan Linear Dua Variabel (SPLDV) dan definisi kesamaan matriks. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kesamaan matriks adalah dasar kelas 11. Langkah penyelesaian sangat langsung dan familiar bagi siswa. |

Run 2 — solusi: Dari kesamaan matriks A=I, diperoleh (x-2y)^2=0 sehingga x=2y. Substitusi ke -x-3y=1 menghasilkan -2y-3y=1, maka -5y=1 atau y=-1/5. Didapat x=2(-1/5)=-2/5. Maka x+y = -2/5 - 1/5 = -3/5.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan definisi kesamaan matriks untuk membentuk sistem persamaan linear, lalu menyelesaikan sistem tersebut. Ini adalah prosedur rutin dalam aljabar matriks.. Bukti: A = I; kesamaan matriks; Tentukan nilai x + y
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang konsep kesamaan dua matriks dan prosedur penyelesaian sistem persamaan linear yang dihasilkan.. Bukti: kesamaan matriks; A = I
- Intended difficulty `classify/Easy`: Soal ini melibatkan dua langkah utama: menyusun sistem persamaan dari kesamaan matriks dan menyelesaikannya. Prosedur ini familiar bagi siswa kelas 11. Tidak ada kendala yang saling berinteraksi secara kompleks.. Bukti: A = I; (x-2y)^2 = 0; -x-3y = 1

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sistem Persamaan Linear Dua Variabel (SPLDV) dan definisi kesamaan matriks. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan langsung dari definisi kesamaan matriks dan SPLDV yang merupakan prasyarat atau materi dasar kelas 11. Langkah penyelesaiannya jelas dan tidak memerlukan strategi non-rutin. |

Run 3 — solusi: Dari A=I, elemen (2,1) memberikan (x-2y)^2=0, sehingga x=2y. Elemen (1,1) memberikan -x-3y=1. Substitusi x=2y ke -x-3y=1 menghasilkan -2y-3y=1, -5y=1, y=-1/5. Maka x=2(-1/5)=-2/5. Nilai x+y = -2/5 + (-1/5) = -3/5.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan definisi kesamaan matriks untuk membentuk sistem persamaan linear dan menyelesaikannya. Ini adalah prosedur rutin dalam topik matriks.. Bukti: A = I; Tentukan nilai x + y
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang definisi kesamaan dua matriks dan prosedur aljabar untuk menyelesaikan sistem persamaan.. Bukti: A = I; Tentukan nilai x + y
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu menyamakan elemen-elemen matriks yang bersesuaian, membentuk sistem persamaan linear dua variabel, dan menyelesaikannya. Tidak ada kendala yang kompleks atau kebutuhan strategi non-rutin.. Bukti: A = I; Tentukan nilai x + y

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sistem persamaan linear dua variabel (SPLDV) dan definisi kesamaan matriks. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini merupakan dasar dalam topik matriks kelas 11. Prosedur penyelesaian sangat langsung dan familiar. |

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
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika $A = \begin{bmatrix} -x-3y & 0 \\ (x-2y)^2 & 1 \end{bmatrix}$ dan $I$ adalah matriks identitas berordo 2 × 2 dengan $A = I$.

Tentukan nilai x + y.
Pilihan: A. -3/5
B. -2/5
C. 3/5
D. -1/5
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `03611fdcdc9bcd66f72bdce7`

$\begin{bmatrix} a+2b & 2a+b \\ c+d & 2c+d \end{bmatrix} = \begin{bmatrix} 3 & -3 \\ 7 & 1 \end{bmatrix}$<br><br>Hitunglah nilai a + b + c + d yang memenuhi kesamaan matriks berikut.

| Opsi | Isi |
|---|---|
| A | 7 |
| B | 13 |
| C | -7 |
| D | 1 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `7`.
Solusi minimum hasil AI: Dari kesamaan matriks: (1) a+2b=3 dan 2a+b=-3. Jumlahkan: 3a+3b=0 -> a+b=0. (2) c+d=7 dan 2c+d=1. Kurangkan: c=-6. Substitusi ke c+d=7: -6+d=7 -> d=13. Maka a+b+c+d = (a+b) + c + d = 0 + (-6) + 13 = 7.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `499b80c65ba0b7a9e90cd540920d0295d7a703be9616a86ae5de83cb2c46ea7f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2829 |
| 2 | success | valid / verified | applying | procedural | Medium | 2935 |
| 3 | success | valid / verified | applying | procedural | Medium | 2853 |

Run 1 — solusi: Dari kesamaan matriks: (1) a+2b=3 dan 2a+b=-3. Jumlahkan: 3a+3b=0 -> a+b=0. (2) c+d=7 dan 2c+d=1. Kurangkan: c=-6. Substitusi ke c+d=7: -6+d=7 -> d=13. Maka a+b+c+d = (a+b) + c + d = 0 + (-6) + 13 = 7.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur sistem persamaan linear dua variabel (SPLDV) untuk dua pasang sistem yang berbeda, lalu menjumlahkan hasilnya. Ini adalah penerapan prosedur rutin pada konteks matriks.. Bukti: a+2b=3 dan 2a+b=-3; c+d=7 dan 2c+d=1; Hitunglah nilai a + b + c + d
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang definisi kesamaan matriks (konseptual) dan kemampuan menjalankan algoritma eliminasi/substitusi (prosedural).. Bukti: kesamaan matriks; a+2b=3 dan 2a+b=-3
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua set sistem persamaan linear yang harus diselesaikan secara terpisah sebelum dijumlahkan. Meskipun prosedurnya rutin, terdapat beberapa langkah yang saling terkait dan potensi kesalahan kalkulasi yang cukup untuk tingkat kelas 11.. Bukti: a+2b=3 dan 2a+b=-3; c+d=7 dan 2c+d=1; Hitunglah nilai a + b + c + d

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | SPLDV (Sistem Persamaan Linear Dua Variabel) |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 diharapkan mampu menyelesaikan SPLDV dengan cepat. Soal ini menuntut ketelitian dalam mengelola dua sistem persamaan sekaligus, yang merupakan tuntutan standar untuk materi matriks. |

Run 2 — solusi: Dari kesamaan matriks, diperoleh dua sistem persamaan linear: (1) a+2b=3 dan 2a+b=-3, (2) c+d=7 dan 2c+d=1. Dari (1), (a+2b)+(2a+b)=3+(-3) => 3(a+b)=0 => a+b=0. Dari (2), (c+d)+(2c+d)=7+1 => 3c+2d=8. Namun, lebih mudah mencari nilai variabel: (1) 2(a+2b)-(2a+b)=2(3)-(-3) => 3b=9 => b=3, a=-3. (2) 2(c+d)-(2c+d)=2(7)-1 => d=13, c=-6. Maka a+b+c+d = -3+3-6+13 = 7.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur sistem persamaan linear dua variabel (SPLDV) untuk menyelesaikan dua sistem terpisah yang diturunkan dari definisi kesamaan matriks, kemudian menjumlahkan hasilnya.. Bukti: a+2b=3 dan 2a+b=-3; c+d=7 dan 2c+d=1; Hitunglah nilai a + b + c + d
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman tentang konsep kesamaan matriks (konseptual) dan penerapan algoritma eliminasi/substitusi SPLDV (prosedural).. Bukti: kesamaan matriks; a+2b=3 dan 2a+b=-3
- Intended difficulty `classify/Medium`: Soal memerlukan penyelesaian dua sistem persamaan linear dua variabel yang terpisah. Prosedur ini rutin bagi siswa kelas 11, namun memerlukan ketelitian dalam pengerjaan dua sistem sekaligus dan penjumlahan akhir. Tidak ada kendala yang saling berinteraksi secara kompleks.. Bukti: a+2b=3 dan 2a+b=-3; c+d=7 dan 2c+d=1; Hitunglah nilai a + b + c + d

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | SPLDV (Sistem Persamaan Linear Dua Variabel) |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun topiknya adalah matriks, inti penyelesaiannya adalah SPLDV yang merupakan prasyarat. Soal ini dikategorikan Medium karena siswa harus mengelola dua sistem persamaan terpisah secara akurat untuk mencapai jawaban akhir, yang meningkatkan beban kerja dibandingkan soal satu variabel. |

Run 3 — solusi: Dari kesamaan matriks: (1) a+2b=3 dan 2a+b=-3. Jumlahkan: 3a+3b=0 -> a+b=0. (2) c+d=7 dan 2c+d=1. Kurangkan: (2c+d)-(c+d)=1-7 -> c=-6. Substitusi c ke c+d=7: -6+d=7 -> d=13. Maka c+d=7. Hasil a+b+c+d = (a+b) + (c+d) = 0 + 7 = 7.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur sistem persamaan linear dua variabel (SPLDV) untuk dua pasang sistem yang berbeda, kemudian menjumlahkan hasilnya. Ini adalah penerapan prosedur rutin pada konteks matriks.. Bukti: a+2b=3 dan 2a+b=-3; c+d=7 dan 2c+d=1; Hitunglah nilai a + b + c + d
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang definisi kesamaan dua matriks dan penggunaan metode eliminasi/substitusi (prosedural) untuk menyelesaikan sistem persamaan yang dihasilkan.. Bukti: kesamaan matriks; a+2b=3 dan 2a+b=-3
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena meskipun prosedurnya rutin (SPLDV), siswa harus mengelola dua sistem persamaan terpisah secara akurat dan melakukan operasi penjumlahan akhir. Tidak ada jebakan konseptual yang kompleks, namun memerlukan ketelitian dalam langkah-langkah yang saling terkait.. Bukti: a+2b=3 dan 2a+b=-3; c+d=7 dan 2c+d=1; Hitunglah nilai a + b + c + d

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | SPLDV (Sistem Persamaan Linear Dua Variabel) |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kesamaan matriks adalah dasar kelas 11. Soal menuntut ketelitian dalam menyelesaikan dua sistem persamaan linear sederhana secara paralel, yang merupakan standar kemampuan kelas 11. |

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
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesamaan Dua Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: $\begin{bmatrix} a+2b & 2a+b \\ c+d & 2c+d \end{bmatrix} = \begin{bmatrix} 3 & -3 \\ 7 & 1 \end{bmatrix}$

Hitunglah nilai a + b + c + d yang memenuhi kesamaan matriks berikut.
Pilihan: A. 7
B. 13
C. -7
D. 1
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `5b5856cb7882715fb808648e`

$\begin{bmatrix} 2x & y \\ 3z & z \end{bmatrix} - \begin{bmatrix} 6 & -x \\ 2y & 7 \end{bmatrix} + \begin{bmatrix} 2 & 1 \\ -9 & 6 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$<br><br>Tentukan $x, y$, dan $z$.

| Opsi | Isi |
|---|---|
| A | x = -2, y = -3, z = 1 |
| B | x = 2, y = -3, z = 1 |
| C | x = 2, y = 3, z = 1 |
| D | x = 2, y = -3, z = -1 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Dari elemen (1,1): 2x - 6 + 2 = 0 => 2x = 4 => x = 2. Dari elemen (1,2): y - (-x) + 1 = 0 => y + 2 + 1 = 0 => y = -3. Dari elemen (2,2): z - 7 + 6 = 0 => z = 1. (Cek elemen (2,1): 3z - 2y - 9 = 3(1) - 2(-3) - 9 = 3 + 6 - 9 = 0. Konsisten).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `121d94d0fa01d172170eb7434ea6186ecdd565f3dc8c47930f52e45c1e8bfb9c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2903 |
| 2 | success | valid / verified | applying | procedural | Easy | 2881 |
| 3 | success | valid / verified | applying | procedural | Easy | 2914 |

Run 1 — solusi: Dari elemen (1,1): 2x - 6 + 2 = 0 => 2x = 4 => x = 2. Dari elemen (1,2): y - (-x) + 1 = 0 => y + 2 + 1 = 0 => y = -3. Dari elemen (2,2): z - 7 + 6 = 0 => z = 1. (Cek elemen (2,1): 3z - 2y - 9 = 3(1) - 2(-3) - 9 = 3 + 6 - 9 = 0. Konsisten).
- Domain kognitif `classify/applying`: Siswa hanya perlu menerapkan prosedur penjumlahan dan pengurangan matriks secara langsung untuk membentuk sistem persamaan linear sederhana dan menyelesaikannya.. Bukti: 2x - 6 + 2 = 0; y - (-x) + 1 = 0; z - 7 + 6 = 0
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi matriks dan penyelesaian sistem persamaan linear.. Bukti: 2x - 6 + 2 = 0; y - (-x) + 1 = 0; z - 7 + 6 = 0
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan langkah-langkah yang jelas dan langsung. Tidak ada kendala yang berinteraksi secara kompleks atau kebutuhan untuk strategi non-rutin.. Bukti: 2x - 6 + 2 = 0; y - (-x) + 1 = 0; z - 7 + 6 = 0

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi dasar matriks dan penyelesaian SPLDV sederhana. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi matriks adalah dasar kelas 11. Soal ini hanya memerlukan manipulasi aljabar dasar tanpa kompleksitas tambahan. |

Run 2 — solusi: Dari elemen (1,1): 2x - 6 + 2 = 0 => 2x = 4 => x = 2. Dari elemen (1,2): y - (-x) + 1 = 0 => y + 2 + 1 = 0 => y = -3. Dari elemen (2,2): z - 7 + 6 = 0 => z - 1 = 0 => z = 1. (Cek elemen (2,1): 3z - 2y - 9 = 3(1) - 2(-3) - 9 = 3 + 6 - 9 = 0, konsisten).
- Domain kognitif `classify/applying`: Siswa hanya perlu menerapkan prosedur rutin penjumlahan dan pengurangan matriks serta menyelesaikan sistem persamaan linear sederhana yang muncul dari kesamaan elemen matriks.. Bukti: 2x - 6 + 2 = 0; y - (-x) + 1 = 0; z - 7 + 6 = 0
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi matriks dan penyelesaian persamaan linear.. Bukti: penjumlahan dan pengurangan antarmatriks
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan langkah-langkah yang jelas dan langsung. Tidak ada kendala yang berinteraksi secara kompleks atau kebutuhan untuk strategi non-rutin.. Bukti: 2x - 6 + 2 = 0; y - (-x) + 1 = 0; z - 7 + 6 = 0

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi dasar matriks dan penyelesaian SPLDV sederhana. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi matriks adalah dasar kelas 11. Soal ini hanya memerlukan manipulasi aljabar dasar tanpa kompleksitas tambahan. |

Run 3 — solusi: Dari elemen (1,1): 2x - 6 + 2 = 0 => 2x = 4 => x = 2. Dari elemen (1,2): y - (-x) + 1 = 0 => y + 2 + 1 = 0 => y = -3. Dari elemen (2,2): z - 7 + 6 = 0 => z - 1 = 0 => z = 1. (Cek elemen (2,1): 3z - 2y - 9 = 3(1) - 2(-3) - 9 = 3 + 6 - 9 = 0, konsisten).
- Domain kognitif `classify/applying`: Siswa hanya perlu menerapkan prosedur rutin penjumlahan dan pengurangan matriks untuk membentuk sistem persamaan linear sederhana dan menyelesaikannya.. Bukti: 2x - 6 + 2 = 0; y - (-x) + 1 = 0; z - 7 + 6 = 0
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi matriks dan penyelesaian sistem persamaan linear.. Bukti: 2x - 6 + 2 = 0; y - (-x) + 1 = 0; z - 7 + 6 = 0
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan langkah-langkah yang jelas dan langsung. Tidak ada kendala yang berinteraksi secara kompleks atau kebutuhan untuk strategi non-rutin.. Bukti: 2x - 6 + 2 = 0; y - (-x) + 1 = 0; z - 7 + 6 = 0

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi dasar matriks dan penyelesaian SPLDV sederhana. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi matriks adalah dasar kelas 11. Soal ini adalah penerapan langsung definisi operasi matriks tanpa modifikasi atau integrasi konsep yang sulit. |

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
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: $\begin{bmatrix} 2x & y \\ 3z & z \end{bmatrix} - \begin{bmatrix} 6 & -x \\ 2y & 7 \end{bmatrix} + \begin{bmatrix} 2 & 1 \\ -9 & 6 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$

Tentukan $x, y$, dan $z$.
Pilihan: A. x = -2, y = -3, z = 1
B. x = 2, y = -3, z = 1
C. x = 2, y = 3, z = 1
D. x = 2, y = -3, z = -1
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `c44f54983cee8c0e1a20ffb3`

$\begin{bmatrix} 3a \\ 3b \end{bmatrix}+\begin{bmatrix} 4b \\ 4a \end{bmatrix}=\begin{bmatrix} 1 \\ -1 \end{bmatrix}$<br><br>Tentukan $a$ dan $b$.

| Opsi | Isi |
|---|---|
| A | a = -1, b = -1 |
| B | a = 1, b = -1 |
| C | a = -1, b = 1 |
| D | a = 1, b = 1 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `a = -1, b = 1`.
Solusi minimum hasil AI: Persamaan matriks menghasilkan sistem: (1) 3a + 4b = 1 dan (2) 4a + 3b = -1. Kalikan (1) dengan 3 dan (2) dengan 4: 9a + 12b = 3 dan 16a + 12b = -4. Kurangi (2) dengan (1): 7a = -7, sehingga a = -1. Substitusi a = -1 ke (1): 3(-1) + 4b = 1, maka 4b = 4, sehingga b = 1.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d862a2d3f61b001c00384465b90471ea3d26e1222dd96b186525ec578e6a91e1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2779 |
| 2 | success | valid / verified | applying | procedural | Easy | 2769 |
| 3 | success | valid / verified | applying | procedural | Easy | 2766 |

Run 1 — solusi: Persamaan matriks menghasilkan sistem: (1) 3a + 4b = 1 dan (2) 4a + 3b = -1. Kalikan (1) dengan 3 dan (2) dengan 4: 9a + 12b = 3 dan 16a + 12b = -4. Kurangi (2) dengan (1): 7a = -7, sehingga a = -1. Substitusi a = -1 ke (1): 3(-1) + 4b = 1, maka 4b = 4, sehingga b = 1.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan persamaan matriks menjadi sistem persamaan linear dua variabel (SPLDV) dan menerapkan prosedur eliminasi/substitusi yang rutin untuk menyelesaikannya.. Bukti: 3a + 4b = 1; 3b + 4a = -1
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman tentang definisi penjumlahan matriks dan penerapan algoritma penyelesaian SPLDV.. Bukti: 3a + 4b = 1; 3b + 4a = -1
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari definisi penjumlahan matriks yang menghasilkan SPLDV standar. Tidak ada kendala kompleks atau kebutuhan strategi non-rutin.. Bukti: 3a + 4b = 1; 3b + 4a = -1

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan matriks dan penyelesaian SPLDV (materi prasyarat kelas 10/11). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun berada di kelas 11, soal ini hanya menguji kemampuan dasar aljabar dan matriks yang sudah familiar bagi siswa, sehingga dikategorikan mudah. |

Run 2 — solusi: Persamaan matriks menghasilkan sistem linear: 3a + 4b = 1 dan 4a + 3b = -1. Kalikan (1) dengan 3 dan (2) dengan 4: 9a + 12b = 3 dan 16a + 12b = -4. Kurangi kedua persamaan: -7a = 7, sehingga a = -1. Substitusi a = -1 ke 3(-1) + 4b = 1, maka -3 + 4b = 1, 4b = 4, b = 1.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan persamaan matriks menjadi sistem persamaan linear dua variabel (SPLDV) dan menerapkan prosedur eliminasi/substitusi yang rutin untuk menyelesaikannya.. Bukti: 3a + 4b = 1; 3b + 4a = -1
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi matriks dan metode penyelesaian sistem persamaan linear.. Bukti: 3a + 4b = 1; 3b + 4a = -1
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 11. Langkah-langkahnya jelas: menjumlahkan matriks, membentuk sistem persamaan, dan menyelesaikannya dengan metode standar.. Bukti: 3a + 4b = 1; 3b + 4a = -1

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi penjumlahan matriks dan penyelesaian SPLDV. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi matriks dan SPLDV adalah prasyarat dasar yang sudah dikuasai siswa kelas 11. Tidak ada tuntutan integrasi konsep yang kompleks. |

Run 3 — solusi: Dari penjumlahan matriks, diperoleh sistem persamaan linear: (1) 3a + 4b = 1 dan (2) 4a + 3b = -1. Kalikan (1) dengan 3 dan (2) dengan 4: 9a + 12b = 3 dan 16a + 12b = -4. Kurangi kedua persamaan: -7a = 7, sehingga a = -1. Substitusi a = -1 ke (1): 3(-1) + 4b = 1, maka 4b = 4, sehingga b = 1.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan operasi matriks ke dalam sistem persamaan linear dua variabel (SPLDV) dan menyelesaikannya. Ini adalah penerapan prosedur rutin yang sudah dipelajari sebelumnya.. Bukti: 3a + 4b = 1; 3b + 4a = -1
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman tentang definisi penjumlahan matriks dan metode penyelesaian sistem persamaan linear (prosedural).. Bukti: 3a + 4b = 1; 4a + 3b = -1
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari definisi penjumlahan matriks yang menghasilkan SPLDV standar. Tidak ada kendala kompleks atau kebutuhan strategi non-rutin.. Bukti: 3a + 4b = 1; 4a + 3b = -1

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan matriks dan metode eliminasi/substitusi SPLDV. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun berada di kelas 11, materi ini merupakan prasyarat dasar matriks yang sangat rutin bagi siswa SMA. |

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
Subtopik: Penjumlahan dan Pengurangan Antarmatriks
Tipe soal: multiple_choice
Stimulus: -
Soal: $\begin{bmatrix} 3a \\ 3b \end{bmatrix}+\begin{bmatrix} 4b \\ 4a \end{bmatrix}=\begin{bmatrix} 1 \\ -1 \end{bmatrix}$

Tentukan $a$ dan $b$.
Pilihan: A. a = -1, b = -1
B. a = 1, b = -1
C. a = -1, b = 1
D. a = 1, b = 1
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `05c9e45acc4d05508ee66bf6`

$P = \begin{bmatrix} 1 & -8 \\ -1 & -2 \end{bmatrix}$, $Q = \begin{bmatrix} 3 & 2 \\ -1 & 2 \end{bmatrix}$, $X \text{ matriks berordo } 2\times 2 \text{ yang memenuhi } P - 2X = 3Q$<br><br>Tentukan matriks $X$.

| Opsi | Isi |
|---|---|
| A | $X = \begin{bmatrix} 5 & -1 \\ -2 & 2 \end{bmatrix}$ |
| B | $X = \begin{bmatrix} -8 & -14 \\ 2 & -8 \end{bmatrix}$ |
| C | $X = \begin{bmatrix} -4 & -7 \\ 1 & -4 \end{bmatrix}$ |
| D | $X = \begin{bmatrix} 4 & 7 \\ -1 & 4 \end{bmatrix}$ |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Persamaan: P - 2X = 3Q, maka 2X = P - 3Q. Hitung 3Q = 3 * [[3, 2], [-1, 2]] = [[9, 6], [-3, 6]]. Hitung P - 3Q = [[1, -8], [-1, -2]] - [[9, 6], [-3, 6]] = [[1-9, -8-6], [-1-(-3), -2-6]] = [[-8, -14], [2, -8]]. Maka X = 1/2 * [[-8, -14], [2, -8]] = [[-4, -7], [1, -4]].
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b548214cebf5a8c2755cfebf39ca36afe938c0940dc54271de03fc42d866c9f1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2917 |
| 2 | success | valid / verified | applying | procedural | Easy | 2864 |
| 3 | success | valid / verified | applying | procedural | Easy | 2904 |

Run 1 — solusi: Persamaan: P - 2X = 3Q, maka 2X = P - 3Q. Hitung 3Q = 3 * [[3, 2], [-1, 2]] = [[9, 6], [-3, 6]]. Hitung P - 3Q = [[1, -8], [-1, -2]] - [[9, 6], [-3, 6]] = [[1-9, -8-6], [-1-(-3), -2-6]] = [[-8, -14], [2, -8]]. Maka X = 1/2 * [[-8, -14], [2, -8]] = [[-4, -7], [1, -4]].
- Domain kognitif `classify/applying`: Siswa perlu melakukan manipulasi aljabar pada persamaan matriks untuk mengisolasi variabel X, kemudian melakukan operasi pengurangan dan perkalian skalar matriks secara berurutan. Ini adalah penerapan prosedur rutin.. Bukti: X matriks berordo 2x2 yang memenuhi P - 2X = 3Q
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritme operasi matriks (pengurangan dan perkalian skalar) serta manipulasi aljabar dasar pada matriks.. Bukti: P - 2X = 3Q
- Intended difficulty `classify/Easy`: Soal ini dikategorikan Easy karena merupakan penerapan langsung dari operasi matriks dasar. Jalur penyelesaian sangat jelas (isolasi X, hitung 3Q, kurangi P, bagi 2), tidak ada kendala yang berinteraksi secara kompleks, dan prosedur yang digunakan sangat familiar bagi siswa kelas 11.. Bukti: P - 2X = 3Q

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi dasar matriks (penjumlahan, pengurangan, perkalian skalar). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi matriks adalah standar kelas 11. Soal ini hanya memerlukan manipulasi aljabar linear sederhana tanpa jebakan konseptual atau integrasi topik lain. |

Run 2 — solusi: Persamaan P - 2X = 3Q diubah menjadi 2X = P - 3Q, sehingga X = 0.5(P - 3Q). Menghitung 3Q = [[9, 6], [-3, 6]]. Maka P - 3Q = [[1-9, -8-6], [-1-(-3), -2-6]] = [[-8, -14], [2, -8]]. Membagi dengan 2 menghasilkan X = [[-4, -7], [1, -4]].
- Domain kognitif `classify/applying`: Siswa perlu melakukan manipulasi aljabar matriks untuk mengisolasi variabel X, kemudian menerapkan operasi pengurangan dan perkalian skalar matriks. Ini adalah penerapan prosedur rutin dalam konteks aljabar matriks.. Bukti: P - 2X = 3Q; Tentukan matriks X
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma operasi matriks (pengurangan dan perkalian skalar) dan manipulasi persamaan linear matriks.. Bukti: P - 2X = 3Q
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 11. Langkah-langkah penyelesaiannya jelas: isolasi variabel, perkalian skalar, dan pengurangan matriks. Tidak ada kendala yang berinteraksi secara kompleks atau kebutuhan strategi non-rutin.. Bukti: P - 2X = 3Q

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi dasar matriks (penjumlahan, pengurangan, perkalian skalar) dan manipulasi aljabar linear sederhana. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi matriks adalah kurikulum standar kelas 11. Soal ini merupakan aplikasi langsung dari definisi operasi matriks tanpa modifikasi tingkat lanjut. |

Run 3 — solusi: Dari P - 2X = 3Q, maka 2X = P - 3Q. Hitung 3Q = 3 * [[3, 2], [-1, 2]] = [[9, 6], [-3, 6]]. Maka 2X = [[1, -8], [-1, -2]] - [[9, 6], [-3, 6]] = [[1-9, -8-6], [-1-(-3), -2-6]] = [[-8, -14], [2, -8]]. Maka X = (1/2) * [[-8, -14], [2, -8]] = [[-4, -7], [1, -4]].
- Domain kognitif `classify/applying`: Siswa perlu melakukan manipulasi aljabar matriks untuk mengisolasi variabel X, kemudian melakukan operasi pengurangan dan perkalian skalar matriks. Ini adalah penerapan prosedur rutin dalam konteks aljabar matriks.. Bukti: X matriks berordo 2x2 yang memenuhi P - 2X = 3Q
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritme operasi matriks (pengurangan dan perkalian skalar) serta manipulasi persamaan matriks.. Bukti: P - 2X = 3Q
- Intended difficulty `classify/Easy`: Soal ini dikategorikan Easy karena melibatkan prosedur standar yang familiar bagi siswa kelas 11. Langkah-langkah penyelesaian (isolasi variabel, operasi matriks) bersifat langsung dan tidak memerlukan strategi non-rutin atau integrasi konsep yang kompleks.. Bukti: P - 2X = 3Q

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi dasar matriks (penjumlahan, pengurangan, perkalian skalar) dan manipulasi aljabar linear sederhana. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi matriks adalah kurikulum standar kelas 11. Soal ini menguji kemampuan dasar dalam memanipulasi persamaan matriks yang merupakan kompetensi inti. |

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
Soal: $P = \begin{bmatrix} 1 & -8 \\ -1 & -2 \end{bmatrix}$, $Q = \begin{bmatrix} 3 & 2 \\ -1 & 2 \end{bmatrix}$, $X \text{ matriks berordo } 2\times 2 \text{ yang memenuhi } P - 2X = 3Q$

Tentukan matriks $X$.
Pilihan: A. $X = \begin{bmatrix} 5 & -1 \\ -2 & 2 \end{bmatrix}$
B. $X = \begin{bmatrix} -8 & -14 \\ 2 & -8 \end{bmatrix}$
C. $X = \begin{bmatrix} -4 & -7 \\ 1 & -4 \end{bmatrix}$
D. $X = \begin{bmatrix} 4 & 7 \\ -1 & 4 \end{bmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `e26865e3a760ece340901b25`

Diketahui $\begin{bmatrix} x-2 & 9 \\ -3 & 0 \end{bmatrix}\begin{bmatrix} -4 & 0 \\ 1 & y+1 \end{bmatrix} = \begin{bmatrix} -3 & -9 \\ 12 & 0 \end{bmatrix}$.<br><br>Tentukan $x+y$.

| Opsi | Isi |
|---|---|
| A | 3 |
| B | 5 |
| C | 7 |
| D | -7 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Perkalian matriks: baris 1 kolom 1: (x-2)(-4) + 9(1) = -4x + 8 + 9 = -4x + 17. Diketahui hasilnya -3, maka -4x + 17 = -3 => -4x = -20 => x = 5. Baris 1 kolom 2: (x-2)(0) + 9(y+1) = 9y + 9. Diketahui hasilnya -9, maka 9y + 9 = -9 => 9y = -18 => y = -2. Maka x + y = 5 + (-2) = 3.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e5742707578415647d14da3e68af34add7d749ab4ce03c1a74aafd2cf80d1ad7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2821 |
| 2 | success | valid / verified | applying | procedural | Easy | 2822 |
| 3 | success | valid / verified | applying | procedural | Easy | 2817 |

Run 1 — solusi: Perkalian matriks: baris 1 kolom 1: (x-2)(-4) + 9(1) = -4x + 8 + 9 = -4x + 17. Diketahui hasilnya -3, maka -4x + 17 = -3 => -4x = -20 => x = 5. Baris 1 kolom 2: (x-2)(0) + 9(y+1) = 9y + 9. Diketahui hasilnya -9, maka 9y + 9 = -9 => 9y = -18 => y = -2. Maka x + y = 5 + (-2) = 3.
- Domain kognitif `classify/applying`: Siswa diminta melakukan operasi perkalian matriks standar dan menyelesaikan sistem persamaan linear sederhana untuk mencari nilai variabel x dan y, kemudian menjumlahkannya. Ini adalah penerapan prosedur rutin.. Bukti: Diketahui [x-2 9; -3 0][ -4 0; 1 y+1] = [-3 -9; 12 0]; Tentukan x+y
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma perkalian matriks dan penyelesaian persamaan linear, yang merupakan pengetahuan prosedural.. Bukti: Perkalian matriks; x-2 9; -3 0
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu melakukan perkalian matriks 2x2 dan menyelesaikan persamaan linear satu variabel. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Diketahui [x-2 9; -3 0][ -4 0; 1 y+1] = [-3 -9; 12 0]; Tentukan x+y

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi perkalian matriks dan penyelesaian persamaan linear satu variabel. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi matriks adalah standar kelas 11. Soal ini adalah latihan langsung tanpa modifikasi atau jebakan konseptual yang rumit. |

Run 2 — solusi: Perkalian matriks menghasilkan: baris 1 kolom 1: (x-2)(-4) + 9(1) = -4x + 8 + 9 = -4x + 17. Diketahui hasilnya -3, maka -4x + 17 = -3 => -4x = -20 => x = 5. Baris 1 kolom 2: (x-2)(0) + 9(y+1) = 9y + 9. Diketahui hasilnya -9, maka 9y + 9 = -9 => 9y = -18 => y = -2. Maka x + y = 5 + (-2) = 3.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur perkalian matriks standar dan menyelesaikan sistem persamaan linear sederhana untuk menemukan nilai variabel x dan y. Ini adalah penerapan prosedur rutin dalam konteks matriks.. Bukti: Diketahui [x-2 9; -3 0][ -4 0; 1 y+1] = [-3 -9; 12 0]; Tentukan x+y
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma perkalian matriks dan penyelesaian persamaan linear, yang merupakan pengetahuan prosedural.. Bukti: Perkalian matriks; x-2 9; -3 0
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu melakukan perkalian matriks 2x2 dan menyelesaikan persamaan linear satu variabel. Tidak ada kendala yang berinteraksi secara kompleks atau kebutuhan untuk strategi non-rutin.. Bukti: Diketahui [x-2 9; -3 0][ -4 0; 1 y+1] = [-3 -9; 12 0]

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
| gradeRelativeRationale | Materi matriks adalah standar kelas 11. Soal ini adalah aplikasi langsung dari definisi perkalian matriks tanpa variasi atau jebakan konseptual yang signifikan. |

Run 3 — solusi: Perkalian matriks: baris 1 kolom 1: (x-2)(-4) + 9(1) = -3 => -4x + 8 + 9 = -3 => -4x = -20 => x = 5. Baris 1 kolom 2: (x-2)(0) + 9(y+1) = -9 => 9y + 9 = -9 => 9y = -18 => y = -2. Maka x+y = 5 + (-2) = 3.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur perkalian matriks untuk membentuk sistem persamaan linear sederhana dan menyelesaikannya. Ini adalah penerapan langsung dari prosedur yang sudah dipelajari.. Bukti: Diketahui [x-2 9; -3 0][ -4 0; 1 y+1] = [-3 -9; 12 0]. Tentukan x+y.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma perkalian matriks dan penyelesaian persamaan linear, yang merupakan pengetahuan prosedural.. Bukti: Diketahui [x-2 9; -3 0][ -4 0; 1 y+1] = [-3 -9; 12 0].
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu melakukan perkalian matriks standar dan menyelesaikan dua persamaan linear satu variabel yang sederhana. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Diketahui [x-2 9; -3 0][ -4 0; 1 y+1] = [-3 -9; 12 0]. Tentukan x+y.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian matriks 2x2 dan penyelesaian SPLDV sederhana. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi matriks adalah standar kelas 11. Soal ini tidak memerlukan manipulasi kompleks, hanya eksekusi algoritma perkalian matriks yang langsung menghasilkan nilai variabel. |

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
Soal: Diketahui $\begin{bmatrix} x-2 & 9 \\ -3 & 0 \end{bmatrix}\begin{bmatrix} -4 & 0 \\ 1 & y+1 \end{bmatrix} = \begin{bmatrix} -3 & -9 \\ 12 & 0 \end{bmatrix}$.

Tentukan $x+y$.
Pilihan: A. 3
B. 5
C. 7
D. -7
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 9. Soal `cedfd4f07ddb24cdfcffdb61`

$A = \begin{bmatrix} 2 & 5 \\ 1 & 2 \end{bmatrix}$, $B = \begin{bmatrix} 2 & 2 \\ -3 & 1 \end{bmatrix}$, $C \text{ memenuhi } AC = B$<br><br>Tentukan determinan $C$.

| Opsi | Isi |
|---|---|
| A | -1/8 |
| B | -4 |
| C | 8 |
| D | -8 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Diketahui AC = B. Berdasarkan sifat determinan, det(AC) = det(A)det(C) = det(B), sehingga det(C) = det(B)/det(A). det(A) = (2)(2) - (5)(1) = 4 - 5 = -1. det(B) = (2)(1) - (2)(-3) = 2 + 6 = 8. Maka det(C) = 8 / -1 = -8.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f83012599172910a140b30ad17da5797f27a7aab58eb9c2232796cf2d5515a7b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2732 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2730 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2753 |

Run 1 — solusi: Diketahui AC = B. Berdasarkan sifat determinan, det(AC) = det(A)det(C) = det(B), sehingga det(C) = det(B)/det(A). det(A) = (2)(2) - (5)(1) = 4 - 5 = -1. det(B) = (2)(1) - (2)(-3) = 2 + 6 = 8. Maka det(C) = 8 / -1 = -8.
- Domain kognitif `classify/applying`: Siswa perlu memahami dan menerapkan sifat determinan matriks (det(AB) = det(A)det(B)) untuk menyelesaikan masalah tanpa harus mencari matriks C secara eksplisit. Ini adalah penerapan prosedur yang sudah dipelajari dalam konteks rutin.. Bukti: AC = B; Tentukan determinan C
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip atau sifat determinan matriks (konseptual) dan kemampuan melakukan perhitungan determinan matriks 2x2 (prosedural).. Bukti: AC = B; Tentukan determinan C
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu menerapkan sifat determinan secara langsung. Tidak ada langkah yang saling bergantung secara kompleks atau kendala yang berinteraksi.. Bukti: AC = B; Tentukan determinan C

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi determinan matriks 2x2 dan sifat determinan perkalian matriks. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi matriks dan determinan adalah standar kelas 11. Penggunaan sifat determinan adalah prosedur rutin yang diharapkan dikuasai siswa. |

Run 2 — solusi: Diketahui AC = B. Berdasarkan sifat determinan, det(AC) = det(A) * det(C) = det(B). Maka det(C) = det(B) / det(A). det(A) = (2*2) - (5*1) = 4 - 5 = -1. det(B) = (2*1) - (2*-3) = 2 + 6 = 8. Jadi, det(C) = 8 / -1 = -8.
- Domain kognitif `classify/applying`: Siswa perlu memahami dan menerapkan sifat determinan matriks (det(AB) = det(A)det(B)) untuk menyelesaikan persamaan matriks tanpa harus mencari matriks C secara eksplisit.. Bukti: AC = B; Tentukan determinan C
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman prinsip atau aturan determinan matriks (konseptual) dan prosedur perhitungan determinan matriks 2x2 (prosedural).. Bukti: AC = B; Tentukan determinan C
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu menerapkan sifat determinan matriks yang merupakan prosedur standar dan familiar di kelas 11. Jalur penyelesaian sangat jelas dan tidak memerlukan perencanaan strategi yang kompleks.. Bukti: AC = B; Tentukan determinan C

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat determinan matriks dan cara menghitung determinan matriks 2x2. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi determinan matriks adalah topik dasar kelas 11. Soal ini menguji pemahaman langsung atas sifat determinan tanpa kerumitan tambahan. |

Run 3 — solusi: Diketahui AC = B. Berdasarkan sifat determinan, det(A)det(C) = det(B). Hitung det(A) = (2)(2) - (5)(1) = 4 - 5 = -1. Hitung det(B) = (2)(1) - (2)(-3) = 2 + 6 = 8. Maka det(C) = det(B)/det(A) = 8/(-1) = -8.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan sifat determinan matriks det(AB) = det(A)det(B) untuk menyelesaikan persamaan matriks tanpa harus mencari matriks C secara eksplisit. Ini adalah penerapan prosedur yang sudah dipelajari pada konteks rutin.. Bukti: AC = B; Tentukan determinan C
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang sifat-sifat determinan matriks (prinsip konseptual) dan kemampuan mengoperasikannya dalam persamaan matriks (prosedural).. Bukti: AC = B; Tentukan determinan C
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 11. Siswa hanya perlu memahami sifat determinan det(AC)=det(A)det(C) dan melakukan perhitungan determinan 2x2 yang sederhana. Tidak ada kendala yang berinteraksi atau kebutuhan strategi nonrutin.. Bukti: AC = B; Tentukan determinan C

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi determinan matriks 2x2 dan sifat determinan perkalian matriks. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi determinan matriks adalah standar kurikulum kelas 11. Soal ini menguji pemahaman dasar sifat determinan tanpa kerumitan tambahan. |

Histori retry: run 1 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 2 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

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
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Determinan Matriks dan Invers Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: $A = \begin{bmatrix} 2 & 5 \\ 1 & 2 \end{bmatrix}$, $B = \begin{bmatrix} 2 & 2 \\ -3 & 1 \end{bmatrix}$, $C \text{ memenuhi } AC = B$

Tentukan determinan $C$.
Pilihan: A. -1/8
B. -4
C. 8
D. -8
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `3be8bb0629a4ad9d30cfd1f6`

Tentukan $(AB^{-1})^{-1}$ jika diketahui $A^{-1} = \begin{bmatrix} 1 & 4 \\ 2 & 3 \end{bmatrix}$ dan $B = \begin{bmatrix} 5 & 1 \\ 1 & 3 \end{bmatrix}$.

| Opsi | Isi |
|---|---|
| A | $\begin{bmatrix} 7 & 7 \\ 23 & 13 \end{bmatrix}$ |
| B | $\begin{bmatrix} 9 & 13 \\ 13 & 11 \end{bmatrix}$ |
| C | $\begin{bmatrix} 7 & 23 \\ 7 & 13 \end{bmatrix}$ |
| D | $\begin{bmatrix} 13 & 9 \\ 11 & 13 \end{bmatrix}$ |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Gunakan sifat invers matriks: (AB^-1)^-1 = (B^-1)^-1 A^-1 = B A^-1. Diketahui B = [[5,1],[1,3]] dan A^-1 = [[1,4],[2,3]]. Maka, B A^-1 = [[5,1],[1,3]] * [[1,4],[2,3]] = [[5*1+1*2, 5*4+1*3], [1*1+3*2, 1*4+3*3]] = [[7, 23], [7, 13]].
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f1b046516af0d1cf30c67c0618fca1e9b553e5ba533aadeeb81b03d6c36bcdfc`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2965 |
| 2 | success | valid / verified | applying | procedural | Medium | 2973 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2928 |

Run 1 — solusi: Menggunakan sifat invers matriks (AB^-1)^-1 = (B^-1)^-1 A^-1 = B A^-1. Diketahui B = [[5,1],[1,3]] dan A^-1 = [[1,4],[2,3]]. Maka, B A^-1 = [[5,1],[1,3]] * [[1,4],[2,3]] = [[5*1+1*2, 5*4+1*3], [1*1+3*2, 1*4+3*3]] = [[5+2, 20+3], [1+6, 4+9]] = [[7, 23], [7, 13]].
- Domain kognitif `classify/applying`: Siswa perlu menerapkan sifat invers matriks (AB^-1)^-1 = B A^-1 untuk menyederhanakan ekspresi sebelum melakukan operasi perkalian matriks. Ini adalah penerapan prosedur yang sudah dipelajari dalam konteks yang rutin.. Bukti: Tentukan (AB^-1)^-1 jika diketahui A^-1 = [[1, 4], [2, 3]] dan B = [[5, 1], [1, 3]].
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan antara operasi matriks dan sifat-sifat invers matriks (konseptual) serta kemampuan melakukan perkalian matriks (prosedural).. Bukti: (AB^-1)^-1
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemahaman sifat invers matriks (AB^-1)^-1 = B A^-1. Meskipun perkalian matriks adalah prosedur rutin, siswa harus melakukan langkah penyederhanaan aljabar matriks terlebih dahulu sebelum menghitung, yang melibatkan beberapa langkah terkait.. Bukti: Tentukan (AB^-1)^-1 jika diketahui A^-1 = [[1, 4], [2, 3]] dan B = [[5, 1], [1, 3]].

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat-sifat invers matriks dan perkalian matriks. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan memahami sifat invers matriks. Soal ini menuntut siswa untuk tidak langsung menghitung invers B, melainkan menggunakan sifat (AB^-1)^-1 = B A^-1 untuk efisiensi, yang merupakan standar kemampuan kelas 11. |

Run 2 — solusi: Gunakan sifat invers matriks: (AB^-1)^-1 = (B^-1)^-1 A^-1 = B A^-1. Diketahui B = [[5,1],[1,3]] dan A^-1 = [[1,4],[2,3]]. Maka, B A^-1 = [[5,1],[1,3]] * [[1,4],[2,3]] = [[5*1+1*2, 5*4+1*3], [1*1+3*2, 1*4+3*3]] = [[7, 23], [7, 13]].
- Domain kognitif `classify/applying`: Siswa perlu menerapkan sifat aljabar matriks (AB^-1)^-1 = B A^-1 untuk menyederhanakan ekspresi sebelum melakukan perkalian matriks. Ini adalah penerapan prosedur yang familiar dalam konteks aljabar matriks.. Bukti: Tentukan (AB^-1)^-1; diketahui A^-1 = [[1,4],[2,3]] dan B = [[5,1],[1,3]]
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman tentang sifat-sifat invers matriks (konseptual) dan kemampuan melakukan operasi perkalian matriks (prosedural).. Bukti: (AB^-1)^-1; A^-1 = [[1,4],[2,3]] dan B = [[5,1],[1,3]]
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua langkah utama: menyederhanakan ekspresi menggunakan sifat invers matriks (B A^-1) dan melakukan perkalian matriks. Meskipun prosedurnya standar, siswa harus berhati-hati dengan urutan perkalian matriks yang tidak komutatif.. Bukti: Tentukan (AB^-1)^-1; A^-1 = [[1,4],[2,3]] dan B = [[5,1],[1,3]]

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat invers matriks (AB)^-1 = B^-1 A^-1 dan perkalian matriks. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan mampu memanipulasi ekspresi matriks menggunakan sifat-sifat dasar. Soal ini menguji pemahaman tentang sifat invers dan ketidakkomutatifan perkalian matriks, yang merupakan standar untuk tingkat kesulitan menengah. |

Run 3 — solusi: Menggunakan sifat invers matriks (AB^-1)^-1 = (B^-1)^-1 A^-1 = B A^-1. Diketahui B = [[5,1],[1,3]] dan A^-1 = [[1,4],[2,3]]. Maka (AB^-1)^-1 = [[5,1],[1,3]] * [[1,4],[2,3]] = [[5*1+1*2, 5*4+1*3], [1*1+3*2, 1*4+3*3]] = [[7, 23], [7, 13]].
- Domain kognitif `classify/applying`: Siswa perlu menerapkan sifat invers matriks (AB^-1)^-1 = B A^-1 untuk menyederhanakan ekspresi sebelum melakukan perkalian matriks. Ini adalah penerapan prosedur yang sudah dipelajari dalam konteks rutin.. Bukti: Tentukan (AB^-1)^-1 jika diketahui A^-1 = [[1,4],[2,3]] dan B = [[5,1],[1,3]].
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara operasi invers dan perkalian matriks (prinsip aljabar matriks).. Bukti: (AB^-1)^-1 = B A^-1
- Intended difficulty `classify/Easy`: Soal memerlukan satu langkah penyederhanaan sifat invers (B A^-1) diikuti dengan satu operasi perkalian matriks 2x2. Jalur penyelesaian sangat jelas, tidak ada kendala yang berinteraksi secara kompleks, dan prosedur perkalian matriks adalah rutin bagi siswa kelas 11.. Bukti: Tentukan (AB^-1)^-1 jika diketahui A^-1 = [[1,4],[2,3]] dan B = [[5,1],[1,3]].

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi perkalian matriks dan sifat invers matriks (AB)^-1 = B^-1 A^-1. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan sudah menguasai sifat-sifat matriks dan perkalian matriks 2x2. Soal ini adalah penerapan langsung dari sifat tersebut tanpa modifikasi atau integrasi konsep yang menantang. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4979`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan sifat invers matriks (AB^-1)^-1 = B A^-1 untuk menyederhanakan ekspresi sebelum melakukan operasi perkalian matriks. Ini adalah penerapan prosedur yang sudah dipelajari dalam konteks yang rutin.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman tentang hubungan antara operasi invers dan perkalian matriks (prinsip aljabar matriks).
- Intended difficulty `Easy`: Soal memerlukan satu langkah penyederhanaan sifat invers (B A^-1) diikuti dengan satu operasi perkalian matriks 2x2. Jalur penyelesaian sangat jelas, tidak ada kendala yang berinteraksi secara kompleks, dan prosedur perkalian matriks adalah rutin bagi siswa kelas 11.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi perkalian matriks dan sifat invers matriks (AB)^-1 = B^-1 A^-1. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan sudah menguasai sifat-sifat matriks dan perkalian matriks 2x2. Soal ini adalah penerapan langsung dari sifat tersebut tanpa modifikasi atau integrasi konsep yang menantang. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
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
Soal: Tentukan $(AB^{-1})^{-1}$ jika diketahui $A^{-1} = \begin{bmatrix} 1 & 4 \\ 2 & 3 \end{bmatrix}$ dan $B = \begin{bmatrix} 5 & 1 \\ 1 & 3 \end{bmatrix}$.
Pilihan: A. $\begin{bmatrix} 7 & 7 \\ 23 & 13 \end{bmatrix}$
B. $\begin{bmatrix} 9 & 13 \\ 13 & 11 \end{bmatrix}$
C. $\begin{bmatrix} 7 & 23 \\ 7 & 13 \end{bmatrix}$
D. $\begin{bmatrix} 13 & 9 \\ 11 & 13 \end{bmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `0b4b98faa7f553833f0db971`

Suatu toko alat lukis menjual 40 kuas lukis. Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.<br><br>Jika uang yang didapat oleh toko tersebut Rp1.103.000,00, maka berapa banyak masing-masing jenis kuas lukis yang terjual?

| Opsi | Isi |
|---|---|
| A | 20 kuas lukis jenis I dan 20 kuas lukis jenis II |
| B | 15 kuas lukis jenis I dan 25 kuas lukis jenis II |
| C | 27 kuas lukis jenis I dan 13 kuas lukis jenis II |
| D | 13 kuas lukis jenis I dan 27 kuas lukis jenis II |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Misal x = jenis I, y = jenis II. Sistem: x + y = 40 (1) dan 35.000x + 24.000y = 1.103.000 (2). Dari (1), x = 40 - y. Substitusi ke (2): 35.000(40 - y) + 24.000y = 1.103.000 => 1.400.000 - 35.000y + 24.000y = 1.103.000 => -11.000y = -297.000 => y = 27. Maka x = 40 - 27 = 13.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0c35320069a6241eb327349d6d4815b0a2cc5c5b77975b389033dfbf5899edfb`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3056 |
| 2 | success | valid / verified | applying | procedural | Easy | 3073 |
| 3 | success | valid / verified | applying | procedural | Easy | 3115 |

Run 1 — solusi: Misal x = jenis I, y = jenis II. Sistem: x + y = 40 (1) dan 35.000x + 24.000y = 1.103.000 (2). Dari (1), x = 40 - y. Substitusi ke (2): 35.000(40 - y) + 24.000y = 1.103.000 => 1.400.000 - 35.000y + 24.000y = 1.103.000 => -11.000y = -297.000 => y = 27. Maka x = 40 - 27 = 13.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerjemahkan masalah kontekstual ke dalam model matematika (SPLDV) dan menyelesaikan sistem tersebut menggunakan prosedur standar (substitusi atau eliminasi). Ini adalah penerapan langsung dari konsep yang sudah dipelajari.. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa tentang prosedur algoritma untuk menyelesaikan sistem persamaan linear dua variabel.. Bukti: x+y=40 dan 35.000x+24.000y=1.103.000
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari materi SPLDV yang merupakan prasyarat kelas 11. Jalur penyelesaian sangat jelas, tidak ada kendala yang berinteraksi secara kompleks, dan beban perhitungan moderat.. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sistem Persamaan Linear Dua Variabel (SPLDV) |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi SPLDV adalah prasyarat, soal ini sangat rutin dan langsung, sehingga tingkat kesulitannya rendah bagi siswa kelas 11. |

Run 2 — solusi: Misalkan x = jenis I, y = jenis II. Sistem: x + y = 40 dan 35.000x + 24.000y = 1.103.000. Dari x = 40 - y, substitusi ke persamaan kedua: 35.000(40 - y) + 24.000y = 1.103.000 => 1.400.000 - 35.000y + 24.000y = 1.103.000 => -11.000y = -297.000 => y = 27. Maka x = 40 - 27 = 13.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerjemahkan masalah kontekstual ke dalam model matematika (SPLDV) dan menyelesaikannya menggunakan prosedur aljabar standar. Ini adalah penerapan konsep yang sudah dipelajari sebelumnya.. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa tentang algoritma penyelesaian sistem persamaan linear dua variabel, yang merupakan pengetahuan prosedural.. Bukti: x+y=40; 35.000x+24.000y=1.103.000
- Intended difficulty `classify/Easy`: Soal ini adalah masalah rutin SPLDV yang sudah dipelajari di jenjang sebelumnya (SMP/SMA kelas 10). Jalur penyelesaian sangat jelas dan tidak memerlukan strategi non-rutin.. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menyusun dan menyelesaikan sistem persamaan linear dua variabel (SPLDV). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun untuk kelas 11, materi SPLDV adalah prasyarat dasar. Soal ini tidak menuntut kedalaman materi kelas 11 (seperti matriks atau polinomial), sehingga dikategorikan mudah bagi siswa kelas 11. |

Run 3 — solusi: Misalkan x = banyak kuas jenis I, y = banyak kuas jenis II. Sistem: x + y = 40 (1) dan 35.000x + 24.000y = 1.103.000 (2). Dari (1), x = 40 - y. Substitusi ke (2): 35.000(40 - y) + 24.000y = 1.103.000 => 1.400.000 - 35.000y + 24.000y = 1.103.000 => -11.000y = -297.000 => y = 27. Maka x = 40 - 27 = 13.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur sistem persamaan linear dua variabel (SPLDV) yang merupakan materi prasyarat untuk menyelesaikan masalah kontekstual. Tidak ada strategi nonrutin yang diperlukan.. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma penyelesaian sistem persamaan linear (substitusi atau eliminasi) yang merupakan prosedur standar.. Bukti: x+y=40; 35.000x+24.000y=1.103.000
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari SPLDV. Meskipun konteksnya cerita, model matematikanya sangat jelas dan rutin bagi siswa SMA. Tidak ada kendala yang berinteraksi secara kompleks.. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar sistem persamaan linear dua variabel (SPLDV). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun SPLDV adalah materi SMP, soal ini diberikan sebagai prasyarat untuk kelas 11. Tingkat kesulitannya rendah karena model matematika langsung dapat dibentuk dari informasi yang diberikan tanpa modifikasi atau penalaran lanjut. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 12. Soal `cbc1c44af555d15fc2ba9abc`

Perilaku ujung fungsi polinomial $f(x) = -5x^7 + 2x^4 - 8$ adalah ….

| Opsi | Isi |
|---|---|
| A | Turun di ujung kiri, turun di ujung kanan (↙, ↘) |
| B | Naik di ujung kiri, turun di ujung kanan (↖, ↘) |
| C | Naik di ujung kiri, naik di ujung kanan (↖, ↗) |
| D | Turun di ujung kiri, naik di ujung kanan (↙, ↗) |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Fungsi f(x) = -5x^7 + 2x^4 - 8 memiliki derajat n=7 (ganjil) dan koefisien utama a=-5 (negatif). Untuk polinomial berderajat ganjil dengan koefisien utama negatif, saat x→-∞ maka f(x)→∞ (naik di kiri) dan saat x→∞ maka f(x)→-∞ (turun di kanan).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `bf1d6fab773e7e466c1e6dc9a759a1862668db918b6d0f871425a74edae291d1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2756 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2745 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2769 |

Run 1 — solusi: Fungsi f(x) = -5x^7 + 2x^4 - 8 memiliki derajat n=7 (ganjil) dan koefisien utama a=-5 (negatif). Untuk polinomial berderajat ganjil dengan koefisien utama negatif, saat x→-∞ maka f(x)→∞ (naik di kiri) dan saat x→∞ maka f(x)→-∞ (turun di kanan).
- Domain kognitif `classify/knowing`: Siswa diminta mengenali dan menerapkan aturan perilaku ujung polinomial berdasarkan derajat dan koefisien utama. Ini adalah prosedur langsung yang familiar dalam kurikulum kelas 11.. Bukti: Perilaku ujung fungsi polinomial f(x) = -5x^7 + 2x^4 - 8 adalah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip dasar perilaku ujung fungsi polinomial, yang merupakan konsep teoretis dalam aljabar polinomial.. Bukti: Perilaku ujung fungsi polinomial
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengidentifikasi derajat dan koefisien utama untuk menentukan perilaku ujung tanpa langkah perantara yang kompleks atau integrasi konsep lain.. Bukti: Perilaku ujung fungsi polinomial f(x) = -5x^7 + 2x^4 - 8

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk umum polinomial, derajat, dan koefisien utama. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi perilaku ujung polinomial adalah topik standar kelas 11. Soal ini tidak memerlukan manipulasi aljabar, hanya pengenalan pola, sehingga tergolong mudah. |

Run 2 — solusi: Fungsi f(x) = -5x^7 + 2x^4 - 8 memiliki derajat n=7 (ganjil) dan koefisien utama a=-5 (negatif). Untuk polinomial derajat ganjil dengan koefisien utama negatif, saat x mendekati negatif tak hingga, f(x) mendekati positif tak hingga (naik di kiri), dan saat x mendekati positif tak hingga, f(x) mendekati negatif tak hingga (turun di kanan).
- Domain kognitif `classify/knowing`: Siswa diminta mengenali dan menerapkan aturan perilaku ujung polinomial berdasarkan derajat dan koefisien utama. Ini adalah prosedur langsung yang sudah dipelajari di kelas 11.. Bukti: Perilaku ujung fungsi polinomial f(x) = -5x^7 + 2x^4 - 8 adalah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip dasar perilaku ujung fungsi polinomial, yang merupakan konsep teoretis dalam aljabar polinomial.. Bukti: Perilaku ujung fungsi polinomial
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengidentifikasi derajat dan koefisien utama untuk menentukan perilaku ujung tanpa langkah perantara yang kompleks.. Bukti: f(x) = -5x^7 + 2x^4 - 8

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang derajat polinomial dan pengaruh koefisien utama terhadap perilaku ujung fungsi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi perilaku ujung polinomial adalah topik standar kelas 11. Soal ini tidak memerlukan manipulasi aljabar, hanya identifikasi sifat fungsi. |

Run 3 — solusi: Fungsi f(x) = -5x^7 + 2x^4 - 8 memiliki derajat n=7 (ganjil) dan koefisien utama a=-5 (negatif). Untuk polinomial berderajat ganjil dengan koefisien utama negatif, saat x mendekati negatif tak hingga, f(x) mendekati positif tak hingga (naik di kiri). Saat x mendekati positif tak hingga, f(x) mendekati negatif tak hingga (turun di kanan). Jadi, perilakunya adalah (↖, ↘).
- Domain kognitif `classify/knowing`: Siswa diminta mengenali dan menerapkan aturan perilaku ujung polinomial berdasarkan derajat dan koefisien utama. Ini adalah prosedur standar dalam materi polinomial.. Bukti: Perilaku ujung fungsi polinomial f(x) = -5x^7 + 2x^4 - 8 adalah ….
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip dasar perilaku ujung polinomial yang merupakan bagian dari konsep polinomial.. Bukti: f(x) = -5x^7 + 2x^4 - 8
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengidentifikasi derajat dan koefisien utama untuk menentukan perilaku ujung tanpa langkah perantara yang kompleks.. Bukti: Perilaku ujung fungsi polinomial f(x) = -5x^7 + 2x^4 - 8 adalah ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang derajat dan koefisien utama polinomial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi perilaku ujung polinomial adalah topik dasar di kelas 11. Soal ini tidak memerlukan manipulasi aljabar atau analisis mendalam, sehingga tergolong mudah. |

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
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Polinomial dan Fungsi Polinomial
Tipe soal: multiple_choice
Stimulus: -
Soal: Perilaku ujung fungsi polinomial $f(x) = -5x^7 + 2x^4 - 8$ adalah ….
Pilihan: A. Turun di ujung kiri, turun di ujung kanan (↙, ↘)
B. Naik di ujung kiri, turun di ujung kanan (↖, ↘)
C. Naik di ujung kiri, naik di ujung kanan (↖, ↗)
D. Turun di ujung kiri, naik di ujung kanan (↙, ↗)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 13. Soal `89fd76a5340ac72134f6800d`

$x^6 - 12x^4 + 3x^2 - 10$<br><br>Cari derajat setiap polinomial berikut.

| Opsi | Isi |
|---|---|
| A | 2 |
| B | 12 |
| C | 6 |
| D | 4 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Derajat polinomial adalah pangkat tertinggi dari variabel dalam polinomial tersebut. Untuk polinomial x^6 - 12x^4 + 3x^2 - 10, pangkat-pangkat variabelnya adalah 6, 4, dan 2. Pangkat tertingginya adalah 6.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a0658279287b06f5f59ad7cf6b7773aa8d1ef1b4fa0ad89169e8b0a47bbddc89`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2603 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2628 |
| 3 | success | valid / verified | knowing | factual | Easy | 2642 |

Run 1 — solusi: Derajat polinomial adalah pangkat tertinggi dari variabel dalam polinomial tersebut. Untuk $x^6 - 12x^4 + 3x^2 - 10$, pangkat tertinggi adalah 6.
- Domain kognitif `classify/knowing`: Soal hanya meminta siswa untuk mengidentifikasi pangkat tertinggi dari variabel dalam polinomial, yang merupakan definisi dasar derajat polinomial.. Bukti: Cari derajat setiap polinomial berikut.; $x^6 - 12x^4 + 3x^2 - 10$
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang definisi atau istilah dasar dalam polinomial, yaitu derajat.. Bukti: Cari derajat setiap polinomial berikut.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan langsung. Siswa hanya perlu melihat eksponen tertinggi pada variabel x. Tidak ada langkah perencanaan, integrasi, atau kendala yang kompleks.. Bukti: Cari derajat setiap polinomial berikut.; $x^6 - 12x^4 + 3x^2 - 10$

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi derajat polinomial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah konsep dasar polinomial yang seharusnya sudah dikuasai siswa kelas 11. Soal tidak menuntut analisis lebih lanjut. |

Run 2 — solusi: Derajat polinomial adalah pangkat tertinggi dari variabel dalam polinomial tersebut. Untuk polinomial x^6 - 12x^4 + 3x^2 - 10, suku-sukunya memiliki pangkat 6, 4, 2, dan 0. Pangkat tertinggi adalah 6.
- Domain kognitif `classify/knowing`: Soal ini hanya meminta siswa untuk mengidentifikasi pangkat tertinggi dari variabel dalam polinomial, yang merupakan prosedur dasar dalam materi polinomial.. Bukti: Cari derajat setiap polinomial berikut.; x^6 - 12x^4 + 3x^2 - 10
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang definisi derajat polinomial, yang merupakan konsep dasar dalam aljabar polinomial.. Bukti: Cari derajat setiap polinomial berikut.
- Intended difficulty `classify/Easy`: Soal ini sangat langsung dan hanya memerlukan pengenalan definisi derajat polinomial. Tidak ada langkah perencanaan atau integrasi yang diperlukan.. Bukti: Cari derajat setiap polinomial berikut.; x^6 - 12x^4 + 3x^2 - 10

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang notasi eksponen dan polinomial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah konsep dasar polinomial yang diajarkan di awal bab. Siswa kelas 11 seharusnya sudah sangat familiar dengan konsep ini. |

Run 3 — solusi: Derajat polinomial adalah pangkat tertinggi dari variabel dalam polinomial tersebut. Untuk $x^6 - 12x^4 + 3x^2 - 10$, pangkat-pangkat variabelnya adalah 6, 4, dan 2. Pangkat tertingginya adalah 6.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi derajat polinomial, yang merupakan definisi dasar dalam materi polinomial. Siswa hanya perlu mengenali pangkat tertinggi dari variabel yang ada.. Bukti: Cari derajat setiap polinomial berikut.; $x^6 - 12x^4 + 3x^2 - 10$
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang definisi atau istilah dasar dalam polinomial, yaitu derajat polinomial.. Bukti: Cari derajat setiap polinomial berikut.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan langsung. Siswa hanya perlu melihat pangkat tertinggi dari suku-suku polinomial yang diberikan tanpa perlu melakukan perhitungan atau manipulasi aljabar.. Bukti: Cari derajat setiap polinomial berikut.; $x^6 - 12x^4 + 3x^2 - 10$

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang notasi eksponen dan definisi polinomial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah konsep dasar polinomial yang diajarkan di awal bab. Tidak ada tuntutan kognitif yang kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4001`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal hanya meminta siswa untuk mengidentifikasi pangkat tertinggi dari variabel dalam polinomial, yang merupakan definisi dasar derajat polinomial.
- Dimensi pengetahuan `factual`: Soal ini menguji pemahaman tentang definisi atau istilah dasar dalam polinomial, yaitu derajat polinomial.
- Intended difficulty `Easy`: Soal ini sangat mendasar dan langsung. Siswa hanya perlu melihat pangkat tertinggi dari suku-suku polinomial yang diberikan tanpa perlu melakukan perhitungan atau manipulasi aljabar.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang notasi eksponen dan definisi polinomial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah konsep dasar polinomial yang diajarkan di awal bab. Tidak ada tuntutan kognitif yang kompleks. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Polinomial dan Fungsi Polinomial
Tipe soal: multiple_choice
Stimulus: -
Soal: $x^6 - 12x^4 + 3x^2 - 10$

Cari derajat setiap polinomial berikut.
Pilihan: A. 2
B. 12
C. 6
D. 4
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "factual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `25d0e4b66183f8ef562d0c9a`

$(2x^4 - x^3 + 4x - 12) - (x^4 + 2x^3 - x^2 - 6)$<br><br>Sederhanakan penjumlahan dan pengurangan polinomial berikut ini.

| Opsi | Isi |
|---|---|
| A | $x^4 - 3x^3 + x^2 + 4x - 18$ |
| B | $x^4 - 3x^3 - x^2 + 4x - 6$ |
| C | $x^4 - 3x^3 + x^2 + 4x - 6$ |
| D | $2x^4 - 3x^3 + x^2 + 4x - 6$ |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Distribusikan tanda negatif ke polinomial kedua: (2x^4 - x^3 + 4x - 12) - x^4 - 2x^3 + x^2 + 6. Kelompokkan suku sejenis: (2-1)x^4 + (-1-2)x^3 + x^2 + 4x + (-12+6) = x^4 - 3x^3 + x^2 + 4x - 6.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fc09be55ce10b8825ad55f428aeec3a2995ed65e444c5ed48db39b9a3e8b2fda`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2880 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2901 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2904 |

Run 1 — solusi: Distribusikan tanda negatif ke polinomial kedua: (2x^4 - x^3 + 4x - 12) - x^4 - 2x^3 + x^2 + 6. Kelompokkan suku sejenis: (2-1)x^4 + (-1-2)x^3 + x^2 + 4x + (-12+6) = x^4 - 3x^3 + x^2 + 4x - 6.
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan operasi pengurangan polinomial secara langsung dengan menggabungkan suku-suku sejenis. Ini adalah prosedur rutin yang langsung.. Bukti: (2x^4 - x^3 + 4x - 12) - (x^4 + 2x^3 - x^2 - 6)
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menerapkan algoritma penjumlahan/pengurangan polinomial (menggabungkan suku sejenis) yang merupakan prosedur standar.. Bukti: Sederhanakan penjumlahan dan pengurangan polinomial berikut ini.
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung dengan tingkat kesulitan rendah. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: (2x^4 - x^3 + 4x - 12) - (x^4 + 2x^3 - x^2 - 6)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aljabar dasar dan penggabungan suku sejenis. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 8 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi polinomial adalah materi dasar kelas 11. Soal ini hanya memerlukan ketelitian dalam distribusi tanda negatif dan penggabungan suku sejenis, yang merupakan keterampilan dasar. |

Run 2 — solusi: Distribusi tanda negatif: (2x^4 - x^3 + 4x - 12) - x^4 - 2x^3 + x^2 + 6. Mengelompokkan suku sejenis: (2-1)x^4 + (-1-2)x^3 + x^2 + 4x + (-12+6) = x^4 - 3x^3 + x^2 + 4x - 6.
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan operasi pengurangan polinomial secara langsung dengan mengelompokkan suku-suku sejenis. Ini adalah prosedur rutin yang sudah dipelajari.. Bukti: Sederhanakan penjumlahan dan pengurangan polinomial berikut ini.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menerapkan algoritma penjumlahan/pengurangan polinomial (prosedural) dengan memahami konsep distribusi tanda negatif pada kurung (konseptual).. Bukti: (2x^4 - x^3 + 4x - 12) - (x^4 + 2x^3 - x^2 - 6)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan langkah-langkah yang jelas dan langsung. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: (2x^4 - x^3 + 4x - 12) - (x^4 + 2x^3 - x^2 - 6)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aljabar dasar dan distribusi tanda negatif. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 8 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi polinomial adalah materi dasar kelas 11 yang merupakan kelanjutan langsung dari aljabar SMP/kelas 10. Soal ini tidak memiliki tingkat kesulitan tinggi. |

Run 3 — solusi: Distribusi tanda negatif: (2x^4 - x^3 + 4x - 12) - x^4 - 2x^3 + x^2 + 6. Mengelompokkan suku sejenis: (2-1)x^4 + (-1-2)x^3 + x^2 + 4x + (-12+6) = x^4 - 3x^3 + x^2 + 4x - 6.
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan operasi pengurangan polinomial dasar dengan mengelompokkan suku-suku sejenis. Ini adalah prosedur rutin yang langsung, tidak memerlukan strategi nonrutin atau integrasi konsep yang kompleks.. Bukti: Sederhanakan penjumlahan dan pengurangan polinomial berikut ini.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menerapkan algoritma penjumlahan/pengurangan polinomial, yang merupakan prosedur standar dalam aljabar.. Bukti: (2x^4 - x^3 + 4x - 12) - (x^4 + 2x^3 - x^2 - 6)
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung dengan langkah-langkah yang jelas dan familiar bagi siswa kelas 11. Tidak ada kendala yang berinteraksi atau kebutuhan untuk perencanaan strategi yang kompleks.. Bukti: (2x^4 - x^3 + 4x - 12) - (x^4 + 2x^3 - x^2 - 6)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aljabar dasar dan penyederhanaan bentuk polinomial. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 8 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pengurangan polinomial adalah materi dasar yang sudah dikuasai sebelum kelas 11, sehingga soal ini tergolong mudah bagi jenjang tersebut. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
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
Subtopik: Penjumlahan, Pengurangan, dan Perkalian Polinomial
Tipe soal: multiple_choice
Stimulus: -
Soal: $(2x^4 - x^3 + 4x - 12) - (x^4 + 2x^3 - x^2 - 6)$

Sederhanakan penjumlahan dan pengurangan polinomial berikut ini.
Pilihan: A. $x^4 - 3x^3 + x^2 + 4x - 18$
B. $x^4 - 3x^3 - x^2 + 4x - 6$
C. $x^4 - 3x^3 + x^2 + 4x - 6$
D. $2x^4 - 3x^3 + x^2 + 4x - 6$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 15. Soal `0dcbc3b7c9d9150afc212041`

$(3m^2n + mn - 12) + (2m^2n - mn^2 + 7)$<br><br>Sederhanakan penjumlahan dan pengurangan polinomial berikut ini.

| Opsi | Isi |
|---|---|
| A | $5m^2n - mn^2 + mn - 5$ |
| B | $5m^2n - mn^2 + mn + 19$ |
| C | $m^2n - mn^2 + mn - 5$ |
| D | $5m^2n + mn^2 + mn - 5$ |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: (3m^2n + 2m^2n) - mn^2 + mn + (-12 + 7) = 5m^2n - mn^2 + mn - 5
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `dbf5d2e1a17ff101899fb38a3786f46dcefcfa3dcfa868a73673c15ed4e80ee5`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 3318 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2780 |
| 3 | success | valid / verified | knowing | procedural | Easy | 3502 |

Run 1 — solusi: (3m^2n + 2m^2n) - mn^2 + mn + (-12 + 7) = 5m^2n - mn^2 + mn - 5
- Domain kognitif `classify/knowing`: Soal ini hanya meminta siswa untuk mengidentifikasi dan menjumlahkan suku-suku sejenis dalam polinomial. Tidak ada strategi nonrutin atau integrasi konsep yang diperlukan.. Bukti: (3m^2n + mn - 12) + (2m^2n - mn^2 + 7); Sederhanakan penjumlahan dan pengurangan polinomial
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan algoritma standar untuk menyederhanakan bentuk aljabar dengan mengelompokkan suku-suku sejenis.. Bukti: Sederhanakan penjumlahan dan pengurangan polinomial
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, tidak memerlukan perencanaan langkah yang kompleks atau integrasi kendala.. Bukti: (3m^2n + mn - 12) + (2m^2n - mn^2 + 7)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi dasar aljabar dan pengelompokan suku sejenis. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini merupakan prasyarat dasar aljabar yang sudah dikuasai sebelum jenjang kelas 11. |

Run 2 — solusi: Kelompokkan suku-suku sejenis: (3m^2n + 2m^2n) + (mn) + (-mn^2) + (-12 + 7) = 5m^2n - mn^2 + mn - 5.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengidentifikasi dan menjumlahkan koefisien dari suku-suku yang sejenis. Ini adalah prosedur langsung tanpa memerlukan strategi non-rutin atau integrasi konsep yang kompleks.. Bukti: (3m^2n + mn - 12) + (2m^2n - mn^2 + 7)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dasar mengenai operasi aljabar pada polinomial, yaitu pengelompokan suku sejenis.. Bukti: Sederhanakan penjumlahan dan pengurangan polinomial
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk tingkat kelas 11. Tidak ada kendala yang berinteraksi, tidak ada pemilihan strategi yang kompleks, dan langkah penyelesaiannya sangat rutin.. Bukti: (3m^2n + mn - 12) + (2m^2n - mn^2 + 7)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar aljabar tentang suku sejenis dan operasi penjumlahan bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun berada di kelas 11, materi ini adalah prasyarat dasar aljabar yang jauh di bawah ekspektasi kompetensi kelas 11 Matematika Tingkat Lanjut. |

Run 3 — solusi: Mengelompokkan suku-suku sejenis: (3m^2n + 2m^2n) + (-mn^2) + (mn) + (-12 + 7) = 5m^2n - mn^2 + mn - 5.
- Domain kognitif `classify/knowing`: Soal ini menuntut penerapan langsung prosedur penjumlahan polinomial dengan mengelompokkan suku sejenis. Tidak ada strategi nonrutin atau penalaran kompleks yang diperlukan.. Bukti: (3m^2n + mn - 12) + (2m^2n - mn^2 + 7); Sederhanakan penjumlahan dan pengurangan polinomial
- Dimensi pengetahuan `classify/procedural`: Tugas ini berfokus pada eksekusi algoritma standar untuk menyederhanakan bentuk aljabar.. Bukti: Sederhanakan penjumlahan dan pengurangan polinomial
- Intended difficulty `classify/Easy`: Soal ini merupakan latihan rutin yang sangat dasar. Siswa hanya perlu mengidentifikasi suku sejenis dan menjumlahkan koefisiennya tanpa kendala atau langkah yang saling bergantung.. Bukti: (3m^2n + mn - 12) + (2m^2n - mn^2 + 7)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dan pengurangan aljabar dasar (suku sejenis). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah latihan rutin penjumlahan polinomial yang sangat dasar, sesuai untuk awal materi kelas 11 atau pengulangan materi SMP/kelas 10. Tidak ada tuntutan integrasi atau perencanaan yang kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
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
Subtopik: Penjumlahan, Pengurangan, dan Perkalian Polinomial
Tipe soal: multiple_choice
Stimulus: -
Soal: $(3m^2n + mn - 12) + (2m^2n - mn^2 + 7)$

Sederhanakan penjumlahan dan pengurangan polinomial berikut ini.
Pilihan: A. $5m^2n - mn^2 + mn - 5$
B. $5m^2n - mn^2 + mn + 19$
C. $m^2n - mn^2 + mn - 5$
D. $5m^2n + mn^2 + mn - 5$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `810355e25e67029b62ca669b`

Misalkan $P(x) = 3x^6 - 11x^5 + x^3 + 20x^2 - 3$ dan $c = \frac{2}{3}$. Gunakan metode Horner dan Teorema Sisa untuk menentukan nilai $P(c)$.

| Opsi | Isi |
|---|---|
| A | $-282$ |
| B | $-5$ |
| C | $5$ |
| D | $12$ |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Koefisien P(x) adalah 3, -11, 0, 1, 20, 0, -3. Menggunakan metode Horner dengan c = 2/3: 3 turun, 3*(2/3)=2, -11+2=-9, -9*(2/3)=-6, 0-6=-6, -6*(2/3)=-4, 1-4=-3, -3*(2/3)=-2, 20-2=18, 18*(2/3)=12, 0+12=12, 12*(2/3)=8, -3+8=5. Sisa akhir adalah 5.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['menerapkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `780f2a30eb577b61a22099a80d28760a294adf5d69dfcc8867fa102153ca9ffc`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3724 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2860 |
| 3 | success | valid / verified | applying | procedural | Medium | 2869 |

Run 1 — solusi: Koefisien polinomial: 3, -11, 0, 1, 20, 0, -3. Menggunakan metode Horner dengan c = 2/3: 3 -> (3*2/3)-11 = -9 -> (-9*2/3)+0 = -6 -> (-6*2/3)+1 = -3 -> (-3*2/3)+20 = 18 -> (18*2/3)+0 = 12 -> (12*2/3)-3 = 5. Sisa = 5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur algoritma Horner yang sudah familiar untuk mengevaluasi nilai polinomial pada titik tertentu.. Bukti: Gunakan metode Horner dan Teorema Sisa untuk menentukan nilai P(c)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji penguasaan algoritma pembagian atau evaluasi polinomial (metode Horner) yang merupakan prosedur standar.. Bukti: Gunakan metode Horner dan Teorema Sisa
- Intended difficulty `classify/Easy`: Soal ini adalah penerapan langsung dari algoritma Horner. Tidak ada kendala yang berinteraksi atau strategi non-rutin yang diperlukan.. Bukti: Gunakan metode Horner dan Teorema Sisa untuk menentukan nilai P(c)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman koefisien polinomial dan operasi aritmatika dasar dengan pecahan. |
| dependentSteps | 6 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan latihan rutin metode Horner. Meskipun polinomial berderajat 6, langkah-langkahnya bersifat repetitif dan prosedural, sehingga dikategorikan Easy untuk kelas 11. |

Run 2 — solusi: Menggunakan skema Horner dengan koefisien 3, -11, 0, 1, 20, 0, -3 dan c = 2/3: 3 turun, 3*(2/3)=2, -11+2=-9, -9*(2/3)=-6, 0-6=-6, -6*(2/3)=-4, 1-4=-3, -3*(2/3)=-2, 20-2=18, 18*(2/3)=12, 0+12=12, 12*(2/3)=8, -3+8=5. Sisa akhir adalah 5.
- Domain kognitif `classify/knowing`: Soal meminta penerapan prosedur algoritma yang spesifik (metode Horner) untuk mengevaluasi polinomial. Siswa hanya perlu menjalankan langkah-langkah prosedural yang sudah ditentukan tanpa perlu merancang strategi baru atau melakukan integrasi konsep yang kompleks.. Bukti: Gunakan metode Horner dan Teorema Sisa untuk menentukan nilai P(c)
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman dan kemampuan eksekusi algoritma pembagian polinomial (metode Horner) yang merupakan prosedur standar dalam materi polinomial.. Bukti: Gunakan metode Horner dan Teorema Sisa
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena prosedurnya sangat rutin dan eksplisit (metode Horner). Meskipun polinomial berderajat 6, langkah-langkahnya bersifat mekanis dan familiar bagi siswa kelas 11. Tidak ada kendala yang berinteraksi atau kebutuhan untuk memilih strategi; siswa hanya perlu mengikuti algoritma.. Bukti: P(x) = 3x^6 - 11x^5 + x^3 + 20x^2 - 3; c = 2/3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmatika dasar dan pemahaman skema Horner. |
| dependentSteps | 6 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi polinomial dan metode Horner adalah standar kurikulum kelas 11. Prosedur ini bersifat rutin dan tidak memerlukan penalaran tingkat tinggi. |

Run 3 — solusi: Koefisien P(x) adalah 3, -11, 0, 1, 20, 0, -3. Menggunakan metode Horner dengan c = 2/3: 3 turun, 3*(2/3)=2, -11+2=-9, -9*(2/3)=-6, 0-6=-6, -6*(2/3)=-4, 1-4=-3, -3*(2/3)=-2, 20-2=18, 18*(2/3)=12, 0+12=12, 12*(2/3)=8, -3+8=5. Sisa akhir adalah 5.
- Domain kognitif `classify/applying`: Soal meminta penerapan algoritma spesifik (metode Horner) untuk mengevaluasi polinomial pada nilai tertentu. Siswa hanya perlu menjalankan prosedur rutin yang sudah dipelajari di kelas 11 untuk pembagian polinomial.. Bukti: Gunakan metode Horner dan Teorema Sisa untuk menentukan nilai P(c)
- Dimensi pengetahuan `classify/procedural`: Soal menguji penguasaan algoritma prosedural (metode Horner) untuk menyelesaikan masalah evaluasi polinomial.. Bukti: Gunakan metode Horner dan Teorema Sisa
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena melibatkan polinomial derajat 6 dengan koefisien yang memerlukan ketelitian tinggi dalam operasi pecahan (2/3). Meskipun prosedurnya rutin, jumlah langkah (6 iterasi Horner) dan potensi kesalahan hitung pada pecahan memberikan beban kognitif yang cukup bagi siswa kelas 11.. Bukti: P(x) = 3x^6 - 11x^5 + x^3 + 20x^2 - 3; c = 2/3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmatika pecahan dan konsep dasar pembagian polinomial (Horner). |
| dependentSteps | 6 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun metodenya standar, derajat polinomial yang tinggi (derajat 6) dan penggunaan pecahan sebagai pembagi meningkatkan beban komputasi dan risiko kesalahan, yang sesuai dengan tuntutan Medium untuk kelas 11. |

Histori retry: run 2 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 3 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 2, "Medium": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4666`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan prosedur algoritma Horner yang sudah familiar untuk mengevaluasi nilai polinomial pada titik tertentu. Ini adalah penerapan prosedur standar.
- Dimensi pengetahuan `procedural`: Soal menguji penguasaan algoritma prosedural (metode Horner) untuk menyelesaikan masalah evaluasi polinomial.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena melibatkan polinomial derajat 6 dengan koefisien yang memerlukan ketelitian tinggi dalam operasi pecahan (2/3). Meskipun prosedurnya rutin, jumlah langkah (6 iterasi Horner) dan potensi kesalahan hitung pada pecahan memberikan beban kognitif yang cukup bagi siswa kelas 11.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aritmatika pecahan dan konsep dasar pembagian polinomial (Horner). |
| dependentSteps | 6 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun metodenya standar, derajat polinomial yang tinggi (derajat 6) dan penggunaan pecahan sebagai pembagi meningkatkan beban komputasi dan risiko kesalahan, yang sesuai dengan tuntutan Medium untuk kelas 11. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Pembagian Polinomial
Tipe soal: multiple_choice
Stimulus: -
Soal: Misalkan $P(x) = 3x^6 - 11x^5 + x^3 + 20x^2 - 3$ dan $c = \frac{2}{3}$. Gunakan metode Horner dan Teorema Sisa untuk menentukan nilai $P(c)$.
Pilihan: A. $-282$
B. $-5$
C. $5$
D. $12$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 17. Soal `a98a9e8ffc21623c387d4f68`

Karena polinomial $P(x)$ dibagi dengan $x - c$ memiliki sisa $k$, nilai $P(c) = ….$

| Opsi | Isi |
|---|---|
| A | $-k$ |
| B | $0$ |
| C | $Q(c)$ |
| D | $k$ |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Berdasarkan Teorema Sisa, jika polinomial P(x) dibagi oleh (x - c), maka sisa pembagiannya adalah P(c). Karena diketahui sisa pembagiannya adalah k, maka P(c) = k.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `44ec7f012625bdc798a125aa1fbc87e19cc15e97b83fd8b648586001ad87e773`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2630 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2635 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2663 |

Run 1 — solusi: Berdasarkan Teorema Sisa, jika polinomial P(x) dibagi oleh (x - c), maka sisa pembagiannya adalah P(c). Karena diketahui sisa pembagiannya adalah k, maka P(c) = k.
- Domain kognitif `classify/knowing`: Soal ini hanya meminta siswa untuk mengingat dan menerapkan definisi langsung dari Teorema Sisa tanpa perlu manipulasi aljabar atau langkah tambahan.. Bukti: Karena polinomial P(x) dibagi dengan x - c memiliki sisa k, nilai P(c) = ….
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman terhadap prinsip dasar atau teorema dalam polinomial, yang merupakan pengetahuan konseptual.. Bukti: Karena polinomial P(x) dibagi dengan x - c memiliki sisa k, nilai P(c) = ….
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan merupakan penerapan langsung dari definisi Teorema Sisa. Tidak ada langkah perencanaan atau integrasi yang diperlukan.. Bukti: Karena polinomial P(x) dibagi dengan x - c memiliki sisa k, nilai P(c) = ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pembagian polinomial dan Teorema Sisa. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 11, Teorema Sisa adalah materi dasar yang sudah dipelajari. Soal ini hanya menanyakan definisi, sehingga tingkat kesulitannya rendah. |

Run 2 — solusi: Berdasarkan Teorema Sisa, jika polinomial P(x) dibagi oleh (x - c), maka sisanya adalah P(c). Karena soal menyatakan sisa pembagian adalah k, maka P(c) = k.
- Domain kognitif `classify/knowing`: Soal ini hanya menuntut siswa untuk mengingat dan menerapkan definisi langsung dari Teorema Sisa tanpa perlu manipulasi atau strategi tambahan.. Bukti: Karena polinomial P(x) dibagi dengan x - c memiliki sisa k, nilai P(c) = ….
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman terhadap konsep dasar atau prinsip Teorema Sisa dalam polinomial.. Bukti: Karena polinomial P(x) dibagi dengan x - c memiliki sisa k, nilai P(c) = ….
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan merupakan penerapan langsung dari teorema yang dipelajari di kelas 11. Tidak ada langkah yang saling bergantung atau kendala yang perlu diintegrasikan.. Bukti: Karena polinomial P(x) dibagi dengan x - c memiliki sisa k, nilai P(c) = ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pembagian polinomial dan Teorema Sisa. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 Matematika Tingkat Lanjut seharusnya sudah menguasai Teorema Sisa sebagai konsep dasar polinomial. Soal ini tidak memerlukan perencanaan atau integrasi langkah. |

Run 3 — solusi: Berdasarkan Teorema Sisa, jika polinomial P(x) dibagi oleh (x - c), maka sisa pembagiannya adalah P(c). Karena diketahui sisa pembagiannya adalah k, maka P(c) = k.
- Domain kognitif `classify/knowing`: Soal ini hanya meminta siswa untuk mengingat dan menerapkan definisi langsung dari Teorema Sisa tanpa perlu melakukan manipulasi aljabar atau perencanaan strategi yang kompleks.. Bukti: Karena polinomial P(x) dibagi dengan x - c memiliki sisa k, nilai P(c) = ….
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap prinsip dasar atau teorema dalam polinomial (Teorema Sisa).. Bukti: Karena polinomial P(x) dibagi dengan x - c memiliki sisa k, nilai P(c) = ….
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan merupakan penerapan langsung dari definisi Teorema Sisa. Tidak ada langkah perhitungan atau integrasi konsep yang diperlukan.. Bukti: Karena polinomial P(x) dibagi dengan x - c memiliki sisa k, nilai P(c) = ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pembagian polinomial dan Teorema Sisa. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 11, Teorema Sisa adalah materi dasar. Soal ini hanya menanyakan definisi, sehingga tingkat kesulitannya rendah. |

Histori retry: run 1 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 2 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 3 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

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
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Pembagian Polinomial
Tipe soal: multiple_choice
Stimulus: -
Soal: Karena polinomial $P(x)$ dibagi dengan $x - c$ memiliki sisa $k$, nilai $P(c) = ….$
Pilihan: A. $-k$
B. $0$
C. $Q(c)$
D. $k$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `a98624ce0ee70784807495e3`

Faktorkan $P(x) = 5x^3 - 28x^2 + 45x - 18$ secara lengkap.

| Opsi | Isi |
|---|---|
| A | $P(x) = (x-2)(x-3)\left(x-\frac{3}{5}\right)$ |
| B | $P(x) = (5x-3)(x-2)(x-3)$ |
| C | $P(x) = (5x-3)(x+2)(x-3)$ |
| D | $P(x) = (5x+3)(x-2)(x-3)$ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Uji akar rasional: P(2) = 5(8) - 28(4) + 45(2) - 18 = 0. Maka (x-2) adalah faktor. Bagi P(x) dengan (x-2) menghasilkan 5x^2 - 18x + 9. Faktorkan 5x^2 - 18x + 9 = (5x-3)(x-3). Jadi, P(x) = (x-2)(x-3)(5x-3).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `aa39752f33fca19b22255bb5b04b60800915ab5946dbead4ce426674dddfbcfe`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2912 |
| 2 | success | valid / verified | applying | procedural | Easy | 2883 |
| 3 | success | valid / verified | applying | procedural | Medium | 2901 |

Run 1 — solusi: Uji akar rasional: P(2) = 5(8) - 28(4) + 45(2) - 18 = 40 - 112 + 90 - 18 = 0. Maka (x-2) adalah faktor. Bagi P(x) dengan (x-2) menghasilkan 5x^2 - 18x + 9. Faktorkan 5x^2 - 18x + 9 = (5x-3)(x-3). Jadi, P(x) = (x-2)(x-3)(5x-3).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur teorema faktor dan pembagian polinomial (atau metode Horner) untuk menemukan akar-akar dan memfaktorkan polinomial derajat tiga. Ini adalah penerapan prosedur standar dalam konteks rutin.. Bukti: Faktorkan P(x) = 5x^3 - 28x^2 + 45x - 18 secara lengkap.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritme faktorisasi polinomial dan hubungan antara akar dengan faktor linear.. Bukti: Faktorkan P(x) = 5x^3 - 28x^2 + 45x - 18 secara lengkap.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah yang saling terkait: mencari akar rasional (teorema faktor), melakukan pembagian polinomial, dan memfaktorkan hasil bagi kuadrat. Meskipun prosedurnya familiar, terdapat beberapa tahap yang harus dilakukan secara berurutan dan teliti.. Bukti: Faktorkan P(x) = 5x^3 - 28x^2 + 45x - 18 secara lengkap.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema faktor, pembagian polinomial (Horner/bersusun), faktorisasi kuadrat. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan mampu memfaktorkan polinomial derajat tiga dengan metode standar. Tingkat kesulitan sedang karena melibatkan koefisien utama bukan 1 dan memerlukan ketelitian dalam pembagian serta faktorisasi akhir. |

Run 2 — solusi: Uji akar rasional: P(2) = 5(8) - 28(4) + 45(2) - 18 = 40 - 112 + 90 - 18 = 0. Maka (x-2) adalah faktor. Bagi P(x) dengan (x-2) menghasilkan 5x^2 - 18x + 9. Faktorkan 5x^2 - 18x + 9 = (5x-3)(x-3). Jadi, P(x) = (x-2)(x-3)(5x-3).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan teorema faktor dan prosedur pembagian polinomial (seperti metode Horner atau pembagian bersusun) untuk menemukan akar-akar dan memfaktorkan polinomial derajat tiga. Ini adalah penerapan prosedur standar.. Bukti: Faktorkan P(x) = 5x^3 - 28x^2 + 45x - 18 secara lengkap.
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut pemahaman tentang hubungan antara akar polinomial dan faktor linear, serta penggunaan algoritma pembagian polinomial.. Bukti: Faktorkan P(x) = 5x^3 - 28x^2 + 45x - 18 secara lengkap.
- Intended difficulty `classify/Easy`: Soal ini merupakan latihan rutin untuk kelas 11. Siswa perlu melakukan uji akar rasional, pembagian polinomial, dan faktorisasi kuadrat. Langkah-langkahnya jelas dan familiar.. Bukti: Faktorkan P(x) = 5x^3 - 28x^2 + 45x - 18 secara lengkap.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema faktor, pembagian polinomial (Horner/bersusun), faktorisasi persamaan kuadrat. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi faktorisasi polinomial derajat 3 adalah standar kurikulum kelas 11. Prosedur yang diperlukan bersifat rutin dan tidak memerlukan strategi non-rutin. |

Run 3 — solusi: Uji akar rasional: P(2) = 5(8) - 28(4) + 45(2) - 18 = 40 - 112 + 90 - 18 = 0. Maka (x-2) adalah faktor. Bagi P(x) dengan (x-2) menghasilkan 5x^2 - 18x + 9. Faktorkan kuadrat tersebut: (5x-3)(x-3). Hasil lengkap: (x-2)(x-3)(5x-3).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur faktorisasi polinomial derajat tiga dengan mencari akar rasional terlebih dahulu, kemudian melakukan pembagian polinomial dan faktorisasi kuadrat. Ini adalah penerapan prosedur standar yang rutin dalam kurikulum kelas 11.. Bukti: Faktorkan P(x) = 5x^3 - 28x^2 + 45x - 18 secara lengkap.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma faktorisasi polinomial (teorema faktor dan pembagian polinomial), yang merupakan pengetahuan prosedural.. Bukti: Faktorkan P(x) = 5x^3 - 28x^2 + 45x - 18 secara lengkap.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah yang saling bergantung (mencari akar, pembagian polinomial, faktorisasi kuadrat) tanpa bantuan langkah antara. Meskipun prosedurnya familiar, siswa harus merencanakan urutan langkah tersebut secara mandiri.. Bukti: Faktorkan P(x) = 5x^3 - 28x^2 + 45x - 18 secara lengkap.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema faktor, pembagian polinomial (Horner atau bersusun), faktorisasi persamaan kuadrat. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan mampu memfaktorkan polinomial derajat tiga dengan lancar. Soal ini menuntut ketelitian dalam koefisien utama (5) dan tanda, namun alurnya standar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4794`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur teorema faktor dan pembagian polinomial (seperti metode Horner atau pembagian bersusun) untuk menemukan akar-akar dan memfaktorkan polinomial derajat tiga. Ini adalah penerapan prosedur standar dalam konteks rutin.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang algoritme faktorisasi polinomial dan hubungan antara akar dengan faktor linear.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah yang saling bergantung (mencari akar, pembagian polinomial, faktorisasi kuadrat) tanpa bantuan langkah antara. Meskipun prosedurnya familiar, siswa harus merencanakan urutan langkah tersebut secara mandiri dan teliti terhadap koefisien utama.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema faktor, pembagian polinomial (Horner atau bersusun), faktorisasi persamaan kuadrat. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan mampu memfaktorkan polinomial derajat tiga dengan lancar. Soal ini menuntut ketelitian dalam koefisien utama (5) dan tanda, namun alurnya standar. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Faktor dan Pembuat Nol Polinomial
Tipe soal: multiple_choice
Stimulus: -
Soal: Faktorkan $P(x) = 5x^3 - 28x^2 + 45x - 18$ secara lengkap.
Pilihan: A. $P(x) = (x-2)(x-3)\left(x-\frac{3}{5}\right)$
B. $P(x) = (5x-3)(x-2)(x-3)$
C. $P(x) = (5x-3)(x+2)(x-3)$
D. $P(x) = (5x+3)(x-2)(x-3)$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 19. Soal `c7f108d75ca02eb28d8fc074`

Untuk suatu polinomial $P(x)$, nilai $P(10)$ adalah 0. Dengan demikian, …. adalah faktor polinomial tersebut.

| Opsi | Isi |
|---|---|
| A | $(x - 10)$ |
| B | $(x-10)(x+10)$ |
| C | $(x + 10)$ |
| D | $10$ |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Berdasarkan Teorema Faktor, jika P(c) = 0, maka (x - c) adalah faktor dari P(x). Karena P(10) = 0, maka (x - 10) adalah faktor dari P(x).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `87707dad45736b2e224d5b9812d294ebf0556d0b1ab43dfd067d951d5bf58215`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2655 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2617 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 3070 |

Run 1 — solusi: Berdasarkan Teorema Faktor, jika P(c) = 0, maka (x - c) adalah faktor dari P(x). Karena P(10) = 0, maka (x - 10) adalah faktor dari P(x).
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengingat dan menerapkan definisi langsung dari Teorema Faktor. Tidak ada strategi nonrutin atau integrasi konsep yang kompleks; siswa hanya perlu mengenali hubungan antara pembuat nol (c) dan faktor (x-c).. Bukti: nilai P(10) adalah 0; adalah faktor polinomial tersebut
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang Teorema Faktor, yaitu prinsip dasar yang menghubungkan akar polinomial dengan bentuk faktornya.. Bukti: P(10) adalah 0; faktor polinomial
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan merupakan penerapan langsung dari definisi Teorema Faktor. Tidak ada langkah-langkah yang saling bergantung atau kendala yang harus diintegrasikan.. Bukti: nilai P(10) adalah 0; adalah faktor polinomial tersebut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang Teorema Faktor pada polinomial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah konsep dasar polinomial yang diajarkan di awal materi kelas 11 TL. Soal tidak memerlukan manipulasi aljabar, hanya pengenalan konsep. |

Run 2 — solusi: Berdasarkan Teorema Faktor, jika P(c) = 0, maka (x - c) adalah faktor dari P(x). Karena P(10) = 0, maka (x - 10) adalah faktor dari P(x).
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengingat dan menerapkan definisi langsung dari Teorema Faktor tanpa perlu melakukan manipulasi aljabar atau perencanaan strategi yang kompleks.. Bukti: nilai P(10) adalah 0; adalah faktor polinomial tersebut
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual dasar mengenai hubungan antara pembuat nol polinomial dan bentuk faktornya.. Bukti: nilai P(10) adalah 0; adalah faktor polinomial tersebut
- Intended difficulty `classify/Easy`: Soal ini bersifat sangat langsung (recall) dan merupakan penerapan dasar dari Teorema Faktor yang diajarkan di kelas 11.. Bukti: nilai P(10) adalah 0; adalah faktor polinomial tersebut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang Teorema Faktor polinomial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Soal ini hanya memerlukan pengenalan konsep dasar Teorema Faktor yang merupakan materi standar kelas 11, tanpa ada langkah tambahan atau jebakan yang kompleks. |

Run 3 — solusi: Berdasarkan Teorema Faktor, $(x-c)$ adalah faktor dari polinomial $P(x)$ jika dan hanya jika $P(c) = 0$. Diketahui $P(10) = 0$, maka $c = 10$. Oleh karena itu, $(x-10)$ adalah faktor dari $P(x)$.
- Domain kognitif `classify/knowing`: Soal ini hanya meminta siswa untuk mengenali dan menerapkan definisi langsung dari Teorema Faktor tanpa modifikasi atau langkah tambahan.. Bukti: nilai P(10) adalah 0; adalah faktor polinomial tersebut
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan konseptual antara nilai pembuat nol polinomial dengan bentuk faktornya.. Bukti: Teorema Faktor; P(10) adalah 0
- Intended difficulty `classify/Easy`: Soal ini bersifat mendasar dan langsung menguji pemahaman definisi Teorema Faktor. Tidak ada langkah perencanaan, integrasi konsep, atau kendala yang harus dipecahkan.. Bukti: nilai P(10) adalah 0; adalah faktor polinomial tersebut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi dasar faktor dan akar polinomial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Ini adalah konsep fundamental dalam materi polinomial kelas 11 yang biasanya diajarkan di awal bab. |

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
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Faktor dan Pembuat Nol Polinomial
Tipe soal: multiple_choice
Stimulus: -
Soal: Untuk suatu polinomial $P(x)$, nilai $P(10)$ adalah 0. Dengan demikian, …. adalah faktor polinomial tersebut.
Pilihan: A. $(x - 10)$
B. $(x-10)(x+10)$
C. $(x + 10)$
D. $10$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `329824aeb50ec2a6e01abb9a`

$p^3 - q^3 = ….$

| Opsi | Isi |
|---|---|
| A | $(p-q)(p^2+2pq+q^2)$ |
| B | $(p-q)(p^2-pq+q^2)$ |
| C | $(p-q)^3$ |
| D | $(p-q)(p^2+pq+q^2)$ |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Identitas selisih dua pangkat tiga adalah p^3 - q^3 = (p - q)(p^2 + pq + q^2). Pilihan D sesuai dengan identitas tersebut.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `180cc44095db6de8c7f3d73d98152983e4e19eba1a275ad059d8ab4958fdbe2e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2640 |
| 2 | success | valid / verified | knowing | factual | Easy | 2648 |
| 3 | success | valid / verified | knowing | factual | Easy | 2644 |

Run 1 — solusi: Identitas selisih dua pangkat tiga adalah p^3 - q^3 = (p - q)(p^2 + pq + q^2). Pilihan D sesuai dengan identitas tersebut.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengenali dan menerapkan identitas aljabar dasar (selisih pangkat tiga) yang merupakan pengetahuan faktual/prosedural standar.. Bukti: p^3 - q^3 = ….
- Dimensi pengetahuan `classify/factual`: Soal menguji penguasaan terhadap identitas polinomial dasar yang bersifat faktual/konseptual dalam aljabar.. Bukti: p^3 - q^3 = ….
- Intended difficulty `classify/Easy`: Soal ini adalah penerapan langsung dari rumus identitas aljabar yang sudah dipelajari. Tidak ada langkah perencanaan atau integrasi yang kompleks.. Bukti: p^3 - q^3 = ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang identitas aljabar (selisih pangkat tiga). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan pengingat identitas dasar yang sering muncul dalam materi polinomial kelas 11, sehingga dikategorikan mudah karena hanya memerlukan ingatan atau pengenalan pola langsung. |

Run 2 — solusi: Identitas selisih dua pangkat tiga adalah p^3 - q^3 = (p - q)(p^2 + pq + q^2). Pilihan D sesuai dengan identitas ini.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengenali dan menerapkan identitas aljabar dasar yang sudah dipelajari. Tidak ada langkah penalaran kompleks atau integrasi strategi yang diperlukan, hanya pengenalan rumus.. Bukti: p^3 - q^3 = ….
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual mengenai identitas polinomial (selisih pangkat tiga) yang merupakan elemen dasar dalam aljabar.. Bukti: p^3 - q^3 = ….
- Intended difficulty `classify/Easy`: Soal ini sangat langsung dan hanya memerlukan ingatan atau pengenalan terhadap identitas aljabar standar. Tidak ada langkah-langkah yang saling bergantung atau kendala yang harus diintegrasikan.. Bukti: p^3 - q^3 = ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengetahuan dasar tentang identitas aljabar polinomial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 11, identitas selisih pangkat tiga adalah materi yang sangat mendasar dan familiar. Soal ini tidak menuntut pemrosesan lebih lanjut. |

Run 3 — solusi: Identitas selisih dua pangkat tiga adalah p^3 - q^3 = (p - q)(p^2 + pq + q^2). Pilihan D sesuai dengan identitas ini.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengenali dan mengingat identitas aljabar dasar (selisih pangkat tiga) tanpa perlu melakukan manipulasi atau strategi kompleks.. Bukti: p^3 - q^3 = ….
- Dimensi pengetahuan `classify/factual`: Soal menguji pengetahuan tentang identitas polinomial yang merupakan bagian dari fakta atau prinsip dasar dalam aljabar.. Bukti: p^3 - q^3 = ….
- Intended difficulty `classify/Easy`: Soal ini bersifat sangat langsung (recall). Tidak ada langkah perencanaan, integrasi kendala, atau strategi yang diperlukan. Siswa hanya perlu memilih identitas yang benar dari opsi yang tersedia.. Bukti: p^3 - q^3 = ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang identitas aljabar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengingat identitas aljabar adalah materi dasar yang sudah diperkenalkan sebelum kelas 11, sehingga soal ini sangat mudah bagi siswa kelas 11. |

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
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Identitas Polinomial
Tipe soal: multiple_choice
Stimulus: -
Soal: $p^3 - q^3 = ….$
Pilihan: A. $(p-q)(p^2+2pq+q^2)$
B. $(p-q)(p^2-pq+q^2)$
C. $(p-q)^3$
D. $(p-q)(p^2+pq+q^2)$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "factual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 21. Soal `6b7cde78dfd3973a1d0a64cb`

Apakah persamaan polinomial berikut merupakan identitas polinomial atau bukan? $3(x-1)^2 = (3x-3)^2$

| Opsi | Isi |
|---|---|
| A | Bukan identitas, karena untuk $x=0$: $3(0-1)^2=3$ sedangkan $(3\cdot0-3)^2=9$ (tidak sama) |
| B | Bukan identitas, karena pangkat di kedua ruas berbeda |
| C | Merupakan identitas, karena untuk $x=1$ kedua ruas sama-sama bernilai 0 |
| D | Merupakan identitas, karena kedua ruas sama-sama berbentuk kuadrat sempurna |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Uji identitas dengan substitusi nilai x. Untuk x=0: Ruas kiri = 3(0-1)^2 = 3(1) = 3. Ruas kanan = (3(0)-3)^2 = (-3)^2 = 9. Karena 3 tidak sama dengan 9, maka persamaan bukan identitas.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `158cbb656883c3432b34e608344fca2c1b55d8dd20cdc0abc904378abda2a304`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2753 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2767 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2769 |

Run 1 — solusi: Uji identitas dengan substitusi nilai x. Untuk x=0: Ruas kiri = 3(0-1)^2 = 3(1) = 3. Ruas kanan = (3(0)-3)^2 = (-3)^2 = 9. Karena 3 tidak sama dengan 9, maka persamaan bukan identitas.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengevaluasi kebenaran sebuah identitas polinomial. Ini melibatkan pemahaman konsep identitas (berlaku untuk semua x) dan menerapkan prosedur pengujian dengan nilai tertentu (counterexample) untuk memverifikasi atau menyanggah.. Bukti: Apakah persamaan polinomial berikut merupakan identitas polinomial atau bukan? 3(x-1)^2 = (3x-3)^2
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang definisi identitas polinomial, yang merupakan konsep fundamental dalam aljabar polinomial.. Bukti: Apakah persamaan polinomial berikut merupakan identitas polinomial atau bukan?
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu memahami definisi identitas dan melakukan substitusi sederhana untuk menemukan penyangkal (counterexample). Tidak ada langkah perencanaan yang kompleks atau integrasi kendala yang sulit.. Bukti: Apakah persamaan polinomial berikut merupakan identitas polinomial atau bukan? 3(x-1)^2 = (3x-3)^2

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang operasi aljabar dan definisi identitas polinomial. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 11, membedakan persamaan biasa dengan identitas polinomial adalah materi dasar yang rutin. |

Run 2 — solusi: Sebuah persamaan adalah identitas jika berlaku untuk semua nilai x. Uji x=0: Ruas kiri = 3(0-1)^2 = 3(1) = 3. Ruas kanan = (3(0)-3)^2 = (-3)^2 = 9. Karena 3 tidak sama dengan 9, maka persamaan bukan identitas.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengevaluasi kebenaran sebuah identitas polinomial. Ini memerlukan pemahaman konseptual tentang definisi identitas (berlaku untuk semua x) dan penerapan prosedur pengecekan (substitusi nilai atau ekspansi aljabar) untuk menyangkal klaim tersebut.. Bukti: Apakah persamaan polinomial berikut merupakan identitas polinomial atau bukan?; 3(x-1)^2 = (3x-3)^2
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang definisi identitas polinomial, yang merupakan konsep fundamental dalam aljabar polinomial.. Bukti: Apakah persamaan polinomial berikut merupakan identitas polinomial atau bukan?
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu memahami definisi identitas atau melakukan substitusi sederhana untuk menemukan penyangkal (counterexample). Tidak ada langkah yang saling bergantung yang kompleks atau kendala yang berinteraksi.. Bukti: Apakah persamaan polinomial berikut merupakan identitas polinomial atau bukan? $3(x-1)^2 = (3x-3)^2$

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang operasi aljabar dan definisi identitas polinomial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, membedakan identitas dari persamaan biasa adalah materi dasar. Soal ini tidak menuntut manipulasi aljabar yang rumit. |

Run 3 — solusi: Persamaan adalah identitas jika berlaku untuk semua x. Uji x=0: Ruas kiri = 3(0-1)^2 = 3(1) = 3. Ruas kanan = (3(0)-3)^2 = (-3)^2 = 9. Karena 3 tidak sama dengan 9, maka persamaan bukan identitas.
- Domain kognitif `classify/applying`: Siswa diminta untuk menentukan apakah suatu persamaan merupakan identitas polinomial. Ini memerlukan pemahaman konseptual tentang definisi identitas (berlaku untuk semua nilai variabel) dan penerapan prosedur pengecekan dengan nilai uji (counterexample).. Bukti: Apakah persamaan polinomial berikut merupakan identitas polinomial atau bukan? $3(x-1)^2 = (3x-3)^2$
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang prinsip dasar identitas polinomial, yaitu hubungan kesamaan yang berlaku untuk setiap nilai variabel, yang merupakan konsep fundamental dalam aljabar.. Bukti: Apakah persamaan polinomial berikut merupakan identitas polinomial atau bukan?
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu memahami definisi identitas dan melakukan substitusi nilai sederhana untuk membuktikan ketidaksamaan. Tidak ada langkah perencanaan yang kompleks atau integrasi kendala yang berat.. Bukti: Apakah persamaan polinomial berikut merupakan identitas polinomial atau bukan? $3(x-1)^2 = (3x-3)^2$

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang operasi aljabar dan definisi identitas polinomial. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, membedakan persamaan biasa dengan identitas adalah materi dasar. Soal ini bersifat rutin dan tidak memerlukan manipulasi aljabar yang rumit. |

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
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Identitas Polinomial
Tipe soal: multiple_choice
Stimulus: -
Soal: Apakah persamaan polinomial berikut merupakan identitas polinomial atau bukan? $3(x-1)^2 = (3x-3)^2$
Pilihan: A. Bukan identitas, karena untuk $x=0$: $3(0-1)^2=3$ sedangkan $(3\cdot0-3)^2=9$ (tidak sama)
B. Bukan identitas, karena pangkat di kedua ruas berbeda
C. Merupakan identitas, karena untuk $x=1$ kedua ruas sama-sama bernilai 0
D. Merupakan identitas, karena kedua ruas sama-sama berbentuk kuadrat sempurna
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 22. Soal `d590344d18abe3ebd38fb8ed`

Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.<br><br>\|Waktu (Detik)\|0\|1\|2\|3\|4\|5\|6\|<br>\|---\|---\|---\|---\|---\|---\|---\|---\|<br>\|Jarak (m)\|0\|5\|8\|9\|8\|5\|0\|<br><br>Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah. Jelaskan alasanmu.

| Opsi | Isi |
|---|---|
| A | Tidak dapat ditentukan tanpa menggambar grafiknya. |
| B | Terbuka ke bawah, karena nilai fungsi turun kemudian naik lagi. |
| C | Terbuka ke atas, karena nilai fungsi naik kemudian turun lagi. |
| D | Terbuka ke bawah, karena nilai fungsi (jarak) naik kemudian turun lagi. |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Data menunjukkan nilai jarak meningkat dari 0 (t=0) hingga mencapai puncak 9 (t=3), kemudian menurun kembali ke 0 (t=6). Pola simetris naik-lalu-turun ini menunjukkan kurva parabola yang memiliki titik puncak maksimum, yang secara definitif berarti grafik fungsi kuadrat terbuka ke bawah (koefisien a < 0).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `183a1cdb8642fbc2cb07dae32324fbcae9a4e950712e75ed35d99e20ccabb850`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2900 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2855 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2865 |

Run 1 — solusi: Data menunjukkan nilai jarak meningkat dari 0 (t=0) hingga mencapai puncak 9 (t=3), kemudian menurun kembali ke 0 (t=6). Pola simetris naik-lalu-turun ini menunjukkan kurva parabola yang memiliki titik puncak maksimum, yang secara definitif berarti grafik fungsi kuadrat terbuka ke bawah (koefisien a < 0).
- Domain kognitif `classify/applying`: Siswa diminta untuk menginterpretasikan pola data numerik dan menghubungkannya dengan sifat geometris fungsi kuadrat (arah bukaan parabola) tanpa bantuan visual grafik. Ini memerlukan pemahaman konseptual tentang hubungan antara perilaku nilai fungsi (naik-turun) dengan koefisien fungsi kuadrat.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana karakteristik fungsi kuadrat (arah bukaan) tercermin dalam pola data diskrit, bukan sekadar menghafal rumus.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena pola data sangat jelas dan simetris. Siswa hanya perlu mengenali pola naik-turun sebagai ciri parabola terbuka ke bawah tanpa harus melakukan perhitungan aljabar yang kompleks atau manipulasi rumus.. Bukti: Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk parabola dan pengaruh koefisien kuadrat terhadap arah bukaan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi fungsi kuadrat sering diajarkan di kelas 9/10, soal ini menuntut interpretasi data yang relevan dengan kurikulum kelas 11. Tingkat kesulitan rendah karena pola data sangat eksplisit dan tidak memerlukan perhitungan rumit. |

Run 2 — solusi: Data menunjukkan nilai jarak naik dari 0 (t=0) ke 9 (t=3) lalu turun kembali ke 0 (t=6). Pola simetris naik-lalu-turun ini menunjukkan titik puncak maksimum. Fungsi kuadrat dengan titik puncak maksimum memiliki koefisien a negatif, yang berarti grafik terbuka ke bawah.
- Domain kognitif `classify/applying`: Siswa diminta untuk menginterpretasikan pola data numerik untuk menyimpulkan sifat geometris grafik fungsi kuadrat (arah bukaan) tanpa menggambar. Ini memerlukan pemahaman konseptual tentang hubungan antara perilaku nilai fungsi (naik-turun) dengan koefisien a pada fungsi kuadrat.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana karakteristik fungsi kuadrat (terbuka ke atas/bawah) tercermin dalam pola data diskrit.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu mengenali pola naik-turun sederhana dari tabel yang simetris. Tidak ada perhitungan kompleks atau integrasi konsep yang berat; cukup pengenalan pola dasar fungsi kuadrat.. Bukti: Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi kuadrat dan interpretasi tabel data. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, menginterpretasikan tabel data fungsi kuadrat adalah tugas rutin yang sederhana. Tidak ada tuntutan perencanaan tinggi. |

Run 3 — solusi: Data menunjukkan jarak meningkat dari 0 (t=0) mencapai puncak 9 (t=3) lalu menurun kembali ke 0 (t=6). Pola simetris naik-lalu-turun ini menunjukkan titik puncak (maksimum) pada grafik parabola. Parabola dengan titik maksimum terbuka ke bawah (koefisien a negatif).
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasikan pola data numerik untuk menyimpulkan sifat geometris fungsi kuadrat (arah bukaan parabola) tanpa bantuan visual grafik. Ini memerlukan pemahaman konseptual tentang hubungan antara titik puncak dan arah bukaan parabola.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.
- Dimensi pengetahuan `classify/conceptual`: Siswa menerapkan pemahaman konseptual tentang bentuk parabola (terbuka ke atas/bawah) berdasarkan perilaku nilai fungsi (naik-turun) yang diberikan dalam tabel.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 11. Siswa hanya perlu mengenali pola data (naik ke puncak lalu turun) sebagai karakteristik parabola terbuka ke bawah. Tidak ada perhitungan kompleks atau integrasi konsep yang sulit.. Bukti: Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi kuadrat dan karakteristik grafiknya. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi fungsi kuadrat adalah prasyarat, soal ini sangat mendasar dan hanya meminta pengenalan pola sederhana yang familiar bagi siswa SMA. |

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
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Fungsi Kuadrat
Tipe soal: multiple_choice
Stimulus: -
Soal: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.

|Waktu (Detik)|0|1|2|3|4|5|6|
|---|---|---|---|---|---|---|---|
|Jarak (m)|0|5|8|9|8|5|0|

Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah. Jelaskan alasanmu.
Pilihan: A. Tidak dapat ditentukan tanpa menggambar grafiknya.
B. Terbuka ke bawah, karena nilai fungsi turun kemudian naik lagi.
C. Terbuka ke atas, karena nilai fungsi naik kemudian turun lagi.
D. Terbuka ke bawah, karena nilai fungsi (jarak) naik kemudian turun lagi.
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 23. Soal `225f6a665ad460166f03d3c7`

Nyatakan sudut-sudut berikut ke dalam radian: 45°, 144°, dan 306°.

| Opsi | Isi |
|---|---|
| A | $45° = 45\pi$ rad; $144° = 144\pi$ rad; $306° = 306\pi$ rad |
| B | $45° = \dfrac{1}{4}$; $144° = \dfrac{4}{5}$; $306° = \dfrac{17}{10}$ (tanpa π) |
| C | $45° = \dfrac{\pi}{4}$ rad; $144° = \dfrac{4\pi}{5}$ rad; $306° = \dfrac{17\pi}{10}$ rad |
| D | $45° = \dfrac{\pi}{8}$ rad; $144° = \dfrac{2\pi}{5}$ rad; $306° = \dfrac{17\pi}{20}$ rad |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Menggunakan konversi derajat ke radian: sudut (rad) = sudut (derajat) * (π/180). 45° = 45 * (π/180) = π/4 rad. 144° = 144 * (π/180) = 4π/5 rad. 306° = 306 * (π/180) = 17π/10 rad.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0851594409a242b3b040aca552f79d439b6d83336715c8452b85caa01f7ef723`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 3588 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2912 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2939 |

Run 1 — solusi: Menggunakan konversi derajat ke radian: sudut (rad) = sudut (derajat) * (π/180). 45° = 45 * (π/180) = π/4 rad. 144° = 144 * (π/180) = 4π/5 rad. 306° = 306 * (π/180) = 17π/10 rad.
- Domain kognitif `classify/knowing`: Siswa hanya perlu menerapkan rumus konversi derajat ke radian secara langsung tanpa memerlukan strategi non-rutin atau integrasi konsep yang kompleks.. Bukti: Nyatakan sudut-sudut berikut ke dalam radian: 45°, 144°, dan 306°.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang prosedur konversi satuan sudut yang merupakan algoritma dasar dalam trigonometri.. Bukti: Nyatakan sudut-sudut berikut ke dalam radian: 45°, 144°, dan 306°.
- Intended difficulty `classify/Easy`: Soal ini sangat rutin dan langsung. Tidak ada kendala yang berinteraksi atau kebutuhan untuk perencanaan langkah yang kompleks.. Bukti: Nyatakan sudut-sudut berikut ke dalam radian: 45°, 144°, dan 306°.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi radian dan hubungan 180° = π rad. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konversi satuan sudut adalah materi dasar trigonometri yang merupakan prosedur rutin bagi siswa kelas 11. |

Run 2 — solusi: Konversi derajat ke radian dilakukan dengan mengalikan sudut dengan (π/180). 45° × (π/180) = π/4 rad. 144° × (π/180) = 144π/180 = 4π/5 rad. 306° × (π/180) = 306π/180 = 17π/10 rad.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk menerapkan prosedur konversi satuan sudut yang sudah dipelajari secara langsung tanpa memerlukan strategi non-rutin atau integrasi konsep yang kompleks.. Bukti: Nyatakan sudut-sudut berikut ke dalam radian: 45°, 144°, dan 306°.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami algoritma atau prosedur standar untuk mengubah satuan derajat ke radian.. Bukti: Nyatakan sudut-sudut berikut ke dalam radian
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung dengan satu langkah algoritma yang familiar bagi siswa kelas 11. Tidak ada kendala yang berinteraksi atau kebutuhan untuk perencanaan strategi.. Bukti: Nyatakan sudut-sudut berikut ke dalam radian: 45°, 144°, dan 306°.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang hubungan antara derajat dan radian (180° = π rad). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konversi satuan adalah materi dasar trigonometri yang sudah rutin dilakukan di kelas 11. |

Run 3 — solusi: Konversi derajat ke radian dilakukan dengan mengalikan sudut dengan (π/180). 45° × (π/180) = 45π/180 = π/4 rad. 144° × (π/180) = 144π/180 = 4π/5 rad. 306° × (π/180) = 306π/180 = 17π/10 rad.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk menerapkan prosedur konversi satuan sudut yang sudah dipelajari secara langsung tanpa memerlukan strategi nonrutin atau integrasi konsep yang kompleks.. Bukti: Nyatakan sudut-sudut berikut ke dalam radian: 45°, 144°, dan 306°.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami algoritma atau metode konversi antara dua satuan sudut (derajat ke radian), yang merupakan pengetahuan prosedural.. Bukti: Nyatakan sudut-sudut berikut ke dalam radian
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang sangat jelas dan langsung. Tidak ada kendala yang berinteraksi atau kebutuhan untuk perencanaan strategi yang kompleks.. Bukti: Nyatakan sudut-sudut berikut ke dalam radian: 45°, 144°, dan 306°.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang hubungan antara derajat dan radian (180° = π rad). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konversi satuan sudut adalah materi dasar trigonometri yang familiar bagi siswa kelas 11. Soal ini hanya menuntut penerapan rumus konversi secara langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
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
Subtopik: Fungsi Trigonometri dan Lingkaran Satuan
Tipe soal: multiple_choice
Stimulus: -
Soal: Nyatakan sudut-sudut berikut ke dalam radian: 45°, 144°, dan 306°.
Pilihan: A. $45° = 45\pi$ rad; $144° = 144\pi$ rad; $306° = 306\pi$ rad
B. $45° = \dfrac{1}{4}$; $144° = \dfrac{4}{5}$; $306° = \dfrac{17}{10}$ (tanpa π)
C. $45° = \dfrac{\pi}{4}$ rad; $144° = \dfrac{4\pi}{5}$ rad; $306° = \dfrac{17\pi}{10}$ rad
D. $45° = \dfrac{\pi}{8}$ rad; $144° = \dfrac{2\pi}{5}$ rad; $306° = \dfrac{17\pi}{20}$ rad
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 24. Soal `f08d9643f3fe34bdc0e78a8c`

Untuk mengonversi sebuah sudut yang dinyatakan ke dalam derajat menjadi radian, kalikan sudut tersebut dengan ….

| Opsi | Isi |
|---|---|
| A | $180\pi$ |
| B | $\dfrac{\pi}{180}$ |
| C | $\dfrac{180}{\pi}$ |
| D | $\dfrac{\pi}{360}$ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Konversi sudut dari derajat ke radian menggunakan faktor konversi 180° = π rad. Maka, 1° = π/180 rad. Untuk mengubah x° menjadi radian, kalikan x dengan π/180.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7c09d914e142206d30b91902f02b8f4dd52d2f8c1c23a0c3da71510e4ebb61f2`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2614 |
| 2 | success | valid / verified | knowing | factual | Easy | 2614 |
| 3 | success | valid / verified | knowing | factual | Easy | 2638 |

Run 1 — solusi: Konversi sudut dari derajat ke radian menggunakan faktor konversi 180° = π rad. Maka, 1° = π/180 rad. Untuk mengubah x° menjadi radian, kalikan x dengan π/180.
- Domain kognitif `classify/knowing`: Soal ini hanya menuntut siswa untuk mengingat atau mengenali definisi faktor konversi antara satuan derajat dan radian. Tidak ada proses pemecahan masalah atau penerapan prosedur kompleks.. Bukti: Untuk mengonversi sebuah sudut yang dinyatakan ke dalam derajat menjadi radian, kalikan sudut tersebut dengan ….
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual mengenai definisi dan hubungan dasar antara dua satuan sudut (derajat dan radian).. Bukti: Untuk mengonversi sebuah sudut yang dinyatakan ke dalam derajat menjadi radian
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan merupakan pengetahuan prasyarat dalam topik trigonometri kelas 11. Tidak ada langkah perhitungan atau perencanaan yang diperlukan.. Bukti: Untuk mengonversi sebuah sudut yang dinyatakan ke dalam derajat menjadi radian, kalikan sudut tersebut dengan ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi radian dan derajat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah konsep dasar yang diajarkan di awal materi trigonometri kelas 11 atau bahkan di jenjang sebelumnya, sehingga tingkat kesulitannya rendah. |

Run 2 — solusi: Konversi derajat ke radian didasarkan pada hubungan 180 derajat = π radian. Maka, 1 derajat = π/180 radian. Untuk mengubah x derajat ke radian, kalikan x dengan π/180.
- Domain kognitif `classify/knowing`: Soal ini hanya meminta siswa untuk mengingat atau mengenali fakta dasar mengenai faktor konversi satuan sudut dari derajat ke radian. Tidak ada proses analisis atau penerapan strategi yang kompleks.. Bukti: Untuk mengonversi sebuah sudut yang dinyatakan ke dalam derajat menjadi radian, kalikan sudut tersebut dengan ….
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual tentang definisi dan hubungan dasar antara dua satuan sudut (derajat dan radian).. Bukti: Untuk mengonversi sebuah sudut yang dinyatakan ke dalam derajat menjadi radian
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan merupakan pengetahuan prasyarat atau awal dalam topik trigonometri kelas 11. Tidak ada langkah yang saling bergantung atau kendala yang harus diintegrasikan.. Bukti: Untuk mengonversi sebuah sudut yang dinyatakan ke dalam derajat menjadi radian, kalikan sudut tersebut dengan ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang satuan sudut derajat dan radian. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah konsep dasar yang seharusnya sudah dikuasai siswa di awal pembelajaran trigonometri kelas 11. |

Run 3 — solusi: Konversi sudut dari derajat ke radian didasarkan pada hubungan 180 derajat = π radian. Maka, 1 derajat = π/180 radian. Untuk mengubah x derajat ke radian, kalikan x dengan π/180.
- Domain kognitif `classify/knowing`: Soal ini hanya menuntut siswa untuk mengingat atau mengenali definisi/fakta dasar mengenai faktor konversi satuan sudut antara derajat dan radian. Tidak ada proses analisis atau penerapan yang kompleks.. Bukti: Untuk mengonversi sebuah sudut yang dinyatakan ke dalam derajat menjadi radian, kalikan sudut tersebut dengan ….
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman terhadap fakta atau istilah dasar dalam trigonometri, yaitu faktor konversi satuan sudut.. Bukti: Untuk mengonversi sebuah sudut yang dinyatakan ke dalam derajat menjadi radian
- Intended difficulty `classify/Easy`: Soal ini bersifat sangat langsung (recall) dan merupakan materi dasar yang sudah diperkenalkan sejak awal pembelajaran trigonometri. Tidak ada langkah yang saling bergantung atau kendala yang harus diintegrasikan.. Bukti: Untuk mengonversi sebuah sudut yang dinyatakan ke dalam derajat menjadi radian, kalikan sudut tersebut dengan ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang satuan sudut (derajat dan radian). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah konsep fundamental yang sangat rutin bagi siswa kelas 11 Matematika Tingkat Lanjut. Tidak ada tuntutan kognitif tinggi. |

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
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Fungsi Trigonometri dan Lingkaran Satuan
Tipe soal: multiple_choice
Stimulus: -
Soal: Untuk mengonversi sebuah sudut yang dinyatakan ke dalam derajat menjadi radian, kalikan sudut tersebut dengan ….
Pilihan: A. $180\pi$
B. $\dfrac{\pi}{180}$
C. $\dfrac{180}{\pi}$
D. $\dfrac{\pi}{360}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "factual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 25. Soal `afd6bffcaa9e9f5ad6f3571c`

Grafik fungsi y = a sin k(x – b) + c memiliki amplitudo … dan periode ….

| Opsi | Isi |
|---|---|
| A | amplitudo $\|a\|$, periode $2\pi k$ |
| B | amplitudo $\|a\|$, periode $\dfrac{2\pi}{k}$ |
| C | amplitudo $\|a\|$, periode $\dfrac{k}{2\pi}$ |
| D | amplitudo $a$, periode $\dfrac{2\pi}{k}$ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Bentuk umum fungsi sinus adalah y = a sin k(x - b) + c. Amplitudo didefinisikan sebagai nilai mutlak dari koefisien a, yaitu \|a\|. Periode fungsi sinus dasar adalah 2π. Dengan adanya faktor k pada argumen fungsi, periode fungsi menjadi 2π/k. Pilihan B adalah yang tepat.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `40f68da15a55cf94244b74d24f99f496781dd0f40ffbdc03bc6e69475f05b4b6`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3501 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2716 |
| 3 | success | valid / verified | knowing | factual | Easy | 2739 |

Run 1 — solusi: Amplitudo fungsi y = a sin k(x – b) + c didefinisikan sebagai nilai mutlak dari koefisien a (\|a\|), sedangkan periode fungsi sinus dasar 2π dibagi dengan koefisien k, sehingga periode = 2π/k. Pilihan B adalah satu-satunya yang tepat.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengenali dan menerapkan definisi parameter amplitudo dan periode pada fungsi trigonometri secara langsung tanpa memerlukan langkah penalaran tambahan.. Bukti: Grafik fungsi y = a sin k(x – b) + c memiliki amplitudo … dan periode ….
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep hubungan antara parameter fungsi (a dan k) dengan karakteristik grafik (amplitudo dan periode).. Bukti: Grafik fungsi y = a sin k(x – b) + c
- Intended difficulty `classify/Easy`: Soal ini adalah pertanyaan definisi dasar yang familiar bagi siswa kelas 11. Tidak ada langkah perhitungan kompleks atau integrasi konsep yang diperlukan.. Bukti: Grafik fungsi y = a sin k(x – b) + c memiliki amplitudo … dan periode ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar parameter fungsi trigonometri y = a sin k(x-b) + c. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah materi dasar dalam topik fungsi trigonometri kelas 11. |

Run 2 — solusi: Fungsi y = a sin k(x - b) + c adalah bentuk umum fungsi sinus. Amplitudo didefinisikan sebagai nilai mutlak dari koefisien a, yaitu \|a\|. Periode fungsi sinus dasar y = sin x adalah 2π. Dengan adanya faktor k pada argumen sin k(x-b), periode fungsi menjadi 2π/\|k\|. Karena k biasanya dianggap positif dalam konteks ini, periode adalah 2π/k.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengingat dan menerapkan definisi dasar amplitudo dan periode pada fungsi trigonometri yang telah dimodifikasi parameternya. Tidak ada langkah analisis kompleks atau strategi nonrutin yang diperlukan.. Bukti: Grafik fungsi y = a sin k(x – b) + c memiliki amplitudo … dan periode ….
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual mengenai parameter dalam fungsi trigonometri (amplitudo dan periode) sebagai bagian dari struktur fungsi tersebut.. Bukti: Grafik fungsi y = a sin k(x – b) + c memiliki amplitudo … dan periode ….
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (recall) mengenai rumus dasar fungsi trigonometri. Tidak ada langkah perencanaan atau integrasi yang diperlukan.. Bukti: Grafik fungsi y = a sin k(x – b) + c memiliki amplitudo … dan periode ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi trigonometri y = sin x dan pengaruh parameter a dan k. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 Matematika Tingkat Lanjut diharapkan sudah menguasai bentuk umum fungsi trigonometri ini sebagai materi dasar sebelum masuk ke analisis grafik yang lebih kompleks. |

Run 3 — solusi: Fungsi y = a sin k(x - b) + c memiliki amplitudo yang didefinisikan sebagai nilai mutlak dari koefisien a, yaitu \|a\|. Periode fungsi sinus dasar y = sin x adalah 2π. Dengan adanya faktor k pada argumen x, periode fungsi menjadi 2π/\|k\| (atau 2π/k untuk k positif). Pilihan B secara tepat menyatakan amplitudo \|a\| dan periode 2π/k.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengingat dan menerapkan definisi faktual mengenai parameter amplitudo dan periode pada fungsi trigonometri sinus yang telah dimodifikasi. Tidak ada strategi non-rutin atau integrasi konsep yang kompleks.. Bukti: Grafik fungsi y = a sin k(x – b) + c memiliki amplitudo … dan periode ….
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman siswa terhadap terminologi dan rumus dasar (fakta) yang mendasari grafik fungsi trigonometri.. Bukti: Grafik fungsi y = a sin k(x – b) + c memiliki amplitudo … dan periode ….
- Intended difficulty `classify/Easy`: Soal ini bersifat sangat langsung (recall). Siswa hanya perlu mengidentifikasi rumus standar untuk amplitudo dan periode tanpa perlu melakukan perhitungan atau manipulasi aljabar yang rumit.. Bukti: Grafik fungsi y = a sin k(x – b) + c memiliki amplitudo … dan periode ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang grafik fungsi trigonometri sinus. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah konsep dasar dalam materi fungsi trigonometri kelas 11. Siswa diharapkan sudah familiar dengan bentuk umum fungsi sinus dan pengaruh parameter a dan k terhadap grafik. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 2, "factual": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4193`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini menuntut siswa untuk mengingat dan menerapkan definisi faktual mengenai parameter amplitudo dan periode pada fungsi trigonometri secara langsung tanpa memerlukan langkah penalaran tambahan.
- Dimensi pengetahuan `conceptual`: Siswa perlu memahami konsep hubungan antara parameter fungsi (a dan k) dengan karakteristik grafik (amplitudo dan periode) sebagai bagian dari struktur fungsi tersebut.
- Intended difficulty `Easy`: Soal ini bersifat langsung (recall) mengenai rumus dasar fungsi trigonometri. Tidak ada langkah perencanaan, integrasi konsep, atau perhitungan kompleks yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk umum fungsi trigonometri y = a sin k(x-b) + c. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah materi dasar dalam topik fungsi trigonometri kelas 11. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Grafik Fungsi Trigonometri
Tipe soal: multiple_choice
Stimulus: -
Soal: Grafik fungsi y = a sin k(x – b) + c memiliki amplitudo … dan periode ….
Pilihan: A. amplitudo $|a|$, periode $2\pi k$
B. amplitudo $|a|$, periode $\dfrac{2\pi}{k}$
C. amplitudo $|a|$, periode $\dfrac{k}{2\pi}$
D. amplitudo $a$, periode $\dfrac{2\pi}{k}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 26. Soal `2c29446767c7632fe13c2025`

Periode grafik fungsi y = tan x adalah ….

| Opsi | Isi |
|---|---|
| A | $2\pi$ |
| B | $4\pi$ |
| C | $\pi$ |
| D | $\dfrac{\pi}{2}$ |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Fungsi tangen y = tan x memiliki periode dasar π. Hal ini didasarkan pada identitas tan(x + π) = tan x, yang menunjukkan bahwa grafik berulang setiap interval π radian.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `cb096487e7ce6d39549a43972a03dd76686bab136f431948706f839b1873acb6`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2519 |
| 2 | success | valid / verified | knowing | factual | Easy | 2515 |
| 3 | success | valid / verified | knowing | factual | Easy | 2532 |

Run 1 — solusi: Fungsi tangen y = tan x memiliki periode dasar π. Hal ini didasarkan pada identitas tan(x + π) = tan x, yang menunjukkan bahwa grafik berulang setiap interval π radian.
- Domain kognitif `classify/knowing`: Soal ini hanya menuntut siswa untuk mengingat atau mengenali fakta dasar mengenai periode fungsi trigonometri tangen. Tidak ada proses perhitungan atau analisis mendalam yang diperlukan.. Bukti: Periode grafik fungsi y = tan x adalah ….
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual mengenai sifat dasar fungsi trigonometri, yaitu periode fungsi tangen.. Bukti: Periode grafik fungsi y = tan x adalah ….
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan merupakan pengetahuan prasyarat atau dasar dalam topik fungsi trigonometri. Siswa hanya perlu mengetahui fakta tersebut tanpa perlu melakukan langkah penyelesaian yang kompleks.. Bukti: Periode grafik fungsi y = tan x adalah ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang fungsi trigonometri dan grafik fungsi tangen. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah pertanyaan recall dasar yang sangat umum diajarkan di awal materi fungsi trigonometri kelas 11. |

Run 2 — solusi: Fungsi tangen y = tan x memiliki periode dasar π karena tan(x + π) = tan x. Grafik fungsi tangen berulang setiap interval π radian.
- Domain kognitif `classify/knowing`: Soal ini hanya menuntut siswa untuk mengingat atau mengenali fakta dasar mengenai sifat periodisitas fungsi trigonometri tangen.. Bukti: Periode grafik fungsi y = tan x adalah ….
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual tentang properti dasar fungsi trigonometri.. Bukti: Periode grafik fungsi y = tan x adalah ….
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan merupakan pengetahuan standar dalam topik fungsi trigonometri kelas 11. Tidak ada langkah perhitungan atau analisis yang diperlukan.. Bukti: Periode grafik fungsi y = tan x adalah ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang fungsi trigonometri. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 Matematika Tingkat Lanjut diharapkan sudah menguasai properti dasar fungsi trigonometri sebagai prasyarat materi yang lebih kompleks. |

Run 3 — solusi: Fungsi tangen y = tan x memiliki periode dasar π. Hal ini dapat ditunjukkan dari identitas tan(x + π) = tan x, yang berarti grafik berulang setiap interval π.
- Domain kognitif `classify/knowing`: Soal ini hanya menuntut siswa untuk mengingat atau mengenali fakta dasar mengenai sifat periodisitas fungsi trigonometri tangen.. Bukti: Periode grafik fungsi y = tan x adalah ….
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual tentang properti dasar fungsi trigonometri.. Bukti: Periode grafik fungsi y = tan x adalah ….
- Intended difficulty `classify/Easy`: Soal ini sangat langsung dan tidak memerlukan langkah perhitungan atau analisis mendalam. Siswa hanya perlu mengetahui definisi periode fungsi tangen.. Bukti: Periode grafik fungsi y = tan x adalah ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengetahuan dasar tentang fungsi trigonometri. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah pertanyaan dasar yang diharapkan dikuasai siswa kelas 11 saat mempelajari grafik fungsi trigonometri. |

Histori retry: run 3 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

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
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Grafik Fungsi Trigonometri
Tipe soal: multiple_choice
Stimulus: -
Soal: Periode grafik fungsi y = tan x adalah ….
Pilihan: A. $2\pi$
B. $4\pi$
C. $\pi$
D. $\dfrac{\pi}{2}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "factual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 27. Soal `333a2cf9330fb76e649f0044`

$\sec^2 t - \tan^2 t = \ldots$

| Opsi | Isi |
|---|---|
| A | $\sin^2 t$ |
| B | $1$ |
| C | $0$ |
| D | $-1$ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Menggunakan identitas dasar trigonometri: 1 + tan² t = sec² t. Maka, sec² t - tan² t = 1.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `05f8bd75fc612c14e7c11b0bd6b126116be47083e1a408825e4a405634833a78`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2593 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2574 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2589 |

Run 1 — solusi: Menggunakan identitas dasar trigonometri: 1 + tan² t = sec² t. Maka, sec² t - tan² t = 1.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengenali dan menerapkan identitas trigonometri dasar secara langsung tanpa memerlukan manipulasi aljabar yang kompleks atau strategi pemecahan masalah yang panjang.. Bukti: \sec^2 t - \tan^2 t = \ldots
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap hubungan dasar antara fungsi trigonometri (identitas Pythagoras), yang merupakan bagian dari pengetahuan konseptual dalam trigonometri.. Bukti: \sec^2 t - \tan^2 t = \ldots
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mengingat atau menurunkan identitas dasar dari sin²t + cos²t = 1. Tidak ada langkah perantara yang kompleks atau kendala yang berinteraksi.. Bukti: \sec^2 t - \tan^2 t = \ldots

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar identitas trigonometri (sin²t + cos²t = 1) |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 11, identitas ini adalah materi dasar yang sudah diperkenalkan dan sering digunakan dalam penyederhanaan ekspresi trigonometri. |

Run 2 — solusi: Menggunakan identitas dasar trigonometri 1 + tan² t = sec² t, maka sec² t - tan² t = 1.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengenali dan menerapkan identitas trigonometri dasar secara langsung tanpa perlu manipulasi atau strategi kompleks.. Bukti: sec^2 t - tan^2 t = ...
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara fungsi trigonometri (secan dan tangen) yang dinyatakan dalam identitas Pythagoras.. Bukti: sec^2 t - tan^2 t = ...
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari identitas dasar yang dipelajari di kelas 11. Tidak ada langkah perantara atau integrasi konsep yang diperlukan.. Bukti: sec^2 t - tan^2 t = ...

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar identitas trigonometri (1 + tan² t = sec² t). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Identitas ini adalah materi fundamental dalam trigonometri kelas 11. Siswa diharapkan langsung mengenali bentuk ini sebagai identitas dasar. |

Run 3 — solusi: Menggunakan identitas dasar trigonometri: 1 + tan² t = sec² t. Dengan mengurangkan kedua ruas dengan tan² t, diperoleh sec² t - tan² t = 1.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengenali dan menerapkan identitas trigonometri dasar secara langsung tanpa memerlukan manipulasi aljabar yang kompleks atau strategi pemecahan masalah yang panjang.. Bukti: \sec^2 t - \tan^2 t = \ldots
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap identitas trigonometri fundamental yang merupakan bagian dari pengetahuan konseptual dalam matematika.. Bukti: \sec^2 t - \tan^2 t = \ldots
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (straightforward) dengan jalur penyelesaian yang sangat jelas dan hanya memerlukan ingatan atau pemahaman dasar mengenai identitas trigonometri.. Bukti: \sec^2 t - \tan^2 t = \ldots

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar identitas trigonometri (sin²t + cos²t = 1 dan turunannya). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 11, identitas ini adalah materi dasar yang sudah diperkenalkan dan sering digunakan dalam penyelesaian masalah trigonometri yang lebih kompleks. |

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
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Identitas Trigonometri
Tipe soal: multiple_choice
Stimulus: -
Soal: $\sec^2 t - \tan^2 t = \ldots$
Pilihan: A. $\sin^2 t$
B. $1$
C. $0$
D. $-1$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 28. Soal `0d276f4b985246c2f7160055`

Menemukan Kesalahan. Abel menyelidiki apakah $\sin t = \sin(-t)$ merupakan identitas. Dia melakukan langkah-langkah berikut ini. $\sin t = \sin(-t)$ (persamaan yang diberikan); $(\sin t)^2 = [\sin(-t)]^2$ (kuadratkan kedua ruas); $\sin^2 t = (-\sin t)^2$ (sederhanakan, karena sin(-t) = -sin t); $\sin^2 t = \sin^2 t$ (sederhanakan). Pada langkah terakhir, Abel mendapatkan bentuk di ruas kiri sama dengan bentuk di ruas kanan. Dengan demikian, dia menyimpulkan bahwa sin t = sin (–t) merupakan identitas.<br><br>Apa yang dilakukan Abel tersebut tidak tepat. Temukan kesalahannya!

| Opsi | Isi |
|---|---|
| A | Kesalahan Abel terletak saat menyederhanakan sin²t = (–sin t)² menjadi sin²t = sin²t; seharusnya hasil penyederhanaan itu adalah –sin²t. |
| B | Abel salah menuliskan sin(–t) sebagai –sin t di langkah ketiga; seharusnya sin(–t) = sin t berlaku untuk semua nilai t yang diberikan. |
| C | Abel sebenarnya tidak melakukan kesalahan apa pun, karena sin t = sin(–t) memang merupakan identitas yang berlaku untuk semua nilai t. |
| D | Abel keliru mengasumsikan sin t = sin(–t) sudah benar sejak awal (padahal itu yang ingin dibuktikan), dan mengkuadratkan kedua ruas tidak selalu menghasilkan persamaan yang ekuivalen. |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Langkah Abel mengkuadratkan kedua ruas persamaan $\sin t = \sin(-t)$ menghasilkan $\sin^2 t = \sin^2 t$. Pernyataan terakhir ini benar untuk semua $t$, namun tidak membuktikan pernyataan awal karena operasi pengkuadratan tidak ekuivalen (dapat mengubah pernyataan salah menjadi benar, misal $1 = -1$ menjadi $1^2 = (-1)^2$). Abel melakukan kesalahan logika dengan mengasumsikan kebenaran pernyataan awal dan menggunakan operasi yang tidak menjaga ekuivalensi.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `aec82b01e787aacc2081d9933ca51319c352c82e22bb460965fe897822b2a251`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Hard | 3099 |
| 2 | success | valid / verified | reasoning | conceptual | Hard | 3124 |
| 3 | success | valid / verified | reasoning | conceptual | Hard | 3695 |

Run 1 — solusi: Langkah Abel mengkuadratkan kedua ruas persamaan $\sin t = \sin(-t)$ menghasilkan $\sin^2 t = \sin^2 t$. Pernyataan terakhir ini benar untuk semua $t$, namun tidak membuktikan pernyataan awal karena operasi pengkuadratan tidak ekuivalen (dapat mengubah pernyataan salah menjadi benar, misal $1 = -1$ menjadi $1^2 = (-1)^2$). Abel melakukan kesalahan logika dengan mengasumsikan kebenaran pernyataan awal dan menggunakan operasi yang tidak menjaga ekuivalensi.
- Domain kognitif `classify/reasoning`: Soal menuntut siswa untuk mengevaluasi validitas argumen logis dan memahami sifat operasi matematika (pengkuadratan) dalam konteks pembuktian identitas, bukan sekadar menghitung nilai.. Bukti: Abel menyelidiki apakah sin t = sin(-t) merupakan identitas; mengkuadratkan kedua ruas bisa menghasilkan pernyataan yang tidak ekuivalen dengan pernyataan awal
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip dasar pembuktian identitas dan batasan operasi aljabar (pengkuadratan) yang tidak selalu ekuivalen, yang merupakan pemahaman konseptual tentang logika matematika.. Bukti: Abel menyelidiki apakah sin t = sin(-t) merupakan identitas; mengkuadratkan kedua ruas bisa menghasilkan pernyataan yang tidak ekuivalen
- Intended difficulty `classify/Hard`: Soal ini menuntut pemahaman konseptual tentang logika pembuktian. Siswa harus mengenali bahwa manipulasi aljabar yang benar secara teknis (kuadrat) tidak menjamin validitas pembuktian jika langkah tersebut tidak ekuivalen. Ini memerlukan perencanaan dan evaluasi strategi, bukan sekadar prosedur rutin.. Bukti: Apa yang dilakukan Abel tersebut tidak tepat. Temukan kesalahannya!; mengkuadratkan kedua ruas bisa menghasilkan pernyataan yang tidak ekuivalen

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang identitas trigonometri, fungsi ganjil/genap, dan prinsip ekuivalensi dalam persamaan. |
| dependentSteps | 3 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun operasi trigonometrinya dasar, kemampuan untuk mengkritisi logika pembuktian dan memahami konsep ekuivalensi persamaan adalah tuntutan tinggi bagi siswa kelas 11. |

Run 2 — solusi: Abel melakukan kesalahan logika dengan mengkuadratkan kedua ruas persamaan yang belum tentu benar. Operasi kuadrat (x^2 = y^2) tidak ekuivalen dengan (x = y) karena dapat mengubah pernyataan salah (seperti 1 = -1) menjadi benar (1^2 = (-1)^2). Identitas sin t = sin(-t) hanya berlaku untuk t = k*pi, bukan untuk semua t, sehingga langkah Abel tidak membuktikan identitas.
- Domain kognitif `classify/reasoning`: Soal meminta siswa mengevaluasi validitas argumen logis dalam pembuktian identitas trigonometri, bukan sekadar menghitung. Siswa harus memahami konsep ekuivalensi logis dalam manipulasi aljabar dan sifat fungsi trigonometri.. Bukti: Abel menyelidiki apakah sin t = sin(-t) merupakan identitas; mengkuadratkan kedua ruas tidak selalu menghasilkan persamaan yang ekuivalen
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang apa yang mendefinisikan sebuah identitas dan batasan manipulasi aljabar (ekuivalensi) dalam pembuktian matematika.. Bukti: Abel menyelidiki apakah sin t = sin(-t) merupakan identitas; mengkuadratkan kedua ruas tidak selalu menghasilkan persamaan yang ekuivalen
- Intended difficulty `classify/Hard`: Soal ini menuntut pemahaman mendalam tentang logika pembuktian. Siswa sering terjebak dalam manipulasi aljabar tanpa memeriksa ekuivalensi logis. Menyadari bahwa operasi kuadrat dapat menghasilkan 'false positive' memerlukan integrasi konsep fungsi dan logika yang melampaui prosedur rutin.. Bukti: Abel menyelidiki apakah sin t = sin(-t) merupakan identitas; mengkuadratkan kedua ruas tidak selalu menghasilkan persamaan yang ekuivalen

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang fungsi ganjil/genap dan definisi identitas trigonometri. |
| dependentSteps | 3 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 sering menganggap manipulasi aljabar (seperti mengkuadratkan) selalu valid. Soal ini menantang miskonsepsi tersebut dengan menuntut analisis kritis terhadap langkah pembuktian, yang merupakan tuntutan kognitif tinggi. |

Run 3 — solusi: Abel's error is the assumption that squaring both sides preserves logical equivalence. While A=B implies A^2=B^2, the converse is not true. Squaring can transform a false statement (like sin t = -sin t) into a true one (sin^2 t = sin^2 t), thus failing to prove the original identity.
- Domain kognitif `classify/reasoning`: Soal menuntut siswa untuk mengevaluasi validitas argumen logis dalam pembuktian identitas trigonometri, bukan sekadar menghitung atau menerapkan rumus secara langsung. Siswa harus memahami konsep ekuivalensi logis.. Bukti: Abel menyelidiki apakah sin t = sin(-t) merupakan identitas; Apa yang dilakukan Abel tersebut tidak tepat. Temukan kesalahannya!
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang sifat-sifat fungsi trigonometri dan prinsip dasar logika dalam pembuktian matematika (ekuivalensi pernyataan).. Bukti: Abel menyelidiki apakah sin t = sin(-t) merupakan identitas; mengkuadratkan kedua ruas tidak selalu menghasilkan persamaan yang ekuivalen
- Intended difficulty `classify/Hard`: Soal ini menuntut kemampuan metakognitif dan pemahaman konseptual yang mendalam tentang logika pembuktian. Siswa tidak bisa hanya mengandalkan prosedur rutin, melainkan harus menganalisis kesalahan logika pada langkah-langkah yang diberikan.. Bukti: Abel menyelidiki apakah sin t = sin(-t) merupakan identitas; mengkuadratkan kedua ruas tidak selalu menghasilkan persamaan yang ekuivalen

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat fungsi ganjil/genap trigonometri, pemahaman tentang ekuivalensi logis dalam pembuktian. |
| dependentSteps | 3 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Memahami mengapa langkah aljabar yang benar (kuadrat) dapat menghasilkan kesimpulan yang salah dalam konteks pembuktian identitas adalah tantangan konseptual yang signifikan bagi siswa kelas 11. |

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
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Identitas Trigonometri
Tipe soal: multiple_choice
Stimulus: -
Soal: Menemukan Kesalahan. Abel menyelidiki apakah $\sin t = \sin(-t)$ merupakan identitas. Dia melakukan langkah-langkah berikut ini. $\sin t = \sin(-t)$ (persamaan yang diberikan); $(\sin t)^2 = [\sin(-t)]^2$ (kuadratkan kedua ruas); $\sin^2 t = (-\sin t)^2$ (sederhanakan, karena sin(-t) = -sin t); $\sin^2 t = \sin^2 t$ (sederhanakan). Pada langkah terakhir, Abel mendapatkan bentuk di ruas kiri sama dengan bentuk di ruas kanan. Dengan demikian, dia menyimpulkan bahwa sin t = sin (–t) merupakan identitas.

Apa yang dilakukan Abel tersebut tidak tepat. Temukan kesalahannya!
Pilihan: A. Kesalahan Abel terletak saat menyederhanakan sin²t = (–sin t)² menjadi sin²t = sin²t; seharusnya hasil penyederhanaan itu adalah –sin²t.
B. Abel salah menuliskan sin(–t) sebagai –sin t di langkah ketiga; seharusnya sin(–t) = sin t berlaku untuk semua nilai t yang diberikan.
C. Abel sebenarnya tidak melakukan kesalahan apa pun, karena sin t = sin(–t) memang merupakan identitas yang berlaku untuk semua nilai t.
D. Abel keliru mengasumsikan sin t = sin(–t) sudah benar sejak awal (padahal itu yang ingin dibuktikan), dan mengkuadratkan kedua ruas tidak selalu menghasilkan persamaan yang ekuivalen.
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Hard"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "reasoning", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Hard", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 29. Soal `ba91e1dbbd3c3d155050439f`

Jika ∠A = 30°, ∠B = 45°, dan a = 15, tentukan panjang b.

| Opsi | Isi |
|---|---|
| A | $b = 7{,}5\sqrt{2} \approx 10{,}61$ |
| B | $b = 22{,}5$ |
| C | $b = 15\sqrt{2} \approx 21{,}21$ |
| D | $b = 5\sqrt{6} \approx 12{,}25$ |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Menggunakan aturan sinus: b/sin(B) = a/sin(A). Maka b = a * sin(B) / sin(A) = 15 * sin(45°) / sin(30°) = 15 * (1/2 * sqrt(2)) / (1/2) = 15 * sqrt(2).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ad6267e23994dc5111c34a913b074b8e9bb91ae9fbf9697e8513a6ba921f791b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2747 |
| 2 | success | valid / verified | applying | procedural | Easy | 2739 |
| 3 | success | valid / verified | applying | procedural | Easy | 2757 |

Run 1 — solusi: Menggunakan aturan sinus: b/sin(B) = a/sin(A). Maka b = a * sin(B) / sin(A) = 15 * sin(45°) / sin(30°) = 15 * (1/2 * sqrt(2)) / (1/2) = 15 * sqrt(2).
- Domain kognitif `classify/applying`: Soal meminta penerapan langsung rumus aturan sinus untuk mencari panjang sisi segitiga. Siswa hanya perlu mengidentifikasi pasangan sisi dan sudut yang bersesuaian, lalu melakukan substitusi dan perhitungan sederhana.. Bukti: Jika ∠A = 30°, ∠B = 45°, dan a = 15, tentukan panjang b.
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman dan penerapan prosedur algoritma aturan sinus yang merupakan konsep standar dalam trigonometri.. Bukti: aturan sinus
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang sangat jelas. Tidak ada kendala yang berinteraksi atau kebutuhan untuk perencanaan strategi yang kompleks. Siswa hanya perlu menerapkan rumus aturan sinus secara langsung.. Bukti: Jika ∠A = 30°, ∠B = 45°, dan a = 15, tentukan panjang b.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang aturan sinus dan nilai trigonometri sudut istimewa. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 11, penerapan aturan sinus dengan data langsung adalah tugas dasar yang familiar dan tidak memerlukan penalaran tingkat tinggi. |

Run 2 — solusi: Menggunakan aturan sinus: b/sin B = a/sin A. Maka b = a * (sin B / sin A) = 15 * (sin 45° / sin 30°) = 15 * ((1/2 * sqrt(2)) / (1/2)) = 15 * sqrt(2).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur aturan sinus secara langsung untuk mencari panjang sisi segitiga. Tidak ada langkah non-rutin atau integrasi konsep yang kompleks.. Bukti: Jika ∠A = 30°, ∠B = 45°, dan a = 15, tentukan panjang b.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan rumus aturan sinus dalam trigonometri.. Bukti: Jika ∠A = 30°, ∠B = 45°, dan a = 15, tentukan panjang b.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang jelas (langsung menggunakan rumus aturan sinus). Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Jika ∠A = 30°, ∠B = 45°, dan a = 15, tentukan panjang b.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang nilai sinus sudut istimewa dan aturan sinus. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, penerapan aturan sinus dengan data langsung merupakan prosedur standar yang familiar dan tidak memerlukan perencanaan tinggi. |

Run 3 — solusi: Menggunakan aturan sinus: b/sin(B) = a/sin(A). Maka b = a * sin(B) / sin(A) = 15 * sin(45°) / sin(30°) = 15 * (1/2 * sqrt(2)) / (1/2) = 15 * sqrt(2).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus aturan sinus secara langsung untuk mencari panjang sisi yang belum diketahui. Ini adalah penerapan prosedur standar yang sudah dipelajari.. Bukti: Jika ∠A = 30°, ∠B = 45°, dan a = 15, tentukan panjang b.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman dan penerapan algoritma aturan sinus, yang merupakan bagian dari pengetahuan prosedural dalam trigonometri.. Bukti: aturan sinus
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang sangat jelas. Siswa hanya perlu mensubstitusi nilai ke dalam rumus aturan sinus yang sudah dikenal. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: Jika ∠A = 30°, ∠B = 45°, dan a = 15, tentukan panjang b.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang aturan sinus dan nilai trigonometri sudut istimewa. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, penerapan langsung aturan sinus dengan sudut istimewa adalah tugas yang sangat mendasar dan rutin. |

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
Subtopik: Aturan Sinus
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika ∠A = 30°, ∠B = 45°, dan a = 15, tentukan panjang b.
Pilihan: A. $b = 7{,}5\sqrt{2} \approx 10{,}61$
B. $b = 22{,}5$
C. $b = 15\sqrt{2} \approx 21{,}21$
D. $b = 5\sqrt{6} \approx 12{,}25$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 30. Soal `5364425a70eacc615935825f`

Jika ∠C = 145°, b = 10, dan c = 6, tentukan besar sudut B.

| Opsi | Isi |
|---|---|
| A | $\angle B \approx 34{,}62°$ |
| B | $\angle B \approx 4{,}78°$ |
| C | $\angle B \approx 17{,}31°$ |
| D | $\angle B \approx 72{,}93°$ |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Menggunakan aturan sinus: sin B / b = sin C / c. Maka sin B = (b * sin C) / c = (10 * sin 145°) / 6. sin B ≈ (10 * 0,57357) / 6 ≈ 0,95596. B = arcsin(0,95596) ≈ 72,93°.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f8842831400cf029284dd6a783ff3de13fa2afa902649762ecda95618fb8f812`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2800 |
| 2 | success | valid / verified | applying | procedural | Easy | 2774 |
| 3 | success | valid / verified | applying | procedural | Easy | 2743 |

Run 1 — solusi: Menggunakan aturan sinus: sin B / b = sin C / c. Maka sin B = (b * sin C) / c = (10 * sin 145°) / 6. sin B ≈ (10 * 0,57357) / 6 ≈ 0,95596. B = arcsin(0,95596) ≈ 72,93°.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus aturan sinus secara langsung untuk mencari nilai sudut yang belum diketahui. Prosedur ini merupakan penerapan standar dari konsep trigonometri yang sudah dipelajari.. Bukti: Jika ∠C = 145°, b = 10, dan c = 6, tentukan besar sudut B.
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penggunaan algoritma atau metode aturan sinus untuk menyelesaikan masalah trigonometri segitiga.. Bukti: Jika ∠C = 145°, b = 10, dan c = 6, tentukan besar sudut B.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang jelas. Siswa hanya perlu mensubstitusi nilai ke dalam rumus aturan sinus dan menghitung invers sinus. Tidak ada kendala kompleks atau integrasi konsep yang berat.. Bukti: Jika ∠C = 145°, b = 10, dan c = 6, tentukan besar sudut B.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar aturan sinus dan penggunaan kalkulator untuk fungsi trigonometri invers. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi aturan sinus adalah standar kelas 11. Soal ini tidak memerlukan analisis kasus ambigu (karena sudut C tumpul, maka B harus lancip dan sin B < 1 sudah terpenuhi) atau langkah penalaran tambahan. |

Run 2 — solusi: Menggunakan aturan sinus: sin B / b = sin C / c. Maka sin B = (b * sin C) / c = (10 * sin 145°) / 6 ≈ (10 * 0,57357) / 6 ≈ 0,95596. Maka B = arcsin(0,95596) ≈ 72,93°.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan aturan sinus secara langsung untuk mencari sudut yang belum diketahui dengan data yang sudah diberikan. Prosedur ini merupakan penerapan standar dari rumus aturan sinus.. Bukti: Jika ∠C = 145°, b = 10, dan c = 6, tentukan besar sudut B.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami hubungan trigonometri dalam segitiga (aturan sinus) dan menerapkannya sebagai algoritma untuk menyelesaikan masalah.. Bukti: Jika ∠C = 145°, b = 10, dan c = 6, tentukan besar sudut B.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu memasukkan nilai ke dalam rumus aturan sinus yang sudah dikenal. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: Jika ∠C = 145°, b = 10, dan c = 6, tentukan besar sudut B.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar aturan sinus dan penggunaan kalkulator untuk fungsi invers trigonometri. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, penerapan langsung aturan sinus dengan data yang sudah lengkap merupakan tugas yang sangat mendasar dan rutin. |

Run 3 — solusi: Menggunakan aturan sinus: sin B / b = sin C / c. Maka sin B = (b * sin C) / c = (10 * sin 145°) / 6 ≈ (10 * 0,57357) / 6 ≈ 0,95596. Maka B = arcsin(0,95596) ≈ 72,93°.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan aturan sinus secara langsung untuk mencari sudut yang belum diketahui dengan data yang sudah diberikan. Ini adalah penerapan prosedur standar.. Bukti: Jika ∠C = 145°, b = 10, dan c = 6, tentukan besar sudut B.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami dan menerapkan algoritma aturan sinus untuk menyelesaikan masalah trigonometri.. Bukti: aturan sinus
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu mensubstitusi nilai ke dalam rumus aturan sinus dan menghitung nilai arcsin. Tidak ada kendala kompleks atau langkah perencanaan yang rumit.. Bukti: Jika ∠C = 145°, b = 10, dan c = 6, tentukan besar sudut B.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar trigonometri dan aturan sinus. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi aturan sinus adalah standar kelas 11. Soal ini tidak memerlukan manipulasi aljabar yang rumit atau pemahaman konsep mendalam, cukup substitusi langsung. |

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
Subtopik: Aturan Sinus
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika ∠C = 145°, b = 10, dan c = 6, tentukan besar sudut B.
Pilihan: A. $\angle B \approx 34{,}62°$
B. $\angle B \approx 4{,}78°$
C. $\angle B \approx 17{,}31°$
D. $\angle B \approx 72{,}93°$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 31. Soal `4efc96ae8cc1e04d35b2d9ce`

Jika ∠C = 60°, a = 6, dan b = 10, panjang c adalah ….

| Opsi | Isi |
|---|---|
| A | $c = \sqrt{106} \approx 10{,}30$ |
| B | $c = \sqrt{136} \approx 11{,}66$ |
| C | $c = 2\sqrt{19} \approx 8{,}72$ |
| D | $c = 14$ |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: c² = a² + b² - 2ab cos C = 6² + 10² - 2(6)(10) cos 60° = 36 + 100 - 120(0,5) = 136 - 60 = 76. Maka c = √76 = √(4 × 19) = 2√19.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4790a66c408dfff862c2aefee837a01454da7268e918108a6d9bbebadf69ddd8`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2814 |
| 2 | success | valid / verified | applying | procedural | Easy | 2805 |
| 3 | success | valid / verified | applying | procedural | Easy | 2819 |

Run 1 — solusi: c² = a² + b² - 2ab cos C = 6² + 10² - 2(6)(10) cos 60° = 36 + 100 - 120(0,5) = 136 - 60 = 76. Maka c = √76 = √(4 × 19) = 2√19.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus aturan kosinus secara langsung untuk mencari panjang sisi segitiga. Prosedur ini merupakan penerapan standar dari rumus yang sudah dipelajari.. Bukti: Jika ∠C = 60°, a = 6, dan b = 10, panjang c adalah ….
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritma atau rumus aturan kosinus (prosedural) dan bagaimana menggunakannya untuk menyelesaikan masalah geometri (konseptual).. Bukti: Jika ∠C = 60°, a = 6, dan b = 10, panjang c adalah ….
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang sangat jelas. Siswa hanya perlu mensubstitusi nilai ke dalam rumus aturan kosinus yang sudah dikenal. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Jika ∠C = 60°, a = 6, dan b = 10, panjang c adalah ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar aturan kosinus dan nilai trigonometri sudut istimewa. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, penggunaan aturan kosinus dengan data langsung adalah tugas rutin yang mendasar. |

Run 2 — solusi: c² = a² + b² - 2ab cos C = 6² + 10² - 2(6)(10) cos 60° = 36 + 100 - 120(0,5) = 136 - 60 = 76. Maka c = √76 = √(4 × 19) = 2√19.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus aturan kosinus secara langsung untuk mencari panjang sisi segitiga. Prosedur ini merupakan penerapan standar dari rumus yang sudah dipelajari.. Bukti: Jika ∠C = 60°, a = 6, dan b = 10, panjang c adalah ….
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritma atau prosedur aturan kosinus untuk menyelesaikan masalah geometri.. Bukti: Jika ∠C = 60°, a = 6, dan b = 10, panjang c adalah ….
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang sangat jelas. Siswa hanya perlu mensubstitusi nilai ke dalam rumus aturan kosinus yang sudah dikenal. Tidak ada kendala yang berinteraksi atau kebutuhan untuk perencanaan strategi yang kompleks.. Bukti: Jika ∠C = 60°, a = 6, dan b = 10, panjang c adalah ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar aturan kosinus dan nilai trigonometri sudut istimewa. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 11, penerapan langsung aturan kosinus pada segitiga dengan sudut istimewa adalah tugas rutin yang mendasar. |

Run 3 — solusi: c² = a² + b² - 2ab cos C = 6² + 10² - 2(6)(10) cos 60° = 36 + 100 - 120(0,5) = 136 - 60 = 76. Maka c = √76 = √(4 × 19) = 2√19.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus aturan kosinus secara langsung dengan nilai yang sudah diberikan. Ini adalah penerapan prosedur standar yang familiar bagi siswa kelas 11.. Bukti: Jika ∠C = 60°, a = 6, dan b = 10, panjang c adalah ….
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman dan penggunaan algoritma aturan kosinus (prosedural) untuk menyelesaikan masalah geometri segitiga.. Bukti: Jika ∠C = 60°, a = 6, dan b = 10, panjang c adalah ….
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang sangat jelas. Siswa hanya perlu mensubstitusi nilai ke dalam rumus aturan kosinus dan melakukan operasi aritmatika dasar. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Jika ∠C = 60°, a = 6, dan b = 10, panjang c adalah ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar trigonometri dan aturan kosinus. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan langsung rumus yang dipelajari di kelas 11, dengan beban kognitif yang rendah karena tidak memerlukan manipulasi aljabar atau penalaran geometris yang kompleks. |

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
Subtopik: Aturan Kosinus
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika ∠C = 60°, a = 6, dan b = 10, panjang c adalah ….
Pilihan: A. $c = \sqrt{106} \approx 10{,}30$
B. $c = \sqrt{136} \approx 11{,}66$
C. $c = 2\sqrt{19} \approx 8{,}72$
D. $c = 14$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 32. Soal `bb3460948df5551e87c20f19`

Jika a = 12, b = 14, dan c = 8, besar sudut B adalah ….

| Opsi | Isi |
|---|---|
| A | $\angle B \approx 86{,}42°$ |
| B | $\angle B \approx 93{,}58°$ |
| C | $\angle B \approx 34{,}84°$ |
| D | $\angle B \approx 58{,}83°$ |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Menggunakan aturan kosinus: cos B = (a^2 + c^2 - b^2) / (2ac). Substitusi nilai: cos B = (12^2 + 8^2 - 14^2) / (2 * 12 * 8) = (144 + 64 - 196) / 192 = 12 / 192 = 0,0625. Maka, B = arccos(0,0625) ≈ 86,42°.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `dcc0604e8f07a2f000804a3f77b73cb6274dc7dc2a019d1c85575c7c5b5cd874`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2859 |
| 2 | success | valid / verified | applying | procedural | Easy | 2823 |
| 3 | success | valid / verified | applying | procedural | Easy | 2823 |

Run 1 — solusi: Menggunakan aturan kosinus: cos B = (a^2 + c^2 - b^2) / (2ac). Substitusi nilai: cos B = (12^2 + 8^2 - 14^2) / (2 * 12 * 8) = (144 + 64 - 196) / 192 = 12 / 192 = 0,0625. Maka, B = arccos(0,0625) ≈ 86,42°.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus aturan kosinus secara langsung untuk mencari besar sudut. Prosedur ini merupakan penerapan standar dari rumus yang sudah dipelajari di kelas 11.. Bukti: Jika a = 12, b = 14, dan c = 8, besar sudut B adalah
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritma atau prosedur aturan kosinus untuk menyelesaikan masalah trigonometri segitiga.. Bukti: Jika a = 12, b = 14, dan c = 8, besar sudut B adalah
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang jelas dan langsung. Siswa hanya perlu mensubstitusi nilai ke dalam rumus aturan kosinus yang sudah dikenal. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi non-rutin.. Bukti: Jika a = 12, b = 14, dan c = 8, besar sudut B adalah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang aturan kosinus dan penggunaan kalkulator untuk fungsi invers trigonometri. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi aturan kosinus adalah materi standar kelas 11. Soal ini tidak memerlukan manipulasi aljabar yang kompleks atau penalaran geometris yang mendalam, sehingga dikategorikan mudah bagi siswa kelas 11. |

Run 2 — solusi: Menggunakan aturan kosinus: cos B = (a^2 + c^2 - b^2) / (2ac). Substitusi nilai: cos B = (12^2 + 8^2 - 14^2) / (2 * 12 * 8) = (144 + 64 - 196) / 192 = 12 / 192 = 0,0625. Maka B = arccos(0,0625) ≈ 86,42°.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus aturan kosinus secara langsung untuk mencari besar sudut segitiga. Prosedur ini merupakan penerapan standar dari rumus yang sudah dipelajari.. Bukti: Jika a = 12, b = 14, dan c = 8, besar sudut B adalah ….
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritma aturan kosinus untuk menentukan sudut dalam segitiga.. Bukti: Jika a = 12, b = 14, dan c = 8, besar sudut B adalah ….
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang jelas. Siswa hanya perlu mensubstitusi nilai ke dalam rumus aturan kosinus yang sudah umum diketahui di kelas 11.. Bukti: Jika a = 12, b = 14, dan c = 8, besar sudut B adalah ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar aturan kosinus dan penggunaan kalkulator untuk fungsi invers trigonometri. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi aturan kosinus adalah standar kurikulum kelas 11. Soal ini tidak memerlukan manipulasi aljabar kompleks atau penalaran non-rutin. |

Run 3 — solusi: Menggunakan aturan kosinus: cos B = (a^2 + c^2 - b^2) / (2ac). Substitusi nilai: cos B = (12^2 + 8^2 - 14^2) / (2 * 12 * 8) = (144 + 64 - 196) / 192 = 12 / 192 = 0,0625. Maka, B = arccos(0,0625) ≈ 86,42°.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus aturan kosinus secara langsung untuk mencari sudut segitiga yang diketahui ketiga sisinya. Ini adalah penerapan prosedur standar yang sudah dipelajari.. Bukti: Jika a = 12, b = 14, dan c = 8, besar sudut B adalah ….
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman dan penerapan algoritma aturan kosinus untuk menyelesaikan masalah trigonometri segitiga.. Bukti: Jika a = 12, b = 14, dan c = 8, besar sudut B adalah ….
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang sangat jelas. Siswa hanya perlu mensubstitusi nilai ke dalam rumus yang sudah diketahui tanpa perlu melakukan manipulasi aljabar yang kompleks atau perencanaan strategi yang rumit.. Bukti: Jika a = 12, b = 14, dan c = 8, besar sudut B adalah ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar aturan kosinus dan penggunaan kalkulator saintifik untuk fungsi invers trigonometri. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, penerapan aturan kosinus dengan data langsung merupakan tugas dasar yang familiar dan tidak memerlukan penalaran tingkat tinggi. |

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
Subtopik: Aturan Kosinus
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika a = 12, b = 14, dan c = 8, besar sudut B adalah ….
Pilihan: A. $\angle B \approx 86{,}42°$
B. $\angle B \approx 93{,}58°$
C. $\angle B \approx 34{,}84°$
D. $\angle B \approx 58{,}83°$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 33. Soal `899fad8c8260df6013a595be`

Sebuah segitiga siku-siku PQR, mempunyai besaran ∠P = 53,2o dan besaran ∠Q = 36,8o. Q 36,8º 5 4 53,2º P 3 R<br><br>Nilai perbandingan panjang sisi QR dan QP sama dengan nilai ________.

| Opsi | Isi |
|---|---|
| A | tan 53,2° |
| B | cos 53,2° |
| C | tan 36,8° |
| D | cos 36,8° |

![Gambar sumber soal 33](<../../../images/kelas10_panduan_siswa_kelas10.pdf-0110-05.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Berdasarkan gambar, QR adalah sisi samping sudut Q dan QP adalah sisi miring. Maka, rasio QR/QP = 4/5 = 0,8. Dalam trigonometri, cos Q = sisi samping/sisi miring = QR/QP. Jadi, QR/QP = cos 36,8°.
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0110-05.png. Transkripsi visual: Segitiga siku-siku PQR dengan sudut siku-siku di R. Sudut P = 53,2 derajat, sudut Q = 36,8 derajat. Panjang sisi PR = 3, QR = 4, dan sisi miring PQ = 5.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d453700af0aeda44ce704edb7019b2c5343adb43f3b19a90e60f2fa093604a35`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3949 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3911 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 3892 |

Run 1 — solusi: Berdasarkan gambar, QR adalah sisi samping sudut Q dan QP adalah sisi miring. Maka, rasio QR/QP = 4/5 = 0,8. Dalam trigonometri, cos Q = sisi samping/sisi miring = QR/QP. Jadi, QR/QP = cos 36,8°.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengidentifikasi posisi sisi terhadap sudut yang diberikan (samping dan miring) dan menghubungkannya dengan definisi dasar fungsi kosinus.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman definisi dasar perbandingan trigonometri pada segitiga siku-siku.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar. Siswa hanya perlu mengenali rasio trigonometri dasar (cosinus) dari segitiga siku-siku yang sudah diberikan lengkap dengan panjang sisinya.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi perbandingan trigonometri dasar (sinus, cosinus, tangen) pada segitiga siku-siku. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini merupakan prasyarat dasar trigonometri yang sudah dipelajari di jenjang sebelumnya (SMP/kelas 10), sehingga untuk kelas 11 ini dikategorikan sangat mudah. |

Run 2 — solusi: Berdasarkan gambar, QR adalah sisi samping sudut Q (36,8°) dan QP adalah sisi miring (hipotenusa). Rasio QR/QP = sisi samping/sisi miring = cos(Q) = cos(36,8°).
- Domain kognitif `classify/knowing`: Soal meminta siswa mengidentifikasi rasio trigonometri dasar (cosinus) dalam segitiga siku-siku berdasarkan definisi sisi samping dan sisi miring. Ini adalah penerapan langsung dari definisi perbandingan trigonometri.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara sisi-sisi segitiga siku-siku dan fungsi trigonometri (konsep dasar cosinus).. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengidentifikasi sisi samping dan sisi miring terhadap sudut Q yang sudah diberikan nilainya. Tidak ada langkah kompleks atau integrasi konsep yang berat.. Bukti: Sebuah segitiga siku-siku PQR; Nilai perbandingan panjang sisi QR dan QP sama dengan nilai

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi perbandingan trigonometri pada segitiga siku-siku (sin, cos, tan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi trigonometri diajarkan di kelas 10, soal ini sangat mendasar dan rutin bagi siswa kelas 11, sehingga dikategorikan mudah. |

Run 3 — solusi: Dalam segitiga siku-siku PQR, QR adalah sisi samping sudut Q dan QP adalah sisi miring. Maka, perbandingan QR/QP = cos(Q) = cos(36,8°).
- Domain kognitif `classify/knowing`: Soal meminta siswa mengidentifikasi rasio trigonometri dasar (cosinus) berdasarkan posisi sisi terhadap sudut yang diketahui dalam segitiga siku-siku. Ini adalah penerapan langsung dari definisi perbandingan trigonometri.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami definisi konseptual dari fungsi trigonometri (cosinus) sebagai perbandingan sisi samping terhadap sisi miring dalam segitiga siku-siku.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar. Siswa hanya perlu mengidentifikasi sisi samping dan sisi miring terhadap sudut Q yang sudah diberikan nilainya. Tidak ada langkah perencanaan yang kompleks atau integrasi konsep yang menantang.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi perbandingan trigonometri pada segitiga siku-siku. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun untuk kelas 11, soal ini menguji konsep dasar trigonometri yang seharusnya sudah dikuasai sejak kelas 10. Tidak ada tuntutan tingkat lanjut. |

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
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Pemanfaatan Perbandingan Trigonometri
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah segitiga siku-siku PQR, mempunyai besaran ∠P = 53,2o dan besaran ∠Q = 36,8o. Q 36,8º 5 4 53,2º P 3 R

Nilai perbandingan panjang sisi QR dan QP sama dengan nilai ________.
Pilihan: A. tan 53,2°
B. cos 53,2°
C. tan 36,8°
D. cos 36,8°
Transkripsi visual: Segitiga siku-siku PQR dengan sudut siku-siku di R. Sudut P = 53,2 derajat, sudut Q = 36,8 derajat. Panjang sisi PR = 3, QR = 4, dan sisi miring PQ = 5.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 34. Soal `80afd89325ff526ea10e623f`

Sebuah vektor memiliki pangkal di (6, 2) dan ujung di (1, –5). Tentukan bentuk komponen vektor tersebut, kemudian hitung panjangnya.

| Opsi | Isi |
|---|---|
| A | $\langle -5,-7\rangle$, panjang 12 |
| B | $\langle -5,-7\rangle$, panjang $\sqrt{74}$ |
| C | $\langle -7,-5\rangle$, panjang $\sqrt{74}$ |
| D | $\langle 5,7\rangle$, panjang $\sqrt{74}$ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Komponen vektor = (1-6, -5-2) = (-5, -7). Panjang vektor = sqrt((-5)^2 + (-7)^2) = sqrt(25 + 49) = sqrt(74).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi', 'menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0809ef358c031404aaff186063870707dda08c35d9ffdd2dac6d358865d48375`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 3201 |
| 2 | success | valid / verified | applying | procedural | Easy | 3173 |
| 3 | success | valid / verified | knowing | procedural | Easy | 3443 |

Run 1 — solusi: Komponen vektor = (1-6, -5-2) = (-5, -7). Panjang vektor = √((-5)² + (-7)²) = √(25 + 49) = √74.
- Domain kognitif `classify/knowing`: Soal meminta penerapan langsung definisi komponen vektor (ujung dikurangi pangkal) dan rumus panjang vektor (magnitudo). Tidak ada strategi non-rutin atau integrasi konsep yang diperlukan.. Bukti: pangkal di (6, 2) dan ujung di (1, –5); bentuk komponen vektor tersebut, kemudian hitung panjangnya
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menjalankan algoritma standar untuk menentukan komponen vektor dan menghitung panjangnya menggunakan teorema Pythagoras.. Bukti: bentuk komponen vektor tersebut, kemudian hitung panjangnya
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang sangat jelas. Siswa hanya perlu menerapkan rumus dasar vektor tanpa kendala yang saling berinteraksi.. Bukti: pangkal di (6, 2) dan ujung di (1, –5); bentuk komponen vektor tersebut, kemudian hitung panjangnya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep koordinat kartesius dan teorema Pythagoras. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan langsung dari rumus dasar vektor di kelas 11. Langkah-langkahnya bersifat rutin dan tidak memerlukan integrasi konsep yang kompleks. |

Run 2 — solusi: Vektor komponen = (1-6, -5-2) = (-5, -7). Panjang = sqrt((-5)^2 + (-7)^2) = sqrt(25+49) = sqrt(74).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus standar untuk menentukan komponen vektor (ujung dikurangi pangkal) dan rumus panjang vektor (teorema Pythagoras). Ini adalah penerapan prosedur langsung.. Bukti: Tentukan bentuk komponen vektor tersebut, kemudian hitung panjangnya.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji penguasaan algoritma dasar vektor, yaitu prosedur pengurangan koordinat dan perhitungan magnitudo.. Bukti: Tentukan bentuk komponen vektor tersebut, kemudian hitung panjangnya.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang jelas dan langsung. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi non-rutin.. Bukti: Sebuah vektor memiliki pangkal di (6, 2) dan ujung di (1, –5).

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar koordinat kartesius dan teorema Pythagoras. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal dasar vektor untuk kelas 11 yang menguji pemahaman definisi komponen dan panjang vektor tanpa kerumitan tambahan. |

Run 3 — solusi: Komponen vektor = (x2-x1, y2-y1) = (1-6, -5-2) = (-5, -7). Panjang vektor = sqrt((-5)^2 + (-7)^2) = sqrt(25+49) = sqrt(74).
- Domain kognitif `classify/knowing`: Soal meminta penerapan langsung definisi komponen vektor (ujung - pangkal) dan rumus panjang vektor (teorema Pythagoras). Tidak ada strategi non-rutin atau integrasi konsep yang kompleks.. Bukti: Sebuah vektor memiliki pangkal di (6, 2) dan ujung di (1, –5). Tentukan bentuk komponen vektor tersebut, kemudian hitung panjangnya.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menjalankan algoritma standar untuk mencari komponen vektor dan menghitung panjangnya menggunakan rumus yang sudah dipelajari.. Bukti: Tentukan bentuk komponen vektor tersebut, kemudian hitung panjangnya.
- Intended difficulty `classify/Easy`: Soal ini adalah penerapan langsung dari definisi dasar vektor. Jalur penyelesaian sangat jelas, tidak ada kendala yang berinteraksi, dan hanya melibatkan dua langkah prosedural standar.. Bukti: Sebuah vektor memiliki pangkal di (6, 2) dan ujung di (1, –5). Tentukan bentuk komponen vektor tersebut, kemudian hitung panjangnya.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar koordinat kartesius dan teorema Pythagoras. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan latihan dasar vektor di kelas 11 yang tidak memerlukan penalaran tingkat tinggi atau integrasi konsep yang kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4100`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta penerapan langsung dari definisi komponen vektor (ujung dikurangi pangkal) dan rumus panjang vektor (magnitudo). Tidak ada strategi non-rutin atau integrasi konsep yang diperlukan.
- Dimensi pengetahuan `procedural`: Siswa perlu menjalankan algoritma standar untuk menentukan komponen vektor dan menghitung panjangnya menggunakan teorema Pythagoras.
- Intended difficulty `Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang sangat jelas. Siswa hanya perlu menerapkan rumus dasar vektor tanpa kendala yang saling berinteraksi.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep koordinat kartesius dan teorema Pythagoras. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan langsung dari rumus dasar vektor di kelas 11. Langkah-langkahnya bersifat rutin dan tidak memerlukan integrasi konsep yang kompleks. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Vektor pada Bidang
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah vektor memiliki pangkal di (6, 2) dan ujung di (1, –5). Tentukan bentuk komponen vektor tersebut, kemudian hitung panjangnya.
Pilihan: A. $\langle -5,-7\rangle$, panjang 12
B. $\langle -5,-7\rangle$, panjang $\sqrt{74}$
C. $\langle -7,-5\rangle$, panjang $\sqrt{74}$
D. $\langle 5,7\rangle$, panjang $\sqrt{74}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 35. Soal `70dbfec033da3e0b6a3374fa`

Vektor $\langle -4,12 \rangle$ dapat dituliskan ke dalam kombinasi vektor-vektor satuan baku $\mathbf{i}$ dan $\mathbf{j}$, yaitu ….

| Opsi | Isi |
|---|---|
| A | $-4\mathbf{i} - 12\mathbf{j}$ |
| B | $-4\mathbf{i} + 12\mathbf{j}$ |
| C | $4\mathbf{i} + 12\mathbf{j}$ |
| D | $12\mathbf{i} - 4\mathbf{j}$ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Vektor <a, b> dapat dinyatakan sebagai kombinasi linear vektor satuan baku i dan j menjadi ai + bj. Untuk vektor <-4, 12>, substitusi a = -4 dan b = 12 menghasilkan -4i + 12j.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a5f1c9007a9d312e0dc6d1b056050a0aa0321d17a1d3e8c076a6a98c5cf7da40`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2658 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2765 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2730 |

Run 1 — solusi: Vektor satuan baku i = <1, 0> dan j = <0, 1>. Vektor <x, y> dapat ditulis sebagai xi + yj. Maka, < -4, 12 > = -4i + 12j.
- Domain kognitif `classify/knowing`: Soal ini hanya meminta siswa untuk mengenali definisi dasar representasi vektor dalam bentuk kombinasi linear vektor satuan baku (i dan j). Tidak ada langkah kompleks atau integrasi konsep yang diperlukan.. Bukti: Vektor < -4, 12 > dapat dituliskan ke dalam kombinasi vektor-vektor satuan baku i dan j
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang notasi dan definisi dasar vektor, yang merupakan pengetahuan faktual/konseptual dasar dalam topik vektor.. Bukti: kombinasi vektor-vektor satuan baku i dan j
- Intended difficulty `classify/Easy`: Soal ini sangat langsung dan hanya memerlukan pemahaman definisi dasar. Tidak ada langkah yang saling bergantung atau kendala yang harus diintegrasikan.. Bukti: Vektor < -4, 12 > dapat dituliskan ke dalam kombinasi vektor-vektor satuan baku i dan j

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi vektor satuan baku i dan j. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL seharusnya sudah sangat familiar dengan notasi vektor ini sejak awal pembelajaran vektor. |

Run 2 — solusi: Vektor $\langle a, b \rangle$ dinyatakan sebagai kombinasi linear vektor satuan baku $\mathbf{i}$ dan $\mathbf{j}$ adalah $a\mathbf{i} + b\mathbf{j}$. Untuk vektor $\langle -4, 12 \rangle$, maka $a = -4$ dan $b = 12$, sehingga bentuknya adalah $-4\mathbf{i} + 12\mathbf{j}$.
- Domain kognitif `classify/knowing`: Soal ini hanya meminta siswa untuk mengenali definisi dasar representasi vektor dalam bentuk kombinasi linear vektor satuan baku $\mathbf{i}$ dan $\mathbf{j}$. Tidak ada proses analisis atau sintesis yang kompleks.. Bukti: Vektor $\langle -4,12 \rangle$ dapat dituliskan ke dalam kombinasi vektor-vektor satuan baku $\mathbf{i}$ dan $\mathbf{j}$
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami definisi atau konsep dasar mengenai bagaimana vektor kolom $\langle a, b \rangle$ dikonversi menjadi bentuk $a\mathbf{i} + b\mathbf{j}$.. Bukti: kombinasi vektor-vektor satuan baku $\mathbf{i}$ dan $\mathbf{j}$
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan merupakan penerapan langsung dari definisi vektor satuan baku. Tidak ada langkah perencanaan, integrasi kendala, atau strategi nonrutin yang diperlukan.. Bukti: Vektor $\langle -4,12 \rangle$ dapat dituliskan ke dalam kombinasi vektor-vektor satuan baku $\mathbf{i}$ dan $\mathbf{j}$

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang notasi vektor dan vektor satuan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Ini adalah materi pengenalan vektor di kelas 11 yang bersifat prosedural dasar. Tidak ada tuntutan kognitif tinggi. |

Run 3 — solusi: Vektor satuan baku i = <1, 0> dan j = <0, 1>. Maka, <a, b> = a<1, 0> + b<0, 1> = ai + bj. Untuk vektor <-4, 12>, substitusi a = -4 dan b = 12 menghasilkan -4i + 12j.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengenali definisi dasar vektor dalam bentuk komponen dan mengubahnya ke bentuk kombinasi linear vektor satuan baku. Ini adalah prosedur langsung yang sudah dipelajari sebagai dasar materi vektor.. Bukti: Vektor < -4, 12 > dapat dituliskan ke dalam kombinasi vektor-vektor satuan baku i dan j
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami definisi simbolik dan konseptual dari vektor satuan baku i dan j serta bagaimana komponen vektor dipetakan ke koefisien kombinasi linear tersebut.. Bukti: Vektor < -4, 12 > dapat dituliskan ke dalam kombinasi vektor-vektor satuan baku i dan j
- Intended difficulty `classify/Easy`: Soal ini bersifat sangat mendasar (fundamental) dalam topik vektor. Tidak ada langkah perencanaan yang kompleks, integrasi konsep, atau kendala yang berinteraksi. Siswa hanya perlu menerapkan definisi langsung.. Bukti: Vektor < -4, 12 > dapat dituliskan ke dalam kombinasi vektor-vektor satuan baku i dan j

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang komponen vektor dan vektor satuan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Ini adalah materi pengenalan vektor di kelas 11. Soal ini menguji pemahaman notasi dasar tanpa manipulasi aljabar atau geometris yang menantang. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4274`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini hanya meminta siswa untuk mengenali dan menerapkan definisi dasar representasi vektor dalam bentuk kombinasi linear vektor satuan baku (i dan j). Tidak ada langkah kompleks, analisis, atau sintesis yang diperlukan.
- Dimensi pengetahuan `conceptual`: Siswa perlu memahami definisi atau konsep dasar mengenai bagaimana komponen vektor kolom dipetakan menjadi koefisien dalam bentuk kombinasi linear vektor satuan baku.
- Intended difficulty `Easy`: Soal ini bersifat sangat mendasar dalam topik vektor. Tidak ada langkah perencanaan yang kompleks, integrasi konsep, atau kendala yang berinteraksi. Siswa hanya perlu menerapkan definisi langsung.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang komponen vektor dan vektor satuan baku i dan j. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah materi pengenalan vektor di kelas 11. Soal ini menguji pemahaman notasi dasar tanpa manipulasi aljabar atau geometris yang menantang. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Vektor pada Bidang
Tipe soal: multiple_choice
Stimulus: -
Soal: Vektor $\langle -4,12 \rangle$ dapat dituliskan ke dalam kombinasi vektor-vektor satuan baku $\mathbf{i}$ dan $\mathbf{j}$, yaitu ….
Pilihan: A. $-4\mathbf{i} - 12\mathbf{j}$
B. $-4\mathbf{i} + 12\mathbf{j}$
C. $4\mathbf{i} + 12\mathbf{j}$
D. $12\mathbf{i} - 4\mathbf{j}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 36. Soal `a6cd9d3eef6dcf642995a65e`

Perahu layar. Sebuah perahu layar bergerak sejauh 100 m ke utara, sedangkan angin memberi gaya 500 N ke timur laut. Berapa banyak usaha yang dilakukan angin?

| Opsi | Isi |
|---|---|
| A | $25.000\sqrt{3}$ J |
| B | $0$ J |
| C | $50.000$ J |
| D | $25.000\sqrt{2}$ J |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Usaha (W) adalah hasil kali titik antara vektor gaya (F) dan vektor perpindahan (d), yaitu W = \|F\|\|d\|cos(θ). Arah utara dan timur laut membentuk sudut θ = 45°. Maka, W = 500 N * 100 m * cos(45°) = 50.000 * (1/2 √2) = 25.000√2 J.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6c6d75434bb7f02a352a579ae266ea9477375a6ecc74ccc622bd74500eec0dc1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2866 |
| 2 | success | valid / verified | applying | procedural | Easy | 2875 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2904 |

Run 1 — solusi: Usaha (W) adalah hasil kali titik antara vektor gaya (F) dan vektor perpindahan (d). W = \|F\|\|d\| cos θ. Arah utara dan timur laut membentuk sudut 45°. Maka, W = 500 N * 100 m * cos 45° = 50000 * (1/2 √2) = 25.000√2 J.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa usaha merupakan aplikasi dari hasil kali titik (dot product) antara vektor gaya dan vektor perpindahan, serta menentukan sudut antara kedua vektor tersebut (45 derajat) untuk menerapkan rumus W = \|F\|\|d\| cos θ.. Bukti: Berapa banyak usaha yang dilakukan angin?; perahu layar bergerak sejauh 100 m ke utara, sedangkan angin memberi gaya 500 N ke timur laut
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman konseptual tentang hubungan antara vektor gaya, vektor perpindahan, dan sudut di antara keduanya dalam konteks fisika (usaha), serta prosedur perhitungan dot product.. Bukti: usaha yang dilakukan angin; 500 N ke timur laut; 100 m ke utara
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemodelan vektor sederhana (menentukan sudut 45 derajat antara utara dan timur laut) dan penerapan rumus dot product yang familiar. Tidak ada kendala yang berinteraksi secara kompleks atau strategi non-rutin yang diperlukan.. Bukti: 100 m ke utara; gaya 500 N ke timur laut; Berapa banyak usaha yang dilakukan angin?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar vektor, dot product, dan trigonometri sudut istimewa. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan mampu mengonversi deskripsi arah mata angin menjadi sudut vektor dan menerapkan rumus usaha sebagai aplikasi dot product. |

Run 2 — solusi: Usaha (W) adalah hasil kali titik antara vektor gaya (F) dan vektor perpindahan (d). W = \|F\|\|d\|cos(θ). Arah utara dan timur laut membentuk sudut θ = 45°. Maka, W = 500 N * 100 m * cos(45°) = 50.000 * (1/2 √2) = 25.000√2 J.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi konsep usaha sebagai hasil kali titik (dot product) antara vektor gaya dan perpindahan, serta menentukan sudut antara arah utara dan timur laut (45 derajat) untuk menerapkan rumus W = \|F\|\|d\|cos(theta). Ini adalah penerapan konsep vektor pada konteks fisika rutin.. Bukti: Perahu layar bergerak sejauh 100 m ke utara; angin memberi gaya 500 N ke timur laut; Berapa banyak usaha yang dilakukan angin?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan rumus hasil kali titik (dot product) dan pengetahuan konseptual tentang hubungan antara vektor gaya, perpindahan, dan sudut di antara keduanya.. Bukti: Berapa banyak usaha yang dilakukan angin?; W = \|F\|\|d\|cos 45°
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena merupakan penerapan langsung rumus dot product dengan sudut yang sudah umum diketahui (45 derajat). Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: 100 m ke utara; gaya 500 N ke timur laut; Berapa banyak usaha yang dilakukan angin?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar vektor, dot product, dan trigonometri sudut istimewa. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL sudah familiar dengan konsep vektor dan dot product. Soal ini hanya memerlukan identifikasi sudut dan substitusi nilai ke rumus, yang merupakan prosedur standar. |

Run 3 — solusi: Usaha (W) adalah hasil kali titik antara gaya (F) dan perpindahan (d), yaitu W = \|F\|\|d\|cos(θ). Arah utara dan timur laut membentuk sudut θ = 45°. Maka, W = 500 N * 100 m * cos(45°) = 50.000 * (1/2 √2) = 25.000√2 J.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa usaha adalah hasil kali titik (dot product) antara vektor gaya dan vektor perpindahan, kemudian menerapkan rumus W = \|F\|\|d\|cos(θ) dengan menentukan sudut antara arah utara dan timur laut.. Bukti: Perahu layar bergerak sejauh 100 m ke utara; angin memberi gaya 500 N ke timur laut; Berapa banyak usaha yang dilakukan angin?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman konseptual tentang hubungan antara vektor gaya, perpindahan, dan sudut dalam konteks usaha (fisika/vektor), serta penerapan prosedur perkalian skalar.. Bukti: Berapa banyak usaha yang dilakukan angin?; W = \|F\|\|d\|cos 45°
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena memerlukan pemahaman tentang representasi vektor (arah mata angin) untuk menentukan sudut θ = 45° sebelum menerapkan rumus dot product. Meskipun prosedurnya standar, siswa harus mampu menerjemahkan deskripsi arah menjadi nilai sudut yang tepat.. Bukti: 100 m ke utara; gaya 500 N ke timur laut; sudut antara arah utara (gerak) dan timur laut (gaya) adalah 45°

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar vektor, arah mata angin, dan konsep dot product (hasil kali titik). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan mampu mengaitkan konsep vektor dengan masalah kontekstual. Penentuan sudut 45 derajat dari arah mata angin adalah langkah krusial yang membedakan tingkat kesulitan soal ini. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4715`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi bahwa usaha merupakan aplikasi dari hasil kali titik (dot product) antara vektor gaya dan vektor perpindahan, serta menentukan sudut antara kedua vektor tersebut (45 derajat) untuk menerapkan rumus W = \|F\|\|d\| cos θ.
- Dimensi pengetahuan `conceptual`: Soal ini menuntut pemahaman konseptual tentang hubungan antara vektor gaya, vektor perpindahan, dan sudut di antara keduanya dalam konteks fisika (usaha), serta prosedur perhitungan dot product.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena memerlukan pemodelan vektor sederhana (menentukan sudut 45 derajat antara utara dan timur laut) dan penerapan rumus dot product yang familiar. Tidak ada kendala yang berinteraksi secara kompleks atau strategi non-rutin yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar vektor, dot product, dan trigonometri sudut istimewa. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan mampu mengonversi deskripsi arah mata angin menjadi sudut vektor dan menerapkan rumus usaha sebagai aplikasi dot product. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Hasil Kali Titik
Tipe soal: multiple_choice
Stimulus: -
Soal: Perahu layar. Sebuah perahu layar bergerak sejauh 100 m ke utara, sedangkan angin memberi gaya 500 N ke timur laut. Berapa banyak usaha yang dilakukan angin?
Pilihan: A. $25.000\sqrt{3}$ J
B. $0$ J
C. $50.000$ J
D. $25.000\sqrt{2}$ J
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 37. Soal `197954ccd24f5bbacd84ed75`

Vektor $\mathbf{u}$ dan vektor $\mathbf{v}$ secara berturut-turut memiliki panjang 12 dan 18. Jika besar sudut di antara kedua vektor tersebut adalah $\dfrac{\pi}{3}$, tentukan $\mathbf{u} \cdot \mathbf{v}$.

| Opsi | Isi |
|---|---|
| A | 108 |
| B | 216 |
| C | ≈215,7 |
| D | 0 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: u · v = \|u\| \|v\| cos(θ) = 12 * 18 * cos(π/3) = 216 * 0.5 = 108
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `dbad90d70b25444dc926a5edcc495aeef7367c1a3bd71561d6048ef816ccb8b6`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 4155 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2717 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2695 |

Run 1 — solusi: u · v = \|u\|\|v\| cos θ = 12 * 18 * cos(π/3) = 216 * 0.5 = 108
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus hasil kali titik vektor yang sudah dipelajari secara langsung dengan nilai yang diberikan.. Bukti: Vektor u dan vektor v secara berturut-turut memiliki panjang 12 dan 18. Jika besar sudut di antara kedua vektor tersebut adalah π/3, tentukan u · v.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji kemampuan siswa dalam menjalankan prosedur perhitungan hasil kali titik menggunakan rumus standar.. Bukti: Vektor u dan vektor v secara berturut-turut memiliki panjang 12 dan 18. Jika besar sudut di antara kedua vektor tersebut adalah π/3, tentukan u · v.
- Intended difficulty `classify/Easy`: Soal ini adalah penerapan langsung rumus dasar. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang diperlukan.. Bukti: Vektor u dan vektor v secara berturut-turut memiliki panjang 12 dan 18. Jika besar sudut di antara kedua vektor tersebut adalah π/3, tentukan u · v.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus hasil kali titik vektor dan nilai trigonometri sudut istimewa. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan mampu menghitung hasil kali titik dengan data eksplisit. Soal tidak memiliki kompleksitas tambahan. |

Run 2 — solusi: u · v = \|u\| \|v\| cos(θ). Diketahui \|u\| = 12, \|v\| = 18, dan θ = π/3. Maka, u · v = 12 * 18 * cos(π/3) = 216 * (1/2) = 108.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk menerapkan rumus dasar hasil kali titik (dot product) secara langsung dengan nilai yang sudah diketahui. Siswa hanya perlu melakukan substitusi nilai ke dalam rumus yang sudah familiar.. Bukti: tentukan u · v; u · v = \|u\| \|v\| cos θ
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap definisi dan rumus hasil kali titik (dot product) antara dua vektor, yang merupakan bagian dari pengetahuan prosedural dalam matematika.. Bukti: u · v = \|u\| \|v\| cos θ
- Intended difficulty `classify/Easy`: Soal ini dikategorikan Easy karena merupakan penerapan langsung dari rumus dot product. Tidak ada langkah perencanaan yang kompleks, kendala yang berinteraksi, atau kebutuhan untuk mengubah representasi. Siswa hanya perlu mensubstitusi nilai yang diberikan ke dalam rumus standar.. Bukti: panjang 12 dan 18; sudut di antara kedua vektor tersebut adalah π/3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang vektor dan nilai trigonometri sudut istimewa. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 11, penggunaan rumus dot product dengan sudut istimewa adalah prosedur standar yang sangat rutin. |

Run 3 — solusi: u · v = \|u\| \|v\| cos(θ) = 12 * 18 * cos(π/3) = 216 * (1/2) = 108.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk menerapkan rumus dasar hasil kali titik (dot product) secara langsung dengan nilai yang sudah diketahui. Tidak ada manipulasi atau strategi non-rutin yang diperlukan.. Bukti: tentukan u · v; u · v = \|u\| \|v\| cos θ = 12·18·cos(π/3)
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami rumus hasil kali titik (konsep) dan melakukan perhitungan (prosedural) untuk mendapatkan hasil akhir.. Bukti: u · v = \|u\| \|v\| cos θ
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mensubstitusi nilai yang diberikan ke dalam rumus standar tanpa perlu melakukan perencanaan langkah yang kompleks atau integrasi konsep yang sulit.. Bukti: panjang 12 dan 18; sudut di antara kedua vektor tersebut adalah π/3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang vektor dan nilai trigonometri sudut istimewa. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, penggunaan rumus dot product dengan sudut istimewa adalah prosedur standar yang sangat familiar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 1, "knowing": 2} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4180`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta penerapan langsung rumus hasil kali titik (dot product) dengan nilai yang sudah diberikan secara eksplisit. Tidak ada langkah penalaran non-rutin atau integrasi konsep yang kompleks.
- Dimensi pengetahuan `procedural`: Siswa perlu mengetahui rumus hasil kali titik (prosedural) dan nilai trigonometri sudut istimewa (faktual) untuk menyelesaikan soal ini.
- Intended difficulty `Easy`: Soal ini adalah latihan rutin yang sangat standar. Siswa hanya perlu mensubstitusi nilai ke dalam rumus yang sudah dikenal. Tidak ada kendala yang berinteraksi atau kebutuhan untuk perencanaan strategi.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus hasil kali titik vektor dan nilai trigonometri sudut istimewa. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 11, penggunaan rumus dot product dengan sudut istimewa adalah prosedur standar yang sangat rutin. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Hasil Kali Titik
Tipe soal: multiple_choice
Stimulus: -
Soal: Vektor $\mathbf{u}$ dan vektor $\mathbf{v}$ secara berturut-turut memiliki panjang 12 dan 18. Jika besar sudut di antara kedua vektor tersebut adalah $\dfrac{\pi}{3}$, tentukan $\mathbf{u} \cdot \mathbf{v}$.
Pilihan: A. 108
B. 216
C. ≈215,7
D. 0
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 38. Soal `3bc06d4dc345f67abded7388`

Pada gambar segitiga _ABC_ di samping, titik _K_ adalah titik tengah dari _AB_ dan titik _L_ adalah titik tengah dari _AC_.<br><br>Nyatakan $\overrightarrow{KL}$ dalam $\overrightarrow{KA}$ dan $\overrightarrow{LA}$.

| Opsi | Isi |
|---|---|
| A | $\overrightarrow{KL} = \overrightarrow{KA} - \overrightarrow{LA}$ |
| B | $\overrightarrow{KL} = \overrightarrow{LA} - \overrightarrow{KA}$ |
| C | $\overrightarrow{KL} = 2(\overrightarrow{KA} - \overrightarrow{LA})$ |
| D | $\overrightarrow{KL} = \overrightarrow{KA} + \overrightarrow{LA}$ |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Berdasarkan aturan penjumlahan vektor, KL = KA + AL. Karena L adalah titik tengah AC, maka AL = -LA. Dengan demikian, KL = KA - LA.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `98f7de567b74ec8bb14e1691f004dff133a40158c960ad31fe0490044bccba4f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2686 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2640 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2742 |

Run 1 — solusi: Berdasarkan aturan penjumlahan vektor, KL = KA + AL. Karena L adalah titik tengah AC, maka AL = -LA. Dengan demikian, KL = KA - LA.
- Domain kognitif `classify/applying`: Siswa perlu memahami hubungan vektor dasar (penjumlahan vektor) dan sifat titik tengah (vektor berlawanan arah) untuk menyatakan vektor KL dalam bentuk KA dan LA. Ini adalah penerapan konsep dasar vektor yang rutin.. Bukti: Nyatakan KL dalam KA dan LA
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang operasi vektor dan representasi geometris titik tengah dalam konteks vektor.. Bukti: Nyatakan KL dalam KA dan LA
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu memahami definisi vektor posisi relatif dan operasi penjumlahan vektor dasar. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: titik K adalah titik tengah dari AB dan titik L adalah titik tengah dari AC; Nyatakan KL dalam KA dan LA

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang vektor posisi dan operasi penjumlahan vektor. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi vektor adalah topik dasar kelas 11. Soal ini hanya meminta manipulasi vektor dasar tanpa kerumitan geometri tambahan, sehingga tergolong mudah bagi siswa kelas 11. |

Run 2 — solusi: Berdasarkan aturan penjumlahan vektor, KL + LA = KA, sehingga KL = KA - LA.
- Domain kognitif `classify/applying`: Siswa perlu memahami hubungan vektor dalam segitiga dan menerapkan aturan penjumlahan vektor dasar untuk menyatakan satu vektor sebagai selisih dua vektor lainnya.. Bukti: Nyatakan KL dalam KA dan LA
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang representasi vektor dalam geometri segitiga dan hubungan antarvektor.. Bukti: titik K adalah titik tengah dari AB dan titik L adalah titik tengah dari AC
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu menerapkan aturan segitiga vektor (KL + LA = KA) untuk mendapatkan KL = KA - LA. Tidak ada kendala kompleks atau perencanaan strategi yang rumit.. Bukti: Nyatakan KL dalam KA dan LA

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang penjumlahan dan pengurangan vektor dalam geometri. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi vektor adalah dasar di kelas 11. Soal ini hanya menuntut pemahaman definisi vektor posisi/relatif yang sangat mendasar. |

Run 3 — solusi: Berdasarkan aturan penjumlahan vektor, KL = AL - AK. Diketahui KA = -AK dan LA = -AL, maka AK = -KA dan AL = -LA. Substitusi ke persamaan: KL = (-LA) - (-KA) = KA - LA.
- Domain kognitif `classify/applying`: Siswa perlu memahami hubungan vektor posisi dan operasi pengurangan vektor untuk menyatakan vektor KL sebagai selisih dari dua vektor lain yang diberikan. Ini adalah penerapan konsep dasar vektor.. Bukti: Nyatakan KL dalam KA dan LA
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip dasar operasi vektor (penjumlahan dan pengurangan) dalam konteks geometri segitiga.. Bukti: Nyatakan KL dalam KA dan LA
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu menerapkan definisi pengurangan vektor KL = AL - AK dan mengubahnya ke bentuk KA dan LA. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Nyatakan KL dalam KA dan LA

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar operasi vektor dan vektor posisi. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, operasi dasar vektor seperti ini adalah materi awal yang rutin dan langsung. |

Histori retry: run 1 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 2 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

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
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Pembuktian Geometris
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada gambar segitiga _ABC_ di samping, titik _K_ adalah titik tengah dari _AB_ dan titik _L_ adalah titik tengah dari _AC_.

Nyatakan $\overrightarrow{KL}$ dalam $\overrightarrow{KA}$ dan $\overrightarrow{LA}$.
Pilihan: A. $\overrightarrow{KL} = \overrightarrow{KA} - \overrightarrow{LA}$
B. $\overrightarrow{KL} = \overrightarrow{LA} - \overrightarrow{KA}$
C. $\overrightarrow{KL} = 2(\overrightarrow{KA} - \overrightarrow{LA})$
D. $\overrightarrow{KL} = \overrightarrow{KA} + \overrightarrow{LA}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: Soal meminta menyatakan vektor KL dalam KA dan LA. Secara geometris, KL = AL - AK. Karena K adalah titik tengah AB, maka KA = -AK. Karena L adalah titik tengah AC, maka LA = -AL. Jadi, KL = AL - AK = (-LA) - (-KA) = KA - LA. Kunci A benar secara matematis..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 39. Soal `a4aba8ef06446b64179d23cf`

Pada gambar segitiga _ABC_ di samping, titik _K_ adalah titik tengah dari _AB_ dan titik _L_ adalah titik tengah dari _AC_.<br><br>Nyatakan $\overrightarrow{BC}$ dalam $\overrightarrow{KA}$ dan $\overrightarrow{LA}$.

| Opsi | Isi |
|---|---|
| A | $\overrightarrow{BC} = 2(\overrightarrow{KA} - \overrightarrow{LA})$ |
| B | $\overrightarrow{BC} = 2(\overrightarrow{KA} + \overrightarrow{LA})$ |
| C | $\overrightarrow{BC} = 2(\overrightarrow{LA} - \overrightarrow{KA})$ |
| D | $\overrightarrow{BC} = \overrightarrow{KA} - \overrightarrow{LA}$ |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Diketahui K titik tengah AB, maka AB = 2AK = -2KA. L titik tengah AC, maka AC = 2AL = -2LA. Vektor BC = AC - AB = (-2LA) - (-2KA) = 2KA - 2LA = 2(KA - LA).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5a3b8f6d9f3bc3ac35460d6222a22a8f2b3191ed3882056d1352aec83aa195a8`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2817 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2791 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2762 |

Run 1 — solusi: Diketahui K titik tengah AB, maka AB = 2AK = -2KA. L titik tengah AC, maka AC = 2AL = -2LA. Vektor BC = AC - AB = (-2LA) - (-2KA) = 2KA - 2LA = 2(KA - LA).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep vektor posisi dan hubungan titik tengah untuk menyatakan vektor BC sebagai selisih vektor AC dan AB, kemudian melakukan manipulasi aljabar vektor untuk mengubah basis ke KA dan LA. Ini adalah penerapan prosedur rutin pada konteks geometri.. Bukti: Nyatakan BC dalam KA dan LA; K adalah titik tengah dari AB dan titik L adalah titik tengah dari AC
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman prinsip vektor (hubungan titik tengah dan operasi pengurangan vektor) serta prosedur aljabar untuk mengubah basis vektor.. Bukti: K adalah titik tengah dari AB; Nyatakan BC dalam KA dan LA
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah logis yang saling terkait: mendefinisikan AB dan AC dalam bentuk KA dan LA, melakukan operasi pengurangan vektor, dan memfaktorkan hasilnya. Meskipun prosedurnya familiar, siswa harus merencanakan langkah-langkah tersebut secara berurutan tanpa bantuan eksplisit.. Bukti: K adalah titik tengah dari AB dan titik L adalah titik tengah dari AC; Nyatakan BC dalam KA dan LA

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi dasar vektor, konsep titik tengah, dan vektor posisi. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan mampu melakukan manipulasi vektor dasar. Soal ini menguji pemahaman konsep titik tengah dan operasi vektor yang merupakan materi standar, dengan tingkat kesulitan menengah karena memerlukan integrasi beberapa langkah. |

Run 2 — solusi: Diketahui K titik tengah AB, maka AB = 2AK = -2KA. L titik tengah AC, maka AC = 2AL = -2LA. Vektor BC = AC - AB = (-2LA) - (-2KA) = 2KA - 2LA = 2(KA - LA).
- Domain kognitif `classify/applying`: Siswa perlu memahami hubungan vektor posisi titik tengah dengan vektor sisi segitiga, kemudian melakukan manipulasi aljabar vektor untuk menyatakan BC dalam KA dan LA. Ini adalah penerapan konsep vektor pada geometri.. Bukti: titik K adalah titik tengah dari AB dan titik L adalah titik tengah dari AC; Nyatakan BC dalam KA dan LA
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan prinsip dasar vektor (penjumlahan/pengurangan vektor dan definisi titik tengah) untuk menyelesaikan masalah pembuktian geometris.. Bukti: titik K adalah titik tengah dari AB dan titik L adalah titik tengah dari AC; Nyatakan BC dalam KA dan LA
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemahaman tentang relasi vektor titik tengah. Langkah-langkahnya rutin (mendefinisikan vektor sisi, melakukan pengurangan vektor), tidak memerlukan strategi non-rutin yang kompleks.. Bukti: titik K adalah titik tengah dari AB dan titik L adalah titik tengah dari AC; Nyatakan BC dalam KA dan LA

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar vektor, operasi vektor, dan konsep titik tengah. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, manipulasi vektor dasar ini adalah standar. Tingkat kesulitan Medium diberikan karena siswa harus berhati-hati dengan arah vektor (KA vs AK) dan faktor skala 2. |

Run 3 — solusi: Diketahui K titik tengah AB, maka AB = 2AK = -2KA. L titik tengah AC, maka AC = 2AL = -2LA. Vektor BC = AC - AB = (-2LA) - (-2KA) = 2KA - 2LA = 2(KA - LA).
- Domain kognitif `classify/applying`: Siswa perlu memahami hubungan vektor posisi titik tengah dan menerapkan operasi pengurangan vektor untuk menyatakan vektor sisi segitiga berdasarkan vektor yang diberikan. Ini melibatkan penerapan konsep vektor pada geometri.. Bukti: Nyatakan BC dalam KA dan LA; K adalah titik tengah dari AB dan titik L adalah titik tengah dari AC
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman tentang prinsip vektor (titik tengah, pengurangan vektor) dan prosedur aljabar vektor untuk menyederhanakan ekspresi.. Bukti: K adalah titik tengah dari AB; Nyatakan BC dalam KA dan LA
- Intended difficulty `classify/Easy`: Soal ini memerlukan pemahaman konsep titik tengah dalam vektor dan manipulasi aljabar vektor yang rutin. Siswa hanya perlu melakukan substitusi dan pengurangan sederhana. Tidak ada kendala yang berinteraksi secara kompleks.. Bukti: Nyatakan BC dalam KA dan LA; K adalah titik tengah dari AB dan titik L adalah titik tengah dari AC

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar vektor, operasi vektor, dan konsep titik tengah. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, hubungan antara vektor posisi titik tengah dan vektor sisi segitiga adalah materi dasar yang rutin dalam topik vektor. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4359`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan konsep vektor posisi dan hubungan titik tengah untuk menyatakan vektor BC sebagai selisih vektor AC dan AB, kemudian melakukan manipulasi aljabar vektor untuk mengubah basis ke KA dan LA. Ini adalah penerapan prosedur rutin pada konteks geometri.
- Dimensi pengetahuan `conceptual`: Soal menuntut pemahaman prinsip vektor (hubungan titik tengah dan operasi pengurangan vektor) serta prosedur aljabar untuk mengubah basis vektor.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah logis yang saling terkait: mendefinisikan AB dan AC dalam bentuk KA dan LA, melakukan operasi pengurangan vektor, dan memfaktorkan hasilnya. Meskipun prosedurnya familiar, siswa harus berhati-hati dengan arah vektor (KA vs AK) dan faktor skala 2.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi dasar vektor, konsep titik tengah, dan vektor posisi. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan mampu melakukan manipulasi vektor dasar. Soal ini menguji pemahaman konsep titik tengah dan operasi vektor yang merupakan materi standar, dengan tingkat kesulitan menengah karena memerlukan integrasi beberapa langkah. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Pembuktian Geometris
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada gambar segitiga _ABC_ di samping, titik _K_ adalah titik tengah dari _AB_ dan titik _L_ adalah titik tengah dari _AC_.

Nyatakan $\overrightarrow{BC}$ dalam $\overrightarrow{KA}$ dan $\overrightarrow{LA}$.
Pilihan: A. $\overrightarrow{BC} = 2(\overrightarrow{KA} - \overrightarrow{LA})$
B. $\overrightarrow{BC} = 2(\overrightarrow{KA} + \overrightarrow{LA})$
C. $\overrightarrow{BC} = 2(\overrightarrow{LA} - \overrightarrow{KA})$
D. $\overrightarrow{BC} = \overrightarrow{KA} - \overrightarrow{LA}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 40. Soal `78652b4108bd747c96b2f4a8`

Pada $\triangle ABC$, $AD$ membagi $\angle A$ menjadi dua bagian yang sama besar. $AD$ disebut garis bagi. Titik $D$ terletak pada sisi $BC$. Petunjuk: Gambarkan garis yang sejajar dengan $AD$ dan melalui titik $C$. Garis ini berpotongan dengan perpanjangan $AB$ di titik $E$.<br><br>Beri alasan bahwa $\triangle ACE$ sama kaki. Tuliskan sisi-sisi yang sama panjang.

| Opsi | Isi |
|---|---|
| A | AC = CE, karena ∠CAE = ∠AEC |
| B | AC = AE, karena ∠ACE = ∠AEC |
| C | AB = AC, karena AD garis bagi |
| D | AE = CE, karena ∠ACE = ∠CAE |

![Gambar sumber soal 40](<../../../images/kelas7_crop-p0205-garis-bagi.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Karena CE sejajar AD, maka sudut AEC = sudut BAD (sehadap) dan sudut ACE = sudut DAC (berseberangan dalam). Karena AD adalah garis bagi, maka sudut BAD = sudut DAC. Akibatnya, sudut AEC = sudut ACE. Karena dua sudut pada segitiga ACE sama besar, maka segitiga ACE sama kaki dengan AC = AE.
Gambar sumber: images/kelas7_crop-p0205-garis-bagi.png. Transkripsi visual: Segitiga ABC dengan titik D pada sisi BC. Garis AD membagi sudut A menjadi dua bagian sama besar (ditandai dengan busur hijau). Titik A, B, C, D terlihat jelas.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['menyebutkan', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fa47fd05b73a4cc4cb29dfe7ef4a4737366f3cc54e1740eb4cc62e55c9a41c04`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 3954 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 4020 |
| 3 | success | valid / verified | reasoning | conceptual | Medium | 3950 |

Run 1 — solusi: Misalkan AD sejajar CE. Sudut BAD = sudut AEC (sehadap). Sudut DAC = sudut ACE (berseberangan dalam). Karena AD adalah garis bagi, sudut BAD = sudut DAC. Maka, sudut AEC = sudut ACE. Dalam segitiga ACE, karena dua sudut alas sama besar, maka segitiga tersebut sama kaki dengan AC = AE.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk melakukan pembuktian geometris sederhana dengan bantuan konstruksi garis tambahan. Siswa perlu mengaitkan sifat garis sejajar (sudut sehadap dan berseberangan) dengan definisi garis bagi untuk menyimpulkan sifat segitiga sama kaki. Ini melibatkan penerapan konsep geometri dasar dalam konteks pembuktian.. Bukti: Beri alasan bahwa ΔACE sama kaki; Gambarkan garis yang sejajar dengan AD dan melalui titik C
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami prinsip-prinsip geometri (garis sejajar, sudut, segitiga sama kaki) dan bagaimana prinsip-prinsip tersebut saling berhubungan dalam sebuah pembuktian.. Bukti: AD membagi ∠A menjadi dua bagian yang sama besar; Garis yang sejajar dengan AD dan melalui titik C
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena meskipun prosedurnya bersifat rutin bagi siswa yang memahami geometri, soal ini menuntut siswa untuk memahami dan menerapkan konstruksi garis bantu serta menghubungkan beberapa sifat sudut (sehadap, berseberangan) untuk mencapai kesimpulan. Ini bukan sekadar ingatan fakta, melainkan penerapan konsep dalam pembuktian.. Bukti: Gambarkan garis yang sejajar dengan AD dan melalui titik C; Beri alasan bahwa ΔACE sama kaki

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat-sifat sudut pada garis sejajar dan definisi segitiga sama kaki. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi ini sering diajarkan di jenjang SMP, untuk kelas 11 SMA, soal ini menguji kemampuan penalaran geometris dasar yang diperlukan sebagai prasyarat untuk materi vektor atau transformasi geometri. |

Run 2 — solusi: Karena CE sejajar AD, maka sudut AEC = sudut BAD (sehadap) dan sudut ACE = sudut DAC (berseberangan dalam). Karena AD adalah garis bagi, maka sudut BAD = sudut DAC. Akibatnya, sudut AEC = sudut ACE. Karena dua sudut pada segitiga ACE sama besar, maka segitiga ACE sama kaki dengan AC = AE.
- Domain kognitif `classify/reasoning`: Soal meminta siswa untuk melakukan pembuktian geometris sederhana dengan mengintegrasikan sifat garis sejajar dan sudut pada segitiga. Siswa harus menghubungkan konsep garis bagi dengan sifat sudut sehadap dan berseberangan untuk menyimpulkan kesamaan sudut, yang kemudian mengarah pada sifat segitiga sama kaki. Ini memerlukan penalaran logis (reasoning) untuk menyusun argumen pembuktian.. Bukti: Beri alasan bahwa ΔACE sama kaki.; Gambarkan garis yang sejajar dengan AD dan melalui titik C.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip-prinsip geometris (konseptual) tentang hubungan sudut yang terbentuk oleh garis sejajar dan transversal, serta definisi segitiga sama kaki, untuk membangun argumen pembuktian.. Bukti: AD membagi ∠A menjadi dua bagian yang sama besar.; Garis ini berpotongan dengan perpanjangan AB di titik E.; Beri alasan bahwa ΔACE sama kaki.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena meskipun prosedurnya melibatkan konsep geometri dasar, siswa kelas 11 diharapkan mampu melakukan konstruksi mental atau visual berdasarkan petunjuk yang diberikan dan menyusun argumen logis. Tingkat kesulitannya moderat karena petunjuk sudah diberikan, namun siswa tetap harus mengintegrasikan beberapa properti sudut secara mandiri.. Bukti: Petunjuk: Gambarkan garis yang sejajar dengan AD dan melalui titik C.; Beri alasan bahwa ΔACE sama kaki.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat sudut pada garis sejajar (sehadap, berseberangan), definisi garis bagi, dan sifat segitiga sama kaki. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi ini sering diajarkan di jenjang SMP, untuk kelas 11 TL, soal ini menuntut kemampuan pembuktian formal yang memerlukan pemahaman konseptual yang kuat, bukan sekadar komputasi. |

Run 3 — solusi: AD sejajar CE. Sudut BAD = sudut AEC (sehadap). Sudut DAC = sudut ACE (berseberangan dalam). Karena AD adalah garis bagi, sudut BAD = sudut DAC. Maka, sudut AEC = sudut ACE. Segitiga ACE memiliki dua sudut alas yang sama, sehingga segitiga ACE sama kaki dengan AC = AE.
- Domain kognitif `classify/reasoning`: Soal meminta siswa untuk melakukan pembuktian geometris sederhana dengan mengikuti petunjuk konstruksi yang diberikan. Siswa perlu mengidentifikasi hubungan sudut (sehadap dan berseberangan dalam) akibat garis sejajar untuk menyimpulkan sifat segitiga sama kaki.. Bukti: Beri alasan bahwa ΔACE sama kaki; Gambarkan garis yang sejajar dengan AD dan melalui titik C
- Dimensi pengetahuan `classify/conceptual`: Siswa harus menerapkan prinsip-prinsip geometri (garis sejajar, sudut, dan sifat segitiga sama kaki) untuk membangun argumen logis.. Bukti: AD membagi ∠A menjadi dua bagian yang sama besar; Garis yang sejajar dengan AD dan melalui titik C
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena meskipun prosedurnya mengikuti petunjuk (scaffolded), siswa harus memahami dan mengintegrasikan hubungan antara garis sejajar, sudut, dan sifat segitiga untuk membenarkan kesimpulan. Ini melampaui sekadar ingatan fakta.. Bukti: Gambarkan garis yang sejajar dengan AD dan melalui titik C; Beri alasan bahwa ΔACE sama kaki

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat sudut pada garis sejajar (sehadap, berseberangan) dan sifat segitiga sama kaki. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi ini sering diajarkan di jenjang SMP, soal ini menuntut kemampuan penalaran geometris yang relevan untuk kelas 11 dalam konteks pembuktian teorema (seperti Teorema Garis Bagi). Tingkat kesulitan Medium sesuai karena adanya bantuan konstruksi namun tetap memerlukan pemahaman konseptual. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 1, "reasoning": 2} | majority_2_of_3 / adjudicated | reasoning |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `5794`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `reasoning`: Soal ini menuntut penalaran geometris untuk menghubungkan sifat garis sejajar (sudut sehadap dan berseberangan) dengan definisi garis bagi untuk membuktikan sifat segitiga sama kaki. Siswa harus mengintegrasikan hubungan antar sudut tersebut, bukan sekadar menghitung.
- Dimensi pengetahuan `conceptual`: Siswa perlu memahami prinsip-prinsip geometri (konseptual) tentang hubungan sudut yang terbentuk oleh garis sejajar dan transversal, serta definisi segitiga sama kaki, untuk membangun argumen pembuktian.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena meskipun prosedurnya melibatkan konsep geometri dasar, siswa kelas 11 diharapkan mampu melakukan konstruksi mental atau visual berdasarkan petunjuk yang diberikan dan menyusun argumen logis. Tingkat kesulitannya moderat karena petunjuk sudah diberikan, namun siswa tetap harus mengintegrasikan beberapa properti sudut secara mandiri.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat sudut pada garis sejajar (sehadap, berseberangan), definisi garis bagi, dan sifat segitiga sama kaki. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi ini sering diajarkan di jenjang SMP, untuk kelas 11 TL, soal ini menuntut kemampuan pembuktian formal yang memerlukan pemahaman konseptual yang kuat, bukan sekadar komputasi. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Kesebangunan pada Segitiga
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada $\triangle ABC$, $AD$ membagi $\angle A$ menjadi dua bagian yang sama besar. $AD$ disebut garis bagi. Titik $D$ terletak pada sisi $BC$. Petunjuk: Gambarkan garis yang sejajar dengan $AD$ dan melalui titik $C$. Garis ini berpotongan dengan perpanjangan $AB$ di titik $E$.

Beri alasan bahwa $\triangle ACE$ sama kaki. Tuliskan sisi-sisi yang sama panjang.
Pilihan: A. AC = CE, karena ∠CAE = ∠AEC
B. AC = AE, karena ∠ACE = ∠AEC
C. AB = AC, karena AD garis bagi
D. AE = CE, karena ∠ACE = ∠CAE
Transkripsi visual: Segitiga ABC dengan titik D pada sisi BC. Garis AD membagi sudut A menjadi dua bagian sama besar (ditandai dengan busur hijau). Titik A, B, C, D terlihat jelas.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "reasoning", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 41. Soal `907f9e4697523a633ea0ac02`

Suatu segitiga ABC siku-siku di titik B memiliki panjang AB=8 cm, BC=15 cm, dan AC=17 cm. Jika ΔA'B'C' merupakan hasil dilatasi dari ΔABC dengan faktor skala 3, maka luas ΔA'B'C' adalah…

| Opsi | Isi |
|---|---|
| A | 180 cm² |
| B | 60 cm² |
| C | 540 cm² |
| D | 1.620 cm² |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Luas segitiga ABC = 0.5 * 8 * 15 = 60 cm². Dilatasi dengan faktor skala k=3 mengubah luas bangun datar menjadi k² kali luas semula. Maka, luas ΔA'B'C' = 3² * 60 = 9 * 60 = 540 cm².
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `bbda9688d887ebbcb18cf6e1a2d9615e960354733ac72b3e8cc4bb5b539566f1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3400 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2736 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2742 |

Run 1 — solusi: Luas segitiga ABC = 0.5 * 8 * 15 = 60 cm². Dilatasi dengan faktor skala k=3 mengubah luas bangun datar menjadi k² kali luas semula. Maka, luas ΔA'B'C' = 3² * 60 = 9 * 60 = 540 cm².
- Domain kognitif `classify/applying`: Siswa menerapkan prosedur rutin untuk menghitung perubahan luas akibat dilatasi dengan faktor skala tertentu.. Bukti: dilatasi dari ΔABC dengan faktor skala 3; luas ΔA'B'C' adalah
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip konseptual bahwa dilatasi dengan faktor skala k menyebabkan perubahan luas sebesar k².. Bukti: dilatasi dari ΔABC dengan faktor skala 3; luas ΔA'B'C'
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari rumus perubahan luas pada dilatasi. Tidak ada kendala yang saling berinteraksi atau kebutuhan untuk merencanakan strategi non-rutin.. Bukti: dilatasi dari ΔABC dengan faktor skala 3; luas ΔA'B'C' adalah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep luas segitiga dan sifat dilatasi pada luas bangun datar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi transformasi geometri (dilatasi) adalah standar kelas 11. Soal ini menguji pemahaman dasar tanpa kompleksitas tambahan, sehingga dikategorikan mudah. |

Run 2 — solusi: Luas segitiga ABC = 0.5 * 8 * 15 = 60 cm². Dilatasi dengan faktor skala k=3 mengubah luas dengan faktor k² = 3² = 9. Luas A'B'C' = 9 * 60 = 540 cm².
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep hubungan antara faktor skala dilatasi dan perubahan luas bangun datar (k²), bukan sekadar menghitung luas awal.. Bukti: Jika ΔA'B'C' merupakan hasil dilatasi dari ΔABC dengan faktor skala 3, maka luas ΔA'B'C' adalah
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman prinsip transformasi geometri (dilatasi) dan pengaruhnya terhadap luas bangun datar.. Bukti: dilatasi dari ΔABC dengan faktor skala 3
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu mengingat atau memahami hubungan luas setelah dilatasi (k²). Prosedur perhitungan luas segitiga dan perkalian faktor skala sangat rutin bagi siswa kelas 11.. Bukti: faktor skala 3; luas ΔA'B'C' adalah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus luas segitiga dan konsep dasar dilatasi (perubahan luas oleh faktor skala k²). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi dilatasi dan perbandingan luas adalah standar kurikulum kelas 11. Soal tidak memerlukan perencanaan kompleks atau integrasi konsep yang sulit. |

Run 3 — solusi: Luas segitiga ABC = 0.5 * 8 * 15 = 60 cm². Dilatasi dengan faktor skala k=3 mengubah luas dengan faktor k² = 3² = 9. Luas ΔA'B'C' = 9 * 60 = 540 cm².
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep hubungan antara faktor skala dilatasi dengan perubahan luas bangun datar (k²), bukan sekadar menerapkan rumus luas segitiga dasar.. Bukti: Jika ΔA'B'C' merupakan hasil dilatasi dari ΔABC dengan faktor skala 3, maka luas ΔA'B'C' adalah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana transformasi geometri (dilatasi) mempengaruhi properti luas suatu bangun.. Bukti: dilatasi dari ΔABC dengan faktor skala 3
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena merupakan penerapan langsung dari prinsip dilatasi luas (k²) yang umum diajarkan. Jalur penyelesaian sangat jelas, hanya melibatkan dua langkah rutin (menghitung luas awal dan mengalikan dengan kuadrat faktor skala).. Bukti: faktor skala 3; luas ΔA'B'C' adalah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Rumus luas segitiga dan konsep dilatasi pada bangun datar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi dilatasi adalah standar kelas 11. Soal ini tidak memerlukan integrasi konsep yang kompleks atau perencanaan strategi non-rutin. |

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
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Dilatasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Suatu segitiga ABC siku-siku di titik B memiliki panjang AB=8 cm, BC=15 cm, dan AC=17 cm. Jika ΔA'B'C' merupakan hasil dilatasi dari ΔABC dengan faktor skala 3, maka luas ΔA'B'C' adalah…
Pilihan: A. 180 cm²
B. 60 cm²
C. 540 cm²
D. 1.620 cm²
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 42. Soal `11862b32db722263e3195403`

Tentukan peta dari transformasi geometri berikut.<br><br>Garis $3x - 2y + 5 = 0$ yang ditransformasi oleh rotasi 180° terhadap titik asal (0, 0).

| Opsi | Isi |
|---|---|
| A | 3x – 2y – 5 = 0 |
| B | –3x + 2y + 5 = 0 |
| C | 3x – 2y + 5 = 0 |
| D | –3x – 2y + 5 = 0 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Rotasi 180° terhadap (0,0) memetakan (x, y) ke (-x', -y'). Substitusi x = -x' dan y = -y' ke dalam persamaan 3x - 2y + 5 = 0 menghasilkan 3(-x') - 2(-y') + 5 = 0, yang disederhanakan menjadi -3x' + 2y' + 5 = 0.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d4ec34774896f366eef68bd4621c78cac07be6717e91c346cbb1996e72e377c4`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2770 |
| 2 | success | valid / verified | applying | procedural | Easy | 2782 |
| 3 | success | valid / verified | applying | procedural | Easy | 3605 |

Run 1 — solusi: Rotasi 180° terhadap (0,0) memetakan (x, y) ke (-x', -y'). Substitusi x = -x' dan y = -y' ke dalam persamaan 3x - 2y + 5 = 0 menghasilkan 3(-x') - 2(-y') + 5 = 0, yang disederhanakan menjadi -3x' + 2y' + 5 = 0.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur transformasi geometri (rotasi 180°) pada persamaan garis. Prosedur ini bersifat rutin dan langsung dalam kurikulum kelas 11.. Bukti: Garis 3x - 2y + 5 = 0 yang ditransformasi oleh rotasi 180° terhadap titik asal (0, 0).
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma transformasi geometri (rotasi) dan substitusi variabel dalam persamaan garis.. Bukti: rotasi 180° terhadap titik asal (0, 0)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan langkah penyelesaian yang jelas dan familiar bagi siswa kelas 11. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Garis 3x - 2y + 5 = 0 yang ditransformasi oleh rotasi 180° terhadap titik asal (0, 0).

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang transformasi geometri (rotasi) dan substitusi aljabar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Transformasi garis dengan rotasi 180 derajat adalah materi standar kelas 11 yang penyelesaiannya mengikuti pola rutin (x,y) -> (-x,-y). |

Run 2 — solusi: Rotasi 180° terhadap (0,0) memetakan (x,y) ke (-x,-y). Maka x = -x' dan y = -y'. Substitusi ke 3x - 2y + 5 = 0 menghasilkan 3(-x') - 2(-y') + 5 = 0, atau -3x' + 2y' + 5 = 0.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur transformasi geometri (rotasi 180°) pada persamaan garis. Ini adalah penerapan prosedur standar yang familiar dalam kurikulum kelas 11.. Bukti: Garis 3x - 2y + 5 = 0 yang ditransformasi oleh rotasi 180° terhadap titik asal (0, 0).
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma transformasi titik dan substitusi variabel ke dalam persamaan garis.. Bukti: Garis 3x - 2y + 5 = 0 yang ditransformasi oleh rotasi 180° terhadap titik asal (0, 0).
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang jelas. Siswa hanya perlu menerapkan aturan rotasi 180 derajat dan melakukan substitusi aljabar sederhana.. Bukti: Garis 3x - 2y + 5 = 0 yang ditransformasi oleh rotasi 180° terhadap titik asal (0, 0).

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang transformasi geometri (rotasi) dan substitusi variabel pada persamaan linear. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Rotasi 180 derajat adalah transformasi dasar yang dipelajari di tingkat SMA. Tidak ada kendala yang saling berinteraksi atau kebutuhan untuk perencanaan strategi yang kompleks. |

Run 3 — solusi: Rotasi 180° terhadap (0,0) memetakan (x, y) ke (-x, -y). Substitusi x = -x' dan y = -y' ke dalam persamaan 3x - 2y + 5 = 0 menghasilkan 3(-x') - 2(-y') + 5 = 0, yang disederhanakan menjadi -3x' + 2y' + 5 = 0.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus transformasi rotasi 180 derajat dan melakukan substitusi variabel ke dalam persamaan garis. Ini adalah penerapan prosedur standar dalam transformasi geometri.. Bukti: Garis 3x - 2y + 5 = 0 yang ditransformasi oleh rotasi 180° terhadap titik asal (0, 0).
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang prosedur transformasi geometri (rotasi) dan bagaimana menerapkannya pada persamaan linear.. Bukti: rotasi 180° terhadap titik asal (0, 0)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 11. Prosedur rotasi 180 derajat adalah konsep dasar transformasi. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Garis 3x - 2y + 5 = 0 yang ditransformasi oleh rotasi 180° terhadap titik asal (0, 0).

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang transformasi geometri (rotasi) dan substitusi variabel pada persamaan linear. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan langsung dari rumus rotasi 180 derajat yang sudah dipelajari di kelas 11. Tidak ada kerumitan tambahan. |

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
Subtopik: Transformasi pada Bidang Kartesius
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan peta dari transformasi geometri berikut.

Garis $3x - 2y + 5 = 0$ yang ditransformasi oleh rotasi 180° terhadap titik asal (0, 0).
Pilihan: A. 3x – 2y – 5 = 0
B. –3x + 2y + 5 = 0
C. 3x – 2y + 5 = 0
D. –3x – 2y + 5 = 0
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 43. Soal `60c388fd31d10f59a7ac5fe0`

Tentukan peta dari transformasi geometri berikut.<br><br>Segitiga ABC dengan A(1, 2), B(3, –1), dan C(–2, –3) yang ditranslasikan oleh vektor $\begin{pmatrix} -5 \\ 3 \end{pmatrix}$.

| Opsi | Isi |
|---|---|
| A | A'(4, –3), B'(6, –6), C'(1, –8) |
| B | A'(6, –1), B'(8, –4), C'(3, –6) |
| C | A'(–4, 2), B'(–2, –1), C'(–7, –3) |
| D | A'(–4, 5), B'(–2, 2), C'(–7, 0) |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Translasi titik (x, y) oleh vektor (a, b) menghasilkan (x+a, y+b). Untuk A(1, 2) + (-5, 3) = (-4, 5). Untuk B(3, -1) + (-5, 3) = (-2, 2). Untuk C(-2, -3) + (-5, 3) = (-7, 0). Hasilnya adalah A'(-4, 5), B'(-2, 2), C'(-7, 0).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8b60243a4a8d7bcbde52c64bdd16f90e08472d5902227c27dda2b6998d83ccd8`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2802 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2850 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2825 |

Run 1 — solusi: Translasi titik (x, y) oleh vektor (a, b) menghasilkan (x+a, y+b). Untuk A(1, 2) + (-5, 3) = (-4, 5). Untuk B(3, -1) + (-5, 3) = (-2, 2). Untuk C(-2, -3) + (-5, 3) = (-7, 0). Hasilnya adalah A'(-4, 5), B'(-2, 2), C'(-7, 0).
- Domain kognitif `classify/knowing`: Soal meminta penerapan langsung definisi translasi pada titik-titik koordinat. Siswa hanya perlu melakukan operasi penjumlahan vektor sederhana pada setiap titik.. Bukti: Segitiga ABC dengan A(1, 2), B(3, –1), dan C(–2, –3) yang ditranslasikan oleh vektor (–5, 3)
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang bagaimana translasi bekerja pada koordinat kartesius.. Bukti: ditranslasikan oleh vektor
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Tidak ada integrasi konsep yang kompleks atau kendala yang saling berinteraksi. Siswa hanya perlu menerapkan rumus translasi dasar.. Bukti: Segitiga ABC dengan A(1, 2), B(3, –1), dan C(–2, –3) yang ditranslasikan oleh vektor (–5, 3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi penjumlahan bilangan bulat dan konsep dasar koordinat kartesius. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi translasi adalah dasar transformasi geometri yang sudah dipelajari dan merupakan prosedur standar yang sangat familiar bagi siswa kelas 11. |

Run 2 — solusi: Translasi titik (x, y) oleh vektor (a, b) menghasilkan (x+a, y+b). Untuk A(1, 2), B(3, -1), C(-2, -3) dengan vektor (-5, 3): A'(1-5, 2+3) = A'(-4, 5); B'(3-5, -1+3) = B'(-2, 2); C'(-2-5, -3+3) = C'(-7, 0). Hasil sesuai dengan opsi D.
- Domain kognitif `classify/knowing`: Soal meminta penerapan langsung definisi translasi pada titik-titik koordinat. Siswa hanya perlu melakukan operasi penjumlahan vektor pada setiap titik, yang merupakan prosedur standar dan langsung.. Bukti: Segitiga ABC dengan A(1, 2), B(3, –1), dan C(–2, –3) yang ditranslasikan oleh vektor (–5, 3)
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang bagaimana vektor translasi memengaruhi koordinat titik pada bidang Kartesius.. Bukti: ditranslasikan oleh vektor
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Tidak ada integrasi konsep yang kompleks atau kendala yang berinteraksi. Siswa hanya perlu menerapkan rumus translasi (x', y') = (x+a, y+b) secara berulang untuk tiga titik.. Bukti: Segitiga ABC dengan A(1, 2), B(3, –1), dan C(–2, –3) yang ditranslasikan oleh vektor (–5, 3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi penjumlahan bilangan bulat dan konsep dasar koordinat Kartesius. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi translasi adalah dasar transformasi geometri di kelas 11. Soal ini tidak menuntut pemahaman mendalam tentang komposisi transformasi atau matriks, sehingga tergolong mudah bagi siswa kelas 11. |

Run 3 — solusi: Translasi titik (x, y) oleh vektor (a, b) menghasilkan (x+a, y+b). Untuk A(1, 2), B(3, -1), C(-2, -3) dengan vektor (-5, 3): A'(1-5, 2+3) = A'(-4, 5); B'(3-5, -1+3) = B'(-2, 2); C'(-2-5, -3+3) = C'(-7, 0). Hasilnya sesuai dengan opsi D.
- Domain kognitif `classify/knowing`: Siswa diminta menerapkan prosedur translasi titik secara langsung menggunakan vektor yang diberikan. Tidak ada langkah penalaran kompleks atau integrasi konsep yang diperlukan.. Bukti: Segitiga ABC dengan A(1, 2), B(3, –1), dan C(–2, –3) yang ditranslasikan oleh vektor (–5, 3)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi penjumlahan vektor pada koordinat titik.. Bukti: ditranslasikan oleh vektor
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu melakukan operasi penjumlahan sederhana pada koordinat titik. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi.. Bukti: Segitiga ABC dengan A(1, 2), B(3, –1), dan C(–2, –3) yang ditranslasikan oleh vektor (–5, 3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan bulat dan konsep dasar koordinat Kartesius. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi translasi adalah dasar transformasi geometri yang sudah dipelajari di jenjang sebelumnya dan diperdalam di kelas 11. Soal ini tidak menuntut pemahaman mendalam atau integrasi konsep, sehingga tergolong mudah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
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
Subtopik: Transformasi pada Bidang Kartesius
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan peta dari transformasi geometri berikut.

Segitiga ABC dengan A(1, 2), B(3, –1), dan C(–2, –3) yang ditranslasikan oleh vektor $\begin{pmatrix} -5 \\ 3 \end{pmatrix}$.
Pilihan: A. A'(4, –3), B'(6, –6), C'(1, –8)
B. A'(6, –1), B'(8, –4), C'(3, –6)
C. A'(–4, 2), B'(–2, –1), C'(–7, –3)
D. A'(–4, 5), B'(–2, 2), C'(–7, 0)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 44. Soal `59ae6ca462ec00892f967ec5`

Tentukan peta dari beberapa operasi transformasi berikut.<br><br>Garis $x - 2y + 3 = 0$ yang ditransformasikan oleh $\begin{bmatrix} 3 & 0 \\ 0 & 3 \end{bmatrix}$.

| Opsi | Isi |
|---|---|
| A | 3x – 2y + 3 = 0 |
| B | x – 2y + 1 = 0 |
| C | x – 2y + 9 = 0 |
| D | x – 2y + 27 = 0 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Matriks transformasi [3 0; 0 3] berarti x' = 3x dan y' = 3y, sehingga x = x'/3 dan y = y'/3. Substitusi ke persamaan garis x - 2y + 3 = 0 menghasilkan (x'/3) - 2(y'/3) + 3 = 0. Kalikan kedua ruas dengan 3 diperoleh x' - 2y' + 9 = 0.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6896db3ce05e5cc4322e7c29bfda2025594ae423b34a9cb80fa81a580fcaeabc`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3363 |
| 2 | success | valid / verified | applying | procedural | Easy | 3467 |
| 3 | success | valid / verified | applying | procedural | Easy | 2685 |

Run 1 — solusi: Matriks transformasi [3 0; 0 3] berarti x' = 3x dan y' = 3y, sehingga x = x'/3 dan y = y'/3. Substitusi ke persamaan garis x - 2y + 3 = 0 menghasilkan (x'/3) - 2(y'/3) + 3 = 0. Kalikan kedua ruas dengan 3 diperoleh x' - 2y' + 9 = 0.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur transformasi matriks standar untuk mencari bayangan garis. Ini adalah penerapan langsung dari konsep dilatasi matriks.. Bukti: Garis x - 2y + 3 = 0 yang ditransformasikan oleh [3 0; 0 3]
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana matriks transformasi bekerja pada persamaan linear.. Bukti: ditransformasikan oleh [3 0; 0 3]
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 11. Langkah-langkah penyelesaiannya jelas dan langsung, tidak memerlukan perencanaan strategi yang kompleks atau integrasi kendala yang sulit.. Bukti: Garis x - 2y + 3 = 0 yang ditransformasikan oleh [3 0; 0 3]

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang matriks dilatasi dan substitusi variabel pada persamaan linear. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal standar transformasi geometri menggunakan matriks yang sesuai dengan kurikulum kelas 11 TL. |

Run 2 — solusi: Matriks transformasi [3 0; 0 3] adalah dilatasi dengan faktor skala 3, sehingga x' = 3x dan y' = 3y, atau x = x'/3 dan y = y'/3. Substitusi ke persamaan garis x - 2y + 3 = 0 menghasilkan (x'/3) - 2(y'/3) + 3 = 0. Mengalikan seluruh persamaan dengan 3 memberikan x' - 2y' + 9 = 0.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep transformasi matriks (dilatasi) pada persamaan garis. Prosedur substitusi variabel adalah standar untuk kelas 11.. Bukti: Garis x - 2y + 3 = 0 yang ditransformasikan oleh [3 0; 0 3]
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma transformasi matriks untuk mengubah persamaan garis.. Bukti: Garis x - 2y + 3 = 0 yang ditransformasikan oleh [3 0; 0 3]
- Intended difficulty `classify/Easy`: Soal ini adalah penerapan langsung dari dilatasi matriks 2x2. Langkah-langkahnya rutin dan tidak melibatkan kendala yang kompleks atau integrasi konsep yang tinggi.. Bukti: Garis x - 2y + 3 = 0 yang ditransformasikan oleh [3 0; 0 3]

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dilatasi matriks dan substitusi variabel. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah penerapan langsung dari dilatasi matriks 2x2. Langkah-langkahnya rutin dan tidak melibatkan kendala yang kompleks atau integrasi konsep yang tinggi. |

Run 3 — solusi: Transformasi dilatasi dengan matriks [3 0; 0 3] berarti x' = 3x dan y' = 3y, sehingga x = x'/3 dan y = y'/3. Substitusi ke garis x - 2y + 3 = 0 menghasilkan (x'/3) - 2(y'/3) + 3 = 0. Kalikan kedua ruas dengan 3 diperoleh x' - 2y' + 9 = 0.
- Domain kognitif `classify/applying`: Siswa perlu memahami hubungan antara matriks transformasi (dilatasi) dan perubahan koordinat pada persamaan garis. Ini melibatkan penerapan prosedur substitusi variabel yang familiar.. Bukti: Garis x - 2y + 3 = 0 yang ditransformasikan oleh [3 0; 0 3]
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang bagaimana matriks transformasi memetakan titik-titik pada garis dan bagaimana melakukan substitusi balik untuk mendapatkan persamaan bayangan.. Bukti: ditransformasikan oleh [3 0; 0 3]
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 11. Prosedur dilatasi dengan matriks diagonal adalah konsep dasar transformasi geometri. Langkah-langkahnya jelas (invers matriks atau substitusi langsung) dan tidak memerlukan integrasi konsep yang kompleks.. Bukti: Garis x - 2y + 3 = 0 yang ditransformasikan oleh [3 0; 0 3]

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang matriks transformasi dan substitusi variabel pada persamaan linear. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi transformasi geometri dengan matriks merupakan kurikulum standar kelas 11. Soal ini adalah penerapan langsung dari definisi dilatasi. |

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
Subtopik: Kaitan Matriks dengan Transformasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan peta dari beberapa operasi transformasi berikut.

Garis $x - 2y + 3 = 0$ yang ditransformasikan oleh $\begin{bmatrix} 3 & 0 \\ 0 & 3 \end{bmatrix}$.
Pilihan: A. 3x – 2y + 3 = 0
B. x – 2y + 1 = 0
C. x – 2y + 9 = 0
D. x – 2y + 27 = 0
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 45. Soal `9dc821c78e2e886c3a7f6c15`

Tentukan peta dari beberapa operasi transformasi berikut.<br><br>Titik (3, 7) yang ditransformasikan dengan matriks $\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$.

| Opsi | Isi |
|---|---|
| A | (–3, –7) |
| B | (–7, 3) |
| C | (7, –3) |
| D | (7, 3) |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Perkalian matriks transformasi dengan vektor posisi titik: [0 -1; 1 0] * [3; 7] = [0*3 + (-1)*7; 1*3 + 0*7] = [-7; 3]. Jadi, peta titik adalah (-7, 3).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `23ba68f692162bf6a8c1f61f78490ecbdf74eb7502e70449350205c6a7e64ce7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2751 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2750 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2747 |

Run 1 — solusi: Perkalian matriks transformasi dengan vektor posisi titik: [0 -1; 1 0] * [3; 7] = [0*3 + (-1)*7; 1*3 + 0*7] = [-7; 3]. Jadi, peta titik adalah (-7, 3).
- Domain kognitif `classify/knowing`: Soal meminta penerapan langsung prosedur perkalian matriks untuk transformasi titik. Siswa hanya perlu melakukan operasi perkalian matriks-vektor standar tanpa perlu merancang strategi atau mengintegrasikan konsep yang kompleks.. Bukti: Titik (3, 7) yang ditransformasikan dengan matriks [0 -1; 1 0]
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang bagaimana matriks transformasi bekerja pada koordinat titik.. Bukti: ditransformasikan dengan matriks [0 -1; 1 0]
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Tidak ada langkah perencanaan yang kompleks atau kendala yang berinteraksi. Siswa hanya perlu melakukan satu operasi perkalian matriks 2x2 dengan vektor kolom.. Bukti: Titik (3, 7) yang ditransformasikan dengan matriks [0 -1; 1 0]

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi perkalian matriks dan konsep koordinat kartesius. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, perkalian matriks transformasi adalah materi dasar. Soal ini tidak memerlukan pemahaman mendalam tentang sifat transformasi, hanya eksekusi prosedur. |

Run 2 — solusi: Perkalian matriks transformasi dengan vektor posisi titik: [0 -1; 1 0] * [3; 7] = [0*3 + (-1)*7; 1*3 + 0*7] = [-7; 3]. Jadi, peta titik adalah (-7, 3).
- Domain kognitif `classify/knowing`: Soal meminta penerapan langsung prosedur perkalian matriks untuk transformasi titik. Siswa hanya perlu melakukan operasi perkalian matriks-vektor standar yang merupakan prosedur rutin dalam materi transformasi geometri.. Bukti: Titik (3, 7) yang ditransformasikan dengan matriks [0 -1; 1 0]
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang bagaimana matriks 2x2 mentransformasikan koordinat titik dalam bidang kartesius.. Bukti: matriks [0 -1; 1 0]
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (straightforward). Tidak ada langkah perencanaan yang kompleks atau integrasi konsep yang menuntut. Siswa hanya perlu melakukan satu operasi perkalian matriks 2x2 dengan vektor kolom.. Bukti: Titik (3, 7) yang ditransformasikan dengan matriks [0 -1; 1 0]

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi perkalian matriks dan representasi titik sebagai vektor kolom. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal dasar transformasi geometri yang sesuai untuk kelas 11. Tidak ada kerumitan tambahan seperti komposisi transformasi atau pencarian matriks invers. |

Run 3 — solusi: Perkalian matriks transformasi dengan titik: [0 -1; 1 0] * [3; 7] = [0*3 + (-1)*7; 1*3 + 0*7] = [-7; 3]. Hasilnya adalah (-7, 3).
- Domain kognitif `classify/knowing`: Siswa hanya perlu menerapkan prosedur perkalian matriks dengan vektor kolom secara langsung untuk mendapatkan peta titik. Tidak ada strategi nonrutin atau integrasi konsep yang kompleks.. Bukti: Titik (3, 7) yang ditransformasikan dengan matriks [0 -1; 1 0]
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana matriks transformasi bekerja pada titik koordinat.. Bukti: matriks [0 -1; 1 0]
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu melakukan satu operasi perkalian matriks 2x2 dengan vektor 2x1. Tidak ada langkah tambahan, tidak ada komposisi transformasi, dan tidak ada kendala yang perlu dipertimbangkan.. Bukti: Titik (3, 7) yang ditransformasikan dengan matriks [0 -1; 1 0]

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian matriks dan konsep transformasi geometri dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, operasi perkalian matriks dasar adalah materi yang sangat rutin dan mendasar. Soal ini tidak menuntut pemahaman mendalam tentang sifat transformasi, hanya eksekusi prosedur. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
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
Subtopik: Kaitan Matriks dengan Transformasi
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan peta dari beberapa operasi transformasi berikut.

Titik (3, 7) yang ditransformasikan dengan matriks $\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$.
Pilihan: A. (–3, –7)
B. (–7, 3)
C. (7, –3)
D. (7, 3)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 46. Soal `74a75b2e70f71b85b00e52be`

Carilah matriks yang berkaitan dengan pencerminan terhadap sumbu-y dilanjutkan dengan rotasi 180° terhadap titik pusat.

| Opsi | Isi |
|---|---|
| A | $\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$ |
| B | $\begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}$ |
| C | $\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$ |
| D | $\begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix}$ |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Matriks pencerminan terhadap sumbu-y adalah M1 = [[-1, 0], [0, 1]]. Matriks rotasi 180 derajat terhadap pusat (0,0) adalah M2 = [[-1, 0], [0, -1]]. Komposisi transformasi (M2 * M1) = [[-1, 0], [0, -1]] * [[-1, 0], [0, 1]] = [[1, 0], [0, -1]].
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7bb467cf37dc4eccfaff73c43d676c05174168cf680c823ad6fcfa60719dc4b4`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2876 |
| 2 | success | valid / verified | applying | procedural | Easy | 2866 |
| 3 | success | valid / verified | applying | procedural | Medium | 2886 |

Run 1 — solusi: Matriks pencerminan terhadap sumbu-y adalah M1 = [[-1, 0], [0, 1]]. Matriks rotasi 180 derajat terhadap pusat (0,0) adalah M2 = [[-1, 0], [0, -1]]. Komposisi transformasi (M2 * M1) = [[-1, 0], [0, -1]] * [[-1, 0], [0, 1]] = [[1, 0], [0, -1]].
- Domain kognitif `classify/applying`: Siswa perlu mengingat matriks transformasi dasar (pencerminan dan rotasi) dan menerapkan prosedur perkalian matriks untuk komposisi transformasi. Ini adalah penerapan prosedur standar dalam konteks rutin.. Bukti: Carilah matriks yang berkaitan dengan pencerminan terhadap sumbu-y dilanjutkan dengan rotasi 180° terhadap titik pusat.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritme perkalian matriks untuk komposisi transformasi geometri, yang merupakan pengetahuan prosedural.. Bukti: pencerminan terhadap sumbu-y; rotasi 180° terhadap titik pusat; matriks yang berkaitan dengan pencerminan... dilanjutkan dengan rotasi
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemahaman tentang urutan komposisi transformasi (perkalian matriks tidak komutatif) dan pengingatan matriks transformasi dasar. Meskipun prosedurnya rutin, siswa harus berhati-hati dengan urutan perkalian matriks (M2 * M1) dan tanda pada matriks transformasi.. Bukti: Carilah matriks yang berkaitan dengan pencerminan terhadap sumbu-y dilanjutkan dengan rotasi 180° terhadap titik pusat.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengetahuan tentang matriks transformasi dasar (refleksi dan rotasi) dan operasi perkalian matriks. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan mampu melakukan komposisi transformasi dengan matriks. Soal ini menuntut ketelitian dalam urutan perkalian matriks, yang merupakan tantangan standar pada tingkat ini. |

Run 2 — solusi: Matriks pencerminan terhadap sumbu-y adalah M1 = [[-1, 0], [0, 1]]. Matriks rotasi 180 derajat terhadap pusat (0,0) adalah M2 = [[-1, 0], [0, -1]]. Komposisi transformasi (M2 * M1) = [[-1, 0], [0, -1]] * [[-1, 0], [0, 1]] = [[1, 0], [0, -1]].
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi matriks standar untuk dua transformasi geometri yang berbeda dan melakukan perkalian matriks untuk mendapatkan komposisinya. Ini adalah penerapan prosedur standar yang telah dipelajari di kelas 11.. Bukti: pencerminan terhadap sumbu-y dilanjutkan dengan rotasi 180°; Carilah matriks yang berkaitan dengan
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang representasi matriks dari transformasi geometri dan aturan komposisi transformasi (perkalian matriks).. Bukti: pencerminan terhadap sumbu-y; rotasi 180° terhadap titik pusat; matriks yang berkaitan dengan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 11. Siswa hanya perlu mengingat atau menurunkan matriks transformasi dasar dan melakukan satu operasi perkalian matriks. Tidak ada kendala yang saling berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: pencerminan terhadap sumbu-y dilanjutkan dengan rotasi 180°

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang matriks transformasi dasar (refleksi dan rotasi) dan perkalian matriks. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi transformasi geometri dengan matriks adalah kurikulum standar kelas 11. Soal ini langsung menanyakan komposisi tanpa variasi yang kompleks, sehingga tergolong mudah. |

Run 3 — solusi: Matriks pencerminan terhadap sumbu-y adalah M1 = [[-1, 0], [0, 1]]. Matriks rotasi 180 derajat terhadap pusat (0,0) adalah M2 = [[-1, 0], [0, -1]]. Komposisi transformasi (M2 * M1) = [[-1, 0], [0, -1]] * [[-1, 0], [0, 1]] = [[1, 0], [0, -1]].
- Domain kognitif `classify/applying`: Siswa perlu mengingat atau menurunkan matriks transformasi dasar (pencerminan dan rotasi) dan menerapkan prosedur perkalian matriks untuk komposisi transformasi. Ini adalah penerapan prosedur rutin pada konteks yang jelas.. Bukti: Carilah matriks yang berkaitan dengan pencerminan terhadap sumbu-y dilanjutkan dengan rotasi 180° terhadap titik pusat.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana matriks transformasi dikalikan untuk membentuk komposisi transformasi.. Bukti: pencerminan terhadap sumbu-y; rotasi 180° terhadap titik pusat; matriks yang berkaitan
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua langkah transformasi yang harus dikomposisikan dengan urutan yang benar (M2 * M1). Meskipun prosedurnya rutin, siswa harus berhati-hati dengan urutan perkalian matriks dan definisi matriks transformasi dasar, yang merupakan tuntutan standar untuk kelas 11.. Bukti: pencerminan terhadap sumbu-y dilanjutkan dengan rotasi 180°; Carilah matriks yang berkaitan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman matriks transformasi dasar (refleksi dan rotasi) dan perkalian matriks. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 diharapkan mampu melakukan komposisi transformasi matriks. Soal ini menuntut ketelitian dalam urutan perkalian matriks, namun prosedurnya bersifat rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4732`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengingat matriks transformasi dasar (refleksi dan rotasi) dan menerapkan prosedur perkalian matriks untuk komposisi transformasi. Ini adalah penerapan prosedur standar dalam konteks rutin.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang algoritme perkalian matriks untuk komposisi transformasi geometri, yang merupakan pengetahuan prosedural.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena memerlukan pemahaman tentang urutan komposisi transformasi (perkalian matriks tidak komutatif) dan pengingatan matriks transformasi dasar. Meskipun prosedurnya rutin, siswa harus berhati-hati dengan urutan perkalian matriks (M2 * M1) dan tanda pada matriks transformasi.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengetahuan tentang matriks transformasi dasar (refleksi dan rotasi) dan operasi perkalian matriks. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan mampu melakukan komposisi transformasi dengan matriks. Soal ini menuntut ketelitian dalam urutan perkalian matriks, yang merupakan tantangan standar pada tingkat ini. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Komposisi Transformasi dengan Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Carilah matriks yang berkaitan dengan pencerminan terhadap sumbu-y dilanjutkan dengan rotasi 180° terhadap titik pusat.
Pilihan: A. $\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$
B. $\begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}$
C. $\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$
D. $\begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 47. Soal `30b59bdcb957a0b0e60092e7`

Misalkan $T_1$ menyatakan operasi pencerminan terhadap sumbu-$x$ dan $T_2$ menyatakan operasi pencerminan terhadap sumbu-$y$. a. Transformasi tunggal apakah yang ekuivalen dengan $T_2$ ◦ $T_1$?<br><br>Apa peta dari P(a, b) dari transformasi tersebut?

| Opsi | Isi |
|---|---|
| A | P'(–a, b) |
| B | P'(–a, –b) |
| C | P'(a, –b) |
| D | P'(b, a) |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: T1(a, b) = (a, -b). T2(a, -b) = (-a, -b). Komposisi T2 ∘ T1 memetakan (a, b) ke (-a, -b), yang ekuivalen dengan rotasi 180 derajat terhadap titik asal (0,0).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9afe415044c9b4d7430f53a6f12e0903ba968debdaf42c10617dc4bab334255c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3695 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3727 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3495 |

Run 1 — solusi: T1(a,b) = (a,-b). T2(a,-b) = (-a,-b). Transformasi ekuivalen adalah rotasi 180 derajat terhadap titik asal (0,0) atau pencerminan terhadap titik asal.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan komposisi dua transformasi geometri dasar secara berurutan untuk menemukan transformasi tunggal yang setara.. Bukti: T1 menyatakan operasi pencerminan terhadap sumbu-x; T2 menyatakan operasi pencerminan terhadap sumbu-y; Transformasi tunggal apakah yang ekuivalen dengan T2 ◦ T1?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan prosedur komposisi matriks transformasi atau penerapan berurutan dari aturan pencerminan.. Bukti: T2 ◦ T1; peta dari P(a, b)
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman tentang urutan komposisi transformasi (T2 setelah T1) dan penerapan dua langkah transformasi. Meskipun prosedurnya standar, siswa harus berhati-hati dengan urutan komposisi dan interpretasi geometrisnya.. Bukti: T2 ◦ T1; peta dari P(a, b)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang matriks transformasi refleksi dan komposisi fungsi/transformasi. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, komposisi transformasi adalah materi standar. Soal ini menguji pemahaman urutan komposisi yang sering menjadi jebakan, namun langkah penyelesaiannya cukup langsung. |

Run 2 — solusi: T1(a,b) = (a,-b). T2(a,-b) = (-a,-b). Komposisi T2 o T1 memetakan P(a,b) ke P'(-a,-b), yang ekuivalen dengan rotasi 180 derajat terhadap titik asal.
- Domain kognitif `classify/applying`: Siswa perlu memahami definisi matriks transformasi dasar dan melakukan komposisi dua transformasi secara berurutan untuk menentukan hasil akhirnya.. Bukti: T1 menyatakan operasi pencerminan terhadap sumbu-x; T2 menyatakan operasi pencerminan terhadap sumbu-y; Transformasi tunggal apakah yang ekuivalen dengan T2 ◦ T1?
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman konseptual tentang bagaimana transformasi geometri direpresentasikan oleh matriks dan bagaimana komposisi transformasi bekerja.. Bukti: T1 menyatakan operasi pencerminan terhadap sumbu-x; T2 menyatakan operasi pencerminan terhadap sumbu-y
- Intended difficulty `classify/Easy`: Soal ini meminta siswa melakukan komposisi dua transformasi dasar. Langkah-langkahnya jelas dan prosedural, tidak memerlukan strategi non-rutin yang kompleks.. Bukti: Transformasi tunggal apakah yang ekuivalen dengan T2 ◦ T1?; Apa peta dari P(a, b) dari transformasi tersebut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang matriks transformasi refleksi. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi transformasi geometri dengan matriks adalah standar kelas 11. Soal ini adalah aplikasi langsung dari definisi refleksi. |

Run 3 — solusi: T1(a, b) = (a, -b). T2(a, -b) = (-a, -b). Komposisi T2 ∘ T1 memetakan (a, b) ke (-a, -b), yang ekuivalen dengan rotasi 180 derajat terhadap titik asal.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur transformasi dasar secara berurutan untuk menentukan hasil komposisi. Ini adalah penerapan konsep transformasi yang rutin.. Bukti: T1 menyatakan operasi pencerminan terhadap sumbu-x; T2 menyatakan operasi pencerminan terhadap sumbu-y; Transformasi tunggal apakah yang ekuivalen dengan T2 ◦ T1?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang sifat refleksi dan bagaimana komposisi dua refleksi menghasilkan transformasi lain (rotasi).. Bukti: T1 menyatakan operasi pencerminan terhadap sumbu-x; T2 menyatakan operasi pencerminan terhadap sumbu-y
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 11. Langkah penyelesaiannya jelas (dua langkah berurutan) tanpa kendala yang saling berinteraksi atau tuntutan perencanaan yang tinggi.. Bukti: T1 menyatakan operasi pencerminan terhadap sumbu-x; T2 menyatakan operasi pencerminan terhadap sumbu-y; Transformasi tunggal apakah yang ekuivalen dengan T2 ◦ T1?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang refleksi pada bidang kartesius. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL sudah familiar dengan transformasi geometri. Soal ini adalah latihan standar komposisi dua transformasi sederhana. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 1, "Easy": 2} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4310`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur transformasi dasar secara berurutan untuk menentukan hasil komposisi. Ini adalah penerapan konsep transformasi yang rutin.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman konseptual tentang sifat refleksi dan bagaimana komposisi dua refleksi menghasilkan transformasi lain (rotasi).
- Intended difficulty `Easy`: Soal ini bersifat rutin bagi siswa kelas 11. Langkah penyelesaiannya jelas (dua langkah berurutan) tanpa kendala yang saling berinteraksi atau tuntutan perencanaan yang tinggi.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang refleksi pada bidang kartesius. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL sudah familiar dengan transformasi geometri. Soal ini adalah latihan standar komposisi dua transformasi sederhana. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Komposisi Transformasi dengan Matriks
Tipe soal: multiple_choice
Stimulus: -
Soal: Misalkan $T_1$ menyatakan operasi pencerminan terhadap sumbu-$x$ dan $T_2$ menyatakan operasi pencerminan terhadap sumbu-$y$. a. Transformasi tunggal apakah yang ekuivalen dengan $T_2$ ◦ $T_1$?

Apa peta dari P(a, b) dari transformasi tersebut?
Pilihan: A. P'(–a, b)
B. P'(–a, –b)
C. P'(a, –b)
D. P'(b, a)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 48. Soal `d1ea45dd56b16f419ac0af6a`

Karena pengaruh gravitasi, molekul udara lebih banyak berada di permukaan bumi daripada di tempat tinggi. Akibatnya, tekanan udara akan terus berkurang seiring makin tingginya suatu tempat. Hubungan antara tekanan udara P (dalam kPa) dan ketinggian h (dalam km) dapat dimodelkan sebagai berikut.<br>$\ln\left(\frac{P}{100}\right) = -\frac{h}{7}$<br><br>Puncak Jayawijaya memiliki ketinggian 4.884 m di atas permukaan laut. Dengan rumus tersebut, prediksilah tekanan udara di daerah tersebut.

| Opsi | Isi |
|---|---|
| A | sekitar 69,77 kPa |
| B | sekitar 49,77 kPa |
| C | sekitar 30,23 kPa |
| D | sekitar 200,91 kPa |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Diketahui ln(P/100) = -h/7. Dengan h = 4,884 km, maka ln(P/100) = -4,884/7 = -0,6977. Mengubah ke bentuk eksponen: P/100 = e^(-0,6977). Maka P = 100 * e^(-0,6977) ≈ 100 * 0,4977 = 49,77 kPa.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['membandingkan', 'menganalisis']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5b2e3fd11787d03855b79f0dc1dfb9ed8fb51d5eda9afb5c9d77ba4462b88548`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2886 |
| 2 | success | valid / verified | applying | procedural | Easy | 2934 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2898 |

Run 1 — solusi: Diketahui ln(P/100) = -h/7. Dengan h = 4,884 km, maka ln(P/100) = -4,884/7 = -0,6977. Menggunakan definisi logaritma natural, P/100 = e^(-0,6977). Maka P = 100 * e^(-0,6977) ≈ 100 * 0,4977 = 49,77 kPa.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur logaritma natural dan eksponen untuk menyelesaikan variabel P. Ini adalah penerapan konsep fungsi logaritma dalam konteks pemodelan.. Bukti: Hubungan antara tekanan udara P (dalam kPa) dan ketinggian h (dalam km) dapat dimodelkan sebagai berikut. \ln\left(\frac{P}{100}\right) = -\frac{h}{7}
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara fungsi logaritma dan eksponen serta penggunaan rumus yang diberikan.. Bukti: \ln\left(\frac{P}{100}\right) = -\frac{h}{7}
- Intended difficulty `classify/Easy`: Soal ini memerlukan konversi satuan (m ke km) dan manipulasi aljabar sederhana untuk mengisolasi variabel P. Langkah-langkahnya rutin dan jelas bagi siswa kelas 11.. Bukti: Puncak Jayawijaya memiliki ketinggian 4.884 m di atas permukaan laut.; \ln\left(\frac{P}{100}\right) = -\frac{h}{7}

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi logaritma dan eksponen, serta konversi satuan panjang. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi logaritma adalah bagian dari kurikulum kelas 11. Soal ini merupakan aplikasi langsung dari model yang diberikan tanpa memerlukan perencanaan strategi yang kompleks. |

Run 2 — solusi: Diketahui ln(P/100) = -h/7. Dengan h = 4,884 km, maka ln(P/100) = -4,884/7 = -0,6977. Mengubah ke bentuk eksponen: P/100 = e^(-0,6977). Maka P = 100 * e^(-0,6977) ≈ 100 * 0,4977 = 49,77 kPa.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur logaritma dan eksponen untuk menyelesaikan variabel P dalam model yang diberikan. Ini melibatkan manipulasi aljabar dasar dari fungsi logaritma ke eksponensial.. Bukti: Hubungan antara tekanan udara P (dalam kPa) dan ketinggian h (dalam km) dapat dimodelkan sebagai berikut. ln(P/100) = -h/7; Puncak Jayawijaya memiliki ketinggian 4.884 m di atas permukaan laut. Dengan rumus tersebut, prediksilah tekanan udara di daerah tersebut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana mengubah bentuk logaritma natural menjadi bentuk eksponensial untuk menyelesaikan variabel yang tidak diketahui.. Bukti: ln(P/100) = -h/7
- Intended difficulty `classify/Easy`: Soal ini dikategorikan Easy karena siswa hanya perlu melakukan substitusi nilai h ke dalam rumus yang sudah diberikan dan melakukan konversi logaritma ke eksponen yang merupakan prosedur standar. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: ln(P/100) = -h/7; Puncak Jayawijaya memiliki ketinggian 4.884 m di atas permukaan laut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi logaritma dan eksponen, serta konversi satuan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, penggunaan model logaritma-eksponen adalah materi standar. Prosedur penyelesaian bersifat langsung dan rutin. |

Run 3 — solusi: Diketahui ln(P/100) = -h/7. Dengan h = 4,884 km, maka ln(P/100) = -4,884/7 = -0,6977. Menggunakan definisi logaritma natural, P/100 = e^(-0,6977). Maka P = 100 * e^(-0,6977) ≈ 100 * 0,4977 = 49,77 kPa.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur logaritma dan eksponen untuk menyelesaikan variabel P dari model yang diberikan. Ini adalah penerapan konsep fungsi logaritma dalam konteks pemodelan.. Bukti: Hubungan antara tekanan udara P (dalam kPa) dan ketinggian h (dalam km) dapat dimodelkan sebagai berikut. \ln\left(\frac{P}{100}\right) = -\frac{h}{7}
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman tentang hubungan antara fungsi logaritma natural dan fungsi eksponensial sebagai inversnya, yang merupakan pengetahuan konseptual.. Bukti: \ln\left(\frac{P}{100}\right) = -\frac{h}{7}
- Intended difficulty `classify/Easy`: Soal ini memerlukan konversi satuan (m ke km) dan manipulasi aljabar sederhana untuk mengisolasi variabel P. Langkah-langkahnya rutin dan jelas bagi siswa kelas 11.. Bukti: Puncak Jayawijaya memiliki ketinggian 4.884 m di atas permukaan laut.; \ln\left(\frac{P}{100}\right) = -\frac{h}{7}

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi logaritma dan eksponensial, serta konversi satuan panjang. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan mampu melakukan manipulasi aljabar pada fungsi logaritma dan eksponensial dengan tingkat kesulitan rendah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4736`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur logaritma natural dan eksponen untuk menyelesaikan variabel P dalam model yang diberikan. Ini adalah penerapan konsep fungsi logaritma dalam konteks pemodelan yang rutin.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana mengubah bentuk logaritma natural menjadi bentuk eksponensial untuk menyelesaikan variabel yang tidak diketahui.
- Intended difficulty `Easy`: Soal ini dikategorikan Easy karena siswa hanya perlu melakukan substitusi nilai h ke dalam rumus yang sudah diberikan dan melakukan konversi logaritma ke eksponen yang merupakan prosedur standar. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi logaritma dan eksponen, serta konversi satuan panjang. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, penggunaan model logaritma-eksponen adalah materi standar. Prosedur penyelesaian bersifat langsung dan rutin. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Fungsi Logaritma
Tipe soal: multiple_choice
Stimulus: -
Soal: Karena pengaruh gravitasi, molekul udara lebih banyak berada di permukaan bumi daripada di tempat tinggi. Akibatnya, tekanan udara akan terus berkurang seiring makin tingginya suatu tempat. Hubungan antara tekanan udara P (dalam kPa) dan ketinggian h (dalam km) dapat dimodelkan sebagai berikut.
$\ln\left(\frac{P}{100}\right) = -\frac{h}{7}$

Puncak Jayawijaya memiliki ketinggian 4.884 m di atas permukaan laut. Dengan rumus tersebut, prediksilah tekanan udara di daerah tersebut.
Pilihan: A. sekitar 69,77 kPa
B. sekitar 49,77 kPa
C. sekitar 30,23 kPa
D. sekitar 200,91 kPa
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 49. Soal `1ac6cf9273745ff232bf8bdb`

Jika segelas jus jeruk mempunyai ion hidrogen $10^{-3,15}$, tentukan nilai pH jus jeruk tersebut.

| Opsi | Isi |
|---|---|
| A | -3,15 |
| B | 0,315 |
| C | 3,85 |
| D | 3,15 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: pH = -log[H+] = -log(10^-3,15) = -(-3,15) = 3,15.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7066d35c4ecfae2457c269c3aa70f5fdbf22f318db8e4cd4a73aaae86484c690`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2594 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2601 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2616 |

Run 1 — solusi: pH = -log[H+] = -log(10^-3,15) = -(-3,15) = 3,15.
- Domain kognitif `classify/knowing`: Soal meminta penerapan langsung definisi pH sebagai fungsi logaritma negatif dari konsentrasi ion hidrogen. Siswa hanya perlu mengenali rumus dan melakukan substitusi sederhana.. Bukti: Jika segelas jus jeruk mempunyai ion hidrogen 10^-3,15, tentukan nilai pH jus jeruk tersebut.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang definisi logaritma dan rumus pH sebagai konsep dasar dalam fungsi logaritma.. Bukti: pH = -log[H+]
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menerapkan rumus pH = -log[H+] tanpa langkah perantara yang kompleks atau kendala yang berinteraksi.. Bukti: Jika segelas jus jeruk mempunyai ion hidrogen 10^-3,15, tentukan nilai pH jus jeruk tersebut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar logaritma (log 10^x = x) dan rumus pH. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi logaritma adalah standar kelas 11. Soal ini adalah aplikasi langsung dari definisi logaritma basis 10, sehingga sangat mudah bagi siswa kelas 11. |

Run 2 — solusi: pH = -log[H+] = -log(10^-3,15) = -(-3,15) = 3,15.
- Domain kognitif `classify/knowing`: Siswa hanya perlu menerapkan definisi logaritma dalam konteks pH (pH = -log[H+]) secara langsung. Tidak ada langkah penalaran kompleks atau integrasi konsep yang diperlukan.. Bukti: Jika segelas jus jeruk mempunyai ion hidrogen 10^-3,15, tentukan nilai pH jus jeruk tersebut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dasar tentang penggunaan rumus logaritma untuk menghitung pH, yang merupakan penerapan langsung dari definisi logaritma.. Bukti: pH = -log[H+]
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana. Siswa hanya perlu mensubstitusi nilai ke dalam rumus yang sudah umum diketahui atau diberikan secara implisit. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang diperlukan.. Bukti: Jika segelas jus jeruk mempunyai ion hidrogen 10^-3,15, tentukan nilai pH jus jeruk tersebut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi logaritma dan sifat logaritma dasar (log 10^x = x). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, soal ini adalah aplikasi langsung dari fungsi logaritma yang sangat mendasar dan rutin. |

Run 3 — solusi: pH = -log[H+] = -log(10^-3,15) = -(-3,15) = 3,15.
- Domain kognitif `classify/knowing`: Soal meminta siswa menerapkan rumus pH = -log[H+] secara langsung dengan substitusi nilai yang diberikan. Ini adalah prosedur rutin yang melibatkan pemahaman dasar logaritma basis 10.. Bukti: Jika segelas jus jeruk mempunyai ion hidrogen 10^-3,15, tentukan nilai pH jus jeruk tersebut.
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang penggunaan rumus logaritma untuk menghitung pH, yang merupakan penerapan standar dari definisi logaritma.. Bukti: pH = -log[H+]
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mensubstitusi nilai ke dalam rumus pH = -log[H+] dan melakukan operasi logaritma dasar. Tidak ada langkah perantara yang kompleks atau kendala yang berinteraksi.. Bukti: Jika segelas jus jeruk mempunyai ion hidrogen 10^-3,15, tentukan nilai pH jus jeruk tersebut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar logaritma (log 10^x = x) dan definisi pH. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, ini adalah aplikasi dasar dari fungsi logaritma. Tidak ada tuntutan kognitif tinggi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4025`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta penerapan langsung definisi pH sebagai fungsi logaritma negatif dari konsentrasi ion hidrogen. Siswa hanya perlu mengenali rumus dan melakukan substitusi sederhana tanpa langkah penalaran kompleks.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman prosedural dasar tentang penggunaan rumus logaritma untuk menghitung pH, yang merupakan penerapan standar dari definisi logaritma.
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menerapkan rumus pH = -log[H+] tanpa langkah perantara yang kompleks atau kendala yang berinteraksi. Beban perhitungan sangat rendah.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar logaritma (log 10^x = x) dan definisi pH. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi logaritma adalah standar kelas 11. Soal ini adalah aplikasi langsung dari definisi logaritma basis 10, sehingga sangat mudah bagi siswa kelas 11. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Fungsi Logaritma
Tipe soal: multiple_choice
Stimulus: -
Soal: Jika segelas jus jeruk mempunyai ion hidrogen $10^{-3,15}$, tentukan nilai pH jus jeruk tersebut.
Pilihan: A. -3,15
B. 0,315
C. 3,85
D. 3,15
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 50. Soal `d374329991b887f56b8800b7`

Tentukan asimtot miring dari fungsi $p(x) = \frac{x^5 + x^4 + x^2 + 1}{x^4 + 3}$.

| Opsi | Isi |
|---|---|
| A | $y = x + 3$ |
| B | $y = 1$ |
| C | $y = x$ |
| D | $y = x + 1$ |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Lakukan pembagian polinomial (x^5 + x^4 + x^2 + 1) dibagi (x^4 + 3). Hasil bagi adalah (x + 1) dengan sisa (x^2 - 3x - 2). Karena derajat sisa (2) lebih kecil dari derajat penyebut (4), maka asimtot miringnya adalah y = x + 1.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4950b142d7ec8d7e22031e96dfa6b7a9a4a96ad891677c2efaf76abfbed8b054`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2765 |
| 2 | success | valid / verified | applying | procedural | Medium | 2773 |
| 3 | success | valid / verified | applying | procedural | Easy | 2739 |

Run 1 — solusi: Melakukan pembagian polinomial (x^5 + x^4 + x^2 + 1) dibagi (x^4 + 3). Hasil bagi adalah (x + 1) dengan sisa (x^2 - 3x - 2). Karena derajat sisa (2) lebih kecil dari derajat penyebut (4), maka asimtot miringnya adalah y = x + 1.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pembagian polinomial untuk menentukan hasil bagi yang merepresentasikan asimtot miring. Ini adalah penerapan prosedur standar dalam konteks fungsi rasional.. Bukti: Tentukan asimtot miring dari fungsi p(x) = (x^5 + x^4 + x^2 + 1) / (x^4 + 3)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pembagian polinomial sebagai metode untuk menentukan asimtot miring fungsi rasional.. Bukti: Tentukan asimtot miring dari fungsi p(x) = (x^5 + x^4 + x^2 + 1) / (x^4 + 3)
- Intended difficulty `classify/Medium`: Soal ini memerlukan pembagian polinomial yang rutin. Langkah-langkahnya jelas dan tidak memerlukan strategi non-rutin atau integrasi konsep yang kompleks. Tingkat kesulitan menengah karena memerlukan ketelitian dalam pembagian polinomial derajat tinggi.. Bukti: Tentukan asimtot miring dari fungsi p(x) = (x^5 + x^4 + x^2 + 1) / (x^4 + 3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pembagian polinomial (pembagian bersusun atau Horner) |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan mampu melakukan pembagian polinomial. Soal ini adalah aplikasi langsung dari definisi asimtot miring melalui pembagian polinomial. |

Run 2 — solusi: Lakukan pembagian polinomial (x^5 + x^4 + x^2 + 1) : (x^4 + 3). Hasil bagi adalah (x + 1) dengan sisa (x^2 - 3x - 2). Karena derajat sisa (2) lebih kecil dari derajat penyebut (4), maka asimtot miringnya adalah y = x + 1.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pembagian polinomial untuk menentukan asimtot miring, yang merupakan penerapan konsep asimtot pada fungsi rasional.. Bukti: Tentukan asimtot miring dari fungsi p(x) = (x^5 + x^4 + x^2 + 1) / (x^4 + 3)
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penggunaan algoritma pembagian polinomial (prosedural) untuk memahami struktur fungsi rasional (konseptual).. Bukti: Tentukan asimtot miring dari fungsi p(x) = (x^5 + x^4 + x^2 + 1) / (x^4 + 3)
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan prosedur pembagian polinomial yang melibatkan beberapa langkah sistematis (pembagian, identifikasi sisa, penarikan kesimpulan asimtot). Meskipun prosedurnya familiar, siswa harus teliti dalam melakukan pembagian polinomial dengan derajat tinggi.. Bukti: Tentukan asimtot miring dari fungsi p(x) = (x^5 + x^4 + x^2 + 1) / (x^4 + 3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pembagian polinomial dan konsep asimtot fungsi rasional. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan mampu melakukan pembagian polinomial untuk menentukan asimtot miring. Prosedur ini rutin namun memerlukan ketelitian dalam operasi aljabar. |

Run 3 — solusi: Melakukan pembagian polinomial (x^5 + x^4 + x^2 + 1) / (x^4 + 3). Hasil bagi adalah (x + 1) dengan sisa (x^2 - 3x - 2). Karena derajat sisa (2) lebih kecil dari derajat penyebut (4), maka asimtot miringnya adalah y = x + 1.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pembagian polinomial untuk menentukan asimtot miring, yang merupakan penerapan rutin dari konsep fungsi rasional.. Bukti: Tentukan asimtot miring dari fungsi p(x) = (x^5 + x^4 + x^2 + 1) / (x^4 + 3)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pembagian polinomial dan kriteria asimtot miring pada fungsi rasional.. Bukti: Tentukan asimtot miring dari fungsi p(x) = (x^5 + x^4 + x^2 + 1) / (x^4 + 3)
- Intended difficulty `classify/Easy`: Soal ini memerlukan satu prosedur utama (pembagian polinomial) yang familiar bagi siswa kelas 11. Jalur penyelesaian jelas dan tidak memerlukan integrasi konsep yang kompleks.. Bukti: Tentukan asimtot miring dari fungsi p(x) = (x^5 + x^4 + x^2 + 1) / (x^4 + 3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pembagian polinomial dan konsep asimtot fungsi rasional. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pembagian polinomial adalah materi standar kelas 11. Prosedur ini langsung dan tidak melibatkan kendala yang saling berinteraksi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4491`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur pembagian polinomial untuk menentukan hasil bagi yang merepresentasikan asimtot miring. Ini adalah penerapan prosedur standar dalam konteks fungsi rasional.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang algoritma pembagian polinomial sebagai metode untuk menentukan asimtot miring fungsi rasional.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena memerlukan prosedur pembagian polinomial yang melibatkan beberapa langkah sistematis. Meskipun prosedurnya familiar, siswa harus teliti dalam melakukan pembagian polinomial dengan derajat tinggi untuk mendapatkan hasil bagi yang tepat.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pembagian polinomial (pembagian bersusun atau Horner) |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan mampu melakukan pembagian polinomial. Soal ini adalah aplikasi langsung dari definisi asimtot miring melalui pembagian polinomial. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Fungsi Aljabar
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan asimtot miring dari fungsi $p(x) = \frac{x^5 + x^4 + x^2 + 1}{x^4 + 3}$.
Pilihan: A. $y = x + 3$
B. $y = 1$
C. $y = x$
D. $y = x + 1$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 51. Soal `471338f922e3d9a1e408d5a7`

Sebuah perusahaan kue bronis membutuhkan biaya bulanan Rp7.000.000,00 dan biaya produksi Rp40.000,00 per loyang kue. Misalkan rumus fungsi biaya adalah $B(x)$ = biaya tetap + $cx$, dengan $c$ adalah biaya produksi setiap kue dan $x$ adalah banyaknya produksi kue bronis (tiap loyang).<br><br>Tentukan model matematika dari fungsi biaya untuk memproduksi $x$ loyang kue bronis.

| Opsi | Isi |
|---|---|
| A | $B(x) = 40.000 + 7.000.000x$ |
| B | $B(x) = 7.040.000x$ |
| C | $B(x) = 7.000.000 + 40.000x$ |
| D | $B(x) = \frac{7.000.000 + 40.000x}{x}$ |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Biaya tetap adalah Rp7.000.000,00 dan biaya variabel adalah Rp40.000,00 per loyang (x). Maka, fungsi biaya total B(x) = biaya tetap + (biaya per unit * x) = 7.000.000 + 40.000x.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5ecc8aa2bcde84009ad7510b3cf4b154e2ada169cc26f66d50d8e221923abf41`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2838 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2824 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2835 |

Run 1 — solusi: Biaya tetap adalah Rp7.000.000,00 dan biaya variabel adalah Rp40.000,00 per loyang (x). Maka, fungsi biaya total B(x) = biaya tetap + (biaya per unit * x) = 7.000.000 + 40.000x.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali komponen biaya tetap dan biaya variabel dari narasi soal, lalu menyusunnya ke dalam bentuk fungsi linear yang sudah diberikan polanya.. Bukti: biaya bulanan Rp7.000.000,00 dan biaya produksi Rp40.000,00 per loyang kue; rumus fungsi biaya adalah B(x) = biaya tetap + cx
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang struktur fungsi biaya linear (biaya tetap vs biaya variabel).. Bukti: rumus fungsi biaya adalah B(x) = biaya tetap + cx
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar. Siswa hanya perlu melakukan substitusi nilai ke dalam rumus yang sudah disediakan secara eksplisit. Tidak ada langkah perencanaan atau integrasi yang kompleks.. Bukti: biaya bulanan Rp7.000.000,00 dan biaya produksi Rp40.000,00 per loyang kue; rumus fungsi biaya adalah B(x) = biaya tetap + cx

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi linear dan variabel. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, soal ini terlalu sederhana karena hanya berupa substitusi langsung ke rumus yang diberikan, jauh di bawah ekspektasi kompetensi matematika tingkat lanjut. |

Run 2 — solusi: Biaya total B(x) terdiri dari biaya tetap (konstanta) dan biaya variabel (biaya per unit dikali jumlah unit). Biaya tetap = 7.000.000. Biaya variabel = 40.000 * x. Maka, B(x) = 7.000.000 + 40.000x.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali komponen biaya tetap dan biaya variabel lalu menyusunnya ke dalam bentuk fungsi linear sederhana sesuai definisi yang diberikan di soal.. Bukti: biaya bulanan Rp7.000.000,00 dan biaya produksi Rp40.000,00 per loyang kue; rumus fungsi biaya adalah B(x) = biaya tetap + cx
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana biaya tetap dan biaya variabel membentuk fungsi biaya linear.. Bukti: rumus fungsi biaya adalah B(x) = biaya tetap + cx
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar. Siswa hanya perlu melakukan substitusi nilai ke dalam rumus yang sudah disediakan secara eksplisit. Tidak ada langkah perencanaan yang kompleks atau kendala yang berinteraksi.. Bukti: biaya bulanan Rp7.000.000,00 dan biaya produksi Rp40.000,00 per loyang kue; Tentukan model matematika dari fungsi biaya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi linear dan konsep biaya tetap/variabel. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Meskipun untuk kelas 11, soal ini terlalu sederhana karena hanya meminta pembentukan fungsi linear dasar yang biasanya sudah dikuasai di jenjang SMP atau kelas 10. |

Run 3 — solusi: Biaya total B(x) terdiri dari biaya tetap (konstanta) dan biaya variabel (biaya per unit dikali jumlah unit). Biaya tetap = 7.000.000. Biaya variabel = 40.000 * x. Maka, B(x) = 7.000.000 + 40.000x.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali komponen biaya tetap dan variabel dari narasi soal, lalu menyusunnya ke dalam bentuk fungsi linear sederhana yang sudah diberikan strukturnya.. Bukti: biaya bulanan Rp7.000.000,00 dan biaya produksi Rp40.000,00 per loyang kue; rumus fungsi biaya adalah B(x) = biaya tetap + cx
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana biaya tetap dan biaya variabel membentuk fungsi linear total.. Bukti: rumus fungsi biaya adalah B(x) = biaya tetap + cx
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar. Siswa hanya perlu melakukan substitusi nilai ke dalam rumus yang sudah disediakan. Tidak ada langkah perencanaan kompleks atau kendala yang berinteraksi.. Bukti: B(x) = biaya tetap + cx; biaya bulanan Rp7.000.000,00 dan biaya produksi Rp40.000,00 per loyang kue

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi linear dan variabel. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Materi ini sebenarnya merupakan prasyarat atau materi dasar aljabar yang jauh di bawah standar kompetensi matematika tingkat lanjut kelas 11. |

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
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Fungsi Aljabar
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah perusahaan kue bronis membutuhkan biaya bulanan Rp7.000.000,00 dan biaya produksi Rp40.000,00 per loyang kue. Misalkan rumus fungsi biaya adalah $B(x)$ = biaya tetap + $cx$, dengan $c$ adalah biaya produksi setiap kue dan $x$ adalah banyaknya produksi kue bronis (tiap loyang).

Tentukan model matematika dari fungsi biaya untuk memproduksi $x$ loyang kue bronis.
Pilihan: A. $B(x) = 40.000 + 7.000.000x$
B. $B(x) = 7.040.000x$
C. $B(x) = 7.000.000 + 40.000x$
D. $B(x) = \frac{7.000.000 + 40.000x}{x}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 52. Soal `208be0f9546df9e4d53632eb`

Sebuah koloni bakteri bermula dengan 500 bakteri. Bakteri jenis ini mampu membelah diri menjadi dua setiap setengah jam sekali.<br><br>Berapa banyak bakteri setelah 40 menit?

| Opsi | Isi |
|---|---|
| A | sekitar 1.260 |
| B | sekitar 794 |
| C | 1.000 |
| D | 2.000 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Model pertumbuhan eksponensial: N(t) = N0 * 2^(t/T). Diketahui N0 = 500, T = 30 menit, t = 40 menit. Maka N(40) = 500 * 2^(40/30) = 500 * 2^(4/3) ≈ 500 * 2,5198 ≈ 1.259,9. Dibulatkan menjadi 1.260.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7c0fc7ed9ab935683391d37a26fce16859d781480dde7549377aff38fab85a71`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2772 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2759 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2747 |

Run 1 — solusi: Model pertumbuhan eksponensial: N(t) = N0 * 2^(t/T). Diketahui N0 = 500, T = 30 menit, t = 40 menit. Maka N(40) = 500 * 2^(40/30) = 500 * 2^(4/3) = 500 * 2^(1.333) ≈ 500 * 2.5198 ≈ 1.259,9. Dibulatkan menjadi 1.260.
- Domain kognitif `classify/applying`: Siswa perlu memodelkan situasi pertumbuhan eksponensial dengan menentukan fungsi yang tepat berdasarkan laju pertumbuhan dan waktu yang diberikan, kemudian menerapkan prosedur perhitungan eksponensial.. Bukti: mampu membelah diri menjadi dua setiap setengah jam sekali; Berapa banyak bakteri setelah 40 menit?
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami konsep pertumbuhan eksponensial dan bagaimana menerjemahkan informasi laju pertumbuhan ke dalam bentuk fungsi matematika.. Bukti: mampu membelah diri menjadi dua setiap setengah jam sekali
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan konversi satuan waktu (menit ke rasio periode pembelahan) dan menerapkan model eksponensial. Meskipun prosedurnya rutin, terdapat langkah perantara yang memerlukan pemahaman konsep pertumbuhan eksponensial yang tepat agar tidak terjebak pada kesalahan pembulatan periode.. Bukti: 500 bakteri; membelah diri menjadi dua setiap setengah jam sekali; 40 menit

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi eksponensial dan operasi bilangan berpangkat pecahan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, memodelkan pertumbuhan eksponensial adalah materi standar. Kesulitan terletak pada penanganan eksponen pecahan (4/3) yang memerlukan kalkulator atau pemahaman logaritma/pangkat, namun konsep dasarnya familiar. |

Run 2 — solusi: Model pertumbuhan eksponensial: N(t) = N0 * 2^(t/T). N0 = 500, T = 30 menit, t = 40 menit. N(40) = 500 * 2^(40/30) = 500 * 2^(4/3) = 500 * 2^(1.333...) ≈ 500 * 2.5198 ≈ 1.259,9. Dibulatkan menjadi sekitar 1.260.
- Domain kognitif `classify/applying`: Siswa perlu memodelkan situasi pertumbuhan eksponensial dengan menentukan fungsi yang tepat berdasarkan laju pertumbuhan dan waktu yang diberikan, kemudian menerapkan prosedur perhitungan eksponensial.. Bukti: mampu membelah diri menjadi dua setiap setengah jam sekali; Berapa banyak bakteri setelah 40 menit?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman konseptual tentang fungsi eksponensial sebagai model pertumbuhan populasi dan prosedur untuk menerapkannya pada konteks waktu yang tidak bulat.. Bukti: koloni bakteri bermula dengan 500 bakteri; membelah diri menjadi dua setiap setengah jam sekali
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena menuntut siswa untuk mengonversi satuan waktu dan memahami bahwa rasio pertumbuhan (pembelahan) harus disesuaikan dengan durasi waktu yang diberikan (40/30), bukan sekadar memasukkan angka bulat.. Bukti: setiap setengah jam sekali; setelah 40 menit

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi eksponensial dan operasi pecahan/eksponen. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 diharapkan mampu memodelkan pertumbuhan eksponensial. Tantangan terletak pada penggunaan eksponen pecahan (4/3) yang memerlukan ketelitian, namun prosedurnya standar. |

Run 3 — solusi: Model pertumbuhan eksponensial: N(t) = N0 * 2^(t/p), dengan N0 = 500, p = 30 menit, t = 40 menit. N(40) = 500 * 2^(40/30) = 500 * 2^(4/3) ≈ 500 * 2,5198 ≈ 1.259,9. Dibulatkan menjadi 1.260.
- Domain kognitif `classify/applying`: Siswa perlu memodelkan situasi pertumbuhan eksponensial dengan menentukan basis dan eksponen yang tepat berdasarkan rasio waktu (40 menit per 30 menit). Ini melibatkan penerapan konsep fungsi eksponensial pada konteks rutin.. Bukti: mampu membelah diri menjadi dua setiap setengah jam sekali; Berapa banyak bakteri setelah 40 menit?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip pertumbuhan eksponensial dan bagaimana menerjemahkan deskripsi verbal ke dalam model matematika.. Bukti: mampu membelah diri menjadi dua setiap setengah jam sekali
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena model pertumbuhan eksponensial adalah prosedur standar yang familiar bagi siswa kelas 11. Langkah penyelesaiannya langsung: menentukan rasio waktu (4/3) dan menghitung nilai fungsi. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: 500 bakteri; membelah diri menjadi dua setiap setengah jam sekali; setelah 40 menit

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi eksponensial dan operasi pecahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi eksponensial adalah bagian standar kurikulum kelas 11. Soal ini hanya memerlukan substitusi nilai ke dalam rumus pertumbuhan yang umum dipelajari. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4511`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu memodelkan situasi pertumbuhan eksponensial dengan menentukan fungsi yang tepat berdasarkan laju pertumbuhan dan waktu yang diberikan, kemudian menerapkan prosedur perhitungan eksponensial.
- Dimensi pengetahuan `conceptual`: Soal ini menuntut pemahaman konseptual tentang fungsi eksponensial sebagai model pertumbuhan populasi dan prosedur untuk menerapkannya pada konteks waktu yang tidak bulat.
- Intended difficulty `Easy`: Soal ini tergolong Easy karena model pertumbuhan eksponensial adalah prosedur standar yang familiar bagi siswa kelas 11. Langkah penyelesaiannya langsung: menentukan rasio waktu (4/3) dan menghitung nilai fungsi. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi eksponensial dan operasi bilangan berpangkat pecahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi eksponensial adalah bagian standar kurikulum kelas 11. Soal ini hanya memerlukan substitusi nilai ke dalam rumus pertumbuhan yang umum dipelajari. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Fungsi Non-aljabar
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah koloni bakteri bermula dengan 500 bakteri. Bakteri jenis ini mampu membelah diri menjadi dua setiap setengah jam sekali.

Berapa banyak bakteri setelah 40 menit?
Pilihan: A. sekitar 1.260
B. sekitar 794
C. 1.000
D. 2.000
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 53. Soal `0e8b25c240073e177fc6a787`

Sebuah koloni bakteri bermula dengan 500 bakteri. Bakteri jenis ini mampu membelah diri menjadi dua setiap setengah jam sekali.<br><br>Berapa banyak bakteri setelah $t$ jam?

| Opsi | Isi |
|---|---|
| A | $500 \times 2^{2t}$ |
| B | $500 \times 2t$ |
| C | $500 \times 2^{t/2}$ |
| D | $500 \times 2^{t}$ |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Bakteri membelah menjadi dua setiap 0,5 jam. Dalam 1 jam, terjadi 2 kali pembelahan. Maka dalam t jam, terjadi 2t kali pembelahan. Model pertumbuhan eksponensialnya adalah N(t) = N0 * 2^(jumlah pembelahan) = 500 * 2^(2t).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `43628be9d1b5570099a89dfff68b81819ff83b2d6e0accb16a71353ee28ebea2`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2696 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2990 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2710 |

Run 1 — solusi: Bakteri membelah menjadi dua setiap 0,5 jam. Dalam 1 jam, terjadi 2 kali pembelahan. Maka dalam t jam, terjadi 2t kali pembelahan. Model pertumbuhan eksponensialnya adalah N(t) = N0 * 2^(jumlah pembelahan) = 500 * 2^(2t).
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan narasi pertumbuhan eksponensial ke dalam model matematika. Ini melibatkan pemahaman konsep laju pertumbuhan dan pembentukan fungsi eksponensial, yang merupakan penerapan konsep pada konteks rutin.. Bukti: mampu membelah diri menjadi dua setiap setengah jam sekali; Berapa banyak bakteri setelah t jam?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara variabel waktu dan frekuensi pembelahan dalam fungsi eksponensial, yang merupakan aspek konseptual dari pertumbuhan eksponensial.. Bukti: mampu membelah diri menjadi dua setiap setengah jam sekali
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena merupakan penerapan langsung dari model pertumbuhan eksponensial standar. Siswa hanya perlu menentukan eksponen yang tepat berdasarkan frekuensi pembelahan (2t). Jalur penyelesaian sangat jelas dan tidak memerlukan perencanaan strategi yang kompleks.. Bukti: bermula dengan 500 bakteri; membelah diri menjadi dua setiap setengah jam sekali

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi eksponensial dan konsep pertumbuhan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi fungsi eksponensial adalah topik standar kelas 11. Soal ini tidak memiliki kendala yang saling berinteraksi atau tuntutan integrasi tinggi. |

Run 2 — solusi: Bakteri membelah menjadi dua setiap 0,5 jam. Dalam t jam, jumlah periode pembelahan adalah t / 0,5 = 2t. Dengan nilai awal 500, model pertumbuhan eksponensialnya adalah P(t) = 500 * 2^(2t).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep pertumbuhan eksponensial untuk memodelkan situasi nyata. Ini adalah penerapan prosedur standar dalam fungsi eksponensial.. Bukti: mampu membelah diri menjadi dua setiap setengah jam sekali; Berapa banyak bakteri setelah t jam?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana periode waktu (setengah jam) mempengaruhi eksponen dalam model pertumbuhan eksponensial.. Bukti: mampu membelah diri menjadi dua setiap setengah jam sekali; Berapa banyak bakteri setelah t jam?
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin dalam fungsi eksponensial. Siswa hanya perlu mengidentifikasi laju pertumbuhan dan menyesuaikan eksponen berdasarkan interval waktu yang diberikan. Tidak ada kendala kompleks atau integrasi konsep yang menuntut.. Bukti: mampu membelah diri menjadi dua setiap setengah jam sekali; Berapa banyak bakteri setelah t jam?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi eksponensial dan konsep pertumbuhan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal standar untuk kelas 11 yang menguji pemahaman dasar tentang model eksponensial tanpa kerumitan tambahan. |

Run 3 — solusi: Model pertumbuhan eksponensial adalah N(t) = N0 * 2^(t/T). Diketahui N0 = 500 dan periode penggandaan T = 0,5 jam. Maka, N(t) = 500 * 2^(t/0,5) = 500 * 2^(2t).
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan situasi pertumbuhan eksponensial ke dalam model matematika. Ini melibatkan pemahaman konsep fungsi eksponensial dan penentuan parameter laju pertumbuhan berdasarkan periode waktu yang diberikan.. Bukti: mampu membelah diri menjadi dua setiap setengah jam sekali; Berapa banyak bakteri setelah t jam?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana fungsi eksponensial memodelkan pertumbuhan populasi, khususnya hubungan antara variabel waktu dan periode penggandaan.. Bukti: Berapa banyak bakteri setelah t jam?
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena merupakan penerapan langsung dari model pertumbuhan eksponensial standar. Siswa hanya perlu mengidentifikasi nilai awal dan periode penggandaan untuk menyusun fungsi tanpa kendala yang kompleks atau integrasi multi-tahap yang sulit.. Bukti: mampu membelah diri menjadi dua setiap setengah jam sekali; Berapa banyak bakteri setelah t jam?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi eksponensial dan konsep laju pertumbuhan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi fungsi eksponensial adalah standar kelas 11. Soal ini tidak menuntut manipulasi aljabar yang rumit atau penalaran non-rutin, sehingga sesuai untuk tingkat kesulitan rendah. |

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
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Fungsi Non-aljabar
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah koloni bakteri bermula dengan 500 bakteri. Bakteri jenis ini mampu membelah diri menjadi dua setiap setengah jam sekali.

Berapa banyak bakteri setelah $t$ jam?
Pilihan: A. $500 \times 2^{2t}$
B. $500 \times 2t$
C. $500 \times 2^{t/2}$
D. $500 \times 2^{t}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 54. Soal `842ca4bb6c6ebd4208641b61`

Sederhanakan bentuk akar berikut ini.<br><br>$(5\sqrt{x^5})(3\sqrt[3]{x})$

| Opsi | Isi |
|---|---|
| A | $15x^{\frac{6}{17}}$ |
| B | $15x^{\frac{17}{6}}$ |
| C | $8x^{\frac{17}{6}}$ |
| D | $15x^{\frac{13}{6}}$ |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Ubah bentuk akar ke pangkat pecahan: (5x^(5/2))(3x^(1/3)). Kalikan koefisien: 5 * 3 = 15. Jumlahkan pangkat: 5/2 + 1/3 = 15/6 + 2/6 = 17/6. Hasil: 15x^(17/6).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `cfe6313bef0b50b121a49b4647c9aba93a5832b11f75ddb541dc6fc510926e84`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2724 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2718 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2685 |

Run 1 — solusi: Ubah bentuk akar ke pangkat pecahan: (5x^(5/2))(3x^(1/3)). Kalikan koefisien: 5 * 3 = 15. Jumlahkan pangkat: 5/2 + 1/3 = 15/6 + 2/6 = 17/6. Hasil: 15x^(17/6).
- Domain kognitif `classify/knowing`: Siswa diminta menerapkan prosedur standar mengubah bentuk akar menjadi pangkat pecahan dan menggunakan sifat eksponen (perkalian basis sama berarti penjumlahan pangkat). Ini adalah prosedur rutin yang langsung.. Bukti: Sederhanakan bentuk akar berikut ini.; (5\sqrt{x^5})(3\sqrt[3]{x})
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau metode operasi aljabar pada bentuk akar dan eksponen pecahan.. Bukti: Sederhanakan bentuk akar berikut ini.; (5\sqrt{x^5})(3\sqrt[3]{x})
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang sangat jelas. Siswa hanya perlu menerapkan aturan eksponen dasar. Tidak ada kendala yang berinteraksi atau kebutuhan perencanaan strategi yang kompleks.. Bukti: Sederhanakan bentuk akar berikut ini.; (5\sqrt{x^5})(3\sqrt[3]{x})

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat-sifat eksponen dan bentuk akar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini merupakan prasyarat dasar yang sudah dipelajari sebelum kelas 11, sehingga bagi siswa kelas 11, ini adalah prosedur yang sangat familiar dan langsung. |

Run 2 — solusi: Ubah bentuk akar ke eksponen pecahan: 5x^(5/2) * 3x^(1/3). Kalikan koefisien: 5 * 3 = 15. Jumlahkan eksponen: 5/2 + 1/3 = 15/6 + 2/6 = 17/6. Hasil akhir: 15x^(17/6).
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan prosedur rutin mengubah bentuk akar ke eksponen pecahan dan menerapkan aturan perkalian eksponen (penjumlahan pangkat). Ini adalah prosedur standar yang langsung.. Bukti: Sederhanakan bentuk akar berikut ini. (5√x^5)(3√[3]x)
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami aturan eksponen (konseptual) dan menerapkan algoritma penyederhanaan (prosedural) untuk menyelesaikan soal.. Bukti: Sederhanakan bentuk akar berikut ini. (5√x^5)(3√[3]x)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan langkah-langkah yang jelas dan familiar bagi siswa kelas 11. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Sederhanakan bentuk akar berikut ini. (5√x^5)(3√[3]x)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar eksponen pecahan dan operasi aljabar pada bentuk akar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini merupakan prasyarat dasar yang sudah dikuasai di jenjang sebelumnya atau awal kelas 11, sehingga tingkat kesulitannya rendah. |

Run 3 — solusi: Ekspresi: (5x^(5/2))(3x^(1/3)) = (5*3) * x^(5/2 + 1/3) = 15 * x^(15/6 + 2/6) = 15x^(17/6).
- Domain kognitif `classify/knowing`: Siswa diminta menerapkan aturan eksponen (perkalian koefisien dan penjumlahan pangkat pecahan) untuk menyederhanakan bentuk akar. Ini adalah prosedur rutin yang langsung.. Bukti: Sederhanakan bentuk akar berikut ini.; (5\sqrt{x^5})(3\sqrt[3]{x})
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma dasar operasi aljabar pada bentuk akar dan eksponen pecahan.. Bukti: Sederhanakan bentuk akar berikut ini.; (5\sqrt{x^5})(3\sqrt[3]{x})
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan langkah penyelesaian yang jelas (mengalikan koefisien dan menjumlahkan eksponen). Tidak ada kendala yang berinteraksi atau kebutuhan perencanaan strategi yang kompleks.. Bukti: Sederhanakan bentuk akar berikut ini.; (5\sqrt{x^5})(3\sqrt[3]{x})

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Aturan eksponen dasar dan operasi pecahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini merupakan prasyarat dasar yang sudah dikuasai di jenjang sebelumnya, sehingga untuk kelas 11 ini dikategorikan mudah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
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
Subtopik: Bentuk Akar
Tipe soal: multiple_choice
Stimulus: -
Soal: Sederhanakan bentuk akar berikut ini.

$(5\sqrt{x^5})(3\sqrt[3]{x})$
Pilihan: A. $15x^{\frac{6}{17}}$
B. $15x^{\frac{17}{6}}$
C. $8x^{\frac{17}{6}}$
D. $15x^{\frac{13}{6}}$
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 55. Soal `72d9df20cc708f4143b713d0`

Apabila diketahui banyak anggota dua himpunan seperti berikut ini, maka ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? a. n(A) = n(B) = 12<br><br>Ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12?

| Opsi | Isi |
|---|---|
| A | 12 + 11 + 10 + ... + 2 + 1 = 78 |
| B | 12 x 12 = 144 |
| C | 12 |
| D | 12! = 479.001.600 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 12, maka banyak korespondensi adalah 12! = 479.001.600.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e15b0d1dba648e061336ce94d5ea96ec6315ea685f8e1547e09aff80f787d76c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2862 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2864 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2874 |

Run 1 — solusi: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 12, maka banyak korespondensi adalah 12! = 12 × 11 × 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 479.001.600.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus faktorial untuk menentukan banyaknya korespondensi satu-satu. Ini adalah penerapan langsung dari konsep dasar kombinatorika yang sudah dipelajari.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang rumus faktorial untuk korespondensi satu-satu.. Bukti: banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengenali bahwa korespondensi satu-satu antara dua himpunan dengan jumlah anggota yang sama n adalah n!. Tidak ada langkah integrasi atau perencanaan yang kompleks.. Bukti: n(A) = n(B) = 12

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar faktorial dan korespondensi satu-satu. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun angka 12! cukup besar, prosedurnya sangat standar dan familiar bagi siswa kelas 11 yang mempelajari materi dasar kombinatorika/fungsi. |

Run 2 — solusi: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 12, maka banyak korespondensi satu-satu adalah 12! = 12 × 11 × 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 479.001.600.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk menerapkan rumus faktorial untuk menentukan banyaknya korespondensi satu-satu (bijeksi) antara dua himpunan berhingga dengan jumlah anggota yang sama. Ini adalah penerapan langsung dari konsep dasar kombinatorika yang sudah dipelajari.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang rumus faktorial untuk korespondensi satu-satu.. Bukti: n(A) = n(B) = 12; banyak korespondensi satu-satu yang mungkin
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu mengenali bahwa korespondensi satu-satu antara dua himpunan dengan n elemen adalah n!. Tidak ada langkah integrasi atau perencanaan yang kompleks.. Bukti: n(A) = n(B) = 12

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar himpunan dan faktorial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun faktorial 12! menghasilkan angka besar, konsepnya sangat mendasar dan familiar bagi siswa kelas 11 yang mempelajari kombinatorika dasar. |

Run 3 — solusi: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 12, maka banyak korespondensi adalah 12! = 12 × 11 × 10 × ... × 1 = 479.001.600.
- Domain kognitif `classify/knowing`: Soal ini meminta penerapan langsung rumus faktorial untuk menentukan banyaknya korespondensi satu-satu (bijeksi) antara dua himpunan berhingga dengan jumlah anggota yang sama. Siswa hanya perlu mengenali konsep dan menerapkan prosedur perhitungan faktorial.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang aturan pencacahan dasar untuk korespondensi satu-satu (bijeksi) pada himpunan berhingga.. Bukti: banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B
- Intended difficulty `classify/Easy`: Soal ini dikategorikan Easy karena merupakan penerapan langsung dari rumus faktorial (n!) untuk korespondensi satu-satu. Tidak ada langkah perencanaan kompleks, integrasi konsep, atau kendala yang berinteraksi. Prosedur sangat rutin bagi siswa yang mempelajari materi ini.. Bukti: n(A) = n(B) = 12

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang himpunan dan aturan perkalian/faktorial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun faktorial adalah materi dasar, soal ini hanya menuntut ingatan/penerapan rumus langsung tanpa variasi atau konteks yang menantang, sehingga sangat mudah bagi level kelas 11. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 1, "knowing": 2} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4545`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta penerapan langsung rumus faktorial untuk menentukan banyaknya korespondensi satu-satu (bijeksi) antara dua himpunan berhingga dengan jumlah anggota yang sama. Siswa hanya perlu mengenali konsep dan menerapkan prosedur perhitungan faktorial.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang aturan pencacahan dasar untuk korespondensi satu-satu (bijeksi) pada himpunan berhingga.
- Intended difficulty `Easy`: Soal ini dikategorikan Easy karena merupakan penerapan langsung dari rumus faktorial (n!) untuk korespondensi satu-satu. Tidak ada langkah perencanaan kompleks, integrasi konsep, atau kendala yang berinteraksi. Prosedur sangat rutin bagi siswa yang mempelajari materi ini.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang himpunan dan aturan perkalian/faktorial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun faktorial 12! menghasilkan angka besar, konsepnya sangat mendasar dan familiar bagi siswa kelas 11 yang mempelajari kombinatorika dasar. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
Jalur mata pelajaran: Matematika Tingkat Lanjut
Topik: Matematika Tingkat Lanjut SMA Kelas 11
Subtopik: Korespondensi Satu-satu (Pengayaan)
Tipe soal: multiple_choice
Stimulus: -
Soal: Apabila diketahui banyak anggota dua himpunan seperti berikut ini, maka ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B? a. n(A) = n(B) = 12

Ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12?
Pilihan: A. 12 + 11 + 10 + ... + 2 + 1 = 78
B. 12 x 12 = 144
C. 12
D. 12! = 479.001.600
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
