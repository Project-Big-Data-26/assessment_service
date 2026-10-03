# Validasi ulang soal kelas 1 — Gemini blind N=3 dan diagnostik IndoBERT

Model penilai: `gemini-3.1-flash-lite`. Prompt: `gemini-silver-math-3x4x3-v4-blind-key-verified`. Rubrik: `math-rubric-3x4x3-v2-grade-aware`.

Ketiga run menilai soal beserta gambar, kunci sumber, dan rubrik kelas 1 tanpa menerima prediksi IndoBERT. Keputusan awal 3–0 diterima sebagai silver; ketidaksepakatan, abstention, dan persoalan konten diperiksa dalam adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama dan menjadi keputusan silver operasional.

Checkpoint dikunci dengan SHA-256 sebelum inferensi IndoBERT. Label akhir advisory mengikuti penilaian blind yang terkunci. Prediksi model lama dipakai untuk menunjukkan ketidaksepakatan; tidak diberikan kembali ke Gemini.

Jumlah soal: 50; distribusi label advisory: `{"mathCognitiveDomain": {"knowing": 27, "applying": 23, "reasoning": 0}, "knowledgeDimension": {"procedural": 17, "factual": 11, "conceptual": 22, "metacognitive": 0}, "intendedDifficulty": {"Easy": 48, "Medium": 2, "Hard": 0}}`.
Distribusi hanya pada soal tanpa blocker konten: `{"mathCognitiveDomain": {"knowing": 27, "applying": 23}, "knowledgeDimension": {"procedural": 17, "factual": 11, "conceptual": 22}, "intendedDifficulty": {"Easy": 48, "Medium": 2}}`. Label usulan pada soal perlu revisi tidak berarti soalnya sudah sah digunakan.
Routing: `{"silver_ready": 50}`.
Run awal sukses: 150/150; adjudikasi: 22; token sukses tercatat: 346,361.

Seluruh label memakai provenance ai_silver. Delivery memakai snapshot silver yang lolos qualification. CTT/IRT tidak dihitung karena respons siswa belum ada. Boundary audit dan gate training tidak dianggap lolos hanya karena batch API selesai.

IndoBERT aktif: `indobert-3x4x3-silver-kelas1-v1`, arsitektur `parallel-v1`, representation `metadata`. Artifact belum disetujui; tidak ada training ulang dalam batch ini. Difficulty model lama dapat mengalami class collapse. Confidence dari kalibrasi kelas 1 yang kecil belum membuktikan ketepatan label.
KKO eksplisit masuk input encoder: `False`. Solusi minimum masuk input encoder: `False`. KKO/solusi tetap dicatat untuk audit; jangan menyatakan fitur itu dipakai model bila serializer artefak tidak memasukkannya.

## Kelompok difficulty

Kesulitan dinilai relatif terhadap kelas sasaran. Kategori kosong tetap ditampilkan; label tidak diubah untuk memenuhi kuota. Soal tanpa blocker konten dapat masuk snapshot silver operasional.

| Difficulty | Semua usulan | Tanpa blocker konten | Data soal |
|---|---:|---:|---|
| Easy | 48 | 48 | [Easy.json](difficulty/Easy.json) |
| Medium | 2 | 2 | [Medium.json](difficulty/Medium.json) |
| Hard | 0 | 0 | [Hard.json](difficulty/Hard.json) |

## Perhitungan yang dipakai

Encoder menghasilkan representasi [CLS], lalu tiga head menghasilkan logits. Probabilitas adalah pᵢ = exp(zᵢ/T) / Σⱼ exp(zⱼ/T), dengan temperature sesuai manifest. Confidence = max(pᵢ). Entropy H = −Σᵢ pᵢ ln(pᵢ) / ln(K). Probabilitas, confidence, entropy, dan action di bawah berasal dari inferensi lokal; tidak dibuat oleh Gemini.

Suara awal LLM dihitung dari label yang benar-benar diberikan tiap run; abstain tidak menjadi suara kelas. Policy saat ini menerima 3–0 langsung dan meminta adjudikasi untuk kasus lainnya. Majority awal minimal 2/3 dicatat sebagai bukti, bukan confidence probabilistik. Label adjudikasi yang berbeda dari mayoritas awal tetap disimpan dengan alasan dan tidak disamarkan menjadi voting 3–0.

## 1. Soal `1f52d8dff6bbb1b9be6a4516`

Ayo menghitung banyak mainan. Wei pergi ke toko mainan. Wei melihat banyak mainan. Wei kesulitan menghitungnya. Ayo bantu Wei.<br><br>Ayo bantu Wei. Ada .... (boneka kelinci). Berapa banyaknya?

| Opsi | Isi |
|---|---|
| A | 5 |
| B | 7 |
| C | 9 |
| D | 6 |

