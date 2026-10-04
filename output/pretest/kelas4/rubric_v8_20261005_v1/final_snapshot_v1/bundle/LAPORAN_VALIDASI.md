# Validasi ulang soal kelas 4 — Gemini blind N=3 dan diagnostik IndoBERT

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v10-blind-key-verified`. Rubrik: `math-rubric-3x4x3-v8-sd-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 4 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan menjadi keputusan silver operasional.

Checkpoint dikunci dengan SHA-256 sebelum inferensi IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Prediksi model dipakai sebagai diagnostik; tidak diberikan kembali ke Gemini.

Jumlah soal: 18; distribusi label advisory: `{"mathCognitiveDomain": {"applying": 15, "knowing": 3, "reasoning": 0}, "knowledgeDimension": {"conceptual": 11, "procedural": 7, "factual": 0, "metacognitive": 0}, "intendedDifficulty": {"Easy": 15, "Medium": 3, "Hard": 0}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"applying": 15, "knowing": 3, "reasoning": 0}, "knowledgeDimension": {"conceptual": 11, "procedural": 7, "factual": 0, "metacognitive": 0}, "intendedDifficulty": {"Easy": 15, "Medium": 3, "Hard": 0}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"silver_ready": 18}`.
Run awal sukses: 54/54; adjudikasi: 7; token sukses tercatat: 198,886.

Seluruh label memakai provenance ai_silver. Delivery memakai snapshot silver yang lolos qualification. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

Artifact diagnostik IndoBERT: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Dataset training: `kelas1-gemini-silver-n3-v1`. Approval provisional: `False`; research-only: `False`; gate data: `False`; anti-collapse: `False`; gate promosi: `False`. Packaging ini tidak melakukan training atau promosi model.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten dapat masuk snapshot silver operasional.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 15 | 15 | [Easy.json](difficulty/Easy.json) |
| Medium | 3 | 3 | [Medium.json](difficulty/Medium.json) |
| Hard | 0 | 0 | [Hard.json](difficulty/Hard.json) |

## Perhitungan yang dipakai

Encoder menghasilkan representasi [CLS], lalu tiga head menghasilkan logits. Probabilitas adalah pᵢ = exp(zᵢ/T) / Σⱼ exp(zⱼ/T), dengan temperature sesuai manifest. Confidence = max(pᵢ). Entropy H = −Σᵢ pᵢ ln(pᵢ) / ln(K). Probabilitas, confidence, entropy, dan action di bawah berasal dari inferensi lokal; tidak dibuat oleh Gemini.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

## 1. Soal `bc95fc44d6c120fad4812c7c`

Slamet membantu ibu membagikan beras kepada masyarakat kurang mampu. Total beras yang dibagikan oleh Ibu Slamet 10 kg. Ibu Slamet akan membagikan semua beras ke beberapa orang dengan berat yang sama. Bantulah ibu Slamet untuk membagikan beras tersebut. Berapa kemungkinan banyaknya orang yang akan mendapat pembagian beras dari Ibu Slamet?

| Opsi | Isi |
|---|---|
| A | 1 orang, 2 orang, 5 orang, atau 10 orang |
| B | 10 orang, 20 orang, 30 orang, atau 40 orang |
| C | 1 orang, 2 orang, 3 orang, 5 orang, atau 10 orang |
| D | 2 orang, 3 orang, 4 orang, atau 5 orang |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Beras 10 kg dibagi sama berat berarti jumlah orang harus merupakan faktor dari 10. Faktor dari 10 adalah bilangan yang habis membagi 10, yaitu 1, 2, 5, dan 10.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c93b160e550f86b9857c772593f98105e466567cd334563f2de2d279fc8f4050`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2425 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2357 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2399 |

Run 1 — solusi: Beras 10 kg dibagi sama berat berarti jumlah orang harus merupakan faktor dari 10. Faktor dari 10 adalah bilangan yang habis membagi 10, yaitu 1, 2, 5, dan 10.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi konsep pembagian rata (tanpa sisa) sebagai konsep faktor. Ini adalah penerapan konsep faktor pada konteks pembagian sederhana yang rutin bagi kelas 4.. Bukti: Total beras yang dibagikan oleh Ibu Slamet 10 kg. Ibu Slamet akan membagikan semua beras ke beberapa orang dengan berat yang sama.; Berapa kemungkinan banyaknya orang yang akan mendapat pembagian beras dari Ibu Slamet?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang faktor bilangan dalam konteks pembagian.. Bukti: Berapa kemungkinan banyaknya orang yang akan mendapat pembagian beras dari Ibu Slamet?
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu mencari faktor dari 10. Konteks pembagian beras adalah situasi rutin, jalur penyelesaiannya langsung (mencari faktor), dan tidak ada kendala yang berinteraksi atau langkah yang kompleks.. Bukti: Total beras yang dibagikan oleh Ibu Slamet 10 kg.; Ibu Slamet akan membagikan semua beras ke beberapa orang dengan berat yang sama.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pembagian dan konsep faktor bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari faktor dari bilangan kecil (10) adalah materi standar kelas 4 yang bersifat rutin. |

Run 2 — solusi: Banyak orang yang menerima beras harus merupakan faktor dari 10 kg agar pembagian sama rata tanpa sisa. Faktor dari 10 adalah 1, 2, 5, dan 10.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi konsep faktor dari bilangan 10 untuk menentukan kemungkinan jumlah orang yang menerima pembagian beras secara merata. Ini adalah penerapan konsep faktor pada konteks pembagian rutin.. Bukti: Berapa kemungkinan banyaknya orang yang akan mendapat pembagian beras dari Ibu Slamet?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara pembagian rata (tanpa sisa) dan konsep faktor bilangan.. Bukti: Total beras yang dibagikan oleh Ibu Slamet 10 kg.; membagikan semua beras ke beberapa orang dengan berat yang sama
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu mencari faktor dari 10. Konsep faktor adalah materi dasar kelas 4. Tidak ada kendala yang berinteraksi atau perencanaan langkah yang kompleks.. Bukti: Total beras yang dibagikan oleh Ibu Slamet 10 kg.; membagikan semua beras ke beberapa orang dengan berat yang sama

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pembagian dan konsep faktor bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari faktor dari bilangan kecil (10) adalah tugas rutin yang sesuai dengan kurikulum kelas 4. |

Run 3 — solusi: Total beras 10 kg harus dibagi sama rata, artinya jumlah orang harus merupakan faktor dari 10. Faktor dari 10 adalah bilangan yang membagi habis 10, yaitu 1, 2, 5, dan 10.
- Domain kognitif `classify/applying`: Siswa perlu memahami konsep faktor sebagai pembagi yang menghasilkan sisa nol dalam konteks pembagian sama rata. Ini melibatkan penerapan konsep faktor pada situasi nyata, yang masuk dalam kategori applying.. Bukti: membagikan semua beras ke beberapa orang dengan berat yang sama; Berapa kemungkinan banyaknya orang yang akan mendapat pembagian beras
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang hubungan antara pembagian sama rata dan konsep faktor bilangan, yang merupakan pengetahuan konseptual.. Bukti: membagikan semua beras ke beberapa orang dengan berat yang sama
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu mengidentifikasi faktor dari 10. Prosedur ini familiar bagi kelas 4, jalur penyelesaiannya langsung, dan tidak ada kendala yang saling berinteraksi.. Bukti: Total beras yang dibagikan oleh Ibu Slamet 10 kg; membagikan semua beras ke beberapa orang dengan berat yang sama

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pembagian dan konsep faktor bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari faktor dari bilangan kecil (10) adalah materi standar kelas 4 yang rutin dan tidak memerlukan perencanaan kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 150/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000000 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.007631; conceptual=0.961604; procedural=0.030765; metacognitive=0.000000 | conceptual | 0.961604 | 0.131257 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.736125; Medium=0.257232; Hard=0.006643 | Easy | 0.736125 | 0.553506 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000000; H = 0.000000/ln(3) = 0.000000; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.961604; −Σp ln(p) = 0.181960; H = 0.181960/ln(4) = 0.131257; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.736125; −Σp ln(p) = 0.608089; H = 0.608089/ln(3) = 0.553506; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 4
Topik: Matematika SD Kelas 4
Subtopik: Faktor dan Kelipatan
Tipe soal: multiple_choice
Stimulus: -
Soal: Slamet membantu ibu membagikan beras kepada masyarakat kurang mampu. Total beras yang dibagikan oleh Ibu Slamet 10 kg. Ibu Slamet akan membagikan semua beras ke beberapa orang dengan berat yang sama. Bantulah ibu Slamet untuk membagikan beras tersebut. Berapa kemungkinan banyaknya orang yang akan mendapat pembagian beras dari Ibu Slamet?
Pilihan: A. 1 orang, 2 orang, 5 orang, atau 10 orang
B. 10 orang, 20 orang, 30 orang, atau 40 orang
C. 1 orang, 2 orang, 3 orang, 5 orang, atau 10 orang
D. 2 orang, 3 orang, 4 orang, atau 5 orang
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `51d112e2cf5ac0ac6feceb42`

Tentukan faktor dari:<br><br>a. 27

| Opsi | Isi |
|---|---|
| A | 1, 3, 6, 9, 27 |
| B | 1, 3, 9, 27 |
| C | 1, 2, 7, 27 |
| D | 3, 9 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Faktor dari 27 adalah bilangan yang membagi habis 27. Pasangan faktor dari 27 adalah 1 x 27 dan 3 x 9. Jadi, faktor dari 27 adalah 1, 3, 9, 27.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `09729e8835a418bb950569a715c38030973b45d1ce4e2315662c31da81538e93`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2215 |
| 2 | success | valid / verified | knowing | procedural | Easy | 3056 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2123 |

Run 1 — solusi: Faktor dari 27 adalah bilangan yang membagi habis 27. 27 = 1 x 27 dan 27 = 3 x 9. Maka faktornya adalah 1, 3, 9, 27.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi faktor dari bilangan 27. Ini adalah prosedur langsung yang melibatkan pengingatan definisi faktor dan pembagian dasar.. Bukti: Tentukan faktor dari: a. 27
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep faktor, yang merupakan bagian dari pengetahuan konseptual tentang hubungan pembagian.. Bukti: Tentukan faktor dari: a. 27
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin bagi siswa kelas 4 yang sudah mempelajari konsep faktor. Tidak ada langkah yang saling bergantung atau kendala yang kompleks.. Bukti: Tentukan faktor dari: a. 27

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang perkalian dan pembagian. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menentukan faktor bilangan dua digit adalah materi standar kelas 4 yang bersifat rutin. |

Run 2 — solusi: Faktor dari 27 dicari dengan mencari pasangan bilangan yang hasil kalinya 27: 1 x 27 = 27 dan 3 x 9 = 27. Jadi, faktornya adalah 1, 3, 9, 27.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan prosedur standar untuk mencari faktor dari bilangan bulat kecil, yang merupakan tugas rutin.. Bukti: Tentukan faktor dari: a. 27
- Dimensi pengetahuan `classify/procedural`: Tugas ini memerlukan penerapan algoritma atau metode untuk menentukan faktor bilangan.. Bukti: Tentukan faktor dari: a. 27
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung bagi siswa kelas 4. Tidak ada kendala atau langkah kompleks yang diperlukan.. Bukti: Tentukan faktor dari: a. 27

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman perkalian dasar dan pembagian. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari faktor bilangan adalah materi dasar kelas 4 yang diajarkan secara eksplisit. |

Run 3 — solusi: Faktor dari 27 adalah bilangan yang membagi habis 27. 27 dibagi 1 = 27, 27 dibagi 3 = 9. Jadi, faktornya adalah 1, 3, 9, 27.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi faktor dari bilangan 27. Ini adalah prosedur langsung yang melibatkan pembagian atau perkalian dasar untuk menemukan pasangan faktor, yang merupakan tugas rutin dalam kurikulum kelas 4.. Bukti: Tentukan faktor dari: a. 27
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang definisi faktor (bilangan yang membagi habis bilangan lain), yang merupakan konsep dasar dalam aritmatika.. Bukti: Tentukan faktor dari: a. 27
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin bagi siswa kelas 4. Tidak ada langkah yang saling bergantung atau kendala kompleks. Siswa hanya perlu menerapkan definisi faktor secara sistematis.. Bukti: Tentukan faktor dari: a. 27

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman perkalian dan pembagian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menentukan faktor bilangan dua digit adalah materi standar kelas 4 yang bersifat prosedural dan rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4263`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa diminta mengidentifikasi faktor dari bilangan 27. Ini adalah tugas rutin yang menguji pemahaman definisi faktor melalui prosedur pembagian atau perkalian dasar.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konsep faktor sebagai bilangan yang membagi habis bilangan lain.
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu menerapkan definisi faktor untuk bilangan kecil. Tidak ada langkah kompleks atau kendala yang harus dipecahkan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar perkalian dan pembagian. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menentukan faktor bilangan adalah materi standar kelas 4 yang bersifat rutin. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 76/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.988245; applying=0.011755; reasoning=0.000000 | knowing | 0.988245 | 0.058182 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.709987; conceptual=0.273535; procedural=0.016478; metacognitive=0.000000 | factual | 0.709987 | 0.480001 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.889270; Medium=0.108331; Hard=0.002398 | Easy | 0.889270 | 0.327323 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.988245; −Σp ln(p) = 0.063919; H = 0.063919/ln(3) = 0.058182; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.709987; −Σp ln(p) = 0.665423; H = 0.665423/ln(4) = 0.480001; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.889270; −Σp ln(p) = 0.359601; H = 0.359601/ln(3) = 0.327323; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 4
Topik: Matematika SD Kelas 4
Subtopik: Faktor dan Kelipatan
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan faktor dari:

a. 27
Pilihan: A. 1, 3, 6, 9, 27
B. 1, 3, 9, 27
C. 1, 2, 7, 27
D. 3, 9
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "conceptual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `d8e3e19d701550680f504300`

Tentukan pembagian berikut sebagai pengurangan berulang!<br><br>16 : 4 = .....

| Opsi | Isi |
|---|---|
| A | 3 kali (16-4-4-4=4) |
| B | 4 kali (16-4-4-4-4=0) |
| C | 5 kali (20-4-4-4-4-4=0) |
| D | 12 kali (16-4=12, dianggap tiap kali kurang 1) |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Pembagian 16 : 4 berarti 16 dikurangi 4 secara berulang sampai hasilnya 0. Langkahnya: 16 - 4 = 12 (1), 12 - 4 = 8 (2), 8 - 4 = 4 (3), 4 - 4 = 0 (4). Jadi, ada 4 kali pengurangan.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c704254fcd1a6bfd045187815b4674cb6c05497bad139cf5be45296fa559a57c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2283 |
| 2 | success | valid / verified | applying | procedural | Easy | 2273 |
| 3 | success | valid / verified | applying | procedural | Easy | 2271 |

