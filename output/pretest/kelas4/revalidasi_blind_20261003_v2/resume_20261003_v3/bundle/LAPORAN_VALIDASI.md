# Validasi ulang soal kelas 4 — Gemini blind N=3 dan diagnostik IndoBERT

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v4-blind-key-verified`. Rubrik: `math-rubric-3x4x3-v2-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 4 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan bukan keputusan ahli manusia.

Checkpoint dikunci dengan SHA-256 sebelum inferensi IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Prediksi model lama dipakai untuk menunjukkan ketidaksepakatan; tidak diberikan kembali ke Gemini.

Jumlah soal: 18; distribusi label advisory: `{"mathCognitiveDomain": {"applying": 17, "knowing": 1, "reasoning": 0}, "knowledgeDimension": {"conceptual": 10, "procedural": 8, "factual": 0, "metacognitive": 0}, "intendedDifficulty": {"Easy": 14, "Medium": 4, "Hard": 0}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"applying": 17, "knowing": 1, "reasoning": 0}, "knowledgeDimension": {"conceptual": 10, "procedural": 8, "factual": 0, "metacognitive": 0}, "intendedDifficulty": {"Easy": 14, "Medium": 4, "Hard": 0}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"pending_expert_review": 18}`.
Run awal sukses: 54/54; adjudikasi: 3; token sukses tercatat: 123,076.

Seluruh label masih silver/advisory, gold manusia tetap null, dan publishing otomatis tidak diaktifkan. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

IndoBERT aktif: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Artifact belum disetujui; tidak ada training ulang dalam batch ini. Difficulty model lama dapat mengalami class collapse. Confidence dari kalibrasi kelas 1 yang kecil belum membuktikan ketepatan label.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten tetap memerlukan pemeriksaan ahli.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 14 | 14 | [Easy.json](difficulty/Easy.json) |
| Medium | 4 | 4 | [Medium.json](difficulty/Medium.json) |
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
Solusi minimum hasil AI: Mencari faktor dari 10. Bilangan yang membagi habis 10 adalah 1, 2, 5, dan 10.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6b27c2f7d25735b6a0b981a28c8f8f3f4ae849de36e9f14b608dc29ae7088355`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1499 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1494 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1476 |

Run 1 — solusi: Mencari faktor dari 10. Bilangan yang membagi habis 10 adalah 1, 2, 5, dan 10.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep faktor bilangan untuk menentukan pembagi dari 10 agar pembagian beras sama rata tanpa sisa.. Bukti: Berapa kemungkinan banyaknya orang yang akan mendapat pembagian beras dari Ibu Slamet?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep faktor sebagai pembagi bilangan bulat yang menghasilkan sisa nol.. Bukti: Berapa kemungkinan banyaknya orang yang akan mendapat pembagian beras dari Ibu Slamet?
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya meminta identifikasi faktor dari bilangan kecil (10) yang merupakan prosedur rutin di kelas 4.. Bukti: Total beras yang dibagikan oleh Ibu Slamet 10 kg.; Berapa kemungkinan banyaknya orang yang akan mendapat pembagian beras

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
| gradeRelativeRationale | Mencari faktor bilangan adalah materi standar kelas 4 yang bersifat rutin. |

Run 2 — solusi: Mencari faktor dari 10 kg beras agar pembagian sama rata tanpa sisa. Faktor dari 10 adalah 1, 2, 5, dan 10.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep faktor bilangan untuk memecahkan masalah pembagian yang sama rata (tanpa sisa) dalam konteks kehidupan sehari-hari.. Bukti: Berapa kemungkinan banyaknya orang yang akan mendapat pembagian beras dari Ibu Slamet?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara pembagian bilangan bulat dan faktor bilangan.. Bukti: membagikan semua beras ke beberapa orang dengan berat yang sama
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena melibatkan bilangan kecil (10) dan konsep faktor yang merupakan materi dasar kelas 4, dengan prosedur yang langsung.. Bukti: Total beras yang dibagikan oleh Ibu Slamet 10 kg; Berapa kemungkinan banyaknya orang yang akan mendapat pembagian beras

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pembagian dan konsep faktor bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari faktor dari bilangan 10 adalah tugas standar untuk siswa kelas 4 dalam topik kelipatan dan faktor. |

Run 3 — solusi: Mencari faktor dari 10. Bilangan yang membagi habis 10 adalah 1, 2, 5, dan 10.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep faktor bilangan untuk menentukan pembagi dari 10 agar pembagian beras sama rata tanpa sisa.. Bukti: Berapa kemungkinan banyaknya orang yang akan mendapat pembagian beras dari Ibu Slamet?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep faktor sebagai pembagi bilangan yang menghasilkan sisa nol.. Bukti: membagikan semua beras ke beberapa orang dengan berat yang sama
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena melibatkan bilangan kecil (10) dan prosedur dasar mencari faktor yang sudah dipelajari di kelas 4.. Bukti: Total beras yang dibagikan oleh Ibu Slamet 10 kg; membagikan semua beras ke beberapa orang dengan berat yang sama

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pembagian dan faktor bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari faktor dari bilangan 10 adalah materi standar kelas 4 SD. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `51d112e2cf5ac0ac6feceb42`

Tentukan faktor dari:<br><br>a. 27

| Opsi | Isi |
|---|---|
| A | 1, 3, 6, 9, 27 |
| B | 1, 3, 9, 27 |
| C | 1, 2, 7, 27 |
| D | 3, 9 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Faktor dari 27 adalah bilangan yang membagi habis 27. Pasangan faktornya adalah 1 x 27 = 27 dan 3 x 9 = 27. Jadi, faktor dari 27 adalah 1, 3, 9, 27.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `13c4beb54ba7bde8594a3c7da1d50c48f8213a4aace6fd18079fc03c2a8e5b6a`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 1355 |
| 2 | success | valid / verified | applying | procedural | Easy | 1341 |
| 3 | success | valid / verified | applying | procedural | Easy | 1387 |

Run 1 — solusi: Faktor dari 27 adalah bilangan yang membagi habis 27. Pasangan faktor: 1 x 27 = 27 dan 3 x 9 = 27. Jadi, faktornya adalah 1, 3, 9, 27.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi faktor dari sebuah bilangan, yang merupakan proses rutin dalam materi faktor dan kelipatan kelas 4.. Bukti: Tentukan faktor dari: a. 27
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang definisi faktor dan penerapan algoritma pembagian sederhana untuk menemukan pasangan faktor.. Bukti: Tentukan faktor dari: a. 27
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung, menggunakan prosedur standar yang sudah dipelajari di kelas 4 tanpa memerlukan strategi kompleks atau integrasi informasi.. Bukti: Tentukan faktor dari: a. 27

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep perkalian dan pembagian dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari faktor bilangan dua digit adalah materi standar kelas 4 yang bersifat rutin. |

Run 2 — solusi: Faktor dari 27 adalah bilangan yang membagi habis 27. 27 = 1 x 27 dan 27 = 3 x 9. Jadi, faktornya adalah 1, 3, 9, 27.
- Domain kognitif `classify/applying`: Siswa diminta untuk menerapkan prosedur standar dalam menentukan faktor bilangan bulat, yang merupakan tugas rutin.. Bukti: Tentukan faktor dari: a. 27
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau teknik mencari pasangan faktor dari suatu bilangan.. Bukti: Tentukan faktor dari: a. 27
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, hanya memerlukan satu langkah prosedural untuk menemukan pasangan faktor dari bilangan kecil.. Bukti: Tentukan faktor dari: a. 27

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep perkalian dasar dan pembagian. |
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

Run 3 — solusi: Faktor dari 27 adalah bilangan yang membagi habis 27. 27 = 1 x 27 dan 27 = 3 x 9. Maka faktornya adalah 1, 3, 9, 27.
- Domain kognitif `classify/applying`: Siswa diminta melakukan prosedur rutin untuk menentukan faktor dari bilangan bulat, yang merupakan proses standar dalam kurikulum kelas 4.. Bukti: Tentukan faktor dari: a. 27
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau teknik mencari pasangan faktor dari suatu bilangan.. Bukti: Tentukan faktor dari: a. 27
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, hanya memerlukan pemahaman dasar tentang perkalian dan pembagian untuk bilangan kecil.. Bukti: Tentukan faktor dari: a. 27

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep perkalian dasar dan pembagian bilangan cacah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mencari faktor bilangan dua digit adalah materi standar kelas 4 yang bersifat prosedural langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 1, "applying": 2} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2604`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta untuk menerapkan prosedur rutin (mencari pasangan faktor) untuk bilangan yang diberikan. Ini adalah penerapan konsep dasar faktor.
- Dimensi pengetahuan `procedural`: Soal ini menguji penguasaan algoritma atau teknik mencari pasangan faktor dari suatu bilangan.
- Intended difficulty `Easy`: Soal ini bersifat rutin, langsung, dan menggunakan angka kecil yang sesuai dengan kurikulum kelas 4. Tidak ada strategi non-rutin yang diperlukan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep perkalian dan pembagian dasar. |
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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `d8e3e19d701550680f504300`

Tentukan pembagian berikut sebagai pengurangan berulang!<br><br>16 : 4 = .....

| Opsi | Isi |
|---|---|
| A | 3 kali (16-4-4-4=4) |
| B | 4 kali (16-4-4-4-4=0) |
| C | 5 kali (20-4-4-4-4-4=0) |
| D | 12 kali (16-4=12, dianggap tiap kali kurang 1) |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: 16 : 4 berarti 16 dikurangi 4 secara berulang sampai hasilnya 0. Langkahnya: 16 - 4 = 12, 12 - 4 = 8, 8 - 4 = 4, 4 - 4 = 0. Ada 4 kali pengurangan.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `41d994a548594c488bb3903242f0f8e758aee9cc32fa75104b60b45a7c44c6e6`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1387 |
| 2 | success | valid / verified | applying | procedural | Easy | 1384 |
| 3 | success | valid / verified | applying | procedural | Easy | 1384 |

