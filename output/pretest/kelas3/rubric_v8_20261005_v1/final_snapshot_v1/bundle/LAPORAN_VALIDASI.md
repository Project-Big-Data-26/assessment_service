# Validasi ulang soal kelas 3 — Gemini blind N=3 dan diagnostik IndoBERT

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v10-blind-key-verified`. Rubrik: `math-rubric-3x4x3-v8-sd-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 3 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan menjadi keputusan silver operasional.

Checkpoint dikunci dengan SHA-256 sebelum inferensi IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Prediksi model dipakai sebagai diagnostik; tidak diberikan kembali ke Gemini.

Jumlah soal: 42; distribusi label advisory: `{"mathCognitiveDomain": {"applying": 27, "knowing": 15, "reasoning": 0}, "knowledgeDimension": {"conceptual": 17, "factual": 8, "procedural": 17, "metacognitive": 0}, "intendedDifficulty": {"Easy": 33, "Medium": 9, "Hard": 0}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"applying": 26, "knowing": 14, "reasoning": 0}, "knowledgeDimension": {"conceptual": 16, "factual": 8, "procedural": 16, "metacognitive": 0}, "intendedDifficulty": {"Easy": 31, "Medium": 9, "Hard": 0}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"silver_ready": 40, "revision_required": 2}`.
Run awal sukses: 126/126; adjudikasi: 21; token sukses tercatat: 456,854.

Seluruh label memakai provenance ai_silver. Delivery memakai snapshot silver yang lolos qualification. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

Artifact diagnostik IndoBERT: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Dataset training: `kelas1-gemini-silver-n3-v1`. Approval provisional: `False`; research-only: `False`; gate data: `False`; anti-collapse: `False`; gate promosi: `False`. Packaging ini tidak melakukan training atau promosi model.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten dapat masuk snapshot silver operasional.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 33 | 31 | [Easy.json](difficulty/Easy.json) |
| Medium | 9 | 9 | [Medium.json](difficulty/Medium.json) |
| Hard | 0 | 0 | [Hard.json](difficulty/Hard.json) |

## Perhitungan yang dipakai

Encoder menghasilkan representasi [CLS], lalu tiga head menghasilkan logits. Probabilitas adalah pᵢ = exp(zᵢ/T) / Σⱼ exp(zⱼ/T), dengan temperature sesuai manifest. Confidence = max(pᵢ). Entropy H = −Σᵢ pᵢ ln(pᵢ) / ln(K). Probabilitas, confidence, entropy, dan action di bawah berasal dari inferensi lokal; tidak dibuat oleh Gemini.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

## 1. Soal `8de4f21dafd4452f79f06e71`

Perhatikan bilangan berikut: 239, 912, 821, 168.<br><br>Tentukan bilangan mana yang memiliki angka puluhan kurang dari 3?

| Opsi | Isi |
|---|---|
| A | 168 dan 821 |
| B | 239 dan 912 |
| C | 821 dan 912 |
| D | 239 dan 168 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Analisis angka puluhan setiap bilangan: 239 (puluhan 3), 912 (puluhan 1), 821 (puluhan 2), 168 (puluhan 6). Bilangan dengan angka puluhan kurang dari 3 adalah 912 (1 < 3) dan 821 (2 < 3). Maka jawabannya adalah 821 dan 912.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b88d63e56a10db50444dd2f2c35c727c50451c3059e3d5fd0bba6535ca697a16`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2419 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2422 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2435 |

Run 1 — solusi: Analisis angka puluhan setiap bilangan: 239 (puluhan 3), 912 (puluhan 1), 821 (puluhan 2), 168 (puluhan 6). Bilangan dengan angka puluhan kurang dari 3 adalah 912 (1 < 3) dan 821 (2 < 3). Maka jawabannya adalah 821 dan 912.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi nilai tempat (puluhan) dari sekumpulan bilangan dan membandingkannya dengan kriteria yang diberikan (kurang dari 3). Ini adalah penerapan langsung dari pemahaman nilai tempat.. Bukti: Tentukan bilangan mana yang memiliki angka puluhan kurang dari 3?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang nilai tempat (ratusan, puluhan, satuan) dalam bilangan cacah sampai 1.000.. Bukti: angka puluhan kurang dari 3
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu mengidentifikasi digit puluhan dari empat bilangan yang diberikan dan membandingkannya dengan angka 3. Tidak ada langkah yang saling bergantung atau strategi kompleks yang diperlukan.. Bukti: 239, 912, 821, 168; angka puluhan kurang dari 3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan cacah sampai 1.000 (ratusan, puluhan, satuan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah mempelajari nilai tempat bilangan sampai 1.000. Tugas ini adalah latihan rutin untuk mengidentifikasi digit tertentu dalam bilangan. |

Run 2 — solusi: Analisis angka puluhan setiap bilangan: 239 (puluhan 3), 912 (puluhan 1), 821 (puluhan 2), 168 (puluhan 6). Bilangan dengan angka puluhan kurang dari 3 adalah 912 (1 < 3) dan 821 (2 < 3). Jadi, jawabannya adalah 821 dan 912.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi nilai tempat (puluhan) dari sekumpulan bilangan yang diberikan dan membandingkannya dengan kriteria yang ditentukan (kurang dari 3). Ini adalah penerapan langsung dari pemahaman nilai tempat.. Bukti: Tentukan bilangan mana yang memiliki angka puluhan kurang dari 3?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konseptual tentang nilai tempat dalam bilangan cacah sampai 1.000, yaitu kemampuan membedakan posisi ratusan, puluhan, dan satuan.. Bukti: angka puluhan kurang dari 3
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu memeriksa angka puluhan dari empat bilangan yang diberikan dan membandingkannya dengan angka 3. Tidak ada langkah yang saling bergantung atau kendala kompleks.. Bukti: 239, 912, 821, 168; angka puluhan kurang dari 3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan cacah sampai 1.000 (ratusan, puluhan, satuan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah mempelajari nilai tempat hingga 1.000. Tugas mengidentifikasi angka puluhan adalah tugas dasar yang familiar. |

Run 3 — solusi: Analisis angka puluhan setiap bilangan: 239 (puluhan 3), 912 (puluhan 1), 821 (puluhan 2), 168 (puluhan 6). Bilangan dengan angka puluhan kurang dari 3 adalah 912 (1 < 3) dan 821 (2 < 3). Jadi, jawabannya adalah 821 dan 912.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi nilai tempat (puluhan) dari sekumpulan bilangan dan membandingkannya dengan kriteria yang diberikan (kurang dari 3). Ini adalah penerapan langsung dari pemahaman nilai tempat.. Bukti: Tentukan bilangan mana yang memiliki angka puluhan kurang dari 3?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang nilai tempat (ratusan, puluhan, satuan) dalam bilangan cacah sampai 1.000.. Bukti: 239, 912, 821, 168; angka puluhan kurang dari 3
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu memeriksa angka puluhan dari empat bilangan yang diberikan dan membandingkannya dengan angka 3. Tidak ada langkah yang saling bergantung atau kendala kompleks.. Bukti: 239, 912, 821, 168; angka puluhan kurang dari 3

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan cacah sampai 1.000. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah mempelajari nilai tempat hingga ratusan. Tugas membandingkan angka puluhan adalah tugas rutin yang sesuai dengan tingkat kelas. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 94/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.569811; applying=0.430189; reasoning=0.000000 | knowing | 0.569811 | 0.622028 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.230915; conceptual=0.737023; procedural=0.032062; metacognitive=0.000000 | conceptual | 0.737023 | 0.485929 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.864159; Medium=0.133262; Hard=0.002579 | Easy | 0.864159 | 0.373308 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.569811; −Σp ln(p) = 0.683368; H = 0.683368/ln(3) = 0.622028; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.737023; −Σp ln(p) = 0.673641; H = 0.673641/ln(4) = 0.485929; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.864159; −Σp ln(p) = 0.410121; H = 0.410121/ln(3) = 0.373308; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Bilangan dan Lambang Bilangan Cacah sampai 1.000
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan bilangan berikut: 239, 912, 821, 168.

Tentukan bilangan mana yang memiliki angka puluhan kurang dari 3?
Pilihan: A. 168 dan 821
B. 239 dan 912
C. 821 dan 912
D. 239 dan 168
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `80e0cb21740609959b756bf3`

Tuliskan lambang bilangan dan cara membaca bilangan yang terdapat pada gambar berikut.

| Opsi | Isi |
|---|---|
| A | 236 dibaca dua ratus tiga puluh enam |
| B | 326 dibaca tiga ratus dua puluh enam |
| C | 263 dibaca dua ratus enam puluh tiga |
| D | 236 dibaca dua ratus tiga enam |

![Gambar sumber soal 2](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0026-02.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Angka pada papan adalah 236. Lambang bilangan: 236. Cara membaca: dua ratus tiga puluh enam.
Gambar sumber: images/kelas3_panduan_siswa_kelas3.pdf-0026-02.png. Transkripsi visual: Gambar menunjukkan seorang anak laki-laki menunjuk ke arah papan penunjuk jalan di depan sekolah. Pada papan tersebut tertulis angka '236' dan kata 'meter'.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menyebutkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9617bdca82a1c06c3e6cb423fdd7fccc9545630dfaeec274a63fea56aff90f8d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3380 |
| 2 | success | valid / verified | knowing | factual | Easy | 3394 |
| 3 | success | valid / verified | knowing | factual | Easy | 3352 |

Run 1 — solusi: Angka pada papan adalah 236. Lambang bilangan: 236. Cara membaca: dua ratus tiga puluh enam.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi lambang bilangan dari representasi visual (angka pada papan) dan menuliskan cara membacanya. Ini adalah tugas pengenalan dan pembacaan bilangan yang bersifat langsung.. Bukti: Tuliskan lambang bilangan dan cara membaca bilangan yang terdapat pada gambar berikut.; 236 meter
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami sistem penamaan bilangan cacah (ratusan, puluhan, satuan) untuk dapat membaca angka 236 dengan benar.. Bukti: Tuliskan lambang bilangan dan cara membaca bilangan yang terdapat pada gambar berikut.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar bagi kelas 3. Siswa hanya perlu membaca angka yang tertera dan mengubahnya ke dalam bentuk kata-kata. Tidak ada langkah kompleks atau kendala yang harus dipecahkan.. Bukti: Tuliskan lambang bilangan dan cara membaca bilangan yang terdapat pada gambar berikut.; 236 meter

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal nilai tempat bilangan cacah sampai 1.000 dan cara membacanya. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca bilangan tiga angka adalah materi dasar kelas 3. Tugas ini bersifat rutin dan tidak memerlukan perencanaan langkah. |

Run 2 — solusi: Angka pada papan adalah 236. Angka 2 menempati nilai ratusan, 3 menempati puluhan, dan 6 menempati satuan. Dibaca dua ratus tiga puluh enam.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengenali lambang bilangan (236) dan menerapkan prosedur membaca bilangan cacah tiga angka yang sudah dipelajari. Ini adalah tugas pengenalan langsung tanpa perlu strategi kompleks.. Bukti: Tuliskan lambang bilangan dan cara membaca bilangan yang terdapat pada gambar berikut.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang sistem penamaan bilangan (fakta/istilah) dan cara membacanya sesuai nilai tempat.. Bukti: Tuliskan lambang bilangan dan cara membaca bilangan yang terdapat pada gambar berikut.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin bagi siswa kelas 3. Tidak ada langkah yang saling bergantung atau kendala yang harus dipecahkan.. Bukti: Tuliskan lambang bilangan dan cara membaca bilangan yang terdapat pada gambar berikut.; 236 meter

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal lambang bilangan cacah sampai 1.000 dan cara membacanya. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca bilangan tiga angka adalah materi dasar kelas 3. Soal memberikan informasi yang jelas dan tidak memerlukan penalaran tambahan. |

Run 3 — solusi: Angka pada papan adalah 236. Lambang bilangan: 236. Cara membaca: dua ratus tiga puluh enam.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengenali dan membaca bilangan yang tertera secara eksplisit pada gambar. Ini adalah prosedur langsung yang tidak memerlukan analisis atau strategi kompleks.. Bukti: Tuliskan lambang bilangan dan cara membaca bilangan yang terdapat pada gambar berikut.
- Dimensi pengetahuan `classify/factual`: Siswa perlu memahami sistem penamaan bilangan (nama bilangan) untuk angka yang diberikan, yang merupakan pengetahuan faktual tentang simbol dan cara membacanya.. Bukti: Tuliskan lambang bilangan dan cara membaca bilangan yang terdapat pada gambar berikut.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengidentifikasi angka dari gambar dan menuliskan nama bilangannya. Tidak ada langkah perantara atau integrasi konsep yang diperlukan.. Bukti: Tuliskan lambang bilangan dan cara membaca bilangan yang terdapat pada gambar berikut.; 236 meter

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal lambang bilangan cacah sampai 1.000 dan cara membacanya. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 3 SD karena membaca bilangan tiga angka adalah kompetensi dasar yang diharapkan sudah dikuasai. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 1, "factual": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4776`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta siswa untuk mengidentifikasi lambang bilangan dari representasi visual (angka pada papan) dan menuliskan cara membacanya. Ini adalah tugas pengenalan dan pembacaan bilangan yang bersifat langsung tanpa memerlukan strategi atau analisis kompleks.
- Dimensi pengetahuan `conceptual`: Siswa perlu memahami sistem penamaan bilangan cacah (ratusan, puluhan, satuan) untuk dapat membaca angka 236 dengan benar. Ini merupakan pengetahuan konseptual tentang struktur bilangan.
- Intended difficulty `Easy`: Soal ini sangat mendasar bagi kelas 3. Siswa hanya perlu membaca angka yang tertera dan mengubahnya ke dalam bentuk kata-kata. Tidak ada langkah kompleks, perencanaan, atau kendala yang harus dipecahkan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal nilai tempat bilangan cacah sampai 1.000 dan cara membacanya. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membaca bilangan tiga angka adalah materi dasar kelas 3. Tugas ini bersifat rutin dan tidak memerlukan perencanaan langkah. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 121/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000001 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.076552; conceptual=0.883988; procedural=0.039460; metacognitive=0.000000 | conceptual | 0.883988 | 0.312547 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.803696; Medium=0.192163; Hard=0.004141 | Easy | 0.803696 | 0.469055 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000001; H = 0.000001/ln(3) = 0.000001; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.883988; −Σp ln(p) = 0.433282; H = 0.433282/ln(4) = 0.312547; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.803696; −Σp ln(p) = 0.515310; H = 0.515310/ln(3) = 0.469055; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Bilangan dan Lambang Bilangan Cacah sampai 1.000
Tipe soal: multiple_choice
Stimulus: -
Soal: Tuliskan lambang bilangan dan cara membaca bilangan yang terdapat pada gambar berikut.
Pilihan: A. 236 dibaca dua ratus tiga puluh enam
B. 326 dibaca tiga ratus dua puluh enam
C. 263 dibaca dua ratus enam puluh tiga
D. 236 dibaca dua ratus tiga enam
Transkripsi visual: Gambar menunjukkan seorang anak laki-laki menunjuk ke arah papan penunjuk jalan di depan sekolah. Pada papan tersebut tertulis angka '236' dan kata 'meter'.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `0c970a6aff64277c753f7671`

Tuliskan bilangan yang terdiri atas 3 angka dan letakkan setiap angka sesuai nilai tempatnya. Ratusan 8, Puluhan 1, Satuan 2.

| Opsi | Isi |
|---|---|
| A | 182 |
| B | 821 |
| C | 128 |
| D | 812 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Bilangan dengan 8 ratusan, 1 puluhan, dan 2 satuan disusun menjadi 812.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menyebutkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `32603b8d8b4ab5d368a648a2f75cf660e29dee55c189e444197422670d99ad05`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2243 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2240 |
| 3 | success | valid / verified | knowing | factual | Easy | 2223 |

Run 1 — solusi: Bilangan dengan 8 ratusan, 1 puluhan, dan 2 satuan disusun menjadi 812.
- Domain kognitif `classify/knowing`: Siswa diminta untuk menyusun angka berdasarkan nilai tempat yang sudah ditentukan secara eksplisit. Ini adalah tugas langsung yang memerlukan pengenalan dan penerapan prosedur dasar nilai tempat.. Bukti: Ratusan 8, Puluhan 1, Satuan 2.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang sistem nilai tempat (ratusan, puluhan, satuan) yang merupakan konsep dasar dalam bilangan cacah.. Bukti: Ratusan 8, Puluhan 1, Satuan 2.
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu menempatkan angka-angka yang diberikan ke posisi yang sesuai (ratusan, puluhan, satuan). Tidak ada langkah tambahan atau integrasi yang diperlukan.. Bukti: Ratusan 8, Puluhan 1, Satuan 2.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang nilai tempat (ratusan, puluhan, satuan) untuk bilangan sampai 1.000. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, menyusun bilangan berdasarkan nilai tempat yang diberikan secara eksplisit adalah tugas rutin yang sangat mendasar. |

Run 2 — solusi: Bilangan dengan 8 ratusan, 1 puluhan, dan 2 satuan disusun menjadi 812.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali dan menempatkan angka sesuai dengan nilai tempat yang diberikan secara eksplisit dalam soal. Ini adalah prosedur langsung tanpa memerlukan analisis atau strategi kompleks.. Bukti: Ratusan 8, Puluhan 1, Satuan 2.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang definisi nilai tempat (ratusan, puluhan, satuan) sebagai konsep dasar dalam sistem bilangan.. Bukti: Ratusan 8, Puluhan 1, Satuan 2.
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu menyusun angka berdasarkan posisi nilai tempat yang sudah ditentukan secara eksplisit. Tidak ada langkah yang saling bergantung atau kendala yang perlu dipecahkan.. Bukti: Ratusan 8, Puluhan 1, Satuan 2.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar nilai tempat (ratusan, puluhan, satuan) untuk bilangan sampai 1.000. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, mengidentifikasi nilai tempat adalah materi dasar yang rutin. Soal tidak menuntut perencanaan atau integrasi konsep, sehingga tergolong mudah. |