![Gambar sumber soal 1](<../images/kelas1_panduan_siswa_kelas1.pdf-0027-06.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Menghitung satu per satu boneka kelinci pada rak paling atas: 1, 2, 3, 4, 5, 6. Jumlahnya adalah 6.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0027-06.png. Transkripsi visual: A girl is looking at a toy store. On a shelf, there are three rows of toys. The top row contains 6 pink rabbit dolls. The middle row contains 4 blue airplanes. The bottom row contains 5 blue spinning tops. To the left, there is a stepped display with 7 red toy cars. To the right, there is a pink bin containing 5 colorful balls.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `5a78aa7081386b0e06112a332c38761d0c5b335583ab7dbaaad2d6051cb5f83f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2448 |
| 2 | success | valid / verified | knowing | factual | Easy | 2442 |
| 3 | success | valid / verified | knowing | procedural | Easy | 2506 |

Run 1 — solusi: Menghitung satu per satu boneka kelinci pada rak paling atas: 1, 2, 3, 4, 5, 6. Jumlahnya adalah 6.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan proses menghitung objek secara langsung (counting) yang merupakan keterampilan dasar.. Bukti: Ayo menghitung banyak mainan; Ada .... (boneka kelinci). Berapa banyaknya?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji kemampuan dasar dalam menghitung jumlah objek konkret, yang merupakan pengetahuan faktual tentang bilangan.. Bukti: Ayo menghitung banyak mainan
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan penghitungan objek yang terlihat jelas dalam satu kelompok (rak atas).. Bukti: Ada .... (boneka kelinci). Berapa banyaknya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena fokus pada keterampilan menghitung dasar (counting) yang merupakan kompetensi inti awal. |

Run 2 — solusi: Menghitung satu per satu boneka kelinci pada rak paling atas: 1, 2, 3, 4, 5, 6.
- Domain kognitif `classify/knowing`: Siswa diminta untuk melakukan proses penghitungan langsung (counting) terhadap objek yang terlihat secara visual. Ini adalah proses dasar dalam matematika.. Bukti: Ayo menghitung banyak mainan; Ada .... (boneka kelinci). Berapa banyaknya?
- Dimensi pengetahuan `classify/factual`: Tugas ini melibatkan penggunaan konsep dasar bilangan (kuantitas) dan teknik menghitung (counting) yang merupakan pengetahuan faktual/prosedural dasar.. Bukti: Ayo menghitung banyak mainan
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, hanya memerlukan penghitungan objek konkret yang tersusun rapi tanpa distraksi yang rumit.. Bukti: Ada .... (boneka kelinci). Berapa banyaknya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 secara berurutan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD untuk materi membilang benda konkret. |

Run 3 — solusi: Menghitung jumlah boneka kelinci pada rak paling atas satu per satu: 1, 2, 3, 4, 5, 6. Totalnya adalah 6.
- Domain kognitif `classify/knowing`: Siswa diminta untuk melakukan proses menghitung objek secara langsung (counting) yang merupakan keterampilan dasar dalam domain knowing.. Bukti: Ayo menghitung banyak mainan; Ada .... (boneka kelinci). Berapa banyaknya?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji kemampuan siswa dalam menerapkan prosedur menghitung (counting) untuk menentukan kuantitas objek, yang merupakan pengetahuan prosedural dasar.. Bukti: Ayo menghitung banyak mainan
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, melibatkan penghitungan objek konkret yang tersusun rapi dalam satu baris, sesuai dengan tingkat perkembangan kelas 1.. Bukti: Ayo bantu Wei. Ada .... (boneka kelinci). Berapa banyaknya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 secara berurutan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menghitung objek konkret adalah kompetensi inti kelas 1 awal. Soal ini tidak memiliki jebakan kompleks, hanya menuntut ketelitian menghitung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3760`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu melakukan proses menghitung objek secara langsung (counting) yang merupakan keterampilan dasar dalam domain knowing.
- Dimensi pengetahuan `procedural`: Tugas ini melibatkan penggunaan konsep dasar bilangan (kuantitas) dan teknik menghitung (counting) yang merupakan pengetahuan prosedural dasar.
- Intended difficulty `Easy`: Soal ini sangat mendasar, melibatkan penghitungan objek konkret yang tersusun rapi dalam satu baris, sesuai dengan tingkat perkembangan kelas 1.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 secara berurutan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Menghitung objek konkret adalah kompetensi inti kelas 1 awal. Soal ini tidak memiliki jebakan kompleks, hanya menuntut ketelitian menghitung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 189/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000541; applying=0.999459; reasoning=0.000000 | applying | 0.999459 | 0.004197 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.021067; conceptual=0.953852; procedural=0.025082; metacognitive=0.000000 | conceptual | 0.953852 | 0.157851 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.655815; Medium=0.322920; Hard=0.021265 | Easy | 0.655815 | 0.658624 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999459; −Σp ln(p) = 0.004611; H = 0.004611/ln(3) = 0.004197; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.953852; −Σp ln(p) = 0.218827; H = 0.218827/ln(4) = 0.157851; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.655815; −Σp ln(p) = 0.723572; H = 0.723572/ln(3) = 0.658624; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Menghitung, Membaca, dan Menulis Bilangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Ayo menghitung banyak mainan. Wei pergi ke toko mainan. Wei melihat banyak mainan. Wei kesulitan menghitungnya. Ayo bantu Wei.

Ayo bantu Wei. Ada .... (boneka kelinci). Berapa banyaknya?
Pilihan: A. 5
B. 7
C. 9
D. 6
Transkripsi visual: A girl is looking at a toy store. On a shelf, there are three rows of toys. The top row contains 6 pink rabbit dolls. The middle row contains 4 blue airplanes. The bottom row contains 5 blue spinning tops. To the left, there is a stepped display with 7 red toy cars. To the right, there is a pink bin containing 5 colorful balls.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 2. Soal `e91b53ee437d36556aa832b8`

Pasangkan lambang bilangan dengan namanya. Bilangan 7 dibaca ....

| Opsi | Isi |
|---|---|
| A | Tujuh |
| B | Delapan |
| C | Enam |
| D | Sembilan |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Lambang bilangan 7 memiliki nama bilangan 'tujuh'.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `28bc514789457f83d4d75614b1d48093282fef89d172f5889ad4cac88b3a3f6c`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 1264 |
| 2 | success | valid / verified | knowing | factual | Easy | 1244 |
| 3 | success | valid / verified | knowing | factual | Easy | 1244 |

Run 1 — solusi: Lambang bilangan 7 memiliki nama bilangan 'tujuh'.
- Domain kognitif `classify/knowing`: Soal ini hanya meminta siswa untuk mengingat atau mengenali nama bilangan dari lambang bilangan yang diberikan, yang merupakan proses kognitif langsung.. Bukti: Bilangan 7 dibaca ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan tentang istilah atau label dasar (nama bilangan) yang dikaitkan dengan simbol numerik.. Bukti: Bilangan 7 dibaca ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar bagi siswa kelas 1, hanya melibatkan satu langkah pengenalan simbol tanpa proses perhitungan atau penalaran kompleks.. Bukti: Bilangan 7 dibaca ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal lambang bilangan 1-10 dan nama bilangannya. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD untuk pengenalan bilangan dasar. |

Run 2 — solusi: Lambang bilangan 7 memiliki nama bilangan 'tujuh'.
- Domain kognitif `classify/knowing`: Soal ini hanya meminta siswa untuk mengingat atau mengenali nama bilangan dari lambang bilangan yang diberikan, yang merupakan proses kognitif langsung.. Bukti: Bilangan 7 dibaca ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan tentang simbol angka dan nama bilangan yang berkorespondensi, yang merupakan pengetahuan faktual dasar.. Bukti: Bilangan 7 dibaca ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan pengenalan simbol angka tunggal tanpa operasi atau langkah tambahan.. Bukti: Bilangan 7 dibaca ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal simbol angka 1-10 dan nama bilangannya. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD untuk pengenalan lambang bilangan dasar. |

Run 3 — solusi: Lambang bilangan 7 memiliki nama bilangan 'tujuh'.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengingat atau mengenali nama bilangan dari lambang bilangan yang diberikan secara langsung.. Bukti: Bilangan 7 dibaca ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual mengenai nama bilangan (simbol dan representasi verbalnya).. Bukti: Bilangan 7 dibaca ....
- Intended difficulty `classify/Easy`: Soal ini bersifat sangat mendasar, hanya memerlukan pengenalan simbol angka tunggal dan nama bilangannya.. Bukti: Bilangan 7 dibaca ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal lambang bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD untuk pengenalan lambang dan nama bilangan dasar. |

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
| Domain kognitif | knowing=0.999906; applying=0.000094; reasoning=0.000000 | knowing | 0.999906 | 0.000877 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.773133; conceptual=0.204016; procedural=0.022851; metacognitive=0.000000 | factual | 0.773133 | 0.439714 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.887681; Medium=0.109815; Hard=0.002505 | Easy | 0.887681 | 0.330726 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999906; −Σp ln(p) = 0.000963; H = 0.000963/ln(3) = 0.000877; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.773133; −Σp ln(p) = 0.609573; H = 0.609573/ln(4) = 0.439714; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.887681; −Σp ln(p) = 0.363339; H = 0.363339/ln(3) = 0.330726; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Menghitung, Membaca, dan Menulis Bilangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Pasangkan lambang bilangan dengan namanya. Bilangan 7 dibaca ....
Pilihan: A. Tujuh
B. Delapan
C. Enam
D. Sembilan
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 3. Soal `aded1ab9ecb9a5ad0e341f2a`

Buah mana yang jumlahnya lebih banyak?

| Opsi | Isi |
|---|---|
| A | Tidak dapat ditentukan |
| B | B (jeruk) |
| C | Sama banyak |
| D | A (mangga) |

![Gambar sumber soal 3](<../images/kelas1_panduan_siswa_kelas1.pdf-0048-05.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Kotak A berisi 4 mangga, kotak B berisi 6 jeruk. Karena 6 > 4, maka kotak B lebih banyak.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0048-05.png. Transkripsi visual: Terdapat dua kotak berlabel A dan B. Kotak A berisi 4 buah mangga. Kotak B berisi 6 buah jeruk.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7340044427e5d71399d187a9b20d06580337e11cea87daa2d2cad4fdfe65a870`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2472 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2497 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2530 |

Run 1 — solusi: Kotak A berisi 4 mangga, kotak B berisi 6 jeruk. Karena 6 > 4, maka kotak B lebih banyak.
- Domain kognitif `classify/applying`: Siswa perlu melakukan proses menghitung jumlah benda pada masing-masing kelompok (fakta) dan membandingkan kedua bilangan tersebut untuk menentukan mana yang lebih banyak.. Bukti: Buah mana yang jumlahnya lebih banyak?; Kotak A berisi 4 buah mangga. Kotak B berisi 6 buah jeruk.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep perbandingan kuantitas antara dua kelompok benda yang berbeda.. Bukti: Membandingkan Banyak Benda
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya melibatkan penghitungan benda konkret dalam jumlah kecil (di bawah 10) dan perbandingan langsung.. Bukti: 4 buah mangga; 6 buah jeruk

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 dan membandingkan dua bilangan cacah. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 SD karena membandingkan jumlah benda konkret adalah materi dasar awal. |

Run 2 — solusi: Kotak A berisi 4 mangga, kotak B berisi 6 jeruk. Karena 6 lebih besar dari 4, maka kotak B memiliki jumlah buah lebih banyak.
- Domain kognitif `classify/applying`: Siswa perlu melakukan proses menghitung jumlah benda pada masing-masing kelompok dan membandingkan hasilnya untuk menentukan mana yang lebih banyak. Ini adalah penerapan prosedur dasar membandingkan bilangan.. Bukti: Buah mana yang jumlahnya lebih banyak?; Kotak A berisi 4 buah mangga. Kotak B berisi 6 buah jeruk.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep perbandingan kuantitas (lebih banyak/sedikit) melalui prosedur menghitung benda konkret.. Bukti: Buah mana yang jumlahnya lebih banyak?
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan penghitungan langsung dan perbandingan dua bilangan kecil (4 dan 6) yang familiar.. Bukti: Buah mana yang jumlahnya lebih banyak?; Kotak A berisi 4 buah mangga. Kotak B berisi 6 buah jeruk.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 dan membandingkan dua bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena hanya melibatkan penghitungan benda konkret dan perbandingan langsung. |

Run 3 — solusi: Kotak A berisi 4 mangga, kotak B berisi 6 jeruk. Karena 6 > 4, maka kotak B lebih banyak.
- Domain kognitif `classify/applying`: Siswa perlu melakukan proses menghitung jumlah benda pada masing-masing kelompok dan membandingkan hasilnya untuk menentukan mana yang lebih banyak. Ini adalah penerapan prosedur dasar.. Bukti: Buah mana yang jumlahnya lebih banyak?; jeruk pada kotak B berjumlah 6, lebih banyak daripada mangga pada kotak A yang berjumlah 4
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep kuantitas dan perbandingan jumlah benda, yang merupakan pengetahuan konseptual dasar.. Bukti: Membandingkan Banyak Benda; jeruk pada kotak B berjumlah 6, lebih banyak daripada mangga pada kotak A yang berjumlah 4
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan penghitungan langsung dan perbandingan sederhana antara dua kelompok benda yang terlihat jelas.. Bukti: Buah mana yang jumlahnya lebih banyak?; jeruk pada kotak B berjumlah 6, lebih banyak daripada mangga pada kotak A yang berjumlah 4

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 dan membandingkan dua bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena hanya melibatkan perbandingan dua kelompok benda kecil yang konkret. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 85/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000497; applying=0.999503; reasoning=0.000000 | applying | 0.999503 | 0.003891 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.111731; conceptual=0.877200; procedural=0.011069; metacognitive=0.000000 | conceptual | 0.877200 | 0.295505 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.858035; Medium=0.139033; Hard=0.002932 | Easy | 0.858035 | 0.384842 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999503; −Σp ln(p) = 0.004275; H = 0.004275/ln(3) = 0.003891; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.877200; −Σp ln(p) = 0.409657; H = 0.409657/ln(4) = 0.295505; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.858035; −Σp ln(p) = 0.422792; H = 0.422792/ln(3) = 0.384842; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Membandingkan Banyak Benda
Tipe soal: multiple_choice
Stimulus: -
Soal: Buah mana yang jumlahnya lebih banyak?
Pilihan: A. Tidak dapat ditentukan
B. B (jeruk)
C. Sama banyak
D. A (mangga)
Transkripsi visual: Terdapat dua kotak berlabel A dan B. Kotak A berisi 4 buah mangga. Kotak B berisi 6 buah jeruk.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 4. Soal `71dcf3a05499a6d3e660d279`

Buah mana yang jumlahnya lebih sedikit?

| Opsi | Isi |
|---|---|
| A | Tidak dapat ditentukan |
| B | A (mangga) |
| C | Sama banyak |
| D | B (jeruk) |

![Gambar sumber soal 4](<../images/kelas1_panduan_siswa_kelas1.pdf-0048-05.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Kotak A berisi 4 mangga, kotak B berisi 6 jeruk. Karena 4 < 6, maka kotak A (mangga) memiliki jumlah lebih sedikit.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0048-05.png. Transkripsi visual: Terdapat dua kotak, A dan B. Kotak A berisi 4 buah mangga. Kotak B berisi 6 buah jeruk.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8f6fe712ed737d791fc399743b8a2f0ccdf6943578e44745af90551a98613151`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2519 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2529 |
| 3 | success | valid / verified | applying | procedural | Easy | 2502 |

Run 1 — solusi: Kotak A berisi 4 mangga, kotak B berisi 6 jeruk. Karena 4 < 6, maka kotak A (mangga) memiliki jumlah lebih sedikit.
- Domain kognitif `classify/applying`: Siswa perlu menghitung jumlah benda di masing-masing kelompok (fakta) dan membandingkan kedua bilangan tersebut untuk menentukan mana yang lebih sedikit. Ini adalah proses penerapan konsep perbandingan dasar.. Bukti: Buah mana yang jumlahnya lebih sedikit?; Kotak A berisi 4 buah mangga. Kotak B berisi 6 buah jeruk.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan 'lebih sedikit' antara dua kuantitas yang dihitung.. Bukti: Membandingkan Banyak Benda
- Intended difficulty `classify/Easy`: Soal ini sangat sesuai untuk kelas 1 karena menggunakan objek konkret yang mudah dihitung dan membandingkan dua bilangan kecil (4 dan 6).. Bukti: Buah mana yang jumlahnya lebih sedikit?; 4 buah mangga; 6 buah jeruk

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 dan memahami konsep perbandingan dasar (lebih banyak/lebih sedikit). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas menghitung dan membandingkan dua kelompok benda kecil adalah standar kompetensi dasar matematika kelas 1. |

Run 2 — solusi: Kotak A berisi 4 mangga, kotak B berisi 6 jeruk. Karena 4 < 6, maka kotak A (mangga) memiliki jumlah lebih sedikit.
- Domain kognitif `classify/applying`: Siswa perlu melakukan proses menghitung benda konkret (4 dan 6) lalu membandingkan nilainya untuk menentukan mana yang lebih sedikit. Ini adalah penerapan prosedur dasar membandingkan bilangan.. Bukti: Buah mana yang jumlahnya lebih sedikit?; Kotak A berisi 4 buah mangga. Kotak B berisi 6 buah jeruk.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep perbandingan jumlah (lebih sedikit) melalui prosedur menghitung benda.. Bukti: Buah mana yang jumlahnya lebih sedikit?
- Intended difficulty `classify/Easy`: Soal ini sangat sesuai untuk kelas 1 karena melibatkan objek konkret yang familiar, operasi hitung dasar (menghitung sampai 6), dan perbandingan langsung.. Bukti: Buah mana yang jumlahnya lebih sedikit?; Kotak A berisi 4 buah mangga. Kotak B berisi 6 buah jeruk.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 dan memahami konsep 'lebih sedikit' vs 'lebih banyak'. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD untuk materi membandingkan banyak benda dengan jumlah di bawah 10. |

Run 3 — solusi: Kotak A berisi 4 mangga, kotak B berisi 6 jeruk. Karena 4 < 6, maka kotak A (mangga) memiliki jumlah lebih sedikit.
- Domain kognitif `classify/applying`: Siswa perlu melakukan proses menghitung jumlah benda pada setiap kelompok (A dan B) lalu membandingkan hasilnya untuk menentukan mana yang lebih sedikit. Ini adalah penerapan prosedur dasar membandingkan bilangan.. Bukti: Buah mana yang jumlahnya lebih sedikit?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung dan membandingkan kuantitas benda konkret.. Bukti: Membandingkan Banyak Benda
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan penghitungan benda konkret dalam jumlah kecil (di bawah 10) dan perbandingan langsung.. Bukti: Buah mana yang jumlahnya lebih sedikit?; Kotak A berisi 4 mangga, kotak B berisi 6 jeruk

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 dan konsep dasar perbandingan 'lebih sedikit'/'lebih banyak'. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD untuk materi membandingkan banyak benda melalui visualisasi langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3835`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu melakukan proses menghitung benda konkret (4 dan 6) lalu membandingkan nilainya untuk menentukan mana yang lebih sedikit. Ini adalah penerapan konsep perbandingan dasar.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan 'lebih sedikit' antara dua kuantitas yang dihitung.
- Intended difficulty `Easy`: Soal ini sangat sesuai untuk kelas 1 karena menggunakan objek konkret yang mudah dihitung dan membandingkan dua bilangan kecil (4 dan 6).

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 dan memahami konsep perbandingan dasar (lebih banyak/lebih sedikit). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas menghitung dan membandingkan dua kelompok benda kecil adalah standar kompetensi dasar matematika kelas 1. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 84/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000587; applying=0.999413; reasoning=0.000000 | applying | 0.999413 | 0.004507 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.096170; conceptual=0.892698; procedural=0.011132; metacognitive=0.000000 | conceptual | 0.892698 | 0.271655 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.856371; Medium=0.140677; Hard=0.002953 | Easy | 0.856371 | 0.387661 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999413; −Σp ln(p) = 0.004952; H = 0.004952/ln(3) = 0.004507; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.892698; −Σp ln(p) = 0.376594; H = 0.376594/ln(4) = 0.271655; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.856371; −Σp ln(p) = 0.425889; H = 0.425889/ln(3) = 0.387661; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Membandingkan Banyak Benda
Tipe soal: multiple_choice
Stimulus: -
Soal: Buah mana yang jumlahnya lebih sedikit?
Pilihan: A. Tidak dapat ditentukan
B. A (mangga)
C. Sama banyak
D. B (jeruk)
Transkripsi visual: Terdapat dua kotak, A dan B. Kotak A berisi 4 buah mangga. Kotak B berisi 6 buah jeruk.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 5. Soal `a035dee2caefafa52096496e`

Lengkapi urutan bilangan berikut: 1, 2, ....

| Opsi | Isi |
|---|---|
| A | 3 |
| B | 1 |
| C | 0 |
| D | 4 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Urutan bilangan 1, 2 menunjukkan pola penambahan 1 (maju), sehingga bilangan berikutnya adalah 2 + 1 = 3.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `87e9ac4734983dd9522c0d00f6e50ad6ae63ba63a274a79cdd72b7578fd66103`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 1237 |
| 2 | success | valid / verified | knowing | factual | Easy | 1263 |
| 3 | success | valid / verified | knowing | factual | Easy | 1257 |

Run 1 — solusi: Urutan bilangan 1, 2 menunjukkan pola penambahan 1 (maju), sehingga bilangan berikutnya adalah 2 + 1 = 3.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali pola urutan bilangan sederhana dan melanjutkan urutan tersebut, yang merupakan proses langsung.. Bukti: Lengkapi urutan bilangan berikut: 1, 2, ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang urutan bilangan dasar (fakta numerik) dalam konteks berhitung maju.. Bukti: 1, 2, ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan pola yang sangat familiar dan satu langkah penyelesaian.. Bukti: 1, 2, ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1 sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD mengenai pengenalan urutan bilangan cacah. |

Run 2 — solusi: Urutan bilangan 1, 2 menunjukkan pola penambahan 1 (maju). Bilangan setelah 2 adalah 2 + 1 = 3.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali pola urutan bilangan dasar yang sudah familiar (1, 2, 3) dan melanjutkan urutan tersebut secara langsung.. Bukti: Lengkapi urutan bilangan berikut: 1, 2, ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang urutan bilangan dasar (fakta numerik) yang merupakan pengetahuan faktual dalam matematika awal.. Bukti: 1, 2, ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, menggunakan urutan bilangan yang paling umum dipelajari di kelas 1, dengan beban kognitif yang sangat rendah.. Bukti: 1, 2, ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal urutan bilangan cacah 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD untuk pengenalan pola bilangan sederhana. |

Run 3 — solusi: Urutan bilangan 1, 2 menunjukkan pola penambahan 1 (maju). Bilangan setelah 2 adalah 2 + 1 = 3.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali pola urutan bilangan dasar (1, 2, 3) yang merupakan proses langsung.. Bukti: Lengkapi urutan bilangan berikut: 1, 2, ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang urutan bilangan dasar (fakta numerik) dalam konteks menghitung maju.. Bukti: 1, 2, ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan prosedur familiar (menghitung maju satu-satu) dengan beban kognitif yang sangat rendah.. Bukti: 1, 2, ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1 sampai 3. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD untuk pengenalan urutan bilangan dasar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 61/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=1.000000; applying=0.000000; reasoning=0.000000 | knowing | 1.000000 | 0.000001 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.878503; conceptual=0.105707; procedural=0.015790; metacognitive=0.000000 | factual | 0.878503 | 0.300681 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.909591; Medium=0.088220; Hard=0.002189 | Easy | 0.909591 | 0.285623 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000001; H = 0.000001/ln(3) = 0.000001; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.878503; −Σp ln(p) = 0.416832; H = 0.416832/ln(4) = 0.300681; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.909591; −Σp ln(p) = 0.313788; H = 0.313788/ln(3) = 0.285623; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Menghitung Maju dan Mundur
Tipe soal: multiple_choice
Stimulus: -
Soal: Lengkapi urutan bilangan berikut: 1, 2, ....
Pilihan: A. 3
B. 1
C. 0
D. 4
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 6. Soal `593cbed3be61dd6c967e770c`

Lengkapi urutan bilangan berikut: 4, 5, ....

| Opsi | Isi |
|---|---|
| A | 3 |
| B | 4 |
| C | 6 |
| D | 7 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Urutan bilangan 4, 5 menunjukkan pola penambahan 1 (menghitung maju). Bilangan setelah 5 dengan pola tersebut adalah 5 + 1 = 6.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `9fe9be503affcc15959049b5ad2edf1f4088fbe863530b5d135ca277c99393ec`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 1289 |
| 2 | success | valid / verified | knowing | factual | Easy | 1279 |
| 3 | success | valid / verified | knowing | factual | Easy | 1274 |

Run 1 — solusi: Urutan bilangan 4, 5 menunjukkan pola penambahan 1 (menghitung maju). Bilangan setelah 5 dengan pola tersebut adalah 5 + 1 = 6.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali pola urutan bilangan sederhana (menghitung maju) dan menentukan bilangan berikutnya, yang merupakan proses langsung.. Bukti: Lengkapi urutan bilangan berikut: 4, 5, ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang urutan bilangan sebagai fakta dasar dalam berhitung.. Bukti: Lengkapi urutan bilangan berikut: 4, 5, ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan pola urutan yang sangat familiar dengan beban kognitif yang rendah.. Bukti: 4, 5, ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 secara berurutan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD untuk pengenalan pola bilangan sederhana. |

Run 2 — solusi: Urutan bilangan 4, 5 menunjukkan pola penambahan 1 (menghitung maju). Bilangan setelah 5 adalah 5 + 1 = 6.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali pola urutan bilangan sederhana dan melanjutkan urutan tersebut dengan satu langkah langsung.. Bukti: Lengkapi urutan bilangan berikut: 4, 5, ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang urutan bilangan dasar (fakta numerik) dalam konteks menghitung maju.. Bukti: 4, 5, ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, hanya melibatkan satu langkah logis dalam urutan bilangan yang familiar.. Bukti: 4, 5, ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 secara berurutan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD untuk pengenalan urutan bilangan dasar. |

Run 3 — solusi: Urutan bilangan 4, 5 menunjukkan pola penambahan 1 (menghitung maju). Bilangan setelah 5 adalah 5 + 1 = 6.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali pola urutan bilangan sederhana dan menerapkan prosedur menghitung maju satu langkah, yang merupakan proses langsung.. Bukti: Lengkapi urutan bilangan berikut: 4, 5, ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang urutan bilangan sebagai fakta dasar dalam sistem bilangan.. Bukti: 4, 5, ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan pola yang sangat familiar dan satu langkah penyelesaian langsung.. Bukti: 4, 5, ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 secara berurutan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 awal yang menekankan pengenalan urutan bilangan dasar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 61/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=1.000000; applying=0.000000; reasoning=0.000000 | knowing | 1.000000 | 0.000001 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.901465; conceptual=0.086746; procedural=0.011789; metacognitive=0.000000 | factual | 0.901465 | 0.258196 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.915153; Medium=0.082765; Hard=0.002083 | Easy | 0.915153 | 0.273280 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000001; H = 0.000001/ln(3) = 0.000001; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.901465; −Σp ln(p) = 0.357936; H = 0.357936/ln(4) = 0.258196; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.915153; −Σp ln(p) = 0.300228; H = 0.300228/ln(3) = 0.273280; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Menghitung Maju dan Mundur
Tipe soal: multiple_choice
Stimulus: -
Soal: Lengkapi urutan bilangan berikut: 4, 5, ....
Pilihan: A. 3
B. 4
C. 6
D. 7
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 7. Soal `82267daa87c52ac8b3876098`

Temukan pasangan bilangan berikut.<br><br>Temukan pasangan bilangan berikut. Bilangan 9 dipasangkan menjadi dua bilangan berapa dan berapa?

| Opsi | Isi |
|---|---|
| A | 5 dan 3 |
| B | 4 dan 4 |
| C | 3 dan 6 |
| D | 4 dan 5 |

![Gambar sumber soal 7](<../images/kelas1_panduan_siswa_kelas1.pdf-0043-04.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Menghitung jumlah objek pada kotak kiri (4) dan kotak kanan (5). Total 4 + 5 = 9. Pasangan bilangan untuk 9 adalah 4 dan 5.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0043-04.png. Transkripsi visual: Terdapat dua kotak berisi objek. Kotak kiri berisi 4 buah jeruk. Kotak kanan berisi 5 buah salak. Di bawahnya terdapat diagram pasangan bilangan (number bond) dengan angka 9 di lingkaran utama yang terhubung ke dua lingkaran kosong.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `bd135fcf0454301d6053e5300a93b5b746e11d6cd6043cc0bf2c740a5603e92d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2545 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2521 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2490 |

Run 1 — solusi: Menghitung jumlah objek pada kotak kiri (4) dan kotak kanan (5). Total 4 + 5 = 9. Pasangan bilangan untuk 9 adalah 4 dan 5.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi jumlah objek dalam dua kelompok visual yang berbeda dan menghubungkannya dengan konsep komposisi bilangan (pasangan bilangan). Ini adalah proses menerapkan konsep dasar penjumlahan/komposisi pada situasi visual yang rutin.. Bukti: Bilangan 9 dipasangkan menjadi dua bilangan berapa dan berapa?; 4 jeruk dan 5 buah lainnya
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur komposisi bilangan (number bonds), yang merupakan prinsip dasar dalam aritmatika awal.. Bukti: pasangan bilangan; 9 dipasangkan menjadi dua bilangan
- Intended difficulty `classify/Easy`: Soal ini sangat sesuai untuk kelas 1 karena menggunakan representasi visual konkret (gambar) untuk mendukung pemahaman konsep pasangan bilangan (number bonds) yang merupakan materi standar.. Bukti: Temukan pasangan bilangan berikut; 4 jeruk; 5 buah lainnya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret sampai 10 dan pemahaman dasar tentang komposisi bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Materi pasangan bilangan (number bonds) adalah kurikulum inti kelas 1. Soal ini menggunakan representasi visual yang membantu siswa, sehingga tingkat kesulitannya rendah. |

Run 2 — solusi: Menghitung jumlah objek pada kotak kiri (4) dan kotak kanan (5), sehingga 9 dapat dipecah menjadi pasangan 4 dan 5.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi jumlah objek dalam dua kelompok yang berbeda dan menghubungkannya dengan konsep komposisi bilangan (pasangan bilangan). Ini adalah proses menerapkan pemahaman konsep bilangan ke situasi visual rutin.. Bukti: Temukan pasangan bilangan berikut; 4 jeruk dan 5 buah lainnya
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan bagian-keseluruhan (part-whole relationship) dalam bilangan, yang merupakan konsep dasar aritmatika.. Bukti: Bilangan 9 dipasangkan menjadi dua bilangan
- Intended difficulty `classify/Easy`: Soal ini sangat sesuai untuk kelas 1 karena menggunakan representasi visual konkret (gambar objek) untuk mendukung pemahaman abstrak tentang pasangan bilangan. Prosedurnya langsung dan familiar.. Bukti: Temukan pasangan bilangan berikut; 4 jeruk; 5 buah lainnya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang benda konkret sampai 10 dan memahami konsep penjumlahan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas memecah bilangan (number bonds) adalah kurikulum standar kelas 1. Penggunaan gambar membuat tugas ini mudah diakses. |

Run 3 — solusi: Menghitung jumlah objek pada kotak kiri (4) dan kotak kanan (5), lalu memverifikasi bahwa 4 + 5 = 9.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi jumlah objek dalam dua kelompok visual dan menghubungkannya dengan konsep pasangan bilangan (number bond) untuk angka 9. Ini adalah penerapan konsep dasar penjumlahan.. Bukti: Temukan pasangan bilangan berikut; 4 jeruk dan 5 buah lainnya
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang komposisi bilangan (part-part-whole), yang merupakan konsep fundamental dalam aritmatika dasar.. Bukti: pasangan bilangan; 9 dipasangkan menjadi dua bilangan
- Intended difficulty `classify/Easy`: Soal ini sangat sesuai untuk kelas 1 karena menggunakan representasi visual konkret untuk mendukung pemahaman abstrak tentang pasangan bilangan.. Bukti: 4 jeruk; 5 buah lainnya; 9 dipasangkan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung objek hingga 10 dan pemahaman dasar tentang penjumlahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah latihan standar untuk kelas 1 mengenai dekomposisi bilangan menggunakan bantuan visual. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 116/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.003529; applying=0.996471; reasoning=0.000000 | applying | 0.996471 | 0.021343 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.077624; conceptual=0.913567; procedural=0.008809; metacognitive=0.000000 | conceptual | 0.913567 | 0.232754 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.842938; Medium=0.153543; Hard=0.003519 | Easy | 0.842938 | 0.411076 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.996471; −Σp ln(p) = 0.023448; H = 0.023448/ln(3) = 0.021343; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.913567; −Σp ln(p) = 0.322665; H = 0.322665/ln(4) = 0.232754; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.842938; −Σp ln(p) = 0.451613; H = 0.451613/ln(3) = 0.411076; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Pasangan Bilangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Temukan pasangan bilangan berikut.

Temukan pasangan bilangan berikut. Bilangan 9 dipasangkan menjadi dua bilangan berapa dan berapa?
Pilihan: A. 5 dan 3
B. 4 dan 4
C. 3 dan 6
D. 4 dan 5
Transkripsi visual: Terdapat dua kotak berisi objek. Kotak kiri berisi 4 buah jeruk. Kotak kanan berisi 5 buah salak. Di bawahnya terdapat diagram pasangan bilangan (number bond) dengan angka 9 di lingkaran utama yang terhubung ke dua lingkaran kosong.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 8. Soal `ddae4518c6926e380356e576`

Pasangkan dua bilangan yang jumlahnya 6. Bilangan berapa yang berpasangan dengan 4?

| Opsi | Isi |
|---|---|
| A | 3 |
| B | 2 |
| C | 4 |
| D | 1 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: 4 + x = 6, maka x = 2.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `40068de1e3104dd5d5f2dce13b1742a9b41e3b4e32d17eb61a054f795d89758e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 1316 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1308 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1327 |

Run 1 — solusi: 4 + x = 6, maka x = 6 - 4 = 2.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi penjumlahan dasar atau pengurangan untuk melengkapi pasangan bilangan, yang merupakan proses langsung dalam konteks kelas 1.. Bukti: Pasangkan dua bilangan yang jumlahnya 6; Bilangan berapa yang berpasangan dengan 4?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang fakta dasar penjumlahan (number bonds) yang merupakan pengetahuan faktual tentang hubungan antar bilangan.. Bukti: jumlahnya 6; berpasangan dengan 4
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan satu operasi aritmatika sederhana dengan angka kecil (di bawah 10).. Bukti: jumlahnya 6; berpasangan dengan 4

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan pasangan bilangan (number bonds) hingga 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 yang menekankan penguasaan pasangan bilangan (number bonds) sebagai fondasi aritmatika. |

Run 2 — solusi: Jumlah pasangan bilangan adalah 6. Jika salah satu bilangan adalah 4, maka 6 - 4 = 2.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep penjumlahan dasar untuk mencari pasangan bilangan yang memenuhi syarat jumlah tertentu (6). Ini adalah penerapan prosedur rutin.. Bukti: Pasangkan dua bilangan yang jumlahnya 6; Bilangan berapa yang berpasangan dengan 4?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antar bilangan (komposisi bilangan 6) yang merupakan pengetahuan konseptual dasar.. Bukti: jumlahnya 6; berpasangan dengan 4
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan satu operasi pengurangan atau penjumlahan sederhana untuk menemukan pasangan bilangan.. Bukti: jumlahnya 6; berpasangan dengan 4

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dan pengurangan dasar hingga 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD mengenai komposisi bilangan (number bonds) hingga 10. |

Run 3 — solusi: Untuk mendapatkan jumlah 6, kita mencari bilangan x sehingga 4 + x = 6. Maka x = 6 - 4 = 2.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep penjumlahan dasar untuk menemukan pasangan bilangan yang membentuk jumlah tertentu (6). Ini adalah penerapan prosedur rutin.. Bukti: Pasangkan dua bilangan yang jumlahnya 6; Bilangan berapa yang berpasangan dengan 4?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antar bilangan (komposisi bilangan 6) yang merupakan pengetahuan konseptual dasar.. Bukti: jumlahnya 6; berpasangan dengan 4
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan satu operasi penjumlahan/pengurangan sederhana dengan angka kecil.. Bukti: Pasangkan dua bilangan yang jumlahnya 6; Bilangan berapa yang berpasangan dengan 4?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan pasangan bilangan hingga 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 yang menekankan pada pengenalan pasangan bilangan (number bonds) hingga 10. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 1, "applying": 2} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"factual": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2531`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan prosedur rutin penjumlahan/pengurangan dasar untuk menemukan pasangan bilangan yang membentuk jumlah tertentu (6).
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman tentang komposisi bilangan (number bonds), yang merupakan hubungan konseptual antar bilangan.
- Intended difficulty `Easy`: Soal ini merupakan tugas rutin yang sangat mendasar untuk kelas 1, melibatkan satu operasi aritmatika sederhana dengan angka kecil.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dan pengurangan dasar hingga 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD mengenai penguasaan pasangan bilangan (number bonds) sebagai fondasi aritmatika. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 61/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999928; applying=0.000072; reasoning=0.000000 | knowing | 0.999928 | 0.000695 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.741863; conceptual=0.228809; procedural=0.029328; metacognitive=0.000000 | factual | 0.741863 | 0.477880 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.882585; Medium=0.115501; Hard=0.001913 | Easy | 0.882585 | 0.338169 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999928; −Σp ln(p) = 0.000763; H = 0.000763/ln(3) = 0.000695; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.741863; −Σp ln(p) = 0.662482; H = 0.662482/ln(4) = 0.477880; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.882585; −Σp ln(p) = 0.371516; H = 0.371516/ln(3) = 0.338169; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Pasangan Bilangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Pasangkan dua bilangan yang jumlahnya 6. Bilangan berapa yang berpasangan dengan 4?
Pilihan: A. 3
B. 2
C. 4
D. 1
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "conceptual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 9. Soal `ef1c6489a0d0caf13ccb067e`

Ada .... mobil berwarna kuning. Ada .... mobil berwarna merah. Semuanya ada .... mobil.

| Opsi | Isi |
|---|---|
| A | 4 mobil kuning, 5 mobil merah, semuanya 9 mobil |
| B | 4 mobil kuning, 4 mobil merah, semuanya 9 mobil |
| C | 4 mobil kuning, 4 mobil merah, semuanya 8 mobil |
| D | 5 mobil kuning, 4 mobil merah, semuanya 9 mobil |

![Gambar sumber soal 9](<../images/kelas1_panduan_siswa_kelas1.pdf-0058-03.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Menghitung jumlah mobil kuning (4), menghitung jumlah mobil merah (4), lalu menjumlahkan keduanya (4 + 4 = 8).
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0058-03.png. Transkripsi visual: Terdapat dua kelompok mobil. Kelompok kiri berisi 4 mobil berwarna kuning. Kelompok kanan berisi 4 mobil berwarna merah. Soal meminta siswa mengisi jumlah mobil kuning, jumlah mobil merah, dan total seluruh mobil.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8cb692d8fca01c2911f1256917b983cf484910bfa707290e7330d474794f6d14`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2497 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2494 |
| 3 | success | valid / verified | knowing | factual | Easy | 2508 |

Run 1 — solusi: Menghitung jumlah mobil kuning (4), mobil merah (4), dan menjumlahkannya (4 + 4 = 8).
- Domain kognitif `classify/knowing`: Siswa perlu melakukan proses menghitung objek secara langsung (counting) dan melakukan operasi penjumlahan dasar yang sangat rutin.. Bukti: Ada .... mobil berwarna kuning. Ada .... mobil berwarna merah. Semuanya ada .... mobil.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman faktual tentang kuantitas objek dan prosedur penjumlahan dasar.. Bukti: Ada .... mobil berwarna kuning. Ada .... mobil berwarna merah. Semuanya ada .... mobil.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, menggunakan representasi visual yang jelas, dan hanya memerlukan operasi penjumlahan satu digit yang familiar bagi siswa kelas 1.. Bukti: 4 mobil kuning; 4 mobil merah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 dan konsep penjumlahan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena menggunakan objek konkret (gambar) dan operasi penjumlahan dasar yang merupakan standar kompetensi awal. |

Run 2 — solusi: Menghitung jumlah mobil kuning (4), menghitung jumlah mobil merah (4), lalu menjumlahkan keduanya (4 + 4 = 8).
- Domain kognitif `classify/knowing`: Siswa perlu melakukan proses menghitung objek secara langsung dan melakukan operasi penjumlahan dasar.. Bukti: Ada .... mobil berwarna kuning. Ada .... mobil berwarna merah. Semuanya ada .... mobil.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep penjumlahan dasar melalui representasi visual.. Bukti: Ada .... mobil berwarna kuning. Ada .... mobil berwarna merah. Semuanya ada .... mobil.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, menggunakan representasi visual yang jelas, dan hanya memerlukan operasi penjumlahan satu digit yang familiar bagi siswa kelas 1.. Bukti: Ada .... mobil berwarna kuning. Ada .... mobil berwarna merah. Semuanya ada .... mobil.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret sampai 10 dan konsep penjumlahan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD untuk pengenalan penjumlahan melalui benda konkret. |

Run 3 — solusi: Menghitung jumlah mobil kuning (4), menghitung jumlah mobil merah (4), lalu menjumlahkan keduanya (4 + 4 = 8).
- Domain kognitif `classify/knowing`: Siswa perlu melakukan proses menghitung objek secara langsung dan melakukan operasi penjumlahan dasar yang sangat rutin.. Bukti: Ada .... mobil berwarna kuning. Ada .... mobil berwarna merah. Semuanya ada .... mobil.
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman dasar tentang konsep penjumlahan sebagai penggabungan dua kelompok objek (fakta dasar aritmatika).. Bukti: Ada .... mobil berwarna kuning. Ada .... mobil berwarna merah. Semuanya ada .... mobil.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, menggunakan representasi visual yang jelas, dan hanya memerlukan operasi penjumlahan satu digit yang sangat rutin bagi siswa kelas 1.. Bukti: Ada .... mobil berwarna kuning. Ada .... mobil berwarna merah. Semuanya ada .... mobil.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 dan konsep dasar penjumlahan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena menggunakan objek konkret (gambar) untuk mengenalkan operasi penjumlahan dasar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3711`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu melakukan proses membilang (counting) objek secara langsung dan melakukan operasi penjumlahan dasar yang sangat rutin.
- Dimensi pengetahuan `factual`: Soal ini menguji pemahaman faktual tentang kuantitas objek dan fakta dasar penjumlahan.
- Intended difficulty `Easy`: Soal ini sangat mendasar, menggunakan representasi visual yang jelas, dan hanya memerlukan operasi penjumlahan satu digit yang familiar bagi siswa kelas 1.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 dan konsep penjumlahan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena menggunakan objek konkret (gambar) dan operasi penjumlahan dasar yang merupakan standar kompetensi awal. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 149/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000896; applying=0.999104; reasoning=0.000000 | applying | 0.999104 | 0.006538 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.024189; conceptual=0.974160; procedural=0.001651; metacognitive=0.000000 | conceptual | 0.974160 | 0.090968 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.656292; Medium=0.336607; Hard=0.007101 | Easy | 0.656292 | 0.617178 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999104; −Σp ln(p) = 0.007183; H = 0.007183/ln(3) = 0.006538; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.974160; −Σp ln(p) = 0.126109; H = 0.126109/ln(4) = 0.090968; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.656292; −Σp ln(p) = 0.678040; H = 0.678040/ln(3) = 0.617178; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Cerita Penjumlahan
Tipe soal: multiple_choice
Stimulus: -
Soal: Ada .... mobil berwarna kuning. Ada .... mobil berwarna merah. Semuanya ada .... mobil.
Pilihan: A. 4 mobil kuning, 5 mobil merah, semuanya 9 mobil
B. 4 mobil kuning, 4 mobil merah, semuanya 9 mobil
C. 4 mobil kuning, 4 mobil merah, semuanya 8 mobil
D. 5 mobil kuning, 4 mobil merah, semuanya 9 mobil
Transkripsi visual: Terdapat dua kelompok mobil. Kelompok kiri berisi 4 mobil berwarna kuning. Kelompok kanan berisi 4 mobil berwarna merah. Soal meminta siswa mengisi jumlah mobil kuning, jumlah mobil merah, dan total seluruh mobil.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "factual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 10. Soal `f00f8cf40ab22284c6d216e4`

Ada 4 anak bermain lompat tali. Datang lagi 2 anak untuk ikut bermain. Mereka bermain bergantian.<br><br>Berapa jumlah anak sekarang?

| Opsi | Isi |
|---|---|
| A | 2 |
| B | 6 |
| C | 8 |
| D | 4 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: 4 + 2 = 6
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d5ffecf23fb2b9f68b0ebb04b5fe092e632969167daa48bbd8301ba26bc7a6da`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1278 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1294 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1308 |

Run 1 — solusi: 4 + 2 = 6
- Domain kognitif `classify/applying`: Siswa perlu menerapkan operasi penjumlahan dasar pada situasi cerita rutin yang diberikan.. Bukti: Ada 4 anak bermain lompat tali. Datang lagi 2 anak untuk ikut bermain.; Berapa jumlah anak sekarang?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi penjumlahan dasar untuk menyelesaikan masalah kontekstual.. Bukti: Ada 4 anak; Datang lagi 2 anak
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah penjumlahan satu langkah yang sangat familiar bagi siswa kelas 1 dengan konteks yang sederhana.. Bukti: Ada 4 anak; Datang lagi 2 anak; Berapa jumlah anak sekarang?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan pengenalan angka 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 untuk operasi penjumlahan dasar dalam konteks cerita sehari-hari. |

Run 2 — solusi: 4 anak + 2 anak = 6 anak.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan operasi penjumlahan dasar pada situasi cerita yang rutin dan langsung.. Bukti: Ada 4 anak bermain lompat tali. Datang lagi 2 anak untuk ikut bermain.; Berapa jumlah anak sekarang?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep penjumlahan sebagai penggabungan dua kelompok benda (anak).. Bukti: Ada 4 anak bermain lompat tali. Datang lagi 2 anak untuk ikut bermain.
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah penjumlahan satu langkah yang sangat familiar bagi siswa kelas 1 dengan angka kecil.. Bukti: Ada 4 anak bermain lompat tali. Datang lagi 2 anak untuk ikut bermain.; Berapa jumlah anak sekarang?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan pengenalan angka 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD untuk materi penjumlahan dasar dalam konteks cerita sederhana. |

Run 3 — solusi: 4 anak awal + 2 anak yang datang = 6 anak.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan operasi penjumlahan dasar pada situasi cerita rutin yang sangat sederhana.. Bukti: Ada 4 anak bermain lompat tali. Datang lagi 2 anak; Berapa jumlah anak sekarang?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep penjumlahan sebagai penggabungan dua kelompok benda (anak).. Bukti: Ada 4 anak; Datang lagi 2 anak; jumlah anak sekarang
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur penjumlahan satu langkah yang sangat familiar bagi siswa kelas 1, dengan beban kognitif rendah.. Bukti: 4 anak; Datang lagi 2 anak; Berapa jumlah anak sekarang?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan membilang sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 untuk operasi penjumlahan dasar dalam konteks cerita sehari-hari. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 1, "conceptual": 2} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2457`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan operasi penjumlahan dasar pada situasi cerita rutin yang sangat sederhana.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konsep penjumlahan sebagai penggabungan dua kelompok benda (anak).
- Intended difficulty `Easy`: Soal ini merupakan masalah penjumlahan satu langkah yang sangat familiar bagi siswa kelas 1 dengan konteks yang sederhana dan angka kecil.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan pengenalan angka 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 untuk operasi penjumlahan dasar dalam konteks cerita sehari-hari. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 70/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.841757; applying=0.158243; reasoning=0.000000 | knowing | 0.841757 | 0.397542 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.539800; conceptual=0.449691; procedural=0.010510; metacognitive=0.000000 | factual | 0.539800 | 0.533858 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.856081; Medium=0.141014; Hard=0.002905 | Easy | 0.856081 | 0.387969 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.841757; −Σp ln(p) = 0.436745; H = 0.436745/ln(3) = 0.397542; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.539800; −Σp ln(p) = 0.740084; H = 0.740084/ln(4) = 0.533858; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.856081; −Σp ln(p) = 0.426227; H = 0.426227/ln(3) = 0.387969; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Cerita Penjumlahan
Tipe soal: multiple_choice
Stimulus: -
Soal: Ada 4 anak bermain lompat tali. Datang lagi 2 anak untuk ikut bermain. Mereka bermain bergantian.

Berapa jumlah anak sekarang?
Pilihan: A. 2
B. 6
C. 8
D. 4
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "conceptual", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 11. Soal `bfe710d81f98780c622d6066`

2 + 4 = ....

| Opsi | Isi |
|---|---|
| A | 4 |
| B | 5 |
| C | 6 |
| D | 7 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: 2 + 4 = 6
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6163722c5e529b6a3c4c251554dc60d794a5eb7805b80c9a6059319063dc05b5`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 1883 |
| 2 | success | valid / verified | knowing | procedural | Easy | 1217 |
| 3 | success | valid / verified | knowing | factual | Easy | 1209 |

Run 1 — solusi: 2 + 4 = 6
- Domain kognitif `classify/knowing`: Soal ini menuntut siswa untuk melakukan operasi penjumlahan dasar secara langsung tanpa perlu strategi kompleks.. Bukti: 2 + 4 = ....
- Dimensi pengetahuan `classify/procedural`: Siswa menerapkan prosedur penjumlahan dasar untuk mendapatkan hasil.. Bukti: 2 + 4 = ....
- Intended difficulty `classify/Easy`: Soal operasi penjumlahan dasar satu langkah yang sangat familiar bagi siswa kelas 1.. Bukti: 2 + 4 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah standar kompetensi dasar penjumlahan untuk kelas 1. |

Run 2 — solusi: 2 + 4 = 6
- Domain kognitif `classify/knowing`: Soal ini meminta siswa melakukan operasi penjumlahan dasar secara langsung tanpa konteks atau strategi tambahan.. Bukti: 2 + 4 = .
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menerapkan algoritma penjumlahan dasar (fakta dasar penjumlahan).. Bukti: 2 + 4 = .
- Intended difficulty `classify/Easy`: Soal ini adalah operasi aritmatika dasar satu langkah yang sangat familiar bagi siswa kelas 1.. Bukti: 2 + 4 = .

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan fakta bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan bilangan satu digit adalah standar kompetensi dasar kelas 1. |

Run 3 — solusi: 2 + 4 = 6
- Domain kognitif `classify/knowing`: Soal ini merupakan operasi penjumlahan dasar yang bersifat langsung dan rutin, sehingga masuk dalam kategori knowing.. Bukti: 2 + 4 = .
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman terhadap fakta penjumlahan dasar (basic facts) yang merupakan bagian dari pengetahuan faktual.. Bukti: 2 + 4 = .
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, melibatkan satu operasi penjumlahan tunggal dengan angka kecil, sesuai dengan ekspektasi kemampuan kelas 1.. Bukti: 2 + 4 = .

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan pengenalan angka 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah standar kompetensi awal kelas 1 untuk penjumlahan bilangan cacah di bawah 10. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 2, "factual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2216`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini menuntut siswa untuk melakukan operasi penjumlahan dasar secara langsung (recall/procedural fluency) tanpa perlu strategi kompleks atau pemecahan masalah.
- Dimensi pengetahuan `procedural`: Siswa menerapkan prosedur penjumlahan dasar atau fakta dasar penjumlahan untuk mendapatkan hasil.
- Intended difficulty `Easy`: Soal ini adalah operasi aritmatika dasar satu langkah yang sangat familiar bagi siswa kelas 1, dengan beban kognitif yang rendah.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan fakta bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan bilangan satu digit adalah standar kompetensi dasar kelas 1. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 56/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999843; applying=0.000157; reasoning=0.000000 | knowing | 0.999843 | 0.001397 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.903190; conceptual=0.068881; procedural=0.027928; metacognitive=0.000000 | factual | 0.903190 | 0.271356 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.911800; Medium=0.086037; Hard=0.002163 | Easy | 0.911800 | 0.280817 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999843; −Σp ln(p) = 0.001535; H = 0.001535/ln(3) = 0.001397; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.903190; −Σp ln(p) = 0.376179; H = 0.376179/ln(4) = 0.271356; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.911800; −Σp ln(p) = 0.308509; H = 0.308509/ln(3) = 0.280817; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Berbagai Cara Melakukan Penjumlahan
Tipe soal: multiple_choice
Stimulus: -
Soal: 2 + 4 = ....
Pilihan: A. 4
B. 5
C. 6
D. 7
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 12. Soal `f9582859a11afb87b07d7da8`

1 + 1 = ....

| Opsi | Isi |
|---|---|
| A | 3 |
| B | 1 |
| C | 11 |
| D | 2 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: 1 + 1 = 2
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a1dcc411d94c79b1428719ee9c349533c0529ede7562d249b3ec679fb6c7e992`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 1234 |
| 2 | success | valid / verified | knowing | factual | Easy | 1244 |
| 3 | success | valid / verified | knowing | factual | Easy | 1252 |

Run 1 — solusi: 1 + 1 = 2
- Domain kognitif `classify/knowing`: Soal ini merupakan operasi penjumlahan dasar yang bersifat langsung dan merupakan fakta matematika dasar yang harus diingat siswa kelas 1.. Bukti: 1 + 1 = ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan tentang fakta penjumlahan dasar (basic addition facts).. Bukti: 1 + 1 = ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya melibatkan satu operasi penjumlahan satu digit yang sangat familiar bagi siswa kelas 1.. Bukti: 1 + 1 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan pengenalan angka 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah standar kompetensi awal kelas 1 untuk penjumlahan bilangan cacah sampai 10. |

Run 2 — solusi: 1 + 1 = 2
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk melakukan operasi penjumlahan dasar yang sudah sangat familiar, yang merupakan proses langsung tanpa perlu strategi kompleks.. Bukti: 1 + 1 = ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang fakta dasar penjumlahan bilangan cacah.. Bukti: 1 + 1 = ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, melibatkan operasi tunggal dengan angka kecil yang umum diajarkan di awal kelas 1.. Bukti: 1 + 1 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan pengenalan angka 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Ini adalah standar kompetensi dasar untuk kelas 1 SD dalam operasi hitung penjumlahan bilangan cacah. |

Run 3 — solusi: 1 + 1 = 2
- Domain kognitif `classify/knowing`: Soal ini meminta siswa untuk melakukan operasi penjumlahan dasar yang sudah sangat familiar, yang merupakan proses langsung tanpa perlu strategi kompleks.. Bukti: 1 + 1 = ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang fakta dasar penjumlahan (basic addition facts) yang merupakan pengetahuan faktual dalam aritmatika.. Bukti: 1 + 1 = ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, melibatkan satu operasi tunggal dengan angka kecil, dan merupakan prosedur yang sangat rutin bagi siswa kelas 1.. Bukti: 1 + 1 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan pengenalan simbol angka 1 dan 2. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Untuk siswa kelas 1, penjumlahan 1+1 adalah materi awal yang sangat rutin dan tidak memerlukan beban kognitif tinggi. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 56/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999873; applying=0.000127; reasoning=0.000000 | knowing | 0.999873 | 0.001156 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.886842; conceptual=0.079171; procedural=0.033987; metacognitive=0.000000 | factual | 0.886842 | 0.304571 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.909786; Medium=0.088019; Hard=0.002195 | Easy | 0.909786 | 0.285229 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999873; −Σp ln(p) = 0.001270; H = 0.001270/ln(3) = 0.001156; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.886842; −Σp ln(p) = 0.422225; H = 0.422225/ln(4) = 0.304571; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.909786; −Σp ln(p) = 0.313356; H = 0.313356/ln(3) = 0.285229; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Berbagai Cara Melakukan Penjumlahan
Tipe soal: multiple_choice
Stimulus: -
Soal: 1 + 1 = ....
Pilihan: A. 3
B. 1
C. 11
D. 2
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 13. Soal `018e7b45e13d10afc8e87d48`

Ada 3 sepeda Ada 1 becak.<br><br>Berapa jumlah semua rodanya?

| Opsi | Isi |
|---|---|
| A | 9 roda |
| B | 10 roda |
| C | 6 roda |
| D | 8 roda |

![Gambar sumber soal 13](<../images/kelas1_panduan_siswa_kelas1.pdf-0081-01.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: 3 sepeda x 2 roda = 6 roda. 1 becak x 3 roda = 3 roda. Total = 6 + 3 = 9 roda.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0081-01.png. Transkripsi visual: Terdapat 3 sepeda (masing-masing dengan 2 roda) dan 1 becak (dengan 3 roda) di jalan.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `1f833c8b0ecd4eb31cf9207f85e7fbc623d0c1218f8cbf2b0e4e3085e82bc63f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 2522 |
| 2 | success | valid / verified | applying | procedural | Medium | 2559 |
| 3 | success | valid / verified | applying | conceptual | Medium | 2544 |

Run 1 — solusi: 3 sepeda x 2 roda = 6 roda. 1 becak x 3 roda = 3 roda. Total = 6 + 3 = 9 roda.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep perkalian dasar (atau penjumlahan berulang) dan penjumlahan untuk menyelesaikan masalah rutin yang melibatkan objek nyata.. Bukti: Berapa jumlah semua rodanya?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang hubungan antara objek (sepeda/becak) dengan atributnya (jumlah roda) dan bagaimana mengintegrasikannya dalam operasi matematika.. Bukti: 3 sepeda; 1 becak; jumlah semua rodanya
- Intended difficulty `classify/Medium`: Soal ini memerlukan pemahaman pengetahuan dunia (jumlah roda sepeda dan becak) yang mungkin belum diajarkan secara eksplisit di kelas 1, sehingga meningkatkan beban kognitif di luar sekadar operasi hitung.. Bukti: 3 sepeda; 1 becak; jumlah semua rodanya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengetahuan umum tentang jumlah roda pada sepeda (2) dan becak (3), serta kemampuan penjumlahan dasar. |
| dependentSteps | 3 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun operasi hitungnya sederhana, siswa kelas 1 mungkin belum memiliki pengetahuan faktual tentang jumlah roda becak, menjadikannya tantangan menengah. |

Run 2 — solusi: 3 sepeda x 2 roda = 6 roda. 1 becak x 3 roda = 3 roda. Total = 6 + 3 = 9 roda.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep perkalian dasar (atau penjumlahan berulang) untuk menentukan jumlah roda per jenis kendaraan, kemudian menjumlahkannya. Ini adalah penerapan prosedur pada situasi rutin.. Bukti: Berapa jumlah semua rodanya?
- Dimensi pengetahuan `classify/procedural`: Siswa harus memahami struktur objek (sepeda memiliki 2 roda, becak memiliki 3 roda) dan menggunakan algoritma penjumlahan untuk menyelesaikan masalah.. Bukti: 3 sepeda; 1 becak
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk mengidentifikasi jumlah objek, mengalikan dengan jumlah roda per objek, dan menjumlahkan hasilnya. Untuk kelas 1, ini melibatkan beberapa langkah rutin yang saling terkait.. Bukti: 3 sepeda; 1 becak; Berapa jumlah semua rodanya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengetahuan dasar tentang jumlah roda sepeda (2) dan becak (3), serta kemampuan penjumlahan dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 3 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun operasi dasarnya sederhana, siswa kelas 1 mungkin kesulitan mengintegrasikan informasi visual (jumlah kendaraan) dengan pengetahuan dunia nyata (jumlah roda) dan melakukan dua tahap perhitungan (perkalian/penjumlahan berulang lalu penjumlahan total). |

Run 3 — solusi: 3 sepeda x 2 roda = 6 roda. 1 becak x 3 roda = 3 roda. Total = 6 + 3 = 9 roda.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi jumlah roda per objek (konsep sepeda=2, becak=3) dan melakukan operasi penjumlahan untuk mendapatkan total, yang merupakan penerapan konsep matematika pada situasi rutin.. Bukti: Berapa jumlah semua rodanya?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang hubungan antara objek (sepeda/becak) dengan atributnya (jumlah roda) dan bagaimana mengintegrasikan informasi tersebut ke dalam prosedur perhitungan.. Bukti: 3 sepeda; 1 becak
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa untuk melakukan dua langkah perhitungan (perkalian dasar atau penjumlahan berulang) dan satu penjumlahan akhir. Untuk kelas 1, ini melibatkan beberapa langkah rutin yang saling terkait.. Bukti: 3 sepeda; 1 becak; Berapa jumlah semua rodanya?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengetahuan dasar tentang jumlah roda pada sepeda (2) dan becak (3), serta kemampuan penjumlahan dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun operasi dasarnya sederhana, siswa kelas 1 harus melakukan dua tahap perhitungan (menghitung roda sepeda, lalu menambah roda becak) yang sedikit lebih kompleks daripada penjumlahan satu langkah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / adjudicated | Medium |

Adjudikasi AI: `success`; token `3883`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu menerapkan konsep penjumlahan berulang atau perkalian dasar untuk menghitung total roda dari dua jenis objek yang berbeda, yang merupakan penerapan prosedur pada situasi rutin.
- Dimensi pengetahuan `conceptual`: Siswa harus memahami atribut objek (jumlah roda pada sepeda dan becak) dan mengintegrasikannya ke dalam prosedur perhitungan.
- Intended difficulty `Medium`: Soal ini menuntut siswa untuk melakukan dua tahap perhitungan (menghitung roda sepeda, lalu menambah roda becak) yang sedikit lebih kompleks daripada penjumlahan satu langkah.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengetahuan dasar tentang jumlah roda pada sepeda (2) dan becak (3), serta kemampuan penjumlahan dasar. |
| dependentSteps | 3 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 2 |
| calculationLoad | moderate |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Meskipun operasi dasarnya sederhana, siswa kelas 1 harus melakukan dua tahap perhitungan (menghitung roda sepeda, lalu menambah roda becak) yang sedikit lebih kompleks daripada penjumlahan satu langkah. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 85/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000338; applying=0.999662; reasoning=0.000000 | applying | 0.999662 | 0.002768 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.365663; conceptual=0.620649; procedural=0.013688; metacognitive=0.000000 | conceptual | 0.620649 | 0.521286 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.806449; Medium=0.190271; Hard=0.003280 | Easy | 0.806449 | 0.462364 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999662; −Σp ln(p) = 0.003041; H = 0.003041/ln(3) = 0.002768; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.620649; −Σp ln(p) = 0.722656; H = 0.722656/ln(4) = 0.521286; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.806449; −Σp ln(p) = 0.507959; H = 0.507959/ln(3) = 0.462364; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Soal Cerita Penjumlahan
Tipe soal: multiple_choice
Stimulus: -
Soal: Ada 3 sepeda Ada 1 becak.

Berapa jumlah semua rodanya?
Pilihan: A. 9 roda
B. 10 roda
C. 6 roda
D. 8 roda
Transkripsi visual: Terdapat 3 sepeda (masing-masing dengan 2 roda) dan 1 becak (dengan 3 roda) di jalan.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 14. Soal `ef576d96de5e9070503cfdbb`

Ada 3 motor. Ada 2 mobil.<br><br>Berapa jumlah semua kendaraan?

| Opsi | Isi |
|---|---|
| A | 6 |
| B | 3 |
| C | 5 |
| D | 4 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: 3 + 2 = 5
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `dc6e657c2d796e973f64cab165218a28df33db4a1bbd7cb6c2bbc1b1b636db80`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 1265 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 1230 |
| 3 | success | valid / verified | knowing | procedural | Easy | 1279 |

Run 1 — solusi: 3 + 2 = 5
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi penjumlahan dasar (3+2) yang merupakan proses langsung dan rutin untuk tingkat kelas 1.. Bukti: Ada 3 motor. Ada 2 mobil.; Berapa jumlah semua kendaraan?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep dasar penjumlahan sebagai penggabungan dua kelompok objek.. Bukti: 3 motor; 2 mobil; jumlah semua
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, melibatkan satu operasi penjumlahan sederhana dengan angka kecil, cocok untuk tingkat kelas 1.. Bukti: Ada 3 motor. Ada 2 mobil.; Berapa jumlah semua kendaraan?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan pengenalan angka 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan standar kompetensi penjumlahan dasar untuk kelas 1 SD. |

Run 2 — solusi: 3 + 2 = 5
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi penjumlahan dasar yang merupakan prosedur rutin dan langsung.. Bukti: Ada 3 motor; Ada 2 mobil; Berapa jumlah semua kendaraan?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep penjumlahan dasar sebagai penggabungan dua kelompok benda.. Bukti: 3 motor; 2 mobil; jumlah semua
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, melibatkan satu operasi penjumlahan sederhana dengan angka kecil yang familiar bagi siswa kelas 1.. Bukti: 3 motor; 2 mobil; jumlah semua

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan pengenalan angka 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD yang baru mulai mempelajari penjumlahan dasar dengan objek konkret atau semi-konkret. |

Run 3 — solusi: 3 motor + 2 mobil = 5 kendaraan.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi penjumlahan dasar yang sangat langsung (3+2) untuk menyelesaikan soal cerita sederhana.. Bukti: Ada 3 motor. Ada 2 mobil. Berapa jumlah semua kendaraan?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dasar tentang operasi penjumlahan untuk menggabungkan dua kelompok objek.. Bukti: 3 motor; 2 mobil; jumlah semua
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, menggunakan angka kecil, dan konteks yang sangat familiar bagi siswa kelas 1 tanpa jebakan atau kompleksitas tambahan.. Bukti: Ada 3 motor. Ada 2 mobil.; Berapa jumlah semua kendaraan?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan pengenalan angka 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD yang baru mulai mempelajari penjumlahan bilangan cacah sampai 10. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2381`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu melakukan operasi penjumlahan dasar (3+2) yang merupakan proses langsung dan rutin.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural dasar tentang operasi penjumlahan untuk menggabungkan dua kelompok objek.
- Intended difficulty `Easy`: Soal ini sangat mendasar, melibatkan satu operasi penjumlahan sederhana dengan angka kecil, cocok untuk tingkat kelas 1.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan pengenalan angka 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan standar kompetensi penjumlahan dasar untuk kelas 1 SD. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 60/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999257; applying=0.000743; reasoning=0.000000 | knowing | 0.999257 | 0.005550 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.740123; conceptual=0.226943; procedural=0.032933; metacognitive=0.000000 | factual | 0.740123 | 0.484537 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.855016; Medium=0.142340; Hard=0.002645 | Easy | 0.855016 | 0.388780 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999257; −Σp ln(p) = 0.006097; H = 0.006097/ln(3) = 0.005550; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.740123; −Σp ln(p) = 0.671711; H = 0.671711/ln(4) = 0.484537; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.855016; −Σp ln(p) = 0.427119; H = 0.427119/ln(3) = 0.388780; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Soal Cerita Penjumlahan
Tipe soal: multiple_choice
Stimulus: -
Soal: Ada 3 motor. Ada 2 mobil.

Berapa jumlah semua kendaraan?
Pilihan: A. 6
B. 3
C. 5
D. 4
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 15. Soal `adaec31c66c75d9c825ad888`

9 - ... = 7. Lengkapi operasi pengurangannya.

| Opsi | Isi |
|---|---|
| A | 3 |
| B | 16 |
| C | 2 |
| D | 7 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: 9 - x = 7, maka x = 9 - 7 = 2.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `6657e5a7dd374fc5a9e591aecdccfe82c5b50bccde64092b3db398bb05cefd79`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 1257 |
| 2 | success | valid / verified | knowing | procedural | Easy | 1259 |
| 3 | success | valid / verified | knowing | factual | Easy | 1248 |

Run 1 — solusi: 9 - x = 7, maka x = 9 - 7 = 2.
- Domain kognitif `classify/knowing`: Siswa diminta untuk melengkapi operasi pengurangan dasar yang melibatkan fakta pengurangan sederhana, yang merupakan proses langsung.. Bukti: 9 - ... = 7
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang hubungan antara angka dalam operasi pengurangan dasar (fakta pengurangan).. Bukti: 9 - ... = 7
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, menggunakan angka kecil di bawah 10, dan merupakan prosedur rutin yang familiar bagi siswa kelas 1.. Bukti: 9 - ... = 7

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sesuai dengan standar kelas 1 untuk pengenalan operasi pengurangan dasar dengan angka kecil. |

Run 2 — solusi: 9 - x = 7, maka x = 9 - 7 = 2.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi pengurangan dasar untuk mencari nilai yang hilang (missing subtrahend), yang merupakan proses rutin dalam aritmatika dasar.. Bukti: 9 - ... = 7
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang hubungan antara angka dalam operasi pengurangan dasar.. Bukti: 9 - ... = 7
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, melibatkan satu langkah operasi pengurangan sederhana yang familiar bagi siswa kelas 1.. Bukti: 9 - ... = 7

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 yang menekankan penguasaan fakta dasar pengurangan. |

Run 3 — solusi: 9 - 2 = 7
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi pengurangan dasar atau mencari selisih antara 9 dan 7 untuk melengkapi kalimat matematika tersebut.. Bukti: 9 - ... = 7
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang fakta dasar pengurangan dan hubungan antara angka-angka dalam operasi pengurangan.. Bukti: 9 - ... = 7
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, melibatkan operasi pengurangan satu digit yang familiar bagi siswa kelas 1, dengan beban kognitif yang rendah.. Bukti: 9 - ... = 7

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 yang fokus pada pengenalan operasi pengurangan dasar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2358`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa diminta untuk melengkapi operasi pengurangan dasar dengan mencari nilai yang hilang (missing subtrahend). Ini adalah proses langsung yang mengandalkan fakta pengurangan dasar.
- Dimensi pengetahuan `procedural`: Soal ini menguji penguasaan fakta pengurangan dasar dan hubungan antar angka dalam operasi pengurangan, yang merupakan pengetahuan prosedural dasar.
- Intended difficulty `Easy`: Soal ini sangat mendasar, melibatkan satu langkah operasi pengurangan sederhana yang familiar bagi siswa kelas 1, dengan beban kognitif yang rendah.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 yang menekankan penguasaan fakta dasar pengurangan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 59/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999688; applying=0.000312; reasoning=0.000000 | knowing | 0.999688 | 0.002579 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.665510; conceptual=0.288354; procedural=0.046135; metacognitive=0.000000 | factual | 0.665510 | 0.556523 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.897543; Medium=0.100066; Hard=0.002390 | Easy | 0.897543 | 0.311113 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999688; −Σp ln(p) = 0.002834; H = 0.002834/ln(3) = 0.002579; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.665510; −Σp ln(p) = 0.771504; H = 0.771504/ln(4) = 0.556523; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.897543; −Σp ln(p) = 0.341793; H = 0.341793/ln(3) = 0.311113; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Cerita Pengurangan
Tipe soal: multiple_choice
Stimulus: -
Soal: 9 - ... = 7. Lengkapi operasi pengurangannya.
Pilihan: A. 3
B. 16
C. 2
D. 7
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 16. Soal `91118c063eea5c139d44fcfe`

7 – 2 = ....<br><br>Isilah dengan bilangan yang tepat.

| Opsi | Isi |
|---|---|
| A | 5 |
| B | 2 |
| C | 7 |
| D | 9 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: 7 - 2 = 5
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `41fb0023e17d3c1a2acf03fbc35202320f24c1539eb3cc5a1fe1a2f9ea96c801`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 1236 |
| 2 | success | valid / verified | knowing | factual | Easy | 1237 |
| 3 | success | valid / verified | knowing | procedural | Easy | 1221 |

Run 1 — solusi: 7 dikurangi 2 sama dengan 5.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa melakukan operasi pengurangan dasar secara langsung tanpa konteks tambahan, yang termasuk dalam kategori mengingat atau melakukan proses langsung.. Bukti: 7 – 2 = .
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji kemampuan siswa dalam menerapkan algoritma pengurangan dasar (fakta pengurangan).. Bukti: 7 – 2 = .
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi aritmatika dasar satu langkah yang sangat familiar bagi siswa kelas 1, dengan beban kognitif yang rendah.. Bukti: 7 – 2 = .

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD yang menekankan penguasaan operasi pengurangan dasar hingga 10. |

Run 2 — solusi: 7 dikurangi 2 sama dengan 5.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa melakukan operasi pengurangan dasar secara langsung tanpa konteks tambahan, yang termasuk dalam kategori mengingat atau melakukan proses langsung.. Bukti: 7 – 2 = ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman siswa terhadap fakta dasar pengurangan (operasi aritmatika dasar).. Bukti: 7 – 2 = ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya melibatkan satu operasi pengurangan satu digit yang familiar bagi siswa kelas 1.. Bukti: 7 – 2 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD yang baru mulai mempelajari operasi pengurangan dasar. |

Run 3 — solusi: 7 - 2 = 5
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi pengurangan dasar yang sudah dipelajari sebagai fakta atau prosedur langsung.. Bukti: 7 – 2 = .
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji penguasaan algoritma pengurangan dasar (fakta numerik).. Bukti: 7 – 2 = .
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur rutin yang sangat familiar bagi siswa kelas 1, tidak memerlukan langkah tambahan atau strategi kompleks.. Bukti: 7 – 2 = .

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan dalam rentang 10 adalah standar kompetensi kelas 1 yang bersifat prosedural langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 2, "factual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2296`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta siswa melakukan operasi pengurangan dasar secara langsung, yang merupakan proses mengingat atau menerapkan fakta dasar aritmatika.
- Dimensi pengetahuan `procedural`: Soal ini menguji penguasaan algoritma atau teknik pengurangan dasar yang merupakan bagian dari pengetahuan prosedural.
- Intended difficulty `Easy`: Soal ini adalah operasi aritmatika satu langkah yang sangat mendasar dan rutin bagi siswa kelas 1.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan dalam rentang 10 adalah standar kompetensi dasar kelas 1 SD. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 61/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999992; applying=0.000008; reasoning=0.000000 | knowing | 0.999992 | 0.000094 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.844785; conceptual=0.080631; procedural=0.074584; metacognitive=0.000000 | factual | 0.844785 | 0.388892 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.924665; Medium=0.072464; Hard=0.002871 | Easy | 0.924665 | 0.254342 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999992; −Σp ln(p) = 0.000103; H = 0.000103/ln(3) = 0.000094; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.844785; −Σp ln(p) = 0.539119; H = 0.539119/ln(4) = 0.388892; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.924665; −Σp ln(p) = 0.279424; H = 0.279424/ln(3) = 0.254342; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Cerita Pengurangan
Tipe soal: multiple_choice
Stimulus: -
Soal: 7 – 2 = ....

Isilah dengan bilangan yang tepat.
Pilihan: A. 5
B. 2
C. 7
D. 9
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 17. Soal `7aa38a3601f61c91adbf30d4`

Isilah titik-titik di bawah ini.<br><br> 6 – 4 = .... . Tulis hasil pengurangannya.

| Opsi | Isi |
|---|---|
| A | 10 |
| B | 2 |
| C | 6 |
| D | 3 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: 6 - 4 = 2
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `835f811062828a40c317f03ace17b2abc7bb05f5af01135f575237879175a5b3`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 1240 |
| 2 | success | valid / verified | knowing | factual | Easy | 1254 |
| 3 | success | valid / verified | knowing | procedural | Easy | 1216 |

Run 1 — solusi: 6 dikurangi 4 sama dengan 2.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi pengurangan dasar yang sudah dipelajari, yang merupakan proses langsung.. Bukti: 6 – 4 = ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang fakta dasar pengurangan (fakta aritmatika).. Bukti: 6 – 4 = ....
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi pengurangan satu digit yang sangat mendasar dan rutin bagi siswa kelas 1.. Bukti: 6 – 4 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan 6-4 adalah materi standar kelas 1 yang bersifat prosedural langsung tanpa memerlukan strategi kompleks. |

Run 2 — solusi: 6 dikurangi 4 sama dengan 2.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi pengurangan dasar yang sudah dipelajari, yang merupakan proses langsung.. Bukti: 6 – 4 = ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman terhadap fakta dasar pengurangan (operasi aritmatika dasar).. Bukti: 6 – 4 = ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, melibatkan satu operasi pengurangan satu digit yang familiar bagi siswa kelas 1.. Bukti: 6 – 4 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 yang baru mulai mempelajari pengurangan bilangan di bawah 10. |

Run 3 — solusi: 6 dikurangi 4 sama dengan 2.
- Domain kognitif `classify/knowing`: Soal ini meminta siswa melakukan operasi pengurangan dasar secara langsung, yang termasuk dalam kategori knowing.. Bukti: 6 – 4 = ....
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menerapkan prosedur pengurangan dasar untuk menyelesaikan soal.. Bukti: 6 – 4 = ....
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi pengurangan satu digit yang sangat mendasar dan familiar bagi siswa kelas 1.. Bukti: 6 – 4 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan 6-4 adalah materi standar kelas 1 yang bersifat rutin dan langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2262`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta siswa melakukan operasi pengurangan dasar secara langsung tanpa memerlukan strategi atau pemecahan masalah yang kompleks.
- Dimensi pengetahuan `procedural`: Siswa perlu menerapkan prosedur pengurangan dasar untuk mendapatkan hasil.
- Intended difficulty `Easy`: Soal ini adalah operasi aritmatika dasar satu digit yang sangat rutin dan familiar bagi siswa kelas 1.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan 6-4 adalah materi standar kelas 1 yang bersifat rutin dan langsung. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 71/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999457; applying=0.000543; reasoning=0.000000 | knowing | 0.999457 | 0.004213 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.693774; conceptual=0.160236; procedural=0.145990; metacognitive=0.000000 | factual | 0.693774 | 0.597258 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.915849; Medium=0.081123; Hard=0.003028 | Easy | 0.915849 | 0.274739 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999457; −Σp ln(p) = 0.004629; H = 0.004629/ln(3) = 0.004213; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.693774; −Σp ln(p) = 0.827975; H = 0.827975/ln(4) = 0.597258; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.915849; −Σp ln(p) = 0.301832; H = 0.301832/ln(3) = 0.274739; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Berbagai Cara Melakukan Pengurangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Isilah titik-titik di bawah ini.

 6 – 4 = .... . Tulis hasil pengurangannya.
Pilihan: A. 10
B. 2
C. 6
D. 3
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 18. Soal `dde0b5654f117861d23c7988`

0 1 2 3 4 5 6 7 8 9 10<br><br>Hitunglah. 9 – 3 =

| Opsi | Isi |
|---|---|
| A | 12 |
| B | 3 |
| C | 6 |
| D | 5 |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: 9 dikurangi 3 sama dengan 6. Menggunakan garis bilangan: mulai dari 9, mundur 3 langkah ke kiri (8, 7, 6).
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `95acbbfd9c8e3f1fed341b3ff0b32ca584a67d6fca30ce5fd142dfd51e265df0`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 1282 |
| 2 | success | valid / verified | knowing | procedural | Easy | 1264 |
| 3 | success | valid / verified | knowing | procedural | Easy | 1254 |

Run 1 — solusi: 9 dikurangi 3 sama dengan 6. Menggunakan garis bilangan: mulai dari 9, mundur 3 langkah ke kiri (8, 7, 6).
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi pengurangan dasar yang merupakan prosedur rutin dan langsung.. Bukti: Hitunglah. 9 – 3 =
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma atau teknik pengurangan dasar.. Bukti: 9 – 3 =
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi pengurangan satu digit yang sangat mendasar dan familiar bagi siswa kelas 1.. Bukti: 9 – 3 =

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan urutan bilangan 0-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan 9-3 adalah standar kompetensi dasar kelas 1 SD. |

Run 2 — solusi: 9 dikurangi 3 sama dengan 6. Menggunakan garis bilangan: mulai dari 9, mundur 3 langkah (8, 7, 6), berhenti di 6.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi pengurangan dasar yang merupakan prosedur rutin dan langsung.. Bukti: Hitunglah. 9 – 3 =
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji kemampuan siswa dalam melakukan algoritma pengurangan dasar.. Bukti: 9 – 3 =
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan operasi satu langkah dengan angka kecil.. Bukti: 9 – 3 =

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan penggunaan garis bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan dalam rentang 10 adalah materi standar kelas 1 yang bersifat prosedural langsung. |

Run 3 — solusi: 9 dikurangi 3 sama dengan 6.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi pengurangan dasar yang merupakan prosedur rutin.. Bukti: Hitunglah. 9 – 3 =
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji kemampuan prosedural dasar dalam melakukan operasi pengurangan.. Bukti: 9 – 3 =
- Intended difficulty `classify/Easy`: Soal ini adalah operasi pengurangan satu digit yang sangat mendasar dan familiar bagi siswa kelas 1.. Bukti: 9 – 3 =

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan pengenalan angka 0-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan 9-3 adalah standar kompetensi dasar kelas 1. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 66/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999282; applying=0.000718; reasoning=0.000000 | knowing | 0.999282 | 0.005383 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.885192; conceptual=0.055372; procedural=0.059435; metacognitive=0.000000 | factual | 0.885192 | 0.314477 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.930516; Medium=0.067243; Hard=0.002241 | Easy | 0.930516 | 0.238667 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999282; −Σp ln(p) = 0.005914; H = 0.005914/ln(3) = 0.005383; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.885192; −Σp ln(p) = 0.435958; H = 0.435958/ln(4) = 0.314477; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.930516; −Σp ln(p) = 0.262202; H = 0.262202/ln(3) = 0.238667; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Berbagai Cara Melakukan Pengurangan
Tipe soal: multiple_choice
Stimulus: -
Soal: 0 1 2 3 4 5 6 7 8 9 10

Hitunglah. 9 – 3 =
Pilihan: A. 12
B. 3
C. 6
D. 5
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 19. Soal `b32a5eeea2898efe65526fe5`

9 - ... = 7<br><br>Isilah titik-titik di bawah ini.

| Opsi | Isi |
|---|---|
| A | 2 |
| B | 3 |
| C | 7 |
| D | 16 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: 9 - x = 7, maka x = 9 - 7 = 2.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `121d38127e273c2f06bd5f8e625c2903fcd8f1b97ff36683aaa14bc83ab77324`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 1261 |
| 2 | success | valid / verified | knowing | factual | Easy | 1231 |
| 3 | success | valid / verified | knowing | factual | Easy | 1244 |

Run 1 — solusi: 9 - x = 7, maka x = 9 - 7 = 2.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi pengurangan dasar atau mengingat fakta pengurangan untuk melengkapi kalimat matematika yang diberikan.. Bukti: 9 - ... = 7
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang fakta dasar pengurangan dan hubungan antara angka-angka dalam operasi tersebut.. Bukti: 9 - ... = 7
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur yang sangat familiar bagi siswa kelas 1, melibatkan satu langkah operasi dasar dengan beban kognitif yang rendah.. Bukti: 9 - ... = 7

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sesuai dengan standar kompetensi kelas 1 untuk operasi pengurangan dasar. |

Run 2 — solusi: 9 - x = 7, maka x = 9 - 7 = 2.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi pengurangan dasar atau mengingat fakta pengurangan untuk melengkapi kalimat matematika tersebut.. Bukti: 9 - ... = 7
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang fakta dasar pengurangan dan hubungan antar bilangan.. Bukti: 9 - ... = 7
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, menggunakan representasi simbolik yang umum, dan hanya memerlukan satu langkah operasi pengurangan sederhana.. Bukti: 9 - ... = 7

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena merupakan latihan rutin pengenalan hubungan pengurangan. |

Run 3 — solusi: 9 - x = 7, maka x = 9 - 7 = 2.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi pengurangan dasar untuk menemukan bilangan yang hilang, yang merupakan proses langsung.. Bukti: 9 - ... = 7
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang fakta dasar pengurangan dan hubungan antara angka dalam kalimat matematika sederhana.. Bukti: 9 - ... = 7
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, melibatkan satu langkah operasi pengurangan sederhana dengan angka di bawah 10, sesuai dengan kemampuan kelas 1.. Bukti: 9 - ... = 7

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini merupakan latihan rutin yang sesuai dengan kurikulum kelas 1 untuk memahami hubungan pengurangan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 64/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999997; applying=0.000003; reasoning=0.000000 | knowing | 0.999997 | 0.000042 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.507478; conceptual=0.438746; procedural=0.053776; metacognitive=0.000000 | factual | 0.507478 | 0.622422 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.902504; Medium=0.095505; Hard=0.001991 | Easy | 0.902504 | 0.299707 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999997; −Σp ln(p) = 0.000046; H = 0.000046/ln(3) = 0.000042; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.507478; −Σp ln(p) = 0.862860; H = 0.862860/ln(4) = 0.622422; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.902504; −Σp ln(p) = 0.329262; H = 0.329262/ln(3) = 0.299707; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Hubungan Penjumlahan dan Pengurangan
Tipe soal: multiple_choice
Stimulus: -
Soal: 9 - ... = 7

Isilah titik-titik di bawah ini.
Pilihan: A. 2
B. 3
C. 7
D. 16
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 20. Soal `f6fcf5836947ff740007f70e`

Isilah titik-titik di bawah ini.<br><br>2 + 6 = ....

| Opsi | Isi |
|---|---|
| A | 4 |
| B | 26 |
| C | 9 |
| D | 8 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: 2 + 6 = 8
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `e59716108118ba012471da0433065edb7f88876dde2a106c07d6b59230d383f7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 1224 |
| 2 | success | valid / verified | knowing | factual | Easy | 1224 |
| 3 | success | valid / verified | knowing | procedural | Easy | 1237 |

Run 1 — solusi: 2 + 6 = 8
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi penjumlahan dasar satu digit yang merupakan proses langsung.. Bukti: 2 + 6 = ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang fakta dasar penjumlahan (fakta aritmatika).. Bukti: 2 + 6 = ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, melibatkan prosedur familiar satu langkah tanpa kompleksitas tambahan.. Bukti: 2 + 6 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan pengenalan angka 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD untuk pengenalan operasi penjumlahan dasar. |

Run 2 — solusi: 2 + 6 = 8
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi penjumlahan dasar satu digit yang bersifat langsung dan rutin.. Bukti: 2 + 6 = ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang fakta dasar penjumlahan (fakta aritmatika).. Bukti: 2 + 6 = ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, melibatkan operasi penjumlahan satu digit yang merupakan prosedur familiar bagi siswa kelas 1.. Bukti: 2 + 6 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan pengenalan angka 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi penjumlahan 2+6 adalah standar kurikulum kelas 1 awal yang bersifat rutin dan tidak memerlukan strategi kompleks. |

Run 3 — solusi: 2 + 6 = 8
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan operasi penjumlahan dasar secara langsung tanpa memerlukan strategi kompleks atau penalaran mendalam.. Bukti: 2 + 6 = ....
- Dimensi pengetahuan `classify/procedural`: Siswa perlu menerapkan algoritma penjumlahan dasar yang sudah dipelajari sebagai prosedur rutin.. Bukti: 2 + 6 = ....
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur aritmatika dasar yang sangat familiar bagi siswa kelas 1, hanya melibatkan satu langkah operasi tanpa kendala tambahan.. Bukti: 2 + 6 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan fakta bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi penjumlahan satu digit adalah standar kompetensi dasar kelas 1 yang bersifat rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"factual": 2, "procedural": 1} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2256`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini meminta siswa melakukan operasi penjumlahan dasar satu digit secara langsung, yang merupakan proses mengingat fakta aritmatika atau prosedur yang sangat rutin.
- Dimensi pengetahuan `factual`: Soal ini menguji fakta dasar penjumlahan (fakta aritmatika) yang harus dikuasai siswa kelas 1.
- Intended difficulty `Easy`: Soal ini adalah prosedur aritmatika satu langkah yang sangat familiar dan rutin bagi siswa kelas 1, dengan beban kognitif yang rendah.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan pengenalan angka 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi penjumlahan 2+6 adalah standar kurikulum kelas 1 awal yang bersifat rutin dan mendasar. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 65/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999968; applying=0.000032; reasoning=0.000000 | knowing | 0.999968 | 0.000329 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.616499; conceptual=0.348460; procedural=0.035041; metacognitive=0.000000 | factual | 0.616499 | 0.564807 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.900719; Medium=0.097314; Hard=0.001967 | Easy | 0.900719 | 0.303254 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999968; −Σp ln(p) = 0.000361; H = 0.000361/ln(3) = 0.000329; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.616499; −Σp ln(p) = 0.782989; H = 0.782989/ln(4) = 0.564807; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.900719; −Σp ln(p) = 0.333159; H = 0.333159/ln(3) = 0.303254; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Hubungan Penjumlahan dan Pengurangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Isilah titik-titik di bawah ini.

2 + 6 = ....
Pilihan: A. 4
B. 26
C. 9
D. 8
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 21. Soal `63d056eda46964278255c543`

Malosi mempunyai 9 kelereng. Malosi memberi Kira 2 kelereng. Malosi juga memberi Upe 4 kelereng.<br><br>Berapakah sisa kelereng Malosi?

| Opsi | Isi |
|---|---|
| A | 3 kelereng |
| B | 7 kelereng |
| C | 5 kelereng |
| D | 15 kelereng |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: 9 - 2 - 4 = 3
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `808582396e3489bd50f5c434466f54c849fcc9e0fe1b2f50232ec4c8f827176e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1373 |
| 2 | success | valid / verified | applying | procedural | Easy | 1382 |
| 3 | success | valid / verified | applying | procedural | Easy | 1372 |

Run 1 — solusi: 9 - 2 - 4 = 3
- Domain kognitif `classify/applying`: Siswa perlu menerapkan operasi pengurangan dua kali secara berurutan untuk menyelesaikan masalah cerita sederhana, yang termasuk dalam kategori applying.. Bukti: Malosi mempunyai 9 kelereng. Malosi memberi Kira 2 kelereng. Malosi juga memberi Upe 4 kelereng.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi pengurangan dasar dalam konteks cerita.. Bukti: Berapakah sisa kelereng Malosi?
- Intended difficulty `classify/Easy`: Soal ini melibatkan prosedur pengurangan rutin yang familiar bagi siswa kelas 1 dengan angka kecil, sehingga dikategorikan mudah.. Bukti: 9 kelereng; memberi Kira 2 kelereng; memberi Upe 4 kelereng

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan kemampuan menghitung mundur atau pengurangan beruntun. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan dua tahap dengan angka di bawah 10 adalah standar kompetensi kelas 1. |

Run 2 — solusi: 9 - 2 - 4 = 3
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pengurangan dua tahap (9-2-4) pada situasi rutin soal cerita.. Bukti: Malosi mempunyai 9 kelereng. Malosi memberi Kira 2 kelereng. Malosi juga memberi Upe 4 kelereng.
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman algoritma pengurangan berulang atau pengurangan bertahap.. Bukti: Malosi mempunyai 9 kelereng. Malosi memberi Kira 2 kelereng. Malosi juga memberi Upe 4 kelereng.
- Intended difficulty `classify/Easy`: Soal ini melibatkan dua langkah pengurangan rutin yang sangat umum untuk kelas 1, dengan beban kognitif yang rendah.. Bukti: 9 kelereng; memberi Kira 2 kelereng; memberi Upe 4 kelereng

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan pengurangan bilangan 1-10. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal cerita pengurangan dua tahap adalah standar kompetensi kelas 1 SD untuk menguji pemahaman operasi hitung dasar dalam konteks sehari-hari. |

Run 3 — solusi: 9 - 2 - 4 = 3
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pengurangan dua kali secara berurutan untuk menyelesaikan masalah rutin ini.. Bukti: Malosi mempunyai 9 kelereng. Malosi memberi Kira 2 kelereng. Malosi juga memberi Upe 4 kelereng.
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan algoritma pengurangan dasar (prosedural) untuk menyelesaikan masalah cerita.. Bukti: 9 kelereng; memberi Kira 2 kelereng; memberi Upe 4 kelereng
- Intended difficulty `classify/Easy`: Soal ini melibatkan dua langkah pengurangan berurutan yang merupakan prosedur standar untuk kelas 1.. Bukti: 9 kelereng; memberi Kira 2 kelereng; memberi Upe 4 kelereng

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pengurangan dasar bilangan 1-10 |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Masalah pengurangan dua langkah adalah standar untuk akhir kelas 1, namun konteksnya sangat familiar dan konkret. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 87/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000122; applying=0.999878; reasoning=0.000000 | applying | 0.999878 | 0.001115 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.198759; conceptual=0.732509; procedural=0.068732; metacognitive=0.000000 | conceptual | 0.732509 | 0.528874 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.813451; Medium=0.183144; Hard=0.003406 | Easy | 0.813451 | 0.453470 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999878; −Σp ln(p) = 0.001225; H = 0.001225/ln(3) = 0.001115; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.732509; −Σp ln(p) = 0.733175; H = 0.733175/ln(4) = 0.528874; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.813451; −Σp ln(p) = 0.498188; H = 0.498188/ln(3) = 0.453470; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Soal Cerita Pengurangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Malosi mempunyai 9 kelereng. Malosi memberi Kira 2 kelereng. Malosi juga memberi Upe 4 kelereng.

Berapakah sisa kelereng Malosi?
Pilihan: A. 3 kelereng
B. 7 kelereng
C. 5 kelereng
D. 15 kelereng
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 22. Soal `9948cc37d48fcfe7ef094209`

Ibu mempunyai 6 telur. Sebanyak 2 telur milik Ibu pecah.<br><br>Berapakah sisa telur Ibu sekarang?

| Opsi | Isi |
|---|---|
| A | 3 telur |
| B | 8 telur |
| C | 4 telur |
| D | 6 telur |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: 6 - 2 = 4
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `66c0a95a0b034cd7425ce9e1ec3d88eb3102f5a9988ac92442555547edfe7030`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1316 |
| 2 | success | valid / verified | applying | procedural | Easy | 1303 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1295 |

Run 1 — solusi: 6 - 2 = 4
- Domain kognitif `classify/applying`: Siswa hanya perlu menerapkan operasi pengurangan dasar yang sudah dipelajari di kelas 1 untuk menyelesaikan masalah rutin ini.. Bukti: Ibu mempunyai 6 telur. Sebanyak 2 telur milik Ibu pecah.; Berapakah sisa telur Ibu sekarang?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi pengurangan dasar (algoritma pengurangan) dalam konteks cerita sederhana.. Bukti: 6 telur; 2 telur; sisa telur
- Intended difficulty `classify/Easy`: Soal ini sangat standar untuk kelas 1, menggunakan angka kecil di bawah 10, dan konteks yang sangat familiar (pengurangan sebagai sisa).. Bukti: 6 telur; 2 telur; pecah; sisa

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan kemampuan menghitung mundur atau menggunakan pasangan bilangan (number bonds) hingga 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD yang fokus pada operasi hitung dasar bilangan cacah sampai 20. |

Run 2 — solusi: 6 - 2 = 4
- Domain kognitif `classify/applying`: Siswa hanya perlu menerapkan operasi pengurangan dasar yang sudah dipelajari di kelas 1 untuk menyelesaikan situasi rutin.. Bukti: Ibu mempunyai 6 telur. Sebanyak 2 telur milik Ibu pecah. Berapakah sisa telur Ibu sekarang?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang operasi pengurangan dasar (algoritma pengurangan) untuk menyelesaikan masalah kontekstual sederhana.. Bukti: 6 telur; 2 telur; sisa
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah satu langkah yang sangat mendasar dan familiar bagi siswa kelas 1, dengan beban kognitif yang rendah.. Bukti: 6 telur; 2 telur; sisa

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 yang menekankan operasi pengurangan bilangan cacah sampai 10. |

Run 3 — solusi: 6 - 2 = 4
- Domain kognitif `classify/applying`: Siswa diminta menerapkan operasi pengurangan dasar pada situasi rutin yang disajikan dalam bentuk cerita pendek.. Bukti: Ibu mempunyai 6 telur; 2 telur milik Ibu pecah; Berapakah sisa telur Ibu sekarang?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep pengurangan sebagai proses pengambilan atau pengurangan jumlah objek.. Bukti: 6 telur; 2 telur; sisa telur
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan operasi pengurangan satu digit yang familiar dengan konteks sehari-hari.. Bukti: 6 telur; 2 telur; sisa telur

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan kemampuan menghitung mundur atau menggunakan fakta pengurangan 6-2. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD yang fokus pada operasi hitung dasar dalam lingkup 10-20. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2487`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan operasi pengurangan dasar pada situasi rutin yang disajikan dalam bentuk cerita pendek.
- Dimensi pengetahuan `procedural`: Soal ini menguji pemahaman prosedural tentang operasi pengurangan dasar (algoritma pengurangan) untuk menyelesaikan masalah kontekstual sederhana.
- Intended difficulty `Easy`: Soal ini merupakan masalah satu langkah yang sangat mendasar dan familiar bagi siswa kelas 1, dengan beban kognitif yang rendah.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan fakta pengurangan bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 yang menekankan operasi pengurangan bilangan cacah sampai 10. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 69/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.078699; applying=0.921301; reasoning=0.000000 | applying | 0.921301 | 0.250845 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.454706; conceptual=0.478181; procedural=0.067112; metacognitive=0.000000 | conceptual | 0.478181 | 0.643758 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.906485; Medium=0.089075; Hard=0.004440 | Easy | 0.906485 | 0.298977 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.921301; −Σp ln(p) = 0.275581; H = 0.275581/ln(3) = 0.250845; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.478181; −Σp ln(p) = 0.892438; H = 0.892438/ln(4) = 0.643758; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.906485; −Σp ln(p) = 0.328460; H = 0.328460/ln(3) = 0.298977; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Soal Cerita Pengurangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Ibu mempunyai 6 telur. Sebanyak 2 telur milik Ibu pecah.

Berapakah sisa telur Ibu sekarang?
Pilihan: A. 3 telur
B. 8 telur
C. 4 telur
D. 6 telur
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 23. Soal `355049fbd1c523a25cd2de3d`

Apa bentuk dari gambar berikut?

| Opsi | Isi |
|---|---|
| A | Bentuk bintang |
| B | Segi empat |
| C | Segitiga |
| D | Bentuk lengkung |

![Gambar sumber soal 23](<../images/kelas1_panduan_siswa_kelas1.pdf-0134-03.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Gambar memiliki tiga sisi lurus dan tiga sudut, yang merupakan ciri khas dari bentuk segitiga.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0134-03.png. Transkripsi visual: Gambar menunjukkan sebuah bangun datar berwarna ungu dengan tiga sisi lurus dan tiga sudut, yang secara geometris merupakan segitiga.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `cf0be1293ee3cfb1d576b73a203b2ddeaf75ab981c91802b291171180fd58330`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 2432 |
| 2 | success | valid / verified | knowing | factual | Easy | 2455 |
| 3 | success | valid / verified | knowing | factual | Easy | 2445 |

Run 1 — solusi: Gambar memiliki tiga sisi lurus dan tiga sudut, yang merupakan ciri khas dari bentuk segitiga.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali dan mengidentifikasi bentuk geometris dasar (segitiga) dari representasi visual yang diberikan. Ini adalah proses pengenalan langsung.. Bukti: Apa bentuk dari gambar berikut?; Gambar menunjukkan sebuah bangun datar berwarna ungu dengan tiga sisi lurus dan tiga sudut
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual tentang nama-nama bentuk dasar (segitiga) dan pengenalan visual terhadap bentuk tersebut.. Bukti: Apa bentuk dari gambar berikut?
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan pengenalan bentuk visual sederhana tanpa langkah prosedural yang kompleks.. Bukti: Apa bentuk dari gambar berikut?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal nama-nama bangun datar dasar (segitiga, segi empat, lingkaran). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Siswa kelas 1 diharapkan sudah mampu mengidentifikasi bentuk dasar seperti segitiga secara visual. |

Run 2 — solusi: Gambar memiliki tiga sisi lurus dan tiga sudut, yang merupakan definisi visual dari segitiga.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali dan mengidentifikasi bentuk geometris dasar (segitiga) berdasarkan atribut visual langsung.. Bukti: Apa bentuk dari gambar berikut?; Gambar menunjukkan sebuah bangun datar berwarna ungu dengan tiga sisi lurus dan tiga sudut
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual tentang nama-nama bentuk dasar (segitiga).. Bukti: Apa bentuk dari gambar berikut?; Gambar menunjukkan sebuah bangun datar berwarna ungu dengan tiga sisi lurus dan tiga sudut
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan pengenalan visual langsung terhadap bentuk geometri yang umum diajarkan di kelas 1.. Bukti: Apa bentuk dari gambar berikut?; Gambar menunjukkan sebuah bangun datar berwarna ungu dengan tiga sisi lurus dan tiga sudut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk-bentuk dasar (segitiga, lingkaran, segi empat). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena hanya menuntut pengenalan visual bentuk dasar tanpa operasi atau analisis kompleks. |

Run 3 — solusi: Gambar memiliki tiga sisi lurus dan tiga sudut, yang merupakan definisi visual dari segitiga.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali dan mengidentifikasi bentuk geometris dasar (segitiga) berdasarkan atribut visual langsung.. Bukti: Apa bentuk dari gambar berikut?; Gambar menunjukkan sebuah bangun datar berwarna ungu dengan tiga sisi lurus dan tiga sudut
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual tentang nama-nama bentuk bangun datar dasar.. Bukti: Apa bentuk dari gambar berikut?; Gambar menunjukkan sebuah bangun datar berwarna ungu dengan tiga sisi lurus dan tiga sudut
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan pengenalan visual langsung terhadap bentuk geometri standar yang diajarkan di kelas 1.. Bukti: Apa bentuk dari gambar berikut?; Gambar menunjukkan sebuah bangun datar berwarna ungu dengan tiga sisi lurus dan tiga sudut

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal nama-nama bangun datar dasar (segitiga, segi empat, lingkaran). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD yang fokus pada pengenalan bentuk bangun datar sederhana. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 78/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.986166; applying=0.013834; reasoning=0.000000 | knowing | 0.986166 | 0.066409 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.846495; conceptual=0.149835; procedural=0.003670; metacognitive=0.000000 | factual | 0.846495 | 0.321770 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.896061; Medium=0.101122; Hard=0.002817 | Easy | 0.896061 | 0.315485 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.986166; −Σp ln(p) = 0.072958; H = 0.072958/ln(3) = 0.066409; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.846495; −Σp ln(p) = 0.446068; H = 0.446068/ln(4) = 0.321770; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.896061; −Σp ln(p) = 0.346596; H = 0.346596/ln(3) = 0.315485; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Mendeskripsikan Benda Berdasarkan Bentuk
Tipe soal: multiple_choice
Stimulus: -
Soal: Apa bentuk dari gambar berikut?
Pilihan: A. Bentuk bintang
B. Segi empat
C. Segitiga
D. Bentuk lengkung
Transkripsi visual: Gambar menunjukkan sebuah bangun datar berwarna ungu dengan tiga sisi lurus dan tiga sudut, yang secara geometris merupakan segitiga.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 24. Soal `83dd4d12892fc170e56f4e1b`

Pasangkan bentuk dengan namanya. Bangun keempat dari atas.

| Opsi | Isi |
|---|---|
| A | Bentuk lengkung |
| B | Bentuk bintang |
| C | Segi empat |
| D | Segitiga |

![Gambar sumber soal 24](<../images/kelas1_panduan_siswa_kelas1.pdf-0153-01.png>)


![Gambar sumber soal 24](<../images/kelas1_panduan_siswa_kelas1.pdf-0153-02.png>)


![Gambar sumber soal 24](<../images/kelas1_panduan_siswa_kelas1.pdf-0153-03.png>)


![Gambar sumber soal 24](<../images/kelas1_panduan_siswa_kelas1.pdf-0153-04.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Bangun keempat dari atas adalah lingkaran merah. Lingkaran memiliki sisi lengkung dan tidak memiliki sudut, sehingga sesuai dengan deskripsi 'Bentuk lengkung'.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0153-01.png, images/kelas1_panduan_siswa_kelas1.pdf-0153-02.png, images/kelas1_panduan_siswa_kelas1.pdf-0153-03.png, images/kelas1_panduan_siswa_kelas1.pdf-0153-04.png. Transkripsi visual: Terdapat empat bangun datar yang disusun vertikal dari atas ke bawah: 1. Persegi berwarna biru, 2. Segitiga berwarna ungu, 3. Persegi panjang berwarna biru, 4. Lingkaran berwarna merah.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f24990388808ccc8e48ed63ad617f4a34080b4d9eb94df00eec32d5d0dbd6a7f`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 5769 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 5741 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 5724 |

Run 1 — solusi: Bangun keempat dari atas adalah lingkaran merah. Lingkaran memiliki sisi lengkung dan tidak memiliki sudut, sehingga sesuai dengan deskripsi 'Bentuk lengkung'.
- Domain kognitif `classify/knowing`: Siswa perlu mengidentifikasi urutan posisi (keempat) dan mengenali properti geometris dasar (lingkaran) untuk mencocokkannya dengan label yang diberikan.. Bukti: Pasangkan bentuk dengan namanya; Bangun keempat dari atas
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap kategori bentuk geometri dasar (lingkaran vs poligon) dan terminologi terkait.. Bukti: Bentuk lengkung; Segi empat; Segitiga
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, hanya memerlukan kemampuan menghitung urutan sederhana dan pengenalan bentuk visual yang sangat umum.. Bukti: Bangun keempat dari atas; Pasangkan bentuk dengan namanya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung urutan 1-4 dan pengenalan bentuk dasar (lingkaran, segitiga, persegi). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 yang fokus pada pengenalan bentuk dan posisi benda. |

Run 2 — solusi: Bangun keempat dari atas adalah lingkaran merah. Lingkaran adalah bentuk lengkung.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi bentuk geometri dasar (lingkaran) berdasarkan posisi dalam urutan. Ini adalah proses mengenali dan mengklasifikasikan objek visual sederhana.. Bukti: Pasangkan bentuk dengan namanya; Bangun keempat dari atas
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang properti bentuk geometri (lingkaran memiliki sisi lengkung) dan kemampuan mengidentifikasi objek berdasarkan kategori bentuk.. Bukti: Bentuk lengkung; Bangun keempat dari atas
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan penghitungan posisi sederhana (ordinal) dan pengenalan bentuk geometri dasar yang familiar.. Bukti: Bangun keempat dari atas; Pasangkan bentuk dengan namanya

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung urutan 1-4 dan mengenal bentuk dasar (lingkaran, segitiga, persegi). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena hanya memerlukan pengenalan visual bentuk dasar dan urutan posisi sederhana. |

Run 3 — solusi: Bangun keempat dari atas adalah lingkaran merah, yang merupakan bentuk lengkung.
- Domain kognitif `classify/knowing`: Siswa perlu mengidentifikasi urutan (posisi keempat) dan mengenali atribut bentuk (lingkaran sebagai bentuk lengkung). Ini adalah proses pengenalan langsung.. Bukti: Pasangkan bentuk dengan namanya; Bangun keempat dari atas
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang kategori bentuk (lingkaran vs poligon) dan terminologi dasar.. Bukti: Pasangkan bentuk dengan namanya; Bentuk lengkung
- Intended difficulty `classify/Easy`: Tugas ini sangat mendasar, melibatkan penghitungan urutan sederhana dan pengenalan visual bentuk geometri dasar yang umum diajarkan di kelas 1.. Bukti: Bangun keempat dari atas

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung urutan 1-4 dan mengenali bentuk dasar (lingkaran). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena hanya memerlukan identifikasi visual dan urutan sederhana tanpa operasi matematika kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 98/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.987719; applying=0.012281; reasoning=0.000000 | knowing | 0.987719 | 0.060294 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.326479; conceptual=0.667217; procedural=0.006304; metacognitive=0.000000 | conceptual | 0.667217 | 0.481414 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.873796; Medium=0.123436; Hard=0.002769 | Easy | 0.873796 | 0.357196 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.987719; −Σp ln(p) = 0.066240; H = 0.066240/ln(3) = 0.060294; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.667217; −Σp ln(p) = 0.667381; H = 0.667381/ln(4) = 0.481414; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.873796; −Σp ln(p) = 0.392420; H = 0.392420/ln(3) = 0.357196; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Mendeskripsikan Benda Berdasarkan Bentuk
Tipe soal: multiple_choice
Stimulus: -
Soal: Pasangkan bentuk dengan namanya. Bangun keempat dari atas.
Pilihan: A. Bentuk lengkung
B. Bentuk bintang
C. Segi empat
D. Segitiga
Transkripsi visual: Terdapat empat bangun datar yang disusun vertikal dari atas ke bawah: 1. Persegi berwarna biru, 2. Segitiga berwarna ungu, 3. Persegi panjang berwarna biru, 4. Lingkaran berwarna merah.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 25. Soal `98891851d1e28d6d8482ab94`

Pilih jawaban yang benar. Bangun yang satu kelompok dengan gambar di atas.

| Opsi | Isi |
|---|---|
| A | Persegi panjang berwarna ungu |
| B | Segitiga terbalik berwarna ungu |
| C | Persegi berwarna ungu |
| D | Oval berwarna ungu |

![Gambar sumber soal 25](<../images/kelas1_panduan_siswa_kelas1.pdf-0143-05.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Ketiga gambar acuan adalah segitiga. Pilihan B adalah satu-satunya segitiga, sehingga termasuk dalam kelompok yang sama berdasarkan bentuk.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0143-05.png. Transkripsi visual: Terdapat tiga bangun datar di dalam kotak: segitiga siku-siku berwarna ungu, segitiga sama kaki berwarna oranye, dan segitiga sama kaki yang lebih tinggi berwarna merah muda. Ketiganya memiliki bentuk dasar segitiga namun berbeda warna dan ukuran.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `3ea66dc81c2f32ec95e120e20f7d66a8c4015760c512915e0176141242fadb8a`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2566 |
| 2 | success | valid / verified | applying | conceptual | Medium | 2575 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2551 |

Run 1 — solusi: Ketiga gambar acuan adalah segitiga. Pilihan B adalah satu-satunya segitiga, sehingga termasuk dalam kelompok yang sama berdasarkan bentuk.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi atribut pembeda (bentuk) dan mengabaikan atribut pengecoh (warna/ukuran) untuk mengklasifikasikan objek ke dalam kelompok yang benar.. Bukti: Bangun yang satu kelompok dengan gambar di atas; Ketiga bangun acuan... sama-sama berbentuk segitiga
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang klasifikasi bangun datar berdasarkan sifat geometris (bentuk) daripada atribut visual permukaan (warna).. Bukti: Mengelompokkan Benda; sama-sama berbentuk segitiga
- Intended difficulty `classify/Easy`: Soal ini menuntut siswa untuk melakukan abstraksi bentuk sederhana. Meskipun ada pengecoh warna, konsep segitiga adalah materi dasar kelas 1.. Bukti: Bangun yang satu kelompok dengan gambar di atas; Ketiga bangun acuan (ungu, oranye, merah muda) sama-sama berbentuk segitiga

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar bangun datar (segitiga). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 1 sudah diajarkan untuk mengelompokkan benda berdasarkan ciri fisik. Membedakan bentuk dari warna adalah tugas rutin pada tingkat ini. |

Run 2 — solusi: Ketiga gambar acuan adalah segitiga. Pilihan B adalah satu-satunya segitiga, sehingga termasuk dalam kelompok yang sama berdasarkan bentuk.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi atribut pembeda (bentuk) di antara berbagai atribut (warna, ukuran) untuk mengelompokkan objek. Ini melibatkan penerapan konsep klasifikasi bangun datar.. Bukti: Bangun yang satu kelompok dengan gambar di atas; Ketiga bangun acuan... sama-sama berbentuk segitiga
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang atribut bangun datar (segitiga) sebagai dasar pengelompokan, bukan sekadar menghafal fakta.. Bukti: Mengelompokkan Benda; sama-sama berbentuk segitiga
- Intended difficulty `classify/Medium`: Soal ini tergolong Medium untuk kelas 1 karena siswa harus mengabaikan distraktor visual yang kuat (warna) dan fokus pada atribut bentuk yang konsisten di antara tiga contoh yang berbeda ukuran dan orientasi.. Bukti: Mengelompokkan Benda; tiga buah bangun datar... warna dan ukurannya berbeda

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar segitiga dan kemampuan membedakan atribut objek (warna vs bentuk). |
| dependentSteps | 2 |
| routineStatus | routine_selection |
| strategySelection | True |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | strong |
| gradeRelativeRationale | Untuk kelas 1, kemampuan mengabstraksi bentuk di tengah variasi warna dan ukuran adalah tantangan kognitif yang sesuai untuk tingkat menengah. |

Run 3 — solusi: Ketiga gambar acuan adalah segitiga dengan warna dan ukuran berbeda. Maka, kelompok tersebut didasarkan pada bentuk (segitiga). Opsi B adalah satu-satunya segitiga.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi atribut pembeda (bentuk vs warna) untuk mengelompokkan objek. Ini melibatkan penerapan konsep klasifikasi bentuk.. Bukti: Bangun yang satu kelompok dengan gambar di atas; Ketiga bangun acuan... sama-sama berbentuk segitiga
- Dimensi pengetahuan `classify/conceptual`: Siswa harus memahami prinsip klasifikasi berdasarkan atribut bentuk, mengabaikan atribut irelevan seperti warna atau ukuran.. Bukti: Mengelompokkan Benda; sama-sama berbentuk segitiga meski warna dan ukurannya berbeda
- Intended difficulty `classify/Easy`: Soal ini menuntut siswa kelas 1 untuk melakukan abstraksi bentuk sederhana. Ini adalah tugas rutin dalam kurikulum awal.. Bukti: Mengelompokkan Benda; tiga bangun acuan... sama-sama berbentuk segitiga

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar (segitiga) dan kemampuan membedakan atribut objek (warna vs bentuk). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena menguji kemampuan klasifikasi dasar yang merupakan kompetensi inti geometri awal. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 2, "Medium": 1} | majority_2_of_3 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3921`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu mengidentifikasi atribut pembeda (bentuk) dan mengabaikan atribut pengecoh (warna/ukuran) untuk mengklasifikasikan objek ke dalam kelompok yang benar.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang klasifikasi bangun datar berdasarkan sifat geometris (bentuk) daripada atribut visual permukaan (warna).
- Intended difficulty `Easy`: Soal ini menuntut siswa kelas 1 untuk melakukan abstraksi bentuk sederhana. Meskipun ada pengecoh warna, konsep segitiga adalah materi dasar kelas 1.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar bangun datar (segitiga). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 1 sudah diajarkan untuk mengelompokkan benda berdasarkan ciri fisik. Membedakan bentuk dari warna adalah tugas rutin pada tingkat ini. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 112/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.002169; applying=0.997831; reasoning=0.000000 | applying | 0.997831 | 0.014081 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.418030; conceptual=0.575849; procedural=0.006121; metacognitive=0.000000 | conceptual | 0.575849 | 0.514766 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.873393; Medium=0.124150; Hard=0.002457 | Easy | 0.873393 | 0.356816 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.997831; −Σp ln(p) = 0.015469; H = 0.015469/ln(3) = 0.014081; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.575849; −Σp ln(p) = 0.713618; H = 0.713618/ln(4) = 0.514766; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.873393; −Σp ln(p) = 0.392002; H = 0.392002/ln(3) = 0.356816; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Mengelompokkan Benda
Tipe soal: multiple_choice
Stimulus: -
Soal: Pilih jawaban yang benar. Bangun yang satu kelompok dengan gambar di atas.
Pilihan: A. Persegi panjang berwarna ungu
B. Segitiga terbalik berwarna ungu
C. Persegi berwarna ungu
D. Oval berwarna ungu
Transkripsi visual: Terdapat tiga bangun datar di dalam kotak: segitiga siku-siku berwarna ungu, segitiga sama kaki berwarna oranye, dan segitiga sama kaki yang lebih tinggi berwarna merah muda. Ketiganya memiliki bentuk dasar segitiga namun berbeda warna dan ukuran.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 26. Soal `7bde28fb9ff374327ad9c3ae`

Bangun yang satu warna dengan gambar di atas.

| Opsi | Isi |
|---|---|
| A | Persegi berwarna ungu |
| B | Oval berwarna hijau |
| C | Persegi panjang berwarna biru |
| D | Segitiga terbalik berwarna merah muda |

![Gambar sumber soal 26](<../images/kelas1_panduan_siswa_kelas1.pdf-0144-00.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Gambar acuan berisi bangun-bangun berwarna merah muda. Pilihan D adalah satu-satunya bangun yang berwarna merah muda, sehingga sesuai dengan kriteria warna.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0144-00.png. Transkripsi visual: Terdapat kotak berisi tiga bangun datar berwarna merah muda: persegi panjang, segitiga siku-siku, dan persegi panjang vertikal. Di bawahnya terdapat tiga pilihan bangun: segitiga terbalik berwarna merah muda, persegi berwarna ungu, dan oval berwarna hijau.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `d7d5a29d7aa50223a7b8e662b6fbc06eb39fdedb7fab88ffac5ffe33fe4ccadf`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2475 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2493 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2498 |

Run 1 — solusi: Gambar acuan berisi bangun-bangun berwarna merah muda. Pilihan D adalah satu-satunya bangun yang berwarna merah muda, sehingga sesuai dengan kriteria warna.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali atribut warna (merah muda) dan mencocokkannya dengan pilihan yang tersedia. Ini adalah proses pengenalan visual langsung tanpa perlu strategi kompleks.. Bukti: Bangun yang satu warna dengan gambar di atas.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang atribut dasar benda (warna) sebagai kategori pengelompokan.. Bukti: Bangun yang satu warna dengan gambar di atas.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan pengenalan atribut visual tunggal (warna) dengan pilihan yang jelas.. Bukti: Bangun yang satu warna dengan gambar di atas.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membedakan warna dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena hanya memerlukan observasi visual sederhana untuk mengelompokkan benda berdasarkan satu atribut yang menonjol. |

Run 2 — solusi: Tiga bangun di kotak atas berwarna merah muda. Pilihan D adalah satu-satunya bangun yang berwarna merah muda.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali atribut warna (merah muda) dari sekumpulan objek dan mencocokkannya dengan pilihan yang tersedia. Ini adalah proses pengenalan langsung.. Bukti: Bangun yang satu warna dengan gambar di atas.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang atribut warna sebagai dasar pengelompokan atau klasifikasi benda, yang merupakan pengetahuan konseptual dasar.. Bukti: Bangun yang satu warna dengan gambar di atas.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, hanya melibatkan satu atribut visual (warna) tanpa distraktor yang rumit.. Bukti: Bangun yang satu warna dengan gambar di atas.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mampu membedakan warna dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | weak |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena hanya menuntut kemampuan observasi visual sederhana untuk mengelompokkan benda berdasarkan satu atribut fisik yang jelas. |

Run 3 — solusi: Gambar acuan di dalam kotak semuanya berwarna merah muda. Pilihan D adalah satu-satunya bangun yang berwarna merah muda, sehingga sesuai dengan kriteria warna.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali atribut warna (merah muda) dan mencocokkannya dengan pilihan yang tersedia. Ini adalah proses pengenalan visual langsung tanpa perlu strategi kompleks.. Bukti: Bangun yang satu warna dengan gambar di atas.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep atribut warna sebagai dasar pengelompokan benda.. Bukti: Bangun yang satu warna dengan gambar di atas.
- Intended difficulty `classify/Easy`: Tugas ini sangat mendasar untuk kelas 1, melibatkan pengenalan atribut visual sederhana (warna) dengan satu kriteria yang jelas.. Bukti: Bangun yang satu warna dengan gambar di atas.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membedakan warna dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena hanya memerlukan observasi visual sederhana untuk mengelompokkan benda berdasarkan satu atribut fisik yang menonjol. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 110/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.006266; applying=0.993734; reasoning=0.000000 | applying | 0.993734 | 0.034619 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.441449; conceptual=0.554535; procedural=0.004017; metacognitive=0.000000 | conceptual | 0.554535 | 0.512228 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.886667; Medium=0.110618; Hard=0.002716 | Easy | 0.886667 | 0.333370 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.993734; −Σp ln(p) = 0.038033; H = 0.038033/ln(3) = 0.034619; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.554535; −Σp ln(p) = 0.710098; H = 0.710098/ln(4) = 0.512228; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.886667; −Σp ln(p) = 0.366244; H = 0.366244/ln(3) = 0.333370; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Mengelompokkan Benda
Tipe soal: multiple_choice
Stimulus: -
Soal: Bangun yang satu warna dengan gambar di atas.
Pilihan: A. Persegi berwarna ungu
B. Oval berwarna hijau
C. Persegi panjang berwarna biru
D. Segitiga terbalik berwarna merah muda
Transkripsi visual: Terdapat kotak berisi tiga bangun datar berwarna merah muda: persegi panjang, segitiga siku-siku, dan persegi panjang vertikal. Di bawahnya terdapat tiga pilihan bangun: segitiga terbalik berwarna merah muda, persegi berwarna ungu, dan oval berwarna hijau.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 27. Soal `aaf396a280df35704272b0d3`

Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?

| Opsi | Isi |
|---|---|
| A | 6 |
| B | 8 |
| C | 4 |
| D | 5 |

![Gambar sumber soal 27](<../images/kelas1_panduan_siswa_kelas1.pdf-0150-03.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Identifikasi bentuk dengan sisi lengkung: 1 hidung (lingkaran), 1 mata (lingkaran), 1 telinga (oval), dan 2 bercak pada badan (lingkaran). Total = 1 + 1 + 1 + 2 = 5.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0150-03.png. Transkripsi visual: Gambar seekor anjing yang disusun dari berbagai bentuk geometri. Bentuk dengan sisi lengkung terdiri dari: 1 lingkaran hitam kecil sebagai hidung, 1 lingkaran hitam kecil sebagai mata, 1 oval merah sebagai telinga, dan 2 lingkaran merah sebagai bercak pada badan. Total ada 5 bentuk dengan sisi lengkung.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c9dc178abbc569f53d8ecf37fcd4a14f0e3273f52844010895152a4e1daea702`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2520 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2551 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2552 |

Run 1 — solusi: Identifikasi bentuk lengkung pada gambar: 1 hidung (lingkaran), 1 mata (lingkaran), 1 telinga (oval), dan 2 bercak pada badan (lingkaran). Total = 1 + 1 + 1 + 2 = 5.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengenali dan menghitung objek berdasarkan atribut visual (bentuk lengkung) yang spesifik, yang merupakan proses pengenalan langsung.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa terhadap kategori bentuk geometri (lengkung vs tidak lengkung/poligon).. Bukti: Bentuk lengkung ada berapa?
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan pengamatan visual langsung dan penghitungan sederhana (subitizing/counting) untuk siswa kelas 1.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membedakan bentuk lengkung dan bentuk bersudut, serta kemampuan berhitung 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena fokus pada pengenalan bentuk dasar dan berhitung sederhana dalam konteks visual yang konkret. |

Run 2 — solusi: Mengidentifikasi dan menghitung bentuk dengan sisi lengkung: 1 hidung (lingkaran), 1 mata (lingkaran), 1 telinga (oval), dan 2 bercak pada badan (lingkaran). Total = 1 + 1 + 1 + 2 = 5.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengidentifikasi dan menghitung objek berdasarkan atribut visual (sisi lengkung) yang spesifik, yang merupakan proses pengenalan dan klasifikasi langsung.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang atribut bentuk (lengkung vs lurus) dan kemampuan mengkategorikan objek berdasarkan atribut tersebut.. Bukti: Bentuk lengkung ada berapa?
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan pengamatan visual langsung dan penghitungan sederhana (counting) untuk siswa kelas 1, tanpa strategi kompleks.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membedakan bentuk lengkung dan lurus, serta kemampuan berhitung 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas menghitung objek berdasarkan atribut visual adalah standar untuk kelas 1, dengan beban kognitif yang rendah. |

Run 3 — solusi: Mengidentifikasi dan menghitung bentuk dengan sisi lengkung: 1 hidung (lingkaran), 1 mata (lingkaran), 1 telinga (oval), dan 2 bercak di badan (lingkaran). Total = 1 + 1 + 1 + 2 = 5.
- Domain kognitif `classify/applying`: Siswa perlu mengenali atribut bentuk (lengkung vs lurus) dan melakukan penghitungan sederhana. Ini adalah proses applying karena menerapkan konsep klasifikasi bentuk pada situasi rutin.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?
- Dimensi pengetahuan `classify/conceptual`: Siswa perlu memahami kategori bentuk (lengkung vs tidak lengkung) untuk mengklasifikasikan objek yang ada.. Bukti: Bentuk lengkung ada berapa?
- Intended difficulty `classify/Easy`: Soal ini meminta siswa untuk membedakan atribut visual (lengkung) dari sekumpulan bentuk geometris. Ini adalah tugas rutin untuk kelas 1.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mampu membedakan bentuk dasar (lingkaran/oval vs persegi/persegi panjang) dan menghitung sampai 5. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas menghitung objek berdasarkan atribut visual adalah standar untuk kelas 1, dengan beban kognitif yang rendah. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3940`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa diminta untuk mengenali dan menghitung objek berdasarkan atribut visual (bentuk lengkung) yang spesifik, yang merupakan proses pengenalan langsung.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman siswa terhadap kategori bentuk geometri (lengkung vs tidak lengkung/poligon).
- Intended difficulty `Easy`: Soal ini tergolong mudah karena hanya memerlukan pengamatan visual langsung dan penghitungan sederhana (counting) untuk siswa kelas 1.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membedakan bentuk lengkung dan bentuk bersudut, serta kemampuan berhitung 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 5 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena fokus pada pengenalan bentuk dasar dan berhitung sederhana dalam konteks visual yang konkret. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 116/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.002566; applying=0.997434; reasoning=0.000000 | applying | 0.997434 | 0.016266 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.398982; conceptual=0.564298; procedural=0.036720; metacognitive=0.000000 | conceptual | 0.564298 | 0.584879 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.851136; Medium=0.145555; Hard=0.003309 | Easy | 0.851136 | 0.397411 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.997434; −Σp ln(p) = 0.017870; H = 0.017870/ln(3) = 0.016266; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.564298; −Σp ln(p) = 0.810814; H = 0.810814/ln(4) = 0.584879; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.851136; −Σp ln(p) = 0.436601; H = 0.436601/ln(3) = 0.397411; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Menyusun dan Mengurai Bentuk Bangun
Tipe soal: multiple_choice
Stimulus: -
Soal: Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?
Pilihan: A. 6
B. 8
C. 4
D. 5
Transkripsi visual: Gambar seekor anjing yang disusun dari berbagai bentuk geometri. Bentuk dengan sisi lengkung terdiri dari: 1 lingkaran hitam kecil sebagai hidung, 1 lingkaran hitam kecil sebagai mata, 1 oval merah sebagai telinga, dan 2 lingkaran merah sebagai bercak pada badan. Total ada 5 bentuk dengan sisi lengkung.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 28. Soal `595d20d8c4a6f9418dc496b0`

Hitunglah banyaknya bentuk bangun pada gambar berikut. Segitiga ada berapa?

| Opsi | Isi |
|---|---|
| A | 8 |
| B | 0 |
| C | 1 |
| D | 2 |

![Gambar sumber soal 28](<../images/kelas1_panduan_siswa_kelas1.pdf-0150-03.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Mengidentifikasi bentuk pada gambar: hanya ekor anjing yang memiliki tiga sisi lurus (segitiga). Jumlah segitiga = 1.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0150-03.png. Transkripsi visual: Gambar seekor anjing yang disusun dari berbagai bentuk geometri: kepala dan tubuh berbentuk persegi/persegi panjang, telinga berbentuk oval, mata dan bintik tubuh berbentuk lingkaran, kaki berbentuk persegi panjang, dan ekor berbentuk segitiga.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b0590ed47eb0abea4b5e1cf540638b492ed303832685851ec5e16ef01f4f1a78`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2512 |
| 2 | success | valid / verified | knowing | factual | Easy | 2463 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2436 |

Run 1 — solusi: Mengidentifikasi bentuk geometri pada gambar: kepala, tubuh, dan kaki adalah persegi/persegi panjang, telinga adalah oval, mata/bintik adalah lingkaran, dan hanya ekor yang memiliki tiga sisi lurus (segitiga). Jumlah segitiga = 1.
- Domain kognitif `classify/applying`: Siswa perlu mengenali properti bentuk geometri (segitiga) dan membedakannya dari bentuk lain (persegi, lingkaran, oval) dalam komposisi gambar yang lebih kompleks.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Segitiga ada berapa?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang atribut yang mendefinisikan bentuk segitiga (tiga sisi lurus) dibandingkan dengan bentuk lain.. Bukti: Segitiga ada berapa?
- Intended difficulty `classify/Easy`: Soal ini menuntut siswa untuk melakukan diskriminasi visual di antara berbagai bentuk yang digabungkan menjadi satu objek (anjing), yang merupakan tugas standar untuk kelas 1.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Segitiga ada berapa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk dasar (segitiga, persegi, lingkaran). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 1 diharapkan mampu mengidentifikasi bentuk dasar dalam gambar komposit sederhana. |

Run 2 — solusi: Mengidentifikasi bentuk segitiga pada gambar. Hanya ekor anjing yang memiliki bentuk segitiga. Jumlahnya adalah 1.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengenali dan menghitung bentuk geometri spesifik (segitiga) dari sekumpulan bentuk yang membentuk gambar anjing. Ini adalah proses pengenalan visual langsung.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Segitiga ada berapa?
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pengetahuan faktual tentang ciri-ciri bentuk geometri dasar (segitiga) dan kemampuan untuk membedakannya dari bentuk lain (persegi, lingkaran, oval).. Bukti: Segitiga ada berapa?
- Intended difficulty `classify/Easy`: Tugas ini sangat langsung bagi siswa kelas 1, hanya memerlukan pengenalan bentuk dasar dan penghitungan sederhana (1 objek).. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Segitiga ada berapa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk geometri dasar (segitiga, lingkaran, persegi). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena hanya memerlukan identifikasi visual bentuk dasar tanpa operasi matematika kompleks. |

Run 3 — solusi: Mengidentifikasi bentuk segitiga pada gambar: hanya ekor anjing yang berbentuk segitiga. Jumlah = 1.
- Domain kognitif `classify/knowing`: Siswa diminta untuk mengenali dan menghitung objek dengan properti geometris tertentu (segitiga) dari sekumpulan bentuk lain. Ini adalah proses pengenalan visual langsung.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Segitiga ada berapa?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang definisi dan karakteristik bentuk dasar (segitiga) dibandingkan dengan bentuk lain seperti lingkaran atau persegi.. Bukti: Segitiga ada berapa?
- Intended difficulty `classify/Easy`: Tugas ini sangat langsung bagi siswa kelas 1, hanya memerlukan identifikasi visual satu bentuk spesifik di antara bentuk-bentuk dasar lainnya.. Bukti: Hitunglah banyaknya bentuk bangun pada gambar berikut. Segitiga ada berapa?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk-bentuk geometri dasar (segitiga, lingkaran, persegi). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena fokus pada pengenalan bentuk dasar dalam konteks visual sederhana. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 1, "knowing": 2} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 2, "factual": 1} | majority_2_of_3 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3747`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa perlu melakukan diskriminasi visual untuk mengenali properti geometris segitiga di antara bentuk-bentuk lain (lingkaran, persegi, oval) dalam komposisi gambar. Ini adalah proses pengenalan dan penerapan kriteria bentuk.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konseptual tentang atribut yang mendefinisikan bentuk segitiga (tiga sisi) dibandingkan dengan bentuk geometri lainnya.
- Intended difficulty `Easy`: Tugas ini sangat langsung bagi siswa kelas 1, hanya memerlukan pengenalan bentuk dasar dan penghitungan sederhana.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal bentuk geometri dasar (segitiga, lingkaran, persegi). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 1 diharapkan mampu mengidentifikasi bentuk dasar dalam gambar komposit sederhana tanpa operasi matematika kompleks. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 101/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.949543; applying=0.050457; reasoning=0.000000 | knowing | 0.949543 | 0.181919 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.466649; conceptual=0.515657; procedural=0.017694; metacognitive=0.000000 | conceptual | 0.515657 | 0.554415 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.867764; Medium=0.129412; Hard=0.002824 | Easy | 0.867764 | 0.367985 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.949543; −Σp ln(p) = 0.199858; H = 0.199858/ln(3) = 0.181919; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.515657; −Σp ln(p) = 0.768582; H = 0.768582/ln(4) = 0.554415; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.867764; −Σp ln(p) = 0.404273; H = 0.404273/ln(3) = 0.367985; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Menyusun dan Mengurai Bentuk Bangun
Tipe soal: multiple_choice
Stimulus: -
Soal: Hitunglah banyaknya bentuk bangun pada gambar berikut. Segitiga ada berapa?
Pilihan: A. 8
B. 0
C. 1
D. 2
Transkripsi visual: Gambar seekor anjing yang disusun dari berbagai bentuk geometri: kepala dan tubuh berbentuk persegi/persegi panjang, telinga berbentuk oval, mata dan bintik tubuh berbentuk lingkaran, kaki berbentuk persegi panjang, dan ekor berbentuk segitiga.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 29. Soal `4d125a6ed9a2701db41cdcd1`

Isilah dengan bilangan yang benar.<br><br>10 ditambah 3 menjadi ....

| Opsi | Isi |
|---|---|
| A | 14 |
| B | 12 |
| C | 31 |
| D | 13 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: 10 + 3 = 13
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `77f3a2e1b230dac593d46f2821f8035288f386534c17bb656fddd549f2170427`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 1277 |
| 2 | success | valid / verified | knowing | factual | Easy | 1272 |
| 3 | success | valid / verified | knowing | factual | Easy | 1284 |

Run 1 — solusi: 10 + 3 = 13
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi penjumlahan dasar yang sangat langsung (fakta dasar penjumlahan 10 dengan satuan).. Bukti: 10 ditambah 3 menjadi ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang fakta dasar bilangan dan operasi penjumlahan sederhana.. Bukti: 10 ditambah 3 menjadi ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan operasi satu langkah yang familiar.. Bukti: 10 ditambah 3 menjadi ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dasar dan penjumlahan bilangan 1-20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 yang menekankan pengenalan bilangan dan operasi dasar. |

Run 2 — solusi: 10 + 3 = 13
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi penjumlahan dasar yang sangat langsung (fakta dasar penjumlahan).. Bukti: 10 ditambah 3 menjadi
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang fakta dasar bilangan dan operasi penjumlahan sederhana.. Bukti: 10 ditambah 3
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur yang sangat familiar bagi siswa kelas 1, melibatkan satu langkah operasi dasar tanpa kompleksitas tambahan.. Bukti: 10 ditambah 3 menjadi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep bilangan 1-20 dan operasi penjumlahan dasar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 yang menekankan pengenalan bilangan dan penjumlahan dasar hingga 20. |

Run 3 — solusi: 10 + 3 = 13
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi penjumlahan dasar yang sangat langsung (10+3) untuk mendapatkan hasil.. Bukti: 10 ditambah 3 menjadi
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang fakta bilangan dan operasi penjumlahan dasar.. Bukti: 10 ditambah 3
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan operasi penjumlahan satu digit dengan sepuluh yang merupakan prosedur sangat familiar.. Bukti: 10 ditambah 3 menjadi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dasar dan penjumlahan bilangan 1-20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 yang menekankan pengenalan bilangan dan operasi hitung dasar. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 66/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999968; applying=0.000032; reasoning=0.000000 | knowing | 0.999968 | 0.000334 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.625335; conceptual=0.350270; procedural=0.024395; metacognitive=0.000000 | factual | 0.625335 | 0.542174 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.893777; Medium=0.103965; Hard=0.002258 | Easy | 0.893777 | 0.318108 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999968; −Σp ln(p) = 0.000367; H = 0.000367/ln(3) = 0.000334; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.625335; −Σp ln(p) = 0.751613; H = 0.751613/ln(4) = 0.542174; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.893777; −Σp ln(p) = 0.349477; H = 0.349477/ln(3) = 0.318108; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Menghitung, Membaca, dan Menulis Bilangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Isilah dengan bilangan yang benar.

10 ditambah 3 menjadi ....
Pilihan: A. 14
B. 12
C. 31
D. 13
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 30. Soal `fbc23bca48392d3c678c3beb`

Isilah titik-titik berikut.<br><br>8 ditambah 10 menjadi ....

| Opsi | Isi |
|---|---|
| A | 18 |
| B | 810 |
| C | 19 |
| D | 17 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: 8 + 10 = 18
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `667035e13b735c918c39e19b21873fbd258cd37da96268770759705296775828`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 1282 |
| 2 | success | valid / verified | knowing | procedural | Easy | 1283 |
| 3 | success | valid / verified | knowing | procedural | Easy | 1286 |

Run 1 — solusi: 8 + 10 = 18
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi penjumlahan dasar yang sudah dipelajari di kelas 1, yaitu menjumlahkan dua bilangan satu/dua digit.. Bukti: 8 ditambah 10 menjadi
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dasar tentang operasi penjumlahan bilangan cacah.. Bukti: 8 ditambah 10
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur penjumlahan standar yang sangat familiar bagi siswa kelas 1 tanpa memerlukan strategi kompleks.. Bukti: 8 ditambah 10 menjadi

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan nilai tempat bilangan sampai 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan 8+10 adalah materi dasar kelas 1 yang rutin dan tidak memerlukan langkah penalaran tambahan. |

Run 2 — solusi: 8 + 10 = 18
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi penjumlahan dasar yang sudah dipelajari di kelas 1, yaitu menjumlahkan bilangan satu digit dengan sepuluh.. Bukti: 8 ditambah 10 menjadi ....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dasar tentang operasi penjumlahan bilangan cacah.. Bukti: 8 ditambah 10
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur penjumlahan standar yang sangat familiar bagi siswa kelas 1, dengan beban kognitif yang rendah.. Bukti: 8 ditambah 10 menjadi ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dasar dan penjumlahan bilangan 1-20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan 8+10 adalah materi dasar kelas 1 yang rutin dan tidak memerlukan strategi kompleks. |

Run 3 — solusi: 8 + 10 = 18
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi penjumlahan dasar yang sudah dipelajari di kelas 1, yaitu menjumlahkan bilangan satu digit dengan sepuluh.. Bukti: 8 ditambah 10 menjadi ....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dasar tentang operasi penjumlahan bilangan cacah.. Bukti: 8 ditambah 10
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur penjumlahan yang sangat familiar bagi siswa kelas 1, hanya melibatkan satu langkah operasi langsung tanpa kompleksitas tambahan.. Bukti: 8 ditambah 10 menjadi ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan nilai tempat bilangan 1-20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan 8+10 adalah standar kompetensi kelas 1 yang bersifat rutin dan langsung. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 66/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999973; applying=0.000027; reasoning=0.000000 | knowing | 0.999973 | 0.000287 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.593649; conceptual=0.387587; procedural=0.018764; metacognitive=0.000000 | factual | 0.593649 | 0.542116 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.895874; Medium=0.102022; Hard=0.002103 | Easy | 0.895874 | 0.313435 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999973; −Σp ln(p) = 0.000316; H = 0.000316/ln(3) = 0.000287; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.593649; −Σp ln(p) = 0.751532; H = 0.751532/ln(4) = 0.542116; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.895874; −Σp ln(p) = 0.344344; H = 0.344344/ln(3) = 0.313435; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Menghitung, Membaca, dan Menulis Bilangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Isilah titik-titik berikut.

8 ditambah 10 menjadi ....
Pilihan: A. 18
B. 810
C. 19
D. 17
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 31. Soal `4953bd9e508059b6896af5e5`

Isilah titik-titik berikut.<br><br>15, 14, ...., ....

| Opsi | Isi |
|---|---|
| A | 14, 13 |
| B | 16, 17 |
| C | 12, 13 |
| D | 13, 12 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Pola bilangan adalah menghitung mundur satu per satu: 15, 14, 13, 12.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `22566b5bb03c2de75ee541bdbc2426a8b2a7d0f508940024f431b8103e158468`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1319 |
| 2 | success | valid / verified | knowing | factual | Easy | 1336 |
| 3 | success | valid / verified | knowing | factual | Easy | 1335 |

Run 1 — solusi: Pola bilangan adalah menghitung mundur satu per satu: 15, 14, 13, 12.
- Domain kognitif `classify/applying`: Siswa perlu mengenali pola urutan bilangan mundur dan menerapkan aturan tersebut untuk menentukan dua angka berikutnya.. Bukti: 15, 14, ...., ....
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang urutan bilangan (konsep) dan teknik menghitung mundur (prosedural).. Bukti: 15, 14, ...., ....
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur rutin bagi siswa kelas 1 untuk melanjutkan pola bilangan mundur sederhana.. Bukti: 15, 14, ...., ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung mundur dari 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 yang menekankan pengenalan urutan bilangan hingga 20. |

Run 2 — solusi: Pola bilangan adalah urutan mundur (dikurangi 1). Setelah 15 dan 14, angka berikutnya adalah 15-1=13 dan 13-1=12.
- Domain kognitif `classify/knowing`: Siswa diminta mengenali pola urutan bilangan mundur sederhana dan melengkapinya, yang merupakan proses langsung.. Bukti: 15, 14, ...., ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang urutan bilangan (fakta dasar) dalam konteks menghitung mundur.. Bukti: 15, 14, ...., ....
- Intended difficulty `classify/Easy`: Soal ini sangat rutin untuk kelas 1, hanya memerlukan pengenalan pola urutan mundur satu langkah tanpa kompleksitas tambahan.. Bukti: 15, 14, ...., ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung mundur dasar di bawah 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD mengenai pengenalan urutan bilangan. |

Run 3 — solusi: Pola bilangan adalah urutan mundur (dikurangi 1). Setelah 15 dan 14, bilangan berikutnya adalah 15-2=13 dan 15-3=12.
- Domain kognitif `classify/knowing`: Siswa diminta mengenali pola urutan bilangan mundur sederhana dan melengkapinya, yang merupakan proses langsung.. Bukti: 15, 14, ...., ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang urutan bilangan (fakta dasar) dalam konteks menghitung mundur.. Bukti: 15, 14, ...., ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, hanya memerlukan pengenalan pola urutan mundur satu langkah tanpa kompleksitas tambahan.. Bukti: 15, 14, ...., ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung mundur bilangan 1-20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan standar kelas 1 untuk pengenalan urutan bilangan. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 1, "knowing": 2} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 1, "factual": 2} | majority_2_of_3 / adjudicated | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2509`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa hanya perlu mengenali pola urutan bilangan mundur yang diberikan dan melanjutkan urutan tersebut secara langsung. Ini adalah proses pengenalan pola dasar.
- Dimensi pengetahuan `factual`: Soal ini menguji pengetahuan faktual tentang urutan bilangan dalam sistem bilangan asli, khususnya kemampuan menghitung mundur.
- Intended difficulty `Easy`: Soal ini sangat mendasar untuk kelas 1, hanya memerlukan pengenalan pola urutan mundur satu langkah tanpa kompleksitas tambahan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung mundur bilangan 1-20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD mengenai pengenalan urutan bilangan. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 76/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999985; applying=0.000015; reasoning=0.000000 | knowing | 0.999985 | 0.000164 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.880450; conceptual=0.106302; procedural=0.013248; metacognitive=0.000000 | factual | 0.880450 | 0.294062 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.913496; Medium=0.084560; Hard=0.001944 | Easy | 0.913496 | 0.276417 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999985; −Σp ln(p) = 0.000180; H = 0.000180/ln(3) = 0.000164; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.880450; −Σp ln(p) = 0.407656; H = 0.407656/ln(4) = 0.294062; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.913496; −Σp ln(p) = 0.303675; H = 0.303675/ln(3) = 0.276417; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Menghitung Maju dan Mundur
Tipe soal: multiple_choice
Stimulus: -
Soal: Isilah titik-titik berikut.