Run 1 — solusi: Pembagian 16 : 4 adalah pengurangan 4 dari 16 secara berulang sampai hasilnya 0. Langkahnya: 16 - 4 = 12, 12 - 4 = 8, 8 - 4 = 4, 4 - 4 = 0. Ada 4 kali pengurangan.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep pembagian sebagai pengurangan berulang yang merupakan prosedur standar dalam pembelajaran pembagian di kelas 4.. Bukti: Tentukan pembagian berikut sebagai pengurangan berulang! 16 : 4 = .....
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang hubungan antara operasi pembagian dan pengurangan berulang, yang merupakan aspek konseptual dari operasi hitung.. Bukti: Tentukan pembagian berikut sebagai pengurangan berulang!
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan familiar bagi siswa kelas 4. Prosedur pengurangan berulang adalah metode dasar yang diajarkan untuk memahami pembagian. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi nonrutin.. Bukti: 16 : 4 = .....

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
| gradeRelativeRationale | Siswa kelas 4 sudah terbiasa dengan konsep pembagian sebagai pengurangan berulang. Soal ini menguji pemahaman dasar tanpa kompleksitas tambahan. |

Run 2 — solusi: Pembagian 16 : 4 berarti 16 dikurangi 4 secara berulang sampai hasilnya 0. Langkahnya: 16 - 4 = 12 (1), 12 - 4 = 8 (2), 8 - 4 = 4 (3), 4 - 4 = 0 (4). Jadi, ada 4 kali pengurangan.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep pembagian sebagai pengurangan berulang, yang merupakan prosedur standar dan langsung untuk memahami makna pembagian di kelas 4.. Bukti: Tentukan pembagian berikut sebagai pengurangan berulang! 16 : 4 = .....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa tentang prosedur pengurangan berulang sebagai representasi dari konsep pembagian.. Bukti: Tentukan pembagian berikut sebagai pengurangan berulang!
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu melakukan pengurangan berulang sederhana dengan angka kecil yang familiar bagi kelas 4.. Bukti: 16 : 4 = .....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dan pembagian dasar. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pengurangan berulang adalah materi dasar pembagian di kelas 4. Soal ini tidak menuntut perencanaan kompleks atau integrasi konsep yang sulit. |

