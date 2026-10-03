# Validasi ulang soal kelas 11 TL — Gemini blind N=3 dan diagnostik IndoBERT

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v9-blind-sma11-tl-key-verified`. Rubrik: `math-rubric-3x4x3-v7-sma11-tl-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 11 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan menjadi keputusan silver operasional.

Checkpoint dikunci dengan SHA-256 sebelum pemeriksaan scope IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Model SD berada di luar cakupan kelas 11, sehingga seluruh head abstain dan tidak menghasilkan ukuran agreement dengan label blind.

Jumlah soal: 55; distribusi label advisory: `{"mathCognitiveDomain": {"knowing": 12, "applying": 41, "reasoning": 2}, "knowledgeDimension": {"conceptual": 20, "procedural": 32, "factual": 3, "metacognitive": 0}, "intendedDifficulty": {"Easy": 44, "Medium": 11, "Hard": 0}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"knowing": 12, "applying": 40, "reasoning": 2}, "knowledgeDimension": {"conceptual": 20, "procedural": 31, "factual": 3}, "intendedDifficulty": {"Easy": 43, "Medium": 11}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"silver_ready": 54, "revision_required": 1}`.
Run awal sukses: 165/165; adjudikasi: 19; token sukses tercatat: 472,494.

Seluruh label memakai provenance ai_silver. Delivery memakai snapshot silver yang lolos qualification. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

IndoBERT aktif: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Artifact belum disetujui; tidak ada training ulang dalam batch ini. Difficulty model lama dapat mengalami class collapse. Confidence dari kalibrasi kelas 1 yang kecil belum membuktikan ketepatan label.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten dapat masuk snapshot silver operasional.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 44 | 43 | [Easy.json](difficulty/Easy.json) |
| Medium | 11 | 11 | [Medium.json](difficulty/Medium.json) |
| Hard | 0 | 0 | [Hard.json](difficulty/Hard.json) |

## Perhitungan yang dipakai

Untuk kelas 11, encoder dan head IndoBERT tidak dijalankan karena scope model hanya kelas 1–6. Probabilitas kosong, label/confidence/entropy null, dan action abstain berasal dari pemeriksaan scope runtime. Suara Gemini adalah bukti penilaian advisory, bukan probabilitas IndoBERT.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

Model IndoBERT lama hanya mendukung SD kelas 1–6. Untuk kelas 11, diagnostik mengembalikan `out_of_scope` dan `abstain`: label, confidence, dan entropy null serta probabilitas kosong. Label advisory mengikuti Gemini blind dengan rubrik SMA kelas 11. Tidak ada inferensi SD yang dipaksakan sebagai prediksi SMA.

## 1. Soal `6678eff0f2f3f2aa21d884b8`

$A = \begin{bmatrix} -3 & 2 & 0 \\ 1 & 3 & 5 \end{bmatrix}$<br><br>Tentukan jenis matriks-matriks berikut.

| Opsi | Isi |
|---|---|
| A | Matriks datar |
| B | Matriks persegi |
| C | Matriks segitiga atas |
| D | Matriks tegak |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Matriks A memiliki 2 baris dan 3 kolom (ordo 2x3). Karena jumlah baris (2) lebih kecil dari jumlah kolom (3), maka matriks A diklasifikasikan sebagai matriks datar.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `265b9448bcc64e3072b6c7e9a603d7d08ea78d5771eedce25ac0dfc6fe3bf095`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2557 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2101 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2670 |

Run 1 — solusi: Matriks A memiliki 2 baris dan 3 kolom (ordo 2x3). Karena jumlah baris (2) lebih kecil dari jumlah kolom (3), maka matriks A diklasifikasikan sebagai matriks datar.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali definisi matriks datar berdasarkan ordo matriks yang diberikan tanpa memerlukan strategi kompleks.. Bukti: Tentukan jenis matriks-matriks berikut.
- Dimensi pengetahuan `classify/conceptual`: Memahami klasifikasi matriks berdasarkan hubungan jumlah baris dan kolom merupakan pemahaman konsep dasar.. Bukti: A = \begin{bmatrix} -3 & 2 & 0 \\ 1 & 3 & 5 \end{bmatrix}; Matriks datar
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan hanya menguji pemahaman definisi dasar matriks datar, yang merupakan materi pengenalan di kelas 11.. Bukti: A = \begin{bmatrix} -3 & 2 & 0 \\ 1 & 3 & 5 \end{bmatrix}; Tentukan jenis matriks-matriks berikut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi ordo matriks (baris x kolom). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan prosedur familiar untuk mengidentifikasi jenis matriks berdasarkan dimensinya, sesuai dengan standar materi awal kelas 11. |

Run 2 — solusi: Matriks A memiliki 2 baris dan 3 kolom (ordo 2x3). Karena jumlah baris (2) kurang dari jumlah kolom (3), maka matriks tersebut diklasifikasikan sebagai matriks datar.
- Domain kognitif `classify/knowing`: Siswa diminta mengidentifikasi jenis matriks berdasarkan ordo yang diberikan. Proses ini hanya memerlukan pengenalan definisi matriks datar (baris < kolom) dan penerapan langsung pada matriks yang diberikan.. Bukti: A = \begin{bmatrix} -3 & 2 & 0 \\ 1 & 3 & 5 \end{bmatrix}; Tentukan jenis matriks-matriks berikut.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap definisi dan klasifikasi jenis-jenis matriks, yang merupakan pengetahuan konseptual dasar dalam aljabar matriks.. Bukti: Tentukan jenis matriks-matriks berikut.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan prosedural. Siswa hanya perlu menghitung jumlah baris dan kolom, lalu mencocokkannya dengan definisi matriks datar. Tidak ada langkah kompleks atau strategi non-rutin yang diperlukan.. Bukti: A = \begin{bmatrix} -3 & 2 & 0 \\ 1 & 3 & 5 \end{bmatrix}; Tentukan jenis matriks-matriks berikut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi ordo matriks dan klasifikasi jenis matriks (persegi, datar, tegak). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini adalah pengenalan dasar matriks di kelas 11. Tingkat kesulitan rendah karena hanya melibatkan identifikasi sifat dasar matriks tanpa operasi atau manipulasi aljabar. |

Run 3 — solusi: Matriks A memiliki 2 baris dan 3 kolom (ordo 2x3). Karena jumlah baris (2) lebih kecil daripada jumlah kolom (3), maka matriks A diklasifikasikan sebagai matriks datar.
- Domain kognitif `classify/knowing`: Siswa perlu mengidentifikasi ordo matriks dan mencocokkannya dengan definisi jenis matriks (matriks datar).. Bukti: A = \begin{bmatrix} -3 & 2 & 0 \\ 1 & 3 & 5 \end{bmatrix}; Tentukan jenis matriks-matriks berikut.
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman konseptual tentang definisi jenis-jenis matriks berdasarkan ordonya.. Bukti: Tentukan jenis matriks-matriks berikut.
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya memerlukan identifikasi ordo dan pencocokan dengan definisi dasar.. Bukti: A = \begin{bmatrix} -3 & 2 & 0 \\ 1 & 3 & 5 \end{bmatrix}

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
| gradeRelativeRationale | Materi dasar matriks yang diajarkan di awal bab matriks kelas 11. |

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: Matriks B memiliki elemen di bawah diagonal utama (b21=0, b31=0, b32=0) yang semuanya bernilai nol. Berdasarkan definisi, matriks persegi dengan elemen di bawah diagonal utama bernilai nol disebut matriks segitiga atas.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `baba89011cec73af0a2c8012794e77ae68f5f0602d89d26c52bcabe18d6423b4`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2913 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2907 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2793 |

Run 1 — solusi: Matriks B memiliki elemen di bawah diagonal utama (b21=0, b31=0, b32=0) yang semuanya bernilai nol. Berdasarkan definisi, matriks persegi dengan elemen di bawah diagonal utama bernilai nol disebut matriks segitiga atas.
- Domain kognitif `classify/knowing`: Siswa diminta mengidentifikasi jenis matriks berdasarkan definisi formal elemen-elemennya. Ini adalah proses mengenali dan mengklasifikasikan objek matematika.. Bukti: B = \begin{bmatrix} 2 & 9 & -1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{bmatrix}; Tentukan jenis matriks-matriks berikut.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi berbagai jenis matriks (segitiga atas, bawah, diagonal, identitas).. Bukti: Tentukan jenis matriks-matriks berikut.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung, hanya memerlukan pengamatan visual terhadap elemen matriks dan pencocokan dengan definisi yang sudah dipelajari.. Bukti: B = \begin{bmatrix} 2 & 9 & -1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{bmatrix}; Tentukan jenis matriks-matriks berikut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi matriks segitiga atas, bawah, diagonal, dan identitas. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi matriks adalah dasar di kelas 11. Mengidentifikasi jenis matriks adalah tugas rutin yang sangat mendasar. |

Run 2 — solusi: Matriks B memiliki elemen-elemen di bawah diagonal utama (B21=0, B31=0, B32=0) yang semuanya bernilai nol. Berdasarkan definisi, matriks persegi dengan elemen di bawah diagonal utama nol adalah matriks segitiga atas.
- Domain kognitif `classify/knowing`: Siswa diminta mengidentifikasi jenis matriks berdasarkan definisi formal matriks segitiga atas. Ini adalah proses pengenalan sifat dasar matriks.. Bukti: Tentukan jenis matriks-matriks berikut.; B = [2 9 -1; 0 1 2; 0 0 1]
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konsep dasar mengenai klasifikasi matriks.. Bukti: Tentukan jenis matriks-matriks berikut.; B = [2 9 -1; 0 1 2; 0 0 1]
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya memerlukan pemeriksaan elemen matriks terhadap definisi matriks segitiga atas tanpa perhitungan kompleks.. Bukti: B = [2 9 -1; 0 1 2; 0 0 1]; Tentukan jenis matriks-matriks berikut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi matriks segitiga atas. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi matriks adalah dasar kelas 11. Soal ini adalah pengenalan konsep dasar yang sangat rutin. |

Run 3 — solusi: Matriks B memiliki elemen-elemen di bawah diagonal utama yang semuanya bernilai nol (b21=0, b31=0, b32=0), sedangkan elemen di atas diagonal utama tidak semuanya nol. Berdasarkan definisi, matriks persegi dengan elemen di bawah diagonal utama nol adalah matriks segitiga atas.
- Domain kognitif `classify/knowing`: Siswa perlu mengenali pola elemen matriks dan mencocokkannya dengan definisi formal matriks segitiga atas.. Bukti: B = \begin{bmatrix} 2 & 9 & -1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{bmatrix}; Tentukan jenis matriks-matriks berikut.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman definisi konseptual tentang jenis-jenis matriks.. Bukti: Tentukan jenis matriks-matriks berikut.
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya memerlukan pengamatan visual terhadap elemen matriks dan pengetahuan definisi dasar.. Bukti: B = \begin{bmatrix} 2 & 9 & -1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{bmatrix}

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi matriks persegi dan elemen diagonal utama. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi matriks adalah dasar kelas 11. Mengidentifikasi jenis matriks adalah tugas prosedural/konseptual dasar. |

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

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `-3/5`.
Solusi minimum hasil AI: Dari A = I, maka elemen-elemen yang bersesuaian sama: (1) -x-3y = 1 dan (2) (x-2y)^2 = 0. Dari (2), x = 2y. Substitusi ke (1): -(2y) - 3y = 1 => -5y = 1 => y = -1/5. Maka x = 2(-1/5) = -2/5. Nilai x + y = -2/5 + (-1/5) = -3/5.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a53a7b2717a74b73911437ee9ffea69db8b94d0bb142c8dbdb0fb445d8b9bede`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2131 |
| 2 | success | valid / verified | applying | procedural | Medium | 2970 |
| 3 | success | valid / verified | applying | procedural | Medium | 3005 |

Run 1 — solusi: Dari A = I, maka: (1) -x-3y = 1 dan (2) (x-2y)^2 = 0. Dari (2), x = 2y. Substitusi ke (1): -(2y) - 3y = 1 => -5y = 1 => y = -1/5. Maka x = 2(-1/5) = -2/5. Nilai x + y = -2/5 + (-1/5) = -3/5.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan definisi kesamaan dua matriks untuk membentuk sistem persamaan linear dan menyelesaikannya. Ini adalah penerapan prosedur rutin pada situasi yang diberikan.. Bukti: A = I; -x-3y = 1; (x-2y)^2 = 0
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman tentang konsep kesamaan matriks dan elemen matriks identitas untuk menyusun persamaan aljabar.. Bukti: A = I; matriks identitas berordo 2 × 2
- Intended difficulty `classify/Easy`: Soal memerlukan dua langkah rutin: menyamakan elemen matriks dan menyelesaikan sistem persamaan linear sederhana. Beban kalkulasi rendah dan prosedurnya standar.. Bukti: A = I; -x-3y = 1; (x-2y)^2 = 0

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep matriks identitas dan penyelesaian sistem persamaan linear dua variabel. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi matriks adalah dasar kelas 11 TL. Soal ini menguji pemahaman dasar kesamaan matriks tanpa kompleksitas tambahan. |

Run 2 — solusi: A=I berarti -x-3y=1 dan (x-2y)^2=0. Dari (x-2y)^2=0 diperoleh x=2y. Substitusi ke -x-3y=1 menghasilkan -2y-3y=1, sehingga -5y=1 atau y=-1/5. Maka x=2(-1/5)=-2/5. Nilai x+y = -2/5 - 1/5 = -3/5.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep kesamaan matriks untuk membentuk sistem persamaan linear dan menyelesaikannya secara rutin.. Bukti: A = I; -x-3y=1; (x-2y)^2=0
- Dimensi pengetahuan `classify/procedural`: Melibatkan prosedur aljabar rutin untuk menyelesaikan sistem persamaan linear dari elemen-elemen matriks yang bersesuaian.. Bukti: -x-3y=1; (x-2y)^2=0; x=2y
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman kesamaan matriks dan penyelesaian SPLDV. Meskipun prosedural, terdapat dua langkah yang saling terkait (sistem persamaan), membuatnya sedikit di atas level dasar.. Bukti: -x-3y=1; (x-2y)^2=0

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | SPLDV (Sistem Persamaan Linear Dua Variabel) |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Soal ini menguji kemampuan dasar dalam kesamaan matriks dan substitusi aljabar yang merupakan standar kelas 11. |

Run 3 — solusi: Dari A=I, diperoleh sistem persamaan: (1) -x-3y=1 dan (2) (x-2y)^2=0. Dari (2), x=2y. Substitusi ke (1): -(2y)-3y=1 => -5y=1 => y=-1/5. Maka x=2(-1/5)=-2/5. Nilai x+y = -2/5 - 1/5 = -3/5.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan definisi kesamaan dua matriks untuk membentuk sistem persamaan linear dan menyelesaikannya secara rutin.. Bukti: A = I; (x-2y)^2 = 0; -x-3y = 1
- Dimensi pengetahuan `classify/procedural`: Melibatkan prosedur aljabar untuk menyelesaikan sistem persamaan yang diturunkan dari definisi kesamaan matriks.. Bukti: A = I; x=2y; -5y=1
- Intended difficulty `classify/Medium`: Memerlukan dua langkah rutin (pembentukan sistem persamaan dan substitusi) serta pemahaman konsep kesamaan matriks.. Bukti: A = I; (x-2y)^2 = 0; -x-3y = 1

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sistem persamaan linear dua variabel (SPLDV) dan definisi kesamaan matriks. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Soal ini adalah latihan rutin untuk kelas 11 TL mengenai kesamaan matriks, memerlukan pemahaman dasar aljabar untuk menyelesaikan sistem persamaan yang dihasilkan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 1, "Medium": 2} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3692`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan definisi kesamaan dua matriks untuk membentuk sistem persamaan linear dan menyelesaikannya. Ini adalah penerapan prosedur rutin pada situasi yang diberikan.
- Dimensi pengetahuan `procedural`: Melibatkan prosedur aljabar rutin untuk menyelesaikan sistem persamaan linear yang diturunkan dari definisi kesamaan matriks.
- Intended difficulty `Easy`: Soal memerlukan dua langkah rutin: menyamakan elemen matriks dan menyelesaikan sistem persamaan linear sederhana. Beban kalkulasi rendah dan prosedurnya standar.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep matriks identitas dan penyelesaian sistem persamaan linear dua variabel. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi matriks adalah dasar kelas 11 TL. Soal ini menguji pemahaman dasar kesamaan matriks tanpa kompleksitas tambahan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
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
Solusi minimum hasil AI: Dari kesamaan matriks: (1) a+2b=3, (2) 2a+b=-3. Eliminasi: (1)x2-(2) -> 3b=9, b=3. Substitusi b=3 ke (1) -> a+6=3, a=-3. (3) c+d=7, (4) 2c+d=1. Eliminasi: (4)-(3) -> c=-6. Substitusi c=-6 ke (3) -> -6+d=7, d=13. Maka a+b+c+d = -3+3-6+13 = 7.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e93e4649df7fe043d7217bea969f403aca3f2a41536c85ea0b530bd2d796019f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2213 |
| 2 | success | valid / verified | applying | procedural | Easy | 2185 |
| 3 | success | valid / verified | applying | procedural | Easy | 2227 |

Run 1 — solusi: Dari kesamaan matriks: (1) a+2b=3, (2) 2a+b=-3. Eliminasi: (1)x2-(2) -> 3b=9, b=3. Substitusi b=3 ke (1) -> a+6=3, a=-3. (3) c+d=7, (4) 2c+d=1. Eliminasi: (4)-(3) -> c=-6. Substitusi c=-6 ke (3) -> -6+d=7, d=13. Maka a+b+c+d = -3+3-6+13 = 7.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep kesamaan matriks untuk membentuk sistem persamaan linear dua variabel (SPLDV) dan menyelesaikannya secara rutin. Ini adalah penerapan prosedur standar.. Bukti: a+2b=3, 2a+b=-3; c+d=7, 2c+d=1; Hitunglah nilai a + b + c + d
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang definisi kesamaan matriks dan penggunaan algoritma SPLDV untuk mencari nilai variabel.. Bukti: kesamaan matriks; a+2b=3, 2a+b=-3; c+d=7, 2c+d=1
- Intended difficulty `classify/Easy`: Soal ini melibatkan dua sistem persamaan linear dua variabel yang terpisah namun rutin. Tidak ada strategi non-rutin atau integrasi konsep yang kompleks.. Bukti: a+2b=3, 2a+b=-3; c+d=7, 2c+d=1

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang kesamaan matriks dan metode eliminasi/substitusi SPLDV. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun matriks adalah materi kelas 11, penyelesaian SPLDV adalah prasyarat yang sangat mendasar dan rutin bagi siswa SMA. |

Run 2 — solusi: Dari kesamaan matriks, diperoleh dua sistem persamaan linear: (1) a+2b=3 dan 2a+b=-3. Menjumlahkan keduanya: 3a+3b=0 -> a+b=0. (2) c+d=7 dan 2c+d=1. Mengurangi (2) dari (1): (2c+d)-(c+d)=1-7 -> c=-6. Substitusi c=-6 ke c+d=7 -> d=13. Maka a+b+c+d = 0 + (-6) + 13 = 7.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan definisi kesamaan matriks untuk membentuk sistem persamaan linear dua variabel (SPLDV) dan menyelesaikannya secara rutin. Tidak ada strategi non-rutin yang diperlukan.. Bukti: a+2b=3 dan 2a+b=-3; c+d=7 dan 2c+d=1; Hitunglah nilai a + b + c + d
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana menyelesaikan sistem persamaan linear yang diturunkan dari konsep kesamaan matriks.. Bukti: kesamaan matriks; a+2b=3 dan 2a+b=-3
- Intended difficulty `classify/Easy`: Soal ini melibatkan prosedur standar SPLDV yang familiar bagi siswa kelas 11. Beban komputasi rendah dan langkah-langkahnya rutin.. Bukti: a+2b=3 dan 2a+b=-3; c+d=7 dan 2c+d=1

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sistem Persamaan Linear Dua Variabel (SPLDV) |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi kesamaan matriks adalah dasar di kelas 11. Soal ini hanya memerlukan manipulasi aljabar dasar tanpa kompleksitas tambahan. |

Run 3 — solusi: Dari kesamaan matriks: 1) a+2b=3 dan 2a+b=-3. Eliminasi/substitusi: (a+2b) + (2a+b) = 0 -> 3(a+b)=0 -> a+b=0. 2) c+d=7 dan 2c+d=1. Kurangi: (2c+d)-(c+d) = 1-7 -> c=-6. Substitusi c ke c+d=7 -> -6+d=7 -> d=13. Maka c+d=7. Nilai a+b+c+d = (a+b) + (c+d) = 0 + 7 = 7.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep kesamaan matriks untuk membentuk sistem persamaan linear dua variabel (SPLDV) dan menyelesaikannya secara rutin untuk mendapatkan nilai variabel, kemudian menjumlahkannya.. Bukti: a+2b=3 dan 2a+b=-3; c+d=7 dan 2c+d=1; Hitunglah nilai a + b + c + d
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menyelesaikan sistem persamaan linear yang diturunkan dari definisi kesamaan dua matriks.. Bukti: kesamaan matriks; a+2b=3 dan 2a+b=-3
- Intended difficulty `classify/Easy`: Soal ini melibatkan dua sistem persamaan linear dua variabel yang terpisah namun rutin. Tidak ada strategi non-rutin atau integrasi konsep yang kompleks.. Bukti: a+2b=3 dan 2a+b=-3; c+d=7 dan 2c+d=1

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sistem Persamaan Linear Dua Variabel (SPLDV) |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun matriks adalah materi kelas 11, penyelesaian SPLDV adalah prasyarat dasar yang rutin bagi siswa kelas 11. Beban komputasi rendah dan langkah-langkahnya sangat standar. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `5b5856cb7882715fb808648e`

$\begin{bmatrix} 2x & y \\ 3z & z \end{bmatrix} - \begin{bmatrix} 6 & -x \\ 2y & 7 \end{bmatrix} + \begin{bmatrix} 2 & 1 \\ -9 & 6 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$<br><br>Tentukan $x, y$, dan $z$.

| Opsi | Isi |
|---|---|
| A | x = -2, y = -3, z = 1 |
| B | x = 2, y = -3, z = 1 |
| C | x = 2, y = 3, z = 1 |
| D | x = 2, y = -3, z = -1 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `x = 2, y = -3, z = 1`.
Solusi minimum hasil AI: Dari elemen (1,1): 2x-6+2=0 -> 2x=4 -> x=2. Dari elemen (1,2): y-(-x)+1=0 -> y+2+1=0 -> y=-3. Dari elemen (2,2): z-7+6=0 -> z=1. Verifikasi elemen (2,1): 3z-2y-9 = 3(1)-2(-3)-9 = 3+6-9=0. Solusi: x=2, y=-3, z=1.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c7717ee108cc23560ee530c44c1745bdcc897bb6b6c4741be476ad97f2960d1d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3623 |
| 2 | success | valid / verified | applying | procedural | Easy | 3232 |
| 3 | success | valid / verified | applying | procedural | Easy | 3445 |

Run 1 — solusi: Dari elemen (1,1): 2x-6+2=0 -> 2x=4 -> x=2. Dari elemen (1,2): y-(-x)+1=0 -> y+2+1=0 -> y=-3. Dari elemen (2,2): z-7+6=0 -> z=1. Verifikasi elemen (2,1): 3z-2y-9 = 3(1)-2(-3)-9 = 3+6-9=0. Solusi: x=2, y=-3, z=1.
- Domain kognitif `classify/applying`: Siswa menerapkan prosedur rutin penjumlahan dan pengurangan matriks untuk membentuk sistem persamaan linear sederhana.. Bukti: 2x - 6 + 2 = 0; y - (-x) + 1 = 0; z - 7 + 6 = 0
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang operasi matriks dan kesamaan dua matriks.. Bukti: 2x - 6 + 2 = 0; y - (-x) + 1 = 0; z - 7 + 6 = 0
- Intended difficulty `classify/Easy`: Prosedur standar, langkah rutin, beban komputasi rendah.. Bukti: 2x - 6 + 2 = 0; y - (-x) + 1 = 0; z - 7 + 6 = 0

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi dasar matriks dan penyelesaian SPLDV sederhana. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi dasar matriks kelas 11, tidak memerlukan strategi kompleks. |

Run 2 — solusi: Dari elemen (1,1): 2x-6+2=0 -> 2x=4 -> x=2. Dari elemen (1,2): y-(-x)+1=0 -> y+2+1=0 -> y=-3. Dari elemen (2,2): z-7+6=0 -> z=1. Verifikasi elemen (2,1): 3z-2y-9 = 3(1)-2(-3)-9 = 3+6-9=0. Solusi: x=2, y=-3, z=1.
- Domain kognitif `classify/applying`: Siswa menerapkan prosedur penjumlahan dan pengurangan matriks untuk membentuk sistem persamaan linear sederhana.. Bukti: 2x - 6 + 2 = 0; y - (-x) + 1 = 0; 3z - 2y - 9 = 0; z - 7 + 6 = 0
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penerapan algoritma operasi matriks dan penyelesaian sistem persamaan linear.. Bukti: 2x - 6 + 2 = 0; y - (-x) + 1 = 0; z - 7 + 6 = 0
- Intended difficulty `classify/Easy`: Prosedur standar, langkah-langkah rutin, beban komputasi rendah.. Bukti: 2x - 6 + 2 = 0; y - (-x) + 1 = 0; 3z - 2y - 9 = 0; z - 7 + 6 = 0

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi dasar matriks dan penyelesaian SPLDV. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 3 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi dasar matriks kelas 11, tidak memerlukan strategi kompleks. |

Run 3 — solusi: Dari elemen (1,1): 2x-6+2=0 => 2x=4 => x=2. Dari elemen (1,2): y-(-x)+1=0 => y+2+1=0 => y=-3. Dari elemen (2,2): z-7+6=0 => z=1. Verifikasi elemen (2,1): 3z-2y-9 = 3(1)-2(-3)-9 = 3+6-9=0. Semua elemen konsisten.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan operasi penjumlahan dan pengurangan matriks untuk membentuk sistem persamaan linear sederhana dan menyelesaikannya secara berurutan.. Bukti: 2x - 6 + 2 = 0; y - (-x) + 1 = 0; 3z - 2y - 9 = 0; z - 7 + 6 = 0
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penerapan algoritma operasi matriks dan teknik penyelesaian sistem persamaan linear.. Bukti: 2x - 6 + 2 = 0; y - (-x) + 1 = 0; 3z - 2y - 9 = 0; z - 7 + 6 = 0
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur rutin yang melibatkan operasi matriks dasar dan penyelesaian SPLDV sederhana. Tidak ada strategi nonrutin atau integrasi konsep yang kompleks.. Bukti: 2x - 6 + 2 = 0; y - (-x) + 1 = 0; 3z - 2y - 9 = 0; z - 7 + 6 = 0

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi dasar matriks (penjumlahan/pengurangan) dan penyelesaian sistem persamaan linear satu/dua variabel. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 3 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi matriks kelas 11 TL mencakup operasi matriks. Soal ini menguji pemahaman dasar operasi matriks tanpa kompleksitas tambahan, sehingga dikategorikan Easy. |

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

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Persamaan matriks menghasilkan sistem: (1) 3a + 4b = 1 dan (2) 4a + 3b = -1. Kalikan (1) dengan 3 dan (2) dengan 4: 9a + 12b = 3 dan 16a + 12b = -4. Kurangi kedua persamaan: -7a = 7, maka a = -1. Substitusi a = -1 ke (1): 3(-1) + 4b = 1, -3 + 4b = 1, 4b = 4, maka b = 1.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `29ba6d472140179964dc8a156b3452af8a8e54bff4f3fd3c807a6116fd461e22`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2169 |
| 2 | success | valid / verified | applying | procedural | Easy | 2151 |
| 3 | success | valid / verified | applying | procedural | Easy | 2977 |

Run 1 — solusi: Persamaan matriks menghasilkan sistem: (1) 3a + 4b = 1 dan (2) 4a + 3b = -1. Kalikan (1) dengan 3 dan (2) dengan 4: 9a + 12b = 3 dan 16a + 12b = -4. Kurangi kedua persamaan: -7a = 7, maka a = -1. Substitusi a = -1 ke (1): 3(-1) + 4b = 1, -3 + 4b = 1, 4b = 4, maka b = 1.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan persamaan matriks menjadi sistem persamaan linear dua variabel (SPLDV) dan menerapkan prosedur eliminasi/substitusi rutin untuk menyelesaikannya.. Bukti: 3a + 4b = 1; 4a + 3b = -1
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi penjumlahan matriks dan teknik penyelesaian sistem persamaan linear.. Bukti: 3a + 4b = 1; 4a + 3b = -1
- Intended difficulty `classify/Easy`: Soal ini adalah prosedur standar yang melibatkan penjumlahan matriks dan SPLDV. Tidak ada langkah non-rutin atau integrasi konsep yang kompleks.. Bukti: 3a + 4b = 1; 4a + 3b = -1

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan matriks dan metode eliminasi/substitusi SPLDV. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi matriks ada di kelas 11, soal ini hanya memerlukan kemampuan dasar SPLDV yang sudah dikuasai sejak SMP/kelas 10, sehingga beban kognitifnya rendah untuk siswa kelas 11. |

Run 2 — solusi: Persamaan matriks menghasilkan sistem: 3a + 4b = 1 dan 4a + 3b = -1. Kalikan (1) dengan 3 dan (2) dengan 4: 9a + 12b = 3 dan 16a + 12b = -4. Kurangi kedua persamaan: -7a = 7, maka a = -1. Substitusi a = -1 ke 3(-1) + 4b = 1, diperoleh -3 + 4b = 1, 4b = 4, maka b = 1.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan persamaan matriks menjadi sistem persamaan linear dua variabel (SPLDV) dan menyelesaikannya menggunakan metode eliminasi atau substitusi yang merupakan prosedur rutin.. Bukti: 3a + 4b = 1; 4a + 3b = -1
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang definisi penjumlahan matriks dan penerapan algoritma penyelesaian sistem persamaan linear.. Bukti: 3a + 4b = 1; 4a + 3b = -1
- Intended difficulty `classify/Easy`: Soal ini melibatkan prosedur standar yang familiar bagi siswa kelas 11. Tidak ada langkah non-rutin atau integrasi konsep yang kompleks.. Bukti: 3a + 4b = 1; 4a + 3b = -1

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan matriks dan penyelesaian SPLDV. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi matriks, tingkat kesulitan soal ini rendah karena hanya melibatkan sistem persamaan linear dua variabel sederhana yang sudah dikuasai sejak SMP. |