Run 1 — solusi: 16 : 4 berarti 16 dikurangi 4 secara berulang sampai hasilnya 0. Langkahnya: 16 - 4 = 12, 12 - 4 = 8, 8 - 4 = 4, 4 - 4 = 0. Ada 4 kali pengurangan.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep pembagian sebagai pengurangan berulang, yang merupakan prosedur standar untuk memahami pembagian di kelas 4.. Bukti: Tentukan pembagian berikut sebagai pengurangan berulang!; 16 : 4 = .....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau teknik pengurangan berulang sebagai representasi dari operasi pembagian.. Bukti: Tentukan pembagian berikut sebagai pengurangan berulang!
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin, menggunakan angka kecil, dan langsung menguji pemahaman konsep dasar pembagian yang diajarkan di kelas 4.. Bukti: 16 : 4 = .....

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
| gradeRelativeRationale | Sesuai untuk kelas 4 karena pembagian sebagai pengurangan berulang adalah materi dasar yang sering dilatih. |

Run 2 — solusi: 16 : 4 berarti 16 dikurangi 4 secara berulang sampai hasilnya 0. Langkahnya: 16 - 4 = 12, 12 - 4 = 8, 8 - 4 = 4, 4 - 4 = 0. Ada 4 kali pengurangan.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep pembagian sebagai pengurangan berulang, yang merupakan prosedur standar untuk memahami pembagian di kelas 4.. Bukti: Tentukan pembagian berikut sebagai pengurangan berulang!; 16 : 4 = .....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau teknik pengurangan berulang sebagai representasi dari operasi pembagian.. Bukti: Tentukan pembagian berikut sebagai pengurangan berulang!
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, menggunakan angka kecil, dan mengikuti prosedur rutin yang diajarkan di kelas 4.. Bukti: 16 : 4 = .....

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
| gradeRelativeRationale | Sesuai untuk kelas 4 karena pembagian sebagai pengurangan berulang adalah materi pengenalan awal pembagian. |