Run 3 — solusi: Pembagian 16 : 4 berarti 16 dikurangi 4 secara berulang sampai hasilnya 0. Langkahnya: 16 - 4 = 12 (1), 12 - 4 = 8 (2), 8 - 4 = 4 (3), 4 - 4 = 0 (4). Jadi, ada 4 kali pengurangan.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pengurangan berulang untuk menyelesaikan pembagian. Ini adalah penerapan prosedur standar yang sudah dipelajari di kelas 4.. Bukti: Tentukan pembagian berikut sebagai pengurangan berulang! 16 : 4 = .....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau metode pengurangan berulang sebagai representasi dari operasi pembagian.. Bukti: Tentukan pembagian berikut sebagai pengurangan berulang!
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu melakukan pengurangan berulang sederhana dengan angka kecil yang familiar bagi kelas 4.. Bukti: 16 : 4 = .....

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
| gradeRelativeRationale | Pengurangan berulang adalah materi dasar kelas 4. Soal ini tidak memerlukan perencanaan kompleks atau integrasi konsep yang sulit. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 1, "procedural": 2} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3641`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan prosedur pengurangan berulang untuk menyelesaikan pembagian. Ini adalah penerapan prosedur standar yang sudah dipelajari di kelas 4.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman tentang algoritma atau metode pengurangan berulang sebagai representasi dari operasi pembagian.
- Intended difficulty `Easy`: Soal ini bersifat rutin dan langsung. Siswa hanya perlu melakukan pengurangan berulang sederhana dengan angka kecil yang familiar bagi kelas 4.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dan pembagian dasar. |
| dependentSteps | 4 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pengurangan berulang adalah materi dasar kelas 4. Soal ini tidak memerlukan perencanaan kompleks atau integrasi konsep yang sulit. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 122/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000062; applying=0.999938; reasoning=0.000000 | applying | 0.999938 | 0.000606 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.027436; conceptual=0.955121; procedural=0.017443; metacognitive=0.000000 | conceptual | 0.955121 | 0.153747 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.840881; Medium=0.156597; Hard=0.002522 | Easy | 0.840881 | 0.410666 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999938; −Σp ln(p) = 0.000666; H = 0.000666/ln(3) = 0.000606; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.955121; −Σp ln(p) = 0.213139; H = 0.213139/ln(4) = 0.153747; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.840881; −Σp ln(p) = 0.451162; H = 0.451162/ln(3) = 0.410666; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 4
Topik: Matematika SD Kelas 4
Subtopik: Pembagian Bilangan Cacah sampai 100
Tipe soal: multiple_choice
Stimulus: -
Soal: Tentukan pembagian berikut sebagai pengurangan berulang!

16 : 4 = .....
Pilihan: A. 3 kali (16-4-4-4=4)
B. 4 kali (16-4-4-4-4=0)
C. 5 kali (20-4-4-4-4-4=0)
D. 12 kali (16-4=12, dianggap tiap kali kurang 1)
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `f01f2f8c93ea076e4331abae`

Nazilla bisa menjawab dengan benar 6 pertanyaan dari 10 soal yang diberikan. Tentukan berapa persen soal yang dijawab benar tersebut !

| Opsi | Isi |
|---|---|
| A | 0,6% |
| B | 40% |
| C | 60% |
| D | 6% |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: 6/10 = 60/100 = 60%.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `['mengidentifikasi', 'menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b90c90cb97c1c12c12f8a4616141dc11dbcc66053c0fea60fbdf065ac2fa5025`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2257 |
| 2 | success | valid / verified | applying | procedural | Easy | 2272 |
| 3 | success | valid / verified | applying | procedural | Easy | 2257 |

Run 1 — solusi: 6/10 = 60/100 = 60%.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur konversi pecahan ke persen yang sudah dipelajari. Soal ini merupakan penerapan rutin dari konsep pecahan per sepuluh menjadi per seratus (persen).. Bukti: Nazilla bisa menjawab dengan benar 6 pertanyaan dari 10 soal yang diberikan. Tentukan berapa persen soal yang dijawab benar tersebut
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma atau metode konversi pecahan ke persen (mengubah penyebut menjadi 100).. Bukti: 6 pertanyaan dari 10 soal; berapa persen
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 4 yang sudah mempelajari hubungan pecahan dan persen. Langkah penyelesaiannya langsung (mengubah 6/10 menjadi 60/100) tanpa kendala yang saling berinteraksi atau kebutuhan strategi nonrutin.. Bukti: 6 pertanyaan dari 10 soal; berapa persen

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman pecahan senilai dan konsep dasar persen sebagai per seratus. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konversi pecahan 6/10 ke persen adalah materi standar kelas 4. Siswa hanya perlu melakukan satu langkah konversi penyebut ke 100, yang merupakan prosedur familiar. |

Run 2 — solusi: 6/10 = 60/100 = 60%
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur mengubah pecahan biasa ke bentuk persen. Prosedur ini merupakan materi rutin yang dipelajari di kelas 4, sehingga termasuk dalam domain applying.. Bukti: Nazilla bisa menjawab dengan benar 6 pertanyaan dari 10 soal; Tentukan berapa persen soal yang dijawab benar
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan antara pecahan dan persen, yang merupakan pengetahuan konseptual, serta penggunaan algoritma konversi pecahan ke persen, yang merupakan pengetahuan prosedural. Fokus utama adalah pada prosedur konversi.. Bukti: 6 pertanyaan dari 10 soal; Tentukan berapa persen
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu melakukan konversi pecahan sederhana (6/10) ke persen. Prosedur ini sangat familiar bagi siswa kelas 4, jalur penyelesaiannya langsung, dan tidak ada kendala yang berinteraksi atau kebutuhan perencanaan yang kompleks.. Bukti: 6 pertanyaan dari 10 soal; Tentukan berapa persen

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman pecahan sebagai bagian dari keseluruhan dan konsep persen sebagai per seratus. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konversi pecahan ke persen adalah materi standar kelas 4. Soal ini tidak menuntut penalaran tingkat tinggi atau perencanaan strategi, sehingga tingkat kesulitannya rendah bagi siswa kelas 4. |

Run 3 — solusi: 6/10 = 60/100 = 60%.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur mengubah pecahan biasa ke bentuk persen. Prosedur ini merupakan materi rutin yang dipelajari di kelas 4 untuk menghubungkan pecahan dengan penyebut 10 atau 100 ke bentuk persen.. Bukti: Nazilla bisa menjawab dengan benar 6 pertanyaan dari 10 soal yang diberikan. Tentukan berapa persen soal yang dijawab benar tersebut
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara mengubah pecahan menjadi persen dengan melakukan konversi penyebut ke 100.. Bukti: 6 pertanyaan dari 10 soal; berapa persen
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena siswa hanya perlu melakukan konversi pecahan sederhana (6/10) menjadi persen. Prosedur ini sangat familiar bagi siswa kelas 4 dan tidak memerlukan perencanaan strategi yang kompleks.. Bukti: 6 pertanyaan dari 10 soal; berapa persen

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman pecahan senilai dan konsep persen sebagai per seratus. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengubah pecahan 6/10 menjadi 60/100 atau 60% adalah prosedur standar yang diajarkan di kelas 4. Tidak ada kendala yang berinteraksi atau kebutuhan perencanaan yang rumit. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 84/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.038414; applying=0.961586; reasoning=0.000000 | applying | 0.961586 | 0.148250 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.152655; conceptual=0.820068; procedural=0.027277; metacognitive=0.000000 | conceptual | 0.820068 | 0.395188 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.849288; Medium=0.148230; Hard=0.002481 | Easy | 0.849288 | 0.397404 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.961586; −Σp ln(p) = 0.162870; H = 0.162870/ln(3) = 0.148250; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.820068; −Σp ln(p) = 0.547846; H = 0.547846/ln(4) = 0.395188; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.849288; −Σp ln(p) = 0.436593; H = 0.436593/ln(3) = 0.397404; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 4
Topik: Matematika SD Kelas 4
Subtopik: Menghubungkan Pecahan Desimal Perseratusan dengan Konsep Persen
Tipe soal: multiple_choice
Stimulus: -
Soal: Nazilla bisa menjawab dengan benar 6 pertanyaan dari 10 soal yang diberikan. Tentukan berapa persen soal yang dijawab benar tersebut !
Pilihan: A. 0,6%
B. 40%
C. 60%
D. 6%
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `87c4b5ff5d1524fbd581c451`

Suatu sekolah memilih 30 siswa dari 100 orang siswa yang akan diikutkan lomba berlari. Tentukan berapa persen siswa yang terpilih lomba lari tersebut!

| Opsi | Isi |
|---|---|
| A | 30% |
| B | 0,3% |
| C | 70% |
| D | 3% |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Persentase adalah per seratus. 30 dari 100 siswa sama dengan 30/100, yang setara dengan 30%.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `['mengidentifikasi', 'menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a5ffbeaeb6500765438d9c8705a66da437e94256f98b8b2a83507703c070c0d5`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2219 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2236 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2886 |

Run 1 — solusi: Persentase adalah per seratus. 30 dari 100 siswa sama dengan 30/100, yang setara dengan 30%.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan pemahaman dasar tentang konsep persen sebagai per seratus dalam konteks yang sangat rutin dan langsung.. Bukti: 30 siswa dari 100 orang siswa; Tentukan berapa persen siswa yang terpilih
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara pecahan per seratus dan notasi persen.. Bukti: 30 siswa dari 100 orang siswa; Tentukan berapa persen
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dengan angka yang sudah dalam bentuk per seratus, sehingga tidak memerlukan langkah tambahan atau perencanaan yang kompleks bagi siswa kelas 4.. Bukti: 30 siswa dari 100 orang siswa; Tentukan berapa persen

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar pecahan per seratus dan definisi persen. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konsep persen sebagai per seratus adalah materi standar kelas 4. Soal ini tidak memiliki kendala tambahan atau langkah yang saling bergantung. |

Run 2 — solusi: Persentase adalah per seratus. 30 dari 100 siswa sama dengan 30/100, yang setara dengan 30%.
- Domain kognitif `classify/applying`: Soal meminta siswa menerapkan definisi dasar persen (per seratus) pada konteks yang diberikan secara langsung. Ini adalah penerapan prosedur standar yang sudah dipelajari di kelas 4.. Bukti: 30 siswa dari 100 orang siswa; Tentukan berapa persen siswa yang terpilih
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami hubungan antara pecahan per seratus dan notasi persen sebagai konsep dasar.. Bukti: 30 siswa dari 100 orang siswa; Tentukan berapa persen
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu mengenali bahwa 30 dari 100 adalah 30%. Tidak ada langkah tambahan atau kendala yang perlu diintegrasikan.. Bukti: 30 siswa dari 100 orang siswa; Tentukan berapa persen

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar pecahan per seratus dan konsep persen. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 sudah mempelajari hubungan pecahan per seratus dengan persen. Soal ini adalah aplikasi langsung dari definisi tersebut tanpa kerumitan tambahan. |

Run 3 — solusi: 30 dari 100 siswa berarti 30/100. Dalam konsep persen, per 100 sama dengan persen, sehingga 30/100 = 30%.
- Domain kognitif `classify/applying`: Siswa menerapkan konsep dasar persen sebagai per seratus untuk mengubah pecahan 30/100 menjadi 30%.. Bukti: 30 siswa dari 100 orang siswa; Tentukan berapa persen
- Dimensi pengetahuan `classify/conceptual`: Memahami hubungan antara pecahan per seratus dengan notasi persen.. Bukti: 30 siswa dari 100 orang siswa; berapa persen
- Intended difficulty `classify/Easy`: Soal ini merupakan penerapan langsung definisi persen. Tidak ada langkah kompleks atau kendala yang berinteraksi.. Bukti: 30 siswa dari 100 orang siswa; Tentukan berapa persen

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar bahwa persen adalah per seratus. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 sudah mempelajari konsep dasar pecahan dan persen sebagai per seratus. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 86/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000216; applying=0.999784; reasoning=0.000000 | applying | 0.999784 | 0.001858 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.163425; conceptual=0.793066; procedural=0.043509; metacognitive=0.000000 | conceptual | 0.793066 | 0.444560 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.797713; Medium=0.199626; Hard=0.002661 | Easy | 0.797713 | 0.471252 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999784; −Σp ln(p) = 0.002041; H = 0.002041/ln(3) = 0.001858; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.793066; −Σp ln(p) = 0.616291; H = 0.616291/ln(4) = 0.444560; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.797713; −Σp ln(p) = 0.517723; H = 0.517723/ln(3) = 0.471252; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 4
Topik: Matematika SD Kelas 4
Subtopik: Menghubungkan Pecahan Desimal Perseratusan dengan Konsep Persen
Tipe soal: multiple_choice
Stimulus: -
Soal: Suatu sekolah memilih 30 siswa dari 100 orang siswa yang akan diikutkan lomba berlari. Tentukan berapa persen siswa yang terpilih lomba lari tersebut!
Pilihan: A. 30%
B. 0,3%
C. 70%
D. 3%
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `764036b9759f6277bc4dca51`

Perhatikan gambar yang diwarnai berikut. Mana gambar yang menunjukkan seperempat. Mana gambar yang tidak menunjukkan seperempat.

| Opsi | Isi |
|---|---|
| A | Gambar 3 (bentuk anak panah) |
| B | Gambar 1 (segitiga) |
| C | Gambar 2 (segi enam memanjang) |
| D | Gambar 4 (kotak berpetak) |

![Gambar sumber soal 6](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0159-10.png>)


![Gambar sumber soal 6](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0159-11.png>)


![Gambar sumber soal 6](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0159-12.png>)


![Gambar sumber soal 6](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0159-13.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `Gambar 2 (segi enam memanjang) adalah satu-satunya yang menunjukkan seperempat karena dibagi menjadi 4 bagian sama besar.`.
Solusi minimum hasil AI: Satu-satunya gambar yang menunjukkan seperempat adalah gambar yang dibagi menjadi 4 bagian dengan luas yang sama persis. Pada gambar 2, garis pembagi membagi bangun menjadi 4 bagian yang kongruen (sama besar). Gambar 1, 3, dan 4 memiliki bagian yang tidak sama besar.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0159-10.png, images/kelas2_panduan_siswa_kelas2.pdf-0159-11.png, images/kelas2_panduan_siswa_kelas2.pdf-0159-12.png, images/kelas2_panduan_siswa_kelas2.pdf-0159-13.png. Transkripsi visual: Terdapat empat gambar bangun datar yang masing-masing dibagi menjadi empat bagian dengan garis pembagi. Gambar 1 adalah segitiga yang dibagi tidak simetris. Gambar 2 adalah segi enam memanjang yang dibagi oleh garis vertikal dan horizontal tepat di tengah, menghasilkan empat bagian yang sama besar. Gambar 3 adalah bentuk anak panah yang dibagi tidak simetris. Gambar 4 adalah persegi panjang yang dibagi menjadi empat bagian dengan ukuran yang tidak sama besar (kolom kiri lebih lebar).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `dde6261603044287d4ed511bc24cc56288f04da95a1e4cd75aa7590d23c7ddf0`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 6810 |
| 2 | success | valid / verified | applying | conceptual | Medium | 6867 |
| 3 | success | valid / verified | applying | conceptual | Easy | 6801 |

Run 1 — solusi: Gambar 2 menunjukkan seperempat karena pembagiannya simetris dan menghasilkan empat bagian yang sama besar. Gambar 1, 3, dan 4 tidak menunjukkan seperempat karena pembagiannya tidak menghasilkan empat bagian yang sama besar.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan pemahaman konsep pecahan (seperempat) pada berbagai representasi visual untuk menentukan mana yang memenuhi syarat 'bagian sama besar'. Ini adalah penerapan konsep pada konteks rutin.. Bukti: Mana gambar yang menunjukkan seperempat. Mana gambar yang tidak menunjukkan seperempat.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang apa yang dimaksud dengan pecahan seperempat (bagian yang sama besar dari keseluruhan), bukan sekadar menghafal fakta atau prosedur algoritma.. Bukti: Perhatikan gambar yang diwarnai berikut.
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu melakukan observasi visual langsung untuk membandingkan luas bagian yang diwarnai dengan bagian lainnya. Tidak ada perhitungan kompleks atau manipulasi abstrak yang diperlukan.. Bukti: Mana gambar yang menunjukkan seperempat. Mana gambar yang tidak menunjukkan seperempat.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pecahan sebagai bagian dari keseluruhan yang sama besar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 diharapkan mampu mengenali pecahan sederhana melalui representasi visual. Tugas ini adalah tugas rutin dalam pengenalan pecahan. |

Run 2 — solusi: Satu-satunya gambar yang menunjukkan seperempat adalah gambar yang dibagi menjadi 4 bagian dengan luas yang sama persis. Pada gambar 2, garis pembagi membagi bangun menjadi 4 bagian yang kongruen (sama besar). Gambar lainnya memiliki bagian yang tidak sama besar.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi representasi visual dari pecahan seperempat. Ini memerlukan pemahaman konsep dasar pecahan sebagai bagian dari keseluruhan yang sama besar, bukan sekadar menghitung jumlah bagian.. Bukti: Mana gambar yang menunjukkan seperempat. Mana gambar yang tidak menunjukkan seperempat.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang apa arti 'seperempat' dalam konteks geometri (pembagian wilayah menjadi bagian yang sama besar), bukan sekadar menghafal simbol pecahan.. Bukti: Mana gambar yang menunjukkan seperempat.
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa tidak bisa hanya mengandalkan hitungan jumlah bagian (semua gambar dibagi menjadi 4 bagian). Siswa harus melakukan analisis visual untuk memverifikasi apakah bagian-bagian tersebut memiliki luas yang sama (kongruen). Ini memerlukan ketelitian dalam membedakan representasi yang benar dan yang menjebak.. Bukti: Mana gambar yang menunjukkan seperempat. Mana gambar yang tidak menunjukkan seperempat.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pecahan sebagai bagian dari keseluruhan dan konsep luas/kesamaan ukuran. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Untuk kelas 4, membedakan pecahan yang benar dari representasi visual yang tidak sama besar adalah tugas yang menuntut pemahaman konsep pecahan yang lebih dalam daripada sekadar membagi benda menjadi 4 bagian. |

Run 3 — solusi: Satu-satunya gambar yang menunjukkan seperempat adalah gambar yang dibagi menjadi empat bagian dengan luas yang sama besar. Pada gambar 2, garis pembagi membagi bangun menjadi empat bagian yang kongruen (sama besar), sehingga satu bagian yang diwarnai mewakili seperempat bagian utuh.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan konsep pecahan (seperempat) pada representasi visual bangun datar. Mereka harus mengenali apakah pembagian bangun tersebut menghasilkan bagian-bagian yang sama besar, yang merupakan prasyarat untuk menyatakan suatu bagian sebagai seperempat.. Bukti: Mana gambar yang menunjukkan seperempat. Mana gambar yang tidak menunjukkan seperempat.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang pecahan sebagai bagian dari keseluruhan yang sama besar, bukan sekadar menghafal prosedur.. Bukti: seperempat dari benda utuh
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu melakukan pengamatan visual langsung untuk membandingkan ukuran bagian-bagian bangun. Tidak ada perhitungan kompleks atau langkah-langkah yang saling bergantung yang harus direncanakan.. Bukti: Mana gambar yang menunjukkan seperempat. Mana gambar yang tidak menunjukkan seperempat.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pecahan sebagai bagian dari keseluruhan yang sama besar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 4, mengidentifikasi pecahan melalui representasi visual bangun datar adalah materi dasar yang rutin. Soal tidak menuntut penalaran tingkat tinggi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 2, "Medium": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `8331`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta untuk menerapkan pemahaman konsep pecahan (seperempat) pada berbagai representasi visual untuk menentukan mana yang memenuhi syarat 'bagian sama besar'. Ini adalah penerapan konsep pada konteks rutin.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang apa yang dimaksud dengan pecahan seperempat (bagian yang sama besar dari keseluruhan), bukan sekadar menghafal fakta atau prosedur algoritma.
- Intended difficulty `Easy`: Soal ini tergolong Easy karena siswa hanya perlu melakukan observasi visual langsung untuk membandingkan luas bagian yang diwarnai dengan bagian lainnya. Tidak ada perhitungan kompleks atau manipulasi abstrak yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pecahan sebagai bagian dari keseluruhan yang sama besar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 diharapkan mampu mengenali pecahan sederhana melalui representasi visual. Tugas ini adalah tugas rutin dalam pengenalan pecahan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 173/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000209; applying=0.999791; reasoning=0.000000 | applying | 0.999791 | 0.001805 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.002489; conceptual=0.993113; procedural=0.004399; metacognitive=0.000000 | conceptual | 0.993113 | 0.032933 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.682143; Medium=0.310145; Hard=0.007712 | Easy | 0.682143 | 0.602160 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999791; −Σp ln(p) = 0.001983; H = 0.001983/ln(3) = 0.001805; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.993113; −Σp ln(p) = 0.045655; H = 0.045655/ln(4) = 0.032933; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.682143; −Σp ln(p) = 0.661540; H = 0.661540/ln(3) = 0.602160; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 4
Topik: Matematika SD Kelas 4
Subtopik: Seperempat dari Benda Utuh
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan gambar yang diwarnai berikut. Mana gambar yang menunjukkan seperempat. Mana gambar yang tidak menunjukkan seperempat.
Pilihan: A. Gambar 3 (bentuk anak panah)
B. Gambar 1 (segitiga)
C. Gambar 2 (segi enam memanjang)
D. Gambar 4 (kotak berpetak)
Transkripsi visual: Terdapat empat gambar bangun datar yang masing-masing dibagi menjadi empat bagian dengan garis pembagi. Gambar 1 adalah segitiga yang dibagi tidak simetris. Gambar 2 adalah segi enam memanjang yang dibagi oleh garis vertikal dan horizontal tepat di tengah, menghasilkan empat bagian yang sama besar. Gambar 3 adalah bentuk anak panah yang dibagi tidak simetris. Gambar 4 adalah persegi panjang yang dibagi menjadi empat bagian dengan ukuran yang tidak sama besar (kolom kiri lebih lebar).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `bcd1ec2726d4dc3e37ec631d`

13, 22, 31, ..., 49, ...<br><br>Tentukan bilangan yang tepat sesuai pola bilangan yang diberikan !

| Opsi | Isi |
|---|---|
| A | 39 dan 59 |
| B | 45 dan 54 |
| C | 31 dan 49 |
| D | 40 dan 58 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Pola bilangan adalah penambahan 9 setiap langkahnya. 13+9=22, 22+9=31, 31+9=40, 40+9=49, 49+9=58. Bilangan yang hilang adalah 40 dan 58.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `300b27ab156f1753795594e0cec9b0e9bc2b4d9b20d7a669f13639869340562e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2325 |
| 2 | success | valid / verified | applying | procedural | Easy | 2305 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2339 |

Run 1 — solusi: Pola bilangan adalah penambahan 9 setiap langkahnya. 13+9=22, 22+9=31, 31+9=40, 40+9=49, 49+9=58. Bilangan yang hilang adalah 40 dan 58.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi aturan penambahan tetap (+9) dari urutan yang diberikan dan menerapkannya untuk menemukan suku yang hilang. Ini adalah penerapan prosedur pada konteks rutin.. Bukti: 13, 22, 31, ..., 49, ...; Tentukan bilangan yang tepat sesuai pola bilangan yang diberikan
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan pemahaman tentang pola aritmetika sederhana (konsep) dan menerapkan operasi penjumlahan berulang (prosedur) untuk menyelesaikan masalah.. Bukti: pola bilangan yang diberikan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 4. Pola penambahan 9 cukup jelas dari dua pasangan bilangan pertama (13 ke 22 dan 22 ke 31). Tidak ada kendala kompleks atau kebutuhan untuk strategi non-rutin.. Bukti: 13, 22, 31, ..., 49, ...

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar dan pemahaman pola bilangan sederhana. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menentukan pola bilangan dengan selisih tetap adalah materi standar kelas 4. Soal memberikan cukup banyak angka awal untuk memudahkan identifikasi pola tanpa beban kognitif tinggi. |

Run 2 — solusi: Pola bilangan adalah penambahan 9 setiap langkahnya (13+9=22, 22+9=31, 31+9=40, 40+9=49, 49+9=58). Bilangan yang hilang adalah 40 dan 58.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi aturan penambahan konstan (+9) dari urutan yang diberikan dan menerapkannya untuk mengisi bagian yang kosong. Ini adalah penerapan prosedur rutin dalam konteks pola bilangan.. Bukti: 13, 22, 31, ..., 49, ...; Tentukan bilangan yang tepat sesuai pola bilangan yang diberikan
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa tentang konsep pola bilangan aritmetika sederhana dan kemampuan prosedural untuk menentukan suku berikutnya.. Bukti: pola bilangan
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena pola penambahannya konstan dan jelas (+9). Siswa kelas 4 sudah familiar dengan pola bilangan sederhana. Tidak ada kendala yang berinteraksi atau kebutuhan strategi nonrutin.. Bukti: 13, 22, 31, ..., 49, ...

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar dan pemahaman konsep urutan bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pola bilangan dengan selisih tetap adalah materi standar kelas 4. Soal ini tidak menuntut perencanaan kompleks atau integrasi konsep yang sulit. |

Run 3 — solusi: Pola bilangan adalah penambahan 9 setiap langkahnya. 13+9=22, 22+9=31, 31+9=40, 40+9=49, 49+9=58. Jadi, bilangan yang tepat adalah 40 dan 58.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi aturan pola bilangan (penambahan konstan) dan menerapkannya untuk melengkapi urutan yang hilang. Ini adalah penerapan prosedur rutin dalam konteks pola bilangan yang familiar bagi kelas 4.. Bukti: 13, 22, 31, ..., 49, ...; Tentukan bilangan yang tepat sesuai pola bilangan yang diberikan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep pola bilangan aritmetika sederhana, di mana siswa harus memahami hubungan antar bilangan dalam urutan.. Bukti: pola bilangan yang diberikan
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena pola penambahan (+9) bersifat konstan dan langsung terlihat dari dua pasangan bilangan pertama. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: 13, 22, 31, ..., 49, ...; Tentukan bilangan yang tepat

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar dan pemahaman konsep urutan bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pola bilangan dengan selisih tetap adalah materi standar kelas 4. Penentuan selisih 9 adalah prosedur rutin yang sesuai dengan tingkat perkembangan kognitif siswa kelas 4. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3830`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi aturan penambahan konstan (+9) dari urutan yang diberikan dan menerapkannya untuk menemukan suku yang hilang. Ini adalah penerapan prosedur rutin dalam konteks pola bilangan.
- Dimensi pengetahuan `procedural`: Siswa menggunakan pemahaman tentang pola aritmetika sederhana (konsep) dan menerapkan operasi penjumlahan berulang (prosedur) untuk menyelesaikan masalah.
- Intended difficulty `Easy`: Soal ini bersifat rutin bagi siswa kelas 4. Pola penambahan 9 cukup jelas dari dua pasangan bilangan pertama. Tidak ada kendala kompleks atau kebutuhan untuk strategi non-rutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar dan pemahaman pola bilangan sederhana. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menentukan pola bilangan dengan selisih tetap adalah materi standar kelas 4. Soal memberikan cukup banyak angka awal untuk memudahkan identifikasi pola tanpa beban kognitif tinggi. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 79/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.905512; applying=0.094488; reasoning=0.000000 | knowing | 0.905512 | 0.284723 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.656193; conceptual=0.306124; procedural=0.037683; metacognitive=0.000000 | factual | 0.656193 | 0.549939 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.905466; Medium=0.092075; Hard=0.002459 | Easy | 0.905466 | 0.295193 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.905512; −Σp ln(p) = 0.312800; H = 0.312800/ln(3) = 0.284723; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.656193; −Σp ln(p) = 0.762378; H = 0.762378/ln(4) = 0.549939; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.905466; −Σp ln(p) = 0.324303; H = 0.324303/ln(3) = 0.295193; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 4
Topik: Matematika SD Kelas 4
Subtopik: Pola Bilangan
Tipe soal: multiple_choice
Stimulus: -
Soal: 13, 22, 31, ..., 49, ...

Tentukan bilangan yang tepat sesuai pola bilangan yang diberikan !
Pilihan: A. 39 dan 59
B. 45 dan 54
C. 31 dan 49
D. 40 dan 58
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `8639aa720008550cb79af345`

34, 27, 20, 13, ...<br><br>Tentukan bilangan yang tepat sesuai pola bilangan yang diberikan!

| Opsi | Isi |
|---|---|
| A | 5 |
| B | 6 |
| C | 7 |
| D | 13 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Pola bilangan adalah pengurangan 7 secara berulang: 34 - 7 = 27; 27 - 7 = 20; 20 - 7 = 13; 13 - 7 = 6.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `14f90c2ea0e1575b87bc99673b1078ed90877dcedc9e64b67690015f083292fe`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2215 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2225 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2253 |

Run 1 — solusi: Pola bilangan adalah pengurangan 7 secara berulang: 34 - 7 = 27; 27 - 7 = 20; 20 - 7 = 13; 13 - 7 = 6.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi aturan pengurangan (pola) dan menerapkannya untuk menentukan suku berikutnya. Ini adalah penerapan prosedur yang rutin dan langsung.. Bukti: 34, 27, 20, 13, ...; Tentukan bilangan yang tepat sesuai pola bilangan yang diberikan!
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang aturan atau prinsip pola bilangan (pengurangan tetap), yang merupakan pengetahuan konseptual.. Bukti: 34, 27, 20, 13, ...
- Intended difficulty `classify/Easy`: Soal ini termasuk mudah karena pola pengurangan 7 sangat konsisten dan langsung terlihat. Siswa hanya perlu melakukan satu operasi pengurangan sederhana untuk menemukan jawaban.. Bukti: 34, 27, 20, 13, ...

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan melakukan operasi pengurangan bilangan cacah dua digit. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pola bilangan sederhana adalah materi standar kelas 4. Tidak ada kendala kompleks atau langkah bertingkat yang menuntut perencanaan tinggi. |

Run 2 — solusi: Pola bilangan adalah pengurangan 7 secara berulang: 34 - 7 = 27; 27 - 7 = 20; 20 - 7 = 13. Maka, bilangan berikutnya adalah 13 - 7 = 6.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi aturan pengurangan yang konstan dalam urutan bilangan dan menerapkannya untuk menemukan suku berikutnya. Ini adalah penerapan prosedur yang rutin.. Bukti: 34, 27, 20, 13, ...; Tentukan bilangan yang tepat sesuai pola bilangan yang diberikan!
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep pola bilangan (pengurangan tetap) dan penggunaan algoritma pengurangan dasar.. Bukti: pola bilangan
- Intended difficulty `classify/Easy`: Soal ini termasuk mudah karena pola pengurangan 7 sangat jelas dan langsung terlihat dari dua pasangan bilangan pertama. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi non-rutin.. Bukti: 34, 27, 20, 13, ...

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan melakukan pengurangan bilangan dua digit. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pola bilangan sederhana adalah materi standar kelas 4. Siswa hanya perlu mengidentifikasi selisih antar bilangan dan menerapkan operasi pengurangan satu kali. |

Run 3 — solusi: Pola bilangan adalah pengurangan 7 secara berulang: 34 - 7 = 27; 27 - 7 = 20; 20 - 7 = 13. Maka, bilangan berikutnya adalah 13 - 7 = 6.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi aturan pengurangan yang konstan (pola aritmetika sederhana) dan menerapkannya untuk menemukan suku berikutnya. Ini adalah penerapan prosedur yang rutin.. Bukti: 34, 27, 20, 13, ...; Tentukan bilangan yang tepat sesuai pola bilangan yang diberikan!
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang konsep pola bilangan (pengurangan tetap) dan penggunaan algoritma pengurangan dasar.. Bukti: pola bilangan
- Intended difficulty `classify/Easy`: Soal ini termasuk kategori Easy karena pola pengurangan 7 sangat jelas dan konsisten. Siswa hanya perlu melakukan satu langkah operasi pengurangan dasar (13 - 7) untuk mendapatkan jawaban. Tidak ada kendala yang berinteraksi atau kebutuhan strategi nonrutin.. Bukti: 34, 27, 20, 13, ...

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan melakukan pengurangan bilangan dua digit dengan satu digit. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pola bilangan sederhana adalah materi standar kelas 4. Soal ini tidak menuntut perencanaan kompleks atau integrasi konsep, sehingga tingkat kesulitannya rendah bagi siswa kelas 4. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 67/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999974; applying=0.000026; reasoning=0.000000 | knowing | 0.999974 | 0.000269 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.725975; conceptual=0.235183; procedural=0.038842; metacognitive=0.000000 | factual | 0.725975 | 0.504263 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.918050; Medium=0.079770; Hard=0.002180 | Easy | 0.918050 | 0.267214 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999974; −Σp ln(p) = 0.000296; H = 0.000296/ln(3) = 0.000269; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.725975; −Σp ln(p) = 0.699057; H = 0.699057/ln(4) = 0.504263; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.918050; −Σp ln(p) = 0.293565; H = 0.293565/ln(3) = 0.267214; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 4
Topik: Matematika SD Kelas 4
Subtopik: Pola Bilangan
Tipe soal: multiple_choice
Stimulus: -
Soal: 34, 27, 20, 13, ...

Tentukan bilangan yang tepat sesuai pola bilangan yang diberikan!
Pilihan: A. 5
B. 6
C. 7
D. 13
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "conceptual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 9. Soal `c5e424e9914591b1d5286ef0`

Amati setiap pola berikut. Mana lanjutan pola pada gambar berikutnya.<br><br>Amati setiap pola berikut (baris b).

| Opsi | Isi |
|---|---|
| A | bunga |
| B | kelinci |
| C | heksagon |
| D | kupu-kupu |

![Gambar sumber soal 9](<../../../images/kelas2_panduan_siswa_kelas2.pdf-0131-01.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Pola baris b adalah pengulangan unit (kupu-kupu, kelinci, kelinci). Setelah gambar kupu-kupu, gambar berikutnya dalam unit pola adalah kelinci.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0131-01.png. Transkripsi visual: Baris b menampilkan pola berulang: kupu-kupu, kelinci, kelinci, kupu-kupu, kelinci, kelinci, kupu-kupu, [kosong]. Pola ini terdiri dari unit berulang (kupu-kupu, kelinci, kelinci).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5be50e673f4f802a3763540eaa39e77b8dda2b3e8007e26893fca5f6449abbc3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3464 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3446 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3500 |

Run 1 — solusi: Pola baris b adalah pengulangan unit (kupu-kupu, kelinci, kelinci). Setelah gambar kupu-kupu, gambar berikutnya dalam unit pola adalah kelinci.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi aturan pengulangan dalam urutan gambar dan menerapkan aturan tersebut untuk menentukan elemen berikutnya. Ini adalah penerapan konsep pola dasar.. Bukti: Amati setiap pola berikut (baris b).; pola berulang tiga gambar (kupu-kupu, kelinci, kelinci)
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep pola berulang (repeating patterns), yang merupakan pengetahuan konseptual dasar dalam matematika.. Bukti: Amati setiap pola berikut (baris b).
- Intended difficulty `classify/Easy`: Soal ini sangat mudah bagi siswa kelas 4. Pola yang diberikan bersifat repetitif dan sederhana, dengan unit pengulangan yang jelas dan langsung terlihat tanpa memerlukan perencanaan langkah yang kompleks.. Bukti: Amati setiap pola berikut (baris b).; pola berulang tiga gambar (kupu-kupu, kelinci, kelinci)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengenali urutan dan pengulangan visual sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pola visual sederhana adalah materi dasar yang sudah dikuasai siswa kelas 4. Tidak ada tuntutan kognitif tinggi. |

Run 2 — solusi: Pola pada baris b adalah pengulangan tiga gambar: kupu-kupu, kelinci, kelinci. Setelah gambar kupu-kupu terakhir, elemen berikutnya dalam urutan adalah kelinci.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi aturan pengulangan dalam urutan visual dan menerapkan aturan tersebut untuk menentukan elemen berikutnya. Ini adalah penerapan prosedur pengenalan pola yang rutin.. Bukti: Amati setiap pola berikut (baris b).; pola berulang tiga gambar (kupu-kupu, kelinci, kelinci)
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep pola berulang (repeating patterns), yang merupakan prinsip dasar dalam struktur matematika.. Bukti: Amati setiap pola berikut (baris b).
- Intended difficulty `classify/Easy`: Soal ini sangat mudah bagi siswa kelas 4. Pola berulang (kupu-kupu, kelinci, kelinci) terlihat jelas dan berulang secara konsisten tanpa variasi yang kompleks. Siswa hanya perlu mengenali unit pengulangan dan melanjutkan urutan tersebut.. Bukti: pola berulang tiga gambar (kupu-kupu, kelinci, kelinci)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengenali urutan visual sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pola visual berulang adalah materi dasar yang sudah dikuasai siswa kelas 4. Tidak ada tuntutan perencanaan atau integrasi yang kompleks. |

Run 3 — solusi: Pola pada baris b adalah pengulangan tiga gambar: (kupu-kupu, kelinci, kelinci). Urutan yang diberikan adalah (kupu-kupu, kelinci, kelinci, kupu-kupu, kelinci, kelinci, kupu-kupu). Maka, gambar berikutnya setelah kupu-kupu adalah kelinci.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi aturan pengulangan dalam urutan gambar dan menerapkan aturan tersebut untuk menentukan elemen berikutnya. Ini adalah penerapan prosedur pengenalan pola yang rutin.. Bukti: Amati setiap pola berikut (baris b).; pola berulang tiga gambar (kupu-kupu, kelinci, kelinci)
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep pola berulang (repeating patterns), yang merupakan bagian dari pengetahuan konseptual tentang struktur urutan.. Bukti: Amati setiap pola berikut (baris b).
- Intended difficulty `classify/Easy`: Soal ini termasuk mudah karena pola pengulangan terlihat jelas dan berulang secara konsisten. Siswa hanya perlu mengenali unit pengulangan (kupu-kupu, kelinci, kelinci) dan menentukan elemen berikutnya dalam urutan tersebut.. Bukti: Amati setiap pola berikut (baris b).; pola berulang tiga gambar (kupu-kupu, kelinci, kelinci)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengenali urutan visual dan pengulangan sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 4, mengidentifikasi pola berulang sederhana adalah tugas dasar yang sudah dipelajari sejak kelas awal. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 124/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000001 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.038041; conceptual=0.951381; procedural=0.010578; metacognitive=0.000000 | conceptual | 0.951381 | 0.158621 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.820555; Medium=0.175002; Hard=0.004443 | Easy | 0.820555 | 0.447265 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000001; H = 0.000001/ln(3) = 0.000001; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.951381; −Σp ln(p) = 0.219895; H = 0.219895/ln(4) = 0.158621; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.820555; −Σp ln(p) = 0.491370; H = 0.491370/ln(3) = 0.447265; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 4
Topik: Matematika SD Kelas 4
Subtopik: Pola
Tipe soal: multiple_choice
Stimulus: -
Soal: Amati setiap pola berikut. Mana lanjutan pola pada gambar berikutnya.

Amati setiap pola berikut (baris b).
Pilihan: A. bunga
B. kelinci
C. heksagon
D. kupu-kupu
Transkripsi visual: Baris b menampilkan pola berulang: kupu-kupu, kelinci, kelinci, kupu-kupu, kelinci, kelinci, kupu-kupu, [kosong]. Pola ini terdiri dari unit berulang (kupu-kupu, kelinci, kelinci).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `4088b8d020de84282c07a2b3`

Sebuah tangki air berisi 2.225 liter air. Pada siang hari 975 liter 325 ml air dipompa keluar dari tangki. Berapa banyak air yang tersisa di tangki?

| Opsi | Isi |
|---|---|
| A | 1.250 liter 675 ml |
| B | 1.249 liter 675 ml |
| C | 1.249 liter 325 ml |
| D | 1.250 liter 325 ml |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: 2.225 liter - 975 liter 325 ml = (2.224 liter + 1.000 ml) - 975 liter 325 ml = (2.224 - 975) liter + (1.000 - 325) ml = 1.249 liter 675 ml.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1f345326f3ccaac7218e60bbda9fafcf58a5e0cb6624f8a3436386636058c24b`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2497 |
| 2 | success | valid / verified | applying | procedural | Medium | 2506 |
| 3 | success | valid / verified | applying | procedural | Medium | 3344 |

Run 1 — solusi: 2.225 liter - 975 liter 325 ml = (2.224 liter + 1.000 ml) - 975 liter 325 ml = (2.224 - 975) liter + (1.000 - 325) ml = 1.249 liter 675 ml.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pengurangan bilangan campuran (liter dan mililiter) yang melibatkan teknik meminjam (regrouping) dari satuan liter ke mililiter. Ini adalah penerapan prosedur rutin dalam konteks pengukuran.. Bukti: 2.225 liter; 975 liter 325 ml; Berapa banyak air yang tersisa
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan antar satuan volume (1 liter = 1.000 ml) dan metode pengurangan yang melibatkan konversi satuan tersebut.. Bukti: 2.225 liter; 975 liter 325 ml
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua langkah utama: (1) melakukan pengurangan liter, dan (2) melakukan pengurangan mililiter dengan teknik meminjam (regrouping) dari 1 liter menjadi 1.000 ml. Meskipun prosedurnya familiar, siswa harus mengelola kendala konversi satuan secara mandiri.. Bukti: 2.225 liter; 975 liter 325 ml; Berapa banyak air yang tersisa

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konversi satuan volume (liter ke mililiter) dan pengurangan bilangan cacah dengan teknik meminjam. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Untuk kelas 4, melakukan pengurangan dengan konversi satuan (meminjam 1 liter menjadi 1.000 ml) adalah tantangan yang sesuai untuk tingkat menengah, karena siswa sering melakukan kesalahan pada proses regrouping. |

Run 2 — solusi: 2.225 liter - 975 liter 325 ml = 2.224 liter 1.000 ml - 975 liter 325 ml = (2.224 - 975) liter + (1.000 - 325) ml = 1.249 liter 675 ml.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pengurangan bilangan campuran (liter dan mililiter) yang memerlukan teknik meminjam (regrouping) dari satuan liter ke mililiter. Ini adalah penerapan prosedur pada konteks rutin.. Bukti: 2.225 liter - 975 liter 325 ml; Berapa banyak air yang tersisa di tangki?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritme pengurangan yang melibatkan konversi satuan (1 liter = 1.000 ml) dalam konteks pengukuran.. Bukti: 2.225 liter; 975 liter 325 ml
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa kelas 4 harus melakukan teknik meminjam (regrouping) dari satuan liter ke mililiter (1 liter menjadi 1.000 ml) sebelum melakukan pengurangan. Meskipun prosedurnya rutin, langkah ini memerlukan ketelitian dalam mengelola satuan yang berbeda dan hubungan antar-satuan tersebut.. Bukti: 2.225 liter - 975 liter 325 ml

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konversi satuan volume (liter ke mililiter) dan pengurangan bersusun dengan teknik meminjam. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 4 sudah mempelajari pengurangan bilangan cacah dan konversi satuan dasar. Tantangan utama terletak pada pengelolaan 'meminjam' 1 liter menjadi 1.000 ml, yang merupakan langkah prosedural penting namun standar untuk tingkat ini. |

Run 3 — solusi: 2.225 liter - 975 liter 325 ml = (2.224 liter 1.000 ml) - (975 liter 325 ml) = 1.249 liter 675 ml.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pengurangan dengan satuan campuran (liter dan mililiter) yang memerlukan pemahaman konversi satuan (meminjam 1 liter menjadi 1000 ml) untuk menyelesaikan masalah.. Bukti: 2.225 liter; 975 liter 325 ml; Berapa banyak air yang tersisa
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma pengurangan dengan teknik meminjam (regrouping) antar satuan volume yang berbeda.. Bukti: 2.225 liter; 975 liter 325 ml
- Intended difficulty `classify/Medium`: Soal menuntut pemahaman konversi satuan (1 liter = 1000 ml) dalam konteks pengurangan. Meskipun prosedurnya rutin, kebutuhan untuk melakukan 'borrowing' lintas satuan membuat tingkat kesulitannya Medium bagi siswa kelas 4.. Bukti: 2.225 liter; 975 liter 325 ml; Berapa banyak air yang tersisa

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengurangan bilangan cacah dan hubungan satuan volume (1 liter = 1000 ml). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 sudah mempelajari satuan volume, namun pengurangan dengan meminjam antar satuan (liter ke ml) memerlukan ketelitian lebih tinggi dibandingkan pengurangan bilangan cacah biasa. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 103/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.013499; applying=0.986501; reasoning=0.000000 | applying | 0.986501 | 0.065101 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.811047; conceptual=0.169530; procedural=0.019422; metacognitive=0.000000 | factual | 0.811047 | 0.394776 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.885681; Medium=0.111057; Hard=0.003262 | Easy | 0.885681 | 0.337031 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.986501; −Σp ln(p) = 0.071521; H = 0.071521/ln(3) = 0.065101; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.811047; −Σp ln(p) = 0.547276; H = 0.547276/ln(4) = 0.394776; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.885681; −Σp ln(p) = 0.370266; H = 0.370266/ln(3) = 0.337031; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 4
Topik: Matematika SD Kelas 4
Subtopik: Pengukuran Volume
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah tangki air berisi 2.225 liter air. Pada siang hari 975 liter 325 ml air dipompa keluar dari tangki. Berapa banyak air yang tersisa di tangki?
Pilihan: A. 1.250 liter 675 ml
B. 1.249 liter 675 ml
C. 1.249 liter 325 ml
D. 1.250 liter 325 ml
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `8a6222ad2919585a4e0febed`

Konversikan volume berikut ke dalam liter dan mililiter<br><br>b. 9.485 ml

| Opsi | Isi |
|---|---|
| A | 9 liter 485 ml |
| B | 94 liter 85 ml |
| C | 948 liter 5 ml |
| D | 9.485 liter |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: 1 liter = 1.000 ml. Maka 9.485 ml = 9.000 ml + 485 ml = 9 liter + 485 ml.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `637d9aa4ffd7a914baf87306fd234f722237c556326b648eb1fc7c831f985664`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2270 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2253 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2268 |

Run 1 — solusi: 1 liter = 1.000 ml. Maka 9.485 ml = 9.000 ml + 485 ml = 9 liter + 485 ml.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur konversi satuan volume yang sudah dipelajari (1 liter = 1.000 ml) ke dalam konteks rutin.. Bukti: Konversikan volume berikut ke dalam liter dan mililiter; 9.485 ml
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritme atau metode konversi satuan volume (prosedural) berdasarkan prinsip nilai tempat dan hubungan antar satuan (konseptual).. Bukti: Konversikan volume berikut ke dalam liter dan mililiter
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 4. Prosedur konversi 1.000 ml = 1 liter adalah materi dasar. Tidak ada kendala yang berinteraksi atau kebutuhan strategi non-rutin.. Bukti: Konversikan volume berikut ke dalam liter dan mililiter; 9.485 ml

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat ribuan dan hubungan 1 liter = 1.000 ml. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konversi satuan volume dasar adalah standar kurikulum kelas 4. Soal ini langsung menguji pemahaman tersebut tanpa jebakan atau kompleksitas tambahan. |

Run 2 — solusi: 1 liter = 1.000 ml. Maka 9.485 ml = 9.000 ml + 485 ml = 9 liter + 485 ml.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur konversi satuan volume yang sudah dipelajari (1 liter = 1.000 ml) pada konteks rutin.. Bukti: Konversikan volume berikut ke dalam liter dan mililiter; 9.485 ml
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara satuan liter dan mililiter serta prosedur konversi nilai tempat.. Bukti: Konversikan volume berikut ke dalam liter dan mililiter
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 4. Prosedur konversi 1.000 ml = 1 liter adalah materi dasar. Tidak ada kendala yang berinteraksi atau kebutuhan strategi nonrutin.. Bukti: Konversikan volume berikut ke dalam liter dan mililiter; 9.485 ml

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat ribuan dan konversi satuan volume dasar (1 liter = 1.000 ml). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konversi satuan volume merupakan standar kurikulum kelas 4. Soal ini adalah penerapan langsung tanpa langkah tambahan yang kompleks. |

Run 3 — solusi: 1 liter = 1.000 ml. Maka, 9.485 ml = 9.000 ml + 485 ml = 9 liter + 485 ml.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur konversi satuan volume yang sudah dipelajari (1 liter = 1.000 ml) ke dalam konteks rutin pemisahan nilai tempat ribuan dan satuan.. Bukti: Konversikan volume berikut ke dalam liter dan mililiter; 9.485 ml
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara satuan liter dan mililiter serta prosedur konversi berbasis nilai tempat.. Bukti: Konversikan volume berikut ke dalam liter dan mililiter
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 4. Prosedur konversi 1 liter = 1.000 ml adalah materi dasar. Tidak ada kendala yang berinteraksi atau kebutuhan strategi nonrutin.. Bukti: Konversikan volume berikut ke dalam liter dan mililiter; 9.485 ml

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat ribuan dan hubungan konversi 1 liter = 1.000 ml. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konversi satuan volume adalah materi standar kelas 4. Soal ini langsung menguji pemahaman konversi tanpa jebakan atau langkah tambahan yang kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3684`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan prosedur konversi satuan volume yang sudah dipelajari (1 liter = 1.000 ml) ke dalam konteks rutin pemisahan nilai tempat ribuan.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara satuan liter dan mililiter serta prosedur konversi berbasis nilai tempat.
- Intended difficulty `Easy`: Soal ini bersifat rutin bagi siswa kelas 4. Prosedur konversi 1 liter = 1.000 ml adalah materi dasar. Tidak ada kendala yang berinteraksi atau kebutuhan strategi nonrutin.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat ribuan dan hubungan konversi 1 liter = 1.000 ml. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konversi satuan volume adalah materi standar kelas 4. Soal ini langsung menguji pemahaman konversi tanpa jebakan atau langkah tambahan yang kompleks. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 78/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.988509; applying=0.011491; reasoning=0.000000 | knowing | 0.988509 | 0.057114 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.907782; conceptual=0.078273; procedural=0.013945; metacognitive=0.000000 | factual | 0.907782 | 0.250175 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.921866; Medium=0.075617; Hard=0.002517 | Easy | 0.921866 | 0.259700 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.988509; −Σp ln(p) = 0.062746; H = 0.062746/ln(3) = 0.057114; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.907782; −Σp ln(p) = 0.346817; H = 0.346817/ln(4) = 0.250175; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.921866; −Σp ln(p) = 0.285309; H = 0.285309/ln(3) = 0.259700; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 4
Topik: Matematika SD Kelas 4
Subtopik: Pengukuran Volume
Tipe soal: multiple_choice
Stimulus: -
Soal: Konversikan volume berikut ke dalam liter dan mililiter

b. 9.485 ml
Pilihan: A. 9 liter 485 ml
B. 94 liter 85 ml
C. 948 liter 5 ml
D. 9.485 liter
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "conceptual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 12. Soal `1a9d9923445f71c78d74086d`

Sebuah karung berisi 90 kg 460 gram beras dan karung lainnya berisi 25 kg 380 gram beras. Berapa berat beras dalam kedua karung tersebut?

| Opsi | Isi |
|---|---|
| A | 115 kg 840 gram |
| B | 65 kg 840 gram |
| C | 116 kg 840 gram |
| D | 115 kg 740 gram |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Jumlahkan kilogram: 90 kg + 25 kg = 115 kg. Jumlahkan gram: 460 g + 380 g = 840 g. Total: 115 kg 840 g.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `22c0ad79826f750764db0e528e4c412fd0dd4cb2931800fba65fd302a82b740e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2369 |
| 2 | success | valid / verified | applying | procedural | Easy | 2350 |
| 3 | success | valid / verified | applying | procedural | Easy | 2364 |

Run 1 — solusi: Jumlahkan kilogram: 90 kg + 25 kg = 115 kg. Jumlahkan gram: 460 g + 380 g = 840 g. Total: 115 kg 840 g.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur penjumlahan standar pada satuan berat yang berbeda (kg dan gram). Prosedur ini rutin dan langsung, tidak memerlukan strategi non-rutin atau penalaran kompleks.. Bukti: 90 kg 460 gram beras dan karung lainnya berisi 25 kg 380 gram beras; Berapa berat beras dalam kedua karung tersebut?
- Dimensi pengetahuan `classify/procedural`: Soal menguji pemahaman tentang algoritme penjumlahan untuk satuan berat campuran (kg dan gram), yang merupakan bagian dari prosedur matematika dasar.. Bukti: 90 kg 460 gram; 25 kg 380 gram
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu melakukan penjumlahan dua bilangan dengan satuan yang sama (kg dengan kg, gram dengan gram) tanpa perlu konversi satuan yang kompleks (karena jumlah gram 840 < 1000). Jalur penyelesaian sangat jelas dan familiar bagi siswa kelas 4.. Bukti: 90 kg 460 gram; 25 kg 380 gram; Berapa berat beras dalam kedua karung tersebut?

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
| gradeRelativeRationale | Penjumlahan satuan berat campuran adalah materi standar kelas 4. Tidak ada kendala interaksi (seperti konversi gram ke kg) yang membuat soal ini sulit. |

Run 2 — solusi: Jumlahkan kilogram dengan kilogram (90 + 25 = 115 kg) dan gram dengan gram (460 + 380 = 840 gram). Hasilnya adalah 115 kg 840 gram.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan prosedur penjumlahan standar pada satuan berat yang berbeda (kg dan gram). Ini adalah penerapan langsung dari konsep penjumlahan satuan baku yang sudah dipelajari di kelas 4.. Bukti: 90 kg 460 gram beras dan karung lainnya berisi 25 kg 380 gram beras; Berapa berat beras dalam kedua karung tersebut?
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut pemahaman tentang algoritma penjumlahan bilangan dengan satuan campuran, yang merupakan bagian dari pengetahuan prosedural.. Bukti: 90 kg 460 gram; 25 kg 380 gram
- Intended difficulty `classify/Easy`: Soal ini dikategorikan Easy karena prosedurnya langsung (penjumlahan) dan tidak memerlukan konversi satuan yang kompleks atau langkah-langkah yang saling bergantung. Siswa hanya perlu menjumlahkan komponen yang sejenis.. Bukti: 90 kg 460 gram; 25 kg 380 gram; Berapa berat beras dalam kedua karung tersebut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah dan pemahaman dasar satuan berat (kg dan gram). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 4, penjumlahan satuan berat campuran adalah materi rutin. Tidak ada kendala yang saling berinteraksi atau kebutuhan untuk merencanakan strategi non-rutin. |

Run 3 — solusi: Jumlahkan kilogram dengan kilogram (90 + 25 = 115 kg) dan gram dengan gram (460 + 380 = 840 gram). Hasilnya adalah 115 kg 840 gram.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan prosedur penjumlahan standar pada satuan berat yang sudah dipelajari di kelas 4. Tidak ada strategi nonrutin atau integrasi konsep yang kompleks.. Bukti: 90 kg 460 gram beras dan karung lainnya berisi 25 kg 380 gram beras; Berapa berat beras dalam kedua karung tersebut?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritme penjumlahan untuk satuan berat campuran (kg dan gram), yang merupakan prosedur standar.. Bukti: 90 kg 460 gram; 25 kg 380 gram
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 4. Prosedur penjumlahan terpisah antara kg dan gram sudah familiar. Tidak ada kendala yang berinteraksi atau kebutuhan untuk konversi satuan yang rumit karena jumlah gram (840) tidak melebihi 1000 gram.. Bukti: 90 kg 460 gram; 25 kg 380 gram; Berapa berat beras dalam kedua karung tersebut?

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
| gradeRelativeRationale | Penjumlahan satuan berat campuran adalah materi standar kelas 4. Karena tidak ada konversi satuan yang diperlukan (hasil gram < 1000), tingkat kesulitannya rendah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 93/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.006801; applying=0.993199; reasoning=0.000000 | applying | 0.993199 | 0.037062 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.242918; conceptual=0.741999; procedural=0.015083; metacognitive=0.000000 | conceptual | 0.741999 | 0.453306 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.909885; Medium=0.087503; Hard=0.002612 | Easy | 0.909885 | 0.286385 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.993199; −Σp ln(p) = 0.040717; H = 0.040717/ln(3) = 0.037062; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.741999; −Σp ln(p) = 0.628416; H = 0.628416/ln(4) = 0.453306; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.909885; −Σp ln(p) = 0.314626; H = 0.314626/ln(3) = 0.286385; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 4
Topik: Matematika SD Kelas 4
Subtopik: Hubungan Antarsatuan Baku Berat
Tipe soal: multiple_choice
Stimulus: -
Soal: Sebuah karung berisi 90 kg 460 gram beras dan karung lainnya berisi 25 kg 380 gram beras. Berapa berat beras dalam kedua karung tersebut?
Pilihan: A. 115 kg 840 gram
B. 65 kg 840 gram
C. 116 kg 840 gram
D. 115 kg 740 gram
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 13. Soal `8fe432cf4c0a120aab6def21`

\|**No**\|**Nama Bangun Datar**\|**Gambar**\|**Banyaknya**\|<br>\|---\|---\|---\|---\|<br>\|1<br>2\|Segitiga<br>...\|...\|...<br>...\|<br><br>Tentukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut :

| Opsi | Isi |
|---|---|
| A | Segitiga 4, jajargenjang 1, persegi 1 |
| B | Segitiga 5, trapesium 1, persegi 1 |
| C | Segitiga 6, persegi 1 |
| D | Segitiga 5, jajargenjang 1, persegi 1 |

![Gambar sumber soal 13](<../../../images/kelas4_panduan_siswa_kelas4.pdf-0184-10.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Mengidentifikasi kepingan pada gambar: terdapat 5 segitiga (biru, merah, hijau tua, oranye, merah muda), 1 persegi (hijau muda), dan 1 jajargenjang (kuning). Total: 5 segitiga, 1 persegi, 1 jajargenjang. Sesuai dengan pilihan D.
Gambar sumber: images/kelas4_panduan_siswa_kelas4.pdf-0184-10.png. Transkripsi visual: Gambar menunjukkan sebuah perahu yang disusun dari 7 keping tangram. Kepingan tersebut terdiri dari: 1 segitiga besar biru, 1 segitiga besar merah, 1 segitiga hijau tua, 1 persegi hijau muda, 1 segitiga oranye, 1 jajargenjang kuning, dan 1 segitiga merah muda. Total kepingan: 5 segitiga, 1 persegi, 1 jajargenjang.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e4d9d69d3e283fdc3dc749c8ebd18a71b0a32e63a2f19f1100db81e4968ee9f5`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3539 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3600 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 3517 |

Run 1 — solusi: Mengidentifikasi kepingan pada gambar: 5 segitiga (biru, merah, hijau tua, oranye, merah muda), 1 persegi (hijau muda), dan 1 jajargenjang (kuning). Total: 5 segitiga, 1 persegi, 1 jajargenjang.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi dan menghitung jumlah bangun datar penyusun (segitiga, persegi, jajargenjang) dari gambar yang diberikan. Ini adalah proses mengenali dan mengklasifikasikan bentuk geometris dasar.. Bukti: Tentukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep bentuk-bentuk geometri dasar (segitiga, persegi, jajargenjang) dan bagaimana mereka menyusun sebuah gambar yang lebih kompleks.. Bukti: Tentukan dekomposisi berbagai macam bangun datar
- Intended difficulty `classify/Easy`: Soal ini meminta siswa melakukan observasi visual langsung terhadap bentuk-bentuk yang sudah familiar. Tidak ada langkah perhitungan rumit atau perencanaan strategi yang kompleks, hanya pengenalan bentuk dan penghitungan sederhana.. Bukti: Tentukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk bangun datar dasar (segitiga, persegi, jajargenjang). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 4, mengidentifikasi bentuk-bentuk dasar dalam komposisi tangram adalah tugas rutin yang sesuai dengan tingkat perkembangan kognitif mereka. |

Run 2 — solusi: Mengidentifikasi kepingan pada gambar: terdapat 5 segitiga (biru, merah, hijau tua, oranye, merah muda), 1 persegi (hijau muda), dan 1 jajargenjang (kuning). Totalnya adalah 5 segitiga, 1 persegi, dan 1 jajargenjang. Sesuai dengan pilihan D.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi dan menghitung jumlah bangun datar penyusun (dekomposisi) dari sebuah gambar kompleks. Ini memerlukan pengenalan sifat-sifat bangun datar dan kemampuan membedakan bentuk secara visual, yang merupakan penerapan konsep dasar geometri.. Bukti: Tentukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang kategori bangun datar (segitiga, persegi, jajargenjang) dan bagaimana bentuk-bentuk tersebut menyusun objek yang lebih besar.. Bukti: Tentukan dekomposisi berbagai macam bangun datar
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan ketelitian visual untuk membedakan bentuk (terutama jajargenjang vs segitiga) dan menghitung jumlah masing-masing keping tanpa bantuan langkah eksplisit. Siswa harus melakukan klasifikasi mandiri terhadap 7 objek yang terintegrasi.. Bukti: Tentukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal sifat-sifat dasar bangun datar (segitiga, persegi, jajargenjang). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 4, mengurai gambar menjadi komponen-komponen bangun datar adalah tugas yang sesuai, namun menuntut ketelitian visual yang cukup tinggi agar tidak salah mengidentifikasi bentuk atau melewatkan kepingan. |

Run 3 — solusi: Mengidentifikasi kepingan pada gambar: 5 segitiga (biru, merah, hijau tua, oranye, merah muda), 1 persegi (hijau muda), dan 1 jajargenjang (kuning). Total: 5 segitiga, 1 persegi, 1 jajargenjang. Sesuai dengan pilihan D.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi dan menghitung jumlah bangun datar penyusun (dekomposisi) dari gambar yang diberikan. Ini adalah tugas mengenali dan mengklasifikasikan bentuk geometris dasar.. Bukti: Tentukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami konsep bentuk bangun datar (segitiga, persegi, jajargenjang) sebagai elemen dasar geometri.. Bukti: Nama Bangun Datar; Banyaknya
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung. Siswa hanya perlu melakukan observasi visual dan menghitung jumlah setiap jenis bangun datar yang terlihat jelas. Tidak ada manipulasi atau perencanaan langkah yang kompleks.. Bukti: Tentukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar bangun datar (segitiga, persegi, jajargenjang). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas mengidentifikasi dan menghitung objek visual sederhana adalah keterampilan dasar yang sesuai untuk kelas 4. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 2, "Medium": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `5118`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa diminta untuk mengidentifikasi dan menghitung jumlah bangun datar penyusun (dekomposisi) dari gambar yang diberikan. Ini adalah proses mengenali dan mengklasifikasikan bentuk geometris dasar, yang termasuk dalam domain knowing.
- Dimensi pengetahuan `conceptual`: Siswa perlu memahami konsep bentuk-bentuk geometri dasar (segitiga, persegi, jajargenjang) dan bagaimana mereka menyusun sebuah gambar yang lebih kompleks.
- Intended difficulty `Easy`: Soal ini meminta siswa melakukan observasi visual langsung terhadap bentuk-bentuk yang sudah familiar. Tidak ada langkah perhitungan rumit atau perencanaan strategi yang kompleks, hanya pengenalan bentuk dan penghitungan sederhana. Tugas ini rutin bagi kelas 4.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk bangun datar dasar (segitiga, persegi, jajargenjang). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 4, mengidentifikasi bentuk-bentuk dasar dalam komposisi tangram adalah tugas rutin yang sesuai dengan tingkat perkembangan kognitif mereka. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 240/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.049214; applying=0.950786; reasoning=0.000000 | applying | 0.950786 | 0.178585 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.010553; conceptual=0.981025; procedural=0.008421; metacognitive=0.000000 | conceptual | 0.981025 | 0.077223 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.694123; Medium=0.295774; Hard=0.010104 | Easy | 0.694123 | 0.600898 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.950786; −Σp ln(p) = 0.196196; H = 0.196196/ln(3) = 0.178585; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.981025; −Σp ln(p) = 0.107053; H = 0.107053/ln(4) = 0.077223; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.694123; −Σp ln(p) = 0.660153; H = 0.660153/ln(3) = 0.600898; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 4
Topik: Matematika SD Kelas 4
Subtopik: Komposisi dan Dekomposisi Bangun Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: |**No**|**Nama Bangun Datar**|**Gambar**|**Banyaknya**|
|---|---|---|---|
|1<br>2|Segitiga<br>...|...|...<br>...|

Tentukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut :
Pilihan: A. Segitiga 4, jajargenjang 1, persegi 1
B. Segitiga 5, trapesium 1, persegi 1
C. Segitiga 6, persegi 1
D. Segitiga 5, jajargenjang 1, persegi 1
Transkripsi visual: Gambar menunjukkan sebuah perahu yang disusun dari 7 keping tangram. Kepingan tersebut terdiri dari: 1 segitiga besar biru, 1 segitiga besar merah, 1 segitiga hijau tua, 1 persegi hijau muda, 1 segitiga oranye, 1 jajargenjang kuning, dan 1 segitiga merah muda. Total kepingan: 5 segitiga, 1 persegi, 1 jajargenjang.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `f068d3ebd6b847a2ae99e0d2`

Lakukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut :<br><br>Setelah kalian mengamati gambar di atas, apa saja bangun datar yang menyusun motif paving di atas?

| Opsi | Isi |
|---|---|
| A | Segitiga siku-siku, persegi, segienam, dan trapesium |
| B | Segitiga sama sisi, persegi, jajargenjang, dan trapesium |
| C | Segitiga siku-siku, persegi, jajargenjang, dan lingkaran |
| D | Segitiga siku-siku, persegi, jajargenjang, dan trapesium |

![Gambar sumber soal 14](<../../../images/kelas4_panduan_siswa_kelas4.pdf-0185-06.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Mengamati setiap kepingan poligon pada gambar: terdapat segitiga dengan sudut siku-siku, persegi dengan sisi sama panjang dan sudut siku-siku, jajargenjang dengan sisi sejajar, dan trapesium dengan sepasang sisi sejajar. Pilihan D mencakup semua jenis bangun tersebut secara akurat.
Gambar sumber: images/kelas4_panduan_siswa_kelas4.pdf-0185-06.png. Transkripsi visual: Gambar menunjukkan sebuah motif paving yang terdiri dari beberapa bangun datar poligon berwarna hijau yang disusun membentuk persegi panjang besar. Terdapat garis-garis putih yang memisahkan kepingan-kepingan tersebut. Kepingan-kepingan tersebut terdiri dari: segitiga siku-siku (di sudut kiri atas, kiri bawah, dan tengah), persegi (di bagian atas tengah dan kanan), jajargenjang (di bagian tengah kiri dan bawah tengah), serta trapesium (di bagian kanan atas dan kanan bawah).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1bdefedf02ea300ceba5af40a9040ee99fa423c482ea3f28b039a7ac958b26f9`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3601 |
| 2 | success | valid / verified | applying | conceptual | Easy | 3600 |
| 3 | success | valid / verified | applying | conceptual | Easy | 3584 |

Run 1 — solusi: Mengamati setiap kepingan poligon pada gambar: terdapat segitiga dengan sudut siku-siku, persegi dengan sisi sama panjang dan sudut siku-siku, jajargenjang dengan sisi sejajar, dan trapesium dengan sepasang sisi sejajar. Pilihan D mencakup semua jenis bangun tersebut secara akurat.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi dan mengklasifikasikan bangun datar penyusun dari sebuah komposisi geometris. Ini melibatkan pengenalan sifat-sifat bangun datar (sudut, sisi) untuk menentukan jenisnya, yang merupakan proses applying konsep geometri dasar.. Bukti: apa saja bangun datar yang menyusun motif paving di atas?; Lakukan dekomposisi berbagai macam bangun datar yang ada pada gambar
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang kategori dan sifat-sifat bangun datar (konsep), bukan sekadar menghafal nama atau melakukan prosedur perhitungan.. Bukti: apa saja bangun datar yang menyusun motif paving di atas?
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu mengidentifikasi bentuk visual yang sudah jelas terlihat. Tidak ada langkah perhitungan atau manipulasi yang kompleks. Siswa kelas 4 sudah familiar dengan bentuk-bentuk dasar ini.. Bukti: apa saja bangun datar yang menyusun motif paving di atas?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal sifat-sifat dasar bangun datar (segitiga, persegi, jajargenjang, trapesium). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengidentifikasi bentuk bangun datar adalah kompetensi dasar geometri kelas 4. Soal ini bersifat langsung (visual recognition) tanpa memerlukan analisis mendalam atau perhitungan. |

Run 2 — solusi: Mengamati gambar secara visual dan mengidentifikasi karakteristik sudut serta sisi setiap bagian: terdapat segitiga dengan sudut siku-siku, persegi dengan sisi sama panjang dan sudut siku-siku, jajargenjang dengan sisi sejajar, dan trapesium dengan sepasang sisi sejajar. Pilihan D mencakup semua jenis bangun yang terlihat.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi dan mengklasifikasikan bangun datar penyusun dari sebuah komposisi geometris. Ini melibatkan pengenalan sifat-sifat bangun datar (sudut, sisi) untuk menentukan jenisnya, yang merupakan aktivitas applying konsep pada konteks visual.. Bukti: apa saja bangun datar yang menyusun motif paving di atas?; Lakukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang definisi dan karakteristik bangun datar (persegi, segitiga siku-siku, dll.), yang merupakan pengetahuan konseptual tentang hubungan dan kategori bentuk.. Bukti: apa saja bangun datar yang menyusun motif paving di atas?
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu melakukan observasi visual langsung untuk mengidentifikasi bentuk-bentuk dasar yang sudah dikenal di kelas 4. Tidak ada perhitungan kompleks atau perencanaan strategi yang rumit; hanya pengenalan pola visual.. Bukti: apa saja bangun datar yang menyusun motif paving di atas?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal sifat-sifat dasar bangun datar (persegi, segitiga, jajargenjang, trapesium). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 4, mengidentifikasi bentuk dari gambar adalah tugas rutin yang sesuai dengan tingkat perkembangan kognitif mereka dalam geometri dasar. |

Run 3 — solusi: Mengamati setiap keping bangun datar pada gambar: terdapat segitiga dengan satu sudut siku-siku, persegi dengan empat sisi sama panjang dan sudut siku-siku, jajargenjang dengan sisi sejajar, dan trapesium dengan sepasang sisi sejajar. Pilihan D mencakup semua jenis bangun tersebut.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi dan mengklasifikasikan bangun datar penyusun dari sebuah komposisi geometris. Ini melibatkan pengenalan sifat-sifat bangun datar (seperti sudut siku-siku, kesejajaran sisi) dan mencocokkannya dengan kategori yang diberikan, yang merupakan proses applying konsep geometri dasar.. Bukti: apa saja bangun datar yang menyusun motif paving di atas?; Lakukan dekomposisi berbagai macam bangun datar
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang definisi dan karakteristik berbagai bangun datar (persegi, segitiga siku-siku, jajargenjang, trapesium), yang merupakan pengetahuan konseptual.. Bukti: apa saja bangun datar yang menyusun motif paving di atas?
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu melakukan observasi visual langsung untuk mengidentifikasi bentuk-bentuk dasar yang sudah dikenal di kelas 4. Tidak ada perhitungan kompleks atau manipulasi geometris yang diperlukan, hanya pengenalan visual.. Bukti: apa saja bangun datar yang menyusun motif paving di atas?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal sifat-sifat dasar bangun datar (persegi, segitiga, jajargenjang, trapesium). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 sudah mempelajari klasifikasi bangun datar sederhana. Mengidentifikasi bentuk dari gambar adalah tugas rutin yang sesuai dengan tingkat kognitif kelas 4. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 235/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000008; applying=0.999992; reasoning=0.000000 | applying | 0.999992 | 0.000091 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.010670; conceptual=0.978962; procedural=0.010368; metacognitive=0.000000 | conceptual | 0.978962 | 0.084132 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.766448; Medium=0.226925; Hard=0.006627 | Easy | 0.766448 | 0.522180 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999992; −Σp ln(p) = 0.000100; H = 0.000100/ln(3) = 0.000091; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.978962; −Σp ln(p) = 0.116632; H = 0.116632/ln(4) = 0.084132; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.766448; −Σp ln(p) = 0.573673; H = 0.573673/ln(3) = 0.522180; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 4
Topik: Matematika SD Kelas 4
Subtopik: Komposisi dan Dekomposisi Bangun Datar
Tipe soal: multiple_choice
Stimulus: -
Soal: Lakukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut :

Setelah kalian mengamati gambar di atas, apa saja bangun datar yang menyusun motif paving di atas?
Pilihan: A. Segitiga siku-siku, persegi, segienam, dan trapesium
B. Segitiga sama sisi, persegi, jajargenjang, dan trapesium
C. Segitiga siku-siku, persegi, jajargenjang, dan lingkaran
D. Segitiga siku-siku, persegi, jajargenjang, dan trapesium
Transkripsi visual: Gambar menunjukkan sebuah motif paving yang terdiri dari beberapa bangun datar poligon berwarna hijau yang disusun membentuk persegi panjang besar. Terdapat garis-garis putih yang memisahkan kepingan-kepingan tersebut. Kepingan-kepingan tersebut terdiri dari: segitiga siku-siku (di sudut kiri atas, kiri bawah, dan tengah), persegi (di bagian atas tengah dan kanan), jajargenjang (di bagian tengah kiri dan bawah tengah), serta trapesium (di bagian kanan atas dan kanan bawah).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 15. Soal `f311bf91df38724a90b35b69`

Perhatikan huruf-huruf berikut ini.<br><br>Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?

| Opsi | Isi |
|---|---|
| A | Huruf E |
| B | Huruf M |
| C | Huruf T |
| D | Tidak ada |

![Gambar sumber soal 15](<../../../images/kelas3_panduan_siswa_kelas3.pdf-0198-01.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Analisis geometri huruf: E memiliki 3 garis sejajar (lebih dari 1 pasang) dan 4 garis tegak lurus (2 pasang). M memiliki 1 pasang garis sejajar (vertikal) tetapi 0 garis tegak lurus. T memiliki 1 pasang garis tegak lurus tetapi 0 garis sejajar. Tidak ada huruf yang memenuhi syarat tepat 1 pasang garis sejajar dan 2 pasang garis tegak lurus.
Gambar sumber: images/kelas3_panduan_siswa_kelas3.pdf-0198-01.png. Transkripsi visual: Gambar menampilkan huruf-huruf 'MATEMATIKA' yang ditulis di atas kertas berpetak. Huruf 'E' memiliki tiga garis horizontal sejajar dan empat garis tegak lurus (dua pasang). Huruf 'M' memiliki dua garis miring yang tidak sejajar dan dua garis vertikal yang sejajar (satu pasang), tanpa garis tegak lurus. Huruf 'T' memiliki satu garis horizontal dan satu garis vertikal yang membentuk satu pasang garis tegak lurus, tanpa garis sejajar.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2516904bb4ae12477daccac7f6c1be89f6508f9e40d356946a4d234b5af9294e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 3681 |
| 2 | success | valid / verified | applying | conceptual | Medium | 3776 |
| 3 | success | valid / verified | applying | conceptual | Medium | 3709 |

Run 1 — solusi: Analisis geometri huruf: E memiliki 3 garis sejajar (lebih dari 1 pasang) dan 4 garis tegak lurus (2 pasang). M memiliki 1 pasang garis sejajar (vertikal) tetapi 0 garis tegak lurus. T memiliki 1 pasang garis tegak lurus tetapi 0 garis sejajar. Tidak ada huruf yang memenuhi syarat tepat 1 pasang garis sejajar dan 2 pasang garis tegak lurus.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi properti geometris (garis sejajar dan tegak lurus) pada bentuk huruf dan memverifikasi apakah properti tersebut sesuai dengan kriteria yang diberikan. Ini melibatkan penerapan konsep geometri pada objek visual.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami definisi dan hubungan antara garis sejajar dan tegak lurus (konsep) untuk menganalisis struktur geometris huruf.. Bukti: satu pasang garis sejajar dan dua pasang garis tegak lurus
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk melakukan analisis visual yang cermat terhadap setiap opsi. Siswa harus memeriksa keberadaan garis sejajar dan tegak lurus secara terpisah untuk setiap huruf, lalu mencocokkannya dengan kriteria yang cukup spesifik. Ini memerlukan ketelitian dalam mengidentifikasi hubungan geometris pada bentuk yang familiar.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?; A. Huruf E; B. Huruf M; C. Huruf T

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang garis sejajar dan tegak lurus. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 diharapkan mampu mengidentifikasi garis sejajar dan tegak lurus. Tugas ini menuntut ketelitian dalam memverifikasi dua kondisi sekaligus untuk setiap opsi, yang merupakan tingkat kesulitan menengah untuk jenjang ini. |

Run 2 — solusi: Analisis setiap huruf: Huruf E memiliki 3 pasang garis sejajar dan 4 pasang garis tegak lurus. Huruf M memiliki 1 pasang garis sejajar tetapi tidak ada garis tegak lurus. Huruf T memiliki 1 pasang garis tegak lurus tetapi tidak ada garis sejajar. Karena tidak ada huruf yang memenuhi kriteria (1 pasang sejajar DAN 2 pasang tegak lurus), maka jawabannya adalah D.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi sifat geometris (garis sejajar dan tegak lurus) pada bentuk huruf yang diberikan. Ini memerlukan penerapan konsep dasar garis pada konteks visual yang rutin.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?; Analisis setiap huruf: Huruf E memiliki 3 pasang garis sejajar dan 4 pasang garis tegak lurus. Huruf M memiliki 1 pasang garis sejajar tetapi tidak ada garis tegak lurus. Huruf T memiliki 1 pasang garis tegak lurus tetapi tidak ada garis sejajar.
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman siswa tentang definisi dan pengenalan visual garis sejajar dan tegak lurus.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk memeriksa setiap opsi secara sistematis terhadap dua kriteria geometris sekaligus. Meskipun prosedurnya rutin, siswa harus melakukan verifikasi ganda untuk setiap huruf, yang meningkatkan beban kognitif sedikit di atas sekadar pengenalan satu sifat.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?; Analisis setiap huruf: Huruf E memiliki 3 pasang garis sejajar dan 4 pasang garis tegak lurus. Huruf M memiliki 1 pasang garis sejajar tetapi tidak ada garis tegak lurus. Huruf T memiliki 1 pasang garis tegak lurus tetapi tidak ada garis sejajar.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang garis sejajar dan tegak lurus. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 diharapkan mampu mengidentifikasi garis sejajar dan tegak lurus. Tugas ini memerlukan ketelitian dalam memeriksa dua kondisi (sejajar dan tegak lurus) pada beberapa objek, yang merupakan tantangan sedang bagi tingkat kelas ini. |

Run 3 — solusi: Analisis geometri huruf: E memiliki 3 pasang garis sejajar dan 4 pasang garis tegak lurus. M memiliki 1 pasang garis sejajar (vertikal) dan 0 garis tegak lurus. T memiliki 0 pasang garis sejajar dan 1 pasang garis tegak lurus. Tidak ada huruf yang memenuhi syarat tepat 1 pasang garis sejajar dan 2 pasang garis tegak lurus.
- Domain kognitif `classify/applying`: Siswa harus mengidentifikasi sifat geometris (sejajar dan tegak lurus) pada setiap huruf yang diberikan dan membandingkannya dengan kriteria yang diminta. Ini melibatkan penerapan konsep pada konteks visual yang rutin.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?; E memang punya garis sejajar dan tegak lurus, tetapi garis sejajarnya tiga; M hanya memenuhi syarat sepasang garis sejajar, tidak punya garis tegak lurus; T hanya memenuhi syarat tegak lurus, tidak punya garis sejajar
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang definisi dan hubungan antara garis sejajar dan tegak lurus dalam bentuk huruf.. Bukti: satu pasang garis sejajar dan dua pasang garis tegak lurus
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk menganalisis sifat geometris dari beberapa objek (huruf) secara terpisah dan memverifikasi apakah mereka memenuhi kriteria yang diberikan. Meskipun prosedurnya rutin, siswa harus melakukan pemeriksaan sistematis pada setiap opsi, yang meningkatkan beban kognitif dibandingkan sekadar mengidentifikasi satu bentuk.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang garis sejajar dan tegak lurus. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 diharapkan mampu mengidentifikasi garis sejajar dan tegak lurus. Tugas ini memerlukan ketelitian dalam memeriksa setiap huruf terhadap dua kendala sekaligus (jumlah pasangan sejajar dan tegak lurus), yang membuatnya sedikit lebih menantang daripada sekadar identifikasi satu sifat. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 166/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000003 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.003242; conceptual=0.977047; procedural=0.019712; metacognitive=0.000000 | conceptual | 0.977047 | 0.085600 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.610215; Medium=0.383054; Hard=0.006731 | Easy | 0.610215 | 0.639573 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000004; H = 0.000004/ln(3) = 0.000003; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.977047; −Σp ln(p) = 0.118667; H = 0.118667/ln(4) = 0.085600; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.610215; −Σp ln(p) = 0.702643; H = 0.702643/ln(3) = 0.639573; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 4
Topik: Matematika SD Kelas 4
Subtopik: Garis-Garis Tegak Lurus dan Garis-Garis Sejajar
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan huruf-huruf berikut ini.

Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?
Pilihan: A. Huruf E
B. Huruf M
C. Huruf T
D. Tidak ada
Transkripsi visual: Gambar menampilkan huruf-huruf 'MATEMATIKA' yang ditulis di atas kertas berpetak. Huruf 'E' memiliki tiga garis horizontal sejajar dan empat garis tegak lurus (dua pasang). Huruf 'M' memiliki dua garis miring yang tidak sejajar dan dua garis vertikal yang sejajar (satu pasang), tanpa garis tegak lurus. Huruf 'T' memiliki satu garis horizontal dan satu garis vertikal yang membentuk satu pasang garis tegak lurus, tanpa garis sejajar.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `177f5534f5d559f72a66d033`

Diagram batang berikut menunjukan banyak siswa di SD Permata.<br><br>Apabila jumlah seluruh siswa di SD Permata adalah 346 siswa. Tentukan:<br><br>Banyak siswa kelas 2 SD Permata?

| Opsi | Isi |
|---|---|
| A | 292 siswa |
| B | 0 siswa |
| C | 54 siswa |
| D | 154 siswa |

![Gambar sumber soal 16](<../../../images/kelas4_panduan_guru_kelas4.pdf-0244-06.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Jumlah siswa kelas 1, 3, 4, 5, dan 6 adalah 57 + 58 + 56 + 62 + 59 = 292. Banyak siswa kelas 2 adalah 346 - 292 = 54.
Gambar sumber: images/kelas4_panduan_guru_kelas4.pdf-0244-06.png. Transkripsi visual: Diagram batang menunjukkan jumlah siswa per kelas di SD Permata. Kelas 1: 57, Kelas 3: 58, Kelas 4: 56, Kelas 5: 62, Kelas 6: 59. Batang untuk Kelas 2 kosong. Total siswa seluruhnya adalah 346.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4766adf2a7878007b156e6536d161b592dad4605500493e6c64bebe23ebc01c0`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 4701 |
| 2 | success | valid / verified | applying | procedural | Medium | 4328 |
| 3 | success | valid / verified | applying | procedural | Medium | 4456 |

Run 1 — solusi: Jumlah siswa kelas 1, 3, 4, 5, dan 6 adalah 57 + 58 + 56 + 62 + 59 = 292. Banyak siswa kelas 2 adalah 346 - 292 = 54.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi data dari diagram, menjumlahkan nilai-nilai yang diketahui, dan melakukan pengurangan dari total untuk menemukan nilai yang hilang.. Bukti: Apabila jumlah seluruh siswa di SD Permata adalah 346 siswa; Tentukan: Banyak siswa kelas 2 SD Permata?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penerapan algoritma penjumlahan dan pengurangan untuk menyelesaikan masalah data yang hilang.. Bukti: Tentukan: Banyak siswa kelas 2 SD Permata?
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah (ekstraksi data, penjumlahan, pengurangan) yang saling terkait. Ini adalah prosedur rutin bagi siswa kelas 4.. Bukti: Apabila jumlah seluruh siswa di SD Permata adalah 346 siswa; Tentukan: Banyak siswa kelas 2 SD Permata?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dan pengurangan bilangan cacah, membaca diagram batang. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas ini melibatkan operasi aritmatika dasar yang sesuai untuk kelas 4, namun memerlukan ketelitian dalam mengelola beberapa langkah (menjumlahkan 5 data lalu mengurangkan dari total). |

Run 2 — solusi: Jumlah siswa kelas 1, 3, 4, 5, 6 adalah 57 + 58 + 56 + 62 + 59 = 292. Jumlah siswa kelas 2 = 346 - 292 = 54.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur penjumlahan data yang diketahui dan pengurangan dari total untuk menemukan nilai yang hilang. Ini adalah penerapan konsep diagram batang dalam konteks rutin.. Bukti: Apabila jumlah seluruh siswa di SD Permata adalah 346 siswa; Tentukan: Banyak siswa kelas 2 SD Permata?
- Dimensi pengetahuan `classify/procedural`: Soal menuntut penggunaan algoritma penjumlahan dan pengurangan untuk menyelesaikan masalah data yang hilang.. Bukti: Tentukan: Banyak siswa kelas 2 SD Permata?
- Intended difficulty `classify/Medium`: Soal memerlukan beberapa langkah (penjumlahan 5 data, lalu pengurangan). Ini bukan sekadar membaca grafik langsung, melainkan mengolah data untuk mencari nilai yang hilang.. Bukti: Apabila jumlah seluruh siswa di SD Permata adalah 346 siswa; Tentukan: Banyak siswa kelas 2 SD Permata?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah dan pengurangan bilangan cacah. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 sudah terbiasa dengan operasi hitung dasar dan membaca diagram batang, namun soal ini menuntut dua langkah operasional yang saling bergantung (menjumlahkan lalu mengurangi), sehingga dikategorikan Medium. |

Run 3 — solusi: Jumlah siswa kelas 1, 3, 4, 5, 6 adalah 57 + 58 + 56 + 62 + 59 = 292. Jumlah siswa kelas 2 = 346 - 292 = 54.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur penjumlahan dan pengurangan untuk menemukan nilai yang hilang dalam konteks data diagram batang.. Bukti: Apabila jumlah seluruh siswa di SD Permata adalah 346 siswa. Tentukan: Banyak siswa kelas 2 SD Permata?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma penjumlahan dan pengurangan untuk menyelesaikan masalah.. Bukti: 57 + 58 + 56 + 62 + 59 = 292, jadi kelas 2 = 346 - 292 = 54 siswa.
- Intended difficulty `classify/Medium`: Soal memerlukan dua langkah operasi (penjumlahan data yang ada, lalu pengurangan dari total) yang saling bergantung. Ini adalah tugas rutin bagi kelas 4 namun memerlukan ketelitian lebih daripada sekadar membaca data langsung.. Bukti: Apabila jumlah seluruh siswa di SD Permata adalah 346 siswa.; Diagram batang berikut menunjukan banyak siswa di SD Permata.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dan pengurangan bilangan cacah sampai ratusan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 sudah terbiasa dengan diagram batang dan operasi hitung dasar. Tantangan terletak pada perlunya mengintegrasikan data dari diagram untuk mencari nilai yang hilang, bukan sekadar membaca nilai yang sudah ada. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 130/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000000 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.053552; conceptual=0.939936; procedural=0.006512; metacognitive=0.000000 | conceptual | 0.939936 | 0.178719 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.723689; Medium=0.269732; Hard=0.006579 | Easy | 0.723689 | 0.564827 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000001; H = 0.000001/ln(3) = 0.000000; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.939936; −Σp ln(p) = 0.247757; H = 0.247757/ln(4) = 0.178719; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.723689; −Σp ln(p) = 0.620525; H = 0.620525/ln(3) = 0.564827; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 4
Topik: Matematika SD Kelas 4
Subtopik: Diagram Batang
Tipe soal: multiple_choice
Stimulus: -
Soal: Diagram batang berikut menunjukan banyak siswa di SD Permata.

Apabila jumlah seluruh siswa di SD Permata adalah 346 siswa. Tentukan:

Banyak siswa kelas 2 SD Permata?
Pilihan: A. 292 siswa
B. 0 siswa
C. 54 siswa
D. 154 siswa
Transkripsi visual: Diagram batang menunjukkan jumlah siswa per kelas di SD Permata. Kelas 1: 57, Kelas 3: 58, Kelas 4: 56, Kelas 5: 62, Kelas 6: 59. Batang untuk Kelas 2 kosong. Total siswa seluruhnya adalah 346.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 17. Soal `4515f80b96eb86e33ab16d92`

Diberikan diagram batang untuk data siswa yang mengikuti lomba PORSENI tingkat kabupaten.<br><br>Lomba apakah yang paling sedikit diikuti siswa?

| Opsi | Isi |
|---|---|
| A | Menyanyi |
| B | Catur |
| C | Renang |
| D | Lari |

![Gambar sumber soal 17](<../../../images/kelas4_panduan_siswa_kelas4.pdf-0205-08.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Mengamati panjang batang pada diagram. Batang terpendek adalah Renang dengan nilai 2 siswa, yang merupakan jumlah paling sedikit dibandingkan kategori lainnya.
Gambar sumber: images/kelas4_panduan_siswa_kelas4.pdf-0205-08.png. Transkripsi visual: Diagram batang horizontal menunjukkan data siswa yang mengikuti lomba PORSENI. Sumbu vertikal berisi kategori lomba: Menyanyi, Renang, Bulu Tangkis, Puisi, Lari, Catur. Sumbu horizontal menunjukkan 'Banyak Siswa' dengan skala 0 sampai 9. Panjang batang untuk setiap lomba adalah: Menyanyi (8), Renang (2), Bulu Tangkis (5), Puisi (7), Lari (3), Catur (5). Batang terpendek adalah Renang dengan nilai 2.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `574e756685d34b0e23bf62ddd42f8d3281c993df0fe62ecdfbf7e100afdbaadb`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 3371 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 3400 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 3365 |

Run 1 — solusi: Mengamati panjang batang pada diagram. Batang terpendek adalah Renang dengan nilai 2 siswa, yang merupakan jumlah paling sedikit dibandingkan kategori lainnya.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca dan membandingkan panjang batang secara visual untuk mengidentifikasi nilai terkecil. Ini adalah prosedur langsung dalam membaca data.. Bukti: Lomba apakah yang paling sedikit diikuti siswa?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman dasar tentang cara membaca diagram batang sebagai representasi data.. Bukti: Lomba apakah yang paling sedikit diikuti siswa?
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena hanya memerlukan pengamatan visual langsung terhadap panjang batang. Tidak ada perhitungan atau manipulasi data yang diperlukan.. Bukti: Lomba apakah yang paling sedikit diikuti siswa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram batang sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 sudah terbiasa membaca diagram batang sederhana. Tugas ini hanya memerlukan perbandingan visual langsung tanpa langkah tambahan. |

Run 2 — solusi: Mengamati panjang batang pada diagram. Batang terpendek menunjukkan jumlah peserta paling sedikit. Batang untuk 'Renang' memiliki panjang paling pendek, yaitu 2 siswa.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data dari diagram batang dan membandingkan panjang batang secara visual untuk menentukan nilai terkecil. Ini adalah prosedur langsung dalam membaca data.. Bukti: Lomba apakah yang paling sedikit diikuti siswa?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang cara membaca dan menginterpretasikan representasi data sederhana (diagram batang), yang merupakan pengetahuan konseptual dasar.. Bukti: diagram batang untuk data siswa
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena hanya memerlukan identifikasi visual langsung terhadap batang terpendek. Tidak ada langkah tambahan, konversi, atau perhitungan yang diperlukan.. Bukti: Lomba apakah yang paling sedikit diikuti siswa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram batang sederhana dan membandingkan panjang objek. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 sudah terbiasa membaca diagram batang sederhana. Soal ini tidak menuntut analisis mendalam, hanya observasi visual dasar. |

Run 3 — solusi: Mengamati panjang batang pada diagram. Batang terpendek menunjukkan jumlah siswa paling sedikit. Batang untuk 'Renang' memiliki panjang paling pendek, yaitu 2 siswa.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca dan membandingkan panjang batang pada diagram untuk mengidentifikasi nilai terkecil. Ini adalah prosedur langsung dalam membaca data visual.. Bukti: Lomba apakah yang paling sedikit diikuti siswa?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman dasar tentang cara membaca dan menafsirkan informasi yang disajikan dalam bentuk diagram batang.. Bukti: diagram batang; Lomba apakah yang paling sedikit diikuti siswa?
- Intended difficulty `classify/Easy`: Soal ini sangat mudah karena hanya memerlukan observasi visual langsung terhadap panjang batang. Tidak ada perhitungan atau manipulasi data yang diperlukan.. Bukti: Lomba apakah yang paling sedikit diikuti siswa?

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
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 sudah terbiasa membaca diagram batang sederhana. Tugas ini hanya memerlukan perbandingan visual langsung tanpa langkah tambahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 160/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000000 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.003922; conceptual=0.991363; procedural=0.004714; metacognitive=0.000000 | conceptual | 0.991363 | 0.040098 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.586616; Medium=0.405029; Hard=0.008355 | Easy | 0.586616 | 0.654401 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000000; H = 0.000000/ln(3) = 0.000000; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.991363; −Σp ln(p) = 0.055588; H = 0.055588/ln(4) = 0.040098; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.586616; −Σp ln(p) = 0.718933; H = 0.718933/ln(3) = 0.654401; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 4
Topik: Matematika SD Kelas 4
Subtopik: Diagram Batang
Tipe soal: multiple_choice
Stimulus: -
Soal: Diberikan diagram batang untuk data siswa yang mengikuti lomba PORSENI tingkat kabupaten.

Lomba apakah yang paling sedikit diikuti siswa?
Pilihan: A. Menyanyi
B. Catur
C. Renang
D. Lari
Transkripsi visual: Diagram batang horizontal menunjukkan data siswa yang mengikuti lomba PORSENI. Sumbu vertikal berisi kategori lomba: Menyanyi, Renang, Bulu Tangkis, Puisi, Lari, Catur. Sumbu horizontal menunjukkan 'Banyak Siswa' dengan skala 0 sampai 9. Panjang batang untuk setiap lomba adalah: Menyanyi (8), Renang (2), Bulu Tangkis (5), Puisi (7), Lari (3), Catur (5). Batang terpendek adalah Renang dengan nilai 2.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `631ea2e9a2d5222d502bdf5c`

Hasil penilaian harian Matematika diperoleh: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10<br><br>Berapa banyak siswa yang mendapatkan nilai lebih dari 7?

| Opsi | Isi |
|---|---|
| A | 12 siswa |
| B | 8 siswa |
| C | 15 siswa |
| D | 10 siswa |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Data: 9, 8, 8, 5, 9, 6, 10, 9, 8, 6, 7, 8, 9, 9, 5, 6, 7, 7, 9, 10. Nilai > 7 adalah 8, 9, dan 10. Frekuensi: nilai 8 ada 4, nilai 9 ada 6, nilai 10 ada 2. Total = 4 + 6 + 2 = 12 siswa.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `44446088e6460e7c3327029926c48abad926f27506a6bfdd7a522b7923e98705`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2435 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2422 |
| 3 | success | valid / verified | applying | procedural | Easy | 2432 |

Run 1 — solusi: Data: 9, 8, 8, 5, 9, 6, 10, 9, 8, 6, 7, 8, 9, 9, 5, 6, 7, 7, 9, 10. Nilai > 7 adalah 8, 9, dan 10. Frekuensi: nilai 8 ada 4, nilai 9 ada 6, nilai 10 ada 2. Total = 4 + 6 + 2 = 12 siswa.
- Domain kognitif `classify/applying`: Siswa diminta untuk mengidentifikasi nilai yang memenuhi kriteria (lebih dari 7) dan menghitung frekuensinya dari sekumpulan data. Ini adalah penerapan prosedur pengolahan data sederhana yang rutin.. Bukti: Berapa banyak siswa yang mendapatkan nilai lebih dari 7?
- Dimensi pengetahuan `classify/procedural`: Soal ini melibatkan penggunaan metode penghitungan frekuensi (tallying) untuk mengorganisir data mentah, yang merupakan prosedur standar dalam penyajian data.. Bukti: Hasil penilaian harian Matematika diperoleh: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu melakukan penyortiran dan penjumlahan sederhana pada data yang diberikan. Tidak ada kendala yang berinteraksi atau kebutuhan untuk merancang strategi kompleks; jalurnya sangat langsung.. Bukti: Berapa banyak siswa yang mendapatkan nilai lebih dari 7?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan bilangan (lebih dari) dan menjumlahkan bilangan cacah. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 20 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 4, mengolah data mentah menjadi frekuensi adalah materi standar. Tugas ini bersifat rutin dan tidak memerlukan penalaran tingkat tinggi. |

Run 2 — solusi: Data: 9, 8, 8, 5, 9, 6, 10, 9, 8, 6, 7, 8, 9, 9, 5, 6, 7, 7, 9, 10. Nilai > 7 adalah 8, 9, dan 10. Frekuensi nilai 8 ada 4, nilai 9 ada 6, nilai 10 ada 2. Total siswa = 4 + 6 + 2 = 12.
- Domain kognitif `classify/applying`: Siswa perlu mengklasifikasikan data mentah ke dalam kategori (nilai > 7) dan menghitung frekuensinya. Ini adalah penerapan prosedur pengolahan data sederhana yang rutin.. Bukti: Berapa banyak siswa yang mendapatkan nilai lebih dari 7?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang bagaimana mengorganisasi dan menghitung frekuensi dari sekumpulan data mentah, yang merupakan konsep dasar dalam penyajian data.. Bukti: Hasil penilaian harian Matematika diperoleh: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10
- Intended difficulty `classify/Easy`: Soal ini meminta siswa mengidentifikasi nilai yang memenuhi kriteria (>7) dan menghitung jumlahnya. Langkah-langkahnya jelas dan rutin bagi siswa kelas 4. Tidak ada kendala yang saling berinteraksi secara kompleks.. Bukti: Berapa banyak siswa yang mendapatkan nilai lebih dari 7?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan bilangan dan menghitung frekuensi data sederhana. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 20 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas mengolah data mentah menjadi informasi frekuensi adalah standar kurikulum kelas 4. Prosedur penghitungan langsung dan tidak memerlukan strategi non-rutin. |

Run 3 — solusi: Data: 9, 8, 8, 5, 9, 6, 10, 9, 8, 6, 7, 8, 9, 9, 5, 6, 7, 7, 9, 10. Nilai > 7 adalah 8, 9, dan 10. Frekuensi: nilai 8 ada 4, nilai 9 ada 6, nilai 10 ada 2. Total = 4 + 6 + 2 = 12 siswa.
- Domain kognitif `classify/applying`: Siswa perlu mengklasifikasikan data mentah ke dalam kategori (nilai > 7) dan menghitung frekuensinya. Ini adalah penerapan prosedur pengolahan data sederhana yang rutin bagi kelas 4.. Bukti: Berapa banyak siswa yang mendapatkan nilai lebih dari 7?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara mengorganisasi dan menghitung frekuensi data mentah.. Bukti: Hasil penilaian harian Matematika diperoleh: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10
- Intended difficulty `classify/Easy`: Soal ini tergolong Easy karena siswa hanya perlu melakukan penghitungan frekuensi sederhana dari data yang diberikan. Tidak ada kendala yang berinteraksi atau kebutuhan untuk strategi nonrutin. Langkah-langkahnya jelas dan familiar bagi siswa kelas 4.. Bukti: Berapa banyak siswa yang mendapatkan nilai lebih dari 7?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung frekuensi data sederhana dan membandingkan bilangan (lebih dari 7). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 20 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas mengolah data mentah menjadi tabel frekuensi atau menghitung jumlah kategori adalah materi standar kelas 4. Beban kognitif rendah karena hanya melibatkan pencacahan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4202`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan prosedur rutin untuk mengklasifikasikan data mentah ke dalam kategori yang ditentukan (nilai > 7) dan menghitung frekuensinya. Tidak ada strategi nonrutin yang diperlukan.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang cara mengorganisasi, menyortir, dan menghitung frekuensi dari sekumpulan data mentah.
- Intended difficulty `Easy`: Soal ini tergolong Easy karena siswa hanya perlu melakukan penghitungan frekuensi sederhana dari data yang diberikan. Langkah-langkahnya jelas, rutin, dan tidak melibatkan kendala yang berinteraksi.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan bilangan (lebih dari) dan menjumlahkan bilangan cacah. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 20 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas mengolah data mentah menjadi frekuensi adalah materi standar kelas 4. Beban kognitif rendah karena hanya melibatkan pencacahan data yang tersedia secara eksplisit. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 89/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.003487; applying=0.996513; reasoning=0.000000 | applying | 0.996513 | 0.021128 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.330920; conceptual=0.655978; procedural=0.013102; metacognitive=0.000000 | conceptual | 0.655978 | 0.504462 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.906528; Medium=0.091449; Hard=0.002023 | Easy | 0.906528 | 0.291508 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.996513; −Σp ln(p) = 0.023212; H = 0.023212/ln(3) = 0.021128; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.655978; −Σp ln(p) = 0.699333; H = 0.699333/ln(4) = 0.504462; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.906528; −Σp ln(p) = 0.320254; H = 0.320254/ln(3) = 0.291508; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 4
Topik: Matematika SD Kelas 4
Subtopik: Menyajikan Data dalam Bentuk Tabel
Tipe soal: multiple_choice
Stimulus: -
Soal: Hasil penilaian harian Matematika diperoleh: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10

Berapa banyak siswa yang mendapatkan nilai lebih dari 7?
Pilihan: A. 12 siswa
B. 8 siswa
C. 15 siswa
D. 10 siswa
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