Run 3 — solusi: Penjumlahan matriks menghasilkan sistem persamaan linear: 3a + 4b = 1 dan 4a + 3b = -1. Dengan eliminasi, 16a + 12b = -4 dan 9a + 12b = 3, dikurangi menjadi 7a = -7, sehingga a = -1. Substitusi a = -1 ke 3a + 4b = 1 menghasilkan -3 + 4b = 1, sehingga b = 1.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan definisi penjumlahan matriks untuk membentuk sistem persamaan linear dua variabel, kemudian menyelesaikannya menggunakan prosedur rutin (eliminasi/substitusi).. Bukti: \begin{bmatrix} 3a \\ 3b \end{bmatrix}+\begin{bmatrix} 4b \\ 4a \end{bmatrix}=\begin{bmatrix} 1 \\ -1 \end{bmatrix}
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi matriks dan penyelesaian sistem persamaan linear.. Bukti: \begin{bmatrix} 3a \\ 3b \end{bmatrix}+\begin{bmatrix} 4b \\ 4a \end{bmatrix}=\begin{bmatrix} 1 \\ -1 \end{bmatrix}
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar yang familiar bagi siswa kelas 11, melibatkan operasi matriks dasar dan penyelesaian SPLDV tanpa kompleksitas tambahan.. Bukti: \begin{bmatrix} 3a \\ 3b \end{bmatrix}+\begin{bmatrix} 4b \\ 4a \end{bmatrix}=\begin{bmatrix} 1 \\ -1 \end{bmatrix}

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan matriks dan penyelesaian SPLDV. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini menguji keterampilan dasar operasi matriks yang merupakan prasyarat untuk materi matriks lebih lanjut di kelas 11. |

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
Solusi minimum hasil AI: Persamaan P - 2X = 3Q diubah menjadi 2X = P - 3Q, sehingga X = 0.5(P - 3Q). 3Q = [[9, 6], [-3, 6]]. P - 3Q = [[1-9, -8-6], [-1-(-3), -2-6]] = [[-8, -14], [2, -8]]. X = 0.5 * [[-8, -14], [2, -8]] = [[-4, -7], [1, -4]].
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b42a05d4b327ef750466bd492a7e023b60b62ef89b939ba93a9ad5a19edab6c0`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3208 |
| 2 | success | valid / verified | applying | procedural | Easy | 3308 |
| 3 | success | valid / verified | applying | procedural | Medium | 3172 |

Run 1 — solusi: 2X = P - 3Q, maka X = 0.5 * (P - 3Q). 3Q = [[9, 6], [-3, 6]]. P - 3Q = [[1-9, -8-6], [-1-(-3), -2-6]] = [[-8, -14], [2, -8]]. X = 0.5 * [[-8, -14], [2, -8]] = [[-4, -7], [1, -4]].
- Domain kognitif `classify/applying`: Siswa perlu menerapkan operasi aljabar matriks (perkalian skalar dan pengurangan) untuk mengisolasi variabel X dalam persamaan linear matriks.. Bukti: P - 2X = 3Q; Tentukan matriks X
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penguasaan algoritma operasi matriks dasar (prosedural) untuk menyelesaikan persamaan.. Bukti: P = [1 -8; -1 -2], Q = [3 2; -1 2]; P - 2X = 3Q
- Intended difficulty `classify/Easy`: Soal ini merupakan latihan rutin operasi matriks yang langsung, tidak memerlukan strategi non-rutin atau integrasi representasi yang kompleks.. Bukti: P - 2X = 3Q; matriks berordo 2x2

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi dasar matriks (penjumlahan, pengurangan, perkalian skalar) dan aljabar linear dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah standar prosedur matriks kelas 11 yang bersifat rutin dan langsung, sesuai untuk tingkat kesulitan rendah. |

Run 2 — solusi: 2X = P - 3Q => X = 0.5(P - 3Q). 3Q = [[9, 6], [-3, 6]]. P - 3Q = [[1-9, -8-6], [-1-(-3), -2-6]] = [[-8, -14], [2, -8]]. X = [[-4, -7], [1, -4]].
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur aljabar matriks (pengurangan dan perkalian skalar) untuk mengisolasi variabel X.. Bukti: P - 2X = 3Q; Tentukan matriks X
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma operasi matriks dasar.. Bukti: P - 2X = 3Q
- Intended difficulty `classify/Easy`: Masalah ini adalah prosedur rutin yang melibatkan operasi matriks standar tanpa kendala tambahan atau strategi non-rutin.. Bukti: P - 2X = 3Q; Tentukan matriks X

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi dasar matriks (penjumlahan, pengurangan, perkalian skalar) |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 11 karena merupakan aplikasi langsung dari operasi matriks yang dipelajari. |

Run 3 — solusi: Persamaan P - 2X = 3Q diubah menjadi 2X = P - 3Q, sehingga X = 0.5(P - 3Q). 3Q = [[9, 6], [-3, 6]]. P - 3Q = [[1-9, -8-6], [-1-(-3), -2-6]] = [[-8, -14], [2, -8]]. X = 0.5 * [[-8, -14], [2, -8]] = [[-4, -7], [1, -4]].
- Domain kognitif `classify/applying`: Siswa perlu menerapkan operasi aljabar matriks (pengurangan dan perkalian skalar) untuk mengisolasi variabel X dalam persamaan linear matriks.. Bukti: P - 2X = 3Q; Tentukan matriks X
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penerapan algoritma standar operasi matriks (perkalian skalar, pengurangan) untuk menyelesaikan persamaan matriks.. Bukti: P - 2X = 3Q; Tentukan matriks X
- Intended difficulty `classify/Medium`: Soal memerlukan manipulasi aljabar untuk mengisolasi X sebelum melakukan operasi matriks, melibatkan beberapa langkah rutin yang saling terkait.. Bukti: P - 2X = 3Q; Tentukan matriks X

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi dasar matriks (penjumlahan, pengurangan, perkalian skalar) |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 11 karena melibatkan manipulasi persamaan matriks yang merupakan standar kurikulum. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 2, "Medium": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3753`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur aljabar matriks (pengurangan dan perkalian skalar) untuk mengisolasi variabel X dalam persamaan linear matriks.
- Dimensi pengetahuan `procedural`: Soal ini menuntut penerapan algoritma standar operasi matriks (perkalian skalar, pengurangan) untuk menyelesaikan persamaan matriks.
- Intended difficulty `Easy`: Soal ini adalah prosedur rutin yang melibatkan operasi matriks standar tanpa kendala tambahan atau strategi non-rutin. Manipulasi aljabar untuk mengisolasi X adalah langkah standar.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi dasar matriks (penjumlahan, pengurangan, perkalian skalar) dan aljabar linear dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 11 karena merupakan aplikasi langsung dari operasi matriks yang dipelajari. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
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

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `3`.
Solusi minimum hasil AI: Perkalian matriks: baris 1 kolom 1 adalah -4(x-2) + 9 = -4x + 17. Diketahui hasilnya -3, maka -4x + 17 = -3, sehingga x = 5. Baris 1 kolom 2 adalah (x-2)(0) + 9(y+1) = 9(y+1). Diketahui hasilnya -9, maka 9(y+1) = -9, sehingga y+1 = -1, y = -2. Maka x + y = 5 + (-2) = 3.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c40bb01764b01a154b889a68a84ed5726ab0d2982d1323780e69eaf38273cbe7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2218 |
| 2 | success | valid / verified | applying | procedural | Medium | 2810 |
| 3 | success | valid / verified | applying | procedural | Medium | 3100 |

Run 1 — solusi: Perkalian matriks: baris 1 kolom 1: (x-2)(-4) + 9(1) = -4x + 8 + 9 = -4x + 17. Diketahui hasilnya -3, maka -4x + 17 = -3 -> -4x = -20 -> x = 5. Baris 1 kolom 2: (x-2)(0) + 9(y+1) = 9y + 9. Diketahui hasilnya -9, maka 9y + 9 = -9 -> 9y = -18 -> y = -2. Maka x + y = 5 + (-2) = 3.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan algoritma perkalian matriks untuk membentuk sistem persamaan linear sederhana dan menyelesaikannya. Ini adalah prosedur rutin yang melibatkan pemilihan elemen yang tepat untuk mencari variabel.. Bukti: Diketahui [x-2 9; -3 0][ -4 0; 1 y+1] = [-3 -9; 12 0]; Tentukan x+y
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang operasi matriks (perkalian) dan penyelesaian sistem persamaan linear dua variabel.. Bukti: Perkalian matriks; sistem persamaan linear
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 11. Langkah-langkahnya jelas: melakukan perkalian matriks, menyamakan elemen, dan menyelesaikan persamaan linear sederhana. Tidak ada strategi non-rutin atau integrasi konsep yang kompleks.. Bukti: Diketahui [x-2 9; -3 0][ -4 0; 1 y+1] = [-3 -9; 12 0]; Tentukan x+y

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi dasar matriks dan penyelesaian SPLDV sederhana. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi perkalian matriks adalah standar kelas 11 TL. Soal ini menguji pemahaman dasar tanpa variasi yang menyulitkan. |

Run 2 — solusi: Perkalian matriks menghasilkan sistem persamaan: -4x + 17 = -3 (x=5) dan 9y + 9 = -9 (y=-2). Maka x + y = 5 + (-2) = 3.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan algoritma perkalian matriks untuk membentuk sistem persamaan linear dan menyelesaikannya untuk mendapatkan nilai variabel.. Bukti: Perkalian matriks menghasilkan sistem persamaan: -4x + 17 = -3 (x=5) dan 9y + 9 = -9 (y=-2)
- Dimensi pengetahuan `classify/procedural`: Melibatkan penerapan algoritma perkalian matriks dan teknik aljabar dasar untuk menyelesaikan sistem persamaan.. Bukti: Perkalian matriks menghasilkan sistem persamaan
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah rutin (perkalian matriks dan penyelesaian dua persamaan linear) yang saling terkait.. Bukti: Perkalian matriks menghasilkan sistem persamaan: -4x + 17 = -3 (x=5) dan 9y + 9 = -9 (y=-2)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian matriks 2x2 dan aljabar linear dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan prosedur rutin bagi siswa kelas 11, namun menuntut ketelitian dalam melakukan dua operasi aljabar secara simultan. |

Run 3 — solusi: Perkalian matriks menghasilkan sistem persamaan: -4(x-2) + 9 = -3 => -4x + 17 = -3 => x = 5. Dan 9(y+1) = -9 => y+1 = -1 => y = -2. Maka x+y = 5 + (-2) = 3.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur perkalian matriks untuk membentuk sistem persamaan linear dan menyelesaikannya.. Bukti: Diketahui [x-2 9; -3 0][ -4 0; 1 y+1] = [-3 -9; 12 0]
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma perkalian matriks dan penyelesaian sistem persamaan linear sederhana.. Bukti: Diketahui [x-2 9; -3 0][ -4 0; 1 y+1] = [-3 -9; 12 0]
- Intended difficulty `classify/Medium`: Memerlukan beberapa langkah rutin (perkalian matriks, pembentukan persamaan, penyelesaian SPL) yang saling terkait.. Bukti: Diketahui [x-2 9; -3 0][ -4 0; 1 y+1] = [-3 -9; 12 0]

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi dasar matriks dan penyelesaian SPLDV. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 11, menguji pemahaman prosedur perkalian matriks dan penyelesaian variabel. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 1, "Medium": 2} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3865`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan algoritma perkalian matriks untuk membentuk sistem persamaan linear dan menyelesaikannya. Ini adalah prosedur rutin yang melibatkan pemilihan elemen yang tepat untuk mencari variabel.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman prosedural tentang operasi matriks (perkalian) dan penyelesaian sistem persamaan linear dua variabel.
- Intended difficulty `Easy`: Soal ini bersifat rutin bagi siswa kelas 11. Langkah-langkahnya jelas: melakukan perkalian matriks, menyamakan elemen, dan menyelesaikan persamaan linear sederhana. Tidak ada strategi non-rutin atau integrasi konsep yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi dasar matriks dan penyelesaian SPLDV sederhana. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi perkalian matriks adalah standar kelas 11 TL. Soal ini menguji pemahaman dasar tanpa variasi yang menyulitkan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
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
Solusi minimum hasil AI: det(A) = (2)(2) - (5)(1) = -1. det(B) = (2)(1) - (2)(-3) = 8. Karena AC = B, maka det(A)det(C) = det(B), sehingga det(C) = det(B)/det(A) = 8/(-1) = -8.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c6bc9a47a3dc168afb1c96fbaaa781c784cd27d13fd334708c5886cc45f445b5`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2740 |
| 2 | success | valid / verified | applying | procedural | Medium | 2841 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2150 |

Run 1 — solusi: det(A) = (2)(2) - (5)(1) = -1. det(B) = (2)(1) - (2)(-3) = 8. Karena AC=B, maka det(A)det(C) = det(B), sehingga det(C) = det(B)/det(A) = 8/(-1) = -8.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan sifat determinan perkalian matriks det(AC) = det(A)det(C) untuk menemukan determinan C. Ini adalah penerapan langsung dari konsep yang dipelajari.. Bukti: AC = B; Tentukan determinan C
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma perhitungan determinan dan sifat distributif determinan terhadap perkalian matriks.. Bukti: A = [2 5; 1 2], B = [2 2; -3 1]
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, hanya memerlukan pemahaman dasar tentang sifat determinan matriks 2x2 tanpa langkah non-rutin.. Bukti: Tentukan determinan C

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perhitungan determinan matriks 2x2 dan sifat determinan perkalian matriks. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal standar kelas 11 Matematika Tingkat Lanjut yang menguji penguasaan prosedur dasar matriks. |

Run 2 — solusi: det(A) = (2)(2)-(5)(1) = -1. det(B) = (2)(1)-(2)(-3) = 8. Karena AC=B, maka det(A)det(C)=det(B), sehingga -1*det(C)=8, maka det(C)=-8.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan sifat determinan det(AC) = det(A)det(C) = det(B) untuk menyelesaikan soal, bukan sekadar menghitung determinan matriks secara langsung.. Bukti: AC = B; Tentukan determinan C
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedur penggunaan sifat-sifat determinan matriks dalam persamaan matriks.. Bukti: AC = B; Tentukan determinan C
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemahaman sifat determinan det(AC)=det(A)det(C) daripada sekadar menghitung determinan matriks secara langsung.. Bukti: A = [2 5; 1 2]; B = [2 2; -3 1]; AC = B

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat determinan matriks dan operasi determinan 2x2. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini berada pada tingkat Medium karena memerlukan pemahaman sifat determinan det(AC)=det(A)det(C) daripada sekadar menghitung determinan matriks secara langsung. |

Run 3 — solusi: Diketahui AC = B. Maka det(AC) = det(B), sehingga det(A)det(C) = det(B). det(A) = (2)(2) - (5)(1) = 4 - 5 = -1. det(B) = (2)(1) - (2)(-3) = 2 + 6 = 8. Maka det(C) = det(B)/det(A) = 8/(-1) = -8.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan sifat determinan matriks det(AB) = det(A)det(B) untuk menyelesaikan persamaan matriks, yang merupakan prosedur standar dalam aljabar matriks.. Bukti: AC = B; Tentukan determinan C
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara determinan dan operasi perkalian matriks (prinsip/konsep) serta prosedur menghitung determinan matriks 2x2.. Bukti: AC = B; Tentukan determinan C
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 11 yang mempelajari matriks. Prosedur yang diperlukan langsung (menggunakan sifat determinan) dengan beban komputasi yang rendah.. Bukti: A = [2 5; 1 2], B = [2 2; -3 1], AC = B; Tentukan determinan C

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi determinan matriks 2x2 dan sifat determinan perkalian matriks. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi determinan matriks adalah kurikulum standar kelas 11 TL. Soal ini tidak memerlukan manipulasi aljabar yang kompleks atau strategi non-rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 2, "Medium": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3664`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan sifat determinan perkalian matriks det(AC) = det(A)det(C) = det(B) untuk menyelesaikan soal. Ini adalah penerapan prosedur standar yang rutin dalam aljabar matriks.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman tentang hubungan antara determinan dan operasi perkalian matriks (prinsip/konsep) serta prosedur menghitung determinan matriks 2x2.
- Intended difficulty `Easy`: Soal ini bersifat rutin bagi siswa kelas 11 yang mempelajari matriks. Prosedur yang diperlukan langsung (menggunakan sifat determinan) dengan beban komputasi yang rendah.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi determinan matriks 2x2 dan sifat determinan perkalian matriks. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi determinan matriks adalah kurikulum standar kelas 11 TL. Soal ini tidak memerlukan manipulasi aljabar yang kompleks atau strategi non-rutin. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
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
Solusi minimum hasil AI: Menggunakan sifat invers matriks (AB^-1)^-1 = (B^-1)^-1 A^-1 = B A^-1. Maka, [5 1; 1 3] [1 4; 2 3] = [5(1)+1(2) 5(4)+1(3); 1(1)+3(2) 1(4)+3(3)] = [7 23; 7 13].
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6f47d54ad45e86be11ddd9854277dd5e486ee0982f8f2461cbbcf9d3e088bfa3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2934 |
| 2 | success | valid / verified | applying | procedural | Medium | 3309 |
| 3 | success | valid / verified | applying | procedural | Medium | 2282 |

Run 1 — solusi: Menggunakan sifat invers matriks (AB^-1)^-1 = (B^-1)^-1 A^-1 = B A^-1. Maka, [5 1; 1 3] [1 4; 2 3] = [5(1)+1(2) 5(4)+1(3); 1(1)+3(2) 1(4)+3(3)] = [7 23; 7 13].
- Domain kognitif `classify/applying`: Siswa perlu menerapkan sifat invers matriks (AB^-1)^-1 = B A^-1 dan melakukan operasi perkalian matriks untuk mendapatkan hasil akhir.. Bukti: Tentukan (AB^-1)^-1 jika diketahui A^-1 = [1 4; 2 3] dan B = [5 1; 1 3].
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang sifat-sifat aljabar matriks dan teknik perkalian matriks.. Bukti: Tentukan (AB^-1)^-1; A^-1 = [1 4; 2 3] dan B = [5 1; 1 3]
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman sifat invers matriks sebelum melakukan perkalian. Ini adalah langkah rutin dalam kurikulum kelas 11 TL.. Bukti: Tentukan (AB^-1)^-1 jika diketahui A^-1 = [1 4; 2 3] dan B = [5 1; 1 3].

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat invers matriks (AB)^-1 = B^-1 A^-1 dan (B^-1)^-1 = B, serta perkalian matriks. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi matriks dan sifat inversnya adalah standar kurikulum kelas 11 Matematika Tingkat Lanjut. |

Run 2 — solusi: Menggunakan sifat invers matriks (AB^-1)^-1 = (B^-1)^-1 A^-1 = B A^-1. Maka, [5 1; 1 3] [1 4; 2 3] = [5(1)+1(2) 5(4)+1(3); 1(1)+3(2) 1(4)+3(3)] = [7 23; 7 13].
- Domain kognitif `classify/applying`: Siswa perlu menerapkan sifat invers matriks (AB^-1)^-1 = B A^-1 dan melakukan perkalian matriks untuk mendapatkan hasil.. Bukti: (AB^{-1})^{-1} = B A^{-1}
- Dimensi pengetahuan `classify/procedural`: Memerlukan pemahaman prosedur perkalian matriks dan sifat aljabar invers matriks.. Bukti: (AB^{-1})^{-1} = B A^{-1}
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman sifat invers matriks dan perkalian matriks. Ini adalah prosedur rutin dalam aljabar matriks.. Bukti: (AB^{-1})^{-1} = B A^{-1}; A^{-1} = \begin{bmatrix} 1 & 4 \\ 2 & 3 \end{bmatrix}; B = \begin{bmatrix} 5 & 1 \\ 1 & 3 \end{bmatrix}

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian matriks dan sifat invers matriks (AB)^-1 = B^-1 A^-1. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 11 TL karena menguji pemahaman sifat invers matriks yang merupakan materi inti. |

Run 3 — solusi: Menggunakan sifat invers matriks (AB^-1)^-1 = (B^-1)^-1 A^-1 = B A^-1. Diketahui B = [[5,1],[1,3]] dan A^-1 = [[1,4],[2,3]]. Maka, B A^-1 = [[5,1],[1,3]] * [[1,4],[2,3]] = [[5*1+1*2, 5*4+1*3], [1*1+3*2, 1*4+3*3]] = [[7, 23], [7, 13]].
- Domain kognitif `classify/applying`: Siswa perlu menerapkan sifat aljabar matriks (AB^-1)^-1 = B A^-1 untuk menyederhanakan ekspresi sebelum melakukan perkalian matriks. Ini adalah penerapan prosedur rutin dalam konteks aljabar matriks.. Bukti: Tentukan (AB^-1)^-1 jika diketahui A^-1 = [[1,4],[2,3]] dan B = [[5,1],[1,3]]
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan dan prinsip sifat-sifat invers matriks (konseptual) serta eksekusi algoritma perkalian matriks (prosedural).. Bukti: (AB^-1)^-1 = B A^-1
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman sifat invers matriks untuk menghindari perhitungan invers yang tidak perlu. Langkah-langkahnya rutin dan terstruktur.. Bukti: Tentukan (AB^-1)^-1 jika diketahui A^-1 = [[1,4],[2,3]] dan B = [[5,1],[1,3]]

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat-sifat invers matriks dan perkalian matriks. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi matriks adalah standar kelas 11 TL. Soal ini menuntut pemilihan strategi (menggunakan sifat invers) daripada sekadar menghitung invers A dan B secara manual, yang sesuai dengan tingkat kesulitan menengah. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
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
Solusi minimum hasil AI: Misal x = jenis I, y = jenis II. Sistem: x + y = 40 dan 35.000x + 24.000y = 1.103.000. Dari x = 40 - y, substitusi ke persamaan kedua: 35.000(40 - y) + 24.000y = 1.103.000 => 1.400.000 - 35.000y + 24.000y = 1.103.000 => -11.000y = -297.000 => y = 27. Maka x = 40 - 27 = 13.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a9aa33caa752bdeca18f6b8f973777f8813d39fb707cde707f7c250bbdf4ee78`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2394 |
| 2 | success | valid / verified | applying | procedural | Easy | 2441 |
| 3 | success | valid / verified | applying | procedural | Easy | 2427 |

Run 1 — solusi: Misal x = jenis I, y = jenis II. Sistem: x + y = 40 dan 35.000x + 24.000y = 1.103.000. Dari x = 40 - y, substitusi ke persamaan kedua: 35.000(40 - y) + 24.000y = 1.103.000 => 1.400.000 - 35.000y + 24.000y = 1.103.000 => -11.000y = -297.000 => y = 27. Maka x = 40 - 27 = 13.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan masalah kontekstual ke dalam model matematika (SPLDV) dan menerapkan prosedur aljabar rutin (substitusi atau eliminasi) untuk menyelesaikannya.. Bukti: x+y=40; 35.000x+24.000y=1.103.000
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut pemahaman tentang bagaimana menyusun dan menyelesaikan sistem persamaan linear dua variabel sebagai teknik prosedural standar.. Bukti: x+y=40; 35.000x+24.000y=1.103.000
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur rutin yang familiar bagi siswa SMA. Meskipun berada di kelas 11, materi SPLDV adalah prasyarat dasar yang tidak memerlukan strategi nonrutin atau integrasi konsep kompleks.. Bukti: 40 kuas lukis; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00; uang yang didapat oleh toko tersebut Rp1.103.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan dasar aljabar untuk menyelesaikan sistem persamaan linear dua variabel. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun SPLDV adalah materi kelas 10, soal ini dinilai sebagai Easy karena merupakan penerapan langsung prosedur standar tanpa kompleksitas tambahan yang menjadi ciri khas matematika tingkat lanjut kelas 11. |

Run 2 — solusi: Misal x = jumlah kuas I, y = jumlah kuas II. Sistem: x + y = 40 dan 35.000x + 24.000y = 1.103.000. Dari x = 40 - y, substitusi ke persamaan kedua: 35.000(40 - y) + 24.000y = 1.103.000 => 1.400.000 - 35.000y + 24.000y = 1.103.000 => -11.000y = -297.000 => y = 27. Maka x = 40 - 27 = 13. Jadi, 13 kuas jenis I dan 27 kuas jenis II.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan masalah kontekstual ke dalam model matematika (SPLDV) dan menerapkan prosedur penyelesaian rutin (substitusi atau eliminasi) untuk menemukan nilai variabel.. Bukti: Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma penyelesaian sistem persamaan linear dua variabel, yang merupakan prosedur standar dalam aljabar.. Bukti: x+y=40 dan 35.000x+24.000y=1.103.000
- Intended difficulty `classify/Easy`: Soal ini merupakan aplikasi langsung dari SPLDV dengan dua variabel. Meskipun konteksnya cerita, langkah penyelesaiannya bersifat rutin dan familiar bagi siswa SMA.. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang sistem persamaan linear dua variabel dan operasi aritmatika. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun SPLDV adalah materi SMP, soal ini diberikan dalam konteks kelas 11 sebagai prasyarat. Tingkat kesulitan rendah karena prosedurnya sangat standar dan tidak memerlukan strategi non-rutin. |

Run 3 — solusi: Misal x = jenis I, y = jenis II. Sistem: x + y = 40 dan 35.000x + 24.000y = 1.103.000. Dari x = 40 - y, substitusi ke persamaan kedua: 35.000(40 - y) + 24.000y = 1.103.000 => 1.400.000 - 35.000y + 24.000y = 1.103.000 => -11.000y = -297.000 => y = 27. Maka x = 40 - 27 = 13.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan masalah kontekstual ke dalam model matematika sistem persamaan linear dua variabel dan menyelesaikannya menggunakan prosedur rutin (substitusi/eliminasi).. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma penyelesaian sistem persamaan linear dua variabel.. Bukti: x+y=40 dan 35.000x+24.000y=1.103.000
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari sistem persamaan linear dua variabel yang merupakan materi prasyarat. Meskipun konteksnya cerita, langkah penyelesaiannya bersifat rutin dan familiar bagi siswa SMA.. Bukti: Suatu toko alat lukis menjual 40 kuas lukis.; Harga kuas lukis jenis I Rp35.000,00 dan harga kuas lukis jenis II Rp24.000,00.; Jika uang yang didapat oleh toko tersebut Rp1.103.000,00

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
| gradeRelativeRationale | Materi SPLDV adalah prasyarat kelas 11. Soal ini tidak menuntut pemahaman mendalam tentang matematika tingkat lanjut, melainkan hanya aplikasi prosedur dasar. |

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
Solusi minimum hasil AI: Fungsi f(x) = -5x^7 + 2x^4 - 8 memiliki derajat n = 7 (ganjil) dan koefisien utama a = -5 (negatif). Untuk polinomial dengan derajat ganjil dan koefisien utama negatif, perilaku ujungnya adalah x -> -∞, f(x) -> ∞ (naik di kiri) dan x -> ∞, f(x) -> -∞ (turun di kanan).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2ae1854cf1d0191104db35535718c3a9dfb750b165a3a60ef175675d670df22d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2143 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2121 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2139 |

Run 1 — solusi: Fungsi f(x) = -5x^7 + 2x^4 - 8 memiliki derajat n = 7 (ganjil) dan koefisien utama a = -5 (negatif). Untuk polinomial dengan derajat ganjil dan koefisien utama negatif, perilaku ujungnya adalah x -> -∞, f(x) -> ∞ (naik di kiri) dan x -> ∞, f(x) -> -∞ (turun di kanan).
- Domain kognitif `classify/applying`: Siswa perlu mengenali hubungan antara derajat dan koefisien utama polinomial dengan perilaku ujung grafiknya. Ini adalah penerapan konsep dasar polinomial yang sudah dipelajari.. Bukti: Perilaku ujung fungsi polinomial f(x) = -5x^7 + 2x^4 - 8 adalah ….
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang sifat-sifat fungsi polinomial (derajat dan koefisien utama) dan bagaimana sifat tersebut menentukan perilaku grafik.. Bukti: Perilaku ujung fungsi polinomial f(x) = -5x^7 + 2x^4 - 8
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan prosedural bagi siswa kelas 11 yang telah mempelajari polinomial. Tidak ada langkah kompleks atau strategi nonrutin yang diperlukan.. Bukti: Perilaku ujung fungsi polinomial f(x) = -5x^7 + 2x^4 - 8

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang derajat polinomial dan koefisien utama. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah materi standar kelas 11 Matematika Tingkat Lanjut mengenai analisis fungsi polinomial. |

Run 2 — solusi: Fungsi f(x) = -5x^7 + 2x^4 - 8 memiliki derajat n=7 (ganjil) dan koefisien utama a=-5 (negatif). Untuk polinomial dengan derajat ganjil dan koefisien utama negatif, saat x -> -∞, f(x) -> ∞ (naik di kiri), dan saat x -> ∞, f(x) -> -∞ (turun di kanan).
- Domain kognitif `classify/applying`: Siswa perlu mengenali sifat dasar perilaku ujung polinomial berdasarkan derajat dan koefisien utama. Ini adalah penerapan langsung dari konsep yang sudah dipelajari.. Bukti: Perilaku ujung fungsi polinomial f(x) = -5x^7 + 2x^4 - 8 adalah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana derajat dan koefisien utama polinomial menentukan perilaku ujung grafik.. Bukti: Perilaku ujung fungsi polinomial
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung dengan satu konsep utama (perilaku ujung polinomial). Tidak ada langkah kompleks atau strategi non-rutin yang diperlukan.. Bukti: Perilaku ujung fungsi polinomial f(x) = -5x^7 + 2x^4 - 8

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang derajat polinomial dan koefisien utama. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi perilaku ujung polinomial adalah topik standar kelas 11 Matematika Tingkat Lanjut. Soal ini menguji pemahaman dasar tanpa variasi yang rumit. |

Run 3 — solusi: Fungsi f(x) = -5x^7 + 2x^4 - 8 memiliki derajat n=7 (ganjil) dan koefisien utama a=-5 (negatif). Untuk polinomial dengan derajat ganjil dan koefisien utama negatif, perilaku ujungnya adalah: saat x -> -∞, f(x) -> ∞ (naik di kiri) dan saat x -> ∞, f(x) -> -∞ (turun di kanan).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep perilaku ujung polinomial berdasarkan derajat dan koefisien utama. Ini adalah penerapan prosedur standar yang sudah dipelajari.. Bukti: Perilaku ujung fungsi polinomial f(x) = -5x^7 + 2x^4 - 8
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip atau aturan perilaku ujung fungsi polinomial (konseptual) dan cara menerapkannya pada fungsi tertentu (prosedural).. Bukti: Perilaku ujung fungsi polinomial
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin bagi siswa kelas 11 yang telah mempelajari polinomial. Tidak ada langkah kompleks atau strategi nonrutin yang diperlukan.. Bukti: Perilaku ujung fungsi polinomial f(x) = -5x^7 + 2x^4 - 8

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang derajat polinomial dan koefisien utama. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi perilaku ujung polinomial adalah topik standar di kelas 11 Matematika Tingkat Lanjut. Soal ini menguji pemahaman dasar tanpa variasi yang rumit. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: Derajat polinomial didefinisikan sebagai pangkat tertinggi dari variabel dalam polinomial tersebut. Pada polinomial x^6 - 12x^4 + 3x^2 - 10, pangkat-pangkat variabel x adalah 6, 4, dan 2. Pangkat tertinggi adalah 6, sehingga derajat polinomial tersebut adalah 6.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0de513b7dfd369ab1dd04c91c7fc28766d8fc22cd072a96807dea050d87beac2`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2029 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 1963 |
| 3 | success | valid / verified | knowing | factual | Easy | 2002 |

Run 1 — solusi: Derajat polinomial adalah pangkat tertinggi dari variabel dalam polinomial tersebut. Untuk polinomial x^6 - 12x^4 + 3x^2 - 10, pangkat-pangkat variabelnya adalah 6, 4, dan 2. Pangkat tertinggi adalah 6.
- Domain kognitif `classify/knowing`: Soal ini hanya meminta siswa untuk mengidentifikasi pangkat tertinggi dari variabel dalam polinomial, yang merupakan definisi dasar dari derajat polinomial. Tidak ada proses perhitungan atau manipulasi yang diperlukan.. Bukti: Cari derajat setiap polinomial berikut.; x^6 - 12x^4 + 3x^2 - 10
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami definisi atau konsep tentang apa itu derajat polinomial (pangkat tertinggi dari variabel).. Bukti: Cari derajat setiap polinomial berikut.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan langsung, hanya memerlukan pengenalan visual terhadap pangkat tertinggi dalam ekspresi polinomial satu variabel.. Bukti: Cari derajat setiap polinomial berikut.; x^6 - 12x^4 + 3x^2 - 10

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
| gradeRelativeRationale | Meskipun materi polinomial diajarkan di kelas 11, menentukan derajat adalah konsep dasar yang sangat sederhana dan tidak menantang bagi siswa kelas 11. |

Run 2 — solusi: Derajat polinomial adalah pangkat tertinggi dari variabel x dalam polinomial tersebut. Pada x^6 - 12x^4 + 3x^2 - 10, pangkat tertinggi adalah 6.
- Domain kognitif `classify/knowing`: Soal ini hanya meminta siswa untuk mengidentifikasi pangkat tertinggi dari variabel dalam polinomial, yang merupakan proses pengenalan definisi dasar.. Bukti: Cari derajat setiap polinomial berikut.; x^6 - 12x^4 + 3x^2 - 10
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang definisi derajat polinomial, yang merupakan konsep dasar dalam aljabar.. Bukti: Cari derajat setiap polinomial berikut.
- Intended difficulty `classify/Easy`: Soal ini sangat langsung dan hanya memerlukan satu langkah identifikasi tanpa perhitungan kompleks atau strategi non-rutin.. Bukti: x^6 - 12x^4 + 3x^2 - 10; Cari derajat setiap polinomial berikut.

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
| gradeRelativeRationale | Meskipun materi polinomial diajarkan di kelas 11, menentukan derajat adalah konsep dasar yang sangat sederhana dan rutin. |

Run 3 — solusi: Derajat polinomial adalah pangkat tertinggi dari variabel dalam polinomial tersebut. Pada $x^6 - 12x^4 + 3x^2 - 10$, suku dengan pangkat tertinggi adalah $x^6$, sehingga derajatnya adalah 6.
- Domain kognitif `classify/knowing`: Soal ini hanya meminta siswa untuk mengidentifikasi pangkat tertinggi dari variabel dalam polinomial, yang merupakan definisi dasar derajat polinomial. Tidak ada proses perhitungan atau strategi yang diperlukan.. Bukti: Cari derajat setiap polinomial berikut.; $x^6 - 12x^4 + 3x^2 - 10$
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang definisi atau terminologi dasar dalam polinomial, yaitu konsep derajat.. Bukti: Cari derajat setiap polinomial berikut.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan hanya memerlukan pengenalan visual terhadap pangkat tertinggi. Tidak ada langkah prosedural atau strategi yang diperlukan.. Bukti: $x^6 - 12x^4 + 3x^2 - 10$

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
| gradeRelativeRationale | Meskipun materi polinomial diajarkan di kelas 11, konsep derajat adalah konsep dasar yang sangat sederhana dan tidak menantang bagi siswa kelas 11. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 2, "factual": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3410`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini hanya meminta siswa untuk mengidentifikasi pangkat tertinggi dari variabel dalam polinomial, yang merupakan definisi dasar dari derajat polinomial. Tidak ada proses perhitungan atau manipulasi yang diperlukan.
- Dimensi pengetahuan `conceptual`: Siswa perlu memahami definisi atau konsep tentang apa itu derajat polinomial (pangkat tertinggi dari variabel).
- Intended difficulty `Easy`: Soal ini sangat mendasar dan langsung, hanya memerlukan pengenalan visual terhadap pangkat tertinggi dalam ekspresi polinomial satu variabel.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang notasi eksponen dan definisi derajat polinomial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi polinomial diajarkan di kelas 11, menentukan derajat adalah konsep dasar yang sangat sederhana dan tidak menantang bagi siswa kelas 11. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: Distribusi tanda negatif: (2x^4 - x^3 + 4x - 12) - x^4 - 2x^3 + x^2 + 6. Mengelompokkan suku sejenis: (2-1)x^4 + (-1-2)x^3 + x^2 + 4x + (-12+6) = x^4 - 3x^3 + x^2 + 4x - 6.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `39d655657992f26b78e3bef36284a9c81df6e1794cf0b6a39bd4ecca76563c90`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2258 |
| 2 | success | valid / verified | applying | procedural | Easy | 2275 |
| 3 | success | valid / verified | applying | procedural | Easy | 2132 |