Run 3 — solusi: 16 : 4 berarti 16 dikurangi 4 secara berulang sampai hasilnya 0. Langkahnya: 16-4=12, 12-4=8, 8-4=4, 4-4=0. Ada 4 kali pengurangan.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan konsep pembagian sebagai pengurangan berulang, yang merupakan prosedur rutin yang diajarkan di kelas 4.. Bukti: Tentukan pembagian berikut sebagai pengurangan berulang!; 16 : 4 = .....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau teknik pengurangan berulang untuk menyelesaikan pembagian.. Bukti: Tentukan pembagian berikut sebagai pengurangan berulang!
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung, menggunakan bilangan kecil, dan merupakan prosedur standar yang familiar bagi siswa kelas 4.. Bukti: 16 : 4 = .....

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
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 4 untuk mengenalkan pembagian sebagai pengurangan berulang dengan angka sederhana. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b90c90cb97c1c12c12f8a4616141dc11dbcc66053c0fea60fbdf065ac2fa5025`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1315 |
| 2 | success | valid / verified | applying | procedural | Easy | 1353 |
| 3 | success | valid / verified | applying | procedural | Easy | 1350 |

Run 1 — solusi: 6/10 = 60/100 = 60%.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur konversi pecahan ke persen dengan mengubah penyebut menjadi 100, yang merupakan prosedur rutin di kelas 4.. Bukti: 6 pertanyaan dari 10 soal; berapa persen soal yang dijawab benar
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau teknik mengubah pecahan menjadi bentuk persen.. Bukti: 6 pertanyaan dari 10 soal; berapa persen
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, hanya memerlukan satu langkah konversi pecahan ke persen yang umum diajarkan di kelas 4.. Bukti: 6 pertanyaan dari 10 soal; berapa persen

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman pecahan senilai dan konsep persen sebagai per seratus. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konversi pecahan ke persen adalah materi standar kelas 4 yang bersifat prosedural langsung. |

Run 2 — solusi: 6/10 = 60/100 = 60%.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur konversi pecahan ke persen dalam situasi rutin yang sudah sering dipelajari di kelas 4.. Bukti: 6 pertanyaan dari 10 soal; berapa persen soal yang dijawab benar
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau teknik mengubah pecahan dengan penyebut 10 menjadi persen (penyebut 100).. Bukti: 6/10 = 60/100 = 60%
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin, menggunakan representasi pecahan yang sederhana, dan hanya memerlukan satu langkah konversi langsung.. Bukti: 6 pertanyaan dari 10 soal; berapa persen

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman pecahan senilai dan konsep persen sebagai per seratus. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konversi pecahan ke persen dengan penyebut 10 adalah materi standar kelas 4 yang bersifat prosedural langsung. |

Run 3 — solusi: 6/10 = 60/100 = 60%.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur konversi pecahan ke persen dengan mengubah penyebut menjadi 100, yang merupakan prosedur rutin di kelas 4.. Bukti: 6 pertanyaan dari 10 soal; Tentukan berapa persen
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau teknik mengubah pecahan biasa menjadi bentuk persen.. Bukti: 6/10 = 60/100 = 60%
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, hanya memerlukan satu langkah konversi pecahan ke persen dengan penyebut yang mudah diubah ke 100.. Bukti: 6 pertanyaan dari 10 soal; Tentukan berapa persen

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman pecahan senilai dan konsep dasar persen sebagai per seratus. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konversi pecahan ke persen adalah materi standar kelas 4. Soal ini tidak memiliki kompleksitas tambahan. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `87c4b5ff5d1524fbd581c451`

Suatu sekolah memilih 30 siswa dari 100 orang siswa yang akan diikutkan lomba berlari. Tentukan berapa persen siswa yang terpilih lomba lari tersebut!

| Opsi | Isi |
|---|---|
| A | 30% |
| B | 0,3% |
| C | 70% |
| D | 3% |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: 30 dari 100 siswa berarti 30/100. Dalam konsep persen, per seratus adalah persen, sehingga 30/100 = 30%.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `['mengidentifikasi', 'menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `efec803afdecbaa7f65a9b6f99d2a21caa885ae8daa19bb6feb136140ce1bb57`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1371 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1355 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1370 |

Run 1 — solusi: 30 dari 100 siswa berarti 30/100. Dalam konsep persen, per seratus adalah persen, sehingga 30/100 = 30%.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan pemahaman dasar tentang definisi persen (per seratus) pada situasi yang sudah terstruktur dengan penyebut 100. Ini adalah penerapan prosedur rutin.. Bukti: 30 siswa dari 100 orang siswa; Tentukan berapa persen
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman hubungan antara pecahan dengan penyebut 100 dan notasi persen sebagai representasi konsep yang sama.. Bukti: 30 dari 100; berapa persen
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung, menggunakan representasi yang familiar, dan hanya memerlukan satu langkah konversi sederhana yang merupakan standar kurikulum kelas 4.. Bukti: 30 siswa dari 100; Tentukan berapa persen

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
| gradeRelativeRationale | Konversi pecahan per seratus ke persen adalah materi dasar kelas 4 yang diajarkan secara eksplisit. |

Run 2 — solusi: 30 dari 100 siswa berarti 30/100. Dalam bentuk persen, 30/100 sama dengan 30%.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan pemahaman dasar tentang definisi persen sebagai per seratus dalam situasi rutin yang langsung.. Bukti: 30 siswa dari 100 orang siswa; Tentukan berapa persen
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan antara pecahan per seratus dengan notasi persen.. Bukti: 30 siswa dari 100 orang siswa; berapa persen
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung dan rutin untuk kelas 4, di mana angka yang diberikan sudah dalam bentuk per seratus, sehingga tidak memerlukan langkah perhitungan kompleks.. Bukti: 30 siswa dari 100 orang siswa; Tentukan berapa persen

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
| gradeRelativeRationale | Sesuai untuk kelas 4 karena langsung menguji definisi persen tanpa manipulasi angka yang rumit. |

Run 3 — solusi: 30 dari 100 siswa berarti 30/100. Dalam bentuk persen, 30/100 sama dengan 30%.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan pemahaman konsep dasar bahwa persen adalah per seratus untuk mengubah pecahan 30/100 menjadi 30%. Ini adalah prosedur rutin dalam kurikulum kelas 4.. Bukti: 30 siswa dari 100 orang siswa; Tentukan berapa persen
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman hubungan antara pecahan per seratus dan notasi persen, yang merupakan konsep dasar dalam topik pecahan.. Bukti: 30 dari 100; berapa persen
- Intended difficulty `classify/Easy`: Soal ini bersifat langsung, menggunakan representasi yang sangat familiar (per seratus), dan hanya memerlukan satu langkah konversi sederhana.. Bukti: 30 siswa dari 100; berapa persen

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
| gradeRelativeRationale | Konversi pecahan per seratus ke persen adalah materi standar kelas 4 yang bersifat prosedural langsung. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `Gambar 2 (segi enam) adalah satu-satunya yang menunjukkan seperempat karena dibagi menjadi empat bagian yang sama besar.`.
Solusi minimum hasil AI: Seperempat berarti satu dari empat bagian yang sama besar. Hanya gambar 2 yang memenuhi syarat luas bagian yang diarsir sama dengan tiga bagian lainnya.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0159-10.png, images/kelas2_panduan_siswa_kelas2.pdf-0159-11.png, images/kelas2_panduan_siswa_kelas2.pdf-0159-12.png, images/kelas2_panduan_siswa_kelas2.pdf-0159-13.png. Transkripsi visual: Terdapat empat gambar bangun datar yang masing-masing dibagi menjadi empat bagian oleh garis vertikal dan horizontal. Gambar 1 (segitiga) dibagi tidak simetris. Gambar 2 (segi enam) dibagi menjadi empat bagian yang tampak sama besar. Gambar 3 (bentuk panah) dibagi tidak simetris. Gambar 4 (persegi panjang) dibagi menjadi empat bagian yang tidak sama besar.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b263f6a66f8e939cae1c46b1660655716d03c39dcbbeca3b0e619dea58d71434`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 5850 |
| 2 | success | valid / verified | applying | conceptual | Easy | 5882 |
| 3 | success | valid / verified | applying | conceptual | Easy | 5859 |

Run 1 — solusi: Seperempat berarti satu dari empat bagian yang sama besar. Hanya gambar 2 yang memenuhi syarat luas bagian yang diarsir sama dengan tiga bagian lainnya.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep pecahan (seperempat) untuk mengidentifikasi apakah pembagian bangun datar menghasilkan bagian yang sama besar.. Bukti: Mana gambar yang menunjukkan seperempat
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang apa arti 'seperempat' (bagian yang sama besar) dalam konteks geometri.. Bukti: seperempat dari benda utuh
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan pemahaman visual dasar tentang pembagian area yang sama besar, yang merupakan materi standar kelas 4.. Bukti: Mana gambar yang menunjukkan seperempat. Mana gambar yang tidak menunjukkan seperempat.

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
| gradeRelativeRationale | Siswa kelas 4 diharapkan sudah mampu membedakan pembagian area yang sama besar dan tidak sama besar secara visual. |

Run 2 — solusi: Gambar 2 menunjukkan pembagian bangun datar menjadi empat bagian yang kongruen (sama besar dan sama bentuk), yang merupakan definisi visual dari seperempat.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman konsep pecahan (seperempat) untuk mengevaluasi apakah pembagian pada setiap gambar menghasilkan bagian yang sama besar.. Bukti: Mana gambar yang menunjukkan seperempat. Mana gambar yang tidak menunjukkan seperempat.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang apa arti 'seperempat' dalam konteks geometri (pembagian area menjadi bagian yang sama besar), bukan sekadar menghafal fakta.. Bukti: seperempat dari benda utuh
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan pengamatan visual langsung terhadap pembagian area tanpa perhitungan numerik yang kompleks.. Bukti: Perhatikan gambar yang diwarnai berikut.; Mana gambar yang menunjukkan seperempat.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pecahan sebagai bagian dari keseluruhan dan konsep kesamaan luas/ukuran. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 diharapkan sudah mampu mengidentifikasi pecahan sederhana melalui representasi visual bangun datar. |

Run 3 — solusi: Seperempat berarti satu dari empat bagian yang sama besar. Hanya Gambar 2 yang memiliki empat bagian dengan luas yang identik.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman konsep pecahan (seperempat) untuk mengevaluasi apakah pembagian pada setiap bangun datar menghasilkan bagian-bagian yang sama besar.. Bukti: Mana gambar yang menunjukkan seperempat. Mana gambar yang tidak menunjukkan seperempat.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang apa arti 'seperempat' dalam konteks luas daerah, yaitu pembagian menjadi bagian-bagian yang sama besar.. Bukti: seperempat dari benda utuh
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan pemahaman visual dasar tentang kesamaan luas bagian dalam pecahan, tanpa perhitungan numerik yang kompleks.. Bukti: Mana gambar yang menunjukkan seperempat. Mana gambar yang tidak menunjukkan seperempat.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang pecahan sebagai bagian dari keseluruhan dan konsep kesamaan luas. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 diharapkan sudah mampu mengidentifikasi pecahan sederhana melalui representasi visual bangun datar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 156/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000015; applying=0.999985; reasoning=0.000000 | applying | 0.999985 | 0.000170 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.001905; conceptual=0.995804; procedural=0.002291; metacognitive=0.000000 | conceptual | 0.995804 | 0.021674 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.687989; Medium=0.304802; Hard=0.007209 | Easy | 0.687989 | 0.596195 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999985; −Σp ln(p) = 0.000187; H = 0.000187/ln(3) = 0.000170; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.995804; −Σp ln(p) = 0.030046; H = 0.030046/ln(4) = 0.021674; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.687989; −Σp ln(p) = 0.654987; H = 0.654987/ln(3) = 0.596195; T = 0.953328.


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
Transkripsi visual: Terdapat empat gambar bangun datar yang masing-masing dibagi menjadi empat bagian oleh garis vertikal dan horizontal. Gambar 1 (segitiga) dibagi tidak simetris. Gambar 2 (segi enam) dibagi menjadi empat bagian yang tampak sama besar. Gambar 3 (bentuk panah) dibagi tidak simetris. Gambar 4 (persegi panjang) dibagi menjadi empat bagian yang tidak sama besar.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `bcd1ec2726d4dc3e37ec631d`

13, 22, 31, ..., 49, ...<br><br>Tentukan bilangan yang tepat sesuai pola bilangan yang diberikan !

| Opsi | Isi |
|---|---|
| A | 39 dan 59 |
| B | 45 dan 54 |
| C | 31 dan 49 |
| D | 40 dan 58 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Pola bilangan adalah penambahan 9 secara konstan. 31 + 9 = 40, dan 49 + 9 = 58. Maka jawabannya 40 dan 58.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7f3b14a549eee4a643c0823369187054f0915e812c7b5e570716182ca59f78ae`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1395 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1426 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1385 |

Run 1 — solusi: Pola bilangan adalah penambahan 9 secara konstan. 31 + 9 = 40, dan 49 + 9 = 58. Maka jawabannya 40 dan 58.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi aturan pola (penambahan 9) dan menerapkannya pada urutan bilangan, yang merupakan proses applying.. Bukti: 13, 22, 31, ..., 49, ...; Tentukan bilangan yang tepat sesuai pola bilangan yang diberikan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep pola bilangan aritmatika sederhana.. Bukti: pola bilangan
- Intended difficulty `classify/Easy`: Soal ini melibatkan pola aritmatika dasar dengan satu aturan yang konsisten, sesuai untuk tingkat kelas 4.. Bukti: 13, 22, 31, ..., 49, ...

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
| gradeRelativeRationale | Pola bilangan dengan selisih tetap adalah materi standar kelas 4 yang bersifat rutin. |

Run 2 — solusi: Pola bilangan adalah penambahan 9 setiap langkahnya (13+9=22, 22+9=31). Maka, bilangan setelah 31 adalah 31+9=40, dan bilangan setelah 49 adalah 49+9=58.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi aturan penambahan konstan (pola) dari deret yang diberikan dan menerapkannya untuk menemukan suku yang hilang.. Bukti: 13, 22, 31, ..., 49, ...; Tentukan bilangan yang tepat sesuai pola bilangan yang diberikan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep pola bilangan aritmatika sederhana yang memerlukan penerapan prosedur penjumlahan berulang.. Bukti: pola bilangan
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena melibatkan pola penambahan yang konsisten dan sederhana, yang merupakan materi standar kelas 4.. Bukti: 13, 22, 31, ..., 49, ...

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan dua digit dan pemahaman dasar tentang urutan bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pola bilangan dengan selisih tetap adalah materi dasar kelas 4 yang rutin dikerjakan siswa. |

Run 3 — solusi: Pola bilangan adalah penambahan 9 secara konstan. 31 + 9 = 40 dan 49 + 9 = 58.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi aturan penambahan konstan (+9) dari urutan bilangan yang diberikan, yang merupakan proses penerapan prosedur rutin.. Bukti: 13, 22, 31, ..., 49, ...
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep pola bilangan aritmatika sederhana dan penggunaan algoritma penjumlahan untuk meneruskannya.. Bukti: Tentukan bilangan yang tepat sesuai pola bilangan yang diberikan
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena melibatkan pola penambahan konstan yang sederhana dan familiar bagi siswa kelas 4, dengan beban perhitungan yang rendah.. Bukti: 13, 22, 31, ..., 49, ...

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan dua digit |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pola bilangan dengan selisih tetap adalah materi standar kelas 4 yang bersifat rutin. |

Histori retry: run 1 sebelumnya `failed` / `ClientError:429`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 1 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

Histori retry: run 2 sebelumnya `failed` / `ConnectError:unknown`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "conceptual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `8639aa720008550cb79af345`

34, 27, 20, 13, ...<br><br>Tentukan bilangan yang tepat sesuai pola bilangan yang diberikan!

| Opsi | Isi |
|---|---|
| A | 5 |
| B | 6 |
| C | 7 |
| D | 13 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Pola bilangan adalah pengurangan 7 secara berulang: 34-7=27, 27-7=20, 20-7=13, 13-7=6.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `549a9dc6406e8423aed4b6863520fe1d3ea9fc8725b28bceb653ee424b31a3df`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1318 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1322 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1311 |

Run 1 — solusi: Pola bilangan adalah pengurangan 7 secara berulang: 34-7=27, 27-7=20, 20-7=13, 13-7=6.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi aturan pengurangan yang konsisten (pola) dan menerapkannya satu kali untuk menemukan suku berikutnya.. Bukti: 34, 27, 20, 13, ...; Tentukan bilangan yang tepat sesuai pola
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep pola bilangan (pengurangan tetap) yang merupakan struktur matematis dasar.. Bukti: 34, 27, 20, 13, ...
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin bagi siswa kelas 4 yang sudah mempelajari pola bilangan sederhana. Hanya memerlukan satu langkah operasi pengurangan.. Bukti: 34, 27, 20, 13, ...

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
| gradeRelativeRationale | Pola bilangan dengan selisih tetap adalah materi standar kelas 4. Operasi pengurangan yang digunakan sederhana. |

Run 2 — solusi: Pola bilangan adalah pengurangan 7 secara berulang: 34 - 7 = 27, 27 - 7 = 20, 20 - 7 = 13, 13 - 7 = 6.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi aturan pola (pengurangan 7) dan menerapkannya untuk menemukan suku berikutnya. Ini adalah proses rutin.. Bukti: 34, 27, 20, 13, ...; Tentukan bilangan yang tepat sesuai pola
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip pola bilangan (pengurangan tetap).. Bukti: 34, 27, 20, 13, ...
- Intended difficulty `classify/Easy`: Soal ini melibatkan prosedur pengurangan sederhana yang familiar bagi siswa kelas 4 dengan satu langkah logis.. Bukti: 34, 27, 20, 13, ...

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan melakukan pengurangan dasar (bilangan dua digit). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pola bilangan dengan pengurangan konstan adalah materi standar kelas 4 yang bersifat rutin. |

Run 3 — solusi: Pola bilangan adalah pengurangan 7 secara berulang: 34-7=27, 27-7=20, 20-7=13, 13-7=6.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi aturan pengurangan konstan (pola) dan menerapkannya untuk menemukan suku berikutnya.. Bukti: 34, 27, 20, 13, ...; Tentukan bilangan yang tepat sesuai pola
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang prinsip pola bilangan (pengurangan tetap) yang merupakan konsep dasar dalam aritmatika.. Bukti: 34, 27, 20, 13, ...; pola bilangan
- Intended difficulty `classify/Easy`: Soal ini melibatkan prosedur pengurangan sederhana yang berulang, sangat familiar bagi siswa kelas 4.. Bukti: 34, 27, 20, 13, ...

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
| gradeRelativeRationale | Pola bilangan dengan selisih tetap adalah materi standar kelas 4 yang rutin. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "conceptual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Pola berulang adalah (kupu-kupu, kelinci, kelinci). Urutan yang diberikan berakhir pada kupu-kupu, sehingga elemen berikutnya adalah kelinci.
Gambar sumber: images/kelas2_panduan_siswa_kelas2.pdf-0131-01.png. Transkripsi visual: Baris b menunjukkan urutan gambar: kupu-kupu, kelinci, kelinci, kupu-kupu, kelinci, kelinci, kupu-kupu. Pola berulang adalah (kupu-kupu, kelinci, kelinci). Setelah kupu-kupu, elemen berikutnya dalam pola adalah kelinci.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ca4ab35d2999d7d652c554aac7f36bf09b560c1ff1aac1c8b80693bba610127f`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2570 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2534 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2599 |

Run 1 — solusi: Pola berulang adalah (kupu-kupu, kelinci, kelinci). Urutan yang diberikan berakhir pada kupu-kupu, sehingga elemen berikutnya adalah kelinci.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi unit pengulangan dalam pola visual dan menerapkan aturan tersebut untuk menentukan elemen berikutnya. Ini adalah proses penerapan konsep pola yang rutin.. Bukti: Amati setiap pola berikut (baris b).; pola berulang tiga gambar (kupu-kupu, kelinci, kelinci)
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur pola berulang, yang merupakan konsep dasar dalam matematika pola.. Bukti: Amati setiap pola berikut; pola berulang tiga gambar
- Intended difficulty `classify/Easy`: Soal ini melibatkan pengenalan pola visual sederhana dengan unit pengulangan yang jelas. Tidak ada strategi non-rutin yang diperlukan.. Bukti: Amati setiap pola berikut (baris b).; pola berulang tiga gambar (kupu-kupu, kelinci, kelinci)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengenali urutan visual dan pola berulang sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pola visual berulang adalah materi standar kelas 4 yang bersifat rutin dan langsung. |

Run 2 — solusi: Pola baris b berulang setiap 3 gambar: (kupu-kupu, kelinci, kelinci). Karena urutan terakhir adalah kupu-kupu, maka gambar selanjutnya adalah kelinci.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi aturan pengulangan dalam urutan gambar (pola berulang) dan menerapkan aturan tersebut untuk menentukan elemen berikutnya.. Bukti: Amati setiap pola berikut (baris b).
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur pola berulang, yang merupakan konsep dasar dalam aljabar awal.. Bukti: Amati setiap pola berikut
- Intended difficulty `classify/Easy`: Soal ini melibatkan identifikasi pola visual sederhana yang berulang. Siswa hanya perlu mengenali unit pengulangan dan menerapkannya, yang merupakan tugas rutin bagi siswa kelas 4.. Bukti: Amati setiap pola berikut (baris b).

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengenali urutan dan pengulangan objek visual. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Pola berulang adalah materi dasar yang sudah diperkenalkan sejak kelas rendah, sehingga untuk kelas 4 ini dikategorikan mudah. |

Run 3 — solusi: Pola baris b adalah pengulangan tiga gambar: kupu-kupu, kelinci, kelinci. Karena urutan terakhir adalah kupu-kupu, maka gambar berikutnya adalah kelinci.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi aturan pengulangan dalam urutan visual dan menerapkan aturan tersebut untuk menentukan elemen berikutnya. Ini adalah proses menerapkan konsep pola yang sudah dipelajari.. Bukti: Amati setiap pola berikut (baris b).; pola berulang tiga gambar (kupu-kupu, kelinci, kelinci)
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang struktur pola berulang (konsep), bukan sekadar menghafal fakta atau melakukan prosedur perhitungan.. Bukti: Amati setiap pola berikut; pola berulang tiga gambar
- Intended difficulty `classify/Easy`: Soal ini melibatkan pengenalan pola visual sederhana dengan unit pengulangan yang jelas. Siswa kelas 4 sudah sangat familiar dengan tugas semacam ini.. Bukti: Amati setiap pola berikut (baris b).; pola berulang tiga gambar (kupu-kupu, kelinci, kelinci)

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan mengenali urutan visual dan pola berulang sederhana. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas mengidentifikasi pola visual adalah materi dasar yang sudah dikuasai siswa kelas 4, sehingga tingkat kesulitannya rendah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 131/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000002; applying=0.999998; reasoning=0.000000 | applying | 0.999998 | 0.000028 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.015671; conceptual=0.980097; procedural=0.004231; metacognitive=0.000000 | conceptual | 0.980097 | 0.077875 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.696317; Medium=0.297318; Hard=0.006364 | Easy | 0.696317 | 0.586967 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999998; −Σp ln(p) = 0.000031; H = 0.000031/ln(3) = 0.000028; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.980097; −Σp ln(p) = 0.107957; H = 0.107957/ln(4) = 0.077875; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.696317; −Σp ln(p) = 0.644849; H = 0.644849/ln(3) = 0.586967; T = 0.953328.


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
Transkripsi visual: Baris b menunjukkan urutan gambar: kupu-kupu, kelinci, kelinci, kupu-kupu, kelinci, kelinci, kupu-kupu. Pola berulang adalah (kupu-kupu, kelinci, kelinci). Setelah kupu-kupu, elemen berikutnya dalam pola adalah kelinci.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `4088b8d020de84282c07a2b3`

Sebuah tangki air berisi 2.225 liter air. Pada siang hari 975 liter 325 ml air dipompa keluar dari tangki. Berapa banyak air yang tersisa di tangki?

| Opsi | Isi |
|---|---|
| A | 1.250 liter 675 ml |
| B | 1.249 liter 675 ml |
| C | 1.249 liter 325 ml |
| D | 1.250 liter 325 ml |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: 2.225 liter - 975 liter 325 ml = (2.224 liter + 1.000 ml) - (975 liter + 325 ml) = (2.224 - 975) liter + (1.000 - 325) ml = 1.249 liter 675 ml.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `322d370123711ca6357a7f498488f75a4280986062adf22cb0397eb18ac87a2e`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 1588 |
| 2 | success | valid / verified | applying | procedural | Medium | 1613 |
| 3 | success | valid / verified | applying | procedural | Medium | 1606 |

Run 1 — solusi: 2.225 liter - 975 liter 325 ml = (2.224 liter + 1.000 ml) - (975 liter + 325 ml) = (2.224 - 975) liter + (1.000 - 325) ml = 1.249 liter 675 ml.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pengurangan dengan melakukan konversi satuan (meminjam 1 liter menjadi 1.000 ml) untuk menyelesaikan masalah pengurangan volume yang melibatkan dua satuan berbeda.. Bukti: 975 liter 325 ml air dipompa keluar; Berapa banyak air yang tersisa
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi pengurangan pada satuan volume yang berbeda dan teknik meminjam (regrouping) antar satuan.. Bukti: 2.225 liter; 975 liter 325 ml
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemahaman tentang hubungan antar satuan (1 liter = 1.000 ml) dan prosedur pengurangan dengan teknik meminjam, yang merupakan standar kompetensi kelas 4.. Bukti: 2.225 liter; 975 liter 325 ml

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konversi satuan volume (liter ke ml) dan pengurangan bersusun dengan teknik meminjam. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 4 diharapkan mampu melakukan operasi hitung campuran pada satuan ukuran. Tingkat kesulitan medium karena adanya kebutuhan melakukan konversi satuan saat melakukan pengurangan. |

Run 2 — solusi: 2.225 liter - 975 liter 325 ml = (2.224 liter + 1.000 ml) - (975 liter + 325 ml) = (2.224 - 975) liter + (1.000 - 325) ml = 1.249 liter 675 ml.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pengurangan satuan volume (liter dan mililiter) yang melibatkan teknik meminjam (regrouping) antar satuan, yang merupakan penerapan rutin dari konsep pengukuran.. Bukti: 975 liter 325 ml air dipompa keluar; Berapa banyak air yang tersisa
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut pemahaman tentang algoritma pengurangan dengan satuan campuran dan konversi antar satuan (1 liter = 1.000 ml) untuk menyelesaikan operasi.. Bukti: 2.225 liter; 975 liter 325 ml
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan dua langkah rutin: melakukan pengurangan liter dan melakukan konversi/regrouping satuan mililiter (meminjam 1 liter menjadi 1.000 ml) untuk menyelesaikan pengurangan.. Bukti: 2.225 liter; 975 liter 325 ml; dipompa keluar

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman hubungan 1 liter = 1.000 ml dan pengurangan bersusun. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 4 sudah mempelajari satuan volume dan operasi hitung campuran, namun melakukan pengurangan dengan 'meminjam' antar satuan yang berbeda (liter ke ml) merupakan tantangan prosedural yang sesuai untuk tingkat menengah. |

Run 3 — solusi: 2.225 liter - 975 liter 325 ml = (2.224 liter + 1.000 ml) - (975 liter + 325 ml) = (2.224 - 975) liter + (1.000 - 325) ml = 1.249 liter 675 ml.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pengurangan dengan melakukan konversi satuan (meminjam 1 liter menjadi 1.000 ml) untuk menyelesaikan masalah pengurangan volume yang melibatkan satuan campuran.. Bukti: 2.225 liter; 975 liter 325 ml; Berapa banyak air yang tersisa
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi pengurangan pada satuan volume yang berbeda (liter dan mililiter) yang memerlukan teknik meminjam antar satuan.. Bukti: 2.225 liter; 975 liter 325 ml
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena melibatkan beberapa langkah rutin (pengurangan liter dan pengurangan mililiter) serta memerlukan pemahaman konversi satuan (1 liter = 1.000 ml) saat melakukan pengurangan.. Bukti: 2.225 liter; 975 liter 325 ml

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman hubungan 1 liter = 1.000 ml dan pengurangan bersusun. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Siswa kelas 4 sudah mempelajari satuan volume dan operasi hitung campuran, namun soal ini menuntut ketelitian dalam melakukan konversi satuan saat meminjam. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `637d9aa4ffd7a914baf87306fd234f722237c556326b648eb1fc7c831f985664`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1350 |
| 2 | success | valid / verified | applying | procedural | Easy | 1356 |
| 3 | success | valid / verified | applying | procedural | Easy | 1338 |

Run 1 — solusi: 1 liter = 1.000 ml. Maka 9.485 ml = 9.000 ml + 485 ml = 9 liter + 485 ml.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur konversi satuan volume yang sudah dipelajari (1 liter = 1.000 ml) pada situasi rutin.. Bukti: Konversikan volume berikut ke dalam liter dan mililiter; 9.485 ml
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan antar satuan volume (liter dan mililiter) dan algoritma konversinya.. Bukti: Konversikan volume berikut ke dalam liter dan mililiter
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar yang rutin bagi siswa kelas 4, melibatkan satu keputusan konversi langsung tanpa langkah kompleks.. Bukti: 9.485 ml

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
| gradeRelativeRationale | Konversi satuan volume adalah materi dasar kelas 4 yang bersifat prosedural dan rutin. |

Run 2 — solusi: 1 liter = 1.000 ml. Maka 9.485 ml = 9.000 ml + 485 ml = 9 liter + 485 ml.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur konversi satuan volume standar (ml ke liter) yang merupakan prosedur rutin dalam kurikulum kelas 4.. Bukti: Konversikan volume berikut ke dalam liter dan mililiter; 9.485 ml
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang hubungan antara satuan liter dan mililiter serta algoritma konversi dasar.. Bukti: Konversikan volume berikut ke dalam liter dan mililiter
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dengan satu langkah konversi utama yang familiar bagi siswa kelas 4, menggunakan angka yang tidak memerlukan perhitungan kompleks.. Bukti: 9.485 ml

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dan konversi satuan volume dasar (1 liter = 1.000 ml). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konversi satuan volume adalah materi standar kelas 4. Soal ini langsung menguji pemahaman dasar tanpa jebakan atau langkah ganda yang rumit. |

Run 3 — solusi: 1 liter = 1.000 ml. Maka, 9.485 ml = 9.000 ml + 485 ml = 9 liter + 485 ml.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur konversi satuan volume yang sudah dipelajari (1 liter = 1.000 ml) pada situasi rutin.. Bukti: Konversikan volume berikut ke dalam liter dan mililiter; 9.485 ml
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau teknik konversi satuan volume.. Bukti: Konversikan volume berikut ke dalam liter dan mililiter
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar yang familiar bagi siswa kelas 4, melibatkan satu keputusan konversi utama dengan beban kalkulasi rendah.. Bukti: 9.485 ml

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman hubungan 1 liter = 1.000 ml dan nilai tempat bilangan ribuan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Konversi satuan volume merupakan materi dasar kelas 4 yang bersifat rutin dan langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 12. Soal `1a9d9923445f71c78d74086d`

Sebuah karung berisi 90 kg 460 gram beras dan karung lainnya berisi 25 kg 380 gram beras. Berapa berat beras dalam kedua karung tersebut?

| Opsi | Isi |
|---|---|
| A | 115 kg 840 gram |
| B | 65 kg 840 gram |
| C | 116 kg 840 gram |
| D | 115 kg 740 gram |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: 90 kg + 25 kg = 115 kg; 460 g + 380 g = 840 g. Total: 115 kg 840 g.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d02c7872466548ad1abbecceae8d019ff7e25d78893a814a9cf5d5cbc3e307ad`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1435 |
| 2 | success | valid / verified | applying | procedural | Easy | 1455 |
| 3 | success | valid / verified | applying | procedural | Easy | 1468 |

Run 1 — solusi: 90 kg + 25 kg = 115 kg; 460 g + 380 g = 840 g. Total: 115 kg 840 g.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur penjumlahan pada satuan berat yang berbeda (kg dan gram) dalam situasi rutin.. Bukti: 90 kg 460 gram beras dan karung lainnya berisi 25 kg 380 gram beras; Berapa berat beras dalam kedua karung tersebut?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma penjumlahan bilangan dengan satuan campuran (kg dan gram).. Bukti: 90 kg 460 gram; 25 kg 380 gram
- Intended difficulty `classify/Easy`: Soal ini melibatkan penjumlahan dua besaran dengan satuan campuran yang prosedurnya sudah familiar bagi siswa kelas 4, dengan beban kalkulasi yang rendah.. Bukti: 90 kg 460 gram; 25 kg 380 gram

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah dan pemahaman satuan berat (kg dan gram). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan satuan berat adalah materi standar kelas 4. Prosedur penjumlahan terpisah antara kg dan gram adalah rutin. |

Run 2 — solusi: 90 kg + 25 kg = 115 kg; 460 g + 380 g = 840 g. Total: 115 kg 840 g.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur penjumlahan satuan berat yang sudah dipelajari (kg dan gram) pada situasi rutin.. Bukti: 90 kg 460 gram; 25 kg 380 gram; Berapa berat beras dalam kedua karung tersebut
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma penjumlahan satuan berat (kg dan gram) yang merupakan prosedur standar.. Bukti: 90 kg 460 gram; 25 kg 380 gram
- Intended difficulty `classify/Easy`: Soal ini melibatkan operasi penjumlahan dua satuan yang berbeda namun rutin, dengan beban kognitif rendah karena tidak memerlukan konversi antar satuan yang kompleks.. Bukti: 90 kg 460 gram; 25 kg 380 gram; Berapa berat beras dalam kedua karung tersebut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah dan pemahaman satuan berat (kg, gram). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan satuan berat adalah materi standar kelas 4. Soal ini bersifat langsung tanpa jebakan konversi yang rumit. |

Run 3 — solusi: 90 kg + 25 kg = 115 kg; 460 g + 380 g = 840 g. Total: 115 kg 840 g.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur penjumlahan satuan berat yang sudah dipelajari (kg dan gram) dalam situasi rutin.. Bukti: 90 kg 460 gram beras dan karung lainnya berisi 25 kg 380 gram beras; Berapa berat beras dalam kedua karung tersebut?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma penjumlahan satuan berat yang terpisah (kg dan gram), yang merupakan prosedur standar.. Bukti: 90 kg 460 gram; 25 kg 380 gram
- Intended difficulty `classify/Easy`: Soal ini melibatkan operasi penjumlahan dua satuan yang berbeda namun tidak memerlukan konversi antar satuan (karena jumlah gram < 1000), sehingga prosedurnya langsung.. Bukti: 90 kg 460 gram; 25 kg 380 gram; Berapa berat beras dalam kedua karung tersebut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah dan pemahaman satuan berat (kg, gram). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 sudah terbiasa dengan operasi penjumlahan bilangan dan pengenalan satuan berat baku. |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Menghitung kepingan berdasarkan bentuk: 5 segitiga (biru, merah, hijau tua, oranye, merah muda), 1 persegi (hijau muda), dan 1 jajargenjang (kuning). Total 7 keping.
Gambar sumber: images/kelas4_panduan_siswa_kelas4.pdf-0184-10.png. Transkripsi visual: Gambar menunjukkan sebuah perahu yang tersusun dari 7 keping bangun datar berwarna: 1 segitiga biru besar, 1 segitiga merah besar, 1 segitiga hijau tua, 1 segitiga oranye, 1 segitiga merah muda, 1 persegi hijau muda, dan 1 jajargenjang kuning.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `2b07bfd8c62e3cd843014833d9a84455bbeef36a34c8be8f46d610cb947192d6`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2602 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2680 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2671 |

Run 1 — solusi: Menghitung jumlah kepingan berdasarkan bentuk geometrisnya: 5 segitiga, 1 persegi, dan 1 jajargenjang.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dan mengklasifikasikan bentuk geometris dari komponen penyusun gambar, yang merupakan proses pengenalan dan penerapan konsep dasar bangun datar.. Bukti: Tentukan dekomposisi berbagai macam bangun datar
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang kategori bangun datar (segitiga, persegi, jajargenjang) dan bagaimana mereka menyusun sebuah bentuk yang lebih besar.. Bukti: dekomposisi berbagai macam bangun datar
- Intended difficulty `classify/Easy`: Soal ini meminta siswa melakukan observasi visual dan klasifikasi bentuk sederhana. Tingkat kesulitannya rendah karena hanya memerlukan pengenalan bentuk dasar pada tangram.. Bukti: Tentukan dekomposisi berbagai macam bangun datar yang ada pada gambar

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal sifat-sifat dasar bangun datar (segitiga, persegi, jajargenjang). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 sudah familiar dengan tangram dan klasifikasi bangun datar sederhana. Tugas ini bersifat langsung tanpa memerlukan perhitungan kompleks. |

Run 2 — solusi: Menghitung jumlah keping berdasarkan bentuk geometris: 5 segitiga (biru, merah, hijau tua, oranye, merah muda), 1 persegi (hijau muda), dan 1 jajargenjang (kuning).
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dan mengklasifikasikan bentuk geometris dari komponen penyusun gambar kompleks (tangram), yang merupakan proses penerapan konsep bangun datar pada situasi visual.. Bukti: Tentukan dekomposisi berbagai macam bangun datar yang ada pada gambar
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang struktur dan kategori bangun datar (segitiga, persegi, jajargenjang) dalam konteks komposisi bentuk.. Bukti: dekomposisi berbagai macam bangun datar
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena siswa harus melakukan dekomposisi visual pada gambar yang terdiri dari beberapa bagian, membedakan bentuk yang mirip (seperti jajargenjang vs trapesium), dan menghitung jumlah masing-masing bentuk dengan teliti.. Bukti: Tentukan dekomposisi berbagai macam bangun datar yang ada pada gambar

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal sifat-sifat dasar bangun datar (segitiga, persegi, jajargenjang). |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 7 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 diharapkan mampu mengidentifikasi bangun datar sederhana dalam komposisi yang lebih kompleks seperti tangram. |

Run 3 — solusi: Perahu terdiri dari 7 keping: 5 segitiga (biru, merah, hijau tua, oranye, merah muda), 1 persegi (hijau muda), dan 1 jajargenjang (kuning). Pilihan D sesuai dengan hitungan ini.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dan mengklasifikasikan bentuk geometris individual yang menyusun gambar kompleks (dekomposisi). Ini melibatkan pengenalan sifat bangun datar.. Bukti: Tentukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut
- Dimensi pengetahuan `classify/conceptual`: Siswa menerapkan pengetahuan konseptual tentang sifat-sifat bangun datar (segitiga, persegi, jajargenjang) untuk mengkategorikan bagian-bagian dari gambar.. Bukti: Tentukan dekomposisi berbagai macam bangun datar
- Intended difficulty `classify/Easy`: Soal ini meminta siswa untuk melakukan dekomposisi visual yang memerlukan ketelitian dalam mengenali bentuk, namun prosedurnya bersifat rutin bagi siswa kelas 4 yang sudah mempelajari tangram atau komposisi bangun datar.. Bukti: Tentukan dekomposisi berbagai macam bangun datar yang ada pada gambar berikut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal sifat-sifat bangun datar dasar (segitiga, persegi, jajargenjang). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 diharapkan mampu mengidentifikasi bentuk-bentuk geometris dasar dalam komposisi visual sederhana. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 2, "Medium": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `4046`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan pengetahuan tentang sifat-sifat bangun datar untuk mengidentifikasi dan mengklasifikasikan setiap komponen penyusun gambar (tangram). Ini adalah proses penerapan konsep pada situasi visual.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang kategori bangun datar (segitiga, persegi, jajargenjang) dan bagaimana mereka membentuk struktur yang lebih besar.
- Intended difficulty `Easy`: Tugas ini bersifat rutin bagi siswa kelas 4 yang sudah mempelajari tangram. Tidak ada perhitungan kompleks, hanya observasi visual dan klasifikasi bentuk dasar.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal sifat-sifat dasar bangun datar (segitiga, persegi, jajargenjang). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 7 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 sudah familiar dengan tangram dan klasifikasi bangun datar sederhana. Tugas ini bersifat langsung tanpa memerlukan perhitungan kompleks. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 219/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.408054; applying=0.591946; reasoning=0.000000 | applying | 0.591946 | 0.615452 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.019820; conceptual=0.971023; procedural=0.009158; metacognitive=0.000000 | conceptual | 0.971023 | 0.107658 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.713617; Medium=0.277480; Hard=0.008903 | Easy | 0.713617 | 0.581228 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.591946; −Σp ln(p) = 0.676143; H = 0.676143/ln(3) = 0.615452; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.971023; −Σp ln(p) = 0.149245; H = 0.149245/ln(4) = 0.107658; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.713617; −Σp ln(p) = 0.638545; H = 0.638545/ln(3) = 0.581228; T = 0.953328.


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
Transkripsi visual: Gambar menunjukkan sebuah perahu yang tersusun dari 7 keping bangun datar berwarna: 1 segitiga biru besar, 1 segitiga merah besar, 1 segitiga hijau tua, 1 segitiga oranye, 1 segitiga merah muda, 1 persegi hijau muda, dan 1 jajargenjang kuning.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Dengan mengamati sifat sudut dan sisi setiap keping, motif tersebut terdiri dari segitiga siku-siku, persegi, jajargenjang, dan trapesium. Pilihan D mencakup semua jenis bangun tersebut secara akurat.
Gambar sumber: images/kelas4_panduan_siswa_kelas4.pdf-0185-06.png. Transkripsi visual: Gambar menunjukkan motif paving berbentuk persegi panjang besar yang terbagi menjadi beberapa bangun datar kecil berwarna hijau dengan garis pembatas putih. Bangun-bangun tersebut meliputi: segitiga siku-siku (di sudut kiri atas, kiri bawah, dan tengah), persegi (di bagian kanan dan miring di tengah), jajargenjang (di bagian tengah kiri dan bawah tengah), serta trapesium (di bagian kanan atas dan kanan bawah).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `85d38c178175330607c5502de2e06c47709ec023d4181614fbfe8bd94470bdba`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2706 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2704 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2686 |

Run 1 — solusi: Dengan mengamati sifat sudut dan sisi setiap keping, motif tersebut terdiri dari segitiga siku-siku, persegi, jajargenjang, dan trapesium. Pilihan D mencakup semua jenis bangun tersebut secara akurat.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dan mengklasifikasikan berbagai bentuk geometris berdasarkan sifat visualnya (sudut dan sisi) dari sebuah komposisi yang kompleks.. Bukti: apa saja bangun datar yang menyusun motif paving di atas?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang sifat-sifat bangun datar dan bagaimana mereka dapat disusun atau didekomposisi menjadi bentuk-bentuk yang lebih sederhana.. Bukti: Lakukan dekomposisi berbagai macam bangun datar
- Intended difficulty `classify/Medium`: Soal ini memerlukan kemampuan visualisasi spasial untuk membedakan berbagai bentuk yang saling berhimpitan. Meskipun prosedurnya langsung (mengidentifikasi), kompleksitas visual motif membuat tingkat kesulitannya menengah bagi siswa kelas 4.. Bukti: apa saja bangun datar yang menyusun motif paving di atas?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang sifat-sifat bangun datar (segitiga siku-siku, persegi, jajargenjang, trapesium). |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 sudah mempelajari klasifikasi bangun datar, namun melakukan dekomposisi pada gambar komposit yang cukup padat memerlukan ketelitian lebih tinggi daripada sekadar mengenali bangun tunggal. |

Run 2 — solusi: Dengan mengamati sifat sudut dan sisi setiap kepingan pada gambar, terlihat jelas adanya segitiga siku-siku, persegi, jajargenjang, dan trapesium. Pilihan D mencantumkan semua jenis bangun tersebut dengan tepat.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dan mengklasifikasikan bentuk-bentuk geometris berdasarkan sifat visualnya (jumlah sisi, jenis sudut) dari sebuah komposisi bangun datar yang kompleks.. Bukti: apa saja bangun datar yang menyusun motif paving di atas?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang sifat-sifat bangun datar dan bagaimana bangun-bangun tersebut menyusun suatu bentuk yang lebih besar.. Bukti: Lakukan dekomposisi berbagai macam bangun datar
- Intended difficulty `classify/Medium`: Soal ini memerlukan ketelitian visual untuk membedakan bentuk yang mirip (seperti jajargenjang vs trapesium) dalam komposisi yang padat, yang merupakan tantangan menengah bagi siswa kelas 4.. Bukti: apa saja bangun datar yang menyusun motif paving di atas?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang sifat-sifat bangun datar (segitiga siku-siku, persegi, jajargenjang, trapesium). |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 sudah mempelajari sifat bangun datar, namun melakukan dekomposisi pada gambar yang kompleks memerlukan kemampuan analisis visual yang lebih tinggi daripada sekadar mengenali bentuk tunggal. |

Run 3 — solusi: Mengamati gambar secara visual menunjukkan adanya bangun segitiga siku-siku, persegi, jajargenjang, dan trapesium yang menyusun motif tersebut. Pilihan D mencakup semua jenis bangun yang terlihat.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi dan membedakan berbagai bentuk geometri (segitiga siku-siku, persegi, jajargenjang, trapesium) dari komposisi visual yang diberikan. Ini adalah proses menerapkan pemahaman konsep bentuk ke situasi visual.. Bukti: apa saja bangun datar yang menyusun motif paving di atas?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang karakteristik dan klasifikasi bangun datar (konsep) yang menyusun sebuah pola.. Bukti: dekomposisi berbagai macam bangun datar
- Intended difficulty `classify/Medium`: Soal ini memerlukan kemampuan observasi visual yang cermat untuk membedakan bentuk-bentuk yang mirip (seperti membedakan jajargenjang dan trapesium) dalam komposisi yang kompleks. Tingkat kesulitan ini sesuai untuk kelas 4.. Bukti: apa saja bangun datar yang menyusun motif paving di atas?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang sifat-sifat bangun datar (segitiga siku-siku, persegi, jajargenjang, trapesium). |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 4 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 diharapkan mampu mengidentifikasi bangun datar sederhana. Kompleksitas terletak pada banyaknya bentuk yang saling berhimpitan, menuntut ketelitian visual. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 219/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000117; applying=0.999883; reasoning=0.000000 | applying | 0.999883 | 0.001068 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.013849; conceptual=0.970017; procedural=0.016135; metacognitive=0.000000 | conceptual | 0.970017 | 0.112083 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.782363; Medium=0.211200; Hard=0.006438 | Easy | 0.782363 | 0.503279 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999883; −Σp ln(p) = 0.001174; H = 0.001174/ln(3) = 0.001068; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.970017; −Σp ln(p) = 0.155380; H = 0.155380/ln(4) = 0.112083; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.782363; −Σp ln(p) = 0.552909; H = 0.552909/ln(3) = 0.503279; T = 0.953328.


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
Transkripsi visual: Gambar menunjukkan motif paving berbentuk persegi panjang besar yang terbagi menjadi beberapa bangun datar kecil berwarna hijau dengan garis pembatas putih. Bangun-bangun tersebut meliputi: segitiga siku-siku (di sudut kiri atas, kiri bawah, dan tengah), persegi (di bagian kanan dan miring di tengah), jajargenjang (di bagian tengah kiri dan bawah tengah), serta trapesium (di bagian kanan atas dan kanan bawah).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Analisis sifat geometris huruf: E memiliki 3 pasang garis sejajar dan 3 pasang tegak lurus. M memiliki 1 pasang garis sejajar, 0 tegak lurus. T memiliki 0 pasang garis sejajar, 1 pasang tegak lurus. Tidak ada huruf yang memenuhi kriteria 1 pasang sejajar dan 2 pasang tegak lurus.
Gambar sumber: images/kelas3_panduan_siswa_kelas3.pdf-0198-01.png. Transkripsi visual: Gambar menunjukkan huruf-huruf M, A, T, E, M, A, T, I, K, A yang digambar di atas kertas berpetak. Huruf E memiliki 3 garis horizontal sejajar dan 3 garis tegak lurus terhadap garis horizontal tersebut. Huruf M memiliki 2 garis vertikal sejajar. Huruf T memiliki 1 garis horizontal dan 1 garis vertikal yang saling tegak lurus.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6e191a54fb4cf26825caad0e07b587d7599829131b36496ddc4126ced4c6d210`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2734 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2739 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2736 |

Run 1 — solusi: Analisis sifat geometris huruf: E memiliki 3 pasang garis sejajar dan 3 pasang tegak lurus. M memiliki 1 pasang garis sejajar, 0 tegak lurus. T memiliki 0 pasang garis sejajar, 1 pasang tegak lurus. Tidak ada huruf yang memenuhi kriteria 1 pasang sejajar dan 2 pasang tegak lurus.
- Domain kognitif `classify/applying`: Siswa perlu menganalisis properti geometris dari setiap huruf (sejajar dan tegak lurus) dan membandingkannya dengan kriteria yang diberikan, yang merupakan proses applying konsep pada situasi visual.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang definisi dan identifikasi garis sejajar dan tegak lurus pada bentuk geometris.. Bukti: Garis-Garis Tegak Lurus dan Garis-Garis Sejajar
- Intended difficulty `classify/Medium`: Soal ini memerlukan analisis visual yang cermat terhadap beberapa objek (huruf) dan verifikasi kondisi ganda (sejajar dan tegak lurus) secara simultan, yang menuntut lebih dari sekadar pengenalan dasar.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang garis sejajar dan tegak lurus. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 4, mengidentifikasi sifat garis pada huruf memerlukan ketelitian visual dan pemahaman konsep yang cukup untuk membedakan antara berbagai konfigurasi garis. |

Run 2 — solusi: Analisis huruf: E memiliki 3 pasang garis sejajar dan 4 pasang garis tegak lurus. M memiliki 1 pasang garis sejajar (vertikal) dan tidak ada garis tegak lurus. T memiliki 1 pasang garis tegak lurus dan tidak ada garis sejajar. Tidak ada huruf yang memenuhi syarat 1 pasang sejajar dan 2 pasang tegak lurus.
- Domain kognitif `classify/applying`: Siswa perlu menganalisis properti geometris dari setiap huruf (sejajar dan tegak lurus) dan membandingkannya dengan kriteria yang diberikan. Ini melibatkan penerapan konsep pada situasi visual.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?
- Dimensi pengetahuan `classify/conceptual`: Soal menguji pemahaman tentang definisi dan karakteristik garis sejajar dan tegak lurus dalam bentuk huruf, yang merupakan konsep geometris dasar.. Bukti: Garis-Garis Tegak Lurus dan Garis-Garis Sejajar
- Intended difficulty `classify/Medium`: Soal ini memerlukan analisis visual yang cermat terhadap beberapa objek (huruf) dan verifikasi kondisi ganda (sejajar dan tegak lurus). Ini lebih kompleks daripada sekadar mengidentifikasi satu jenis garis.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman definisi garis sejajar dan tegak lurus serta kemampuan mengidentifikasinya pada objek visual. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 4, mengidentifikasi sifat garis pada huruf adalah tugas standar, namun menuntut ketelitian dalam memeriksa kondisi ganda pada setiap opsi, sehingga dikategorikan Medium. |

Run 3 — solusi: Analisis geometri huruf: E memiliki 3 garis sejajar dan 3 pasang tegak lurus. M memiliki 1 pasang garis sejajar, 0 tegak lurus. T memiliki 0 pasang garis sejajar, 1 pasang tegak lurus. Tidak ada huruf yang memenuhi kriteria 1 pasang sejajar dan 2 pasang tegak lurus.
- Domain kognitif `classify/applying`: Siswa harus menganalisis properti geometris dari setiap huruf (sejajar dan tegak lurus) dan membandingkannya dengan kriteria yang diberikan, yang merupakan proses applying konsep pada situasi visual.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang definisi dan identifikasi hubungan antar garis (sejajar dan tegak lurus) yang merupakan konsep dasar geometri.. Bukti: Garis-Garis Tegak Lurus dan Garis-Garis Sejajar
- Intended difficulty `classify/Medium`: Soal ini memerlukan analisis visual yang cermat terhadap beberapa objek (huruf) dan verifikasi kondisi ganda (sejajar dan tegak lurus), yang sedikit lebih kompleks daripada sekadar identifikasi satu properti.. Bukti: Huruf manakah yang hanya memiliki satu pasang garis sejajar dan dua pasang garis tegak lurus?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman definisi garis sejajar dan tegak lurus pada bidang datar. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 diharapkan mampu mengidentifikasi hubungan garis pada bentuk geometris sederhana. Soal ini menuntut ketelitian dalam memeriksa setiap huruf terhadap dua kriteria sekaligus. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 153/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000024; applying=0.999976; reasoning=0.000000 | applying | 0.999976 | 0.000258 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.012056; conceptual=0.967417; procedural=0.020527; metacognitive=0.000000 | conceptual | 0.967417 | 0.119081 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.714899; Medium=0.280493; Hard=0.004608 | Easy | 0.714899 | 0.565517 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999976; −Σp ln(p) = 0.000283; H = 0.000283/ln(3) = 0.000258; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.967417; −Σp ln(p) = 0.165081; H = 0.165081/ln(4) = 0.119081; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.714899; −Σp ln(p) = 0.621284; H = 0.621284/ln(3) = 0.565517; T = 0.953328.


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
Transkripsi visual: Gambar menunjukkan huruf-huruf M, A, T, E, M, A, T, I, K, A yang digambar di atas kertas berpetak. Huruf E memiliki 3 garis horizontal sejajar dan 3 garis tegak lurus terhadap garis horizontal tersebut. Huruf M memiliki 2 garis vertikal sejajar. Huruf T memiliki 1 garis horizontal dan 1 garis vertikal yang saling tegak lurus.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Jumlah siswa kelas 1, 3, 4, 5, dan 6 adalah 57 + 58 + 56 + 62 + 59 = 292. Jumlah siswa kelas 2 adalah total siswa dikurangi jumlah kelas lainnya: 346 - 292 = 54.
Gambar sumber: images/kelas4_panduan_guru_kelas4.pdf-0244-06.png. Transkripsi visual: Diagram batang menunjukkan jumlah siswa per kelas: Kelas 1=57, Kelas 3=58, Kelas 4=56, Kelas 5=62, Kelas 6=59. Batang untuk Kelas 2 tidak ada (kosong). Total siswa seluruh sekolah adalah 346.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `['mengidentifikasi']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `0d9c46e259c0b139cce9276194acf324d797a497b3ed178b75e756d2fb082742`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Medium | 2733 |
| 2 | success | valid / verified | applying | procedural | Medium | 2683 |
| 3 | success | valid / verified | applying | procedural | Medium | 2691 |

Run 1 — solusi: Jumlah siswa kelas 1, 3, 4, 5, dan 6 adalah 57 + 58 + 56 + 62 + 59 = 292. Jumlah siswa kelas 2 adalah total siswa dikurangi jumlah kelas lainnya: 346 - 292 = 54.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan informasi dari diagram batang dengan informasi teks (total siswa) untuk menyimpulkan nilai yang hilang. Ini melibatkan pemahaman hubungan bagian-keseluruhan, bukan sekadar membaca data langsung.. Bukti: Apabila jumlah seluruh siswa di SD Permata adalah 346 siswa. Tentukan: Banyak siswa kelas 2 SD Permata?
- Dimensi pengetahuan `classify/procedural`: Soal ini menuntut penggunaan algoritma penjumlahan dan pengurangan (prosedural) untuk menyelesaikan masalah yang berbasis pada pemahaman konsep diagram batang (konseptual).. Bukti: Diagram batang berikut menunjukan banyak siswa di SD Permata.; 346 - 292 = 54
- Intended difficulty `classify/Medium`: Soal ini dikategorikan Medium karena memerlukan beberapa langkah rutin yang terkait (penjumlahan data yang ada, lalu pengurangan dari total) dan menuntut siswa untuk menyadari bahwa batang yang kosong mewakili data yang harus dicari.. Bukti: 57 + 58 + 56 + 62 + 59 = 292; 346 - 292 = 54

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah hingga ratusan, pengurangan dengan meminjam, dan pembacaan diagram batang sederhana. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk kelas 4, melakukan operasi penjumlahan beruntun dan pengurangan dengan total yang diberikan adalah tugas yang sesuai dengan tingkat perkembangan kognitif mereka. |

Run 2 — solusi: Jumlah siswa kelas 1, 3, 4, 5, dan 6 adalah 57 + 58 + 56 + 62 + 59 = 292. Jumlah siswa kelas 2 = Total - Jumlah kelas lain = 346 - 292 = 54.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan informasi dari diagram batang (penjumlahan data yang ada) dan menerapkan konsep pengurangan untuk menemukan nilai yang hilang dari total yang diketahui.. Bukti: Apabila jumlah seluruh siswa di SD Permata adalah 346 siswa. Tentukan: Banyak siswa kelas 2 SD Permata?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur aritmatika (penjumlahan dan pengurangan) untuk menyelesaikan masalah yang melibatkan interpretasi data.. Bukti: Diagram batang berikut menunjukan banyak siswa di SD Permata.; 346 - 292 = 54
- Intended difficulty `classify/Medium`: Soal ini memerlukan beberapa langkah rutin (menjumlahkan 5 data, lalu mengurangkan dari total). Ini adalah tugas standar untuk kelas 4.. Bukti: 57 + 58 + 56 + 62 + 59 = 292; 346 - 292 = 54

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah hingga ratusan dan pemahaman dasar diagram batang. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 diharapkan mampu melakukan operasi penjumlahan dan pengurangan bilangan tiga angka serta membaca data dari diagram batang. |

Run 3 — solusi: Jumlah siswa kelas 1, 3, 4, 5, dan 6 adalah 57 + 58 + 56 + 62 + 59 = 292. Jumlah siswa kelas 2 adalah total siswa dikurangi jumlah siswa kelas lainnya: 346 - 292 = 54.
- Domain kognitif `classify/applying`: Siswa perlu mengintegrasikan informasi dari diagram (membaca data) dengan informasi teks (total) untuk menyimpulkan nilai yang hilang. Ini melibatkan lebih dari sekadar membaca data langsung.. Bukti: Apabila jumlah seluruh siswa di SD Permata adalah 346 siswa. Tentukan: Banyak siswa kelas 2 SD Permata?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan prosedur aritmatika (penjumlahan dan pengurangan) untuk menyelesaikan masalah yang terstruktur dalam konteks diagram batang.. Bukti: Diagram batang berikut menunjukan banyak siswa di SD Permata.; 346 - 292 = 54
- Intended difficulty `classify/Medium`: Soal ini memerlukan dua tahap perhitungan rutin (penjumlahan data yang ada, lalu pengurangan dari total). Ini adalah tugas standar untuk kelas 4.. Bukti: 57 + 58 + 56 + 62 + 59 = 292; 346 - 292 = 54

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan bilangan cacah dan pemahaman dasar diagram batang. |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 1 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 diharapkan mampu melakukan operasi penjumlahan dan pengurangan bilangan tiga angka serta menginterpretasikan data dari grafik sederhana. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 132/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000000 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.043494; conceptual=0.947174; procedural=0.009333; metacognitive=0.000000 | conceptual | 0.947174 | 0.166911 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.759152; Medium=0.234894; Hard=0.005955 | Easy | 0.759152 | 0.527911 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000000; H = 0.000000/ln(3) = 0.000000; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.947174; −Σp ln(p) = 0.231388; H = 0.231388/ln(4) = 0.166911; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.759152; −Σp ln(p) = 0.579969; H = 0.579969/ln(3) = 0.527911; T = 0.953328.


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
Transkripsi visual: Diagram batang menunjukkan jumlah siswa per kelas: Kelas 1=57, Kelas 3=58, Kelas 4=56, Kelas 5=62, Kelas 6=59. Batang untuk Kelas 2 tidak ada (kosong). Total siswa seluruh sekolah adalah 346.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Medium"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

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
Solusi minimum hasil AI: Mengamati panjang batang pada diagram. Batang untuk 'Renang' adalah yang paling pendek, sejajar dengan angka 2 pada sumbu horizontal, yang merupakan nilai terkecil dibandingkan kategori lainnya.
Gambar sumber: images/kelas4_panduan_siswa_kelas4.pdf-0205-08.png. Transkripsi visual: Diagram batang horizontal menunjukkan data lomba: Menyanyi (8 siswa), Renang (2 siswa), Bulu Tangkis (5 siswa), Puisi (7 siswa), Lari (3 siswa), Catur (5 siswa). Sumbu horizontal menunjukkan 'Banyak Siswa' dari 0 sampai 9.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `58eeeecab1a31f0ac4775de29b14e96e3c169174d5960d4c514de3005cef0684`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 3502 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2485 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2438 |

Run 1 — solusi: Membandingkan panjang batang pada diagram. Batang 'Renang' adalah yang paling pendek dengan nilai 2, yang merupakan nilai terkecil di antara semua kategori.
- Domain kognitif `classify/applying`: Siswa diminta untuk membaca dan membandingkan data visual secara langsung untuk menentukan nilai minimum.. Bukti: Lomba apakah yang paling sedikit diikuti siswa?; Batang Renang paling pendek, yaitu 2 siswa.
- Dimensi pengetahuan `classify/conceptual`: Memerlukan pemahaman tentang bagaimana panjang batang merepresentasikan kuantitas data.. Bukti: Diberikan diagram batang untuk data siswa
- Intended difficulty `classify/Easy`: Tugas ini bersifat rutin dan langsung, hanya memerlukan perbandingan visual sederhana tanpa perhitungan kompleks.. Bukti: Lomba apakah yang paling sedikit diikuti siswa?

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
| gradeRelativeRationale | Sesuai untuk kelas 4 karena merupakan keterampilan dasar dalam interpretasi data. |

Run 2 — solusi: Membandingkan panjang batang pada diagram. Batang 'Renang' adalah yang paling pendek, dengan nilai 2, yang merupakan nilai terkecil di antara semua kategori.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data secara langsung dari diagram batang dan membandingkan panjang batang untuk menentukan nilai terkecil. Ini adalah proses pengenalan data visual yang sangat langsung.. Bukti: Lomba apakah yang paling sedikit diikuti siswa?; Batang Renang paling pendek, yaitu 2 siswa.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang cara membaca diagram batang sebagai representasi data, yang merupakan pengetahuan konseptual dasar tentang grafik.. Bukti: Diberikan diagram batang untuk data siswa
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana karena hanya memerlukan observasi visual langsung terhadap panjang batang untuk menentukan nilai minimum tanpa perhitungan atau manipulasi data.. Bukti: Lomba apakah yang paling sedikit diikuti siswa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca diagram batang sederhana dan membandingkan bilangan cacah. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 6 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 4 sudah sangat familiar dengan interpretasi diagram batang sederhana. Soal ini tidak menuntut analisis kompleks. |

Run 3 — solusi: Membandingkan panjang batang pada diagram: Renang memiliki batang terpendek yang sejajar dengan angka 2 pada sumbu horizontal, yang merupakan nilai terkecil dibandingkan lomba lainnya.
- Domain kognitif `classify/knowing`: Siswa hanya perlu membaca data secara langsung dari diagram batang dan membandingkan nilai untuk menemukan nilai minimum.. Bukti: Lomba apakah yang paling sedikit diikuti siswa?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman dasar tentang cara membaca dan menginterpretasikan informasi yang disajikan dalam bentuk diagram batang.. Bukti: Diberikan diagram batang untuk data siswa
- Intended difficulty `classify/Easy`: Soal ini sangat langsung, hanya memerlukan identifikasi visual sederhana tanpa perhitungan kompleks atau manipulasi data.. Bukti: Lomba apakah yang paling sedikit diikuti siswa?

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
| gradeRelativeRationale | Siswa kelas 4 sudah terbiasa membaca data dari diagram batang sederhana sebagai bagian dari kurikulum dasar statistika. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 1, "knowing": 2} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3601`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu melakukan observasi visual langsung untuk membandingkan panjang batang dan mengidentifikasi nilai minimum. Ini adalah proses pengenalan data visual yang sangat langsung.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman dasar tentang bagaimana panjang batang dalam diagram merepresentasikan kuantitas data.
- Intended difficulty `Easy`: Soal ini sangat sederhana karena hanya memerlukan observasi visual langsung terhadap panjang batang untuk menentukan nilai minimum tanpa perhitungan atau manipulasi data.

Profil difficulty hasil adjudikasi:

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
| gradeRelativeRationale | Siswa kelas 4 sudah sangat familiar dengan interpretasi diagram batang sederhana sebagai bagian dari kurikulum dasar statistika. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 124/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000000 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.044880; conceptual=0.949069; procedural=0.006052; metacognitive=0.000000 | conceptual | 0.949069 | 0.158563 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.781381; Medium=0.214434; Hard=0.004185 | Easy | 0.781381 | 0.496858 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000000; H = 0.000000/ln(3) = 0.000000; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.949069; −Σp ln(p) = 0.219815; H = 0.219815/ln(4) = 0.158563; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.781381; −Σp ln(p) = 0.545855; H = 0.545855/ln(3) = 0.496858; T = 0.953328.


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
Transkripsi visual: Diagram batang horizontal menunjukkan data lomba: Menyanyi (8 siswa), Renang (2 siswa), Bulu Tangkis (5 siswa), Puisi (7 siswa), Lari (3 siswa), Catur (5 siswa). Sumbu horizontal menunjukkan 'Banyak Siswa' dari 0 sampai 9.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `631ea2e9a2d5222d502bdf5c`

Hasil penilaian harian Matematika diperoleh: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10<br><br>Berapa banyak siswa yang mendapatkan nilai lebih dari 7?

| Opsi | Isi |
|---|---|
| A | 12 siswa |
| B | 8 siswa |
| C | 15 siswa |
| D | 10 siswa |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Data: 9, 8, 8, 5, 9, 6, 10, 9, 8, 6, 7, 8, 9, 9, 5, 6, 7, 7, 9, 10. Nilai > 7 adalah 8, 9, 10. Frekuensi 8 ada 4, 9 ada 6, 10 ada 2. Total = 4 + 6 + 2 = 12.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 4 / Matematika SD Kelas 4. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4c5933e97ee282a1f9476d48b294041a5c3b00c83479beca49f33db0dd0bf2dd`. Bukti verifikasi AI tidak sama dengan verifikasi ahli.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1523 |
| 2 | success | valid / verified | applying | procedural | Easy | 1523 |
| 3 | success | valid / verified | applying | procedural | Easy | 1508 |