15, 14, ...., ....
Pilihan: A. 14, 13
B. 16, 17
C. 12, 13
D. 13, 12
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 32. Soal `02bd8bfdfd682bd80aa5f426`

Lengkapi urutan bilangan berikut.<br><br>20, ...., 18

| Opsi | Isi |
|---|---|
| A | 18 |
| B | 19 |
| C | 21 |
| D | 17 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Urutan bilangan mundur dari 20 ke 18 adalah 20, 19, 18. Bilangan yang hilang adalah 19.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `be4cda6dfe446ecbd86a0acbadda0ae520d3fc7972d0a1997680f7111438c7ab`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | factual | Easy | 1311 |
| 2 | success | valid / verified | knowing | factual | Easy | 1281 |
| 3 | success | valid / verified | knowing | factual | Easy | 1303 |

Run 1 — solusi: Urutan bilangan mundur dari 20 ke 18 adalah 20, 19, 18. Bilangan yang hilang adalah 19.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali pola urutan bilangan mundur sederhana dan mengisi satu angka yang hilang, yang merupakan proses langsung.. Bukti: Lengkapi urutan bilangan berikut. 20, ...., 18
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang urutan bilangan (fakta dasar matematika) dalam rentang 1-20.. Bukti: 20, ...., 18
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan satu langkah pengisian angka dalam urutan mundur yang familiar.. Bukti: 20, ...., 18

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung mundur dari 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD mengenai pengenalan urutan bilangan hingga 20. |