Run 1 — solusi: Distribusi tanda negatif: (2x^4 - x^3 + 4x - 12) - x^4 - 2x^3 + x^2 + 6. Mengelompokkan suku sejenis: (2-1)x^4 + (-1-2)x^3 + x^2 + 4x + (-12+6) = x^4 - 3x^3 + x^2 + 4x - 6.
- Domain kognitif `classify/applying`: Siswa hanya perlu menerapkan prosedur rutin pengurangan polinomial dengan mendistribusikan tanda negatif dan menjumlahkan suku-suku sejenis.. Bukti: (2x^4 - x^3 + 4x - 12) - (x^4 + 2x^3 - x^2 - 6)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang algoritma pengurangan polinomial.. Bukti: Sederhanakan penjumlahan dan pengurangan polinomial berikut ini.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin, hanya memerlukan satu langkah utama (distribusi tanda negatif) dan penggabungan suku sejenis. Beban perhitungan rendah.. Bukti: (2x^4 - x^3 + 4x - 12) - (x^4 + 2x^3 - x^2 - 6)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aljabar dasar dan penjumlahan/pengurangan suku sejenis. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 8 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun polinomial adalah materi kelas 11, operasi pengurangan ini adalah prosedur dasar yang familiar dari jenjang sebelumnya. |

Run 2 — solusi: Distribusi tanda negatif: (2x^4 - x^3 + 4x - 12) - x^4 - 2x^3 + x^2 + 6. Mengelompokkan suku sejenis: (2-1)x^4 + (-1-2)x^3 + x^2 + 4x + (-12+6) = x^4 - 3x^3 + x^2 + 4x - 6.
- Domain kognitif `classify/applying`: Siswa diminta melakukan operasi pengurangan polinomial dengan mendistribusikan tanda negatif dan menggabungkan suku sejenis. Ini adalah penerapan prosedur standar.. Bukti: (2x^4 - x^3 + 4x - 12) - (x^4 + 2x^3 - x^2 - 6)
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma pengurangan polinomial dan pengelompokan suku sejenis.. Bukti: Sederhanakan penjumlahan dan pengurangan polinomial berikut ini.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan beban komputasi rendah. Siswa hanya perlu menerapkan aturan tanda dan penjumlahan aljabar dasar.. Bukti: (2x^4 - x^3 + 4x - 12) - (x^4 + 2x^3 - x^2 - 6)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aljabar dasar dan penjumlahan/pengurangan suku sejenis. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 8 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun polinomial diajarkan di kelas 11, operasi dasar ini adalah prasyarat yang sangat familiar dan prosedural, sehingga dikategorikan mudah untuk tingkat kelas 11. |

Run 3 — solusi: (2x^4 - x^4) + (-x^3 - 2x^3) + (0 - (-x^2)) + (4x - 0) + (-12 - (-6)) = x^4 - 3x^3 + x^2 + 4x - 6
- Domain kognitif `classify/applying`: Soal meminta siswa melakukan operasi pengurangan polinomial dasar dengan mengelompokkan suku-suku sejenis. Ini adalah prosedur rutin yang langsung.. Bukti: (2x^4 - x^3 + 4x - 12) - (x^4 + 2x^3 - x^2 - 6)
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menerapkan algoritma penjumlahan/pengurangan polinomial dengan mendistribusikan tanda negatif pada polinomial kedua.. Bukti: Sederhanakan penjumlahan dan pengurangan polinomial berikut ini.
- Intended difficulty `classify/Easy`: Soal ini melibatkan operasi polinomial dasar yang merupakan materi prasyarat atau awal di kelas 11. Prosedurnya familiar, langkah-langkahnya rutin, dan beban kalkulasinya rendah.. Bukti: (2x^4 - x^3 + 4x - 12) - (x^4 + 2x^3 - x^2 - 6)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi aljabar dasar dan pengelompokan suku sejenis. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 8 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun polinomial adalah materi kelas 11, tingkat kesulitan soal ini sangat dasar (hanya operasi penjumlahan/pengurangan), sehingga dikategorikan Easy untuk siswa kelas 11. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: Kelompokkan suku-suku sejenis: (3m^2n + 2m^2n) + (-mn^2) + (mn) + (-12 + 7) = 5m^2n - mn^2 + mn - 5.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `da97a5f96c37c655f8e02855d97d72b96d76b4bae3e6eed7153c117616511cf4`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2127 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2142 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2158 |

Run 1 — solusi: Kelompokkan suku-suku sejenis: (3m^2n + 2m^2n) + (-mn^2) + (mn) + (-12 + 7) = 5m^2n - mn^2 + mn - 5.
- Domain kognitif `classify/knowing`: Soal ini hanya meminta siswa untuk mengidentifikasi dan menjumlahkan suku-suku sejenis dalam polinomial, yang merupakan proses rutin dan langsung.. Bukti: (3m^2n + mn - 12) + (2m^2n - mn^2 + 7)
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami konsep suku sejenis (conceptual) dan menerapkan algoritma penjumlahan polinomial (procedural).. Bukti: Sederhanakan penjumlahan dan pengurangan polinomial berikut ini.
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural dasar dengan satu langkah utama yaitu pengelompokan suku sejenis. Tidak ada kompleksitas tambahan.. Bukti: (3m^2n + mn - 12) + (2m^2n - mn^2 + 7)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang variabel, koefisien, dan suku sejenis dalam aljabar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi polinomial ada di kelas 11, soal ini terlalu mendasar (setara kelas 7/8) untuk standar kelas 11 TL. |

Run 2 — solusi: Kelompokkan suku-suku sejenis: (3m^2n + 2m^2n) + (-mn^2) + (mn) + (-12 + 7) = 5m^2n - mn^2 + mn - 5.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengidentifikasi suku-suku sejenis dan melakukan operasi penjumlahan dasar. Ini adalah proses rutin yang langsung.. Bukti: (3m^2n + mn - 12) + (2m^2n - mn^2 + 7)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang aturan penjumlahan polinomial dengan mengelompokkan suku sejenis.. Bukti: Sederhanakan penjumlahan dan pengurangan polinomial
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya melibatkan penggabungan suku sejenis tanpa manipulasi aljabar yang kompleks atau langkah bertingkat.. Bukti: (3m^2n + mn - 12) + (2m^2n - mn^2 + 7)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang suku sejenis dalam aljabar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi polinomial ada di kelas 11, soal ini terlalu sederhana untuk tingkat SMA kelas 11 karena hanya menguji operasi dasar yang seharusnya sudah dikuasai di jenjang SMP. |

Run 3 — solusi: Kelompokkan suku-suku sejenis: (3m^2n + 2m^2n) + (mn) + (-mn^2) + (-12 + 7) = 5m^2n + mn - mn^2 - 5. Hasilnya adalah 5m^2n - mn^2 + mn - 5.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi penjumlahan polinomial dasar dengan mengelompokkan suku-suku sejenis. Proses ini bersifat prosedural dan langsung tanpa memerlukan strategi nonrutin.. Bukti: (3m^2n + mn - 12) + (2m^2n - mn^2 + 7)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma penjumlahan polinomial, yang merupakan teknik prosedural standar dalam aljabar.. Bukti: Sederhanakan penjumlahan dan pengurangan polinomial berikut ini.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya melibatkan pengelompokan suku sejenis dengan variabel yang sudah ditentukan. Tidak ada langkah kompleks atau jebakan konseptual.. Bukti: (3m^2n + mn - 12) + (2m^2n - mn^2 + 7)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan aljabar dasar dan pengelompokan suku sejenis. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Meskipun materi polinomial ada di kelas 11, soal ini setara dengan materi aljabar dasar kelas 7-8, sehingga sangat mudah bagi siswa kelas 11. |

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
Solusi minimum hasil AI: Koefisien P(x) adalah 3, -11, 0, 1, 20, 0, -3. Menggunakan skema Horner dengan c = 2/3: 3 turun; 3*(2/3)=2, -11+2=-9; -9*(2/3)=-6, 0-6=-6; -6*(2/3)=-4, 1-4=-3; -3*(2/3)=-2, 20-2=18; 18*(2/3)=12, 0+12=12; 12*(2/3)=8, -3+8=5. Sisa akhir adalah 5.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['menerapkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d6047647dd2e6094bb599eb59842de2bf3ab7d42f142e3072984aff33221cfe7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2250 |
| 2 | success | valid / verified | applying | procedural | Easy | 2186 |
| 3 | success | valid / verified | applying | procedural | Easy | 2211 |

Run 1 — solusi: Menggunakan skema Horner untuk P(x) = 3x^6 - 11x^5 + 0x^4 + 1x^3 + 20x^2 + 0x - 3 dengan c = 2/3: Koefisien [3, -11, 0, 1, 20, 0, -3]. Langkah: 3 turun; 3*(2/3)=2, -11+2=-9; -9*(2/3)=-6, 0-6=-6; -6*(2/3)=-4, 1-4=-3; -3*(2/3)=-2, 20-2=18; 18*(2/3)=12, 0+12=12; 12*(2/3)=8, -3+8=5. Sisa akhir adalah 5.
- Domain kognitif `classify/applying`: Soal meminta penerapan algoritma spesifik (metode Horner) untuk mengevaluasi polinomial pada nilai tertentu. Ini adalah penerapan prosedur rutin yang sudah dipelajari di kelas 11.. Bukti: Gunakan metode Horner dan Teorema Sisa untuk menentukan nilai P(c)
- Dimensi pengetahuan `classify/procedural`: Siswa harus menggunakan algoritma Horner, yang merupakan prosedur standar untuk pembagian polinomial atau evaluasi nilai polinomial.. Bukti: Gunakan metode Horner dan Teorema Sisa
- Intended difficulty `classify/Medium`: Soal ini bersifat rutin. Meskipun polinomial berderajat 6, langkah-langkahnya mekanis dan tidak memerlukan strategi non-rutin. Beban perhitungan moderat karena melibatkan pecahan.. Bukti: P(x) = 3x^6 - 11x^5 + x^3 + 20x^2 - 3; c = 2/3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang koefisien polinomial, operasi aritmatika pecahan, dan algoritma Horner. |
| dependentSteps | 6 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 11 TL karena melibatkan polinomial derajat tinggi yang memerlukan ketelitian dalam skema Horner, namun metodenya sangat standar. |

Run 2 — solusi: Koefisien P(x) adalah 3, -11, 0, 1, 20, 0, -3. Horner dengan c=2/3: 3 turun, 3*(2/3)=2, -11+2=-9, -9*(2/3)=-6, 0-6=-6, -6*(2/3)=-4, 1-4=-3, -3*(2/3)=-2, 20-2=18, 18*(2/3)=12, 0+12=12, 12*(2/3)=8, -3+8=5. Sisa adalah 5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan algoritma spesifik (Horner) untuk mengevaluasi polinomial pada nilai tertentu, yang merupakan prosedur standar dalam kurikulum.. Bukti: Gunakan metode Horner dan Teorema Sisa untuk menentukan nilai P(c)
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman dan penerapan algoritma pembagian polinomial (Horner) sebagai teknik prosedural.. Bukti: Gunakan metode Horner dan Teorema Sisa
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Meskipun polinomial berderajat 6, langkah-langkahnya mekanis dan familiar bagi siswa kelas 11. Tidak ada jebakan konseptual atau strategi non-rutin yang diperlukan.. Bukti: 3x^6 - 11x^5 + x^3 + 20x^2 - 3; c = 2/3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar operasi polinomial dan skema Horner. |
| dependentSteps | 6 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 11 TL sebagai latihan rutin penerapan Teorema Sisa. |

Run 3 — solusi: Koefisien P(x): 3, -11, 0, 1, 20, 0, -3. Horner dengan c=2/3: (3) -> 3*(2/3)=2 -> -11+2=-9 -> -9*(2/3)=-6 -> 0-6=-6 -> -6*(2/3)=-4 -> 1-4=-3 -> -3*(2/3)=-2 -> 20-2=18 -> 18*(2/3)=12 -> 0+12=12 -> 12*(2/3)=8 -> -3+8=5. Sisa = 5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan algoritma spesifik (metode Horner) untuk mengevaluasi nilai polinomial pada titik tertentu, yang merupakan prosedur standar dalam kurikulum kelas 11.. Bukti: Gunakan metode Horner dan Teorema Sisa untuk menentukan nilai P(c)
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman dan penerapan algoritma pembagian polinomial (prosedural) untuk mendapatkan nilai fungsi.. Bukti: Gunakan metode Horner dan Teorema Sisa
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Meskipun polinomial berderajat 6, langkah-langkah Horner bersifat mekanis dan familiar bagi siswa kelas 11. Tidak ada jebakan konseptual atau strategi non-rutin yang diperlukan.. Bukti: P(x) = 3x^6 - 11x^5 + x^3 + 20x^2 - 3; c = 2/3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar operasi polinomial dan metode Horner. |
| dependentSteps | 6 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Metode Horner adalah materi standar kelas 11. Derajat 6 mungkin terlihat panjang, namun prosedurnya sangat repetitif dan langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 1, "Easy": 2} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4040`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Soal meminta penerapan algoritma spesifik (metode Horner) untuk mengevaluasi polinomial pada nilai tertentu. Ini adalah penerapan prosedur rutin yang sudah dipelajari di kelas 11.
- Dimensi pengetahuan `procedural`: Siswa harus menggunakan algoritma Horner, yang merupakan prosedur standar untuk pembagian polinomial atau evaluasi nilai polinomial.
- Intended difficulty `Easy`: Soal ini bersifat rutin. Meskipun polinomial berderajat 6, langkah-langkahnya mekanis dan tidak memerlukan strategi non-rutin. Beban perhitungan moderat karena melibatkan pecahan, namun prosedurnya sangat standar.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang koefisien polinomial, operasi aritmatika pecahan, dan algoritma Horner. |
| dependentSteps | 6 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 11 TL sebagai latihan rutin penerapan Teorema Sisa. Derajat 6 mungkin terlihat panjang, namun prosedurnya sangat repetitif dan langsung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: Berdasarkan Teorema Sisa, jika polinomial P(x) dibagi oleh (x - c), maka sisanya adalah P(c). Karena diketahui sisa pembagian adalah k, maka P(c) = k.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2e2dee62f2ce3b462e3f2bc93da17a7d89b8a419d06726d37b0d194f65f5e657`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2738 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2057 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2051 |

Run 1 — solusi: Berdasarkan Teorema Sisa, jika polinomial P(x) dibagi oleh (x - c), maka sisanya adalah P(c). Karena diketahui sisa pembagian adalah k, maka P(c) = k.
- Domain kognitif `classify/knowing`: Soal ini hanya menanyakan pemahaman definisi dasar Teorema Sisa tanpa memerlukan proses perhitungan atau strategi kompleks.. Bukti: Karena polinomial P(x) dibagi dengan x - c memiliki sisa k, nilai P(c) = ....
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep Teorema Sisa yang menghubungkan sisa pembagian polinomial dengan nilai fungsi pada titik tertentu.. Bukti: Karena polinomial P(x) dibagi dengan x - c memiliki sisa k, nilai P(c) = ....
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung dan menguji ingatan terhadap definisi dasar Teorema Sisa tanpa langkah tambahan.. Bukti: Karena polinomial P(x) dibagi dengan x - c memiliki sisa k, nilai P(c) = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi pembagian polinomial dan Teorema Sisa. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini adalah dasar dari topik polinomial di kelas 11, sehingga soal ini dikategorikan mudah karena hanya menguji pemahaman definisi. |

Run 2 — solusi: Berdasarkan Teorema Sisa, jika polinomial P(x) dibagi oleh (x - c), maka sisa pembagiannya adalah P(c). Diketahui sisa pembagian adalah k, maka P(c) = k.
- Domain kognitif `classify/knowing`: Soal ini hanya menanyakan definisi atau penerapan langsung dari Teorema Sisa tanpa memerlukan manipulasi aljabar atau langkah pemecahan masalah yang kompleks.. Bukti: Karena polinomial $P(x)$ dibagi dengan $x - c$ memiliki sisa $k$, nilai $P(c) = ….$
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap prinsip atau teorema dasar dalam pembagian polinomial (Teorema Sisa).. Bukti: Karena polinomial $P(x)$ dibagi dengan $x - c$ memiliki sisa $k$
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan langsung menguji pemahaman definisi Teorema Sisa tanpa ada beban perhitungan atau langkah prosedural yang panjang.. Bukti: Karena polinomial $P(x)$ dibagi dengan $x - c$ memiliki sisa $k$, nilai $P(c) = ….$

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
| gradeRelativeRationale | Ini adalah konsep fundamental dalam materi polinomial kelas 11, namun tingkat kesulitannya sangat rendah karena hanya berupa pengenalan definisi. |

Run 3 — solusi: Berdasarkan Teorema Sisa, jika polinomial P(x) dibagi oleh (x - c), maka sisa pembagiannya adalah P(c). Karena diketahui sisa pembagiannya adalah k, maka P(c) = k.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengingat dan menerapkan definisi langsung dari Teorema Sisa. Tidak ada strategi kompleks atau pemecahan masalah yang diperlukan, hanya pemahaman dasar tentang hubungan antara sisa pembagian polinomial dan nilai fungsi.. Bukti: Karena polinomial P(x) dibagi dengan x - c memiliki sisa k, nilai P(c) = ….
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa mengenai prinsip atau aturan dasar dalam polinomial, yaitu Teorema Sisa, yang merupakan bagian dari struktur konsep polinomial.. Bukti: Karena polinomial P(x) dibagi dengan x - c memiliki sisa k, nilai P(c) = ….
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan langsung menguji definisi Teorema Sisa tanpa memerlukan langkah perhitungan atau manipulasi aljabar.. Bukti: Karena polinomial P(x) dibagi dengan x - c memiliki sisa k, nilai P(c) = ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pembagian polinomial dan notasi fungsi. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah konsep dasar yang diajarkan di awal materi polinomial kelas 11, sehingga tingkat kesulitannya rendah. |

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
Solusi minimum hasil AI: Uji akar: P(2) = 5(8) - 28(4) + 45(2) - 18 = 40 - 112 + 90 - 18 = 0. P(3) = 5(27) - 28(9) + 45(3) - 18 = 135 - 252 + 135 - 18 = 0. Membagi P(x) dengan (x-2)(x-3) = x^2 - 5x + 6 menghasilkan 5x - 3. Maka P(x) = (x-2)(x-3)(5x-3).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6f2f6859fe2d868aca840001b9b07b5687f412abbf845cafb097c4d66f1ef7fb`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 3284 |
| 2 | success | valid / verified | applying | procedural | Medium | 3213 |
| 3 | success | valid / verified | applying | procedural | Medium | 3383 |

Run 1 — solusi: Uji akar: P(2) = 5(8) - 28(4) + 45(2) - 18 = 40 - 112 + 90 - 18 = 0. P(3) = 5(27) - 28(9) + 45(3) - 18 = 135 - 252 + 135 - 18 = 0. Membagi P(x) dengan (x-2)(x-3) = x^2 - 5x + 6 menghasilkan 5x - 3. Maka P(x) = (x-2)(x-3)(5x-3).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan teorema faktor dan melakukan pembagian polinomial atau metode Horner untuk memfaktorkan polinomial derajat tiga. Ini adalah prosedur rutin dalam kurikulum kelas 11.. Bukti: Faktorkan P(x) = 5x^3 - 28x^2 + 45x - 18 secara lengkap.
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma pembagian polinomial atau teorema faktor untuk menemukan akar dan memfaktorkan ekspresi.. Bukti: Faktorkan P(x) = 5x^3 - 28x^2 + 45x - 18 secara lengkap.
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah rutin (mencari akar rasional, pembagian polinomial) dan ketelitian dalam menangani koefisien utama.. Bukti: Faktorkan P(x) = 5x^3 - 28x^2 + 45x - 18 secara lengkap.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema faktor, pembagian polinomial, operasi aljabar dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Memfaktorkan polinomial derajat 3 adalah standar kelas 11. Memerlukan pemilihan akar yang tepat dan pembagian polinomial. |

Run 2 — solusi: Uji akar: P(2) = 5(8) - 28(4) + 45(2) - 18 = 40 - 112 + 90 - 18 = 0. P(3) = 5(27) - 28(9) + 45(3) - 18 = 135 - 252 + 135 - 18 = 0. Membagi P(x) dengan (x-2)(x-3) = x^2 - 5x + 6 menghasilkan 5x - 3. Maka P(x) = (5x-3)(x-2)(x-3).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan teorema faktor dan prosedur pembagian polinomial untuk memfaktorkan ekspresi derajat tiga secara lengkap.. Bukti: Faktorkan P(x) = 5x^3 - 28x^2 + 45x - 18 secara lengkap.
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penggunaan algoritma pembagian polinomial dan penerapan teorema faktor sebagai teknik prosedural standar.. Bukti: Faktorkan P(x) = 5x^3 - 28x^2 + 45x - 18 secara lengkap.
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah rutin yang saling terkait (uji akar dan pembagian polinomial) serta ketelitian dalam menangani koefisien utama.. Bukti: Faktorkan P(x) = 5x^3 - 28x^2 + 45x - 18 secara lengkap.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema faktor, pembagian polinomial, dan operasi aljabar dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan mampu memfaktorkan polinomial derajat tiga dengan metode pembagian atau skema Horner. |

Run 3 — solusi: Uji akar: P(2) = 5(8) - 28(4) + 45(2) - 18 = 40 - 112 + 90 - 18 = 0 dan P(3) = 5(27) - 28(9) + 45(3) - 18 = 135 - 252 + 135 - 18 = 0. Membagi P(x) dengan (x-2)(x-3) = x^2 - 5x + 6 menghasilkan faktor linear (5x-3). Maka P(x) = (x-2)(x-3)(5x-3).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan teorema faktor untuk menemukan akar-akar polinomial dan melakukan pembagian polinomial (atau metode Horner) untuk menentukan faktor linear lainnya secara sistematis.. Bukti: Faktorkan P(x) = 5x^3 - 28x^2 + 45x - 18 secara lengkap.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji penguasaan algoritma faktorisasi polinomial dan penggunaan teorema faktor yang merupakan prosedur standar dalam aljabar polinomial.. Bukti: Faktorkan P(x) = 5x^3 - 28x^2 + 45x - 18 secara lengkap.
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah rutin yang saling terkait: menguji akar, melakukan pembagian polinomial, dan menyusun faktor akhir dengan memperhatikan koefisien utama.. Bukti: Faktorkan P(x) = 5x^3 - 28x^2 + 45x - 18 secara lengkap.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Teorema faktor, pembagian polinomial (Horner atau bersusun), dan operasi aljabar dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan standar materi polinomial kelas 11 yang menuntut ketelitian dalam faktorisasi dan penanganan koefisien utama. |

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
| 1 | success | valid / verified | knowing | conceptual | Easy | 2669 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2048 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2716 |

Run 1 — solusi: Berdasarkan Teorema Faktor, jika P(c) = 0, maka (x - c) adalah faktor dari P(x). Karena P(10) = 0, maka (x - 10) adalah faktor dari P(x).
- Domain kognitif `classify/knowing`: Soal ini hanya menuntut pengingatan langsung terhadap definisi Teorema Faktor tanpa memerlukan langkah prosedural atau strategi kompleks.. Bukti: nilai P(10) adalah 0; adalah faktor polinomial tersebut
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konsep dasar mengenai hubungan antara pembuat nol polinomial dan faktornya.. Bukti: P(10) adalah 0; adalah faktor polinomial tersebut
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural dasar yang langsung menguji pemahaman definisi Teorema Faktor. Tidak ada langkah perhitungan atau manipulasi aljabar yang diperlukan.. Bukti: nilai P(10) adalah 0; adalah faktor polinomial tersebut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi faktor dan pembuat nol polinomial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Materi ini merupakan pengenalan dasar polinomial di kelas 11, sehingga tingkat kesulitannya rendah. |

Run 2 — solusi: Berdasarkan Teorema Faktor, jika P(c) = 0, maka (x - c) adalah faktor dari polinomial P(x). Diketahui P(10) = 0, maka c = 10. Dengan demikian, (x - 10) adalah faktor dari P(x).
- Domain kognitif `classify/knowing`: Soal ini menguji pemahaman langsung terhadap definisi Teorema Faktor. Siswa hanya perlu mengenali hubungan antara pembuat nol (c) dan bentuk faktor (x-c) tanpa memerlukan strategi kompleks atau langkah prosedural yang panjang.. Bukti: nilai P(10) adalah 0; …. adalah faktor polinomial tersebut
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman konseptual mengenai prinsip dasar Teorema Faktor dalam polinomial, yaitu hubungan antara akar (pembuat nol) dan faktor linear.. Bukti: P(10) adalah 0; Teorema Faktor
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar dan langsung menguji satu konsep kunci (Teorema Faktor) tanpa memerlukan manipulasi aljabar atau langkah tambahan.. Bukti: nilai P(10) adalah 0; …. adalah faktor polinomial tersebut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang definisi faktor dan pembuat nol polinomial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi polinomial diajarkan di kelas 11, soal ini hanya menanyakan definisi dasar Teorema Faktor, sehingga termasuk kategori mudah bagi siswa kelas 11. |

Run 3 — solusi: Berdasarkan Teorema Faktor, jika P(c) = 0, maka (x - c) adalah faktor dari P(x). Karena P(10) = 0, maka (x - 10) adalah faktor dari P(x).
- Domain kognitif `classify/knowing`: Soal ini hanya meminta penerapan langsung dari definisi Teorema Faktor tanpa memerlukan strategi atau manipulasi tambahan.. Bukti: nilai P(10) adalah 0; adalah faktor polinomial tersebut
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara pembuat nol polinomial dan bentuk faktornya (konsep Teorema Faktor).. Bukti: P(10) adalah 0; faktor polinomial
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya menanyakan pemahaman langsung terhadap Teorema Faktor tanpa langkah perhitungan atau analisis lanjut.. Bukti: nilai P(10) adalah 0; adalah faktor polinomial tersebut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang Teorema Faktor. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini merupakan dasar dari topik polinomial di kelas 11, dan soal ini tidak menuntut analisis lebih dari sekadar mengingat teorema. |

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
Solusi minimum hasil AI: Identitas selisih dua pangkat tiga adalah p^3 - q^3 = (p - q)(p^2 + pq + q^2). Pilihan D sesuai dengan identitas ini.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ff0c11e642a60eff77559b6b58b0fb0be2950bba019d234d0d5b96ef4e5b9041`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2040 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2031 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2039 |

Run 1 — solusi: Identitas selisih dua pangkat tiga adalah p^3 - q^3 = (p - q)(p^2 + pq + q^2). Pilihan D sesuai dengan identitas ini.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengingat dan menerapkan identitas aljabar dasar (selisih dua pangkat tiga). Tidak ada strategi non-rutin atau integrasi konsep yang kompleks yang diperlukan.. Bukti: p^3 - q^3 = ….
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap identitas polinomial, yang merupakan bagian dari pengetahuan konseptual dalam aljabar.. Bukti: p^3 - q^3 = ….
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan menguji ingatan terhadap rumus dasar yang sudah dipelajari. Tidak ada langkah perhitungan yang rumit atau pemilihan strategi yang menantang.. Bukti: p^3 - q^3 = ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang faktorisasi polinomial dan identitas aljabar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Identitas selisih pangkat tiga adalah materi dasar yang sering ditemui dalam aljabar SMA. Soal ini hanya menuntut pengenalan pola identitas tanpa manipulasi lebih lanjut. |

Run 2 — solusi: Identitas selisih dua pangkat tiga adalah p^3 - q^3 = (p - q)(p^2 + pq + q^2). Pilihan D sesuai dengan identitas tersebut.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengingat dan mengenali identitas aljabar dasar (selisih pangkat tiga). Tidak ada strategi kompleks atau pemecahan masalah yang diperlukan, hanya pengenalan bentuk faktorisasi standar.. Bukti: p^3 - q^3 = ….
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap identitas polinomial, yang merupakan bagian dari pengetahuan konseptual mengenai struktur dan hubungan antar bentuk aljabar.. Bukti: p^3 - q^3 = ….
- Intended difficulty `classify/Easy`: Soal ini sangat langsung dan hanya memerlukan ingatan terhadap rumus identitas dasar. Tidak ada langkah perhitungan atau manipulasi yang diperlukan.. Bukti: p^3 - q^3 = ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang faktorisasi aljabar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi polinomial diajarkan di kelas 11, identitas selisih pangkat tiga adalah pengetahuan dasar yang sangat rutin dan tidak memerlukan penalaran tingkat lanjut. |

Run 3 — solusi: Identitas selisih dua pangkat tiga adalah p^3 - q^3 = (p - q)(p^2 + pq + q^2). Pilihan D sesuai dengan identitas tersebut.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengingat dan mengenali identitas aljabar dasar (selisih dua pangkat tiga). Tidak ada strategi kompleks atau pemecahan masalah yang diperlukan, hanya pengenalan bentuk faktorisasi polinomial.. Bukti: p^3 - q^3 = ….
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap rumus atau identitas faktorisasi polinomial yang merupakan bagian dari pengetahuan konseptual dalam aljabar.. Bukti: p^3 - q^3 = ….
- Intended difficulty `classify/Easy`: Soal ini sangat langsung dan hanya memerlukan ingatan terhadap rumus identitas aljabar standar tanpa langkah perhitungan atau manipulasi lebih lanjut.. Bukti: p^3 - q^3 = ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang faktorisasi polinomial dan identitas aljabar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun identitas ini sering diajarkan di kelas 10, pada kelas 11 tingkat lanjut, ini dianggap sebagai pengetahuan dasar (prasyarat) yang sangat rutin dan langsung. |

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: Identitas polinomial harus bernilai sama untuk semua nilai x. Uji x=0: Ruas kiri = 3(0-1)^2 = 3(1) = 3. Ruas kanan = (3(0)-3)^2 = (-3)^2 = 9. Karena 3 tidak sama dengan 9, maka persamaan tersebut bukan identitas.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3d4b70446196c516b2b8820483eb27d260eb456035d11bd555bd8b6a3a648d34`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2118 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2150 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2141 |

Run 1 — solusi: Identitas polinomial harus bernilai sama untuk semua nilai x. Uji x=0: Ruas kiri = 3(0-1)^2 = 3(1) = 3. Ruas kanan = (3(0)-3)^2 = (-3)^2 = 9. Karena 3 tidak sama dengan 9, maka persamaan tersebut bukan identitas.
- Domain kognitif `classify/applying`: Siswa perlu memahami definisi identitas polinomial (berlaku untuk semua x) dan menerapkan strategi kontra-contoh untuk menyangkal klaim identitas.. Bukti: Apakah persamaan polinomial berikut merupakan identitas polinomial atau bukan? $3(x-1)^2 = (3x-3)^2$
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang definisi identitas polinomial dibandingkan dengan persamaan biasa.. Bukti: Apakah persamaan polinomial berikut merupakan identitas polinomial atau bukan?
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural dasar dalam menguji identitas dengan substitusi nilai sederhana. Tidak memerlukan manipulasi aljabar yang kompleks.. Bukti: Apakah persamaan polinomial berikut merupakan identitas polinomial atau bukan? $3(x-1)^2 = (3x-3)^2$

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang operasi aljabar dan definisi identitas. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi identitas polinomial adalah topik awal kelas 11. Soal ini menguji pemahaman dasar definisi identitas dengan angka yang sangat sederhana. |

Run 2 — solusi: Identitas polinomial harus berlaku untuk semua nilai x. Uji x=0: Ruas kiri = 3(0-1)^2 = 3(1) = 3. Ruas kanan = (3(0)-3)^2 = (-3)^2 = 9. Karena 3 tidak sama dengan 9, maka persamaan tersebut bukan identitas.
- Domain kognitif `classify/applying`: Siswa perlu memahami definisi identitas polinomial (berlaku untuk semua x) dan menerapkan strategi kontra-contoh untuk menyangkalnya. Ini melibatkan penerapan konsep dasar identitas.. Bukti: Apakah persamaan polinomial berikut merupakan identitas polinomial atau bukan? $3(x-1)^2 = (3x-3)^2$
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang apa yang mendefinisikan sebuah identitas polinomial dibandingkan dengan persamaan biasa.. Bukti: Apakah persamaan polinomial berikut merupakan identitas polinomial atau bukan?
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan prosedural. Siswa hanya perlu menguji satu nilai x atau melakukan ekspansi aljabar sederhana untuk melihat ketidaksamaan. Tidak ada langkah kompleks atau strategi non-rutin yang diperlukan.. Bukti: Apakah persamaan polinomial berikut merupakan identitas polinomial atau bukan? $3(x-1)^2 = (3x-3)^2$

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
| gradeRelativeRationale | Meskipun materi polinomial kelas 11, konsep identitas adalah dasar yang familiar. Soal ini tidak menuntut manipulasi aljabar yang rumit. |

Run 3 — solusi: Sebuah persamaan adalah identitas jika berlaku untuk semua nilai x. Uji x=0: Ruas kiri = 3(0-1)^2 = 3(1) = 3. Ruas kanan = (3(0)-3)^2 = (-3)^2 = 9. Karena 3 tidak sama dengan 9, maka persamaan tersebut bukan identitas.
- Domain kognitif `classify/applying`: Siswa perlu memahami definisi identitas polinomial (berlaku untuk semua x) dan menerapkan strategi penyangkal (counterexample) untuk membuktikan bahwa persamaan tersebut bukan identitas.. Bukti: Apakah persamaan polinomial berikut merupakan identitas polinomial atau bukan? $3(x-1)^2 = (3x-3)^2$
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi identitas polinomial dibandingkan dengan persamaan kondisional.. Bukti: Apakah persamaan polinomial berikut merupakan identitas polinomial atau bukan?
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural dasar dalam menguji identitas. Siswa hanya perlu melakukan substitusi nilai sederhana untuk menyanggah pernyataan, yang merupakan prosedur standar dalam aljabar.. Bukti: Apakah persamaan polinomial berikut merupakan identitas polinomial atau bukan? $3(x-1)^2 = (3x-3)^2$

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang operasi aljabar dan definisi identitas. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi identitas polinomial adalah bagian dari kurikulum kelas 11 TL. Soal ini menguji konsep dasar dengan beban komputasi yang sangat rendah, sehingga dikategorikan mudah. |

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
Solusi minimum hasil AI: Data menunjukkan nilai jarak meningkat dari 0 (t=0) hingga mencapai puncak 9 (t=3), kemudian menurun kembali ke 0 (t=6). Pola naik-lalu-turun ini menunjukkan adanya titik maksimum, yang merupakan karakteristik parabola terbuka ke bawah (a < 0).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `380d3936142ae792c8b78dd85ca65cfad5d7230aa96776a1e92936301ba6cbc7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2862 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2704 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2231 |