Run 1 — solusi: Data: 9, 8, 8, 5, 9, 6, 10, 9, 8, 6, 7, 8, 9, 9, 5, 6, 7, 7, 9, 10. Nilai > 7 adalah 8, 9, 10. Frekuensi 8 ada 4, 9 ada 6, 10 ada 2. Total = 4 + 6 + 2 = 12.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi nilai yang memenuhi kriteria (lebih dari 7) dan menghitung frekuensinya dari data yang diberikan. Ini adalah penerapan prosedur rutin dalam pengolahan data.. Bukti: Berapa banyak siswa yang mendapatkan nilai lebih dari 7?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan teknik penghitungan (counting) dan pengelompokan data untuk menjawab pertanyaan, yang merupakan prosedur standar dalam statistika dasar.. Bukti: Hasil penilaian harian Matematika diperoleh: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10
- Intended difficulty `classify/Easy`: Soal ini melibatkan pengolahan data sederhana dengan kriteria yang jelas. Siswa hanya perlu melakukan klasifikasi dan penjumlahan sederhana.. Bukti: Berapa banyak siswa yang mendapatkan nilai lebih dari 7?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan bilangan dan menghitung frekuensi data. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 20 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 4 SD karena melibatkan pengolahan data mentah sederhana yang merupakan materi dasar statistika di jenjang tersebut. |