Run 2 — solusi: Urutan bilangan mundur dari 20 ke 18 adalah 20, 19, 18. Jadi, bilangan yang hilang adalah 19.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali pola urutan bilangan mundur sederhana dan mengisi satu angka yang hilang, yang merupakan proses langsung.. Bukti: Lengkapi urutan bilangan berikut. 20, ...., 18
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang urutan bilangan (fakta dasar matematika) dalam konteks menghitung mundur.. Bukti: Lengkapi urutan bilangan berikut. 20, ...., 18
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan prosedur menghitung mundur satu langkah yang sangat familiar.. Bukti: 20, ...., 18

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung mundur bilangan 1-20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD untuk pengenalan urutan bilangan. |

Run 3 — solusi: Urutan bilangan mundur dari 20 ke 18 adalah 20, 19, 18. Maka bilangan yang hilang adalah 19.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali pola urutan bilangan mundur sederhana (20, 19, 18) yang merupakan proses langsung.. Bukti: Lengkapi urutan bilangan berikut. 20, ...., 18
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang urutan bilangan (fakta dasar matematika) dalam konteks menghitung mundur.. Bukti: 20, ...., 18
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan satu langkah pengisian bilangan dalam urutan yang sangat familiar.. Bukti: 20, ...., 18

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung mundur bilangan 20-1. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 yang menekankan pengenalan urutan bilangan hingga 20. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"factual": 3} | unanimous_3_0 / unanimous | factual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 61/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.999999; applying=0.000001; reasoning=0.000000 | knowing | 0.999999 | 0.000009 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.855945; conceptual=0.130357; procedural=0.013698; metacognitive=0.000000 | factual | 0.855945 | 0.330025 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.916232; Medium=0.081517; Hard=0.002250 | Easy | 0.916232 | 0.271466 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999999; −Σp ln(p) = 0.000010; H = 0.000010/ln(3) = 0.000009; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.855945; −Σp ln(p) = 0.457512; H = 0.457512/ln(4) = 0.330025; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.916232; −Σp ln(p) = 0.298235; H = 0.298235/ln(3) = 0.271466; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Menghitung Maju dan Mundur
Tipe soal: multiple_choice
Stimulus: -
Soal: Lengkapi urutan bilangan berikut.