Run 1 — solusi: Data menunjukkan nilai jarak meningkat dari 0 (t=0) hingga mencapai puncak 9 (t=3), kemudian menurun kembali ke 0 (t=6). Pola naik-lalu-turun ini menunjukkan adanya titik maksimum, yang merupakan karakteristik parabola terbuka ke bawah (a < 0).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman konseptual tentang perilaku fungsi kuadrat (titik puncak dan arah bukaan) untuk menginterpretasikan pola data numerik tanpa bantuan visual.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara pola nilai fungsi (naik-turun) dengan sifat geometris parabola (konkavitas).. Bukti: Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung karena pola simetris pada tabel sangat jelas menunjukkan titik puncak, sehingga siswa hanya perlu mengenali sifat dasar fungsi kuadrat.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang sifat fungsi kuadrat dan titik puncak. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun untuk kelas 11 TL, soal ini sangat mendasar karena hanya meminta identifikasi pola tanpa perhitungan aljabar yang rumit. |

Run 2 — solusi: Data menunjukkan nilai jarak meningkat dari 0 (t=0) hingga mencapai puncak 9 (t=3), kemudian menurun kembali ke 0 (t=6). Pola simetris naik-lalu-turun ini menunjukkan grafik parabola dengan koefisien kuadrat (a) negatif, sehingga grafik terbuka ke bawah.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan pemahaman konseptual tentang perilaku fungsi kuadrat (concavity) berdasarkan pola data numerik tanpa harus melakukan perhitungan aljabar yang kompleks.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang hubungan antara pola nilai fungsi (naik-turun) dengan sifat geometris grafik fungsi kuadrat.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan prosedural bagi siswa yang memahami karakteristik dasar fungsi kuadrat. Tidak ada strategi non-rutin yang diperlukan.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk parabola dan perilaku fungsi kuadrat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan mampu mengenali sifat fungsi kuadrat dari data tabel dengan cepat tanpa perlu menggambar grafik. |

Run 3 — solusi: Data menunjukkan nilai jarak naik dari 0 (t=0) ke 9 (t=3) lalu turun kembali ke 0 (t=6). Pola simetris naik-lalu-turun ini menunjukkan titik puncak maksimum, yang merupakan karakteristik fungsi kuadrat dengan koefisien a negatif (terbuka ke bawah).
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasikan pola numerik dalam tabel untuk menyimpulkan sifat geometris fungsi kuadrat (arah bukaan) tanpa bantuan visual langsung, yang memerlukan pemahaman konseptual tentang hubungan antara nilai fungsi dan bentuk parabola.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana perilaku nilai fungsi kuadrat (naik-turun) berkaitan dengan sifat aljabar koefisien kuadratnya.. Bukti: Tabel di bawah menunjukkan jarak tempuh sebuah mobil pada setiap waktu.; Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 11 yang memahami karakteristik fungsi kuadrat. Tidak memerlukan perhitungan kompleks, hanya analisis pola data.. Bukti: Tanpa menggambar grafik, tentukan apakah grafik fungsi kuadrat terbuka ke atas atau ke bawah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk umum fungsi kuadrat dan karakteristik grafiknya. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 7 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi fungsi kuadrat sering diajarkan di kelas 10, soal ini menuntut kemampuan interpretasi data yang relevan dengan kurikulum kelas 11 TL sebagai dasar analisis fungsi. |

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
Solusi minimum hasil AI: Konversi derajat ke radian menggunakan faktor pengali (π/180). 45° × (π/180) = π/4 rad. 144° × (π/180) = 144π/180 = 4π/5 rad. 306° × (π/180) = 306π/180 = 17π/10 rad.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `39b89863e5b29aec5fd8822480764b9cb828d7dcab712908ddef99aff37f9549`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2278 |
| 2 | success | valid / verified | applying | procedural | Easy | 2317 |
| 3 | success | valid / verified | applying | procedural | Easy | 2338 |

Run 1 — solusi: Konversi derajat ke radian menggunakan faktor pengali (π/180). 45° × (π/180) = π/4 rad. 144° × (π/180) = 144π/180 = 4π/5 rad. 306° × (π/180) = 306π/180 = 17π/10 rad.
- Domain kognitif `classify/applying`: Soal ini meminta siswa untuk menerapkan prosedur konversi satuan sudut yang sudah dipelajari secara langsung. Tidak ada strategi nonrutin atau integrasi konsep yang kompleks.. Bukti: Nyatakan sudut-sudut berikut ke dalam radian: 45°, 144°, dan 306°.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami hubungan antara satuan derajat dan radian (konsep) serta menerapkan algoritma konversi (prosedural) untuk menyelesaikan soal.. Bukti: Nyatakan sudut-sudut berikut ke dalam radian
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan prosedur yang jelas dan langsung. Beban perhitungan rendah dan tidak memerlukan strategi khusus.. Bukti: Nyatakan sudut-sudut berikut ke dalam radian: 45°, 144°, dan 306°.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang satuan sudut (derajat dan radian) dan faktor konversi π/180. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi trigonometri diajarkan di kelas 11, konversi satuan adalah prosedur dasar yang sangat familiar dan tidak menuntut kemampuan analisis tingkat lanjut. |

Run 2 — solusi: Konversi derajat ke radian dilakukan dengan mengalikan sudut dengan (π/180). 45° × (π/180) = π/4 rad. 144° × (π/180) = 144π/180 = 4π/5 rad. 306° × (π/180) = 306π/180 = 17π/10 rad.
- Domain kognitif `classify/applying`: Soal ini meminta siswa untuk menerapkan prosedur konversi satuan sudut yang sudah dipelajari secara langsung tanpa memerlukan strategi nonrutin atau integrasi konsep yang kompleks.. Bukti: Nyatakan sudut-sudut berikut ke dalam radian: 45°, 144°, dan 306°.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menggunakan algoritma atau teknik konversi (mengalikan dengan faktor konversi π/180) untuk menyelesaikan masalah.. Bukti: Nyatakan sudut-sudut berikut ke dalam radian
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, hanya memerlukan satu prosedur standar konversi satuan sudut.. Bukti: Nyatakan sudut-sudut berikut ke dalam radian: 45°, 144°, dan 306°.

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
| gradeRelativeRationale | Meskipun materi trigonometri diajarkan di kelas 11, konversi satuan adalah prosedur dasar yang sangat rutin dan tidak menuntut kemampuan analisis tingkat lanjut. |

Run 3 — solusi: Konversi derajat ke radian menggunakan faktor pengali π/180. 45° × (π/180) = π/4 rad. 144° × (π/180) = 144π/180 = 4π/5 rad. 306° × (π/180) = 306π/180 = 17π/10 rad.
- Domain kognitif `classify/applying`: Soal ini meminta siswa untuk menerapkan prosedur konversi satuan sudut yang sudah dipelajari (derajat ke radian) secara langsung tanpa memerlukan strategi nonrutin atau pemecahan masalah yang kompleks.. Bukti: Nyatakan sudut-sudut berikut ke dalam radian: 45°, 144°, dan 306°.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami hubungan konseptual antara derajat dan radian serta menerapkan algoritma konversi (mengalikan dengan π/180) untuk menyelesaikan soal.. Bukti: Nyatakan sudut-sudut berikut ke dalam radian
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menerapkan satu rumus konversi yang umum. Beban perhitungan moderat karena penyederhanaan pecahan, namun prosedurnya sangat familiar.. Bukti: 45°, 144°, dan 306°

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang satuan sudut (derajat dan radian) dan penyederhanaan pecahan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi trigonometri kelas 11, konversi satuan adalah keterampilan dasar yang biasanya diperkenalkan di awal bab trigonometri. Soal ini tidak menuntut pemahaman mendalam tentang fungsi trigonometri itu sendiri. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: Definisi hubungan antara derajat dan radian adalah 180° = π rad. Untuk mengubah x derajat ke radian, kita gunakan faktor konversi (π rad / 180°). Jadi, sudut dalam derajat dikalikan dengan π/180.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d9c1c28a76ff63638717f58c8d3282feaa5dc924f1b055dddcfec790bb17cba7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2028 |
| 2 | success | valid / verified | knowing | factual | Easy | 1984 |
| 3 | success | valid / verified | knowing | factual | Easy | 2016 |

Run 1 — solusi: Definisi hubungan antara derajat dan radian adalah 180° = π rad. Untuk mengubah x derajat ke radian, kita gunakan faktor konversi (π rad / 180°). Jadi, sudut dalam derajat dikalikan dengan π/180.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengingat dan menerapkan fakta dasar mengenai konversi satuan sudut (derajat ke radian). Siswa hanya perlu mengenali faktor konversi yang tepat.. Bukti: Untuk mengonversi sebuah sudut yang dinyatakan ke dalam derajat menjadi radian, kalikan sudut tersebut dengan ….
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual mengenai hubungan antara satuan derajat dan radian dalam trigonometri.. Bukti: Untuk mengonversi sebuah sudut yang dinyatakan ke dalam derajat menjadi radian
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya menanyakan definisi atau faktor konversi dasar tanpa memerlukan perhitungan atau langkah prosedural yang kompleks.. Bukti: Untuk mengonversi sebuah sudut yang dinyatakan ke dalam derajat menjadi radian, kalikan sudut tersebut dengan ….

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
| gradeRelativeRationale | Meskipun materi ini sering diajarkan di kelas 10, ini merupakan prasyarat mutlak untuk materi trigonometri kelas 11 TL. Soal ini bersifat sangat mendasar (recall). |

Run 2 — solusi: Konversi sudut dari derajat ke radian didasarkan pada hubungan 180° = π radian. Maka, 1° = π/180 radian. Untuk mengubah x derajat menjadi radian, kalikan x dengan π/180.
- Domain kognitif `classify/knowing`: Soal ini hanya menuntut siswa untuk mengingat atau mengenali fakta dasar mengenai faktor konversi satuan sudut antara derajat dan radian.. Bukti: Untuk mengonversi sebuah sudut yang dinyatakan ke dalam derajat menjadi radian, kalikan sudut tersebut dengan ….
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman terhadap fakta dasar atau definisi konversi satuan dalam trigonometri.. Bukti: Untuk mengonversi sebuah sudut yang dinyatakan ke dalam derajat menjadi radian
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural dasar yang sangat familiar bagi siswa kelas 11 Matematika Tingkat Lanjut, tidak memerlukan langkah kompleks atau strategi khusus.. Bukti: Untuk mengonversi sebuah sudut yang dinyatakan ke dalam derajat menjadi radian, kalikan sudut tersebut dengan ….

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
| gradeRelativeRationale | Konversi derajat ke radian adalah materi dasar yang sudah diperkenalkan dan sering digunakan dalam topik trigonometri kelas 11. |

Run 3 — solusi: Konversi sudut dari derajat ke radian didasarkan pada hubungan 180° = π radian. Maka, 1° = π/180 radian. Untuk mengubah x derajat ke radian, kalikan x dengan π/180.
- Domain kognitif `classify/knowing`: Soal ini hanya menuntut siswa untuk mengingat atau mengenali fakta dasar mengenai faktor konversi satuan sudut (derajat ke radian). Tidak ada proses analisis atau penerapan prosedur kompleks yang diperlukan.. Bukti: Untuk mengonversi sebuah sudut yang dinyatakan ke dalam derajat menjadi radian, kalikan sudut tersebut dengan ….
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual tentang definisi dan hubungan antara dua satuan sudut (derajat dan radian) yang merupakan fakta dasar dalam trigonometri.. Bukti: Untuk mengonversi sebuah sudut yang dinyatakan ke dalam derajat menjadi radian
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya menanyakan faktor konversi standar. Tidak memerlukan langkah perhitungan atau strategi pemecahan masalah.. Bukti: Untuk mengonversi sebuah sudut yang dinyatakan ke dalam derajat menjadi radian, kalikan sudut tersebut dengan ….

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
| gradeRelativeRationale | Meskipun materi ini sering diajarkan di kelas 10, ini merupakan prasyarat mutlak untuk materi trigonometri kelas 11 TL. Soal ini sangat mendasar dan tidak memiliki kompleksitas yang diharapkan untuk tingkat lanjut. |

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
Solusi minimum hasil AI: Fungsi y = a sin k(x - b) + c adalah bentuk umum fungsi sinus. Amplitudo didefinisikan sebagai nilai mutlak dari koefisien a, yaitu \|a\|. Periode fungsi sinus dasar y = sin x adalah 2π. Untuk fungsi y = sin kx, periode menjadi 2π/\|k\|. Jadi, untuk y = a sin k(x - b) + c, amplitudonya adalah \|a\| dan periodenya adalah 2π/\|k\|.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c2309f0c8a2a9438fe67a7777664f6ebc3eee30f93cbdffa3365b99cb98e3789`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2091 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2117 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2083 |

Run 1 — solusi: Fungsi y = a sin k(x - b) + c adalah bentuk umum fungsi sinus. Amplitudo didefinisikan sebagai nilai mutlak dari koefisien a, yaitu \|a\|. Periode fungsi sinus dasar y = sin x adalah 2π. Untuk fungsi y = sin kx, periode menjadi 2π/\|k\|. Jadi, untuk y = a sin k(x - b) + c, amplitudonya adalah \|a\| dan periodenya adalah 2π/\|k\|.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengingat dan mengenali definisi serta rumus dasar dari parameter fungsi trigonometri sinus. Tidak ada manipulasi atau strategi non-rutin yang diperlukan.. Bukti: Grafik fungsi y = a sin k(x – b) + c memiliki amplitudo … dan periode ….
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep (conceptual) tentang bagaimana parameter a dan k mempengaruhi bentuk grafik fungsi sinus (amplitudo dan periode).. Bukti: Grafik fungsi y = a sin k(x – b) + c memiliki amplitudo … dan periode ….
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung dan menguji pemahaman definisi dasar yang diajarkan di awal materi grafik fungsi trigonometri.. Bukti: Grafik fungsi y = a sin k(x – b) + c memiliki amplitudo … dan periode ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi trigonometri dan transformasi grafik. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah konsep fundamental dalam materi fungsi trigonometri kelas 11 TL yang biasanya diperkenalkan sebagai pengetahuan dasar sebelum melakukan penggambaran grafik yang lebih kompleks. |

Run 2 — solusi: Fungsi y = a sin(k(x-b)) + c memiliki amplitudo yang didefinisikan sebagai nilai mutlak dari koefisien a, yaitu \|a\|. Periode fungsi sinus dasar y = sin(x) adalah 2π. Untuk fungsi y = sin(kx), periode menjadi 2π/\|k\|. Oleh karena itu, untuk y = a sin(k(x-b)) + c, periodenya adalah 2π/k (asumsi k > 0).
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengingat dan menerapkan definisi dasar dari parameter amplitudo dan periode pada fungsi trigonometri umum. Tidak ada strategi non-rutin atau integrasi konsep yang kompleks; ini adalah pemahaman faktual/konseptual langsung.. Bukti: Grafik fungsi y = a sin k(x – b) + c memiliki amplitudo … dan periode ….
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara parameter dalam persamaan fungsi trigonometri (a, k) dengan karakteristik grafiknya (amplitudo, periode). Ini adalah pengetahuan konseptual tentang struktur fungsi.. Bukti: Grafik fungsi y = a sin k(x – b) + c memiliki amplitudo … dan periode ….
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan menguji pemahaman definisi dasar tanpa memerlukan perhitungan atau manipulasi aljabar yang rumit. Siswa hanya perlu mengenali rumus standar.. Bukti: Grafik fungsi y = a sin k(x – b) + c memiliki amplitudo … dan periode ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi trigonometri dan transformasi grafik. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah materi dasar dalam topik fungsi trigonometri kelas 11 TL yang biasanya diajarkan di awal bab. |

Run 3 — solusi: Fungsi y = a sin k(x - b) + c memiliki amplitudo yang didefinisikan sebagai nilai mutlak dari koefisien a, yaitu \|a\|. Periode fungsi sinus dasar y = sin x adalah 2π. Dengan adanya faktor k pada argumen k(x-b), periode fungsi menjadi 2π dibagi dengan nilai mutlak k (atau 2π/k).
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengingat dan menerapkan definisi dasar amplitudo dan periode pada fungsi trigonometri umum. Siswa hanya perlu mengenali parameter fungsi sinus, yang merupakan proses langsung (knowing).. Bukti: Grafik fungsi y = a sin k(x – b) + c memiliki amplitudo … dan periode ….
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa mengenai struktur rumus fungsi trigonometri dan hubungan antara parameter (a, k) dengan karakteristik grafik (amplitudo, periode), yang merupakan pengetahuan konseptual.. Bukti: Grafik fungsi y = a sin k(x – b) + c memiliki amplitudo … dan periode ….
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung dan menguji pemahaman dasar tentang parameter fungsi trigonometri tanpa memerlukan manipulasi aljabar yang kompleks atau strategi pemecahan masalah.. Bukti: Grafik fungsi y = a sin k(x – b) + c memiliki amplitudo … dan periode ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi trigonometri dan grafik sinus. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini adalah dasar dari topik grafik fungsi trigonometri di kelas 11 TL, sehingga dianggap sebagai prosedur familiar. |

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
Solusi minimum hasil AI: Fungsi tangen y = tan(x) memiliki periode dasar π karena tan(x + π) = tan(x).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `af28070f38656bd2ce665fc9f4ead250057d274c7f51f63b7b0ce8aff2b0327a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2380 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 1952 |
| 3 | success | valid / verified | knowing | factual | Easy | 1918 |

Run 1 — solusi: Fungsi tangen y = tan(x) memiliki periode dasar π karena tan(x + π) = tan(x).
- Domain kognitif `classify/knowing`: Soal ini hanya menanyakan definisi atau fakta dasar mengenai periode fungsi trigonometri tangen tanpa memerlukan proses perhitungan atau analisis lebih lanjut.. Bukti: Periode grafik fungsi y = tan x adalah
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual tentang karakteristik dasar fungsi trigonometri (periode tangen).. Bukti: Periode grafik fungsi y = tan x adalah
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya memerlukan ingatan tentang sifat dasar fungsi trigonometri. Tidak ada langkah perhitungan atau strategi yang diperlukan.. Bukti: Periode grafik fungsi y = tan x adalah

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
| gradeRelativeRationale | Sangat mendasar untuk kelas 11, tidak memerlukan analisis mendalam. |

Run 2 — solusi: Fungsi tangen y = tan x memiliki asimtot tegak di x = π/2 + kπ. Jarak antara dua asimtot berturut-turut atau interval pengulangan nilai fungsi adalah π. Oleh karena itu, periode fungsi y = tan x adalah π.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengingat atau mengenali properti dasar dari fungsi trigonometri tangen. Tidak ada strategi kompleks atau penerapan prosedur yang panjang; ini adalah pengetahuan faktual/konseptual dasar dalam trigonometri.. Bukti: Periode grafik fungsi y = tan x adalah ….
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang definisi dan karakteristik dasar (periode) dari fungsi trigonometri, yang merupakan bagian dari pengetahuan konseptual.. Bukti: Periode grafik fungsi y = tan x adalah ….
- Intended difficulty `classify/Easy`: Soal ini sangat langsung dan menguji fakta dasar yang dipelajari di awal topik fungsi trigonometri. Tidak ada perhitungan atau langkah-langkah yang diperlukan.. Bukti: Periode grafik fungsi y = tan x adalah ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi fungsi trigonometri dasar |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah pertanyaan dasar mengenai properti fungsi trigonometri yang diharapkan dikuasai siswa kelas 11 sebagai prasyarat untuk analisis grafik yang lebih kompleks. |

Run 3 — solusi: Fungsi y = tan x memiliki asimtot tegak di x = π/2 + kπ. Jarak antara dua asimtot berturut-turut atau interval pengulangan nilai fungsi tangen adalah π. Oleh karena itu, periode fungsi y = tan x adalah π.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengingat atau mengenali properti dasar dari fungsi trigonometri tangen. Tidak ada langkah perhitungan atau strategi kompleks yang diperlukan.. Bukti: Periode grafik fungsi y = tan x adalah ….
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual mengenai karakteristik dasar (periode) dari fungsi trigonometri tangen.. Bukti: Periode grafik fungsi y = tan x adalah ….
- Intended difficulty `classify/Easy`: Soal ini sangat langsung dan hanya memerlukan ingatan akan fakta dasar trigonometri tanpa proses perhitungan atau analisis lebih lanjut.. Bukti: Periode grafik fungsi y = tan x adalah ….

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
| gradeRelativeRationale | Ini adalah konsep dasar yang diajarkan di awal materi fungsi trigonometri kelas 11. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3104`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini hanya menanyakan definisi atau fakta dasar mengenai periode fungsi trigonometri tangen tanpa memerlukan proses perhitungan atau analisis lebih lanjut.
- Dimensi pengetahuan `factual`: Soal ini menguji pengetahuan faktual tentang karakteristik dasar fungsi trigonometri (periode tangen).
- Intended difficulty `Easy`: Soal ini sangat langsung, hanya memerlukan ingatan tentang sifat dasar fungsi trigonometri. Tidak ada langkah perhitungan atau strategi yang diperlukan.

Profil difficulty hasil adjudikasi:

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
| gradeRelativeRationale | Sangat mendasar untuk kelas 11, tidak memerlukan analisis mendalam. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
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
Solusi minimum hasil AI: Berdasarkan identitas trigonometri dasar sin²t + cos²t = 1, bagi kedua ruas dengan cos²t menghasilkan tan²t + 1 = sec²t. Maka, sec²t - tan²t = 1.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d772f0705dc58f56b7922e53ac892ff56a3acabc26ee7df700aa7b678cf076f3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2584 |
| 2 | success | valid / verified | knowing | factual | Easy | 2536 |
| 3 | success | valid / verified | knowing | factual | Easy | 2695 |

Run 1 — solusi: Berdasarkan identitas trigonometri dasar sin²t + cos²t = 1, bagi kedua ruas dengan cos²t menghasilkan tan²t + 1 = sec²t. Maka, sec²t - tan²t = 1.
- Domain kognitif `classify/knowing`: Soal ini menuntut pengenalan langsung terhadap identitas trigonometri dasar tanpa perlu manipulasi kompleks.. Bukti: sec^2 t - tan^2 t = ...
- Dimensi pengetahuan `classify/factual`: Soal ini menguji ingatan siswa terhadap identitas trigonometri fundamental.. Bukti: sec^2 t - tan^2 t = ...
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung dan menguji ingatan terhadap identitas dasar yang dipelajari di kelas 11.. Bukti: sec^2 t - tan^2 t = ...

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Identitas trigonometri dasar (sin²t + cos²t = 1) |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah identitas dasar yang diharapkan dikuasai siswa kelas 11 sebagai prasyarat materi trigonometri lebih lanjut. |

Run 2 — solusi: Berdasarkan identitas trigonometri dasar sin²t + cos²t = 1, jika kedua ruas dibagi dengan cos²t, diperoleh tan²t + 1 = sec²t. Maka, sec²t - tan²t = 1.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengingat atau menurunkan identitas trigonometri dasar.. Bukti: sec^2 t - tan^2 t = ...
- Dimensi pengetahuan `classify/factual`: Soal menguji pemahaman terhadap identitas trigonometri dasar.. Bukti: sec^2 t - tan^2 t = ...
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari identitas dasar trigonometri yang dipelajari di kelas 11.. Bukti: sec^2 t - tan^2 t = ...

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Identitas trigonometri dasar (sin²t + cos²t = 1) |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Identitas ini adalah materi dasar dalam trigonometri kelas 11. |

Run 3 — solusi: Berdasarkan identitas trigonometri dasar sin^2 t + cos^2 t = 1, jika kedua ruas dibagi dengan cos^2 t, diperoleh tan^2 t + 1 = sec^2 t. Maka, sec^2 t - tan^2 t = 1.
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk mengingat dan menerapkan identitas trigonometri dasar secara langsung tanpa modifikasi kompleks.. Bukti: sec^2 t - tan^2 t = ...
- Dimensi pengetahuan `classify/factual`: Soal menguji pengetahuan faktual mengenai identitas trigonometri dasar.. Bukti: sec^2 t - tan^2 t = ...
- Intended difficulty `classify/Easy`: Soal ini sangat langsung dan hanya memerlukan ingatan terhadap identitas dasar trigonometri.. Bukti: sec^2 t - tan^2 t = ...

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Identitas trigonometri dasar (sin^2 t + cos^2 t = 1) |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi identitas trigonometri adalah dasar di kelas 11 TL, soal ini merupakan pengenalan langsung terhadap identitas turunan. |

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

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "factual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: Abel mengasumsikan pernyataan yang ingin dibuktikan sebagai premis. Selain itu, operasi penguadratan kedua ruas (x=y menjadi x^2=y^2) tidak ekuivalen karena dapat mengubah pernyataan salah menjadi benar (misal: 1 = -1 menjadi 1 = 1). Kesalahan logika ini membuat pembuktiannya tidak valid.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1078d54fc683a12e60edab3f452932ccaaedd267c4ff64013d7ee0aa8d310ee6`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Medium | 2486 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 2495 |
| 3 | success | valid / verified | reasoning | conceptual | Medium | 2440 |

Run 1 — solusi: Abel mengasumsikan pernyataan yang ingin dibuktikan sebagai premis. Selain itu, operasi penguadratan kedua ruas (x=y menjadi x^2=y^2) tidak ekuivalen karena dapat mengubah pernyataan salah menjadi benar (misal: 1 = -1 menjadi 1 = 1). Kesalahan logika ini membuat pembuktiannya tidak valid.
- Domain kognitif `classify/reasoning`: Soal ini menuntut siswa untuk mengevaluasi validitas logika pembuktian matematika, bukan sekadar menghitung. Siswa harus memahami konsep ekuivalensi logis dan sifat identitas, yang masuk dalam kategori reasoning.. Bukti: Abel menyelidiki apakah sin t = sin(-t) merupakan identitas.; Apa yang dilakukan Abel tersebut tidak tepat. Temukan kesalahannya!
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip-prinsip dasar pembuktian (konseptual) dan bagaimana manipulasi aljabar (prosedural) mempengaruhi kebenaran pernyataan matematika.. Bukti: sin t = sin(-t) (persamaan yang diberikan); (sin t)^2 = [sin(-t)]^2 (kuadratkan kedua ruas); Abel keliru mengasumsikan sin t = sin(–t) sudah benar sejak awal
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemahaman konseptual tentang logika pembuktian dan ekuivalensi, bukan sekadar prosedur rutin. Siswa harus menganalisis langkah-langkah yang diberikan untuk menemukan cacat logika.. Bukti: Menemukan Kesalahan. Abel menyelidiki apakah sin t = sin(-t) merupakan identitas.; Abel keliru mengasumsikan sin t = sin(–t) sudah benar sejak awal (padahal itu yang ingin dibuktikan), dan mengkuadratkan kedua ruas tidak selalu menghasilkan persamaan yang ekuivalen.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang fungsi ganjil/genap trigonometri dan prinsip dasar logika pembuktian/ekuivalensi persamaan. |
| dependentSteps | 3 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan mampu melakukan analisis kritis terhadap pembuktian identitas trigonometri, melampaui sekadar manipulasi simbol. |

Run 2 — solusi: Mengkuadratkan kedua ruas persamaan (a=b menjadi a^2=b^2) tidak menjamin ekuivalensi. Jika a^2=b^2 benar, belum tentu a=b benar (bisa jadi a=-b). Abel membuktikan bahwa sin^2(t) = sin^2(-t) adalah identitas, namun ini tidak membuktikan sin(t) = sin(-t) karena sin(t) = -sin(-t) juga memenuhi kuadrat yang sama.
- Domain kognitif `classify/reasoning`: Soal menuntut siswa untuk menganalisis validitas langkah logika dalam pembuktian matematika, bukan sekadar menghitung. Siswa harus memahami konsep ekuivalensi dalam manipulasi aljabar (pengkuadratan) dan sifat fungsi trigonometri.. Bukti: Abel menyelidiki apakah sin t = sin(-t) merupakan identitas; mengkuadratkan kedua ruas bisa menghasilkan pernyataan yang tidak ekuivalen dengan pernyataan awal
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip konseptual tentang kapan suatu operasi (seperti pengkuadratan) mempertahankan ekuivalensi persamaan dan bagaimana hal itu mempengaruhi validitas pembuktian identitas.. Bukti: sin t = sin(-t) (persamaan yang diberikan); (sin t)^2 = [sin(-t)]^2 (kuadratkan kedua ruas); mengkuadratkan kedua ruas tidak selalu menghasilkan persamaan yang ekuivalen
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemahaman konseptual tentang logika pembuktian dan ekuivalensi, bukan sekadar prosedur rutin. Siswa harus mengevaluasi langkah-langkah yang diberikan untuk menemukan kesalahan logis.. Bukti: Temukan kesalahannya!; Abel keliru mengasumsikan sin t = sin(–t) sudah benar sejak awal; mengkuadratkan kedua ruas tidak selalu menghasilkan persamaan yang ekuivalen

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang identitas trigonometri dan sifat fungsi ganjil/genap, serta logika dasar pembuktian matematika. |
| dependentSteps | 3 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan mampu melakukan pembuktian identitas trigonometri dan memahami batasan manipulasi aljabar dalam pembuktian. |