Run 2 — solusi: Data: 9, 8, 8, 5, 9, 6, 10, 9, 8, 6, 7, 8, 9, 9, 5, 6, 7, 7, 9, 10. Nilai > 7 adalah 8, 9, dan 10. Frekuensi: nilai 8 ada 4, nilai 9 ada 6, nilai 10 ada 2. Total = 4 + 6 + 2 = 12.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi nilai yang memenuhi kriteria (>7) dan menghitung frekuensinya dari data yang diberikan. Ini adalah penerapan prosedur rutin dalam pengolahan data.. Bukti: Berapa banyak siswa yang mendapatkan nilai lebih dari 7?
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan teknik penghitungan (counting) dan pengelompokan data untuk menyelesaikan masalah.. Bukti: Hasil penilaian harian Matematika diperoleh: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10
- Intended difficulty `classify/Easy`: Soal ini melibatkan pengolahan data sederhana yang rutin bagi siswa kelas 4. Langkah-langkahnya jelas dan tidak memerlukan strategi kompleks.. Bukti: Berapa banyak siswa yang mendapatkan nilai lebih dari 7?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan bilangan dan menghitung frekuensi data. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 20 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 4 karena melibatkan pengolahan data dasar yang merupakan standar kompetensi di jenjang tersebut. |