Run 3 — solusi: Bilangan yang terdiri dari 8 ratusan, 1 puluhan, dan 2 satuan disusun menjadi 812.
- Domain kognitif `classify/knowing`: Siswa diminta untuk menyusun angka berdasarkan nilai tempat yang telah ditentukan secara eksplisit. Ini adalah prosedur langsung yang sudah dipelajari di kelas 3.. Bukti: Ratusan 8, Puluhan 1, Satuan 2.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang sistem nilai tempat (ratusan, puluhan, satuan) dalam bilangan cacah.. Bukti: Ratusan 8, Puluhan 1, Satuan 2.
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu menempatkan angka sesuai label nilai tempat yang diberikan tanpa langkah tambahan atau integrasi yang kompleks.. Bukti: Ratusan 8, Puluhan 1, Satuan 2.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang nilai tempat (ratusan, puluhan, satuan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, konsep nilai tempat sampai 1.000 adalah materi dasar yang rutin. Soal ini tidak memerlukan perencanaan atau pemecahan masalah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 2, "factual": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3572`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu mengenali dan menempatkan angka sesuai dengan nilai tempat yang diberikan secara eksplisit. Ini adalah prosedur langsung yang memerlukan pengenalan dasar.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman tentang sistem nilai tempat (ratusan, puluhan, satuan) yang merupakan konsep dasar dalam bilangan cacah.
- Intended difficulty `Easy`: Soal ini sangat langsung. Siswa hanya perlu menyusun angka berdasarkan posisi nilai tempat yang sudah ditentukan secara eksplisit. Tidak ada langkah yang saling bergantung atau kendala yang perlu dipecahkan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar nilai tempat (ratusan, puluhan, satuan) untuk bilangan sampai 1.000. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, mengidentifikasi dan menyusun bilangan berdasarkan nilai tempat adalah materi dasar yang rutin. Soal tidak menuntut perencanaan atau integrasi konsep. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 79/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.880028; applying=0.119972; reasoning=0.000000 | knowing | 0.880028 | 0.333938 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.557330; conceptual=0.422618; procedural=0.020053; metacognitive=0.000000 | factual | 0.557330 | 0.554142 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.905591; Medium=0.092145; Hard=0.002264 | Easy | 0.905591 | 0.294284 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.880028; −Σp ln(p) = 0.366869; H = 0.366869/ln(3) = 0.333938; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.557330; −Σp ln(p) = 0.768203; H = 0.768203/ln(4) = 0.554142; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.905591; −Σp ln(p) = 0.323304; H = 0.323304/ln(3) = 0.294284; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Nilai Tempat Bilangan Cacah sampai 1.000
Tipe soal: multiple_choice
Stimulus: -
Soal: Tuliskan bilangan yang terdiri atas 3 angka dan letakkan setiap angka sesuai nilai tempatnya. Ratusan 8, Puluhan 1, Satuan 2.
Pilihan: A. 182
B. 821
C. 128
D. 812
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "conceptual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `a33c3cd30e2555b8f613b155`

Lengkapi tabel berikut dengan bilangan yang sesuai dengan nilai tempatnya! Lambang Bilangan 328.

| Opsi | Isi |
|---|---|
| A | 2 ratusan, 3 puluhan, 8 satuan |
| B | 3 ratusan, 8 puluhan, 2 satuan |
| C | 3 ratusan, 2 puluhan, 8 satuan |
| D | 8 ratusan, 2 puluhan, 3 satuan |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Bilangan 328 terdiri dari angka 3 di posisi ratusan (300), 2 di posisi puluhan (20), dan 8 di posisi satuan (8). Jadi, 328 = 3 ratusan + 2 puluhan + 8 satuan.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `34deeabfcb4406cfed944e0957691395ccde5407a968aa9496a617b5340159f2`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2338 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2332 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2311 |

Run 1 — solusi: Bilangan 328 terdiri dari angka 3 di posisi ratusan (300), 2 di posisi puluhan (20), dan 8 di posisi satuan (8). Jadi, 328 = 3 ratusan + 2 puluhan + 8 satuan.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi nilai tempat dari angka-angka penyusun bilangan 328. Ini adalah tugas pengenalan langsung terhadap konsep nilai tempat yang sudah dipelajari di kelas 3.. Bukti: Lengkapi tabel berikut dengan bilangan yang sesuai dengan nilai tempatnya! Lambang Bilangan 328.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang konsep dasar nilai tempat (ratusan, puluhan, satuan) dalam bilangan cacah.. Bukti: Lengkapi tabel berikut dengan bilangan yang sesuai dengan nilai tempatnya! Lambang Bilangan 328.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung (straightforward) dan rutin bagi siswa kelas 3. Tidak ada langkah yang saling bergantung atau kendala yang harus diintegrasikan. Siswa hanya perlu memetakan digit ke posisi nilai tempatnya.. Bukti: Lengkapi tabel berikut dengan bilangan yang sesuai dengan nilai tempatnya! Lambang Bilangan 328.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang nilai tempat (ratusan, puluhan, satuan) untuk bilangan sampai 1.000. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi nilai tempat adalah kurikulum standar kelas 3. Soal ini tidak memerlukan perencanaan atau integrasi langkah, sehingga dikategorikan mudah. |

Run 2 — solusi: Bilangan 328 terdiri dari angka 3 di posisi ratusan (300), angka 2 di posisi puluhan (20), dan angka 8 di posisi satuan (8). Jadi, bentuk nilai tempatnya adalah 3 ratusan, 2 puluhan, dan 8 satuan.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi nilai tempat dari angka-angka penyusun bilangan 328. Ini adalah prosedur langsung yang sudah dipelajari di kelas 3, yaitu membedakan nilai ratusan, puluhan, dan satuan.. Bukti: Lengkapi tabel berikut dengan bilangan yang sesuai dengan nilai tempatnya! Lambang Bilangan 328.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang konsep dasar nilai tempat (place value) dalam sistem bilangan desimal.. Bukti: Lengkapi tabel berikut dengan bilangan yang sesuai dengan nilai tempatnya! Lambang Bilangan 328.
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin bagi siswa kelas 3. Tidak ada langkah yang saling bergantung atau kendala yang harus dipecahkan; siswa hanya perlu mengenali posisi angka dalam bilangan tiga digit.. Bukti: Lengkapi tabel berikut dengan bilangan yang sesuai dengan nilai tempatnya! Lambang Bilangan 328.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan tiga angka (ratusan, puluhan, satuan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi nilai tempat adalah kurikulum standar kelas 3. Soal ini tidak memerlukan perencanaan atau integrasi langkah, sehingga dikategorikan mudah. |

Run 3 — solusi: Bilangan 328 terdiri dari angka 3 di posisi ratusan (300), angka 2 di posisi puluhan (20), dan angka 8 di posisi satuan (8). Jadi, 328 = 3 ratusan + 2 puluhan + 8 satuan.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi nilai tempat dari angka-angka penyusun bilangan 328. Ini adalah prosedur langsung untuk mengenali representasi nilai tempat bilangan tiga angka.. Bukti: Lengkapi tabel berikut dengan bilangan yang sesuai dengan nilai tempatnya! Lambang Bilangan 328.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep dasar nilai tempat (ratusan, puluhan, satuan) yang merupakan pengetahuan konseptual dasar dalam matematika kelas 3.. Bukti: nilai tempatnya! Lambang Bilangan 328.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu memetakan digit ke posisi nilai tempatnya tanpa ada langkah tambahan atau kendala yang harus dipecahkan.. Bukti: Lengkapi tabel berikut dengan bilangan yang sesuai dengan nilai tempatnya! Lambang Bilangan 328.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan cacah sampai 1.000. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi nilai tempat adalah standar kurikulum kelas 3. Soal ini tidak memerlukan perencanaan atau integrasi langkah, sehingga dikategorikan mudah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 96/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.650976; applying=0.349024; reasoning=0.000000 | knowing | 0.650976 | 0.588780 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.314460; conceptual=0.658173; procedural=0.027367; metacognitive=0.000000 | conceptual | 0.658173 | 0.532053 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.882652; Medium=0.115130; Hard=0.002218 | Easy | 0.882652 | 0.339162 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.650976; −Σp ln(p) = 0.646841; H = 0.646841/ln(3) = 0.588780; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.658173; −Σp ln(p) = 0.737582; H = 0.737582/ln(4) = 0.532053; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.882652; −Σp ln(p) = 0.372608; H = 0.372608/ln(3) = 0.339162; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Nilai Tempat Bilangan Cacah sampai 1.000
Tipe soal: multiple_choice
Stimulus: -
Soal: Lengkapi tabel berikut dengan bilangan yang sesuai dengan nilai tempatnya! Lambang Bilangan 328.
Pilihan: A. 2 ratusan, 3 puluhan, 8 satuan
B. 3 ratusan, 8 puluhan, 2 satuan
C. 3 ratusan, 2 puluhan, 8 satuan
D. 8 ratusan, 2 puluhan, 3 satuan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `076b46a03e171eb8019de109`

Urutkan bilangan 537, 590, 518, dan 601 dari yang terkecil ke terbesar.

| Opsi | Isi |
|---|---|
| A | 518, 537, 590, 601 |
| B | 537, 518, 590, 601 |
| C | 601, 590, 537, 518 |
| D | 518, 590, 537, 601 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Bandingkan nilai ratusan: 518, 537, 590 (ratusan 5) dan 601 (ratusan 6). Karena 601 memiliki ratusan terbesar, ia diletakkan di akhir. Untuk bilangan dengan ratusan 5, bandingkan puluhannya: 1 (518) < 3 (537) < 9 (590). Urutan dari terkecil: 518, 537, 590, 601.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b20ee73fa1747d1babc46791be19a232d022d2d9e74fe5de3a47753e5fd1c1de`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2358 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2987 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2476 |

Run 1 — solusi: Bandingkan angka ratusan: 518, 537, 590 memiliki ratusan 5, sedangkan 601 memiliki ratusan 6 (terbesar). Bandingkan angka puluhan untuk bilangan ratusan 5: 1 (518) < 3 (537) < 9 (590). Urutan dari terkecil: 518, 537, 590, 601.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur membandingkan nilai tempat (ratusan, puluhan) untuk mengurutkan bilangan. Ini adalah prosedur rutin yang dipelajari di kelas 3.. Bukti: Urutkan bilangan 537, 590, 518, dan 601 dari yang terkecil ke terbesar.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau metode perbandingan nilai tempat untuk mengurutkan bilangan cacah.. Bukti: Urutkan bilangan 537, 590, 518, dan 601
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu membandingkan nilai tempat ratusan dan puluhan dari empat bilangan yang diberikan. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Urutkan bilangan 537, 590, 518, dan 601 dari yang terkecil ke terbesar.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan cacah sampai 1.000. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan empat bilangan tiga angka adalah tugas standar kelas 3 yang dapat diselesaikan dengan prosedur perbandingan nilai tempat yang familiar. |

Run 2 — solusi: Bandingkan nilai tempat ratusan: 518, 537, 590 (ratusan 5) dan 601 (ratusan 6). Untuk yang ratusannya sama, bandingkan puluhannya: 10 < 30 < 90. Urutan: 518, 537, 590, 601.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan prosedur rutin membandingkan dan mengurutkan bilangan berdasarkan nilai tempat, yang merupakan keterampilan dasar.. Bukti: Urutkan bilangan 537, 590, 518, dan 601 dari yang terkecil ke terbesar.
- Dimensi pengetahuan `classify/conceptual`: Tugas ini menguji pemahaman konseptual tentang nilai tempat (ratusan, puluhan, satuan) untuk menentukan besaran bilangan.. Bukti: Urutkan bilangan 537, 590, 518, dan 601
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang jelas dan langsung, sesuai dengan ekspektasi kemampuan siswa kelas 3.. Bukti: Urutkan bilangan 537, 590, 518, dan 601 dari yang terkecil ke terbesar.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan cacah sampai 1.000 (ratusan, puluhan, satuan). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Membandingkan bilangan tiga angka adalah materi standar kelas 3. Tidak ada kendala yang berinteraksi atau kebutuhan perencanaan kompleks. |

Run 3 — solusi: Bandingkan nilai ratusan: 518, 537, 590 memiliki ratusan 5, sedangkan 601 memiliki ratusan 6 (terbesar). Bandingkan nilai puluhan untuk bilangan ratusan 5: 1 (518) < 3 (537) < 9 (590). Urutan terkecil ke terbesar: 518, 537, 590, 601.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur perbandingan nilai tempat (ratusan, puluhan) untuk mengurutkan bilangan. Ini adalah penerapan konsep nilai tempat pada konteks rutin.. Bukti: Urutkan bilangan 537, 590, 518, dan 601 dari yang terkecil ke terbesar.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan nilai tempat (ratusan, puluhan, satuan) dalam mengurutkan bilangan cacah.. Bukti: Urutkan bilangan 537, 590, 518, dan 601 dari yang terkecil ke terbesar.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 3. Prosedur perbandingan nilai tempat sudah dipelajari dan jalur penyelesaiannya sangat jelas tanpa memerlukan perencanaan kompleks.. Bukti: Urutkan bilangan 537, 590, 518, dan 601 dari yang terkecil ke terbesar.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan cacah sampai 1.000. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan empat bilangan tiga angka adalah tugas standar kelas 3 yang menggunakan prosedur perbandingan nilai tempat yang sudah familiar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4136`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan prosedur rutin membandingkan nilai tempat (ratusan dan puluhan) untuk mengurutkan bilangan. Ini adalah penerapan konsep dasar yang sudah dipelajari.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang nilai tempat (ratusan, puluhan) sebagai dasar untuk menentukan urutan besaran bilangan.
- Intended difficulty `Easy`: Soal ini bersifat rutin dengan jalur penyelesaian yang jelas. Siswa hanya perlu membandingkan nilai tempat secara sistematis. Tidak ada kendala yang berinteraksi atau kebutuhan strategi non-rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan cacah sampai 1.000. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan empat bilangan tiga angka adalah tugas standar kelas 3 yang menggunakan prosedur perbandingan nilai tempat yang sudah familiar. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 116/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.543308; applying=0.456692; reasoning=0.000000 | knowing | 0.543308 | 0.627511 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.334296; conceptual=0.636073; procedural=0.029631; metacognitive=0.000000 | conceptual | 0.636073 | 0.547035 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.890689; Medium=0.106618; Hard=0.002693 | Easy | 0.890689 | 0.325599 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.543308; −Σp ln(p) = 0.689391; H = 0.689391/ln(3) = 0.627511; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.636073; −Σp ln(p) = 0.758352; H = 0.758352/ln(4) = 0.547035; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.890689; −Σp ln(p) = 0.357707; H = 0.357707/ln(3) = 0.325599; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Membandingkan dan Mengurutkan Bilangan Cacah sampai 1.000
Tipe soal: multiple_choice
Stimulus: -
Soal: Urutkan bilangan 537, 590, 518, dan 601 dari yang terkecil ke terbesar.
Pilihan: A. 518, 537, 590, 601
B. 537, 518, 590, 601
C. 601, 590, 537, 518
D. 518, 590, 537, 601
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `95b3dddf90876e587a0dc101`

Isilah titik-titik dengan tanda >, <, atau =!<br><br>705 ..... 705

| Opsi | Isi |
|---|---|
| A | 700 = 705 |
| B | 705 = 705 |
| C | 705 < 705 |
| D | 705 > 705 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Bilangan 705 sama dengan 705, sehingga tanda yang tepat adalah =.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4b7680ce7bdbd942bc8b385f02d1383a261a7373695af9e9670808eae5f9b297`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2228 |
| 2 | success | valid / verified | knowing | factual | Easy | 2223 |
| 3 | success | valid / verified | knowing | factual | Easy | 2225 |

Run 1 — solusi: Bilangan 705 sama dengan 705, sehingga tanda yang tepat adalah =.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali nilai tempat dan membandingkan dua bilangan yang identik untuk menentukan relasi kesamaan. Ini adalah tugas pengenalan langsung.. Bukti: Isilah titik-titik dengan tanda >, <, atau =!; 705 ..... 705
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang simbol relasi matematika (=, <, >) dan konsep kesamaan bilangan.. Bukti: 705 ..... 705
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar bagi siswa kelas 3. Tidak ada langkah yang saling bergantung atau strategi kompleks yang diperlukan. Siswa hanya perlu melakukan perbandingan langsung antara dua angka yang sama.. Bukti: 705 ..... 705

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan cacah sampai 1.000 dan simbol perbandingan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Membandingkan dua bilangan yang sama persis adalah tugas rutin yang sangat sederhana untuk tingkat kelas 3. |

Run 2 — solusi: Kedua bilangan adalah 705. Karena 705 sama dengan 705, maka tanda yang tepat adalah =.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali nilai tempat dan membandingkan dua bilangan yang identik untuk menentukan relasi kesamaan. Ini adalah prosedur langsung tanpa langkah tambahan.. Bukti: 705 ..... 705
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual mengenai simbol relasi matematika (=, <, >) dan perbandingan nilai bilangan cacah.. Bukti: 705 ..... 705
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar bagi kelas 3. Siswa hanya perlu membandingkan dua angka yang sama persis. Tidak ada langkah perantara atau kendala yang harus dipecahkan.. Bukti: 705 ..... 705

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan cacah sampai 1.000 dan simbol perbandingan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Membandingkan dua bilangan yang sama adalah tugas rutin yang sangat sederhana untuk siswa kelas 3. |

Run 3 — solusi: Bilangan 705 sama dengan 705, sehingga tanda yang tepat adalah =.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengenali hubungan kesamaan antara dua bilangan yang identik. Ini adalah tugas pengenalan langsung terhadap simbol relasi dasar.. Bukti: Isilah titik-titik dengan tanda >, <, atau =!; 705 ..... 705
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual mengenai simbol perbandingan matematika (=, <, >) dan konsep kesamaan bilangan.. Bukti: 705 ..... 705
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu membandingkan dua angka yang identik. Tidak ada langkah tambahan atau kompleksitas yang terlibat.. Bukti: 705 ..... 705

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan cacah sampai 1.000 dan arti simbol perbandingan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Membandingkan dua bilangan yang sama persis adalah tugas dasar yang sesuai untuk kelas 3, tidak memerlukan perencanaan atau integrasi langkah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 93/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.879887; applying=0.120113; reasoning=0.000000 | knowing | 0.879887 | 0.334194 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.396662; conceptual=0.569934; procedural=0.033405; metacognitive=0.000000 | conceptual | 0.569934 | 0.577629 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.903009; Medium=0.095230; Hard=0.001761 | Easy | 0.903009 | 0.297853 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.879887; −Σp ln(p) = 0.367150; H = 0.367150/ln(3) = 0.334194; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.569934; −Σp ln(p) = 0.800764; H = 0.800764/ln(4) = 0.577629; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.903009; −Σp ln(p) = 0.327225; H = 0.327225/ln(3) = 0.297853; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Membandingkan dan Mengurutkan Bilangan Cacah sampai 1.000
Tipe soal: multiple_choice
Stimulus: -
Soal: Isilah titik-titik dengan tanda >, <, atau =!

705 ..... 705
Pilihan: A. 700 = 705
B. 705 = 705
C. 705 < 705
D. 705 > 705
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `53e94d84aab7a547c9b05a51`

Andi membeli beberapa barang untuk dibagikan ke temannya. Andi membeli buku sebanyak 25 buah dan membeli pensil sebanyak 36 buah.<br><br>Berapakah jumlah barang yang dibeli Andi?

| Opsi | Isi |
|---|---|
| A | 51 buah |
| B | 11 buah |
| C | 61 buah |
| D | 60 buah |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: 25 + 36 = 61
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `20969c5ffb4a8968c2a7332d415ae970356d38e61ee99df868b1e789a2397e2c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2259 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2270 |
| 3 | success | valid / verified | applying | procedural | Easy | 2334 |

Run 1 — solusi: Jumlah barang = 25 + 36 = 61.
- Domain kognitif `classify/knowing`: Siswa diminta untuk melakukan operasi penjumlahan bilangan cacah dua digit yang merupakan prosedur standar dan langsung untuk kelas 3.. Bukti: Andi membeli buku sebanyak 25 buah dan membeli pensil sebanyak 36 buah.; Berapakah jumlah barang yang dibeli Andi?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritma penjumlahan bersusun atau penjumlahan bilangan cacah, yang merupakan pengetahuan prosedural.. Bukti: Berapakah jumlah barang yang dibeli Andi?
- Intended difficulty `classify/Easy`: Soal ini adalah soal penjumlahan dua bilangan dua digit dengan teknik menyimpan (5+6=11). Ini adalah materi standar kelas 3 yang rutin.. Bukti: Andi membeli buku sebanyak 25 buah dan membeli pensil sebanyak 36 buah.; Berapakah jumlah barang yang dibeli Andi?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah sampai 100 dengan teknik menyimpan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan dua bilangan dua digit dengan teknik menyimpan adalah kompetensi dasar kelas 3 yang diajarkan secara rutin. |

Run 2 — solusi: Jumlah barang = 25 + 36 = 61.
- Domain kognitif `classify/knowing`: Siswa diminta untuk melakukan operasi penjumlahan bilangan dua angka yang merupakan prosedur standar dan rutin pada kelas 3.. Bukti: Andi membeli buku sebanyak 25 buah dan membeli pensil sebanyak 36 buah.; Berapakah jumlah barang yang dibeli Andi?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritma penjumlahan bersusun atau penjumlahan bilangan cacah, yang merupakan pengetahuan prosedural.. Bukti: Berapakah jumlah barang yang dibeli Andi?
- Intended difficulty `classify/Easy`: Soal ini adalah soal penjumlahan dua bilangan dua angka dengan teknik menyimpan yang sederhana. Jalur penyelesaian sangat jelas dan langsung, tidak memerlukan perencanaan kompleks atau integrasi kendala.. Bukti: 25 buah; 36 buah; Berapakah jumlah barang yang dibeli Andi?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah sampai 100 dengan teknik menyimpan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan bilangan dua angka adalah materi dasar kelas 3. Soal ini tidak memiliki jebakan atau tuntutan kognitif tambahan selain melakukan operasi hitung tersebut. |

Run 3 — solusi: 25 + 36 = 61. Penjumlahan dilakukan dengan menjumlahkan satuan (5+6=11, tulis 1 simpan 1) dan puluhan (2+3+1=6), sehingga totalnya 61.
- Domain kognitif `classify/applying`: Siswa diminta untuk melakukan operasi penjumlahan bilangan dua angka yang memerlukan teknik menyimpan. Ini adalah prosedur standar yang diajarkan di kelas 3, sehingga termasuk dalam domain applying.. Bukti: Berapakah jumlah barang yang dibeli Andi?; Andi membeli buku sebanyak 25 buah dan membeli pensil sebanyak 36 buah.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritma penjumlahan bersusun dengan teknik menyimpan, yang merupakan bagian dari pengetahuan prosedural.. Bukti: 25 buah dan membeli pensil sebanyak 36 buah; Berapakah jumlah barang
- Intended difficulty `classify/Easy`: Soal ini adalah soal penjumlahan dua bilangan dua angka dengan teknik menyimpan. Bagi siswa kelas 3, ini adalah prosedur rutin yang familiar. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merancang strategi non-rutin.. Bukti: 25 buah dan membeli pensil sebanyak 36 buah; Berapakah jumlah barang yang dibeli Andi?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah sampai 100 dengan teknik menyimpan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan dua bilangan dua angka dengan teknik menyimpan adalah materi dasar kelas 3 yang sudah rutin dipelajari. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4465`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta siswa melakukan operasi penjumlahan dua bilangan dua digit dengan teknik menyimpan. Ini adalah prosedur standar yang langsung dan rutin bagi siswa kelas 3.
- Dimensi pengetahuan `procedural`: Siswa perlu menerapkan algoritma penjumlahan bersusun dengan teknik menyimpan untuk menyelesaikan masalah ini.
- Intended difficulty `Easy`: Soal ini adalah soal penjumlahan dua bilangan dua digit dengan teknik menyimpan yang sederhana. Jalur penyelesaian sangat jelas dan langsung, tidak memerlukan perencanaan kompleks atau integrasi kendala.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah sampai 100 dengan teknik menyimpan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan dua bilangan dua digit dengan teknik menyimpan adalah materi dasar kelas 3 yang rutin dan langsung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 83/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000006 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.232041; conceptual=0.752967; procedural=0.014992; metacognitive=0.000000 | conceptual | 0.752967 | 0.444052 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.871820; Medium=0.124954; Hard=0.003226 | Easy | 0.871820 | 0.362255 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000007; H = 0.000007/ln(3) = 0.000006; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.752967; −Σp ln(p) = 0.615587; H = 0.615587/ln(4) = 0.444052; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.871820; −Σp ln(p) = 0.397977; H = 0.397977/ln(3) = 0.362255; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Penjumlahan Bilangan Cacah sampai 100
Tipe soal: multiple_choice
Stimulus: -
Soal: Andi membeli beberapa barang untuk dibagikan ke temannya. Andi membeli buku sebanyak 25 buah dan membeli pensil sebanyak 36 buah.

Berapakah jumlah barang yang dibeli Andi?
Pilihan: A. 51 buah
B. 11 buah
C. 61 buah
D. 60 buah
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `a5652daac47c0bfd276b6692`

70 + 13 = ......

| Opsi | Isi |
|---|---|
| A | 93 |
| B | 80 |
| C | 73 |
| D | 83 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: 70 + 13 = 70 + (10 + 3) = (70 + 10) + 3 = 80 + 3 = 83.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f8825d4fa4af1906341fca9b6612b096b231ce992c7db09d93a40ad26f3d6f02`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2198 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2196 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2215 |

Run 1 — solusi: 70 + 13 = 70 + (10 + 3) = (70 + 10) + 3 = 80 + 3 = 83.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi penjumlahan bilangan dua angka yang merupakan prosedur standar dan langsung.. Bukti: 70 + 13 = ......
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman algoritma penjumlahan dasar (prosedural) untuk bilangan cacah.. Bukti: 70 + 13 = ......
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi penjumlahan dasar yang familiar bagi siswa kelas 3. Jalur penyelesaian sangat jelas dan tidak memerlukan perencanaan atau integrasi langkah yang kompleks.. Bukti: 70 + 13 = ......

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah sampai 100 dengan teknik tanpa menyimpan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan 70+13 adalah materi dasar kelas 3 yang rutin dilakukan siswa. |

Run 2 — solusi: 70 + 13 = 70 + (10 + 3) = (70 + 10) + 3 = 80 + 3 = 83.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi penjumlahan bilangan dua angka yang merupakan prosedur standar dan langsung bagi kelas 3.. Bukti: 70 + 13 = ......
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dasar tentang penjumlahan bilangan cacah.. Bukti: 70 + 13 = ......
- Intended difficulty `classify/Easy`: Soal ini adalah operasi penjumlahan langsung tanpa konteks cerita atau kendala tambahan. Siswa kelas 3 diharapkan sudah menguasai penjumlahan bilangan puluhan dengan satuan.. Bukti: 70 + 13 = ......

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah sampai 100. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi penjumlahan 70+13 adalah materi dasar kelas 3 yang bersifat rutin dan langsung. |

Run 3 — solusi: 70 + 13 = 70 + (10 + 3) = (70 + 10) + 3 = 80 + 3 = 83.
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan operasi penjumlahan bilangan cacah dua angka secara langsung. Ini adalah prosedur rutin yang sudah dipelajari di kelas 3.. Bukti: 70 + 13 = ......
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma penjumlahan bilangan cacah, yang merupakan bagian dari pengetahuan prosedural.. Bukti: 70 + 13 = ......
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi penjumlahan dasar yang familiar bagi siswa kelas 3. Tidak ada langkah kompleks atau kendala yang harus diintegrasikan.. Bukti: 70 + 13 = ......

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah sampai 100. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan dua bilangan dua angka adalah materi dasar kelas 3 yang diselesaikan dengan prosedur standar tanpa memerlukan penalaran tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 60/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999709; applying=0.000291; reasoning=0.000000 | knowing | 0.999709 | 0.002418 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.877368; conceptual=0.103577; procedural=0.019054; metacognitive=0.000000 | factual | 0.877368 | 0.306647 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.922444; Medium=0.075678; Hard=0.001877 | Easy | 0.922444 | 0.256323 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999709; −Σp ln(p) = 0.002656; H = 0.002656/ln(3) = 0.002418; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.877368; −Σp ln(p) = 0.425104; H = 0.425104/ln(4) = 0.306647; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.922444; −Σp ln(p) = 0.281599; H = 0.281599/ln(3) = 0.256323; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Penjumlahan Bilangan Cacah sampai 100
Tipe soal: multiple_choice
Stimulus: -
Soal: 70 + 13 = ......
Pilihan: A. 93
B. 80
C. 73
D. 83
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 9. Soal `13af70c61db0c35f9ece2f68`

Bia memiliki 19 stiker mobil. Aldo memiliki 8 stiker robot.<br><br>Berapa selisih stiker milik Bia dan Aldo?

| Opsi | Isi |
|---|---|
| A | 27 stiker |
| B | 11 stiker |
| C | 9 stiker |
| D | 12 stiker |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: 19 - 8 = 11
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6e926c759b9ca1e005e4f0cf7f1b7fedabe8378db4d9e4180be4dc2528cd0bae`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 3022 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2266 |
| 3 | success | valid / verified | applying | procedural | Easy | 2214 |

Run 1 — solusi: 19 - 8 = 11
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi bahwa kata kunci 'selisih' menuntut operasi pengurangan dan menerapkan prosedur pengurangan dasar.. Bukti: Berapa selisih stiker milik Bia dan Aldo?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penerapan algoritme pengurangan bilangan cacah untuk menyelesaikan masalah selisih.. Bukti: 19 stiker mobil; 8 stiker robot
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung konsep pengurangan untuk mencari selisih. Prosedur pengurangan 19-8 adalah rutin bagi siswa kelas 3, dengan beban kognitif rendah dan tanpa kendala yang saling berinteraksi.. Bukti: Bia memiliki 19 stiker mobil. Aldo memiliki 8 stiker robot.; Berapa selisih stiker milik Bia dan Aldo?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengurangan bilangan cacah sampai 20 |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pengurangan dua bilangan di bawah 20 adalah materi dasar kelas 3 yang sudah familiar. |

Run 2 — solusi: Selisih stiker Bia dan Aldo adalah 19 - 8 = 11 stiker.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk mengidentifikasi operasi pengurangan yang diperlukan untuk mencari selisih antara dua jumlah yang diketahui. Ini adalah penerapan langsung dari konsep pengurangan dasar.. Bukti: Bia memiliki 19 stiker mobil. Aldo memiliki 8 stiker robot.; Berapa selisih stiker milik Bia dan Aldo?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep 'selisih' sebagai hubungan antara dua kuantitas yang memerlukan operasi pengurangan.. Bukti: Berapa selisih stiker milik Bia dan Aldo?
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah satu langkah yang sangat rutin. Siswa hanya perlu melakukan pengurangan 19 - 8. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: Bia memiliki 19 stiker mobil. Aldo memiliki 8 stiker robot.; Berapa selisih stiker milik Bia dan Aldo?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan bilangan cacah sampai 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, pengurangan bilangan di bawah 20 adalah keterampilan dasar yang sudah dikuasai. Soal ini tidak menuntut perencanaan atau integrasi lebih lanjut. |

Run 3 — solusi: Selisih stiker Bia dan Aldo adalah 19 - 8 = 11.
- Domain kognitif `classify/applying`: Soal meminta siswa melakukan operasi pengurangan dasar untuk mencari selisih dua bilangan. Ini adalah prosedur rutin yang langsung, sehingga masuk dalam domain applying.. Bukti: Berapa selisih stiker milik Bia dan Aldo?
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami konsep selisih sebagai operasi pengurangan dan menerapkan algoritma pengurangan bilangan cacah.. Bukti: 19 stiker mobil; 8 stiker robot; Berapa selisih
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mengidentifikasi dua angka dan melakukan satu operasi pengurangan. Tidak ada langkah tambahan atau kendala yang perlu diintegrasikan.. Bukti: 19 stiker mobil; 8 stiker robot; Berapa selisih

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan bilangan cacah sampai 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, pengurangan bilangan di bawah 20 adalah materi dasar yang sudah dikuasai. Soal tidak memiliki jebakan atau kompleksitas tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3483`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan prosedur pengurangan dasar untuk menyelesaikan masalah selisih yang rutin.
- Dimensi pengetahuan `procedural`: Soal menuntut penggunaan algoritme pengurangan bilangan cacah yang merupakan prosedur standar.
- Intended difficulty `Easy`: Soal ini adalah masalah satu langkah yang sangat rutin. Siswa hanya perlu mengidentifikasi operasi pengurangan dari kata kunci 'selisih' dan menghitung hasilnya. Tidak ada kendala yang berinteraksi atau kebutuhan perencanaan strategi yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengurangan bilangan cacah sampai 20 |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pengurangan dua bilangan di bawah 20 adalah materi dasar kelas 3 yang sudah familiar dan tidak menuntut integrasi langkah. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 76/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.006971; applying=0.993029; reasoning=0.000000 | applying | 0.993029 | 0.037833 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.764947; conceptual=0.170236; procedural=0.064818; metacognitive=0.000000 | factual | 0.764947 | 0.493209 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.842131; Medium=0.153894; Hard=0.003974 | Easy | 0.842131 | 0.413864 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.993029; −Σp ln(p) = 0.041564; H = 0.041564/ln(3) = 0.037833; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.764947; −Σp ln(p) = 0.683733; H = 0.683733/ln(4) = 0.493209; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.842131; −Σp ln(p) = 0.454676; H = 0.454676/ln(3) = 0.413864; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Pengurangan Bilangan Cacah sampai 100
Tipe soal: multiple_choice
Stimulus: -
Soal: Bia memiliki 19 stiker mobil. Aldo memiliki 8 stiker robot.

Berapa selisih stiker milik Bia dan Aldo?
Pilihan: A. 27 stiker
B. 11 stiker
C. 9 stiker
D. 12 stiker
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `618b8db11b04736854c11a46`

Pak Doni memiliki kolam ikan yang diisi dengan 23 ekor ikan gurami dan 42 ekor ikan nila.<br><br>Berapa selisih jumlah ikan gurami dan ikan nila milik Pak Doni?

| Opsi | Isi |
|---|---|
| A | 21 ekor |
| B | 65 ekor |
| C | 19 ekor |
| D | 20 ekor |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Selisih ikan = 42 - 23 = 19 ekor.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `804a393f15ddb9e01174b5cd0848bffc65bcef2184a8e5a232b53aaabf1a28cc`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2249 |
| 2 | success | valid / verified | applying | procedural | Easy | 2270 |
| 3 | success | valid / verified | applying | procedural | Easy | 2304 |

Run 1 — solusi: Selisih ikan = 42 - 23 = 19 ekor.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pengurangan bilangan cacah (pengurangan dengan meminjam) untuk menyelesaikan masalah selisih yang rutin.. Bukti: Berapa selisih jumlah ikan gurami dan ikan nila milik Pak Doni?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang algoritma pengurangan bilangan cacah dengan teknik meminjam.. Bukti: 23 ekor ikan gurami dan 42 ekor ikan nila; Berapa selisih
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin satu langkah yang familiar bagi siswa kelas 3. Prosedur pengurangan dengan meminjam adalah standar kurikulum kelas 3. Tidak ada kendala yang berinteraksi atau kebutuhan strategi non-rutin.. Bukti: 23 ekor ikan gurami dan 42 ekor ikan nila; Berapa selisih

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengurangan bilangan cacah sampai 100 dengan teknik meminjam. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pengurangan dua bilangan dua digit dengan meminjam adalah kompetensi dasar kelas 3. Soal disajikan secara langsung tanpa jebakan atau kompleksitas tambahan. |

Run 2 — solusi: Selisih ikan adalah 42 - 23 = 19 ekor.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan prosedur pengurangan bilangan cacah (pengurangan dengan teknik meminjam) untuk menyelesaikan masalah selisih yang rutin.. Bukti: Berapa selisih jumlah ikan gurami dan ikan nila milik Pak Doni?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang algoritma pengurangan bilangan cacah dengan teknik meminjam.. Bukti: 23 ekor ikan gurami dan 42 ekor ikan nila; Berapa selisih
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena merupakan penerapan langsung dari konsep pengurangan bilangan cacah dua digit dengan teknik meminjam yang merupakan materi standar kelas 3. Jalur penyelesaian sangat jelas (langsung melakukan pengurangan 42 - 23) tanpa memerlukan perencanaan kompleks atau integrasi kendala.. Bukti: 23 ekor ikan gurami dan 42 ekor ikan nila; Berapa selisih

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengurangan bilangan cacah dua digit dengan teknik meminjam. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pengurangan bilangan dua digit dengan meminjam adalah kompetensi dasar kelas 3. Soal tidak memiliki jebakan atau kompleksitas tambahan. |

Run 3 — solusi: Selisih ikan nila dan gurami adalah 42 - 23. Karena 2 < 3, lakukan teknik meminjam: (30 + 12) - (20 + 3) = (30 - 20) + (12 - 3) = 10 + 9 = 19.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pengurangan bilangan cacah dua angka dengan teknik meminjam untuk mencari selisih. Ini adalah penerapan konsep pengurangan pada konteks rutin.. Bukti: Berapa selisih jumlah ikan gurami dan ikan nila milik Pak Doni?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma pengurangan (teknik meminjam) untuk menyelesaikan masalah selisih dua bilangan.. Bukti: 23 ekor ikan gurami dan 42 ekor ikan nila; Berapa selisih
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena merupakan prosedur pengurangan dua angka yang standar bagi kelas 3. Jalur penyelesaiannya langsung (pengurangan selisih) dan tidak memerlukan perencanaan kompleks atau integrasi kendala.. Bukti: 23 ekor ikan gurami dan 42 ekor ikan nila; Berapa selisih

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengurangan bilangan cacah dua angka dengan teknik meminjam. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pengurangan dengan meminjam adalah materi standar kelas 3. Soal tidak memiliki jebakan atau tuntutan penalaran tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 86/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000066; applying=0.999934; reasoning=0.000000 | applying | 0.999934 | 0.000636 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.403513; conceptual=0.558779; procedural=0.037709; metacognitive=0.000000 | conceptual | 0.558779 | 0.587914 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.860042; Medium=0.135623; Hard=0.004335 | Easy | 0.860042 | 0.386140 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999934; −Σp ln(p) = 0.000699; H = 0.000699/ln(3) = 0.000636; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.558779; −Σp ln(p) = 0.815021; H = 0.815021/ln(4) = 0.587914; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.860042; −Σp ln(p) = 0.424219; H = 0.424219/ln(3) = 0.386140; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Pengurangan Bilangan Cacah sampai 100
Tipe soal: multiple_choice
Stimulus: -
Soal: Pak Doni memiliki kolam ikan yang diisi dengan 23 ekor ikan gurami dan 42 ekor ikan nila.

Berapa selisih jumlah ikan gurami dan ikan nila milik Pak Doni?
Pilihan: A. 21 ekor
B. 65 ekor
C. 19 ekor
D. 20 ekor
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `0b7434eea7cad7663b154cc2`

Isilah titik-titik berikut dengan bilangan yang tepat sesuai gambar! (c)

| Opsi | Isi |
|---|---|
| A | 4 x 9 = 36 (dihitung sebagai 4 kelompok isi 9) |
| B | 9 x 4 = 32 |
| C | 9 x 4 = 36 |
| D | 8 x 4 = 32 |

![Gambar sumber soal 11](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0072-02.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Gambar menunjukkan 9 kelompok yang masing-masing berisi 4 objek. Operasi perkalian yang sesuai adalah (banyak kelompok) x (isi per kelompok) = total, yaitu 9 x 4 = 36.
Gambar sumber: images/kelas3_panduan_siswa_kelas3.pdf-0072-02.png. Transkripsi visual: Gambar menunjukkan 9 kelompok objek yang disusun berjajar. Setiap kelompok berisi 4 item (kartu bergambar). Di bawah gambar terdapat pola titik-titik untuk operasi perkalian: .... X .... = ....

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9dc7981e35c1a31b98bfd81adae3c477b1dc2fc3f147a1771a104035b53df38f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3435 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3425 |
| 3 | success | valid / verified | applying | conceptual | Easy | 4115 |

Run 1 — solusi: Gambar menampilkan 9 kelompok yang masing-masing berisi 4 item. Operasi perkalian yang sesuai adalah (banyak kelompok) x (isi per kelompok) = total, yaitu 9 x 4 = 36.
- Domain kognitif `classify/knowing`: Siswa diminta untuk menerjemahkan representasi visual (kelompok objek) ke dalam bentuk operasi perkalian dasar. Ini adalah tugas pengenalan konsep perkalian sebagai penjumlahan berulang atau pengelompokan, yang merupakan prosedur langsung.. Bukti: Isilah titik-titik berikut dengan bilangan yang tepat sesuai gambar!; Gambar menunjukkan 9 kelompok objek... Setiap kelompok berisi 4 item
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep perkalian sebagai pengelompokan objek, yang merupakan pengetahuan konseptual dasar tentang operasi perkalian.. Bukti: Isilah titik-titik berikut dengan bilangan yang tepat sesuai gambar!
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu menghitung jumlah kelompok dan jumlah item per kelompok, lalu menuliskan kalimat matematikanya. Tidak ada langkah yang saling bergantung atau strategi kompleks yang diperlukan.. Bukti: Isilah titik-titik berikut dengan bilangan yang tepat sesuai gambar!; Gambar menunjukkan 9 kelompok objek... Setiap kelompok berisi 4 item

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang perkalian sebagai pengelompokan objek. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, mengidentifikasi perkalian dari gambar adalah tugas rutin yang sesuai dengan kurikulum dasar perkalian. |

Run 2 — solusi: Gambar menunjukkan 9 kelompok yang masing-masing berisi 4 objek. Operasi perkalian yang sesuai adalah 9 kelompok dikali 4 objek per kelompok, yaitu 9 x 4 = 36.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerjemahkan representasi visual (kelompok objek) ke dalam bentuk operasi perkalian dasar. Ini adalah penerapan langsung dari konsep perkalian sebagai penjumlahan berulang atau pengelompokan, yang merupakan prosedur standar di kelas 3.. Bukti: Isilah titik-titik berikut dengan bilangan yang tepat sesuai gambar!; 9 kelompok yang masing-masing berisi 4 boneka
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang perkalian sebagai pengelompokan objek (konsep perkalian) dan kemampuan menerapkan prosedur perkalian dasar.. Bukti: 9 kelompok yang masing-masing berisi 4 boneka
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menghitung jumlah kelompok dan jumlah objek per kelompok, lalu menuliskan kalimat matematikanya. Tidak ada langkah yang saling bergantung atau strategi kompleks yang diperlukan.. Bukti: Isilah titik-titik berikut dengan bilangan yang tepat sesuai gambar!

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar perkalian sebagai pengelompokan objek. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah terbiasa dengan model perkalian menggunakan gambar kelompok objek. Tugas ini adalah latihan standar yang tidak menuntut perencanaan tinggi. |

Run 3 — solusi: Terdapat 9 kelompok, setiap kelompok berisi 4 objek. Maka bentuk perkalian yang sesuai adalah 9 x 4 = 36.
- Domain kognitif `classify/applying`: Siswa perlu menerjemahkan representasi visual (9 kelompok berisi 4) ke dalam kalimat matematika perkalian yang sesuai. Ini adalah penerapan konsep perkalian pada konteks visual rutin.. Bukti: 9 kelompok; masing-masing berisi 4 boneka
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konsep perkalian sebagai pengelompokan objek yang sama jumlahnya.. Bukti: 9 kelompok; masing-masing berisi 4 boneka
- Intended difficulty `classify/Easy`: Soal ini adalah penerapan langsung konsep perkalian sebagai pengelompokan. Siswa hanya perlu menghitung jumlah kelompok dan jumlah objek per kelompok, lalu mengalikan. Tidak ada langkah rumit atau kendala yang berinteraksi.. Bukti: 9 kelompok; masing-masing berisi 4 boneka

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Konsep dasar perkalian sebagai pengelompokan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah mempelajari perkalian sebagai pengelompokan. Soal ini sangat standar dan langsung, sesuai dengan kurikulum kelas 3. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 1, "applying": 2} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4819`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta untuk menerjemahkan representasi visual (kelompok objek) ke dalam bentuk operasi perkalian dasar. Ini adalah penerapan konsep perkalian sebagai pengelompokan yang merupakan prosedur standar dan rutin di kelas 3.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang perkalian sebagai pengelompokan objek (konsep perkalian) dan kemampuan menerapkan prosedur perkalian dasar.
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menghitung jumlah kelompok dan jumlah objek per kelompok, lalu menuliskan kalimat matematikanya. Tidak ada langkah yang saling bergantung atau strategi kompleks yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar perkalian sebagai pengelompokan objek. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah terbiasa dengan model perkalian menggunakan gambar kelompok objek. Tugas ini adalah latihan standar yang tidak menuntut perencanaan tinggi. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 135/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.010646; applying=0.989354; reasoning=0.000000 | applying | 0.989354 | 0.053658 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.009827; conceptual=0.986735; procedural=0.003438; metacognitive=0.000000 | conceptual | 0.986735 | 0.056341 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.822756; Medium=0.174191; Hard=0.003053 | Easy | 0.822756 | 0.439294 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.989354; −Σp ln(p) = 0.058949; H = 0.058949/ln(3) = 0.053658; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.986735; −Σp ln(p) = 0.078106; H = 0.078106/ln(4) = 0.056341; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.822756; −Σp ln(p) = 0.482614; H = 0.482614/ln(3) = 0.439294; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Perkalian Bilangan Cacah sampai 100
Tipe soal: multiple_choice
Stimulus: -
Soal: Isilah titik-titik berikut dengan bilangan yang tepat sesuai gambar! (c)
Pilihan: A. 4 x 9 = 36 (dihitung sebagai 4 kelompok isi 9)
B. 9 x 4 = 32
C. 9 x 4 = 36
D. 8 x 4 = 32
Transkripsi visual: Gambar menunjukkan 9 kelompok objek yang disusun berjajar. Setiap kelompok berisi 4 item (kartu bergambar). Di bawah gambar terdapat pola titik-titik untuk operasi perkalian: .... X .... = ....
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 12. Soal `ea6784174a435a89a237b709`

Hitunglah hasil perkalian berikut! 5 x 7 = .....

| Opsi | Isi |
|---|---|
| A | 12 |
| B | 42 |
| C | 30 |
| D | 35 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: 5 x 7 = 35
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a2d56353f14e05928d55ddbb75b3e38d7adc41e5be18c6b57d07d441e545c0dc`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2147 |
| 2 | success | valid / verified | knowing | factual | Easy | 2150 |
| 3 | success | valid / verified | knowing | factual | Easy | 2165 |

Run 1 — solusi: 5 x 7 = 35
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk melakukan operasi perkalian dasar yang sudah dipelajari di kelas 3. Ini adalah prosedur langsung yang tidak memerlukan penalaran kompleks.. Bukti: Hitunglah hasil perkalian berikut! 5 x 7 = .....
- Dimensi pengetahuan `classify/factual`: Soal menguji penguasaan fakta perkalian dasar (tabel perkalian).. Bukti: 5 x 7 = .....
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi perkalian dasar satu langkah yang sangat familiar bagi siswa kelas 3. Tidak ada kendala atau langkah tambahan yang diperlukan.. Bukti: 5 x 7 = .....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep perkalian sebagai penjumlahan berulang atau hafalan tabel perkalian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Perkalian 5x7 adalah materi standar kelas 3 yang bersifat rutin dan langsung. |

Run 2 — solusi: 5 x 7 = 35
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk melakukan operasi perkalian dasar yang sudah dipelajari. Ini adalah prosedur langsung yang tidak memerlukan pemikiran kompleks atau strategi non-rutin.. Bukti: Hitunglah hasil perkalian berikut! 5 x 7 = .....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji penguasaan fakta perkalian dasar (tabel perkalian) yang merupakan elemen dasar dalam matematika.. Bukti: 5 x 7 = .....
- Intended difficulty `classify/Easy`: Soal ini adalah operasi perkalian satu langkah yang sangat familiar bagi siswa kelas 3. Tidak ada kendala atau langkah tambahan yang diperlukan.. Bukti: 5 x 7 = .....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep perkalian sebagai penjumlahan berulang atau hafalan tabel perkalian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Perkalian 5x7 adalah materi standar kelas 3 yang bersifat rutin dan langsung. |

Run 3 — solusi: 5 x 7 = 35
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk melakukan operasi perkalian dasar yang sudah dipelajari di kelas 3. Ini adalah prosedur langsung yang tidak memerlukan strategi kompleks.. Bukti: Hitunglah hasil perkalian berikut! 5 x 7 = .....
- Dimensi pengetahuan `classify/factual`: Soal menguji penguasaan fakta perkalian dasar (tabel perkalian) yang merupakan elemen dasar dalam matematika.. Bukti: 5 x 7
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari fakta perkalian dasar yang familiar bagi siswa kelas 3. Tidak ada langkah tambahan, kendala, atau kebutuhan untuk memilih strategi.. Bukti: 5 x 7 = .....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep perkalian sebagai penjumlahan berulang atau hafalan tabel perkalian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Perkalian 5x7 adalah fakta dasar yang diharapkan sudah dikuasai siswa kelas 3. Soal tidak memiliki kompleksitas tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 65/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999561; applying=0.000439; reasoning=0.000000 | knowing | 0.999561 | 0.003491 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.572667; conceptual=0.392155; procedural=0.035178; metacognitive=0.000000 | factual | 0.572667 | 0.580022 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.912429; Medium=0.085720; Hard=0.001851 | Easy | 0.912429 | 0.278399 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999561; −Σp ln(p) = 0.003835; H = 0.003835/ln(3) = 0.003491; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.572667; −Σp ln(p) = 0.804081; H = 0.804081/ln(4) = 0.580022; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.912429; −Σp ln(p) = 0.305853; H = 0.305853/ln(3) = 0.278399; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Perkalian Bilangan Cacah sampai 100
Tipe soal: multiple_choice
Stimulus: -
Soal: Hitunglah hasil perkalian berikut! 5 x 7 = .....
Pilihan: A. 12
B. 42
C. 30
D. 35
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 13. Soal `d8e3e19d701550680f504300`

Tulislah pembagian berikut sebagai pengurangan berulang!<br><br>16 : 4 = .....

| Opsi | Isi |
|---|---|
| A | 4 kali (16-4-4-4-4=0) |
| B | 12 kali (16-4=12, dianggap tiap kali kurang 1) |
| C | 3 kali (16-4-4-4=4) |
| D | 5 kali (20-4-4-4-4-4=0) |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Pembagian 16 : 4 berarti 16 dikurangi 4 secara berulang sampai hasilnya 0. Langkahnya: 16 - 4 = 12; 12 - 4 = 8; 8 - 4 = 4; 4 - 4 = 0. Ada 4 kali pengurangan.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f0249b27eaaf495e8f2e0b256bc98e226b1132ad4b80588000d1f11cec263a06`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 2202 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2858 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2182 |

Run 1 — solusi: Pembagian 16 : 4 berarti 16 dikurangi 4 secara berulang sampai hasilnya 0. Langkahnya: 16 - 4 = 12; 12 - 4 = 8; 8 - 4 = 4; 4 - 4 = 0. Ada 4 kali pengurangan.
- Domain kognitif `classify/knowing`: Siswa diminta menerapkan konsep pembagian sebagai pengurangan berulang yang merupakan prosedur dasar yang diajarkan di kelas 3. Soal ini menguji pemahaman prosedural langsung tanpa memerlukan strategi nonrutin.. Bukti: Tulislah pembagian berikut sebagai pengurangan berulang!; 16 : 4 = .....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau metode pengurangan berulang sebagai representasi dari operasi pembagian.. Bukti: Tulislah pembagian berikut sebagai pengurangan berulang!
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu melakukan pengurangan berulang 16 - 4 sampai habis dan menghitung jumlah pengurangannya. Tidak ada kendala yang berinteraksi atau kebutuhan perencanaan yang kompleks.. Bukti: 16 : 4 = .....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dan pembagian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 3 karena pengurangan berulang adalah cara standar untuk memperkenalkan pembagian di tingkat ini. |

Run 2 — solusi: 16 : 4 berarti 16 dikurangi 4 secara berulang sampai hasilnya 0. Langkahnya: 16 - 4 = 12, 12 - 4 = 8, 8 - 4 = 4, 4 - 4 = 0. Terdapat 4 kali pengurangan.
- Domain kognitif `classify/knowing`: Soal meminta siswa menjalankan prosedur dasar pembagian sebagai pengurangan berulang yang merupakan materi standar kelas 3.. Bukti: Tulislah pembagian berikut sebagai pengurangan berulang!; 16 : 4 = .....
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan metode atau algoritma pengurangan berulang untuk menyelesaikan operasi pembagian.. Bukti: Tulislah pembagian berikut sebagai pengurangan berulang!
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menerapkan konsep pembagian sebagai pengurangan berulang tanpa perlu perencanaan langkah yang kompleks atau integrasi kendala.. Bukti: 16 : 4 = .....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dan pembagian sebagai pengurangan berulang. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tingkat kesulitan rendah karena soal merupakan latihan rutin yang sesuai dengan kurikulum kelas 3 tanpa tuntutan kognitif tambahan. |

Run 3 — solusi: Pembagian 16 : 4 berarti 16 dikurangi 4 secara berulang sampai hasilnya 0. Langkahnya: 16 - 4 = 12; 12 - 4 = 8; 8 - 4 = 4; 4 - 4 = 0. Ada 4 kali pengurangan.
- Domain kognitif `classify/knowing`: Siswa diminta menjalankan prosedur pengurangan berulang yang merupakan definisi dasar dari pembagian bilangan cacah. Ini adalah tugas prosedural langsung yang familiar bagi siswa kelas 3.. Bukti: Tulislah pembagian berikut sebagai pengurangan berulang!; 16 : 4 = .....
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritma atau metode pengurangan berulang sebagai representasi dari operasi pembagian.. Bukti: Tulislah pembagian berikut sebagai pengurangan berulang!
- Intended difficulty `classify/Easy`: Soal ini sangat langsung dan rutin. Siswa hanya perlu menerapkan konsep pengurangan berulang pada angka kecil yang familiar. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi kompleks.. Bukti: 16 : 4 = .....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dan pembagian dasar sebagai pengurangan berulang. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, konsep pembagian sebagai pengurangan berulang adalah materi standar. Soal ini tidak menuntut lebih dari sekadar menjalankan prosedur tersebut secara langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 123/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000286; applying=0.999714; reasoning=0.000000 | applying | 0.999714 | 0.002387 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.033069; conceptual=0.953338; procedural=0.013593; metacognitive=0.000000 | conceptual | 0.953338 | 0.156329 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.866888; Medium=0.130900; Hard=0.002212 | Easy | 0.866888 | 0.367296 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999714; −Σp ln(p) = 0.002622; H = 0.002622/ln(3) = 0.002387; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.953338; −Σp ln(p) = 0.216718; H = 0.216718/ln(4) = 0.156329; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.866888; −Σp ln(p) = 0.403516; H = 0.403516/ln(3) = 0.367296; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Pembagian Bilangan Cacah sampai 100
Tipe soal: multiple_choice
Stimulus: -
Soal: Tulislah pembagian berikut sebagai pengurangan berulang!

16 : 4 = .....
Pilihan: A. 4 kali (16-4-4-4-4=0)
B. 12 kali (16-4=12, dianggap tiap kali kurang 1)
C. 3 kali (16-4-4-4=4)
D. 5 kali (20-4-4-4-4-4=0)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `ea7d38ffd5b2b15fbd33446e`

Ayah memelihara beberapa ekor ayam. Ayam-ayam tersebut bertelur dan menghasilkan 24 telur. Ayah ingin memasukkan telur-telur itu ke dalam 3 kotak dengan sama banyak.<br><br>Berapa jumlah telur dalam setiap kotak?

| Opsi | Isi |
|---|---|
| A | 8 butir |
| B | 7 butir |
| C | 6 butir |
| D | 21 butir |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: 24 telur dibagi ke dalam 3 kotak sama banyak berarti 24 : 3 = 8. Jadi, setiap kotak berisi 8 telur.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `05f893ca024cf77cc71df3d7c67f36dc3e791ec5ed37d54c55df998fd2bb76ae`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2274 |
| 2 | success | valid / verified | applying | procedural | Easy | 2275 |
| 3 | success | valid / verified | applying | procedural | Easy | 2264 |

Run 1 — solusi: 24 telur dibagi ke dalam 3 kotak sama banyak berarti 24 : 3 = 8. Jadi, setiap kotak berisi 8 telur.
- Domain kognitif `classify/applying`: Soal meminta siswa untuk menerapkan operasi pembagian dasar yang sudah dipelajari di kelas 3 untuk menyelesaikan masalah pembagian kelompok sama rata yang rutin.. Bukti: Ayah ingin memasukkan telur-telur itu ke dalam 3 kotak dengan sama banyak.; Berapa jumlah telur dalam setiap kotak?
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami konsep pembagian sebagai pembagian rata (partitive division) dan menerapkan prosedur pembagian bilangan cacah.. Bukti: 24 telur; 3 kotak dengan sama banyak
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari konsep pembagian dasar. Jalur penyelesaian sangat jelas, tidak ada kendala yang berinteraksi, dan operasi yang digunakan adalah operasi dasar yang familiar bagi siswa kelas 3.. Bukti: 24 telur; 3 kotak dengan sama banyak

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pembagian dasar dan fakta perkalian/pembagian bilangan cacah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pembagian 24 dengan 3 adalah standar kurikulum kelas 3. Soal tidak memiliki jebakan atau langkah tambahan yang kompleks. |

Run 2 — solusi: 24 telur dibagi ke dalam 3 kotak sama banyak berarti 24 : 3 = 8. Jadi, setiap kotak berisi 8 telur.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan prosedur pembagian dasar yang sudah dipelajari di kelas 3 untuk membagi jumlah total benda ke dalam kelompok yang sama.. Bukti: Ayah ingin memasukkan telur-telur itu ke dalam 3 kotak dengan sama banyak.; Berapa jumlah telur dalam setiap kotak?
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami konsep pembagian sebagai pembagian rata (partitive division) dan menerapkan algoritma pembagian dasar.. Bukti: menghasilkan 24 telur; memasukkan telur-telur itu ke dalam 3 kotak dengan sama banyak
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari konsep pembagian dasar yang familiar bagi siswa kelas 3. Jalur penyelesaiannya tunggal dan jelas.. Bukti: menghasilkan 24 telur; memasukkan telur-telur itu ke dalam 3 kotak dengan sama banyak

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pembagian dasar dan fakta perkalian/pembagian bilangan cacah sampai 100. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pembagian 24 dengan 3 adalah operasi dasar yang sesuai dengan kurikulum kelas 3. Tidak ada kendala tambahan atau langkah kompleks yang diperlukan. |

Run 3 — solusi: 24 telur dibagi ke dalam 3 kotak sama banyak berarti 24 : 3 = 8. Jadi, setiap kotak berisi 8 telur.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan konsep pembagian dasar untuk membagi jumlah total benda ke dalam kelompok yang sama. Ini adalah prosedur rutin yang sudah dipelajari di kelas 3.. Bukti: Ayah ingin memasukkan telur-telur itu ke dalam 3 kotak dengan sama banyak.; Berapa jumlah telur dalam setiap kotak?
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami hubungan antara pembagian sebagai pembagian rata (partitive division) dan menerapkan algoritma pembagian dasar.. Bukti: 24 telur; 3 kotak; sama banyak
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari konsep pembagian dasar. Jalur penyelesaian sangat jelas, tidak ada kendala yang berinteraksi, dan beban kognitif rendah bagi siswa kelas 3.. Bukti: menghasilkan 24 telur; memasukkan telur-telur itu ke dalam 3 kotak dengan sama banyak

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pembagian sebagai pembagian rata dan fakta dasar pembagian. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pembagian 24 dengan 3 adalah operasi dasar yang sesuai dengan kurikulum kelas 3. Tidak ada tuntutan perencanaan atau integrasi yang kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 92/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000001; applying=0.999999; reasoning=0.000000 | applying | 0.999999 | 0.000011 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.129711; conceptual=0.847574; procedural=0.022715; metacognitive=0.000000 | conceptual | 0.847574 | 0.354230 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.848646; Medium=0.147216; Hard=0.004138 | Easy | 0.848646 | 0.404171 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999999; −Σp ln(p) = 0.000012; H = 0.000012/ln(3) = 0.000011; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.847574; −Σp ln(p) = 0.491066; H = 0.491066/ln(4) = 0.354230; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.848646; −Σp ln(p) = 0.444027; H = 0.444027/ln(3) = 0.404171; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Pembagian Bilangan Cacah sampai 100
Tipe soal: multiple_choice
Stimulus: -
Soal: Ayah memelihara beberapa ekor ayam. Ayam-ayam tersebut bertelur dan menghasilkan 24 telur. Ayah ingin memasukkan telur-telur itu ke dalam 3 kotak dengan sama banyak.

Berapa jumlah telur dalam setiap kotak?
Pilihan: A. 8 butir
B. 7 butir
C. 6 butir
D. 21 butir
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 15. Soal `86ef303fdabf175f3223919d`

Di atas bunga hinggap kupu-kupu merah, kuning, dan hijau. Ada 5 kupu-kupu merah. Ada 6 kupu-kupu hijau. Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.<br><br>Berapa jumlah semua kupu-kupu?

| Opsi | Isi |
|---|---|
| A | 18 |
| B | 12 |
| C | 13 |
| D | 11 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Kuning = 5 + 2 = 7. Total = 5 (merah) + 6 (hijau) + 7 (kuning) = 18.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9a7a9e53c0f35840db25adfa6655d1700b2d91a6530e4c01adc4cdba38312c46`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2399 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2375 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2394 |

Run 1 — solusi: Jumlah kupu-kupu kuning adalah 5 + 2 = 7. Total semua kupu-kupu adalah 5 (merah) + 6 (hijau) + 7 (kuning) = 18.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi informasi yang diberikan, melakukan operasi penjumlahan sederhana untuk menentukan jumlah kupu-kupu kuning, dan kemudian menjumlahkan ketiga kelompok kupu-kupu tersebut. Ini adalah penerapan prosedur penjumlahan dalam konteks rutin.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.; Berapa jumlah semua kupu-kupu?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang hubungan antar kuantitas (konsep 'lebih dari') dan penggunaan algoritme penjumlahan dasar untuk menyelesaikan masalah.. Bukti: Ada 5 kupu-kupu merah. Ada 6 kupu-kupu hijau. Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan dua langkah berurutan: menentukan jumlah kupu-kupu kuning terlebih dahulu sebelum menjumlahkan totalnya. Meskipun operasinya dasar, terdapat ketergantungan langkah yang memerlukan ketelitian.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.; Berapa jumlah semua kupu-kupu?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar dan pemahaman konsep 'lebih dari' (penjumlahan). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, soal cerita dua langkah seperti ini adalah standar. Siswa perlu mengelola informasi yang diberikan secara bertahap (menghitung kuning, lalu total) tanpa bantuan eksplisit. |

Run 2 — solusi: Kupu-kupu merah = 5. Kupu-kupu hijau = 6. Kupu-kupu kuning = 5 + 2 = 7. Total = 5 + 6 + 7 = 18.
- Domain kognitif `classify/applying`: Siswa perlu memahami hubungan '2 lebihnya' untuk menentukan jumlah kupu-kupu kuning, kemudian mengintegrasikan ketiga nilai tersebut untuk mendapatkan total. Ini adalah penerapan konsep penjumlahan dasar dalam konteks rutin.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.; Berapa jumlah semua kupu-kupu?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang hubungan antar kuantitas (konseptual) dan penggunaan operasi penjumlahan (prosedural) untuk menyelesaikan masalah cerita.. Bukti: Ada 5 kupu-kupu merah. Ada 6 kupu-kupu hijau.; Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.
- Intended difficulty `classify/Easy`: Soal ini memerlukan dua langkah: menentukan jumlah kupu-kupu kuning (5+2=7) lalu menjumlahkan ketiganya (5+6+7=18). Jalur penyelesaian sangat jelas dan familiar bagi siswa kelas 3.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.; Berapa jumlah semua kupu-kupu?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar dan pemahaman konsep 'lebih dari'. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tingkat kesulitan sesuai untuk kelas 3 karena melibatkan operasi penjumlahan dasar dengan langkah perantara yang sederhana dan eksplisit. |

Run 3 — solusi: Kupu-kupu merah = 5. Kupu-kupu hijau = 6. Kupu-kupu kuning = 5 + 2 = 7. Total = 5 + 6 + 7 = 18.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi informasi yang diberikan, melakukan satu langkah operasi untuk menentukan jumlah kupu-kupu kuning, lalu menjumlahkan ketiga kelompok tersebut. Ini adalah penerapan prosedur penjumlahan dalam konteks rutin.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.; Berapa jumlah semua kupu-kupu?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang hubungan antar kuantitas (konsep 'lebih dari') dan penggunaan algoritma penjumlahan dasar untuk menyelesaikan masalah.. Bukti: Ada 5 kupu-kupu merah. Ada 6 kupu-kupu hijau. Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan dua tahap: menentukan jumlah kupu-kupu kuning terlebih dahulu sebelum menjumlahkan totalnya. Meskipun operasinya dasar, terdapat ketergantungan langkah yang memerlukan ketelitian.. Bukti: Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.; Berapa jumlah semua kupu-kupu?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar dan pemahaman konsep 'lebih dari' (penjumlahan sederhana). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, soal cerita dua langkah seperti ini adalah standar menengah. Siswa harus mengelola informasi yang tidak eksplisit (jumlah kuning) sebelum menghitung total. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3999`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa harus menerapkan prosedur penjumlahan untuk menentukan nilai yang belum diketahui (kuning) dan kemudian menerapkan prosedur penjumlahan lagi untuk mendapatkan total. Ini adalah penerapan konsep dalam konteks rutin.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman hubungan antar kuantitas (konsep 'lebih dari') dan penggunaan algoritme penjumlahan dasar.
- Intended difficulty `Easy`: Soal ini dikategorikan Easy karena alur penyelesaiannya sangat linear dan familiar bagi siswa kelas 3. Meskipun ada dua langkah (menentukan nilai kuning lalu menjumlahkan total), langkah-langkah tersebut sangat langsung dan tidak memerlukan perencanaan strategi yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar dan pemahaman konsep 'lebih dari'. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal cerita dua langkah dengan operasi penjumlahan dasar adalah standar untuk kelas 3. Tidak ada kendala yang berinteraksi secara kompleks atau kebutuhan untuk memilih strategi non-rutin. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 112/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000209; applying=0.999791; reasoning=0.000000 | applying | 0.999791 | 0.001802 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.291642; conceptual=0.693791; procedural=0.014567; metacognitive=0.000000 | conceptual | 0.693791 | 0.486630 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.865333; Medium=0.131663; Hard=0.003004 | Easy | 0.865333 | 0.372795 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999791; −Σp ln(p) = 0.001980; H = 0.001980/ln(3) = 0.001802; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.693791; −Σp ln(p) = 0.674612; H = 0.674612/ln(4) = 0.486630; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.865333; −Σp ln(p) = 0.409558; H = 0.409558/ln(3) = 0.372795; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Soal Cerita Penjumlahan dan Pengurangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Di atas bunga hinggap kupu-kupu merah, kuning, dan hijau. Ada 5 kupu-kupu merah. Ada 6 kupu-kupu hijau. Banyaknya kupu-kupu kuning 2 lebihnya dari banyak kupu-kupu merah.

Berapa jumlah semua kupu-kupu?
Pilihan: A. 18
B. 12
C. 13
D. 11
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `f366f15007b61b27653bdf58`

Kira menuliskan satu bilangan.<br><br>Kira berkata, 'Jika aku tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55.' Berapa bilangan yang ditulis Kira?

| Opsi | Isi |
|---|---|
| A | 92 |
| B | 81 |
| C | 29 |
| D | 12 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Bilangan Kira adalah N. Operasi yang dilakukan adalah N + 43 = 55. Maka N = 55 - 43 = 12.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d5bca85d43139b6f7ee0aca3902ceba402499eedd1b88a2ed8bf9f4169123a71`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2351 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2319 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2362 |

Run 1 — solusi: Bilangan Kira adalah N. Operasi yang dilakukan adalah N + 43 = 55. Maka N = 55 - 43 = 12.
- Domain kognitif `classify/applying`: Siswa perlu memahami hubungan antara operasi penjumlahan yang diberikan dan operasi kebalikannya (pengurangan) untuk menemukan bilangan awal. Ini melibatkan penerapan konsep nilai tempat dan operasi dasar dalam konteks rutin.. Bukti: Jika aku tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang nilai tempat (puluhan dan satuan) dan bagaimana operasi aritmatika memengaruhi nilai tersebut.. Bukti: tambahkan 4 pada puluhan dan 3 pada satuan
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak hanya melakukan operasi hitung langsung, tetapi harus membalikkan proses (inverse operation) dari hasil akhir ke bilangan awal dengan mempertimbangkan nilai tempat. Meskipun prosedurnya familiar, langkah berpikir untuk membalikkan operasi memerlukan sedikit perencanaan.. Bukti: Jika aku tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat (puluhan dan satuan) dan operasi pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah mempelajari nilai tempat dan pengurangan. Soal ini menuntut pemahaman konsep nilai tempat dalam konteks pemecahan masalah sederhana, yang sesuai dengan tingkat kognitif kelas 3. |

Run 2 — solusi: Bilangan awal = 55 - 43. Puluhan: 5 - 4 = 1. Satuan: 5 - 3 = 2. Jadi, bilangan tersebut adalah 12.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep nilai tempat (puluhan dan satuan) dan melakukan operasi kebalikan (pengurangan) untuk menemukan bilangan awal. Ini adalah penerapan konsep nilai tempat pada konteks rutin.. Bukti: Jika aku tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur bilangan (puluhan dan satuan) dan bagaimana operasi aritmatika dasar mempengaruhi nilai tempat tersebut.. Bukti: tambahkan 4 pada puluhan dan 3 pada satuan
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemahaman konsep nilai tempat dan operasi kebalikan. Meskipun prosedurnya sederhana, siswa harus melakukan dua langkah pengurangan (puluhan dan satuan) secara terpisah, yang merupakan tantangan yang sesuai untuk kelas 3.. Bukti: Jika aku tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat (puluhan dan satuan) dan pengurangan bilangan dua angka. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah mempelajari nilai tempat dan pengurangan. Soal ini menuntut pembalikan operasi yang merupakan langkah logis menengah bagi mereka. |

Run 3 — solusi: Bilangan Kira adalah 12. Jika 12 ditambah 4 pada puluhan (1+4=5) dan 3 pada satuan (2+3=5), hasilnya adalah 55.
- Domain kognitif `classify/applying`: Siswa perlu melakukan operasi kebalikan (invers) dari penambahan yang diberikan untuk menemukan bilangan awal. Ini melibatkan pemahaman tentang nilai tempat (puluhan dan satuan) dan menerapkan prosedur pengurangan untuk membalikkan proses yang dijelaskan.. Bukti: Jika aku tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang nilai tempat (puluhan dan satuan) dan bagaimana angka-angka tersebut berinteraksi dalam operasi penjumlahan dan pengurangan.. Bukti: tambahkan 4 pada puluhan dan 3 pada satuan
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak bisa langsung menghitung, melainkan harus memahami struktur nilai tempat dan melakukan operasi invers (pengurangan) untuk mendapatkan bilangan awal. Meskipun operasinya sederhana, proses berpikir untuk membalikkan kondisi memerlukan integrasi konsep nilai tempat yang lebih dari sekadar prosedur rutin satu langkah.. Bukti: Jika aku tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan dua angka (puluhan dan satuan) dan operasi pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, memahami bahwa 55 terdiri dari 5 puluhan dan 5 satuan, lalu membalikkan operasi penambahan pada masing-masing posisi, merupakan tantangan yang sesuai untuk tingkat Medium karena memerlukan penalaran terbalik. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 77/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.986888; applying=0.013112; reasoning=0.000000 | knowing | 0.986888 | 0.063585 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.110817; conceptual=0.830592; procedural=0.058591; metacognitive=0.000000 | conceptual | 0.830592 | 0.406976 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.751435; Medium=0.245294; Hard=0.003271 | Easy | 0.751435 | 0.526272 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.986888; −Σp ln(p) = 0.069855; H = 0.069855/ln(3) = 0.063585; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.830592; −Σp ln(p) = 0.564188; H = 0.564188/ln(4) = 0.406976; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.751435; −Σp ln(p) = 0.578169; H = 0.578169/ln(3) = 0.526272; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Membandingkan Bilangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Kira menuliskan satu bilangan.

Kira berkata, 'Jika aku tambahkan 4 pada puluhan dan 3 pada satuan, hasilnya adalah 55.' Berapa bilangan yang ditulis Kira?
Pilihan: A. 92
B. 81
C. 29
D. 12
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 17. Soal `134652ea27846439dcee22e8`

Pak Budi sedang panen buah durian. Hasil panennya itu diletakkan dalam dua keranjang sebelum dijual di pasar. Keranjang pertama berisi 42 buah durian. Sementara jumlah durian yang ada pada kedua keranjang tersebut adalah 78 buah.<br><br>Berapa banyak durian yang ada di keranjang kedua ?

| Opsi | Isi |
|---|---|
| A | 120 buah |
| B | 36 buah |
| C | 46 buah |
| D | 42 buah |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Diketahui total durian = 78, keranjang pertama = 42. Maka keranjang kedua = 78 - 42 = 36.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `46d977daa7149bb4ac83e81d0ec7dec70ae1378692b7f4cd29dd6927eaf5f56f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2322 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2369 |
| 3 | success | valid / verified | applying | procedural | Easy | 2355 |

Run 1 — solusi: Diketahui total durian 78 dan keranjang pertama 42. Banyak durian di keranjang kedua adalah 78 - 42 = 36.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi hubungan antara bagian dan keseluruhan (part-whole) untuk menentukan operasi pengurangan yang diperlukan. Ini adalah penerapan konsep penjumlahan/pengurangan pada konteks soal cerita rutin.. Bukti: Keranjang pertama berisi 42 buah durian. Sementara jumlah durian yang ada pada kedua keranjang tersebut adalah 78 buah.; Berapa banyak durian yang ada di keranjang kedua ?
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami struktur hubungan penjumlahan (bagian + bagian = total) untuk menentukan prosedur penyelesaian yang tepat.. Bukti: jumlah durian yang ada pada kedua keranjang tersebut adalah 78 buah
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah rutin satu langkah yang familiar bagi siswa kelas 3. Siswa hanya perlu melakukan operasi pengurangan dasar untuk menemukan nilai yang hilang.. Bukti: Keranjang pertama berisi 42 buah durian.; jumlah durian yang ada pada kedua keranjang tersebut adalah 78 buah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dan pengurangan bilangan cacah hingga 100. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah part-whole sederhana dengan angka di bawah 100 adalah standar kompetensi kelas 3 yang rutin. |

Run 2 — solusi: Diketahui total durian 78 dan keranjang pertama 42. Banyak durian di keranjang kedua adalah 78 - 42 = 36.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi hubungan antara bagian dan keseluruhan (part-whole) dalam konteks penjumlahan, lalu menerapkan prosedur pengurangan untuk menemukan nilai yang hilang. Ini adalah penerapan konsep dasar pada konteks rutin.. Bukti: Keranjang pertama berisi 42 buah durian. Sementara jumlah durian yang ada pada kedua keranjang tersebut adalah 78 buah.; Berapa banyak durian yang ada di keranjang kedua ?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang hubungan antara penjumlahan dan pengurangan (konsep part-whole) serta kemampuan melakukan prosedur pengurangan bilangan cacah.. Bukti: jumlah durian yang ada pada kedua keranjang tersebut adalah 78 buah
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena merupakan masalah rutin satu langkah yang melibatkan operasi pengurangan dasar. Siswa hanya perlu menerjemahkan narasi ke dalam kalimat matematika sederhana (42 + x = 78) dan menyelesaikannya.. Bukti: Keranjang pertama berisi 42 buah durian.; jumlah durian yang ada pada kedua keranjang tersebut adalah 78 buah.; Berapa banyak durian yang ada di keranjang kedua ?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dan pengurangan bilangan cacah hingga 100. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah ini sesuai untuk kelas 3 karena menggunakan operasi dasar yang sudah dipelajari dan konteks yang sangat umum. |

Run 3 — solusi: Diketahui total durian 78 dan keranjang pertama 42. Maka durian di keranjang kedua adalah 78 - 42 = 36 buah.
- Domain kognitif `classify/applying`: Siswa perlu memahami hubungan antara bagian dan keseluruhan (part-part-whole) dalam konteks penjumlahan, lalu menerapkan prosedur pengurangan untuk menemukan nilai yang hilang. Ini adalah penerapan konsep dasar pada konteks rutin.. Bukti: Keranjang pertama berisi 42 buah durian.; jumlah durian yang ada pada kedua keranjang tersebut adalah 78 buah.; Berapa banyak durian yang ada di keranjang kedua ?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman tentang struktur penjumlahan (42 + x = 78) dan penggunaan algoritma pengurangan untuk menyelesaikannya.. Bukti: jumlah durian yang ada pada kedua keranjang tersebut adalah 78 buah.; Berapa banyak durian yang ada di keranjang kedua ?
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena merupakan masalah satu langkah yang familiar bagi siswa kelas 3. Hubungan antara total dan bagian sudah jelas, dan prosedur pengurangan yang diperlukan adalah standar untuk tingkat kelas tersebut.. Bukti: Keranjang pertama berisi 42 buah durian.; jumlah durian yang ada pada kedua keranjang tersebut adalah 78 buah.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dan pengurangan bilangan cacah hingga 100. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah satu langkah ini sesuai dengan kurikulum kelas 3 yang menekankan pada pemahaman kalimat matematika sederhana dan operasi hitung dasar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3837`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan konsep hubungan bagian-keseluruhan (part-whole) untuk menentukan operasi yang tepat (pengurangan) guna menyelesaikan masalah rutin ini.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan penjumlahan (bagian + bagian = total) dan bagaimana membalikkan operasi tersebut untuk mencari nilai yang tidak diketahui.
- Intended difficulty `Easy`: Soal ini adalah masalah rutin satu langkah yang sangat familiar bagi siswa kelas 3. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi kompleks; siswa hanya perlu mengidentifikasi operasi pengurangan yang diperlukan dari hubungan part-whole.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dan pengurangan bilangan cacah hingga 100. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah part-whole sederhana dengan angka di bawah 100 adalah standar kompetensi kelas 3 yang rutin dan langsung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 105/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000001 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.078325; conceptual=0.908014; procedural=0.013660; metacognitive=0.000000 | conceptual | 0.908014 | 0.249407 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.877228; Medium=0.119608; Hard=0.003164 | Easy | 0.877228 | 0.352363 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000001; H = 0.000001/ln(3) = 0.000001; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.908014; −Σp ln(p) = 0.345751; H = 0.345751/ln(4) = 0.249407; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.877228; −Σp ln(p) = 0.387110; H = 0.387110/ln(3) = 0.352363; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Kalimat Matematika Berkaitan dengan Penjumlahan Bilangan Cacah
Tipe soal: multiple_choice
Stimulus: -
Soal: Pak Budi sedang panen buah durian. Hasil panennya itu diletakkan dalam dua keranjang sebelum dijual di pasar. Keranjang pertama berisi 42 buah durian. Sementara jumlah durian yang ada pada kedua keranjang tersebut adalah 78 buah.

Berapa banyak durian yang ada di keranjang kedua ?
Pilihan: A. 120 buah
B. 36 buah
C. 46 buah
D. 42 buah
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `4083151b80c126b0090bb512`

Jawablah pertanyaan berikut dengan tepat!<br><br>38 + … = 67

| Opsi | Isi |
|---|---|
| A | 39 |
| B | 29 |
| C | 38 |
| D | 105 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Untuk mencari bilangan yang hilang, kurangkan hasil dengan bilangan yang diketahui: 67 - 38 = 29.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `833971718f2ae1b7a9f73205b091b118f0091ec6e50630086a162d27aa39a176`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2234 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2246 |
| 3 | success | valid / verified | applying | procedural | Easy | 2260 |

Run 1 — solusi: Untuk mencari bilangan yang hilang, kurangkan hasil dengan bilangan yang diketahui: 67 - 38 = 29.
- Domain kognitif `classify/applying`: Siswa diminta untuk menentukan nilai yang hilang dalam kalimat matematika penjumlahan. Ini adalah prosedur standar yang melibatkan pemahaman hubungan antara penjumlahan dan pengurangan.. Bukti: 38 + … = 67
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara penjumlahan dan pengurangan (konsep invers) untuk menyelesaikan kalimat matematika terbuka.. Bukti: 38 + … = 67
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung dari konsep hubungan penjumlahan dan pengurangan. Siswa hanya perlu melakukan satu operasi pengurangan (67 - 38) untuk menemukan jawaban. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: 38 + … = 67

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dan pengurangan bilangan cacah hingga 100. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 3, mencari nilai yang hilang dalam kalimat matematika penjumlahan sederhana adalah tugas rutin yang sesuai dengan kurikulum. |

Run 2 — solusi: Untuk mencari angka yang hilang, hitung selisih antara hasil penjumlahan dan angka yang diketahui: 67 - 38 = 29.
- Domain kognitif `classify/applying`: Siswa diminta untuk menentukan nilai yang hilang dalam kalimat matematika penjumlahan. Ini adalah prosedur langsung untuk mencari selisih antara total dan salah satu suku yang diketahui, yang merupakan penerapan rutin dari konsep hubungan penjumlahan dan pengurangan.. Bukti: 38 + … = 67
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara penjumlahan dan pengurangan (konsep invers) untuk menyelesaikan kalimat matematika terbuka.. Bukti: 38 + … = 67
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu melakukan satu operasi pengurangan (67 - 38) untuk menemukan nilai yang hilang. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi kompleks.. Bukti: 38 + … = 67

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dan pengurangan bilangan cacah hingga 100, termasuk teknik meminjam. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 3, mencari suku yang hilang dalam penjumlahan adalah materi dasar yang sudah sering dilatih. Operasi 67 - 38 dengan teknik meminjam adalah prosedur standar yang diharapkan sudah dikuasai. |

Run 3 — solusi: Untuk mencari angka yang hilang, kurangkan hasil dengan angka yang diketahui: 67 - 38 = 29.
- Domain kognitif `classify/applying`: Siswa diminta untuk menentukan nilai yang hilang dalam kalimat matematika penjumlahan. Ini adalah prosedur standar yang sudah dipelajari di kelas 3, yaitu menggunakan operasi invers (pengurangan) untuk menemukan nilai yang belum diketahui.. Bukti: 38 + … = 67
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan antara penjumlahan dan pengurangan sebagai operasi invers, yang merupakan pengetahuan prosedural dasar dalam aritmatika.. Bukti: 38 + … = 67
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu melakukan satu operasi pengurangan (67 - 38) untuk mendapatkan jawaban. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: 38 + … = 67

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dan pengurangan bilangan cacah sampai 100, termasuk teknik meminjam. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah latihan standar kelas 3 untuk memahami hubungan penjumlahan dan pengurangan. Tingkat kesulitan rendah karena prosedurnya langsung dan familiar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3509`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan prosedur rutin untuk mencari nilai yang hilang dalam kalimat matematika penjumlahan dengan menggunakan operasi invers (pengurangan).
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang hubungan invers antara penjumlahan dan pengurangan untuk menyelesaikan kalimat matematika terbuka.
- Intended difficulty `Easy`: Soal ini adalah latihan rutin yang sangat familiar bagi siswa kelas 3. Prosedur penyelesaiannya langsung (satu langkah pengurangan) tanpa kendala yang berinteraksi atau kebutuhan strategi non-rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dan pengurangan bilangan cacah hingga 100, termasuk teknik meminjam. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari suku yang hilang dalam penjumlahan adalah materi dasar kelas 3. Operasi 67 - 38 dengan teknik meminjam adalah prosedur standar yang diharapkan sudah dikuasai. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 64/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.997427; applying=0.002573; reasoning=0.000000 | knowing | 0.997427 | 0.016301 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.808877; conceptual=0.116948; procedural=0.074175; metacognitive=0.000000 | factual | 0.808877 | 0.443987 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.932819; Medium=0.064504; Hard=0.002676 | Easy | 0.932819 | 0.234415 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.997427; −Σp ln(p) = 0.017909; H = 0.017909/ln(3) = 0.016301; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.808877; −Σp ln(p) = 0.615496; H = 0.615496/ln(4) = 0.443987; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.932819; −Σp ln(p) = 0.257532; H = 0.257532/ln(3) = 0.234415; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Kalimat Matematika Berkaitan dengan Penjumlahan Bilangan Cacah
Tipe soal: multiple_choice
Stimulus: -
Soal: Jawablah pertanyaan berikut dengan tepat!

38 + … = 67
Pilihan: A. 39
B. 29
C. 38
D. 105
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 19. Soal `15c4621ae2b13cb48dc0c3b9`

Pak Budi panen buah manggis. Manggis yang dipanen sebanyak 78 buah. Hasil panen tersebut sebagian besar dibagikan kepada saudara dan tetangganya. Sisa manggis yang tersedia sebanyak 42 buah.<br><br>Berapa banyak manggis yang dibagikan oleh Pak Budi ?

| Opsi | Isi |
|---|---|
| A | 36 buah |
| B | 46 buah |
| C | 120 buah |
| D | 42 buah |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Jumlah manggis yang dibagikan adalah total panen dikurangi sisa manggis: 78 - 42 = 36.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f9192c2ced80afdadbc10afefab8a500a4dd6059ce842eb60408c2f39429832a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2284 |
| 2 | success | valid / verified | applying | procedural | Easy | 2239 |
| 3 | success | valid / verified | applying | procedural | Easy | 2248 |

Run 1 — solusi: Jumlah manggis yang dibagikan adalah total panen dikurangi sisa manggis: 78 - 42 = 36.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan operasi pengurangan pada konteks cerita sederhana. Siswa perlu mengidentifikasi hubungan antara total, sisa, dan bagian yang dibagikan, lalu melakukan prosedur pengurangan dasar. Ini adalah penerapan konsep pengurangan dalam konteks rutin.. Bukti: Manggis yang dipanen sebanyak 78 buah.; Sisa manggis yang tersedia sebanyak 42 buah.; Berapa banyak manggis yang dibagikan oleh Pak Budi ?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa tentang algoritme pengurangan bilangan cacah (prosedural) dan pemahaman bahwa pengurangan dapat digunakan untuk mencari selisih atau bagian yang hilang dari suatu total (konseptual).. Bukti: 78 - 42 = 36
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena merupakan masalah satu langkah yang langsung. Siswa hanya perlu mengenali bahwa 'dibagikan' berarti pengurangan dari total. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: Manggis yang dipanen sebanyak 78 buah.; Sisa manggis yang tersedia sebanyak 42 buah.; Berapa banyak manggis yang dibagikan oleh Pak Budi ?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan bilangan cacah hingga 100 dan kemampuan melakukan pengurangan bersusun. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 3, pengurangan dua angka tanpa teknik meminjam yang rumit (karena 8-2=6 dan 7-4=3) adalah tugas rutin yang sesuai dengan tingkat perkembangan mereka. |

Run 2 — solusi: Jumlah manggis yang dibagikan adalah total panen dikurangi sisa manggis: 78 - 42 = 36.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan operasi pengurangan pada konteks cerita sederhana. Siswa perlu mengidentifikasi hubungan antara total, sisa, dan bagian yang dibagikan, lalu melakukan prosedur pengurangan standar.. Bukti: Manggis yang dipanen sebanyak 78 buah.; Sisa manggis yang tersedia sebanyak 42 buah.; Berapa banyak manggis yang dibagikan oleh Pak Budi ?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa tentang algoritma pengurangan bilangan cacah dua angka (prosedural) dalam konteks masalah sehari-hari.. Bukti: 78 - 42 = 36
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena merupakan masalah satu langkah yang langsung. Siswa hanya perlu mengenali bahwa 'dibagikan' berarti pengurangan dari total. Tidak ada kendala yang berinteraksi atau perencanaan strategi yang kompleks.. Bukti: Manggis yang dipanen sebanyak 78 buah.; Sisa manggis yang tersedia sebanyak 42 buah.; Berapa banyak manggis yang dibagikan oleh Pak Budi ?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan bilangan cacah hingga 100. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, operasi pengurangan dua angka dengan angka yang tidak memerlukan teknik meminjam yang rumit (78-42) adalah materi standar yang rutin. |

Run 3 — solusi: Jumlah manggis yang dibagikan adalah total panen dikurangi sisa manggis: 78 - 42 = 36.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan operasi pengurangan pada konteks cerita sederhana. Siswa perlu mengidentifikasi hubungan antara total, sisa, dan bagian yang dibagikan, lalu melakukan prosedur pengurangan dasar. Ini adalah penerapan konsep pengurangan pada konteks rutin.. Bukti: Manggis yang dipanen sebanyak 78 buah.; Sisa manggis yang tersedia sebanyak 42 buah.; Berapa banyak manggis yang dibagikan oleh Pak Budi ?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa tentang algoritme pengurangan bilangan cacah dua digit, yang merupakan pengetahuan prosedural.. Bukti: 78 - 42 = 36
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hubungan antara total, sisa, dan bagian yang dibagikan sangat eksplisit. Siswa hanya perlu melakukan satu operasi pengurangan dasar tanpa kendala yang saling berinteraksi atau kebutuhan untuk merencanakan strategi yang kompleks.. Bukti: Manggis yang dipanen sebanyak 78 buah.; Sisa manggis yang tersedia sebanyak 42 buah.; Berapa banyak manggis yang dibagikan oleh Pak Budi ?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan bilangan cacah dua digit. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, pengurangan dua digit tanpa teknik meminjam yang rumit (karena 8-2 dan 7-4 langsung) adalah prosedur standar yang familiar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 97/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000008; applying=0.999992; reasoning=0.000000 | applying | 0.999992 | 0.000092 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.210876; conceptual=0.712573; procedural=0.076551; metacognitive=0.000000 | conceptual | 0.712573 | 0.552853 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.908157; Medium=0.088649; Hard=0.003194 | Easy | 0.908157 | 0.291864 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999992; −Σp ln(p) = 0.000101; H = 0.000101/ln(3) = 0.000092; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.712573; −Σp ln(p) = 0.766417; H = 0.766417/ln(4) = 0.552853; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.908157; −Σp ln(p) = 0.320646; H = 0.320646/ln(3) = 0.291864; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Kalimat Matematika Berkaitan dengan Pengurangan Bilangan Cacah
Tipe soal: multiple_choice
Stimulus: -
Soal: Pak Budi panen buah manggis. Manggis yang dipanen sebanyak 78 buah. Hasil panen tersebut sebagian besar dibagikan kepada saudara dan tetangganya. Sisa manggis yang tersedia sebanyak 42 buah.

Berapa banyak manggis yang dibagikan oleh Pak Budi ?
Pilihan: A. 36 buah
B. 46 buah
C. 120 buah
D. 42 buah
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `4c4a8d5909026263b43d6f5c`

Jawablah pertanyaan berikut dengan tepat!<br><br>83 – … = 38

| Opsi | Isi |
|---|---|
| A | 121 |
| B | 38 |
| C | 35 |
| D | 45 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: 83 - 38 = 45
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7d449cddccae318cfca4630fa7fd62dd53b36bd3ebe0b146fdd0a2444b76c7e1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2609 |
| 2 | success | valid / verified | applying | procedural | Easy | 2223 |
| 3 | success | valid / verified | applying | procedural | Easy | 2242 |

Run 1 — solusi: 83 - 38 = 45
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep pengurangan untuk mencari nilai yang hilang dalam kalimat matematika. Ini adalah prosedur rutin yang langsung.. Bukti: 83 – … = 38
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritme pengurangan bilangan cacah dengan teknik meminjam.. Bukti: 83 – … = 38
- Intended difficulty `classify/Easy`: Soal ini merupakan latihan pengurangan standar kelas 3 yang familiar. Jalur penyelesaiannya langsung dan tidak memerlukan perencanaan kompleks.. Bukti: 83 – … = 38

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengurangan bilangan cacah dengan teknik meminjam. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sesuai dengan kurikulum kelas 3 untuk menguji pemahaman hubungan pengurangan dan kemampuan berhitung dasar. |

Run 2 — solusi: Untuk mencari bilangan yang hilang dalam 83 - x = 38, kita dapat menghitung 83 - 38. 83 - 38 = 45.
- Domain kognitif `classify/applying`: Siswa diminta untuk menentukan nilai yang hilang dalam kalimat matematika pengurangan. Ini adalah penerapan langsung dari hubungan antara pengurangan dan penjumlahan atau prosedur pengurangan standar yang sudah dipelajari di kelas 3.. Bukti: 83 – … = 38
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi pengurangan bilangan cacah dengan teknik meminjam.. Bukti: 83 – … = 38
- Intended difficulty `classify/Easy`: Soal ini merupakan latihan rutin pengurangan bilangan dua angka dengan teknik meminjam. Jalur penyelesaiannya sangat jelas dan tidak memerlukan perencanaan strategi yang kompleks atau integrasi kendala yang berinteraksi.. Bukti: 83 – … = 38

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan bilangan cacah dua angka dengan teknik meminjam. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah diajarkan pengurangan bilangan dua angka. Soal ini adalah bentuk standar yang sering ditemui dalam latihan rutin. |

Run 3 — solusi: Untuk mencari bilangan yang hilang, gunakan hubungan pengurangan: 83 - 38 = 45. Jadi, 83 - 45 = 38.
- Domain kognitif `classify/applying`: Siswa diminta untuk menentukan nilai yang hilang dalam kalimat matematika pengurangan. Ini adalah penerapan langsung dari hubungan antara pengurangan dan penjumlahan atau pemahaman dasar tentang operasi pengurangan, yang merupakan prosedur rutin.. Bukti: 83 – … = 38
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pengurangan bilangan cacah (prosedural) dan hubungan antar bilangan dalam operasi pengurangan (konseptual).. Bukti: 83 – … = 38
- Intended difficulty `classify/Easy`: Soal ini adalah latihan pengurangan standar yang familiar bagi siswa kelas 3. Tidak ada langkah yang saling bergantung yang kompleks atau kendala yang berinteraksi.. Bukti: 83 – … = 38

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman pengurangan bilangan cacah dengan teknik meminjam. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan latihan rutin pengurangan dua angka yang sesuai dengan kurikulum kelas 3, di mana siswa diharapkan mampu menyelesaikan kalimat matematika sederhana. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 64/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999791; applying=0.000209; reasoning=0.000000 | knowing | 0.999791 | 0.001806 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.842066; conceptual=0.086418; procedural=0.071516; metacognitive=0.000000 | factual | 0.842066 | 0.393131 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.932862; Medium=0.064064; Hard=0.003074 | Easy | 0.932862 | 0.235437 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999791; −Σp ln(p) = 0.001984; H = 0.001984/ln(3) = 0.001806; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.842066; −Σp ln(p) = 0.544995; H = 0.544995/ln(4) = 0.393131; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.932862; −Σp ln(p) = 0.258654; H = 0.258654/ln(3) = 0.235437; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Kalimat Matematika Berkaitan dengan Pengurangan Bilangan Cacah
Tipe soal: multiple_choice
Stimulus: -
Soal: Jawablah pertanyaan berikut dengan tepat!

83 – … = 38
Pilihan: A. 121
B. 38
C. 35
D. 45
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 21. Soal `fdf4f64afe025be58e0fbd08`

Ibu Meutia membeli kain untuk seragam. Terdapat 3 pesanan seragam dari sekolah kebangsaan. Ukuran panjang kain yang dibutuhkan untuk setiap seragam adalah 200 cm. Ibu Meutia memiliki kain dengan panjang 850 cm.<br><br>Berapakah panjang sisa kain Ibu Meutia?

| Opsi | Isi |
|---|---|
| A | 250 cm |
| B | 150 cm |
| C | 350 cm |
| D | 600 cm |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Total kebutuhan kain = 3 seragam x 200 cm/seragam = 600 cm. Sisa kain = 850 cm - 600 cm = 250 cm.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b11f1ef7a2a0459ab0e424bcaa5c5136e683dbd212e0cda36b19dc1adaef5e2f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2365 |
| 2 | success | valid / verified | applying | procedural | Medium | 2419 |
| 3 | success | valid / verified | applying | procedural | Medium | 2428 |

Run 1 — solusi: Total kebutuhan kain = 3 seragam x 200 cm/seragam = 600 cm. Sisa kain = 850 cm - 600 cm = 250 cm.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi operasi perkalian untuk menentukan total kebutuhan kain, kemudian melakukan operasi pengurangan untuk mencari sisa. Ini adalah penerapan konsep pengukuran dan operasi dasar pada konteks rutin.. Bukti: 3 pesanan seragam; panjang kain yang dibutuhkan untuk setiap seragam adalah 200 cm; Ibu Meutia memiliki kain dengan panjang 850 cm; Berapakah panjang sisa kain
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma perkalian dan pengurangan (prosedural) untuk menyelesaikan masalah pengukuran panjang.. Bukti: 3 pesanan seragam; 200 cm; 850 cm
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena melibatkan dua langkah operasi yang saling terkait (perkalian lalu pengurangan) yang harus direncanakan oleh siswa, meskipun prosedurnya familiar bagi kelas 3.. Bukti: 3 pesanan seragam; setiap seragam adalah 200 cm; memiliki kain dengan panjang 850 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian bilangan satu digit dengan ratusan dan pengurangan bilangan ratusan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah mempelajari perkalian dan pengurangan. Soal menuntut dua langkah berurutan (menghitung total kebutuhan, lalu mencari selisih), yang merupakan tuntutan standar untuk tingkat Medium. |

Run 2 — solusi: Total kain yang dibutuhkan untuk 3 seragam adalah 3 x 200 cm = 600 cm. Sisa kain Ibu Meutia adalah 850 cm - 600 cm = 250 cm.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dua langkah operasi (perkalian untuk total kebutuhan dan pengurangan untuk sisa) dalam konteks rutin pengukuran panjang. Ini melibatkan penerapan konsep operasi dasar pada situasi sehari-hari.. Bukti: 3 pesanan seragam; panjang kain yang dibutuhkan untuk setiap seragam adalah 200 cm; Ibu Meutia memiliki kain dengan panjang 850 cm; Berapakah panjang sisa kain Ibu Meutia?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma perkalian dan pengurangan (prosedural) untuk menyelesaikan masalah pengukuran yang sudah dipahami konsepnya.. Bukti: 3 pesanan seragam; setiap seragam adalah 200 cm; memiliki kain dengan panjang 850 cm
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua langkah perhitungan yang saling bergantung (menghitung total kebutuhan sebelum menghitung sisa). Meskipun operasinya dasar, siswa kelas 3 harus merencanakan urutan langkah tersebut tanpa bantuan eksplisit.. Bukti: 3 pesanan seragam; setiap seragam adalah 200 cm; memiliki kain dengan panjang 850 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian dasar (bilangan 1 digit dengan ratusan) dan pengurangan bilangan ratusan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah mempelajari perkalian dan pengurangan. Tantangan utama adalah mengintegrasikan dua langkah operasi tersebut secara berurutan untuk mencapai jawaban akhir. |

Run 3 — solusi: Total kebutuhan kain = 3 seragam x 200 cm/seragam = 600 cm. Sisa kain = 850 cm - 600 cm = 250 cm.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi informasi yang relevan, melakukan perkalian untuk menentukan total kebutuhan kain, dan melakukan pengurangan untuk mencari sisa. Ini adalah penerapan prosedur matematika pada konteks rutin.. Bukti: 3 pesanan seragam; panjang kain yang dibutuhkan untuk setiap seragam adalah 200 cm; Ibu Meutia memiliki kain dengan panjang 850 cm; Berapakah panjang sisa kain Ibu Meutia?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma perkalian dan pengurangan dalam konteks pengukuran panjang.. Bukti: 3 pesanan seragam; panjang kain yang dibutuhkan untuk setiap seragam adalah 200 cm; 850 cm - 600 cm = 250 cm
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena melibatkan dua langkah operasional yang saling terkait (perkalian untuk total kebutuhan, lalu pengurangan untuk sisa). Meskipun prosedurnya familiar bagi kelas 3, siswa harus merencanakan urutan operasi tersebut secara mandiri tanpa bantuan langkah-langkah perantara.. Bukti: 3 pesanan seragam; setiap seragam adalah 200 cm; memiliki kain dengan panjang 850 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian dasar (bilangan 1 digit dengan ratusan) dan pengurangan bilangan ratusan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah mempelajari perkalian dan pengurangan. Soal menuntut dua langkah logis, yang merupakan tuntutan standar untuk tingkat menengah di kelas 3. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 102/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000020; applying=0.999980; reasoning=0.000000 | applying | 0.999980 | 0.000210 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.228600; conceptual=0.760225; procedural=0.011175; metacognitive=0.000000 | conceptual | 0.760225 | 0.429917 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.880127; Medium=0.115650; Hard=0.004224 | Easy | 0.880127 | 0.350399 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999980; −Σp ln(p) = 0.000231; H = 0.000231/ln(3) = 0.000210; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.760225; −Σp ln(p) = 0.595992; H = 0.595992/ln(4) = 0.429917; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.880127; −Σp ln(p) = 0.384953; H = 0.384953/ln(3) = 0.350399; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Pengukuran Panjang dengan Satuan Baku
Tipe soal: multiple_choice
Stimulus: -
Soal: Ibu Meutia membeli kain untuk seragam. Terdapat 3 pesanan seragam dari sekolah kebangsaan. Ukuran panjang kain yang dibutuhkan untuk setiap seragam adalah 200 cm. Ibu Meutia memiliki kain dengan panjang 850 cm.

Berapakah panjang sisa kain Ibu Meutia?
Pilihan: A. 250 cm
B. 150 cm
C. 350 cm
D. 600 cm
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 22. Soal `08ecea23df04cbe525f37e73`

Ibu Meutia membeli kain untuk seragam. Terdapat 3 pesanan seragam dari sekolah kebangsaan. Ukuran panjang kain yang dibutuhkan untuk setiap seragam adalah 200 cm. Ibu Meutia memiliki kain dengan panjang 850 cm.<br><br>Apakah ada sisa kain yang dimiliki Ibu Meutia?

| Opsi | Isi |
|---|---|
| A | Tidak ada |
| B | Tidak dapat ditentukan |
| C | Ada, tetapi kurang dari kebutuhan satu seragam |
| D | Ada |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Total kebutuhan kain = 3 x 200 cm = 600 cm. Sisa kain = 850 cm - 600 cm = 250 cm. Karena 250 cm > 0, maka ada sisa kain.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5a51d4497b91da229ac27943bd94b965f3283cb7bc39418910c9329f515915a3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2369 |
| 2 | success | valid / verified | applying | procedural | Easy | 2415 |
| 3 | success | valid / verified | applying | procedural | Medium | 2430 |

Run 1 — solusi: Total kebutuhan kain = 3 seragam x 200 cm/seragam = 600 cm. Sisa kain = 850 cm - 600 cm = 250 cm. Karena 250 cm > 0, maka ada sisa kain.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi informasi yang relevan, melakukan perkalian untuk total kebutuhan, dan pengurangan untuk mencari sisa. Ini adalah penerapan prosedur matematika dasar dalam konteks rutin.. Bukti: 3 pesanan seragam; panjang kain yang dibutuhkan untuk setiap seragam adalah 200 cm; Ibu Meutia memiliki kain dengan panjang 850 cm; Apakah ada sisa kain
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma perkalian dan pengurangan (prosedural) untuk menyelesaikan masalah pengukuran panjang.. Bukti: 3 pesanan seragam; 200 cm; 850 cm
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena memerlukan dua langkah perhitungan (perkalian lalu pengurangan) yang saling terkait untuk mencapai jawaban, namun prosedurnya sangat familiar bagi siswa kelas 3.. Bukti: 3 pesanan seragam; 200 cm; 850 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian dasar dan pengurangan bilangan ratusan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah diajarkan perkalian dan pengurangan. Soal menuntut dua langkah logis (hitung total kebutuhan, lalu bandingkan dengan persediaan), yang merupakan standar untuk tingkat menengah di kelas 3. |

Run 2 — solusi: Total kebutuhan kain = 3 seragam x 200 cm/seragam = 600 cm. Sisa kain = 850 cm - 600 cm = 250 cm. Karena 250 cm > 0, maka ada sisa kain.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi informasi yang diberikan, melakukan operasi perkalian sederhana untuk total kebutuhan, dan operasi pengurangan untuk menentukan sisa. Ini adalah penerapan prosedur matematika dasar dalam konteks rutin.. Bukti: 3 pesanan seragam; panjang kain yang dibutuhkan untuk setiap seragam adalah 200 cm; Ibu Meutia memiliki kain dengan panjang 850 cm; Apakah ada sisa kain yang dimiliki Ibu Meutia?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi hitung (perkalian dan pengurangan) yang diterapkan pada masalah pengukuran panjang.. Bukti: 3 pesanan seragam; 200 cm; 850 cm
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena langkah-langkah penyelesaiannya sangat jelas dan rutin bagi siswa kelas 3. Siswa hanya perlu menghitung total kebutuhan (3x200) lalu membandingkannya dengan persediaan (850) melalui pengurangan. Tidak ada kendala yang saling berinteraksi atau kebutuhan untuk menyusun strategi non-rutin.. Bukti: 3 pesanan seragam; 200 cm; 850 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian dasar (1 digit x ratusan) dan pengurangan bilangan ratusan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi hitung yang digunakan (perkalian dan pengurangan) sesuai dengan kurikulum kelas 3. Masalah ini adalah aplikasi langsung dari konsep pengukuran dan operasi dasar. |

Run 3 — solusi: Kebutuhan total kain = 3 x 200 cm = 600 cm. Sisa kain = 850 cm - 600 cm = 250 cm. Karena 250 cm > 0, maka ada sisa kain.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi operasi perkalian untuk menentukan total kebutuhan kain (3 x 200 cm) dan operasi pengurangan untuk menentukan sisa (850 cm - 600 cm). Ini adalah penerapan prosedur matematika rutin dalam konteks sehari-hari.. Bukti: 3 pesanan seragam; panjang kain yang dibutuhkan untuk setiap seragam adalah 200 cm; Ibu Meutia memiliki kain dengan panjang 850 cm; Apakah ada sisa kain
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang konsep pengukuran panjang dan penggunaan algoritma perkalian serta pengurangan dalam situasi nyata.. Bukti: 3 pesanan seragam; panjang kain yang dibutuhkan untuk setiap seragam adalah 200 cm; Ibu Meutia memiliki kain dengan panjang 850 cm
- Intended difficulty `classify/Medium`: Soal ini memerlukan dua langkah perhitungan yang berurutan (perkalian lalu pengurangan) yang sudah familiar bagi siswa kelas 3. Jalur penyelesaian sangat jelas dan tidak memerlukan strategi non-rutin.. Bukti: 3 pesanan seragam; panjang kain yang dibutuhkan untuk setiap seragam adalah 200 cm; Ibu Meutia memiliki kain dengan panjang 850 cm

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian dasar (bilangan ratusan) dan pengurangan bilangan ratusan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah mempelajari perkalian dan pengurangan bilangan ratusan. Soal ini menuntut dua langkah perhitungan sederhana yang merupakan rutinitas standar di kelas 3. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4020`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur perkalian untuk menghitung total kebutuhan dan pengurangan untuk menentukan sisa. Ini adalah penerapan konsep matematika dasar dalam konteks rutin.
- Dimensi pengetahuan `procedural`: Soal menuntut penggunaan algoritma perkalian dan pengurangan (prosedural) untuk menyelesaikan masalah pengukuran panjang.
- Intended difficulty `Easy`: Soal ini tergolong Easy karena langkah-langkah penyelesaiannya sangat jelas dan rutin bagi siswa kelas 3. Siswa hanya perlu menghitung total kebutuhan (3x200) lalu membandingkannya dengan persediaan (850) melalui pengurangan. Tidak ada kendala yang saling berinteraksi atau kebutuhan untuk menyusun strategi non-rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian dasar (1 digit x ratusan) dan pengurangan bilangan ratusan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi hitung yang digunakan (perkalian dan pengurangan) sesuai dengan kurikulum kelas 3. Masalah ini adalah aplikasi langsung dari konsep pengukuran dan operasi dasar tanpa kompleksitas tambahan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 110/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000001; applying=0.999999; reasoning=0.000000 | applying | 0.999999 | 0.000009 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.041531; conceptual=0.942972; procedural=0.015497; metacognitive=0.000000 | conceptual | 0.942972 | 0.181830 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.825719; Medium=0.168748; Hard=0.005533 | Easy | 0.825719 | 0.443415 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999999; −Σp ln(p) = 0.000010; H = 0.000010/ln(3) = 0.000009; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.942972; −Σp ln(p) = 0.252069; H = 0.252069/ln(4) = 0.181830; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.825719; −Σp ln(p) = 0.487141; H = 0.487141/ln(3) = 0.443415; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Pengukuran Panjang dengan Satuan Baku
Tipe soal: multiple_choice
Stimulus: -
Soal: Ibu Meutia membeli kain untuk seragam. Terdapat 3 pesanan seragam dari sekolah kebangsaan. Ukuran panjang kain yang dibutuhkan untuk setiap seragam adalah 200 cm. Ibu Meutia memiliki kain dengan panjang 850 cm.

Apakah ada sisa kain yang dimiliki Ibu Meutia?
Pilihan: A. Tidak ada
B. Tidak dapat ditentukan
C. Ada, tetapi kurang dari kebutuhan satu seragam
D. Ada
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 23. Soal `1c5670f69b8db58e4f5e09c6`

Pada lomba 17 Agustusan, warga RT 005 mengadakan lomba balap karung. Panjang lintasan yang harus ditempuh 900 cm. Syarat pemenang lomba adalah peserta yang tercepat kembali ke tempat semula.<br><br>Berapa total panjang lintasan yang harus dilalui peserta lomba balap karung?

| Opsi | Isi |
|---|---|
| A | 450 cm |
| B | 1.800 cm |
| C | 900 cm |
| D | 2.700 cm |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Lintasan balap karung adalah pergi dan kembali. Total panjang = 900 cm (pergi) + 900 cm (kembali) = 1.800 cm.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `279b8b76acf3433f45c0038c8465dd1a066f8b46b1b26cbca1eb454ec734f5f3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2352 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2373 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2380 |

Run 1 — solusi: Lintasan balap karung adalah pergi dan kembali. Total panjang = 900 cm (pergi) + 900 cm (kembali) = 1.800 cm.
- Domain kognitif `classify/applying`: Siswa perlu memahami konteks 'kembali ke tempat semula' sebagai dua kali perjalanan (pergi dan pulang) dan menerapkan operasi perkalian atau penjumlahan berulang pada nilai yang diberikan.. Bukti: Syarat pemenang lomba adalah peserta yang tercepat kembali ke tempat semula.; Berapa total panjang lintasan yang harus dilalui peserta lomba balap karung?
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan konsep panjang lintasan dan hubungan logis antara perjalanan pergi dan kembali untuk menyelesaikan masalah.. Bukti: Panjang lintasan yang harus ditempuh 900 cm.; Syarat pemenang lomba adalah peserta yang tercepat kembali ke tempat semula.
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena siswa harus menginterpretasikan narasi 'kembali ke tempat semula' untuk menentukan operasi yang diperlukan (2 x 900), bukan sekadar membaca angka yang ada di soal.. Bukti: Panjang lintasan yang harus ditempuh 900 cm.; Syarat pemenang lomba adalah peserta yang tercepat kembali ke tempat semula.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang satuan panjang dan konsep dua kali perjalanan (pergi-pulang). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah mengenal satuan cm dan operasi perkalian dasar. Tantangan utama adalah memahami bahwa 'kembali' berarti menempuh jarak yang sama dua kali. |

Run 2 — solusi: Lintasan balap karung adalah pergi dan kembali, sehingga total jarak adalah 2 x 900 cm = 1.800 cm.
- Domain kognitif `classify/applying`: Siswa perlu memahami konteks 'kembali ke tempat semula' sebagai dua kali perjalanan (pergi dan pulang) dan menerapkan operasi perkalian atau penjumlahan berulang untuk mendapatkan total jarak.. Bukti: Syarat pemenang lomba adalah peserta yang tercepat kembali ke tempat semula.; Berapa total panjang lintasan yang harus dilalui peserta lomba balap karung?
- Dimensi pengetahuan `classify/conceptual`: Siswa menerapkan pemahaman konseptual tentang jarak tempuh pulang-pergi dalam konteks pengukuran panjang.. Bukti: Panjang lintasan yang harus ditempuh 900 cm.; Syarat pemenang lomba adalah peserta yang tercepat kembali ke tempat semula.
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena siswa harus menginterpretasikan teks untuk menyadari bahwa jarak total mencakup perjalanan pergi dan pulang (2x), bukan sekadar menghitung angka yang ada di soal. Ini memerlukan pemahaman hubungan antar informasi dalam soal.. Bukti: Panjang lintasan yang harus ditempuh 900 cm.; Syarat pemenang lomba adalah peserta yang tercepat kembali ke tempat semula.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang konsep jarak dan operasi perkalian/penjumlahan bilangan ratusan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 diharapkan mampu memahami konteks cerita sederhana. Kesulitan terletak pada interpretasi 'kembali ke tempat semula' yang menuntut siswa mengalikan jarak satu arah dengan dua, yang merupakan langkah logis tambahan di luar sekadar membaca angka. |

Run 3 — solusi: Lintasan balap karung adalah pergi dan kembali. Total panjang = 900 cm (pergi) + 900 cm (kembali) = 1.800 cm.
- Domain kognitif `classify/applying`: Siswa perlu memahami konteks 'kembali ke tempat semula' untuk menentukan bahwa jarak yang ditempuh adalah dua kali panjang lintasan. Ini melibatkan penerapan konsep dasar pada situasi rutin.. Bukti: Syarat pemenang lomba adalah peserta yang tercepat kembali ke tempat semula.; Berapa total panjang lintasan yang harus dilalui peserta lomba balap karung?
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan pemahaman konseptual tentang jarak tempuh pulang-pergi dan prosedur perkalian atau penjumlahan berulang.. Bukti: Panjang lintasan yang harus ditempuh 900 cm.; peserta yang tercepat kembali ke tempat semula
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium bagi kelas 3 karena siswa harus menginterpretasikan narasi 'kembali ke tempat semula' untuk menyimpulkan bahwa jarak harus dikalikan dua. Meskipun operasinya sederhana, terdapat langkah logika tambahan yang harus dilakukan siswa sebelum menghitung.. Bukti: Panjang lintasan yang harus ditempuh 900 cm.; Syarat pemenang lomba adalah peserta yang tercepat kembali ke tempat semula.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan ratusan atau perkalian dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah belajar panjang dan operasi hitung, namun soal menuntut pemahaman konteks 'pulang-pergi' yang merupakan langkah logika tambahan di luar sekadar menghitung angka yang tersedia. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 104/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000000 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.236612; conceptual=0.740796; procedural=0.022592; metacognitive=0.000000 | conceptual | 0.740796 | 0.468101 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.857178; Medium=0.139315; Hard=0.003508 | Easy | 0.857178 | 0.388235 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000000; H = 0.000000/ln(3) = 0.000000; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.740796; −Σp ln(p) = 0.648926; H = 0.648926/ln(4) = 0.468101; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.857178; −Σp ln(p) = 0.426520; H = 0.426520/ln(3) = 0.388235; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Hubungan Antarsatuan Baku Panjang
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada lomba 17 Agustusan, warga RT 005 mengadakan lomba balap karung. Panjang lintasan yang harus ditempuh 900 cm. Syarat pemenang lomba adalah peserta yang tercepat kembali ke tempat semula.

Berapa total panjang lintasan yang harus dilalui peserta lomba balap karung?
Pilihan: A. 450 cm
B. 1.800 cm
C. 900 cm
D. 2.700 cm
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 24. Soal `8daba6059f9c3edf55ee4254`

Pada lomba 17 Agustusan, warga RT 005 mengadakan lomba balap karung. Panjang lintasan yang harus ditempuh 900 cm. Syarat pemenang lomba adalah peserta yang tercepat kembali ke tempat semula.<br><br>Ubahlah satuan cm menjadi m!

| Opsi | Isi |
|---|---|
| A | 1,8 m |
| B | 9 m |
| C | 18 m |
| D | 180 m |

Kunci sumber: `C`; status AI: `conflict`; jawaban diverifikasi AI: `None`.
Solusi minimum hasil AI: Jika lintasan 900 cm, maka 900 cm = 9 m. Jika maksud soal adalah jarak pulang-pergi, maka 900 cm + 900 cm = 1800 cm = 18 m. Karena teks soal tidak menyebutkan perhitungan jarak pulang-pergi, kunci jawaban C (18 m) tidak dapat dibenarkan secara logis dari teks yang tersedia.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3c8ae75057f2fb788440b87573509131a661b1a7b35066405e4f73abcb6345fc`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | concern / conflict | knowing | procedural | Easy | 2359 |
| 2 | success | concern / conflict | knowing | procedural | Easy | 2392 |
| 3 | success | concern / conflict | knowing | procedural | Easy | 2429 |

Run 1 — solusi: Soal memiliki ketidaksesuaian data. Jika lintasan 900 cm, maka 900 cm = 9 m. Jika mengikuti kunci jawaban 18 m, maka lintasan seharusnya 1.800 cm. Karena data soal dan kunci bertentangan, solusi tidak dapat diverifikasi.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan konversi satuan panjang (cm ke m) yang merupakan prosedur standar yang dipelajari di kelas 3.. Bukti: Ubahlah satuan cm menjadi m!
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan antara satuan panjang (cm dan m) dan prosedur konversi antar satuan tersebut.. Bukti: Ubahlah satuan cm menjadi m!
- Intended difficulty `classify/Easy`: Konversi satuan panjang dasar (cm ke m) adalah materi rutin kelas 3. Namun, karena adanya kesalahan data pada soal (ketidaksesuaian angka antara soal dan kunci), tingkat kesulitan tidak dapat dinilai secara objektif.. Bukti: Panjang lintasan yang harus ditempuh 900 cm.; Ubahlah satuan cm menjadi m!

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman hubungan 1 m = 100 cm. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konversi satuan panjang dasar adalah prosedur rutin bagi siswa kelas 3. Kesalahan data pada soal tidak mengubah sifat prosedural dari tugas tersebut. |

Run 2 — solusi: Konversi 900 cm ke meter adalah 900 : 100 = 9 m. Kunci jawaban C (18 m) tidak sesuai dengan data soal yang tertulis (900 cm).
- Domain kognitif `classify/knowing`: Siswa diminta melakukan prosedur konversi satuan panjang yang bersifat langsung dan rutin bagi kelas 3.. Bukti: Ubahlah satuan cm menjadi m!
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan prosedur algoritme konversi satuan panjang (pembagian dengan 100).. Bukti: Ubahlah satuan cm menjadi m!
- Intended difficulty `classify/Easy`: Tugas ini adalah prosedur rutin satu langkah. Namun, karena terdapat konflik data antara soal dan kunci, tingkat kesulitan teknis menjadi tidak relevan untuk dinilai secara akurat.. Bukti: Panjang lintasan yang harus ditempuh 900 cm.; Ubahlah satuan cm menjadi m!

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman hubungan 1 m = 100 cm. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konversi satuan panjang dasar adalah materi standar kelas 3. Prosedur ini sangat rutin. |

Run 3 — solusi: Jika mengikuti teks soal (900 cm), maka 900 cm = 9 m. Jika mengikuti logika kunci jawaban (jarak pulang-pergi), maka 900 cm + 900 cm = 1.800 cm = 18 m. Karena soal tidak meminta total jarak pulang-pergi, kunci C tidak valid berdasarkan teks yang diberikan.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan konversi satuan panjang sederhana dari cm ke m. Ini adalah prosedur langsung yang sudah dipelajari di kelas 3.. Bukti: Ubahlah satuan cm menjadi m!
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang hubungan antar satuan baku panjang (konversi cm ke m), yang merupakan pengetahuan prosedural.. Bukti: Ubahlah satuan cm menjadi m!
- Intended difficulty `classify/Easy`: Secara prosedural, konversi 900 cm ke m adalah tugas rutin bagi siswa kelas 3. Namun, karena adanya ambiguitas antara teks soal dan logika kunci jawaban (yang mengasumsikan jarak pulang-pergi), tingkat kesulitan menjadi tidak relevan karena soal cacat secara konten.. Bukti: Panjang lintasan yang harus ditempuh 900 cm.; Ubahlah satuan cm menjadi m!

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman hubungan 100 cm = 1 m. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Konversi satuan panjang adalah materi standar kelas 3. Soal ini hanya memerlukan satu langkah pembagian sederhana (atau pemindahan koma). |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3833`.
Konten: `concern`; kunci: `conflict`; masalah: Terdapat ketidaksesuaian antara data pada soal (900 cm) dengan kunci jawaban (18 m).; Soal menyebutkan panjang lintasan 900 cm, namun kunci jawaban mengasumsikan jarak pulang-pergi (900 cm + 900 cm = 1800 cm = 18 m) tanpa menyatakan secara eksplisit dalam teks soal bahwa siswa harus menghitung jarak total pulang-pergi.; Soal ambigu karena tidak jelas apakah yang diminta adalah konversi lintasan satu arah atau total jarak tempuh lomba..
- Domain kognitif `knowing`: Siswa diminta melakukan konversi satuan panjang (cm ke m), yang merupakan prosedur standar dan langsung bagi siswa kelas 3.
- Dimensi pengetahuan `procedural`: Soal menguji penerapan algoritme konversi satuan panjang baku (pembagian dengan 100), yang merupakan pengetahuan prosedural.
- Intended difficulty `Easy`: Secara prosedural, konversi satuan panjang adalah tugas rutin kelas 3. Namun, karena soal cacat secara konten (ambiguitas antara data soal dan kunci), tingkat kesulitan teknis tidak dapat dinilai secara objektif.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman hubungan 1 m = 100 cm. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konversi satuan panjang dasar adalah prosedur rutin bagi siswa kelas 3. Kesalahan data pada soal tidak mengubah sifat prosedural dari tugas tersebut. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 97/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |

<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Hubungan Antarsatuan Baku Panjang
Tipe soal: multiple_choice
Stimulus: -
Soal: Pada lomba 17 Agustusan, warga RT 005 mengadakan lomba balap karung. Panjang lintasan yang harus ditempuh 900 cm. Syarat pemenang lomba adalah peserta yang tercepat kembali ke tempat semula.

Ubahlah satuan cm menjadi m!
Pilihan: A. 1,8 m
B. 9 m
C. 18 m
D. 180 m
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `revision_required`.
Status konten: `concern`. Catatan konten: Terdapat ketidaksesuaian antara data pada soal (900 cm) dengan kunci jawaban (18 m).; Soal menyebutkan panjang lintasan 900 cm, namun kunci jawaban mengasumsikan jarak pulang-pergi (900 cm + 900 cm = 1800 cm = 18 m) tanpa menyatakan secara eksplisit dalam teks soal bahwa siswa harus menghitung jarak total pulang-pergi.; Soal ambigu karena tidak jelas apakah yang diminta adalah konversi lintasan satu arah atau total jarak tempuh lomba..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "knowing", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "procedural", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 25. Soal `a258009ba2d7730a91f12d2e`

Meutia menimbang tepung untuk bahan membuat kue. Timbangan yang digunakan adalah timbangan duduk dengan satuan kg. Meutia meletakkan tepung dan jarum timbangan menunjuk angka 4 kurang 3 garis. Berapa berat tepung yang ditimbang Meutia?

| Opsi | Isi |
|---|---|
| A | 3 kg 970 gram |
| B | 4 kg 300 gram |
| C | 3 kg 700 gram |
| D | 3 kg 300 gram |

![Gambar sumber soal 25](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0151-11.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Satu satuan kg pada timbangan terbagi menjadi 10 garis kecil, sehingga 1 garis = 100 gram. Posisi jarum pada '4 kg kurang 3 garis' berarti 4 kg - (3 x 100 gram) = 4 kg - 300 gram = 3 kg 700 gram.
Gambar sumber: images/kelas3_panduan_siswa_kelas3.pdf-0151-11.png. Transkripsi visual: Gambar menunjukkan timbangan duduk analog dengan piringan di atasnya berisi tepung. Dial timbangan memiliki angka 0 sampai 11. Jarum timbangan menunjuk ke posisi di antara angka 3 dan 4, tepatnya 3 garis kecil sebelum angka 4.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d70a6b4478417a3a488741d37ac97e9fd7b4813d46a6ff2367144660bfb57a07`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 3670 |
| 2 | success | valid / verified | applying | procedural | Medium | 3585 |
| 3 | success | valid / verified | applying | conceptual | Medium | 3644 |

Run 1 — solusi: Satu satuan kg dibagi menjadi 10 garis kecil, sehingga 1 garis = 100 gram. Jarum berada 3 garis sebelum angka 4 kg. Berat = 4 kg - (3 x 100 gram) = 4 kg - 300 gram = 3 kg 700 gram.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasikan skala timbangan (membaca representasi visual) dan menerapkan konversi satuan sederhana (1 kg = 1000 gram) untuk menentukan nilai berat yang ditunjukkan. Ini adalah penerapan konsep pengukuran pada konteks rutin.. Bukti: jarum timbangan menunjuk angka 4 kurang 3 garis; Setiap 1 kg pada dial terbagi 10 garis kecil (tiap garis = 100 gram)
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang cara membaca skala timbangan analog dan hubungan antara satuan kilogram dan gram dalam konteks pengukuran berat.. Bukti: timbangan duduk dengan satuan kg; jarum timbangan menunjuk angka 4 kurang 3 garis
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan interpretasi visual skala (membaca garis) dan operasi pengurangan yang melibatkan konversi satuan (4 kg - 300 gram). Siswa harus memahami bahwa 1 kg = 1000 gram dan setiap garis bernilai 100 gram, yang merupakan langkah-langkah yang saling terkait.. Bukti: jarum timbangan menunjuk angka 4 kurang 3 garis; Setiap 1 kg pada dial terbagi 10 garis kecil

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang satuan berat (kg ke gram) dan kemampuan membaca skala timbangan analog. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, membaca skala timbangan dengan subdivisi (garis kecil) dan melakukan konversi satuan adalah tuntutan yang sesuai untuk tingkat Medium, karena memerlukan ketelitian dalam interpretasi visual dan operasi hitung. |

Run 2 — solusi: Satu satuan kg pada timbangan terbagi menjadi 10 garis kecil, sehingga 1 garis = 100 gram. Posisi jarum pada '4 kurang 3 garis' berarti 4 kg - (3 x 100 gram) = 4 kg - 300 gram = 3 kg 700 gram.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman tentang skala timbangan (konsep 1 kg = 1000 gram dan pembagian skala) untuk menginterpretasikan posisi jarum. Ini adalah penerapan prosedur pengukuran pada konteks rutin.. Bukti: jarum timbangan menunjuk angka 4 kurang 3 garis; Setiap 1 kg pada dial terbagi 10 garis kecil
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara membaca skala timbangan dan melakukan konversi satuan berat sederhana.. Bukti: timbangan duduk dengan satuan kg; Setiap 1 kg pada dial terbagi 10 garis kecil
- Intended difficulty `classify/Medium`: Soal ini memerlukan interpretasi visual terhadap skala timbangan dan operasi pengurangan sederhana. Siswa harus memahami hubungan antara angka utama dan garis-garis kecil (skala). Ini adalah tugas rutin bagi kelas 3.. Bukti: jarum timbangan menunjuk angka 4 kurang 3 garis; Setiap 1 kg pada dial terbagi 10 garis kecil

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar satuan berat (kg ke gram) dan membaca skala timbangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah mempelajari pengukuran berat. Membaca skala yang tidak tepat pada angka bulat memerlukan ketelitian, namun prosedurnya standar. |

Run 3 — solusi: Satu satuan kg dibagi menjadi 10 garis, sehingga 1 garis = 100 gram. Posisi jarum di '4 kg kurang 3 garis' berarti 4 kg - (3 x 100 gram) = 4 kg - 300 gram = 3 kg 700 gram.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasikan skala timbangan (membaca representasi visual) dan menerapkan konversi satuan sederhana (1 kg = 1000 gram) untuk menentukan nilai berat yang ditunjukkan. Ini adalah penerapan konsep pengukuran pada konteks rutin.. Bukti: jarum timbangan menunjuk angka 4 kurang 3 garis; Setiap 1 kg pada dial terbagi 10 garis kecil (tiap garis = 100 gram)
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami hubungan antara satuan kg dan gram serta struktur skala pada alat ukur (konsep pengukuran berat).. Bukti: timbangan duduk dengan satuan kg; jarum timbangan menunjuk angka 4 kurang 3 garis
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa membaca skala yang tidak tepat pada angka bulat. Siswa harus memahami bahwa 1 kg = 1000 gram dan membagi 1000 dengan 10 garis untuk mendapatkan nilai per garis (100 gram). Meskipun prosedurnya rutin, ini memerlukan pemahaman konsep skala yang sedikit lebih dalam daripada sekadar membaca angka bulat.. Bukti: jarum timbangan menunjuk angka 4 kurang 3 garis; Setiap 1 kg pada dial terbagi 10 garis kecil

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar satuan berat (kg ke gram) dan kemampuan membaca skala timbangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, membaca timbangan dengan skala tidak bulat (kurang dari angka tertentu) merupakan tantangan menengah yang menguji pemahaman konsep pengukuran, bukan sekadar membaca angka. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `5367`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menginterpretasikan skala timbangan (membaca representasi visual) dan menerapkan konversi satuan sederhana (1 kg = 1000 gram) untuk menentukan nilai berat yang ditunjukkan. Ini adalah penerapan konsep pengukuran pada konteks rutin.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang cara membaca skala timbangan analog dan hubungan antara satuan kilogram dan gram dalam konteks pengukuran berat.
- Intended difficulty `Medium`: Soal ini menuntut siswa membaca skala yang tidak tepat pada angka bulat. Siswa harus memahami bahwa 1 kg = 1000 gram dan membagi 1000 dengan 10 garis untuk mendapatkan nilai per garis (100 gram). Meskipun prosedurnya rutin, ini memerlukan pemahaman konsep skala yang sedikit lebih dalam daripada sekadar membaca angka bulat.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar satuan berat (kg ke gram) dan kemampuan membaca skala timbangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, membaca timbangan dengan skala tidak bulat (kurang dari angka tertentu) merupakan tantangan menengah yang menguji pemahaman konsep pengukuran, bukan sekadar membaca angka. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 146/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000018; applying=0.999982; reasoning=0.000000 | applying | 0.999982 | 0.000196 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.049458; conceptual=0.940273; procedural=0.010269; metacognitive=0.000000 | conceptual | 0.940273 | 0.182952 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.742431; Medium=0.251017; Hard=0.006552 | Easy | 0.742431 | 0.547073 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999982; −Σp ln(p) = 0.000215; H = 0.000215/ln(3) = 0.000196; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.940273; −Σp ln(p) = 0.253626; H = 0.253626/ln(4) = 0.182952; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.742431; −Σp ln(p) = 0.601021; H = 0.601021/ln(3) = 0.547073; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Pengukuran Berat dengan Satuan Baku
Tipe soal: multiple_choice
Stimulus: -
Soal: Meutia menimbang tepung untuk bahan membuat kue. Timbangan yang digunakan adalah timbangan duduk dengan satuan kg. Meutia meletakkan tepung dan jarum timbangan menunjuk angka 4 kurang 3 garis. Berapa berat tepung yang ditimbang Meutia?
Pilihan: A. 3 kg 970 gram
B. 4 kg 300 gram
C. 3 kg 700 gram
D. 3 kg 300 gram
Transkripsi visual: Gambar menunjukkan timbangan duduk analog dengan piringan di atasnya berisi tepung. Dial timbangan memiliki angka 0 sampai 11. Jarum timbangan menunjuk ke posisi di antara angka 3 dan 4, tepatnya 3 garis kecil sebelum angka 4.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 26. Soal `e35b2320cf47f2b1b2b92fc9`

Drio memiliki 10 kantong plastik berisi buah apel untuk dijual. Setiap plastik memiliki berat 3 kg. Buah apel yang terjual sebanyak 18 kg. Berapa sisa buah apel yang belum terjual?

| Opsi | Isi |
|---|---|
| A | 12 kg |
| B | 17 kg |
| C | 15 kg |
| D | 30 kg |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Total berat = 10 kantong x 3 kg = 30 kg. Sisa = 30 kg - 18 kg = 12 kg.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c6df02c39fa01de828cac32d8ec6350d90daa49e62c9be0ea2c580cbaa2c23f0`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2357 |
| 2 | success | valid / verified | applying | procedural | Medium | 2391 |
| 3 | success | valid / verified | applying | procedural | Easy | 2363 |

Run 1 — solusi: Total berat apel = 10 kantong x 3 kg/kantong = 30 kg. Sisa apel = 30 kg - 18 kg = 12 kg.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep perkalian untuk mencari total berat dan pengurangan untuk mencari sisa. Ini adalah penerapan prosedur rutin pada konteks soal cerita yang umum di kelas 3.. Bukti: Drio memiliki 10 kantong plastik berisi buah apel untuk dijual. Setiap plastik memiliki berat 3 kg.; Buah apel yang terjual sebanyak 18 kg. Berapa sisa buah apel yang belum terjual?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritme perkalian dan pengurangan dalam konteks pengukuran berat.. Bukti: 10 kantong plastik berisi buah apel; Setiap plastik memiliki berat 3 kg; Buah apel yang terjual sebanyak 18 kg
- Intended difficulty `classify/Medium`: Soal ini melibatkan dua langkah operasi dasar (perkalian dan pengurangan) yang saling terkait. Jalur penyelesaian sangat jelas dan familiar bagi siswa kelas 3.. Bukti: 10 kantong plastik berisi buah apel; Setiap plastik memiliki berat 3 kg; Buah apel yang terjual sebanyak 18 kg

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian dasar (10x3) dan pengurangan bilangan dua angka (30-18). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah mempelajari perkalian dan pengurangan. Soal ini menuntut dua langkah berurutan yang merupakan standar kompetensi kelas 3, namun tidak memerlukan strategi non-rutin atau perencanaan yang kompleks. |

Run 2 — solusi: Total berat apel = 10 kantong x 3 kg/kantong = 30 kg. Sisa apel = 30 kg - 18 kg = 12 kg.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur perkalian untuk mencari total berat, kemudian menerapkan prosedur pengurangan untuk mencari sisa. Ini adalah penerapan konsep dasar pada konteks rutin.. Bukti: Drio memiliki 10 kantong plastik berisi buah apel; Setiap plastik memiliki berat 3 kg; Buah apel yang terjual sebanyak 18 kg; Berapa sisa buah apel yang belum terjual?
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penggunaan algoritme perkalian dan pengurangan (prosedural) untuk menyelesaikan masalah pengukuran berat.. Bukti: 10 kantong plastik; berat 3 kg; terjual sebanyak 18 kg
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena melibatkan dua langkah operasional yang saling terkait (perkalian lalu pengurangan). Siswa harus memahami hubungan antara jumlah kantong, berat per kantong, dan total berat sebelum melakukan pengurangan. Meskipun prosedurnya rutin, ketergantungan langkah ini memberikan tuntutan sedang bagi siswa kelas 3.. Bukti: 10 kantong plastik berisi buah apel; Setiap plastik memiliki berat 3 kg; Buah apel yang terjual sebanyak 18 kg

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian dasar (10x3) dan pengurangan bilangan dua angka. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah mempelajari perkalian dan pengurangan. Soal ini menuntut dua langkah berurutan yang logis, yang merupakan standar menengah untuk tingkat kelas ini. |

Run 3 — solusi: Total berat apel = 10 kantong x 3 kg/kantong = 30 kg. Sisa apel = 30 kg - 18 kg = 12 kg.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi operasi perkalian untuk mencari total berat, kemudian operasi pengurangan untuk mencari sisa. Ini adalah penerapan prosedur rutin pada konteks soal cerita yang umum bagi kelas 3.. Bukti: Drio memiliki 10 kantong plastik berisi buah apel untuk dijual. Setiap plastik memiliki berat 3 kg.; Buah apel yang terjual sebanyak 18 kg. Berapa sisa buah apel yang belum terjual?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang konsep perkalian sebagai penjumlahan berulang dan pengurangan dalam konteks pengukuran berat, yang merupakan pengetahuan prosedural.. Bukti: 10 kantong plastik berisi buah apel; Setiap plastik memiliki berat 3 kg; terjual sebanyak 18 kg
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena alur penyelesaiannya sangat jelas dan rutin bagi siswa kelas 3. Siswa hanya perlu melakukan dua langkah operasi dasar (perkalian dan pengurangan) tanpa kendala yang saling berinteraksi atau kebutuhan untuk memilih strategi yang kompleks.. Bukti: 10 kantong plastik berisi buah apel untuk dijual. Setiap plastik memiliki berat 3 kg.; Buah apel yang terjual sebanyak 18 kg.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian dasar (10x3) dan pengurangan bilangan dua angka. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi perkalian 10x3 dan pengurangan 30-18 adalah standar kompetensi kelas 3. Tidak ada jebakan atau kompleksitas tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3939`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur perkalian untuk menentukan total berat, kemudian menerapkan prosedur pengurangan untuk menentukan sisa. Ini adalah penerapan konsep matematika dasar pada konteks rutin.
- Dimensi pengetahuan `procedural`: Soal ini menguji penguasaan algoritme perkalian dan pengurangan dalam konteks pengukuran berat.
- Intended difficulty `Easy`: Soal ini tergolong Easy karena alur penyelesaiannya sangat jelas dan rutin bagi siswa kelas 3. Siswa hanya perlu melakukan dua langkah operasi dasar (perkalian dan pengurangan) tanpa kendala yang saling berinteraksi atau kebutuhan untuk memilih strategi yang kompleks.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Perkalian dasar (10x3) dan pengurangan bilangan dua angka. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi perkalian 10x3 dan pengurangan 30-18 adalah standar kompetensi kelas 3. Tidak ada jebakan atau kompleksitas tambahan yang menuntut perencanaan tinggi. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 88/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.063860; applying=0.936140; reasoning=0.000000 | applying | 0.936140 | 0.216144 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.290610; conceptual=0.692167; procedural=0.017223; metacognitive=0.000000 | conceptual | 0.692167 | 0.493220 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.866309; Medium=0.130889; Hard=0.002802 | Easy | 0.866309 | 0.370420 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.936140; −Σp ln(p) = 0.237459; H = 0.237459/ln(3) = 0.216144; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.692167; −Σp ln(p) = 0.683748; H = 0.683748/ln(4) = 0.493220; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.866309; −Σp ln(p) = 0.406948; H = 0.406948/ln(3) = 0.370420; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Pengukuran Berat dengan Satuan Baku
Tipe soal: multiple_choice
Stimulus: -
Soal: Drio memiliki 10 kantong plastik berisi buah apel untuk dijual. Setiap plastik memiliki berat 3 kg. Buah apel yang terjual sebanyak 18 kg. Berapa sisa buah apel yang belum terjual?
Pilihan: A. 12 kg
B. 17 kg
C. 15 kg
D. 30 kg
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 27. Soal `1a9d9923445f71c78d74086d`

Sebuah karung berisi 90 kg 460 gram beras dan karung lainnya berisi 25 kg 380 gram beras. Berapa berat beras dalam kedua karung tersebut?

| Opsi | Isi |
|---|---|
| A | 65 kg 840 gram |
| B | 115 kg 740 gram |
| C | 115 kg 840 gram |
| D | 116 kg 840 gram |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Jumlahkan kilogram: 90 kg + 25 kg = 115 kg. Jumlahkan gram: 460 g + 380 g = 840 g. Total: 115 kg 840 gram.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c4cf597273cd24aecc63808f79a9c1e3c725db70ae19f669abd5207b18b51685`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2390 |
| 2 | success | valid / verified | applying | procedural | Easy | 2404 |
| 3 | success | valid / verified | applying | procedural | Easy | 2396 |

Run 1 — solusi: Jumlahkan kilogram: 90 kg + 25 kg = 115 kg. Jumlahkan gram: 460 g + 380 g = 840 g. Total: 115 kg 840 g.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur penjumlahan standar pada satuan berat yang berbeda (kg dan gram). Prosedur ini rutin dan langsung, sehingga masuk dalam domain applying.. Bukti: Sebuah karung berisi 90 kg 460 gram beras dan karung lainnya berisi 25 kg 380 gram beras. Berapa berat beras dalam kedua karung tersebut?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma penjumlahan bilangan dengan satuan campuran, yang merupakan bagian dari pengetahuan prosedural.. Bukti: 90 kg 460 gram; 25 kg 380 gram
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena melibatkan penjumlahan dua satuan yang berbeda (kg dan gram) yang memerlukan ketelitian dalam menjumlahkan bagian gram (460+380=840) dan kilogram secara terpisah. Meskipun prosedurnya rutin, siswa harus mengelola dua komponen satuan secara bersamaan.. Bukti: 90 kg 460 gram; 25 kg 380 gram; Berapa berat beras dalam kedua karung tersebut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah hingga 1000 dan pemahaman dasar satuan berat. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, menjumlahkan satuan campuran (kg dan gram) adalah materi yang sesuai. Kesalahan pada distractor menunjukkan pengecoh yang umum terjadi pada operasi penjumlahan dengan penyimpanan atau kesalahan penjumlahan sederhana. |

Run 2 — solusi: Jumlahkan kilogram dengan kilogram (90+25=115 kg) dan gram dengan gram (460+380=840 gram). Hasilnya adalah 115 kg 840 gram.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur penjumlahan satuan berat (kg dan gram) yang sudah dipelajari di kelas 3. Soal ini merupakan penerapan langsung dari konsep penjumlahan satuan baku dalam konteks rutin.. Bukti: 90 kg 460 gram beras dan karung lainnya berisi 25 kg 380 gram beras; Berapa berat beras dalam kedua karung tersebut?
- Dimensi pengetahuan `classify/procedural`: Siswa perlu memahami algoritme penjumlahan bersusun atau penjumlahan terpisah untuk satuan berat (kg dan gram), yang merupakan bagian dari pengetahuan prosedural.. Bukti: 90 kg 460 gram; 25 kg 380 gram
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu melakukan penjumlahan dua bilangan dengan satuan yang sama (kg dengan kg, gram dengan gram) tanpa perlu melakukan konversi satuan (karena jumlah gram tidak melebihi 1000). Jalur penyelesaian sangat jelas dan rutin.. Bukti: 90 kg 460 gram; 25 kg 380 gram; Berapa berat beras dalam kedua karung tersebut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah dan pemahaman satuan berat (kg dan gram). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan satuan berat tanpa konversi (karena 460+380 < 1000) adalah materi standar kelas 3 yang bersifat rutin. |

Run 3 — solusi: Jumlahkan kilogram: 90 kg + 25 kg = 115 kg. Jumlahkan gram: 460 g + 380 g = 840 g. Total: 115 kg 840 gram.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur penjumlahan satuan berat (kg dan gram) yang sudah dipelajari di kelas 3. Prosedur ini rutin dan langsung.. Bukti: 90 kg 460 gram beras dan karung lainnya berisi 25 kg 380 gram beras; Berapa berat beras dalam kedua karung tersebut?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman tentang algoritma penjumlahan satuan berat yang terpisah (kg dengan kg, gram dengan gram), yang merupakan prosedur standar.. Bukti: 90 kg 460 gram; 25 kg 380 gram
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena merupakan penerapan langsung prosedur penjumlahan satuan berat yang familiar bagi siswa kelas 3. Tidak ada kendala yang berinteraksi atau kebutuhan untuk konversi satuan yang kompleks (karena jumlah gram tidak melebihi 1000g).. Bukti: 90 kg 460 gram; 25 kg 380 gram; Berapa berat beras dalam kedua karung tersebut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah dan pemahaman satuan berat kg dan gram. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan satuan berat adalah materi standar kelas 3. Soal ini tidak memerlukan konversi satuan (misal: gram ke kg) karena hasil penjumlahan gram (840) kurang dari 1000, sehingga langkah penyelesaian sangat langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Medium": 1, "Easy": 2} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4007`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan prosedur penjumlahan standar pada satuan berat yang berbeda (kg dan gram). Prosedur ini rutin dan langsung, sehingga masuk dalam domain applying.
- Dimensi pengetahuan `procedural`: Soal menguji pemahaman tentang algoritma penjumlahan bilangan dengan satuan campuran, yang merupakan bagian dari pengetahuan prosedural.
- Intended difficulty `Easy`: Soal ini tergolong Easy karena merupakan penerapan langsung prosedur penjumlahan satuan berat yang familiar bagi siswa kelas 3. Tidak ada konversi satuan yang diperlukan karena hasil penjumlahan gram (840) tidak melebihi 1000 gram, sehingga jalur penyelesaian sangat langsung dan rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah dan pemahaman satuan berat (kg dan gram). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan satuan berat tanpa konversi (karena 460+380 < 1000) adalah materi standar kelas 3 yang bersifat rutin dan langsung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 93/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.007821; applying=0.992179; reasoning=0.000000 | applying | 0.992179 | 0.041626 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.221338; conceptual=0.763077; procedural=0.015585; metacognitive=0.000000 | conceptual | 0.763077 | 0.436402 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.905865; Medium=0.091473; Hard=0.002662 | Easy | 0.905865 | 0.295026 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.992179; −Σp ln(p) = 0.045731; H = 0.045731/ln(3) = 0.041626; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.763077; −Σp ln(p) = 0.604981; H = 0.604981/ln(4) = 0.436402; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.905865; −Σp ln(p) = 0.324119; H = 0.324119/ln(3) = 0.295026; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Hubungan Antarsatuan Baku Berat
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah karung berisi 90 kg 460 gram beras dan karung lainnya berisi 25 kg 380 gram beras. Berapa berat beras dalam kedua karung tersebut?
Pilihan: A. 65 kg 840 gram
B. 115 kg 740 gram
C. 115 kg 840 gram
D. 116 kg 840 gram
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 28. Soal `23dc07e9d3dc8f5423d3bb7e`

Meutia memiliki satu pohon mangga. Dari hasil panennya, Meutia mendapatkan 8.000 gram mangga. Kemudian Meutia menjual mangga tersebut sebanyak 4 kg. Berapa sisa mangga yang belum terjual?

| Opsi | Isi |
|---|---|
| A | 8.000 gram |
| B | 4.000 gram (4 kg) |
| C | 4.400 gram |
| D | 12.000 gram |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Konversi 4 kg menjadi 4.000 gram. Sisa mangga = 8.000 gram - 4.000 gram = 4.000 gram.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `05888d1cee6c0e23691449899112282332698e33b34cdfde4090f1a70751d9d6`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2299 |
| 2 | success | valid / verified | applying | procedural | Medium | 2282 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2233 |

Run 1 — solusi: Konversi 8.000 gram menjadi 8 kg (atau 4 kg menjadi 4.000 gram). Sisa mangga = 8 kg - 4 kg = 4 kg (atau 8.000 gram - 4.000 gram = 4.000 gram).
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi perbedaan satuan (gram dan kg), melakukan konversi satuan berat, dan menerapkan operasi pengurangan untuk menemukan sisa. Ini adalah penerapan konsep dalam konteks rutin.. Bukti: 8.000 gram mangga; menjual mangga tersebut sebanyak 4 kg; Berapa sisa mangga yang belum terjual?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman tentang hubungan antarsatuan berat (konversi gram ke kg atau sebaliknya) dan prosedur pengurangan.. Bukti: 8.000 gram; 4 kg
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa kelas 3 harus melakukan konversi satuan sebelum melakukan pengurangan. Meskipun prosedurnya rutin, terdapat dua langkah yang saling bergantung (konversi dan operasi hitung) yang meningkatkan tuntutan kognitif dibandingkan soal satu langkah langsung.. Bukti: 8.000 gram; 4 kg; Berapa sisa mangga

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konversi satuan berat (1 kg = 1.000 gram) dan operasi pengurangan bilangan ribuan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah mempelajari konversi satuan berat. Mengharuskan siswa menyamakan satuan sebelum mengurangkan adalah tuntutan yang sesuai untuk tingkat kesulitan menengah di kelas 3. |

Run 2 — solusi: Konversi 8.000 gram menjadi 8 kg (atau 4 kg menjadi 4.000 gram). Sisa mangga = 8 kg - 4 kg = 4 kg (atau 8.000 gram - 4.000 gram = 4.000 gram).
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi perbedaan satuan (gram dan kg), melakukan konversi satuan berat yang merupakan prosedur standar, lalu melakukan operasi pengurangan. Ini adalah penerapan konsep pada konteks rutin.. Bukti: 8.000 gram mangga; menjual mangga tersebut sebanyak 4 kg; Berapa sisa mangga yang belum terjual?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut pemahaman tentang hubungan antarsatuan berat (gram ke kg) dan penggunaan algoritma pengurangan.. Bukti: 8.000 gram; 4 kg
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena menuntut siswa melakukan konversi satuan sebelum melakukan operasi pengurangan. Meskipun prosedurnya familiar, siswa harus menyadari perlunya kesamaan satuan sebagai kendala sebelum menghitung.. Bukti: 8.000 gram; 4 kg; Berapa sisa mangga

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konversi satuan berat (1 kg = 1.000 gram) dan operasi pengurangan bilangan ribuan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah mempelajari konversi satuan berat dan pengurangan. Langkah konversi adalah prasyarat wajib yang membuat soal ini sedikit lebih menantang daripada sekadar pengurangan langsung. |

Run 3 — solusi: Konversi 8.000 gram menjadi 8 kg. Sisa mangga = 8 kg - 4 kg = 4 kg. Karena 4 kg = 4.000 gram, maka jawabannya 4.000 gram.
- Domain kognitif `classify/applying`: Siswa perlu mengonversi satuan berat (gram ke kg atau sebaliknya) sebelum melakukan operasi pengurangan. Ini adalah penerapan konsep satuan baku pada konteks rutin.. Bukti: 8.000 gram mangga; menjual mangga tersebut sebanyak 4 kg; Berapa sisa mangga yang belum terjual?
- Dimensi pengetahuan `classify/conceptual`: Soal menuntut pemahaman hubungan antarsatuan berat (gram dan kilogram) dan prosedur pengurangan.. Bukti: 8.000 gram; 4 kg
- Intended difficulty `classify/Medium`: Soal memerlukan konversi satuan sebelum pengurangan. Meskipun melibatkan dua langkah (konversi dan pengurangan), prosedurnya sangat rutin dan familiar bagi siswa kelas 3.. Bukti: 8.000 gram; 4 kg; Berapa sisa mangga

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konversi satuan berat (1 kg = 1.000 gram) dan operasi pengurangan bilangan ribuan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah mempelajari hubungan antar satuan berat. Langkah konversi dan pengurangan adalah standar untuk tingkat ini. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3888`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur konversi satuan berat (gram ke kg atau sebaliknya) dan operasi pengurangan dalam konteks rutin. Ini adalah penerapan konsep yang sudah dipelajari.
- Dimensi pengetahuan `procedural`: Soal menuntut pemahaman tentang hubungan antarsatuan berat (gram dan kilogram) dan penggunaan algoritma pengurangan.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena menuntut siswa melakukan konversi satuan sebelum melakukan pengurangan. Meskipun prosedurnya rutin, terdapat dua langkah yang saling bergantung (konversi dan operasi hitung) yang meningkatkan tuntutan kognitif dibandingkan soal satu langkah langsung.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konversi satuan berat (1 kg = 1.000 gram) dan operasi pengurangan bilangan ribuan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah mempelajari konversi satuan berat. Mengharuskan siswa menyamakan satuan sebelum mengurangkan adalah tuntutan yang sesuai untuk tingkat kesulitan menengah di kelas 3. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 107/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000004 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.058422; conceptual=0.931595; procedural=0.009983; metacognitive=0.000000 | conceptual | 0.931595 | 0.200479 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.876315; Medium=0.120015; Hard=0.003670 | Easy | 0.876315 | 0.355657 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000005; H = 0.000005/ln(3) = 0.000004; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.931595; −Σp ln(p) = 0.277922; H = 0.277922/ln(4) = 0.200479; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.876315; −Σp ln(p) = 0.390729; H = 0.390729/ln(3) = 0.355657; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Hubungan Antarsatuan Baku Berat
Tipe soal: multiple_choice
Stimulus: -
Soal: Meutia memiliki satu pohon mangga. Dari hasil panennya, Meutia mendapatkan 8.000 gram mangga. Kemudian Meutia menjual mangga tersebut sebanyak 4 kg. Berapa sisa mangga yang belum terjual?
Pilihan: A. 8.000 gram
B. 4.000 gram (4 kg)
C. 4.400 gram
D. 12.000 gram
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 29. Soal `dd3cb9360df4fe034e2f2480`

Urutkan gambar sesuai dengan waktu kegiatan.<br><br>Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).

| Opsi | Isi |
|---|---|
| A | bangun tidur, menyikat gigi, makan siang, bermain bola |
| B | menyikat gigi, bangun tidur, makan siang, bermain bola |
| C | bangun tidur, makan siang, menyikat gigi, bermain bola |
| D | bermain bola, makan siang, menyikat gigi, bangun tidur |

![Gambar sumber soal 29](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0198-04.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Mengurutkan kegiatan berdasarkan waktu pada jam: bangun tidur (06.00) -> menyikat gigi (08.00) -> makan siang (12.00) -> bermain bola (16.00). Urutan yang benar adalah C, D, B, A.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0198-04.png. Transkripsi visual: Empat gambar kegiatan dengan jam: Gambar C (bangun tidur, jam 6:00), Gambar D (menyikat gigi, jam 8:00), Gambar B (makan siang, jam 12:00), Gambar A (bermain bola, jam 4:00). Urutan kronologis berdasarkan waktu pada jam adalah C, D, B, A.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `17b235a4a103a607662c78e33232a4f3f9d32dce40c8b6dce2d570a24b35adf1`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3491 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3471 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3479 |

Run 1 — solusi: Mengurutkan kegiatan berdasarkan waktu pada jam: bangun tidur (06.00) -> menyikat gigi (08.00) -> makan siang (12.00) -> bermain bola (16.00). Urutan yang benar adalah C, D, B, A.
- Domain kognitif `classify/applying`: Siswa diminta untuk membaca waktu pada jam analog di setiap gambar dan mengurutkan kegiatan berdasarkan urutan waktu tersebut. Ini adalah penerapan prosedur membaca jam dan mengurutkan kejadian yang rutin.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang urutan waktu dalam sehari dan kemampuan prosedural membaca jam analog.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu membaca waktu pada jam analog yang jelas dan mengurutkan angka-angka tersebut. Tidak ada kendala yang berinteraksi atau kebutuhan strategi kompleks.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mampu membaca jam analog (jam tepat) dan memahami urutan waktu pagi hingga sore. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 3 sudah terbiasa membaca jam analog dan mengurutkan kejadian sehari-hari. Tugas ini bersifat langsung tanpa memerlukan perencanaan langkah yang rumit. |

Run 2 — solusi: Mengurutkan kegiatan berdasarkan waktu pada jam analog: bangun tidur (06.00), menyikat gigi (08.00), makan siang (12.00), bermain bola (16.00). Urutan yang benar adalah C, D, B, A.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi waktu pada jam analog dan mengurutkan kegiatan berdasarkan kronologi waktu tersebut. Ini adalah penerapan konsep waktu yang sudah dipelajari.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).
- Dimensi pengetahuan `classify/conceptual`: Siswa menggunakan pengetahuan konseptual tentang urutan waktu dalam sehari dan cara membaca jam analog untuk menyelesaikan tugas.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 3. Siswa hanya perlu membaca waktu pada empat jam analog yang berbeda dan mengurutkannya secara kronologis. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca jam analog dan memahami urutan waktu dalam sehari. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah terbiasa dengan konsep waktu dan membaca jam analog. Tugas mengurutkan empat kejadian berdasarkan waktu adalah tugas standar yang familiar. |

Run 3 — solusi: Berdasarkan waktu pada jam analog: bangun tidur (06.00) adalah yang paling pagi, diikuti menyikat gigi (08.00), makan siang (12.00), dan bermain bola (16.00). Urutan yang benar adalah C, D, B, A.
- Domain kognitif `classify/applying`: Siswa diminta untuk membaca waktu pada jam analog dan mengurutkan kegiatan berdasarkan kronologi waktu tersebut. Ini adalah penerapan prosedur membaca jam yang familiar dalam konteks rutin sehari-hari.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang urutan waktu dalam sehari yang dikaitkan dengan pembacaan jam analog.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu membaca waktu pada empat jam analog yang jelas dan mengurutkannya secara kronologis. Tidak ada kendala yang berinteraksi atau strategi non-rutin yang diperlukan.. Bukti: Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca jam analog (jam tepat) dan pemahaman urutan waktu sehari-hari. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 3 sudah mempelajari pembacaan jam dan urutan waktu. Tugas ini bersifat langsung dan rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 180/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.027270; applying=0.972730; reasoning=0.000000 | applying | 0.972730 | 0.113891 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.024279; conceptual=0.972761; procedural=0.002960; metacognitive=0.000000 | conceptual | 0.972761 | 0.096929 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.673432; Medium=0.319162; Hard=0.007406 | Easy | 0.673432 | 0.607206 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.972730; −Σp ln(p) = 0.125122; H = 0.125122/ln(3) = 0.113891; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.972761; −Σp ln(p) = 0.134372; H = 0.134372/ln(4) = 0.096929; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.673432; −Σp ln(p) = 0.667084; H = 0.667084/ln(3) = 0.607206; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Waktu
Tipe soal: multiple_choice
Stimulus: -
Soal: Urutkan gambar sesuai dengan waktu kegiatan.

Urutkan gambar sesuai dengan waktu kegiatan (dari pagi ke malam).
Pilihan: A. bangun tidur, menyikat gigi, makan siang, bermain bola
B. menyikat gigi, bangun tidur, makan siang, bermain bola
C. bangun tidur, makan siang, menyikat gigi, bermain bola
D. bermain bola, makan siang, menyikat gigi, bangun tidur
Transkripsi visual: Empat gambar kegiatan dengan jam: Gambar C (bangun tidur, jam 6:00), Gambar D (menyikat gigi, jam 8:00), Gambar B (makan siang, jam 12:00), Gambar A (bermain bola, jam 4:00). Urutan kronologis berdasarkan waktu pada jam adalah C, D, B, A.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 30. Soal `75434d44f2b377da3027e153`

Temukan panjang pensil berikut. A B C. Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.<br><br>Urutan pensil dari paling pendek: ...., ...., ....

| Opsi | Isi |
|---|---|
| A | A, B, C |
| B | A, C, B |
| C | C, A, B |
| D | B, C, A |

![Gambar sumber soal 30](<../../../images/kelas1_panduan_siswa_kelas1.pdf-0225-04.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Pensil A = 4 kotak, Pensil C = 5 kotak, Pensil B = 8 kotak. Urutan dari terpendek adalah A, C, B.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0225-04.png. Transkripsi visual: Gambar menunjukkan tiga pensil (A, B, C) di atas latar belakang kertas berpetak. Pensil A horizontal, panjangnya 4 kotak. Pensil B horizontal, panjangnya 8 kotak. Pensil C vertikal, panjangnya 5 kotak.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d321b26368e82d07f59164ffe8eb5be3f6684a1e63dddd2ff2fd6a764997314d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3431 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3448 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3503 |

Run 1 — solusi: Pensil A = 4 kotak, Pensil C = 5 kotak, Pensil B = 8 kotak. Urutan dari terpendek adalah A, C, B.
- Domain kognitif `classify/applying`: Siswa diminta untuk membandingkan panjang benda yang sudah diketahui ukurannya dan mengurutkannya. Ini adalah penerapan prosedur perbandingan langsung.. Bukti: Urutan pensil dari paling pendek
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang urutan besaran panjang (magnitude) berdasarkan nilai numerik yang diberikan.. Bukti: Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu membandingkan tiga bilangan bulat (4, 5, 8) dan mengurutkannya. Tidak ada kendala yang berinteraksi atau kebutuhan strategi kompleks.. Bukti: Urutan pensil dari paling pendek

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Membandingkan dan mengurutkan bilangan cacah sampai 10. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, membandingkan tiga nilai numerik sederhana adalah tugas dasar yang sesuai dengan tingkat perkembangan kognitif mereka. |

Run 2 — solusi: Bandingkan panjang pensil: A=4 kotak, C=5 kotak, B=8 kotak. Urutan dari terpendek ke terpanjang adalah 4, 5, 8, yaitu A, C, B.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengurutkan panjang benda berdasarkan data yang sudah diberikan atau dapat dihitung langsung dari gambar. Ini adalah penerapan prosedur membandingkan dan mengurutkan bilangan yang sudah dipelajari.. Bukti: Urutan pensil dari paling pendek
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang perbandingan panjang dan pengurutan bilangan.. Bukti: Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu membandingkan tiga bilangan (4, 5, 8) dan mengurutkannya. Tidak ada kendala yang berinteraksi atau kebutuhan strategi nonrutin.. Bukti: Urutan pensil dari paling pendek

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Membandingkan dan mengurutkan bilangan cacah sampai 10. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, membandingkan panjang benda yang diwakili oleh satuan kotak adalah tugas dasar yang sesuai dengan tingkat perkembangan kognitif mereka. |

Run 3 — solusi: Pensil A = 4 kotak, Pensil C = 5 kotak, Pensil B = 8 kotak. Mengurutkan dari yang paling pendek (4, 5, 8) menghasilkan urutan A, C, B.
- Domain kognitif `classify/applying`: Siswa diminta untuk membandingkan nilai panjang yang sudah diketahui dan mengurutkannya. Ini adalah penerapan langsung dari konsep perbandingan bilangan sederhana dalam konteks pengukuran.. Bukti: Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.; Urutan pensil dari paling pendek
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang urutan besaran panjang (4 < 5 < 8) yang direpresentasikan melalui satuan kotak.. Bukti: Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena nilai panjang sudah diberikan secara eksplisit dalam teks soal. Siswa hanya perlu membandingkan tiga bilangan bulat positif dan mengurutkannya dari yang terkecil.. Bukti: Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.; Urutan pensil dari paling pendek

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Membandingkan dan mengurutkan bilangan cacah sampai 10. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 3 sudah terbiasa membandingkan panjang benda dan mengurutkan bilangan. Tidak ada kendala kompleks atau langkah yang saling bergantung. |

Histori retry: run 1 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 155/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.038037; applying=0.961963; reasoning=0.000000 | applying | 0.961963 | 0.147144 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.015513; conceptual=0.981687; procedural=0.002801; metacognitive=0.000000 | conceptual | 0.981687 | 0.071582 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.698830; Medium=0.296356; Hard=0.004814 | Easy | 0.698830 | 0.579401 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.961963; −Σp ln(p) = 0.161654; H = 0.161654/ln(3) = 0.147144; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.981687; −Σp ln(p) = 0.099234; H = 0.099234/ln(4) = 0.071582; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.698830; −Σp ln(p) = 0.636537; H = 0.636537/ln(3) = 0.579401; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Mengukur Panjang Benda
Tipe soal: multiple_choice
Stimulus: -
Soal: Temukan panjang pensil berikut. A B C. Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.

Urutan pensil dari paling pendek: ...., ...., ....
Pilihan: A. A, B, C
B. A, C, B
C. C, A, B
D. B, C, A
Transkripsi visual: Gambar menunjukkan tiga pensil (A, B, C) di atas latar belakang kertas berpetak. Pensil A horizontal, panjangnya 4 kotak. Pensil B horizontal, panjangnya 8 kotak. Pensil C vertikal, panjangnya 5 kotak.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 31. Soal `e5989dcabcf5ead62a6aec0b`

KL adalah ....

| Opsi | Isi |
|---|---|
| A | Ruas garis |
| B | Garis |
| C | Sinar garis |
| D | Kurva/garis lengkung |

![Gambar sumber soal 31](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0162-00.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Gambar menunjukkan garis lurus yang dibatasi oleh dua titik (K dan L) di kedua ujungnya. Dalam geometri, garis yang memiliki dua titik ujung yang terbatas disebut ruas garis.
Gambar sumber: images/kelas3_panduan_siswa_kelas3.pdf-0162-00.png. Transkripsi visual: Gambar menunjukkan sebuah garis lurus horizontal yang dibatasi oleh dua titik tebal di kedua ujungnya, dengan label K di ujung kiri dan L di ujung kanan.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5e60bb4649dfe15b19bdc28be8c1eaeba536c5b4c429add03a4d67b45f8616d0`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3396 |
| 2 | success | valid / verified | knowing | factual | Easy | 3407 |
| 3 | success | valid / verified | knowing | factual | Easy | 3389 |

Run 1 — solusi: Gambar menunjukkan garis lurus dengan titik di kedua ujungnya (K dan L). Dalam geometri, garis yang dibatasi oleh dua titik di kedua ujungnya disebut ruas garis.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengidentifikasi objek geometri berdasarkan representasi visualnya. Siswa perlu mengenali definisi ruas garis (garis yang dibatasi oleh dua titik) dibandingkan dengan garis atau sinar garis. Ini adalah tugas pengenalan konsep dasar.. Bukti: KL adalah ....; Gambar menunjukkan sebuah garis lurus horizontal dengan titik tebal di kedua ujungnya.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami terminologi geometri dasar (ruas garis) dan menghubungkannya dengan representasi visual yang diberikan.. Bukti: KL adalah ....; Gambar menunjukkan sebuah garis lurus horizontal dengan titik tebal di kedua ujungnya.
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mengenali fitur visual (titik di kedua ujung) dan mencocokkannya dengan istilah yang sudah dipelajari. Tidak ada langkah tambahan atau integrasi yang diperlukan.. Bukti: KL adalah ....; Gambar menunjukkan sebuah garis lurus horizontal dengan titik tebal di kedua ujungnya.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang perbedaan antara garis, ruas garis, dan sinar garis. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, pengenalan istilah geometri dasar seperti ruas garis adalah materi standar yang bersifat hafalan atau pengenalan konsep langsung. |

Run 2 — solusi: Gambar menunjukkan garis lurus yang dibatasi oleh dua titik (titik K dan titik L) di kedua ujungnya. Berdasarkan definisi geometri, garis yang memiliki dua titik ujung yang terbatas disebut ruas garis.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk mengidentifikasi objek geometri berdasarkan representasi visualnya. Siswa hanya perlu mengenali karakteristik visual (dua titik ujung) dan mencocokkannya dengan istilah yang sudah dipelajari (ruas garis). Ini adalah proses pengenalan langsung.. Bukti: KL adalah ....; Gambar menunjukkan sebuah garis lurus horizontal dengan titik tebal di kedua ujungnya.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman siswa terhadap terminologi dasar geometri (fakta/istilah) mengenai perbedaan antara garis, sinar garis, dan ruas garis.. Bukti: KL adalah ....; Gambar menunjukkan sebuah garis lurus horizontal dengan titik tebal di kedua ujungnya.
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mengidentifikasi objek berdasarkan ciri visual yang jelas (titik di kedua ujung). Tidak ada langkah tambahan atau integrasi konsep yang diperlukan.. Bukti: KL adalah ....; Gambar menunjukkan sebuah garis lurus horizontal dengan titik tebal di kedua ujungnya.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk garis dan titik ujung. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, membedakan ruas garis dari garis atau sinar garis adalah materi dasar yang rutin. Soal ini tidak menuntut analisis kompleks. |

Run 3 — solusi: Gambar menunjukkan garis lurus dengan titik di kedua ujungnya (K dan L), yang secara definisi geometris merupakan ruas garis karena memiliki panjang terbatas.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi objek geometris berdasarkan representasi visualnya. Ini adalah tugas pengenalan istilah dasar (ruas garis) dari ciri visual yang diberikan.. Bukti: KL adalah ....; Gambar menunjukkan sebuah garis lurus horizontal dengan titik tebal di kedua ujungnya
- Dimensi pengetahuan `classify/factual`: Soal menguji pemahaman tentang terminologi dasar geometri (fakta/istilah) mengenai perbedaan antara ruas garis, garis, dan sinar garis.. Bukti: KL adalah ....; Ruas garis; Garis; Sinar garis
- Intended difficulty `classify/Easy`: Soal ini sangat langsung. Siswa hanya perlu mengenali definisi visual dari ruas garis yang ditandai dengan titik di kedua ujungnya. Tidak ada langkah perhitungan atau perencanaan yang diperlukan.. Bukti: KL adalah ....; A. Ruas garis; B. Garis; C. Sinar garis

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bentuk geometris dan perbedaan visual antara ruas garis, garis, dan sinar garis. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk kelas 3, membedakan ruas garis dari garis atau sinar garis adalah materi pengenalan dasar yang bersifat prosedural/faktual langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 1, "factual": 2} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4818`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta siswa untuk mengidentifikasi objek geometri berdasarkan representasi visualnya. Siswa perlu mengenali definisi ruas garis (garis yang dibatasi oleh dua titik) dibandingkan dengan garis atau sinar garis. Ini adalah tugas pengenalan konsep dasar.
- Dimensi pengetahuan `factual`: Siswa perlu memahami terminologi geometri dasar (ruas garis) dan menghubungkannya dengan representasi visual yang diberikan. Ini adalah pengetahuan tentang istilah dan simbol dasar.
- Intended difficulty `Easy`: Soal ini sangat langsung. Siswa hanya perlu mengenali fitur visual (titik di kedua ujung) dan mencocokkannya dengan istilah yang sudah dipelajari. Tidak ada langkah tambahan atau integrasi yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang perbedaan antara garis, ruas garis, dan sinar garis. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, pengenalan istilah geometri dasar seperti ruas garis adalah materi standar yang bersifat hafalan atau pengenalan konsep langsung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 86/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999108; applying=0.000892; reasoning=0.000000 | knowing | 0.999108 | 0.006516 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.601321; conceptual=0.374961; procedural=0.023718; metacognitive=0.000000 | factual | 0.601321 | 0.549955 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.824532; Medium=0.172566; Hard=0.002903 | Easy | 0.824532 | 0.436219 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999108; −Σp ln(p) = 0.007159; H = 0.007159/ln(3) = 0.006516; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.601321; −Σp ln(p) = 0.762400; H = 0.762400/ln(4) = 0.549955; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.824532; −Σp ln(p) = 0.479236; H = 0.479236/ln(3) = 0.436219; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Sisi Pada Bangun Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: KL adalah ....
Pilihan: A. Ruas garis
B. Garis
C. Sinar garis
D. Kurva/garis lengkung
Transkripsi visual: Gambar menunjukkan sebuah garis lurus horizontal yang dibatasi oleh dua titik tebal di kedua ujungnya, dengan label K di ujung kiri dan L di ujung kanan.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 32. Soal `d0868911a2fc9547f4f8231b`

PQ adalah ....

| Opsi | Isi |
|---|---|
| A | Kurva/garis lengkung |
| B | Garis |
| C | Ruas garis |
| D | Sinar garis |

![Gambar sumber soal 32](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0162-01.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Gambar menunjukkan objek geometri dengan satu titik pangkal (P) dan satu ujung yang dapat diperpanjang tak hingga (tanda panah di kanan). Definisi geometri untuk objek dengan satu titik pangkal dan satu arah perpanjangan adalah sinar garis.
Gambar sumber: images/kelas3_panduan_siswa_kelas3.pdf-0162-01.png. Transkripsi visual: Gambar menunjukkan sebuah garis lurus horizontal. Di ujung kiri terdapat titik tebal berlabel P. Di tengah garis terdapat titik tebal berlabel Q. Di ujung kanan garis terdapat tanda panah yang menunjukkan arah perpanjangan ke kanan.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9c855ea7d9c11cdbf91f7545e565ef4a3b1cb46fbf8d8e673c09d77c5ba9260a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | concern / verified | knowing | factual | Hard | 3508 |
| 2 | success | valid / verified | knowing | factual | Easy | 3503 |
| 3 | success | valid / verified | knowing | factual | Easy | 3525 |

Run 1 — solusi: Berdasarkan definisi geometri, objek yang memiliki satu titik pangkal (titik P) dan dapat diperpanjang tak terbatas ke satu arah (ditandai dengan anak panah di ujung kanan) disebut sinar garis.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi objek geometri berdasarkan representasi visualnya. Ini adalah tugas pengenalan istilah dasar (knowing).. Bukti: PQ adalah ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan tentang terminologi atau definisi dasar dalam geometri (fakta/istilah).. Bukti: PQ adalah ....
- Intended difficulty `classify/Hard`: Meskipun secara teknis mudah bagi yang sudah mempelajari materi ini, soal ini dikategorikan 'Hard' untuk kelas 3 SD karena materi 'sinar garis' berada di luar cakupan kurikulum standar kelas 3, sehingga menuntut pengetahuan yang tidak seharusnya diharapkan pada tingkat ini.. Bukti: PQ adalah ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar geometri tingkat lanjut (di luar kurikulum kelas 3). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi sinar garis tidak diajarkan di kelas 3 SD. Oleh karena itu, soal ini memiliki tingkat kesulitan tinggi bagi siswa kelas 3 karena menuntut pengetahuan di luar jenjangnya. |

Run 2 — solusi: Gambar menunjukkan objek geometri dengan satu titik pangkal (P) dan satu ujung yang dapat diperpanjang tak hingga (tanda panah di kanan). Definisi geometri untuk objek dengan satu titik pangkal dan satu arah perpanjangan adalah sinar garis.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi objek geometri berdasarkan representasi visualnya. Ini adalah tugas pengenalan istilah dasar (knowing) yang menghubungkan representasi visual dengan terminologi geometri yang tepat.. Bukti: PQ adalah ....; Gambar menunjukkan sebuah garis lurus horizontal. Pada ujung kiri terdapat titik tebal berlabel P. Di tengah garis terdapat titik tebal berlabel Q. Pada ujung kanan garis terdapat tanda panah yang menunjukkan arah perpanjangan.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman siswa terhadap terminologi dasar geometri (faktual) mengenai perbedaan antara garis, ruas garis, dan sinar garis.. Bukti: PQ adalah ....; A. Kurva/garis lengkung; B. Garis; C. Ruas garis
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan menguji pengenalan istilah dasar. Tidak ada langkah kompleks atau integrasi konsep yang diperlukan.. Bukti: PQ adalah ....; Gambar menunjukkan sebuah garis lurus horizontal. Pada ujung kiri terdapat titik tebal berlabel P. Di tengah garis terdapat titik tebal berlabel Q. Pada ujung kanan garis terdapat tanda panah yang menunjukkan arah perpanjangan.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengenalan dasar bentuk geometri dan istilah garis, ruas garis, dan sinar garis. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi pengenalan sinar garis adalah materi dasar geometri kelas 3. Soal ini hanya meminta identifikasi visual langsung tanpa perhitungan atau analisis mendalam. |

Run 3 — solusi: Gambar menunjukkan objek geometri dengan satu titik ujung (P) dan satu ujung yang dapat diperpanjang tak hingga (tanda panah di kanan). Objek dengan satu titik pangkal dan satu arah yang dapat diperpanjang disebut sinar garis.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengenali dan mengklasifikasikan objek geometri berdasarkan representasi visualnya. Ini adalah tugas pengenalan istilah dasar (knowing) yang tidak memerlukan prosedur kompleks atau penalaran nonrutin.. Bukti: PQ adalah ....; Gambar menunjukkan sebuah garis lurus horizontal. Di ujung kiri terdapat titik tebal berlabel P. Di tengah garis terdapat titik tebal berlabel Q. Di ujung kanan garis terdapat tanda panah yang menunjukkan arah ke kanan.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman siswa terhadap terminologi dasar geometri (fakta/istilah) mengenai perbedaan antara garis, ruas garis, dan sinar garis.. Bukti: PQ adalah ....; A. Kurva/garis lengkung; B. Garis; C. Ruas garis
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan menguji pengetahuan dasar. Tidak ada langkah yang saling bergantung atau strategi yang perlu dipilih. Siswa hanya perlu mencocokkan visual dengan definisi istilah yang sudah dipelajari.. Bukti: PQ adalah ....; Gambar menunjukkan sebuah garis lurus horizontal. Di ujung kiri terdapat titik tebal berlabel P. Di tengah garis terdapat titik tebal berlabel Q. Di ujung kanan garis terdapat tanda panah yang menunjukkan arah ke kanan.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang titik, garis, dan sinar garis. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi pengenalan unsur geometri dasar (garis, sinar garis, ruas garis) adalah materi standar kelas 3. Soal ini tidak menuntut analisis mendalam, hanya pengenalan visual langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / adjudicated | factual |
| Intended difficulty | {"Hard": 1, "Easy": 2} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4965`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa diminta untuk mengidentifikasi objek geometri berdasarkan representasi visualnya. Ini adalah tugas pengenalan istilah dasar (knowing) yang menghubungkan representasi visual dengan terminologi geometri yang tepat.
- Dimensi pengetahuan `factual`: Soal ini menguji pemahaman siswa terhadap terminologi dasar geometri (fakta/istilah) mengenai perbedaan antara garis, ruas garis, dan sinar garis.
- Intended difficulty `Easy`: Soal ini bersifat langsung dan menguji pengenalan istilah dasar. Tidak ada langkah kompleks, integrasi konsep, atau strategi nonrutin yang diperlukan. Siswa hanya perlu mencocokkan visual dengan definisi istilah yang sudah dipelajari.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang titik, garis, dan sinar garis. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi pengenalan unsur geometri dasar (garis, sinar garis, ruas garis) adalah materi standar kelas 3. Soal ini tidak menuntut analisis mendalam, hanya pengenalan visual langsung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 100/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.861044; applying=0.138956; reasoning=0.000000 | knowing | 0.861044 | 0.366885 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.177822; conceptual=0.806078; procedural=0.016101; metacognitive=0.000000 | conceptual | 0.806078 | 0.394824 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.846304; Medium=0.151124; Hard=0.002572 | Easy | 0.846304 | 0.402452 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.861044; −Σp ln(p) = 0.403064; H = 0.403064/ln(3) = 0.366885; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.806078; −Σp ln(p) = 0.547343; H = 0.547343/ln(4) = 0.394824; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.846304; −Σp ln(p) = 0.442139; H = 0.442139/ln(3) = 0.402452; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Sisi Pada Bangun Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: PQ adalah ....
Pilihan: A. Kurva/garis lengkung
B. Garis
C. Ruas garis
D. Sinar garis
Transkripsi visual: Gambar menunjukkan sebuah garis lurus horizontal. Di ujung kiri terdapat titik tebal berlabel P. Di tengah garis terdapat titik tebal berlabel Q. Di ujung kanan garis terdapat tanda panah yang menunjukkan arah perpanjangan ke kanan.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 33. Soal `2c9c0a53b57350101ebd57b0`

Sebutkan nama sudut-sudut berikut. Tuliskan ukuran dan jenisnya.

| Opsi | Isi |
|---|---|
| A | ∠MON, ukurannya 120°, jenisnya sudut lancip |
| B | ∠MON, ukurannya 120°, jenisnya sudut tumpul |
| C | ∠MON, ukurannya 60°, jenisnya sudut lancip |
| D | ∠MON, ukurannya 90°, jenisnya sudut siku-siku |

![Gambar sumber soal 33](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0182-01.png>)


Kunci sumber: `B`; status AI: `conflict`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Sudut MON pada gambar c memiliki bukaan lebih dari 90° dan kurang dari 180°, sehingga diklasifikasikan sebagai sudut tumpul. Nilai 120° adalah estimasi yang valid untuk sudut tumpul tersebut.
Gambar sumber: images/kelas3_panduan_siswa_kelas3.pdf-0182-01.png. Transkripsi visual: Gambar menampilkan 6 sudut: a (sudut lancip PQR), b (sudut siku-siku RST), c (sudut tumpul MON), d (sudut lurus BOA), e (sudut refleks KLM), f (sudut tumpul EFG).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menyebutkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f1b21c47cc7090c4577b9fbb226b2cdbfe4f42e2f92f05c940dee02f86270e34`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / conflict | applying | conceptual | Medium | 3625 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3586 |
| 3 | success | concern / unverifiable | — | — | — | 3282 |

Run 1 — solusi: Soal tidak dapat diselesaikan secara eksak karena tidak ada informasi ukuran sudut atau alat ukur yang disediakan. Secara visual, sudut MON pada gambar c adalah sudut tumpul, namun nilai 120° tidak dapat dipastikan.
- Domain kognitif `classify/applying`: Siswa diminta mengidentifikasi jenis sudut (konseptual) dan mencoba menentukan ukuran (prosedural/estimasi). Karena soal meminta ukuran eksak tanpa alat, ini menuntut prosedur yang tidak valid.. Bukti: Sebutkan nama sudut-sudut berikut. Tuliskan ukuran dan jenisnya.
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep jenis sudut (lancip, siku-siku, tumpul) dan mencoba menerapkan prosedur pengukuran atau estimasi.. Bukti: jenisnya sudut tumpul; ukurannya 120°
- Intended difficulty `classify/Medium`: Soal ini secara teknis tidak valid karena meminta ukuran derajat tanpa data. Jika dianggap sebagai estimasi, ini adalah tugas rutin. Namun, karena ketidakvalidan konten, tingkat kesulitan menjadi tidak relevan.. Bukti: Sebutkan nama sudut-sudut berikut. Tuliskan ukuran dan jenisnya.; Pilihan jawaban memberikan nilai numerik spesifik

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang jenis-jenis sudut (lancip, siku-siku, tumpul). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, mengidentifikasi jenis sudut adalah materi standar. Namun, meminta ukuran derajat tanpa busur derajat adalah tuntutan yang tidak wajar dan tidak valid secara matematis. |

Run 2 — solusi: Sudut MON pada gambar c memiliki bukaan lebih dari 90° dan kurang dari 180°, sehingga diklasifikasikan sebagai sudut tumpul. Ukuran 120° konsisten dengan visualisasi sudut tumpul tersebut.
- Domain kognitif `classify/applying`: Siswa diminta mengidentifikasi jenis sudut berdasarkan representasi visual dan menentukan ukurannya. Ini adalah penerapan konsep dasar sudut pada konteks rutin.. Bukti: Sebutkan nama sudut-sudut berikut. Tuliskan ukuran dan jenisnya.; ∠MON, ukurannya 120°, jenisnya sudut tumpul
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara besar sudut (derajat) dan klasifikasi jenis sudut (lancip, siku-siku, tumpul) sebagai konsep dasar geometri.. Bukti: jenisnya sudut tumpul; ukurannya 120°
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya meminta identifikasi langsung dari representasi visual sudut yang umum dipelajari di kelas 3. Tidak ada langkah kompleks atau integrasi yang diperlukan.. Bukti: ∠MON, ukurannya 120°, jenisnya sudut tumpul

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang jenis-jenis sudut (lancip, siku-siku, tumpul) dan estimasi besar sudut. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah diajarkan untuk mengenali jenis sudut berdasarkan perbandingannya dengan sudut siku-siku. |

Run 3 — solusi: Tidak dapat ditentukan karena ketidaksesuaian antara instruksi soal (meminta 6 sudut) dan pilihan jawaban (hanya satu opsi untuk ∠MON).
- Domain kognitif `abstain/None`: Soal memiliki cacat instruksi yang fatal karena meminta identifikasi untuk enam gambar berbeda (a-f), namun hanya menyediakan pilihan jawaban untuk satu gambar (∠MON). Abstain diperlukan karena soal tidak dapat diselesaikan secara valid.. Bukti: 
- Dimensi pengetahuan `abstain/None`: Karena soal tidak dapat diselesaikan akibat ketidaksesuaian format, klasifikasi dimensi pengetahuan tidak dapat dilakukan dengan tepat.. Bukti: 
- Intended difficulty `abstain/None`: Soal tidak dapat diklasifikasikan tingkat kesulitannya karena instruksi yang diberikan tidak lengkap dan tidak selaras dengan pilihan jawaban yang tersedia.. Bukti: 

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 1, "Easy": 1} | no_consensus / adjudicated | Easy |

Adjudikasi AI: `success`; token `6113`.
Konten: `concern`; kunci: `conflict`; masalah: Soal meminta identifikasi untuk enam gambar (a-f), namun pilihan jawaban hanya menyediakan opsi untuk satu sudut (∠MON). Instruksi tidak selaras dengan pilihan jawaban.; Meminta ukuran derajat eksak tanpa alat ukur atau data pendukung (seperti busur derajat atau tanda sudut siku-siku) adalah praktik yang kurang tepat untuk asesmen kelas 3..
- Domain kognitif `applying`: Siswa diminta menerapkan konsep jenis sudut untuk mengidentifikasi sudut tumpul dan mengestimasi ukurannya.
- Dimensi pengetahuan `conceptual`: Memerlukan pemahaman konsep klasifikasi sudut (lancip, siku-siku, tumpul) berdasarkan besar bukaan.
- Intended difficulty `Easy`: Tugas ini adalah identifikasi visual langsung yang rutin diajarkan di kelas 3. Meskipun soal memiliki cacat instruksi, tingkat kesulitan untuk mengidentifikasi sudut tumpul adalah rendah.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang jenis-jenis sudut (lancip, siku-siku, tumpul). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 3 sudah diajarkan untuk mengenali jenis sudut berdasarkan perbandingannya dengan sudut siku-siku. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 147/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Dimensi pengetahuan |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |
| Intended difficulty |  | — | — | — | abstain / content_not_qualified;answer_key_not_verified;minimal_solution_not_verified |

<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Sudut Pada Bidang Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebutkan nama sudut-sudut berikut. Tuliskan ukuran dan jenisnya.
Pilihan: A. ∠MON, ukurannya 120°, jenisnya sudut lancip
B. ∠MON, ukurannya 120°, jenisnya sudut tumpul
C. ∠MON, ukurannya 60°, jenisnya sudut lancip
D. ∠MON, ukurannya 90°, jenisnya sudut siku-siku
Transkripsi visual: Gambar menampilkan 6 sudut: a (sudut lancip PQR), b (sudut siku-siku RST), c (sudut tumpul MON), d (sudut lurus BOA), e (sudut refleks KLM), f (sudut tumpul EFG).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `revision_required`.
Status konten: `concern`. Catatan konten: Soal meminta identifikasi untuk enam gambar (a-f), namun pilihan jawaban hanya menyediakan opsi untuk satu sudut (∠MON). Instruksi tidak selaras dengan pilihan jawaban.; Meminta ukuran derajat eksak tanpa alat ukur atau data pendukung (seperti busur derajat atau tanda sudut siku-siku) adalah praktik yang kurang tepat untuk asesmen kelas 3..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": null, "blindLabel": "applying", "agreement": null}, "knowledgeDimension": {"modelLabel": null, "blindLabel": "conceptual", "agreement": null}, "intendedDifficulty": {"modelLabel": null, "blindLabel": "Easy", "agreement": null}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 34. Soal `e856f8b6ea486b876939d3ba`

Sebutkan nama sudut-sudut berikut. Tuliskan ukuran dan jenisnya.

| Opsi | Isi |
|---|---|
| A | ∠RST, ukurannya 45°, jenisnya sudut lancip |
| B | ∠RST, ukurannya 180°, jenisnya sudut lurus |
| C | ∠RST, ukurannya 90°, jenisnya sudut siku-siku |
| D | ∠RST, ukurannya 90°, jenisnya sudut tumpul |

![Gambar sumber soal 34](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0182-01.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Sudut b memiliki simbol kotak kecil di titik sudut S, yang secara konvensional dalam geometri dasar menandakan sudut siku-siku dengan besar 90 derajat.
Gambar sumber: images/kelas3_panduan_siswa_kelas3.pdf-0182-01.png. Transkripsi visual: Gambar menampilkan 6 sudut yang diberi label a sampai f. Sudut b adalah sudut siku-siku dengan titik sudut S, garis RS vertikal, garis ST horizontal, dan terdapat simbol kotak kecil di titik S yang menandakan sudut 90 derajat.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menyebutkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3cee3fb1b142bede95b17e63e2ec4c054265332500b4b765ceec44cf0aa6953e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 3531 |
| 2 | success | valid / verified | knowing | factual | Easy | 3587 |
| 3 | success | valid / verified | knowing | factual | Easy | 3633 |

Run 1 — solusi: Sudut b memiliki simbol kotak kecil di titik sudut S, yang secara konvensional dalam geometri dasar menandakan sudut siku-siku dengan besar 90 derajat.
- Domain kognitif `classify/knowing`: Siswa diminta mengenali simbol geometris standar (kotak kecil) untuk mengidentifikasi jenis sudut (siku-siku) dan ukurannya. Ini adalah pengenalan langsung terhadap fakta geometris.. Bukti: tanda kotak kecil di titik sudut S yang menunjukkan sudut tepat 90°
- Dimensi pengetahuan `classify/factual`: Soal menguji pemahaman tentang istilah (sudut siku-siku) dan simbol (kotak kecil) yang merepresentasikan konsep dasar sudut.. Bukti: Sebutkan nama sudut-sudut berikut. Tuliskan ukuran dan jenisnya.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar. Siswa hanya perlu mengenali simbol visual yang sudah diajarkan sebagai penanda sudut siku-siku. Tidak ada langkah perencanaan atau integrasi yang diperlukan.. Bukti: tanda kotak kecil di titik sudut S

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal simbol sudut siku-siku (kotak kecil). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk kelas 3, pengenalan sudut siku-siku melalui simbol visual adalah materi dasar yang rutin. |

Run 2 — solusi: Gambar b memiliki simbol kotak di titik sudut S, yang menunjukkan sudut siku-siku dengan besar 90 derajat. Oleh karena itu, sudut tersebut adalah ∠RST, ukurannya 90°, dan jenisnya sudut siku-siku.
- Domain kognitif `classify/knowing`: Siswa diminta mengenali simbol geometris (kotak kecil) yang merepresentasikan konsep sudut siku-siku. Ini adalah tugas pengenalan langsung terhadap simbol dan definisi dasar sudut.. Bukti: simbol kotak kecil di titik sudut S; menunjukkan sudut tepat 90°, sehingga termasuk sudut siku-siku
- Dimensi pengetahuan `classify/factual`: Soal menguji pemahaman tentang fakta geometris dasar (simbol sudut siku-siku) dan terminologi sudut.. Bukti: simbol kotak kecil di titik sudut S; sudut tepat 90°, sehingga termasuk sudut siku-siku
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena siswa hanya perlu mengidentifikasi simbol visual standar (kotak) yang sudah dipelajari sebagai penanda sudut siku-siku. Tidak ada langkah perhitungan atau analisis kompleks yang diperlukan.. Bukti: simbol kotak kecil di titik sudut S; menunjukkan sudut tepat 90°

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang jenis-jenis sudut (siku-siku, lancip, tumpul) dan simbol sudut siku-siku. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Untuk kelas 3, pengenalan sudut siku-siku melalui simbol visual adalah materi dasar yang rutin dan langsung. |

Run 3 — solusi: Gambar b menunjukkan sudut RST dengan simbol kotak di titik S, yang secara geometris mendefinisikan sudut siku-siku sebesar 90°.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengenali simbol geometris standar (tanda kotak) untuk mengidentifikasi jenis sudut dan ukurannya. Ini adalah proses pengenalan langsung terhadap fakta geometris dasar.. Bukti: Sebutkan nama sudut-sudut berikut. Tuliskan ukuran dan jenisnya.; Pada gambar b, sudut RST digambar dengan tanda kotak kecil di titik sudut S yang menunjukkan sudut tepat 90°, sehingga termasuk sudut siku-siku
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang terminologi sudut (siku-siku) dan simbol konvensional yang merepresentasikan fakta geometris tersebut.. Bukti: Sebutkan nama sudut-sudut berikut. Tuliskan ukuran dan jenisnya.; sudut RST digambar dengan tanda kotak kecil di titik sudut S yang menunjukkan sudut tepat 90°, sehingga termasuk sudut siku-siku
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar bagi kelas 3. Siswa hanya perlu mengenali simbol visual standar untuk sudut siku-siku tanpa perlu melakukan perhitungan atau perencanaan langkah yang kompleks.. Bukti: Sebutkan nama sudut-sudut berikut. Tuliskan ukuran dan jenisnya.; Pada gambar b, sudut RST digambar dengan tanda kotak kecil di titik sudut S yang menunjukkan sudut tepat 90°

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal konsep dasar sudut dan simbol sudut siku-siku. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Pengenalan sudut siku-siku melalui simbol kotak adalah materi standar kelas 3 yang bersifat langsung dan tidak memerlukan analisis mendalam. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 135/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.893055; applying=0.106945; reasoning=0.000000 | knowing | 0.893055 | 0.309555 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.038068; conceptual=0.946822; procedural=0.015110; metacognitive=0.000000 | conceptual | 0.946822 | 0.172767 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.793962; Medium=0.202343; Hard=0.003694 | Easy | 0.793962 | 0.479856 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.893055; −Σp ln(p) = 0.340081; H = 0.340081/ln(3) = 0.309555; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.946822; −Σp ln(p) = 0.239506; H = 0.239506/ln(4) = 0.172767; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.793962; −Σp ln(p) = 0.527176; H = 0.527176/ln(3) = 0.479856; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Sudut Pada Bidang Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebutkan nama sudut-sudut berikut. Tuliskan ukuran dan jenisnya.
Pilihan: A. ∠RST, ukurannya 45°, jenisnya sudut lancip
B. ∠RST, ukurannya 180°, jenisnya sudut lurus
C. ∠RST, ukurannya 90°, jenisnya sudut siku-siku
D. ∠RST, ukurannya 90°, jenisnya sudut tumpul
Transkripsi visual: Gambar menampilkan 6 sudut yang diberi label a sampai f. Sudut b adalah sudut siku-siku dengan titik sudut S, garis RS vertikal, garis ST horizontal, dan terdapat simbol kotak kecil di titik S yang menandakan sudut 90 derajat.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: Soal meminta siswa menyebutkan nama, ukuran, dan jenis untuk semua sudut (a-f), namun pilihan jawaban hanya menyediakan opsi untuk sudut b (∠RST). Soal ini tidak konsisten antara instruksi (semua sudut) dan format pilihan ganda (hanya satu sudut).; Soal meminta siswa menyebutkan nama, ukuran, dan jenis sudut untuk semua gambar (a-f), namun pilihan jawaban yang disediakan hanya merujuk pada satu gambar (∠RST pada gambar b). Terdapat ketidaksesuaian antara instruksi soal dengan format pilihan ganda yang diberikan.; Soal meminta siswa menyebutkan nama, ukuran, dan jenis untuk semua sudut (a-f), namun pilihan jawaban hanya menyediakan opsi untuk satu sudut (∠RST) yang merujuk pada gambar b. Soal ini tidak konsisten antara instruksi utama dan format pilihan ganda yang diberikan..
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 35. Soal `f311bf91df38724a90b35b69`

Perhatikan huruf-huruf berikut ini.<br><br>Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?

| Opsi | Isi |
|---|---|
| A | Huruf M |
| B | Tidak ada |
| C | Huruf T |
| D | Huruf E |

![Gambar sumber soal 35](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0198-01.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Analisis setiap huruf: M memiliki sepasang garis sejajar (vertikal) tetapi tidak ada garis tegak lurus. T memiliki sepasang garis tegak lurus tetapi tidak ada garis sejajar. E memiliki tiga garis horizontal yang sejajar (lebih dari satu pasang) dan dua garis tegak lurus. Karena tidak ada huruf yang memenuhi kriteria tepat satu pasang garis sejajar dan dua pasang garis tegak lurus, maka jawabannya adalah 'Tidak ada'.
Gambar sumber: images/kelas3_panduan_siswa_kelas3.pdf-0198-01.png. Transkripsi visual: Gambar menunjukkan kata 'MATEMATIKA' yang ditulis dengan huruf kapital di atas kertas berpetak. Seorang anak laki-laki menunjuk ke arah kata tersebut.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ae58e6c170892af151d3adb2da9e890b84de9cd1cb9cd2660e12dcd3d50b57ad`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 3828 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3692 |
| 3 | success | valid / verified | applying | conceptual | Hard | 3855 |

Run 1 — solusi: Analisis setiap huruf: M tidak memiliki garis sejajar atau tegak lurus. A tidak memiliki garis sejajar atau tegak lurus. T memiliki sepasang garis tegak lurus tetapi tidak memiliki garis sejajar. E memiliki tiga garis horizontal yang sejajar (lebih dari satu pasang) dan dua garis tegak lurus. Karena tidak ada huruf yang memenuhi syarat 'hanya satu pasang garis sejajar dan dua pasang garis tegak lurus', maka jawabannya adalah 'Tidak ada'.
- Domain kognitif `classify/applying`: Siswa diminta untuk menganalisis properti geometris (garis sejajar dan tegak lurus) dari setiap huruf yang diberikan dan membandingkannya dengan kriteria yang ditentukan. Ini memerlukan penerapan konsep pada konteks visual yang spesifik.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?; M tidak memiliki garis sejajar atau tegak lurus.; T memiliki sepasang garis tegak lurus tetapi tidak memiliki garis sejajar.; E memiliki tiga garis horizontal yang sejajar (lebih dari satu pasang) dan dua garis tegak lurus.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang definisi dan identifikasi garis sejajar dan tegak lurus dalam bentuk huruf, yang merupakan konsep dasar geometri.. Bukti: Garis-Garis Tegak Lurus dan Garis-Garis Sejajar; Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk memeriksa setiap huruf satu per satu terhadap dua kriteria yang berbeda secara bersamaan. Meskipun konsepnya dasar, kebutuhan untuk memverifikasi setiap huruf dan menolak opsi yang salah (termasuk jebakan pada huruf E) meningkatkan beban kognitif bagi siswa kelas 3.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?; M tidak memiliki garis sejajar atau tegak lurus.; T memiliki sepasang garis tegak lurus tetapi tidak memiliki garis sejajar.; E memiliki tiga garis horizontal yang sejajar (lebih dari satu pasang) dan dua garis tegak lurus.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang garis sejajar dan garis tegak lurus. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 3 harus melakukan analisis visual yang cermat pada setiap huruf. Menentukan bahwa tidak ada huruf yang memenuhi kriteria ganda (sejajar dan tegak lurus) memerlukan ketelitian tinggi dan kemampuan untuk menolak jawaban yang tampak benar sebagian (seperti huruf E). |

Run 2 — solusi: Analisis setiap huruf: M (sejajar, tidak tegak lurus), A (tidak sejajar, tidak tegak lurus), T (tegak lurus, tidak sejajar), E (tiga pasang sejajar, dua pasang tegak lurus), I (tidak sejajar, tidak tegak lurus), K (tidak sejajar, tidak tegak lurus). Tidak ada huruf yang memenuhi syarat tepat satu pasang sejajar dan dua pasang tegak lurus.
- Domain kognitif `classify/applying`: Siswa harus menganalisis sifat geometris (sejajar dan tegak lurus) pada setiap huruf yang diberikan dan membandingkannya dengan kriteria yang diminta. Ini melibatkan penerapan konsep pada konteks visual.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman siswa tentang definisi dan identifikasi garis sejajar dan tegak lurus pada bentuk huruf, yang merupakan konsep geometris dasar.. Bukti: Garis-Garis Tegak Lurus dan Garis-Garis Sejajar
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk memeriksa setiap huruf secara sistematis terhadap dua kriteria sekaligus. Meskipun konsepnya dasar, kebutuhan untuk mengevaluasi beberapa huruf dan memverifikasi kondisi ganda (sejajar dan tegak lurus) meningkatkan beban kognitif bagi siswa kelas 3.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman visual tentang garis sejajar dan tegak lurus. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 3 biasanya baru mengenal konsep garis. Memeriksa setiap huruf dengan dua kriteria (sejajar dan tegak lurus) memerlukan ketelitian dan kemampuan membedakan sifat geometris, yang cukup menantang untuk tingkat kelas ini. |

Run 3 — solusi: Analisis setiap huruf: M memiliki sepasang garis sejajar (vertikal) tapi tidak ada tegak lurus. T memiliki sepasang garis tegak lurus tapi tidak ada garis sejajar. E memiliki tiga garis horizontal sejajar (lebih dari satu pasang) dan dua garis tegak lurus. Tidak ada huruf yang memenuhi syarat tepat satu pasang garis sejajar dan dua pasang garis tegak lurus.
- Domain kognitif `classify/applying`: Siswa harus menganalisis properti geometris (garis sejajar dan tegak lurus) dari setiap huruf yang diberikan dan membandingkannya dengan kriteria yang sangat spesifik (tepat satu pasang sejajar dan dua pasang tegak lurus). Ini memerlukan penerapan konsep pada konteks visual.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?; M hanya memenuhi syarat sepasang garis sejajar, tidak punya garis tegak lurus; E memang punya garis sejajar dan tegak lurus, tetapi garis sejajarnya tiga
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antar garis (sejajar dan tegak lurus) dan bagaimana konsep tersebut diterapkan pada bentuk huruf.. Bukti: Garis-Garis Tegak Lurus dan Garis-Garis Sejajar; Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?
- Intended difficulty `classify/Hard`: Soal ini menuntut siswa untuk memeriksa setiap opsi secara mendalam terhadap dua kriteria sekaligus (sejajar dan tegak lurus). Siswa harus melakukan eliminasi sistematis dan memverifikasi kondisi 'hanya satu pasang' dan 'dua pasang' yang cukup menantang untuk kelas 3.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?; M hanya memenuhi syarat sepasang garis sejajar, tidak punya garis tegak lurus; E memang punya garis sejajar dan tegak lurus, tetapi garis sejajarnya tiga

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang garis sejajar dan tegak lurus. |
| dependentSteps | 4 |
| routineStatus | nonroutine_strategy |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Meskipun konsepnya dasar, menuntut siswa untuk mengevaluasi setiap huruf dengan batasan kuantitatif yang ketat (tepat satu pasang, tepat dua pasang) membuat soal ini sulit bagi siswa kelas 3 karena memerlukan ketelitian tinggi dan analisis komparatif. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 2, "Hard": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `5599`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa harus menerapkan konsep geometris (sejajar dan tegak lurus) untuk menganalisis properti visual dari setiap huruf yang diberikan. Ini adalah penerapan konsep pada konteks visual.
- Dimensi pengetahuan `conceptual`: Soal menguji pemahaman konseptual tentang definisi dan identifikasi garis sejajar dan tegak lurus pada bentuk huruf.
- Intended difficulty `Medium`: Soal ini menuntut siswa untuk memeriksa setiap huruf secara sistematis terhadap dua kriteria sekaligus. Meskipun konsepnya dasar, kebutuhan untuk memverifikasi kondisi ganda (sejajar dan tegak lurus) dan menolak opsi yang tampak benar sebagian (seperti E) meningkatkan beban kognitif bagi siswa kelas 3.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman visual tentang garis sejajar dan tegak lurus. |
| dependentSteps | 4 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 3 biasanya baru mengenal konsep garis. Memeriksa setiap huruf dengan dua kriteria (sejajar dan tegak lurus) memerlukan ketelitian dan kemampuan membedakan sifat geometris, yang cukup menantang untuk tingkat kelas ini. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 108/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.082541; applying=0.917459; reasoning=0.000000 | applying | 0.917459 | 0.259356 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.149342; conceptual=0.828056; procedural=0.022602; metacognitive=0.000000 | conceptual | 0.828056 | 0.379330 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.815384; Medium=0.180595; Hard=0.004021 | Easy | 0.815384 | 0.453012 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.917459; −Σp ln(p) = 0.284932; H = 0.284932/ln(3) = 0.259356; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.828056; −Σp ln(p) = 0.525863; H = 0.525863/ln(4) = 0.379330; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.815384; −Σp ln(p) = 0.497685; H = 0.497685/ln(3) = 0.453012; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Garis-Garis Tegak Lurus dan Garis-Garis Sejajar
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan huruf-huruf berikut ini.

Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?
Pilihan: A. Huruf M
B. Tidak ada
C. Huruf T
D. Huruf E
Transkripsi visual: Gambar menunjukkan kata 'MATEMATIKA' yang ditulis dengan huruf kapital di atas kertas berpetak. Seorang anak laki-laki menunjuk ke arah kata tersebut.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 36. Soal `548ed93702987b740b35d2b4`

Manakah dari pasangan garis berikut yang sejajar?

| Opsi | Isi |
|---|---|
| A | a dan b |
| B | a, b, c, dan e |
| C | c, d, dan e |
| D | a, b, c, d, dan e |

![Gambar sumber soal 36](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0196-03.png>)


![Gambar sumber soal 36](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0196-04.png>)


![Gambar sumber soal 36](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0196-05.png>)


![Gambar sumber soal 36](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0196-06.png>)


![Gambar sumber soal 36](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0196-07.png>)


![Gambar sumber soal 36](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0196-08.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Garis sejajar adalah garis yang tidak akan pernah berpotongan meskipun diperpanjang. Pada gambar, pasangan a (horizontal), b (vertikal), c (miring), dan e (miring) memiliki jarak yang tetap dan kemiringan yang sama, sehingga tidak akan pernah bertemu. Pasangan d dan f tidak sejajar karena akan berpotongan jika diperpanjang.
Gambar sumber: images/kelas3_panduan_siswa_kelas3.pdf-0196-03.png, images/kelas3_panduan_siswa_kelas3.pdf-0196-04.png, images/kelas3_panduan_siswa_kelas3.pdf-0196-05.png, images/kelas3_panduan_siswa_kelas3.pdf-0196-06.png, images/kelas3_panduan_siswa_kelas3.pdf-0196-07.png, images/kelas3_panduan_siswa_kelas3.pdf-0196-08.png. Transkripsi visual: Soal menampilkan enam gambar (a sampai f) pada latar belakang kotak-kotak (grid). Gambar a menunjukkan dua garis horizontal sejajar. Gambar b menunjukkan dua garis vertikal sejajar. Gambar c menunjukkan dua garis miring sejajar (kemiringan sama). Gambar d menunjukkan dua garis miring yang tidak sejajar (jarak menyempit). Gambar e menunjukkan dua garis miring sejajar (kemiringan sama). Gambar f menunjukkan dua garis miring yang bertemu di satu titik (tidak sejajar).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `19626d6d67b7dfac692dfce86eb9df2030626087b94920665e99c3300dc1528c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 9093 |
| 2 | success | valid / verified | applying | conceptual | Medium | 10283 |
| 3 | success | valid / verified | applying | conceptual | Medium | 9106 |

Run 1 — solusi: Garis sejajar adalah garis yang tidak akan pernah berpotongan meskipun diperpanjang. Pada gambar, pasangan a (horizontal), b (vertikal), c (miring), dan e (miring) memiliki jarak yang tetap dan kemiringan yang sama, sehingga tidak akan pernah bertemu. Pasangan d dan f tidak sejajar karena akan berpotongan jika diperpanjang.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi pasangan garis sejajar dari beberapa contoh visual. Ini adalah tugas pengenalan konsep dasar garis sejajar yang sudah dipelajari, sehingga termasuk dalam domain applying karena siswa harus menerapkan pemahaman konsep 'sejajar' pada berbagai orientasi garis (horizontal, vertikal, dan miring).. Bukti: Manakah dari pasangan garis berikut yang sejajar?; pasangan a (mendatar), b (tegak), c dan e (miring dengan kemiringan sama)
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang konsep garis sejajar, yaitu hubungan antara dua garis yang tidak akan pernah berpotongan. Ini adalah pemahaman konseptual tentang sifat geometris.. Bukti: Manakah dari pasangan garis berikut yang sejajar?
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak hanya mengidentifikasi garis sejajar pada posisi standar (horizontal/vertikal), tetapi juga harus mengenali garis sejajar pada posisi miring. Meskipun konsepnya dasar, tuntutan untuk membedakan antara garis yang sejajar dan yang tidak sejajar (seperti pada d dan f) memerlukan ketelitian visual yang lebih dari sekadar pengenalan satu orientasi.. Bukti: Manakah dari pasangan garis berikut yang sejajar?; a, b, c, dan e

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang garis dan konsep bahwa garis sejajar tidak akan pernah berpotongan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, mengidentifikasi garis sejajar dalam berbagai orientasi (terutama miring) adalah tugas yang sesuai namun menuntut perhatian lebih dibandingkan hanya garis horizontal/vertikal, sehingga dikategorikan Medium. |

Run 2 — solusi: Garis sejajar adalah garis yang tidak akan pernah berpotongan dan memiliki jarak yang tetap. Berdasarkan pengamatan pada petak, garis a (horizontal), b (vertikal), c (diagonal), dan e (diagonal) memiliki jarak yang tetap dan tidak akan bertemu. Garis d tidak sejajar karena jaraknya menyempit.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep garis sejajar (jarak tetap, tidak berpotongan) untuk mengidentifikasi pasangan garis yang memenuhi syarat di antara beberapa pilihan visual.. Bukti: Manakah dari pasangan garis berikut yang sejajar?; a, b, c, dan e
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman konsep garis sejajar yang mencakup berbagai orientasi (horizontal, vertikal, diagonal) dan kemampuan membedakannya dari garis yang tidak sejajar.. Bukti: Manakah dari pasangan garis berikut yang sejajar?
- Intended difficulty `classify/Medium`: Siswa harus mengevaluasi lima pasangan garis secara terpisah untuk menentukan mana yang sejajar. Adanya pengecoh (garis d) yang terlihat mirip namun tidak sejajar meningkatkan tuntutan analisis dibandingkan sekadar mengenali satu contoh.. Bukti: a, b, c, dan e; d

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang garis sejajar dan kemampuan mengamati jarak antar garis pada bidang berpetak. |
| dependentSteps | 5 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, membedakan garis sejajar dalam berbagai orientasi adalah standar, namun keharusan memeriksa lima kasus sekaligus dan mengidentifikasi pengecoh 'd' membuat soal ini berada di tingkat Medium. |

Run 3 — solusi: Garis sejajar adalah garis yang tidak akan pernah berpotongan meskipun diperpanjang. Dengan mengamati kemiringan dan jarak antar garis pada grid: a (horizontal), b (vertikal), c (miring), dan e (miring) memiliki jarak yang tetap dan arah yang sama. Garis d dan f tidak sejajar karena jarak antar garis berubah atau garis bertemu di satu titik.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi pasangan garis sejajar dari beberapa pilihan visual. Ini adalah tugas pengenalan konsep dasar garis sejajar, yang merupakan penerapan langsung dari definisi garis sejajar pada contoh visual yang diberikan.. Bukti: Manakah dari pasangan garis berikut yang sejajar?; a (mendatar), b (tegak), c dan e (miring dengan kemiringan sama) berjarak tetap sehingga tidak pernah bertemu
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang sifat garis sejajar (tidak berpotongan, jarak tetap) melalui representasi visual.. Bukti: Garis-Garis Tegak Lurus dan Garis-Garis Sejajar
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus memeriksa beberapa pasangan garis (a, b, c, d, e, f) dan membedakan mana yang sejajar dan mana yang tidak. Meskipun konsepnya dasar, siswa perlu melakukan observasi visual yang cermat pada setiap pasangan untuk memastikan tidak ada yang berpotongan, yang melibatkan lebih dari satu langkah perbandingan.. Bukti: Manakah dari pasangan garis berikut yang sejajar?; a (mendatar), b (tegak), c dan e (miring dengan kemiringan sama)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang garis dan konsep sejajar (tidak berpotongan). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, membedakan garis sejajar pada grid adalah tugas yang sesuai. Tingkat kesulitan Medium diberikan karena siswa harus mengevaluasi 5-6 pasangan garis secara terpisah untuk menentukan jawaban yang benar, bukan sekadar mengenali satu contoh tunggal. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 175/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.021294; applying=0.978706; reasoning=0.000000 | applying | 0.978706 | 0.093785 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.002327; conceptual=0.994881; procedural=0.002793; metacognitive=0.000000 | conceptual | 0.994881 | 0.025706 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.511406; Medium=0.477624; Hard=0.010969 | Easy | 0.511406 | 0.678471 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.978706; −Σp ln(p) = 0.103034; H = 0.103034/ln(3) = 0.093785; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.994881; −Σp ln(p) = 0.035636; H = 0.035636/ln(4) = 0.025706; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.511406; −Σp ln(p) = 0.745377; H = 0.745377/ln(3) = 0.678471; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Garis-Garis Tegak Lurus dan Garis-Garis Sejajar
Tipe soal: multiple_choice
Stimulus: -
Soal: Manakah dari pasangan garis berikut yang sejajar?
Pilihan: A. a dan b
B. a, b, c, dan e
C. c, d, dan e
D. a, b, c, d, dan e
Transkripsi visual: Soal menampilkan enam gambar (a sampai f) pada latar belakang kotak-kotak (grid). Gambar a menunjukkan dua garis horizontal sejajar. Gambar b menunjukkan dua garis vertikal sejajar. Gambar c menunjukkan dua garis miring sejajar (kemiringan sama). Gambar d menunjukkan dua garis miring yang tidak sejajar (jarak menyempit). Gambar e menunjukkan dua garis miring sejajar (kemiringan sama). Gambar f menunjukkan dua garis miring yang bertemu di satu titik (tidak sejajar).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 37. Soal `087423442be49795c5b1bf93`

Toni sedang menyusun mainan balok.<br><br>Ada berapa banyak balok satuan pada mainan yang Toni susun?

| Opsi | Isi |
|---|---|
| A | 7 |
| B | 14 |
| C | 6 |
| D | 8 |

![Gambar sumber soal 37](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0110-06.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Menghitung jumlah balok satuan: baris bawah depan ada 4 balok, baris bawah belakang ada 2 balok (tersembunyi sebagian), dan baris atas ada 2 balok. Total = 4 + 2 + 2 = 8.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0110-06.png. Transkripsi visual: Gambar menunjukkan susunan balok satuan. Baris depan terdiri dari 4 balok (2 di kiri bawah, 2 di kanan bawah). Di atas 2 balok tengah terdapat 2 balok lagi. Di belakang 2 balok tengah yang bawah, terdapat 2 balok lagi yang menopang balok atas. Total balok: 4 (baris depan bawah) + 2 (baris belakang bawah) + 2 (baris atas) = 8 balok.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5aa661b10ae0d9132375b19957a15573cd56db01583d5908f18a77fef6425c5d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 3552 |
| 2 | success | valid / verified | applying | conceptual | Medium | 5458 |
| 3 | success | valid / verified | applying | conceptual | Medium | 3539 |

Run 1 — solusi: Menghitung jumlah balok satuan: baris bawah depan ada 4 balok, baris bawah belakang ada 2 balok (tersembunyi sebagian), dan baris atas ada 2 balok. Total = 4 + 2 + 2 = 8.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengenali dan menghitung jumlah objek dalam susunan 3D. Ini adalah prosedur langsung untuk memvisualisasikan dan menghitung objek yang terlihat dan yang tersembunyi (inferensi spasial dasar).. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang volume atau jumlah objek dalam susunan 3D, di mana siswa harus memahami bahwa objek yang tidak terlihat sepenuhnya tetap ada dalam struktur.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium karena menuntut siswa untuk melakukan penalaran spasial guna mengidentifikasi balok yang tersembunyi di balik susunan, bukan sekadar menghitung apa yang tampak di permukaan. Ini memerlukan integrasi visual yang sedikit lebih kompleks daripada sekadar menghitung objek 2D.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang objek 3D dan kemampuan menghitung benda konkret. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, membayangkan objek tersembunyi dalam susunan balok adalah tantangan kognitif yang sesuai untuk tingkat Medium, karena memerlukan kemampuan visualisasi spasial di luar apa yang terlihat langsung. |

Run 2 — solusi: Susunan terdiri dari lapisan dasar 2x3 (6 balok) dan lapisan atas 2 balok. Total = 6 + 2 = 8 balok.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman tentang volume bangun ruang sederhana dengan menghitung balok satuan, termasuk menyimpulkan keberadaan balok yang tidak terlihat (tersembunyi) berdasarkan struktur yang tampak.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?; lupa menghitung satu balok yang tersembunyi di belakang susunan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep bangun ruang dan komposisi objek 3D, bukan sekadar prosedur menghitung.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?
- Intended difficulty `classify/Medium`: Soal memerlukan penalaran spasial untuk membayangkan bagian yang tersembunyi. Meskipun operasinya sederhana, siswa harus mengintegrasikan informasi visual untuk menentukan jumlah total balok, yang merupakan tantangan sedang bagi kelas 3.. Bukti: lupa menghitung satu balok yang tersembunyi di belakang susunan; menghitung berlebih, seolah susunan berupa balok besar penuh tanpa celah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang bangun ruang dan kemampuan visualisasi spasial sederhana. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 3 mulai belajar tentang volume dan bangun ruang. Menghitung balok tersembunyi memerlukan kemampuan visualisasi yang sedikit di atas sekadar menghitung objek yang terlihat langsung. |

Run 3 — solusi: Menghitung jumlah balok: baris depan bawah (3) + baris depan atas (2) + baris belakang bawah (3) = 8 balok.
- Domain kognitif `classify/applying`: Siswa diminta untuk menghitung jumlah balok satuan dalam struktur 3D. Ini memerlukan visualisasi spasial untuk mengenali balok yang tersembunyi di balik balok lain, yang merupakan penerapan konsep volume atau jumlah objek dalam konteks rutin.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang struktur bangun ruang yang tersusun dari kubus satuan, di mana siswa harus memahami bahwa objek 3D memiliki bagian yang tidak terlihat langsung.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium bagi kelas 3 karena menuntut siswa untuk melakukan visualisasi spasial (membayangkan bagian yang tersembunyi) dan tidak sekadar menghitung objek yang terlihat langsung. Meskipun prosedurnya sederhana (penjumlahan), integrasi visualisasi spasial meningkatkan tuntutan kognitif.. Bukti: Ada berapa banyak balok satuan pada mainan yang Toni susun?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang objek 3D dan kemampuan menghitung objek. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, membayangkan objek tersembunyi dalam susunan balok adalah tantangan spasial yang sesuai untuk tingkat Medium, karena memerlukan penalaran di luar apa yang terlihat secara langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 139/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000002 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.026283; conceptual=0.968589; procedural=0.005128; metacognitive=0.000000 | conceptual | 0.968589 | 0.110793 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.715260; Medium=0.281129; Hard=0.003611 | Easy | 0.715260 | 0.561376 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000002; H = 0.000002/ln(3) = 0.000002; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.968589; −Σp ln(p) = 0.153591; H = 0.153591/ln(4) = 0.110793; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.715260; −Σp ln(p) = 0.616735; H = 0.616735/ln(3) = 0.561376; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Bangun Ruang
Tipe soal: multiple_choice
Stimulus: -
Soal: Toni sedang menyusun mainan balok.

Ada berapa banyak balok satuan pada mainan yang Toni susun?
Pilihan: A. 7
B. 14
C. 6
D. 8
Transkripsi visual: Gambar menunjukkan susunan balok satuan. Baris depan terdiri dari 4 balok (2 di kiri bawah, 2 di kanan bawah). Di atas 2 balok tengah terdapat 2 balok lagi. Di belakang 2 balok tengah yang bawah, terdapat 2 balok lagi yang menopang balok atas. Total balok: 4 (baris depan bawah) + 2 (baris belakang bawah) + 2 (baris atas) = 8 balok.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 38. Soal `7c1d7c661ba64bbf365e8625`

Hasil penilaian harian Matematika diperoleh: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10<br><br>Berapakah jangkauan data hasil penilaian harian Matematika?

| Opsi | Isi |
|---|---|
| A | 6 |
| B | 5 (10 - 5) |
| C | 15 |
| D | 10 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Data terbesar adalah 10. Data terkecil adalah 5. Jangkauan = data terbesar - data terkecil = 10 - 5 = 5.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c4731220eb73e6d25e960b87a33fcaa8a2250b6eb640ef63dbed43f8622619d5`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2368 |
| 2 | success | valid / verified | applying | procedural | Easy | 2362 |
| 3 | success | valid / verified | applying | procedural | Easy | 2348 |

Run 1 — solusi: Data terbesar adalah 10. Data terkecil adalah 5. Jangkauan = data terbesar - data terkecil = 10 - 5 = 5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik sederhana (menghitung jangkauan) pada sekumpulan data yang diberikan. Ini adalah penerapan langsung dari konsep jangkauan (selisih nilai terbesar dan terkecil) yang merupakan prosedur rutin.. Bukti: Berapakah jangkauan data hasil penilaian harian Matematika?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritme atau metode untuk menghitung jangkauan data, yang termasuk dalam dimensi pengetahuan prosedural.. Bukti: Berapakah jangkauan data hasil penilaian harian Matematika?
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu mengidentifikasi nilai maksimum dan minimum dari data yang tersedia, lalu melakukan satu operasi pengurangan. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10; Berapakah jangkauan data hasil penilaian harian Matematika?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan bilangan cacah dan melakukan pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, mengidentifikasi nilai terbesar dan terkecil dari sekumpulan data serta menghitung selisihnya adalah tugas rutin yang sesuai dengan tingkat perkembangan kognitif mereka. |

Run 2 — solusi: Data terbesar adalah 10 dan data terkecil adalah 5. Jangkauan = data terbesar - data terkecil = 10 - 5 = 5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik sederhana (menghitung jangkauan) pada sekumpulan data yang diberikan. Ini adalah penerapan konsep dasar jangkauan dalam konteks rutin.. Bukti: Berapakah jangkauan data hasil penilaian harian Matematika?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang definisi jangkauan (konsep) dan prosedur pengurangannya (prosedural). Karena fokus utamanya adalah melakukan perhitungan berdasarkan definisi, ini diklasifikasikan sebagai prosedural.. Bukti: Berapakah jangkauan data hasil penilaian harian Matematika?
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu mengidentifikasi nilai maksimum dan minimum dari kumpulan data yang diberikan, lalu melakukan satu operasi pengurangan sederhana. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi nonrutin.. Bukti: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10; Berapakah jangkauan data hasil penilaian harian Matematika?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengurutkan bilangan dan melakukan pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, mengidentifikasi nilai terbesar dan terkecil dari data yang diberikan adalah tugas yang sesuai dengan tingkat perkembangan kognitif dan kurikulum. |

Run 3 — solusi: Data terbesar adalah 10 dan data terkecil adalah 5. Jangkauan = data terbesar - data terkecil = 10 - 5 = 5.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur statistik sederhana (menghitung jangkauan) pada sekumpulan data yang diberikan. Prosedur ini bersifat rutin dan langsung.. Bukti: Berapakah jangkauan data hasil penilaian harian Matematika?
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritme atau metode untuk menghitung jangkauan data (data terbesar dikurangi data terkecil).. Bukti: Berapakah jangkauan data hasil penilaian harian Matematika?
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu mengidentifikasi nilai maksimum dan minimum dari data yang tersedia, lalu melakukan satu operasi pengurangan. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10; Berapakah jangkauan data hasil penilaian harian Matematika?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengurutkan bilangan dan melakukan operasi pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari jangkauan data adalah konsep dasar yang sesuai untuk kelas 3. Tugas ini hanya memerlukan identifikasi nilai ekstrem dan pengurangan sederhana, yang merupakan prosedur rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 88/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.001123; applying=0.998877; reasoning=0.000000 | applying | 0.998877 | 0.007963 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.382692; conceptual=0.578524; procedural=0.038784; metacognitive=0.000000 | conceptual | 0.578524 | 0.584461 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.916176; Medium=0.081825; Hard=0.001999 | Easy | 0.916176 | 0.270754 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.998877; −Σp ln(p) = 0.008748; H = 0.008748/ln(3) = 0.007963; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.578524; −Σp ln(p) = 0.810235; H = 0.810235/ln(4) = 0.584461; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.916176; −Σp ln(p) = 0.297454; H = 0.297454/ln(3) = 0.270754; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Mengurutkan dan Membandingkan Data
Tipe soal: multiple_choice
Stimulus: -
Soal: Hasil penilaian harian Matematika diperoleh: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10

Berapakah jangkauan data hasil penilaian harian Matematika?
Pilihan: A. 6
B. 5 (10 - 5)
C. 15
D. 10
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 39. Soal `50d5212989ff58e40d99d14c`

Perhatikan gambar berikut!<br><br>Berapa banyak bola dalam gambar tersebut?

| Opsi | Isi |
|---|---|
| A | 5 |
| B | 2 |
| C | 3 |
| D | 4 |

![Gambar sumber soal 39](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0220-01.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Mengidentifikasi dan menghitung objek yang berbentuk bola basket dalam gambar. Terdapat satu bola di kiri atas, satu bola di kiri bawah, dan satu bola di kanan tengah. Total bola adalah 3.
Gambar sumber: images/kelas3_panduan_siswa_kelas3.pdf-0220-01.png. Transkripsi visual: Gambar menampilkan kumpulan benda-benda sekolah yang tersebar secara acak. Benda-benda tersebut meliputi buku tulis bertuliskan 'MATH', pensil, penghapus, rautan pensil, dan bola basket. Terdapat tiga buah bola basket yang tersebar di gambar: satu di kiri atas, satu di kiri bawah, dan satu di kanan tengah.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c0dd7aee623e0535cda08ee6d35b4db5085557e4d48c1ec13ac355433774431a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 3419 |
| 2 | success | valid / verified | knowing | factual | Easy | 3395 |
| 3 | success | valid / verified | knowing | factual | Easy | 3438 |

Run 1 — solusi: Mengidentifikasi dan menghitung objek yang berbentuk bola basket dalam gambar. Terdapat satu bola di kiri atas, satu bola di kiri bawah, dan satu bola di kanan tengah. Total bola adalah 3.
- Domain kognitif `classify/knowing`: Soal meminta siswa untuk mengidentifikasi dan menghitung objek tertentu (bola) dari sekumpulan objek lain. Ini adalah tugas pengenalan visual dasar yang langsung, tidak memerlukan strategi kompleks atau penalaran mendalam.. Bukti: Berapa banyak bola dalam gambar tersebut?
- Dimensi pengetahuan `classify/factual`: Siswa perlu mengenali atribut visual dari objek 'bola' untuk membedakannya dari objek lain (buku, pensil, rautan). Ini melibatkan pengetahuan faktual tentang bentuk dan karakteristik objek.. Bukti: Berapa banyak bola dalam gambar tersebut?
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena hanya memerlukan kemampuan observasi dasar untuk menghitung objek yang jelas perbedaannya. Tidak ada langkah perencanaan atau integrasi konsep yang diperlukan.. Bukti: Berapa banyak bola dalam gambar tersebut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret atau gambar hingga 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, tugas menghitung objek visual sederhana adalah tugas dasar yang sangat mudah dan rutin. |

Run 2 — solusi: Mengidentifikasi dan menghitung objek yang berbentuk bola basket dalam gambar. Terdapat satu bola di kiri atas, satu bola di kiri bawah, dan satu bola di kanan tengah. Total ada 3 bola.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi objek tertentu (bola) dari sekumpulan objek lain (buku, pensil, dll) dan menghitung jumlahnya. Ini adalah tugas pengenalan dan penghitungan langsung.. Bukti: Berapa banyak bola dalam gambar tersebut?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji kemampuan siswa dalam mengenali atribut visual dasar (bentuk bola) dan melakukan enumerasi sederhana.. Bukti: Berapa banyak bola dalam gambar tersebut?
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana. Siswa hanya perlu membedakan objek bola dari objek lain yang tidak relevan dan menghitungnya. Tidak ada langkah kompleks atau jebakan yang signifikan.. Bukti: Berapa banyak bola dalam gambar tersebut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret dan membedakan bentuk dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Tugas menghitung objek dalam gambar adalah keterampilan dasar kelas 1-2, sehingga untuk kelas 3 ini sangat mudah. |

Run 3 — solusi: Mengidentifikasi objek yang berbentuk bola basket dalam gambar. Terdapat satu bola di kiri atas, satu bola di kiri bawah, dan satu bola di kanan tengah. Total bola adalah 3.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengenali dan menghitung objek spesifik (bola) di antara objek lain (distraktor) dalam gambar. Ini adalah tugas pengenalan visual langsung yang tidak memerlukan strategi kompleks.. Bukti: Berapa banyak bola dalam gambar tersebut?
- Dimensi pengetahuan `classify/factual`: Tugas ini melibatkan pengenalan elemen dasar (bola) sebagai bagian dari kumpulan objek, yang merupakan pengetahuan faktual tentang klasifikasi objek.. Bukti: Berapa banyak bola dalam gambar tersebut?
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena hanya memerlukan kemampuan observasi visual dasar untuk menghitung objek yang jelas perbedaannya dengan objek lain (buku, pensil, rautan). Tidak ada langkah perencanaan atau integrasi yang diperlukan.. Bukti: Berapa banyak bola dalam gambar tersebut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 3, menghitung objek dalam gambar adalah tugas dasar yang sudah dikuasai sejak kelas awal. Distraktor (rautan/buku) cukup jelas perbedaannya dengan bola. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 121/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000038; applying=0.999962; reasoning=0.000000 | applying | 0.999962 | 0.000391 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.183263; conceptual=0.814784; procedural=0.001953; metacognitive=0.000000 | conceptual | 0.814784 | 0.353493 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.839174; Medium=0.157542; Hard=0.003284 | Easy | 0.839174 | 0.416041 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999962; −Σp ln(p) = 0.000430; H = 0.000430/ln(3) = 0.000391; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.814784; −Σp ln(p) = 0.490045; H = 0.490045/ln(4) = 0.353493; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.839174; −Σp ln(p) = 0.457068; H = 0.457068/ln(3) = 0.416041; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Mengurutkan dan Membandingkan Data
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan gambar berikut!

Berapa banyak bola dalam gambar tersebut?
Pilihan: A. 5
B. 2
C. 3
D. 4
Transkripsi visual: Gambar menampilkan kumpulan benda-benda sekolah yang tersebar secara acak. Benda-benda tersebut meliputi buku tulis bertuliskan 'MATH', pensil, penghapus, rautan pensil, dan bola basket. Terdapat tiga buah bola basket yang tersebar di gambar: satu di kiri atas, satu di kiri bawah, dan satu di kanan tengah.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 40. Soal `631ea2e9a2d5222d502bdf5c`

Hasil penilaian harian Matematika diperoleh: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10<br><br>Berapa banyak siswa yang mendapatkan nilai lebih dari 7?

| Opsi | Isi |
|---|---|
| A | 15 siswa |
| B | 8 siswa |
| C | 10 siswa |
| D | 12 siswa |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Data: 9, 8, 8, 5, 9, 6, 10, 9, 8, 6, 7, 8, 9, 9, 5, 6, 7, 7, 9, 10. Nilai > 7 adalah 8, 9, dan 10. Frekuensi: nilai 8 ada 4, nilai 9 ada 6, nilai 10 ada 2. Total = 4 + 6 + 2 = 12 siswa.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d5918840351ec13f82ac29df307c59ab74b0a8ff6aa0db413651276d0262d642`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2451 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2441 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2453 |

Run 1 — solusi: Data: 9, 8, 8, 5, 9, 6, 10, 9, 8, 6, 7, 8, 9, 9, 5, 6, 7, 7, 9, 10. Nilai > 7 adalah 8, 9, dan 10. Frekuensi nilai 8 ada 4, nilai 9 ada 6, nilai 10 ada 2. Total = 4 + 6 + 2 = 12 siswa.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi nilai yang memenuhi kriteria (lebih dari 7), mengelompokkan data, dan menjumlahkan frekuensinya. Ini adalah penerapan prosedur pengolahan data sederhana pada konteks rutin.. Bukti: Berapa banyak siswa yang mendapatkan nilai lebih dari 7?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan metode penghitungan frekuensi data (tallying atau pengelompokan) untuk menjawab pertanyaan.. Bukti: Hasil penilaian harian Matematika diperoleh: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena menuntut siswa untuk melakukan beberapa langkah terstruktur: menyaring data (nilai > 7), menghitung frekuensi tiap nilai yang memenuhi, dan menjumlahkannya. Meskipun prosedurnya familiar, terdapat risiko kesalahan dalam ketelitian menghitung data yang acak.. Bukti: Berapa banyak siswa yang mendapatkan nilai lebih dari 7?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung frekuensi data dan membandingkan bilangan (lebih dari). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 20 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, mengolah data mentah sebanyak 20 angka memerlukan ketelitian tinggi dalam proses klasifikasi dan penjumlahan, yang merupakan tuntutan kognitif yang sesuai untuk tingkat Medium. |

Run 2 — solusi: Data: 9, 8, 8, 5, 9, 6, 10, 9, 8, 6, 7, 8, 9, 9, 5, 6, 7, 7, 9, 10. Nilai > 7 adalah 8, 9, dan 10. Frekuensi nilai 8 ada 4, nilai 9 ada 6, nilai 10 ada 2. Total = 4 + 6 + 2 = 12 siswa.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi nilai yang memenuhi kriteria (>7), menghitung frekuensi masing-masing nilai tersebut, dan menjumlahkannya. Ini adalah penerapan prosedur pengolahan data sederhana pada konteks rutin.. Bukti: Berapa banyak siswa yang mendapatkan nilai lebih dari 7?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang cara mengorganisasi dan menghitung data mentah ke dalam kategori yang ditentukan (nilai > 7), yang merupakan konsep dasar penyajian data.. Bukti: Hasil penilaian harian Matematika diperoleh: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10
- Intended difficulty `classify/Easy`: Soal ini meminta siswa melakukan klasifikasi data (nilai > 7) dan penjumlahan frekuensi. Langkah-langkahnya jelas dan rutin bagi siswa kelas 3. Tidak ada kendala yang saling berinteraksi secara kompleks.. Bukti: Berapa banyak siswa yang mendapatkan nilai lebih dari 7?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan bilangan (lebih dari) dan menjumlahkan bilangan cacah. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 20 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas mengelompokkan dan menghitung frekuensi data adalah materi standar kelas 3. Prosedur penyelesaiannya langsung dan tidak memerlukan strategi nonrutin. |

Run 3 — solusi: Data: 9, 8, 8, 5, 9, 6, 10, 9, 8, 6, 7, 8, 9, 9, 5, 6, 7, 7, 9, 10. Nilai > 7 adalah 8, 9, dan 10. Frekuensi: nilai 8 ada 4, nilai 9 ada 6, nilai 10 ada 2. Total = 4 + 6 + 2 = 12 siswa.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi nilai yang memenuhi kriteria (lebih dari 7), mengelompokkan data, dan menjumlahkan frekuensinya. Ini adalah penerapan prosedur pengolahan data sederhana pada konteks rutin.. Bukti: Berapa banyak siswa yang mendapatkan nilai lebih dari 7?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang cara mengorganisasi dan menghitung frekuensi data mentah, yang merupakan konsep dasar dalam statistika deskriptif.. Bukti: Hasil penilaian harian Matematika diperoleh: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah terstruktur: menyaring data (nilai > 7), menghitung frekuensi tiap nilai, dan menjumlahkannya. Meskipun prosedurnya rutin, siswa harus teliti dalam mengelompokkan data agar tidak terjadi kesalahan hitung.. Bukti: Berapa banyak siswa yang mendapatkan nilai lebih dari 7?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung frekuensi data dan membandingkan bilangan. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 20 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, mengolah 20 data mentah memerlukan ketelitian dan langkah sistematis yang cukup menantang namun masih dalam taraf rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Medium": 2, "Easy": 1} | majority_2_of_3 / adjudicated | Medium |

Adjudikasi AI: `success`; token `4336`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan prosedur pengolahan data: mengidentifikasi kriteria (>7), menyaring data mentah, menghitung frekuensi, dan menjumlahkan hasilnya. Ini adalah penerapan prosedur rutin pada konteks data.
- Dimensi pengetahuan `procedural`: Siswa menggunakan algoritme atau metode penghitungan frekuensi (tallying) untuk mengolah data mentah menjadi informasi yang diminta.
- Intended difficulty `Medium`: Soal ini dikategorikan Medium karena menuntut ketelitian tinggi dalam memproses 20 data acak. Meskipun prosedurnya rutin, siswa harus melakukan beberapa langkah terstruktur (filter, hitung, jumlah) tanpa bantuan tabel frekuensi yang sudah jadi, sehingga beban kognitif dalam menjaga akurasi cukup signifikan untuk kelas 3.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan bilangan (lebih dari) dan menghitung frekuensi data. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 20 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengolah 20 data mentah secara manual menuntut ketelitian yang cukup tinggi bagi siswa kelas 3. Langkah-langkahnya rutin, namun risiko kesalahan dalam klasifikasi data acak membuat tingkat kesulitannya berada di atas Easy. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 89/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.003469; applying=0.996531; reasoning=0.000000 | applying | 0.996531 | 0.021036 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.325887; conceptual=0.660661; procedural=0.013452; metacognitive=0.000000 | conceptual | 0.660661 | 0.502924 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.902638; Medium=0.095299; Hard=0.002063 | Easy | 0.902638 | 0.299685 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.996531; −Σp ln(p) = 0.023110; H = 0.023110/ln(3) = 0.021036; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.660661; −Σp ln(p) = 0.697200; H = 0.697200/ln(4) = 0.502924; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.902638; −Σp ln(p) = 0.329238; H = 0.329238/ln(3) = 0.299685; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Menyajikan Data dalam Bentuk Tabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Hasil penilaian harian Matematika diperoleh: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10

Berapa banyak siswa yang mendapatkan nilai lebih dari 7?
Pilihan: A. 15 siswa
B. 8 siswa
C. 10 siswa
D. 12 siswa
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 41. Soal `af80792faa77f2a7be932750`

a, b, c, x, y, z, b, c, x, y, a, b, c, a, b, c, x, y, y, b, c, x, y, x, b, c, x, b, c, x, a, y, b, c, x, c, c, b, c,<br><br>Berapa banyak c yang ada pada data tersebut?

| Opsi | Isi |
|---|---|
| A | 11 |
| B | 9 |
| C | 6 |
| D | 8 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Menghitung kemunculan huruf 'c' satu per satu dalam deretan: a, b, c(1), x, y, z, b, c(2), x, y, a, b, c(3), a, b, c(4), x, y, y, b, c(5), x, y, x, b, c(6), x, b, c(7), x, a, y, b, c(8), x, c(9), c(10), b, c(11). Total ada 11 huruf 'c'.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c90e196a0b8c634b6c9ac4a6cee28771daa16a5c18445e5e904ae470007f2f52`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2426 |
| 2 | success | valid / verified | knowing | procedural | Easy | 2474 |
| 3 | success | valid / verified | knowing | factual | Easy | 2383 |

Run 1 — solusi: Menghitung kemunculan huruf 'c' dalam urutan: 1 (setelah b), 2 (setelah b), 3 (setelah b), 4 (setelah b), 5 (setelah b), 6 (setelah b), 7 (setelah b), 8 (setelah b), 9 (setelah b), 10 (setelah c), 11 (setelah b). Total ada 11.
- Domain kognitif `classify/knowing`: Siswa diminta untuk melakukan prosedur penghitungan langsung (counting) terhadap elemen data yang diberikan. Ini adalah tugas rutin yang memerlukan pengenalan dan penghitungan objek, yang masuk dalam domain knowing.. Bukti: Berapa banyak c yang ada pada data tersebut?
- Dimensi pengetahuan `classify/factual`: Tugas ini melibatkan pengenalan simbol (huruf) dan penghitungan frekuensi kemunculannya, yang merupakan pengetahuan faktual tentang data.. Bukti: Berapa banyak c yang ada pada data tersebut?
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin (menghitung frekuensi). Meskipun deret datanya cukup panjang, langkah penyelesaiannya sangat jelas dan tidak memerlukan strategi kompleks atau integrasi antar konsep. Beban kognitif utama hanya pada ketelitian menghitung.. Bukti: a, b, c, x, y, z, b, c, x, y, a, b, c, a, b, c, x, y, y, b, c, x, y, x, b, c, x, b, c, x, a, y, b, c, x, c, c, b, c

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung objek dan ketelitian dalam memilah data. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 3, menghitung frekuensi data dalam deret adalah tugas dasar yang sesuai dengan tingkat perkembangan mereka. Tidak ada tuntutan perencanaan atau penalaran yang kompleks. |

Run 2 — solusi: Menghitung kemunculan huruf 'c' dalam deretan: a, b, c(1), x, y, z, b, c(2), x, y, a, b, c(3), a, b, c(4), x, y, y, b, c(5), x, y, x, b, c(6), x, b, c(7), x, a, y, b, c(8), x, c(9), c(10), b, c(11). Total ada 11 huruf 'c'.
- Domain kognitif `classify/knowing`: Siswa diminta untuk melakukan prosedur penghitungan (counting) yang sangat langsung terhadap data yang diberikan. Tidak ada analisis hubungan atau strategi nonrutin yang diperlukan.. Bukti: Berapa banyak c yang ada pada data tersebut?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji kemampuan dasar dalam mengidentifikasi dan menghitung frekuensi elemen dalam sebuah kumpulan data, yang merupakan bagian dari pengetahuan prosedural dasar.. Bukti: Berapa banyak c yang ada pada data tersebut?
- Intended difficulty `classify/Easy`: Soal ini dikategorikan Easy karena tugas utamanya adalah menghitung frekuensi (counting) yang merupakan prosedur familiar bagi siswa kelas 3. Meskipun deretan datanya cukup panjang, tidak ada kendala yang berinteraksi atau kebutuhan untuk memilih strategi yang kompleks. Jalur penyelesaian sangat jelas (menghitung satu per satu).. Bukti: a, b, c, x, y, z, b, c, x, y, a, b, c, a, b, c, x, y, y, b, c, x, y, x, b, c, x, b, c, x, a, y, b, c, x, c, c, b, c

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung dan ketelitian dalam mengidentifikasi objek. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 3, menghitung frekuensi dari daftar data adalah tugas rutin. Panjang data yang diberikan tidak mengubah tingkat kesulitan kognitif menjadi Medium atau Hard karena tidak ada tuntutan integrasi atau perencanaan. |

Run 3 — solusi: Menghitung kemunculan huruf 'c' dalam urutan: c (1), c (2), c (3), c (4), c (5), c (6), c (7), c (8), c (9), c (10), c (11). Total ada 11.
- Domain kognitif `classify/knowing`: Siswa diminta untuk melakukan prosedur penghitungan langsung (counting) terhadap data yang diberikan. Tidak ada strategi kompleks atau inferensi yang diperlukan, hanya ketelitian dalam menghitung frekuensi item tertentu.. Bukti: Berapa banyak c yang ada pada data tersebut?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji kemampuan dasar dalam mengidentifikasi dan menghitung elemen dalam kumpulan data, yang merupakan pengetahuan faktual tentang frekuensi data.. Bukti: Berapa banyak c yang ada pada data tersebut?
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin. Siswa hanya perlu menghitung kemunculan satu item spesifik. Meskipun urutannya cukup panjang, tidak ada kendala yang berinteraksi atau kebutuhan untuk memilih strategi; siswa hanya perlu melakukan penghitungan linear yang sederhana.. Bukti: a, b, c, x, y, z, b, c, x, y, a, b, c, a, b, c, x, y, y, b, c, x, y, x, b, c, x, b, c, x, a, y, b, c, x, c, c, b, c

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung dan membedakan simbol/huruf. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 3, menghitung frekuensi data dalam daftar adalah tugas rutin yang sesuai dengan tingkat perkembangan kognitif mereka. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4284`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa diminta melakukan prosedur penghitungan langsung (counting) terhadap elemen data yang diberikan. Ini adalah tugas rutin yang memerlukan pengenalan dan penghitungan objek, yang masuk dalam domain knowing.
- Dimensi pengetahuan `factual`: Tugas ini melibatkan pengenalan simbol (huruf) dan penghitungan frekuensi kemunculannya, yang merupakan pengetahuan faktual tentang data.
- Intended difficulty `Easy`: Soal ini bersifat rutin (menghitung frekuensi). Meskipun deret datanya cukup panjang, langkah penyelesaiannya sangat jelas dan tidak memerlukan strategi kompleks atau integrasi antar konsep. Beban kognitif utama hanya pada ketelitian menghitung.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung objek dan ketelitian dalam memilah data. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 3, menghitung frekuensi data dalam deret adalah tugas dasar yang sesuai dengan tingkat perkembangan mereka. Tidak ada tuntutan perencanaan atau penalaran yang kompleks. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 136/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.496660; applying=0.503340; reasoning=0.000000 | applying | 0.503340 | 0.630909 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.054010; conceptual=0.943489; procedural=0.002501; metacognitive=0.000000 | conceptual | 0.943489 | 0.164107 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.775324; Medium=0.220530; Hard=0.004146 | Easy | 0.775324 | 0.503746 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.503340; −Σp ln(p) = 0.693125; H = 0.693125/ln(3) = 0.630909; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.943489; −Σp ln(p) = 0.227501; H = 0.227501/ln(4) = 0.164107; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.775324; −Σp ln(p) = 0.553421; H = 0.553421/ln(3) = 0.503746; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Menyajikan Data dalam Bentuk Tabel
Tipe soal: multiple_choice
Stimulus: -
Soal: a, b, c, x, y, z, b, c, x, y, a, b, c, a, b, c, x, y, y, b, c, x, y, x, b, c, x, b, c, x, a, y, b, c, x, c, c, b, c,

Berapa banyak c yang ada pada data tersebut?
Pilihan: A. 11
B. 9
C. 6
D. 8
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 42. Soal `655cea6ab3fa2ff165080502`

Kira sedang mendata kue kesukaan teman-teman sekelasnya. Berikut adalah data yang Kira dapatkan. Diagram Gambar Kue Kesukaan. Setiap gambar mewakili 1 anak. Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.<br><br>Ada 5 anak yang suka onde-onde.<br>Ada 3 anak yang suka lemper.<br>Ada 7 anak yang suka kue talam.<br><br>Ada .... anak yang suka kue cucur.

| Opsi | Isi |
|---|---|
| A | 3 |
| B | 5 |
| C | 7 |
| D | 6 |

![Gambar sumber soal 42](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0254-04.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Menghitung jumlah bintang pada baris kue cucur di diagram gambar. Terdapat 6 bintang, yang berarti ada 6 anak yang menyukai kue cucur. Pilihan yang sesuai adalah D.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0254-04.png. Transkripsi visual: Diagram gambar menampilkan empat jenis kue dengan jumlah bintang di sampingnya. Baris pertama (kue cucur) memiliki 6 bintang. Baris kedua (onde-onde) memiliki 5 bintang. Baris ketiga (lemper) memiliki 3 bintang. Baris keempat (kue talam) memiliki 7 bintang. Keterangan menyatakan setiap gambar bintang mewakili 1 anak.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 3 / Matematika SD Kelas 3. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2058712c07fbec74674a04cc530b3c572945e80e287c23b64be74975900c9584`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 3508 |
| 2 | success | valid / verified | knowing | factual | Easy | 3509 |
| 3 | success | valid / verified | knowing | factual | Easy | 3482 |

Run 1 — solusi: Menghitung jumlah bintang pada baris kue cucur di diagram gambar. Terdapat 6 bintang, yang berarti ada 6 anak yang menyukai kue cucur. Pilihan yang sesuai adalah D.
- Domain kognitif `classify/knowing`: Siswa diminta untuk membaca data dari diagram gambar (pictograph) dan melakukan penghitungan langsung (counting) untuk menentukan jumlah anak yang menyukai kue cucur. Ini adalah prosedur yang sangat langsung dan rutin.. Bukti: Kira sedang mendata kue kesukaan teman-teman sekelasnya.; Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.; Ada .... anak yang suka kue cucur.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman siswa terhadap representasi data sederhana dalam bentuk diagram gambar, yang merupakan elemen dasar dalam literasi data.. Bukti: Diagram Gambar Kue Kesukaan.; Setiap gambar mewakili 1 anak.
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena hanya memerlukan penghitungan langsung (counting) objek visual yang sudah terstruktur. Tidak ada langkah tambahan atau integrasi yang diperlukan.. Bukti: Ada .... anak yang suka kue cucur.; Setiap gambar mewakili 1 anak.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret atau gambar (1-10). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 3 sudah sangat familiar dengan membaca diagram gambar sederhana. Tugas ini hanya memerlukan ketelitian dalam menghitung jumlah simbol yang tersedia. |

Run 2 — solusi: Menghitung jumlah simbol bintang pada baris kue cucur di diagram gambar. Terdapat 6 simbol bintang, yang berarti ada 6 anak yang menyukai kue cucur.
- Domain kognitif `classify/knowing`: Siswa diminta untuk membaca data dari diagram gambar (piktogram) secara langsung. Tugas ini hanya memerlukan kemampuan mengenali dan menghitung simbol yang sudah tersedia, yang merupakan prosedur yang sangat langsung.. Bukti: Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.; Ada .... anak yang suka kue cucur.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman siswa terhadap representasi data sederhana (piktogram) di mana satu simbol mewakili satu unit data (fakta).. Bukti: Diagram Gambar Kue Kesukaan; Setiap gambar mewakili 1 anak
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena siswa hanya perlu menghitung jumlah simbol bintang pada baris yang ditanyakan. Tidak ada langkah tambahan, integrasi, atau manipulasi data yang diperlukan.. Bukti: Ada .... anak yang suka kue cucur.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang benda konkret atau simbol. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 3 sudah terbiasa membaca piktogram sederhana dengan skala 1:1. Tugas ini adalah tugas dasar membaca data tanpa kompleksitas tambahan. |

Run 3 — solusi: Menghitung jumlah bintang pada baris kue cucur di diagram gambar. Terdapat 6 bintang, sehingga ada 6 anak yang suka kue cucur.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan pembacaan langsung data dari diagram gambar (pictograph) dengan menghitung jumlah simbol yang tersedia. Tidak ada manipulasi data atau interpretasi kompleks yang diperlukan.. Bukti: Ada .... anak yang suka kue cucur.; Diagram Gambar Kue Kesukaan. Setiap gambar mewakili 1 anak.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman siswa terhadap representasi data sederhana dalam bentuk diagram gambar (piktogram), yang merupakan pengetahuan faktual tentang cara membaca simbol dalam statistik dasar.. Bukti: Diagram Gambar Kue Kesukaan.; Setiap gambar mewakili 1 anak.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar. Siswa hanya perlu menghitung jumlah objek (bintang) pada satu baris yang sudah ditentukan. Tidak ada langkah perantara, tidak ada perbandingan, dan tidak ada kendala yang harus dipecahkan.. Bukti: Ada .... anak yang suka kue cucur.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret atau simbol. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Membaca diagram gambar sederhana adalah materi standar kelas 3. Tugas ini hanya memerlukan penghitungan satu-ke-satu yang sangat rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 191/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000001; applying=0.999999; reasoning=0.000000 | applying | 0.999999 | 0.000011 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.003408; conceptual=0.986032; procedural=0.010560; metacognitive=0.000000 | conceptual | 0.986032 | 0.058635 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.606997; Medium=0.381598; Hard=0.011405 | Easy | 0.606997 | 0.656902 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999999; −Σp ln(p) = 0.000012; H = 0.000012/ln(3) = 0.000011; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.986032; −Σp ln(p) = 0.081286; H = 0.081286/ln(4) = 0.058635; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.606997; −Σp ln(p) = 0.721681; H = 0.721681/ln(3) = 0.656902; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 3
Topik: Matematika SD Kelas 3
Subtopik: Diagram Gambar
Tipe soal: multiple_choice
Stimulus: -
Soal: Kira sedang mendata kue kesukaan teman-teman sekelasnya. Berikut adalah data yang Kira dapatkan. Diagram Gambar Kue Kesukaan. Setiap gambar mewakili 1 anak. Lengkapi setiap kalimat berikut sesuai dengan diagram di atas.

Ada 5 anak yang suka onde-onde.
Ada 3 anak yang suka lemper.
Ada 7 anak yang suka kue talam.

Ada .... anak yang suka kue cucur.
Pilihan: A. 3
B. 5
C. 7
D. 6
Transkripsi visual: Diagram gambar menampilkan empat jenis kue dengan jumlah bintang di sampingnya. Baris pertama (kue cucur) memiliki 6 bintang. Baris kedua (onde-onde) memiliki 5 bintang. Baris ketiga (lemper) memiliki 3 bintang. Baris keempat (kue talam) memiliki 7 bintang. Keterangan menyatakan setiap gambar bintang mewakili 1 anak.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