Run 3 — solusi: Abel melakukan kesalahan logika dengan mengkuadratkan kedua ruas persamaan yang belum terbukti kebenarannya. Operasi kuadrat (f(x) -> f(x)^2) tidak selalu menghasilkan ekuivalensi (bisa mengubah pernyataan salah menjadi benar, contoh: 1 = -1 menjadi 1 = 1). Kesimpulan Abel bahwa sin t = sin(-t) adalah identitas berdasarkan hasil akhir sin^2 t = sin^2 t adalah sesat karena langkah tersebut tidak membuktikan pernyataan awal.
- Domain kognitif `classify/reasoning`: Soal ini menuntut siswa untuk mengevaluasi validitas argumen logis dan memahami sifat ekuivalensi dalam manipulasi aljabar/trigonometri, bukan sekadar menghitung nilai.. Bukti: Abel menyelidiki apakah sin t = sin(-t) merupakan identitas.; Pada langkah terakhir, Abel mendapatkan bentuk di ruas kiri sama dengan bentuk di ruas kanan. Dengan demikian, dia menyimpulkan bahwa sin t = sin (–t) merupakan identitas.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip konseptual tentang ekuivalensi persamaan dan bagaimana operasi matematika (seperti penguadratan) dapat mengubah domain kebenaran suatu pernyataan.. Bukti: mengkuadratkan kedua ruas tidak selalu menghasilkan persamaan yang ekuivalen
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemahaman konseptual tentang logika pembuktian dan ekuivalensi, bukan sekadar prosedur rutin. Siswa harus menganalisis langkah-langkah yang diberikan untuk menemukan cacat logika.. Bukti: Apa yang dilakukan Abel tersebut tidak tepat. Temukan kesalahannya!; mengkuadratkan kedua ruas tidak selalu menghasilkan persamaan yang ekuivalen

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi trigonometri (fungsi ganjil) dan prinsip dasar ekuivalensi persamaan. |
| dependentSteps | 3 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan mampu melakukan analisis kritis terhadap argumen matematika, melampaui sekadar manipulasi simbolik. |

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
Kelas: 11
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

Label advisory blind: `{"mathCognitiveDomain": "reasoning", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "reasoning", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
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
Solusi minimum hasil AI: b/sin 45° = 15/sin 30° -> b = 15 * (1/2 * sqrt(2)) / (1/2) = 15 * sqrt(2)
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `af20b4d77803b894dec4cad86456bac8985cd1d4d4bd3587ab76332e21a36924`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2836 |
| 2 | success | valid / verified | applying | procedural | Easy | 2145 |
| 3 | success | valid / verified | applying | procedural | Easy | 2118 |

Run 1 — solusi: b/sin 45° = 15/sin 30° -> b = 15 * (1/2 * sqrt(2)) / (1/2) = 15 * sqrt(2)
- Domain kognitif `classify/applying`: Siswa diminta menerapkan aturan sinus secara langsung untuk mencari panjang sisi segitiga.. Bukti: Jika ∠A = 30°, ∠B = 45°, dan a = 15, tentukan panjang b.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan aturan sinus dalam segitiga.. Bukti: Jika ∠A = 30°, ∠B = 45°, dan a = 15, tentukan panjang b.
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung rumus aturan sinus dengan angka yang sederhana dan familiar bagi siswa kelas 11.. Bukti: Jika ∠A = 30°, ∠B = 45°, dan a = 15, tentukan panjang b.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Nilai sinus sudut istimewa (30°, 45°). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal standar aturan sinus yang merupakan materi dasar trigonometri kelas 11. |

Run 2 — solusi: Menggunakan aturan sinus: b/sin(45°) = 15/sin(30°). Maka b = 15 * (sin(45°)/sin(30°)) = 15 * ((1/2 * √2) / (1/2)) = 15√2.
- Domain kognitif `classify/applying`: Soal meminta penerapan langsung rumus aturan sinus untuk mencari panjang sisi segitiga. Siswa hanya perlu memilih prosedur yang tepat dan melakukan substitusi nilai trigonometri sudut istimewa.. Bukti: Jika ∠A = 30°, ∠B = 45°, dan a = 15, tentukan panjang b.
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang penggunaan aturan sinus untuk menyelesaikan masalah geometri segitiga.. Bukti: Jika ∠A = 30°, ∠B = 45°, dan a = 15, tentukan panjang b.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan satu prosedur utama (aturan sinus) dan beban perhitungan yang rendah karena menggunakan sudut istimewa.. Bukti: Jika ∠A = 30°, ∠B = 45°, dan a = 15, tentukan panjang b.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai trigonometri sudut istimewa dan aturan sinus. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan penerapan dasar aturan sinus yang sesuai untuk kelas 11 sebagai pengingat atau latihan awal sebelum masuk ke kasus yang lebih kompleks. |

Run 3 — solusi: Menggunakan aturan sinus: b/sin(45°) = 15/sin(30°). Maka b = 15 * (sin(45°)/sin(30°)) = 15 * ((1/2 * √2) / (1/2)) = 15√2.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus aturan sinus secara langsung untuk mencari panjang sisi yang belum diketahui. Ini adalah prosedur standar dalam trigonometri.. Bukti: Jika ∠A = 30°, ∠B = 45°, dan a = 15, tentukan panjang b.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap prinsip aturan sinus dan kemampuan prosedural dalam menghitung nilai trigonometri sudut istimewa.. Bukti: aturan sinus
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan satu langkah utama (substitusi ke rumus aturan sinus) dan menggunakan sudut istimewa yang familiar bagi siswa kelas 11.. Bukti: Jika ∠A = 30°, ∠B = 45°, dan a = 15, tentukan panjang b.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai trigonometri sudut istimewa dan aturan sinus. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi aturan sinus adalah dasar trigonometri kelas 11 yang prosedurnya sangat langsung dan rutin. |

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

Kunci sumber: `D`; status AI: `conflict`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: Berdasarkan aturan sinus, sin B = (b * sin C) / c = (10 * sin 145°) / 6 ≈ 0,956. Namun, karena b > c, maka ∠B harus > ∠C (145°). Jika ∠B > 145° dan ∠C = 145°, maka ∠B + ∠C > 290°, yang melanggar aturan jumlah sudut segitiga (180°). Segitiga ini tidak mungkin terbentuk.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e84265f0eb0f424e911efd3ebf782faed8879bd91130e681ca183fff5b3bed29`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | concern / conflict | applying | procedural | Medium | 2223 |
| 2 | success | concern / conflict | applying | procedural | Medium | 2274 |
| 3 | success | concern / conflict | applying | procedural | Easy | 2297 |

Run 1 — solusi: Segitiga tidak mungkin terbentuk karena sisi c (6) lebih pendek dari sisi b (10), padahal sudut C (145°) adalah sudut tumpul (sudut terbesar). Menurut aturan sinus, sin B = (b * sin C) / c = (10 * sin 145°) / 6 ≈ 0,956. Meskipun secara kalkulasi sin B menghasilkan nilai, secara geometris segitiga ini tidak valid.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan aturan sinus untuk mencari sudut yang tidak diketahui. Meskipun prosedurnya rutin, soal ini secara geometris tidak valid.. Bukti: Jika ∠C = 145°, b = 10, dan c = 6, tentukan besar sudut B.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami dan menerapkan algoritma aturan sinus untuk menyelesaikan masalah.. Bukti: sinB/b = sinC/c
- Intended difficulty `classify/Medium`: Secara prosedural, soal ini hanya memerlukan substitusi langsung ke rumus aturan sinus. Namun, karena soal ini secara geometris tidak mungkin, tingkat kesulitan menjadi tidak relevan.. Bukti: Jika ∠C = 145°, b = 10, dan c = 6, tentukan besar sudut B.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Aturan sinus dan konsep dasar segitiga. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi aturan sinus adalah standar kelas 11. Soal ini rutin namun cacat secara geometris. |

Run 2 — solusi: Berdasarkan aturan sinus, sin B = (b * sin C) / c = (10 * sin 145°) / 6 ≈ 0,956. Namun, karena b > c, maka ∠B harus > ∠C (145°). Nilai arcsin(0,956) ≈ 72,93° tidak memenuhi syarat segitiga karena 72,93° < 145°. Soal ini tidak memiliki solusi segitiga yang valid.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan aturan sinus untuk mencari sudut yang tidak diketahui. Ini melibatkan pemilihan prosedur rutin (aturan sinus) dan manipulasi aljabar sederhana, yang termasuk dalam domain applying.. Bukti: Jika ∠C = 145°, b = 10, dan c = 6, tentukan besar sudut B.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau teknik aturan sinus untuk menyelesaikan masalah segitiga.. Bukti: Aturan Sinus: sinB/b = sinC/c
- Intended difficulty `classify/Medium`: Secara prosedural, soal ini hanya memerlukan substitusi ke rumus aturan sinus. Namun, karena soal ini secara matematis tidak valid (tidak mungkin membentuk segitiga), tingkat kesulitan teknisnya rendah namun jebakannya fatal.. Bukti: Jika ∠C = 145°, b = 10, dan c = 6, tentukan besar sudut B.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Aturan sinus dan sifat dasar segitiga. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi aturan sinus adalah standar kelas 11. Soal ini rutin secara prosedural namun cacat secara konsep geometri. |

Run 3 — solusi: Berdasarkan aturan sinus: sin B / b = sin C / c. Maka sin B = (b * sin C) / c = (10 * sin 145°) / 6 ≈ 0,956. Namun, karena b > c, maka ∠B harus > ∠C (145°). Ini mustahil karena ∠B + ∠C harus < 180°. Segitiga tidak mungkin terbentuk.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan aturan sinus untuk mencari sudut yang tidak diketahui. Meskipun prosedurnya rutin, soal ini mengandung kontradiksi geometris yang membuat penyelesaiannya tidak valid.. Bukti: Jika ∠C = 145°, b = 10, dan c = 6, tentukan besar sudut B.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami dan menerapkan algoritma aturan sinus untuk menyelesaikan masalah trigonometri.. Bukti: Aturan Sinus: sinB/b = sinC/c
- Intended difficulty `classify/Easy`: Secara prosedural, soal ini adalah penerapan langsung aturan sinus (Easy). Namun, karena soal tidak valid secara geometris, tingkat kesulitan menjadi tidak relevan.. Bukti: Jika ∠C = 145°, b = 10, dan c = 6, tentukan besar sudut B.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Aturan sinus dasar |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penerapan aturan sinus adalah materi standar kelas 11, namun soal ini cacat secara konsep segitiga. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3842`.
Konten: `concern`; kunci: `conflict`; masalah: Soal secara geometris tidak valid. Dalam segitiga, sudut terbesar harus berhadapan dengan sisi terpanjang. Di sini, ∠C = 145° adalah sudut tumpul (sudut terbesar), sehingga sisi c harus menjadi sisi terpanjang. Namun, diberikan c = 6 dan b = 10 (b > c), yang berarti ∠B harus lebih besar dari ∠C. Jika ∠C = 145°, maka ∠B harus > 145°, yang membuat jumlah sudut segitiga (∠A+∠B+∠C) > 180°. Segitiga ini mustahil ada..
- Domain kognitif `applying`: Siswa diminta menerapkan aturan sinus untuk mencari sudut yang tidak diketahui. Meskipun prosedurnya rutin, soal ini mengandung kontradiksi geometris yang membuat penyelesaiannya tidak valid secara matematis.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang algoritma atau teknik aturan sinus untuk menyelesaikan masalah segitiga.
- Intended difficulty `Easy`: Secara prosedural, soal ini adalah penerapan langsung aturan sinus (Easy). Namun, karena soal tidak valid secara geometris, tingkat kesulitan teknisnya rendah namun jebakannya fatal.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Aturan sinus dan sifat dasar segitiga. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penerapan aturan sinus adalah materi standar kelas 11, namun soal ini cacat secara konsep segitiga. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `revision_required`.
Status konten: `concern`. Catatan konten: Soal secara geometris tidak valid. Dalam segitiga, sudut terbesar harus berhadapan dengan sisi terpanjang. Di sini, ∠C = 145° adalah sudut tumpul (sudut terbesar), sehingga sisi c harus menjadi sisi terpanjang. Namun, diberikan c = 6 dan b = 10 (b > c), yang berarti ∠B harus lebih besar dari ∠C. Jika ∠C = 145°, maka ∠B harus > 145°, yang membuat jumlah sudut segitiga (∠A+∠B+∠C) > 180°. Segitiga ini mustahil ada..
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
Solusi minimum hasil AI: c^2 = a^2 + b^2 - 2ab cos C = 6^2 + 10^2 - 2(6)(10)(0.5) = 36 + 100 - 60 = 76. Maka c = sqrt(76) = 2*sqrt(19).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9a7b3fa43caa3b6432e1b1f7b6ae89c0f4383e6063889e995973c8b3e8bc44d0`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2155 |
| 2 | success | valid / verified | applying | procedural | Easy | 2147 |
| 3 | success | valid / verified | applying | procedural | Easy | 2151 |

Run 1 — solusi: c^2 = a^2 + b^2 - 2ab cos C = 6^2 + 10^2 - 2(6)(10)(0.5) = 36 + 100 - 60 = 76. Maka c = sqrt(76) = 2*sqrt(19).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus aturan kosinus secara langsung untuk mencari panjang sisi segitiga. Ini adalah prosedur rutin yang melibatkan substitusi nilai ke dalam rumus yang sudah dikenal.. Bukti: Jika ∠C = 60°, a = 6, dan b = 10, panjang c adalah ….
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa tentang algoritma aturan kosinus untuk menyelesaikan masalah geometri segitiga.. Bukti: Jika ∠C = 60°, a = 6, dan b = 10, panjang c adalah ….
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (straightforward) dengan satu rumus utama dan beban perhitungan yang rendah, sesuai untuk tingkat kemahiran dasar kelas 11.. Bukti: Jika ∠C = 60°, a = 6, dan b = 10, panjang c adalah ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar trigonometri dan aturan kosinus. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan aplikasi standar aturan kosinus yang diharapkan dikuasai siswa kelas 11 sebagai prosedur rutin. |

Run 2 — solusi: c^2 = a^2 + b^2 - 2ab cos C = 6^2 + 10^2 - 2(6)(10)(0.5) = 36 + 100 - 60 = 76. Maka c = sqrt(76) = 2sqrt(19).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus aturan kosinus secara langsung untuk mencari panjang sisi segitiga. Ini adalah prosedur rutin yang sudah dipelajari.. Bukti: Jika ∠C = 60°, a = 6, dan b = 10, panjang c adalah ….
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman dan penggunaan algoritma aturan kosinus (prosedural) serta pemahaman hubungan antar sisi dan sudut dalam segitiga (konseptual).. Bukti: c² = a²+b²-2ab·cosC
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung rumus aturan kosinus dengan angka yang sederhana. Tidak ada langkah non-rutin atau integrasi konsep yang kompleks.. Bukti: Jika ∠C = 60°, a = 6, dan b = 10, panjang c adalah ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar trigonometri dan aturan kosinus. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 11, penggunaan aturan kosinus adalah materi standar yang bersifat rutin dan langsung. |

Run 3 — solusi: c^2 = a^2 + b^2 - 2ab cos C = 6^2 + 10^2 - 2(6)(10)(0.5) = 36 + 100 - 60 = 76. Maka c = sqrt(76) = 2sqrt(19).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus aturan kosinus secara langsung untuk mencari panjang sisi segitiga. Ini adalah prosedur standar yang rutin.. Bukti: Jika ∠C = 60°, a = 6, dan b = 10, panjang c adalah ….
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman dan penerapan algoritma aturan kosinus (prosedural) serta pemahaman hubungan antar sisi dan sudut dalam segitiga (konseptual).. Bukti: c² = a²+b²-2ab·cosC
- Intended difficulty `classify/Easy`: Soal ini merupakan aplikasi langsung dari rumus aturan kosinus tanpa modifikasi atau langkah tambahan yang kompleks.. Bukti: Jika ∠C = 60°, a = 6, dan b = 10, panjang c adalah ….

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar trigonometri dan aturan kosinus. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi aturan kosinus adalah standar kelas 11 TL. Soal ini hanya memerlukan substitusi nilai ke dalam rumus, sehingga dikategorikan mudah. |

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
| 1 | success | valid / verified | applying | procedural | Easy | 2189 |
| 2 | success | valid / verified | applying | procedural | Easy | 2189 |
| 3 | success | valid / verified | applying | procedural | Easy | 2158 |

Run 1 — solusi: Menggunakan aturan kosinus: cos B = (a^2 + c^2 - b^2) / (2ac). Substitusi nilai: cos B = (12^2 + 8^2 - 14^2) / (2 * 12 * 8) = (144 + 64 - 196) / 192 = 12 / 192 = 0,0625. Maka, B = arccos(0,0625) ≈ 86,42°.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus aturan kosinus secara langsung untuk mencari sudut segitiga yang diketahui ketiga sisinya. Ini adalah prosedur standar yang rutin.. Bukti: Jika a = 12, b = 14, dan c = 8, besar sudut B adalah
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang penggunaan rumus aturan kosinus untuk menyelesaikan masalah geometri.. Bukti: Jika a = 12, b = 14, dan c = 8, besar sudut B adalah
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan satu prosedur utama (aturan kosinus) dan beban komputasi yang rendah.. Bukti: Jika a = 12, b = 14, dan c = 8, besar sudut B adalah

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
| gradeRelativeRationale | Materi aturan kosinus adalah standar kelas 11. Soal ini langsung menguji penerapan rumus tanpa modifikasi atau langkah tambahan yang kompleks. |

Run 2 — solusi: Menggunakan aturan kosinus: cos B = (a^2 + c^2 - b^2) / (2ac). Substitusi nilai: cos B = (12^2 + 8^2 - 14^2) / (2 * 12 * 8) = (144 + 64 - 196) / 192 = 12 / 192 = 0,0625. Maka, B = arccos(0,0625) ≈ 86,42°.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus aturan kosinus secara langsung untuk mencari besar sudut segitiga. Ini adalah prosedur rutin yang sudah dipelajari.. Bukti: Jika a = 12, b = 14, dan c = 8, besar sudut B adalah
- Dimensi pengetahuan `classify/procedural`: Soal memerlukan pemahaman tentang hubungan antara panjang sisi dan besar sudut dalam segitiga (konsep) serta penggunaan algoritma aturan kosinus (prosedural).. Bukti: Jika a = 12, b = 14, dan c = 8, besar sudut B adalah
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (straightforward) dengan satu prosedur standar yang harus diikuti tanpa modifikasi strategi atau integrasi konsep yang kompleks.. Bukti: Jika a = 12, b = 14, dan c = 8, besar sudut B adalah

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
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi aturan kosinus adalah standar kelas 11. Soal ini hanya menuntut substitusi nilai ke dalam rumus yang sudah dikenal. |

Run 3 — solusi: Menggunakan aturan kosinus: cos B = (a² + c² - b²) / (2ac). Substitusi nilai: cos B = (12² + 8² - 14²) / (2 * 12 * 8) = (144 + 64 - 196) / 192 = 12 / 192 = 0,0625. Maka B = arccos(0,0625) ≈ 86,42°.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus aturan kosinus secara langsung untuk mencari sudut segitiga. Ini adalah prosedur rutin yang sudah dipelajari.. Bukti: Jika a = 12, b = 14, dan c = 8, besar sudut B adalah
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang penggunaan rumus aturan kosinus untuk menyelesaikan masalah geometri.. Bukti: cosB = (a²+c²-b²)/(2ac)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan satu langkah utama (substitusi ke rumus aturan kosinus). Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: a = 12, b = 14, dan c = 8; besar sudut B adalah

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
| gradeRelativeRationale | Aturan kosinus adalah materi standar kelas 11. Soal ini hanya meminta aplikasi langsung rumus tanpa variasi atau konteks tambahan. |

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