Run 3 — solusi: Data: 9, 8, 8, 5, 9, 6, 10, 9, 8, 6, 7, 8, 9, 9, 5, 6, 7, 7, 9, 10. Nilai > 7 adalah 8, 9, 10. Frekuensi: 8 ada 4, 9 ada 6, 10 ada 2. Total = 4 + 6 + 2 = 12.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi nilai yang memenuhi kriteria (>7) dan menghitung frekuensinya dari kumpulan data yang diberikan. Ini adalah penerapan prosedur rutin dalam pengolahan data sederhana.. Bukti: Berapa banyak siswa yang mendapatkan nilai lebih dari 7?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang bagaimana mengorganisasi dan menghitung frekuensi data mentah, yang merupakan bagian dari prosedur statistik dasar.. Bukti: Hasil penilaian harian Matematika diperoleh: 9 8 8 5 9 6 10 9 8 6 7 8 9 9 5 6 7 7 9 10
- Intended difficulty `classify/Easy`: Tugas ini melibatkan pengelompokan data dan penjumlahan sederhana. Siswa kelas 4 diharapkan mampu melakukan ini dengan teliti.. Bukti: Berapa banyak siswa yang mendapatkan nilai lebih dari 7?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan bilangan dan menghitung frekuensi data sederhana. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 20 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 4 karena melibatkan pengolahan data mentah yang merupakan standar kompetensi dasar pengumpulan dan penyajian data. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

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

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `pending_expert_review`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Gold ahli tetap null; human review wajib. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