20, ...., 18
Pilihan: A. 18
B. 19
C. 21
D. 17
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "factual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "factual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 33. Soal `fb13c7e49793c36315b9e324`

Isilah titik-titik dalam tabel. Lengkapi juga nilai tempatnya.<br><br>.... puluhan dan .... satuan = ....

| Opsi | Isi |
|---|---|
| A | 1 puluhan dan 5 satuan = 15 |
| B | 0 puluhan dan 15 satuan = 15 |
| C | 1 puluhan dan 6 satuan = 16 |
| D | 1 puluhan dan 4 satuan = 14 |

![Gambar sumber soal 33](<../images/kelas1_panduan_siswa_kelas1.pdf-0175-03.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Gambar menunjukkan 1 kelompok berisi 10 telur (1 puluhan) dan 5 telur lepas (5 satuan), sehingga membentuk bilangan 15.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0175-03.png. Transkripsi visual: Gambar menunjukkan satu karton berisi 10 telur (dikelompokkan sebagai satu puluhan) dan 5 telur lepas (sebagai satuan). Terdapat tabel dengan kolom 'Puluhan' dan 'Satuan', serta kalimat rumpang '... puluhan dan ... satuan = ...'.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ce0161e57dcd5cdba352fad8bd7a31425378587b767320fc2f98faa108b5ba56`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2595 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2536 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2551 |

Run 1 — solusi: Gambar menunjukkan 1 kelompok berisi 10 telur (1 puluhan) dan 5 telur lepas (5 satuan), sehingga membentuk bilangan 15.
- Domain kognitif `classify/knowing`: Siswa diminta mengenali representasi visual (kelompok 10 dan satuan) dan menerjemahkannya langsung ke dalam format nilai tempat (puluhan dan satuan). Ini adalah proses pengenalan konsep dasar.. Bukti: Isilah titik-titik dalam tabel; 1 puluhan dan 5 satuan = 15
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang bagaimana angka dibentuk melalui pengelompokan sepuluh (base-ten system) pada tingkat dasar.. Bukti: Nilai Tempat; 1 puluhan dan 5 satuan
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin dan langsung, menggunakan representasi visual yang umum untuk kelas 1 (benda konkret dikelompokkan).. Bukti: Isilah titik-titik dalam tabel; 1 puluhan dan 5 satuan = 15

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang menghitung benda sampai 20 dan konsep pengelompokan sepuluh. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena menggunakan manipulatif visual (telur) untuk memperkenalkan konsep nilai tempat puluhan dan satuan secara konkret. |

Run 2 — solusi: Gambar menunjukkan 1 kelompok berisi 10 telur (1 puluhan) dan 5 telur lepas (5 satuan), sehingga membentuk bilangan 15.
- Domain kognitif `classify/knowing`: Siswa diminta mengenali dan mengelompokkan objek konkret ke dalam konsep nilai tempat (puluhan dan satuan) yang merupakan proses langsung.. Bukti: Isilah titik-titik dalam tabel. Lengkapi juga nilai tempatnya.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur nilai tempat (puluhan dan satuan) sebagai konsep dasar bilangan.. Bukti: .... puluhan dan .... satuan = ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, menggunakan representasi visual yang familiar dan prosedur pengelompokan yang rutin.. Bukti: 1 puluhan dan 5 satuan = 15

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang menghitung benda sampai 20 dan konsep pengelompokan sepuluh. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena menggunakan objek konkret (telur) untuk menjelaskan konsep abstrak nilai tempat. |

Run 3 — solusi: Wadah berisi 10 telur dihitung sebagai 1 puluhan, dan 5 telur lepas dihitung sebagai 5 satuan. Jadi, 1 puluhan dan 5 satuan = 15.
- Domain kognitif `classify/knowing`: Siswa diminta mengenali representasi visual (kelompok sepuluh dan satuan) dan memetakan jumlah tersebut ke dalam format nilai tempat yang sudah familiar.. Bukti: Isilah titik-titik dalam tabel. Lengkapi juga nilai tempatnya.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep dasar nilai tempat (puluhan dan satuan) sebagai struktur bilangan.. Bukti: .... puluhan dan .... satuan = ....
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, menggunakan representasi konkret yang umum (telur dalam wadah) untuk mengajarkan konsep nilai tempat.. Bukti: 1 puluhan dan 5 satuan = 15

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda hingga 20 dan memahami pengelompokan sepuluh. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena menggunakan objek konkret untuk memvisualisasikan konsep abstrak nilai tempat. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 152/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000000 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.001662; conceptual=0.985109; procedural=0.013228; metacognitive=0.000000 | conceptual | 0.985109 | 0.059609 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.775085; Medium=0.219548; Hard=0.005367 | Easy | 0.775085 | 0.508288 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000000; H = 0.000000/ln(3) = 0.000000; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.985109; −Σp ln(p) = 0.082635; H = 0.082635/ln(4) = 0.059609; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.775085; −Σp ln(p) = 0.558411; H = 0.558411/ln(3) = 0.508288; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Nilai Tempat
Tipe soal: multiple_choice
Stimulus: -
Soal: Isilah titik-titik dalam tabel. Lengkapi juga nilai tempatnya.

.... puluhan dan .... satuan = ....
Pilihan: A. 1 puluhan dan 5 satuan = 15
B. 0 puluhan dan 15 satuan = 15
C. 1 puluhan dan 6 satuan = 16
D. 1 puluhan dan 4 satuan = 14
Transkripsi visual: Gambar menunjukkan satu karton berisi 10 telur (dikelompokkan sebagai satu puluhan) dan 5 telur lepas (sebagai satuan). Terdapat tabel dengan kolom 'Puluhan' dan 'Satuan', serta kalimat rumpang '... puluhan dan ... satuan = ...'.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 34. Soal `daa41e2808537d493a6c0994`

Hitunglah dan isi tabelnya.<br><br>Nilai tempat 14 = .... puluhan dan .... satuan

| Opsi | Isi |
|---|---|
| A | 1 puluhan dan 4 satuan |
| B | 1 puluhan dan 3 satuan |
| C | 4 puluhan dan 1 satuan |
| D | 0 puluhan dan 14 satuan |

![Gambar sumber soal 34](<../images/kelas1_panduan_siswa_kelas1.pdf-0175-04.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Angka 14 terdiri dari 1 kelompok sepuluh (1 puluhan) dan 4 satuan.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0175-04.png. Transkripsi visual: Gambar menunjukkan satu ikat pensil berisi 10 buah dan 4 pensil lepas di sampingnya. Terdapat tabel dengan kolom 'Puluhan' dan 'Satuan' yang harus diisi. Teks soal meminta untuk menentukan nilai tempat dari angka 14.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `ac71205aa65564d67d8d073358f8194e5eeba65645fcebacd78f2782b85cdd15`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2476 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2503 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2494 |

Run 1 — solusi: Angka 14 terdiri dari 1 puluhan (10) dan 4 satuan (4).
- Domain kognitif `classify/applying`: Siswa diminta menerapkan pemahaman konsep nilai tempat pada objek konkret yang sudah dikelompokkan (bundling 10). Ini adalah penerapan prosedur rutin.. Bukti: Nilai tempat 14 = .... puluhan dan .... satuan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur sistem bilangan desimal (nilai tempat), yang merupakan konsep dasar dalam matematika.. Bukti: Nilai tempat 14
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, menggunakan representasi visual yang jelas (bundling) untuk membedakan puluhan dan satuan.. Bukti: Nilai tempat 14 = .... puluhan dan .... satuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mengenal konsep bilangan 11-20 dan pengelompokan sepuluh. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD mengenai pengenalan nilai tempat bilangan cacah sampai 20. |

Run 2 — solusi: Angka 14 terdiri dari 1 kelompok sepuluh (1 puluhan) dan 4 satuan.
- Domain kognitif `classify/knowing`: Siswa diminta mengenali dan menerapkan pemahaman dasar tentang nilai tempat (puluhan dan satuan) pada angka 14 yang direpresentasikan secara konkret.. Bukti: Nilai tempat 14 = .... puluhan dan .... satuan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep dasar tentang bagaimana angka dua digit disusun berdasarkan nilai tempat (puluhan dan satuan).. Bukti: Nilai tempat 14
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, menggunakan representasi visual yang familiar (benda dikelompokkan sepuluh-sepuluh), dan hanya memerlukan satu langkah identifikasi langsung.. Bukti: Nilai tempat 14 = .... puluhan dan .... satuan

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep bilangan 11-20 dan pengelompokan sepuluh. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD mengenai pengenalan nilai tempat bilangan cacah sampai 20. |

Run 3 — solusi: 14 terdiri dari 1 kelompok sepuluh (1 puluhan) dan 4 satuan.
- Domain kognitif `classify/applying`: Siswa diminta menerapkan pemahaman konsep nilai tempat pada objek konkret yang sudah dikelompokkan (bundling). Ini adalah penerapan prosedur standar dalam konteks rutin.. Bukti: Nilai tempat 14 = .... puluhan dan .... satuan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang struktur sistem bilangan desimal (konsep nilai tempat), yaitu bagaimana angka 14 dikategorikan ke dalam puluhan dan satuan.. Bukti: Nilai tempat 14
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, menggunakan representasi visual yang eksplisit (bundling) untuk membantu siswa memahami konsep puluhan dan satuan.. Bukti: Hitunglah dan isi tabelnya; Nilai tempat 14

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang menghitung benda sampai 20 dan konsep pengelompokan sepuluh. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD yang memperkenalkan konsep nilai tempat melalui benda konkret. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3710`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan pemahaman konsep nilai tempat pada objek konkret yang sudah dikelompokkan (bundling). Ini adalah penerapan prosedur standar dalam konteks rutin.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman tentang struktur sistem bilangan desimal (konsep nilai tempat), yaitu bagaimana angka 14 dikategorikan ke dalam puluhan dan satuan.
- Intended difficulty `Easy`: Soal ini sangat mendasar untuk kelas 1, menggunakan representasi visual yang eksplisit (bundling) untuk membantu siswa memahami konsep puluhan dan satuan.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman dasar tentang menghitung benda sampai 20 dan konsep pengelompokan sepuluh. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD yang memperkenalkan konsep nilai tempat melalui benda konkret. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 124/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000150; applying=0.999850; reasoning=0.000000 | applying | 0.999850 | 0.001342 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.011010; conceptual=0.983025; procedural=0.005965; metacognitive=0.000000 | conceptual | 0.983025 | 0.069990 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.796064; Medium=0.199934; Hard=0.004002 | Easy | 0.796064 | 0.478336 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999850; −Σp ln(p) = 0.001474; H = 0.001474/ln(3) = 0.001342; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.983025; −Σp ln(p) = 0.097026; H = 0.097026/ln(4) = 0.069990; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.796064; −Σp ln(p) = 0.525505; H = 0.525505/ln(3) = 0.478336; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Nilai Tempat
Tipe soal: multiple_choice
Stimulus: -
Soal: Hitunglah dan isi tabelnya.

Nilai tempat 14 = .... puluhan dan .... satuan
Pilihan: A. 1 puluhan dan 4 satuan
B. 1 puluhan dan 3 satuan
C. 4 puluhan dan 1 satuan
D. 0 puluhan dan 14 satuan
Transkripsi visual: Gambar menunjukkan satu ikat pensil berisi 10 buah dan 4 pensil lepas di sampingnya. Terdapat tabel dengan kolom 'Puluhan' dan 'Satuan' yang harus diisi. Teks soal meminta untuk menentukan nilai tempat dari angka 14.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 35. Soal `76bd2315ce21573dfa2ea8d7`

Perhatikan bilangan berikut. 13 11 18<br><br>Urutan mulai dari bilangan terkecil: .... , .... , ....

| Opsi | Isi |
|---|---|
| A | 13, 11, 18 |
| B | 11, 13, 18 |
| C | 11, 18, 13 |
| D | 18, 13, 11 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Membandingkan nilai bilangan 11, 13, dan 18. Karena 11 < 13 < 18, maka urutan dari yang terkecil adalah 11, 13, 18.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8033d883ba2c5a0920f213e162e9eb2871485c6e9c5615feeda7401eb9640023`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1398 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1414 |
| 3 | success | valid / verified | applying | procedural | Easy | 1388 |

Run 1 — solusi: Membandingkan nilai tempat puluhan dan satuan: 11 (1 puluhan, 1 satuan), 13 (1 puluhan, 3 satuan), 18 (1 puluhan, 8 satuan). Urutan dari terkecil: 11, 13, 18.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur membandingkan bilangan dua angka dan mengurutkannya, yang merupakan penerapan konsep dasar bilangan.. Bukti: Urutan mulai dari bilangan terkecil
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara mengurutkan bilangan berdasarkan nilai tempat.. Bukti: 13 11 18; Urutan mulai dari bilangan terkecil
- Intended difficulty `classify/Easy`: Soal ini merupakan tugas rutin bagi siswa kelas 1 untuk mengurutkan tiga bilangan dua angka.. Bukti: 13 11 18; Urutan mulai dari bilangan terkecil

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami nilai tempat bilangan 11-20 dan perbandingan bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan bilangan 11-20 adalah kompetensi standar kelas 1. |

Run 2 — solusi: Membandingkan nilai tempat puluhan dan satuan: 11 (1 puluhan, 1 satuan), 13 (1 puluhan, 3 satuan), 18 (1 puluhan, 8 satuan). Urutan dari terkecil: 11, 13, 18.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur membandingkan bilangan dua angka untuk mengurutkannya, yang merupakan penerapan konsep dasar bilangan.. Bukti: Urutan mulai dari bilangan terkecil
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang urutan bilangan (konsep) dan prosedur pengurutan bilangan cacah.. Bukti: 13 11 18; Urutan mulai dari bilangan terkecil
- Intended difficulty `classify/Easy`: Soal ini merupakan tugas rutin bagi siswa kelas 1 untuk mengurutkan tiga bilangan dua angka.. Bukti: 13 11 18; Urutan mulai dari bilangan terkecil

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami nilai tempat bilangan 11-20 dan perbandingan bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan tiga bilangan dua angka adalah standar kompetensi dasar kelas 1 SD. |

Run 3 — solusi: Membandingkan nilai tempat puluhan dan satuan: 11 (1 puluhan, 1 satuan), 13 (1 puluhan, 3 satuan), 18 (1 puluhan, 8 satuan). Urutan dari terkecil adalah 11, 13, 18.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan prosedur pengurutan bilangan berdasarkan nilai tempat yang sudah dipelajari.. Bukti: Urutan mulai dari bilangan terkecil
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang bagaimana mengurutkan bilangan cacah.. Bukti: 13 11 18; Urutan mulai dari bilangan terkecil
- Intended difficulty `classify/Easy`: Tugas ini merupakan prosedur rutin yang familiar bagi siswa kelas 1 dalam membandingkan bilangan dua angka.. Bukti: 13 11 18; Urutan mulai dari bilangan terkecil

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat bilangan 11-20 dan konsep perbandingan lebih kecil/lebih besar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan tiga bilangan dua angka adalah standar kompetensi dasar kelas 1 yang bersifat rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 2, "conceptual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2696`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa menerapkan prosedur perbandingan bilangan yang sudah dipelajari untuk mengurutkan sekumpulan bilangan.
- Dimensi pengetahuan `procedural`: Soal ini menguji penguasaan prosedur pengurutan bilangan cacah.
- Intended difficulty `Easy`: Tugas ini adalah prosedur rutin yang sangat standar untuk kelas 1, melibatkan perbandingan bilangan dua angka yang sederhana.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami urutan bilangan 1-20 dan konsep perbandingan lebih kecil/lebih besar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan tiga bilangan dua angka adalah kompetensi dasar yang rutin bagi siswa kelas 1. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 89/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.998339; applying=0.001661; reasoning=0.000000 | knowing | 0.998339 | 0.011189 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.271071; conceptual=0.706599; procedural=0.022330; metacognitive=0.000000 | conceptual | 0.706599 | 0.493503 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.866569; Medium=0.130640; Hard=0.002792 | Easy | 0.866569 | 0.369935 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.998339; −Σp ln(p) = 0.012293; H = 0.012293/ln(3) = 0.011189; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.706599; −Σp ln(p) = 0.684140; H = 0.684140/ln(4) = 0.493503; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.866569; −Σp ln(p) = 0.406415; H = 0.406415/ln(3) = 0.369935; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Membandingkan Bilangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan bilangan berikut. 13 11 18

Urutan mulai dari bilangan terkecil: .... , .... , ....
Pilihan: A. 13, 11, 18
B. 11, 13, 18
C. 11, 18, 13
D. 18, 13, 11
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 36. Soal `84e373946789a200e6b5203a`

Malosi mempunyai 13 bola. Wei mempunyai 11 bola. Kira mempunyai 10 bola.<br><br>Urutan banyak bola dari yang terkecil: .... , .... , ....

| Opsi | Isi |
|---|---|
| A | 13, 11, 10 |
| B | 10, 13, 11 |
| C | 11, 10, 13 |
| D | 10, 11, 13 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Membandingkan nilai bilangan: 10 < 11 < 13. Urutan dari terkecil adalah 10, 11, 13.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `eefde0832abc8c1f812cd03a1a31094edb25c861642a5ad877c4bab549702640`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1393 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1386 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1373 |

Run 1 — solusi: Membandingkan nilai bilangan: 10 < 11 < 13. Urutan dari terkecil adalah 10, 11, 13.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman tentang urutan bilangan (konsep membandingkan) untuk menyusun angka-angka yang diberikan.. Bukti: Urutan banyak bola dari yang terkecil
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang urutan bilangan dan nilai tempat dasar.. Bukti: 13 bola; 11 bola; 10 bola
- Intended difficulty `classify/Easy`: Tugas ini bersifat rutin bagi siswa kelas 1 yang sudah mempelajari perbandingan bilangan hingga 20. Prosedurnya langsung dan tidak memerlukan strategi kompleks.. Bukti: 13 bola; 11 bola; 10 bola; Urutan banyak bola dari yang terkecil

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami nilai bilangan 10-20 dan konsep urutan (lebih kecil/lebih besar). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena membandingkan tiga bilangan adalah standar kompetensi dasar untuk fase A. |

Run 2 — solusi: Membandingkan nilai bilangan: 10 < 11 < 13. Urutan dari terkecil adalah 10, 11, 13.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman tentang urutan bilangan (konsep dasar perbandingan) untuk mengurutkan tiga bilangan yang diberikan.. Bukti: Urutan banyak bola dari yang terkecil
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang urutan bilangan dan nilai tempat sederhana dalam rentang 1-20.. Bukti: 13 bola; 11 bola; 10 bola
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin untuk kelas 1, melibatkan perbandingan langsung tiga bilangan bulat positif tanpa jebakan kompleks.. Bukti: 13 bola; 11 bola; 10 bola; Urutan banyak bola dari yang terkecil

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami nilai bilangan 1-20 dan konsep perbandingan lebih kecil/lebih besar. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan tiga bilangan adalah kompetensi dasar yang diharapkan dikuasai siswa kelas 1. |

Run 3 — solusi: Membandingkan nilai bilangan: 10 < 11 < 13. Urutan dari terkecil adalah 10, 11, 13.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan pemahaman tentang urutan bilangan (konsep membandingkan) untuk mengurutkan tiga bilangan yang diberikan.. Bukti: Urutan banyak bola dari yang terkecil
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang nilai tempat dan urutan bilangan (magnitude) dalam rentang 1-20.. Bukti: 13 bola; 11 bola; 10 bola
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur rutin bagi siswa kelas 1 untuk mengurutkan tiga bilangan bulat positif.. Bukti: 13 bola; 11 bola; 10 bola; Urutan banyak bola dari yang terkecil

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep urutan bilangan 1-20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Mengurutkan tiga bilangan adalah standar kompetensi dasar kelas 1. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 99/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.039129; applying=0.960871; reasoning=0.000000 | applying | 0.960871 | 0.150341 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.241632; conceptual=0.735878; procedural=0.022490; metacognitive=0.000000 | conceptual | 0.735878 | 0.471927 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.878514; Medium=0.118864; Hard=0.002623 | Easy | 0.878514 | 0.348194 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.960871; −Σp ln(p) = 0.165166; H = 0.165166/ln(3) = 0.150341; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.735878; −Σp ln(p) = 0.654230; H = 0.654230/ln(4) = 0.471927; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.878514; −Σp ln(p) = 0.382531; H = 0.382531/ln(3) = 0.348194; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Membandingkan Bilangan
Tipe soal: multiple_choice
Stimulus: -
Soal: Malosi mempunyai 13 bola. Wei mempunyai 11 bola. Kira mempunyai 10 bola.

Urutan banyak bola dari yang terkecil: .... , .... , ....
Pilihan: A. 13, 11, 10
B. 10, 13, 11
C. 11, 10, 13
D. 10, 11, 13
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 37. Soal `31e0c54a133ed9b166d1ed06`

Malosi mempunyai 5 kelereng. Halim mempunyai 2 kelereng lebihnya dari Malosi.<br><br>Berapakah selisih banyak kelereng Halim dan Malosi?

| Opsi | Isi |
|---|---|
| A | 7 |
| B | 9 |
| C | 5 |
| D | 2 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Kelereng Malosi = 5. Kelereng Halim = 5 + 2 = 7. Selisih = 7 - 5 = 2.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8f952ac18255d2f8027b25dacae02dd43b6017e6da7ffdeeb08fa991304b6991`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Medium | 1426 |
| 2 | success | valid / verified | applying | conceptual | Medium | 1472 |
| 3 | success | valid / verified | applying | conceptual | Medium | 1435 |

Run 1 — solusi: Kelereng Malosi = 5. Kelereng Halim = 5 + 2 = 7. Selisih = 7 - 5 = 2.
- Domain kognitif `classify/applying`: Siswa perlu memahami hubungan 'lebih dari' untuk menentukan jumlah kelereng Halim, kemudian menerapkan operasi pengurangan untuk mencari selisih. Ini adalah penerapan konsep dasar pada situasi rutin.. Bukti: Halim mempunyai 2 kelereng lebihnya dari Malosi; Berapakah selisih banyak kelereng Halim dan Malosi?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep selisih dan hubungan kuantitatif antar dua objek, yang merupakan pengetahuan konseptual.. Bukti: 2 kelereng lebihnya; selisih banyak kelereng
- Intended difficulty `classify/Medium`: Soal ini melibatkan dua langkah rutin (menentukan jumlah Halim, lalu mencari selisih) yang sesuai untuk tingkat kelas 1.. Bukti: Malosi mempunyai 5 kelereng; Halim mempunyai 2 kelereng lebihnya; Berapakah selisih

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar dan pemahaman konsep perbandingan jumlah. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 1 sudah diajarkan perbandingan jumlah dan selisih sederhana. Soal ini menuntut dua langkah logis yang rutin. |

Run 2 — solusi: Kelereng Malosi = 5. Kelereng Halim = 5 + 2 = 7. Selisih = 7 - 5 = 2.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep penjumlahan untuk mencari jumlah kelereng Halim, kemudian menerapkan konsep selisih (pengurangan) untuk membandingkan kedua jumlah tersebut.. Bukti: Halim mempunyai 2 kelereng lebihnya dari Malosi; Berapakah selisih banyak kelereng Halim dan Malosi?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang hubungan antara kuantitas (konsep selisih) dan prosedur aritmatika dasar untuk menyelesaikannya.. Bukti: 2 kelereng lebihnya; selisih banyak kelereng
- Intended difficulty `classify/Medium`: Soal ini memerlukan dua langkah berpikir (menentukan jumlah Halim, lalu mencari selisih), yang merupakan tuntutan standar untuk kelas 1 dalam memahami konsep perbandingan.. Bukti: Malosi mempunyai 5 kelereng; Halim mempunyai 2 kelereng lebihnya; Berapakah selisih

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dasar 1-10 dan pemahaman konsep 'lebih dari' sebagai selisih. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 1 sudah diperkenalkan dengan konsep perbandingan jumlah, namun soal ini menuntut pemahaman dua tahap (menghitung jumlah kedua lalu mencari selisih) yang sedikit lebih kompleks daripada sekadar menghitung jumlah. |

Run 3 — solusi: Banyak kelereng Halim = 5 + 2 = 7. Selisih = 7 - 5 = 2.
- Domain kognitif `classify/applying`: Siswa perlu menerapkan konsep 'lebih dari' untuk menentukan jumlah kelereng Halim, kemudian menerapkan konsep selisih (pengurangan) untuk membandingkan kedua jumlah tersebut.. Bukti: Halim mempunyai 2 kelereng lebihnya dari Malosi; Berapakah selisih banyak kelereng Halim dan Malosi?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman siswa tentang hubungan antar kuantitas (konsep selisih) dan prosedur penjumlahan/pengurangan dasar.. Bukti: 5 kelereng; 2 kelereng lebihnya; selisih
- Intended difficulty `classify/Medium`: Soal ini menuntut siswa melakukan dua langkah rutin: menentukan jumlah kelereng Halim (5+2) dan menghitung selisih (7-5). Ini adalah standar untuk kelas 1.. Bukti: 5 kelereng; 2 kelereng lebihnya; selisih

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Penjumlahan dan pengurangan dasar dalam lingkup 10, pemahaman konsep 'lebih dari'. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 1 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 1 sudah diajarkan membandingkan dua kumpulan benda dan menghitung selisih sederhana. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Medium": 3} | unanimous_3_0 / unanimous | Medium |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 82/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.005753; applying=0.994247; reasoning=0.000000 | applying | 0.994247 | 0.032231 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.115207; conceptual=0.800676; procedural=0.084117; metacognitive=0.000000 | conceptual | 0.800676 | 0.458192 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.817709; Medium=0.179379; Hard=0.002912 | Easy | 0.817709 | 0.445823 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.994247; −Σp ln(p) = 0.035410; H = 0.035410/ln(3) = 0.032231; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.800676; −Σp ln(p) = 0.635189; H = 0.635189/ln(4) = 0.458192; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.817709; −Σp ln(p) = 0.489787; H = 0.489787/ln(3) = 0.445823; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Mengenal Konsep Lebih dari, Kurang dari, dan Selisih
Tipe soal: multiple_choice
Stimulus: -
Soal: Malosi mempunyai 5 kelereng. Halim mempunyai 2 kelereng lebihnya dari Malosi.

Berapakah selisih banyak kelereng Halim dan Malosi?
Pilihan: A. 7
B. 9
C. 5
D. 2
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Medium"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Medium", "agreement": false}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 38. Soal `fafff0345aa730c0722fc259`

Hari Minggu telah tiba. Tika membantu Ibu memasak di dapur. Mereka membuat donat. Tika membantu Ibu menghias donat. Ibu menghias 7 kue donat. Tika menghias 6 donat. Tika sangat senang.<br><br>Siapa yang memiliki donat lebih banyak?

| Opsi | Isi |
|---|---|
| A | Tidak bisa ditentukan |
| B | Sama banyak |
| C | Ibu |
| D | Tika |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Ibu menghias 7 donat, Tika menghias 6 donat. Karena 7 > 6, maka Ibu memiliki donat lebih banyak.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4240274822d77119f03e650517b2781293bc6cbd30d797cb3a5519d83270a962`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1408 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1399 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1411 |

Run 1 — solusi: Ibu menghias 7 donat, Tika menghias 6 donat. Karena 7 > 6, maka Ibu memiliki donat lebih banyak.
- Domain kognitif `classify/applying`: Siswa perlu membandingkan dua kuantitas yang diberikan secara eksplisit (7 dan 6) untuk menentukan mana yang lebih besar. Ini adalah proses applying karena menerapkan konsep perbandingan bilangan pada situasi rutin.. Bukti: Ibu menghias 7 kue donat; Tika menghias 6 donat; Siapa yang memiliki donat lebih banyak?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep perbandingan kuantitas (lebih dari/kurang dari) antara dua bilangan cacah.. Bukti: 7 kue donat; 6 donat; lebih banyak
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin untuk kelas 1, hanya melibatkan perbandingan langsung dua bilangan satu digit yang sudah tersedia dalam teks.. Bukti: Ibu menghias 7 kue donat; Tika menghias 6 donat; Siapa yang memiliki donat lebih banyak?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan dua bilangan cacah 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 yang menekankan perbandingan bilangan dasar. |

Run 2 — solusi: Ibu menghias 7 donat, Tika menghias 6 donat. Karena 7 > 6, maka Ibu memiliki donat lebih banyak.
- Domain kognitif `classify/applying`: Siswa perlu membandingkan dua bilangan (7 dan 6) untuk menentukan mana yang lebih besar. Ini adalah proses penerapan konsep perbandingan dasar.. Bukti: Ibu menghias 7 kue donat; Tika menghias 6 donat; Siapa yang memiliki donat lebih banyak?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang nilai bilangan dan hubungan 'lebih dari' dalam konteks perbandingan jumlah.. Bukti: 7 kue donat; 6 donat; lebih banyak
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan perbandingan dua bilangan satu digit yang eksplisit dalam cerita pendek.. Bukti: Ibu menghias 7 kue donat; Tika menghias 6 donat; Siapa yang memiliki donat lebih banyak?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan dua bilangan cacah sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 SD yang menekankan perbandingan jumlah benda konkret atau angka sampai 10. |

Run 3 — solusi: Ibu menghias 7 donat, Tika menghias 6 donat. Karena 7 > 6, maka Ibu memiliki donat lebih banyak.
- Domain kognitif `classify/applying`: Siswa perlu membandingkan dua kuantitas yang diberikan secara eksplisit untuk menentukan mana yang lebih besar, yang merupakan proses penerapan konsep perbandingan dasar.. Bukti: Ibu menghias 7 kue donat. Tika menghias 6 donat.; Siapa yang memiliki donat lebih banyak?
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan urutan bilangan (lebih dari/kurang dari) antara dua kuantitas.. Bukti: Ibu menghias 7 kue donat. Tika menghias 6 donat.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan perbandingan langsung antara dua angka tunggal dalam konteks cerita yang sederhana.. Bukti: Ibu menghias 7 kue donat. Tika menghias 6 donat.; Siapa yang memiliki donat lebih banyak?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman urutan bilangan 1-10 dan konsep perbandingan lebih dari/kurang dari. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai dengan kurikulum kelas 1 yang menekankan perbandingan dua kumpulan benda atau angka hingga 10. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 101/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000000; applying=1.000000; reasoning=0.000000 | applying | 1.000000 | 0.000004 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.027509; conceptual=0.962838; procedural=0.009652; metacognitive=0.000000 | conceptual | 0.962838 | 0.129917 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.839304; Medium=0.155455; Hard=0.005241 | Easy | 0.839304 | 0.422274 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 1.000000; −Σp ln(p) = 0.000005; H = 0.000005/ln(3) = 0.000004; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.962838; −Σp ln(p) = 0.180103; H = 0.180103/ln(4) = 0.129917; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.839304; −Σp ln(p) = 0.463915; H = 0.463915/ln(3) = 0.422274; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Mengenal Konsep Lebih dari, Kurang dari, dan Selisih
Tipe soal: multiple_choice
Stimulus: -
Soal: Hari Minggu telah tiba. Tika membantu Ibu memasak di dapur. Mereka membuat donat. Tika membantu Ibu menghias donat. Ibu menghias 7 kue donat. Tika menghias 6 donat. Tika sangat senang.

Siapa yang memiliki donat lebih banyak?
Pilihan: A. Tidak bisa ditentukan
B. Sama banyak
C. Ibu
D. Tika
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 39. Soal `4a1c88e1d656ed6e318fbc08`

Halim mempunyai 11 kelereng. Malosi mempunyai 6 kelereng.<br><br>Berapa jumlah kelereng mereka?

| Opsi | Isi |
|---|---|
| A | 18 |
| B | 16 |
| C | 5 |
| D | 17 |

Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: 11 + 6 = 17
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `8b06f5cbe3683f666688563bd2a26215bbdfb6d1f35092e84e0e70733c9e7792`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1300 |
| 2 | success | valid / verified | knowing | procedural | Easy | 1316 |
| 3 | success | valid / verified | applying | procedural | Easy | 1307 |

Run 1 — solusi: 11 + 6 = 17
- Domain kognitif `classify/applying`: Siswa diminta melakukan operasi penjumlahan dasar yang merupakan prosedur rutin untuk menyelesaikan masalah cerita sederhana.. Bukti: Halim mempunyai 11 kelereng. Malosi mempunyai 6 kelereng.; Berapa jumlah kelereng mereka?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa tentang algoritma penjumlahan dasar (prosedural) untuk menggabungkan dua kuantitas.. Bukti: Berapa jumlah kelereng mereka?
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah penjumlahan satu langkah yang sangat standar untuk kelas 1, menggunakan angka di bawah 20 tanpa teknik menyimpan yang kompleks.. Bukti: 11 kelereng; 6 kelereng; jumlah kelereng mereka

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan kemampuan menghitung sampai 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi penjumlahan 11+6 adalah materi inti kelas 1 yang bersifat rutin dan langsung. |

Run 2 — solusi: 11 + 6 = 17
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi penjumlahan dasar (11+6) yang merupakan prosedur rutin dalam matematika kelas 1.. Bukti: Halim mempunyai 11 kelereng. Malosi mempunyai 6 kelereng.; Berapa jumlah kelereng mereka?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritma penjumlahan dasar (prosedural) untuk menyelesaikan masalah kontekstual sederhana.. Bukti: 11 kelereng; 6 kelereng; jumlah
- Intended difficulty `classify/Easy`: Soal ini bersifat rutin, menggunakan representasi angka yang familiar, dan hanya memerlukan satu langkah operasi penjumlahan dasar tanpa kendala tambahan.. Bukti: 11 kelereng; 6 kelereng; Berapa jumlah kelereng mereka?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan bilangan cacah hingga 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan dua bilangan dengan hasil di bawah 20 adalah standar kompetensi dasar kelas 1. |

Run 3 — solusi: 11 + 6 = 17
- Domain kognitif `classify/applying`: Siswa diminta melakukan operasi penjumlahan dasar yang merupakan prosedur rutin untuk menyelesaikan masalah kontekstual sederhana.. Bukti: Berapa jumlah kelereng mereka?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman siswa terhadap algoritma penjumlahan dasar (prosedural) untuk menggabungkan dua kuantitas.. Bukti: 11 kelereng; 6 kelereng; jumlah kelereng mereka
- Intended difficulty `classify/Easy`: Soal ini merupakan masalah penjumlahan satu langkah yang sangat mendasar dan familiar bagi siswa kelas 1.. Bukti: 11 kelereng; 6 kelereng; Berapa jumlah kelereng mereka?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan fakta bilangan hingga 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi penjumlahan 11+6 adalah standar kurikulum kelas 1, dengan beban kognitif yang rendah karena tidak memerlukan strategi non-rutin. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 2, "knowing": 1} | majority_2_of_3 / adjudicated | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2505`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `applying`: Siswa diminta menerapkan operasi penjumlahan dasar untuk menyelesaikan masalah cerita sederhana yang merupakan prosedur rutin.
- Dimensi pengetahuan `procedural`: Soal ini menguji penguasaan algoritma penjumlahan dasar (prosedural) untuk menggabungkan dua kuantitas.
- Intended difficulty `Easy`: Soal ini adalah masalah penjumlahan satu langkah yang sangat standar dan rutin untuk kelas 1, dengan beban kognitif rendah.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep penjumlahan dasar dan fakta bilangan hingga 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi penjumlahan 11+6 adalah materi inti kelas 1 yang bersifat rutin dan langsung tanpa memerlukan strategi non-rutin. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 69/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.056262; applying=0.943738; reasoning=0.000000 | applying | 0.943738 | 0.197118 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.321111; conceptual=0.630184; procedural=0.048705; metacognitive=0.000000 | conceptual | 0.630184 | 0.579199 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.873440; Medium=0.123988; Hard=0.002572 | Easy | 0.873440 | 0.357143 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.943738; −Σp ln(p) = 0.216556; H = 0.216556/ln(3) = 0.197118; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.630184; −Σp ln(p) = 0.802940; H = 0.802940/ln(4) = 0.579199; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.873440; −Σp ln(p) = 0.392362; H = 0.392362/ln(3) = 0.357143; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Penjumlahan yang Hasilnya kurang dari 20
Tipe soal: multiple_choice
Stimulus: -
Soal: Halim mempunyai 11 kelereng. Malosi mempunyai 6 kelereng.

Berapa jumlah kelereng mereka?
Pilihan: A. 18
B. 16
C. 5
D. 17
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 40. Soal `c5a941d72ce972bb9d49a4cc`

Hitunglah operasi penjumlahan berikut. Gunakan cara yang paling mudah.<br><br>14 + 5 = ....

| Opsi | Isi |
|---|---|
| A | 19 |
| B | 9 |
| C | 20 |
| D | 14 |

Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: 14 + 5 = 19. Menjumlahkan satuan 4 + 5 = 9, lalu menambahkan puluhan 10 + 9 = 19.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung', 'menerapkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `b9286a2185815d733cea4c7fb4e8c52720cfba7c22449960f6989b1fa53b4f4d`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 1280 |
| 2 | success | valid / verified | knowing | procedural | Easy | 1275 |
| 3 | success | valid / verified | knowing | procedural | Easy | 1263 |

Run 1 — solusi: 14 + 5 = 19. Menjumlahkan satuan 4 + 5 = 9, lalu menambahkan puluhan 10 + 9 = 19.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi penjumlahan dasar yang sudah dipelajari di kelas 1, yaitu menjumlahkan bilangan satu digit ke bilangan dua digit (belasan).. Bukti: 14 + 5 = ..
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dasar tentang operasi penjumlahan bilangan cacah.. Bukti: 14 + 5 = ..
- Intended difficulty `classify/Easy`: Soal ini adalah prosedur standar penjumlahan bilangan di bawah 20 yang sangat familiar bagi siswa kelas 1.. Bukti: 14 + 5 = ..

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dasar dan penjumlahan bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Penjumlahan 14+5 adalah materi dasar kelas 1 yang rutin dan tidak memerlukan strategi kompleks. |

Run 2 — solusi: 14 + 5 = 19. Penjumlahan dilakukan dengan menambahkan satuan 4 + 5 = 9, kemudian digabungkan dengan puluhan 10, sehingga 10 + 9 = 19.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi penjumlahan dasar yang merupakan prosedur rutin dan langsung.. Bukti: 14 + 5 = ..
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman algoritma penjumlahan dasar (prosedural) untuk bilangan di bawah 20.. Bukti: 14 + 5 = ..
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur penjumlahan satu digit dengan bilangan belasan yang sangat familiar bagi siswa kelas 1.. Bukti: 14 + 5 = ..

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dasar dan penjumlahan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi penjumlahan 14+5 adalah standar kurikulum kelas 1, tidak memerlukan strategi kompleks. |

Run 3 — solusi: 14 + 5 = 19. Penjumlahan 4 satuan dengan 5 satuan menghasilkan 9, ditambah 1 puluhan menjadi 19.
- Domain kognitif `classify/knowing`: Siswa diminta melakukan operasi penjumlahan dasar yang merupakan prosedur rutin.. Bukti: 14 + 5 = ..
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman algoritma penjumlahan dasar (prosedural) untuk bilangan di bawah 20.. Bukti: 14 + 5 = ..
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi penjumlahan satu digit dengan dua digit tanpa teknik menyimpan, yang sangat familiar bagi siswa kelas 1.. Bukti: 14 + 5 = ..

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman nilai tempat dasar dan penjumlahan bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi penjumlahan 14+5 adalah standar kurikulum kelas 1, tidak memerlukan strategi kompleks. |

Histori retry: run 3 sebelumnya `failed` / `ServerError:503`. Percobaan gagal ini bukan suara kelas; tabel run di atas berisi hasil terbaru.

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 70/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.987252; applying=0.012748; reasoning=0.000000 | knowing | 0.987252 | 0.062150 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.289140; conceptual=0.616053; procedural=0.094807; metacognitive=0.000000 | conceptual | 0.616053 | 0.635193 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.898797; Medium=0.098771; Hard=0.002432 | Easy | 0.898797 | 0.308744 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.987252; −Σp ln(p) = 0.068278; H = 0.068278/ln(3) = 0.062150; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.616053; −Σp ln(p) = 0.880564; H = 0.880564/ln(4) = 0.635193; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.898797; −Σp ln(p) = 0.339189; H = 0.339189/ln(3) = 0.308744; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Penjumlahan yang Hasilnya kurang dari 20
Tipe soal: multiple_choice
Stimulus: -
Soal: Hitunglah operasi penjumlahan berikut. Gunakan cara yang paling mudah.

14 + 5 = ....
Pilihan: A. 19
B. 9
C. 20
D. 14
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 41. Soal `54e65cf97cc65f3ef126daef`

Ibu membeli 13 bolu kukus. Malosi memakan 2 bolu kukus.<br><br>Berapakah sisa bolu kukus Ibu sekarang?

| Opsi | Isi |
|---|---|
| A | 10 |
| B | 11 |
| C | 15 |
| D | 12 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: 13 - 2 = 11
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `80d1844d6b8b7f2d4e32fac770fcb8b8191211326e1882f35ca957447ecf18a7`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 1329 |
| 2 | success | valid / verified | applying | procedural | Easy | 1309 |
| 3 | success | valid / verified | applying | procedural | Easy | 1316 |

Run 1 — solusi: 13 - 2 = 11
- Domain kognitif `classify/applying`: Siswa diminta menerapkan operasi pengurangan dasar pada situasi kontekstual yang rutin.. Bukti: Ibu membeli 13 bolu kukus. Malosi memakan 2 bolu kukus.; Berapakah sisa bolu kukus Ibu sekarang?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pengurangan dasar (prosedural) dalam konteks pengurangan jumlah benda.. Bukti: 13 bolu kukus; memakan 2 bolu kukus
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur pengurangan satu digit dari dua digit yang sangat familiar bagi siswa kelas 1, dengan beban kognitif rendah.. Bukti: 13 bolu kukus; memakan 2 bolu kukus

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan pengurangan bilangan 1-20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini sesuai dengan standar kompetensi kelas 1 untuk operasi pengurangan bilangan di bawah 20. |

Run 2 — solusi: 13 - 2 = 11
- Domain kognitif `classify/applying`: Siswa diminta menerapkan operasi pengurangan dasar pada situasi kontekstual yang rutin.. Bukti: Ibu membeli 13 bolu kukus. Malosi memakan 2 bolu kukus.; Berapakah sisa bolu kukus Ibu sekarang?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji kemampuan siswa dalam melakukan algoritma pengurangan bilangan cacah.. Bukti: 13 - 2
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur standar pengurangan bilangan di bawah 20 yang sangat familiar bagi siswa kelas 1.. Bukti: 13 bolu kukus; memakan 2 bolu kukus

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan pengurangan bilangan 1-20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan 13-2 adalah standar kompetensi kelas 1 yang bersifat langsung tanpa langkah tambahan. |

Run 3 — solusi: 13 - 2 = 11
- Domain kognitif `classify/applying`: Siswa diminta menerapkan prosedur pengurangan dasar untuk menyelesaikan masalah kontekstual sederhana.. Bukti: Ibu membeli 13 bolu kukus. Malosi memakan 2 bolu kukus. Berapakah sisa bolu kukus Ibu sekarang?
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman tentang algoritma pengurangan dasar (prosedural) dalam konteks pengurangan jumlah objek.. Bukti: 13 bolu kukus; memakan 2; sisa
- Intended difficulty `classify/Easy`: Soal ini merupakan prosedur rutin satu langkah yang sesuai untuk kelas 1, dengan beban kognitif rendah.. Bukti: 13 bolu kukus; memakan 2; Berapakah sisa

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan pengurangan bilangan di bawah 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Soal ini adalah standar operasi pengurangan satu digit dari bilangan dua digit yang umum diajarkan di kelas 1. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 70/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000336; applying=0.999664; reasoning=0.000000 | applying | 0.999664 | 0.002752 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.394923; conceptual=0.557740; procedural=0.047337; metacognitive=0.000000 | conceptual | 0.557740 | 0.603733 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.897328; Medium=0.097928; Hard=0.004744 | Easy | 0.897328 | 0.318705 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999664; −Σp ln(p) = 0.003023; H = 0.003023/ln(3) = 0.002752; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.557740; −Σp ln(p) = 0.836951; H = 0.836951/ln(4) = 0.603733; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.897328; −Σp ln(p) = 0.350133; H = 0.350133/ln(3) = 0.318705; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Pengurangan yang Hasilnya Kurang dari 20
Tipe soal: multiple_choice
Stimulus: -
Soal: Ibu membeli 13 bolu kukus. Malosi memakan 2 bolu kukus.

Berapakah sisa bolu kukus Ibu sekarang?
Pilihan: A. 10
B. 11
C. 15
D. 12
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 42. Soal `3dbc40f08ab7c63a376fc3e5`

Hitunglah operasi pengurangan berikut. Gunakan cara yang paling mudah.<br><br>15 – 4 = ....

| Opsi | Isi |
|---|---|
| A | 12 |
| B | 11 |
| C | 19 |
| D | 10 |

Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: 15 - 4 = 11
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['menghitung', 'menerapkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `c44dc01b049dfe14e5f2d64abc28a6ab4ff41bf727bcc546af7e36b9ac309737`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | procedural | Easy | 1231 |
| 2 | success | valid / verified | knowing | procedural | Easy | 1263 |
| 3 | success | valid / verified | knowing | factual | Easy | 1270 |

Run 1 — solusi: 15 - 4 = 11
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi pengurangan dasar secara langsung.. Bukti: 15 – 4 = ..
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dasar tentang pengurangan bilangan di bawah 20.. Bukti: 15 – 4 = ..
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi pengurangan satu langkah yang sangat familiar bagi siswa kelas 1.. Bukti: 15 – 4 = ..

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan urutan bilangan. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan 15-4 adalah standar kurikulum kelas 1 yang bersifat rutin dan langsung. |

Run 2 — solusi: 15 - 4 = 11. Operasi pengurangan dasar dengan bilangan di bawah 20.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan operasi pengurangan dasar yang sudah dipelajari di kelas 1, yaitu pengurangan bilangan di bawah 20.. Bukti: 15 – 4 = ..
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji kemampuan prosedural dasar dalam melakukan operasi pengurangan.. Bukti: 15 – 4 = ..
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi pengurangan satu langkah yang sangat mendasar dan familiar bagi siswa kelas 1.. Bukti: 15 – 4 = ..

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan pengurangan bilangan di bawah 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan 15-4 adalah standar kompetensi kelas 1 yang bersifat rutin dan langsung. |

Run 3 — solusi: 15 - 4 = 11
- Domain kognitif `classify/knowing`: Soal meminta siswa melakukan operasi pengurangan dasar secara langsung, yang termasuk dalam kategori knowing.. Bukti: 15 – 4 = ....
- Dimensi pengetahuan `classify/factual`: Soal ini menguji pemahaman tentang fakta pengurangan dasar dalam lingkup bilangan 20, yang merupakan pengetahuan faktual.. Bukti: 15 – 4 = ....
- Intended difficulty `classify/Easy`: Soal ini merupakan operasi pengurangan satu digit dari dua digit yang sangat rutin dan familiar bagi siswa kelas 1.. Bukti: 15 – 4 = ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan urutan bilangan hingga 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan 15-4 adalah standar kompetensi dasar kelas 1 yang bersifat langsung dan tidak memerlukan strategi kompleks. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / adjudicated | knowing |
| Dimensi pengetahuan | {"procedural": 2, "factual": 1} | majority_2_of_3 / adjudicated | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `2308`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Soal ini menuntut siswa untuk melakukan operasi pengurangan dasar secara langsung tanpa perlu menyusun strategi atau mengintegrasikan informasi kompleks.
- Dimensi pengetahuan `procedural`: Soal ini menguji penguasaan algoritma pengurangan dasar, yang merupakan bagian dari pengetahuan prosedural.
- Intended difficulty `Easy`: Soal ini adalah operasi aritmatika satu langkah yang sangat rutin dan familiar bagi siswa kelas 1, dengan beban kognitif yang rendah.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Pemahaman konsep pengurangan dasar dan urutan bilangan hingga 20. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Operasi pengurangan 15-4 merupakan standar kompetensi dasar kelas 1 yang bersifat langsung dan rutin. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 70/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.998046; applying=0.001954; reasoning=0.000000 | knowing | 0.998046 | 0.012871 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.622915; conceptual=0.206623; procedural=0.170462; metacognitive=0.000000 | factual | 0.622915 | 0.665268 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.920146; Medium=0.076652; Hard=0.003201 | Easy | 0.920146 | 0.265649 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.998046; −Σp ln(p) = 0.014141; H = 0.014141/ln(3) = 0.012871; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.622915; −Σp ln(p) = 0.922258; H = 0.922258/ln(4) = 0.665268; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.920146; −Σp ln(p) = 0.291845; H = 0.291845/ln(3) = 0.265649; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Pengurangan yang Hasilnya Kurang dari 20
Tipe soal: multiple_choice
Stimulus: -
Soal: Hitunglah operasi pengurangan berikut. Gunakan cara yang paling mudah.

15 – 4 = ....
Pilihan: A. 12
B. 11
C. 19
D. 10
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "factual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 43. Soal `ff83d65211d6e4aa98e13b06`

Perhatikan gambar berikut.<br><br>Urutan bunga dari paling pendek: ...., ...., ....

| Opsi | Isi |
|---|---|
| A | B, C, A |
| B | C, A, B |
| C | A, C, B |
| D | A, B, C |

![Gambar sumber soal 43](<../images/kelas1_panduan_siswa_kelas1.pdf-0218-01.png>)


Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Berdasarkan pengamatan visual, tinggi bunga adalah A < C < B. Maka urutan dari yang paling pendek adalah A, C, B.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0218-01.png. Transkripsi visual: Terdapat tiga bunga matahari yang berjejer di atas garis tanah yang sama, masing-masing diberi label A, B, dan C. Bunga A adalah yang paling pendek, bunga C memiliki tinggi sedang, dan bunga B adalah yang paling tinggi.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `bb866c2af831fa0410e3b49aa3df3b442a36ea6328c7468124d78b7a390c80da`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2475 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2478 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2494 |

Run 1 — solusi: Berdasarkan pengamatan visual, tinggi bunga adalah A < C < B. Maka urutan dari yang paling pendek adalah A, C, B.
- Domain kognitif `classify/knowing`: Siswa diminta untuk melakukan perbandingan visual langsung dan mengurutkan objek berdasarkan atribut panjang (tinggi), yang merupakan proses rutin dalam domain kognitif knowing.. Bukti: Urutan bunga dari paling pendek
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep dasar tentang urutan dan perbandingan panjang (atribut fisik), yang termasuk dalam dimensi pengetahuan konseptual.. Bukti: Urutan bunga dari paling pendek
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan perbandingan visual langsung tanpa perhitungan kompleks atau strategi non-rutin.. Bukti: Urutan bunga dari paling pendek

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membedakan panjang/tinggi benda secara visual. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena hanya memerlukan observasi visual langsung terhadap tiga objek yang sejajar. |

Run 2 — solusi: Berdasarkan pengamatan visual, tinggi bunga adalah A < C < B. Maka urutan dari yang paling pendek adalah A, C, B.
- Domain kognitif `classify/knowing`: Siswa perlu melakukan perbandingan visual langsung dan mengurutkan objek berdasarkan atribut panjang/tinggi, yang merupakan proses rutin dalam domain kognitif knowing.. Bukti: Urutan bunga dari paling pendek
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep dasar tentang urutan dan perbandingan panjang, yang termasuk dalam pengetahuan konseptual.. Bukti: Urutan bunga dari paling pendek
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan perbandingan visual langsung dari tiga objek yang sudah disejajarkan pada garis dasar yang sama.. Bukti: Urutan bunga dari paling pendek

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membedakan tinggi benda secara visual. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena hanya memerlukan observasi visual sederhana tanpa perhitungan atau manipulasi kompleks. |

Run 3 — solusi: Berdasarkan pengamatan visual, tinggi bunga adalah A < C < B. Maka urutan dari yang paling pendek adalah A, C, B.
- Domain kognitif `classify/applying`: Siswa perlu melakukan perbandingan visual langsung dan mengurutkan objek berdasarkan atribut panjang/tinggi, yang merupakan proses rutin dalam domain kognitif applying.. Bukti: Urutan bunga dari paling pendek
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep dasar tentang urutan (seriasi) berdasarkan atribut fisik (tinggi), yang termasuk dalam dimensi pengetahuan konseptual.. Bukti: Urutan bunga dari paling pendek
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan perbandingan visual langsung tanpa perhitungan kompleks atau strategi non-rutin.. Bukti: Urutan bunga dari paling pendek: ...., ...., ....

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membedakan tinggi benda secara visual. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena hanya memerlukan observasi visual langsung terhadap tiga objek yang diletakkan pada garis dasar yang sama. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 2, "applying": 1} | majority_2_of_3 / adjudicated | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / adjudicated | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / adjudicated | Easy |

Adjudikasi AI: `success`; token `3663`.
Konten: `valid`; kunci: `verified`; masalah: .
- Domain kognitif `knowing`: Siswa diminta untuk melakukan perbandingan visual langsung dan mengurutkan objek berdasarkan atribut panjang (tinggi), yang merupakan proses rutin dalam domain kognitif knowing.
- Dimensi pengetahuan `conceptual`: Soal ini menguji pemahaman konsep dasar tentang urutan (seriasi) berdasarkan atribut fisik (tinggi), yang termasuk dalam dimensi pengetahuan konseptual.
- Intended difficulty `Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan perbandingan visual langsung dari tiga objek yang sudah disejajarkan pada garis dasar yang sama.