![Gambar sumber soal 33](<../images/kelas10_panduan_siswa_kelas10.pdf-0110-05.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Pada segitiga siku-siku PQR, QR adalah sisi samping sudut Q (36,8°) dan QP adalah sisi miring. Rasio QR/QP = cos(Q) = cos(36,8°).
Gambar sumber: images/kelas10_panduan_siswa_kelas10.pdf-0110-05.png. Transkripsi visual: Segitiga siku-siku PQR dengan sudut siku-siku di R. Sisi PR = 3, sisi QR = 4, sisi miring PQ = 5. Sudut P = 53,2 derajat, sudut Q = 36,8 derajat.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7dcc789a77d012a9f9bae897d726d124ebe2a5907b63618bc23a4b810ac528a8`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3313 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3274 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3289 |

Run 1 — solusi: Pada segitiga siku-siku PQR, QR adalah sisi samping sudut Q (36,8°) dan QP adalah sisi miring. Rasio QR/QP = cos(Q) = cos(36,8°).
- Domain kognitif `classify/applying`: Siswa diminta mengidentifikasi rasio trigonometri dasar (cosinus) berdasarkan posisi sisi terhadap sudut dalam segitiga siku-siku. Ini adalah proses penerapan definisi trigonometri pada situasi rutin.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang hubungan antara rasio sisi segitiga dan fungsi trigonometri (konsep dasar trigonometri).. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung, menggunakan representasi segitiga yang sudah diberikan lengkap dengan panjang sisi dan sudutnya. Siswa hanya perlu mengenali definisi cosinus.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai

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
| gradeRelativeRationale | Meskipun materi trigonometri diajarkan di kelas 10, soal ini menguji pemahaman dasar yang menjadi prasyarat untuk materi trigonometri kelas 11 (seperti identitas atau fungsi trigonometri). Tingkat kesulitannya rendah karena tidak memerlukan manipulasi aljabar atau strategi kompleks. |

Run 2 — solusi: Pada segitiga siku-siku PQR, QR adalah sisi samping sudut Q (36,8°) dan QP adalah sisi miring. Rasio QR/QP = cos(Q) = cos(36,8°).
- Domain kognitif `classify/applying`: Siswa diminta mengidentifikasi rasio trigonometri dasar (cosinus) berdasarkan posisi sisi terhadap sudut tertentu dalam segitiga siku-siku.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi rasio trigonometri (sinus, cosinus, tangen) pada segitiga siku-siku.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung dengan representasi visual yang jelas. Siswa hanya perlu mengenali definisi cosinus sebagai perbandingan sisi samping terhadap sisi miring.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai

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
| gradeRelativeRationale | Meskipun materi trigonometri dasar, soal ini sangat mendasar dan tidak menuntut integrasi konsep yang kompleks, sehingga tergolong mudah untuk level kelas 11. |

Run 3 — solusi: Pada segitiga PQR, QR adalah sisi samping sudut Q (36,8°) dan QP adalah sisi miring. Rasio QR/QP = cos(Q) = cos(36,8°).
- Domain kognitif `classify/applying`: Siswa diminta mengidentifikasi rasio trigonometri dasar berdasarkan posisi sisi terhadap sudut tertentu dalam segitiga siku-siku. Ini adalah penerapan langsung definisi kosinus.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang definisi perbandingan trigonometri (sinus, kosinus, tangen) dalam segitiga siku-siku.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan pengenalan sisi samping dan miring terhadap sudut Q untuk menentukan rasio kosinus.. Bukti: Nilai perbandingan panjang sisi QR dan QP sama dengan nilai

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi perbandingan trigonometri dasar (sin, cos, tan) pada segitiga siku-siku. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi trigonometri diajarkan di kelas 10, soal ini terlalu sederhana untuk standar kelas 11 Matematika Tingkat Lanjut yang seharusnya lebih fokus pada identitas, grafik, atau aturan sinus/kosinus pada segitiga sembarang. |

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
Transkripsi visual: Segitiga siku-siku PQR dengan sudut siku-siku di R. Sisi PR = 3, sisi QR = 4, sisi miring PQ = 5. Sudut P = 53,2 derajat, sudut Q = 36,8 derajat.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: Komponen vektor = (x2-x1, y2-y1) = (1-6, -5-2) = (-5, -7). Panjang vektor = sqrt((-5)^2 + (-7)^2) = sqrt(25 + 49) = sqrt(74).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi', 'menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `981dfca1fd20731325ef87c72244be8759dc89aecb849ad86d3dc48bad6d3707`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2086 |
| 2 | success | valid / verified | applying | procedural | Easy | 2901 |
| 3 | success | valid / verified | applying | procedural | Easy | 2113 |

Run 1 — solusi: Komponen vektor = (x2-x1, y2-y1) = (1-6, -5-2) = (-5, -7). Panjang vektor = sqrt((-5)^2 + (-7)^2) = sqrt(25 + 49) = sqrt(74).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur standar untuk menentukan komponen vektor (ujung dikurangi pangkal) dan menghitung panjang vektor menggunakan teorema Pythagoras. Ini adalah penerapan langsung dari definisi vektor pada situasi rutin.. Bukti: Sebuah vektor memiliki pangkal di (6, 2) dan ujung di (1, –5). Tentukan bentuk komponen vektor tersebut, kemudian hitung panjangnya.
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut pemahaman dan penggunaan algoritma atau teknik spesifik (prosedur) untuk mencari komponen dan panjang vektor.. Bukti: Tentukan bentuk komponen vektor tersebut, kemudian hitung panjangnya.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan langkah-langkah yang jelas dan familiar bagi siswa kelas 11. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: Sebuah vektor memiliki pangkal di (6, 2) dan ujung di (1, –5). Tentukan bentuk komponen vektor tersebut, kemudian hitung panjangnya.

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
| gradeRelativeRationale | Materi vektor merupakan dasar di kelas 11 TL. Soal ini menguji pemahaman dasar komponen dan panjang vektor yang merupakan prosedur standar. |

Run 2 — solusi: Komponen vektor = (1-6, -5-2) = (-5, -7). Panjang vektor = sqrt((-5)^2 + (-7)^2) = sqrt(25 + 49) = sqrt(74).
- Domain kognitif `classify/applying`: Siswa menerapkan prosedur standar untuk menentukan komponen vektor (ujung dikurangi pangkal) dan menghitung panjang vektor menggunakan teorema Pythagoras.. Bukti: Sebuah vektor memiliki pangkal di (6, 2) dan ujung di (1, –5). Tentukan bentuk komponen vektor tersebut, kemudian hitung panjangnya.
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penerapan algoritma atau prosedur baku dalam geometri vektor.. Bukti: Tentukan bentuk komponen vektor tersebut, kemudian hitung panjangnya.
- Intended difficulty `classify/Easy`: Soal bersifat rutin dengan dua langkah perhitungan yang langsung. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: Sebuah vektor memiliki pangkal di (6, 2) dan ujung di (1, –5). Tentukan bentuk komponen vektor tersebut, kemudian hitung panjangnya.

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
| gradeRelativeRationale | Materi vektor dasar yang merupakan prosedur standar di kelas 11. |

Run 3 — solusi: Komponen vektor = (x2-x1, y2-y1) = (1-6, -5-2) = (-5, -7). Panjang vektor = sqrt((-5)^2 + (-7)^2) = sqrt(25+49) = sqrt(74).
- Domain kognitif `classify/applying`: Soal meminta penerapan langsung rumus komponen vektor (ujung - pangkal) dan rumus panjang vektor (teorema Pythagoras). Ini adalah prosedur rutin yang dipelajari di kelas 11.. Bukti: Sebuah vektor memiliki pangkal di (6, 2) dan ujung di (1, –5). Tentukan bentuk komponen vektor tersebut, kemudian hitung panjangnya.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menerapkan algoritma atau urutan langkah standar untuk menentukan komponen dan panjang vektor.. Bukti: Tentukan bentuk komponen vektor tersebut, kemudian hitung panjangnya.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan langkah-langkah yang jelas dan familiar bagi siswa kelas 11. Tidak ada strategi non-rutin atau integrasi konsep yang kompleks.. Bukti: Sebuah vektor memiliki pangkal di (6, 2) dan ujung di (1, –5). Tentukan bentuk komponen vektor tersebut, kemudian hitung panjangnya.

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
| gradeRelativeRationale | Materi vektor dasar adalah standar awal kelas 11. Soal ini menguji pemahaman dasar tanpa variasi atau tingkat kesulitan tambahan. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: Vektor dalam bentuk komponen <a, b> dapat ditulis sebagai kombinasi linear ai + bj. Untuk vektor <-4, 12>, maka a = -4 dan b = 12. Jadi, bentuknya adalah -4i + 12j.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `aa50adb453f2934211d0c581bdbd2cf3fcab542c6d5451879088991b523d4ddb`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2052 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2065 |
| 3 | success | valid / verified | knowing | factual | Easy | 2087 |

Run 1 — solusi: Vektor satuan baku i = <1, 0> dan j = <0, 1>. Maka, <a, b> = a<1, 0> + b<0, 1> = ai + bj. Untuk vektor <-4, 12>, maka -4i + 12j.
- Domain kognitif `classify/knowing`: Soal ini hanya meminta siswa untuk mengubah representasi vektor dari bentuk komponen ke bentuk kombinasi linear vektor satuan baku. Ini adalah proses langsung yang bersifat mengingat definisi dasar vektor satuan.. Bukti: Vektor < -4,12 > dapat dituliskan ke dalam kombinasi vektor-vektor satuan baku i dan j
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami definisi dan notasi vektor satuan baku (i dan j) serta bagaimana komponen vektor dipetakan ke koefisien vektor satuan tersebut.. Bukti: kombinasi vektor-vektor satuan baku i dan j
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan pemahaman notasi vektor tanpa langkah perhitungan yang kompleks atau strategi khusus.. Bukti: Vektor < -4,12 > dapat dituliskan ke dalam kombinasi vektor-vektor satuan baku i dan j

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi vektor satuan baku i dan j. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi vektor ada di kelas 11, soal ini adalah pengenalan dasar notasi yang sangat rutin dan tidak menuntut kemampuan analisis tingkat lanjut. |

Run 2 — solusi: Vektor dalam bentuk komponen <a, b> dapat ditulis sebagai ai + bj. Untuk vektor <-4, 12>, maka a = -4 dan b = 12. Jadi, bentuk kombinasi linearnya adalah -4i + 12j.
- Domain kognitif `classify/knowing`: Soal ini hanya meminta siswa untuk mengubah representasi vektor dari bentuk komponen ke bentuk kombinasi linear standar. Ini adalah proses langsung yang tidak memerlukan strategi kompleks atau pemecahan masalah.. Bukti: Vektor < -4, 12 > dapat dituliskan ke dalam kombinasi vektor-vektor satuan baku i dan j
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami definisi dan notasi vektor satuan baku (i dan j) serta bagaimana komponen vektor dipetakan ke koefisien vektor satuan tersebut.. Bukti: Vektor < -4, 12 > dapat dituliskan ke dalam kombinasi vektor-vektor satuan baku i dan j
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan pemahaman notasi vektor tanpa langkah perhitungan yang berarti atau pemilihan strategi.. Bukti: Vektor < -4, 12 > dapat dituliskan ke dalam kombinasi vektor-vektor satuan baku i dan j

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang notasi vektor komponen dan vektor satuan i, j. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi vektor diajarkan di kelas 11, soal ini berada pada tingkat pengenalan notasi yang sangat dasar, sehingga dikategorikan Easy. |

Run 3 — solusi: Vektor v = <x, y> dapat dinyatakan sebagai xi + yj. Untuk v = <-4, 12>, maka x = -4 dan y = 12. Substitusi nilai tersebut menghasilkan -4i + 12j.
- Domain kognitif `classify/knowing`: Soal ini hanya meminta siswa untuk memahami definisi dasar representasi vektor dalam bentuk kombinasi linear vektor satuan i dan j. Tidak ada strategi kompleks atau pemecahan masalah yang diperlukan.. Bukti: Vektor < -4,12 > dapat dituliskan ke dalam kombinasi vektor-vektor satuan baku i dan j
- Dimensi pengetahuan `classify/factual`: Siswa perlu mengetahui definisi atau fakta bahwa komponen vektor (x, y) berkorespondensi langsung dengan koefisien pada basis i dan j (xi + yj).. Bukti: Vektor < -4,12 > dapat dituliskan ke dalam kombinasi vektor-vektor satuan baku i dan j
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural dasar dan sangat familiar bagi siswa yang baru mempelajari vektor. Tidak ada langkah tambahan atau manipulasi yang diperlukan.. Bukti: Vektor < -4,12 > dapat dituliskan ke dalam kombinasi vektor-vektor satuan baku i dan j

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang komponen vektor dan vektor satuan i, j. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi vektor diajarkan di kelas 11, soal ini berada pada tingkat pengenalan notasi dasar, sehingga dikategorikan Easy. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 2, "factual": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3528`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini hanya meminta siswa untuk mengubah representasi vektor dari bentuk komponen ke bentuk kombinasi linear vektor satuan baku. Ini adalah proses langsung yang bersifat mengingat definisi dasar vektor satuan.
- Dimensi pengetahuan `conceptual`: Siswa perlu memahami definisi dan notasi vektor satuan baku (i dan j) serta bagaimana komponen vektor dipetakan ke koefisien vektor satuan tersebut.
- Intended difficulty `Easy`: Soal ini sangat mendasar, hanya memerlukan pemahaman notasi vektor tanpa langkah perhitungan yang kompleks atau strategi khusus.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi vektor satuan baku i dan j. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi vektor ada di kelas 11, soal ini adalah pengenalan dasar notasi yang sangat rutin dan tidak menuntut kemampuan analisis tingkat lanjut. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
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
Solusi minimum hasil AI: Usaha (W) adalah hasil kali titik antara gaya (F) dan perpindahan (d). W = \|F\|\|d\|cos(θ). Arah utara dan timur laut membentuk sudut θ = 45°. Maka, W = 500 N * 100 m * cos(45°) = 50.000 * (1/2 √2) = 25.000√2 J.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9ab7b5d3baf8be475b625807102bc45af3caba3b22af1e5a7da57daab460b77e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2253 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2226 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2239 |

Run 1 — solusi: Usaha (W) adalah hasil kali titik antara gaya (F) dan perpindahan (d). W = \|F\|\|d\|cos(θ). Arah utara dan timur laut membentuk sudut θ = 45°. Maka, W = 500 N * 100 m * cos(45°) = 50.000 * (1/2 √2) = 25.000√2 J.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi konsep hasil kali titik (dot product) dalam konteks vektor gaya dan perpindahan, serta menentukan sudut antara kedua vektor tersebut untuk menerapkan rumus W = F.d = \|F\|\|d\|cos(θ).. Bukti: Perahu layar bergerak sejauh 100 m ke utara; angin memberi gaya 500 N ke timur laut; Berapa banyak usaha yang dilakukan angin?
- Dimensi pengetahuan `classify/procedural`: Soal ini memerlukan pemahaman prosedural tentang penggunaan rumus hasil kali titik dan pengetahuan konseptual tentang hubungan sudut antara vektor gaya dan perpindahan.. Bukti: W = \|F\|\|d\|cos 45° = 500·100·(1/2 √2) = 25.000√2 J
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan translasi representasi dari deskripsi arah (utara, timur laut) menjadi sudut geometris (45°) sebelum menerapkan prosedur perhitungan rutin.. Bukti: 100 m ke utara; gaya 500 N ke timur laut; sudut antara arah utara (gerak) dan timur laut (gaya) adalah 45°

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar vektor, hasil kali titik, dan sudut arah mata angin. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Sesuai untuk kelas 11 TL yang mempelajari vektor dan aplikasinya. Memerlukan pemahaman sudut antara dua vektor yang tidak eksplisit diberikan. |

Run 2 — solusi: Usaha (W) adalah hasil kali titik antara gaya (F) dan perpindahan (d). W = \|F\|\|d\| cos(θ). Arah utara dan timur laut membentuk sudut θ = 45°. W = 500 N * 100 m * cos(45°) = 50.000 * (1/2 √2) = 25.000√2 J.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi konsep hasil kali titik (dot product) untuk menghitung usaha, menentukan sudut antara dua vektor (utara dan timur laut), dan menerapkan rumus W = \|F\|\|d\| cos θ. Ini adalah penerapan prosedur rutin pada konteks fisika.. Bukti: Perahu layar bergerak sejauh 100 m ke utara; angin memberi gaya 500 N ke timur laut; Berapa banyak usaha yang dilakukan angin?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara vektor gaya, vektor perpindahan, dan sudut di antara keduanya dalam konteks usaha, serta penggunaan algoritma dot product.. Bukti: usaha yang dilakukan angin; 100 m ke utara; gaya 500 N ke timur laut
- Intended difficulty `classify/Easy`: Soal ini memerlukan pemahaman arah mata angin untuk menentukan sudut (45 derajat) dan penerapan rumus dasar usaha. Langkah-langkahnya rutin dan langsung.. Bukti: 100 m ke utara; gaya 500 N ke timur laut; Berapa banyak usaha yang dilakukan angin?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar vektor, arah mata angin, dan trigonometri sudut istimewa. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan aplikasi standar vektor di kelas 11, namun prosedurnya sangat langsung dan tidak memerlukan strategi non-rutin. |

Run 3 — solusi: Usaha (W) adalah hasil kali titik antara vektor gaya (F) dan vektor perpindahan (d). W = \|F\|\|d\|cos(θ). Arah utara dan timur laut membentuk sudut θ = 45°. W = 500 N * 100 m * cos(45°) = 50.000 * (1/2 √2) = 25.000√2 J.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa masalah usaha (work) dalam konteks vektor dapat diselesaikan dengan operasi hasil kali titik (dot product) dan menentukan sudut yang tepat antara dua vektor arah (utara dan timur laut).. Bukti: Berapa banyak usaha yang dilakukan angin?; perahu layar bergerak sejauh 100 m ke utara, sedangkan angin memberi gaya 500 N ke timur laut
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman konseptual tentang hubungan antara vektor gaya, vektor perpindahan, dan sudut di antara keduanya untuk menghitung usaha.. Bukti: usaha yang dilakukan angin; gaya 500 N ke timur laut; sejauh 100 m ke utara
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemahaman tentang representasi vektor dalam konteks fisik dan penerapan rumus dot product yang rutin. Tidak ada strategi non-rutin yang kompleks.. Bukti: 100 m ke utara; gaya 500 N ke timur laut; sudut antara arah utara (gerak) dan timur laut (gaya) adalah 45°

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar vektor, operasi dot product, dan trigonometri sudut istimewa. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan mampu mengintegrasikan konsep vektor dengan aplikasi fisika sederhana. Tingkat kesulitan Medium karena siswa harus menentukan sudut 45 derajat dari deskripsi arah mata angin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4037`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi konsep hasil kali titik (dot product) dalam konteks vektor gaya dan perpindahan, serta menentukan sudut antara kedua vektor tersebut untuk menerapkan rumus W = F.d = \|F\|\|d\|cos(θ).
- Dimensi pengetahuan `procedural`: Soal ini memerlukan pemahaman prosedural tentang penggunaan rumus hasil kali titik dan pengetahuan konseptual tentang hubungan sudut antara vektor gaya dan perpindahan.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan translasi representasi dari deskripsi arah (utara, timur laut) menjadi sudut geometris (45°) sebelum menerapkan prosedur perhitungan rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar vektor, hasil kali titik, dan sudut arah mata angin. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Sesuai untuk kelas 11 TL yang mempelajari vektor dan aplikasinya. Memerlukan pemahaman sudut antara dua vektor yang tidak eksplisit diberikan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
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
Solusi minimum hasil AI: u · v = \|u\|\|v\| cos(θ) = 12 * 18 * cos(π/3) = 216 * 0.5 = 108.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `520c74b607a8ef06f84027e2b46aa29b0428aa3c920ebbea87262c5d5410d61f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2734 |
| 2 | success | valid / verified | applying | procedural | Easy | 2085 |
| 3 | success | valid / verified | applying | procedural | Easy | 2419 |

Run 1 — solusi: u · v = \|u\|\|v\| cos(θ) = 12 * 18 * cos(π/3) = 216 * 0.5 = 108.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus dasar hasil kali titik vektor yang melibatkan panjang vektor dan kosinus sudut apit. Proses ini bersifat rutin dan langsung.. Bukti: vektor u dan vektor v secara berturut-turut memiliki panjang 12 dan 18; besar sudut di antara kedua vektor tersebut adalah π/3; tentukan u · v
- Dimensi pengetahuan `classify/procedural`: Menggunakan algoritma atau rumus standar untuk menghitung hasil kali titik vektor.. Bukti: u · v = \|u\|\|v\|cos θ
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (straightforward) dengan prosedur yang sudah familiar bagi siswa kelas 11. Tidak ada langkah tambahan atau jebakan konseptual yang kompleks.. Bukti: panjang 12 dan 18; sudut π/3; tentukan u · v

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi hasil kali titik vektor dan nilai trigonometri sudut istimewa. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi vektor merupakan bagian standar kurikulum kelas 11 TL. Soal ini hanya menguji pemahaman rumus dasar tanpa modifikasi. |

Run 2 — solusi: u·v = \|u\|\|v\|cos(θ) = 12 * 18 * cos(π/3) = 216 * 0.5 = 108.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus dasar hasil kali titik vektor (dot product) yang melibatkan panjang vektor dan sudut apit. Ini adalah prosedur standar yang langsung.. Bukti: Vektor u dan vektor v secara berturut-turut memiliki panjang 12 dan 18. Jika besar sudut di antara kedua vektor tersebut adalah π/3, tentukan u · v.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang definisi dan algoritma perhitungan hasil kali titik vektor.. Bukti: u · v = \|u\|\|v\|cos θ
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan satu langkah penerapan rumus langsung tanpa kendala tambahan atau manipulasi kompleks.. Bukti: panjang 12 dan 18; sudut di antara kedua vektor tersebut adalah π/3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi hasil kali titik vektor dan nilai trigonometri sudut istimewa. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi vektor merupakan bagian dari kurikulum matematika tingkat lanjut kelas 11. Soal ini menguji pemahaman dasar yang diharapkan dikuasai siswa setelah mempelajari operasi vektor. |

Run 3 — solusi: u · v = \|u\|\|v\| cos(θ) = 12 * 18 * cos(π/3) = 216 * 0.5 = 108.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus dasar hasil kali titik vektor yang sudah diketahui panjang dan sudutnya. Ini adalah prosedur standar dalam matematika tingkat lanjut.. Bukti: Vektor u dan vektor v secara berturut-turut memiliki panjang 12 dan 18. Jika besar sudut di antara kedua vektor tersebut adalah π/3, tentukan u · v.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman dan penggunaan algoritma atau rumus hasil kali titik (dot product) vektor.. Bukti: u · v = \|u\|\|v\| cos(θ)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan satu langkah penyelesaian langsung menggunakan rumus dot product. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: panjang 12 dan 18; sudut di antara kedua vektor tersebut adalah π/3

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
| gradeRelativeRationale | Sesuai untuk kelas 11 karena merupakan penerapan langsung dari definisi hasil kali titik yang dipelajari di awal bab vektor. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: Berdasarkan aturan penjumlahan vektor, KL = AL - AK. Karena KA = -AK dan LA = -AL, maka KL = (-LA) - (-KA) = KA - LA.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b5b07d410d34c8538b5bb7473c124b58c973bf8086ccc86377393d460c32efdd`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3039 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3067 |
| 3 | success | valid / verified | applying | procedural | Medium | 2933 |

Run 1 — solusi: Berdasarkan aturan penjumlahan vektor, KL = AL - AK. Karena KA = -AK dan LA = -AL, maka KL = (-LA) - (-KA) = KA - LA.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan aturan dasar pengurangan vektor untuk menyatakan vektor KL dalam bentuk vektor lain yang diberikan.. Bukti: Nyatakan KL dalam KA dan LA
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman konseptual tentang hubungan antar vektor dalam segitiga dan operasi pengurangan vektor.. Bukti: Nyatakan KL dalam KA dan LA
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar dalam geometri vektor yang memerlukan satu langkah operasi pengurangan vektor dasar.. Bukti: titik K adalah titik tengah dari AB dan titik L adalah titik tengah dari AC; Nyatakan KL dalam KA dan LA

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dan pengurangan vektor dasar |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL sudah familiar dengan operasi vektor dasar. Soal ini hanya memerlukan manipulasi aljabar vektor satu langkah. |

Run 2 — solusi: Berdasarkan aturan pengurangan vektor, KL = L - K. Dengan titik acuan A, maka K = A - KA dan L = A - LA. Substitusi memberikan KL = (A - LA) - (A - KA) = KA - LA.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan aturan pengurangan vektor dan melakukan manipulasi aljabar untuk menyatakan vektor KL dalam bentuk vektor KA dan LA. Ini adalah penerapan prosedur rutin dalam geometri vektor.. Bukti: titik K adalah titik tengah dari AB dan titik L adalah titik tengah dari AC; Nyatakan KL dalam KA dan LA
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang hubungan antara titik-titik geometri dan representasi vektornya, serta bagaimana melakukan operasi pengurangan vektor.. Bukti: Nyatakan KL dalam KA dan LA
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman tentang vektor posisi dan manipulasi aljabar vektor yang merupakan standar kurikulum kelas 11 TL. Tidak memerlukan strategi nonrutin.. Bukti: titik K adalah titik tengah dari AB dan titik L adalah titik tengah dari AC; Nyatakan KL dalam KA dan LA

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar vektor posisi, pengurangan vektor, dan representasi titik dalam vektor. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini menguji kemampuan manipulasi vektor dasar yang sesuai dengan tuntutan kurikulum matematika tingkat lanjut kelas 11. |

Run 3 — solusi: Berdasarkan aturan penjumlahan vektor, KL = AL - AK. Karena KA = -AK dan LA = -AL, maka KL = (-LA) - (-KA) = KA - LA.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan aturan pengurangan vektor dan melakukan manipulasi aljabar untuk menyatakan vektor KL dalam basis KA dan LA.. Bukti: Nyatakan KL dalam KA dan LA
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang manipulasi aljabar vektor dan hubungan antar vektor posisi.. Bukti: Nyatakan KL dalam KA dan LA
- Intended difficulty `classify/Medium`: Memerlukan pemahaman tentang arah vektor dan manipulasi aljabar yang tepat, namun prosedurnya rutin.. Bukti: Nyatakan KL dalam KA dan LA

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar vektor, penjumlahan dan pengurangan vektor, vektor posisi. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini menguji pemahaman dasar vektor di kelas 11, namun memerlukan ketelitian dalam arah vektor agar tidak terbalik. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 1, "Medium": 2} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3333`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan aturan pengurangan vektor dan melakukan manipulasi aljabar untuk menyatakan vektor KL dalam basis KA dan LA. Ini adalah penerapan prosedur rutin dalam geometri vektor.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman konseptual tentang hubungan antara titik-titik geometri dan representasi vektornya, serta bagaimana melakukan operasi pengurangan vektor.
- Intended difficulty `Medium`: Soal memerlukan pemahaman tentang vektor posisi dan manipulasi aljabar vektor yang merupakan standar kurikulum kelas 11 TL. Tidak memerlukan strategi nonrutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar vektor posisi, pengurangan vektor, dan representasi titik dalam vektor. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini menguji kemampuan manipulasi vektor dasar yang sesuai dengan tuntutan kurikulum matematika tingkat lanjut kelas 11. Memerlukan ketelitian dalam arah vektor agar tidak terbalik. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
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
| 1 | success | valid / verified | applying | procedural | Easy | 2169 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2125 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2223 |

Run 1 — solusi: Diketahui K titik tengah AB, maka AB = 2AK = -2KA. L titik tengah AC, maka AC = 2AL = -2LA. Vektor BC = AC - AB = (-2LA) - (-2KA) = 2KA - 2LA = 2(KA - LA).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep vektor posisi dan hubungan titik tengah untuk menyatakan vektor BC sebagai selisih vektor AC dan AB, kemudian melakukan manipulasi aljabar vektor. Ini adalah penerapan prosedur rutin dalam konteks geometri.. Bukti: Nyatakan BC dalam KA dan LA; K adalah titik tengah dari AB dan titik L adalah titik tengah dari AC
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan antara titik tengah dan vektor, serta teknik manipulasi aljabar vektor (prosedural) berdasarkan prinsip geometri (konseptual).. Bukti: K adalah titik tengah dari AB; Nyatakan BC dalam KA dan LA
- Intended difficulty `classify/Easy`: Soal memerlukan pemahaman dasar vektor dan titik tengah. Langkah penyelesaiannya rutin dan langsung, tidak memerlukan strategi non-rutin.. Bukti: Nyatakan BC dalam KA dan LA; K adalah titik tengah dari AB dan titik L adalah titik tengah dari AC

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar vektor, penjumlahan/pengurangan vektor, dan definisi titik tengah. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi vektor di kelas 11 TL mencakup operasi vektor dan pembuktian geometris sederhana. Soal ini adalah latihan standar untuk memahami hubungan vektor posisi. |

Run 2 — solusi: Diketahui K titik tengah AB, maka AB = 2AK = -2KA. L titik tengah AC, maka AC = 2AL = -2LA. Vektor BC = AC - AB = (-2LA) - (-2KA) = 2KA - 2LA = 2(KA - LA).
- Domain kognitif `classify/applying`: Siswa perlu memahami hubungan vektor posisi titik tengah dan melakukan manipulasi aljabar vektor untuk menyatakan vektor BC sebagai selisih dua vektor yang diberikan.. Bukti: titik K adalah titik tengah dari AB dan titik L adalah titik tengah dari AC; Nyatakan BC dalam KA dan LA
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman konseptual tentang vektor posisi titik tengah dan prosedur aljabar vektor untuk menyusun ulang ekspresi.. Bukti: titik K adalah titik tengah dari AB; Nyatakan BC dalam KA dan LA
- Intended difficulty `classify/Easy`: Soal memerlukan pemahaman dasar vektor posisi dan operasi pengurangan vektor. Langkah-langkahnya rutin dan langsung.. Bukti: titik K adalah titik tengah dari AB; Nyatakan BC dalam KA dan LA

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dan pengurangan vektor, konsep titik tengah. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi vektor kelas 11 TL mencakup operasi vektor dasar. Soal ini adalah aplikasi langsung dari definisi titik tengah dan operasi vektor. |

Run 3 — solusi: Diketahui K titik tengah AB, maka AB = 2AK = -2KA. L titik tengah AC, maka AC = 2AL = -2LA. Vektor BC = AC - AB = (-2LA) - (-2KA) = 2KA - 2LA = 2(KA - LA).
- Domain kognitif `classify/applying`: Siswa perlu memahami hubungan vektor posisi titik tengah dan melakukan operasi pengurangan vektor untuk menyatakan vektor sisi segitiga, yang merupakan penerapan konsep vektor dalam geometri.. Bukti: titik K adalah titik tengah dari AB dan titik L adalah titik tengah dari AC; Nyatakan BC dalam KA dan LA
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan vektor posisi titik tengah dalam segitiga dan prosedur manipulasi aljabar vektor.. Bukti: titik K adalah titik tengah dari AB dan titik L adalah titik tengah dari AC
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman hubungan vektor posisi dan manipulasi aljabar vektor yang rutin bagi siswa kelas 11 TL.. Bukti: titik K adalah titik tengah dari AB dan titik L adalah titik tengah dari AC; Nyatakan BC dalam KA dan LA

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dan pengurangan vektor, konsep titik tengah. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi vektor kelas 11 TL mencakup operasi vektor dan pembuktian geometris sederhana. Soal ini adalah aplikasi standar dari konsep titik tengah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 2, "Medium": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3592`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan konsep vektor posisi dan hubungan titik tengah untuk menyatakan vektor BC sebagai selisih vektor AC dan AB, kemudian melakukan manipulasi aljabar vektor. Ini adalah penerapan prosedur rutin dalam konteks geometri.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang hubungan antara titik tengah dan vektor, serta teknik manipulasi aljabar vektor (prosedural) berdasarkan prinsip geometri (konseptual).
- Intended difficulty `Easy`: Soal memerlukan pemahaman dasar vektor dan titik tengah. Langkah penyelesaiannya rutin dan langsung, tidak memerlukan strategi non-rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar vektor, penjumlahan/pengurangan vektor, dan definisi titik tengah. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi vektor di kelas 11 TL mencakup operasi vektor dan pembuktian geometris sederhana. Soal ini adalah latihan standar untuk memahami hubungan vektor posisi. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 40. Soal `78652b4108bd747c96b2f4a8`

Pada $\triangle ABC$, $AD$ membagi $\angle A$ menjadi dua bagian yang sama besar. $AD$ disebut garis bagi. Titik $D$ terletak pada sisi $BC$. Petunjuk: Gambarkan garis yang sejajar dengan $AD$ dan melalui titik $C$. Garis ini berpotongan dengan perpanjangan $AB$ di titik $E$.<br><br>Beri alasan bahwa $\triangle ACE$ sama kaki. Tuliskan sisi-sisi yang sama panjang.

| Opsi | Isi |
|---|---|
| A | AC = CE, karena ∠CAE = ∠AEC |
| B | AC = AE, karena ∠ACE = ∠AEC |
| C | AB = AC, karena AD garis bagi |
| D | AE = CE, karena ∠ACE = ∠CAE |

![Gambar sumber soal 40](<../images/kelas7_crop-p0205-garis-bagi.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Misalkan AD sejajar CE. Sudut BAD = sudut AEC (sehadap). Sudut DAC = sudut ACE (berseberangan dalam). Karena AD garis bagi, sudut BAD = sudut DAC. Maka sudut AEC = sudut ACE. Segitiga ACE sama kaki dengan AC = AE.
Gambar sumber: images/kelas7_crop-p0205-garis-bagi.png. Transkripsi visual: Gambar menunjukkan segitiga ABC dengan titik D pada sisi BC. Garis AD membagi sudut A menjadi dua bagian yang sama besar (ditandai dengan busur hijau). Titik A, B, C, D terlihat jelas.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['menyebutkan', 'menjelaskan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `04e26f7f06514e4931aea0716a87c8f99e238c85806c19f1ce4179cc0a4a0de1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | reasoning | conceptual | Medium | 3267 |
| 2 | success | valid / verified | reasoning | conceptual | Medium | 3256 |
| 3 | success | valid / verified | reasoning | conceptual | Medium | 3309 |

Run 1 — solusi: Misalkan AD sejajar CE. Sudut BAD = sudut AEC (sehadap). Sudut DAC = sudut ACE (berseberangan dalam). Karena AD garis bagi, sudut BAD = sudut DAC. Maka sudut AEC = sudut ACE. Segitiga ACE sama kaki dengan AC = AE.
- Domain kognitif `classify/reasoning`: Soal meminta siswa untuk melakukan pembuktian geometris sederhana menggunakan sifat sudut pada garis sejajar dan segitiga sama kaki. Ini memerlukan integrasi informasi geometris dan pemahaman konsep dasar, bukan sekadar ingatan.. Bukti: Beri alasan bahwa ΔACE sama kaki.; Gambarkan garis yang sejajar dengan AD dan melalui titik C.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara sifat sudut (sehadap, berseberangan) dan sifat segitiga sama kaki untuk membangun argumen logis.. Bukti: Gambarkan garis yang sejajar dengan AD dan melalui titik C.; Beri alasan bahwa ΔACE sama kaki.
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemahaman konsep geometri yang lebih dalam daripada sekadar menghitung, namun prosedurnya cukup standar dalam pembuktian teorema garis bagi segitiga.. Bukti: Gambarkan garis yang sejajar dengan AD dan melalui titik C.; Beri alasan bahwa ΔACE sama kaki.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat sudut pada garis sejajar, definisi segitiga sama kaki, konsep garis bagi. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi ini sering diajarkan di SMP, pembuktian geometris formal seperti ini tetap relevan untuk menguji kemampuan penalaran siswa kelas 11 dalam konteks geometri lanjut. |

Run 2 — solusi: Misalkan CE sejajar AD. ∠BAD = ∠AEC (sehadap) dan ∠DAC = ∠ACE (berseberangan dalam). Karena ∠BAD = ∠DAC, maka ∠AEC = ∠ACE. Segitiga ACE sama kaki dengan AC = AE.
- Domain kognitif `classify/reasoning`: Siswa diminta untuk melakukan pembuktian geometris sederhana dengan bantuan konstruksi garis tambahan, yang memerlukan pemahaman konsep sudut pada garis sejajar dan sifat segitiga sama kaki.. Bukti: Gambarkan garis yang sejajar dengan AD dan melalui titik C; Beri alasan bahwa ΔACE sama kaki
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan sudut-sudut pada garis sejajar (sehadap, berseberangan) dan sifat segitiga sama kaki dalam konteks pembuktian teorema garis bagi.. Bukti: AD membagi ∠A menjadi dua bagian yang sama besar; Garis yang sejajar dengan AD dan melalui titik C
- Intended difficulty `classify/Medium`: Soal ini memerlukan konstruksi tambahan dan penalaran deduktif untuk menghubungkan sudut-sudut yang terbentuk oleh garis sejajar. Meskipun prosedurnya standar dalam pembuktian geometri, ini melampaui sekadar aplikasi rumus langsung.. Bukti: Gambarkan garis yang sejajar dengan AD dan melalui titik C; Beri alasan bahwa ΔACE sama kaki

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat sudut pada garis sejajar dan segitiga sama kaki. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi geometri dasar, pembuktian teorema garis bagi adalah topik yang menuntut penalaran logis di tingkat SMA, bukan sekadar komputasi. |

Run 3 — solusi: Misalkan AD sejajar CE. Sudut BAD = sudut AEC (sehadap). Sudut DAC = sudut ACE (berseberangan dalam). Karena sudut BAD = sudut DAC (AD garis bagi), maka sudut AEC = sudut ACE. Segitiga ACE sama kaki dengan AC = AE.
- Domain kognitif `classify/reasoning`: Soal meminta siswa untuk melakukan pembuktian geometris sederhana dengan menggunakan konstruksi tambahan (garis sejajar) dan sifat-sifat sudut pada garis sejajar (sehadap dan berseberangan). Ini memerlukan penalaran logis untuk menghubungkan konstruksi dengan sifat segitiga sama kaki.. Bukti: Beri alasan bahwa ΔACE sama kaki.; Gambarkan garis yang sejajar dengan AD dan melalui titik C.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami prinsip-prinsip geometri (sudut sehadap, berseberangan, sifat segitiga sama kaki) dan mengintegrasikannya dalam sebuah pembuktian.. Bukti: Gambarkan garis yang sejajar dengan AD dan melalui titik C.; Beri alasan bahwa ΔACE sama kaki.
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk melakukan konstruksi tambahan dan menerapkan teorema sudut pada garis sejajar untuk membuktikan sifat segitiga. Meskipun prosedurnya standar dalam pembuktian teorema garis bagi, ini melampaui sekadar ingatan atau aplikasi rumus langsung.. Bukti: Gambarkan garis yang sejajar dengan AD dan melalui titik C.; Beri alasan bahwa ΔACE sama kaki.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Sifat sudut pada garis sejajar (sehadap, berseberangan) dan definisi segitiga sama kaki. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | partial |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini merupakan bagian dari pembuktian teorema garis bagi yang sering muncul dalam geometri SMA. Tingkat kesulitan Medium karena memerlukan konstruksi tambahan dan penalaran deduktif, bukan sekadar komputasi. |

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
Kelas: 11
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
Transkripsi visual: Gambar menunjukkan segitiga ABC dengan titik D pada sisi BC. Garis AD membagi sudut A menjadi dua bagian yang sama besar (ditandai dengan busur hijau). Titik A, B, C, D terlihat jelas.
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
Solusi minimum hasil AI: Luas ΔABC = 0.5 * 8 * 15 = 60 cm². Dilatasi dengan faktor skala k=3 mengubah luas dengan faktor k² = 3² = 9. Luas ΔA'B'C' = 9 * 60 = 540 cm².
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6be483d86a1fd94d4fe43f6ed665fa9ca02bbe883e3aba19ee1324328c9c4610`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2105 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2133 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2099 |

Run 1 — solusi: Luas ΔABC = 0.5 * 8 * 15 = 60 cm². Dilatasi dengan faktor skala k=3 mengubah luas dengan faktor k² = 3² = 9. Luas ΔA'B'C' = 9 * 60 = 540 cm².
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep hubungan antara faktor skala dilatasi dan perubahan luas bangun datar (k²), bukan sekadar menghitung luas awal.. Bukti: Jika ΔA'B'C' merupakan hasil dilatasi dari ΔABC dengan faktor skala 3, maka luas ΔA'B'C' adalah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman prinsip geometris tentang bagaimana transformasi (dilatasi) mempengaruhi properti luas bangun datar.. Bukti: dilatasi dari ΔABC dengan faktor skala 3
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan pemahaman konsep bahwa luas berubah sebesar kuadrat faktor skala, bukan sekadar mengalikan dengan faktor skala itu sendiri. Ini adalah langkah rutin dalam transformasi geometri namun memerlukan pemilihan prosedur yang tepat.. Bukti: luas ΔA'B'C' adalah; faktor skala 3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep luas segitiga dan sifat transformasi dilatasi pada luas bangun datar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi dilatasi adalah bagian dari kurikulum transformasi geometri kelas 11. Soal ini menguji pemahaman konseptual tentang properti luas di bawah dilatasi. |

Run 2 — solusi: Luas segitiga ABC = 0,5 * 8 * 15 = 60 cm². Dilatasi dengan faktor skala k=3 mengubah luas dengan faktor k²=9. Luas A'B'C' = 9 * 60 = 540 cm².
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prinsip dilatasi pada luas bangun datar (k²), bukan sekadar panjang sisi (k). Ini adalah penerapan prosedur rutin dalam konteks transformasi geometri.. Bukti: Jika ΔA'B'C' merupakan hasil dilatasi dari ΔABC dengan faktor skala 3, maka luas ΔA'B'C' adalah
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang bagaimana faktor skala dilatasi mempengaruhi luas bangun datar (hubungan kuadratik).. Bukti: dilatasi dari ΔABC dengan faktor skala 3
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa sering terjebak menggunakan faktor skala k=3 secara linear pada luas, padahal harus menggunakan k²=9. Memerlukan pemahaman konsep transformasi yang tepat.. Bukti: dilatasi dari ΔABC dengan faktor skala 3; luas ΔA'B'C' adalah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep luas segitiga dan sifat dilatasi pada luas bangun datar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi dilatasi adalah bagian dari kurikulum kelas 11. Soal ini menguji pemahaman mendalam tentang properti dilatasi yang sering disalahpahami. |

Run 3 — solusi: Luas ΔABC = 0.5 * 8 * 15 = 60 cm². Dilatasi dengan faktor skala k=3 mengubah luas dengan faktor k² = 3² = 9. Luas ΔA'B'C' = 9 * 60 = 540 cm².
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep hubungan antara faktor skala dilatasi dan perubahan luas bangun datar (k²), bukan sekadar menghitung luas awal.. Bukti: Jika ΔA'B'C' merupakan hasil dilatasi dari ΔABC dengan faktor skala 3, maka luas ΔA'B'C' adalah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman prinsip geometris tentang bagaimana transformasi dilatasi mempengaruhi luas bangun datar.. Bukti: dilatasi dari ΔABC dengan faktor skala 3
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus memahami prinsip bahwa luas berubah sebesar kuadrat faktor skala, bukan sekadar mengalikan dengan faktor skala itu sendiri. Ini adalah langkah rutin dalam geometri transformasi namun memerlukan pemahaman konseptual yang tepat.. Bukti: luas ΔA'B'C' adalah; faktor skala 3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep luas segitiga dan sifat dilatasi pada luas bangun datar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Materi dilatasi adalah bagian dari kurikulum geometri transformasi kelas 11. Soal ini menguji pemahaman konseptual dasar tentang properti dilatasi. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
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
Solusi minimum hasil AI: Rotasi 180° terhadap (0,0) memetakan (x,y) ke (-x,-y). Maka x = -x' dan y = -y'. Substitusi ke 3x - 2y + 5 = 0 menghasilkan 3(-x') - 2(-y') + 5 = 0, atau -3x' + 2y' + 5 = 0.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `306c3e36b81bcf3c3a2d436e125796bb0bfccb465f1936fcd5ea98edf3249315`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2148 |
| 2 | success | valid / verified | applying | procedural | Easy | 2153 |
| 3 | success | valid / verified | applying | procedural | Easy | 2170 |

Run 1 — solusi: Rotasi 180° terhadap (0,0) memetakan (x,y) ke (-x,-y). Maka x = -x' dan y = -y'. Substitusi ke 3x - 2y + 5 = 0 menghasilkan 3(-x') - 2(-y') + 5 = 0, atau -3x' + 2y' + 5 = 0.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur transformasi geometri (rotasi) pada persamaan garis. Ini adalah penerapan rutin dari konsep transformasi titik ke persamaan.. Bukti: Garis 3x - 2y + 5 = 0 yang ditransformasi oleh rotasi 180° terhadap titik asal (0, 0).
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma transformasi geometri (rotasi) dan bagaimana menerapkannya pada persamaan linear.. Bukti: Garis 3x - 2y + 5 = 0 yang ditransformasi oleh rotasi 180° terhadap titik asal (0, 0).
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 11. Prosedur substitusi variabel setelah transformasi rotasi adalah standar dan tidak memerlukan strategi non-rutin.. Bukti: Garis 3x - 2y + 5 = 0 yang ditransformasi oleh rotasi 180° terhadap titik asal (0, 0).

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang koordinat kartesius dan persamaan garis lurus. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Rotasi 180 derajat adalah transformasi dasar yang dipelajari di tingkat menengah, sehingga untuk kelas 11 TL ini dikategorikan mudah. |

Run 2 — solusi: Rotasi 180° terhadap (0,0) memetakan (x, y) ke (-x', -y'). Substitusi x = -x' dan y = -y' ke persamaan 3x - 2y + 5 = 0 menghasilkan 3(-x') - 2(-y') + 5 = 0, atau -3x' + 2y' + 5 = 0.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur transformasi geometri (rotasi) pada persamaan garis. Ini adalah penerapan rutin dari konsep transformasi yang sudah dipelajari.. Bukti: Garis 3x - 2y + 5 = 0 yang ditransformasi oleh rotasi 180° terhadap titik asal (0, 0).
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma transformasi geometri (prosedural) dan bagaimana transformasi tersebut mengubah persamaan garis (konseptual).. Bukti: Garis 3x - 2y + 5 = 0 yang ditransformasi oleh rotasi 180° terhadap titik asal (0, 0).
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena rotasi 180 derajat memiliki aturan transformasi yang standar dan langsung. Tidak ada langkah non-rutin atau integrasi konsep yang kompleks.. Bukti: Garis 3x - 2y + 5 = 0 yang ditransformasi oleh rotasi 180° terhadap titik asal (0, 0).

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang transformasi geometri (rotasi) dan substitusi variabel pada persamaan linear. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi transformasi geometri adalah standar kelas 11. Soal ini menguji prosedur dasar tanpa kerumitan tambahan. |

Run 3 — solusi: Rotasi 180° terhadap (0,0) memetakan (x,y) ke (-x', -y'). Substitusi x = -x' dan y = -y' ke persamaan 3x - 2y + 5 = 0 menghasilkan 3(-x') - 2(-y') + 5 = 0, yang disederhanakan menjadi -3x' + 2y' + 5 = 0.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan aturan transformasi rotasi 180 derajat dan melakukan substitusi variabel ke dalam persamaan garis. Ini adalah prosedur rutin yang melibatkan penerapan konsep transformasi geometri.. Bukti: Garis 3x - 2y + 5 = 0 yang ditransformasi oleh rotasi 180° terhadap titik asal (0, 0).
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma transformasi geometri (rotasi) dan teknik substitusi aljabar untuk menentukan persamaan bayangan.. Bukti: Garis 3x - 2y + 5 = 0 yang ditransformasi oleh rotasi 180° terhadap titik asal (0, 0).
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 11. Prosedur rotasi 180 derajat adalah standar, dan langkah substitusinya langsung tanpa memerlukan strategi non-rutin atau integrasi konsep yang kompleks.. Bukti: Garis 3x - 2y + 5 = 0 yang ditransformasi oleh rotasi 180° terhadap titik asal (0, 0).

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang rotasi titik dan substitusi variabel dalam persamaan linear. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Rotasi 180 derajat adalah materi dasar transformasi geometri yang sudah dipelajari dan sering dilatih di kelas 11. |

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
Solusi minimum hasil AI: Translasi titik (x, y) oleh vektor (a, b) menghasilkan (x+a, y+b). Untuk A(1, 2), B(3, -1), C(-2, -3) dengan vektor (-5, 3): A'(1-5, 2+3) = (-4, 5); B'(3-5, -1+3) = (-2, 2); C'(-2-5, -3+3) = (-7, 0). Hasil sesuai dengan opsi D.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d96037d8062e10e381cf016cb3d745fe40c98bbe65ccb3925973036753e22afe`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2212 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2212 |
| 3 | success | valid / verified | applying | procedural | Easy | 2205 |

Run 1 — solusi: Translasi titik (x, y) oleh vektor (a, b) menghasilkan (x+a, y+b). Untuk A(1, 2), B(3, -1), C(-2, -3) dengan vektor (-5, 3): A'(1-5, 2+3) = (-4, 5); B'(3-5, -1+3) = (-2, 2); C'(-2-5, -3+3) = (-7, 0). Hasil sesuai dengan opsi D.
- Domain kognitif `classify/applying`: Siswa hanya perlu menerapkan definisi translasi titik (x, y) + (a, b) = (x+a, y+b) secara langsung pada koordinat yang diberikan.. Bukti: Segitiga ABC dengan A(1, 2), B(3, –1), dan C(–2, –3) yang ditranslasikan oleh vektor (–5, 3)
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang operasi penjumlahan vektor pada koordinat titik.. Bukti: ditranslasikan oleh vektor
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar satu langkah yang familiar bagi siswa kelas 11. Tidak ada kompleksitas tambahan.. Bukti: Segitiga ABC dengan A(1, 2), B(3, –1), dan C(–2, –3) yang ditranslasikan oleh vektor (–5, 3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan bulat dan konsep dasar translasi titik. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Translasi adalah materi dasar transformasi geometri yang sudah dipelajari sejak SMP dan diulang di kelas 11. Soal ini bersifat rutin. |

Run 2 — solusi: Translasi titik (x, y) oleh vektor (a, b) menghasilkan (x+a, y+b). Untuk A(1, 2), B(3, -1), C(-2, -3) dengan vektor (-5, 3): A'(1-5, 2+3) = A'(-4, 5); B'(3-5, -1+3) = B'(-2, 2); C'(-2-5, -3+3) = C'(-7, 0). Hasil sesuai dengan opsi D.
- Domain kognitif `classify/knowing`: Siswa hanya perlu menerapkan definisi translasi titik (x, y) + (a, b) = (x+a, y+b) secara langsung pada koordinat yang diberikan.. Bukti: Segitiga ABC dengan A(1, 2), B(3, –1), dan C(–2, –3) yang ditranslasikan oleh vektor (–5, 3)
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural dasar mengenai operasi translasi pada bidang Kartesius.. Bukti: ditranslasikan oleh vektor
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar satu langkah yang familiar bagi siswa kelas 11, dengan beban komputasi yang sangat rendah.. Bukti: Segitiga ABC dengan A(1, 2), B(3, –1), dan C(–2, –3) yang ditranslasikan oleh vektor (–5, 3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar koordinat Kartesius dan operasi penjumlahan bilangan bulat. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Translasi adalah materi dasar transformasi geometri yang sudah diperkenalkan sejak SMP dan diulang di kelas 11 dengan tingkat kompleksitas yang sama. |

Run 3 — solusi: Translasi titik (x, y) oleh vektor (a, b) menghasilkan (x+a, y+b). Untuk A(1, 2): (1-5, 2+3) = (-4, 5). Untuk B(3, -1): (3-5, -1+3) = (-2, 2). Untuk C(-2, -3): (-2-5, -3+3) = (-7, 0). Hasilnya adalah A'(-4, 5), B'(-2, 2), C'(-7, 0).
- Domain kognitif `classify/applying`: Soal meminta penerapan langsung definisi translasi pada titik-titik koordinat. Siswa hanya perlu melakukan operasi penjumlahan vektor sederhana pada setiap titik.. Bukti: Segitiga ABC dengan A(1, 2), B(3, –1), dan C(–2, –3) yang ditranslasikan oleh vektor (–5, 3)
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami konsep translasi sebagai penambahan vektor pada koordinat titik (konsep prosedural).. Bukti: ditranslasikan oleh vektor (-5, 3)
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, hanya memerlukan satu operasi penjumlahan sederhana untuk setiap titik tanpa ada kendala atau langkah tambahan.. Bukti: Segitiga ABC dengan A(1, 2), B(3, –1), dan C(–2, –3) yang ditranslasikan oleh vektor (-5, 3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan bulat dan konsep koordinat kartesius. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi transformasi diajarkan di kelas 11, soal ini merupakan prosedur dasar yang sangat familiar dan tidak menuntut pemahaman mendalam tentang matriks transformasi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3869`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan prosedur standar translasi titik (x, y) + (a, b) = (x+a, y+b) secara langsung pada koordinat yang diberikan.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman prosedural tentang operasi penjumlahan vektor pada koordinat titik.
- Intended difficulty `Easy`: Soal ini merupakan prosedur standar satu langkah yang familiar bagi siswa kelas 11. Tidak ada kompleksitas tambahan atau kendala yang perlu diintegrasikan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan bulat dan konsep dasar translasi titik. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Translasi adalah materi dasar transformasi geometri yang sudah dipelajari sejak SMP dan diulang di kelas 11. Soal ini bersifat rutin dan langsung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: Matriks transformasi adalah dilatasi dengan faktor skala k=3, sehingga (x', y') = (3x, 3y) atau x = x'/3 dan y = y'/3. Substitusi ke persamaan garis: (x'/3) - 2(y'/3) + 3 = 0. Kalikan kedua ruas dengan 3: x' - 2y' + 9 = 0.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `72cf89b3c1866fc7d0e7095ae2900be09f482725b61470c5f7066e7cf39ae343`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2153 |
| 2 | success | valid / verified | applying | procedural | Easy | 2225 |
| 3 | success | valid / verified | applying | procedural | Easy | 2206 |

Run 1 — solusi: Matriks transformasi adalah dilatasi dengan faktor skala k=3, sehingga (x', y') = (3x, 3y) atau x = x'/3 dan y = y'/3. Substitusi ke persamaan garis: (x'/3) - 2(y'/3) + 3 = 0. Kalikan kedua ruas dengan 3: x' - 2y' + 9 = 0.
- Domain kognitif `classify/applying`: Siswa perlu memahami hubungan antara matriks transformasi (dilatasi) dan substitusi variabel pada persamaan garis. Ini adalah prosedur standar dalam transformasi geometri.. Bukti: Garis x - 2y + 3 = 0 yang ditransformasikan oleh [3 0; 0 3]
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana menerapkan matriks transformasi pada persamaan linear.. Bukti: ditransformasikan oleh [3 0; 0 3]
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 11 yang mempelajari transformasi geometri dengan matriks. Prosedur substitusi invers matriks adalah standar.. Bukti: Garis x - 2y + 3 = 0 yang ditransformasikan oleh [3 0; 0 3]

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang dilatasi, matriks transformasi, dan substitusi variabel pada persamaan garis. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi transformasi geometri dengan matriks adalah kurikulum standar kelas 11 TL. Soal ini menguji kemampuan dasar tanpa kompleksitas tambahan. |

Run 2 — solusi: Transformasi matriks [3 0; 0 3] adalah dilatasi dengan faktor skala k=3, sehingga x' = 3x dan y' = 3y. Maka x = x'/3 dan y = y'/3. Substitusi ke persamaan garis x - 2y + 3 = 0 menghasilkan (x'/3) - 2(y'/3) + 3 = 0. Kalikan kedua ruas dengan 3 diperoleh x' - 2y' + 9 = 0.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep transformasi geometri menggunakan matriks (dilatasi) untuk menentukan persamaan bayangan garis. Ini melibatkan pemilihan prosedur substitusi variabel yang tepat, yang merupakan proses applying.. Bukti: Garis x - 2y + 3 = 0 yang ditransformasikan oleh [3 0; 0 3]
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana matriks transformasi memetakan titik-titik pada garis dan bagaimana melakukan substitusi balik untuk mendapatkan persamaan bayangan.. Bukti: Garis x - 2y + 3 = 0 yang ditransformasikan oleh [3 0; 0 3]
- Intended difficulty `classify/Easy`: Soal ini adalah prosedur rutin dalam transformasi geometri. Siswa hanya perlu memahami hubungan antara matriks dilatasi dan substitusi variabel. Tidak ada strategi non-rutin atau integrasi konsep yang kompleks.. Bukti: Garis x - 2y + 3 = 0 yang ditransformasikan oleh [3 0; 0 3]

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang matriks transformasi dasar (dilatasi) dan substitusi aljabar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah materi standar kelas 11 Matematika Tingkat Lanjut mengenai transformasi geometri dengan matriks. Prosedurnya langsung dan familiar bagi siswa. |

Run 3 — solusi: Transformasi matriks [3 0; 0 3] adalah dilatasi dengan faktor skala k=3, sehingga x' = 3x dan y' = 3y, atau x = x'/3 dan y = y'/3. Substitusi ke persamaan garis x - 2y + 3 = 0 menghasilkan (x'/3) - 2(y'/3) + 3 = 0. Kalikan kedua ruas dengan 3 diperoleh x' - 2y' + 9 = 0.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep transformasi geometri menggunakan matriks (dilatasi) pada persamaan garis, yang melibatkan substitusi variabel dan manipulasi aljabar rutin.. Bukti: Garis x - 2y + 3 = 0 yang ditransformasikan oleh [3 0; 0 3]; Tentukan peta dari beberapa operasi transformasi berikut
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana matriks transformasi mengubah koordinat titik pada persamaan garis.. Bukti: Garis x - 2y + 3 = 0 yang ditransformasikan oleh [3 0; 0 3]
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar dalam transformasi geometri kelas 11. Siswa hanya perlu melakukan substitusi invers matriks ke dalam persamaan garis.. Bukti: Garis x - 2y + 3 = 0 yang ditransformasikan oleh [3 0; 0 3]

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman tentang dilatasi dengan pusat (0,0) dan substitusi variabel pada persamaan linear. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi transformasi matriks adalah kurikulum standar kelas 11 TL. Soal ini bersifat rutin dan tidak memerlukan strategi kompleks. |

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
Solusi minimum hasil AI: Perkalian matriks transformasi dengan titik (3, 7) adalah: [[0, -1], [1, 0]] * [[3], [7]] = [[0*3 + (-1)*7], [1*3 + 0*7]] = [[-7], [3]]. Hasilnya adalah (-7, 3).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d1c425636aa609da7255f8484ea19eb4fbda2cf1dbf6f8a848b02abae3ceb45a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2141 |
| 2 | success | valid / verified | applying | procedural | Easy | 2115 |
| 3 | success | valid / verified | applying | procedural | Easy | 2125 |

Run 1 — solusi: Perkalian matriks transformasi dengan titik (3, 7) adalah: [[0, -1], [1, 0]] * [[3], [7]] = [[0*3 + (-1)*7], [1*3 + 0*7]] = [[-7], [3]]. Hasilnya adalah (-7, 3).
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan prosedur perkalian matriks standar untuk transformasi geometri. Ini adalah penerapan langsung dari definisi transformasi matriks yang sudah dipelajari di kelas 11.. Bukti: Titik (3, 7) yang ditransformasikan dengan matriks [[0, -1], [1, 0]]
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami algoritma perkalian matriks (prosedural) dan konsep transformasi geometri menggunakan matriks (konseptual).. Bukti: matriks [[0, -1], [1, 0]]
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu melakukan satu operasi perkalian matriks 2x2 dengan vektor kolom 2x1 tanpa ada langkah tambahan atau kendala yang kompleks.. Bukti: Titik (3, 7) yang ditransformasikan dengan matriks [[0, -1], [1, 0]]

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
| gradeRelativeRationale | Ini adalah soal dasar transformasi matriks yang sesuai untuk kelas 11, tidak memerlukan strategi non-rutin. |

Run 2 — solusi: Perkalian matriks transformasi dengan titik (3, 7) adalah: [0 -1; 1 0] * [3; 7] = [0*3 + (-1)*7; 1*3 + 0*7] = [-7; 3]. Hasilnya adalah titik (-7, 3).
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan prosedur perkalian matriks standar untuk transformasi geometri. Siswa hanya perlu melakukan operasi perkalian matriks-vektor yang rutin dan familiar di kelas 11.. Bukti: Titik (3, 7) yang ditransformasikan dengan matriks [0 -1; 1 0]
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman prosedural tentang bagaimana matriks transformasi bekerja pada koordinat titik.. Bukti: matriks [0 -1; 1 0]
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (prosedural) dengan beban komputasi yang rendah dan tidak memerlukan strategi non-rutin.. Bukti: Titik (3, 7) yang ditransformasikan dengan matriks [0 -1; 1 0]

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian matriks 2x2 dengan vektor kolom. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah soal dasar transformasi matriks yang merupakan standar kurikulum kelas 11 Matematika Tingkat Lanjut. |

Run 3 — solusi: Perkalian matriks transformasi dengan titik (3, 7) adalah: [0 -1; 1 0] * [3; 7] = [0*3 + (-1)*7; 1*3 + 0*7] = [-7; 3]. Jadi, peta titik tersebut adalah (-7, 3).
- Domain kognitif `classify/applying`: Soal meminta penerapan langsung prosedur perkalian matriks untuk transformasi titik. Siswa hanya perlu melakukan operasi perkalian matriks-vektor standar yang merupakan prosedur rutin.. Bukti: Titik (3, 7) yang ditransformasikan dengan matriks [0 -1; 1 0]
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma perkalian matriks untuk transformasi geometri, yang merupakan pengetahuan prosedural.. Bukti: ditransformasikan dengan matriks [0 -1; 1 0]
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (satu langkah perkalian matriks) dengan beban komputasi rendah dan prosedur yang sangat familiar bagi siswa kelas 11.. Bukti: Titik (3, 7) yang ditransformasikan dengan matriks [0 -1; 1 0]

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
| gradeRelativeRationale | Soal ini merupakan aplikasi dasar dari materi transformasi geometri dengan matriks yang dipelajari di kelas 11, tidak memerlukan langkah kompleks. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: Matriks pencerminan terhadap sumbu-y adalah M1 = [[-1, 0], [0, 1]]. Matriks rotasi 180 derajat terhadap pusat (0,0) adalah M2 = [[-1, 0], [0, -1]]. Komposisi transformasi (pencerminan dilanjutkan rotasi) adalah M2 * M1 = [[-1, 0], [0, -1]] * [[-1, 0], [0, 1]] = [[1, 0], [0, -1]].
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `709b387307a36104cf9559d3b7295eccfcd94c1c2d3e8197307b66edb8dd9820`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2186 |
| 2 | success | valid / verified | applying | procedural | Easy | 2176 |
| 3 | success | valid / verified | applying | procedural | Easy | 2168 |

Run 1 — solusi: Matriks pencerminan terhadap sumbu-y adalah M1 = [[-1, 0], [0, 1]]. Matriks rotasi 180 derajat terhadap pusat (0,0) adalah M2 = [[-1, 0], [0, -1]]. Komposisi transformasi (pencerminan dilanjutkan rotasi) adalah M2 * M1 = [[-1, 0], [0, -1]] * [[-1, 0], [0, 1]] = [[1, 0], [0, -1]].
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur perkalian matriks untuk komposisi transformasi geometri yang sudah dipelajari di kelas 11.. Bukti: Carilah matriks yang berkaitan dengan pencerminan terhadap sumbu-y dilanjutkan dengan rotasi 180°
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana merepresentasikan transformasi geometri dalam bentuk matriks dan mengoperasikannya.. Bukti: pencerminan terhadap sumbu-y; rotasi 180° terhadap titik pusat
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 11 yang telah mempelajari transformasi geometri. Siswa hanya perlu mengingat matriks standar dan melakukan perkalian matriks 2x2.. Bukti: pencerminan terhadap sumbu-y dilanjutkan dengan rotasi 180°

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman matriks transformasi dasar (refleksi dan rotasi). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi transformasi geometri dengan matriks adalah kurikulum standar kelas 11 TL. Prosedur perkalian matriks untuk komposisi adalah latihan rutin. |

Run 2 — solusi: Matriks refleksi terhadap sumbu-y adalah M1 = [[-1, 0], [0, 1]]. Matriks rotasi 180 derajat terhadap pusat (0,0) adalah M2 = [[-1, 0], [0, -1]]. Komposisi transformasi (M2 * M1) = [[-1, 0], [0, -1]] * [[-1, 0], [0, 1]] = [[1, 0], [0, -1]].
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur perkalian matriks untuk komposisi transformasi geometri yang sudah dipelajari. Ini adalah penerapan rutin dari konsep transformasi matriks.. Bukti: Carilah matriks yang berkaitan dengan pencerminan terhadap sumbu-y dilanjutkan dengan rotasi 180° terhadap titik pusat.
- Dimensi pengetahuan `classify/procedural`: Siswa harus memahami hubungan antara transformasi geometri dan representasi matriksnya, serta urutan operasi komposisi.. Bukti: pencerminan terhadap sumbu-y; rotasi 180° terhadap titik pusat
- Intended difficulty `classify/Easy`: Soal ini melibatkan dua langkah transformasi rutin yang harus dikomposisikan dengan urutan yang benar. Beban kognitif rendah karena matriks transformasi dasar sudah standar.. Bukti: pencerminan terhadap sumbu-y dilanjutkan dengan rotasi 180°

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
| gradeRelativeRationale | Materi transformasi geometri dengan matriks adalah standar kelas 11 TL. Soal ini menguji pemahaman prosedur dasar tanpa kompleksitas tambahan. |

Run 3 — solusi: Matriks pencerminan terhadap sumbu-y adalah M1 = [[-1, 0], [0, 1]]. Matriks rotasi 180 derajat terhadap pusat (0,0) adalah M2 = [[-1, 0], [0, -1]]. Komposisi transformasi (M2 * M1) = [[-1, 0], [0, -1]] * [[-1, 0], [0, 1]] = [[1, 0], [0, -1]].
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur perkalian matriks untuk komposisi transformasi geometri yang sudah dipelajari, yang merupakan tugas rutin dalam kurikulum kelas 11.. Bukti: pencerminan terhadap sumbu-y dilanjutkan dengan rotasi 180°
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana matriks transformasi dikalikan untuk mendapatkan matriks komposisi.. Bukti: matriks yang berkaitan dengan pencerminan; rotasi 180° terhadap titik pusat
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena hanya melibatkan perkalian dua matriks standar yang sudah dipelajari di kelas 11.. Bukti: pencerminan terhadap sumbu-y dilanjutkan dengan rotasi 180°

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman matriks transformasi dasar (refleksi dan rotasi). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi transformasi geometri dengan matriks adalah standar kelas 11, dan soal ini menggunakan prosedur standar tanpa modifikasi kompleks. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: T1(a,b) = (a,-b). T2(a,-b) = (-a,-b). Komposisi T2 o T1 memetakan (a,b) ke (-a,-b), yang ekuivalen dengan rotasi 180 derajat terhadap titik asal (0,0).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `01fc8fac6fb0e28dc9ba2b9bb462b823fae3aad8b1cbb9c4a7065c15c2ddcf78`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 3141 |
| 2 | success | valid / verified | applying | procedural | Medium | 3014 |
| 3 | success | valid / verified | applying | procedural | Easy | 2793 |

Run 1 — solusi: T1(a,b) = (a,-b). T2(a,-b) = (-a,-b). Matriks komposisi: [[-1,0],[0,1]][[1,0],[0,-1]] = [[-1,0],[0,-1]]. Ini adalah rotasi 180 derajat terhadap titik asal.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan dua transformasi berurutan dan mengidentifikasi transformasi tunggal yang setara, yang merupakan prosedur standar dalam transformasi geometri.. Bukti: T1 menyatakan operasi pencerminan terhadap sumbu-x; T2 menyatakan operasi pencerminan terhadap sumbu-y; Transformasi tunggal apakah yang ekuivalen dengan T2 ◦ T1?
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman konseptual tentang sifat matriks transformasi dan komposisi fungsi.. Bukti: T1 menyatakan operasi pencerminan terhadap sumbu-x; T2 menyatakan operasi pencerminan terhadap sumbu-y
- Intended difficulty `classify/Medium`: Soal ini melibatkan dua langkah transformasi rutin yang saling terkait. Siswa harus memahami urutan komposisi dan representasi matriks atau koordinat.. Bukti: Transformasi tunggal apakah yang ekuivalen dengan T2 ◦ T1?; Apa peta dari P(a, b) dari transformasi tersebut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar matriks transformasi dan koordinat kartesius. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 11 TL karena melibatkan komposisi transformasi yang merupakan materi standar, namun memerlukan ketelitian dalam urutan operasi. |

Run 2 — solusi: T1(a,b) = (a,-b). T2(a,-b) = (-a,-b). Komposisi T2 o T1 memetakan (a,b) ke (-a,-b), yang ekuivalen dengan rotasi 180 derajat terhadap titik asal.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur komposisi transformasi secara berurutan (T1 lalu T2) untuk menentukan hasil akhir. Ini adalah penerapan konsep transformasi geometri rutin.. Bukti: T1 menyatakan operasi pencerminan terhadap sumbu-x; T2 menyatakan operasi pencerminan terhadap sumbu-y; Transformasi tunggal apakah yang ekuivalen dengan T2 ◦ T1?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman algoritma komposisi transformasi (matriks atau koordinat) untuk mencapai hasil.. Bukti: T1 menyatakan operasi pencerminan terhadap sumbu-x; T2 menyatakan operasi pencerminan terhadap sumbu-y; Transformasi tunggal apakah yang ekuivalen dengan T2 ◦ T1?
- Intended difficulty `classify/Medium`: Memerlukan dua langkah rutin (penerapan T1, lalu T2) dan pemahaman tentang urutan komposisi transformasi.. Bukti: Transformasi tunggal apakah yang ekuivalen dengan T2 ◦ T1?; Apa peta dari P(a, b) dari transformasi tersebut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar transformasi geometri (refleksi) dan komposisi fungsi. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan mampu melakukan komposisi transformasi sederhana. Soal ini rutin namun memerlukan ketelitian pada urutan operasi. |

Run 3 — solusi: T1(a, b) = (a, -b). T2(a, -b) = (-a, -b). Komposisi T2 o T1 adalah pencerminan terhadap titik asal (0,0) yang memetakan (a, b) ke (-a, -b).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan definisi transformasi pencerminan secara berurutan untuk mendapatkan hasil komposisi.. Bukti: T1 menyatakan operasi pencerminan terhadap sumbu-x dan T2 menyatakan operasi pencerminan terhadap sumbu-y; Transformasi tunggal apakah yang ekuivalen dengan T2 ◦ T1?
- Dimensi pengetahuan `classify/procedural`: Melibatkan prosedur standar komposisi transformasi menggunakan aturan koordinat atau perkalian matriks.. Bukti: T1 menyatakan operasi pencerminan terhadap sumbu-x dan T2 menyatakan operasi pencerminan terhadap sumbu-y
- Intended difficulty `classify/Easy`: Soal ini merupakan aplikasi langsung dari definisi transformasi dasar yang rutin dipelajari di kelas 11.. Bukti: T1 menyatakan operasi pencerminan terhadap sumbu-x dan T2 menyatakan operasi pencerminan terhadap sumbu-y; Transformasi tunggal apakah yang ekuivalen dengan T2 ◦ T1?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi matriks pencerminan terhadap sumbu-x dan sumbu-y. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi transformasi geometri dengan matriks adalah standar kelas 11 TL. Soal ini adalah aplikasi langsung dari definisi dasar tanpa modifikasi kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3685`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur komposisi transformasi secara berurutan (T1 lalu T2) untuk menentukan hasil akhir. Ini adalah penerapan konsep transformasi geometri rutin.
- Dimensi pengetahuan `procedural`: Soal menuntut pemahaman algoritma komposisi transformasi (matriks atau koordinat) untuk mencapai hasil.
- Intended difficulty `Medium`: Memerlukan dua langkah rutin (penerapan T1, lalu T2) dan pemahaman tentang urutan komposisi transformasi. Soal ini rutin namun memerlukan ketelitian pada urutan operasi.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar transformasi geometri (refleksi) dan komposisi fungsi. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 11 TL diharapkan mampu melakukan komposisi transformasi sederhana. Soal ini rutin namun memerlukan ketelitian pada urutan operasi. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
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
Solusi minimum hasil AI: Konversi ketinggian: h = 4,884 km. Substitusi ke rumus: ln(P/100) = -4,884/7 = -0,6977. Menggunakan invers logaritma natural (eksponensial): P/100 = e^(-0,6977) ≈ 0,4977. Maka P = 100 * 0,4977 = 49,77 kPa.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['membandingkan', 'menganalisis']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f3555349c05bfdf63395cd886b09681f6370cc0f0f369425fd90940ae60a48f8`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2899 |
| 2 | success | valid / verified | applying | procedural | Medium | 2867 |
| 3 | success | valid / verified | applying | procedural | Medium | 2803 |

Run 1 — solusi: Diketahui ln(P/100) = -h/7 dengan h = 4,884 km. Maka ln(P/100) = -4,884/7 = -0,6977. Menggunakan invers logaritma natural (eksponen), P/100 = e^(-0,6977) ≈ 0,4977. Sehingga P = 100 * 0,4977 = 49,77 kPa.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan rumus yang diberikan untuk memprediksi nilai variabel P. Ini melibatkan pemilihan prosedur yang tepat (mengubah bentuk logaritma ke eksponen) untuk menyelesaikan masalah kontekstual.. Bukti: Hubungan antara tekanan udara P (dalam kPa) dan ketinggian h (dalam km) dapat dimodelkan sebagai berikut. ln(P/100) = -h/7; Puncak Jayawijaya memiliki ketinggian 4.884 m di atas permukaan laut. Dengan rumus tersebut, prediksilah tekanan udara di daerah tersebut.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman tentang hubungan invers antara fungsi logaritma natural dan fungsi eksponensial untuk memanipulasi persamaan yang diberikan.. Bukti: ln(P/100) = -h/7
- Intended difficulty `classify/Medium`: Soal memerlukan konversi satuan (meter ke kilometer), substitusi nilai, dan manipulasi aljabar untuk menyelesaikan fungsi eksponensial. Ini adalah prosedur rutin dalam pemodelan matematika kelas 11.. Bukti: Puncak Jayawijaya memiliki ketinggian 4.884 m di atas permukaan laut.; ln(P/100) = -h/7

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konversi satuan, sifat logaritma, dan fungsi eksponensial. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Sesuai untuk kelas 11 TL karena melibatkan pemodelan fungsi logaritma/eksponensial yang merupakan standar kurikulum. |

Run 2 — solusi: h = 4,884 km. ln(P/100) = -4,884/7 ≈ -0,6977. P/100 = e^(-0,6977) ≈ 0,4977. P ≈ 49,77 kPa.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan rumus logaritma natural yang diberikan untuk memodelkan situasi nyata dan melakukan konversi satuan ketinggian.. Bukti: Hubungan antara tekanan udara P (dalam kPa) dan ketinggian h (dalam km) dapat dimodelkan sebagai berikut. ln(P/100) = -h/7
- Dimensi pengetahuan `classify/procedural`: Melibatkan penggunaan algoritma invers logaritma (eksponensial) untuk menyelesaikan variabel P.. Bukti: ln(P/100) = -h/7
- Intended difficulty `classify/Medium`: Soal menuntut pemahaman fungsi logaritma dan eksponensial dalam konteks aplikasi, memerlukan konversi satuan dan manipulasi aljabar.. Bukti: Puncak Jayawijaya memiliki ketinggian 4.884 m di atas permukaan laut.; ln(P/100) = -h/7

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep logaritma natural, fungsi eksponensial, dan konversi satuan. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 11 TL yang mencakup fungsi logaritma dan aplikasinya. |

Run 3 — solusi: ln(P/100) = -4.884/7 = -0.6977. Maka P/100 = e^(-0.6977) = 0.4977. P = 100 * 0.4977 = 49.77 kPa.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur invers logaritma natural (eksponensial) untuk mengisolasi variabel P dan melakukan konversi satuan ketinggian dari meter ke kilometer.. Bukti: Hubungan antara tekanan udara P (dalam kPa) dan ketinggian h (dalam km) dapat dimodelkan sebagai berikut. ln(P/100) = -h/7; Puncak Jayawijaya memiliki ketinggian 4.884 m di atas permukaan laut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dalam memanipulasi fungsi logaritma natural menjadi bentuk eksponensial untuk menyelesaikan masalah kontekstual.. Bukti: ln(P/100) = -h/7
- Intended difficulty `classify/Medium`: Soal memerlukan konversi satuan (m ke km), pemahaman hubungan log-eksponen, dan kalkulasi nilai eksponensial. Ini adalah langkah rutin yang saling terkait.. Bukti: Puncak Jayawijaya memiliki ketinggian 4.884 m di atas permukaan laut.; ln(P/100) = -h/7

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman fungsi logaritma natural dan eksponensial, serta konversi satuan dasar. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 11 TL karena melibatkan penerapan fungsi transenden (logaritma/eksponen) dalam pemodelan nyata. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3947`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur invers logaritma natural (eksponensial) untuk mengisolasi variabel P dan melakukan konversi satuan ketinggian dari meter ke kilometer. Ini adalah penerapan konsep fungsi transenden dalam konteks nyata.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural dalam memanipulasi fungsi logaritma natural menjadi bentuk eksponensial untuk menyelesaikan masalah kontekstual.
- Intended difficulty `Medium`: Soal memerlukan konversi satuan (m ke km), pemahaman hubungan log-eksponen, dan kalkulasi nilai eksponensial. Ini adalah langkah rutin yang saling terkait.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konversi satuan, sifat logaritma, dan fungsi eksponensial. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 11 TL karena melibatkan penerapan fungsi transenden (logaritma/eksponen) dalam pemodelan nyata. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
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
| 1 | success | valid / verified | applying | procedural | Easy | 2046 |
| 2 | success | valid / verified | knowing | procedural | Easy | 1950 |
| 3 | success | valid / verified | applying | procedural | Easy | 2014 |

Run 1 — solusi: pH = -log[H+] = -log(10^-3,15) = -(-3,15) = 3,15.
- Domain kognitif `classify/applying`: Soal ini meminta siswa menerapkan definisi logaritma dalam konteks pH secara langsung. Siswa hanya perlu mengenali rumus pH = -log[H+] dan melakukan substitusi nilai yang diberikan, yang merupakan proses rutin.. Bukti: Jika segelas jus jeruk mempunyai ion hidrogen 10^-3,15, tentukan nilai pH jus jeruk tersebut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma perhitungan pH menggunakan logaritma basis 10, yang merupakan prosedur standar dalam materi logaritma.. Bukti: Jika segelas jus jeruk mempunyai ion hidrogen 10^-3,15, tentukan nilai pH jus jeruk tersebut.
- Intended difficulty `classify/Easy`: Soal ini sangat langsung (prosedural) dengan beban kognitif rendah. Siswa hanya perlu menerapkan satu rumus dasar tanpa modifikasi atau strategi kompleks.. Bukti: Jika segelas jus jeruk mempunyai ion hidrogen 10^-3,15, tentukan nilai pH jus jeruk tersebut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar logaritma basis 10 dan sifat logaritma log(a^b) = b log a. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun logaritma diajarkan di kelas 10/11, soal ini adalah aplikasi langsung dari definisi logaritma tanpa variasi tingkat lanjut, sehingga tergolong mudah bagi siswa kelas 11. |

Run 2 — solusi: pH = -log[H+] = -log(10^-3,15) = -(-3,15) = 3,15.
- Domain kognitif `classify/knowing`: Siswa hanya perlu menerapkan definisi logaritma dan rumus pH secara langsung tanpa modifikasi strategi.. Bukti: Jika segelas jus jeruk mempunyai ion hidrogen 10^-3,15, tentukan nilai pH jus jeruk tersebut.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dasar mengenai penggunaan rumus logaritma dalam konteks kimia (pH).. Bukti: pH = -log[H+]
- Intended difficulty `classify/Easy`: Soal ini sangat rutin dan langsung, hanya memerlukan satu langkah substitusi nilai ke dalam rumus logaritma.. Bukti: Jika segelas jus jeruk mempunyai ion hidrogen 10^-3,15, tentukan nilai pH jus jeruk tersebut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi logaritma dan sifat logaritma basis 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun logaritma diajarkan di kelas 11, soal ini hanya berupa aplikasi rumus dasar tanpa kompleksitas variabel atau fungsi. |

Run 3 — solusi: pH = -log[H+] = -log(10^-3,15) = -(-3,15) = 3,15.
- Domain kognitif `classify/applying`: Soal ini meminta siswa menerapkan definisi logaritma secara langsung ke dalam rumus pH yang diberikan atau diketahui. Tidak ada strategi non-rutin yang diperlukan, hanya substitusi nilai ke dalam rumus logaritma dasar.. Bukti: Jika segelas jus jeruk mempunyai ion hidrogen 10^-3,15, tentukan nilai pH jus jeruk tersebut.
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami hubungan antara logaritma basis 10 dan eksponen, serta menerapkan prosedur perhitungan logaritma sederhana.. Bukti: pH = -log[H+] = -log 10^-3,15 = 3,15
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung dengan satu langkah perhitungan menggunakan sifat logaritma dasar. Beban kognitif sangat rendah.. Bukti: Jika segelas jus jeruk mempunyai ion hidrogen 10^-3,15, tentukan nilai pH jus jeruk tersebut.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar logaritma basis 10 dan sifat logaritma log(a^n) = n. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun logaritma dipelajari di kelas 10/11, soal ini hanya menuntut penerapan rumus dasar tanpa kompleksitas tambahan, sehingga dikategorikan mudah untuk siswa kelas 11. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3440`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Soal ini meminta penerapan langsung definisi logaritma dalam konteks rumus pH. Siswa hanya perlu mengenali rumus pH = -log[H+] dan melakukan substitusi nilai yang diberikan, yang merupakan proses rutin tanpa modifikasi strategi.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural dasar mengenai penggunaan rumus logaritma dan sifat logaritma basis 10 dalam konteks kimia.
- Intended difficulty `Easy`: Soal ini sangat rutin dan langsung, hanya memerlukan satu langkah substitusi nilai ke dalam rumus logaritma tanpa kompleksitas variabel atau fungsi.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Definisi logaritma dan sifat logaritma basis 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun logaritma diajarkan di kelas 11, soal ini hanya berupa aplikasi rumus dasar tanpa kompleksitas variabel atau fungsi, sehingga tergolong mudah. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: Lakukan pembagian polinomial: (x^5 + x^4 + x^2 + 1) / (x^4 + 3). Hasil bagi (x^5 + x^4 + x^2 + 1) = x(x^4 + 3) + 1(x^4 + 3) + (x^2 - 3x - 2). Maka p(x) = x + 1 + (x^2 - 3x - 2)/(x^4 + 3). Saat x mendekati tak hingga, suku sisa mendekati 0, sehingga asimtot miringnya adalah y = x + 1.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `91fe5a4293e98b57e1f459ac45a4b89de6126158b7b8d142666683821e0f11ea`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2200 |
| 2 | success | valid / verified | applying | procedural | Medium | 2268 |
| 3 | success | valid / verified | applying | procedural | Medium | 2201 |

Run 1 — solusi: Lakukan pembagian polinomial: (x^5 + x^4 + x^2 + 1) / (x^4 + 3). Hasil bagi (x^5 + x^4 + x^2 + 1) = x(x^4 + 3) + 1(x^4 + 3) + (x^2 - 3x - 2). Maka p(x) = x + 1 + (x^2 - 3x - 2)/(x^4 + 3). Saat x mendekati tak hingga, suku sisa mendekati 0, sehingga asimtot miringnya adalah y = x + 1.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pembagian polinomial untuk menentukan perilaku fungsi saat x mendekati tak hingga. Ini adalah penerapan algoritma standar pada situasi rutin.. Bukti: Tentukan asimtot miring dari fungsi p(x) = (x^5 + x^4 + x^2 + 1) / (x^4 + 3)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pembagian polinomial untuk menemukan asimtot miring.. Bukti: Tentukan asimtot miring dari fungsi p(x) = (x^5 + x^4 + x^2 + 1) / (x^4 + 3)
- Intended difficulty `classify/Medium`: Soal memerlukan pembagian polinomial yang melibatkan beberapa langkah rutin (pembagian bersusun) untuk mendapatkan hasil bagi linear. Prosedur ini standar untuk kelas 11 TL.. Bukti: Tentukan asimtot miring dari fungsi p(x) = (x^5 + x^4 + x^2 + 1) / (x^4 + 3)

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
| gradeRelativeRationale | Materi asimtot fungsi rasional dan pembagian polinomial adalah kurikulum standar kelas 11 TL. Tingkat kesulitan menengah karena memerlukan ketelitian dalam pembagian polinomial. |

Run 2 — solusi: Melakukan pembagian polinomial: (x^5 + x^4 + x^2 + 1) / (x^4 + 3). x^5 dibagi x^4 adalah x. (x^4 + 3) * x = x^5 + 3x. Sisa: (x^5 + x^4 + x^2 + 1) - (x^5 + 3x) = x^4 + x^2 - 3x + 1. x^4 dibagi x^4 adalah 1. (x^4 + 3) * 1 = x^4 + 3. Sisa akhir: (x^4 + x^2 - 3x + 1) - (x^4 + 3) = x^2 - 3x - 2. Hasil bagi adalah x + 1 dengan sisa (x^2 - 3x - 2). Asimtot miring adalah y = x + 1.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pembagian polinomial untuk menentukan asimtot miring, yang merupakan prosedur standar dalam analisis fungsi rasional.. Bukti: Tentukan asimtot miring dari fungsi p(x) = (x^5 + x^4 + x^2 + 1) / (x^4 + 3)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pembagian polinomial untuk menentukan perilaku asimtotik fungsi rasional.. Bukti: Tentukan asimtot miring dari fungsi p(x) = (x^5 + x^4 + x^2 + 1) / (x^4 + 3)
- Intended difficulty `classify/Medium`: Soal memerlukan pembagian polinomial dua langkah (x+1) dan pemahaman konsep asimtot miring. Prosedur ini rutin bagi siswa kelas 11 TL.. Bukti: Tentukan asimtot miring dari fungsi p(x) = (x^5 + x^4 + x^2 + 1) / (x^4 + 3)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pembagian polinomial dan konsep asimtot fungsi rasional. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi asimtot fungsi rasional adalah bagian dari kurikulum Matematika Tingkat Lanjut kelas 11. Prosedur pembagian polinomial adalah keterampilan rutin. |

Run 3 — solusi: Lakukan pembagian polinomial: (x^5 + x^4 + x^2 + 1) / (x^4 + 3). Hasil bagi (x^5 + x^4 + x^2 + 1) = x(x^4 + 3) + 1(x^4 + 3) + (x^2 - 3x - 2). Maka p(x) = x + 1 + (x^2 - 3x - 2)/(x^4 + 3). Saat x mendekati tak hingga, suku sisa mendekati 0. Asimtot miring adalah y = x + 1.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pembagian polinomial untuk menentukan perilaku fungsi saat x mendekati tak hingga. Ini adalah penerapan algoritma standar pada situasi rutin.. Bukti: Tentukan asimtot miring dari fungsi p(x) = (x^5 + x^4 + x^2 + 1) / (x^4 + 3)
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pembagian polinomial dan konsep asimtot miring sebagai hasil bagi polinomial.. Bukti: Tentukan asimtot miring dari fungsi p(x) = (x^5 + x^4 + x^2 + 1) / (x^4 + 3)
- Intended difficulty `classify/Medium`: Soal memerlukan pembagian polinomial yang melibatkan beberapa langkah rutin. Tingkat kesulitan sedang karena siswa harus melakukan pembagian polinomial secara teliti untuk mendapatkan hasil bagi yang benar.. Bukti: Tentukan asimtot miring dari fungsi p(x) = (x^5 + x^4 + x^2 + 1) / (x^4 + 3)

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
| gradeRelativeRationale | Materi asimtot fungsi rasional adalah bagian dari kurikulum Matematika Tingkat Lanjut kelas 11. Prosedur pembagian polinomial adalah keterampilan rutin yang diharapkan. |

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
Solusi minimum hasil AI: Biaya total B(x) adalah jumlah biaya tetap dan biaya variabel. Biaya tetap = 7.000.000. Biaya variabel = 40.000 per loyang (x). Maka, B(x) = 7.000.000 + 40.000x.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0b0249bab0e9e25edb06bc904e6070e0b1da43b70c918775ce63cba3f80fb3b1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2584 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2948 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2989 |

Run 1 — solusi: Fungsi biaya total adalah jumlah dari biaya tetap dan biaya variabel. Biaya tetap = 7.000.000. Biaya variabel = 40.000 per loyang (x). Maka, B(x) = 7.000.000 + 40.000x.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep fungsi linear sederhana untuk memodelkan situasi biaya nyata, yang merupakan proses rutin dalam matematika.. Bukti: Tentukan model matematika dari fungsi biaya untuk memproduksi x loyang kue bronis.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang struktur fungsi linear (biaya tetap vs biaya variabel).. Bukti: Misalkan rumus fungsi biaya adalah B(x) = biaya tetap + cx
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung dengan beban kognitif rendah, cocok untuk tingkat kemahiran dasar.. Bukti: biaya bulanan Rp7.000.000,00 dan biaya produksi Rp40.000,00 per loyang kue

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
| gradeRelativeRationale | Materi ini merupakan dasar pemodelan linear yang sudah dikuasai siswa sebelum kelas 11, sehingga tingkat kesulitannya rendah. |

Run 2 — solusi: Fungsi biaya total dirumuskan sebagai B(x) = biaya tetap + (biaya per unit) * x. Dengan biaya tetap = 7.000.000 dan biaya per unit = 40.000, maka model matematikanya adalah B(x) = 7.000.000 + 40.000x.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali komponen biaya tetap dan biaya variabel, lalu menyusunnya ke dalam bentuk fungsi linear yang sudah diberikan dalam soal.. Bukti: biaya bulanan Rp7.000.000,00; biaya produksi Rp40.000,00 per loyang kue; rumus fungsi biaya adalah B(x) = biaya tetap + cx
- Dimensi pengetahuan `classify/conceptual`: Memahami struktur fungsi linear sebagai penjumlahan antara konstanta (biaya tetap) dan variabel (biaya produksi per unit).. Bukti: rumus fungsi biaya adalah B(x) = biaya tetap + cx
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung dengan beban kognitif rendah, tidak memerlukan strategi non-rutin atau integrasi konsep yang kompleks.. Bukti: biaya bulanan Rp7.000.000,00; biaya produksi Rp40.000,00 per loyang kue

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
| gradeRelativeRationale | Meskipun berada di kelas 11, soal ini merupakan aplikasi dasar fungsi linear yang sudah dipelajari di jenjang sebelumnya dan tidak memenuhi kriteria kesulitan matematika tingkat lanjut. |

Run 3 — solusi: B(x) = biaya tetap + (biaya per unit * x) = 7.000.000 + 40.000x
- Domain kognitif `classify/knowing`: Siswa hanya perlu memetakan nilai yang diberikan ke dalam struktur fungsi linear yang sudah disediakan di soal tanpa memerlukan strategi kompleks.. Bukti: biaya bulanan Rp7.000.000,00; biaya produksi Rp40.000,00 per loyang kue; rumus fungsi biaya adalah B(x) = biaya tetap + cx
- Dimensi pengetahuan `classify/conceptual`: Memahami hubungan antara komponen biaya tetap dan biaya variabel dalam struktur fungsi linear.. Bukti: rumus fungsi biaya adalah B(x) = biaya tetap + cx
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dengan substitusi nilai ke dalam rumus yang sudah diberikan, sehingga beban kognitif sangat rendah.. Bukti: biaya bulanan Rp7.000.000,00; biaya produksi Rp40.000,00 per loyang kue; B(x) = biaya tetap + cx

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
| gradeRelativeRationale | Materi ini terlalu mendasar untuk standar kelas 11 Matematika Tingkat Lanjut, lebih tepat sebagai materi prasyarat atau pengingat konsep fungsi linear. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 1, "knowing": 2} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4346`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan konsep fungsi linear sederhana untuk memodelkan situasi biaya nyata, yang merupakan proses rutin dalam matematika.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang struktur fungsi linear (biaya tetap vs biaya variabel).
- Intended difficulty `Easy`: Soal ini bersifat prosedural langsung dengan beban kognitif rendah, cocok untuk tingkat kemahiran dasar.

Profil difficulty hasil adjudikasi:

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
| gradeRelativeRationale | Materi ini merupakan dasar pemodelan linear yang sudah dikuasai siswa sebelum kelas 11, sehingga tingkat kesulitannya rendah. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: Model pertumbuhan eksponensial: N(t) = N0 * 2^(t/T). N0 = 500, T = 30 menit, t = 40 menit. N(40) = 500 * 2^(40/30) = 500 * 2^(4/3) = 500 * 2^(1.333) ≈ 500 * 2.5198 ≈ 1.259,9. Dibulatkan menjadi sekitar 1.260.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `264357d4b6c46949cbbaf2d8eccd0b9a743722dcec09459127403781ddcbed0a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2162 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2135 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2142 |

Run 1 — solusi: Model pertumbuhan eksponensial: N(t) = N0 * 2^(t/T). N0 = 500, T = 30 menit, t = 40 menit. N(40) = 500 * 2^(40/30) = 500 * 2^(4/3) = 500 * 2^(1.333) ≈ 500 * 2.5198 ≈ 1.259,9. Dibulatkan menjadi sekitar 1.260.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan model fungsi eksponensial untuk situasi pertumbuhan. Ini melibatkan pemilihan prosedur yang tepat (rumus pertumbuhan eksponensial) dan menerapkannya pada konteks yang diberikan, yang masuk dalam kategori applying.. Bukti: Bakteri jenis ini mampu membelah diri menjadi dua setiap setengah jam sekali.; Berapa banyak bakteri setelah 40 menit?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara variabel waktu dan pertumbuhan eksponensial, yang merupakan konsep dasar dalam fungsi non-aljabar.. Bukti: Bakteri jenis ini mampu membelah diri menjadi dua setiap setengah jam sekali.
- Intended difficulty `classify/Medium`: Soal ini memerlukan konversi satuan waktu dan penerapan rumus eksponensial sederhana. Langkah-langkahnya rutin dan prosedural, cocok untuk tingkat kesulitan menengah bagi kelas 11.. Bukti: Bakteri jenis ini mampu membelah diri menjadi dua setiap setengah jam sekali.; Berapa banyak bakteri setelah 40 menit?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi eksponensial dan operasi pecahan/eksponen. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini menguji aplikasi fungsi eksponensial yang merupakan materi kelas 11 TL. Tingkat kesulitan menengah karena memerlukan konversi waktu (40 menit ke 4/3 jam) dan perhitungan eksponen pecahan. |

Run 2 — solusi: Model pertumbuhan eksponensial: N(t) = N0 * 2^(t/T). Diketahui N0 = 500, T = 30 menit, t = 40 menit. N(40) = 500 * 2^(40/30) = 500 * 2^(4/3) = 500 * 2^(1.333) ≈ 500 * 2.5198 ≈ 1259.9. Dibulatkan menjadi sekitar 1.260.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan model pertumbuhan eksponensial (konsep) untuk situasi nyata. Ini melibatkan pemilihan prosedur yang tepat (menggunakan rasio waktu terhadap periode pembelahan) dan melakukan perhitungan, yang masuk dalam kategori applying.. Bukti: mampu membelah diri menjadi dua setiap setengah jam sekali; Berapa banyak bakteri setelah 40 menit?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menuntut pemahaman tentang hubungan antara waktu dan laju pertumbuhan eksponensial, yang merupakan konsep dasar dalam fungsi non-aljabar.. Bukti: mampu membelah diri menjadi dua setiap setengah jam sekali; Berapa banyak bakteri setelah 40 menit?
- Intended difficulty `classify/Medium`: Soal memerlukan konversi satuan waktu dan penerapan rumus eksponensial sederhana. Langkah-langkahnya rutin dan langsung, namun memerlukan ketelitian dalam menentukan eksponen (40/30).. Bukti: setiap setengah jam sekali; setelah 40 menit

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi eksponensial dan operasi pecahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun konsepnya dasar, penggunaan eksponen pecahan (4/3) dan konteks pertumbuhan bakteri adalah standar untuk kelas 11 TL. |

Run 3 — solusi: Model pertumbuhan eksponensial: N(t) = N0 * 2^(t/T). N0 = 500, T = 30 menit, t = 40 menit. N(40) = 500 * 2^(40/30) = 500 * 2^(4/3) = 500 * 2^(1.333) ≈ 500 * 2.5198 ≈ 1259.9. Dibulatkan menjadi sekitar 1.260.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan model pertumbuhan eksponensial (fungsi non-aljabar) pada situasi kontekstual. Ini melibatkan pemilihan prosedur yang tepat untuk memodelkan pertumbuhan bakteri dengan periode waktu yang tidak bulat, yang merupakan penerapan konsep rutin.. Bukti: Bakteri jenis ini mampu membelah diri menjadi dua setiap setengah jam sekali.; Berapa banyak bakteri setelah 40 menit?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara variabel waktu dan pertumbuhan eksponensial, yang merupakan konsep dasar dalam fungsi non-aljabar.. Bukti: Bakteri jenis ini mampu membelah diri menjadi dua setiap setengah jam sekali.
- Intended difficulty `classify/Medium`: Soal memerlukan pemahaman konsep pertumbuhan eksponensial dan kemampuan untuk memanipulasi eksponen pecahan (40/30). Ini adalah prosedur standar untuk kelas 11 TL.. Bukti: Bakteri jenis ini mampu membelah diri menjadi dua setiap setengah jam sekali.; Berapa banyak bakteri setelah 40 menit?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman fungsi eksponensial dan operasi bilangan berpangkat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sesuai untuk kelas 11 TL karena melibatkan penerapan fungsi eksponensial pada masalah pertumbuhan, yang merupakan materi standar. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Medium", "agreement": null}}`.
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
Solusi minimum hasil AI: Model pertumbuhan eksponensial adalah N(t) = N0 * 2^(t/T), dengan N0 = 500 dan periode pembelahan T = 0,5 jam. Maka, N(t) = 500 * 2^(t/0,5) = 500 * 2^(2t).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `980fdf23391ce2b3a674daabaadad0e7d937f5b1ce358e146f7706d74bbd3eec`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2702 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2695 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2890 |

Run 1 — solusi: Model pertumbuhan eksponensial adalah P(t) = P0 * 2^(t/d), dengan P0 = 500 dan d = 0,5 jam. Maka, P(t) = 500 * 2^(t/0,5) = 500 * 2^(2t).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep fungsi eksponensial untuk memodelkan pertumbuhan bakteri berdasarkan laju pembelahan yang diberikan.. Bukti: mampu membelah diri menjadi dua setiap setengah jam sekali; Berapa banyak bakteri setelah t jam?
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman konseptual tentang hubungan antara waktu, periode penggandaan, dan eksponen dalam fungsi pertumbuhan.. Bukti: mampu membelah diri menjadi dua setiap setengah jam sekali
- Intended difficulty `classify/Medium`: Soal ini merupakan aplikasi rutin fungsi eksponensial. Siswa harus menentukan eksponen yang tepat (2t) berdasarkan periode pembelahan (0,5 jam).. Bukti: mampu membelah diri menjadi dua setiap setengah jam sekali; Berapa banyak bakteri setelah t jam?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi eksponensial dan sifat perpangkatan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 11 sebagai penerapan fungsi eksponensial dalam konteks pertumbuhan. |

Run 2 — solusi: Model pertumbuhan eksponensial adalah N(t) = N0 * 2^(t/Td). Dengan N0 = 500 dan periode pembelahan Td = 0,5 jam, maka N(t) = 500 * 2^(t/0,5) = 500 * 2^(2t).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan model pertumbuhan eksponensial pada konteks pembelahan bakteri, yang memerlukan pemahaman tentang bagaimana periode waktu mempengaruhi eksponen.. Bukti: mampu membelah diri menjadi dua setiap setengah jam sekali; Berapa banyak bakteri setelah t jam?
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman konseptual tentang hubungan antara laju pertumbuhan, periode waktu, dan bentuk fungsi eksponensial.. Bukti: membelah diri menjadi dua setiap setengah jam sekali
- Intended difficulty `classify/Medium`: Soal ini menuntut pemahaman konsep eksponensial yang diaplikasikan pada masalah nyata, sedikit lebih kompleks dari sekadar substitusi langsung karena adanya pembagi pada eksponen.. Bukti: 500 bakteri; membelah diri menjadi dua setiap setengah jam sekali

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep fungsi eksponensial dasar dan pemahaman variabel waktu. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sesuai untuk kelas 11 karena menguji pemahaman fungsi eksponensial dalam konteks pertumbuhan, yang merupakan bagian dari kurikulum matematika tingkat lanjut. |

Run 3 — solusi: Bakteri membelah menjadi dua setiap 0,5 jam. Dalam t jam, jumlah periode pembelahan adalah t / 0,5 = 2t. Maka, jumlah bakteri setelah t jam adalah 500 * 2^(2t).
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan konteks pertumbuhan eksponensial ke dalam model matematika dengan menentukan eksponen yang tepat berdasarkan periode waktu.. Bukti: Bakteri jenis ini mampu membelah diri menjadi dua setiap setengah jam sekali.; Berapa banyak bakteri setelah t jam?
- Dimensi pengetahuan `classify/conceptual`: Memahami hubungan antara laju pertumbuhan (periode waktu) dan model fungsi eksponensial.. Bukti: Bakteri jenis ini mampu membelah diri menjadi dua setiap setengah jam sekali.
- Intended difficulty `classify/Easy`: Soal ini memerlukan pemahaman konsep pertumbuhan eksponensial dan penentuan variabel waktu yang tepat. Ini adalah prosedur rutin dalam pemodelan fungsi eksponensial.. Bukti: Bakteri jenis ini mampu membelah diri menjadi dua setiap setengah jam sekali.; Berapa banyak bakteri setelah t jam?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep fungsi eksponensial dan pemahaman dasar tentang laju pertumbuhan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi fungsi eksponensial adalah bagian standar kurikulum kelas 11. Soal ini menguji pemahaman dasar pemodelan tanpa kompleksitas tinggi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3494`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan konsep fungsi eksponensial untuk memodelkan pertumbuhan bakteri. Proses ini melibatkan pemilihan model yang tepat dan penyesuaian eksponen berdasarkan periode waktu yang diberikan, yang merupakan penerapan prosedur rutin.
- Dimensi pengetahuan `conceptual`: Memerlukan pemahaman konseptual tentang hubungan antara laju pertumbuhan, periode waktu, dan bentuk fungsi eksponensial untuk menentukan eksponen yang benar.
- Intended difficulty `Easy`: Soal ini adalah prosedur rutin dalam pemodelan fungsi eksponensial. Siswa hanya perlu memahami hubungan antara periode pembelahan dan variabel waktu t untuk menyusun fungsi.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar fungsi eksponensial dan sifat perpangkatan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan aplikasi standar fungsi eksponensial yang sesuai untuk kelas 11, menguji pemahaman dasar tanpa kompleksitas tinggi. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
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
Solusi minimum hasil AI: (5x^{5/2})(3x^{1/3}) = (5 \cdot 3)(x^{5/2 + 1/3}) = 15x^{15/6 + 2/6} = 15x^{17/6}
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `16fa2dc1f3df6aec3e5cf64dd8aeb63fb93012c1a69d3583cf33552131454d63`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2076 |
| 2 | success | valid / verified | applying | procedural | Easy | 2126 |
| 3 | success | valid / verified | applying | procedural | Easy | 2059 |

Run 1 — solusi: (5x^{5/2})(3x^{1/3}) = (5 \cdot 3)(x^{5/2 + 1/3}) = 15x^{15/6 + 2/6} = 15x^{17/6}
- Domain kognitif `classify/applying`: Siswa perlu menerapkan aturan eksponen (perkalian koefisien dan penjumlahan pangkat pecahan) untuk menyederhanakan ekspresi. Ini adalah penerapan prosedur rutin pada situasi yang familiar.. Bukti: Sederhanakan bentuk akar berikut ini. (5\sqrt{x^5})(3\sqrt[3]{x})
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma operasi aljabar pada bentuk akar dan konversi ke eksponen pecahan.. Bukti: (5\sqrt{x^5})(3\sqrt[3]{x})
- Intended difficulty `classify/Easy`: Soal ini memerlukan konversi radikal ke eksponen pecahan dan penjumlahan pecahan dengan penyebut berbeda. Ini adalah prosedur standar yang rutin bagi siswa kelas 11.. Bukti: (5\sqrt{x^5})(3\sqrt[3]{x})

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar eksponen pecahan dan operasi aljabar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun materi bentuk akar sering diajarkan di kelas 10, soal ini merupakan prasyarat dasar untuk materi logaritma dan fungsi eksponen di kelas 11 TL. |

Run 2 — solusi: Ubah bentuk akar ke eksponen pecahan: 5x^(5/2) * 3x^(1/3). Kalikan koefisien: 5 * 3 = 15. Jumlahkan eksponen: 5/2 + 1/3 = 15/6 + 2/6 = 17/6. Hasil akhir: 15x^(17/6).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan aturan eksponen (perkalian basis sama) dan mengubah bentuk akar menjadi eksponen pecahan. Ini adalah prosedur rutin yang dipelajari di kelas 10 dan diterapkan di kelas 11, sehingga masuk kategori applying.. Bukti: Sederhanakan bentuk akar berikut ini. (5\sqrt{x^5})(3\sqrt[3]{x})
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma operasi aljabar pada bentuk akar dan eksponen, yang merupakan pengetahuan prosedural.. Bukti: Sederhanakan bentuk akar berikut ini. (5\sqrt{x^5})(3\sqrt[3]{x})
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan langkah-langkah yang jelas (mengubah bentuk akar, menyamakan penyebut pecahan, menjumlahkan eksponen). Tidak ada strategi non-rutin atau integrasi konsep yang kompleks.. Bukti: Sederhanakan bentuk akar berikut ini. (5\sqrt{x^5})(3\sqrt[3]{x})

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Operasi dasar eksponen dan bentuk akar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini merupakan prasyarat dasar untuk aljabar tingkat lanjut di kelas 11, sehingga bagi siswa kelas 11, ini adalah prosedur yang sangat familiar dan mudah. |

Run 3 — solusi: Ekspresi: (5x^(5/2))(3x^(1/3)) = (5*3) * x^(5/2 + 1/3) = 15 * x^(15/6 + 2/6) = 15x^(17/6).
- Domain kognitif `classify/applying`: Siswa perlu menerapkan aturan eksponen untuk menyederhanakan perkalian bentuk akar, yang merupakan prosedur rutin dalam matematika tingkat lanjut.. Bukti: Sederhanakan bentuk akar berikut ini. (5\sqrt{x^5})(3\sqrt[3]{x})
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma konversi bentuk akar ke eksponen pecahan dan aturan penjumlahan eksponen.. Bukti: Sederhanakan bentuk akar berikut ini. (5\sqrt{x^5})(3\sqrt[3]{x})
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan langkah-langkah yang jelas (konversi ke eksponen, samakan penyebut, jumlahkan). Tidak memerlukan strategi non-rutin.. Bukti: Sederhanakan bentuk akar berikut ini. (5\sqrt{x^5})(3\sqrt[3]{x})

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar eksponen pecahan dan operasi pecahan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi ini merupakan prasyarat dasar untuk aljabar tingkat lanjut di kelas 11, namun prosedurnya sangat standar dan familiar. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
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
Solusi minimum hasil AI: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 12, maka banyak korespondensi satu-satu adalah 12! = 479.001.600.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 11 / Matematika Tingkat Lanjut SMA Kelas 11. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `36dbe81fb81c6b1b53006f6bafb3b833187eba1380e0300346df35543e87332a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2348 |
| 2 | success | valid / verified | applying | procedural | Easy | 2281 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2315 |

Run 1 — solusi: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 12, maka banyak korespondensi adalah 12! = 12 × 11 × 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 479.001.600.
- Domain kognitif `classify/applying`: Soal ini meminta siswa untuk menerapkan rumus faktorial untuk menentukan banyaknya korespondensi satu-satu (bijeksi) antara dua himpunan berhingga dengan jumlah anggota yang sama. Ini adalah penerapan langsung dari konsep dasar kombinatorika.. Bukti: Ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep korespondensi satu-satu dan prinsip perkalian (faktorial) untuk menyelesaikan masalah ini.. Bukti: n(A) = n(B) = 12; banyak korespondensi satu-satu yang mungkin adalah n! = 12! = 479.001.600
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung dengan satu langkah utama (menghitung faktorial). Tidak ada strategi nonrutin atau integrasi representasi yang kompleks.. Bukti: n(A) = n(B) = 12; banyak korespondensi satu-satu yang mungkin adalah n! = 12!

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang himpunan dan faktorial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun faktorial 12 cukup besar, konsep dasarnya adalah materi dasar kombinatorika yang rutin bagi siswa kelas 11. |

Run 2 — solusi: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 12, maka 12! = 12 × 11 × 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 479.001.600.
- Domain kognitif `classify/applying`: Siswa perlu mengenali konsep korespondensi satu-satu sebagai permutasi dari n elemen, yang merupakan prosedur standar dalam materi himpunan/kombinatorika.. Bukti: Ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang rumus faktorial untuk menghitung banyaknya korespondensi satu-satu.. Bukti: n(A) = n(B) = 12; banyak korespondensi satu-satu yang mungkin adalah n!
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin karena hanya memerlukan penerapan langsung rumus n! untuk n=12. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.. Bukti: n(A) = n(B) = 12

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang himpunan dan faktorial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun faktorial 12 cukup besar, konsep dasarnya adalah prosedur standar yang familiar di tingkat SMA. |

Run 3 — solusi: Banyak korespondensi satu-satu antara dua himpunan A dan B dengan n(A) = n(B) = n adalah n!. Untuk n = 12, maka banyak korespondensi satu-satu adalah 12! = 12 × 11 × 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 479.001.600.
- Domain kognitif `classify/knowing`: Soal meminta penerapan langsung rumus faktorial untuk menghitung banyaknya korespondensi satu-satu (bijeksi) antara dua himpunan berhingga dengan kardinalitas yang sama. Siswa hanya perlu mengenali konsep dan menerapkan prosedur perhitungan faktorial.. Bukti: ada berapa banyak korespondensi satu-satu yang mungkin dari himpunan A dan himpunan B jika n(A) = n(B) = 12
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang rumus permutasi/korespondensi satu-satu pada himpunan berhingga.. Bukti: banyak korespondensi satu-satu yang mungkin adalah n! = 12! = 479.001.600
- Intended difficulty `classify/Easy`: Soal ini bersifat prosedural langsung dengan satu langkah utama (menghitung faktorial). Tidak ada strategi nonrutin atau integrasi konsep yang kompleks.. Bukti: n(A) = n(B) = 12

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang himpunan dan faktorial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun faktorial 12 cukup besar, konsep korespondensi satu-satu adalah materi dasar yang rutin dalam kombinatorika tingkat SMA. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3915`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Soal ini meminta penerapan langsung rumus faktorial untuk menghitung banyaknya korespondensi satu-satu (bijeksi) antara dua himpunan berhingga dengan kardinalitas yang sama. Siswa hanya perlu mengenali konsep dan menerapkan prosedur perhitungan faktorial.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang rumus faktorial untuk menghitung banyaknya korespondensi satu-satu pada himpunan berhingga.
- Intended difficulty `Easy`: Soal ini bersifat rutin karena hanya memerlukan penerapan langsung rumus n! untuk n=12. Tidak ada kendala kompleks atau strategi non-rutin yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang himpunan dan faktorial. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun faktorial 12 cukup besar, konsep korespondensi satu-satu adalah materi dasar yang rutin dalam kombinatorika tingkat SMA. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Scope model: `out_of_scope`. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi tetap dicatat untuk audit.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / grade_outside_sd_v1 |
| Dimensi pengetahuan |  | — | — | — | abstain / grade_outside_sd_v1 |
| Intended difficulty |  | — | — | — | abstain / grade_outside_sd_v1 |

<details><summary>Input terserialisasi untuk audit; encoder tidak dijalankan</summary>

```text
Kelas: 11
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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