Profil difficulty hasil adjudikasi:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membedakan tinggi benda secara visual. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena hanya memerlukan observasi visual sederhana tanpa perhitungan atau manipulasi kompleks. |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 137/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.738380; applying=0.261620; reasoning=0.000000 | knowing | 0.738380 | 0.523155 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.017097; conceptual=0.981615; procedural=0.001287; metacognitive=0.000000 | conceptual | 0.981615 | 0.069500 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.731651; Medium=0.264472; Hard=0.003877 | Easy | 0.731651 | 0.547861 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.738380; −Σp ln(p) = 0.574744; H = 0.574744/ln(3) = 0.523155; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.981615; −Σp ln(p) = 0.096348; H = 0.096348/ln(4) = 0.069500; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.731651; −Σp ln(p) = 0.601886; H = 0.601886/ln(3) = 0.547861; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Membandingkan dan Mengurutkan Panjang Benda
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan gambar berikut.

Urutan bunga dari paling pendek: ...., ...., ....
Pilihan: A. B, C, A
B. C, A, B
C. A, C, B
D. A, B, C
Transkripsi visual: Terdapat tiga bunga matahari yang berjejer di atas garis tanah yang sama, masing-masing diberi label A, B, dan C. Bunga A adalah yang paling pendek, bunga C memiliki tinggi sedang, dan bunga B adalah yang paling tinggi.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "knowing", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 44. Soal `dc65bbd6611c904972206f6c`

Burung yang terbang paling tinggi adalah ....

| Opsi | Isi |
|---|---|
| A | Ketiga burung terbang sama tinggi |
| B | C |
| C | B |
| D | A |

![Gambar sumber soal 44](<../images/kelas1_panduan_siswa_kelas1.pdf-0219-07.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Secara visual, posisi vertikal burung C berada paling atas dibandingkan burung A dan B, sehingga burung C terbang paling tinggi.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0219-07.png. Transkripsi visual: Terdapat tiga burung yang diberi label A, B, dan C. Burung C berada di posisi paling atas (paling tinggi). Burung A berada di posisi tengah. Burung B berada di posisi paling bawah.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `4e42f565fcd0f0f0a43d26b54e036b6d5944a2817b449744122a85a477e00ce5`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | knowing | conceptual | Easy | 2419 |
| 2 | success | valid / verified | knowing | conceptual | Easy | 2411 |
| 3 | success | valid / verified | knowing | conceptual | Easy | 2430 |

Run 1 — solusi: Secara visual, posisi vertikal burung C berada paling atas dibandingkan burung A dan B, sehingga burung C terbang paling tinggi.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan observasi visual langsung untuk membandingkan posisi benda (burung) dalam ruang dua dimensi, yang merupakan proses pengenalan sederhana.. Bukti: Burung yang terbang paling tinggi adalah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep dasar tentang perbandingan posisi atau ketinggian (konseptual) dalam konteks visual.. Bukti: paling tinggi
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan persepsi visual langsung tanpa perhitungan atau strategi kompleks.. Bukti: Burung yang terbang paling tinggi adalah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membedakan posisi atas dan bawah secara visual. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena membandingkan posisi benda secara visual adalah materi awal yang rutin. |

Run 2 — solusi: Berdasarkan posisi vertikal pada gambar, burung C berada pada posisi paling atas dibandingkan burung A dan B.
- Domain kognitif `classify/knowing`: Siswa hanya perlu mengenali posisi relatif objek (tinggi/rendah) secara visual tanpa melakukan perhitungan atau strategi kompleks.. Bukti: Burung yang terbang paling tinggi adalah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep dasar tentang perbandingan posisi atau ketinggian (konseptual) dalam konteks visual.. Bukti: paling tinggi
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar, hanya memerlukan observasi visual langsung terhadap posisi objek.. Bukti: Burung yang terbang paling tinggi adalah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membedakan posisi atas dan bawah secara visual. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena hanya melibatkan pengamatan visual sederhana untuk membandingkan posisi benda. |

Run 3 — solusi: Secara visual, posisi burung C berada paling tinggi dibandingkan burung A dan B.
- Domain kognitif `classify/knowing`: Siswa hanya perlu melakukan observasi visual langsung untuk mengenali posisi objek tertinggi, yang merupakan proses kognitif tingkat dasar.. Bukti: Burung yang terbang paling tinggi adalah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep dasar tentang perbandingan posisi atau ketinggian (tinggi/rendah) secara visual.. Bukti: Membandingkan dan Mengurutkan Panjang Benda
- Intended difficulty `classify/Easy`: Soal ini sangat sederhana, hanya memerlukan pengamatan visual langsung tanpa perhitungan atau prosedur kompleks, cocok untuk tingkat kelas 1.. Bukti: Burung yang terbang paling tinggi adalah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membedakan posisi atas dan bawah secara visual. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 1 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena hanya melibatkan identifikasi visual sederhana pada objek yang konkret. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"knowing": 3} | unanimous_3_0 / unanimous | knowing |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 103/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.036980; applying=0.963020; reasoning=0.000000 | applying | 0.963020 | 0.144022 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.182157; conceptual=0.808423; procedural=0.009420; metacognitive=0.000000 | conceptual | 0.808423 | 0.379473 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.869730; Medium=0.127816; Hard=0.002455 | Easy | 0.869730 | 0.363259 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.963020; −Σp ln(p) = 0.158224; H = 0.158224/ln(3) = 0.144022; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.808423; −Σp ln(p) = 0.526062; H = 0.526062/ln(4) = 0.379473; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.869730; −Σp ln(p) = 0.399081; H = 0.399081/ln(3) = 0.363259; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Membandingkan dan Mengurutkan Panjang Benda
Tipe soal: multiple_choice
Stimulus: -
Soal: Burung yang terbang paling tinggi adalah ....
Pilihan: A. Ketiga burung terbang sama tinggi
B. C
C. B
D. A
Transkripsi visual: Terdapat tiga burung yang diberi label A, B, dan C. Burung C berada di posisi paling atas (paling tinggi). Burung A berada di posisi tengah. Burung B berada di posisi paling bawah.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "knowing", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "knowing", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 45. Soal `75434d44f2b377da3027e153`

Temukan panjang pensil berikut. Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.<br><br>Urutan pensil dari paling pendek: ...., ...., ....

| Opsi | Isi |
|---|---|
| A | A, C, B |
| B | A, B, C |
| C | B, C, A |
| D | C, A, B |

![Gambar sumber soal 45](<../images/kelas1_panduan_siswa_kelas1.pdf-0225-04.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Membandingkan nilai panjang: 4 (A) < 5 (C) < 8 (B). Urutan dari terpendek adalah A, C, B.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0225-04.png. Transkripsi visual: Terdapat tiga pensil di atas kertas berpetak. Pensil A memiliki panjang 4 kotak. Pensil B memiliki panjang 8 kotak. Pensil C memiliki panjang 5 kotak.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `fac1c33fefe109b5b046e32578f85e535f1ca195f06b0664b2e0963cf742afa5`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2610 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2565 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2555 |

Run 1 — solusi: Membandingkan nilai panjang: 4 (A) < 5 (C) < 8 (B). Urutan dari terpendek adalah A, C, B.
- Domain kognitif `classify/applying`: Siswa perlu mengurutkan nilai yang sudah diberikan (4, 5, 8) dari yang terkecil ke terbesar. Ini adalah proses rutin yang menerapkan konsep perbandingan bilangan dasar.. Bukti: Urutan pensil dari paling pendek; Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang urutan bilangan dan panjang benda yang direpresentasikan oleh satuan kotak.. Bukti: Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.
- Intended difficulty `classify/Easy`: Soal ini sangat sesuai untuk kelas 1 karena menggunakan angka kecil (di bawah 10) dan prosedur pengurutan yang langsung.. Bukti: Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.; Urutan pensil dari paling pendek

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami konsep panjang dan membandingkan bilangan 1-10. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas mengurutkan tiga benda berdasarkan panjang yang sudah terukur (diberikan dalam soal) adalah tugas standar untuk kelas 1. |

Run 2 — solusi: Membandingkan nilai panjang: A=4, C=5, B=8. Urutan dari yang terkecil adalah 4, 5, 8, yaitu A, C, B.
- Domain kognitif `classify/applying`: Siswa perlu membandingkan nilai numerik yang diberikan (4, 8, 5) dan mengurutkannya. Ini adalah proses rutin yang menerapkan konsep perbandingan bilangan.. Bukti: Urutan pensil dari paling pendek
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang urutan besaran panjang yang direpresentasikan oleh angka.. Bukti: Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena nilai panjang sudah diberikan secara eksplisit, sehingga siswa hanya perlu mengurutkan tiga bilangan satu digit.. Bukti: Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.; Urutan pensil dari paling pendek

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan dan mengurutkan bilangan cacah 1-10. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena hanya melibatkan perbandingan bilangan dasar yang sudah diberikan nilainya. |

Run 3 — solusi: Membandingkan nilai panjang: 4 (A) < 5 (C) < 8 (B). Urutan dari terpendek adalah A, C, B.
- Domain kognitif `classify/applying`: Siswa perlu membandingkan nilai numerik yang diberikan (4, 8, 5) dan mengurutkannya. Ini adalah proses rutin yang menerapkan konsep perbandingan bilangan.. Bukti: Urutan pensil dari paling pendek
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang konsep urutan dan perbandingan panjang yang direpresentasikan oleh angka.. Bukti: Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan perbandingan langsung dari tiga bilangan satu digit yang sudah disediakan nilainya.. Bukti: Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan dan mengurutkan bilangan cacah 1-10. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena hanya memerlukan pengurutan bilangan sederhana yang sudah diketahui nilainya. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 138/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.220782; applying=0.779218; reasoning=0.000000 | applying | 0.779218 | 0.480511 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.011593; conceptual=0.984981; procedural=0.003426; metacognitive=0.000000 | conceptual | 0.984981 | 0.062054 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.731540; Medium=0.264504; Hard=0.003956 | Easy | 0.731540 | 0.548267 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.779218; −Σp ln(p) = 0.527895; H = 0.527895/ln(3) = 0.480511; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.984981; −Σp ln(p) = 0.086025; H = 0.086025/ln(4) = 0.062054; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.731540; −Σp ln(p) = 0.602332; H = 0.602332/ln(3) = 0.548267; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Mengukur Panjang Benda
Tipe soal: multiple_choice
Stimulus: -
Soal: Temukan panjang pensil berikut. Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.

Urutan pensil dari paling pendek: ...., ...., ....
Pilihan: A. A, C, B
B. A, B, C
C. B, C, A
D. C, A, B
Transkripsi visual: Terdapat tiga pensil di atas kertas berpetak. Pensil A memiliki panjang 4 kotak. Pensil B memiliki panjang 8 kotak. Pensil C memiliki panjang 5 kotak.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 46. Soal `62785ac6ff0622ab70a94b13`

Temukan panjang pita berikut. Panjang pita B = 5 kotak. Panjang pita C = 4 kotak.<br><br>Pita B lebih .... dari pita C.

| Opsi | Isi |
|---|---|
| A | panjang |
| B | pendek |
| C | tinggi |
| D | besar |

![Gambar sumber soal 46](<../images/kelas1_panduan_siswa_kelas1.pdf-0228-03.png>)


Kunci sumber: `A`; status AI: `verified`; jawaban diverifikasi AI: `A`.
Solusi minimum hasil AI: Pita B = 5 kotak, Pita C = 4 kotak. Karena 5 > 4, maka pita B lebih panjang dari pita C.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0228-03.png. Transkripsi visual: Terdapat gambar pita B (oranye) yang panjangnya 5 kotak pada grid dan pita C (ungu) yang panjangnya 4 kotak pada grid. Soal meminta membandingkan panjang pita B dengan pita C.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `19e852392e031c6c1cab2462628810eeb957eca3e9cb140a2cb7b4fa608cdbda`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2513 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2524 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2535 |

Run 1 — solusi: Pita B = 5 kotak, Pita C = 4 kotak. Karena 5 > 4, maka pita B lebih panjang dari pita C.
- Domain kognitif `classify/applying`: Siswa perlu membandingkan dua nilai yang sudah diberikan (5 dan 4) untuk menentukan hubungan 'lebih panjang'. Ini adalah proses applying karena menerapkan konsep perbandingan dasar pada situasi rutin.. Bukti: Panjang pita B = 5 kotak. Panjang pita C = 4 kotak.; Pita B lebih .... dari pita C.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang perbandingan panjang (lebih panjang/pendek) menggunakan satuan tidak baku (kotak).. Bukti: Panjang pita B = 5 kotak; Pita B lebih .... dari pita C
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, hanya memerlukan perbandingan dua bilangan bulat sederhana dalam konteks pengukuran panjang yang familiar.. Bukti: Panjang pita B = 5 kotak. Panjang pita C = 4 kotak.; Pita B lebih .... dari pita C.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami konsep perbandingan bilangan (lebih besar/kecil) dan istilah panjang. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena menggunakan satuan grid yang konkret dan perbandingan bilangan dasar. |

Run 2 — solusi: Pita B memiliki panjang 5 kotak dan pita C memiliki panjang 4 kotak. Karena 5 > 4, maka pita B lebih panjang daripada pita C.
- Domain kognitif `classify/applying`: Siswa diminta untuk membandingkan dua nilai panjang yang sudah diketahui (5 dan 4) dan memilih kata sifat pembanding yang tepat. Ini adalah proses menerapkan konsep perbandingan dasar pada situasi rutin.. Bukti: Panjang pita B = 5 kotak. Panjang pita C = 4 kotak.; Pita B lebih .... dari pita C.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang hubungan perbandingan panjang (lebih panjang/pendek) antara dua objek.. Bukti: Pita B lebih .... dari pita C.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, melibatkan perbandingan langsung antara dua bilangan bulat kecil (5 dan 4) dalam konteks pengukuran sederhana.. Bukti: Panjang pita B = 5 kotak. Panjang pita C = 4 kotak.; Pita B lebih .... dari pita C.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami konsep panjang dan perbandingan bilangan dasar (lebih dari/kurang dari). |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena hanya memerlukan perbandingan bilangan sederhana dalam konteks pengukuran panjang yang konkret. |

Run 3 — solusi: Pita B memiliki panjang 5 kotak dan pita C memiliki panjang 4 kotak. Karena 5 > 4, maka pita B lebih panjang dari pita C.
- Domain kognitif `classify/applying`: Siswa perlu membandingkan dua nilai numerik yang sudah diberikan (5 dan 4) untuk menentukan hubungan perbandingan (lebih panjang). Ini adalah proses penerapan konsep perbandingan dasar.. Bukti: Panjang pita B = 5 kotak. Panjang pita C = 4 kotak.; Pita B lebih .... dari pita C.
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang perbandingan panjang antara dua objek yang diukur dengan satuan tidak baku (kotak).. Bukti: Panjang pita B = 5 kotak. Panjang pita C = 4 kotak.
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, hanya memerlukan perbandingan dua bilangan bulat sederhana yang sudah disediakan dalam teks.. Bukti: Panjang pita B = 5 kotak. Panjang pita C = 4 kotak.; Pita B lebih .... dari pita C.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Memahami konsep perbandingan bilangan dasar (lebih dari/kurang dari) dan kosakata perbandingan panjang. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena hanya melibatkan perbandingan langsung dari data yang sudah eksplisit. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 112/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.594059; applying=0.405941; reasoning=0.000000 | knowing | 0.594059 | 0.614728 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.039744; conceptual=0.953516; procedural=0.006740; metacognitive=0.000000 | conceptual | 0.953516 | 0.149513 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.823523; Medium=0.173768; Hard=0.002710 | Easy | 0.823523 | 0.436929 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.594059; −Σp ln(p) = 0.675347; H = 0.675347/ln(3) = 0.614728; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.953516; −Σp ln(p) = 0.207270; H = 0.207270/ln(4) = 0.149513; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.823523; −Σp ln(p) = 0.480015; H = 0.480015/ln(3) = 0.436929; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Mengukur Panjang Benda
Tipe soal: multiple_choice
Stimulus: -
Soal: Temukan panjang pita berikut. Panjang pita B = 5 kotak. Panjang pita C = 4 kotak.

Pita B lebih .... dari pita C.
Pilihan: A. panjang
B. pendek
C. tinggi
D. besar
Transkripsi visual: Terdapat gambar pita B (oranye) yang panjangnya 5 kotak pada grid dan pita C (ungu) yang panjangnya 4 kotak pada grid. Soal meminta membandingkan panjang pita B dengan pita C.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "knowing", "blindLabel": "applying", "agreement": false}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 47. Soal `5e007b54e25f6f72efa82174`

Amati gambar buah-buahan. Lengkapi daftarnya. Daftar Buah-buahan: Ada ... buah jeruk. Ada ... buah apel. Ada ... buah mangga.<br><br>Buah yang paling banyak adalah ...

| Opsi | Isi |
|---|---|
| A | Apel |
| B | Mangga |
| C | Jambu |
| D | Jeruk |

![Gambar sumber soal 47](<../images/kelas1_panduan_siswa_kelas1.pdf-0238-11.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Menghitung jumlah masing-masing buah: jeruk ada 5, apel ada 4, mangga ada 6. Karena 6 adalah jumlah terbanyak, maka mangga adalah jawabannya.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0238-11.png. Transkripsi visual: Terdapat 15 buah dalam susunan 3x5. Baris 1: jeruk, apel, mangga, jeruk, mangga. Baris 2: apel, mangga, jeruk, mangga, apel. Baris 3: jeruk, mangga, apel, jeruk, mangga. Total jeruk: 5. Total apel: 4. Total mangga: 6.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `a5856533e5edb309fc524d04840e1d79ae8a55bf1e417f26300eb419fb70f3be`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2562 |
| 2 | success | valid / verified | applying | procedural | Easy | 2578 |
| 3 | success | valid / verified | applying | procedural | Easy | 2559 |

Run 1 — solusi: Menghitung jumlah masing-masing buah: jeruk ada 5, apel ada 4, mangga ada 6. Karena 6 adalah jumlah terbanyak, maka mangga adalah jawabannya.
- Domain kognitif `classify/applying`: Siswa perlu melakukan proses penghitungan (counting) dan membandingkan hasil hitung untuk menentukan nilai maksimum. Ini adalah penerapan prosedur dasar dalam situasi rutin.. Bukti: Amati gambar buah-buahan. Lengkapi daftarnya.; Buah yang paling banyak adalah
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural tentang cara menghitung objek dan membandingkan kuantitas (data sederhana).. Bukti: Amati gambar buah-buahan.; Lengkapi daftarnya.
- Intended difficulty `classify/Easy`: Soal ini melibatkan prosedur menghitung yang familiar bagi siswa kelas 1, dengan jumlah objek yang kecil dan terstruktur, sehingga beban kognitifnya rendah.. Bukti: Amati gambar buah-buahan.; Lengkapi daftarnya.; Buah yang paling banyak adalah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 dan membandingkan dua bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena hanya memerlukan penghitungan objek konkret dan perbandingan sederhana. |

Run 2 — solusi: Menghitung jumlah masing-masing buah: jeruk (5), apel (4), mangga (6). Membandingkan jumlah tersebut (6 > 5 > 4), maka mangga adalah yang paling banyak.
- Domain kognitif `classify/applying`: Siswa perlu melakukan proses penghitungan (counting) dan membandingkan kuantitas untuk menentukan nilai maksimum. Ini adalah penerapan prosedur dasar dalam situasi rutin.. Bukti: Amati gambar buah-buahan; Lengkapi daftarnya; Buah yang paling banyak adalah
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan teknik menghitung (prosedural) untuk mengorganisasi data visual ke dalam kategori dan membandingkannya.. Bukti: Lengkapi daftarnya; Buah yang paling banyak adalah
- Intended difficulty `classify/Easy`: Soal ini meminta siswa melakukan tugas rutin (menghitung dan membandingkan) dengan representasi visual yang jelas. Beban kognitif rendah.. Bukti: Amati gambar buah-buahan; Lengkapi daftarnya; Buah yang paling banyak adalah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 dan membandingkan dua bilangan (lebih banyak/sedikit). |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena melibatkan penghitungan objek konkret/gambar dan perbandingan sederhana yang merupakan kompetensi dasar awal. |

Run 3 — solusi: Menghitung jumlah setiap jenis buah: jeruk (5), apel (4), mangga (6). Membandingkan jumlah tersebut (6 > 5 > 4), maka mangga adalah yang paling banyak.
- Domain kognitif `classify/applying`: Siswa perlu melakukan proses penghitungan (counting) dan perbandingan (comparing) sederhana untuk menentukan nilai maksimum dari data yang disajikan secara visual.. Bukti: Amati gambar buah-buahan. Lengkapi daftarnya.; Buah yang paling banyak adalah
- Dimensi pengetahuan `classify/procedural`: Soal ini menguji pemahaman prosedural dalam menghitung objek dan mengorganisasikannya ke dalam kategori sederhana (data grouping).. Bukti: Amati gambar buah-buahan. Lengkapi daftarnya.
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya melibatkan penghitungan objek konkret yang familiar dan perbandingan langsung, sesuai dengan kemampuan dasar siswa kelas 1.. Bukti: Amati gambar buah-buahan.; Lengkapi daftarnya.; Buah yang paling banyak adalah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membilang 1-10 dan membandingkan dua bilangan. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 3 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas menghitung dan membandingkan jumlah benda konkret adalah standar kompetensi dasar untuk kelas 1 SD. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"procedural": 3} | unanimous_3_0 / unanimous | procedural |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 154/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.003223; applying=0.996777; reasoning=0.000000 | applying | 0.996777 | 0.019762 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.014018; conceptual=0.981245; procedural=0.004737; metacognitive=0.000000 | conceptual | 0.981245 | 0.074842 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.734189; Medium=0.259363; Hard=0.006448 | Easy | 0.734189 | 0.554697 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.996777; −Σp ln(p) = 0.021711; H = 0.021711/ln(3) = 0.019762; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.981245; −Σp ln(p) = 0.103753; H = 0.103753/ln(4) = 0.074842; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.734189; −Σp ln(p) = 0.609397; H = 0.609397/ln(3) = 0.554697; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Mengelompokkan Data
Tipe soal: multiple_choice
Stimulus: -
Soal: Amati gambar buah-buahan. Lengkapi daftarnya. Daftar Buah-buahan: Ada ... buah jeruk. Ada ... buah apel. Ada ... buah mangga.

Buah yang paling banyak adalah ...
Pilihan: A. Apel
B. Mangga
C. Jambu
D. Jeruk
Transkripsi visual: Terdapat 15 buah dalam susunan 3x5. Baris 1: jeruk, apel, mangga, jeruk, mangga. Baris 2: apel, mangga, jeruk, mangga, apel. Baris 3: jeruk, mangga, apel, jeruk, mangga. Total jeruk: 5. Total apel: 4. Total mangga: 6.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 48. Soal `17ba235cdc9fddc600303514`

Perhatikan tabel dan jawablah pertanyaannya.<br><br>Apa nama kue yang paling disukai?

| Opsi | Isi |
|---|---|
| A | Kue Cucur |
| B | Kue Lapis |
| C | Kue Talam |
| D | Kue Bugis |

![Gambar sumber soal 48](<../images/kelas1_panduan_siswa_kelas1.pdf-0238-12.png>)


Kunci sumber: `D`; status AI: `verified`; jawaban diverifikasi AI: `D`.
Solusi minimum hasil AI: Membandingkan nilai pada baris 'Banyak anak': 3, 5, 5, 6. Nilai terbesar adalah 6, yang berkorespondensi dengan Kue Bugis.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0238-12.png. Transkripsi visual: Tabel berjudul 'Tabel Kue Kesukaan' berisi data: Kue Talam (5), Kue Cucur (3), Kue Lapis (5), Kue Bugis (6).

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `7dd9ed153f68cfbda631d333ebc7c6746431643841089bca6c837075152c0e2e`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 2464 |
| 2 | success | valid / verified | applying | conceptual | Easy | 2462 |
| 3 | success | valid / verified | applying | conceptual | Easy | 2450 |

Run 1 — solusi: Membandingkan nilai pada baris 'Banyak anak': 3, 5, 5, 6. Nilai terbesar adalah 6, yang berkorespondensi dengan Kue Bugis.
- Domain kognitif `classify/applying`: Siswa perlu membaca data dari tabel dan melakukan perbandingan sederhana untuk menentukan nilai maksimum. Ini adalah proses applying karena menerapkan konsep perbandingan bilangan pada data yang disajikan.. Bukti: Apa nama kue yang paling disukai?; Tabel Kue Kesukaan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang bagaimana data diorganisir dalam tabel dan bagaimana menginterpretasikan hubungan antar nilai (konsep 'paling banyak').. Bukti: Tabel Kue Kesukaan
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya memerlukan pembacaan tabel sederhana dan perbandingan bilangan satu digit yang familiar bagi siswa kelas 1.. Bukti: Tabel Kue Kesukaan; Apa nama kue yang paling disukai?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca tabel sederhana dan membandingkan bilangan 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 1 sudah diajarkan membaca tabel sederhana dan membandingkan jumlah benda/data. |

Run 2 — solusi: Membandingkan nilai pada baris 'Banyak anak': 3, 5, 5, 6. Nilai terbesar adalah 6, yang berkorespondensi dengan Kue Bugis.
- Domain kognitif `classify/applying`: Siswa perlu membaca data dari tabel dan membandingkan nilai untuk menentukan nilai maksimum (paling banyak). Ini adalah proses applying karena menggunakan konsep perbandingan data sederhana dalam situasi rutin.. Bukti: Apa nama kue yang paling disukai?; Tabel Kue Kesukaan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang bagaimana data diorganisir dalam tabel dan bagaimana menginterpretasikan nilai-nilai tersebut (konsep perbandingan).. Bukti: Tabel Kue Kesukaan
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah untuk kelas 1 karena hanya memerlukan pembacaan tabel sederhana dan perbandingan angka satu digit secara langsung.. Bukti: Tabel Kue Kesukaan; Apa nama kue yang paling disukai?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membaca tabel sederhana dan membandingkan bilangan cacah sampai 10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena melibatkan interpretasi data visual dasar yang sudah diajarkan di tingkat awal. |

Run 3 — solusi: Membandingkan nilai pada baris 'Banyak anak': 6 > 5 > 3. Nilai terbesar adalah 6, yang berkorespondensi dengan Kue Bugis.
- Domain kognitif `classify/applying`: Siswa perlu membaca data dari tabel dan membandingkan nilai untuk menentukan nilai maksimum (paling disukai). Ini adalah proses applying karena menerapkan konsep perbandingan bilangan pada data yang disajikan.. Bukti: Apa nama kue yang paling disukai?; Tabel Kue Kesukaan
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman tentang cara membaca dan menginterpretasikan tabel sederhana (konsep data).. Bukti: Tabel Kue Kesukaan
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah untuk kelas 1 karena hanya memerlukan pembacaan tabel sederhana dan perbandingan bilangan satu digit yang langsung terlihat.. Bukti: Tabel Kue Kesukaan; Apa nama kue yang paling disukai?

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Mampu membaca tabel sederhana dan membandingkan bilangan 1-10. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 SD dalam topik pengumpulan dan penyajian data sederhana. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 101/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.000012; applying=0.999988; reasoning=0.000000 | applying | 0.999988 | 0.000135 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.159027; conceptual=0.831974; procedural=0.008999; metacognitive=0.000000 | conceptual | 0.831974 | 0.351898 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.869253; Medium=0.126905; Hard=0.003842 | Easy | 0.869253 | 0.368775 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999988; −Σp ln(p) = 0.000149; H = 0.000149/ln(3) = 0.000135; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.831974; −Σp ln(p) = 0.487835; H = 0.487835/ln(4) = 0.351898; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.869253; −Σp ln(p) = 0.405141; H = 0.405141/ln(3) = 0.368775; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Mengelompokkan Data
Tipe soal: multiple_choice
Stimulus: -
Soal: Perhatikan tabel dan jawablah pertanyaannya.

Apa nama kue yang paling disukai?
Pilihan: A. Kue Cucur
B. Kue Lapis
C. Kue Talam
D. Kue Bugis
Transkripsi visual: Tabel berjudul 'Tabel Kue Kesukaan' berisi data: Kue Talam (5), Kue Cucur (3), Kue Lapis (5), Kue Bugis (6).
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 49. Soal `e7d8a29f2e3a28f99529dfc8`

Diagram berikut menunjukkan jenis buah kesukaan anak-anak. Lengkapi setiap kalimat berikut.<br><br>Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.

| Opsi | Isi |
|---|---|
| A | 2 |
| B | 3 |
| C | 4 |
| D | 1 |

![Gambar sumber soal 49](<../images/kelas1_panduan_siswa_kelas1.pdf-0246-04.png>)


Kunci sumber: `B`; status AI: `verified`; jawaban diverifikasi AI: `B`.
Solusi minimum hasil AI: Jumlah anak suka belimbing adalah 7. Jumlah anak suka apel adalah 4. Selisihnya adalah 7 - 4 = 3.
Gambar sumber: images/kelas1_panduan_siswa_kelas1.pdf-0246-04.png. Transkripsi visual: Diagram batang gambar (pictograph) dengan 4 kolom buah: jeruk (6 bintang), apel (4 bintang), belimbing (7 bintang), jambu air (5 bintang). Keterangan: 1 bintang mewakili 1 anak.

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `['membandingkan']`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `f8c09af4703b188f8ba0f790af556645d169716369cf66fd943a1ed7f0869967`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | procedural | Easy | 2479 |
| 2 | success | valid / verified | applying | procedural | Easy | 2513 |
| 3 | success | valid / verified | applying | procedural | Easy | 2485 |

Run 1 — solusi: Jumlah anak suka belimbing adalah 7. Jumlah anak suka apel adalah 4. Selisihnya adalah 7 - 4 = 3.
- Domain kognitif `classify/applying`: Siswa perlu membaca data dari diagram (7 dan 4) lalu melakukan operasi pengurangan sederhana untuk menemukan selisih. Ini adalah penerapan prosedur rutin pada data yang diberikan.. Bukti: Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan teknik membaca diagram gambar (pictograph) dan menerapkan algoritma pengurangan dasar untuk menyelesaikan masalah.. Bukti: Diagram berikut menunjukkan jenis buah kesukaan anak-anak.
- Intended difficulty `classify/Easy`: Soal ini sesuai untuk kelas 1 karena melibatkan pembacaan data visual sederhana dan operasi pengurangan dasar (di bawah 10).. Bukti: Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung objek (bintang) dan operasi pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 1 sudah diajarkan membaca diagram gambar sederhana dan melakukan pengurangan bilangan cacah hingga 10. |

Run 2 — solusi: Jumlah anak yang suka belimbing adalah 7, jumlah anak yang suka apel adalah 4. Selisihnya adalah 7 - 4 = 3.
- Domain kognitif `classify/applying`: Siswa perlu menginterpretasikan diagram gambar untuk mendapatkan data, lalu melakukan operasi pengurangan sederhana untuk menemukan selisih. Ini adalah penerapan prosedur rutin pada situasi yang diberikan.. Bukti: Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan pengetahuan prosedural tentang cara membaca diagram gambar (menghitung simbol) dan melakukan operasi pengurangan dasar.. Bukti: Diagram berikut menunjukkan jenis buah kesukaan anak-anak.
- Intended difficulty `classify/Easy`: Soal ini sesuai untuk kelas 1 karena melibatkan pembacaan data sederhana dan operasi pengurangan dasar dalam konteks yang familiar.. Bukti: Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung objek (korespondensi satu-satu) dan operasi pengurangan dasar dalam lingkup 10. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | True |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 1 diharapkan mampu membaca diagram gambar sederhana dan melakukan perbandingan jumlah (selisih) dengan angka di bawah 10. |

Run 3 — solusi: Jumlah anak suka belimbing adalah 7, jumlah anak suka apel adalah 4. Selisihnya adalah 7 - 4 = 3.
- Domain kognitif `classify/applying`: Siswa perlu membaca data dari piktogram (menghitung bintang) dan melakukan operasi pengurangan sederhana untuk menemukan selisih. Ini adalah penerapan prosedur rutin pada situasi yang diberikan.. Bukti: Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.
- Dimensi pengetahuan `classify/procedural`: Siswa menggunakan teknik menghitung dan algoritma pengurangan untuk memproses informasi dalam diagram.. Bukti: Diagram berikut menunjukkan jenis buah kesukaan anak-anak.
- Intended difficulty `classify/Easy`: Soal ini sesuai untuk kelas 1 karena melibatkan pembacaan data visual sederhana dan operasi pengurangan dasar (di bawah 10).. Bukti: Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan menghitung benda konkret (bintang) dan konsep pengurangan dasar. |
| dependentSteps | 2 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 2 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Siswa kelas 1 sudah diajarkan membaca piktogram sederhana dan melakukan pengurangan bilangan cacah di bawah 10. |

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
| Domain kognitif | knowing=0.000007; applying=0.999993; reasoning=0.000000 | applying | 0.999993 | 0.000078 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.085859; conceptual=0.911510; procedural=0.002631; metacognitive=0.000000 | conceptual | 0.911510 | 0.224246 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.795873; Medium=0.197843; Hard=0.006284 | Easy | 0.795873 | 0.486185 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.999993; −Σp ln(p) = 0.000086; H = 0.000086/ln(3) = 0.000078; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.911510; −Σp ln(p) = 0.310871; H = 0.310871/ln(4) = 0.224246; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.795873; −Σp ln(p) = 0.534129; H = 0.534129/ln(3) = 0.486185; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Diagram Gambar
Tipe soal: multiple_choice
Stimulus: -
Soal: Diagram berikut menunjukkan jenis buah kesukaan anak-anak. Lengkapi setiap kalimat berikut.

Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.
Pilihan: A. 2
B. 3
C. 4
D. 1
Transkripsi visual: Diagram batang gambar (pictograph) dengan 4 kolom buah: jeruk (6 bintang), apel (4 bintang), belimbing (7 bintang), jambu air (5 bintang). Keterangan: 1 bintang mewakili 1 anak.
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "procedural", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "procedural", "agreement": false}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.

## 50. Soal `8812007076d1edea9f050f6f`

Ibu membeli buah di pasar. Ibu membeli 6 jeruk, 3 apel, 4 mangga, dan 5 belimbing.<br><br>Buah yang paling sedikit adalah ...

| Opsi | Isi |
|---|---|
| A | Belimbing |
| B | Jeruk |
| C | Apel |
| D | Mangga |

Kunci sumber: `C`; status AI: `verified`; jawaban diverifikasi AI: `C`.
Solusi minimum hasil AI: Membandingkan jumlah buah: 3 (apel) < 4 (mangga) < 5 (belimbing) < 6 (jeruk). Jumlah terkecil adalah 3, yaitu apel.
Gambar sumber: —. Transkripsi visual: —

### 1. Pemeriksaan input dan fitur

Struktur: `pass`; alasan: `[]`. Grade/topik: kelas 1 / Matematika SD Kelas 1. KKO: `[]`; KKO hanya petunjuk bantu.
Isi dan kunci berasal dari sumber yang sama pada ketiga run. Versi konten: 2; hash: `62e5bf71864b713843ee1d0df624c082ad2add7d3816e5d9868a03034580dfb9`. Bukti verifikasi AI tetap tercatat sebagai silver.

### 2. Penilaian Gemini blind — tiga run sebelum melihat IndoBERT

| Run | Status | Konten / kunci | Kognitif | Pengetahuan | Difficulty | Token |
|---:|---|---|---|---|---|---:|
| 1 | success | valid / verified | applying | conceptual | Easy | 1356 |
| 2 | success | valid / verified | applying | conceptual | Easy | 1310 |
| 3 | success | valid / verified | applying | conceptual | Easy | 1308 |

Run 1 — solusi: Membandingkan jumlah buah: 3 (apel) < 4 (mangga) < 5 (belimbing) < 6 (jeruk). Jumlah terkecil adalah 3, yaitu apel.
- Domain kognitif `classify/applying`: Siswa perlu mengidentifikasi nilai dari setiap kategori buah dan membandingkannya untuk menentukan nilai minimum. Ini adalah proses applying karena menerapkan konsep perbandingan bilangan pada data yang diberikan.. Bukti: Ibu membeli 6 jeruk, 3 apel, 4 mangga, dan 5 belimbing.; Buah yang paling sedikit adalah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konsep urutan dan perbandingan bilangan (lebih dari/kurang dari) dalam konteks data sederhana.. Bukti: 6 jeruk, 3 apel, 4 mangga, dan 5 belimbing
- Intended difficulty `classify/Easy`: Soal ini tergolong mudah karena hanya melibatkan perbandingan langsung dari empat bilangan bulat kecil yang sudah eksplisit disebutkan dalam teks.. Bukti: 6 jeruk, 3 apel, 4 mangga, dan 5 belimbing

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan bilangan cacah 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena membandingkan jumlah benda konkret (buah) adalah materi dasar yang familiar. |

Run 2 — solusi: Membandingkan jumlah buah: 3 (apel) < 4 (mangga) < 5 (belimbing) < 6 (jeruk). Jumlah terkecil adalah 3, yaitu apel.
- Domain kognitif `classify/applying`: Siswa perlu membandingkan nilai bilangan untuk menentukan urutan terkecil, yang merupakan proses penerapan konsep dasar perbandingan.. Bukti: Buah yang paling sedikit adalah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang urutan dan perbandingan besaran bilangan dalam konteks data sederhana.. Bukti: 6 jeruk, 3 apel, 4 mangga, dan 5 belimbing
- Intended difficulty `classify/Easy`: Soal ini sangat mendasar untuk kelas 1, hanya memerlukan perbandingan langsung dari empat nilai bilangan yang diberikan tanpa langkah tambahan yang kompleks.. Bukti: 6 jeruk, 3 apel, 4 mangga, dan 5 belimbing; Buah yang paling sedikit adalah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan bilangan cacah 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Sesuai untuk kelas 1 karena hanya melibatkan perbandingan langsung dari sekumpulan data kecil yang sudah terstruktur. |

Run 3 — solusi: Membandingkan jumlah buah: 3 (apel) < 4 (mangga) < 5 (belimbing) < 6 (jeruk). Nilai terkecil adalah 3, yaitu apel.
- Domain kognitif `classify/applying`: Siswa perlu membandingkan nilai numerik dari empat kategori buah untuk menentukan nilai minimum, yang merupakan proses penerapan konsep perbandingan dasar.. Bukti: Buah yang paling sedikit adalah
- Dimensi pengetahuan `classify/conceptual`: Soal ini menguji pemahaman konseptual tentang urutan dan perbandingan besaran bilangan dalam konteks data sederhana.. Bukti: 6 jeruk, 3 apel, 4 mangga, dan 5 belimbing
- Intended difficulty `classify/Easy`: Soal ini sangat sesuai untuk kelas 1 karena hanya melibatkan perbandingan bilangan satu digit yang familiar dan langsung.. Bukti: 6 jeruk, 3 apel, 4 mangga, dan 5 belimbing; Buah yang paling sedikit adalah

Profil difficulty run ini:

| Parameter | Nilai |
|---|---|
| expectedPrerequisite | Kemampuan membandingkan bilangan cacah 1-10. |
| dependentSteps | 1 |
| routineStatus | familiar_routine |
| strategySelection | False |
| representationTransfer | False |
| relevantInformationUnits | 4 |
| interactingConstraints | 0 |
| calculationLoad | low |
| scaffoldLevel | none |
| distractorQuality | plausible |
| gradeRelativeRationale | Tugas membandingkan empat bilangan satu digit adalah standar kompetensi dasar untuk kelas 1 SD. |

### 3. Voting awal dan adjudikasi

| Head | Suara awal | Pola / status akhir | Label akhir advisory |
|---|---|---|---|
| Domain kognitif | {"applying": 3} | unanimous_3_0 / unanimous | applying |
| Dimensi pengetahuan | {"conceptual": 3} | unanimous_3_0 / unanimous | conceptual |
| Intended difficulty | {"Easy": 3} | unanimous_3_0 / unanimous | Easy |

### 4. Diagnostik IndoBERT setelah label blind dikunci

Model membaca representation `metadata`; token input 75/256; truncation: `False`.

| Head | Probabilitas | Label | Confidence | Entropy | Action / alasan |
|---|---|---|---:|---:|---|
| Domain kognitif | knowing=0.001439; applying=0.998561; reasoning=0.000000 | applying | 0.998561 | 0.009882 | review / selective_threshold_gate_not_met |
| Dimensi pengetahuan | factual=0.370495; conceptual=0.614093; procedural=0.015412; metacognitive=0.000000 | conceptual | 0.614093 | 0.527748 | review / selective_threshold_gate_not_met |
| Intended difficulty | Easy=0.894204; Medium=0.101535; Hard=0.004261 | Easy | 0.894204 | 0.323583 | review / selective_threshold_gate_not_met |

Domain kognitif: Σp = 1.00000000; confidence = max(p) = 0.998561; −Σp ln(p) = 0.010857; H = 0.010857/ln(3) = 0.009882; T = 0.050000.


Dimensi pengetahuan: Σp = 1.00000000; confidence = max(p) = 0.614093; −Σp ln(p) = 0.731615; H = 0.731615/ln(4) = 0.527748; T = 0.209800.


Intended difficulty: Σp = 1.00000000; confidence = max(p) = 0.894204; −Σp ln(p) = 0.355493; H = 0.355493/ln(3) = 0.323583; T = 0.953328.


<details><summary>Input sebenarnya yang dibaca model</summary>

```text
Kelas: 1
Topik: Matematika SD Kelas 1
Subtopik: Diagram Gambar
Tipe soal: multiple_choice
Stimulus: -
Soal: Ibu membeli buah di pasar. Ibu membeli 6 jeruk, 3 apel, 4 mangga, dan 5 belimbing.

Buah yang paling sedikit adalah ...
Pilihan: A. Belimbing
B. Jeruk
C. Apel
D. Mangga
Transkripsi visual: -
```

</details>

### 5. Keputusan batch

Label advisory blind: `{"mathCognitiveDomain": "applying", "knowledgeDimension": "conceptual", "intendedDifficulty": "Easy"}`. Routing: `silver_ready`.
Status konten: `valid`. Catatan konten: .
Perbedaan model dan blind: `{"mathCognitiveDomain": {"modelLabel": "applying", "blindLabel": "applying", "agreement": true}, "knowledgeDimension": {"modelLabel": "conceptual", "blindLabel": "conceptual", "agreement": true}, "intendedDifficulty": {"modelLabel": "Easy", "blindLabel": "Easy", "agreement": true}}`.
Label tetap silver AI; revalidation memakai AI. Confidence IndoBERT tidak digunakan untuk mengganti label blind.
